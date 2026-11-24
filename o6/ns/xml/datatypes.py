# Copyright (c) 2026 o6 Automation GmbH
#
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

"""Generated OPC UA xml namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=xml;i=3003", browseName="ns=xml;XmlQName", parent="i=12")
class XmlQName:
    pass


@o6.datatype(nodeId="ns=xml;i=3006", browseName="ns=xml;XmlToken", parent="i=12877")
class XmlToken:
    pass


@o6.datatype(nodeId="ns=xml;i=3009", browseName="ns=xml;XmlNmToken", parent="ns=xml;i=3006")
class XmlNmToken:
    pass


@o6.datatype(nodeId="ns=xml;i=3012", browseName="ns=xml;XmlName", parent="ns=xml;i=3006")
class XmlName:
    pass


@o6.datatype(nodeId="ns=xml;i=3015", browseName="ns=xml;XmlNcName", parent="ns=xml;i=3012")
class XmlNcName:
    pass


@o6.datatype(nodeId="ns=xml;i=3018", browseName="ns=xml;XmlId", parent="ns=xml;i=3015")
class XmlId:
    pass


@o6.datatype(nodeId="ns=xml;i=3021", browseName="ns=xml;XmlIdRef", parent="ns=xml;i=3015")
class XmlIdRef:
    pass


@o6.datatype(nodeId="ns=xml;i=3024", browseName="ns=xml;XmlEntity", parent="ns=xml;i=3015")
class XmlEntity:
    pass


@o6.datatype(nodeId="ns=xml;i=3027", browseName="ns=xml;XmlInteger", parent="i=8")
class XmlInteger:
    pass


@o6.datatype(nodeId="ns=xml;i=3030", browseName="ns=xml;XmlNonPositiveInteger", parent="ns=xml;i=3027")
class XmlNonPositiveInteger:
    pass


@o6.datatype(nodeId="ns=xml;i=3033", browseName="ns=xml;XmlNegativeInteger", parent="ns=xml;i=3027")
class XmlNegativeInteger:
    pass


@o6.datatype(nodeId="ns=xml;i=3036", browseName="ns=xml;XmlNonNegativeInteger", parent="i=9")
class XmlNonNegativeInteger:
    pass


@o6.datatype(nodeId="ns=xml;i=3039", browseName="ns=xml;XmlPositiveInteger", parent="ns=xml;i=3036")
class XmlPositiveInteger:
    pass


@o6.datatype(nodeId="ns=xml;i=3042", browseName="ns=xml;XmlHexBinary", parent="i=15")
class XmlHexBinary:
    pass


@o6.datatype(nodeId="ns=xml;i=3045", browseName="ns=xml;XmlYearMonthDuration", parent="i=12")
class XmlYearMonthDuration:
    pass


@o6.datatype(nodeId="ns=xml;i=3048", browseName="ns=xml;XmlGYearMonth", parent="i=12")
class XmlGYearMonth:
    pass


@o6.datatype(nodeId="ns=xml;i=3051", browseName="ns=xml;XmlDayTimeDuration", parent="i=12")
class XmlDayTimeDuration:
    pass


@o6.datatype(nodeId="ns=xml;i=3054", browseName="ns=xml;XmlGYear", parent="i=12")
class XmlGYear:
    pass


@o6.datatype(nodeId="ns=xml;i=3057", browseName="ns=xml;XmlGMonth", parent="i=12")
class XmlGMonth:
    pass


@o6.datatype(nodeId="ns=xml;i=3060", browseName="ns=xml;XmlGDay", parent="i=12")
class XmlGDay:
    pass


@o6.datatype(nodeId="ns=xml;i=3063", browseName="ns=xml;XmlGMonthDay", parent="i=12")
class XmlGMonthDay:
    pass


@o6.datatype(nodeId="ns=xml;i=3066", browseName="ns=xml;XmlTime", parent="i=12")
class XmlTime:
    pass


@o6.datatype(nodeId="ns=xml;i=3069", browseName="ns=xml;XmlDate", parent="i=12")
class XmlDate:
    pass


del Any, TYPE_CHECKING, uuid, o6, ns0
