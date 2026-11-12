# Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner)
# SPDX-License-Identifier: AGPL-3.0-or-later
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Public utilities and shared helpers for the high-level API.

Includes certificate generation and helpers for loading certificate material.
"""

from __future__ import annotations

import asyncio as _asyncio
from collections.abc import Iterable as _Iterable
import enum as _enum
from pathlib import Path as _Path
import threading as _threading
from typing import Any as _Any

import numpy as _np

import o6 as _o6_api

from . import _o6

_create_certificate = _o6.create_certificate
del _o6


def createSelfSignedCertificate(
    *,
    appUri: str = "urn:o6-Python.unconfigured.application",
    commonName: str = "o6 Python@localhost",
    organization: str = "o6",
    country: str = "DE",
    altNames: list[str] | None = None,
    expiresInDays: int = 365,
    keySize: int = 2048,
    fmt: str = "DER",
) -> tuple[bytes, bytes]:
    """Create a self-signed certificate and private key.

    `DNS:localhost` and `URI:<appUri>` are always included as subject
    alternative names.

    Args:
        appUri: Application URI embedded as a subject alternative name.
            The default is the ApplicationUri of a server or client that sets
            none.
        commonName: Certificate subject common name, 1 to 64 characters.
        organization: Certificate subject organization, 1 to 64 characters.
        country: Two-letter certificate subject country code.
        altNames: Additional subject alternative names, such as
            `["DNS:myhost"]`.
        expiresInDays: Certificate validity in days.
        keySize: RSA key size in bits.
        fmt: Output format, either `"DER"` or `"PEM"`.

    Returns:
        A `(privateKey, certificate)` pair as raw bytes.

    Raises:
        ValueError: `commonName` or `organization` is empty or longer than
            the X.509 limit of 64 characters, or `country` does not have two
            characters.
    """
    # The native call reports a subject it cannot encode only as
    # Bad_InternalError. X.509 upper bounds: RFC 5280, Appendix A.
    for field, value in (("commonName", commonName), ("organization", organization)):
        if not 1 <= len(value) <= 64:
            raise ValueError(f"{field} must have 1 to 64 characters, not {len(value)}: {value!r}")
    if len(country) != 2:
        raise ValueError(f"country must be a two-letter code, not {country!r}")
    subject = [f"C={country}", f"O={organization}", f"CN={commonName}"]

    san: list[str] = [f"DNS:localhost", f"URI:{appUri}"]
    if altNames:
        for entry in altNames:
            if entry not in san:
                san.append(entry)

    return _create_certificate(
        subject,
        san,
        expires_in_days=expiresInDays,
        key_size=keySize,
        fmt=fmt,
    )


def loadCertificate(path: str | _Path) -> bytes:
    """Load a DER- or PEM-encoded certificate from `path`.

    Returns the file's bytes unchanged. `Client.config` and the `Server`
    constructor also accept a path directly.

    Args:
        path: File to read.

    Returns:
        The raw certificate bytes.

    Raises:
        OSError: The file cannot be read.
    """
    return _Path(path).read_bytes()


def loadPrivateKey(path: str | _Path) -> bytes:
    """Load a DER- or PEM-encoded private key from `path`.

    Returns the file's bytes unchanged.

    Args:
        path: File to read.

    Returns:
        The raw private-key bytes.

    Raises:
        OSError: The file cannot be read.
    """
    return _Path(path).read_bytes()


def _load_cert_or_bytes(value: str | _Path | bytes | None) -> bytes | None:
    """Return certificate bytes from a path or an existing byte string."""
    if value is None:
        return None
    if isinstance(value, bytes):
        return value
    return _Path(value).read_bytes()


def _load_cert_list(values: list[str | _Path | bytes] | None) -> list[bytes]:
    """Load certificate bytes from a list of paths and byte strings."""
    if not values:
        return []
    return [b for v in values if (b := _load_cert_or_bytes(v)) is not None]


def _index_range_to_string(value: _o6_api.IndexRange) -> str | None:
    """Convert a public index range to OPC UA's inclusive string syntax."""
    if value is None:
        return None
    if isinstance(value, str):
        return value
    if isinstance(value, slice):
        value = (value,)
    if not isinstance(value, tuple) or not value:
        raise TypeError("index range must be a string or a non-empty tuple of slices")
    dimensions: list[str] = []
    for dimension in value:
        if not isinstance(dimension, slice):
            raise TypeError("index range tuple entries must be slices")
        if dimension.start is None or dimension.stop is None:
            raise ValueError("index range slices must have explicit start and stop values")
        if dimension.step is not None:
            raise ValueError("index range slices do not support a step")
        if dimension.start < 0 or dimension.stop <= dimension.start:
            raise ValueError("index range slices must describe a non-empty, non-negative range")
        inclusive_stop = dimension.stop - 1
        if inclusive_stop == dimension.start:
            dimensions.append(str(dimension.start))
        else:
            dimensions.append(f"{dimension.start}:{inclusive_stop}")
    return ",".join(dimensions)


