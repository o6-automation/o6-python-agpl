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
from . import objtypes as machine_vision_amcm_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision_amcm;i=5215", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision_amcm;i=5216", browseName="Default XML")
o6.hasEncoding(machine_vision_amcm_datypes.SEMI_E10SystemStateDataType, o6.ns["ns=machine_vision_amcm;i=5216"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision_amcm;i=5217", browseName="Default JSON")
o6.hasEncoding(machine_vision_amcm_datypes.SEMI_E10SystemStateDataType, o6.ns["ns=machine_vision_amcm;i=5217"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision_amcm;i=5218", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision_amcm;i=5219", browseName="Default XML")
o6.hasEncoding(machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType, o6.ns["ns=machine_vision_amcm;i=5219"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision_amcm;i=5220", browseName="Default JSON")
o6.hasEncoding(machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType, o6.ns["ns=machine_vision_amcm;i=5220"])
ns0.objtypes.FolderType(
    nodeId="ns=machine_vision_amcm;i=5060",
    browseName="ns=machine_vision_amcm;ImageHandlingAspects",
    modellingRule="Optional",
    references=[
        o6.organizes(
            ns0.objtypes.BaseObjectType(nodeId="ns=machine_vision_amcm;i=5222", browseName="ns=machine_vision_amcm;<ImageHandlingAspect>", modellingRule="MandatoryPlaceholder")
        )
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5060"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6011",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6012", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machine_vision_amcm_objtypes.VisionHealthInfoType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=6011"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMachineVisionSlashAMCMSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=machine_vision_amcm;i=5005",
    browseName="ns=machine_vision_amcm;http://opcfoundation.org/UA/MachineVision/AMCM/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6016", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6017", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2024-05-17T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6018", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/MachineVision/AMCM/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6019", browseName="NamespaceVersion", dataType=o6.String, value="1.00.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6020",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6021", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6022", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5006",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6023",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6024",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryOperationCounterType(
    nodeId="ns=machine_vision_amcm;i=5258",
    browseName="ns=di;OperationCounters",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6002",
                browseName="ns=di;OperationCycleCounter",
                description="OperationCycleCounter is counting the times the component switches from not performing an activity to performing an activity. For example, each time a valve starts moving, is counted. This value shall only increase during the lifetime of the component and shall not be reset when the component is restarted.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6004",
                browseName="ns=di;OperationDuration",
                description="OperationDuration is the duration the MachineryItem has been powered and performing an activity. This counter is intended for machines and components where a distinction is made between switched on and in operation. For example, a drive might be powered on but not operating. It is not intended for machines or components always performing an activity like sensors always measuring data. This value shall only increase during the lifetime of the MachineryItem and shall not be reset when it is restarted. The OperationDuration is provided as Duration, i.e., in milliseconds or even fractions of a millisecond. However, the Server is not expected to update the value in such a high frequency, but maybe once a minute or once an hour, depending on the application.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6027",
                browseName="ns=di;PowerOnDuration",
                description="PowerOnDuration is the duration the MachineryItem has been powered. The main purpose is to determine the time in which degradation of the MachineryItem occurred. The details, when the time is counted, is implementation-specific. Companion specifications might define specific rules. Typically, when the MachineryItem has supply voltage and the main CPU is running, the time is counted. This may include any kind of sleep mode, but may not include pure Wake on LAN. This value shall only increase during the lifetime of the MachineryItem and shall not be reset when it is restarted. The PowerOnDuration is provided as Duration, i.e., in milliseconds or even fractions of a millisecond. However, the Server is not expected to update the value in such a high frequency, but maybe once a minute or once an hour, depending on the application.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionMaintenanceInfoType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5258"])
o6.reference(o6.ns["ns=machine_vision_amcm;i=5258"], "i=17603", "ns=di;i=480")
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=machine_vision_amcm;i=6008",
    browseName="ns=machine_vision_amcm;ServiceClass",
    description="provides information that an item is classified as a wear and tear part, whether it is a line replaceable unit (LRU), shop replaceable unit (SRU), wear and tear part (WTP), infrastructural unit (ISU), infrastructural equipment (ISE), etc",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6028",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    o6.LocalizedText("OTHER", "en"),
                    o6.LocalizedText("LRU – Line Replaceable Unit ", "en"),
                    o6.LocalizedText("SRU – Shop Replaceable Unit", "en"),
                    o6.LocalizedText("WTP – Wear and Tear Part", "en"),
                    o6.LocalizedText("ISU – Infrastructural Unit ", "en"),
                    o6.LocalizedText("ISE – Infrastructural Equipment", "en"),
                ],
            )
        )
    ],
    dataType=ns0.datatypes.UInteger,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machine_vision_amcm_objtypes.VisionMaintenanceInfoType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=6008"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=machine_vision_amcm;i=6030",
    browseName="ns=machine_vision_amcm;ServiceClass",
    description="provides information that an item is classified as a wear and tear part, whether it is a line replaceable unit (LRU), shop replaceable unit (SRU), wear and tear part (WTP), infrastructural unit (ISU), infrastructural equipment (ISE), etc",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6031",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[6],
                value=[
                    o6.LocalizedText("OTHER", "en"),
                    o6.LocalizedText("LRU – Line Replaceable Unit ", "en"),
                    o6.LocalizedText("SRU – Shop Replaceable Unit", "en"),
                    o6.LocalizedText("WTP – Wear and Tear Part", "en"),
                    o6.LocalizedText("ISU – Infrastructural Unit ", "en"),
                    o6.LocalizedText("ISE – Infrastructural Equipment", "en"),
                ],
            )
        )
    ],
    dataType=ns0.datatypes.UInteger,
    accessLevel=3,
    userAccessLevel=1,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5065",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6036",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6037",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5068",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6038",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6039",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5071",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6040",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6041",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5074",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6042",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6043",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5077",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6044",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6045",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5080",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6046",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6047",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5083",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6048",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6049",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5086",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6050",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6051",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5089",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6052",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6053",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5092",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6054",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6055",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5095",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6056",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6057",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5098",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6058",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6059",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5101",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6060",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6061",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5104",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6062",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6063",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5107",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6064",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6065",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5113",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6068",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6069",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5116",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6070",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6071",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5119",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6072",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6073",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5122",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6074",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6075",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5125",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6076",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6077",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5128",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6078",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6079",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5131",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6080",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6081",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5134",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6082",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6083",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5137",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6084",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6085",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5199",
    browseName="ns=machine_vision_amcm;Health",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6092",
                browseName="ns=machine_vision_amcm;ConnectionStatus",
                description="denotes if a signal is being received by the physical interface from the perspective of the machine vision system",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionPhysicalInterfaceType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5199"])
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5140",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6093",
                browseName="ns=machine_vision_amcm;OperatingSystemInfo",
                description="denotes information about low-level software that supports the basic functions of the computing device such as scheduling task and controlling peripherals",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6094",
                browseName="ns=machine_vision_amcm;DriverInfo",
                description="denotes information about the set of drivers being used by the computing device",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6095",
                browseName="ns=machine_vision_amcm;SoftwareImageInfo",
                description="denotes information about the software image that is in use in the computing device",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.IComputingDeviceType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5140"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5141",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6096",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6097",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionComputingDeviceType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5141"])
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5197",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6100",
                browseName="ns=machine_vision_amcm;ConnectorType",
                description="property denotes the type of connector for the physical interface (e.g., USB, Ethernet, etc.)",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionPhysicalInterfaceType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5197"])
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5144",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6098",
                browseName="ns=machine_vision_amcm;InputInUse",
                description="denotes the signal port for the display unit currently in use. This property could also be used from the vision system perspective to denote signal source for the display unit if multiple sources share the same display unit e.g., X1, X2 (as per the convention used in the DIN EN IEC 81346-2:2020-10 specification)",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6099",
                browseName="ns=machine_vision_amcm;ResolutionInUse",
                description="denotes the pixel resolution in use (e.g., 1920x1080)",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6102",
                browseName="ns=machine_vision_amcm;InputSignalDetected",
                description="a flag that denotes if a signal is being detected in the InputInUse",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.IDisplayUnitType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5144"])
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5142",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6101",
                browseName="ns=machine_vision_amcm;OperatingSystemInfo",
                description="denotes information about low-level software that supports the basic functions of the computing device such as scheduling task and controlling peripherals",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6103",
                browseName="ns=machine_vision_amcm;DriverInfo",
                description="denotes information about the set of drivers being used by the computing device",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6104",
                browseName="ns=machine_vision_amcm;SoftwareImageInfo",
                description="denotes information about the software image that is in use in the computing device",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionComputingDeviceType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5142"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5155",
    browseName="ns=machine_vision_amcm;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6088",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6107",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionFrameGrabberType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5155"])
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5143",
    browseName="ns=machine_vision_amcm;Health",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6105",
                browseName="ns=machine_vision_amcm;BatteryState",
                description="denotes overall information about the condition of the battery or batteries",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6106",
                browseName="ns=machine_vision_amcm;CCUState",
                description="denotes a composite state providing overall information about the condition of the climate control units (CCU) e.g., fans, heatsinks, cooling pumps, heating etc",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6108",
                browseName="ns=machine_vision_amcm;MassStorageState",
                description="denotes overall information about the condition of the mass storage e.g., specific drives or RAID arrays etc.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6109",
                browseName="ns=machine_vision_amcm;PatchLevel",
                description="denotes the patch level or patch set. When patches must be applied in order, it is usually an identifier of the most recent patch applied to the system",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6110",
                browseName="ns=machine_vision_amcm;RAMState",
                description="denotes overall information about the condition of the RAM (e.g., there are systems using ECC enabled RAM that can provide information about the health state of the RAM modules)",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionComputingDeviceType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5143"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5153",
    browseName="ns=machine_vision_amcm;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6111",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6112",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionDisplayUnitType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5153"])
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5145",
    browseName="ns=machine_vision_amcm;Health",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6114",
                browseName="ns=machine_vision_amcm;ConnectionStatus",
                description="denotes if a signal is being received by the physical interface from the perspective of the machine vision system",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
)
o6.reference(machine_vision_amcm_objtypes.IPhysicalInterfaceType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5145"])
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5146",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6115",
                browseName="ns=machine_vision_amcm;ConnectorType",
                description="property denotes the type of connector for the physical interface (e.g., USB, Ethernet, etc.)",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
)
o6.reference(machine_vision_amcm_objtypes.IPhysicalInterfaceType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5146"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=machine_vision_amcm;i=6116",
    browseName="ns=machine_vision_amcm;MountType",
    description="is an enumeration using MultiStateDiscreteType that defines the mount type of the Lens",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6117",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[9],
                value=[
                    o6.LocalizedText("CUSTOM", "en"),
                    o6.LocalizedText("CS-MOUNT", "en"),
                    o6.LocalizedText("D-MOUNT", "en"),
                    o6.LocalizedText("A-MOUNT", "en"),
                    o6.LocalizedText("F-MOUNT", "en"),
                    o6.LocalizedText("T-MOUNT", "en"),
                    o6.LocalizedText("E-MOUNT", "en"),
                    o6.LocalizedText("EF-MOUNT", "en"),
                    o6.LocalizedText("V-MOUNT", "en"),
                ],
            )
        )
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5147",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6118",
                browseName="ns=machine_vision_amcm;LensType",
                description="type of the Lens. Examples are “Macro”, “Telecentric” and “Tilt-Shift”",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6119",
                browseName="ns=machine_vision_amcm;FocalLength",
                description="distance between the principal plane and the point where the light passing through the lens is focused and is given in millimeters",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6120",
                browseName="ns=machine_vision_amcm;Aperture",
                description="the current aperture set on the lens. Examples are “1.4” and “2.0”",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6121",
                browseName="ns=machine_vision_amcm;ModulationTransferFunction",
                description="is the ratio expressed as a percentage, between the actual contrast in the scene and the contrast transferred by the lens to the image at a given resolution",
                dataType=o6.Byte,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6122",
                browseName="ns=machine_vision_amcm;Resolution",
                description="the resolution that the lens is capable of (this is usually the catalog value). It is given in line pairs per millimeter (lp/mm) as the resolution would be determined with something like a 1951-USAF resolution target",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6123",
                browseName="ns=machine_vision_amcm;BackFocalLength",
                description="distance from the vertex of the last optical surface of the system to the rear focal point and is given in millimeters. This property should only exist when needed to provide additional system information such as to calculate the scheimpflug angle for tilted systems",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6124",
                browseName="ns=machine_vision_amcm;MinimumWorkingDistance",
                description="minimum object distance where you can still get a sharp image and is given in meters",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6125",
                browseName="ns=machine_vision_amcm;Magnification",
                description="relation between object size and image size. An example value of 1 will deliver a life-sized image. This property usually needs to be provided for Telecentric lenses only but might also be calculated for other lens types",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6126",
                browseName="ns=machine_vision_amcm;WorkingDistance",
                description="the current distance from the object to the lens and is given in meters",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6127",
                browseName="ns=machine_vision_amcm;OpticalFormat",
                description="denotes the maximum size of the sensor that the lens is suitable for (typically in inches)",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6116"]),
    ],
)
o6.reference(machine_vision_amcm_objtypes.ILensType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5147"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=machine_vision_amcm;i=6128",
    browseName="ns=machine_vision_amcm;LightingMode",
    description="denotes the current lighting mode of the lighting controller e.g. STROBE, CONTINUOUS, MODULATED, etc",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6129",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[3],
                value=[o6.LocalizedText("STROBE", "en"), o6.LocalizedText("CONTINUOUS", "en"), o6.LocalizedText("MODULATED", "en")],
            )
        )
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5148", browseName="ns=di;Maintenance", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6128"])]
)
o6.reference(machine_vision_amcm_objtypes.ILightingControllerType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5148"])
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5149",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6130",
                browseName="ns=machine_vision_amcm;LampType",
                description="represents the type of the lamp e.g., FLUORESCENT, LED, LASER or XENON",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6131",
                browseName="ns=machine_vision_amcm;Quality",
                description="the percentage of the lamp quality and represents the light degradation because of multiple factors including the environment or age. A new lamp can have a quality of 100",
                dataType=o6.Byte,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6132",
                browseName="ns=machine_vision_amcm;Wavelength",
                description="the wavelength of the light emitted by the lamp and is given in nanometers (nm)",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6133",
                browseName="ns=machine_vision_amcm;RelativeIntensity",
                description="amount of light emitted by the source as a percentage of the lamp total capability",
                dataType=o6.Byte,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6134",
                browseName="ns=machine_vision_amcm;WorkingDistance",
                description="current distance from the object to the lamp and is given in meters",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.ILampType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5149"])
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5150",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6135",
                browseName="ns=machine_vision_amcm;EndDate",
                description="end date of the license validity. If this property is set, the effects of not having a valid license are defined by the policy of the software or hardware provider",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6136",
                browseName="ns=machine_vision_amcm;StartDate",
                description="start date of the license validity. If this property is set, the effects of not having a valid license are defined by the policy of the software or hardware provider",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6137",
                browseName="ns=machine_vision_amcm;LicenseId",
                description="id that uniquely identifies the license for the software or hardware provider. It might be used for maintenance and/or support requests",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6138",
                browseName="ns=machine_vision_amcm;LicenseType",
                description="type of license based on the policy of the software of hardware provider e.g., runtime, trial, developer, support",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6139",
                browseName="ns=machine_vision_amcm;LicenseReference",
                description="a reference to a file on the system, documentation, or webpage where more information about the license can be obtained",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6140",
                browseName="ns=machine_vision_amcm;LicenseDescription",
                description="a short description of the license",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6141",
                browseName="ns=machine_vision_amcm;EnabledFeatures",
                description="a list of the enabled features by the license",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.ILicenseType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5150"])
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5154",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6113",
                browseName="ns=machine_vision_amcm;InputInUse",
                description="denotes the signal port for the display unit currently in use. This property could also be used from the vision system perspective to denote signal source for the display unit if multiple sources share the same display unit e.g., X1, X2 (as per the convention used in the DIN EN IEC 81346-2:2020-10 specification)",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6146",
                browseName="ns=machine_vision_amcm;InputSignalDetected",
                description="a flag that denotes if a signal is being detected in the InputInUse",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6147",
                browseName="ns=machine_vision_amcm;ResolutionInUse",
                description="denotes the pixel resolution in use (e.g., 1920x1080)",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionDisplayUnitType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5154"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5160",
    browseName="ns=machine_vision_amcm;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6148",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6149",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionHousingType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5160"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5162",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6150",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6151",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionImageSensorType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5162"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5165",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6152",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6153",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionLampType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5165"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5168",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6154",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6155",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionLensControllerType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5168"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5172",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6156",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6157",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionLensType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5172"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5173",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6158",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6159",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionLicenseType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5173"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5177",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6160",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6161",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionLightingControllerType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5177"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5181",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6162",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6163",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionAcquisitionBackgroundType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5181"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5182",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6164",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6165",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionCableType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5182"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5187",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6166",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6167",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionNetworkDeviceType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5187"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5188",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6168",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6169",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionOpticalFilterType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5188"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5193",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6170",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6171",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionOtherOpticalEquipmentType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5193"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5194",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6172",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6173",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionPatternGeneratorType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5194"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5198",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6174",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6175",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionPhysicalInterfaceType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5198"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5202",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6176",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6177",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionPowerSupplyType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5202"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5203",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6178",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6179",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionSurroundingEnvironmentType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5203"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5208",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6180",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6181",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionClimateControllerType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5208"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5209",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6182",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6183",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionTriggerSensorType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5209"])
