# Copyright (c) 2026 o6 Automation GmbH
#
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
"""
Cryptographic utilities for OPC UA encryption.

Provides certificate generation, loading, and a CLI tool for creating
self-signed certificates suitable for OPC UA client/server communication.

Usage as module:
    from o6.crypto import create_self_signed_certificate, load_certificate

    key, cert = create_self_signed_certificate(
        app_uri="urn:my:app",
        common_name="MyApp@localhost",
    )

Usage as CLI:
    python -m o6.crypto --app-uri urn:my:app --common-name MyApp@localhost
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Optional, Tuple, Union

def encryption_available() -> bool:
    """Return True if the underlying library was compiled with encryption."""
    ...

def create_self_signed_certificate(
    *,
    app_uri: str = "urn:open62541.server.application",
    common_name: str = "Open62541Server@localhost",
    organization: str = "o6",
    country: str = "DE",
    alt_names: Optional[List[str]] = None,
    expires_in_days: int = 365,
    key_size: int = 2048,
    fmt: str = "DER",
) -> Tuple[bytes, bytes]:
    """Create a self-signed certificate and private key.

    Parameters
    ----------
    app_uri : str
        Application URI embedded as SAN (default: urn:open62541.server.application).
    common_name : str
        CN field in the certificate subject.
    organization : str
        O field in the certificate subject.
    country : str
        C field in the certificate subject.
    alt_names : list of str, optional
        Additional Subject Alternative Names (e.g. ``["DNS:myhost"]``).
        ``DNS:localhost`` and ``URI:<app_uri>`` are always included.
    expires_in_days : int
        Certificate validity in days (default: 365).
    key_size : int
        RSA key size in bits (default: 2048).
    fmt : str
        Output format: ``"DER"`` or ``"PEM"`` (default: ``"DER"``).

    Returns
    -------
    tuple of (bytes, bytes)
        ``(private_key, certificate)`` as raw bytes.

    Raises
    ------
    RuntimeError
        If encryption support is not compiled in.
    """
    ...

def load_certificate(path: Union[str, Path]) -> bytes:
    """Load a certificate from a file.

    Parameters
    ----------
    path : str or Path
        Path to a DER or PEM encoded certificate file.

    Returns
    -------
    bytes
        Raw certificate bytes.
    """
    ...

def load_private_key(path: Union[str, Path]) -> bytes:
    """Load a private key from a file.

    Parameters
    ----------
    path : str or Path
        Path to a DER or PEM encoded private key file.

    Returns
    -------
    bytes
        Raw private key bytes.
    """
    ...

def _load_cert_or_bytes(value: Union[str, Path, bytes, None]) -> Optional[bytes]:
    """Accept a file path or raw bytes and return bytes (or None)."""
    ...

def _load_cert_list(values: Optional[List[Union[str, Path, bytes]]]) -> List[bytes]:
    """Load a list of certificates from paths or raw bytes."""
    ...