class _WorkerLoop:
    """Background thread driving an asyncio event loop."""

    def __init__(self, loop: _asyncio.AbstractEventLoop) -> None:
        """Wrap an existing event loop with a worker-thread driver."""
        self._loop = loop
        self._thread: _threading.Thread | None = None

    @property
    def loop(self) -> _asyncio.AbstractEventLoop:
        """Return the asyncio event loop driven by this worker."""
        return self._loop

    @property
    def running(self) -> bool:
        """Return whether the worker thread is currently alive."""
        return self._thread is not None and self._thread.is_alive()

    @property
    def on_loop_thread(self) -> bool:
        """Return whether this code is running on the worker thread."""
        return self._thread is not None and _threading.current_thread() is self._thread

    def start(self) -> None:
        """Start the worker thread unless it is already running."""
        if self.running:
            return
        loop = self._loop

        def worker() -> None:
            _asyncio.set_event_loop(loop)
            loop.run_forever()

        self._thread = _threading.Thread(target=worker, daemon=True)
        self._thread.start()

    def stop(self, close: bool = False, timeout: float = 2.0) -> None:
        """Stop the loop, join its thread, and optionally close the loop."""
        thread = self._thread
        self._thread = None
        if thread is not None and thread.is_alive():
            try:
                self._loop.call_soon_threadsafe(self._loop.stop)
            except RuntimeError:
                pass
            if _threading.current_thread() is not thread:
                thread.join(timeout=timeout)
        if close and not self._loop.is_closed():
            try:
                self._loop.close()
            except Exception:
                pass


def _value_rank(value: _Any) -> int:
    """Infer the ValueRank for Variable creation.

    NumPy arrays keep their dimensions; other iterable values except text,
    bytes and enum members are one-dimensional. Native conversion validates
    the value. Enum members are scalars, although `enum.Flag` members such as
    StatusCodes and OptionSets are iterable.
    """
    if isinstance(value, _np.ndarray):
        return value.ndim
    if isinstance(value, (str, bytes, _enum.Enum)):
        return -1
    if isinstance(value, _Iterable):
        return 1
    return -1


def _empty_sequence_shape(value: _Any) -> tuple[int, ...] | None:
    """Return the shape of a rectangular nested sequence with no elements."""
    if not isinstance(value, (list, tuple)):
        return None
    if not value:
        return (0,)
    shape = _empty_sequence_shape(value[0])
    if shape is not None and all(_empty_sequence_shape(item) == shape for item in value[1:]):
        return (len(value), *shape)
    return None


def _infer_data_type(value: _Any) -> tuple[_o6_api.NodeId, int]:
    """Infer the OPC UA data-type NodeId and value rank for `value`."""
    value_rank = _value_rank(value)

    normalized = _o6_api.DataValue()
    normalized.value = value
    normalized_value = normalized.value
    if isinstance(normalized_value, _np.ndarray) and normalized_value.size == 0:
        element_type = normalized_value.dtype.type
        if normalized_value.dtype.kind == "T":
            element_type = str
        return _o6_api.NodeId(element_type), value_rank
    if value_rank >= 1:
        if isinstance(normalized_value, _np.ndarray):
            normalized_value = normalized_value.flat[0]
        else:
            normalized_value = next(iter(normalized_value))
    return _o6_api.NodeId(type(normalized_value)), value_rank


def _coerce_builtin_value(data_type: _Any, value: _Any) -> _Any:
    """Wrap values in the native scalar type selected by an ns0 DataType."""
    if value is None:
        return None
    nodeid = _o6_api.NodeId(data_type)
    namespace = nodeid.ns if isinstance(nodeid.ns, int) else nodeid.ns.index
    if namespace != 0 or not isinstance(nodeid.id, int) or not 1 <= nodeid.id <= 11:
        return value
    wrapper = (
        _o6_api.Boolean,
        _o6_api.SByte,
        _o6_api.Byte,
        _o6_api.Int16,
        _o6_api.UInt16,
        _o6_api.Int32,
        _o6_api.UInt32,
        _o6_api.Int64,
        _o6_api.UInt64,
        _o6_api.Float,
        _o6_api.Double,
    )[nodeid.id - 1]
    try:
        if isinstance(value, list):
            return [wrapper(item) for item in value]
        if isinstance(value, tuple):
            return tuple(wrapper(item) for item in value)
        return wrapper(value)
    except (TypeError, ValueError) as exc:
        exc.add_note(f"while coercing a value declared with DataType {nodeid}")
        raise


__all__ = ["createSelfSignedCertificate", "loadCertificate", "loadPrivateKey"]


def __dir__() -> list[str]:
    return sorted(__all__)


# ---------------------------------------------------------------------------
