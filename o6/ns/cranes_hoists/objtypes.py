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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.BaseObjectType(nodeId="ns=cranes_hoists;i=2114", browseName="ns=di;ParameterSet")
machinery.objtypes.MachineIdentificationType(nodeId="ns=cranes_hoists;i=5000", browseName="ns=di;Identification")
machinery.objtypes.MachineIdentificationType(nodeId="ns=cranes_hoists;i=5005", browseName="ns=di;Identification")
di.objtypes.FunctionalGroupType(nodeId="ns=cranes_hoists;i=5009", browseName="ns=di;Operational")


@o6.objecttype(nodeId="ns=cranes_hoists;i=1556", browseName="ns=cranes_hoists;BrakeType", displayName="BrakeType")
class BrakeType(di.objtypes.ComponentType):
    identification: machinery.objtypes.MachineryComponentIdentificationType | None = o6.hasAddIn(
        machinery.objtypes.MachineryComponentIdentificationType(nodeId="ns=cranes_hoists;i=5002", browseName="ns=machinery;Identification")
    )
    operational: di.objtypes.FunctionalGroupType | None = o6.hasComponent(o6.ns["ns=cranes_hoists;i=5009"])
    parameterSet: ns0.objtypes.BaseObjectType


@o6.objecttype(nodeId="ns=cranes_hoists;i=1369", browseName="ns=cranes_hoists;CraneAxisType", displayName="CraneAxisType")
class CraneAxisType(robotics.objtypes.AxisType):
    actualLoad: robotics.objtypes.LoadType | None = o6.hasComponent(robotics.objtypes.LoadType(nodeId="ns=cranes_hoists;i=1378", browseName="ns=cranes_hoists;ActualLoad"))
    configuration: di.objtypes.FunctionalGroupType | None
    langleBackupBrakeIdentifierRangle: BrakeType | None = o6.hasComponent(
        BrakeType(nodeId="ns=cranes_hoists;i=1373", browseName="ns=cranes_hoists;<BackupBrakeIdentifier>", modellingRule="OptionalPlaceholder")
    )
    operational: di.objtypes.FunctionalGroupType | None
    parameterSet: ns0.objtypes.BaseObjectType


di.objtypes.FunctionalGroupType(nodeId="ns=cranes_hoists;i=5013", browseName="ns=di;Operational")
di.objtypes.FunctionalGroupType(nodeId="ns=cranes_hoists;i=5014", browseName="ns=di;Operational")
machinery.objtypes.MachineryComponentIdentificationType(nodeId="ns=cranes_hoists;i=5015", browseName="ns=machinery;Identification")
di.objtypes.FunctionalGroupType(nodeId="ns=cranes_hoists;i=5019", browseName="ns=di;Operational")


@o6.objecttype(nodeId="ns=cranes_hoists;i=1262", browseName="ns=cranes_hoists;CraneMotorType", displayName="CraneMotorType")
class CraneMotorType(robotics.objtypes.MotorType):
    identification: machinery.objtypes.MachineryComponentIdentificationType | None = o6.hasAddIn(o6.ns["ns=cranes_hoists;i=5015"])
    operational: di.objtypes.FunctionalGroupType | None = o6.hasComponent(o6.ns["ns=cranes_hoists;i=5019"])
    parameterSet: ns0.objtypes.BaseObjectType


o6.reference(CraneMotorType, "ns=robotics;i=18181", "ns=robotics;i=16041")


@o6.objecttype(nodeId="ns=cranes_hoists;i=1462", browseName="ns=cranes_hoists;ProtectiveFunctionType", displayName="ProtectiveFunctionType")
class ProtectiveFunctionType(ns0.objtypes.BaseObjectType):
    identification: machinery.objtypes.MachineryComponentIdentificationType | None = o6.hasAddIn(
        machinery.objtypes.MachineryComponentIdentificationType(nodeId="ns=cranes_hoists;i=5024", browseName="ns=machinery;Identification")
    )
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cranes_hoists;i=1479",
            browseName="ns=cranes_hoists;Name",
            description="The Name of the ProtectiveStopFunctionType provides a manufacturer-specific protective function identifier within the safety system.",
            dataType=o6.String,
        )
    )
    operational: di.objtypes.FunctionalGroupType | None = o6.hasComponent(o6.ns["ns=cranes_hoists;i=5013"])
    parameterSet: ns0.objtypes.BaseObjectType
    protectiveFunctionMode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cranes_hoists;i=1864",
            browseName="ns=cranes_hoists;ProtectiveFunctionMode",
            description="This property describes which is the mode of operation for this protective function, for example force limiter for overload protection devices or motion limiter for limit switches etc.",
            dataType=cranes_hoists_datypes.ProtectiveFunctionEnum,
        )
    )
    rampDown: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cranes_hoists;i=1472",
            browseName="ns=cranes_hoists;RampDown",
            description="Indicates if the motion is slowed down or stopped gracefully with ramping down instead of with brakes.",
            dataType=o6.Boolean,
        )
    )


