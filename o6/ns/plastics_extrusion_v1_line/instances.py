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

"""Generated OPC UA plastics_extrusion_v1_line namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_extrusion_v1_line_datypes
from . import objtypes as plastics_extrusion_v1_line_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_extrusion_v1_line;i=5007", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_extrusion_v1_line;i=5008", browseName="Default XML")
o6.hasEncoding(plastics_extrusion_v1_line_datypes.MaterialMappingType, o6.ns["ns=plastics_extrusion_v1_line;i=5008"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=plastics_extrusion_v1_line;i=5009", browseName="Default JSON")
o6.hasEncoding(plastics_extrusion_v1_line_datypes.MaterialMappingType, o6.ns["ns=plastics_extrusion_v1_line;i=5009"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6002",
    browseName="ns=plastics_extrusion_v1_line;Throughput",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6003", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_extrusion_v1_line_objtypes.ProductionParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=6002"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6005",
    browseName="ns=plastics_extrusion_v1_line;ProductWeight",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6006", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_extrusion_v1_line_objtypes.ProductionParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=6005"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6007",
    browseName="ns=plastics_extrusion_v1_line;LineSpeed",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6008", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_extrusion_v1_line_objtypes.ProductionParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=6007"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6009",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6010", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6011",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6012", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6013",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6014", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6015",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6016", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_v1_line;i=5017",
    browseName="ns=plastics_extrusion_v1_line;ElectricalEnergy",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6009"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6011"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6013"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_line;i=6017", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)
        ),
    ],
)
o6.reference(plastics_extrusion_v1_line_objtypes.ProductionParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=5017"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6018",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6021", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6022",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6024", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_v1_line;i=5016",
    browseName="ns=plastics_extrusion_v1_line;FluidEnergy",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6015"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6018"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6022"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_line;i=6025", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)
        ),
    ],
)
o6.reference(plastics_extrusion_v1_line_objtypes.ProductionParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=5016"])
plastics_rubber.objtypes.MachineMESConfigurationType(
    nodeId="ns=plastics_extrusion_v1_line;i=5003",
    browseName="ns=plastics_extrusion_v1_line;MachineMESConfiguration",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6046",
                browseName="ns=plastics_rubber;StandstillReasons",
                description="List of the standstill reasons from which one is selected by the operator in the case of a standstill",
                dataType=plastics_rubber.datatypes.StandstillReasonType,
                valueRank=1,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6047",
                browseName="ns=plastics_rubber;StandstillReasonsLockedByMES",
                description="Indication if the list StandstillReasons has been modified by the MES and may not be changed by the machine",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6053",
                browseName="ns=plastics_rubber;MESUrl",
                description="URL to display a webpage generated by the MES in a web browser integrated in the machine",
                dataType=o6.String,
                value="0",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(plastics_extrusion_v1_line_objtypes.ExtrusionLine_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=5003"])
plastics_rubber.objtypes.MESMessageType(
    nodeId="ns=plastics_extrusion_v1_line;i=5004",
    browseName="ns=plastics_extrusion_v1_line;MESMessage",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6054", browseName="ns=plastics_rubber;Id", description="Id of the message", dataType=o6.String, value="\n      "
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6055", browseName="ns=plastics_rubber;Message", description="Text of the message", dataType=o6.String, value="\n      "
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6056", browseName="Severity", description="Severity of the message", dataType=o6.UInt16, value=0)
        ),
    ],
)
o6.reference(plastics_extrusion_v1_line_objtypes.ExtrusionLine_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=5004"])
plastics_rubber.objtypes.UsersType(
    nodeId="ns=plastics_extrusion_v1_line;i=5005",
    browseName="ns=plastics_extrusion_v1_line;Users",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6059", browseName="NodeVersion", dataType=o6.String, value="\n      "))],
)
o6.reference(plastics_extrusion_v1_line_objtypes.ExtrusionLine_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=5005"])
o6.reference(o6.ns["ns=plastics_extrusion_v1_line;i=5005"], "i=41", "i=2133")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6019",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6061", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6020",
    browseName="ns=plastics_extrusion_v1_line;LineSpeed",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6063", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6062",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6066", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6067",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6068", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6023",
    browseName="ns=plastics_extrusion_v1_line;ProductWeight",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6069", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6071",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6072", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6004",
    browseName="ns=plastics_extrusion_v1_line;Throughput",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6075", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6064",
    browseName="ns=plastics_extrusion_v1_line;ElectricalEnergyConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6076", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_extrusion_v1_line;i=6114", browseName="ns=plastics_extrusion_v1_line;MaterialMappingType", dataType=o6.String, value="MaterialMappingType"
)
o6.reference(o6.ns["ns=plastics_extrusion_v1_line;i=5007"], "i=39", o6.ns["ns=plastics_extrusion_v1_line;i=6114"])
oPC40084_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_extrusion_v1_line;i=6027",
    browseName="ns=plastics_extrusion_v1_line;OPC40084_2",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/Extrusion/ExtrusionLine/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6028",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/ExtrusionLine/",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6114"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/ExtrusionLine/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/ExtrusionLine/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="MaterialMappingType">\n  <opc:Field TypeName="opc:CharArray" Name="MaterialId"/>\n  <opc:Field TypeName="opc:CharArray" Name="MaterialLot"/>\n  <opc:Field TypeName="opc:CharArray" Name="HopperId"/>\n </opc:StructuredType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=plastics_extrusion_v1_line;i=6115",
    browseName="ns=plastics_extrusion_v1_line;MaterialMappingType",
    dataType=o6.String,
    value="//xs:element[@name='MaterialMappingType']",
)
o6.reference(o6.ns["ns=plastics_extrusion_v1_line;i=5008"], "i=39", o6.ns["ns=plastics_extrusion_v1_line;i=6115"])
oPC40084_2_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_extrusion_v1_line;i=6029",
    browseName="ns=plastics_extrusion_v1_line;OPC40084_2",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/Extrusion/ExtrusionLine/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6030",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/ExtrusionLine/Types.xsd",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6115"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/ExtrusionLine/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/ExtrusionLine/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:complexType name="MaterialMappingType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="MaterialId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="MaterialLot"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="HopperId"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:MaterialMappingType" name="MaterialMappingType"/>\n <xs:complexType name="ListOfMaterialMappingType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:MaterialMappingType" name="MaterialMappingType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfMaterialMappingType" name="ListOfMaterialMappingType" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6131",
    browseName="ns=plastics_extrusion_v1_line;Throughput",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6132", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_extrusion_v1_line_objtypes.JobType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=6131"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6134",
    browseName="ns=plastics_extrusion_v1_line;ProductWeight",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6135", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_extrusion_v1_line_objtypes.JobType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=6134"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6137",
    browseName="ns=plastics_extrusion_v1_line;LineSpeed",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6138", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_extrusion_v1_line_objtypes.JobType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=6137"])
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_v1_line;i=5018",
    browseName="ns=plastics_extrusion_v1_line;PressureAir",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6062"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6067"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6071"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_line;i=6140", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)
        ),
    ],
)
o6.reference(plastics_extrusion_v1_line_objtypes.ProductionParametersType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=5018"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6141",
    browseName="ns=plastics_extrusion_v1_line;FluidEnergyConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6147", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6152",
    browseName="ns=plastics_extrusion_v1_line;ElectricalEnergyConsumption",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6070", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_extrusion_v1_line_objtypes.JobGroupType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=6152"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6153",
    browseName="ns=plastics_extrusion_v1_line;FluidEnergyConsumption",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6144", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_extrusion_v1_line_objtypes.JobGroupType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=6153"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6065",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6181", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6182",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6183", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_v1_line;i=5019",
    browseName="ns=plastics_extrusion_v1_line;ElectricalEnergy",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6019"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6065"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6182"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_line;i=6184", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)
        ),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6185",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6186", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6154",
    browseName="ns=plastics_extrusion_v1_line;PressureAirConsumption",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6211", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
o6.reference(plastics_extrusion_v1_line_objtypes.JobGroupType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=6154"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6210",
    browseName="ns=plastics_extrusion_v1_line;PressureAirConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6212", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6226",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6227", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6228",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6229", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6230",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6231", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_v1_line;i=5022",
    browseName="ns=plastics_extrusion_v1_line;FluidEnergy",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6185"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6226"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6228"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_line;i=6232", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)
        ),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6233",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6234", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6235",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6236", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_v1_line;i=5023",
    browseName="ns=plastics_extrusion_v1_line;PressureAir",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6230"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6233"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6235"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_line;i=6237", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)
        ),
    ],
)
plastics_extrusion_v1_line_objtypes.ProductionParametersType(
    nodeId="ns=plastics_extrusion_v1_line;i=5006",
    browseName="ns=plastics_extrusion_v1_line;ProductionParameters",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=5019"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=5022"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=5023"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6004"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6020"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6023"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_extrusion_v1_line;i=6060", browseName="ns=plastics_extrusion_v1_line;GoodProduct", dataType=o6.Boolean, value=False
            )
        ),
    ],
)
o6.reference(plastics_extrusion_v1_line_objtypes.ExtrusionLine_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=5006"])
plastics_rubber.objtypes.MachineInformationType(
    nodeId="ns=plastics_extrusion_v1_line;i=5001",
    browseName="ns=plastics_extrusion_v1_line;MachineInformation",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6032",
                browseName="ns=plastics_rubber;ControllerName",
                description="Name of the machine controller",
                dataType=o6.String,
                value="\n      ",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6033",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose a device is used.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6034",
                browseName="ns=plastics_rubber;SupportedLogbookEvents",
                description="Information which LogbookEvents are supported by the machine",
                dataType=plastics_rubber.datatypes.LogbookEventsEnumeration,
                valueRank=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6035",
                browseName="ns=di;DeviceManual",
                description="Address (pathname in the file system or a URL | Web address) of user manual for the device",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6036", browseName="ns=di;DeviceRevision", description="Overall revision level of the device", dataType=o6.String
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6037", browseName="ns=di;HardwareRevision", description="Revision level of the hardware of the device", dataType=o6.String
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6038",
                browseName="ns=di;Manufacturer",
                description="Name of the company that manufactured the device",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6039", browseName="ns=di;Model", description="Model name of the device", dataType=o6.LocalizedText)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6040",
                browseName="ns=di;RevisionCounter",
                description="An incremental counter indicating the number of times the static data within the Device has been modified",
                dataType=o6.Int32,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6041",
                browseName="ns=di;SerialNumber",
                description="Identifier that uniquely identifies, within a manufacturer, a device instance",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6238",
                browseName="ns=di;SoftwareRevision",
                description="Revision level of the software/firmware of the device",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6239", browseName="ns=di;AssetId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6240", browseName="ns=di;ComponentName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6241", browseName="ns=di;ManufacturerUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6242", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6243", browseName="ns=di;ProductInstanceUri", dataType=o6.String)),
    ],
)
o6.reference(plastics_extrusion_v1_line_objtypes.ExtrusionLine_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=5001"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6139",
    browseName="ns=plastics_extrusion_v1_line;LineSpeed",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6256", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6136",
    browseName="ns=plastics_extrusion_v1_line;ProductWeight",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6258", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1_line;i=6133",
    browseName="ns=plastics_extrusion_v1_line;Throughput",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6260", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
)
plastics_extrusion_v1_line_objtypes.JobType(
    nodeId="ns=plastics_extrusion_v1_line;i=5010",
    browseName="ns=plastics_extrusion_v1_line;Job_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6158", browseName="ns=plastics_extrusion_v1_line;CustomerName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6159", browseName="ns=plastics_extrusion_v1_line;Description", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6160", browseName="ns=plastics_extrusion_v1_line;Id", dataType=o6.String, value="\n      ")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6161", browseName="ns=plastics_extrusion_v1_line;LotSize", dataType=o6.Double)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6162",
                browseName="ns=plastics_extrusion_v1_line;ParameterSetting",
                dataType=plastics_rubber.datatypes.ParameterSettingType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6163", browseName="ns=plastics_extrusion_v1_line;ProductDescription", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6164", browseName="ns=plastics_extrusion_v1_line;ProductId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6167", browseName="ns=plastics_extrusion_v1_line;Sequence", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6168", browseName="ns=plastics_extrusion_v1_line;SetOutput", dataType=o6.Double)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6169", browseName="ns=plastics_extrusion_v1_line;Status", dataType=plastics_rubber.datatypes.JobStatusEnumeration
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6170", browseName="ns=plastics_extrusion_v1_line;Strand", dataType=o6.UInt32)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_line;i=6130", browseName="ns=plastics_extrusion_v1_line;GoodProduct", dataType=o6.Boolean)
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6133"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6136"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6139"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_line;i=6155", browseName="ns=plastics_extrusion_v1_line;ActualLot", dataType=o6.UInt32)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_line;i=6156", browseName="ns=plastics_extrusion_v1_line;ActualOutput", dataType=o6.Double)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_line;i=6157", browseName="ns=plastics_extrusion_v1_line;ActualOutputRate", dataType=o6.Double)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_extrusion_v1_line;i=6172", browseName="ns=plastics_extrusion_v1_line;ActualBadOutput", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_extrusion_v1_line;i=6178", browseName="ns=plastics_extrusion_v1_line;ActualGoodOutput", dataType=o6.Double, value=0.0
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_extrusion_v1_line;i=6179",
                browseName="ns=plastics_extrusion_v1_line;ActualLotName",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=plastics_extrusion_v1_line;i=6180", browseName="ns=plastics_extrusion_v1_line;ActualSampleOutput", dataType=o6.Double, value=0.0
            )
        ),
    ],
)
o6.reference(plastics_extrusion_v1_line_objtypes.JobGroupType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=5010"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPlasticsRubberSlashExtrusionSlashExtrusionLineSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=plastics_extrusion_v1_line;i=5024",
    browseName="ns=plastics_extrusion_v1_line;http://opcfoundation.org/UA/PlasticsRubber/Extrusion/ExtrusionLine/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6257", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6259", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2020-11-09T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6261",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/ExtrusionLine/",
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6262", browseName="NamespaceVersion", dataType=o6.String, value="1.00.01")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6263",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6264", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6265", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6271", browseName="NodeVersion", dataType=o6.String, value="\n      ")
o6.reference(o6.ns["ns=plastics_extrusion_v1_line;i=6271"], "i=41", plastics_extrusion_v1_line_objtypes.JobStatusChangedEventType)
o6.reference(o6.ns["ns=plastics_extrusion_v1_line;i=6271"], "i=41", plastics_extrusion_v1_line_objtypes.UnitFinishedEventType)
o6.reference(o6.ns["ns=plastics_extrusion_v1_line;i=6271"], "i=41", plastics_extrusion_v1_line_objtypes.LotFinishedEventType)
o6.reference(o6.ns["ns=plastics_extrusion_v1_line;i=6271"], "i=41", plastics_extrusion_v1_line_objtypes.JobGroupStatusChangedEventType)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6043",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="DateTime", dataType=o6.DateTime, valueRank=-1),
        ns0.datatypes.Argument(name="TimeZoneOffset", dataType=ns0.datatypes.TimeZoneDataType, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7001",
    browseName="ns=plastics_rubber;SetMachineTime",
    description="Method for setting the server time together with TimeZoneOffset",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6043"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6048",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="VisualisationUnit", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6049",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Page", dataType=ns0.datatypes.Image, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7002",
    browseName="ns=plastics_rubber;GetCurrentPage",
    description="Method for retrieving a screenshot of the control system with the currently shown contents",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6048"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6049"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6050",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6051",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Page", dataType=ns0.datatypes.Image, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7003",
    browseName="ns=plastics_rubber;GetPage",
    description="Method for retrieving the image of a page of the control system",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6050"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6051"]),
)

plastics_rubber.objtypes.MachineConfigurationType(
    nodeId="ns=plastics_extrusion_v1_line;i=5002",
    browseName="ns=plastics_extrusion_v1_line;MachineConfiguration",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6042",
                browseName="ns=plastics_rubber;LocationName",
                description="Description of the location of the machine given by the machine operator or OPC client",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6044",
                browseName="ns=plastics_rubber;TimeZoneOffset",
                description="Difference of the local time to Coordinated Universal Time (UTC) given by the machine operator or OPC client",
                dataType=ns0.datatypes.TimeZoneDataType,
                value=ns0.datatypes.TimeZoneDataType(offset=0, daylightSavingInOffset=False),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6045",
                browseName="ns=plastics_rubber;UserMachineName",
                description="Description of the machine given by the machine operator or OPC client",
                dataType=o6.String,
                value="\n      ",
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6052",
                browseName="ns=plastics_rubber;PageDirectory",
                description="List of the pages that are implemented in the machine control system and are shown on the screen of the machine",
                dataType=plastics_rubber.datatypes.PageEntryDataType,
                valueRank=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7001"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7002"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7003"]),
    ],
)
o6.reference(plastics_extrusion_v1_line_objtypes.ExtrusionLine_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=5002"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6191",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[10],
    value=[
        ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Description", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="CustomerName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ProductName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ProductDescription", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Strand", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="Sequence", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ParameterSetting", dataType=o6.NodeId("ns=plastics_rubber;i=3026"), valueRank=1),
        ns0.datatypes.Argument(name="SetOutput", dataType=o6.Double, valueRank=-1),
        ns0.datatypes.Argument(name="LotSize", dataType=o6.Double, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6192",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="JobNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7011",
    browseName="ns=plastics_extrusion_v1_line;AddJob",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6191"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6192"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6117",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6118",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7012",
    browseName="CloseAndCommit",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6117"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6118"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6119",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=plastics_rubber;i=3007"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6120",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7013",
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
    nodeId="ns=plastics_extrusion_v1_line;i=7013",
    browseName="GenerateFileForRead",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6119"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6120"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6121",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=plastics_rubber;i=3004"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6122",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7014",
    browseName="GenerateFileForWrite",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6121"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6122"]),
)

ns0.objtypes.TemporaryFileTransferType(
    nodeId="ns=plastics_extrusion_v1_line;i=5013",
    browseName="ns=plastics_rubber;ProductionDatasetTransfer",
    description="Transfer of production datasets between server and client",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6074", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7012"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7013"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7014"]),
    ],
    eventNotifier=1,
)
o6.reference(o6.ns["ns=plastics_extrusion_v1_line;i=5013"], "i=41", "ns=plastics_rubber;i=1006")
o6.reference(o6.ns["ns=plastics_extrusion_v1_line;i=5013"], "i=41", "ns=plastics_rubber;i=1007")
o6.reference(o6.ns["ns=plastics_extrusion_v1_line;i=5013"], "i=41", "ns=plastics_rubber;i=1040")


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6123",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="fileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6124",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Information", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7015",
    browseName="ns=plastics_rubber;GetProductionDatasetInformation",
    description="This Method allows reading the description of a production dataset during the file transfer from the server to the client with ProductionDatasetTransfer",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6123"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6124"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6126",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="NameFilter", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="MouldId", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6127",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductionDatasetList", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7016",
    browseName="ns=plastics_rubber;GetProductionDatasetList",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6126"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6127"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6128",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductionDatasetList", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7017",
    browseName="ns=plastics_rubber;SendProductionDatasetList",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6128"]),
)

plastics_rubber.objtypes.ProductionDatasetListsType(
    nodeId="ns=plastics_extrusion_v1_line;i=5015",
    browseName="ns=plastics_rubber;ProductionDatasetLists",
    description="Functions for exchanging information on the available production datasets on client and server",
    references=[o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7016"]), o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7017"])],
    eventNotifier=1,
)
o6.reference(o6.ns["ns=plastics_extrusion_v1_line;i=5015"], "i=41", "ns=plastics_rubber;i=1040")


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6129",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="fileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="Information", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7018",
    browseName="ns=plastics_rubber;SendProductionDatasetInformation",
    description="This Method allows sending of the description of a production dataset during the file transfer from the client to the server with ProductionDatasetTransfer",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6129"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6219",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="Components", dataType=o6.UInt16, valueRank=1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7019",
    browseName="ns=plastics_rubber;Load",
    description="Loads a production dataset from the file system of the machine to the control of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6219"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6221",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7020",
    browseName="ns=plastics_rubber;Save",
    description="Stores a production dataset from the control of the machine to the file system of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6221"]),
)

plastics_rubber.objtypes.ProductionDatasetStatusType(
    nodeId="ns=plastics_extrusion_v1_line;i=5012",
    browseName="ns=plastics_rubber;ActiveProductionDatasetStatus",
    description="Status of the active production dataset",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6073",
                browseName="ns=plastics_rubber;Information",
                description="Set of information on the production dataset",
                dataType=plastics_rubber.datatypes.ProductionDatasetInformationType,
                value=plastics_rubber.datatypes.ProductionDatasetInformationType(
                    name="",
                    description="",
                    mESId="",
                    creationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastModificationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastSaveTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    userName="",
                    components=[],
                    manufacturer="",
                    serialNumber="",
                    model="",
                    controllerName="",
                    userMachineName="",
                    locationName="",
                    productName=[],
                    mouldId="",
                    numCavities=0,
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6143",
                browseName="ns=plastics_rubber;Frozen",
                description="Indication if changes on the machine in the production dataset are allowed",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6220",
                browseName="ns=plastics_rubber;Modified",
                description="Indication if the production dataset has been changed after the last storage",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7019"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7020"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6166",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Name", dataType=o6.LocalizedText, valueRank=-1),
        ns0.datatypes.Argument(name="Density", dataType=o6.Double, valueRank=-1),
    ],
)
o6.call(nodeId="ns=plastics_extrusion_v1_line;i=7021", browseName="ns=plastics_rubber;AddMaterial", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6166"]))

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6279",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=plastics_extrusion_v1_line;i=7022", browseName="ns=plastics_rubber;RemoveMaterialById", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6279"]))

plastics_rubber.objtypes.MaterialListType(
    nodeId="ns=plastics_extrusion_v1_line;i=5020",
    browseName="ns=plastics_extrusion_v1_line;MaterialList",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6145", browseName="ns=plastics_rubber;DensityUnit", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6146", browseName="NodeVersion", dataType=o6.String, value="\n      ")),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7021"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7022"]),
    ],
)
o6.reference(plastics_extrusion_v1_line_objtypes.ExtrusionLine_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=5020"])
o6.reference(o6.ns["ns=plastics_extrusion_v1_line;i=5020"], "i=41", plastics_extrusion_v1_line_objtypes.RequestAddMaterialEventType)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6196",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7023", browseName="ns=plastics_extrusion_v1_line;FinishJobById", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6196"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6198",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7024",
    browseName="ns=plastics_extrusion_v1_line;InterruptJobById",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6198"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6207",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7025", browseName="ns=plastics_extrusion_v1_line;RemoveJobById", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6207"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6208",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7026", browseName="ns=plastics_extrusion_v1_line;StartJobById", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6208"])
)

plastics_extrusion_v1_line_objtypes.JobGroupType(
    nodeId="ns=plastics_extrusion_v1_line;i=5021",
    browseName="ns=plastics_extrusion_v1_line;JobGroup_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6193",
                browseName="ns=plastics_extrusion_v1_line;ConfigurationParameters",
                dataType=plastics_rubber.datatypes.ConfigurationParameterType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6194", browseName="ns=plastics_extrusion_v1_line;Description", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6195", browseName="ns=plastics_extrusion_v1_line;EquipmentDescription", dataType=o6.String)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6197", browseName="ns=plastics_extrusion_v1_line;Id", dataType=o6.String, value="\n      ")
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6199", browseName="ns=plastics_extrusion_v1_line;LatestEnd", dataType=ns0.datatypes.UtcTime)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6200", browseName="ns=plastics_extrusion_v1_line;PlannedProductionTime", dataType=ns0.datatypes.Duration
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6201", browseName="ns=plastics_extrusion_v1_line;PlannedSetUpTime", dataType=ns0.datatypes.Duration)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6202", browseName="ns=plastics_extrusion_v1_line;PlannedStart", dataType=ns0.datatypes.UtcTime)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6203", browseName="ns=plastics_extrusion_v1_line;Priority", dataType=o6.UInt32)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6204",
                browseName="ns=plastics_extrusion_v1_line;MaterialMapping",
                dataType=plastics_extrusion_v1_line_datypes.MaterialMappingType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6205", browseName="NodeVersion", dataType=o6.String, value="\n      ")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6206", browseName="ns=plastics_extrusion_v1_line;ProductionDatasetName", dataType=o6.String)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6209", browseName="ns=plastics_extrusion_v1_line;Status", dataType=plastics_rubber.datatypes.JobStatusEnumeration
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6064"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6141"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=6210"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7011"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7023"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7024"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7025"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7026"]),
    ],
)
o6.reference(plastics_extrusion_v1_line_objtypes.JobGroupsType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=5021"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6223",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7032",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="Components", dataType=o6.UInt16, valueRank=1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7032",
    browseName="ns=plastics_rubber;Load",
    description="Loads a production dataset from the file system of the machine to the control of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6223"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6225",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7033",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7033",
    browseName="ns=plastics_rubber;Save",
    description="Stores a production dataset from the control of the machine to the file system of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6225"]),
)

plastics_rubber.objtypes.ProductionDatasetStatusType(
    nodeId="ns=plastics_extrusion_v1_line;i=5014",
    browseName="ns=plastics_rubber;ProductionDatasetInPreparationStatus",
    description="Status of the production dataset in the preparation layer",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6125",
                browseName="ns=plastics_rubber;Information",
                description="Set of information on the production dataset",
                dataType=plastics_rubber.datatypes.ProductionDatasetInformationType,
                value=plastics_rubber.datatypes.ProductionDatasetInformationType(
                    name="",
                    description="",
                    mESId="",
                    creationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastModificationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    lastSaveTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                    userName="",
                    components=[],
                    manufacturer="",
                    serialNumber="",
                    model="",
                    controllerName="",
                    userMachineName="",
                    locationName="",
                    productName=[],
                    mouldId="",
                    numCavities=0,
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6222",
                browseName="ns=plastics_rubber;Frozen",
                description="Indication if changes on the machine in the production dataset are allowed",
                dataType=o6.Boolean,
                value=False,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1_line;i=6224",
                browseName="ns=plastics_rubber;Modified",
                description="Indication if the production dataset has been changed after the last storage",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7032"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7033"]),
    ],
)
plastics_rubber.objtypes.ProductionDatasetManagementType(
    nodeId="ns=plastics_extrusion_v1_line;i=5011",
    browseName="ns=plastics_extrusion_v1_line;ProductionDatasetManagement",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=5012"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=5013"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=5014"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=5015"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7015"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7018"]),
    ],
)
o6.reference(plastics_extrusion_v1_line_objtypes.ExtrusionLine_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=5011"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6269",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7034",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[10],
    value=[
        ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Description", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="EquipmentDescription", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ProductionDatasetName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="MaterialMapping", dataType=o6.NodeId("ns=plastics_extrusion_v1_line;i=3003"), valueRank=1),
        ns0.datatypes.Argument(name="Priority", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="PlannedStart", dataType=ns0.datatypes.UtcTime, valueRank=-1),
        ns0.datatypes.Argument(name="PlannedProductionTime", dataType=ns0.datatypes.Duration, valueRank=-1),
        ns0.datatypes.Argument(name="PlannedSetUpTime", dataType=ns0.datatypes.Duration, valueRank=-1),
        ns0.datatypes.Argument(name="LatestEnd", dataType=ns0.datatypes.UtcTime, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6270",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7034",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="JobGroupNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7034",
    browseName="ns=plastics_extrusion_v1_line;AddJobGroup",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6269"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6270"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6272",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7035",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7035",
    browseName="ns=plastics_extrusion_v1_line;RemoveJobGroupById",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6272"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6273",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7036",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7036",
    browseName="ns=plastics_extrusion_v1_line;FinishJobGroupById",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6273"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6274",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7037",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7037",
    browseName="ns=plastics_extrusion_v1_line;InterruptJobGroupById",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6274"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6275",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7038",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7038",
    browseName="ns=plastics_extrusion_v1_line;StartJobGroupById",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6275"]),
)

plastics_extrusion_v1_line_objtypes.JobGroupsType(
    nodeId="ns=plastics_extrusion_v1_line;i=5025",
    browseName="ns=plastics_extrusion_v1_line;JobGroups",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6271"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7034"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7035"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7036"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7037"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7038"]),
    ],
)
o6.reference(plastics_extrusion_v1_line_objtypes.ExtrusionLine_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1_line;i=5025"])


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_rubber, plastics_extrusion_v1_line_datypes, plastics_extrusion_v1_line_objtypes
