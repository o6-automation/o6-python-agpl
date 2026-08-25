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

"""Generated OPC UA plastics_extrusion_v1 namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_extrusion_v1_datypes
from . import objtypes as plastics_extrusion_v1_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6007",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=3001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[29],
    value=[
        o6.LocalizedText("OTHER"),
        o6.LocalizedText("LINE_CONTROL"),
        o6.LocalizedText("MATERIAL_HANDLING"),
        o6.LocalizedText("PRE_HEATING"),
        o6.LocalizedText("FEEDING"),
        o6.LocalizedText("DOSING"),
        o6.LocalizedText("EXTRUDER"),
        o6.LocalizedText("VACUUM_STATION"),
        o6.LocalizedText("FILTER"),
        o6.LocalizedText("MELT_PUMP"),
        o6.LocalizedText("DIE"),
        o6.LocalizedText("COOLING"),
        o6.LocalizedText("HAUL_OFF"),
        o6.LocalizedText("CORRUGATOR"),
        o6.LocalizedText("SAW"),
        o6.LocalizedText("CALIBRATION"),
        o6.LocalizedText("ROLL_STACK"),
        o6.LocalizedText("MDO"),
        o6.LocalizedText("BIAX"),
        o6.LocalizedText("CUTTING"),
        o6.LocalizedText("WINDER"),
        o6.LocalizedText("PELLETIZING"),
        o6.LocalizedText("DRYER"),
        o6.LocalizedText("HANDLING_SYSTEM"),
        o6.LocalizedText("LAMINATION_SYSTEM"),
        o6.LocalizedText("MEASURING_SYSTEM"),
        o6.LocalizedText("QUALITY_SYSTEM"),
        o6.LocalizedText("MANUAL_INSPECTION"),
        o6.LocalizedText("MANUAL_OPERATION"),
    ],
)
oPC40084_1 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_extrusion_v1;i=6008",
    browseName="ns=plastics_extrusion_v1;OPC40084_1",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/Extrusion/GeneralTypes/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6009", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/GeneralTypes/"
            )
        )
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/GeneralTypes/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/GeneralTypes/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:EnumeratedType LengthInBits="32" Name="ComponentStatusEnumeration">\n  <opc:EnumeratedValue Name="OFFLINE" Value="0"/>\n  <opc:EnumeratedValue Name="IDLE" Value="1"/>\n  <opc:EnumeratedValue Name="PREPARING" Value="2"/>\n  <opc:EnumeratedValue Name="READY_TO_RUN" Value="3"/>\n  <opc:EnumeratedValue Name="MANUAL_RUN" Value="4"/>\n  <opc:EnumeratedValue Name="CONTROLLED_RUN" Value="5"/>\n  <opc:EnumeratedValue Name="MALFUNCTION" Value="6"/>\n  <opc:EnumeratedValue Name="MAINTENANCE" Value="7"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ExtrusionMessageClassificationEnumeration">\n  <opc:EnumeratedValue Name="OTHER" Value="0"/>\n  <opc:EnumeratedValue Name="LINE_CONTROL" Value="1"/>\n  <opc:EnumeratedValue Name="MATERIAL_HANDLING" Value="2"/>\n  <opc:EnumeratedValue Name="PRE_HEATING" Value="3"/>\n  <opc:EnumeratedValue Name="FEEDING" Value="4"/>\n  <opc:EnumeratedValue Name="DOSING" Value="5"/>\n  <opc:EnumeratedValue Name="EXTRUDER" Value="6"/>\n  <opc:EnumeratedValue Name="VACUUM_STATION" Value="7"/>\n  <opc:EnumeratedValue Name="FILTER" Value="8"/>\n  <opc:EnumeratedValue Name="MELT_PUMP" Value="9"/>\n  <opc:EnumeratedValue Name="DIE" Value="10"/>\n  <opc:EnumeratedValue Name="COOLING" Value="11"/>\n  <opc:EnumeratedValue Name="HAUL_OFF" Value="12"/>\n  <opc:EnumeratedValue Name="CORRUGATOR" Value="13"/>\n  <opc:EnumeratedValue Name="SAW" Value="14"/>\n  <opc:EnumeratedValue Name="CALIBRATION" Value="15"/>\n  <opc:EnumeratedValue Name="ROLL_STACK" Value="16"/>\n  <opc:EnumeratedValue Name="MDO" Value="17"/>\n  <opc:EnumeratedValue Name="BIAX" Value="18"/>\n  <opc:EnumeratedValue Name="CUTTING" Value="19"/>\n  <opc:EnumeratedValue Name="WINDER" Value="20"/>\n  <opc:EnumeratedValue Name="PELLETIZING" Value="21"/>\n  <opc:EnumeratedValue Name="DRYER" Value="22"/>\n  <opc:EnumeratedValue Name="HANDLING_SYSTEM" Value="23"/>\n  <opc:EnumeratedValue Name="LAMINATION_SYSTEM" Value="24"/>\n  <opc:EnumeratedValue Name="MEASURING_SYSTEM" Value="25"/>\n  <opc:EnumeratedValue Name="QUALITY_SYSTEM" Value="26"/>\n  <opc:EnumeratedValue Name="MANUAL_INSPECTION" Value="27"/>\n  <opc:EnumeratedValue Name="MANUAL_OPERATION" Value="28"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
oPC40084_1_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=plastics_extrusion_v1;i=6010",
    browseName="ns=plastics_extrusion_v1;OPC40084_1",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PlasticsRubber/Extrusion/GeneralTypes/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6011",
                browseName="NamespaceUri",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/GeneralTypes/Types.xsd",
            )
        )
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/GeneralTypes/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/GeneralTypes/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="ComponentStatusEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OFFLINE_0"/>\n   <xs:enumeration value="IDLE_1"/>\n   <xs:enumeration value="PREPARING_2"/>\n   <xs:enumeration value="READY_TO_RUN_3"/>\n   <xs:enumeration value="MANUAL_RUN_4"/>\n   <xs:enumeration value="CONTROLLED_RUN_5"/>\n   <xs:enumeration value="MALFUNCTION_6"/>\n   <xs:enumeration value="MAINTENANCE_7"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ComponentStatusEnumeration" name="ComponentStatusEnumeration"/>\n <xs:complexType name="ListOfComponentStatusEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ComponentStatusEnumeration" name="ComponentStatusEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfComponentStatusEnumeration" name="ListOfComponentStatusEnumeration" nillable="true"/>\n <xs:simpleType name="ExtrusionMessageClassificationEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OTHER_0"/>\n   <xs:enumeration value="LINE_CONTROL_1"/>\n   <xs:enumeration value="MATERIAL_HANDLING_2"/>\n   <xs:enumeration value="PRE_HEATING_3"/>\n   <xs:enumeration value="FEEDING_4"/>\n   <xs:enumeration value="DOSING_5"/>\n   <xs:enumeration value="EXTRUDER_6"/>\n   <xs:enumeration value="VACUUM_STATION_7"/>\n   <xs:enumeration value="FILTER_8"/>\n   <xs:enumeration value="MELT_PUMP_9"/>\n   <xs:enumeration value="DIE_10"/>\n   <xs:enumeration value="COOLING_11"/>\n   <xs:enumeration value="HAUL_OFF_12"/>\n   <xs:enumeration value="CORRUGATOR_13"/>\n   <xs:enumeration value="SAW_14"/>\n   <xs:enumeration value="CALIBRATION_15"/>\n   <xs:enumeration value="ROLL_STACK_16"/>\n   <xs:enumeration value="MDO_17"/>\n   <xs:enumeration value="BIAX_18"/>\n   <xs:enumeration value="CUTTING_19"/>\n   <xs:enumeration value="WINDER_20"/>\n   <xs:enumeration value="PELLETIZING_21"/>\n   <xs:enumeration value="DRYER_22"/>\n   <xs:enumeration value="HANDLING_SYSTEM_23"/>\n   <xs:enumeration value="LAMINATION_SYSTEM_24"/>\n   <xs:enumeration value="MEASURING_SYSTEM_25"/>\n   <xs:enumeration value="QUALITY_SYSTEM_26"/>\n   <xs:enumeration value="MANUAL_INSPECTION_27"/>\n   <xs:enumeration value="MANUAL_OPERATION_28"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ExtrusionMessageClassificationEnumeration" name="ExtrusionMessageClassificationEnumeration"/>\n <xs:complexType name="ListOfExtrusionMessageClassificationEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ExtrusionMessageClassificationEnumeration" name="ExtrusionMessageClassificationEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfExtrusionMessageClassificationEnumeration" name="ListOfExtrusionMessageClassificationEnumeration" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6012",
    browseName="ns=plastics_extrusion_v1;ControllerOutput",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6013", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_extrusion_v1_objtypes.ExtrusionTemperatureZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=6012"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6003",
    browseName="ns=plastics_rubber;Interval",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6004", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6014", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6005",
    browseName="ns=plastics_rubber;RemainingInterval",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6006", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6015", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6017",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        o6.LocalizedText("OFFLINE"),
        o6.LocalizedText("IDLE"),
        o6.LocalizedText("PREPARING"),
        o6.LocalizedText("READY_TO_RUN"),
        o6.LocalizedText("MANUAL_RUN"),
        o6.LocalizedText("CONTROLLED_RUN"),
        o6.LocalizedText("MALFUNCTION"),
        o6.LocalizedText("MAINTENANCE"),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6018",
    browseName="ns=plastics_extrusion_v1;NominalCoolingPower",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6019", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_extrusion_v1_objtypes.ExtrusionTemperatureZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=6018"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6039",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6040", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6041",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6042", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6043",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6044", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6045",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6046", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6048",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6049", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_v1;i=5010",
    browseName="ns=plastics_extrusion_v1;ElectricalEnergy",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6039"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6045"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6048"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1;i=6050", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.ExtrusionDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5010"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6047",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6051", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6052",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6053", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6054",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6055", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_v1;i=5011",
    browseName="ns=plastics_extrusion_v1;FluidEnergy",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6041"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6047"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6054"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1;i=6056", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.ExtrusionDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5011"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6057",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6058", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_v1;i=5012",
    browseName="ns=plastics_extrusion_v1;PressureAir",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6043"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6052"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6057"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1;i=6062", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.ExtrusionDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5012"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPlasticsRubberSlashExtrusionSlashGeneralTypesSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=plastics_extrusion_v1;i=5025",
    browseName="ns=plastics_extrusion_v1;http://opcfoundation.org/UA/PlasticsRubber/Extrusion/GeneralTypes/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6059", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6060", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2021-04-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6061", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion/GeneralTypes/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6090", browseName="NamespaceVersion", dataType=o6.String, value="1.01")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6091",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6092", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6093", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6065",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6066", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6101", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6067",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6068", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6102", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6069",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6070", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6103", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6100",
    browseName="ns=plastics_extrusion_v1;NominalHeatingPower",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6105", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(plastics_extrusion_v1_objtypes.ExtrusionTemperatureZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=6100"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6112",
    browseName="ns=plastics_rubber;TotalOperation",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6113", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6114", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6117",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6118", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6119", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6121",
    browseName="ns=plastics_extrusion_v1;ControllerOutput",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6122", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_v1;i=5023",
    browseName="ns=plastics_extrusion_v1;AdditionalMeasuringDevices",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6129", browseName="NodeVersion", dataType=o6.String, value="\n      "))],
)
o6.reference(plastics_extrusion_v1_objtypes.ExtrusionDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5023"])
o6.reference(o6.ns["ns=plastics_extrusion_v1;i=5023"], "i=41", "i=2133")
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6136",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6137", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6138", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6140",
    browseName="ns=plastics_extrusion_v1;NominalCoolingPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6141", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6142",
    browseName="ns=plastics_extrusion_v1;NominalHeatingPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6143", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6115",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6116", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6156", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6160",
    browseName="ns=plastics_rubber;AlarmSuppression",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6161", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6162", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6164",
    browseName="ns=plastics_rubber;LowerTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6165", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6166", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6168",
    browseName="ns=plastics_rubber;LowerTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6169", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6170", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6171",
    browseName="ns=plastics_rubber;MaxValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6172", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6173", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6176",
    browseName="ns=plastics_rubber;MinValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6177", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6178", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6179",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6180", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6181", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6182",
    browseName="ns=plastics_rubber;SetRampDown",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6183", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6184", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6185",
    browseName="ns=plastics_rubber;SetRampUp",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6186", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6187", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6188",
    browseName="ns=plastics_rubber;SetValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6189", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6190", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6191",
    browseName="ns=plastics_rubber;UpperTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6192", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6193", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6194",
    browseName="ns=plastics_rubber;UpperTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6195", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6196", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6125",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6126", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6197", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6127",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6130", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6198", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6132",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6133", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6199", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6134",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6135", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6200", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6145",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6146", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6201", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MachineInformationType(
    nodeId="ns=plastics_extrusion_v1;i=5008",
    browseName="ns=plastics_extrusion_v1;MachineInformation",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6021",
                browseName="ns=plastics_rubber;ControllerName",
                description="Name of the machine controller",
                dataType=o6.String,
                value="\n      ",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6022",
                browseName="ns=di;DeviceClass",
                description="Indicates in which domain or for what purpose a device is used.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6023", browseName="ns=di;Manufacturer", description="Name of the company that manufactured the device", dataType=o6.LocalizedText
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6024", browseName="ns=di;Model", description="Model name of the device", dataType=o6.LocalizedText)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6025",
                browseName="ns=di;SerialNumber",
                description="Identifier that uniquely identifies, within a manufacturer, a device instance",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6026",
                browseName="ns=plastics_rubber;SupportedLogbookEvents",
                description="Information which LogbookEvents are supported by the machine",
                dataType=plastics_rubber.datatypes.LogbookEventsEnumeration,
                valueRank=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6027", browseName="ns=di;AssetId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6028", browseName="ns=di;ComponentName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6029", browseName="ns=di;DeviceManual", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6030", browseName="ns=di;DeviceRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6099", browseName="ns=di;HardwareRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6175", browseName="ns=di;ManufacturerUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6202", browseName="ns=di;ProductCode", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6203", browseName="ns=di;ProductInstanceUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6204", browseName="ns=di;RevisionCounter", dataType=o6.Int32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6205", browseName="ns=di;SoftwareRevision", dataType=o6.String)),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.ExtrusionDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5008"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6147",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6148", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6206", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6149",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6150", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6207", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6152",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6153", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6208", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6154",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6155", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6209", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6123",
    browseName="ns=plastics_rubber;ActualValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6124", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6210", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=5,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6212",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6213", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6214", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6215",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6216", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6217", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6218",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6219", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6220", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6222",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6223", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6224", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6225",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6226", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6227", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6229",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6230", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6231", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6232",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6233", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6234", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6235",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6236", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6237", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6238",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6239", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6240", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6241",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6251", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6252", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6253",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6254", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6255", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6256",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6257", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6258", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6259",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6260", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6261", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6262",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6263", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6264", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6265",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6266", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6267", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6268",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6269", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6270", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6271",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6272", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6273", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6275",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6276", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6277", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6278",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6279", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6280", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6281",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6282", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6283", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6284",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6285", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6286", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6287",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6288", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6289", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6290",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6291", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6292", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6293",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6294", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6295", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6296",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6297", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6298", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6299",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6300", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6301", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6302",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6303", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6304", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6307",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6308", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6309", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6310",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6311", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6312", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6314",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6315", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6316", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6317",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6318", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6319", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6320",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6321", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6322", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6323",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6324", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6325", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6326",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6327", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6328", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6329",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6330", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6331", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6332",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6333", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6334", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6335",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6336", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6337", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6338",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6339", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6340", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6341",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6342", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6343", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6352",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6353", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6356", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6361",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6362", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6363", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6365",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6366", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6367", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6368",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6369", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6370", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6371",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6372", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6373", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6374",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6375", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6376", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6377",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6378", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6379", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6380",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6381", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6382", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6383",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6384", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6385", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6386",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6387", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6388", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6389",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6390", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6391", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6392",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6393", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6394", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6354",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6355", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6395", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6396",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6397", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6398", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6400",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6401", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6402", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6403",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6404", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6405", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6406",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6407", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6408", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6409",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6410", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6411", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6412",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6413", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6414", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6415",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6416", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6417", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6418",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6419", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6420", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6421",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6422", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6423", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6424",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6425", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6426", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6427",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6428", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6429", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6357",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6358", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6432", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6433",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6434", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6435", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6437",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6438", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6439", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6440",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6441", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6442", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6443",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6444", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6445", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6446",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6447", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6448", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6449",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6450", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6451", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6452",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6453", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6454", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6455",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6456", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6457", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6458",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6459", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6460", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6461",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6462", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6463", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6464",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6465", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6466", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6468", browseName="NodeVersion", dataType=o6.String)
o6.reference(o6.ns["ns=plastics_extrusion_v1;i=6468"], "i=41", "i=2133")
plastics_extrusion_v1_objtypes.RollPeripheralDevicesType(
    nodeId="ns=plastics_extrusion_v1;i=5030",
    browseName="ns=plastics_extrusion_v1;PeripheralDevices",
    modellingRule="Optional",
    references=[o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6468"])],
)
o6.reference(plastics_extrusion_v1_objtypes.RollType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5030"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6470",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6471", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6472", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6473",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6474", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6475", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6477",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6478", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6479", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6480",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6481", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6482", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6483",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6484", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6485", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6486",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6487", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6488", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6489",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6490", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6491", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6492",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6493", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6494", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6495",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6496", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6497", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6498",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6499", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6500", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6501",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6502", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6503", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6504",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6505", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6506", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6507",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6508", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6509", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6510",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6511", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6512", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6514",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6515", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6516", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6517",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6518", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6519", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6520",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6521", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6522", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6523",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6524", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6525", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6526",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6527", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6528", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6529",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6530", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6531", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6532",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6533", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6534", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6535",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6536", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6537", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6538",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6539", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6540", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6541",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6542", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6543", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_v1;i=5034",
    browseName="ns=plastics_rubber;AdditionalMeasuringDevices",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6544", browseName="NodeVersion", dataType=o6.String, value="\n      "))],
)
o6.reference(o6.ns["ns=plastics_extrusion_v1;i=5034"], "i=41", "i=2133")
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_v1;i=5057",
    browseName="ns=plastics_rubber;AdditionalMeasuringDevices",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6551", browseName="NodeVersion", dataType=o6.String, value="\n      "))],
)
o6.reference(o6.ns["ns=plastics_extrusion_v1;i=5057"], "i=41", "i=2133")
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6469",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6558", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6559",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6560", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_extrusion_v1_objtypes.RollBendingType(
    nodeId="ns=plastics_extrusion_v1;i=5041",
    browseName="ns=plastics_extrusion_v1;RollBending",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6562", browseName="NodeVersion", dataType=o6.String))],
)
o6.reference(plastics_extrusion_v1_objtypes.RollType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5041"])
plastics_extrusion_v1_objtypes.RollBendingType(
    nodeId="ns=plastics_extrusion_v1;i=5042",
    browseName="ns=plastics_extrusion_v1;RollBending",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6563", browseName="NodeVersion", dataType=o6.String))],
)
o6.reference(o6.ns["ns=plastics_extrusion_v1;i=5042"], "i=41", "i=2133")
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6567",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6568", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6569",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6570", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6571", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6573",
    browseName="ns=plastics_extrusion_v1;ControllerOutput",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6574", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6575",
    browseName="ns=plastics_rubber;ActualValue",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6576", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=5,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1;i=5045", browseName="ns=plastics_extrusion_v1;ElectricalCurrent", references=[o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6575"])]
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6577",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6578", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6579",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6580", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6582",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6583", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6584",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6585", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6586",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6587", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6588", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6590",
    browseName="ns=plastics_extrusion_v1;NominalCoolingPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6591", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6592",
    browseName="ns=plastics_extrusion_v1;NominalHeatingPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6593", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6595",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6596", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6597",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6598", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6599",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6600", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_v1;i=5049",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6601",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        )
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6602",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6603", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6604",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6605", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6606",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6607", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6608",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6609", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6610", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6612",
    browseName="ns=plastics_extrusion_v1;ControllerOutput",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6613", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6615",
    browseName="ns=plastics_rubber;ActualValue",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6616", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=5,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1;i=5051", browseName="ns=plastics_extrusion_v1;ElectricalCurrent", references=[o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6615"])]
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6619",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6620", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6621",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6622", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6624",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6625", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6626",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6627", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6628",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6629", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6630", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6632",
    browseName="ns=plastics_extrusion_v1;NominalCoolingPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6633", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6634",
    browseName="ns=plastics_extrusion_v1;NominalHeatingPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6635", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6637",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6639", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6640",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6643", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6644",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6645", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_v1;i=5063",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6646",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        )
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6647",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6648", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6649",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6650", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6717",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6718", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6719", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6720",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6721", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6722", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6733",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6734", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6735", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6724",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6725", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6752", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6726",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6727", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6753", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6729",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6730", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6761", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6731",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6732", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6762", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6738",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6739", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6763", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6740",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6741", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6764", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6742",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6743", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6765", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6745",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6746", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6767", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6747",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6748", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6768", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6755",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6756", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6769", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6757",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6758", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6770", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6759",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6760", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6771", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6561",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6777", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_v1;i=5035",
    browseName="ns=plastics_rubber;Energy",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6469"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6559"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6561"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1;i=6778", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6786",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6787", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6788", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6798",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6799", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6800", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6808",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6809", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6810", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6812",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6813", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6814", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6815",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6816", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6817", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6818",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6819", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6820", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6821",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6822", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6823", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6824",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6825", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6826", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6827",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6828", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6829", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6830",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6831", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6832", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6833",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6834", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6835", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6836",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6837", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6838", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6839",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6840", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6841", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6844",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6845", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6846", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6848",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6849", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6850", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6851",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6852", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6853", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6854",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6855", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6856", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6857",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6858", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6859", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6860",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6861", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6862", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6863",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6864", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6865", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6866",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6867", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6868", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6869",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6870", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6871", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6874",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6875", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6876", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6872",
    browseName="ns=plastics_rubber;ActualValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6873", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6877", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=5,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6878",
    browseName="ns=plastics_rubber;AlarmSuppression",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6879", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6880", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6882",
    browseName="ns=plastics_rubber;LowerTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6242", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6883", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6884",
    browseName="ns=plastics_rubber;LowerTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6243", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6885", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6886",
    browseName="ns=plastics_rubber;MaxValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6244", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6887", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6888",
    browseName="ns=plastics_rubber;MinValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6245", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6889", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6890",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6891", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6892", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6893",
    browseName="ns=plastics_rubber;SetRampDown",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6246", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6894", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6895",
    browseName="ns=plastics_rubber;SetRampUp",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6247", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6896", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6897",
    browseName="ns=plastics_rubber;SetValue",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6248", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6898", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6899",
    browseName="ns=plastics_rubber;UpperTolerance",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6249", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6900", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6901",
    browseName="ns=plastics_rubber;UpperTolerance2",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6250", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6902", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6806",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6807", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6903", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6842",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6843", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6904", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6905",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6906", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6907", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6915",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6916", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6917", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6927",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6928", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6929", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6780",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6781", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6940", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6782",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6783", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6941", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6784",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6785", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6942", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6546",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6547", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6943", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6790",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6791", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6944", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6792",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6793", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6945", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6794",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6795", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6946", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6796",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6797", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6947", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6801",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6802", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6948", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6804",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6805", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6949", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6908",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6909", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6950", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6910",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6911", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6951", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6912",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6913", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6952", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6549",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6550", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6953", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6919",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6920", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6954", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6921",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6922", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6955", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6923",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6924", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6956", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6925",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6926", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6957", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6930",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6931", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6958", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6932",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6933", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6959", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6934",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6935", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6960", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6936",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6937", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6961", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6938",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6939", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6962", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6963",
    browseName="ns=plastics_rubber;ActualPower",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6964", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6965",
    browseName="ns=plastics_rubber;ActualSpecificEnergy",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6966", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=plastics_extrusion_v1;i=6967",
    browseName="ns=plastics_rubber;PowerConsumption",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6968", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.EnergyType(
    nodeId="ns=plastics_extrusion_v1;i=5058",
    browseName="ns=plastics_rubber;Energy",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6963"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6965"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6967"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1;i=6969", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6971",
    browseName="ns=plastics_rubber;Interval",
    description="Regular interval between two maintenances",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6972", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6973", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6974",
    browseName="ns=plastics_rubber;RemainingInterval",
    description="Interval before next maintenance is due",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6975", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6976", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6977",
    browseName="ns=plastics_rubber;TotalOperation",
    description="How long is the component running in total",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6978", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6979", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6553",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6554", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6980", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6981",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6982", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6983", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6985",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6986", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6988", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6989",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6990", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6991", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6992",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6993", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6994", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6995",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6996", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6997", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=6998",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6999", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7000", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_v1;i=5001",
    browseName="ns=plastics_extrusion_v1;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6002",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6016", browseName="ns=plastics_rubber;AdditionalInformation", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6003"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6005"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6112"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1;i=7001", browseName="ns=plastics_rubber;Reset")),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.ExtrusionTemperatureZonesType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5001"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6032",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7002",
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
    nodeId="ns=plastics_extrusion_v1;i=7002",
    browseName="ns=plastics_rubber;SetMachineTime",
    description="Method for setting the server time together with TimeZoneOffset",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6032"]),
)

plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_v1;i=5013",
    browseName="ns=plastics_extrusion_v1;Maintenance",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6063",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6064",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6065"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6067"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6069"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7003",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the RemainingInterval to Interval and Status to NOT_DUE_0",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.ExtrusionDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5013"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6073",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6074",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1;i=7004",
    browseName="CloseAndCommit",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6073"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6074"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6075",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=plastics_rubber;i=3007"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6076",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7005",
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
    nodeId="ns=plastics_extrusion_v1;i=7005",
    browseName="GenerateFileForRead",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6075"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6076"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6077",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=o6.NodeId("ns=plastics_rubber;i=3004"), valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6078",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1;i=7006",
    browseName="GenerateFileForWrite",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6077"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6078"]),
)

ns0.objtypes.TemporaryFileTransferType(
    nodeId="ns=plastics_extrusion_v1;i=5016",
    browseName="ns=plastics_rubber;ProductionDatasetTransfer",
    description="Transfer of production datasets between server and client",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6072", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7004"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7005"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7006"]),
    ],
    eventNotifier=1,
)
o6.reference(o6.ns["ns=plastics_extrusion_v1;i=5016"], "i=41", "ns=plastics_rubber;i=1006")
o6.reference(o6.ns["ns=plastics_extrusion_v1;i=5016"], "i=41", "ns=plastics_rubber;i=1007")
o6.reference(o6.ns["ns=plastics_extrusion_v1;i=5016"], "i=41", "ns=plastics_rubber;i=1040")


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6080",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="Components", dataType=o6.UInt16, valueRank=1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1;i=7007",
    browseName="ns=plastics_rubber;Load",
    description="Loads a production dataset from the file system of the machine to the control of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6080"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6082",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1;i=7008",
    browseName="ns=plastics_rubber;Save",
    description="Stores a production dataset from the control of the machine to the file system of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6082"]),
)

plastics_rubber.objtypes.ProductionDatasetStatusType(
    nodeId="ns=plastics_extrusion_v1;i=5015",
    browseName="ns=plastics_rubber;ActiveProductionDatasetStatus",
    description="Status of the active production dataset",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6071",
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
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6079",
                browseName="ns=plastics_rubber;Frozen",
                description="Indication if changes on the machine in the production dataset are allowed",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6081",
                browseName="ns=plastics_rubber;Modified",
                description="Indication if the production dataset has been changed after the last storage",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7007"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7008"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6083",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="fileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6084",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Information", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1;i=7009",
    browseName="ns=plastics_rubber;GetProductionDatasetInformation",
    description="This Method allows reading the description of a production dataset during the file transfer from the server to the client with ProductionDatasetTransfer",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6083"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6084"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6086",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="NameFilter", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="MouldId", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6087",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductionDatasetList", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1;i=7010",
    browseName="ns=plastics_rubber;GetProductionDatasetList",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6086"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6087"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6088",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductionDatasetList", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=1)],
)
o6.call(nodeId="ns=plastics_extrusion_v1;i=7011", browseName="ns=plastics_rubber;SendProductionDatasetList", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6088"]))

plastics_rubber.objtypes.ProductionDatasetListsType(
    nodeId="ns=plastics_extrusion_v1;i=5020",
    browseName="ns=plastics_rubber;ProductionDatasetLists",
    description="Functions for exchanging information on the available production datasets on client and server",
    references=[o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7010"]), o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7011"])],
    eventNotifier=1,
)
o6.reference(o6.ns["ns=plastics_extrusion_v1;i=5020"], "i=41", "ns=plastics_rubber;i=1040")


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6089",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7012",
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
    nodeId="ns=plastics_extrusion_v1;i=7012",
    browseName="ns=plastics_rubber;SendProductionDatasetInformation",
    description="This Method allows sending of the description of a production dataset during the file transfer from the client to the server with ProductionDatasetTransfer",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6089"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6094",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="VisualisationUnit", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6095",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Page", dataType=ns0.datatypes.Image, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1;i=7013",
    browseName="ns=plastics_rubber;GetCurrentPage",
    description="Method for retrieving a screenshot of the control system with the currently shown contents",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6094"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6095"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6096",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6097",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Page", dataType=ns0.datatypes.Image, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1;i=7014",
    browseName="ns=plastics_rubber;GetPage",
    description="Method for retrieving the image of a page of the control system",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6096"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6097"]),
)

plastics_rubber.objtypes.MachineConfigurationType(
    nodeId="ns=plastics_extrusion_v1;i=5009",
    browseName="ns=plastics_extrusion_v1;MachineConfiguration",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6031",
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
                nodeId="ns=plastics_extrusion_v1;i=6033",
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
                nodeId="ns=plastics_extrusion_v1;i=6034",
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
                nodeId="ns=plastics_extrusion_v1;i=6098",
                browseName="ns=plastics_rubber;PageDirectory",
                description="List of the pages that are implemented in the machine control system and are shown on the screen of the machine",
                dataType=plastics_rubber.datatypes.PageEntryDataType,
                valueRank=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7002"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7013"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7014"]),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.ExtrusionDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5009"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6107",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="Components", dataType=o6.UInt16, valueRank=1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1;i=7015",
    browseName="ns=plastics_rubber;Load",
    description="Loads a production dataset from the file system of the machine to the control of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6107"]),
)

plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_v1;i=5017",
    browseName="ns=plastics_extrusion_v1;StartTempering",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6167", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6174",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1;i=7016", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1;i=7017", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.ExtrusionTemperatureZonesType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5017"])
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_v1;i=5004",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6131",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6211",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6212"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6215"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6218"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7018", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0"
            )
        ),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1;i=6109",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1;i=7019",
    browseName="ns=plastics_rubber;Save",
    description="Stores a production dataset from the control of the machine to the file system of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=6109"]),
)

plastics_rubber.objtypes.ProductionDatasetStatusType(
    nodeId="ns=plastics_extrusion_v1;i=5019",
    browseName="ns=plastics_rubber;ProductionDatasetInPreparationStatus",
    description="Status of the production dataset in the preparation layer",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6085",
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
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6106",
                browseName="ns=plastics_rubber;Frozen",
                description="Indication if changes on the machine in the production dataset are allowed",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6108",
                browseName="ns=plastics_rubber;Modified",
                description="Indication if the production dataset has been changed after the last storage",
                dataType=o6.Boolean,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7015"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7019"]),
    ],
)
plastics_rubber.objtypes.ProductionDatasetManagementType(
    nodeId="ns=plastics_extrusion_v1;i=5014",
    browseName="ns=plastics_extrusion_v1;ProductionDatasetManagement",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5015"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5016"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5019"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5020"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7009"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7012"]),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.ExtrusionDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5014"])
o6.reference(o6.ns["ns=plastics_extrusion_v1;i=5014"], "i=41", "ns=plastics_rubber;i=1004")
o6.reference(o6.ns["ns=plastics_extrusion_v1;i=5014"], "i=41", "ns=plastics_rubber;i=1011")
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_v1;i=5002",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6157",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6158",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6159",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7021",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_v1;i=7023", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_v1;i=5018",
    browseName="ns=plastics_extrusion_v1;StartDevice",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6104", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6128",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1;i=7022", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1;i=7024", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.ExtrusionDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5018"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1;i=5003",
    browseName="ns=plastics_extrusion_v1;ElectricalCurrent",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6163", browseName="ns=plastics_rubber;AutomaticMonitoring", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6123"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6160"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6164"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6168"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6171"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6176"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6179"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6182"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6185"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6188"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6191"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6194"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1;i=7025", browseName="ns=plastics_rubber;ResetMonitoring")),
    ],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_v1;i=5005",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6151",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6221", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1;i=7026", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1;i=7027", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_extrusion_v1_objtypes.ExtrusionTemperatureZoneType(
    nodeId="ns=plastics_extrusion_v1;i=5047",
    browseName="ns=plastics_extrusion_v1;TemperatureZone_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6001",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6110", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="\n      ")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6111", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6120",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6139", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6144", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5002"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5003"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5004"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5005"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6115"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6117"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6121"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6125"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6127"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6132"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6134"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6136"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6140"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6142"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6145"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6147"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6149"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6152"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6154"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7020",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.ExtrusionTemperatureZonesType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5047"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1;i=5006",
    browseName="ns=plastics_extrusion_v1;DistanceLeft",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6228",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6222"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6225"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6229"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6232"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6235"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6238"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6241"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6253"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6256"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6259"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6262"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6265"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7028",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.GapType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5006"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1;i=5007",
    browseName="ns=plastics_extrusion_v1;DistanceRight",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6274",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6268"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6271"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6275"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6278"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6281"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6284"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6287"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6290"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6293"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6296"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6299"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6302"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7029",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.GapType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5007"])
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_v1;i=5073",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6728",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6754",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6755"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6757"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6759"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7030", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0"
            )
        ),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1;i=5022",
    browseName="ns=plastics_extrusion_v1;ContactForce",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6313",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6307"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6310"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6314"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6317"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6320"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6323"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6326"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6329"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6332"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6335"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6338"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6341"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7032",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.GapType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5022"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1;i=5026",
    browseName="ns=plastics_extrusion_v1;DistanceLeft",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6364",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6352"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6361"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6365"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6368"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6371"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6374"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6377"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6380"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6383"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6386"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6389"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6392"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7033",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1;i=5044",
    browseName="ns=plastics_extrusion_v1;ElectricalCurrent",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6881", browseName="ns=plastics_rubber;AutomaticMonitoring", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6872"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6878"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6882"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6884"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6886"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6888"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6890"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6893"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6895"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6897"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6899"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6901"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1;i=7034", browseName="ns=plastics_rubber;ResetMonitoring")),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.ExtrusionTemperatureZoneType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5044"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1;i=5027",
    browseName="ns=plastics_extrusion_v1;DistanceRight",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6399",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6354"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6396"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6400"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6403"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6406"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6409"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6412"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6415"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6418"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6421"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6424"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6427"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7035",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.ClosedLoopControlType(
    nodeId="ns=plastics_extrusion_v1;i=5028",
    browseName="ns=plastics_rubber;ClosedLoopControl",
    description="With this type the client can do settings for the closed loop control on the device for a parameter",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6749",
                browseName="ns=plastics_rubber;AutoTuningActive",
                description="Informs if the automatic tuning is currently active",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6750",
                browseName="ns=plastics_rubber;AutomaticControllerMode",
                description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6751",
                browseName="ns=plastics_rubber;PIDParameters",
                description="PID Parameters as array if several input signals (sensors) are used for the control",
                dataType=plastics_rubber.datatypes.PIDParametersDataType,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7036",
                browseName="ns=plastics_rubber;AutoTuningOff",
                description="Stops an already active self-optimisation process (no control parameters are changed)",
            )
        ),
        o6.hasComponent(
            o6.call(nodeId="ns=plastics_extrusion_v1;i=7037", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
        ),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1;i=5029",
    browseName="ns=plastics_extrusion_v1;ContactForce",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6436",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6357"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6433"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6437"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6440"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6443"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6446"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6449"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6452"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6455"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6458"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6461"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6464"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7038",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_extrusion_v1_objtypes.GapType(
    nodeId="ns=plastics_extrusion_v1;i=5024",
    browseName="ns=plastics_extrusion_v1;Gap_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6349", browseName="ns=plastics_extrusion_v1;Id", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6350", browseName="ns=plastics_extrusion_v1;RollId1", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6351", browseName="ns=plastics_extrusion_v1;RollId2", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6360", browseName="ns=plastics_extrusion_v1;StockingGuideIsPresent", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5026"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5027"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5029"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1;i=6359", browseName="ns=plastics_extrusion_v1;IsClosed", dataType=o6.Boolean)),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.GapsType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5024"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1;i=5037",
    browseName="ns=plastics_rubber;Speed",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6789",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6546"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6786"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6790"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6792"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6794"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6796"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6798"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6801"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6804"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6908"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6910"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6912"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7039",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1;i=5031",
    browseName="ns=plastics_extrusion_v1;CrossAxisLeft",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6476",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6470"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6473"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6477"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6480"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6483"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6486"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6489"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6492"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6495"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6498"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6501"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6504"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7041",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.RollType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5031"])
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1;i=5032",
    browseName="ns=plastics_extrusion_v1;CrossAxisRight",
    modellingRule="Optional",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6513",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6507"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6510"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6514"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6517"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6520"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6523"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6526"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6529"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6532"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6535"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6538"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6541"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7042",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.RollType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5032"])
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_v1;i=5036",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6545",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6779",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6780"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6782"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6784"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7043",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the RemainingInterval to Interval and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_v1;i=5059",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6552",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6970",
                browseName="ns=plastics_rubber;AdditionalInformation",
                description="Additional information on the necessary maintenance. Can be also a link to another document.",
                dataType=o6.String,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6971"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6974"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6977"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7044",
                browseName="ns=plastics_rubber;Reset",
                description="This Method sets the RemainingInterval to Interval and Status to NOT_DUE_0",
            )
        ),
    ],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_v1;i=5038",
    browseName="ns=plastics_rubber;StartDrive",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6548",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6914", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1;i=7040", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1;i=7045", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1;i=5039",
    browseName="ns=plastics_rubber;Torque",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6918",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6549"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6915"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6919"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6921"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6923"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6925"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6927"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6930"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6932"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6934"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6936"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6938"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7046",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.DriveType(
    nodeId="ns=plastics_extrusion_v1;i=5033",
    browseName="ns=plastics_extrusion_v1;Drive",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5034"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5035"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5036"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5037"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5038"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5039"]),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.RollType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5033"])
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_v1;i=5048",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6581",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7049", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0"
            )
        ),
    ],
)
plastics_extrusion_v1_objtypes.ExtrusionTemperatureZoneType(
    nodeId="ns=plastics_extrusion_v1;i=5046",
    browseName="ns=plastics_extrusion_v1;Temperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6564",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6565", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="\n      ")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6566", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6572",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6589", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6594", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(
            plastics_rubber.objtypes.ClosedLoopControlType(
                nodeId="ns=plastics_extrusion_v1;i=5043",
                browseName="ns=plastics_rubber;ClosedLoopControl",
                description="With this type the client can do settings for the closed loop control on the device for a parameter",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5045"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5048"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5049"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6567"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6569"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6573"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6577"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6579"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6582"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6584"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6586"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6590"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6592"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6595"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6597"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6599"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6602"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6604"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7050",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.RollType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5046"])
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_v1;i=5053",
    browseName="ns=plastics_rubber;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6623",
                browseName="ns=plastics_rubber;Status",
                description="Maintenance status of the machine/device/component (represented by the parent element)",
                dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration,
                value=plastics_rubber.datatypes.MaintenanceStatusEnumeration.NOT_DUE,
            )
        ),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7051", browseName="ns=plastics_rubber;Reset", description="This Method sets the CurrentInterval to 0 and Status to NOT_DUE_0"
            )
        ),
    ],
)
plastics_extrusion_v1_objtypes.ExtrusionTemperatureZoneType(
    nodeId="ns=plastics_extrusion_v1;i=5068",
    browseName="ns=plastics_extrusion_v1;Temperature",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6611",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6614",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6617", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="\n      ")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6618", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6631", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6636", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(
            plastics_rubber.objtypes.ClosedLoopControlType(
                nodeId="ns=plastics_extrusion_v1;i=5050",
                browseName="ns=plastics_rubber;ClosedLoopControl",
                description="With this type the client can do settings for the closed loop control on the device for a parameter",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5051"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5053"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5063"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6606"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6608"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6612"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6619"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6621"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6624"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6626"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6628"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6632"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6634"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6637"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6640"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6644"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6647"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6649"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7052",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_v1;i=5074",
    browseName="ns=plastics_rubber;StartDevice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6744",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6766", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1;i=7057", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1;i=7058", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_rubber.objtypes.MeasuringDeviceType(
    nodeId="ns=plastics_extrusion_v1;i=5021",
    browseName="ns=plastics_extrusion_v1;ReferencePoint_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6306",
                browseName="ns=plastics_rubber;ControlMode",
                dataType=plastics_rubber.datatypes.ControlModeEnumeration,
                value=plastics_rubber.datatypes.ControlModeEnumeration.OTHER,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6430", browseName="ns=plastics_rubber;Id", dataType=o6.String, value="\n      ")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6431", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6723",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6736", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6737", browseName="ns=plastics_rubber;Position", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5028"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5073"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5074"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6717"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6720"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6724"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6726"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6729"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6731"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6733"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6738"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6740"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6742"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6745"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6747"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7031",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.RollBendingType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5021"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_v1;i=5076",
    browseName="ns=plastics_extrusion_v1;CleaningSystem_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6774",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6775", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1;i=7059", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1;i=7060", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.RollPeripheralDevicesType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5076"])
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_v1;i=5075",
    browseName="ns=plastics_extrusion_v1;InfraredHeatingSystem_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6773",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6776", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1;i=7061", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1;i=7062", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.RollPeripheralDevicesType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5075"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=7048",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7063", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7064", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1;i=5054",
    browseName="ns=plastics_extrusion_v1;CrossAxisLeft",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6811",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6806"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6808"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6812"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6815"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6818"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6821"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6824"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6827"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6830"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6833"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6836"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6839"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7065",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1;i=5055",
    browseName="ns=plastics_extrusion_v1;CrossAxisRight",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6847",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6842"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6844"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6848"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6851"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6854"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6857"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6860"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6863"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6866"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6869"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6874"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6905"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7066",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=7067",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7068", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7069", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=7070",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7071", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7072", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=7073",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7075", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7076", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=7077",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7078", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7081", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1;i=5060",
    browseName="ns=plastics_rubber;Speed",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6984",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6553"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6981"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6985"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6989"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6992"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6995"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6998"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7047",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7048"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7067"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7070"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7073"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7077"]),
    ],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_v1;i=5061",
    browseName="ns=plastics_rubber;StartDrive",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=6555",
                browseName="ns=plastics_rubber;Status",
                dataType=plastics_rubber.datatypes.StartEnumeration,
                value=plastics_rubber.datatypes.StartEnumeration.NOT_READY_TO_START,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=7082", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1;i=7083", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1;i=7084", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=6556",
    browseName="ns=plastics_rubber;ActualValue",
    description="Actual value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=6557", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7085", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=7086",
    browseName="ns=plastics_rubber;AlarmSuppression",
    description="The start-up alarm suppression deactivates alarms of a monitored parameter during start up or a setpoint jump",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7087", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7088", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=7090",
    browseName="ns=plastics_rubber;LowerTolerance",
    description="Lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7091", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7092", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=7093",
    browseName="ns=plastics_rubber;LowerTolerance2",
    description="Second lower relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7094", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7095", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=7096",
    browseName="ns=plastics_rubber;MaxValue",
    description="Maximum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7097", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7098", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=7099",
    browseName="ns=plastics_rubber;MinValue",
    description="Minimum absolute value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7100", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7101", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=plastics_extrusion_v1;i=7102",
    browseName="ns=plastics_rubber;MonitoringSensitivity",
    description="Defines how closely the tolerances are set during the automatic limit setting",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7103", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7104", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=o6.UInt16,
    value=0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=7106",
    browseName="ns=plastics_rubber;SetRampDown",
    description="Indication if SetValue that is lower than the actual value shall be reached as fast as possible (SetRampDown = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7107", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7108", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=7109",
    browseName="ns=plastics_rubber;SetRampUp",
    description="Indication if a SetValue that is higher than the actual value shall be reached as fast as possible (SetRampUp = 0) or within a given value change per time",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7110", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7111", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=7112",
    browseName="ns=plastics_rubber;SetValue",
    description="Set/nominal/target value of the monitored parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7113", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7114", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=7115",
    browseName="ns=plastics_rubber;UpperTolerance",
    description="Upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7116", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7117", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_v1;i=7118",
    browseName="ns=plastics_rubber;UpperTolerance2",
    description="Second upper relative tolerance value of the process parameter",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7119", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7120", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
plastics_rubber.objtypes.MonitoredParameterType(
    nodeId="ns=plastics_extrusion_v1;i=5062",
    browseName="ns=plastics_rubber;Torque",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_v1;i=7089",
                browseName="ns=plastics_rubber;AutomaticMonitoring",
                description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=6556"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7086"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7090"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7093"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7096"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7099"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7102"]),
        o6.hasComponent(
            o6.call(
                nodeId="ns=plastics_extrusion_v1;i=7105",
                browseName="ns=plastics_rubber;ResetMonitoring",
                description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
            )
        ),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7106"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7109"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7112"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7115"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=7118"]),
    ],
)
plastics_rubber.objtypes.DriveType(
    nodeId="ns=plastics_extrusion_v1;i=5056",
    browseName="ns=plastics_extrusion_v1;Drive",
    references=[
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5057"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5058"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5059"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5060"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5061"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5062"]),
    ],
)
ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7305", browseName="NodeVersion", dataType=o6.String)
o6.reference(o6.ns["ns=plastics_extrusion_v1;i=7305"], "i=41", "i=2133")
plastics_extrusion_v1_objtypes.RollPeripheralDevicesType(
    nodeId="ns=plastics_extrusion_v1;i=5040", browseName="ns=plastics_extrusion_v1;PeripheralDevices", references=[o6.hasProperty(o6.ns["ns=plastics_extrusion_v1;i=7305"])]
)
o6.reference(o6.ns["ns=plastics_extrusion_v1;i=5040"], "i=41", "i=2133")
plastics_extrusion_v1_objtypes.RollType(
    nodeId="ns=plastics_extrusion_v1;i=5052",
    browseName="ns=plastics_extrusion_v1;Roll_<Nr>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7074", browseName="ns=plastics_extrusion_v1;Id", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7079", browseName="ns=plastics_extrusion_v1;MasterRollId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1;i=7080", browseName="ns=plastics_extrusion_v1;Name", dataType=o6.LocalizedText)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5040"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5042"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5054"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5055"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5056"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_v1;i=5068"]),
    ],
)
o6.reference(plastics_extrusion_v1_objtypes.RollsType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_v1;i=5052"])


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_rubber, plastics_extrusion_v1_datypes, plastics_extrusion_v1_objtypes
