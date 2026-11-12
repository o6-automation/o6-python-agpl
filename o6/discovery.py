# Copyright 2026 (c) o6 Automation GmbH
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

"""Server-owned multicast discovery configuration."""

from collections.abc import Mapping as _Mapping, Sequence as _Sequence
from dataclasses import dataclass as _dataclass, field as _field
import ipaddress as _ipaddress
import re as _re
from types import MappingProxyType as _MappingProxyType

from o6 import _o6

__all__ = ["MdnsConfig", "mdnsAvailable"]

mdnsAvailable: bool = bool(_o6.MDNS_AVAILABLE)
"""Whether this build includes the bundled mDNSd driver; not network readiness."""


def _hostname(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("hostname must be a string")
    name = value[:-1] if value.endswith(".") else value
    if (
        not name
        or len(name) > 253
        or any(
            not _re.fullmatch(r"[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?", label)
            for label in name.split(".")
        )
    ):
        raise ValueError(f"Invalid hostname: {value!r}")
    try:
        _ipaddress.ip_address(name)
    except ValueError:
        pass
    else:
        raise ValueError("hostname must be a DNS name, not an IP address")
    if "." not in name:
        name += ".local"
    return name.lower() + "."


# Schemes whose host the bundled driver extracts with UA_parseEndpointUrl.
_URL_SCHEMES = (
    "opc.tcp://",
    "opc.udp://",
    "opc.eth://",
    "opc.mqtt://",
    "opc.wss://",
    "opc.ws://",
    "opc.https://",
    "opc.http://",
)


def _announced_url(url: str) -> str:
    """Return `url` with the host the bundled driver can announce.

    The driver announces the URL host as the SRV target `<host>.local.`, so the
    host must be one DNS label. A `.local`-qualified host is reduced to its
    label, keeping its case. URLs with other schemes are returned unchanged; the
    driver does not announce them.
    """
    scheme = next((prefix for prefix in _URL_SCHEMES if url.startswith(prefix)), None)
    if scheme is None:
        return url
    rest = url[len(scheme) :]
    end = next((i for i, char in enumerate(rest) if char in ":/"), len(rest))
    host, tail = rest[:end], rest[end:]
    label = host[:-1] if host.endswith(".") else host
    if label.lower().endswith(".local"):
        label = label[: -len(".local")]
    try:
        # An IPv6 host ends at its first colon, leaving "[...", which is invalid.
        valid = _hostname(label) == label.lower() + ".local."
    except ValueError:
        valid = False
    if not valid:
        raise ValueError(
            f"mDNS cannot announce the host of {url!r}; use a bare hostname such as "
            "'opc.tcp://myhost:4840', which is discovered as 'opc.tcp://myhost.local:4840'"
        )
    return scheme + label + tail


@_dataclass(frozen=True, slots=True)
class MdnsConfig:
    """Immutable options for one server's bundled mDNSd driver.

    The transport is IPv4 multicast. AAAA records can describe IPv6 endpoints
    over it. A listener with `announce`, `queryPresence`, and `queryDetails`
    all false fails at server startup.

    Attributes:
        interface: Network interface name (for example `"eth0"`) or IP address.
            `None` leaves it unset.
        listen: Receive announcements of other applications. The query options
            apply only when this is true.
        announce: Announce this server's records.
        announceRegisteredServers: Announce servers that register with this
            LDS. Requires `announce=True` and a discovery server. A successful
            registration does not guarantee that the announcement is published
            or received; invalid names or URLs can be accepted without being
            announced.
        announceTtl: TTL of announced records in seconds. Must be nonzero.
        queryPresence: Send a presence query on startup.
        queryDetails: Send follow-up queries for partially received services.
        queryInterval: Interval of repeated presence queries in seconds. `0`
            disables repetition.
        hostAddresses: Address records to publish, as hostname to numeric
            addresses. Copied into an immutable mapping. Bare hostnames gain
            `.local.` and addresses are normalized. Requires `announce=True`.

    Raises:
        TypeError: A field has the wrong type.
        ValueError: A value is out of range, a hostname or address is invalid,
            or a dependency on `announce=True` is not met.
    """

    interface: str | None = None
    listen: bool = True
    announce: bool = True
    announceRegisteredServers: bool = False
    announceTtl: int = 600
    queryPresence: bool = False
    queryDetails: bool = False
    queryInterval: int = 0
    hostAddresses: _Mapping[str, _Sequence[str]] = _field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.interface is not None:
            if not isinstance(self.interface, str):
                raise TypeError("interface must be a string or None")
            if not self.interface or "\0" in self.interface:
                raise ValueError("interface must be nonempty and contain no NUL")
        for name in (
            "listen",
            "announce",
            "announceRegisteredServers",
            "queryPresence",
            "queryDetails",
        ):
            if type(getattr(self, name)) is not bool:
                raise TypeError(f"{name} must be bool")
        for name in ("announceTtl", "queryInterval"):
            value = getattr(self, name)
            if type(value) is not int:
                raise TypeError(f"{name} must be int")
            if not (0 <= value <= 0xFFFFFFFF) or (name == "announceTtl" and value == 0):
                raise ValueError(f"{name} is outside its unsigned 32-bit range")
        if self.announceRegisteredServers and not self.announce:
            raise ValueError("announceRegisteredServers requires announce=True")
        if not isinstance(self.hostAddresses, _Mapping):
            raise TypeError("hostAddresses must be a mapping")
        copied: dict[str, tuple[str, ...]] = {}
        for hostname, addresses in self.hostAddresses.items():
            hostname = _hostname(hostname)
            if isinstance(addresses, (str, bytes)) or not isinstance(addresses, _Sequence):
                raise TypeError("hostAddresses values must be sequences of address strings")
            normalized = []
            for address in addresses:
                if not isinstance(address, str):
                    raise TypeError("host addresses must be strings")
                if "%" in address:
                    raise ValueError("host addresses cannot contain IPv6 scope identifiers")
                normalized.append(str(_ipaddress.ip_address(address)))
            if hostname in copied:
                raise ValueError(f"Duplicate normalized hostname: {hostname}")
            copied[hostname] = tuple(dict.fromkeys(normalized))
        if copied and not self.announce:
            raise ValueError("hostAddresses requires announce=True")
        object.__setattr__(self, "hostAddresses", _MappingProxyType(copied))


def __dir__() -> list[str]:
    return sorted(__all__)
