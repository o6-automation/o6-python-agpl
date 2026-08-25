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

"""Generated OPC UA cranes_hoists namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
import o6.ns.robotics as robotics
from . import reftypes as cranes_hoists_reftypes
from . import datatypes as cranes_hoists_datypes
from . import objtypes as cranes_hoists_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

httpColonSlashSlashOpcfoundationDotOrgSlashUASlashCranesHoistsSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=cranes_hoists;i=1000",
    browseName="ns=cranes_hoists;http://opcfoundation.org/UA/CranesHoists/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cranes_hoists;i=1001", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cranes_hoists;i=1002", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2023-05-01T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=cranes_hoists;i=1003", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/CranesHoists/")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cranes_hoists;i=1004", browseName="NamespaceVersion", dataType=o6.String, value="1.00")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cranes_hoists;i=1005",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cranes_hoists;i=1006", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["1:65535"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cranes_hoists;i=1007", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cranes_hoists;i=1008", browseName="DefaultRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
cranes_hoists_objtypes.CraneMotionDeviceType(nodeId="ns=cranes_hoists;i=1263", browseName="ns=cranes_hoists;<CraneMotionDeviceIdentifier>", modellingRule="OptionalPlaceholder")
o6.reference(cranes_hoists_objtypes.CraneMotionDeviceType, ns0.reftypes.HasPhysicalComponent, o6.ns["ns=cranes_hoists;i=1263"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=cranes_hoists;i=1463",
    browseName="ns=cranes_hoists;Active",
    description="The Active variable is TRUE if this particular protective function is active, i.e. that a stop or slowdown is initiated, FALSE otherwise. If Enabled is FALSE then Active shall be FALSE.",
    dataType=o6.Boolean,
)
o6.reference(o6.ns["ns=cranes_hoists;i=5013"], "i=35", o6.ns["ns=cranes_hoists;i=1463"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=cranes_hoists;i=1478",
    browseName="ns=cranes_hoists;Enabled",
    description="The Enabled variable is TRUE if this protective function is currently supervising the system, FALSE otherwise. A protective function may or may not be enabled at all times, e.g. the protective stop function of the safety doors are typically enabled in automatic operational mode and disabled in manual mode.",
    dataType=o6.Boolean,
)
o6.reference(o6.ns["ns=cranes_hoists;i=5013"], "i=35", o6.ns["ns=cranes_hoists;i=1478"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=cranes_hoists;i=1485",
    browseName="ns=cranes_hoists;SpeedLimitDirPlusSetpoint",
    description="Speed limitation request written from client, in direction where position value increases, in percentage of rated speed, range [0%..100%]",
    dataType=o6.Double,
    accessLevel=3,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=cranes_hoists;i=1486",
    browseName="ns=cranes_hoists;SpeedLimitDirMinusSetpoint",
    description="Speed limitation request written from client, in direction where position value decreases, in percentage of rated speed, range [0%..100%]",
    dataType=o6.Double,
    accessLevel=3,
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=cranes_hoists;i=1511",
    browseName="ns=cranes_hoists;SpeedLimitEnabledDirPlus",
    description="Speed limitation request active, written from client, in direction where position value increases. True if a client requests the speed to be limited in this direction, false if speed doesn't need to be limited.",
    dataType=o6.Boolean,
    accessLevel=3,
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=cranes_hoists;i=1845",
    browseName="ns=cranes_hoists;SpeedLimitEnabledDirMinus",
    description="Speed limitation request active, written from client, in direction where position value decreases. True if a client requests the speed to be limited in this direction, false if speed doesn't need to be limited.",
    dataType=o6.Boolean,
    accessLevel=3,
)
ns0.vartypes.AnalogUnitType(nodeId="ns=cranes_hoists;i=1852", browseName="ns=cranes_hoists;RatedSpeed", description="Rated speed of this Axis.", dataType=o6.Double)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=cranes_hoists;i=1860",
    browseName="ns=cranes_hoists;DirPlusStop",
    description="Stop enabled for direction where position value increases (plus).",
    dataType=o6.Boolean,
)
o6.reference(o6.ns["ns=cranes_hoists;i=5013"], "i=35", o6.ns["ns=cranes_hoists;i=1860"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=cranes_hoists;i=1861",
    browseName="ns=cranes_hoists;DirMinusStop",
    description="Stop enabled for direction where position value decreases (minus).",
    dataType=o6.Boolean,
)
o6.reference(o6.ns["ns=cranes_hoists;i=5013"], "i=35", o6.ns["ns=cranes_hoists;i=1861"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=cranes_hoists;i=1950",
    browseName="ns=cranes_hoists;SpeedLimitDirPlus",
    description="Speed limitation value active on the control system, in direction where position value increases, in percentage of rated speed, range [0%..100%]",
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=cranes_hoists;i=2031",
    browseName="ns=cranes_hoists;SpeedLimitDirMinus",
    description="Speed limitation value active on the control system, in direction where position value decreases, in percentage of rated speed, range [0%..100%]",
    dataType=o6.Double,
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=cranes_hoists;i=2037", browseName="ns=cranes_hoists;IsMoving", description="True when the Axis is moving, false if not.", dataType=o6.Boolean
)
ns0.vartypes.BaseDataVariableType(nodeId="ns=cranes_hoists;i=2096", browseName="ns=cranes_hoists;ActualPositionCapability", dataType=o6.Boolean)
ns0.objtypes.BaseObjectType(
    nodeId="ns=cranes_hoists;i=2093", browseName="ns=di;ParameterSet", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=cranes_hoists;i=2096"])]
)
o6.reference(cranes_hoists_objtypes.CraneAxisType, ns0.reftypes.HasComponent, o6.ns["ns=cranes_hoists;i=2093"])
o6.reference(o6.ns["ns=cranes_hoists;i=2093"], "i=47", o6.ns["ns=cranes_hoists;i=1485"])
o6.reference(o6.ns["ns=cranes_hoists;i=2093"], "i=47", o6.ns["ns=cranes_hoists;i=1486"])
o6.reference(o6.ns["ns=cranes_hoists;i=2093"], "i=47", o6.ns["ns=cranes_hoists;i=1511"])
o6.reference(o6.ns["ns=cranes_hoists;i=2093"], "i=47", o6.ns["ns=cranes_hoists;i=1845"])
o6.reference(o6.ns["ns=cranes_hoists;i=2093"], "i=47", o6.ns["ns=cranes_hoists;i=1852"])
o6.reference(o6.ns["ns=cranes_hoists;i=2093"], "i=47", o6.ns["ns=cranes_hoists;i=1950"])
o6.reference(o6.ns["ns=cranes_hoists;i=2093"], "i=47", o6.ns["ns=cranes_hoists;i=2031"])
o6.reference(o6.ns["ns=cranes_hoists;i=2093"], "i=47", o6.ns["ns=cranes_hoists;i=2037"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=cranes_hoists;i=2347", browseName="ns=cranes_hoists;SystemOn", dataType=o6.Boolean)
o6.reference(o6.ns["ns=cranes_hoists;i=2114"], "i=47", o6.ns["ns=cranes_hoists;i=2347"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=cranes_hoists;i=2348", browseName="ns=cranes_hoists;CraneOperationalMode", dataType=cranes_hoists_datypes.CraneOperationalModeEnum)
o6.reference(o6.ns["ns=cranes_hoists;i=2114"], "i=47", o6.ns["ns=cranes_hoists;i=2348"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=cranes_hoists;i=2369", browseName="ns=cranes_hoists;ExternalControlRequest", dataType=cranes_hoists_datypes.ExternalControlRequestEnum)
o6.reference(o6.ns["ns=cranes_hoists;i=2114"], "i=47", o6.ns["ns=cranes_hoists;i=2369"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=cranes_hoists;i=2375",
    browseName="ns=cranes_hoists;DirMinusSlowdown",
    description="Stop enabled for direction where position value decreases (minus).",
    dataType=o6.Boolean,
)
o6.reference(o6.ns["ns=cranes_hoists;i=5013"], "i=35", o6.ns["ns=cranes_hoists;i=2375"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=cranes_hoists;i=2379",
    browseName="ns=cranes_hoists;DirPlusSlowdown",
    description="Stop enabled for direction where position value increases (plus).",
    dataType=o6.Boolean,
)
o6.reference(o6.ns["ns=cranes_hoists;i=5013"], "i=35", o6.ns["ns=cranes_hoists;i=2379"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=cranes_hoists;i=2381", browseName="ns=cranes_hoists;SpeedLimitGlobalEnabled", dataType=o6.Boolean, accessLevel=3)
o6.reference(o6.ns["ns=cranes_hoists;i=2114"], "i=47", o6.ns["ns=cranes_hoists;i=2381"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=cranes_hoists;i=5004",
    browseName="ns=di;ParameterSet",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=cranes_hoists;i=1463"]),
        o6.hasComponent(o6.ns["ns=cranes_hoists;i=1478"]),
        o6.hasComponent(o6.ns["ns=cranes_hoists;i=1860"]),
        o6.hasComponent(o6.ns["ns=cranes_hoists;i=1861"]),
        o6.hasComponent(o6.ns["ns=cranes_hoists;i=2375"]),
        o6.hasComponent(o6.ns["ns=cranes_hoists;i=2379"]),
    ],
)
o6.reference(cranes_hoists_objtypes.ProtectiveFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=cranes_hoists;i=5004"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=cranes_hoists;i=5007",
    browseName="ns=di;Configuration",
    modellingRule="Optional",
    references=[
        o6.organizes(o6.ns["ns=cranes_hoists;i=1485"]),
        o6.organizes(o6.ns["ns=cranes_hoists;i=1486"]),
        o6.organizes(o6.ns["ns=cranes_hoists;i=1511"]),
        o6.organizes(o6.ns["ns=cranes_hoists;i=1845"]),
    ],
)
o6.reference(cranes_hoists_objtypes.CraneAxisType, ns0.reftypes.HasComponent, o6.ns["ns=cranes_hoists;i=5007"])
machinery.objtypes.MachineComponentsType(
    nodeId="ns=cranes_hoists;i=5006",
    browseName="ns=machinery;Components",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            cranes_hoists_objtypes.CraneMotionDeviceType(
                nodeId="ns=cranes_hoists;i=5008", browseName="ns=cranes_hoists;<CraneMotionDeviceIdentifier>", modellingRule="MandatoryPlaceholder"
            )
        )
    ],
)
o6.reference(cranes_hoists_objtypes.CraneMotionDeviceSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=cranes_hoists;i=5006"])
ns0.objtypes.FolderType(
    nodeId="ns=cranes_hoists;i=5010",
    browseName="ns=robotics;Axes",
    description="Axes is a container for one or more instances of the AxisType.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(robotics.objtypes.AxisType(nodeId="ns=cranes_hoists;i=5001", browseName="ns=robotics;<AxisIdentifier>", modellingRule="MandatoryPlaceholder"))],
)
o6.reference(cranes_hoists_objtypes.CraneMotionDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=cranes_hoists;i=5010"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=cranes_hoists;i=5011", browseName="ns=di;Configuration", modellingRule="Optional", references=[o6.organizes(o6.ns["ns=cranes_hoists;i=2381"])]
)
o6.reference(cranes_hoists_objtypes.CraneMotionDeviceSystemType, ns0.reftypes.HasComponent, o6.ns["ns=cranes_hoists;i=5011"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=cranes_hoists;i=5012",
    browseName="ns=di;Operational",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=cranes_hoists;i=2347"]), o6.organizes(o6.ns["ns=cranes_hoists;i=2348"]), o6.organizes(o6.ns["ns=cranes_hoists;i=2369"])],
)
o6.reference(cranes_hoists_objtypes.CraneMotionDeviceSystemType, ns0.reftypes.HasComponent, o6.ns["ns=cranes_hoists;i=5012"])
cranes_hoists_objtypes.CraneMotorType(nodeId="ns=cranes_hoists;i=5022", browseName="ns=cranes_hoists;<CraneMotorIdentifier>")
o6.reference(o6.ns["ns=cranes_hoists;i=5022"], "ns=robotics;i=18181", "ns=robotics;i=16041")
machinery.objtypes.MachineComponentsType(
    nodeId="ns=cranes_hoists;i=5016", browseName="ns=machinery;Components", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=cranes_hoists;i=5022"])]
)
o6.reference(cranes_hoists_objtypes.CraneMotionDeviceType, ns0.reftypes.HasAddIn, o6.ns["ns=cranes_hoists;i=5016"])
cranes_hoists_objtypes.ProtectiveFunctionType(nodeId="ns=cranes_hoists;i=5025", browseName="ns=cranes_hoists;<ProtectiveFunctionIdentifier>", modellingRule="MandatoryPlaceholder")
o6.reference(o6.ns["ns=cranes_hoists;i=5025"], "ns=cranes_hoists;i=4001", "ns=robotics;i=15743")
ns0.objtypes.FolderType(
    nodeId="ns=cranes_hoists;i=2113", browseName="ns=cranes_hoists;ProtectiveFunctions", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=cranes_hoists;i=5025"])]
)
o6.reference(cranes_hoists_objtypes.CraneMotionDeviceSystemType, ns0.reftypes.HasComponent, o6.ns["ns=cranes_hoists;i=2113"])
ns0.vartypes.BaseDataVariableType(nodeId="ns=cranes_hoists;i=6000", browseName="ns=cranes_hoists;Overheated", dataType=o6.Boolean)
o6.reference(o6.ns["ns=cranes_hoists;i=5019"], "i=35", o6.ns["ns=cranes_hoists;i=6000"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=cranes_hoists;i=5018", browseName="ns=di;ParameterSet", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=cranes_hoists;i=6000"])]
)
o6.reference(cranes_hoists_objtypes.CraneMotorType, ns0.reftypes.HasComponent, o6.ns["ns=cranes_hoists;i=5018"])
ns0.vartypes.PropertyType(
    nodeId="ns=cranes_hoists;i=6001",
    browseName="EnumValues",
    parent="ns=cranes_hoists;i=3000",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OTHER", "en"), description=o6.LocalizedText("Use if vendor specific", "en")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("MANUAL", "en"), description=o6.LocalizedText("Crane is operated manually by a human operator", "en")),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("SEMIAUTOMATIC", "en"),
            description=o6.LocalizedText("Some or all of crane motions are automated, but a human operator is required in the loop.", "en"),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("FULLAUTOMATIC", "en"),
            description=o6.LocalizedText("All of the crane motions are automated. No human intervention is required.", "en"),
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("BYPASS_ON", "en"),
            description=o6.LocalizedText(
                "A function, such as an assistive feature, is bypassed on the crane, e. g. to continue productive work in case a non-critical function suffers a fault.", "en"
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=5,
            displayName=o6.LocalizedText("MAINTENANCE", "en"),
            description=o6.LocalizedText(
                "Crane is in maintenance mode, typically operating at reduced speed and possibly with some protective functions disabled so they will not hinder or prohibit service activities.",
                "en",
            ),
        ),
    ],
    accessLevel=3,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=cranes_hoists;i=6002",
    browseName="ns=cranes_hoists;DesignedWorkingPeriod",
    description="The lowest ISO 12482 designed working period (DWP) of this component. Percentage, initial value: 100.0%",
    dataType=o6.Double,
)
o6.reference(o6.ns["ns=cranes_hoists;i=5014"], "i=35", o6.ns["ns=cranes_hoists;i=6002"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=cranes_hoists;i=5017",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=cranes_hoists;i=6002"])],
)
o6.reference(cranes_hoists_objtypes.CraneMotionDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=cranes_hoists;i=5017"])
ns0.vartypes.PropertyType(
    nodeId="ns=cranes_hoists;i=6003",
    browseName="EnumValues",
    parent="ns=cranes_hoists;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("HOIST"), description=o6.LocalizedText("Hoisting machinery")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("TROLLEY_TRAVERSE"), description=o6.LocalizedText("Trolley traverse or cross travel machinery")),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("BRIDGE_OR_GANTRY_TRAVEL"), description=o6.LocalizedText("Bridge or gantry travel, long travel machinery")
        ),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("LOAD_LIFTING_ATTACHMENT"), description=o6.LocalizedText("Load lifting attachment")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("ROTATING_OR_SLEWING"), description=o6.LocalizedText("Rotating or slewing machinery")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("LUFFING"), description=o6.LocalizedText("Luffing machinery")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("POWER_SUPPLY_MACHINERY"), description=o6.LocalizedText("Power supply or power delivery")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("OTHER"), description=o6.LocalizedText("Other")),
    ],
    accessLevel=3,
)
ns0.vartypes.BaseDataVariableType(nodeId="ns=cranes_hoists;i=6005", browseName="ns=cranes_hoists;BrakeReleased", dataType=o6.Boolean)
o6.reference(o6.ns["ns=cranes_hoists;i=5009"], "i=35", o6.ns["ns=cranes_hoists;i=6005"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=cranes_hoists;i=5020", browseName="ns=di;ParameterSet", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=cranes_hoists;i=6005"])]
)
o6.reference(cranes_hoists_objtypes.BrakeType, ns0.reftypes.HasComponent, o6.ns["ns=cranes_hoists;i=5020"])
ns0.vartypes.PropertyType(
    nodeId="ns=cranes_hoists;i=6013",
    browseName="EnumValues",
    parent="ns=cranes_hoists;i=3001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("NOT_REQUESTED", "en"), description=o6.LocalizedText("No control request inputs have been received from any client", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("REQUESTED_AND_CONTROL_ACTIVE", "en"),
            description=o6.LocalizedText("Control request input has been received from a client and the request is being applied to the control", "en"),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("REQUESTED_AND_CONTROL_INACTIVE", "en"),
            description=o6.LocalizedText("Control request input has been received from a client but the request is not currently being applied to the control", "en"),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("REQUESTED_AND_CONTROL_BYPASSED", "en"),
            description=o6.LocalizedText(
                "Control request input has been received from a client but the request is not currently being applied to the control because it has been bypassed in the control system",
                "en",
            ),
        ),
    ],
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=cranes_hoists;i=6014",
    browseName="EnumValues",
    parent="ns=cranes_hoists;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OTHER", "en"), description=o6.LocalizedText("Use if vendor specific", "en")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("FORCE_LIMITER", "en"), description=o6.LocalizedText("Limiting the transmitted force")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("OVERSPEED_CONTROL", "en"), description=o6.LocalizedText("Limiting the speed during operation")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("MOTION_LIMITER", "en"), description=o6.LocalizedText("Limiting by stopping motion")),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("ANTICOLLISION", "en"),
            description=o6.LocalizedText("Device with the ability to bring the moving crane or trolley(s) to a stop before a collision occurs"),
        ),
    ],
    accessLevel=3,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=cranes_hoists;i=2416",
    browseName="ns=cranes_hoists;CraneAxisFunction",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=cranes_hoists;i=6016",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[9],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("RATED_SPEED", "en"), description=o6.LocalizedText("The axis moves at rated speed.", "en")),
                    ns0.datatypes.EnumValueType(
                        value=1,
                        displayName=o6.LocalizedText("EXTENDED_SPEED", "en"),
                        description=o6.LocalizedText(
                            "The axis moves above the rated speed when load is under certain percentage of rated load. This function reduces the load cycle time and can be used for hoisting.",
                            "en",
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=2,
                        displayName=o6.LocalizedText("MICROSPEED", "en"),
                        description=o6.LocalizedText(
                            "Microspeed turns large joystick movements on the operator interface into slow and exact load movements. This function assists in very accurate and precise load handling and reduces the risk of collision and can be used for hoisting and travelling.",
                            "en",
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=3,
                        displayName=o6.LocalizedText("INCHING", "en"),
                        description=o6.LocalizedText(
                            "Inching is designed to ensure accurate final load positioning by allowing the crane operator to move the load in small increments. This function assists in very accurate and precise load handling and reduces the risk of collision and can be used for hoisting and travelling.",
                            "en",
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=4,
                        displayName=o6.LocalizedText("ANTISWAY", "en"),
                        description=o6.LocalizedText(
                            "This function limits load swing by controlling the bridge and trolley acceleration and deceleration. Antisway allows faster load handling and more precise positioning. This feature also reduces the risk of damage to the load, crane and surrounding area.",
                            "en",
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=5,
                        displayName=o6.LocalizedText("TANDEM_HOIST", "en"),
                        description=o6.LocalizedText(
                            "Two or more hoists are operated from a single control station for handling of a single load. Two or more load lifting attachments&#8217;/hooks&#8217; positions are synchronized. This function gives more accuracy when two or more hoists are used at the same time. Hoisting speeds are the same within the tolerances required for the particular application.",
                            "en",
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=6,
                        displayName=o6.LocalizedText("TANDEM_TROLLEY", "en"),
                        description=o6.LocalizedText(
                            "Two or more trolleys are operated from a single control station for handling of a single load. Horizontal speeds are the same within the tolerances required for the particular application.",
                            "en",
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=7,
                        displayName=o6.LocalizedText("TANDEM_CRANE", "en"),
                        description=o6.LocalizedText(
                            "This function allows the operator to control two cranes at the same time from one control station. The operator controls two cranes as one. This feature is useful when the operator needs to handle a single load with two cranes.",
                            "en",
                        ),
                    ),
                    ns0.datatypes.EnumValueType(
                        value=8,
                        displayName=o6.LocalizedText("PRESET_DESTINATION", "en"),
                        description=o6.LocalizedText(
                            "This function allows the operator to move the crane to a predefined position without effort. With a single operator input, the crane carries out the sequence to reach the selected destination.",
                            "en",
                        ),
                    ),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=cranes_hoists;i=6017", browseName="ValueAsText", dataType=o6.LocalizedText, valueRank=-2)),
    ],
    dataType=o6.UInt16,
    valueRank=1,
)
o6.reference(o6.ns["ns=cranes_hoists;i=2093"], "i=47", o6.ns["ns=cranes_hoists;i=2416"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=cranes_hoists;i=5003",
    browseName="ns=di;Operational",
    modellingRule="Optional",
    references=[
        o6.organizes(o6.ns["ns=cranes_hoists;i=1852"]),
        o6.organizes(o6.ns["ns=cranes_hoists;i=1950"]),
        o6.organizes(o6.ns["ns=cranes_hoists;i=2031"]),
        o6.organizes(o6.ns["ns=cranes_hoists;i=2037"]),
        o6.organizes(o6.ns["ns=cranes_hoists;i=2416"]),
    ],
)
o6.reference(cranes_hoists_objtypes.CraneAxisType, ns0.reftypes.HasComponent, o6.ns["ns=cranes_hoists;i=5003"])
o6.reference(o6.ns["ns=cranes_hoists;i=5003"], "i=35", o6.ns["ns=cranes_hoists;i=2096"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, robotics, cranes_hoists_reftypes, cranes_hoists_datypes, cranes_hoists_objtypes