machine_vision_amcm_objtypes.VisionComponentIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5214",
    browseName="ns=machine_vision_amcm;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6184",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6185",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionWayEncoderType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5214"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision_amcm;i=6190", browseName="ns=machine_vision_amcm;SEMI_E10SystemStateDataType", dataType=o6.String, value="SEMI_E10SystemStateDataType"
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5215"], "i=39", o6.ns["ns=machine_vision_amcm;i=6190"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision_amcm;i=6191",
    browseName="ns=machine_vision_amcm;SEMI_E10SystemStateDataType",
    dataType=o6.String,
    value="//xs:element[@name='SEMI_E10SystemStateDataType']",
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5216"], "i=39", o6.ns["ns=machine_vision_amcm;i=6191"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision_amcm;i=6192", browseName="ns=machine_vision_amcm;SEMI_E10SystemStateInfoDataType", dataType=o6.String, value="SEMI_E10SystemStateInfoDataType"
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5218"], "i=39", o6.ns["ns=machine_vision_amcm;i=6192"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=machine_vision_amcm;i=6186",
    browseName="ns=machine_vision_amcm;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/MachineVision/AMCM/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6187", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/MachineVision/AMCM/"
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6190"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6192"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/MachineVision/AMCM/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/MachineVision/AMCM/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="SEMI_E10SystemStateDataType">\n  <opc:Field TypeName="opc:Bit" Name="PrioritySpecified"/>\n  <opc:Field Length="31" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:UInt32" Name="Id"/>\n  <opc:Field SwitchField="PrioritySpecified" TypeName="opc:UInt32" Name="Priority"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="SEMI_E10SystemStateInfoDataType">\n  <opc:Field TypeName="opc:UInt32" Name="Id"/>\n  <opc:Field TypeName="ua:LocalizedText" Name="Name"/>\n  <opc:Field TypeName="opc:UInt32" Name="ParentStateId"/>\n  <opc:Field TypeName="ua:LocalizedText" Name="Description"/>\n </opc:StructuredType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision_amcm;i=6193",
    browseName="ns=machine_vision_amcm;SEMI_E10SystemStateInfoDataType",
    dataType=o6.String,
    value="//xs:element[@name='SEMI_E10SystemStateInfoDataType']",
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5219"], "i=39", o6.ns["ns=machine_vision_amcm;i=6193"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=machine_vision_amcm;i=6188",
    browseName="ns=machine_vision_amcm;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/MachineVision/AMCM/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6189", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/MachineVision/AMCM/Types.xsd"
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6191"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6193"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/MachineVision/AMCM/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/MachineVision/AMCM/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:complexType name="SEMI_E10SystemStateDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Id"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Priority"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:SEMI_E10SystemStateDataType" name="SEMI_E10SystemStateDataType"/>\n <xs:complexType name="ListOfSEMI_E10SystemStateDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SEMI_E10SystemStateDataType" name="SEMI_E10SystemStateDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSEMI_E10SystemStateDataType" name="ListOfSEMI_E10SystemStateDataType" nillable="true"/>\n <xs:complexType name="SEMI_E10SystemStateInfoDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Id"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="Name"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="ParentStateId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="Description"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:SEMI_E10SystemStateInfoDataType" name="SEMI_E10SystemStateInfoDataType"/>\n <xs:complexType name="ListOfSEMI_E10SystemStateInfoDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SEMI_E10SystemStateInfoDataType" name="SEMI_E10SystemStateInfoDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSEMI_E10SystemStateInfoDataType" name="ListOfSEMI_E10SystemStateInfoDataType" nillable="true"/>\n</xs:schema>\n',
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6194",
    browseName="ns=machine_vision_amcm;SubStates",
    description="recursive SEMI_E10SystemStateType to specify the next level of the sub states of the state store on the variable. It is possible to provide any number of levels to completely map all the SEMI E10 states of an item",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6197",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-3,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machine_vision_amcm_vartypes.SEMI_E10SystemStateType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=6194"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6200",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6201", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5003",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6014",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6015",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6211",
                browseName="ns=di;AssetId",
                description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6212",
                browseName="ns=di;ComponentName",
                description="To be used by end users to store a human-readable localized text for the MachineryItem. The minimum number of locales supported for this property shall be two. Servers shall support at least 40 Unicode characters for the clients writing the text part of each locale, this means clients can expect to be able to write texts with a length of 40 Unicode characters into that field.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6213",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose the MachineryItem is used.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6214",
                browseName="ns=di;HardwareRevision",
                description="A string representation of the revision level of the hardware of a MachineryItem. Hardware is physical equipment, as opposed to programs, procedures, rules and associated documentation. Many machines will not provide such information due to the modular and configurable nature of the machine.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6215",
                browseName="ns=machinery;InitialOperationDate",
                description="The date, when the MachineryItem was switched on the first time after it has left the manufacturer plant.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6216",
                browseName="ns=di;ManufacturerUri",
                description="A globally unique identifier of the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6217",
                browseName="ns=di;Model",
                description="A human-readable, localized name of the model of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6218",
                browseName="ns=machinery;MonthOfConstruction",
                description="The month in which the manufacturing process of the MachineryItem has been completed. It shall be a number between 1 and 12, representing the month from January to December.",
                dataType=o6.Byte,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6219",
                browseName="ns=di;ProductCode",
                description="A machine-readable string of the model of the MachineryItem, that might include options like the hardware configuration of the model. This information might be provided by the ERP system of the vendor. For example, it can be used as order information.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6220",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6221",
                browseName="ns=di;SoftwareRevision",
                description="A string representation of the revision level of a MachineryItem. In most cases, MachineryItems consist of several software components. In that case, information about the software components might be provided as additional information in the address space, including individual revision information. In that case, this property is either not provided or provides an overall software revision level. The value might change during the life-cycle of a MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6222",
                browseName="ns=machinery;YearOfConstruction",
                description="The year (Gregorian calendar) in which the manufacturing process of the MachineryItem has been completed. It shall be a four-digit number and never change during the life-cycle of a MachineryItem.",
                dataType=o6.UInt16,
            )
        ),
    ],
    _allow_abstract=True,
)
o6.reference(machine_vision_amcm_objtypes.IVisionInfoType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5003"])
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6013",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6223",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machine_vision_amcm_objtypes.VisionHealthInfoType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=6013"])
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6199",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6224",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=machine_vision_amcm;i=6226",
    browseName="ns=machine_vision_amcm;MountType",
    description="an enumeration using MultiStateDiscreteType that defines the mount type of the Lens",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6227",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[9],
                value=[
                    o6.LocalizedText("CUSTOM", "en"),
                    o6.LocalizedText("CS-MOUNT", "en"),
                    o6.LocalizedText("D-MOUNT", "en"),
                    o6.LocalizedText("A-MOUNT", "en"),
                    o6.LocalizedText("F-MOUNT", "en"),
                    o6.LocalizedText("T-MOUNT", "en"),
                    o6.LocalizedText("E-MOUNT", "en"),
                    o6.LocalizedText("EF-MOUNT", "en"),
                    o6.LocalizedText("V-MOUNT", "en"),
                ],
            )
        )
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5171",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6228",
                browseName="ns=machine_vision_amcm;LensType",
                description="the type of the Lens. Examples are “Macro”, “Telecentric” and “Tilt-Shift”",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6229",
                browseName="ns=machine_vision_amcm;FocalLength",
                description="distance between the principal plane and the point where the light passing through the lens is focused and is given in millimeters",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6230",
                browseName="ns=machine_vision_amcm;Aperture",
                description="the current aperture set on the lens. Examples are “1.4” and “2.0”.",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6231",
                browseName="ns=machine_vision_amcm;ModulationTransferFunction",
                description="the ratio expressed as a percentage, between the actual contrast in the scene and the contrast transferred by the lens to the image at a given resolution",
                dataType=o6.Byte,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6232",
                browseName="ns=machine_vision_amcm;Resolution",
                description="the resolution that the lens is capable of (this is usually the catalog value). It is given in line pairs per millimeter (lp/mm) as the resolution would be determined with something like a 1951-USAF resolution target.",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6233",
                browseName="ns=machine_vision_amcm;BackFocalLength",
                description="distance from the vertex of the last optical surface of the system to the rear focal point and is given in millimeters. This property should only exist when needed to provide additional system information such as to calculate the scheimpflug angle for tilted systems",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6234",
                browseName="ns=machine_vision_amcm;MinimumWorkingDistance",
                description="the minimum object distance where you can still get a sharp image and is given in meters",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6235",
                browseName="ns=machine_vision_amcm;Magnification",
                description="the relation between object size and image size. An example value of 1 will deliver a life-sized image. This property usually needs to be provided for Telecentric lenses only but might also be calculated for other lens types",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6236",
                browseName="ns=machine_vision_amcm;WorkingDistance",
                description="current distance from the object to the lens and is given in meters",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6237",
                browseName="ns=machine_vision_amcm;OpticalFormat",
                description="denotes the maximum size of the sensor that the lens is suitable for (typically in inches)",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6226"]),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionLensType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5171"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=machine_vision_amcm;i=6238",
    browseName="ns=machine_vision_amcm;LightingMode",
    description="denotes the current lighting mode of the lighting controller e.g. STROBE, CONTINUOUS, MODULATED, etc",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6239",
                browseName="EnumStrings",
                dataType=o6.LocalizedText,
                valueRank=1,
                arrayDimensions=[3],
                value=[o6.LocalizedText("STROBE", "en"), o6.LocalizedText("CONTINUOUS", "en"), o6.LocalizedText("MODULATED", "en")],
            )
        )
    ],
    dataType=o6.UInt32,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5176", browseName="ns=di;Maintenance", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6238"])]
)
o6.reference(machine_vision_amcm_objtypes.VisionLightingControllerType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5176"])
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5164",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6240",
                browseName="ns=machine_vision_amcm;LampType",
                description="represents the type of the lamp e.g., FLUORESCENT, LED, LASER or XENON",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6241",
                browseName="ns=machine_vision_amcm;Quality",
                description="the percentage of the lamp quality and represents the light degradation because of multiple factors including the environment or age. A new lamp can have a quality of 100",
                dataType=o6.Byte,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6242",
                browseName="ns=machine_vision_amcm;Wavelength",
                description="the wavelength of the light emitted by the lamp and is given in nanometers (nm).",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6243",
                browseName="ns=machine_vision_amcm;RelativeIntensity",
                description="amount of light emitted by the source as a percentage of the lamp total capability",
                dataType=o6.Byte,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6244",
                browseName="ns=machine_vision_amcm;WorkingDistance",
                description="current distance from the object to the lamp and is given in meters",
                dataType=o6.Double,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionLampType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5164"])
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5174",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6245",
                browseName="ns=machine_vision_amcm;EndDate",
                description="end date of the license validity. If this property is set, the effects of not having a valid license are defined by the policy of the software or hardware provider",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6246",
                browseName="ns=machine_vision_amcm;StartDate",
                description="start date of the license validity. If this property is set, the effects of not having a valid license are defined by the policy of the software or hardware provider",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6247",
                browseName="ns=machine_vision_amcm;LicenseId",
                description="id that uniquely identifies the license for the software or hardware provider. It might be used for maintenance and/or support requests",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6248",
                browseName="ns=machine_vision_amcm;LicenseType",
                description="type of license based on the policy of the software of hardware provider e.g., runtime, trial, developer, support",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6249",
                browseName="ns=machine_vision_amcm;LicenseReference",
                description="a reference to a file on the system, documentation, or webpage where more information about the license can be obtained",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6250",
                browseName="ns=machine_vision_amcm;LicenseDescription",
                description="a short description of the license",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6251",
                browseName="ns=machine_vision_amcm;EnableFeatures",
                description="a list of the enabled features by the license",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionLicenseType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5174"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6143",
    browseName="ns=machine_vision_amcm;Diameter",
    description="denotes the outer diameter of the cable in millimeters",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6252",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5066068,
                    displayName=o6.LocalizedText("mm", "en"),
                    description=o6.LocalizedText("millimetre", "en"),
                ),
            )
        )
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6142",
    browseName="ns=machine_vision_amcm;Length",
    description="denotes the length of the cable in meters",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6253",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5067858,
                    displayName=o6.LocalizedText("m", "en"),
                    description=o6.LocalizedText("metre", "en"),
                ),
            )
        )
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5151",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6144",
                browseName="ns=machine_vision_amcm;Shielding",
                description="denotes the description of shielding on the cable",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6145",
                browseName="ns=machine_vision_amcm;Connectors",
                description="denotes the connectors that the cable supports USB-A Female, Hirose 6-pin male",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6142"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6143"]),
    ],
)
o6.reference(machine_vision_amcm_objtypes.ICableType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5151"])
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6067",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6260",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6261",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6262", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6274",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6275",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6276",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6277", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5180",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6278",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6279",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6281",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6282",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6284",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6285",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6287",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionAcquisitionBackgroundType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5180"])
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6289",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6290",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6291",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6292", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5223",
    browseName="ns=di;Identification",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6303",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6304",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6306",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6307",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6308",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6309", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6321",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6322",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6323",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6324", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6336",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6337",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6338",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6339", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5207",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6340",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6341",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6343",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6344",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6346",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6347",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6349",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionClimateControllerType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5207"])
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6351",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6352",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6353",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6354", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6010",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6348",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6350",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6357", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machine_vision_amcm_objtypes.VisionHealthInfoType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=6010"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6198",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6360", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6363",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6365",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6366",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6367",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6368",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6369", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6066",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6372", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6375",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6378",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6381",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6382",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6383",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6384", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6320",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6380", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6387",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6390",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6396",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6397",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6398",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6399", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6288",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6393", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6395",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6400",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6401",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6402",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6403",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6404", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6327",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6407", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6410",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6413",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6416",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6417",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6418",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6419", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6330",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6415", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6422",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6425",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6431",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6432",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6433",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6434", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6273",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6428", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6430",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6437",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5179",
    browseName="ns=machine_vision_amcm;Health",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5110",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6273"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6274"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6276"]),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionAcquisitionBackgroundType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5179"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6333",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6440", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6443",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6445",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6446",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6447",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6448",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6449", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6335",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6452", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6455",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6458",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5206",
    browseName="ns=machine_vision_amcm;Health",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5228",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6335"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6336"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6338"]),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionClimateControllerType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5206"])
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6461",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6462",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6463",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6464", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6342",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6460", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6467",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6470",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6476",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6477",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6478",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6479", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6345",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6473", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6475",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6482",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6305",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6485", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6488",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6490",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6491",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6492",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6493",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6494", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5002",
    browseName="ns=machine_vision_amcm;Health",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5255",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6198"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6199"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6200"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6500",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.IVisionInfoType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5002"])
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6506",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6507",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6508",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6509", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5008",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5109",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6066"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6067"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6261"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6512",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5007",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6263",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6264",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6266",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6267",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6269",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6270",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6272",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6515",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5260", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5004",
    browseName="ns=machine_vision_amcm;<VisionItem>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5006"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5007"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5008"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionItemFolderType, ns0.reftypes.Organizes, o6.ns["ns=machine_vision_amcm;i=5004"])
