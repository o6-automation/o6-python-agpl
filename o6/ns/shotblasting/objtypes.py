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

"""Generated OPC UA shotblasting namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=shotblasting;i=1010", browseName="ns=shotblasting;DeploymentType", displayName="DeploymentType")
class DeploymentType(ns0.objtypes.BaseObjectType):
    actualConsumption: ns0.vartypes.AnalogUnitType | None
    consumedMedia: ns0.vartypes.MultiStateValueDiscreteType
    totalConsumption: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=shotblasting;i=1011", browseName="ns=shotblasting;HopperType", displayName="HopperType")
class HopperType(ns0.objtypes.BaseObjectType):
    monitoring: ns0.objtypes.FolderType | None


@o6.objecttype(nodeId="ns=shotblasting;i=1014", browseName="ns=shotblasting;RefillSiloType", displayName="RefillSiloType")
class RefillSiloType(ns0.objtypes.BaseObjectType):
    monitoring: ns0.objtypes.FolderType | None


@o6.objecttype(nodeId="ns=shotblasting;i=1015", browseName="ns=shotblasting;FiltrationType", displayName="FiltrationType")
class FiltrationType(ns0.objtypes.BaseObjectType):
    identification: machinery.objtypes.MachineryComponentIdentificationType
    machineryBuildingBlocks: ns0.objtypes.FolderType
    monitoring: ns0.objtypes.FolderType


ns0.objtypes.FolderType(nodeId="ns=shotblasting;i=5008", browseName="ns=machinery;MachineryBuildingBlocks")
ns0.objtypes.FolderType(nodeId="ns=shotblasting;i=5011", browseName="ns=machinery;MachineryBuildingBlocks")


@o6.objecttype(nodeId="ns=shotblasting;i=1008", browseName="ns=shotblasting;BlasterType", displayName="BlasterType")
class BlasterType(ns0.objtypes.BaseObjectType):
    identification: machinery.objtypes.MachineryComponentIdentificationType
    machineryBuildingBlocks: ns0.objtypes.FolderType = o6.hasComponent(o6.ns["ns=shotblasting;i=5011"])
    monitoring: ns0.objtypes.FolderType


ns0.objtypes.FolderType(nodeId="ns=shotblasting;i=5020", browseName="ns=machinery;MachineryBuildingBlocks")


@o6.objecttype(nodeId="ns=shotblasting;i=1017", browseName="ns=shotblasting;PressurisedBoilerType", displayName="PressurisedBoilerType")
class PressurisedBoilerType(ns0.objtypes.BaseObjectType):
    identification: machinery.objtypes.MachineryComponentIdentificationType
    machineryBuildingBlocks: ns0.objtypes.FolderType = o6.hasComponent(o6.ns["ns=shotblasting;i=5020"])
    monitoring: ns0.objtypes.FolderType


ns0.objtypes.FolderType(nodeId="ns=shotblasting;i=5023", browseName="ns=machinery;MachineryBuildingBlocks")


@o6.objecttype(nodeId="ns=shotblasting;i=1005", browseName="ns=shotblasting;ConveyorType", displayName="ConveyorType")
class ConveyorType(ns0.objtypes.BaseObjectType):
    identification: machinery.objtypes.MachineryComponentIdentificationType
    machineryBuildingBlocks: ns0.objtypes.FolderType = o6.hasComponent(o6.ns["ns=shotblasting;i=5023"])
    monitoring: ns0.objtypes.FolderType | None


@o6.objecttype(nodeId="ns=shotblasting;i=1004", browseName="ns=shotblasting;ShotBlastChamberType", displayName="ShotBlastChamberType")
class ShotBlastChamberType(ns0.objtypes.BaseObjectType):
    components: machinery.objtypes.MachineComponentsType
    identification: machinery.objtypes.MachineIdentificationType
    loadingState: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6014", browseName="ns=shotblasting;LoadingState", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    machineryBuildingBlocks: ns0.objtypes.FolderType = o6.hasComponent(o6.ns["ns=shotblasting;i=5008"])


@o6.objecttype(nodeId="ns=shotblasting;i=1006", browseName="ns=shotblasting;ShotBlastMediaType", displayName="ShotBlastMediaType")
class ShotBlastMediaType(ns0.objtypes.BaseObjectType):
    actualParticleSizeRange: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=shotblasting;i=6096", browseName="ns=shotblasting;ActualParticleSizeRange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1
        )
    )
    nominalParticleSizeAverage: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=shotblasting;i=6009", browseName="ns=shotblasting;NominalParticleSizeAverage", dataType=o6.Double, accessLevel=3, userAccessLevel=1
        )
    )
    nominalParticleSizeRange: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=shotblasting;i=6095", browseName="ns=shotblasting;NominalParticleSizeRange", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1
        )
    )
    shotBlastMediaBatch: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6134", browseName="ns=shotblasting;ShotBlastMediaBatch", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    shotBlastMediaHardnessAverage: ns0.vartypes.BaseDataVariableType | None
    shotBlastMediaHardnessRange: ns0.vartypes.BaseDataVariableType | None
    shotBlastMediaManufacturer: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6008", browseName="ns=shotblasting;ShotBlastMediaManufacturer", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    shotBlastMediaName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=shotblasting;i=6007", browseName="ns=shotblasting;ShotBlastMediaName", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=shotblasting;i=1003", browseName="ns=shotblasting;ShotBlastMachineType", displayName="ShotBlastMachineType")
class ShotBlastMachineType(ns0.objtypes.BaseObjectType):
    components: machinery.objtypes.MachineComponentsType
    identification: machinery.objtypes.MachineIdentificationType
    machineryBuildingBlocks: ns0.objtypes.FolderType
    monitoring: ns0.objtypes.FolderType | None
    shotBlastMedia: ShotBlastMediaType | None = o6.hasComponent(ShotBlastMediaType(nodeId="ns=shotblasting;i=5003", browseName="ns=shotblasting;ShotBlastMedia"))


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, ns0
