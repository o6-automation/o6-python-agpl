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

"""Generated OPC UA machine_vision namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as machine_vision_reftypes
from . import datatypes as machine_vision_datypes
from . import vartypes as machine_vision_vartypes
from . import objtypes as machine_vision_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5002", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5003", browseName="Default XML")
o6.hasEncoding(machine_vision_datypes.RecipeIdExternalDataType, o6.ns["ns=machine_vision;i=5003"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5006", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5007", browseName="Default XML")
o6.hasEncoding(machine_vision_datypes.MeasIdDataType, o6.ns["ns=machine_vision;i=5007"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5008", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5013", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5014", browseName="Default XML")
o6.hasEncoding(machine_vision_datypes.PartIdDataType, o6.ns["ns=machine_vision;i=5014"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5016", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5017", browseName="Default XML")
o6.hasEncoding(machine_vision_datypes.ProcessingTimesDataType, o6.ns["ns=machine_vision;i=5017"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5018", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5019", browseName="Default XML")
o6.hasEncoding(machine_vision_datypes.ResultDataType, o6.ns["ns=machine_vision;i=5019"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5026", browseName="Default XML")
o6.hasEncoding(machine_vision_datypes.JobIdDataType, o6.ns["ns=machine_vision;i=5026"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5027", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5088", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5089", browseName="Default XML")
o6.hasEncoding(machine_vision_datypes.ConfigurationDataType, o6.ns["ns=machine_vision;i=5089"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5090", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5091", browseName="Default XML")
o6.hasEncoding(machine_vision_datypes.ConfigurationIdDataType, o6.ns["ns=machine_vision;i=5091"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5224", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5225", browseName="Default XML")
o6.hasEncoding(machine_vision_datypes.ProductIdDataType, o6.ns["ns=machine_vision;i=5225"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5246", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5247", browseName="Default XML")
o6.hasEncoding(machine_vision_datypes.ConfigurationTransferOptions, o6.ns["ns=machine_vision;i=5247"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5248", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5249", browseName="Default XML")
o6.hasEncoding(machine_vision_datypes.RecipeTransferOptions, o6.ns["ns=machine_vision;i=5249"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5268", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5269", browseName="Default XML")
o6.hasEncoding(machine_vision_datypes.RecipeIdInternalDataType, o6.ns["ns=machine_vision;i=5269"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5271", browseName="Default XML")
o6.hasEncoding(machine_vision_datypes.BinaryIdBaseDataType, o6.ns["ns=machine_vision;i=5271"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5272", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5273", browseName="Default XML")
o6.hasEncoding(machine_vision_datypes.ProductDataType, o6.ns["ns=machine_vision;i=5273"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5274", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5275", browseName="Default XML")
o6.hasEncoding(machine_vision_datypes.ResultIdDataType, o6.ns["ns=machine_vision;i=5275"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5276", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5277", browseName="Default XML")
o6.hasEncoding(machine_vision_datypes.ResultTransferOptions, o6.ns["ns=machine_vision;i=5277"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5278", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=machine_vision;i=5279", browseName="Default XML")
o6.hasEncoding(machine_vision_datypes.SystemStateDescriptionDataType, o6.ns["ns=machine_vision;i=5279"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6021", browseName="ns=machine_vision;RecipeIdExternalDataType", dataType=o6.String, value="RecipeIdExternalDataType"
)
o6.reference(o6.ns["ns=machine_vision;i=5002"], "i=39", o6.ns["ns=machine_vision;i=6021"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6022", browseName="ns=machine_vision;RecipeIdExternalDataType", dataType=o6.String, value="//xs:element[@name='RecipeIdExternalDataType']"
)
o6.reference(o6.ns["ns=machine_vision;i=5003"], "i=39", o6.ns["ns=machine_vision;i=6022"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=machine_vision;i=6028", browseName="ns=machine_vision;MeasIdDataType", dataType=o6.String, value="MeasIdDataType")
o6.reference(o6.ns["ns=machine_vision;i=5006"], "i=39", o6.ns["ns=machine_vision;i=6028"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6029", browseName="ns=machine_vision;MeasIdDataType", dataType=o6.String, value="//xs:element[@name='MeasIdDataType']"
)
o6.reference(o6.ns["ns=machine_vision;i=5007"], "i=39", o6.ns["ns=machine_vision;i=6029"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=machine_vision;i=6030", browseName="ns=machine_vision;JobIdDataType", dataType=o6.String, value="JobIdDataType")
o6.reference(o6.ns["ns=machine_vision;i=5008"], "i=39", o6.ns["ns=machine_vision;i=6030"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6031", browseName="ns=machine_vision;JobIdDataType", dataType=o6.String, value="//xs:element[@name='JobIdDataType']"
)
o6.reference(o6.ns["ns=machine_vision;i=5026"], "i=39", o6.ns["ns=machine_vision;i=6031"])
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6032",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=3023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("PRD_1"), description=o6.LocalizedText("Production: The vision system is currently working on a job.", "")
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("SBY_2"),
            description=o6.LocalizedText(
                "Stand by: The vision system is ready to accept a command but is currently not executing a job. It could for example be waiting for a Start command or a user input.",
                "",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("ENG_3"),
            description=o6.LocalizedText(
                "Engineering: The vision system is not working and not ready to accept a command because a user is currently working on the system.  This could be for editing a recipe or changing the system configuration.",
                "",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("SDT_4"),
            description=o6.LocalizedText(
                "Scheduled downtime: The vision system is not available for production and this was planned in advance. This could be for cleaning, maintenance or calibration works.",
                "",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=5,
            displayName=o6.LocalizedText("UDT_5"),
            description=o6.LocalizedText(
                "Unscheduled downtime: The vision system is not available for production due to failure and repair. This covers all kinds of error states that might occur during operation.",
                "",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=6,
            displayName=o6.LocalizedText("NST_6"),
            description=o6.LocalizedText(
                "Nonscheduled time: The vision system is not working because no production was scheduled. This also covers things like operator training on the system.", ""
            ),
        ),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=machine_vision;i=6033", browseName="ns=machine_vision;BinaryIdBaseDataType", dataType=o6.String, value="BinaryIdBaseDataType")
o6.reference(o6.ns["ns=machine_vision;i=5027"], "i=39", o6.ns["ns=machine_vision;i=6033"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6034", browseName="ns=machine_vision;BinaryIdBaseDataType", dataType=o6.String, value="//xs:element[@name='BinaryIdBaseDataType']"
)
o6.reference(o6.ns["ns=machine_vision;i=5271"], "i=39", o6.ns["ns=machine_vision;i=6034"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6035", browseName="ns=machine_vision;RecipeIdInternalDataType", dataType=o6.String, value="RecipeIdInternalDataType"
)
o6.reference(o6.ns["ns=machine_vision;i=5268"], "i=39", o6.ns["ns=machine_vision;i=6035"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6036", browseName="ns=machine_vision;RecipeIdInternalDataType", dataType=o6.String, value="//xs:element[@name='RecipeIdInternalDataType']"
)
o6.reference(o6.ns["ns=machine_vision;i=5269"], "i=39", o6.ns["ns=machine_vision;i=6036"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=machine_vision;i=6037", browseName="ns=machine_vision;ProductDataType", dataType=o6.String, value="ProductDataType")
o6.reference(o6.ns["ns=machine_vision;i=5272"], "i=39", o6.ns["ns=machine_vision;i=6037"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6038", browseName="ns=machine_vision;ProductDataType", dataType=o6.String, value="//xs:element[@name='ProductDataType']"
)
o6.reference(o6.ns["ns=machine_vision;i=5273"], "i=39", o6.ns["ns=machine_vision;i=6038"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=machine_vision;i=6039", browseName="ns=machine_vision;ResultIdDataType", dataType=o6.String, value="ResultIdDataType")
o6.reference(o6.ns["ns=machine_vision;i=5274"], "i=39", o6.ns["ns=machine_vision;i=6039"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6040", browseName="ns=machine_vision;ResultIdDataType", dataType=o6.String, value="//xs:element[@name='ResultIdDataType']"
)
o6.reference(o6.ns["ns=machine_vision;i=5275"], "i=39", o6.ns["ns=machine_vision;i=6040"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6058",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6060", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6063",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6064", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=machine_vision;i=6071", browseName="ns=machine_vision;ProductIdDataType", dataType=o6.String, value="ProductIdDataType")
o6.reference(o6.ns["ns=machine_vision;i=5224"], "i=39", o6.ns["ns=machine_vision;i=6071"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=machine_vision;i=6072", browseName="ns=machine_vision;PartIdDataType", dataType=o6.String, value="PartIdDataType")
o6.reference(o6.ns["ns=machine_vision;i=5013"], "i=39", o6.ns["ns=machine_vision;i=6072"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6073", browseName="ns=machine_vision;PartIdDataType", dataType=o6.String, value="//xs:element[@name='PartIdDataType']"
)
o6.reference(o6.ns["ns=machine_vision;i=5014"], "i=39", o6.ns["ns=machine_vision;i=6073"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=machine_vision;i=6074", browseName="ns=machine_vision;ProcessingTimesDataType", dataType=o6.String, value="ProcessingTimesDataType")
o6.reference(o6.ns["ns=machine_vision;i=5016"], "i=39", o6.ns["ns=machine_vision;i=6074"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6075", browseName="ns=machine_vision;ProcessingTimesDataType", dataType=o6.String, value="//xs:element[@name='ProcessingTimesDataType']"
)
o6.reference(o6.ns["ns=machine_vision;i=5017"], "i=39", o6.ns["ns=machine_vision;i=6075"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=machine_vision;i=6076", browseName="ns=machine_vision;ResultDataType", dataType=o6.String, value="ResultDataType")
o6.reference(o6.ns["ns=machine_vision;i=5018"], "i=39", o6.ns["ns=machine_vision;i=6076"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6077", browseName="ns=machine_vision;ResultDataType", dataType=o6.String, value="//xs:element[@name='ResultDataType']"
)
o6.reference(o6.ns["ns=machine_vision;i=5019"], "i=39", o6.ns["ns=machine_vision;i=6077"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6080",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6081", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5045",
    browseName="ns=machine_vision;InitializedToReadyProduct",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6084", browseName="TransitionNumber", dataType=o6.UInt32, value=562))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5045"])
o6.reference(o6.ns["ns=machine_vision;i=5045"], "i=53", o6.ns["ns=machine_vision;i=7060"])
o6.reference(o6.ns["ns=machine_vision;i=5045"], "i=54", machine_vision_objtypes.StateChangedEventType)
o6.reference(o6.ns["ns=machine_vision;i=5045"], "i=54", machine_vision_objtypes.RecipePreparedEventType)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6085",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6088", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6091",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6092", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6093", browseName="ns=machine_vision;ProductIdDataType", dataType=o6.String, value="//xs:element[@name='ProductIdDataType']"
)
o6.reference(o6.ns["ns=machine_vision;i=5225"], "i=39", o6.ns["ns=machine_vision;i=6093"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6125", browseName="ns=machine_vision;ConfigurationTransferOptions", dataType=o6.String, value="ConfigurationTransferOptions"
)
o6.reference(o6.ns["ns=machine_vision;i=5246"], "i=39", o6.ns["ns=machine_vision;i=6125"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6126", browseName="ns=machine_vision;ConfigurationTransferOptions", dataType=o6.String, value="//xs:element[@name='ConfigurationTransferOptions']"
)
o6.reference(o6.ns["ns=machine_vision;i=5247"], "i=39", o6.ns["ns=machine_vision;i=6126"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=machine_vision;i=6127", browseName="ns=machine_vision;ResultTransferOptions", dataType=o6.String, value="ResultTransferOptions")
o6.reference(o6.ns["ns=machine_vision;i=5276"], "i=39", o6.ns["ns=machine_vision;i=6127"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6128", browseName="ns=machine_vision;ResultTransferOptions", dataType=o6.String, value="//xs:element[@name='ResultTransferOptions']"
)
o6.reference(o6.ns["ns=machine_vision;i=5277"], "i=39", o6.ns["ns=machine_vision;i=6128"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6130", browseName="ns=machine_vision;SystemStateDescriptionDataType", dataType=o6.String, value="SystemStateDescriptionDataType"
)
o6.reference(o6.ns["ns=machine_vision;i=5278"], "i=39", o6.ns["ns=machine_vision;i=6130"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6131",
    browseName="ns=machine_vision;SystemStateDescriptionDataType",
    dataType=o6.String,
    value="//xs:element[@name='SystemStateDescriptionDataType']",
)
o6.reference(o6.ns["ns=machine_vision;i=5279"], "i=39", o6.ns["ns=machine_vision;i=6131"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6135",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6136", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6162",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6163", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6082",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6166", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5253",
    browseName="ns=machine_vision;PreoperationalToOperational",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6171", browseName="TransitionNumber", dataType=o6.UInt32, value=141))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5253"])
o6.reference(o6.ns["ns=machine_vision;i=5253"], "i=53", o6.ns["ns=machine_vision;i=7095"])
o6.reference(o6.ns["ns=machine_vision;i=5253"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6175",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6178", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=machine_vision;i=6188", browseName="ns=machine_vision;RecipeTransferOptions", dataType=o6.String, value="RecipeTransferOptions")
o6.reference(o6.ns["ns=machine_vision;i=5248"], "i=39", o6.ns["ns=machine_vision;i=6188"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6189", browseName="ns=machine_vision;RecipeTransferOptions", dataType=o6.String, value="//xs:element[@name='RecipeTransferOptions']"
)
o6.reference(o6.ns["ns=machine_vision;i=5249"], "i=39", o6.ns["ns=machine_vision;i=6189"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6183",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6211", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6219",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6220", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5254",
    browseName="ns=machine_vision;PreoperationalToOperationalAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6221", browseName="TransitionNumber", dataType=o6.UInt32, value=140))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5254"])
o6.reference(o6.ns["ns=machine_vision;i=5254"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.StateType(
    nodeId="ns=machine_vision;i=5028",
    browseName="ns=machine_vision;Preoperational",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6226", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5028"])
o6.reference(o6.ns["ns=machine_vision;i=5028"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5253"])
o6.reference(o6.ns["ns=machine_vision;i=5028"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5254"])
o6.reference(o6.ns["ns=machine_vision;i=5253"], "i=51", o6.ns["ns=machine_vision;i=5028"])
o6.reference(o6.ns["ns=machine_vision;i=5254"], "i=51", o6.ns["ns=machine_vision;i=5028"])
ns0.objtypes.StateType(
    nodeId="ns=machine_vision;i=5029",
    browseName="ns=machine_vision;Halted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6227", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5029"])
ns0.objtypes.StateType(
    nodeId="ns=machine_vision;i=5030",
    browseName="ns=machine_vision;Error",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6228", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5030"])
ns0.objtypes.StateType(
    nodeId="ns=machine_vision;i=5031",
    browseName="ns=machine_vision;Operational",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6229", browseName="StateNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5031"])
o6.reference(o6.ns["ns=machine_vision;i=5031"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5253"])
o6.reference(o6.ns["ns=machine_vision;i=5031"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5254"])
o6.reference(o6.ns["ns=machine_vision;i=5253"], "i=52", o6.ns["ns=machine_vision;i=5031"])
o6.reference(o6.ns["ns=machine_vision;i=5254"], "i=52", o6.ns["ns=machine_vision;i=5031"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5032",
    browseName="ns=machine_vision;PreoperationalToHalted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6230", browseName="TransitionNumber", dataType=o6.UInt32, value=121))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5032"])
o6.reference(o6.ns["ns=machine_vision;i=5028"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5032"])
o6.reference(o6.ns["ns=machine_vision;i=5029"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5032"])
o6.reference(o6.ns["ns=machine_vision;i=5032"], "i=51", o6.ns["ns=machine_vision;i=5028"])
o6.reference(o6.ns["ns=machine_vision;i=5032"], "i=52", o6.ns["ns=machine_vision;i=5029"])
o6.reference(o6.ns["ns=machine_vision;i=5032"], "i=53", o6.ns["ns=machine_vision;i=7094"])
o6.reference(o6.ns["ns=machine_vision;i=5032"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5033",
    browseName="ns=machine_vision;PreoperationalToHaltedAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6231", browseName="TransitionNumber", dataType=o6.UInt32, value=120))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5033"])
o6.reference(o6.ns["ns=machine_vision;i=5028"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5033"])
o6.reference(o6.ns["ns=machine_vision;i=5029"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5033"])
o6.reference(o6.ns["ns=machine_vision;i=5033"], "i=51", o6.ns["ns=machine_vision;i=5028"])
o6.reference(o6.ns["ns=machine_vision;i=5033"], "i=52", o6.ns["ns=machine_vision;i=5029"])
o6.reference(o6.ns["ns=machine_vision;i=5033"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5034",
    browseName="ns=machine_vision;PreoperationalToErrorAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6232", browseName="TransitionNumber", dataType=o6.UInt32, value=130))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5034"])
o6.reference(o6.ns["ns=machine_vision;i=5028"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5034"])
o6.reference(o6.ns["ns=machine_vision;i=5030"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5034"])
o6.reference(o6.ns["ns=machine_vision;i=5034"], "i=51", o6.ns["ns=machine_vision;i=5028"])
o6.reference(o6.ns["ns=machine_vision;i=5034"], "i=52", o6.ns["ns=machine_vision;i=5030"])
o6.reference(o6.ns["ns=machine_vision;i=5034"], "i=54", machine_vision_objtypes.StateChangedEventType)
o6.reference(o6.ns["ns=machine_vision;i=5034"], "i=54", machine_vision_objtypes.ErrorEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5035",
    browseName="ns=machine_vision;PreoperationalToInitialized",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6233", browseName="TransitionNumber", dataType=o6.UInt32, value=151))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5035"])
o6.reference(o6.ns["ns=machine_vision;i=5028"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5035"])
o6.reference(o6.ns["ns=machine_vision;i=5035"], "i=51", o6.ns["ns=machine_vision;i=5028"])
o6.reference(o6.ns["ns=machine_vision;i=5035"], "i=53", o6.ns["ns=machine_vision;i=7095"])
o6.reference(o6.ns["ns=machine_vision;i=5035"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5036",
    browseName="ns=machine_vision;PreoperationalToInitializedAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6234", browseName="TransitionNumber", dataType=o6.UInt32, value=150))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5036"])
o6.reference(o6.ns["ns=machine_vision;i=5028"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5036"])
o6.reference(o6.ns["ns=machine_vision;i=5036"], "i=51", o6.ns["ns=machine_vision;i=5028"])
o6.reference(o6.ns["ns=machine_vision;i=5036"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5037",
    browseName="ns=machine_vision;HaltedToPreoperational",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6235", browseName="TransitionNumber", dataType=o6.UInt32, value=211))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5037"])
o6.reference(o6.ns["ns=machine_vision;i=5028"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5037"])
o6.reference(o6.ns["ns=machine_vision;i=5029"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5037"])
o6.reference(o6.ns["ns=machine_vision;i=5037"], "i=51", o6.ns["ns=machine_vision;i=5029"])
o6.reference(o6.ns["ns=machine_vision;i=5037"], "i=52", o6.ns["ns=machine_vision;i=5028"])
o6.reference(o6.ns["ns=machine_vision;i=5037"], "i=53", o6.ns["ns=machine_vision;i=7093"])
o6.reference(o6.ns["ns=machine_vision;i=5037"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5038",
    browseName="ns=machine_vision;HaltedToPreoperationalAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6236", browseName="TransitionNumber", dataType=o6.UInt32, value=210))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5038"])
o6.reference(o6.ns["ns=machine_vision;i=5028"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5038"])
o6.reference(o6.ns["ns=machine_vision;i=5029"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5038"])
o6.reference(o6.ns["ns=machine_vision;i=5038"], "i=51", o6.ns["ns=machine_vision;i=5029"])
o6.reference(o6.ns["ns=machine_vision;i=5038"], "i=52", o6.ns["ns=machine_vision;i=5028"])
o6.reference(o6.ns["ns=machine_vision;i=5038"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5039",
    browseName="ns=machine_vision;ErrorToPreoperational",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6237", browseName="TransitionNumber", dataType=o6.UInt32, value=311))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5039"])
o6.reference(o6.ns["ns=machine_vision;i=5028"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5039"])
o6.reference(o6.ns["ns=machine_vision;i=5030"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5039"])
o6.reference(o6.ns["ns=machine_vision;i=5039"], "i=51", o6.ns["ns=machine_vision;i=5030"])
o6.reference(o6.ns["ns=machine_vision;i=5039"], "i=52", o6.ns["ns=machine_vision;i=5028"])
o6.reference(o6.ns["ns=machine_vision;i=5039"], "i=53", o6.ns["ns=machine_vision;i=7093"])
o6.reference(o6.ns["ns=machine_vision;i=5039"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5040",
    browseName="ns=machine_vision;ErrorToPreoperationalAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6238", browseName="TransitionNumber", dataType=o6.UInt32, value=310))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5040"])
o6.reference(o6.ns["ns=machine_vision;i=5028"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5040"])
o6.reference(o6.ns["ns=machine_vision;i=5030"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5040"])
o6.reference(o6.ns["ns=machine_vision;i=5040"], "i=51", o6.ns["ns=machine_vision;i=5030"])
o6.reference(o6.ns["ns=machine_vision;i=5040"], "i=52", o6.ns["ns=machine_vision;i=5028"])
o6.reference(o6.ns["ns=machine_vision;i=5040"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5041",
    browseName="ns=machine_vision;ErrorToHalted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6239", browseName="TransitionNumber", dataType=o6.UInt32, value=321))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5041"])
o6.reference(o6.ns["ns=machine_vision;i=5029"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5041"])
o6.reference(o6.ns["ns=machine_vision;i=5030"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5041"])
o6.reference(o6.ns["ns=machine_vision;i=5041"], "i=51", o6.ns["ns=machine_vision;i=5030"])
o6.reference(o6.ns["ns=machine_vision;i=5041"], "i=52", o6.ns["ns=machine_vision;i=5029"])
o6.reference(o6.ns["ns=machine_vision;i=5041"], "i=53", o6.ns["ns=machine_vision;i=7094"])
o6.reference(o6.ns["ns=machine_vision;i=5041"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5042",
    browseName="ns=machine_vision;ErrorToHaltedAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6240", browseName="TransitionNumber", dataType=o6.UInt32, value=320))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5042"])
o6.reference(o6.ns["ns=machine_vision;i=5029"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5042"])
o6.reference(o6.ns["ns=machine_vision;i=5030"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5042"])
o6.reference(o6.ns["ns=machine_vision;i=5042"], "i=51", o6.ns["ns=machine_vision;i=5030"])
o6.reference(o6.ns["ns=machine_vision;i=5042"], "i=52", o6.ns["ns=machine_vision;i=5029"])
o6.reference(o6.ns["ns=machine_vision;i=5042"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6139",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6242", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5044",
    browseName="ns=machine_vision;ReadyToInitializedProduct",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6243", browseName="TransitionNumber", dataType=o6.UInt32, value=652))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5044"])
o6.reference(o6.ns["ns=machine_vision;i=5044"], "i=53", o6.ns["ns=machine_vision;i=7059"])
o6.reference(o6.ns["ns=machine_vision;i=5044"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5047",
    browseName="ns=machine_vision;OperationalToPreoperational",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6245", browseName="TransitionNumber", dataType=o6.UInt32, value=411))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5047"])
o6.reference(o6.ns["ns=machine_vision;i=5028"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5047"])
o6.reference(o6.ns["ns=machine_vision;i=5031"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5047"])
o6.reference(o6.ns["ns=machine_vision;i=5047"], "i=51", o6.ns["ns=machine_vision;i=5031"])
o6.reference(o6.ns["ns=machine_vision;i=5047"], "i=52", o6.ns["ns=machine_vision;i=5028"])
o6.reference(o6.ns["ns=machine_vision;i=5047"], "i=53", o6.ns["ns=machine_vision;i=7093"])
o6.reference(o6.ns["ns=machine_vision;i=5047"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5048",
    browseName="ns=machine_vision;OperationalToPreoperationalAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6246", browseName="TransitionNumber", dataType=o6.UInt32, value=410))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5048"])
o6.reference(o6.ns["ns=machine_vision;i=5028"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5048"])
o6.reference(o6.ns["ns=machine_vision;i=5031"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5048"])
o6.reference(o6.ns["ns=machine_vision;i=5048"], "i=51", o6.ns["ns=machine_vision;i=5031"])
o6.reference(o6.ns["ns=machine_vision;i=5048"], "i=52", o6.ns["ns=machine_vision;i=5028"])
o6.reference(o6.ns["ns=machine_vision;i=5048"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5049",
    browseName="ns=machine_vision;OperationalToHalted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6247", browseName="TransitionNumber", dataType=o6.UInt32, value=421))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5049"])
o6.reference(o6.ns["ns=machine_vision;i=5029"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5049"])
o6.reference(o6.ns["ns=machine_vision;i=5031"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5049"])
o6.reference(o6.ns["ns=machine_vision;i=5049"], "i=51", o6.ns["ns=machine_vision;i=5031"])
o6.reference(o6.ns["ns=machine_vision;i=5049"], "i=52", o6.ns["ns=machine_vision;i=5029"])
o6.reference(o6.ns["ns=machine_vision;i=5049"], "i=53", o6.ns["ns=machine_vision;i=7094"])
o6.reference(o6.ns["ns=machine_vision;i=5049"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5050",
    browseName="ns=machine_vision;OperationalToHaltedAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6248", browseName="TransitionNumber", dataType=o6.UInt32, value=420))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5050"])
o6.reference(o6.ns["ns=machine_vision;i=5029"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5050"])
o6.reference(o6.ns["ns=machine_vision;i=5031"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5050"])
o6.reference(o6.ns["ns=machine_vision;i=5050"], "i=51", o6.ns["ns=machine_vision;i=5031"])
o6.reference(o6.ns["ns=machine_vision;i=5050"], "i=52", o6.ns["ns=machine_vision;i=5029"])
o6.reference(o6.ns["ns=machine_vision;i=5050"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5051",
    browseName="ns=machine_vision;OperationalToErrorAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6249", browseName="TransitionNumber", dataType=o6.UInt32, value=430))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5051"])
o6.reference(o6.ns["ns=machine_vision;i=5030"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5051"])
o6.reference(o6.ns["ns=machine_vision;i=5031"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5051"])
o6.reference(o6.ns["ns=machine_vision;i=5051"], "i=51", o6.ns["ns=machine_vision;i=5031"])
o6.reference(o6.ns["ns=machine_vision;i=5051"], "i=52", o6.ns["ns=machine_vision;i=5030"])
o6.reference(o6.ns["ns=machine_vision;i=5051"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6244",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6250", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.objtypes.StateType(
    nodeId="ns=machine_vision;i=5056",
    browseName="ns=machine_vision;Initialized",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6259", browseName="StateNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5056"])
o6.reference(o6.ns["ns=machine_vision;i=5035"], "i=52", o6.ns["ns=machine_vision;i=5056"])
o6.reference(o6.ns["ns=machine_vision;i=5036"], "i=52", o6.ns["ns=machine_vision;i=5056"])
o6.reference(o6.ns["ns=machine_vision;i=5044"], "i=52", o6.ns["ns=machine_vision;i=5056"])
o6.reference(o6.ns["ns=machine_vision;i=5045"], "i=51", o6.ns["ns=machine_vision;i=5056"])
o6.reference(o6.ns["ns=machine_vision;i=5056"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5044"])
o6.reference(o6.ns["ns=machine_vision;i=5056"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5045"])
ns0.objtypes.StateType(
    nodeId="ns=machine_vision;i=5057",
    browseName="ns=machine_vision;Ready",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6260", browseName="StateNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5057"])
o6.reference(o6.ns["ns=machine_vision;i=5044"], "i=51", o6.ns["ns=machine_vision;i=5057"])
o6.reference(o6.ns["ns=machine_vision;i=5045"], "i=52", o6.ns["ns=machine_vision;i=5057"])
o6.reference(o6.ns["ns=machine_vision;i=5057"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5045"])
o6.reference(o6.ns["ns=machine_vision;i=5057"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5044"])
ns0.objtypes.StateType(
    nodeId="ns=machine_vision;i=5058",
    browseName="ns=machine_vision;SingleExecution",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6261", browseName="StateNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5058"])
ns0.objtypes.StateType(
    nodeId="ns=machine_vision;i=5059",
    browseName="ns=machine_vision;ContinuousExecution",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6262", browseName="StateNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5059"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5060",
    browseName="ns=machine_vision;InitializedToReadyRecipe",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6263", browseName="TransitionNumber", dataType=o6.UInt32, value=561))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5060"])
o6.reference(o6.ns["ns=machine_vision;i=5056"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5060"])
o6.reference(o6.ns["ns=machine_vision;i=5057"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5060"])
o6.reference(o6.ns["ns=machine_vision;i=5060"], "i=51", o6.ns["ns=machine_vision;i=5056"])
o6.reference(o6.ns["ns=machine_vision;i=5060"], "i=52", o6.ns["ns=machine_vision;i=5057"])
o6.reference(o6.ns["ns=machine_vision;i=5060"], "i=53", o6.ns["ns=machine_vision;i=7015"])
o6.reference(o6.ns["ns=machine_vision;i=5060"], "i=54", machine_vision_objtypes.StateChangedEventType)
o6.reference(o6.ns["ns=machine_vision;i=5060"], "i=54", machine_vision_objtypes.RecipePreparedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5061",
    browseName="ns=machine_vision;InitializedToReadyAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6264", browseName="TransitionNumber", dataType=o6.UInt32, value=560))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5061"])
o6.reference(o6.ns["ns=machine_vision;i=5056"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5061"])
o6.reference(o6.ns["ns=machine_vision;i=5057"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5061"])
o6.reference(o6.ns["ns=machine_vision;i=5061"], "i=51", o6.ns["ns=machine_vision;i=5056"])
o6.reference(o6.ns["ns=machine_vision;i=5061"], "i=52", o6.ns["ns=machine_vision;i=5057"])
o6.reference(o6.ns["ns=machine_vision;i=5061"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5062",
    browseName="ns=machine_vision;ReadyToInitializedRecipe",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6265", browseName="TransitionNumber", dataType=o6.UInt32, value=651))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5062"])
o6.reference(o6.ns["ns=machine_vision;i=5056"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5062"])
o6.reference(o6.ns["ns=machine_vision;i=5057"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5062"])
o6.reference(o6.ns["ns=machine_vision;i=5062"], "i=51", o6.ns["ns=machine_vision;i=5057"])
o6.reference(o6.ns["ns=machine_vision;i=5062"], "i=52", o6.ns["ns=machine_vision;i=5056"])
o6.reference(o6.ns["ns=machine_vision;i=5062"], "i=53", o6.ns["ns=machine_vision;i=7055"])
o6.reference(o6.ns["ns=machine_vision;i=5062"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5063",
    browseName="ns=machine_vision;ReadyToInitializedAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6266", browseName="TransitionNumber", dataType=o6.UInt32, value=650))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5063"])
o6.reference(o6.ns["ns=machine_vision;i=5056"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5063"])
o6.reference(o6.ns["ns=machine_vision;i=5057"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5063"])
o6.reference(o6.ns["ns=machine_vision;i=5063"], "i=51", o6.ns["ns=machine_vision;i=5057"])
o6.reference(o6.ns["ns=machine_vision;i=5063"], "i=52", o6.ns["ns=machine_vision;i=5056"])
o6.reference(o6.ns["ns=machine_vision;i=5063"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5064",
    browseName="ns=machine_vision;ReadyToSingleExecution",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6267", browseName="TransitionNumber", dataType=o6.UInt32, value=671))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5064"])
o6.reference(o6.ns["ns=machine_vision;i=5057"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5064"])
o6.reference(o6.ns["ns=machine_vision;i=5058"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5064"])
o6.reference(o6.ns["ns=machine_vision;i=5064"], "i=51", o6.ns["ns=machine_vision;i=5057"])
o6.reference(o6.ns["ns=machine_vision;i=5064"], "i=52", o6.ns["ns=machine_vision;i=5058"])
o6.reference(o6.ns["ns=machine_vision;i=5064"], "i=53", o6.ns["ns=machine_vision;i=7098"])
o6.reference(o6.ns["ns=machine_vision;i=5064"], "i=54", machine_vision_objtypes.JobStartedEventType)
o6.reference(o6.ns["ns=machine_vision;i=5064"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5065",
    browseName="ns=machine_vision;ReadyToSingleExecutionAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6268", browseName="TransitionNumber", dataType=o6.UInt32, value=670))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5065"])
o6.reference(o6.ns["ns=machine_vision;i=5057"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5065"])
o6.reference(o6.ns["ns=machine_vision;i=5058"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5065"])
o6.reference(o6.ns["ns=machine_vision;i=5065"], "i=51", o6.ns["ns=machine_vision;i=5057"])
o6.reference(o6.ns["ns=machine_vision;i=5065"], "i=52", o6.ns["ns=machine_vision;i=5058"])
o6.reference(o6.ns["ns=machine_vision;i=5065"], "i=54", machine_vision_objtypes.JobStartedEventType)
o6.reference(o6.ns["ns=machine_vision;i=5065"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5066",
    browseName="ns=machine_vision;ReadyToContinuousExecution",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6269", browseName="TransitionNumber", dataType=o6.UInt32, value=681))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5066"])
o6.reference(o6.ns["ns=machine_vision;i=5057"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5066"])
o6.reference(o6.ns["ns=machine_vision;i=5059"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5066"])
o6.reference(o6.ns["ns=machine_vision;i=5066"], "i=51", o6.ns["ns=machine_vision;i=5057"])
o6.reference(o6.ns["ns=machine_vision;i=5066"], "i=52", o6.ns["ns=machine_vision;i=5059"])
o6.reference(o6.ns["ns=machine_vision;i=5066"], "i=53", o6.ns["ns=machine_vision;i=7009"])
o6.reference(o6.ns["ns=machine_vision;i=5066"], "i=54", machine_vision_objtypes.JobStartedEventType)
o6.reference(o6.ns["ns=machine_vision;i=5066"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5067",
    browseName="ns=machine_vision;ReadyToContinuousExecutionAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6270", browseName="TransitionNumber", dataType=o6.UInt32, value=680))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5067"])
o6.reference(o6.ns["ns=machine_vision;i=5057"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5067"])
o6.reference(o6.ns["ns=machine_vision;i=5059"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5067"])
o6.reference(o6.ns["ns=machine_vision;i=5067"], "i=51", o6.ns["ns=machine_vision;i=5057"])
o6.reference(o6.ns["ns=machine_vision;i=5067"], "i=52", o6.ns["ns=machine_vision;i=5059"])
o6.reference(o6.ns["ns=machine_vision;i=5067"], "i=54", machine_vision_objtypes.JobStartedEventType)
o6.reference(o6.ns["ns=machine_vision;i=5067"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5068",
    browseName="ns=machine_vision;SingleExecutionToReadyStop",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6271", browseName="TransitionNumber", dataType=o6.UInt32, value=761))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5068"])
o6.reference(o6.ns["ns=machine_vision;i=5057"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5068"])
o6.reference(o6.ns["ns=machine_vision;i=5058"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5068"])
o6.reference(o6.ns["ns=machine_vision;i=5068"], "i=51", o6.ns["ns=machine_vision;i=5058"])
o6.reference(o6.ns["ns=machine_vision;i=5068"], "i=52", o6.ns["ns=machine_vision;i=5057"])
o6.reference(o6.ns["ns=machine_vision;i=5068"], "i=53", o6.ns["ns=machine_vision;i=7096"])
o6.reference(o6.ns["ns=machine_vision;i=5068"], "i=54", machine_vision_objtypes.StateChangedEventType)
o6.reference(o6.ns["ns=machine_vision;i=5068"], "i=54", machine_vision_objtypes.ReadyEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5069",
    browseName="ns=machine_vision;SingleExecutionToReadyAbort",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6272", browseName="TransitionNumber", dataType=o6.UInt32, value=762))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5069"])
o6.reference(o6.ns["ns=machine_vision;i=5057"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5069"])
o6.reference(o6.ns["ns=machine_vision;i=5058"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5069"])
o6.reference(o6.ns["ns=machine_vision;i=5069"], "i=51", o6.ns["ns=machine_vision;i=5058"])
o6.reference(o6.ns["ns=machine_vision;i=5069"], "i=52", o6.ns["ns=machine_vision;i=5057"])
o6.reference(o6.ns["ns=machine_vision;i=5069"], "i=53", o6.ns["ns=machine_vision;i=7097"])
o6.reference(o6.ns["ns=machine_vision;i=5069"], "i=54", machine_vision_objtypes.StateChangedEventType)
o6.reference(o6.ns["ns=machine_vision;i=5069"], "i=54", machine_vision_objtypes.ReadyEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5070",
    browseName="ns=machine_vision;SingleExecutionToReadyAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6273", browseName="TransitionNumber", dataType=o6.UInt32, value=760))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5070"])
o6.reference(o6.ns["ns=machine_vision;i=5057"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5070"])
o6.reference(o6.ns["ns=machine_vision;i=5058"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5070"])
o6.reference(o6.ns["ns=machine_vision;i=5070"], "i=51", o6.ns["ns=machine_vision;i=5058"])
o6.reference(o6.ns["ns=machine_vision;i=5070"], "i=52", o6.ns["ns=machine_vision;i=5057"])
o6.reference(o6.ns["ns=machine_vision;i=5070"], "i=54", machine_vision_objtypes.StateChangedEventType)
o6.reference(o6.ns["ns=machine_vision;i=5070"], "i=54", machine_vision_objtypes.ReadyEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5071",
    browseName="ns=machine_vision;ContinuousExecutionToReadyStop",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6274", browseName="TransitionNumber", dataType=o6.UInt32, value=861))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5071"])
o6.reference(o6.ns["ns=machine_vision;i=5057"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5071"])
o6.reference(o6.ns["ns=machine_vision;i=5059"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5071"])
o6.reference(o6.ns["ns=machine_vision;i=5071"], "i=51", o6.ns["ns=machine_vision;i=5059"])
o6.reference(o6.ns["ns=machine_vision;i=5071"], "i=52", o6.ns["ns=machine_vision;i=5057"])
o6.reference(o6.ns["ns=machine_vision;i=5071"], "i=53", o6.ns["ns=machine_vision;i=7096"])
o6.reference(o6.ns["ns=machine_vision;i=5071"], "i=54", machine_vision_objtypes.StateChangedEventType)
o6.reference(o6.ns["ns=machine_vision;i=5071"], "i=54", machine_vision_objtypes.ReadyEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5072",
    browseName="ns=machine_vision;ContinuousExecutionToReadyAbort",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6275", browseName="TransitionNumber", dataType=o6.UInt32, value=862))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5072"])
o6.reference(o6.ns["ns=machine_vision;i=5057"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5072"])
o6.reference(o6.ns["ns=machine_vision;i=5059"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5072"])
o6.reference(o6.ns["ns=machine_vision;i=5072"], "i=51", o6.ns["ns=machine_vision;i=5059"])
o6.reference(o6.ns["ns=machine_vision;i=5072"], "i=52", o6.ns["ns=machine_vision;i=5057"])
o6.reference(o6.ns["ns=machine_vision;i=5072"], "i=53", o6.ns["ns=machine_vision;i=7097"])
o6.reference(o6.ns["ns=machine_vision;i=5072"], "i=54", machine_vision_objtypes.StateChangedEventType)
o6.reference(o6.ns["ns=machine_vision;i=5072"], "i=54", machine_vision_objtypes.ReadyEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5073",
    browseName="ns=machine_vision;ContinuousExecutionToReadyAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6276", browseName="TransitionNumber", dataType=o6.UInt32, value=860))],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5073"])
o6.reference(o6.ns["ns=machine_vision;i=5057"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5073"])
o6.reference(o6.ns["ns=machine_vision;i=5059"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5073"])
o6.reference(o6.ns["ns=machine_vision;i=5073"], "i=51", o6.ns["ns=machine_vision;i=5059"])
o6.reference(o6.ns["ns=machine_vision;i=5073"], "i=52", o6.ns["ns=machine_vision;i=5057"])
o6.reference(o6.ns["ns=machine_vision;i=5073"], "i=54", machine_vision_objtypes.StateChangedEventType)
o6.reference(o6.ns["ns=machine_vision;i=5073"], "i=54", machine_vision_objtypes.ReadyEventType)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6277",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6278", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.objtypes.InitialStateType(
    nodeId="ns=machine_vision;i=5078",
    browseName="ns=machine_vision;Entry",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6309", browseName="StateNumber", dataType=o6.UInt32, value=11))],
)
o6.reference(machine_vision_objtypes.VisionStepModelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5078"])
ns0.objtypes.StateType(
    nodeId="ns=machine_vision;i=5079",
    browseName="ns=machine_vision;Exit",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6310", browseName="StateNumber", dataType=o6.UInt32, value=12))],
)
o6.reference(machine_vision_objtypes.VisionStepModelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5079"])
ns0.objtypes.StateType(
    nodeId="ns=machine_vision;i=5080",
    browseName="ns=machine_vision;Wait",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6311", browseName="StateNumber", dataType=o6.UInt32, value=13))],
)
o6.reference(machine_vision_objtypes.VisionStepModelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5080"])
ns0.objtypes.StateType(
    nodeId="ns=machine_vision;i=5081",
    browseName="ns=machine_vision;Step",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6312", browseName="StateNumber", dataType=o6.UInt32, value=14))],
)
o6.reference(machine_vision_objtypes.VisionStepModelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5081"])
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5082",
    browseName="ns=machine_vision;EntryToExitAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6313", browseName="TransitionNumber", dataType=o6.UInt32, value=11120))],
)
o6.reference(machine_vision_objtypes.VisionStepModelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5082"])
o6.reference(o6.ns["ns=machine_vision;i=5078"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5082"])
o6.reference(o6.ns["ns=machine_vision;i=5079"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5082"])
o6.reference(o6.ns["ns=machine_vision;i=5082"], "i=51", o6.ns["ns=machine_vision;i=5078"])
o6.reference(o6.ns["ns=machine_vision;i=5082"], "i=52", o6.ns["ns=machine_vision;i=5079"])
o6.reference(o6.ns["ns=machine_vision;i=5082"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5083",
    browseName="ns=machine_vision;EntryToWaitAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6314", browseName="TransitionNumber", dataType=o6.UInt32, value=11130))],
)
o6.reference(machine_vision_objtypes.VisionStepModelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5083"])
o6.reference(o6.ns["ns=machine_vision;i=5078"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5083"])
o6.reference(o6.ns["ns=machine_vision;i=5080"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5083"])
o6.reference(o6.ns["ns=machine_vision;i=5083"], "i=51", o6.ns["ns=machine_vision;i=5078"])
o6.reference(o6.ns["ns=machine_vision;i=5083"], "i=52", o6.ns["ns=machine_vision;i=5080"])
o6.reference(o6.ns["ns=machine_vision;i=5083"], "i=54", machine_vision_objtypes.StateChangedEventType)
o6.reference(o6.ns["ns=machine_vision;i=5083"], "i=54", machine_vision_objtypes.EnterStepSequenceEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5084",
    browseName="ns=machine_vision;WaitToStep",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6315", browseName="TransitionNumber", dataType=o6.UInt32, value=13141))],
)
o6.reference(machine_vision_objtypes.VisionStepModelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5084"])
o6.reference(o6.ns["ns=machine_vision;i=5080"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5084"])
o6.reference(o6.ns["ns=machine_vision;i=5081"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5084"])
o6.reference(o6.ns["ns=machine_vision;i=5084"], "i=51", o6.ns["ns=machine_vision;i=5080"])
o6.reference(o6.ns["ns=machine_vision;i=5084"], "i=52", o6.ns["ns=machine_vision;i=5081"])
o6.reference(o6.ns["ns=machine_vision;i=5084"], "i=53", o6.ns["ns=machine_vision;i=7101"])
o6.reference(o6.ns["ns=machine_vision;i=5084"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5085",
    browseName="ns=machine_vision;WaitToStepAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6316", browseName="TransitionNumber", dataType=o6.UInt32, value=13140))],
)
o6.reference(machine_vision_objtypes.VisionStepModelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5085"])
o6.reference(o6.ns["ns=machine_vision;i=5080"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5085"])
o6.reference(o6.ns["ns=machine_vision;i=5081"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5085"])
o6.reference(o6.ns["ns=machine_vision;i=5085"], "i=51", o6.ns["ns=machine_vision;i=5080"])
o6.reference(o6.ns["ns=machine_vision;i=5085"], "i=52", o6.ns["ns=machine_vision;i=5081"])
o6.reference(o6.ns["ns=machine_vision;i=5085"], "i=54", machine_vision_objtypes.StateChangedEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5086",
    browseName="ns=machine_vision;StepToWaitAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6317", browseName="TransitionNumber", dataType=o6.UInt32, value=14130))],
)
o6.reference(machine_vision_objtypes.VisionStepModelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5086"])
o6.reference(o6.ns["ns=machine_vision;i=5080"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5086"])
o6.reference(o6.ns["ns=machine_vision;i=5081"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5086"])
o6.reference(o6.ns["ns=machine_vision;i=5086"], "i=51", o6.ns["ns=machine_vision;i=5081"])
o6.reference(o6.ns["ns=machine_vision;i=5086"], "i=52", o6.ns["ns=machine_vision;i=5080"])
o6.reference(o6.ns["ns=machine_vision;i=5086"], "i=54", machine_vision_objtypes.StateChangedEventType)
o6.reference(o6.ns["ns=machine_vision;i=5086"], "i=54", machine_vision_objtypes.NextStepEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5087",
    browseName="ns=machine_vision;StepToExitAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6318", browseName="TransitionNumber", dataType=o6.UInt32, value=14120))],
)
o6.reference(machine_vision_objtypes.VisionStepModelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5087"])
o6.reference(o6.ns["ns=machine_vision;i=5079"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5087"])
o6.reference(o6.ns["ns=machine_vision;i=5081"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5087"])
o6.reference(o6.ns["ns=machine_vision;i=5087"], "i=51", o6.ns["ns=machine_vision;i=5081"])
o6.reference(o6.ns["ns=machine_vision;i=5087"], "i=52", o6.ns["ns=machine_vision;i=5079"])
o6.reference(o6.ns["ns=machine_vision;i=5087"], "i=54", machine_vision_objtypes.StateChangedEventType)
o6.reference(o6.ns["ns=machine_vision;i=5087"], "i=54", machine_vision_objtypes.LeaveStepSequenceEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=machine_vision;i=5255",
    browseName="ns=machine_vision;ErrorToOperationalAuto",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6341", browseName="TransitionNumber", dataType=o6.UInt32, value=340))],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5255"])
o6.reference(o6.ns["ns=machine_vision;i=5030"], "ns=machine_vision;i=4003", o6.ns["ns=machine_vision;i=5255"])
o6.reference(o6.ns["ns=machine_vision;i=5031"], "ns=machine_vision;i=4002", o6.ns["ns=machine_vision;i=5255"])
o6.reference(o6.ns["ns=machine_vision;i=5255"], "i=51", o6.ns["ns=machine_vision;i=5030"])
o6.reference(o6.ns["ns=machine_vision;i=5255"], "i=52", o6.ns["ns=machine_vision;i=5031"])
o6.reference(o6.ns["ns=machine_vision;i=5255"], "i=54", machine_vision_objtypes.StateChangedEventType)
o6.reference(o6.ns["ns=machine_vision;i=5255"], "i=54", machine_vision_objtypes.ErrorResolvedEventType)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=machine_vision;i=6352", browseName="ns=machine_vision;ConfigurationDataType", dataType=o6.String, value="ConfigurationDataType")
o6.reference(o6.ns["ns=machine_vision;i=5088"], "i=39", o6.ns["ns=machine_vision;i=6352"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6353", browseName="ns=machine_vision;ConfigurationDataType", dataType=o6.String, value="//xs:element[@name='ConfigurationDataType']"
)
o6.reference(o6.ns["ns=machine_vision;i=5089"], "i=39", o6.ns["ns=machine_vision;i=6353"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=machine_vision;i=6354", browseName="ns=machine_vision;ConfigurationIdDataType", dataType=o6.String, value="ConfigurationIdDataType")
o6.reference(o6.ns["ns=machine_vision;i=5090"], "i=39", o6.ns["ns=machine_vision;i=6354"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=machine_vision;i=6001",
    browseName="ns=machine_vision;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/MachineVision",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6002", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/MachineVision")
        ),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6021"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6028"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6030"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6033"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6035"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6037"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6039"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6071"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6072"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6074"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6076"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6125"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6127"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6130"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6188"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6352"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6354"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/MachineVision" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/MachineVision">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BinaryIdBaseDataType">\n  <opc:Field TypeName="opc:Bit" Name="VersionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="HashSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="HashAlgorithmSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field Length="28" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="Id"/>\n  <opc:Field SwitchField="VersionSpecified" TypeName="opc:CharArray" Name="Version"/>\n  <opc:Field SwitchField="HashSpecified" TypeName="opc:ByteString" Name="Hash"/>\n  <opc:Field SwitchField="HashAlgorithmSpecified" TypeName="opc:CharArray" Name="HashAlgorithm"/>\n  <opc:Field SwitchField="DescriptionSpecified" TypeName="ua:LocalizedText" Name="Description"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:BinaryIdBaseDataType" Name="ConfigurationIdDataType">\n  <opc:Field TypeName="opc:Bit" Name="VersionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="HashSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="HashAlgorithmSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field Length="28" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field SourceType="tns:BinaryIdBaseDataType" TypeName="opc:CharArray" Name="Id"/>\n  <opc:Field SwitchField="VersionSpecified" SourceType="tns:BinaryIdBaseDataType" TypeName="opc:CharArray" Name="Version"/>\n  <opc:Field SwitchField="HashSpecified" SourceType="tns:BinaryIdBaseDataType" TypeName="opc:ByteString" Name="Hash"/>\n  <opc:Field SwitchField="HashAlgorithmSpecified" SourceType="tns:BinaryIdBaseDataType" TypeName="opc:CharArray" Name="HashAlgorithm"/>\n  <opc:Field SwitchField="DescriptionSpecified" SourceType="tns:BinaryIdBaseDataType" TypeName="ua:LocalizedText" Name="Description"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:BinaryIdBaseDataType" Name="RecipeIdExternalDataType">\n  <opc:Field TypeName="opc:Bit" Name="VersionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="HashSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="HashAlgorithmSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field Length="28" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field SourceType="tns:BinaryIdBaseDataType" TypeName="opc:CharArray" Name="Id"/>\n  <opc:Field SwitchField="VersionSpecified" SourceType="tns:BinaryIdBaseDataType" TypeName="opc:CharArray" Name="Version"/>\n  <opc:Field SwitchField="HashSpecified" SourceType="tns:BinaryIdBaseDataType" TypeName="opc:ByteString" Name="Hash"/>\n  <opc:Field SwitchField="HashAlgorithmSpecified" SourceType="tns:BinaryIdBaseDataType" TypeName="opc:CharArray" Name="HashAlgorithm"/>\n  <opc:Field SwitchField="DescriptionSpecified" SourceType="tns:BinaryIdBaseDataType" TypeName="ua:LocalizedText" Name="Description"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:BinaryIdBaseDataType" Name="RecipeIdInternalDataType">\n  <opc:Field TypeName="opc:Bit" Name="VersionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="HashSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="HashAlgorithmSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field Length="28" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field SourceType="tns:BinaryIdBaseDataType" TypeName="opc:CharArray" Name="Id"/>\n  <opc:Field SwitchField="VersionSpecified" SourceType="tns:BinaryIdBaseDataType" TypeName="opc:CharArray" Name="Version"/>\n  <opc:Field SwitchField="HashSpecified" SourceType="tns:BinaryIdBaseDataType" TypeName="opc:ByteString" Name="Hash"/>\n  <opc:Field SwitchField="HashAlgorithmSpecified" SourceType="tns:BinaryIdBaseDataType" TypeName="opc:CharArray" Name="HashAlgorithm"/>\n  <opc:Field SwitchField="DescriptionSpecified" SourceType="tns:BinaryIdBaseDataType" TypeName="ua:LocalizedText" Name="Description"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ConfigurationDataType">\n  <opc:Field TypeName="opc:Bit" Name="HasTransferableDataOnFileSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ExternalIdSpecified"/>\n  <opc:Field Length="30" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field SwitchField="HasTransferableDataOnFileSpecified" TypeName="opc:Boolean" Name="HasTransferableDataOnFile"/>\n  <opc:Field SwitchField="ExternalIdSpecified" TypeName="tns:ConfigurationIdDataType" Name="ExternalId"/>\n  <opc:Field TypeName="tns:ConfigurationIdDataType" Name="InternalId"/>\n  <opc:Field TypeName="opc:DateTime" Name="LastModified"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ConfigurationTransferOptions">\n  <opc:Field TypeName="tns:ConfigurationIdDataType" Name="InternalId"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="JobIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="Id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="MeasIdDataType">\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field Length="31" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="Id"/>\n  <opc:Field SwitchField="DescriptionSpecified" TypeName="ua:LocalizedText" Name="Description"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="PartIdDataType">\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field Length="31" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="Id"/>\n  <opc:Field SwitchField="DescriptionSpecified" TypeName="ua:LocalizedText" Name="Description"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ProcessingTimesDataType">\n  <opc:Field TypeName="opc:Bit" Name="AcquisitionDurationSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ProcessingDurationSpecified"/>\n  <opc:Field Length="30" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:DateTime" Name="StartTime"/>\n  <opc:Field TypeName="opc:DateTime" Name="EndTime"/>\n  <opc:Field SwitchField="AcquisitionDurationSpecified" TypeName="opc:Double" Name="AcquisitionDuration"/>\n  <opc:Field SwitchField="ProcessingDurationSpecified" TypeName="opc:Double" Name="ProcessingDuration"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ProductDataType">\n  <opc:Field TypeName="tns:ProductIdDataType" Name="ExternalId"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ProductIdDataType">\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field Length="31" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="Id"/>\n  <opc:Field SwitchField="DescriptionSpecified" TypeName="ua:LocalizedText" Name="Description"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RecipeTransferOptions">\n  <opc:Field TypeName="tns:RecipeIdInternalDataType" Name="InternalId"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ResultDataType">\n  <opc:Field TypeName="opc:Bit" Name="HasTransferableDataOnFileSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="IsSimulatedSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="MeasIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PartIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ExternalRecipeIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ProductIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ExternalConfigurationIdSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ProcessingTimesSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ResultContentSpecified"/>\n  <opc:Field Length="23" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="tns:ResultIdDataType" Name="ResultId"/>\n  <opc:Field SwitchField="HasTransferableDataOnFileSpecified" TypeName="opc:Boolean" Name="HasTransferableDataOnFile"/>\n  <opc:Field TypeName="opc:Boolean" Name="IsPartial"/>\n  <opc:Field SwitchField="IsSimulatedSpecified" TypeName="opc:Boolean" Name="IsSimulated"/>\n  <opc:Field TypeName="opc:Int32" Name="ResultState"/>\n  <opc:Field SwitchField="MeasIdSpecified" TypeName="tns:MeasIdDataType" Name="MeasId"/>\n  <opc:Field SwitchField="PartIdSpecified" TypeName="tns:PartIdDataType" Name="PartId"/>\n  <opc:Field SwitchField="ExternalRecipeIdSpecified" TypeName="tns:RecipeIdExternalDataType" Name="ExternalRecipeId"/>\n  <opc:Field TypeName="tns:RecipeIdInternalDataType" Name="InternalRecipeId"/>\n  <opc:Field SwitchField="ProductIdSpecified" TypeName="tns:ProductIdDataType" Name="ProductId"/>\n  <opc:Field SwitchField="ExternalConfigurationIdSpecified" TypeName="tns:ConfigurationIdDataType" Name="ExternalConfigurationId"/>\n  <opc:Field TypeName="tns:ConfigurationIdDataType" Name="InternalConfigurationId"/>\n  <opc:Field TypeName="tns:JobIdDataType" Name="JobId"/>\n  <opc:Field TypeName="opc:DateTime" Name="CreationTime"/>\n  <opc:Field SwitchField="ProcessingTimesSpecified" TypeName="tns:ProcessingTimesDataType" Name="ProcessingTimes"/>\n  <opc:Field SwitchField="ResultContentSpecified" TypeName="opc:Int32" Name="NoOfResultContent"/>\n  <opc:Field LengthField="NoOfResultContent" SwitchField="ResultContentSpecified" TypeName="ua:Variant" Name="ResultContent"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ResultIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="Id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ResultTransferOptions">\n  <opc:Field TypeName="tns:ResultIdDataType" Name="Id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="SystemStateDescriptionDataType">\n  <opc:Field TypeName="opc:Bit" Name="StateDescriptionSpecified"/>\n  <opc:Field Length="31" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="tns:SystemStateDataType" Name="State"/>\n  <opc:Field SwitchField="StateDescriptionSpecified" TypeName="opc:CharArray" Name="StateDescription"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="SystemStateDataType">\n  <opc:EnumeratedValue Name="PRD_1" Value="1"/>\n  <opc:EnumeratedValue Name="SBY_2" Value="2"/>\n  <opc:EnumeratedValue Name="ENG_3" Value="3"/>\n  <opc:EnumeratedValue Name="SDT_4" Value="4"/>\n  <opc:EnumeratedValue Name="UDT_5" Value="5"/>\n  <opc:EnumeratedValue Name="NST_6" Value="6"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="TriStateBooleanDataType">\n  <opc:EnumeratedValue Name="FALSE_0" Value="0"/>\n  <opc:EnumeratedValue Name="TRUE_1" Value="1"/>\n  <opc:EnumeratedValue Name="DONTCARE_2" Value="2"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=machine_vision;i=6355", browseName="ns=machine_vision;ConfigurationIdDataType", dataType=o6.String, value="//xs:element[@name='ConfigurationIdDataType']"
)
o6.reference(o6.ns["ns=machine_vision;i=5091"], "i=39", o6.ns["ns=machine_vision;i=6355"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=machine_vision;i=6003",
    browseName="ns=machine_vision;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/MachineVision",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6020", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/MachineVision/Types.xsd")
        ),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6022"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6029"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6031"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6034"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6036"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6038"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6040"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6073"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6075"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6077"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6093"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6126"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6128"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6131"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6189"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6353"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6355"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/MachineVision/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/MachineVision/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="SystemStateDataType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="PRD_1_1"/>\n   <xs:enumeration value="SBY_2_2"/>\n   <xs:enumeration value="ENG_3_3"/>\n   <xs:enumeration value="SDT_4_4"/>\n   <xs:enumeration value="UDT_5_5"/>\n   <xs:enumeration value="NST_6_6"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SystemStateDataType" name="SystemStateDataType"/>\n <xs:complexType name="ListOfSystemStateDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SystemStateDataType" name="SystemStateDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSystemStateDataType" name="ListOfSystemStateDataType" nillable="true"/>\n <xs:simpleType name="TriStateBooleanDataType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="FALSE_0_0"/>\n   <xs:enumeration value="TRUE_1_1"/>\n   <xs:enumeration value="DONTCARE_2_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:TriStateBooleanDataType" name="TriStateBooleanDataType"/>\n <xs:complexType name="ListOfTriStateBooleanDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:TriStateBooleanDataType" name="TriStateBooleanDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfTriStateBooleanDataType" name="ListOfTriStateBooleanDataType" nillable="true"/>\n <xs:complexType name="BinaryIdBaseDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Id"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Version"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:base64Binary" name="Hash"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="HashAlgorithm"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="Description"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BinaryIdBaseDataType" name="BinaryIdBaseDataType"/>\n <xs:complexType name="ListOfBinaryIdBaseDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BinaryIdBaseDataType" name="BinaryIdBaseDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBinaryIdBaseDataType" name="ListOfBinaryIdBaseDataType" nillable="true"/>\n <xs:complexType name="ConfigurationIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:BinaryIdBaseDataType">\n    <xs:sequence/>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:ConfigurationIdDataType" name="ConfigurationIdDataType"/>\n <xs:complexType name="ListOfConfigurationIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ConfigurationIdDataType" name="ConfigurationIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfConfigurationIdDataType" name="ListOfConfigurationIdDataType" nillable="true"/>\n <xs:complexType name="RecipeIdExternalDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:BinaryIdBaseDataType">\n    <xs:sequence/>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:RecipeIdExternalDataType" name="RecipeIdExternalDataType"/>\n <xs:complexType name="ListOfRecipeIdExternalDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RecipeIdExternalDataType" name="RecipeIdExternalDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRecipeIdExternalDataType" name="ListOfRecipeIdExternalDataType" nillable="true"/>\n <xs:complexType name="RecipeIdInternalDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:BinaryIdBaseDataType">\n    <xs:sequence/>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:RecipeIdInternalDataType" name="RecipeIdInternalDataType"/>\n <xs:complexType name="ListOfRecipeIdInternalDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RecipeIdInternalDataType" name="RecipeIdInternalDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRecipeIdInternalDataType" name="ListOfRecipeIdInternalDataType" nillable="true"/>\n <xs:complexType name="ConfigurationDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="HasTransferableDataOnFile"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ConfigurationIdDataType" name="ExternalId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ConfigurationIdDataType" name="InternalId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="LastModified"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ConfigurationDataType" name="ConfigurationDataType"/>\n <xs:complexType name="ListOfConfigurationDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ConfigurationDataType" name="ConfigurationDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfConfigurationDataType" name="ListOfConfigurationDataType" nillable="true"/>\n <xs:complexType name="ConfigurationTransferOptions">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ConfigurationIdDataType" name="InternalId"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ConfigurationTransferOptions" name="ConfigurationTransferOptions"/>\n <xs:complexType name="ListOfConfigurationTransferOptions">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ConfigurationTransferOptions" name="ConfigurationTransferOptions" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfConfigurationTransferOptions" name="ListOfConfigurationTransferOptions" nillable="true"/>\n <xs:complexType name="JobIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Id"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:JobIdDataType" name="JobIdDataType"/>\n <xs:complexType name="ListOfJobIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:JobIdDataType" name="JobIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfJobIdDataType" name="ListOfJobIdDataType" nillable="true"/>\n <xs:complexType name="MeasIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Id"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="Description"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:MeasIdDataType" name="MeasIdDataType"/>\n <xs:complexType name="ListOfMeasIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:MeasIdDataType" name="MeasIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfMeasIdDataType" name="ListOfMeasIdDataType" nillable="true"/>\n <xs:complexType name="PartIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Id"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="Description"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:PartIdDataType" name="PartIdDataType"/>\n <xs:complexType name="ListOfPartIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PartIdDataType" name="PartIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPartIdDataType" name="ListOfPartIdDataType" nillable="true"/>\n <xs:complexType name="ProcessingTimesDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="StartTime"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="EndTime"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="AcquisitionDuration"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="ProcessingDuration"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ProcessingTimesDataType" name="ProcessingTimesDataType"/>\n <xs:complexType name="ListOfProcessingTimesDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ProcessingTimesDataType" name="ProcessingTimesDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfProcessingTimesDataType" name="ListOfProcessingTimesDataType" nillable="true"/>\n <xs:complexType name="ProductDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ProductIdDataType" name="ExternalId"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ProductDataType" name="ProductDataType"/>\n <xs:complexType name="ListOfProductDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ProductDataType" name="ProductDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfProductDataType" name="ListOfProductDataType" nillable="true"/>\n <xs:complexType name="ProductIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Id"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="Description"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ProductIdDataType" name="ProductIdDataType"/>\n <xs:complexType name="ListOfProductIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ProductIdDataType" name="ProductIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfProductIdDataType" name="ListOfProductIdDataType" nillable="true"/>\n <xs:complexType name="RecipeTransferOptions">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RecipeIdInternalDataType" name="InternalId"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RecipeTransferOptions" name="RecipeTransferOptions"/>\n <xs:complexType name="ListOfRecipeTransferOptions">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RecipeTransferOptions" name="RecipeTransferOptions" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRecipeTransferOptions" name="ListOfRecipeTransferOptions" nillable="true"/>\n <xs:complexType name="ResultDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ResultIdDataType" name="ResultId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="HasTransferableDataOnFile"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="IsPartial"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="IsSimulated"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="ResultState"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:MeasIdDataType" name="MeasId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:PartIdDataType" name="PartId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RecipeIdExternalDataType" name="ExternalRecipeId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:RecipeIdInternalDataType" name="InternalRecipeId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ProductIdDataType" name="ProductId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ConfigurationIdDataType" name="ExternalConfigurationId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ConfigurationIdDataType" name="InternalConfigurationId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:JobIdDataType" name="JobId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="CreationTime"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ProcessingTimesDataType" name="ProcessingTimes"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfVariant" name="ResultContent"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ResultDataType" name="ResultDataType"/>\n <xs:complexType name="ListOfResultDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ResultDataType" name="ResultDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfResultDataType" name="ListOfResultDataType" nillable="true"/>\n <xs:complexType name="ResultIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Id"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ResultIdDataType" name="ResultIdDataType"/>\n <xs:complexType name="ListOfResultIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ResultIdDataType" name="ResultIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfResultIdDataType" name="ListOfResultIdDataType" nillable="true"/>\n <xs:complexType name="ResultTransferOptions">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ResultIdDataType" name="Id"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ResultTransferOptions" name="ResultTransferOptions"/>\n <xs:complexType name="ListOfResultTransferOptions">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ResultTransferOptions" name="ResultTransferOptions" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfResultTransferOptions" name="ListOfResultTransferOptions" nillable="true"/>\n <xs:complexType name="SystemStateDescriptionDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:SystemStateDataType" name="State"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="StateDescription"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:SystemStateDescriptionDataType" name="SystemStateDescriptionDataType"/>\n <xs:complexType name="ListOfSystemStateDescriptionDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SystemStateDescriptionDataType" name="SystemStateDescriptionDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSystemStateDescriptionDataType" name="ListOfSystemStateDescriptionDataType" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6367",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=3014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("FALSE_0"), description=o6.LocalizedText("The filtering function shall look for entities where the filtered value is FALSE.")
        ),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("TRUE_1"), description=o6.LocalizedText("The filtering function shall look for entities where the filtered value is TRUE.")
        ),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("DONTCARE_2"), description=o6.LocalizedText("The filtering function shall not take the value into account.")
        ),
    ],
)
machine_vision_objtypes.ProductFolderType(
    nodeId="ns=machine_vision;i=5095",
    browseName="ns=machine_vision;Products",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision;i=6373", browseName="ns=machine_vision;<Product>", dataType=machine_vision_datypes.ProductDataType, accessLevel=3, userAccessLevel=1
            )
        )
    ],
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6358",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6390", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6401",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6402", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6407",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6408", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.objtypes.StateType(
    nodeId="ns=machine_vision;i=5101",
    browseName="ns=machine_vision;Preoperational",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6415", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6416",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6417", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6420",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6421", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6424",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6425", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machine_vision;i=6430",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6431", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.objtypes.StateType(
    nodeId="ns=machine_vision;i=5106",
    browseName="ns=machine_vision;Halted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6434", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
ns0.objtypes.StateType(
    nodeId="ns=machine_vision;i=5107",
    browseName="ns=machine_vision;Error",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6435", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
ns0.objtypes.StateType(
    nodeId="ns=machine_vision;i=5108",
    browseName="ns=machine_vision;Operational",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6436", browseName="StateNumber", dataType=o6.UInt32, value=4))],
)
machine_vision_vartypes.ResultType(
    nodeId="ns=machine_vision;i=6168",
    browseName="ns=machine_vision;<ResultVariable>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision;i=6334", browseName="ns=machine_vision;CreationTime", dataType=ns0.datatypes.UtcTime, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision;i=6335",
                browseName="ns=machine_vision;InternalConfigurationId",
                dataType=machine_vision_datypes.ConfigurationIdDataType,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision;i=6336",
                browseName="ns=machine_vision;InternalRecipeId",
                dataType=machine_vision_datypes.RecipeIdInternalDataType,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_vision;i=6356", browseName="ns=machine_vision;IsPartial", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision;i=6357", browseName="ns=machine_vision;JobId", dataType=machine_vision_datypes.JobIdDataType, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision;i=6379", browseName="ns=machine_vision;ResultId", dataType=machine_vision_datypes.ResultIdDataType, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision;i=6548", browseName="ns=machine_vision;ResultState", dataType=machine_vision_datypes.ResultStateDataType, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
    dataType=machine_vision_datypes.ResultDataType,
    value=machine_vision_datypes.ResultDataType(
        resultId=machine_vision_datypes.ResultIdDataType(id=""),
        hasTransferableDataOnFile=None,
        isPartial=False,
        isSimulated=None,
        resultState=0,
        measId=None,
        partId=None,
        externalRecipeId=None,
        internalRecipeId=machine_vision_datypes.RecipeIdInternalDataType(id="", version=None, hash=None, hashAlgorithm=None, description=None),
        productId=None,
        externalConfigurationId=None,
        internalConfigurationId=machine_vision_datypes.ConfigurationIdDataType(id="", version=None, hash=None, hashAlgorithm=None, description=None),
        jobId=machine_vision_datypes.JobIdDataType(id=""),
        creationTime=o6.DateTime("1900-01-01T00:00:00Z"),
        processingTimes=None,
        resultContent=[],
    ),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machine_vision_objtypes.ResultFolderType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=6168"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMachineVision = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=machine_vision;i=5009",
    browseName="ns=machine_vision;http://opcfoundation.org/UA/MachineVision",
    description="Provides the metadata for a namespace used by the server.",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision;i=6549",
                browseName="IsNamespaceSubset",
                description="If TRUE then the server only supports a subset of the namespace.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision;i=6552",
                browseName="NamespacePublicationDate",
                description="The publication date for the namespace.",
                dataType=o6.DateTime,
                value=o6.DateTime("2019-07-11T10:18:27Z"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision;i=6553",
                browseName="NamespaceUri",
                description="The URI of the namespace.",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/MachineVision",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision;i=6554",
                browseName="NamespaceVersion",
                description="The human readable string representing version of the namespace.",
                dataType=o6.String,
                value="1.0.0",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision;i=6556",
                browseName="StaticNodeIdTypes",
                description="A list of IdTypes for nodes which are the same in every server that exposes them.",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision;i=6558",
                browseName="StaticNumericNodeIdRange",
                description="A list of ranges for numeric node ids which are the same in every server that exposes them.",
                dataType=ns0.datatypes.NumericRange,
                valueRank=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision;i=6559",
                browseName="StaticStringNodeIdPattern",
                description="A regular expression which matches string node ids are the same in every server that exposes them.",
                dataType=o6.String,
            )
        ),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
machine_vision_objtypes.ProductFolderType(
    nodeId="ns=machine_vision;i=5022",
    browseName="ns=machine_vision;Products",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision;i=6622", browseName="ns=machine_vision;<Product>", dataType=machine_vision_datypes.ProductDataType, accessLevel=3, userAccessLevel=1
            )
        )
    ],
)
o6.reference(machine_vision_objtypes.RecipeManagementType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5022"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6004",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=machine_vision;i=7001", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6004"]))

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6005",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6006",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7002",
    browseName="GetPosition",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6005"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6006"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6007",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6008",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7003", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6007"]), outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6008"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6010",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6011",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7004", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6010"]), outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6011"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6012",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=machine_vision;i=7005", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6012"]))

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6016",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=machine_vision;i=7006", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6016"]))

ns0.objtypes.FileType(
    nodeId="ns=machine_vision;i=5001",
    browseName="ns=machine_vision;Handle",
    description="The file handle refers to the recipe data, which are teated as a BLOB, i.e. they are not interpreted outside the system. They are accessed via OPC UA file operations.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6009", browseName="OpenCount", description="The current number of open file handles.", dataType=o6.UInt16)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6013", browseName="Size", description="The size of the file in bytes.", dataType=o6.UInt64)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision;i=6014", browseName="UserWritable", description="Whether the file is writable by the current user.", dataType=o6.Boolean
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6015", browseName="Writable", description="Whether the file is writable.", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7001"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7002"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7003"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7004"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7005"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7006"]),
    ],
)
o6.reference(machine_vision_objtypes.RecipeType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5001"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6026",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InternalId", dataType=o6.NodeId("ns=machine_vision;i=3008"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6027",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7008",
    browseName="ns=machine_vision;ActivateConfiguration",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6026"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6027"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6056",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6057",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7010",
    browseName="ns=machine_vision;Sync",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6056"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6057"]),
)

machine_vision_objtypes.VisionStepModelStateMachineType(
    nodeId="ns=machine_vision;i=5011",
    browseName="ns=machine_vision;HaltedStepModel",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=machine_vision;i=6058"]), o6.hasComponent(o6.ns["ns=machine_vision;i=7010"])],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5011"])
o6.reference(o6.ns["ns=machine_vision;i=5029"], "i=117", o6.ns["ns=machine_vision;i=5011"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6061",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6062",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7011",
    browseName="ns=machine_vision;Sync",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6061"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6062"]),
)

machine_vision_objtypes.VisionStepModelStateMachineType(
    nodeId="ns=machine_vision;i=5012",
    browseName="ns=machine_vision;PreoperationalStepModel",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=machine_vision;i=6063"]), o6.hasComponent(o6.ns["ns=machine_vision;i=7011"])],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5012"])
o6.reference(o6.ns["ns=machine_vision;i=5028"], "i=117", o6.ns["ns=machine_vision;i=5012"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6337",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=machine_vision;i=3011"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6338",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7012",
    browseName="GenerateFileForRead",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6337"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6338"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6044",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="InternalId", dataType=o6.NodeId("ns=machine_vision;i=3008"), valueRank=-1),
        ns0.datatypes.Argument(name="Timeout", dataType=o6.Int32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6098",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ConfigurationHandle", dataType=o6.NodeId("ns=machine_vision;i=3018"), valueRank=-1),
        ns0.datatypes.Argument(name="Configuration", dataType=o6.NodeId("ns=machine_vision;i=3007"), valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7016",
    browseName="ns=machine_vision;GetConfigurationById",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6044"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6098"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6099",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="MaxResults", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="StartIndex", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="Timeout", dataType=o6.Int32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6102",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="IsComplete", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="ResultCount", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ConfigurationHandle", dataType=o6.NodeId("ns=machine_vision;i=3018"), valueRank=-1),
        ns0.datatypes.Argument(name="ConfigurationList", dataType=o6.NodeId("ns=machine_vision;i=3007"), valueRank=1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7017",
    browseName="ns=machine_vision;GetConfigurationList",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6099"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6102"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6103",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        ns0.datatypes.Argument(name="ExternalId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1),
        ns0.datatypes.Argument(name="IsPrepared", dataType=o6.NodeId("ns=machine_vision;i=3014"), valueRank=-1),
        ns0.datatypes.Argument(name="MaxResults", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="StartIndex", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="Timeout", dataType=o6.Int32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6106",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="IsComplete", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="ResultCount", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="RecipeHandle", dataType=o6.NodeId("ns=machine_vision;i=3018"), valueRank=-1),
        ns0.datatypes.Argument(name="RecipeList", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7018",
    browseName="ns=machine_vision;GetRecipeListFiltered",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6103"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6106"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6252",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6349",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7019",
    browseName="ns=machine_vision;Sync",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6252"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6349"]),
)

machine_vision_objtypes.VisionStepModelStateMachineType(
    nodeId="ns=machine_vision;i=5054",
    browseName="ns=machine_vision;ErrorStepModel",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=machine_vision;i=6358"]), o6.hasComponent(o6.ns["ns=machine_vision;i=7019"])],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5054"])
o6.reference(o6.ns["ns=machine_vision;i=5030"], "i=117", o6.ns["ns=machine_vision;i=5054"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6065",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6066",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7020",
    browseName="ns=machine_vision;Abort",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6065"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6066"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6067",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="MeasId", dataType=o6.NodeId("ns=machine_vision;i=3015"), valueRank=-1),
        ns0.datatypes.Argument(name="PartId", dataType=o6.NodeId("ns=machine_vision;i=3004"), valueRank=-1),
        ns0.datatypes.Argument(name="RecipeId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1),
        ns0.datatypes.Argument(name="Parameters", dataType=ns0.datatypes.BaseDataType, valueRank=1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6068",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="JobId", dataType=o6.NodeId("ns=machine_vision;i=3016"), valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7021",
    browseName="ns=machine_vision;StartContinuous",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6067"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6068"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6069",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="MeasId", dataType=o6.NodeId("ns=machine_vision;i=3015"), valueRank=-1),
        ns0.datatypes.Argument(name="PartId", dataType=o6.NodeId("ns=machine_vision;i=3004"), valueRank=-1),
        ns0.datatypes.Argument(name="RecipeId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1),
        ns0.datatypes.Argument(name="Parameters", dataType=ns0.datatypes.BaseDataType, valueRank=1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6070",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="JobId", dataType=o6.NodeId("ns=machine_vision;i=3016"), valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7022",
    browseName="ns=machine_vision;StartSingleJob",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6069"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6070"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6078",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6079",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7023",
    browseName="ns=machine_vision;Stop",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6078"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6079"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6059",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6083",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7024",
    browseName="ns=machine_vision;Sync",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6059"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6083"]),
)

machine_vision_objtypes.VisionStepModelStateMachineType(
    nodeId="ns=machine_vision;i=5021",
    browseName="ns=machine_vision;ContinuousExecutionStepModel",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=machine_vision;i=6085"]), o6.hasComponent(o6.ns["ns=machine_vision;i=7024"])],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5021"])
o6.reference(o6.ns["ns=machine_vision;i=5059"], "i=117", o6.ns["ns=machine_vision;i=5021"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6089",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6090",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7027",
    browseName="ns=machine_vision;Sync",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6089"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6090"]),
)

machine_vision_objtypes.VisionStepModelStateMachineType(
    nodeId="ns=machine_vision;i=5043",
    browseName="ns=machine_vision;InitializedStepModel",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=machine_vision;i=6091"]), o6.hasComponent(o6.ns["ns=machine_vision;i=7027"])],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5043"])
o6.reference(o6.ns["ns=machine_vision;i=5056"], "i=117", o6.ns["ns=machine_vision;i=5043"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6129",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7028",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6134",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7028",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7028",
    browseName="ns=machine_vision;Sync",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6129"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6134"]),
)

machine_vision_objtypes.VisionStepModelStateMachineType(
    nodeId="ns=machine_vision;i=5046",
    browseName="ns=machine_vision;ReadyStepModel",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=machine_vision;i=6135"]), o6.hasComponent(o6.ns["ns=machine_vision;i=7028"])],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5046"])
o6.reference(o6.ns["ns=machine_vision;i=5057"], "i=117", o6.ns["ns=machine_vision;i=5046"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6339",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=machine_vision;i=3011"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6340",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7029",
    browseName="GenerateFileForWrite",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6339"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6340"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6137",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6138",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7030",
    browseName="ns=machine_vision;Sync",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6137"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6138"]),
)

machine_vision_objtypes.VisionStepModelStateMachineType(
    nodeId="ns=machine_vision;i=5052",
    browseName="ns=machine_vision;SingleExecutionStepModel",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=machine_vision;i=6139"]), o6.hasComponent(o6.ns["ns=machine_vision;i=7030"])],
)
o6.reference(machine_vision_objtypes.VisionAutomaticModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5052"])
o6.reference(o6.ns["ns=machine_vision;i=5058"], "i=117", o6.ns["ns=machine_vision;i=5052"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6107",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7031",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ExternalId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="InternalIdIn", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6110",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7031",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="InternalIdOut", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
        ns0.datatypes.Argument(name="IsCompleted", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7031",
    browseName="ns=machine_vision;PrepareRecipe",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6107"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6110"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6111",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7032",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ExternalId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="InternalIdIn", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6114",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7032",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="InternalIdOut", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7032",
    browseName="ns=machine_vision;UnprepareRecipe",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6111"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6114"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6115",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7033",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ResultId", dataType=o6.NodeId("ns=machine_vision;i=3021"), valueRank=-1),
        ns0.datatypes.Argument(name="Timeout", dataType=o6.Int32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6118",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7033",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ResultHandle", dataType=o6.NodeId("ns=machine_vision;i=3018"), valueRank=-1),
        ns0.datatypes.Argument(name="Result", dataType=o6.NodeId("ns=machine_vision;i=3006"), valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7033",
    browseName="ns=machine_vision;GetResultById",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6115"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6118"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6119",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7034",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ResultId", dataType=o6.NodeId("ns=machine_vision;i=3021"), valueRank=-1),
        ns0.datatypes.Argument(name="Timeout", dataType=o6.Int32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6123",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7034",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[17],
    value=[
        ns0.datatypes.Argument(name="HasTransferableDataOnFile", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="ResultHandle", dataType=o6.NodeId("ns=machine_vision;i=3018"), valueRank=-1),
        ns0.datatypes.Argument(name="IsPartial", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="IsSimulated", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="ResultState", dataType=o6.NodeId("ns=machine_vision;i=3009"), valueRank=-1),
        ns0.datatypes.Argument(name="MeasId", dataType=o6.NodeId("ns=machine_vision;i=3015"), valueRank=-1),
        ns0.datatypes.Argument(name="PartId", dataType=o6.NodeId("ns=machine_vision;i=3004"), valueRank=-1),
        ns0.datatypes.Argument(name="ExternalRecipeId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="InternalRecipeId", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
        ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1),
        ns0.datatypes.Argument(name="ExternalConfigurationId", dataType=o6.NodeId("ns=machine_vision;i=3008"), valueRank=-1),
        ns0.datatypes.Argument(name="InternalConfigurationId", dataType=o6.NodeId("ns=machine_vision;i=3008"), valueRank=-1),
        ns0.datatypes.Argument(name="JobId", dataType=o6.NodeId("ns=machine_vision;i=3016"), valueRank=-1),
        ns0.datatypes.Argument(name="CreationTime", dataType=ns0.datatypes.UtcTime, valueRank=-1),
        ns0.datatypes.Argument(name="ProcessingTimes", dataType=o6.NodeId("ns=machine_vision;i=3005"), valueRank=-1),
        ns0.datatypes.Argument(name="ResultContent", dataType=ns0.datatypes.BaseDataType, valueRank=1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7034",
    browseName="ns=machine_vision;GetResultComponentsById",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6119"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6123"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6124",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7035",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[12],
    value=[
        ns0.datatypes.Argument(name="ResultState", dataType=o6.NodeId("ns=machine_vision;i=3009"), valueRank=-1),
        ns0.datatypes.Argument(name="MeasId", dataType=o6.NodeId("ns=machine_vision;i=3015"), valueRank=-1),
        ns0.datatypes.Argument(name="PartId", dataType=o6.NodeId("ns=machine_vision;i=3004"), valueRank=-1),
        ns0.datatypes.Argument(name="ExternalRecipeId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="InternalRecipeId", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
        ns0.datatypes.Argument(name="ExternalConfigurationId", dataType=o6.NodeId("ns=machine_vision;i=3008"), valueRank=-1),
        ns0.datatypes.Argument(name="InternalConfigurationId", dataType=o6.NodeId("ns=machine_vision;i=3008"), valueRank=-1),
        ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1),
        ns0.datatypes.Argument(name="JobId", dataType=o6.NodeId("ns=machine_vision;i=3016"), valueRank=-1),
        ns0.datatypes.Argument(name="MaxResults", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="StartIndex", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="Timeout", dataType=o6.Int32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6133",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7035",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="IsComplete", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="ResultCount", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ResultHandle", dataType=o6.NodeId("ns=machine_vision;i=3018"), valueRank=-1),
        ns0.datatypes.Argument(name="ResultList", dataType=o6.NodeId("ns=machine_vision;i=3006"), valueRank=1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7035",
    browseName="ns=machine_vision;GetResultListFiltered",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6124"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6133"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6146",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7036",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="SafetyTriggered", dataType=o6.Boolean, valueRank=-1), ns0.datatypes.Argument(name="SafetyInformation", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6147",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7036",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7036",
    browseName="ns=machine_vision;ReportSafetyState",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6146"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6147"]),
)

machine_vision_objtypes.SafetyStateManagementType(
    nodeId="ns=machine_vision;i=5023",
    browseName="ns=machine_vision;SafetyStateManagement",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision;i=6150", browseName="ns=machine_vision;VisionSafetyInformation", dataType=o6.String, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision;i=6151", browseName="ns=machine_vision;VisionSafetyTriggered", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7036"]),
    ],
)
o6.reference(machine_vision_objtypes.VisionSystemType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5023"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6154",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7037",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6155",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7037",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7037",
    browseName="ns=machine_vision;Halt",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6154"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6155"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6158",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7038",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6159",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7038",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7038",
    browseName="ns=machine_vision;Reset",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6158"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6159"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6167",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7039",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6174",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7039",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7039",
    browseName="ns=machine_vision;Sync",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6167"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6174"]),
)

machine_vision_objtypes.VisionStepModelStateMachineType(
    nodeId="ns=machine_vision;i=5025",
    browseName="ns=machine_vision;ContinuousExecutionStepModel",
    references=[o6.hasComponent(o6.ns["ns=machine_vision;i=6082"]), o6.hasComponent(o6.ns["ns=machine_vision;i=7039"])],
)


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6179",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7040",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6182",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7040",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7040",
    browseName="ns=machine_vision;Sync",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6179"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6182"]),
)

machine_vision_objtypes.VisionStepModelStateMachineType(
    nodeId="ns=machine_vision;i=5055",
    browseName="ns=machine_vision;InitializedStepModel",
    references=[o6.hasComponent(o6.ns["ns=machine_vision;i=6175"]), o6.hasComponent(o6.ns["ns=machine_vision;i=7040"])],
)


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6212",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7042",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6215",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7042",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7042",
    browseName="ns=machine_vision;Sync",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6212"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6215"]),
)

machine_vision_objtypes.VisionStepModelStateMachineType(
    nodeId="ns=machine_vision;i=5074",
    browseName="ns=machine_vision;ReadyStepModel",
    references=[o6.hasComponent(o6.ns["ns=machine_vision;i=6183"]), o6.hasComponent(o6.ns["ns=machine_vision;i=7042"])],
)


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6326",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7044",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Activate", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1),
        ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6400",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7044",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7044",
    browseName="ns=machine_vision;SimulationMode",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6326"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6400"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6216",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7049",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1)],
)
o6.call(nodeId="ns=machine_vision;i=7049", browseName="ns=machine_vision;ConfirmAll", inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6216"]))

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6224",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7050",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6225",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7050",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7050",
    browseName="ns=machine_vision;Sync",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6224"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6225"]),
)

machine_vision_objtypes.VisionStepModelStateMachineType(
    nodeId="ns=machine_vision;i=5075",
    browseName="ns=machine_vision;ErrorStepModel",
    references=[o6.hasComponent(o6.ns["ns=machine_vision;i=6219"]), o6.hasComponent(o6.ns["ns=machine_vision;i=7050"])],
)


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6251",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7051",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6253",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7051",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7051",
    browseName="ns=machine_vision;Sync",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6251"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6253"]),
)

machine_vision_objtypes.VisionStepModelStateMachineType(
    nodeId="ns=machine_vision;i=5076",
    browseName="ns=machine_vision;HaltedStepModel",
    references=[o6.hasComponent(o6.ns["ns=machine_vision;i=6244"]), o6.hasComponent(o6.ns["ns=machine_vision;i=7051"])],
)


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6279",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7052",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6280",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7052",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7052",
    browseName="ns=machine_vision;Sync",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6279"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6280"]),
)

machine_vision_objtypes.VisionStepModelStateMachineType(
    nodeId="ns=machine_vision;i=5077",
    browseName="ns=machine_vision;PreoperationalStepModel",
    references=[o6.hasComponent(o6.ns["ns=machine_vision;i=6277"]), o6.hasComponent(o6.ns["ns=machine_vision;i=7052"])],
)


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6325",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7053",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=machine_vision;i=7053", browseName="ns=machine_vision;SelectModeAutomatic", outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6325"]))

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6342",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7054",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExternalId", dataType=o6.NodeId("ns=machine_vision;i=3008"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6348",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7054",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="InternalId", dataType=o6.NodeId("ns=machine_vision;i=3008"), valueRank=-1),
        ns0.datatypes.Argument(name="Configuration", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="TransferRequired", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7054",
    browseName="ns=machine_vision;AddConfiguration",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6342"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6348"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6541",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7067",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=machine_vision;i=3022"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6542",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7067",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7067",
    browseName="GenerateFileForRead",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6541"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6542"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6351",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7068",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6359",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7068",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7068",
    browseName="CloseAndCommit",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6351"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6359"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6360",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7069",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=machine_vision;i=3011"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6361",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7069",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7069",
    browseName="GenerateFileForRead",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6360"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6361"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6362",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7070",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=machine_vision;i=3011"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6363",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7070",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7070",
    browseName="GenerateFileForWrite",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6362"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6363"]),
)

machine_vision_objtypes.ConfigurationTransferType(
    nodeId="ns=machine_vision;i=5093",
    browseName="ns=machine_vision;ConfigurationTransfer",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6350", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7068"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7069"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7070"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6544",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7071",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6545",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7071",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7071",
    browseName="CloseAndCommit",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6544"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6545"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6364",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7072",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ConfigurationHandle", dataType=o6.NodeId("ns=machine_vision;i=3018"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6365",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7072",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7072",
    browseName="ns=machine_vision;ReleaseConfigurationHandle",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6364"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6365"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6366",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7073",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InternalId", dataType=o6.NodeId("ns=machine_vision;i=3008"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6368",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7073",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7073",
    browseName="ns=machine_vision;RemoveConfiguration",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6366"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6368"]),
)

machine_vision_objtypes.ConfigurationManagementType(
    nodeId="ns=machine_vision;i=5004",
    browseName="ns=machine_vision;ConfigurationManagement",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=machine_vision;i=5093"]),
        o6.hasComponent(machine_vision_objtypes.ConfigurationFolderType(nodeId="ns=machine_vision;i=5094", browseName="ns=machine_vision;Configurations")),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machine_vision;i=6043",
                browseName="ns=machine_vision;ActiveConfiguration",
                dataType=machine_vision_datypes.ConfigurationDataType,
                value=machine_vision_datypes.ConfigurationDataType(
                    hasTransferableDataOnFile=None,
                    externalId=None,
                    internalId=machine_vision_datypes.ConfigurationIdDataType(id="", version=None, hash=None, hashAlgorithm=None, description=None),
                    lastModified=o6.DateTime("1900-01-01T00:00:00Z"),
                ),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7008"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7016"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7017"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7054"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7072"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7073"]),
    ],
)
o6.reference(machine_vision_objtypes.VisionSystemType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5004"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6369",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7074",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ExternalId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6370",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7074",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="InternalId", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
        ns0.datatypes.Argument(name="Recipe", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="Product", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="TransferRequired", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7074",
    browseName="ns=machine_vision;AddRecipe",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6369"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6370"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6371",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7075",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6372",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7075",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="InternalId", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7075",
    browseName="ns=machine_vision;PrepareProduct",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6371"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6372"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6613",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7076",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6614",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7076",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7076",
    browseName="ns=machine_vision;LinkProduct",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6613"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6614"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6546",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7077",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=ns0.datatypes.BaseDataType, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6547",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7077",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7077",
    browseName="GenerateFileForWrite",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6546"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6547"]),
)

machine_vision_objtypes.ResultTransferType(
    nodeId="ns=machine_vision;i=5251",
    browseName="ns=machine_vision;ResultTransfer",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6543", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7067"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7071"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7077"]),
    ],
)
o6.reference(machine_vision_objtypes.ResultManagementType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5251"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6375",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7078",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6376",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7078",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7078",
    browseName="CloseAndCommit",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6375"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6376"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6377",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7079",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="generateOptions", dataType=o6.NodeId("ns=machine_vision;i=3012"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6378",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7079",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="fileNodeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="fileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="completionStateMachine", dataType=o6.NodeId, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7079",
    browseName="GenerateFileForRead",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6377"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6378"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6380",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7080",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=machine_vision;i=3012"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6381",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7080",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7080",
    browseName="GenerateFileForWrite",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6380"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6381"]),
)

machine_vision_objtypes.RecipeTransferType(
    nodeId="ns=machine_vision;i=5096",
    browseName="ns=machine_vision;RecipeTransfer",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6374", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7078"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7079"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7080"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6382",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7081",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RecipeHandle", dataType=o6.NodeId("ns=machine_vision;i=3018"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6383",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7081",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7081",
    browseName="ns=machine_vision;ReleaseRecipeHandle",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6382"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6383"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6384",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7082",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExternalId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6385",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7082",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7082",
    browseName="ns=machine_vision;RemoveRecipe",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6384"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6385"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6386",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7083",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="InternalId", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
        ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6387",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7083",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7083",
    browseName="ns=machine_vision;UnlinkProduct",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6386"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6387"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6388",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7084",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6389",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7084",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="InternalId", dataType=o6.NodeId("ns=machine_vision;i=3013"), valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7084",
    browseName="ns=machine_vision;UnprepareProduct",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6388"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6389"]),
)

machine_vision_objtypes.RecipeManagementType(
    nodeId="ns=machine_vision;i=5015",
    browseName="ns=machine_vision;RecipeManagement",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=machine_vision;i=5095"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=5096"]),
        o6.hasComponent(machine_vision_objtypes.RecipeFolderType(nodeId="ns=machine_vision;i=5097", browseName="ns=machine_vision;Recipes")),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7018"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7031"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7032"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7074"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7075"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7081"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7082"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7083"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7084"]),
    ],
)
o6.reference(machine_vision_objtypes.VisionSystemType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5015"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6391",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7085",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ResultHandle", dataType=o6.NodeId("ns=machine_vision;i=3018"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6392",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7085",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7085",
    browseName="ns=machine_vision;ReleaseResultHandle",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6391"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6392"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6394",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7086",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6395",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7086",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7086",
    browseName="CloseAndCommit",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6394"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6395"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6396",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7087",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=machine_vision;i=3022"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6397",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7087",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7087",
    browseName="GenerateFileForRead",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6396"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6397"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6398",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7088",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=ns0.datatypes.BaseDataType, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6399",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7088",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7088",
    browseName="GenerateFileForWrite",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6398"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6399"]),
)

machine_vision_objtypes.ResultTransferType(
    nodeId="ns=machine_vision;i=5098",
    browseName="ns=machine_vision;ResultTransfer",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6393", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7086"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7087"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7088"]),
    ],
)
machine_vision_objtypes.ResultManagementType(
    nodeId="ns=machine_vision;i=5020",
    browseName="ns=machine_vision;ResultManagement",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=machine_vision;i=5098"]),
        o6.hasComponent(machine_vision_objtypes.ResultFolderType(nodeId="ns=machine_vision;i=5099", browseName="ns=machine_vision;Results")),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7033"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7034"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7035"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7085"]),
    ],
)
o6.reference(machine_vision_objtypes.VisionSystemType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5020"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6403",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7091",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6404",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7091",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7091",
    browseName="ns=machine_vision;Sync",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6403"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6404"]),
)

machine_vision_objtypes.VisionStepModelStateMachineType(
    nodeId="ns=machine_vision;i=5092",
    browseName="ns=machine_vision;SingleExecutionStepModel",
    references=[o6.hasComponent(o6.ns["ns=machine_vision;i=6401"]), o6.hasComponent(o6.ns["ns=machine_vision;i=7091"])],
)
machine_vision_objtypes.VisionAutomaticModeStateMachineType(
    nodeId="ns=machine_vision;i=5024",
    browseName="ns=machine_vision;AutomaticModeStateMachine",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=machine_vision;i=5025"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=5055"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=5074"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=5092"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6080"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7020"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7021"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7022"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7023"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7044"]),
    ],
)
o6.reference(machine_vision_objtypes.VisionStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5024"])
o6.reference(o6.ns["ns=machine_vision;i=5031"], "i=117", o6.ns["ns=machine_vision;i=5024"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6405",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7092",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6406",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7092",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7092",
    browseName="ns=machine_vision;Abort",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6405"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6406"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6409",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7099",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="MeasId", dataType=o6.NodeId("ns=machine_vision;i=3015"), valueRank=-1),
        ns0.datatypes.Argument(name="PartId", dataType=o6.NodeId("ns=machine_vision;i=3004"), valueRank=-1),
        ns0.datatypes.Argument(name="RecipeId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1),
        ns0.datatypes.Argument(name="Parameters", dataType=ns0.datatypes.BaseDataType, valueRank=1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6410",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7099",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="JobId", dataType=o6.NodeId("ns=machine_vision;i=3016"), valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7099",
    browseName="ns=machine_vision;StartContinuous",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6409"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6410"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6411",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7102",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="MeasId", dataType=o6.NodeId("ns=machine_vision;i=3015"), valueRank=-1),
        ns0.datatypes.Argument(name="PartId", dataType=o6.NodeId("ns=machine_vision;i=3004"), valueRank=-1),
        ns0.datatypes.Argument(name="RecipeId", dataType=o6.NodeId("ns=machine_vision;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1),
        ns0.datatypes.Argument(name="Parameters", dataType=ns0.datatypes.BaseDataType, valueRank=1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6412",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7102",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="JobId", dataType=o6.NodeId("ns=machine_vision;i=3016"), valueRank=-1),
        ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7102",
    browseName="ns=machine_vision;StartSingleJob",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6411"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6412"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6413",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7103",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6414",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7103",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7103",
    browseName="ns=machine_vision;Stop",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6413"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6414"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6418",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7104",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6419",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7104",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7104",
    browseName="ns=machine_vision;Sync",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6418"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6419"]),
)

machine_vision_objtypes.VisionStepModelStateMachineType(
    nodeId="ns=machine_vision;i=5102",
    browseName="ns=machine_vision;ContinuousExecutionStepModel",
    references=[o6.hasComponent(o6.ns["ns=machine_vision;i=6416"]), o6.hasComponent(o6.ns["ns=machine_vision;i=7104"])],
)


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6422",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7105",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6423",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7105",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7105",
    browseName="ns=machine_vision;Sync",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6422"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6423"]),
)

machine_vision_objtypes.VisionStepModelStateMachineType(
    nodeId="ns=machine_vision;i=5103",
    browseName="ns=machine_vision;InitializedStepModel",
    references=[o6.hasComponent(o6.ns["ns=machine_vision;i=6420"]), o6.hasComponent(o6.ns["ns=machine_vision;i=7105"])],
)


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6426",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7106",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6427",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7106",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7106",
    browseName="ns=machine_vision;Sync",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6426"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6427"]),
)

machine_vision_objtypes.VisionStepModelStateMachineType(
    nodeId="ns=machine_vision;i=5104",
    browseName="ns=machine_vision;ReadyStepModel",
    references=[o6.hasComponent(o6.ns["ns=machine_vision;i=6424"]), o6.hasComponent(o6.ns["ns=machine_vision;i=7106"])],
)


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6428",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7107",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Activate", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1),
        ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6429",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7107",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7107",
    browseName="ns=machine_vision;SimulationMode",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6428"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6429"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6432",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7108",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Cause", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="CauseDescription", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6433",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7108",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7108",
    browseName="ns=machine_vision;Sync",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6432"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6433"]),
)

machine_vision_objtypes.VisionStepModelStateMachineType(
    nodeId="ns=machine_vision;i=5105",
    browseName="ns=machine_vision;SingleExecutionStepModel",
    references=[o6.hasComponent(o6.ns["ns=machine_vision;i=6430"]), o6.hasComponent(o6.ns["ns=machine_vision;i=7108"])],
)
machine_vision_objtypes.VisionAutomaticModeStateMachineType(
    nodeId="ns=machine_vision;i=5100",
    browseName="ns=machine_vision;AutomaticModeStateMachine",
    references=[
        o6.hasComponent(o6.ns["ns=machine_vision;i=5102"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=5103"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=5104"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=5105"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6407"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7092"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7099"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7102"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7103"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7107"]),
    ],
)
machine_vision_objtypes.VisionStateMachineType(
    nodeId="ns=machine_vision;i=5053",
    browseName="ns=machine_vision;VisionStateMachine",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=machine_vision;i=5075"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=5076"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=5077"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=5100"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=5101"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=5106"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=5107"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=5108"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=6162"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7037"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7038"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7049"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7053"]),
    ],
)
o6.reference(machine_vision_objtypes.VisionSystemType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5053"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6600",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7113",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6601",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7113",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7113",
    browseName="CloseAndCommit",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6600"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6601"]),
)

machine_vision_objtypes.ConfigurationTransferType(
    nodeId="ns=machine_vision;i=5266",
    browseName="ns=machine_vision;ConfigurationTransfer",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6599", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7012"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7029"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7113"]),
    ],
)
o6.reference(machine_vision_objtypes.ConfigurationManagementType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5266"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6615",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7114",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="IsCompleted", dataType=o6.Boolean, valueRank=-1), ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=machine_vision;i=7114", browseName="ns=machine_vision;Prepare", outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6615"]))

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6586",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7115",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6587",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7115",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7115",
    browseName="CloseAndCommit",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6586"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6587"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6186",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7118",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="generateOptions", dataType=o6.NodeId("ns=machine_vision;i=3012"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6187",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7118",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="fileNodeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="fileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="completionStateMachine", dataType=o6.NodeId, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=machine_vision;i=7118",
    browseName="GenerateFileForRead",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6186"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6187"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6588",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7119",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=machine_vision;i=3012"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6589",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7119",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7119",
    browseName="GenerateFileForWrite",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6588"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6589"]),
)

machine_vision_objtypes.RecipeTransferType(
    nodeId="ns=machine_vision;i=5264",
    browseName="ns=machine_vision;RecipeTransfer",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6585", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7115"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7118"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7119"]),
    ],
)
o6.reference(machine_vision_objtypes.RecipeManagementType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5264"])


ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6616",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7120",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductId", dataType=o6.NodeId("ns=machine_vision;i=3003"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6619",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7120",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=machine_vision;i=7120",
    browseName="ns=machine_vision;UnlinkProduct",
    inputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6616"]),
    outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6619"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=machine_vision;i=6620",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=machine_vision;i=7121",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Error", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=machine_vision;i=7121", browseName="ns=machine_vision;Unprepare", outputArgs=o6.hasProperty(o6.ns["ns=machine_vision;i=6620"]))

machine_vision_objtypes.RecipeType(
    nodeId="ns=machine_vision;i=5270",
    browseName="ns=machine_vision;<Recipe>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision;i=6608",
                browseName="ns=machine_vision;ExternalId",
                description="Recipe ID for identifying the recipe outside the vision system. The ExternalID is only managed by the host system.",
                dataType=machine_vision_datypes.RecipeIdExternalDataType,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision;i=6609",
                browseName="ns=machine_vision;InternalId",
                description="System-wide unique ID for identifying a recipe. This ID is assigned by the vision system.",
                dataType=machine_vision_datypes.RecipeIdInternalDataType,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machine_vision;i=6610", browseName="ns=machine_vision;IsPrepared", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision;i=6611",
                browseName="ns=machine_vision;LastModified",
                description="The time when this recipe was last modified.",
                dataType=ns0.datatypes.UtcTime,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machine_vision;i=6612",
                browseName="ns=machine_vision;LinkedProducts",
                dataType=machine_vision_datypes.ProductIdDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7076"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7114"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7120"]),
        o6.hasComponent(o6.ns["ns=machine_vision;i=7121"]),
    ],
)
o6.reference(machine_vision_objtypes.RecipeFolderType, ns0.reftypes.HasComponent, o6.ns["ns=machine_vision;i=5270"])


del Any, TYPE_CHECKING, uuid, o6, ns0, machine_vision_reftypes, machine_vision_datypes, machine_vision_vartypes, machine_vision_objtypes
