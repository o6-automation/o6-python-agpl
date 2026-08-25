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

"""Generated OPC UA wire_harness namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.machinery_result as machinery_result
import o6.ns.ns0 as ns0
import o6.ns.wire_harness_vec as wire_harness_vec
from . import datatypes as wire_harness_datypes
from . import objtypes as wire_harness_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5007", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5008", browseName="Default XML")
o6.hasEncoding(wire_harness_datypes.CutInputDataType, o6.ns["ns=wire_harness;i=5008"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5011", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5012", browseName="Default XML")
o6.hasEncoding(wire_harness_datypes.ProcessOutputDataType, o6.ns["ns=wire_harness;i=5012"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5016", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5017", browseName="Default XML")
o6.hasEncoding(wire_harness_datypes.ForceCurvePointDataType, o6.ns["ns=wire_harness;i=5017"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5037", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5038", browseName="Default XML")
o6.hasEncoding(wire_harness_datypes.StripInputDataType, o6.ns["ns=wire_harness;i=5038"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5039", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5040", browseName="Default XML")
o6.hasEncoding(wire_harness_datypes.CrimpInputDataType, o6.ns["ns=wire_harness;i=5040"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5041", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5042", browseName="Default XML")
o6.hasEncoding(wire_harness_datypes.CutOutputDataType, o6.ns["ns=wire_harness;i=5042"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5046", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5047", browseName="Default XML")
o6.hasEncoding(wire_harness_datypes.ForceCurveDataType, o6.ns["ns=wire_harness;i=5047"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5059", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5060", browseName="Default XML")
o6.hasEncoding(wire_harness_datypes.StripOutputDataType, o6.ns["ns=wire_harness;i=5060"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5063", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5064", browseName="Default XML")
o6.hasEncoding(wire_harness_datypes.CrimpOutputDataType, o6.ns["ns=wire_harness;i=5064"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5071", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5072", browseName="Default XML")
o6.hasEncoding(wire_harness_datypes.SealInputDataType, o6.ns["ns=wire_harness;i=5072"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5073", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness;i=5074", browseName="Default XML")
o6.hasEncoding(wire_harness_datypes.SealOutputDataType, o6.ns["ns=wire_harness;i=5074"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashWireHarnessSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=wire_harness;i=5000",
    browseName="ns=wire_harness;http://opcfoundation.org/UA/WireHarness/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wire_harness;i=6000", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=wire_harness;i=6001", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-04-01T00:00:00Z"))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wire_harness;i=6002", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/WireHarness/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wire_harness;i=6003", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wire_harness;i=6004",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=wire_harness;i=6005", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wire_harness;i=6006", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wire_harness;i=6007", browseName="DefaultRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0]
            )
        ),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
wire_harness_objtypes.WireHarnessMachineIdentificationType(
    nodeId="ns=wire_harness;i=5001",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wire_harness;i=6009",
                browseName="ns=di;AssetId",
                description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wire_harness;i=6010",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wire_harness;i=6011",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wire_harness;i=6012",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(wire_harness_objtypes.WireHarnessMachineType, ns0.reftypes.HasAddIn, o6.ns["ns=wire_harness;i=5001"])
ns0.vartypes.FiniteStateVariableType(nodeId="ns=wire_harness;i=6015", browseName="CurrentState", dataType=o6.LocalizedText)
o6.reference(o6.ns["ns=wire_harness;i=6015"], "i=46", "i=3728")
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=wire_harness;i=5003", browseName="ns=machinery;MachineryItemState", references=[o6.hasComponent(o6.ns["ns=wire_harness;i=6015"])]
)
ns0.vartypes.FiniteStateVariableType(nodeId="ns=wire_harness;i=6016", browseName="CurrentState", dataType=o6.LocalizedText)
o6.reference(o6.ns["ns=wire_harness;i=6016"], "i=46", "i=3728")
machinery.objtypes.MachineryOperationModeStateMachineType(
    nodeId="ns=wire_harness;i=5004", browseName="ns=machinery;MachineryOperationMode", references=[o6.hasComponent(o6.ns["ns=wire_harness;i=6016"])]
)
wire_harness_objtypes.ArticleSpecManagementType(
    nodeId="ns=wire_harness;i=5010",
    browseName="ns=wire_harness;ArticleSpecManagement",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=wire_harness;i=6019",
                browseName="ns=wire_harness;ArticleSpecList",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95MaterialDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
)
o6.reference(wire_harness_objtypes.WireHarnessMachineType, ns0.reftypes.HasComponent, o6.ns["ns=wire_harness;i=5010"])
o6.reference(o6.ns["ns=wire_harness;i=5010"], "i=47", o6.ns["ns=wire_harness;i=7017"])
o6.reference(o6.ns["ns=wire_harness;i=5010"], "i=47", o6.ns["ns=wire_harness;i=7018"])
baseObject = ns0.objtypes.BaseObjectType(
    nodeId="ns=wire_harness;i=5015",
    browseName="ns=wire_harness;BaseObject",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=wire_harness;i=6035",
                browseName="ns=wire_harness;BaseDataVariable",
                dataType=isa95_jobcontrol_v2.datatypes.ISA95MaterialDataType,
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
    parent="i=2253",
    referenceType=ns0.reftypes.Organizes,
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6060", browseName="ns=wire_harness;ForceCurveDataType", dataType=o6.String, value="ForceCurveDataType", accessLevel=3, userAccessLevel=1
)
o6.reference(o6.ns["ns=wire_harness;i=5046"], "i=39", o6.ns["ns=wire_harness;i=6060"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6063", browseName="ns=wire_harness;CrimpInputDataType", dataType=o6.String, value="CrimpInputDataType", accessLevel=3, userAccessLevel=1
)
o6.reference(o6.ns["ns=wire_harness;i=5039"], "i=39", o6.ns["ns=wire_harness;i=6063"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6064", browseName="ns=wire_harness;CutInputDataType", dataType=o6.String, value="CutInputDataType", accessLevel=3, userAccessLevel=1
)
o6.reference(o6.ns["ns=wire_harness;i=5007"], "i=39", o6.ns["ns=wire_harness;i=6064"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6065", browseName="ns=wire_harness;SealInputDataType", dataType=o6.String, value="SealInputDataType", accessLevel=3, userAccessLevel=1
)
o6.reference(o6.ns["ns=wire_harness;i=5071"], "i=39", o6.ns["ns=wire_harness;i=6065"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6068", browseName="ns=wire_harness;StripInputDataType", dataType=o6.String, value="StripInputDataType", accessLevel=3, userAccessLevel=1
)
o6.reference(o6.ns["ns=wire_harness;i=5037"], "i=39", o6.ns["ns=wire_harness;i=6068"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6069", browseName="ns=wire_harness;ProcessOutputDataType", dataType=o6.String, value="ProcessOutputDataType", accessLevel=3, userAccessLevel=1
)
o6.reference(o6.ns["ns=wire_harness;i=5011"], "i=39", o6.ns["ns=wire_harness;i=6069"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6070", browseName="ns=wire_harness;CrimpOutputDataType", dataType=o6.String, value="CrimpOutputDataType", accessLevel=3, userAccessLevel=1
)
o6.reference(o6.ns["ns=wire_harness;i=5063"], "i=39", o6.ns["ns=wire_harness;i=6070"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6071", browseName="ns=wire_harness;CutOutputDataType", dataType=o6.String, value="CutOutputDataType", accessLevel=3, userAccessLevel=1
)
o6.reference(o6.ns["ns=wire_harness;i=5041"], "i=39", o6.ns["ns=wire_harness;i=6071"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6072", browseName="ns=wire_harness;SealOutputDataType", dataType=o6.String, value="SealOutputDataType", accessLevel=3, userAccessLevel=1
)
o6.reference(o6.ns["ns=wire_harness;i=5073"], "i=39", o6.ns["ns=wire_harness;i=6072"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness;i=6073", browseName="ns=wire_harness;ForceCurvePointDataType", dataType=o6.String, value="ForceCurvePointDataType")
o6.reference(o6.ns["ns=wire_harness;i=5016"], "i=39", o6.ns["ns=wire_harness;i=6073"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6074", browseName="ns=wire_harness;StripOutputDataType", dataType=o6.String, value="StripOutputDataType", accessLevel=3, userAccessLevel=1
)
o6.reference(o6.ns["ns=wire_harness;i=5059"], "i=39", o6.ns["ns=wire_harness;i=6074"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=wire_harness;i=6029",
    browseName="ns=wire_harness;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/WireHarness/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wire_harness;i=6030", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/WireHarness/", accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6060"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6063"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6064"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6065"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6068"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6069"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6070"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6071"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6072"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6073"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6074"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/WireHarness/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ns1="http://opcfoundation.org/UA/WireHarness/VEC/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/WireHarness/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:Import Namespace="http://opcfoundation.org/UA/WireHarness/VEC/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ForceCurveDataType">\n  <opc:Field TypeName="opc:Int32" Name="NoOfPoints"/>\n  <opc:Field LengthField="NoOfPoints" TypeName="tns:ForceCurvePointDataType" Name="Points"/>\n  <opc:Field TypeName="ua:EUInformation" Name="EngineeringUnitsX"/>\n  <opc:Field TypeName="ua:EUInformation" Name="EngineeringUnitsValue"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ForceCurvePointDataType">\n  <opc:Field TypeName="opc:Int32" Name="NoOfX"/>\n  <opc:Field LengthField="NoOfX" TypeName="opc:UInt32" Name="X"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfValue"/>\n  <opc:Field LengthField="NoOfValue" TypeName="opc:UInt32" Name="Value"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ProcessInputDataType">\n  <opc:Field TypeName="opc:Int32" Name="NoOfToolType"/>\n  <opc:Field LengthField="NoOfToolType" TypeName="opc:CharArray" Name="ToolType"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfProcessDescription"/>\n  <opc:Field LengthField="NoOfProcessDescription" TypeName="opc:CharArray" Name="ProcessDescription"/>\n  <opc:Field TypeName="opc:CharArray" Name="Id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ProcessInputDataType" Name="CrimpInputDataType">\n  <opc:Field SourceType="tns:ProcessInputDataType" TypeName="opc:Int32" Name="NoOfToolType"/>\n  <opc:Field LengthField="NoOfToolType" SourceType="tns:ProcessInputDataType" TypeName="opc:CharArray" Name="ToolType"/>\n  <opc:Field SourceType="tns:ProcessInputDataType" TypeName="opc:Int32" Name="NoOfProcessDescription"/>\n  <opc:Field LengthField="NoOfProcessDescription" SourceType="tns:ProcessInputDataType" TypeName="opc:CharArray" Name="ProcessDescription"/>\n  <opc:Field SourceType="tns:ProcessInputDataType" TypeName="opc:CharArray" Name="Id"/>\n  <opc:Field TypeName="ns1:WireMountingIdDataType" Name="ReferencedElement"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfVerifyCrimpHeight"/>\n  <opc:Field LengthField="NoOfVerifyCrimpHeight" TypeName="opc:Boolean" Name="VerifyCrimpHeight"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfVerifyCrimpWidth"/>\n  <opc:Field LengthField="NoOfVerifyCrimpWidth" TypeName="opc:Boolean" Name="VerifyCrimpWidth"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfVerifyInsulationCrimpHeight"/>\n  <opc:Field LengthField="NoOfVerifyInsulationCrimpHeight" TypeName="opc:Boolean" Name="VerifyInsulationCrimpHeight"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfVerifyInsulationCrimpWidth"/>\n  <opc:Field LengthField="NoOfVerifyInsulationCrimpWidth" TypeName="opc:Boolean" Name="VerifyInsulationCrimpWidth"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfVerifyPullOutForce"/>\n  <opc:Field LengthField="NoOfVerifyPullOutForce" TypeName="opc:Boolean" Name="VerifyPullOutForce"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfCrimpForceMonitoring"/>\n  <opc:Field LengthField="NoOfCrimpForceMonitoring" TypeName="opc:Boolean" Name="CrimpForceMonitoring"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ProcessInputDataType" Name="CutInputDataType">\n  <opc:Field SourceType="tns:ProcessInputDataType" TypeName="opc:Int32" Name="NoOfToolType"/>\n  <opc:Field LengthField="NoOfToolType" SourceType="tns:ProcessInputDataType" TypeName="opc:CharArray" Name="ToolType"/>\n  <opc:Field SourceType="tns:ProcessInputDataType" TypeName="opc:Int32" Name="NoOfProcessDescription"/>\n  <opc:Field LengthField="NoOfProcessDescription" SourceType="tns:ProcessInputDataType" TypeName="opc:CharArray" Name="ProcessDescription"/>\n  <opc:Field SourceType="tns:ProcessInputDataType" TypeName="opc:CharArray" Name="Id"/>\n  <opc:Field TypeName="ns1:WireElementReferenceIdDataType" Name="ReferencedElement"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfVerifyWireLength"/>\n  <opc:Field LengthField="NoOfVerifyWireLength" TypeName="opc:Boolean" Name="VerifyWireLength"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ProcessInputDataType" Name="SealInputDataType">\n  <opc:Field SourceType="tns:ProcessInputDataType" TypeName="opc:Int32" Name="NoOfToolType"/>\n  <opc:Field LengthField="NoOfToolType" SourceType="tns:ProcessInputDataType" TypeName="opc:CharArray" Name="ToolType"/>\n  <opc:Field SourceType="tns:ProcessInputDataType" TypeName="opc:Int32" Name="NoOfProcessDescription"/>\n  <opc:Field LengthField="NoOfProcessDescription" SourceType="tns:ProcessInputDataType" TypeName="opc:CharArray" Name="ProcessDescription"/>\n  <opc:Field SourceType="tns:ProcessInputDataType" TypeName="opc:CharArray" Name="Id"/>\n  <opc:Field TypeName="ns1:WireMountingIdDataType" Name="ReferencedElement"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfMonitorSealPosition"/>\n  <opc:Field LengthField="NoOfMonitorSealPosition" TypeName="opc:Boolean" Name="MonitorSealPosition"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ProcessInputDataType" Name="StripInputDataType">\n  <opc:Field SourceType="tns:ProcessInputDataType" TypeName="opc:Int32" Name="NoOfToolType"/>\n  <opc:Field LengthField="NoOfToolType" SourceType="tns:ProcessInputDataType" TypeName="opc:CharArray" Name="ToolType"/>\n  <opc:Field SourceType="tns:ProcessInputDataType" TypeName="opc:Int32" Name="NoOfProcessDescription"/>\n  <opc:Field LengthField="NoOfProcessDescription" SourceType="tns:ProcessInputDataType" TypeName="opc:CharArray" Name="ProcessDescription"/>\n  <opc:Field SourceType="tns:ProcessInputDataType" TypeName="opc:CharArray" Name="Id"/>\n  <opc:Field TypeName="ns1:WireEndIdDataType" Name="ReferencedElement"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfStrippingLengthMonitoring"/>\n  <opc:Field LengthField="NoOfStrippingLengthMonitoring" TypeName="opc:Boolean" Name="StrippingLengthMonitoring"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ProcessOutputDataType">\n  <opc:Field TypeName="opc:CharArray" Name="ToolInstance"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ProcessOutputDataType" Name="CrimpOutputDataType">\n  <opc:Field SourceType="tns:ProcessOutputDataType" TypeName="opc:CharArray" Name="ToolInstance"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfActualCrimpHeight"/>\n  <opc:Field LengthField="NoOfActualCrimpHeight" TypeName="ns1:NumericalValue" Name="ActualCrimpHeight"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfActualCrimpWidth"/>\n  <opc:Field LengthField="NoOfActualCrimpWidth" TypeName="ns1:NumericalValue" Name="ActualCrimpWidth"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfActualInsulationCrimpHeight"/>\n  <opc:Field LengthField="NoOfActualInsulationCrimpHeight" TypeName="ns1:NumericalValue" Name="ActualInsulationCrimpHeight"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfActualCrimpForceCurve"/>\n  <opc:Field LengthField="NoOfActualCrimpForceCurve" TypeName="tns:ForceCurveDataType" Name="ActualCrimpForceCurve"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfActualCrimpPullOutForce"/>\n  <opc:Field LengthField="NoOfActualCrimpPullOutForce" TypeName="ns1:NumericalValue" Name="ActualCrimpPullOutForce"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ProcessOutputDataType" Name="CutOutputDataType">\n  <opc:Field SourceType="tns:ProcessOutputDataType" TypeName="opc:CharArray" Name="ToolInstance"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfActualLength"/>\n  <opc:Field LengthField="NoOfActualLength" TypeName="ns1:NumericalValue" Name="ActualLength"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ProcessOutputDataType" Name="SealOutputDataType">\n  <opc:Field SourceType="tns:ProcessOutputDataType" TypeName="opc:CharArray" Name="ToolInstance"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfActualPosition"/>\n  <opc:Field LengthField="NoOfActualPosition" TypeName="ns1:NumericalValue" Name="ActualPosition"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ProcessOutputDataType" Name="StripOutputDataType">\n  <opc:Field SourceType="tns:ProcessOutputDataType" TypeName="opc:CharArray" Name="ToolInstance"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfActualStrippingLength"/>\n  <opc:Field LengthField="NoOfActualStrippingLength" TypeName="ns1:NumericalValue" Name="ActualStrippingLength"/>\n </opc:StructuredType>\n</opc:TypeDictionary>\n',
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6081", browseName="ns=wire_harness;ForceCurvePointDataType", dataType=o6.String, value="//xs:element[@name='ForceCurvePointDataType']"
)
o6.reference(o6.ns["ns=wire_harness;i=5017"], "i=39", o6.ns["ns=wire_harness;i=6081"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6082",
    browseName="ns=wire_harness;ForceCurveDataType",
    dataType=o6.String,
    value="//xs:element[@name='ForceCurveDataType']",
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=wire_harness;i=5047"], "i=39", o6.ns["ns=wire_harness;i=6082"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6085",
    browseName="ns=wire_harness;CrimpInputDataType",
    dataType=o6.String,
    value="//xs:element[@name='CrimpInputDataType']",
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=wire_harness;i=5040"], "i=39", o6.ns["ns=wire_harness;i=6085"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6086",
    browseName="ns=wire_harness;CutInputDataType",
    dataType=o6.String,
    value="//xs:element[@name='CutInputDataType']",
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=wire_harness;i=5008"], "i=39", o6.ns["ns=wire_harness;i=6086"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6087",
    browseName="ns=wire_harness;SealInputDataType",
    dataType=o6.String,
    value="//xs:element[@name='SealInputDataType']",
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=wire_harness;i=5072"], "i=39", o6.ns["ns=wire_harness;i=6087"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6090",
    browseName="ns=wire_harness;StripInputDataType",
    dataType=o6.String,
    value="//xs:element[@name='StripInputDataType']",
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=wire_harness;i=5038"], "i=39", o6.ns["ns=wire_harness;i=6090"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6091",
    browseName="ns=wire_harness;ProcessOutputDataType",
    dataType=o6.String,
    value="//xs:element[@name='ProcessOutputDataType']",
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=wire_harness;i=5012"], "i=39", o6.ns["ns=wire_harness;i=6091"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6092",
    browseName="ns=wire_harness;CrimpOutputDataType",
    dataType=o6.String,
    value="//xs:element[@name='CrimpOutputDataType']",
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=wire_harness;i=5064"], "i=39", o6.ns["ns=wire_harness;i=6092"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6093",
    browseName="ns=wire_harness;CutOutputDataType",
    dataType=o6.String,
    value="//xs:element[@name='CutOutputDataType']",
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=wire_harness;i=5042"], "i=39", o6.ns["ns=wire_harness;i=6093"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6094",
    browseName="ns=wire_harness;SealOutputDataType",
    dataType=o6.String,
    value="//xs:element[@name='SealOutputDataType']",
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=wire_harness;i=5074"], "i=39", o6.ns["ns=wire_harness;i=6094"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness;i=6096",
    browseName="ns=wire_harness;StripOutputDataType",
    dataType=o6.String,
    value="//xs:element[@name='StripOutputDataType']",
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=wire_harness;i=5060"], "i=39", o6.ns["ns=wire_harness;i=6096"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=wire_harness;i=6031",
    browseName="ns=wire_harness;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/WireHarness/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wire_harness;i=6032",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/WireHarness/Types.xsd",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6081"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6082"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6085"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6086"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6087"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6090"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6091"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6092"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6093"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6094"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=6096"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/WireHarness/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/WireHarness/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:ns6="http://opcfoundation.org/UA/WireHarness/VEC/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:import namespace="http://opcfoundation.org/UA/WireHarness/VEC/Types.xsd"/>\n <xs:complexType name="ForceCurveDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfForceCurvePointDataType" name="Points"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="EngineeringUnitsX"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="EngineeringUnitsValue"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ForceCurveDataType" name="ForceCurveDataType"/>\n <xs:complexType name="ListOfForceCurveDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ForceCurveDataType" name="ForceCurveDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfForceCurveDataType" name="ListOfForceCurveDataType" nillable="true"/>\n <xs:complexType name="ForceCurvePointDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfUInt32" name="X"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfUInt32" name="Value"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ForceCurvePointDataType" name="ForceCurvePointDataType"/>\n <xs:complexType name="ListOfForceCurvePointDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ForceCurvePointDataType" name="ForceCurvePointDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfForceCurvePointDataType" name="ListOfForceCurvePointDataType" nillable="true"/>\n <xs:complexType name="ProcessInputDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="ToolType"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="ProcessDescription"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Id"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ProcessInputDataType" name="ProcessInputDataType"/>\n <xs:complexType name="ListOfProcessInputDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ProcessInputDataType" name="ProcessInputDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfProcessInputDataType" name="ListOfProcessInputDataType" nillable="true"/>\n <xs:complexType name="CrimpInputDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ns6:WireMountingIdDataType" name="ReferencedElement"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfBoolean" name="VerifyCrimpHeight"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfBoolean" name="VerifyCrimpWidth"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfBoolean" name="VerifyInsulationCrimpHeight"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfBoolean" name="VerifyInsulationCrimpWidth"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfBoolean" name="VerifyPullOutForce"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfBoolean" name="CrimpForceMonitoring"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CrimpInputDataType" name="CrimpInputDataType"/>\n <xs:complexType name="ListOfCrimpInputDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CrimpInputDataType" name="CrimpInputDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCrimpInputDataType" name="ListOfCrimpInputDataType" nillable="true"/>\n <xs:complexType name="CutInputDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ns6:WireElementReferenceIdDataType" name="ReferencedElement"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfBoolean" name="VerifyWireLength"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CutInputDataType" name="CutInputDataType"/>\n <xs:complexType name="ListOfCutInputDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CutInputDataType" name="CutInputDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCutInputDataType" name="ListOfCutInputDataType" nillable="true"/>\n <xs:complexType name="SealInputDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ns6:WireMountingIdDataType" name="ReferencedElement"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfBoolean" name="MonitorSealPosition"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:SealInputDataType" name="SealInputDataType"/>\n <xs:complexType name="ListOfSealInputDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SealInputDataType" name="SealInputDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSealInputDataType" name="ListOfSealInputDataType" nillable="true"/>\n <xs:complexType name="StripInputDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ns6:WireEndIdDataType" name="ReferencedElement"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfBoolean" name="StrippingLengthMonitoring"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:StripInputDataType" name="StripInputDataType"/>\n <xs:complexType name="ListOfStripInputDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:StripInputDataType" name="StripInputDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfStripInputDataType" name="ListOfStripInputDataType" nillable="true"/>\n <xs:complexType name="ProcessOutputDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ToolInstance"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ProcessOutputDataType" name="ProcessOutputDataType"/>\n <xs:complexType name="ListOfProcessOutputDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ProcessOutputDataType" name="ProcessOutputDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfProcessOutputDataType" name="ListOfProcessOutputDataType" nillable="true"/>\n <xs:complexType name="CrimpOutputDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:ProcessOutputDataType">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ns6:ListOfNumericalValue" name="ActualCrimpHeight"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ns6:ListOfNumericalValue" name="ActualCrimpWidth"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ns6:ListOfNumericalValue" name="ActualInsulationCrimpHeight"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfForceCurveDataType" name="ActualCrimpForceCurve"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ns6:ListOfNumericalValue" name="ActualCrimpPullOutForce"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CrimpOutputDataType" name="CrimpOutputDataType"/>\n <xs:complexType name="ListOfCrimpOutputDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CrimpOutputDataType" name="CrimpOutputDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCrimpOutputDataType" name="ListOfCrimpOutputDataType" nillable="true"/>\n <xs:complexType name="CutOutputDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:ProcessOutputDataType">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ns6:ListOfNumericalValue" name="ActualLength"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CutOutputDataType" name="CutOutputDataType"/>\n <xs:complexType name="ListOfCutOutputDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CutOutputDataType" name="CutOutputDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCutOutputDataType" name="ListOfCutOutputDataType" nillable="true"/>\n <xs:complexType name="SealOutputDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:ProcessOutputDataType">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ns6:ListOfNumericalValue" name="ActualPosition"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:SealOutputDataType" name="SealOutputDataType"/>\n <xs:complexType name="ListOfSealOutputDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SealOutputDataType" name="SealOutputDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSealOutputDataType" name="ListOfSealOutputDataType" nillable="true"/>\n <xs:complexType name="StripOutputDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:ProcessOutputDataType">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ns6:ListOfNumericalValue" name="ActualStrippingLength"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:StripOutputDataType" name="StripOutputDataType"/>\n <xs:complexType name="ListOfStripOutputDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:StripOutputDataType" name="StripOutputDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfStripOutputDataType" name="ListOfStripOutputDataType" nillable="true"/>\n</xs:schema>\n',
    accessLevel=3,
    userAccessLevel=1,
)


o6.call(nodeId="ns=wire_harness;i=7000", browseName="ns=isa95_jobcontrol_v2;Store")
o6.reference(o6.ns["ns=wire_harness;i=7000"], "i=46", "ns=isa95_jobcontrol_v2;i=6040")
o6.reference(o6.ns["ns=wire_harness;i=7000"], "i=46", "ns=isa95_jobcontrol_v2;i=6041")

ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6013",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(
            name="Filter",
            dataType=ns0.datatypes.ContentFilter,
            valueRank=-1,
            description=o6.LocalizedText(
                "Filter used to filter for specific results based on the meta data of the results. Valid BrowsePaths used in the filter can be built from the fields of the ResultReadyEventType, the ResultType VariableType or the ResultDataType or corresponding subtypes."
            ),
        ),
        ns0.datatypes.Argument(
            name="OrderedBy",
            dataType=ns0.datatypes.RelativePath,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "An array of BrowsePaths (as array of QualifiedName) identifying the ordering criteria for the results. If the array is null or empty, no ordering is executed.\nIf several BrowsePaths are provided, the first entry in the array is used as first ordering criteria, etc."
            ),
        ),
        ns0.datatypes.Argument(
            name="MaxResults",
            dataType=o6.UInt32,
            valueRank=-1,
            description=o6.LocalizedText("Defines how many resultIds the Client wants to receive at most. If no maximum should be provided, it is set to 0."),
        ),
        ns0.datatypes.Argument(
            name="Timeout",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "With this argument the client can give a hint to the server how long it will need access to the result data.\nA value &gt; 0 indicates an estimated maximum time for processing the data in milliseconds. \nA value = 0 indicates that the client will not need anything besides the data returned by the method call.\nA value &lt; 0 indicates that the client cannot give an estimate.\nThe client cannot rely on the data being available during the indicated time period. The argument is merely a hint allowing the server to optimize its resource management."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6014",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ResultHandle",
            dataType=ns0.datatypes.Handle,
            valueRank=-1,
            description=o6.LocalizedText(
                "The server shall return to each client requesting result data a system-wide unique handle identifying the result set / client combination. This handle has to be used by the client to release the result set.\nIf the instance of ResultManagementType does not support the ReleaseResultHandle Method, the resultHandle should always be set to 0.\nIf the error is set to a value other than 0, the resultHandle may be set to 0."
            ),
        ),
        ns0.datatypes.Argument(
            name="ResultIdList",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("List of resultIds of results matching the Filter."),
        ),
        ns0.datatypes.Argument(
            name="Error",
            dataType=o6.Int32,
            valueRank=-1,
            description=o6.LocalizedText(
                "0 &#8211; OK\nValues &gt; 0 are reserved for errors defined by this and future standards.\nValues &lt; 0 shall be used for application-specific errors."
            ),
        ),
    ],
)
o6.call(
    nodeId="ns=wire_harness;i=7001",
    browseName="ns=machinery_result;GetResultIdListFiltered",
    inputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6013"]),
    outputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6014"]),
)

machinery_result.objtypes.ResultManagementType(
    nodeId="ns=wire_harness;i=5043",
    browseName="ns=machinery_result;ResultManagement",
    references=[
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=wire_harness;i=5044", browseName="ns=machinery_result;Results")),
        o6.hasComponent(o6.ns["ns=wire_harness;i=7001"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6033",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TypeNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=wire_harness;i=7010", browseName="ns=wire_harness;FindPartsByType", inputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6033"]))

wire_harness_objtypes.PartManagementType(
    nodeId="ns=wire_harness;i=5045", browseName="ns=wire_harness;PartManagement", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=wire_harness;i=7010"])]
)
o6.reference(wire_harness_objtypes.WireHarnessMachineType, ns0.reftypes.HasComponent, o6.ns["ns=wire_harness;i=5045"])
o6.reference(o6.ns["ns=wire_harness;i=5045"], "i=47", o6.ns["ns=wire_harness;i=7015"])
o6.reference(o6.ns["ns=wire_harness;i=5045"], "i=47", o6.ns["ns=wire_harness;i=7016"])


o6.call(nodeId="ns=wire_harness;i=7011", browseName="ns=isa95_jobcontrol_v2;Clear")
o6.reference(o6.ns["ns=wire_harness;i=7011"], "i=46", "ns=isa95_jobcontrol_v2;i=6067")
o6.reference(o6.ns["ns=wire_harness;i=7011"], "i=46", "ns=isa95_jobcontrol_v2;i=6068")

o6.call(nodeId="ns=wire_harness;i=7012", browseName="ns=isa95_jobcontrol_v2;Start")
o6.reference(o6.ns["ns=wire_harness;i=7012"], "i=46", "ns=isa95_jobcontrol_v2;i=6053")
o6.reference(o6.ns["ns=wire_harness;i=7012"], "i=46", "ns=isa95_jobcontrol_v2;i=6054")

o6.call(nodeId="ns=wire_harness;i=7013", browseName="ns=isa95_jobcontrol_v2;Abort")
o6.reference(o6.ns["ns=wire_harness;i=7013"], "i=46", "ns=isa95_jobcontrol_v2;i=6063")
o6.reference(o6.ns["ns=wire_harness;i=7013"], "i=46", "ns=isa95_jobcontrol_v2;i=6064")

isa95_jobcontrol_v2.objtypes.ISA95JobOrderReceiverObjectType(
    nodeId="ns=wire_harness;i=5013",
    browseName="ns=machinery_jobs;JobOrderControl",
    references=[
        o6.hasComponent(o6.ns["ns=wire_harness;i=7000"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=7011"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=7012"]),
        o6.hasComponent(o6.ns["ns=wire_harness;i=7013"]),
    ],
)
o6.reference(o6.ns["ns=wire_harness;i=5013"], "i=46", "ns=machinery_jobs;i=6005")
o6.reference(o6.ns["ns=wire_harness;i=5013"], "i=47", "ns=machinery_jobs;i=6001")
o6.reference(o6.ns["ns=wire_harness;i=5013"], "i=47", "ns=machinery_jobs;i=6002")
o6.reference(o6.ns["ns=wire_harness;i=5013"], "i=47", "ns=machinery_jobs;i=6003")
o6.reference(o6.ns["ns=wire_harness;i=5013"], "i=47", "ns=machinery_jobs;i=6004")
o6.reference(o6.ns["ns=wire_harness;i=5013"], "i=47", "ns=machinery_jobs;i=6006")
o6.reference(o6.ns["ns=wire_harness;i=5013"], "i=47", "ns=machinery_jobs;i=6007")
o6.reference(o6.ns["ns=wire_harness;i=5013"], "i=47", "ns=machinery_jobs;i=6008")
o6.reference(o6.ns["ns=wire_harness;i=5013"], "i=47", "ns=machinery_jobs;i=6009")
machinery_jobs.objtypes.JobManagementType(
    nodeId="ns=wire_harness;i=5005", browseName="ns=machinery_jobs;JobManagement", references=[o6.hasComponent(o6.ns["ns=wire_harness;i=5013"])]
)
o6.reference(o6.ns["ns=wire_harness;i=5005"], "i=47", "ns=machinery_jobs;i=5002")
ns0.objtypes.FolderType(
    nodeId="ns=wire_harness;i=5002",
    browseName="ns=machinery;MachineryBuildingBlocks",
    modellingRule="Mandatory",
    references=[
        o6.hasAddIn(o6.ns["ns=wire_harness;i=5003"]),
        o6.hasAddIn(o6.ns["ns=wire_harness;i=5004"]),
        o6.hasAddIn(o6.ns["ns=wire_harness;i=5005"]),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=wire_harness;i=5006", browseName="ns=di;OperationCounters")),
        o6.hasAddIn(o6.ns["ns=wire_harness;i=5043"]),
    ],
)
o6.reference(wire_harness_objtypes.WireHarnessMachineType, ns0.reftypes.HasComponent, o6.ns["ns=wire_harness;i=5002"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, machinery_result, ns0, wire_harness_vec, wire_harness_datypes, wire_harness_objtypes
