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

"""Generated OPC UA plcopen namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as plcopen_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=plcopen;i=3001", browseName="BYTE", description="It describes that the type is used as bit string of length 8.", parent="i=3")
class BYTE:
    pass


@o6.datatype(nodeId="ns=plcopen;i=3002", browseName="WORD", description="It describes that the type is used as bit string of length 16.", parent="i=5")
class WORD:
    pass


@o6.datatype(nodeId="ns=plcopen;i=3003", browseName="DWORD", description="It describes that the type is used as bit string of length 32.", parent="i=7")
class DWORD:
    pass


@o6.datatype(nodeId="ns=plcopen;i=3004", browseName="LWORD", description="It describes that the type is used as bit string of length 64.", parent="i=9")
class LWORD:
    pass


@o6.datatype(
    nodeId="ns=plcopen;i=3005",
    browseName="TIME",
    description="It describes that the type is used as interval of time in milliseconds. The representation contains information for days (d), hours (h), minutes (m), seconds (s) and milliseconds (ms). The range of valid values is vendor specific. The server has to check if the value has a valid range. Sample: T#+24d20h31m23s647ms.",
    parent="i=8",
)
class TIME:
    pass


@o6.datatype(
    nodeId="ns=plcopen;i=3006",
    browseName="LTIME",
    description="It describes that the type is used as interval of time in nanoseconds. The valid range is LT#-106751d23h47m16s854ms775us808ns to LT#+106751d23h47m16s854ms775us807ns. The representation contains information for days (d), hours (h), minutes (m), seconds (s) milliseconds (ms), microseconds (us) and nanoseconds (ns).",
    parent="i=8",
)
class LTIME:
    pass


@o6.datatype(nodeId="ns=plcopen;i=3007", browseName="DATE", description="It describes that the type is used as a date only.", parent="i=13")
class DATE:
    pass


@o6.datatype(
    nodeId="ns=plcopen;i=3008",
    browseName="TOD",
    description="TIME_OF_DAY stores number of milliseconds since the beginning of the day: TOD#00:00:00.000 to TOD#23:59:59.999.",
    parent="i=7",
)
class TOD:
    pass


@o6.datatype(
    nodeId="ns=plcopen;i=3009",
    browseName="LTOD",
    description="LTIME_OF_DAY stores the number of nanoseconds since the beginning of the day: LTOD#00:00:00.000000000 to LTOD#23:59:59.999999999.",
    parent="i=8",
)
class LTOD:
    pass


@o6.datatype(nodeId="ns=plcopen;i=3010", browseName="DT", description="Vendor specific type.", parent="i=13")
class DT:
    pass


@o6.datatype(nodeId="ns=plcopen;i=3011", browseName="CHAR", description=". It describes that the type is used as single-byte character.", parent="i=3")
class CHAR:
    pass


@o6.datatype(nodeId="ns=plcopen;i=3012", browseName="WCHAR", description="It describes that the type is used as double-byte character.", parent="i=5")
class WCHAR:
    pass


@o6.datatype(nodeId="ns=plcopen;i=3013", browseName="STRING", description="It describes that the type is used as a variable-length single-byte character string.", parent="i=12")
class STRING:
    pass


@o6.datatype(
    nodeId="ns=plcopen;i=3014", browseName="LDATE", description="It describes that the type is used as date only. The interval is nanoseconds since 1970-01-01.", parent="i=8"
)
class LDATE:
    pass


@o6.datatype(nodeId="ns=plcopen;i=3015", browseName="LDT", description="It describes the number of nanoseconds elapsed since 1970-01-01-00:00:00.", parent="i=8")
class LDT:
    pass


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plcopen_reftypes