o6.reference(o6.ns["ns=machine_vision_amcm;i=5004"], "i=17603", machine_vision_amcm_objtypes.IVisionInfoType)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5224",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5226",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6305"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6306"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6308"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6518",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5126",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6355",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6356",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6358",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6359",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6361",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6362",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6364",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6522",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5263", browseName="ns=di;OperationCounters")),
    ],
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6531",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6532",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6533",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6534", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6537",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6540", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6543",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6545",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5064",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5230",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6366"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6368"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6530",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6537"]),
    ],
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6546",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6547",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6548",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6549", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5066",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6370",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6371",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6373",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6374",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6376",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6377",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6379",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6552",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5264", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5011",
    browseName="ns=machine_vision_amcm;<ComputingDevice>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5064"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5065"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5066"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5011"], "i=17603", machine_vision_amcm_objtypes.IComputingDeviceType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5010",
    browseName="ns=machine_vision_amcm;ComputingDevices",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5011"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5010"])
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6561",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6562",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6563",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6564", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5136",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5111",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6288"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6289"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6291"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6575",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6576",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6577",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6578",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6579", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6567",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6570", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6582",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6585",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5067",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5231",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6381"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6383"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6560",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6567"]),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5069",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6385",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6386",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6388",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6389",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6391",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6392",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6394",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6588",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5265", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5013",
    browseName="ns=machine_vision_amcm;<DisplayUnit>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5067"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5068"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5069"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5013"], "i=17603", machine_vision_amcm_objtypes.IDisplayUnitType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5012",
    browseName="ns=machine_vision_amcm;DisplayUnits",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5013"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5012"])
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6591",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6592",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6593",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6594", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6606",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6607",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6608",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6609", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6603",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6605", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6612",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6615",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5076",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5233",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6401"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6403"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6600",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6603"]),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5078",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6405",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6406",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6408",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6409",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6411",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6412",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6414",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6618",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5266", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5019",
    browseName="ns=machine_vision_amcm;<FrameGrabber>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5076"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5077"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5078"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5019"], "i=17603", machine_vision_amcm_objtypes.IVisionInfoType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5018",
    browseName="ns=machine_vision_amcm;FrameGrabbers",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5019"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5018"])
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6621",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6622",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6623",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6624", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5063",
    browseName="ns=machine_vision_amcm;Health",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5232",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6320"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6396"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6398"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6630",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5063"])
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6636",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6637",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6638",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6639", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6635",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6642", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6645",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6648",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5106",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5227",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6321"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6323"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6633",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6635"]),
    ],
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6651",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6652",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6653",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6654", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6657",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6660", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6663",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6665",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5115",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5234",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6416"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6418"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6650",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6657"]),
    ],
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6666",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6667",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6668",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6669", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5117",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6420",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6421",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6423",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6424",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6426",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6427",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6429",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6672",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5267", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5045",
    browseName="ns=machine_vision_amcm;<Housing>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5115"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5116"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5117"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5045"], "i=17603", machine_vision_amcm_objtypes.IVisionInfoType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5044",
    browseName="ns=machine_vision_amcm;Housings",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5045"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5044"])
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6681",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6682",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6683",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6684", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6696",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6697",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6698",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6699", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5211",
    browseName="ns=machine_vision_amcm;Health",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5252",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6342"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6696"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6698"]),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionTriggerSensorType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5211"])
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5108",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6325",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6326",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6328",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6329",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6331",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6332",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6334",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6705",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5262", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5039",
    browseName="ns=machine_vision_amcm;<CalibrationTarget>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5106"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5107"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5108"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5039"], "i=17603", machine_vision_amcm_objtypes.IVisionInfoType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5038",
    browseName="ns=machine_vision_amcm;CalibrationTargets",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5039"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5038"])
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5210",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6700",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6701",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6703",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6704",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6706",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6707",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6709",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionTriggerSensorType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5210"])
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6711",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6712",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6713",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6714", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5213",
    browseName="ns=machine_vision_amcm;Health",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5253",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6345"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6711"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6713"]),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionWayEncoderType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5213"])
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5212",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6715",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6716",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6718",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6719",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6721",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6722",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6724",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionWayEncoderType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5212"])
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6726",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6727",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6728",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6729", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5184",
    browseName="ns=machine_vision_amcm;Health",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5254",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6333"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6726"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6728"]),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionCableType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5184"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6720",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6723", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6725",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6732",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5124",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5229",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6351"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6353"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6717",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6720"]),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5051",
    browseName="ns=machine_vision_amcm;<ClimateController>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5124"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5125"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5126"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5051"], "i=17603", machine_vision_amcm_objtypes.IVisionInfoType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5050",
    browseName="ns=machine_vision_amcm;ClimateControllers",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5051"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5050"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6735",
    browseName="ns=machine_vision_amcm;Diameter",
    description="denotes the outer diameter of the cable in millimeters",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6736",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5066068,
                    displayName=o6.LocalizedText("mm", "en"),
                    description=o6.LocalizedText("millimetre", "en"),
                ),
            )
        )
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6737",
    browseName="ns=machine_vision_amcm;Length",
    description="denotes the length of the cable in meters",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6738",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5067858,
                    displayName=o6.LocalizedText("m", "en"),
                    description=o6.LocalizedText("metre", "en"),
                ),
            )
        )
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5183",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6254",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6255",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6257",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6258",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6730",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6731",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6733",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6734",
                browseName="ns=machine_vision_amcm;Connectors",
                description="denotes the connectors that the cable supports e.g. USB-A Female, Hirose 6-pin male",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6739",
                browseName="ns=machine_vision_amcm;Shielding",
                description="denotes the description of shielding on the cable",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6735"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6737"]),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionCableType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5183"])
