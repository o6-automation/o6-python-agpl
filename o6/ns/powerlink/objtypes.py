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

"""Generated OPC UA powerlink namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import datatypes as powerlink_datypes
from . import vartypes as powerlink_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=powerlink;i=2",
    browseName="ns=powerlink;PowerlinkDeviceType",
    displayName="PowerlinkDeviceType",
    description="example for a DeviceType that only implements POWERLINK Managing Node (MN) and/or POWERLINK Controlled Node (CN) interfaces",
)
class PowerlinkDeviceType(di.objtypes.DeviceType):
    langleCNIdentifierRangle: PowerlinkCnConnectionPointType | None
    langleMNIdentifierRangle: PowerlinkMnConnectionPointType | None


@o6.objecttype(nodeId="ns=powerlink;i=6", browseName="ns=powerlink;PowerlinkProtocolType", displayName="PowerlinkProtocolType")
class PowerlinkProtocolType(di.objtypes.ProtocolType):
    pass


di.objtypes.FunctionalGroupType(nodeId="ns=powerlink;i=57", browseName="ns=di;NetworkAddress", description="The address of the device on this network.")
di.objtypes.FunctionalGroupType(nodeId="ns=powerlink;i=58", browseName="ns=di;Identification", description="Used to organize parameters for identification of this TopologyElement")
di.objtypes.FunctionalGroupType(nodeId="ns=powerlink;i=60", browseName="ns=powerlink;Diagnostics")
di.objtypes.FunctionalGroupType(nodeId="ns=powerlink;i=63", browseName="ns=powerlink;Configuration")
di.objtypes.FunctionalGroupType(nodeId="ns=powerlink;i=64", browseName="ns=powerlink;Status")
di.objtypes.FunctionalGroupType(nodeId="ns=powerlink;i=65", browseName="ns=powerlink;Control")
di.objtypes.FunctionalGroupType(nodeId="ns=powerlink;i=66", browseName="ns=powerlink;SdoServices")


@o6.objecttype(
    nodeId="ns=powerlink;i=3",
    browseName="ns=powerlink;PowerlinkConnectionPointType",
    displayName="PowerlinkConnectionPointType",
    description="defines the POWERLINK Objects, which are common for both POWERLINK Managing Node and POWERLINK Controlled Node",
    isAbstract=True,
)
class PowerlinkConnectionPointType(di.objtypes.ConnectionPointType):
    configuration: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=powerlink;i=63"])
    control: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=powerlink;i=65"])
    diagnostics: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=powerlink;i=60"])
    identification: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=powerlink;i=58"])
    langleProfileIdRangle: PowerlinkProtocolType = o6.hasComponent(
        PowerlinkProtocolType(nodeId="ns=powerlink;i=59", browseName="ns=di;<ProfileId>", modellingRule="MandatoryPlaceholder")
    )
    methodSet: ns0.objtypes.BaseObjectType
    networkAddress: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=powerlink;i=57"])
    parameterSet: ns0.objtypes.BaseObjectType
    sdoServices: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=powerlink;i=66"])
    status: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=powerlink;i=64"])


@o6.objecttype(nodeId="ns=powerlink;i=4", browseName="ns=powerlink;PowerlinkCnConnectionPointType", displayName="PowerlinkCnConnectionPointType")
class PowerlinkCnConnectionPointType(PowerlinkConnectionPointType):
    configuration: di.objtypes.FunctionalGroupType
    diagnostics: di.objtypes.FunctionalGroupType
    langleDeviceProfileIdentifierRangle: PowerlinkDeviceProfileType | None
    parameterSet: ns0.objtypes.BaseObjectType


@o6.objecttype(nodeId="ns=powerlink;i=5", browseName="ns=powerlink;PowerlinkMnConnectionPointType", displayName="PowerlinkMnConnectionPointType")
class PowerlinkMnConnectionPointType(PowerlinkConnectionPointType):
    configuration: di.objtypes.FunctionalGroupType
    diagnostics: di.objtypes.FunctionalGroupType
    parameterSet: ns0.objtypes.BaseObjectType


@o6.objecttype(nodeId="ns=powerlink;i=1", browseName="ns=powerlink;PowerlinkDeviceProfileType", displayName="PowerlinkDeviceProfileType")
class PowerlinkDeviceProfileType(di.objtypes.TopologyElementType):
    indexRangeSize: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powerlink;i=444", browseName="ns=powerlink;IndexRangeSize", dataType=o6.UInt16, value=0)
    )
    indexRangeStart: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powerlink;i=443", browseName="ns=powerlink;IndexRangeStart", dataType=o6.UInt16, value=0)
    )


del Any, TYPE_CHECKING, uuid, o6, di, ns0, powerlink_datypes, powerlink_vartypes
