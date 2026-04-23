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

from __future__ import annotations

from pathlib import Path
from typing import List, Optional, Tuple, Union

from . import _o6


def encryption_available() -> bool:
    return _o6.encryption_available()


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
    if not encryption_available():
        raise RuntimeError(
            "Encryption not available. Rebuild open62541 with "
            "-DUA_ENABLE_ENCRYPTION=MBEDTLS or OPENSSL."
        )

    subject = [f"C={country}", f"O={organization}", f"CN={common_name}"]

    san: list[str] = [f"DNS:localhost", f"URI:{app_uri}"]
    if alt_names:
        for entry in alt_names:
            if entry not in san:
                san.append(entry)

    return _o6.create_certificate(
        subject,
        san,
        expires_in_days=expires_in_days,
        key_size=key_size,
        fmt=fmt,
    )


def load_certificate(path: Union[str, Path]) -> bytes:
    return Path(path).read_bytes()


def load_private_key(path: Union[str, Path]) -> bytes:
    return Path(path).read_bytes()


def _load_cert_or_bytes(value: Union[str, Path, bytes, None]) -> Optional[bytes]:
    if value is None:
        return None
    if isinstance(value, bytes):
        return value
    return Path(value).read_bytes()


def _load_cert_list(values: Optional[List[Union[str, Path, bytes]]]) -> List[bytes]:
    if not values:
        return []
    return [b for v in values if (b := _load_cert_or_bytes(v)) is not None]


# ---------------------------------------------------------------------------