machine_vision_amcm_objtypes.VisionMachineIdentificationType(
    nodeId="ns=machine_vision_amcm;i=5061",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6033",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6034",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6035",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6680",
                browseName="ns=di;AssetId",
                description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
                dataType=o6.String,
                value="",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6687",
                browseName="ns=di;ComponentName",
                description="To be used by end users to store a human-readable localized text for the MachineryItem. The minimum number of locales supported for this property shall be two. Servers shall support at least 40 Unicode characters for the clients writing the text part of each locale, this means clients can expect to be able to write texts with a length of 40 Unicode characters into that field.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText(),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6690",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose the MachineryItem is used.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6693",
                browseName="ns=di;HardwareRevision",
                description="provides the revision level of the hardware of the machine vision system following the rules of Sematic Versioning 2.0.0",
                dataType=ns0.datatypes.SemanticVersionString,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6695",
                browseName="ns=machinery;InitialOperationDate",
                description="The date, when the MachineryItem was switched on the first time after it has left the manufacturer plant.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6702",
                browseName="ns=machinery;Location",
                description="To be used by end users to store the location of the machine in a scheme specific to the end user. Servers shall support at least 60 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 60 Unicode characters into that field.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6740",
                browseName="ns=di;ManufacturerUri",
                description="A globally unique identifier of the manufacturer of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6741",
                browseName="ns=di;Model",
                description="A human-readable, localized name of the model of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6742",
                browseName="ns=machine_vision_amcm;ConfigurationCode",
                description="provides the specific information how the machine vision system has been configured for a specific use case or application",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6743",
                browseName="ns=machinery;MonthOfConstruction",
                description="The month in which the manufacturing process of the MachineryItem has been completed. It shall be a number between 1 and 12, representing the month from January to December.",
                dataType=o6.Byte,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6744",
                browseName="ns=di;ProductCode",
                description="A machine-readable string of the model of the MachineryItem, that might include options like the hardware configuration of the model. This information might be provided by the ERP system of the vendor. For example, it can be used as order information.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6745",
                browseName="ns=di;SoftwareRevision",
                description="property provides the version or revision level of the software in the machine vision system following the rules of Semantic Versioning 2.0.0.",
                dataType=ns0.datatypes.SemanticVersionString,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6746",
                browseName="ns=machinery;YearOfConstruction",
                description="The year (Gregorian calendar) in which the manufacturing process of the MachineryItem has been completed. It shall be a four-digit number and never change during the life-cycle of a MachineryItem.",
                dataType=o6.UInt16,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5061"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6748",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6749", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6750",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6751",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5073",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5235",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6431"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6433"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6747",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6748"]),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5075",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6435",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6436",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6438",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6439",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6441",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6442",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6444",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6752",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5268", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5017",
    browseName="ns=machine_vision_amcm;<ImageSensor>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5073"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5074"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5075"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5017"], "i=17603", machine_vision_amcm_objtypes.IVisionInfoType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5016",
    browseName="ns=machine_vision_amcm;ImageSensors",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5017"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5016"])
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6757",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6758",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6759",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6760", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6762",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6763",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6764",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6765", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5157",
    browseName="ns=machine_vision_amcm;Health",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5257",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6330"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6762"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6764"]),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionFrameGrabberType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5157"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6756",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6761", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6766",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6782",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5097",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5236",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6446"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6448"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6755",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6756"]),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5099",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6450",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6451",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6453",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6454",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6456",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6457",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6459",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6798",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5269", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5033",
    browseName="ns=machine_vision_amcm;<Lamp>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5097"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5098"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5099"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5033"], "i=17603", machine_vision_amcm_objtypes.ILampType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5032", browseName="ns=machine_vision_amcm;Lamps", modellingRule="Optional", references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5033"])]
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5032"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6802",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6803", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6804",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6805",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5082",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5237",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6461"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6463"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6801",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6802"]),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5084",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6465",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6466",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6468",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6469",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6471",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6472",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6474",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6806",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5270", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5023",
    browseName="ns=machine_vision_amcm;<LensController>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5082"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5083"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5084"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5023"], "i=17603", machine_vision_amcm_objtypes.IVisionInfoType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5022",
    browseName="ns=machine_vision_amcm;LensControllers",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5023"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5022"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6810",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6811", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6812",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6813",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5079",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5238",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6476"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6478"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6809",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6810"]),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5081",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6480",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6481",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6483",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6484",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6486",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6487",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6489",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6814",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5271", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5021",
    browseName="ns=machine_vision_amcm;<Lens>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5079"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5080"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5081"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5021"], "i=17603", machine_vision_amcm_objtypes.ILensType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5020", browseName="ns=machine_vision_amcm;Lenses", modellingRule="Optional", references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5021"])]
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5020"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6818",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6819", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6820",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6821",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5127",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5239",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6491"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6493"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6817",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6818"]),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5129",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6495",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6496",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6498",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6499",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6501",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6502",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6504",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6822",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5272", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5053",
    browseName="ns=machine_vision_amcm;<License>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5127"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5128"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5129"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5053"], "i=17603", machine_vision_amcm_objtypes.ILicenseType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5052",
    browseName="ns=machine_vision_amcm;Licenses",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5053"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5052"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6826",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6827", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6828",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6829",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5100",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5240",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6506"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6508"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6825",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6826"]),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5102",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6510",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6511",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6513",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6514",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6516",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6517",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6519",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6830",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5273", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5035",
    browseName="ns=machine_vision_amcm;<LightingController>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5100"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5101"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5102"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5035"], "i=17603", machine_vision_amcm_objtypes.ILightingControllerType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5034",
    browseName="ns=machine_vision_amcm;LightingControllers",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5035"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5034"])
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5062",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6520",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6521",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6523",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6524",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6526",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6527",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6529",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6833",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5274", browseName="ns=di;OperationCounters")),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5062"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6835",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6836", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6837",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6838",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5118",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5241",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6531"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6533"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6834",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6835"]),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5120",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6535",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6536",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6538",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6539",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6541",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6542",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6544",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6839",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5275", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5047",
    browseName="ns=machine_vision_amcm;<MotionDevice>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5118"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5119"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5120"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5047"], "i=17603", machine_vision_amcm_objtypes.IVisionInfoType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5046",
    browseName="ns=machine_vision_amcm;MotionDevices",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5047"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5046"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6843",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6844", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6845",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6846",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5133",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5242",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6546"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6548"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6842",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6843"]),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5135",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6550",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6551",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6553",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6554",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6556",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6557",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6559",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6847",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5276", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5057",
    browseName="ns=machine_vision_amcm;<NetworkDevice>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5133"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5134"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5135"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5057"], "i=17603", machine_vision_amcm_objtypes.IVisionInfoType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5056",
    browseName="ns=machine_vision_amcm;NetworkDevices",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5057"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5056"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6851",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6852", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6853",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6854",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5085",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5243",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6561"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6563"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6850",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6851"]),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5087",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6565",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6566",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6568",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6569",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6571",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6572",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6574",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6855",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5277", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5025",
    browseName="ns=machine_vision_amcm;<OpticalFilter>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5085"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5086"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5087"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5025"], "i=17603", machine_vision_amcm_objtypes.IVisionInfoType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5024",
    browseName="ns=machine_vision_amcm;OpticalFilters",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5025"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5024"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6859",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6860", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6861",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6862",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5088",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5244",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6576"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6578"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6858",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6859"]),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5090",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6580",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6581",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6583",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6584",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6586",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6587",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6589",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6863",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5278", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5027",
    browseName="ns=machine_vision_amcm;<OtherOpticalEquipment>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5088"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5089"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5090"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5027"], "i=17603", machine_vision_amcm_objtypes.IVisionInfoType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5026",
    browseName="ns=machine_vision_amcm;OtherOpticalEquipments",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5027"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5026"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6867",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6868", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6869",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6870",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5103",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5245",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6591"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6593"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6866",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6867"]),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5105",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6595",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6596",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6598",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6599",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6601",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6602",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6604",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6871",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5279", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5037",
    browseName="ns=machine_vision_amcm;<PatternGenerator>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5103"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5104"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5105"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5037"], "i=17603", machine_vision_amcm_objtypes.IVisionInfoType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5036",
    browseName="ns=machine_vision_amcm;PatternGenerators",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5037"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5036"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6875",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6876", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6877",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6878",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5070",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5246",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6606"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6608"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6874",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6875"]),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5072",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6610",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6611",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6613",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6614",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6616",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6617",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6619",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6879",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5280", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5015",
    browseName="ns=machine_vision_amcm;<PhysicalInterface>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5070"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5071"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5072"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5015"], "i=17603", machine_vision_amcm_objtypes.IPhysicalInterfaceType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5014",
    browseName="ns=machine_vision_amcm;PhysicalInterfaces",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5015"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5014"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6883",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6884", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6885",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6886",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5121",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5247",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6621"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6623"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6882",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6883"]),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5123",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6625",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6626",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6628",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6629",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6631",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6632",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6634",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6887",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5281", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5049",
    browseName="ns=machine_vision_amcm;<PowerSupply>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5121"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5122"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5123"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5049"], "i=17603", machine_vision_amcm_objtypes.IVisionInfoType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5048",
    browseName="ns=machine_vision_amcm;PowerSupplies",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5049"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5048"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6891",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6892", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6893",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6894",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5130",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5248",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6636"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6638"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6890",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6891"]),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5132",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6640",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6641",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6643",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6644",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6646",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6647",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6649",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6895",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5282", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5055",
    browseName="ns=machine_vision_amcm;<Software>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5130"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5131"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5132"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5055"], "i=17603", machine_vision_amcm_objtypes.IVisionInfoType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5054",
    browseName="ns=machine_vision_amcm;SoftwareComponents",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5055"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5054"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6899",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6900", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6901",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6902",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5112",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5249",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6651"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6653"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6898",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6899"]),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5114",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6655",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6656",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6658",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6659",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6661",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6662",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6664",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6903",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5283", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5043",
    browseName="ns=machine_vision_amcm;<SurroundingEnvironment>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5112"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5113"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5114"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5043"], "i=17603", machine_vision_amcm_objtypes.IVisionInfoType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5042",
    browseName="ns=machine_vision_amcm;SurroundingEnvironment",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5043"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5042"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6907",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6908", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6909",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6910",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5094",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5250",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6666"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6668"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6906",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6907"]),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5096",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6670",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6671",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6673",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6674",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6676",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6677",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6679",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6911",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5284", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5031",
    browseName="ns=machine_vision_amcm;<TriggerSensor>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5094"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5095"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5096"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5031"], "i=17603", machine_vision_amcm_objtypes.IVisionInfoType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5030",
    browseName="ns=machine_vision_amcm;TriggerSensors",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5031"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5030"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6915",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6916", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6917",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6918",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5091",
    browseName="ns=machine_vision_amcm;Health",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5251",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6681"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6683"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6914",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6915"]),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5093",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6685",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6686",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6688",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6689",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6691",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6692",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6694",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6919",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5285", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5029",
    browseName="ns=machine_vision_amcm;<WayEncoder>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5091"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5092"]), o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5093"])],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5029"], "i=17603", machine_vision_amcm_objtypes.IVisionInfoType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5028",
    browseName="ns=machine_vision_amcm;WayEncoders",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5029"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5028"])
