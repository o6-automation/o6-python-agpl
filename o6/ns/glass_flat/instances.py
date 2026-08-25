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

"""Generated OPC UA glass_flat namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
from . import datatypes as glass_flat_datypes
from . import objtypes as glass_flat_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.TransitionType(
    nodeId="ns=glass_flat;i=1000",
    browseName="ns=glass_flat;InitializingToRunning",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=1048", browseName="TransitionNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(glass_flat_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=1000"])
ns0.objtypes.TransitionType(
    nodeId="ns=glass_flat;i=1001",
    browseName="ns=glass_flat;RunningToInterrupted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=1049", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(glass_flat_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=1001"])
ns0.objtypes.TransitionType(
    nodeId="ns=glass_flat;i=1012",
    browseName="ns=glass_flat;InterruptedToRunning",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=1050", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(glass_flat_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=1012"])
ns0.objtypes.TransitionType(
    nodeId="ns=glass_flat;i=1013",
    browseName="ns=glass_flat;RunningToAborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=1051", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(glass_flat_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=1013"])
ns0.objtypes.TransitionType(
    nodeId="ns=glass_flat;i=1014",
    browseName="ns=glass_flat;RunningToEnded",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=1052", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(glass_flat_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=1014"])
ns0.objtypes.TransitionType(
    nodeId="ns=glass_flat;i=1042",
    browseName="ns=glass_flat;EndedToInitializing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=1054", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(glass_flat_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=1042"])
ns0.objtypes.TransitionType(
    nodeId="ns=glass_flat;i=1043",
    browseName="ns=glass_flat;InterruptedToAborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=1055", browseName="TransitionNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(glass_flat_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=1043"])
ns0.objtypes.TransitionType(
    nodeId="ns=glass_flat;i=1044",
    browseName="ns=glass_flat;IdleToQueued",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=1056", browseName="TransitionNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(glass_flat_objtypes.InitializingSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=1044"])
o6.reference(o6.ns["ns=glass_flat;i=1044"], "i=53", o6.ns["ns=glass_flat;i=7021"])
ns0.objtypes.TransitionType(
    nodeId="ns=glass_flat;i=1045",
    browseName="ns=glass_flat;QueuedToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=1057", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(glass_flat_objtypes.InitializingSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=1045"])
ns0.objtypes.TransitionType(
    nodeId="ns=glass_flat;i=1046",
    browseName="ns=glass_flat;QueuedToReleased",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=1058", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(glass_flat_objtypes.InitializingSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=1046"])
o6.reference(o6.ns["ns=glass_flat;i=1046"], "i=53", o6.ns["ns=glass_flat;i=7003"])
ns0.objtypes.TransitionType(
    nodeId="ns=glass_flat;i=1047",
    browseName="ns=glass_flat;ReleasedToQueued",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=1059", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(glass_flat_objtypes.InitializingSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=1047"])
o6.reference(o6.ns["ns=glass_flat;i=1047"], "i=53", o6.ns["ns=glass_flat;i=7004"])
ns0.objtypes.TransitionType(
    nodeId="ns=glass_flat;i=1022",
    browseName="ns=glass_flat;RunningToRunning",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=1060", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(glass_flat_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=1022"])
ns0.objtypes.TransitionType(
    nodeId="ns=glass_flat;i=1028",
    browseName="ns=glass_flat;AbortedToInitializing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=1061", browseName="TransitionNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(glass_flat_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=1028"])
ns0.objtypes.TransitionType(
    nodeId="ns=glass_flat;i=1053",
    browseName="ns=glass_flat;InitializingToAborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=1062", browseName="TransitionNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(glass_flat_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=1053"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat;i=5037", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat;i=5038", browseName="Default XML")
o6.hasEncoding(glass_flat_datypes.FileFormatType, o6.ns["ns=glass_flat;i=5038"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat;i=5039", browseName="Default JSON")
o6.hasEncoding(glass_flat_datypes.FileFormatType, o6.ns["ns=glass_flat;i=5039"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat;i=5082", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat;i=5083", browseName="Default XML")
o6.hasEncoding(glass_flat_datypes.UserProfileType, o6.ns["ns=glass_flat;i=5083"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=glass_flat;i=5084", browseName="Default JSON")
o6.hasEncoding(glass_flat_datypes.UserProfileType, o6.ns["ns=glass_flat;i=5084"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6021",
    browseName="ns=glass_flat;Weight",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6022", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(glass_flat_objtypes.BaseMaterialType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=6021"])
ns0.objtypes.InitialStateType(
    nodeId="ns=glass_flat;i=5032",
    browseName="ns=glass_flat;Initializing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6024", browseName="StateNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(glass_flat_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5032"])
o6.reference(o6.ns["ns=glass_flat;i=1000"], "i=51", o6.ns["ns=glass_flat;i=5032"])
o6.reference(o6.ns["ns=glass_flat;i=1028"], "i=52", o6.ns["ns=glass_flat;i=5032"])
o6.reference(o6.ns["ns=glass_flat;i=1042"], "i=52", o6.ns["ns=glass_flat;i=5032"])
o6.reference(o6.ns["ns=glass_flat;i=1053"], "i=51", o6.ns["ns=glass_flat;i=5032"])
glass_flat_objtypes.BaseMaterialType(
    nodeId="ns=glass_flat;i=5005",
    browseName="ns=glass_flat;<InputMaterial>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6023", browseName="ns=glass_flat;Identifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6025", browseName="ns=glass_flat;Location", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6026", browseName="ns=glass_flat;MaterialIdentifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=glass_flat;i=5014", browseName="ns=glass_flat;InputMaterials", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=glass_flat;i=5005"])]
)
o6.reference(glass_flat_objtypes.ProductionJobType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5014"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6018",
    browseName="ns=glass_flat;Y",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6028", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(glass_flat_objtypes.BaseMaterialType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=6018"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6019",
    browseName="ns=glass_flat;X",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6029", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(glass_flat_objtypes.BaseMaterialType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=6019"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6020",
    browseName="ns=glass_flat;Z",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6030", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(glass_flat_objtypes.BaseMaterialType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=6020"])
glass_flat_objtypes.BaseMaterialType(
    nodeId="ns=glass_flat;i=5006",
    browseName="ns=glass_flat;<InputMaterial>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6027", browseName="ns=glass_flat;Identifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6031", browseName="ns=glass_flat;Location", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6032", browseName="ns=glass_flat;MaterialIdentifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
ns0.objtypes.FolderType(nodeId="ns=glass_flat;i=5022", browseName="ns=glass_flat;InputMaterials", references=[o6.hasComponent(o6.ns["ns=glass_flat;i=5006"])])
glass_flat_objtypes.BaseMaterialType(
    nodeId="ns=glass_flat;i=5027",
    browseName="ns=glass_flat;<OutputMaterial>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6033", browseName="ns=glass_flat;Identifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6034", browseName="ns=glass_flat;Location", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6035", browseName="ns=glass_flat;MaterialIdentifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=glass_flat;i=5018", browseName="ns=glass_flat;OutputMaterials", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=glass_flat;i=5027"])]
)
o6.reference(glass_flat_objtypes.ProductionJobType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5018"])
glass_flat_objtypes.GlassMachineIdentificationType(
    nodeId="ns=glass_flat;i=5001",
    browseName="ns=glass_flat;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6057", browseName="ns=glass_flat;LoggedInProfiles", dataType=glass_flat_datypes.UserProfileType, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6058",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6061",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6062",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(glass_flat_objtypes.GlassMachineType, ns0.reftypes.HasAddIn, o6.ns["ns=glass_flat;i=5001"])
glass_flat_objtypes.BaseMaterialType(
    nodeId="ns=glass_flat;i=5028",
    browseName="ns=glass_flat;<OutputMaterial>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6036", browseName="ns=glass_flat;Identifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6065", browseName="ns=glass_flat;Location", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6066", browseName="ns=glass_flat;MaterialIdentifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
ns0.objtypes.FolderType(nodeId="ns=glass_flat;i=5026", browseName="ns=glass_flat;OutputMaterials", references=[o6.hasComponent(o6.ns["ns=glass_flat;i=5028"])])
glass_flat_objtypes.ConfigurationRulesType(
    nodeId="ns=glass_flat;i=5029",
    browseName="ns=glass_flat;ConfigurationRules",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6067",
                browseName="ns=glass_flat;MachineProcessingCoordinateSystem",
                dataType=glass_flat_datypes.CoordinateSystemEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
)
o6.reference(glass_flat_objtypes.GlassMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5029"])
glass_flat_objtypes.ProductionJobType(
    nodeId="ns=glass_flat;i=5003",
    browseName="<OrderedObject>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6056", browseName="ns=glass_flat;Identifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6073", browseName="ns=glass_flat;NumberInList", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=glass_flat;i=5022"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=5026"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=glass_flat;i=6052", browseName="ns=glass_flat;EndTime", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=glass_flat;i=6074", browseName="ns=glass_flat;StartTime", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)
        ),
    ],
)
o6.reference(glass_flat_objtypes.ProductionPlanType, ns0.reftypes.HasOrderedComponent, o6.ns["ns=glass_flat;i=5003"])
glass_flat_objtypes.ProductionType(
    nodeId="ns=glass_flat;i=5015",
    browseName="ns=glass_flat;Production",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6063", browseName="ns=glass_flat;JobListIsRecommendation", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6080",
                browseName="ns=glass_flat;SupportedMaterialTypes",
                dataType=o6.NodeId,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(glass_flat_objtypes.ProductionPlanType(nodeId="ns=glass_flat;i=5016", browseName="ns=glass_flat;ProductionPlan")),
    ],
)
o6.reference(glass_flat_objtypes.GlassMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5015"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6094",
    browseName="ns=glass_flat;Weight",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6095", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6105",
    browseName="ns=glass_flat;Weight",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6106", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6114",
    browseName="ns=glass_flat;Weight",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6115", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6116",
    browseName="ns=glass_flat;GasFilling",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6059", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=100.0))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6117",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(glass_flat_objtypes.GasMixType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=6116"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6118",
    browseName="ns=glass_flat;MixingRatio",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6060", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=100.0))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6119",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(glass_flat_objtypes.GasMixType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=6118"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6120",
    browseName="ns=glass_flat;X",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6121", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
glass_flat_objtypes.AssemblyType(
    nodeId="ns=glass_flat;i=5023",
    browseName="ns=glass_flat;<OutputMaterial>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6125", browseName="ns=glass_flat;Identifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6126", browseName="ns=glass_flat;Location", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6127", browseName="ns=glass_flat;MaterialIdentifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
o6.reference(glass_flat_objtypes.AssemblyJobType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5023"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6122",
    browseName="ns=glass_flat;Y",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6129", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6130",
    browseName="ns=glass_flat;Z",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6131", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
glass_flat_objtypes.BaseMaterialType(
    nodeId="ns=glass_flat;i=5019",
    browseName="ns=glass_flat;<InputMaterial>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6071", browseName="ns=glass_flat;Location", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6072", browseName="ns=glass_flat;Identifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6089", browseName="ns=glass_flat;MaterialIdentifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6090", browseName="ns=glass_flat;Description", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6094"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6120"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6122"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6130"]),
    ],
)
o6.reference(glass_flat_objtypes.CuttingJobType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5019"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6138",
    browseName="ns=glass_flat;X",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6141", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6143",
    browseName="ns=glass_flat;Weight",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6144", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6142",
    browseName="ns=glass_flat;Y",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6151", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6154",
    browseName="ns=glass_flat;Z",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6155", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.objtypes.StateType(
    nodeId="ns=glass_flat;i=5033",
    browseName="ns=glass_flat;Aborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6159", browseName="StateNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(glass_flat_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5033"])
o6.reference(o6.ns["ns=glass_flat;i=1013"], "i=52", o6.ns["ns=glass_flat;i=5033"])
o6.reference(o6.ns["ns=glass_flat;i=1028"], "i=51", o6.ns["ns=glass_flat;i=5033"])
o6.reference(o6.ns["ns=glass_flat;i=1043"], "i=52", o6.ns["ns=glass_flat;i=5033"])
o6.reference(o6.ns["ns=glass_flat;i=1053"], "i=52", o6.ns["ns=glass_flat;i=5033"])
ns0.objtypes.StateType(
    nodeId="ns=glass_flat;i=5034",
    browseName="ns=glass_flat;Ended",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6160", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(glass_flat_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5034"])
o6.reference(o6.ns["ns=glass_flat;i=1014"], "i=52", o6.ns["ns=glass_flat;i=5034"])
o6.reference(o6.ns["ns=glass_flat;i=1042"], "i=51", o6.ns["ns=glass_flat;i=5034"])
ns0.objtypes.StateType(
    nodeId="ns=glass_flat;i=5035",
    browseName="ns=glass_flat;Interrupted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6161", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(glass_flat_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5035"])
o6.reference(o6.ns["ns=glass_flat;i=1001"], "i=52", o6.ns["ns=glass_flat;i=5035"])
o6.reference(o6.ns["ns=glass_flat;i=1012"], "i=51", o6.ns["ns=glass_flat;i=5035"])
o6.reference(o6.ns["ns=glass_flat;i=1043"], "i=51", o6.ns["ns=glass_flat;i=5035"])
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6162",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=3005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[5],
    value=[o6.LocalizedText("Other"), o6.LocalizedText("Metalic"), o6.LocalizedText("TPS"), o6.LocalizedText("Plastic"), o6.LocalizedText("Elastic")],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6166",
    browseName="ns=glass_flat;SealantDepth",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6167", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(glass_flat_objtypes.SpacerType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=6166"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6170",
    browseName="ns=glass_flat;MixingRatio",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6068",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        )
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(glass_flat_objtypes.SealingMaterialType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=6170"])
ns0.objtypes.StateType(
    nodeId="ns=glass_flat;i=5036",
    browseName="ns=glass_flat;Running",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6171", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(glass_flat_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5036"])
o6.reference(o6.ns["ns=glass_flat;i=1000"], "i=52", o6.ns["ns=glass_flat;i=5036"])
o6.reference(o6.ns["ns=glass_flat;i=1001"], "i=51", o6.ns["ns=glass_flat;i=5036"])
o6.reference(o6.ns["ns=glass_flat;i=1012"], "i=52", o6.ns["ns=glass_flat;i=5036"])
o6.reference(o6.ns["ns=glass_flat;i=1013"], "i=51", o6.ns["ns=glass_flat;i=5036"])
o6.reference(o6.ns["ns=glass_flat;i=1014"], "i=51", o6.ns["ns=glass_flat;i=5036"])
o6.reference(o6.ns["ns=glass_flat;i=1022"], "i=51", o6.ns["ns=glass_flat;i=5036"])
o6.reference(o6.ns["ns=glass_flat;i=1022"], "i=52", o6.ns["ns=glass_flat;i=5036"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6182",
    browseName="ns=glass_flat;ElectricalConductivity",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6183", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(glass_flat_objtypes.GlassType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=6182"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6184",
    browseName="ns=glass_flat;ElectricalConductivity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6185", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6189",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=3008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[9],
    value=[
        o6.LocalizedText("Unknown"),
        o6.LocalizedText("System1"),
        o6.LocalizedText("System2"),
        o6.LocalizedText("System3"),
        o6.LocalizedText("System4"),
        o6.LocalizedText("System5"),
        o6.LocalizedText("System6"),
        o6.LocalizedText("System7"),
        o6.LocalizedText("System8"),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6203",
    browseName="ns=glass_flat;X",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6204", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(glass_flat_objtypes.GlassType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=6203"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6205",
    browseName="ns=glass_flat;Y",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6206", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(glass_flat_objtypes.GlassType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=6205"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6207",
    browseName="ns=glass_flat;Absorption",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6208", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(glass_flat_objtypes.GlassType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=6207"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6209",
    browseName="ns=glass_flat;Reflection",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6210", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(glass_flat_objtypes.GlassType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=6209"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6211",
    browseName="ns=glass_flat;CoatingEmessivity",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6212", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(glass_flat_objtypes.GlassType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=6211"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6213",
    browseName="ns=glass_flat;Transmission",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6214", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(glass_flat_objtypes.GlassType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=6213"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6215",
    browseName="ns=glass_flat;Weight",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6216", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6217",
    browseName="ns=glass_flat;Absorption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6218", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6219",
    browseName="ns=glass_flat;Reflection",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6220", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6221",
    browseName="ns=glass_flat;X",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6222", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6223",
    browseName="ns=glass_flat;CoatingEmessivity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6224", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6225",
    browseName="ns=glass_flat;Transmission",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6226", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
glass_flat_objtypes.GlassType(
    nodeId="ns=glass_flat;i=5020",
    browseName="ns=glass_flat;<OutputMaterial>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6096", browseName="ns=glass_flat;Location", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6099", browseName="ns=glass_flat;Identifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6100", browseName="ns=glass_flat;MaterialIdentifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6101", browseName="ns=glass_flat;Description", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6133", browseName="ns=glass_flat;Orientation", dataType=ns0.datatypes.Number, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6148", browseName="ns=glass_flat;SignificantSide", dataType=glass_flat_datypes.SignificantSideEnumeration, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6149", browseName="ns=glass_flat;StructureClass", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6152",
                browseName="ns=glass_flat;StructureAlignment",
                dataType=glass_flat_datypes.StructureAlignmentEnumeration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6228", browseName="ns=glass_flat;CoatingClass", dataType=glass_flat_datypes.CoatingClassEnumeration, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6105"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6138"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6142"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6154"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6184"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6217"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6219"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6223"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6225"]),
    ],
)
o6.reference(glass_flat_objtypes.CuttingJobType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5020"])
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6229",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=3009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("HardCoating"), o6.LocalizedText("SoftCoating"), o6.LocalizedText("CoatedWithFoilProtection"), o6.LocalizedText("UserDefined")],
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashGlassSlashFlatSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=glass_flat;i=5041",
    browseName="ns=glass_flat;http://opcfoundation.org/UA/Glass/Flat/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6262", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6263", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2022-01-01T00:00:00Z"))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6264", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Glass/Flat/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6265", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6266", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6267", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6268", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=glass_flat;i=6282",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6283", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
glass_flat_objtypes.InitializingSubStateMachineType(
    nodeId="ns=glass_flat;i=5059", browseName="ns=glass_flat;InitializingState", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=glass_flat;i=6282"])]
)
o6.reference(glass_flat_objtypes.ProductionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5059"])
o6.reference(o6.ns["ns=glass_flat;i=5059"], "i=117", glass_flat_objtypes.InitializingSubStateMachineType)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=glass_flat;i=6286",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6287", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
glass_flat_objtypes.InitializingSubStateMachineType(
    nodeId="ns=glass_flat;i=5061", browseName="ns=glass_flat;InitializedState", references=[o6.hasComponent(o6.ns["ns=glass_flat;i=6286"])]
)
o6.reference(o6.ns["ns=glass_flat;i=5061"], "i=117", glass_flat_objtypes.InitializingSubStateMachineType)
glass_flat_objtypes.ProductionStateMachineType(
    nodeId="ns=glass_flat;i=5013",
    browseName="ns=glass_flat;State",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=glass_flat;i=5061"]),
        o6.hasComponent(ns0.vartypes.FiniteStateVariableType(nodeId="ns=glass_flat;i=6173", browseName="CurrentState", dataType=o6.LocalizedText)),
    ],
)
o6.reference(glass_flat_objtypes.ProductionJobType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5013"])
ns0.objtypes.InitialStateType(
    nodeId="ns=glass_flat;i=5067",
    browseName="ns=glass_flat;Idle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6298", browseName="StateNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(glass_flat_objtypes.InitializingSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5067"])
o6.reference(o6.ns["ns=glass_flat;i=1044"], "i=51", o6.ns["ns=glass_flat;i=5067"])
o6.reference(o6.ns["ns=glass_flat;i=1045"], "i=52", o6.ns["ns=glass_flat;i=5067"])
ns0.objtypes.StateType(
    nodeId="ns=glass_flat;i=5076",
    browseName="ns=glass_flat;Queued",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6307", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(glass_flat_objtypes.InitializingSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5076"])
o6.reference(o6.ns["ns=glass_flat;i=1044"], "i=52", o6.ns["ns=glass_flat;i=5076"])
o6.reference(o6.ns["ns=glass_flat;i=1045"], "i=51", o6.ns["ns=glass_flat;i=5076"])
o6.reference(o6.ns["ns=glass_flat;i=1046"], "i=51", o6.ns["ns=glass_flat;i=5076"])
o6.reference(o6.ns["ns=glass_flat;i=1047"], "i=52", o6.ns["ns=glass_flat;i=5076"])
ns0.objtypes.StateType(
    nodeId="ns=glass_flat;i=5077",
    browseName="ns=glass_flat;Released",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6308", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(glass_flat_objtypes.InitializingSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5077"])
o6.reference(o6.ns["ns=glass_flat;i=1046"], "i=52", o6.ns["ns=glass_flat;i=5077"])
o6.reference(o6.ns["ns=glass_flat;i=1047"], "i=51", o6.ns["ns=glass_flat;i=5077"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6313",
    browseName="ns=glass_flat;Y",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6326", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6327",
    browseName="ns=glass_flat;Z",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6328", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
glass_flat_objtypes.BaseMaterialType(
    nodeId="ns=glass_flat;i=5021",
    browseName="ns=glass_flat;<InputMaterial>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6107", browseName="ns=glass_flat;Location", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6108", browseName="ns=glass_flat;Identifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6109", browseName="ns=glass_flat;MaterialIdentifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6110", browseName="ns=glass_flat;Description", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6114"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6221"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6313"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6327"]),
    ],
)
o6.reference(glass_flat_objtypes.AssemblyJobType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5021"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6343",
    browseName="ns=glass_flat;X",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6344", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6345",
    browseName="ns=glass_flat;Y",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6346", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6347",
    browseName="ns=glass_flat;Z",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6348", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
glass_flat_objtypes.BaseMaterialType(
    nodeId="ns=glass_flat;i=5024",
    browseName="ns=glass_flat;<InputMaterial>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6134", browseName="ns=glass_flat;Location", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6135", browseName="ns=glass_flat;Identifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6136", browseName="ns=glass_flat;MaterialIdentifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6137", browseName="ns=glass_flat;Description", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6143"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6343"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6345"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6347"]),
    ],
)
o6.reference(glass_flat_objtypes.ProcessingJobType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5024"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6349",
    browseName="ns=glass_flat;X",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6350", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6351",
    browseName="ns=glass_flat;Y",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6352", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6353",
    browseName="ns=glass_flat;Z",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6354", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
glass_flat_objtypes.BaseMaterialType(
    nodeId="ns=glass_flat;i=5025",
    browseName="ns=glass_flat;<OutputMaterial>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6145", browseName="ns=glass_flat;Location", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6146", browseName="ns=glass_flat;Identifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6147", browseName="ns=glass_flat;MaterialIdentifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6150", browseName="ns=glass_flat;Description", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6215"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6349"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6351"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=6353"]),
    ],
)
o6.reference(glass_flat_objtypes.ProcessingJobType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5025"])
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6372",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("Indifferent"), o6.LocalizedText("Top"), o6.LocalizedText("Down")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6377",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("Indifferent"), o6.LocalizedText("Longitudinal"), o6.LocalizedText("Transverse")],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6168",
    browseName="ns=glass_flat;FillLevel",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6381", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=glass_flat;i=6164",
    browseName="ns=glass_flat;Filling",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=glass_flat;i=6168"])],
    dataType=glass_flat_datypes.LimitedString64,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(glass_flat_objtypes.SpacerType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=6164"])
glass_flat_objtypes.BaseMaterialType(
    nodeId="ns=glass_flat;i=5078",
    browseName="ns=glass_flat;Gas_1",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6169", browseName="ns=glass_flat;Location", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6382", browseName="ns=glass_flat;MaterialIdentifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6383", browseName="ns=glass_flat;Identifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
o6.reference(glass_flat_objtypes.GasMixType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5078"])
glass_flat_objtypes.BaseMaterialType(
    nodeId="ns=glass_flat;i=5079",
    browseName="ns=glass_flat;Gas_2",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6384", browseName="ns=glass_flat;Location", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6385", browseName="ns=glass_flat;MaterialIdentifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6386", browseName="ns=glass_flat;Identifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
o6.reference(glass_flat_objtypes.GasMixType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5079"])
glass_flat_objtypes.BaseMaterialType(
    nodeId="ns=glass_flat;i=5080",
    browseName="ns=glass_flat;Resin",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6392", browseName="ns=glass_flat;Location", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6393", browseName="ns=glass_flat;MaterialIdentifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6394", browseName="ns=glass_flat;Identifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
o6.reference(glass_flat_objtypes.SealingMaterialType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5080"])
glass_flat_objtypes.BaseMaterialType(
    nodeId="ns=glass_flat;i=5081",
    browseName="ns=glass_flat;Hardener",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6395", browseName="ns=glass_flat;Location", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6396", browseName="ns=glass_flat;MaterialIdentifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6397", browseName="ns=glass_flat;Identifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
o6.reference(glass_flat_objtypes.SealingMaterialType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5081"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=glass_flat;i=6401",
    browseName="ns=glass_flat;Z",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6402", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(glass_flat_objtypes.FoilType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=6401"])


ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6081",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7001", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6081"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6082",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6083",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7002", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6082"]), outputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6083"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6084",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6085",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7005", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6084"]), outputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6085"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6004",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7006", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6004"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6005",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6006",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7007", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6005"]), outputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6006"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6007",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6008",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7008", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6007"]), outputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6008"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6010",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6011",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7009", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6010"]), outputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6011"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6012",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7010", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6012"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6016",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7011", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6016"]))

ns0.objtypes.FileType(
    nodeId="ns=glass_flat;i=5008",
    browseName="ns=glass_flat;Plan",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6009", browseName="OpenCount", description="The current number of open file handles.", dataType=o6.UInt16)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6013", browseName="Size", description="The size of the file in bytes.", dataType=o6.UInt64)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6014", browseName="UserWritable", description="Whether the file is writable by the current user.", dataType=o6.Boolean
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6015", browseName="Writable", description="Whether the file is writable.", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7006"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7007"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7008"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7009"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7010"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7011"]),
    ],
)
o6.reference(glass_flat_objtypes.InstructionType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5008"])


ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6124",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6139",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7012", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6124"]), outputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6139"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6140",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7013", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6140"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6175",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7014", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6175"]))

ns0.objtypes.FileType(
    nodeId="ns=glass_flat;i=5017",
    browseName="ns=glass_flat;<LocalManuals>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6086", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6157", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6158", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6172", browseName="Writable", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7001"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7002"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7005"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7012"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7013"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7014"]),
    ],
)
o6.reference(glass_flat_objtypes.ManualFolderType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5017"])


ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6037",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7015", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6037"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6038",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6039",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7016", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6038"]), outputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6039"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6040",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6041",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7017", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6040"]), outputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6041"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6043",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6044",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7018", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6043"]), outputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6044"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6045",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7019", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6045"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6049",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7020", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6049"]))

ns0.objtypes.FileType(
    nodeId="ns=glass_flat;i=5012",
    browseName="ns=glass_flat;Plan",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6042", browseName="OpenCount", description="The current number of open file handles.", dataType=o6.UInt16)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6046", browseName="Size", description="The size of the file in bytes.", dataType=o6.UInt64)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6047", browseName="UserWritable", description="Whether the file is writable by the current user.", dataType=o6.Boolean
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6048", browseName="Writable", description="Whether the file is writable.", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7015"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7016"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7017"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7018"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7019"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7020"]),
    ],
)
glass_flat_objtypes.InstructionType(
    nodeId="ns=glass_flat;i=5010",
    browseName="ns=glass_flat;Instruction",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=glass_flat;i=6274",
                browseName="ns=glass_flat;PlanFileFormat",
                dataType=glass_flat_datypes.FileFormatType,
                value=glass_flat_datypes.FileFormatType(name="", fileExtension="", version=""),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=glass_flat;i=5012"]),
    ],
)
o6.reference(glass_flat_objtypes.ProductionJobType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5010"])


ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6191",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7027", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6191"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6192",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7028",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7028", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6192"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6193",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6194",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=glass_flat;i=7029", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6193"]), outputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6194"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6199",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7030", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6199"]))

di.objtypes.LockingServicesType(
    nodeId="ns=glass_flat;i=5004",
    browseName="ns=glass_flat;Lock",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6195", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6196", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6197", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6198", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7027"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7028"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7029"]),
        o6.hasComponent(o6.ns["ns=glass_flat;i=7030"]),
    ],
)
o6.reference(glass_flat_objtypes.ProductionJobType, ns0.reftypes.HasComponent, o6.ns["ns=glass_flat;i=5004"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, glass_flat_datypes, glass_flat_objtypes