ns0.vartypes.PropertyType(nodeId="ns=cranes_hoists;i=6007", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)
o6.reference(o6.ns["ns=cranes_hoists;i=5000"], "i=46", o6.ns["ns=cranes_hoists;i=6007"])
ns0.vartypes.PropertyType(nodeId="ns=cranes_hoists;i=6008", browseName="ns=di;SerialNumber", dataType=o6.String)
o6.reference(o6.ns["ns=cranes_hoists;i=5000"], "i=46", o6.ns["ns=cranes_hoists;i=6008"])
ns0.vartypes.PropertyType(nodeId="ns=cranes_hoists;i=6009", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)
o6.reference(o6.ns["ns=cranes_hoists;i=5005"], "i=46", o6.ns["ns=cranes_hoists;i=6009"])
o6.reference(o6.ns["ns=cranes_hoists;i=5015"], "i=46", o6.ns["ns=cranes_hoists;i=6009"])
ns0.vartypes.PropertyType(nodeId="ns=cranes_hoists;i=6010", browseName="ns=di;SerialNumber", dataType=o6.String)
o6.reference(o6.ns["ns=cranes_hoists;i=5005"], "i=46", o6.ns["ns=cranes_hoists;i=6010"])
o6.reference(o6.ns["ns=cranes_hoists;i=5015"], "i=46", o6.ns["ns=cranes_hoists;i=6010"])
ns0.vartypes.PropertyType(nodeId="ns=cranes_hoists;i=6011", browseName="ns=di;ProductInstanceUri", dataType=o6.String)
o6.reference(o6.ns["ns=cranes_hoists;i=5000"], "i=46", o6.ns["ns=cranes_hoists;i=6011"])


@o6.objecttype(nodeId="ns=cranes_hoists;i=2112", browseName="ns=cranes_hoists;CraneMotionDeviceSystemType", displayName="CraneMotionDeviceSystemType")
class CraneMotionDeviceSystemType(robotics.objtypes.MotionDeviceSystemType):
    components: machinery.objtypes.MachineComponentsType | None
    configuration: di.objtypes.FunctionalGroupType | None
    identification: machinery.objtypes.MachineIdentificationType = o6.hasAddIn(o6.ns["ns=cranes_hoists;i=5000"])
    manufacturer: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=cranes_hoists;i=6007"])
    operational: di.objtypes.FunctionalGroupType | None
    parameterSet: ns0.objtypes.BaseObjectType = o6.hasComponent(o6.ns["ns=cranes_hoists;i=2114"])
    productInstanceUri: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=cranes_hoists;i=6011"])
    protectiveFunctions: ns0.objtypes.FolderType | None
    serialNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=cranes_hoists;i=6008"])


ns0.vartypes.PropertyType(nodeId="ns=cranes_hoists;i=6012", browseName="ns=di;ProductInstanceUri", dataType=o6.String)
o6.reference(o6.ns["ns=cranes_hoists;i=5005"], "i=46", o6.ns["ns=cranes_hoists;i=6012"])
o6.reference(o6.ns["ns=cranes_hoists;i=5015"], "i=46", o6.ns["ns=cranes_hoists;i=6012"])


@o6.objecttype(nodeId="ns=cranes_hoists;i=1392", browseName="ns=cranes_hoists;CraneMotionDeviceType", displayName="CraneMotionDeviceType")
class CraneMotionDeviceType(robotics.objtypes.MotionDeviceType):
    axes: ns0.objtypes.FolderType
    components: machinery.objtypes.MachineComponentsType | None
    craneMotionDeviceCategory: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cranes_hoists;i=6004",
            browseName="ns=cranes_hoists;CraneMotionDeviceCategory",
            description="This property describes which category this motion device belongs to. Different categories include hoists, trolley traversing machineries, bridge or gantry travelling machineries, load lifting attachments etc.",
            dataType=cranes_hoists_datypes.CraneMotionDeviceCategoryEnum,
        )
    )
    identification: machinery.objtypes.MachineIdentificationType = o6.hasAddIn(o6.ns["ns=cranes_hoists;i=5005"])
    langleCraneMotionDeviceIdentifierRangle: CraneMotionDeviceType | None
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=cranes_hoists;i=6009"])
    operational: di.objtypes.FunctionalGroupType | None = o6.hasComponent(o6.ns["ns=cranes_hoists;i=5014"])
    parameterSet: ns0.objtypes.BaseObjectType
    productInstanceUri: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=cranes_hoists;i=6012"])
    serialNumber: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=cranes_hoists;i=6010"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, robotics, cranes_hoists_reftypes, cranes_hoists_datypes