machinery.objtypes.MachineryOperationCounterType(
    nodeId="ns=machine_vision_amcm;i=5261",
    browseName="ns=di;OperationCounters",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6922",
                browseName="ns=di;OperationCycleCounter",
                description="OperationCycleCounter is counting the times the component switches from not performing an activity to performing an activity. For example, each time a valve starts moving, is counted. This value shall only increase during the lifetime of the component and shall not be reset when the component is restarted.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6923",
                browseName="ns=di;OperationDuration",
                description="OperationDuration is the duration the MachineryItem has been powered and performing an activity. This counter is intended for machines and components where a distinction is made between switched on and in operation. For example, a drive might be powered on but not operating. It is not intended for machines or components always performing an activity like sensors always measuring data. This value shall only increase during the lifetime of the MachineryItem and shall not be reset when it is restarted. The OperationDuration is provided as Duration, i.e., in milliseconds or even fractions of a millisecond. However, the Server is not expected to update the value in such a high frequency, but maybe once a minute or once an hour, depending on the application.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6924",
                browseName="ns=di;PowerOnDuration",
                description="PowerOnDuration is the duration the MachineryItem has been powered. The main purpose is to determine the time in which degradation of the MachineryItem occurred. The details, when the time is counted, is implementation-specific. Companion specifications might define specific rules. Typically, when the MachineryItem has supply voltage and the main CPU is running, the time is counted. This may include any kind of sleep mode, but may not include pure Wake on LAN. This value shall only increase during the lifetime of the MachineryItem and shall not be reset when it is restarted. The PowerOnDuration is provided as Duration, i.e., in milliseconds or even fractions of a millisecond. However, the Server is not expected to update the value in such a high frequency, but maybe once a minute or once an hour, depending on the application.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5225",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6310",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6311",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6313",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6314",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6316",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6317",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6319",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6573",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5261"]),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5041",
    browseName="ns=machine_vision_amcm;<AcquisitionBackground>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=5223"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=5224"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=5225"]),
    ],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5041"], "i=17603", machine_vision_amcm_objtypes.IVisionInfoType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5040",
    browseName="ns=machine_vision_amcm;AcquisitionBackgrounds",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5041"])],
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5040"])
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5138",
    browseName="ns=di;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6293",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6294",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6296",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6297",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6299",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6300",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6302",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6925",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=machine_vision_amcm;i=5286", browseName="ns=di;OperationCounters")),
    ],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machine_vision_amcm;i=5059",
    browseName="ns=machine_vision_amcm;<Cable>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=5136"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=5137"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=5138"]),
    ],
)
o6.reference(o6.ns["ns=machine_vision_amcm;i=5059"], "i=17603", machine_vision_amcm_objtypes.ICableType)
machine_vision_amcm_objtypes.VisionItemFolderType(
    nodeId="ns=machine_vision_amcm;i=5058", browseName="ns=machine_vision_amcm;Cables", modellingRule="Optional", references=[o6.organizes(o6.ns["ns=machine_vision_amcm;i=5059"])]
)
o6.reference(machine_vision_amcm_objtypes.VisionSystemAssetType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision_amcm;i=5058"])
machinery.objtypes.MachineryOperationCounterType(
    nodeId="ns=machine_vision_amcm;i=5259",
    browseName="ns=di;OperationCounters",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6926",
                browseName="ns=di;OperationCycleCounter",
                description="OperationCycleCounter is counting the times the component switches from not performing an activity to performing an activity. For example, each time a valve starts moving, is counted. This value shall only increase during the lifetime of the component and shall not be reset when the component is restarted.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6927",
                browseName="ns=di;OperationDuration",
                description="OperationDuration is the duration the MachineryItem has been powered and performing an activity. This counter is intended for machines and components where a distinction is made between switched on and in operation. For example, a drive might be powered on but not operating. It is not intended for machines or components always performing an activity like sensors always measuring data. This value shall only increase during the lifetime of the MachineryItem and shall not be reset when it is restarted. The OperationDuration is provided as Duration, i.e., in milliseconds or even fractions of a millisecond. However, the Server is not expected to update the value in such a high frequency, but maybe once a minute or once an hour, depending on the application.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6928",
                browseName="ns=di;PowerOnDuration",
                description="PowerOnDuration is the duration the MachineryItem has been powered. The main purpose is to determine the time in which degradation of the MachineryItem occurred. The details, when the time is counted, is implementation-specific. Companion specifications might define specific rules. Typically, when the MachineryItem has supply voltage and the main CPU is running, the time is counted. This may include any kind of sleep mode, but may not include pure Wake on LAN. This value shall only increase during the lifetime of the MachineryItem and shall not be reset when it is restarted. The PowerOnDuration is provided as Duration, i.e., in milliseconds or even fractions of a millisecond. However, the Server is not expected to update the value in such a high frequency, but maybe once a minute or once an hour, depending on the application.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
machine_vision_amcm_objtypes.VisionMaintenanceInfoType(
    nodeId="ns=machine_vision_amcm;i=5001",
    browseName="ns=di;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6202",
                browseName="ns=machine_vision_amcm;CalibrationNeeded",
                description="a flag that if True denotes that the item needs calibration",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6204",
                browseName="ns=machine_vision_amcm;LastCalibration",
                description="denotes the time when the previous calibration was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6205",
                browseName="ns=machine_vision_amcm;MaintenanceRecord",
                description="provides the most recent note that was recorded while performing maintenance. This property can be historized if a history of previous maintenance notes is to be made available",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6207",
                browseName="ns=machine_vision_amcm;NextCalibration",
                description="denotes the planned time when the next calibration is to be carried out on the item.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6208",
                browseName="ns=machine_vision_amcm;NextService",
                description="denotes the planned moment in time when the next service is to be carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6210",
                browseName="ns=machine_vision_amcm;StartOfWarranty",
                description="denotes the beginning of the warranty period of the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6503",
                browseName="ns=machine_vision_amcm;FirmwareInfo",
                description="denotes the information about the firmware of the Item",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6505",
                browseName="ns=machine_vision_amcm;LastService",
                description="denotes the last moment in time when the most recent service was carried out on the item",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6030"]),
        o6.hasAddIn(o6.ns["ns=machine_vision_amcm;i=5259"]),
    ],
)
o6.reference(machine_vision_amcm_objtypes.IVisionInfoType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5001"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machine_vision_amcm;i=6930",
    browseName="ns=machine_vision_amcm;RemainingLifeTime",
    description="denotes the remaining lifetime of the item. It serves as an indication to service personnel for maintenance activities",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6931", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6932",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6933",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_vartypes.SEMI_E10SystemStateType(
    nodeId="ns=machine_vision_amcm;i=6934",
    browseName="ns=machine_vision_amcm;State",
    description="denotes the SEMI E10 State of the item",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6935",
                browseName="ns=machine_vision_amcm;StatesInfo",
                description="mandatory property of all the states that can be assigned to the level of variable",
                dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateInfoDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    dataType=machine_vision_amcm_datypes.SEMI_E10SystemStateDataType,
    valueRank=-1,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=machine_vision_amcm;i=6936",
    browseName="ns=machine_vision_amcm;Temperature",
    description="denotes the temperature value (along with its unit) of the item",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision_amcm;i=6937", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5139",
    browseName="ns=machine_vision_amcm;Health",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6086",
                browseName="ns=machine_vision_amcm;BatteryState",
                description="denotes overall information about the condition of the battery or batteries",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6087",
                browseName="ns=machine_vision_amcm;CCUState",
                description="denotes information about the set of drivers being used by the computing device",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6089",
                browseName="ns=machine_vision_amcm;MassStorageState",
                description="denotes overall information about the condition of the mass storage e.g., specific drives or RAID arrays etc",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6090",
                browseName="ns=machine_vision_amcm;PatchLevel",
                description="denotes the patch level or patch set. When patches must be applied in order, it is usually an identifier of the most recent patch applied to the system",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision_amcm;i=6091",
                browseName="ns=machine_vision_amcm;RAMState",
                description="denotes overall information about the condition of the RAM (e.g., there are systems using ECC enabled RAM that can provide information about the health state of the RAM modules)",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5287",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6929",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6930"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6934"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6936"]),
    ],
)
o6.reference(machine_vision_amcm_objtypes.IComputingDeviceType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5139"])
machine_vision_amcm_objtypes.VisionHealthInfoType(
    nodeId="ns=machine_vision_amcm;i=5152",
    browseName="ns=machine_vision_amcm;Health",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=machine_vision_amcm;i=5256",
                browseName="ns=di;DeviceHealthAlarms",
                description="folder to organize the Alarms and Conditions related to the item if these Alarms and Conditions are instantiated in the address space",
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6327"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6757"]),
        o6.hasComponent(o6.ns["ns=machine_vision_amcm;i=6759"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision_amcm;i=6938",
                browseName="ns=di;DeviceHealth",
                description="indicates the status as defined by NAMUR Recommendation NE107. The DeviceHealthEnumeration DataType is formally defined in OPC 10000-100 Device Model",
                dataType=di.datatypes.DeviceHealthEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(machine_vision_amcm_objtypes.VisionDisplayUnitType, ns0.reftypes.HasAddIn, o6.ns["ns=machine_vision_amcm;i=5152"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, machine_vision_amcm_reftypes, machine_vision_amcm_datypes, machine_vision_amcm_vartypes, machine_vision_amcm_objtypes
