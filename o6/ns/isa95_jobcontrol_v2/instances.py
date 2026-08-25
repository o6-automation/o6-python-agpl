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

"""Generated OPC UA isa95_jobcontrol_v2 namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import datatypes as isa95_jobcontrol_v2_datypes
from . import objtypes as isa95_jobcontrol_v2_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5002", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5003", browseName="Default XML")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95PropertyDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5003"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5004", browseName="Default JSON")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95PropertyDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5004"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5005", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5006", browseName="Default XML")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95ParameterDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5006"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5007", browseName="Default JSON")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95ParameterDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5007"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5008", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5009", browseName="Default XML")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95EquipmentDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5009"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5010", browseName="Default JSON")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95EquipmentDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5010"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5011", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5012", browseName="Default XML")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95WorkMasterDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5012"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5013", browseName="Default JSON")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95WorkMasterDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5013"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5014", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5015", browseName="Default XML")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95JobOrderDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5015"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5016", browseName="Default JSON")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95JobOrderDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5016"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5017", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5018", browseName="Default XML")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95MaterialDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5018"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5019", browseName="Default JSON")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95MaterialDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5019"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5020", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5021", browseName="Default XML")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95PersonnelDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5021"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5022", browseName="Default JSON")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95PersonnelDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5022"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5023", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5024", browseName="Default XML")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95PhysicalAssetDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5024"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5025", browseName="Default JSON")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95PhysicalAssetDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5025"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5026", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5027", browseName="Default XML")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95JobResponseDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5027"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5028", browseName="Default JSON")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95JobResponseDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5028"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5029", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5030", browseName="Default XML")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95StateDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5030"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5031", browseName="Default JSON")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95StateDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5031"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5032", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5033", browseName="Default XML")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95JobOrderAndStateDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5033"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95_jobcontrol_v2;i=5034", browseName="Default JSON")
o6.hasEncoding(isa95_jobcontrol_v2_datypes.ISA95JobOrderAndStateDataType, o6.ns["ns=isa95_jobcontrol_v2;i=5034"])
ns0.objtypes.StateType(
    nodeId="ns=isa95_jobcontrol_v2;i=5000",
    browseName="ns=isa95_jobcontrol_v2;Waiting",
    description="The necessary pre-conditions have not been met and the job order is not ready to run.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6000", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95PrepareStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5000"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=isa95_jobcontrol_v2;i=6001",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6002", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
isa95_jobcontrol_v2_objtypes.ISA95PrepareStateMachineType(
    nodeId="ns=isa95_jobcontrol_v2;i=5080",
    browseName="ns=isa95_jobcontrol_v2;NotAllowedToStartSubstates",
    description="Substates of NotAllowedToStart",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6001"])],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5080"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=isa95_jobcontrol_v2;i=6003",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6004", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
isa95_jobcontrol_v2_objtypes.ISA95PrepareStateMachineType(
    nodeId="ns=isa95_jobcontrol_v2;i=5081",
    browseName="ns=isa95_jobcontrol_v2;AllowedToStartSubstates",
    description="Substates of AllowedToStart",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6003"])],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5081"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=isa95_jobcontrol_v2;i=6005",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6006", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
isa95_jobcontrol_v2_objtypes.ISA95EndedStateMachineType(
    nodeId="ns=isa95_jobcontrol_v2;i=5082",
    browseName="ns=isa95_jobcontrol_v2;EndedSubstates",
    description="Substates of Ended",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6005"])],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5082"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=isa95_jobcontrol_v2;i=6007",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6008", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
isa95_jobcontrol_v2_objtypes.ISA95InterruptedStateMachineType(
    nodeId="ns=isa95_jobcontrol_v2;i=5083",
    browseName="ns=isa95_jobcontrol_v2;InterruptedSubstates",
    description="Substates of Interrupted",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6007"])],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5083"])
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5084",
    browseName="ns=isa95_jobcontrol_v2;FromNotAllowedToStartToAborted",
    description="This transition is triggered when Abort Method is called.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6009", browseName="TransitionNumber", dataType=o6.UInt32, value=12))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverObjectType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5084"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5084"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7010"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5084"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5085",
    browseName="ns=isa95_jobcontrol_v2;FromAllowedToStartToAborted",
    description="This transition is triggered when Abort Method is called.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6010", browseName="TransitionNumber", dataType=o6.UInt32, value=13))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverObjectType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5085"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5085"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7010"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5085"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5086",
    browseName="ns=isa95_jobcontrol_v2;FromAllowedToStartToAborted",
    description="This transition is triggered when Abort Method is called.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6011", browseName="TransitionNumber", dataType=o6.UInt32, value=13))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5086"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5086"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7010"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5086"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5087",
    browseName="ns=isa95_jobcontrol_v2;FromNotAllowedToStartToAborted",
    description="This transition is triggered when Abort Method is called.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6012", browseName="TransitionNumber", dataType=o6.UInt32, value=12))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5087"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5087"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7010"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5087"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5088",
    browseName="ns=isa95_jobcontrol_v2;FromReadyToWaiting",
    description="This transition is triggered when the system is not ready to start the execution of the job order anymore.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6013", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95PrepareStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5088"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5088"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5000"])
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5089",
    browseName="ns=isa95_jobcontrol_v2;FromLoadedToReady",
    description="This transition is triggered when the program or configuration to execute the job order is unloaded.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6014", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95PrepareStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5089"])
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5090",
    browseName="ns=isa95_jobcontrol_v2;FromLoadedToWaiting",
    description="This transition is triggered when the system is not ready to start the execution of the job order anymore.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6015", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95PrepareStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5090"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5090"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5000"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6022", browseName="ns=isa95_jobcontrol_v2;ISA95EquipmentDataType", dataType=o6.String, value="ISA95EquipmentDataType"
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5008"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6022"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashISA95MinusJOBCONTROL_V2Slash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=isa95_jobcontrol_v2;i=5001",
    browseName="ns=isa95_jobcontrol_v2;http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6023", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=isa95_jobcontrol_v2;i=6024", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2024-01-31T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=isa95_jobcontrol_v2;i=6025", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6026", browseName="NamespaceVersion", dataType=o6.String, value="2.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=isa95_jobcontrol_v2;i=6027",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=isa95_jobcontrol_v2;i=6028",
                browseName="StaticNumericNodeIdRange",
                dataType=ns0.datatypes.NumericRange,
                valueRank=1,
                arrayDimensions=[1],
                value=["1:2147483647"],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6029", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="0")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6030", browseName="ns=isa95_jobcontrol_v2;ISA95EquipmentDataType", dataType=o6.String, value="//xs:element[@name='ISA95EquipmentDataType']"
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5009"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6030"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6031", browseName="ns=isa95_jobcontrol_v2;ISA95JobOrderAndStateDataType", dataType=o6.String, value="ISA95JobOrderAndStateDataType"
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5032"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6031"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6032",
    browseName="ns=isa95_jobcontrol_v2;ISA95JobOrderAndStateDataType",
    dataType=o6.String,
    value="//xs:element[@name='ISA95JobOrderAndStateDataType']",
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5033"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6032"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6046", browseName="ns=isa95_jobcontrol_v2;ISA95JobOrderDataType", dataType=o6.String, value="ISA95JobOrderDataType"
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5014"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6046"])
ns0.objtypes.StateType(
    nodeId="ns=isa95_jobcontrol_v2;i=5035",
    browseName="ns=isa95_jobcontrol_v2;NotAllowedToStart",
    description="The job order is stored but may not be executed.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6071", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverObjectType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5035"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5084"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5035"])
ns0.objtypes.StateType(
    nodeId="ns=isa95_jobcontrol_v2;i=5036",
    browseName="ns=isa95_jobcontrol_v2;AllowedToStart",
    description="The job order is stored and may be executed.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6072", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverObjectType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5036"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5085"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5036"])
ns0.objtypes.StateType(
    nodeId="ns=isa95_jobcontrol_v2;i=5037",
    browseName="ns=isa95_jobcontrol_v2;Running",
    description="The job order is executing.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6073", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverObjectType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5037"])
ns0.objtypes.StateType(
    nodeId="ns=isa95_jobcontrol_v2;i=5038",
    browseName="ns=isa95_jobcontrol_v2;Interrupted",
    description="The job order has been temporarily stopped.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6074", browseName="StateNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverObjectType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5038"])
ns0.objtypes.StateType(
    nodeId="ns=isa95_jobcontrol_v2;i=5039",
    browseName="ns=isa95_jobcontrol_v2;Ended",
    description="The job order has been completed and is no longer in execution.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6075", browseName="StateNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverObjectType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5039"])
ns0.objtypes.StateType(
    nodeId="ns=isa95_jobcontrol_v2;i=5040",
    browseName="ns=isa95_jobcontrol_v2;Aborted",
    description="The job order is aborted.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6076", browseName="StateNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverObjectType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5040"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5084"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5040"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5085"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5040"])
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5041",
    browseName="ns=isa95_jobcontrol_v2;FromNotAllowedToStartToNotAllowedToStart",
    description="This transition is triggered when the Update Method is called and the job order is modified.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6077", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverObjectType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5041"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5041"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5035"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5041"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5035"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5041"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7009"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5041"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5042",
    browseName="ns=isa95_jobcontrol_v2;FromNotAllowedToStartToAllowedToStart",
    description="This transition is triggered when the Start Method is called.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6078", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverObjectType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5042"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5042"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5035"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5042"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5036"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5042"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7005"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5042"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5043",
    browseName="ns=isa95_jobcontrol_v2;FromAllowedToStartToNotAllowedToStart",
    description="This transition is triggered when the RevokeStart Method is called.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6079", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverObjectType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5043"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5043"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5036"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5043"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5035"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5043"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7013"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5043"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5044",
    browseName="ns=isa95_jobcontrol_v2;FromAllowedToStartToAllowedToStart",
    description="This transition is triggered when the Update Method is called and the job order is modified.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6080", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverObjectType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5044"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5044"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5036"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5044"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5036"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5044"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7009"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5044"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5045",
    browseName="ns=isa95_jobcontrol_v2;FromAllowedToStartToRunning",
    description="This transition is triggered when a job order is started to be executed.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6081", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverObjectType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5045"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5045"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5036"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5045"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5037"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5045"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5046",
    browseName="ns=isa95_jobcontrol_v2;FromRunningToInterrupted",
    description="This transition is triggered when an executing job order gets interrupted, either internally or by the Pause Method.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6082", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverObjectType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5046"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5046"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5037"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5046"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5038"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5046"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7007"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5046"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5047",
    browseName="ns=isa95_jobcontrol_v2;FromRunningToEnded",
    description="This transition is triggered when the execution of a job order has finished, either internally or by the Stop Method.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6083", browseName="TransitionNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverObjectType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5047"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5047"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5037"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5047"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5039"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5047"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7006"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5047"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5048",
    browseName="ns=isa95_jobcontrol_v2;FromRunningToAborted",
    description="This transition is triggered when Abort Method is called.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6084", browseName="TransitionNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverObjectType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5048"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5048"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5037"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5048"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5040"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5048"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7010"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5048"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5049",
    browseName="ns=isa95_jobcontrol_v2;FromInterruptedToAborted",
    description="This transition is triggered when Abort Method is called.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6085", browseName="TransitionNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverObjectType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5049"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5049"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5038"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5049"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5040"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5049"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7010"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5049"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5050",
    browseName="ns=isa95_jobcontrol_v2;FromInterruptedToRunning",
    description="This transition is triggered when Resume Method is called.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6086", browseName="TransitionNumber", dataType=o6.UInt32, value=10))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverObjectType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5050"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5050"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5038"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5050"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5037"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5050"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7008"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5050"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5051",
    browseName="ns=isa95_jobcontrol_v2;FromInterruptedToEnded",
    description="This transition is triggered when Stop Method is called.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6087", browseName="TransitionNumber", dataType=o6.UInt32, value=11))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverObjectType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5051"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5051"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5038"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5051"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5039"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5051"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7006"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5051"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.StateType(
    nodeId="ns=isa95_jobcontrol_v2;i=5052",
    browseName="ns=isa95_jobcontrol_v2;Ready",
    description="The necessary pre-conditions have been met and the job order is ready to run, awaiting a Start command.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6089", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95PrepareStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5052"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5088"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5052"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5089"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5052"])
ns0.objtypes.StateType(
    nodeId="ns=isa95_jobcontrol_v2;i=5053",
    browseName="ns=isa95_jobcontrol_v2;Loaded",
    description="In situations where only one job may be in active memory and is able to be run, then the job is loaded in active memory, the necessary pre-conditions have been met, and the job order is ready to run, awaiting a Start command.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6090", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95PrepareStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5053"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5089"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5053"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5090"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5053"])
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5054",
    browseName="ns=isa95_jobcontrol_v2;FromWaitingToReady",
    description="This transition is triggered when the system is ready to start the execution of the job order.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6091", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95PrepareStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5054"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5054"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5000"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5054"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5052"])
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5055",
    browseName="ns=isa95_jobcontrol_v2;FromReadyToLoaded",
    description="This transition is triggered when the program or configuration to execute the job order is loaded.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6092", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95PrepareStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5055"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5055"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5052"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5055"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5053"])
ns0.objtypes.StateType(
    nodeId="ns=isa95_jobcontrol_v2;i=5056",
    browseName="ns=isa95_jobcontrol_v2;Completed",
    description="The job order has been completed and is no longer in execution.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6093", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95EndedStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5056"])
ns0.objtypes.StateType(
    nodeId="ns=isa95_jobcontrol_v2;i=5057",
    browseName="ns=isa95_jobcontrol_v2;Closed",
    description="The job order has been completed and no further post processing is performed.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6094", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95EndedStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5057"])
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5058",
    browseName="ns=isa95_jobcontrol_v2;FromCompletedToClosed",
    description="This transition is triggered when the system has finalized post processing of a ended job order.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6095", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95EndedStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5058"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5058"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5056"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5058"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5057"])
ns0.objtypes.StateType(
    nodeId="ns=isa95_jobcontrol_v2;i=5059",
    browseName="ns=isa95_jobcontrol_v2;Held",
    description="The job order has been temporarily stopped due to a constraint of some form.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6096", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95InterruptedStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5059"])
ns0.objtypes.StateType(
    nodeId="ns=isa95_jobcontrol_v2;i=5060",
    browseName="ns=isa95_jobcontrol_v2;Suspended",
    description="The job order has been temporarily stopped due to a deliberate decision within the execution system.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6097", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95InterruptedStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5060"])
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5061",
    browseName="ns=isa95_jobcontrol_v2;FromHeldToSuspended",
    description="This transition is triggered when the system has switched the job order from internally held to externally suspended, for example by a call of the Pause Method.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6098", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95InterruptedStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5061"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5061"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5059"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5061"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5060"])
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5062",
    browseName="ns=isa95_jobcontrol_v2;FromSuspendedToHeld",
    description="This transition is triggered when the system has switched the job order from externally suspended to an internal held, for example by a call of the Resume Method.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6099", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95InterruptedStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5062"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5062"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5060"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5062"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5059"])
ns0.objtypes.StateType(
    nodeId="ns=isa95_jobcontrol_v2;i=5063",
    browseName="ns=isa95_jobcontrol_v2;NotAllowedToStart",
    description="The job order is stored but may not be executed.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6100", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5063"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5063"], "i=117", o6.ns["ns=isa95_jobcontrol_v2;i=5080"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5087"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5063"])
ns0.objtypes.StateType(
    nodeId="ns=isa95_jobcontrol_v2;i=5064",
    browseName="ns=isa95_jobcontrol_v2;AllowedToStart",
    description="The job order is stored and may be executed.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6101", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5064"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5064"], "i=117", o6.ns["ns=isa95_jobcontrol_v2;i=5081"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5086"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5064"])
ns0.objtypes.StateType(
    nodeId="ns=isa95_jobcontrol_v2;i=5065",
    browseName="ns=isa95_jobcontrol_v2;Running",
    description="The job order is executing.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6102", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5065"])
ns0.objtypes.StateType(
    nodeId="ns=isa95_jobcontrol_v2;i=5066",
    browseName="ns=isa95_jobcontrol_v2;Interrupted",
    description="The job order has been temporarily stopped.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6103", browseName="StateNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5066"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5066"], "i=117", o6.ns["ns=isa95_jobcontrol_v2;i=5083"])
ns0.objtypes.StateType(
    nodeId="ns=isa95_jobcontrol_v2;i=5067",
    browseName="ns=isa95_jobcontrol_v2;Ended",
    description="The job order has been completed and is no longer in execution.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6104", browseName="StateNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5067"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5067"], "i=117", o6.ns["ns=isa95_jobcontrol_v2;i=5082"])
ns0.objtypes.StateType(
    nodeId="ns=isa95_jobcontrol_v2;i=5068",
    browseName="ns=isa95_jobcontrol_v2;Aborted",
    description="The job order is aborted.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6105", browseName="StateNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5068"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5086"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5068"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5087"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5068"])
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5069",
    browseName="ns=isa95_jobcontrol_v2;FromNotAllowedToStartToNotAllowedToStart",
    description="This transition is triggered when the Update Method is called and the job order is modified.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6106", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5069"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5069"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5063"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5069"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5063"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5069"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7009"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5069"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5070",
    browseName="ns=isa95_jobcontrol_v2;FromNotAllowedToStartToAllowedToStart",
    description="This transition is triggered when the Start Method is called.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6107", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5070"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5070"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5063"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5070"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5064"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5070"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7005"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5070"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5071",
    browseName="ns=isa95_jobcontrol_v2;FromAllowedToStartToNotAllowedToStart",
    description="This transition is triggered when the RevokeStart Method is called.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6108", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5071"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5071"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5064"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5071"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5063"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5071"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7013"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5071"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5072",
    browseName="ns=isa95_jobcontrol_v2;FromAllowedToStartToAllowedToStart",
    description="This transition is triggered when the Update Method is called and the job order is modified.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6109", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5072"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5072"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5064"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5072"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5064"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5072"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7009"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5072"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5073",
    browseName="ns=isa95_jobcontrol_v2;FromAllowedToStartToRunning",
    description="This transition is triggered when a job order is started to be executed.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6110", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5073"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5073"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5064"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5073"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5065"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5073"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5074",
    browseName="ns=isa95_jobcontrol_v2;FromRunningToInterrupted",
    description="This transition is triggered when an executing job order gets interrupted, either internally or by the Pause Method.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6111", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5074"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5074"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5065"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5074"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5066"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5074"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7007"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5074"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5075",
    browseName="ns=isa95_jobcontrol_v2;FromRunningToEnded",
    description="This transition is triggered when the execution of a job order has finished, either internally or by the Stop Method.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6112", browseName="TransitionNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5075"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5075"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5065"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5075"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5067"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5075"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7006"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5075"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5076",
    browseName="ns=isa95_jobcontrol_v2;FromRunningToAborted",
    description="This transition is triggered when Abort Method is called.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6113", browseName="TransitionNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5076"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5076"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5065"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5076"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5068"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5076"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7010"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5076"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5077",
    browseName="ns=isa95_jobcontrol_v2;FromInterruptedToAborted",
    description="This transition is triggered when Abort Method is called.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6114", browseName="TransitionNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5077"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5077"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5066"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5077"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5068"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5077"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7010"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5077"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5078",
    browseName="ns=isa95_jobcontrol_v2;FromInterruptedToRunning",
    description="This transition is triggered when Resume Method is called.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6115", browseName="TransitionNumber", dataType=o6.UInt32, value=10))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5078"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5078"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5066"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5078"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5065"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5078"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7008"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5078"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.objtypes.TransitionType(
    nodeId="ns=isa95_jobcontrol_v2;i=5079",
    browseName="ns=isa95_jobcontrol_v2;FromInterruptedToEnded",
    description="This transition is triggered when Stop Method is called.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6116", browseName="TransitionNumber", dataType=o6.UInt32, value=11))],
)
o6.reference(isa95_jobcontrol_v2_objtypes.ISA95JobOrderReceiverSubStatesType, ns0.reftypes.HasComponent, o6.ns["ns=isa95_jobcontrol_v2;i=5079"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5079"], "i=51", o6.ns["ns=isa95_jobcontrol_v2;i=5066"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5079"], "i=52", o6.ns["ns=isa95_jobcontrol_v2;i=5067"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5079"], "i=53", o6.ns["ns=isa95_jobcontrol_v2;i=7006"])
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5079"], "i=54", isa95_jobcontrol_v2_objtypes.ISA95JobOrderStatusEventType)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6117", browseName="ns=isa95_jobcontrol_v2;ISA95JobOrderDataType", dataType=o6.String, value="//xs:element[@name='ISA95JobOrderDataType']"
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5015"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6117"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6118", browseName="ns=isa95_jobcontrol_v2;ISA95JobResponseDataType", dataType=o6.String, value="ISA95JobResponseDataType"
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5026"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6118"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6119", browseName="ns=isa95_jobcontrol_v2;ISA95JobResponseDataType", dataType=o6.String, value="//xs:element[@name='ISA95JobResponseDataType']"
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5027"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6119"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6120", browseName="ns=isa95_jobcontrol_v2;ISA95MaterialDataType", dataType=o6.String, value="ISA95MaterialDataType"
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5017"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6120"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6121", browseName="ns=isa95_jobcontrol_v2;ISA95MaterialDataType", dataType=o6.String, value="//xs:element[@name='ISA95MaterialDataType']"
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5018"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6121"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6122", browseName="ns=isa95_jobcontrol_v2;ISA95ParameterDataType", dataType=o6.String, value="ISA95ParameterDataType"
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5005"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6122"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6123", browseName="ns=isa95_jobcontrol_v2;ISA95ParameterDataType", dataType=o6.String, value="//xs:element[@name='ISA95ParameterDataType']"
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5006"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6123"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6124", browseName="ns=isa95_jobcontrol_v2;ISA95PersonnelDataType", dataType=o6.String, value="ISA95PersonnelDataType"
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5020"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6124"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6125", browseName="ns=isa95_jobcontrol_v2;ISA95PersonnelDataType", dataType=o6.String, value="//xs:element[@name='ISA95PersonnelDataType']"
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5021"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6125"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6126", browseName="ns=isa95_jobcontrol_v2;ISA95PhysicalAssetDataType", dataType=o6.String, value="ISA95PhysicalAssetDataType"
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5023"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6126"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6127",
    browseName="ns=isa95_jobcontrol_v2;ISA95PhysicalAssetDataType",
    dataType=o6.String,
    value="//xs:element[@name='ISA95PhysicalAssetDataType']",
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5024"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6127"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6128", browseName="ns=isa95_jobcontrol_v2;ISA95PropertyDataType", dataType=o6.String, value="ISA95PropertyDataType"
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5002"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6128"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6129", browseName="ns=isa95_jobcontrol_v2;ISA95PropertyDataType", dataType=o6.String, value="//xs:element[@name='ISA95PropertyDataType']"
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5003"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6129"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=isa95_jobcontrol_v2;i=6130", browseName="ns=isa95_jobcontrol_v2;ISA95StateDataType", dataType=o6.String, value="ISA95StateDataType")
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5029"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6130"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6131", browseName="ns=isa95_jobcontrol_v2;ISA95StateDataType", dataType=o6.String, value="//xs:element[@name='ISA95StateDataType']"
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5030"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6131"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6132", browseName="ns=isa95_jobcontrol_v2;ISA95WorkMasterDataType", dataType=o6.String, value="ISA95WorkMasterDataType"
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5011"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6132"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=isa95_jobcontrol_v2;i=6018",
    browseName="ns=isa95_jobcontrol_v2;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=isa95_jobcontrol_v2;i=6019", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/"
            )
        ),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6022"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6031"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6046"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6118"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6120"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6122"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6124"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6126"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6128"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6130"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6132"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ISA95EquipmentDataType">\n  <opc:Documentation>Defines an equipment resource or a piece of equipment, a quantity, an optional description, and an optional collection of properties.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="EquipmentUseSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="QuantitySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="EngineeringUnitsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PropertiesSpecified"/>\n  <opc:Field Length="27" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="ID"/>\n  <opc:Field SwitchField="DescriptionSpecified" TypeName="opc:Int32" Name="NoOfDescription"/>\n  <opc:Field LengthField="NoOfDescription" SwitchField="DescriptionSpecified" TypeName="ua:LocalizedText" Name="Description"/>\n  <opc:Field SwitchField="EquipmentUseSpecified" TypeName="opc:CharArray" Name="EquipmentUse"/>\n  <opc:Field SwitchField="QuantitySpecified" TypeName="opc:CharArray" Name="Quantity"/>\n  <opc:Field SwitchField="EngineeringUnitsSpecified" TypeName="ua:EUInformation" Name="EngineeringUnits"/>\n  <opc:Field SwitchField="PropertiesSpecified" TypeName="opc:Int32" Name="NoOfProperties"/>\n  <opc:Field LengthField="NoOfProperties" SwitchField="PropertiesSpecified" TypeName="tns:ISA95PropertyDataType" Name="Properties"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ISA95JobOrderAndStateDataType">\n  <opc:Documentation>Defines the information needed to schedule and execute a job.</opc:Documentation>\n  <opc:Field TypeName="tns:ISA95JobOrderDataType" Name="JobOrder"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfState"/>\n  <opc:Field LengthField="NoOfState" TypeName="tns:ISA95StateDataType" Name="State"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ISA95JobOrderDataType">\n  <opc:Documentation>Defines the information needed to schedule and execute a job.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="WorkMasterIDSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="StartTimeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="EndTimeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PrioritySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="JobOrderParametersSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PersonnelRequirementsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="EquipmentRequirementsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PhysicalAssetRequirementsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="MaterialRequirementsSpecified"/>\n  <opc:Field Length="22" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="JobOrderID"/>\n  <opc:Field SwitchField="DescriptionSpecified" TypeName="opc:Int32" Name="NoOfDescription"/>\n  <opc:Field LengthField="NoOfDescription" SwitchField="DescriptionSpecified" TypeName="ua:LocalizedText" Name="Description"/>\n  <opc:Field SwitchField="WorkMasterIDSpecified" TypeName="opc:Int32" Name="NoOfWorkMasterID"/>\n  <opc:Field LengthField="NoOfWorkMasterID" SwitchField="WorkMasterIDSpecified" TypeName="tns:ISA95WorkMasterDataType" Name="WorkMasterID"/>\n  <opc:Field SwitchField="StartTimeSpecified" TypeName="opc:DateTime" Name="StartTime"/>\n  <opc:Field SwitchField="EndTimeSpecified" TypeName="opc:DateTime" Name="EndTime"/>\n  <opc:Field SwitchField="PrioritySpecified" TypeName="opc:Int16" Name="Priority"/>\n  <opc:Field SwitchField="JobOrderParametersSpecified" TypeName="opc:Int32" Name="NoOfJobOrderParameters"/>\n  <opc:Field LengthField="NoOfJobOrderParameters" SwitchField="JobOrderParametersSpecified" TypeName="tns:ISA95ParameterDataType" Name="JobOrderParameters"/>\n  <opc:Field SwitchField="PersonnelRequirementsSpecified" TypeName="opc:Int32" Name="NoOfPersonnelRequirements"/>\n  <opc:Field LengthField="NoOfPersonnelRequirements" SwitchField="PersonnelRequirementsSpecified" TypeName="tns:ISA95PersonnelDataType" Name="PersonnelRequirements"/>\n  <opc:Field SwitchField="EquipmentRequirementsSpecified" TypeName="opc:Int32" Name="NoOfEquipmentRequirements"/>\n  <opc:Field LengthField="NoOfEquipmentRequirements" SwitchField="EquipmentRequirementsSpecified" TypeName="tns:ISA95EquipmentDataType" Name="EquipmentRequirements"/>\n  <opc:Field SwitchField="PhysicalAssetRequirementsSpecified" TypeName="opc:Int32" Name="NoOfPhysicalAssetRequirements"/>\n  <opc:Field LengthField="NoOfPhysicalAssetRequirements" SwitchField="PhysicalAssetRequirementsSpecified" TypeName="tns:ISA95PhysicalAssetDataType" Name="PhysicalAssetRequirements"/>\n  <opc:Field SwitchField="MaterialRequirementsSpecified" TypeName="opc:Int32" Name="NoOfMaterialRequirements"/>\n  <opc:Field LengthField="NoOfMaterialRequirements" SwitchField="MaterialRequirementsSpecified" TypeName="tns:ISA95MaterialDataType" Name="MaterialRequirements"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ISA95JobResponseDataType">\n  <opc:Documentation>Defines the information needed to schedule and execute a job.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="StartTimeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="EndTimeSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="JobResponseDataSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PersonnelActualsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="EquipmentActualsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PhysicalAssetActualsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="MaterialActualsSpecified"/>\n  <opc:Field Length="24" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="JobResponseID"/>\n  <opc:Field SwitchField="DescriptionSpecified" TypeName="ua:LocalizedText" Name="Description"/>\n  <opc:Field TypeName="opc:CharArray" Name="JobOrderID"/>\n  <opc:Field SwitchField="StartTimeSpecified" TypeName="opc:DateTime" Name="StartTime"/>\n  <opc:Field SwitchField="EndTimeSpecified" TypeName="opc:DateTime" Name="EndTime"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfJobState"/>\n  <opc:Field LengthField="NoOfJobState" TypeName="tns:ISA95StateDataType" Name="JobState"/>\n  <opc:Field SwitchField="JobResponseDataSpecified" TypeName="opc:Int32" Name="NoOfJobResponseData"/>\n  <opc:Field LengthField="NoOfJobResponseData" SwitchField="JobResponseDataSpecified" TypeName="tns:ISA95ParameterDataType" Name="JobResponseData"/>\n  <opc:Field SwitchField="PersonnelActualsSpecified" TypeName="opc:Int32" Name="NoOfPersonnelActuals"/>\n  <opc:Field LengthField="NoOfPersonnelActuals" SwitchField="PersonnelActualsSpecified" TypeName="tns:ISA95PersonnelDataType" Name="PersonnelActuals"/>\n  <opc:Field SwitchField="EquipmentActualsSpecified" TypeName="opc:Int32" Name="NoOfEquipmentActuals"/>\n  <opc:Field LengthField="NoOfEquipmentActuals" SwitchField="EquipmentActualsSpecified" TypeName="tns:ISA95EquipmentDataType" Name="EquipmentActuals"/>\n  <opc:Field SwitchField="PhysicalAssetActualsSpecified" TypeName="opc:Int32" Name="NoOfPhysicalAssetActuals"/>\n  <opc:Field LengthField="NoOfPhysicalAssetActuals" SwitchField="PhysicalAssetActualsSpecified" TypeName="tns:ISA95PhysicalAssetDataType" Name="PhysicalAssetActuals"/>\n  <opc:Field SwitchField="MaterialActualsSpecified" TypeName="opc:Int32" Name="NoOfMaterialActuals"/>\n  <opc:Field LengthField="NoOfMaterialActuals" SwitchField="MaterialActualsSpecified" TypeName="tns:ISA95MaterialDataType" Name="MaterialActuals"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ISA95MaterialDataType">\n  <opc:Documentation>Defines a material resource, a quantity, an optional description, and an optional collection of properties.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="MaterialClassIDSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="MaterialDefinitionIDSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="MaterialLotIDSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="MaterialSublotIDSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="MaterialUseSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="QuantitySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="EngineeringUnitsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PropertiesSpecified"/>\n  <opc:Field Length="23" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field SwitchField="MaterialClassIDSpecified" TypeName="opc:CharArray" Name="MaterialClassID"/>\n  <opc:Field SwitchField="MaterialDefinitionIDSpecified" TypeName="opc:CharArray" Name="MaterialDefinitionID"/>\n  <opc:Field SwitchField="MaterialLotIDSpecified" TypeName="opc:CharArray" Name="MaterialLotID"/>\n  <opc:Field SwitchField="MaterialSublotIDSpecified" TypeName="opc:CharArray" Name="MaterialSublotID"/>\n  <opc:Field SwitchField="DescriptionSpecified" TypeName="opc:Int32" Name="NoOfDescription"/>\n  <opc:Field LengthField="NoOfDescription" SwitchField="DescriptionSpecified" TypeName="ua:LocalizedText" Name="Description"/>\n  <opc:Field SwitchField="MaterialUseSpecified" TypeName="opc:CharArray" Name="MaterialUse"/>\n  <opc:Field SwitchField="QuantitySpecified" TypeName="opc:CharArray" Name="Quantity"/>\n  <opc:Field SwitchField="EngineeringUnitsSpecified" TypeName="ua:EUInformation" Name="EngineeringUnits"/>\n  <opc:Field SwitchField="PropertiesSpecified" TypeName="opc:Int32" Name="NoOfProperties"/>\n  <opc:Field LengthField="NoOfProperties" SwitchField="PropertiesSpecified" TypeName="tns:ISA95PropertyDataType" Name="Properties"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ISA95ParameterDataType">\n  <opc:Documentation>A subtype of OPC UA Structure that defines three linked data items: the ID, which is a unique identifier for a property, the value, which is the data that is identified, and an optional description of the parameter.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="EngineeringUnitsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SubparametersSpecified"/>\n  <opc:Field Length="29" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="ID"/>\n  <opc:Field TypeName="ua:Variant" Name="Value"/>\n  <opc:Field SwitchField="DescriptionSpecified" TypeName="opc:Int32" Name="NoOfDescription"/>\n  <opc:Field LengthField="NoOfDescription" SwitchField="DescriptionSpecified" TypeName="ua:LocalizedText" Name="Description"/>\n  <opc:Field SwitchField="EngineeringUnitsSpecified" TypeName="ua:EUInformation" Name="EngineeringUnits"/>\n  <opc:Field SwitchField="SubparametersSpecified" TypeName="opc:Int32" Name="NoOfSubparameters"/>\n  <opc:Field LengthField="NoOfSubparameters" SwitchField="SubparametersSpecified" TypeName="tns:ISA95ParameterDataType" Name="Subparameters"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ISA95PersonnelDataType">\n  <opc:Documentation>Defines a personnel resource or a person, a quantity, an optional description, and an optional collection of properties.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PersonnelUseSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="QuantitySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="EngineeringUnitsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PropertiesSpecified"/>\n  <opc:Field Length="27" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="ID"/>\n  <opc:Field SwitchField="DescriptionSpecified" TypeName="opc:Int32" Name="NoOfDescription"/>\n  <opc:Field LengthField="NoOfDescription" SwitchField="DescriptionSpecified" TypeName="ua:LocalizedText" Name="Description"/>\n  <opc:Field SwitchField="PersonnelUseSpecified" TypeName="opc:CharArray" Name="PersonnelUse"/>\n  <opc:Field SwitchField="QuantitySpecified" TypeName="opc:CharArray" Name="Quantity"/>\n  <opc:Field SwitchField="EngineeringUnitsSpecified" TypeName="ua:EUInformation" Name="EngineeringUnits"/>\n  <opc:Field SwitchField="PropertiesSpecified" TypeName="opc:Int32" Name="NoOfProperties"/>\n  <opc:Field LengthField="NoOfProperties" SwitchField="PropertiesSpecified" TypeName="tns:ISA95PropertyDataType" Name="Properties"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ISA95PhysicalAssetDataType">\n  <opc:Documentation>Defines a physical asset, a quantity, an optional description, and an optional collection of properties.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PhysicalAssetUseSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="QuantitySpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="EngineeringUnitsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PropertiesSpecified"/>\n  <opc:Field Length="27" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="ID"/>\n  <opc:Field SwitchField="DescriptionSpecified" TypeName="opc:Int32" Name="NoOfDescription"/>\n  <opc:Field LengthField="NoOfDescription" SwitchField="DescriptionSpecified" TypeName="ua:LocalizedText" Name="Description"/>\n  <opc:Field SwitchField="PhysicalAssetUseSpecified" TypeName="opc:CharArray" Name="PhysicalAssetUse"/>\n  <opc:Field SwitchField="QuantitySpecified" TypeName="opc:CharArray" Name="Quantity"/>\n  <opc:Field SwitchField="EngineeringUnitsSpecified" TypeName="ua:EUInformation" Name="EngineeringUnits"/>\n  <opc:Field SwitchField="PropertiesSpecified" TypeName="opc:Int32" Name="NoOfProperties"/>\n  <opc:Field LengthField="NoOfProperties" SwitchField="PropertiesSpecified" TypeName="tns:ISA95PropertyDataType" Name="Properties"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ISA95PropertyDataType">\n  <opc:Documentation>A subtype of OPC UA Structure that defines two linked data items: an ID, which is a unique identifier for a property within the scope of the associated resource, and the value, which is the data for the property.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="EngineeringUnitsSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="SubpropertiesSpecified"/>\n  <opc:Field Length="29" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="ID"/>\n  <opc:Field TypeName="ua:Variant" Name="Value"/>\n  <opc:Field SwitchField="DescriptionSpecified" TypeName="opc:Int32" Name="NoOfDescription"/>\n  <opc:Field LengthField="NoOfDescription" SwitchField="DescriptionSpecified" TypeName="ua:LocalizedText" Name="Description"/>\n  <opc:Field SwitchField="EngineeringUnitsSpecified" TypeName="ua:EUInformation" Name="EngineeringUnits"/>\n  <opc:Field SwitchField="SubpropertiesSpecified" TypeName="opc:Int32" Name="NoOfSubproperties"/>\n  <opc:Field LengthField="NoOfSubproperties" SwitchField="SubpropertiesSpecified" TypeName="tns:ISA95PropertyDataType" Name="Subproperties"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ISA95StateDataType">\n  <opc:Documentation>Defines the information needed to schedule and execute a job.</opc:Documentation>\n  <opc:Field TypeName="ua:RelativePath" Name="BrowsePath"/>\n  <opc:Field TypeName="ua:LocalizedText" Name="StateText"/>\n  <opc:Field TypeName="opc:UInt32" Name="StateNumber"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ISA95WorkMasterDataType">\n  <opc:Documentation>Defines a Work Master ID and the defined parameters for the Work Master.</opc:Documentation>\n  <opc:Field TypeName="opc:Bit" Name="DescriptionSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="ParametersSpecified"/>\n  <opc:Field Length="30" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:CharArray" Name="ID"/>\n  <opc:Field SwitchField="DescriptionSpecified" TypeName="ua:LocalizedText" Name="Description"/>\n  <opc:Field SwitchField="ParametersSpecified" TypeName="opc:Int32" Name="NoOfParameters"/>\n  <opc:Field LengthField="NoOfParameters" SwitchField="ParametersSpecified" TypeName="tns:ISA95ParameterDataType" Name="Parameters"/>\n </opc:StructuredType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95_jobcontrol_v2;i=6133", browseName="ns=isa95_jobcontrol_v2;ISA95WorkMasterDataType", dataType=o6.String, value="//xs:element[@name='ISA95WorkMasterDataType']"
)
o6.reference(o6.ns["ns=isa95_jobcontrol_v2;i=5012"], "i=39", o6.ns["ns=isa95_jobcontrol_v2;i=6133"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=isa95_jobcontrol_v2;i=6020",
    browseName="ns=isa95_jobcontrol_v2;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=isa95_jobcontrol_v2;i=6021", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/Types.xsd"
            )
        ),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6030"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6032"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6117"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6119"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6121"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6123"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6125"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6127"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6129"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6131"]),
        o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=6133"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/ISA95-JOBCONTROL_V2/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:complexType name="ISA95EquipmentDataType">\n  <xs:annotation>\n   <xs:documentation>Defines an equipment resource or a piece of equipment, a quantity, an optional description, and an optional collection of properties.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfLocalizedText" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="EquipmentUse"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Quantity"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="EngineeringUnits"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95PropertyDataType" name="Properties"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ISA95EquipmentDataType" name="ISA95EquipmentDataType"/>\n <xs:complexType name="ListOfISA95EquipmentDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ISA95EquipmentDataType" name="ISA95EquipmentDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfISA95EquipmentDataType" name="ListOfISA95EquipmentDataType" nillable="true"/>\n <xs:complexType name="ISA95JobOrderAndStateDataType">\n  <xs:annotation>\n   <xs:documentation>Defines the information needed to schedule and execute a job.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ISA95JobOrderDataType" name="JobOrder"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95StateDataType" name="State"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ISA95JobOrderAndStateDataType" name="ISA95JobOrderAndStateDataType"/>\n <xs:complexType name="ListOfISA95JobOrderAndStateDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ISA95JobOrderAndStateDataType" name="ISA95JobOrderAndStateDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfISA95JobOrderAndStateDataType" name="ListOfISA95JobOrderAndStateDataType" nillable="true"/>\n <xs:complexType name="ISA95JobOrderDataType">\n  <xs:annotation>\n   <xs:documentation>Defines the information needed to schedule and execute a job.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="JobOrderID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfLocalizedText" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95WorkMasterDataType" name="WorkMasterID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="StartTime"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="EndTime"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:short" name="Priority"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95ParameterDataType" name="JobOrderParameters"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95PersonnelDataType" name="PersonnelRequirements"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95EquipmentDataType" name="EquipmentRequirements"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95PhysicalAssetDataType" name="PhysicalAssetRequirements"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95MaterialDataType" name="MaterialRequirements"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ISA95JobOrderDataType" name="ISA95JobOrderDataType"/>\n <xs:complexType name="ListOfISA95JobOrderDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ISA95JobOrderDataType" name="ISA95JobOrderDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfISA95JobOrderDataType" name="ListOfISA95JobOrderDataType" nillable="true"/>\n <xs:complexType name="ISA95JobResponseDataType">\n  <xs:annotation>\n   <xs:documentation>Defines the information needed to schedule and execute a job.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="JobResponseID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="JobOrderID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="StartTime"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="EndTime"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95StateDataType" name="JobState"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95ParameterDataType" name="JobResponseData"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95PersonnelDataType" name="PersonnelActuals"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95EquipmentDataType" name="EquipmentActuals"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95PhysicalAssetDataType" name="PhysicalAssetActuals"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95MaterialDataType" name="MaterialActuals"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ISA95JobResponseDataType" name="ISA95JobResponseDataType"/>\n <xs:complexType name="ListOfISA95JobResponseDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ISA95JobResponseDataType" name="ISA95JobResponseDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfISA95JobResponseDataType" name="ListOfISA95JobResponseDataType" nillable="true"/>\n <xs:complexType name="ISA95MaterialDataType">\n  <xs:annotation>\n   <xs:documentation>Defines a material resource, a quantity, an optional description, and an optional collection of properties.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="MaterialClassID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="MaterialDefinitionID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="MaterialLotID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="MaterialSublotID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfLocalizedText" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="MaterialUse"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Quantity"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="EngineeringUnits"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95PropertyDataType" name="Properties"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ISA95MaterialDataType" name="ISA95MaterialDataType"/>\n <xs:complexType name="ListOfISA95MaterialDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ISA95MaterialDataType" name="ISA95MaterialDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfISA95MaterialDataType" name="ListOfISA95MaterialDataType" nillable="true"/>\n <xs:complexType name="ISA95ParameterDataType">\n  <xs:annotation>\n   <xs:documentation>A subtype of OPC UA Structure that defines three linked data items: the ID, which is a unique identifier for a property, the value, which is the data that is identified, and an optional description of the parameter.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:Variant" name="Value"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfLocalizedText" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="EngineeringUnits"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95ParameterDataType" name="Subparameters"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ISA95ParameterDataType" name="ISA95ParameterDataType"/>\n <xs:complexType name="ListOfISA95ParameterDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ISA95ParameterDataType" name="ISA95ParameterDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfISA95ParameterDataType" name="ListOfISA95ParameterDataType" nillable="true"/>\n <xs:complexType name="ISA95PersonnelDataType">\n  <xs:annotation>\n   <xs:documentation>Defines a personnel resource or a person, a quantity, an optional description, and an optional collection of properties.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfLocalizedText" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="PersonnelUse"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Quantity"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="EngineeringUnits"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95PropertyDataType" name="Properties"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ISA95PersonnelDataType" name="ISA95PersonnelDataType"/>\n <xs:complexType name="ListOfISA95PersonnelDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ISA95PersonnelDataType" name="ISA95PersonnelDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfISA95PersonnelDataType" name="ListOfISA95PersonnelDataType" nillable="true"/>\n <xs:complexType name="ISA95PhysicalAssetDataType">\n  <xs:annotation>\n   <xs:documentation>Defines a physical asset, a quantity, an optional description, and an optional collection of properties.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfLocalizedText" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="PhysicalAssetUse"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Quantity"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="EngineeringUnits"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95PropertyDataType" name="Properties"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ISA95PhysicalAssetDataType" name="ISA95PhysicalAssetDataType"/>\n <xs:complexType name="ListOfISA95PhysicalAssetDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ISA95PhysicalAssetDataType" name="ISA95PhysicalAssetDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfISA95PhysicalAssetDataType" name="ListOfISA95PhysicalAssetDataType" nillable="true"/>\n <xs:complexType name="ISA95PropertyDataType">\n  <xs:annotation>\n   <xs:documentation>A subtype of OPC UA Structure that defines two linked data items: an ID, which is a unique identifier for a property within the scope of the associated resource, and the value, which is the data for the property.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:Variant" name="Value"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfLocalizedText" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="EngineeringUnits"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95PropertyDataType" name="Subproperties"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ISA95PropertyDataType" name="ISA95PropertyDataType"/>\n <xs:complexType name="ListOfISA95PropertyDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ISA95PropertyDataType" name="ISA95PropertyDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfISA95PropertyDataType" name="ListOfISA95PropertyDataType" nillable="true"/>\n <xs:complexType name="ISA95StateDataType">\n  <xs:annotation>\n   <xs:documentation>Defines the information needed to schedule and execute a job.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:RelativePath" name="BrowsePath"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="StateText"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="StateNumber"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ISA95StateDataType" name="ISA95StateDataType"/>\n <xs:complexType name="ListOfISA95StateDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ISA95StateDataType" name="ISA95StateDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfISA95StateDataType" name="ListOfISA95StateDataType" nillable="true"/>\n <xs:complexType name="ISA95WorkMasterDataType">\n  <xs:annotation>\n   <xs:documentation>Defines a Work Master ID and the defined parameters for the Work Master.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfISA95ParameterDataType" name="Parameters"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ISA95WorkMasterDataType" name="ISA95WorkMasterDataType"/>\n <xs:complexType name="ListOfISA95WorkMasterDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ISA95WorkMasterDataType" name="ISA95WorkMasterDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfISA95WorkMasterDataType" name="ListOfISA95WorkMasterDataType" nillable="true"/>\n</xs:schema>\n',
)


del Any, TYPE_CHECKING, uuid, o6, ns0, isa95_jobcontrol_v2_datypes, isa95_jobcontrol_v2_objtypes
