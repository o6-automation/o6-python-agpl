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

"""Generated OPC UA machine_vision_amcm namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
from . import reftypes as machine_vision_amcm_reftypes
from . import datatypes as machine_vision_amcm_datypes
from . import vartypes as machine_vision_amcm_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1002", browseName="ns=machine_vision_amcm;IVisionInfoType", displayName="IVisionInfoType", isAbstract=True)
class IVisionInfoType(ns0.objtypes.BaseInterfaceType):
    health: VisionHealthInfoType | None
    identification: machinery.objtypes.MachineryItemIdentificationType
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1005", browseName="ns=machine_vision_amcm;VisionItemFolderType", displayName="VisionItemFolderType")
class VisionItemFolderType(ns0.objtypes.FolderType):
    langleVisionItemRangle: ns0.objtypes.BaseObjectType


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1009", browseName="ns=machine_vision_amcm;IComputingDeviceType", displayName="IComputingDeviceType", isAbstract=True)
class IComputingDeviceType(IVisionInfoType):
    health: VisionHealthInfoType | None
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(
    nodeId="ns=machine_vision_amcm;i=1010",
    browseName="ns=machine_vision_amcm;VisionComputingDeviceType",
    displayName="VisionComputingDeviceType",
    interfaces=[IComputingDeviceType],
)
class VisionComputingDeviceType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1011", browseName="ns=machine_vision_amcm;IDisplayUnitType", displayName="IDisplayUnitType", isAbstract=True)
class IDisplayUnitType(IVisionInfoType):
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1012", browseName="ns=machine_vision_amcm;IPhysicalInterfaceType", displayName="IPhysicalInterfaceType", isAbstract=True)
class IPhysicalInterfaceType(IVisionInfoType):
    health: VisionHealthInfoType | None
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1013", browseName="ns=machine_vision_amcm;ILensType", displayName="ILensType", isAbstract=True)
class ILensType(IVisionInfoType):
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(
    nodeId="ns=machine_vision_amcm;i=1014",
    browseName="ns=machine_vision_amcm;VisionPhysicalInterfaceType",
    displayName="VisionPhysicalInterfaceType",
    interfaces=[IPhysicalInterfaceType],
)
class VisionPhysicalInterfaceType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1015", browseName="ns=machine_vision_amcm;ILightingControllerType", displayName="ILightingControllerType", isAbstract=True)
class ILightingControllerType(IVisionInfoType):
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1016", browseName="ns=machine_vision_amcm;ILampType", displayName="ILampType", isAbstract=True)
class ILampType(IVisionInfoType):
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1017", browseName="ns=machine_vision_amcm;ILicenseType", displayName="ILicenseType", isAbstract=True)
class ILicenseType(IVisionInfoType):
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1018", browseName="ns=machine_vision_amcm;ICableType", displayName="ICableType", isAbstract=True)
class ICableType(IVisionInfoType):
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(
    nodeId="ns=machine_vision_amcm;i=1019", browseName="ns=machine_vision_amcm;VisionDisplayUnitType", displayName="VisionDisplayUnitType", interfaces=[IDisplayUnitType]
)
class VisionDisplayUnitType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1026", browseName="ns=machine_vision_amcm;VisionWayEncoderType", displayName="VisionWayEncoderType", interfaces=[IVisionInfoType])
class VisionWayEncoderType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(
    nodeId="ns=machine_vision_amcm;i=1027", browseName="ns=machine_vision_amcm;VisionTriggerSensorType", displayName="VisionTriggerSensorType", interfaces=[IVisionInfoType]
)
class VisionTriggerSensorType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(
    nodeId="ns=machine_vision_amcm;i=1032",
    browseName="ns=machine_vision_amcm;VisionAcquisitionBackgroundType",
    displayName="VisionAcquisitionBackgroundType",
    interfaces=[IVisionInfoType],
)
class VisionAcquisitionBackgroundType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(
    nodeId="ns=machine_vision_amcm;i=1035", browseName="ns=machine_vision_amcm;VisionClimateControllerType", displayName="VisionClimateControllerType", interfaces=[IVisionInfoType]
)
class VisionClimateControllerType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1038", browseName="ns=machine_vision_amcm;VisionCableType", displayName="VisionCableType", interfaces=[ICableType])
class VisionCableType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1039", browseName="ns=machine_vision_amcm;VisionAspectImageTransmitterType", displayName="VisionAspectImageTransmitterType")
class VisionAspectImageTransmitterType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1040", browseName="ns=machine_vision_amcm;VisionAspectImageReceiverType", displayName="VisionAspectImageReceiverType")
class VisionAspectImageReceiverType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1041", browseName="ns=machine_vision_amcm;VisionAspectImageTransceiverType", displayName="VisionAspectImageTransceiverType")
class VisionAspectImageTransceiverType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1008", browseName="ns=machine_vision_amcm;VisionSystemAssetType", displayName="VisionSystemAssetType", interfaces=[IVisionInfoType])
class VisionSystemAssetType(ns0.objtypes.BaseObjectType):
    acquisitionBackgrounds: VisionItemFolderType | None
    cables: VisionItemFolderType | None
    calibrationTargets: VisionItemFolderType | None
    climateControllers: VisionItemFolderType | None
    components: machinery.objtypes.MachineComponentsType | None = o6.hasAddIn(
        machinery.objtypes.MachineComponentsType(nodeId="ns=machine_vision_amcm;i=5009", browseName="ns=machinery;Components")
    )
    computingDevices: VisionItemFolderType | None
    displayUnits: VisionItemFolderType | None
    frameGrabbers: VisionItemFolderType | None
    health: VisionHealthInfoType | None
    housings: VisionItemFolderType | None
    identification: VisionMachineIdentificationType
    imageHandlingAspects: ns0.objtypes.FolderType | None
    imageSensors: VisionItemFolderType | None
    lamps: VisionItemFolderType | None
    lensControllers: VisionItemFolderType | None
    lenses: VisionItemFolderType | None
    licenses: VisionItemFolderType | None
    lightingControllers: VisionItemFolderType | None
    maintenance: VisionMaintenanceInfoType | None
    motionDevices: VisionItemFolderType | None
    networkDevices: VisionItemFolderType | None
    opticalFilters: VisionItemFolderType | None
    otherOpticalEquipments: VisionItemFolderType | None
    patternGenerators: VisionItemFolderType | None
    physicalInterfaces: VisionItemFolderType | None
    powerSupplies: VisionItemFolderType | None
    softwareComponents: VisionItemFolderType | None
    surroundingEnvironment: VisionItemFolderType | None
    triggerSensors: VisionItemFolderType | None
    wayEncoders: VisionItemFolderType | None


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1003", browseName="ns=machine_vision_amcm;VisionMaintenanceInfoType", displayName="VisionMaintenanceInfoType")
class VisionMaintenanceInfoType(di.objtypes.FunctionalGroupType):
    calibrationNeeded: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6005",
            browseName="ns=machine_vision_amcm;CalibrationNeeded",
            description="a flag that if True denotes that the item needs calibration",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    firmwareInfo: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6225",
            browseName="ns=machine_vision_amcm;FirmwareInfo",
            description="denotes the information about the firmware of the Item",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    lastCalibration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6006",
            browseName="ns=machine_vision_amcm;LastCalibration",
            description="denotes the time when the previous calibration was carried out on the item",
            dataType=ns0.datatypes.UtcTime,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    lastService: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6025",
            browseName="ns=machine_vision_amcm;LastService",
            description="denotes the last moment in time when the most recent service was carried out on the item",
            dataType=ns0.datatypes.UtcTime,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    maintenanceRecord: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6009",
            browseName="ns=machine_vision_amcm;MaintenanceRecord",
            description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    nextCalibration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6007",
            browseName="ns=machine_vision_amcm;NextCalibration",
            description="denotes the planned time when the next calibration is to be carried out on the item.",
            dataType=ns0.datatypes.UtcTime,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    nextService: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6003",
            browseName="ns=machine_vision_amcm;NextService",
            description="denotes the planned moment in time when the next service is to be carried out on the item",
            dataType=ns0.datatypes.UtcTime,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    operationCounters: machinery.objtypes.MachineryOperationCounterType | None
    serviceClass: ns0.vartypes.MultiStateDiscreteType | None
    startOfWarranty: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6001",
            browseName="ns=machine_vision_amcm;StartOfWarranty",
            description="denotes the beginning of the warranty period of the item",
            dataType=ns0.datatypes.UtcTime,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=machine_vision_amcm;i=1021", browseName="ns=machine_vision_amcm;VisionFrameGrabberType", displayName="VisionFrameGrabberType", interfaces=[IVisionInfoType]
)
class VisionFrameGrabberType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None = o6.hasAddIn(VisionMaintenanceInfoType(nodeId="ns=machine_vision_amcm;i=5156", browseName="ns=di;Maintenance"))


@o6.objecttype(
    nodeId="ns=machine_vision_amcm;i=1004", browseName="ns=machine_vision_amcm;VisionHealthInfoType", displayName="VisionHealthInfoType", interfaces=[di.objtypes.IDeviceHealthType]
)
class VisionHealthInfoType(di.objtypes.FunctionalGroupType):
    deviceHealth: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_vision_amcm;i=6497",
            browseName="ns=di;DeviceHealth",
            description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
            dataType=di.datatypes.DeviceHealthEnumeration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    deviceHealthAlarms: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(
            nodeId="ns=machine_vision_amcm;i=5221",
            browseName="ns=di;DeviceHealthAlarms",
            description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
        )
    )
    remainingLifeTime: di.vartypes.LifetimeVariableType | None
    state: machine_vision_amcm_vartypes.SEMI_E10SystemStateType | None
    temperature: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1034", browseName="ns=machine_vision_amcm;VisionHousingType", displayName="VisionHousingType", interfaces=[IVisionInfoType])
class VisionHousingType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None = o6.hasAddIn(VisionHealthInfoType(nodeId="ns=machine_vision_amcm;i=5158", browseName="ns=machine_vision_amcm;Health"))
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None = o6.hasAddIn(VisionMaintenanceInfoType(nodeId="ns=machine_vision_amcm;i=5159", browseName="ns=di;Maintenance"))


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1020", browseName="ns=machine_vision_amcm;VisionImageSensorType", displayName="VisionImageSensorType", interfaces=[IVisionInfoType])
class VisionImageSensorType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None = o6.hasAddIn(VisionHealthInfoType(nodeId="ns=machine_vision_amcm;i=5161", browseName="ns=machine_vision_amcm;Health"))
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None = o6.hasAddIn(VisionMaintenanceInfoType(nodeId="ns=machine_vision_amcm;i=5163", browseName="ns=di;Maintenance"))


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1028", browseName="ns=machine_vision_amcm;VisionLampType", displayName="VisionLampType", interfaces=[ILampType])
class VisionLampType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None = o6.hasAddIn(VisionHealthInfoType(nodeId="ns=machine_vision_amcm;i=5166", browseName="ns=machine_vision_amcm;Health"))
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(
    nodeId="ns=machine_vision_amcm;i=1023", browseName="ns=machine_vision_amcm;VisionLensControllerType", displayName="VisionLensControllerType", interfaces=[IVisionInfoType]
)
class VisionLensControllerType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None = o6.hasAddIn(VisionHealthInfoType(nodeId="ns=machine_vision_amcm;i=5169", browseName="ns=machine_vision_amcm;Health"))
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None = o6.hasAddIn(VisionMaintenanceInfoType(nodeId="ns=machine_vision_amcm;i=5167", browseName="ns=di;Maintenance"))


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1022", browseName="ns=machine_vision_amcm;VisionLensType", displayName="VisionLensType", interfaces=[ILensType])
class VisionLensType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None = o6.hasAddIn(VisionHealthInfoType(nodeId="ns=machine_vision_amcm;i=5170", browseName="ns=machine_vision_amcm;Health"))
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1036", browseName="ns=machine_vision_amcm;VisionLicenseType", displayName="VisionLicenseType", interfaces=[ILicenseType])
class VisionLicenseType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None = o6.hasAddIn(VisionHealthInfoType(nodeId="ns=machine_vision_amcm;i=5175", browseName="ns=machine_vision_amcm;Health"))
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(
    nodeId="ns=machine_vision_amcm;i=1029",
    browseName="ns=machine_vision_amcm;VisionLightingControllerType",
    displayName="VisionLightingControllerType",
    interfaces=[ILightingControllerType],
)
class VisionLightingControllerType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None = o6.hasAddIn(VisionHealthInfoType(nodeId="ns=machine_vision_amcm;i=5178", browseName="ns=machine_vision_amcm;Health"))
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None


@o6.objecttype(
    nodeId="ns=machine_vision_amcm;i=1037", browseName="ns=machine_vision_amcm;VisionNetworkDeviceType", displayName="VisionNetworkDeviceType", interfaces=[IVisionInfoType]
)
class VisionNetworkDeviceType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None = o6.hasAddIn(VisionHealthInfoType(nodeId="ns=machine_vision_amcm;i=5186", browseName="ns=machine_vision_amcm;Health"))
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None = o6.hasAddIn(VisionMaintenanceInfoType(nodeId="ns=machine_vision_amcm;i=5185", browseName="ns=di;Maintenance"))


@o6.objecttype(
    nodeId="ns=machine_vision_amcm;i=1024", browseName="ns=machine_vision_amcm;VisionOpticalFilterType", displayName="VisionOpticalFilterType", interfaces=[IVisionInfoType]
)
class VisionOpticalFilterType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None = o6.hasAddIn(VisionHealthInfoType(nodeId="ns=machine_vision_amcm;i=5190", browseName="ns=machine_vision_amcm;Health"))
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None = o6.hasAddIn(VisionMaintenanceInfoType(nodeId="ns=machine_vision_amcm;i=5189", browseName="ns=di;Maintenance"))


@o6.objecttype(
    nodeId="ns=machine_vision_amcm;i=1025",
    browseName="ns=machine_vision_amcm;VisionOtherOpticalEquipmentType",
    displayName="VisionOtherOpticalEquipmentType",
    interfaces=[IVisionInfoType],
)
class VisionOtherOpticalEquipmentType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None = o6.hasAddIn(VisionHealthInfoType(nodeId="ns=machine_vision_amcm;i=5191", browseName="ns=machine_vision_amcm;Health"))
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None = o6.hasAddIn(VisionMaintenanceInfoType(nodeId="ns=machine_vision_amcm;i=5192", browseName="ns=di;Maintenance"))


@o6.objecttype(
    nodeId="ns=machine_vision_amcm;i=1030", browseName="ns=machine_vision_amcm;VisionPatternGeneratorType", displayName="VisionPatternGeneratorType", interfaces=[IVisionInfoType]
)
class VisionPatternGeneratorType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None = o6.hasAddIn(VisionHealthInfoType(nodeId="ns=machine_vision_amcm;i=5196", browseName="ns=machine_vision_amcm;Health"))
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None = o6.hasAddIn(VisionMaintenanceInfoType(nodeId="ns=machine_vision_amcm;i=5195", browseName="ns=di;Maintenance"))


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1031", browseName="ns=machine_vision_amcm;VisionPowerSupplyType", displayName="VisionPowerSupplyType", interfaces=[IVisionInfoType])
class VisionPowerSupplyType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None = o6.hasAddIn(VisionHealthInfoType(nodeId="ns=machine_vision_amcm;i=5200", browseName="ns=machine_vision_amcm;Health"))
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None = o6.hasAddIn(VisionMaintenanceInfoType(nodeId="ns=machine_vision_amcm;i=5201", browseName="ns=di;Maintenance"))


@o6.objecttype(
    nodeId="ns=machine_vision_amcm;i=1033",
    browseName="ns=machine_vision_amcm;VisionSurroundingEnvironmentType",
    displayName="VisionSurroundingEnvironmentType",
    interfaces=[IVisionInfoType],
)
class VisionSurroundingEnvironmentType(ns0.objtypes.BaseObjectType):
    health: VisionHealthInfoType | None = o6.hasAddIn(VisionHealthInfoType(nodeId="ns=machine_vision_amcm;i=5205", browseName="ns=machine_vision_amcm;Health"))
    identification: VisionComponentIdentificationType
    maintenance: VisionMaintenanceInfoType | None = o6.hasAddIn(VisionMaintenanceInfoType(nodeId="ns=machine_vision_amcm;i=5204", browseName="ns=di;Maintenance"))


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1007", browseName="ns=machine_vision_amcm;VisionComponentIdentificationType", displayName="VisionComponentIdentificationType")
class VisionComponentIdentificationType(machinery.objtypes.MachineryComponentIdentificationType):
    assetId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6768",
            browseName="ns=di;AssetId",
            description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    componentName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6769",
            browseName="ns=di;ComponentName",
            description="To be used by end users to store a human-readable localized text for the MachineryItem. The minimum number of locales supported for this property shall be two. Servers shall support at least 40 Unicode characters for the clients writing the text part of each locale, this means clients can expect to be able to write texts with a length of 40 Unicode characters into that field.",
            dataType=o6.LocalizedText,
            value=o6.LocalizedText(),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    configurationCode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6029",
            browseName="ns=machine_vision_amcm;ConfigurationCode",
            description="provides the specific information how the machine vision system has been configured for a specific use case or application",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    deviceClass: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6770",
            browseName="ns=di;DeviceClass",
            description="Indicates in which domain or for what purpose the MachineryItem is used.",
            dataType=o6.String,
        )
    )
    deviceRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6767",
            browseName="ns=di;DeviceRevision",
            description="A string representation of the overall revision level of the component. Often, it is increased when either the SoftwareRevision and / or the HardwareRevision of the component is increased. As an example, it can be used in ERP systems together with the ProductCode.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    hardwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6771",
            browseName="ns=di;HardwareRevision",
            description="provides the revision level of the hardware of the machine vision system following the rules of Sematic Versioning 2.0.0",
            dataType=ns0.datatypes.SemanticVersionString,
        )
    )
    initialOperationDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6772",
            browseName="ns=machinery;InitialOperationDate",
            description="The date, when the MachineryItem was switched on the first time after it has left the manufacturer plant.",
            dataType=o6.DateTime,
        )
    )
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6773",
            browseName="ns=di;Manufacturer",
            description="A human-readable, localized name of the manufacturer of the MachineryItem.",
            dataType=o6.LocalizedText,
        )
    )
    manufacturerUri: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6774",
            browseName="ns=di;ManufacturerUri",
            description="A globally unique identifier of the manufacturer of the MachineryItem.",
            dataType=o6.String,
        )
    )
    model: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6775",
            browseName="ns=di;Model",
            description="A human-readable, localized name of the model of the MachineryItem.",
            dataType=o6.LocalizedText,
        )
    )
    monthOfConstruction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6776",
            browseName="ns=machinery;MonthOfConstruction",
            description="The month in which the manufacturing process of the MachineryItem has been completed. It shall be a number between 1 and 12, representing the month from January to December.",
            dataType=o6.Byte,
        )
    )
    productCode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6777",
            browseName="ns=di;ProductCode",
            description="A machine-readable string of the model of the MachineryItem, that might include options like the hardware configuration of the model. This information might be provided by the ERP system of the vendor. For example, it can be used as order information.",
            dataType=o6.String,
        )
    )
    productInstanceUri: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6778",
            browseName="ns=di;ProductInstanceUri",
            description="A globally unique resource identifier provided by the manufacturer of the MachineryItem.",
            dataType=o6.String,
        )
    )
    serialNumber: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6779",
            browseName="ns=di;SerialNumber",
            description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
            dataType=o6.String,
        )
    )
    softwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6780",
            browseName="ns=di;SoftwareRevision",
            description="property provides the version or revision level of the software in the machine vision system following the rules of Semantic Versioning 2.0.0.",
            dataType=ns0.datatypes.SemanticVersionString,
        )
    )
    yearOfConstruction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6781",
            browseName="ns=machinery;YearOfConstruction",
            description="The year (Gregorian calendar) in which the manufacturing process of the MachineryItem has been completed. It shall be a four-digit number and never change during the life-cycle of a MachineryItem.",
            dataType=o6.UInt16,
        )
    )


@o6.objecttype(nodeId="ns=machine_vision_amcm;i=1006", browseName="ns=machine_vision_amcm;VisionMachineIdentificationType", displayName="VisionMachineIdentificationType")
class VisionMachineIdentificationType(machinery.objtypes.MachineIdentificationType):
    assetId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6785",
            browseName="ns=di;AssetId",
            description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    componentName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6786",
            browseName="ns=di;ComponentName",
            description="To be used by end users to store a human-readable localized text for the MachineryItem. The minimum number of locales supported for this property shall be two. Servers shall support at least 40 Unicode characters for the clients writing the text part of each locale, this means clients can expect to be able to write texts with a length of 40 Unicode characters into that field.",
            dataType=o6.LocalizedText,
            value=o6.LocalizedText(),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    configurationCode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6026",
            browseName="ns=machine_vision_amcm;ConfigurationCode",
            description="provides the specific information how the machine vision system has been configured for a specific use case or application",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    deviceClass: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6787",
            browseName="ns=di;DeviceClass",
            description="Indicates in which domain or for what purpose the MachineryItem is used.",
            dataType=o6.String,
        )
    )
    hardwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6788",
            browseName="ns=di;HardwareRevision",
            description="provides the revision level of the hardware of the machine vision system following the rules of Sematic Versioning 2.0.0",
            dataType=ns0.datatypes.SemanticVersionString,
        )
    )
    initialOperationDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6789",
            browseName="ns=machinery;InitialOperationDate",
            description="The date, when the MachineryItem was switched on the first time after it has left the manufacturer plant.",
            dataType=o6.DateTime,
        )
    )
    location: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6783",
            browseName="ns=machinery;Location",
            description="To be used by end users to store the location of the machine in a scheme specific to the end user. Servers shall support at least 60 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 60 Unicode characters into that field.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6790",
            browseName="ns=di;Manufacturer",
            description="A human-readable, localized name of the manufacturer of the MachineryItem.",
            dataType=o6.LocalizedText,
        )
    )
    manufacturerUri: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6791",
            browseName="ns=di;ManufacturerUri",
            description="A globally unique identifier of the manufacturer of the MachineryItem.",
            dataType=o6.String,
        )
    )
    model: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6792",
            browseName="ns=di;Model",
            description="A human-readable, localized name of the model of the MachineryItem.",
            dataType=o6.LocalizedText,
        )
    )
    monthOfConstruction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6793",
            browseName="ns=machinery;MonthOfConstruction",
            description="The month in which the manufacturing process of the MachineryItem has been completed. It shall be a number between 1 and 12, representing the month from January to December.",
            dataType=o6.Byte,
        )
    )
    productCode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6794",
            browseName="ns=di;ProductCode",
            description="A machine-readable string of the model of the MachineryItem, that might include options like the hardware configuration of the model. This information might be provided by the ERP system of the vendor. For example, it can be used as order information.",
            dataType=o6.String,
        )
    )
    productInstanceUri: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6784",
            browseName="ns=di;ProductInstanceUri",
            description="A globally unique resource identifier provided by the manufacturer of the machine",
            dataType=o6.String,
        )
    )
    serialNumber: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6795",
            browseName="ns=di;SerialNumber",
            description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
            dataType=o6.String,
        )
    )
    softwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6796",
            browseName="ns=di;SoftwareRevision",
            description="property provides the version or revision level of the software in the machine vision system following the rules of Semantic Versioning 2.0.0.",
            dataType=ns0.datatypes.SemanticVersionString,
        )
    )
    yearOfConstruction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_vision_amcm;i=6797",
            browseName="ns=machinery;YearOfConstruction",
            description="The year (Gregorian calendar) in which the manufacturing process of the MachineryItem has been completed. It shall be a four-digit number and never change during the life-cycle of a MachineryItem.",
            dataType=o6.UInt16,
        )
    )


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, machine_vision_amcm_reftypes, machine_vision_amcm_datypes, machine_vision_amcm_vartypes
