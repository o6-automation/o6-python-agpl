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

"""Generated OPC UA commercial_kitchen namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import datatypes as commercial_kitchen_datypes
from . import objtypes as commercial_kitchen_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=commercial_kitchen;i=6011",
    browseName="ns=commercial_kitchen;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/CommercialKitchenEquipment/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6012", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/CommercialKitchenEquipment/"
            )
        )
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/CommercialKitchenEquipment/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/CommercialKitchenEquipment/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:EnumeratedType LengthInBits="32" Name="BeverageSMLEnumeration">\n  <opc:EnumeratedValue Name="Inactive" Value="0"/>\n  <opc:EnumeratedValue Name="Small" Value="1"/>\n  <opc:EnumeratedValue Name="Large" Value="2"/>\n  <opc:EnumeratedValue Name="ExtraLarge" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ChamberModeEnumeration">\n  <opc:EnumeratedValue Name="NoSpecialMode" Value="0"/>\n  <opc:EnumeratedValue Name="Off" Value="1"/>\n  <opc:EnumeratedValue Name="Autostart" Value="2"/>\n  <opc:EnumeratedValue Name="Standby" Value="3"/>\n  <opc:EnumeratedValue Name="PreHeat" Value="4"/>\n  <opc:EnumeratedValue Name="CoolDown" Value="5"/>\n  <opc:EnumeratedValue Name="Working" Value="6"/>\n  <opc:EnumeratedValue Name="Cleaning" Value="7"/>\n  <opc:EnumeratedValue Name="EnergySave" Value="8"/>\n  <opc:EnumeratedValue Name="ServiceMode" Value="9"/>\n  <opc:EnumeratedValue Name="QuickCool" Value="10"/>\n  <opc:EnumeratedValue Name="FlashFreeze" Value="11"/>\n  <opc:EnumeratedValue Name="ProofingInterruption" Value="12"/>\n  <opc:EnumeratedValue Name="ProofingDelay" Value="13"/>\n  <opc:EnumeratedValue Name="Proofing" Value="14"/>\n  <opc:EnumeratedValue Name="Setting" Value="15"/>\n  <opc:EnumeratedValue Name="Defrost" Value="16"/>\n  <opc:EnumeratedValue Name="Baking" Value="17"/>\n  <opc:EnumeratedValue Name="Steaming" Value="18"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="CoffeeMachineModeEnumeration">\n  <opc:EnumeratedValue Name="Off" Value="0"/>\n  <opc:EnumeratedValue Name="Standby" Value="1"/>\n  <opc:EnumeratedValue Name="Error" Value="2"/>\n  <opc:EnumeratedValue Name="Cleaning" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="CombiSteamerModeEnumeration">\n  <opc:EnumeratedValue Name="Off" Value="0"/>\n  <opc:EnumeratedValue Name="On" Value="1"/>\n  <opc:EnumeratedValue Name="Preheat" Value="2"/>\n  <opc:EnumeratedValue Name="StandBy" Value="3"/>\n  <opc:EnumeratedValue Name="Steaming" Value="4"/>\n  <opc:EnumeratedValue Name="CombiSteaming" Value="5"/>\n  <opc:EnumeratedValue Name="HotAir" Value="6"/>\n  <opc:EnumeratedValue Name="Perfection" Value="7"/>\n  <opc:EnumeratedValue Name="Cleaning" Value="8"/>\n  <opc:EnumeratedValue Name="PresetStart" Value="9"/>\n  <opc:EnumeratedValue Name="Error" Value="10"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="CookingKettleModeEnumeration">\n  <opc:EnumeratedValue Name="Off" Value="0"/>\n  <opc:EnumeratedValue Name="Preheat" Value="1"/>\n  <opc:EnumeratedValue Name="SoftCook" Value="2"/>\n  <opc:EnumeratedValue Name="Cook" Value="3"/>\n  <opc:EnumeratedValue Name="CookSlow" Value="4"/>\n  <opc:EnumeratedValue Name="KeepWarming" Value="5"/>\n  <opc:EnumeratedValue Name="Stiring" Value="6"/>\n  <opc:EnumeratedValue Name="PresetStart" Value="7"/>\n  <opc:EnumeratedValue Name="Error" Value="8"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="CurrentStateEnumeration">\n  <opc:EnumeratedValue Name="Off" Value="0"/>\n  <opc:EnumeratedValue Name="Standby" Value="1"/>\n  <opc:EnumeratedValue Name="Power" Value="2"/>\n  <opc:EnumeratedValue Name="PotDetection" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="EnergySourceEnumeration">\n  <opc:EnumeratedValue Name="Electric" Value="0"/>\n  <opc:EnumeratedValue Name="Gas" Value="1"/>\n  <opc:EnumeratedValue Name="Steam" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="FryerModeEnumeration">\n  <opc:EnumeratedValue Name="Off" Value="0"/>\n  <opc:EnumeratedValue Name="Preheat" Value="1"/>\n  <opc:EnumeratedValue Name="Melting" Value="2"/>\n  <opc:EnumeratedValue Name="Frying" Value="3"/>\n  <opc:EnumeratedValue Name="StandBy" Value="4"/>\n  <opc:EnumeratedValue Name="Filtering" Value="5"/>\n  <opc:EnumeratedValue Name="Error" Value="6"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="FryingPanModeEnumeration">\n  <opc:EnumeratedValue Name="Off" Value="0"/>\n  <opc:EnumeratedValue Name="Preheat" Value="1"/>\n  <opc:EnumeratedValue Name="SoftCook" Value="2"/>\n  <opc:EnumeratedValue Name="Cook" Value="3"/>\n  <opc:EnumeratedValue Name="CookSlow" Value="4"/>\n  <opc:EnumeratedValue Name="Frying" Value="5"/>\n  <opc:EnumeratedValue Name="PressureCooking" Value="6"/>\n  <opc:EnumeratedValue Name="KeepWarming" Value="7"/>\n  <opc:EnumeratedValue Name="PresetStart" Value="8"/>\n  <opc:EnumeratedValue Name="Error" Value="9"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="GrillingZoneStateEnumeration">\n  <opc:EnumeratedValue Name="Off" Value="0"/>\n  <opc:EnumeratedValue Name="Standby" Value="1"/>\n  <opc:EnumeratedValue Name="Idle" Value="2"/>\n  <opc:EnumeratedValue Name="Grilling" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="HygieneModeEnumeration">\n  <opc:EnumeratedValue Name="HygieneOperationOFF" Value="0"/>\n  <opc:EnumeratedValue Name="HygieneA0" Value="1"/>\n  <opc:EnumeratedValue Name="HygieneHUE" Value="2"/>\n  <opc:EnumeratedValue Name="HygieneMU" Value="3"/>\n  <opc:EnumeratedValue Name="HygieneThermolable" Value="4"/>\n  <opc:EnumeratedValue Name="HygieneA0_TD" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="MultiFunctionPanModeEnumeration">\n  <opc:EnumeratedValue Name="Off" Value="0"/>\n  <opc:EnumeratedValue Name="On" Value="1"/>\n  <opc:EnumeratedValue Name="Preheat" Value="2"/>\n  <opc:EnumeratedValue Name="StandBy" Value="3"/>\n  <opc:EnumeratedValue Name="PressureCooking" Value="4"/>\n  <opc:EnumeratedValue Name="SoftCooking" Value="5"/>\n  <opc:EnumeratedValue Name="Cooking" Value="6"/>\n  <opc:EnumeratedValue Name="Grilling" Value="7"/>\n  <opc:EnumeratedValue Name="Frying" Value="8"/>\n  <opc:EnumeratedValue Name="Regenerate" Value="9"/>\n  <opc:EnumeratedValue Name="DeltaTcooking" Value="10"/>\n  <opc:EnumeratedValue Name="ZoneGrilling" Value="11"/>\n  <opc:EnumeratedValue Name="ZoneCooking" Value="12"/>\n  <opc:EnumeratedValue Name="Cleaning" Value="13"/>\n  <opc:EnumeratedValue Name="PresetStart" Value="14"/>\n  <opc:EnumeratedValue Name="Error" Value="15"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="OperatingModeEnumeration">\n  <opc:EnumeratedValue Name="Preheat" Value="0"/>\n  <opc:EnumeratedValue Name="CoolDown" Value="1"/>\n  <opc:EnumeratedValue Name="Process" Value="2"/>\n  <opc:EnumeratedValue Name="PowerSaving" Value="3"/>\n  <opc:EnumeratedValue Name="Standby" Value="4"/>\n  <opc:EnumeratedValue Name="Service" Value="5"/>\n  <opc:EnumeratedValue Name="Cleaning" Value="6"/>\n  <opc:EnumeratedValue Name="Off" Value="7"/>\n  <opc:EnumeratedValue Name="Error" Value="8"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="OperationModeEnumeration">\n  <opc:EnumeratedValue Name="Init" Value="0"/>\n  <opc:EnumeratedValue Name="MachineOff" Value="1"/>\n  <opc:EnumeratedValue Name="Filling" Value="2"/>\n  <opc:EnumeratedValue Name="FillingHeating" Value="3"/>\n  <opc:EnumeratedValue Name="Heating" Value="4"/>\n  <opc:EnumeratedValue Name="EnableOperation" Value="5"/>\n  <opc:EnumeratedValue Name="ReadyForOperation" Value="6"/>\n  <opc:EnumeratedValue Name="Operation" Value="7"/>\n  <opc:EnumeratedValue Name="Cycle_pause" Value="8"/>\n  <opc:EnumeratedValue Name="NotDefined1" Value="9"/>\n  <opc:EnumeratedValue Name="SelfCleaning" Value="10"/>\n  <opc:EnumeratedValue Name="NotDefined2" Value="11"/>\n  <opc:EnumeratedValue Name="RemoteControl" Value="12"/>\n  <opc:EnumeratedValue Name="ControllingOutputs" Value="13"/>\n  <opc:EnumeratedValue Name="NotDefined3" Value="14"/>\n  <opc:EnumeratedValue Name="Error" Value="15"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PastaCookerModeEnumeration">\n  <opc:EnumeratedValue Name="Off" Value="0"/>\n  <opc:EnumeratedValue Name="Preheat" Value="1"/>\n  <opc:EnumeratedValue Name="SoftCook" Value="2"/>\n  <opc:EnumeratedValue Name="Cook" Value="3"/>\n  <opc:EnumeratedValue Name="CookSlow" Value="4"/>\n  <opc:EnumeratedValue Name="KeepWarming" Value="5"/>\n  <opc:EnumeratedValue Name="PresetStart" Value="6"/>\n  <opc:EnumeratedValue Name="Error" Value="7"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PlatenPositionStateEnumeration">\n  <opc:EnumeratedValue Name="Home" Value="0"/>\n  <opc:EnumeratedValue Name="Cooking" Value="1"/>\n  <opc:EnumeratedValue Name="Idle" Value="2"/>\n  <opc:EnumeratedValue Name="Open" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PressureCookingKettleModeEnumeration">\n  <opc:EnumeratedValue Name="Off" Value="0"/>\n  <opc:EnumeratedValue Name="Preheat" Value="1"/>\n  <opc:EnumeratedValue Name="SoftCook" Value="2"/>\n  <opc:EnumeratedValue Name="Cook" Value="3"/>\n  <opc:EnumeratedValue Name="CookSlow" Value="4"/>\n  <opc:EnumeratedValue Name="Pressure" Value="5"/>\n  <opc:EnumeratedValue Name="KeepWarming" Value="6"/>\n  <opc:EnumeratedValue Name="PresetStart" Value="7"/>\n  <opc:EnumeratedValue Name="Error" Value="8"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ProgramModeEnumeration">\n  <opc:EnumeratedValue Name="OperationOFF" Value="0"/>\n  <opc:EnumeratedValue Name="PreWash" Value="1"/>\n  <opc:EnumeratedValue Name="Cleaning1" Value="2"/>\n  <opc:EnumeratedValue Name="WashTimeIncreased" Value="3"/>\n  <opc:EnumeratedValue Name="Cleaning2" Value="4"/>\n  <opc:EnumeratedValue Name="DrainingPause" Value="5"/>\n  <opc:EnumeratedValue Name="Draining" Value="6"/>\n  <opc:EnumeratedValue Name="FinalRinse" Value="7"/>\n  <opc:EnumeratedValue Name="WaitingTime" Value="8"/>\n  <opc:EnumeratedValue Name="HeatRecovery" Value="9"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="SignalModeEnumeration">\n  <opc:EnumeratedValue Name="SignalOff" Value="0"/>\n  <opc:EnumeratedValue Name="SignalOn" Value="1"/>\n  <opc:EnumeratedValue Name="SignalAck" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="SpecialCookingModeEnumeration">\n  <opc:EnumeratedValue Name="NoSpecialMode" Value="0"/>\n  <opc:EnumeratedValue Name="Baking" Value="1"/>\n  <opc:EnumeratedValue Name="SousVide" Value="2"/>\n  <opc:EnumeratedValue Name="RestStage" Value="3"/>\n  <opc:EnumeratedValue Name="Humidification" Value="4"/>\n  <opc:EnumeratedValue Name="PerfectHold" Value="5"/>\n  <opc:EnumeratedValue Name="InfoStep" Value="6"/>\n  <opc:EnumeratedValue Name="Smoking" Value="7"/>\n  <opc:EnumeratedValue Name="LowTemp-Cooking" Value="8"/>\n  <opc:EnumeratedValue Name="DeltaTSteaming" Value="9"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="SpecialFunctionModeEnumeration">\n  <opc:EnumeratedValue Name="LidUpDown" Value="0"/>\n  <opc:EnumeratedValue Name="PanTilt" Value="1"/>\n  <opc:EnumeratedValue Name="WaterSupply" Value="2"/>\n  <opc:EnumeratedValue Name="DrainOnOff" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="StatusEnumeration">\n  <opc:EnumeratedValue Name="INIT" Value="0"/>\n  <opc:EnumeratedValue Name="WATER_PURGE" Value="1"/>\n  <opc:EnumeratedValue Name="PRE_CHILL" Value="2"/>\n  <opc:EnumeratedValue Name="FREEZE" Value="3"/>\n  <opc:EnumeratedValue Name="HARVEST" Value="4"/>\n  <opc:EnumeratedValue Name="BIN_FULL" Value="5"/>\n  <opc:EnumeratedValue Name="CLEAN" Value="6"/>\n  <opc:EnumeratedValue Name="OFF" Value="7"/>\n  <opc:EnumeratedValue Name="SLEEP_MODE" Value="8"/>\n  <opc:EnumeratedValue Name="STANDBY" Value="9"/>\n  <opc:EnumeratedValue Name="SAFE_MODE" Value="10"/>\n  <opc:EnumeratedValue Name="WATER_OUTAGE" Value="11"/>\n  <opc:EnumeratedValue Name="HPCO_DELAY_ACTIVE" Value="12"/>\n  <opc:EnumeratedValue Name="CURTAIN_OPEN" Value="13"/>\n  <opc:EnumeratedValue Name="PRODUCTION_TEST" Value="14"/>\n  <opc:EnumeratedValue Name="SAFE_MODE_PRECHILL" Value="15"/>\n  <opc:EnumeratedValue Name="SAFE_MODE_FREEZE" Value="16"/>\n  <opc:EnumeratedValue Name="SAFE_MODE_HARVEST" Value="17"/>\n  <opc:EnumeratedValue Name="SAFE_MODE_FULL_BIN" Value="18"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="TrayModeEnumeration">\n  <opc:EnumeratedValue Name="Off" Value="0"/>\n  <opc:EnumeratedValue Name="PreHeat" Value="1"/>\n  <opc:EnumeratedValue Name="PreCool" Value="2"/>\n  <opc:EnumeratedValue Name="HoldWarm" Value="3"/>\n  <opc:EnumeratedValue Name="HoldCool" Value="4"/>\n  <opc:EnumeratedValue Name="Regenerating" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="TrayTypeEnumeration">\n  <opc:EnumeratedValue Name="Generic" Value="0"/>\n  <opc:EnumeratedValue Name="HeaterPlate" Value="1"/>\n  <opc:EnumeratedValue Name="CoolingPlate" Value="2"/>\n  <opc:EnumeratedValue Name="CombiPlate" Value="3"/>\n  <opc:EnumeratedValue Name="BainMarie" Value="4"/>\n  <opc:EnumeratedValue Name="HeaterCabinet" Value="5"/>\n  <opc:EnumeratedValue Name="CoolingCabinet" Value="6"/>\n  <opc:EnumeratedValue Name="HeatBridge" Value="7"/>\n  <opc:EnumeratedValue Name="CombiCabinet" Value="8"/>\n  <opc:EnumeratedValue Name="RegenCabinet" Value="9"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=commercial_kitchen;i=6013",
    browseName="ns=commercial_kitchen;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/CommercialKitchenEquipment/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6014", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/CommercialKitchenEquipment/Types.xsd"
            )
        )
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/CommercialKitchenEquipment/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/CommercialKitchenEquipment/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="BeverageSMLEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Inactive_0"/>\n   <xs:enumeration value="Small_1"/>\n   <xs:enumeration value="Large_2"/>\n   <xs:enumeration value="ExtraLarge_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BeverageSMLEnumeration" name="BeverageSMLEnumeration"/>\n <xs:complexType name="ListOfBeverageSMLEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BeverageSMLEnumeration" name="BeverageSMLEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBeverageSMLEnumeration" name="ListOfBeverageSMLEnumeration" nillable="true"/>\n <xs:simpleType name="ChamberModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NoSpecialMode_0"/>\n   <xs:enumeration value="Off_1"/>\n   <xs:enumeration value="Autostart_2"/>\n   <xs:enumeration value="Standby_3"/>\n   <xs:enumeration value="PreHeat_4"/>\n   <xs:enumeration value="CoolDown_5"/>\n   <xs:enumeration value="Working_6"/>\n   <xs:enumeration value="Cleaning_7"/>\n   <xs:enumeration value="EnergySave_8"/>\n   <xs:enumeration value="ServiceMode_9"/>\n   <xs:enumeration value="QuickCool_10"/>\n   <xs:enumeration value="FlashFreeze_11"/>\n   <xs:enumeration value="ProofingInterruption_12"/>\n   <xs:enumeration value="ProofingDelay_13"/>\n   <xs:enumeration value="Proofing_14"/>\n   <xs:enumeration value="Setting_15"/>\n   <xs:enumeration value="Defrost_16"/>\n   <xs:enumeration value="Baking_17"/>\n   <xs:enumeration value="Steaming_18"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ChamberModeEnumeration" name="ChamberModeEnumeration"/>\n <xs:complexType name="ListOfChamberModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ChamberModeEnumeration" name="ChamberModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfChamberModeEnumeration" name="ListOfChamberModeEnumeration" nillable="true"/>\n <xs:simpleType name="CoffeeMachineModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Off_0"/>\n   <xs:enumeration value="Standby_1"/>\n   <xs:enumeration value="Error_2"/>\n   <xs:enumeration value="Cleaning_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CoffeeMachineModeEnumeration" name="CoffeeMachineModeEnumeration"/>\n <xs:complexType name="ListOfCoffeeMachineModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CoffeeMachineModeEnumeration" name="CoffeeMachineModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCoffeeMachineModeEnumeration" name="ListOfCoffeeMachineModeEnumeration" nillable="true"/>\n <xs:simpleType name="CombiSteamerModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Off_0"/>\n   <xs:enumeration value="On_1"/>\n   <xs:enumeration value="Preheat_2"/>\n   <xs:enumeration value="StandBy_3"/>\n   <xs:enumeration value="Steaming_4"/>\n   <xs:enumeration value="CombiSteaming_5"/>\n   <xs:enumeration value="HotAir_6"/>\n   <xs:enumeration value="Perfection_7"/>\n   <xs:enumeration value="Cleaning_8"/>\n   <xs:enumeration value="PresetStart_9"/>\n   <xs:enumeration value="Error_10"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CombiSteamerModeEnumeration" name="CombiSteamerModeEnumeration"/>\n <xs:complexType name="ListOfCombiSteamerModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CombiSteamerModeEnumeration" name="CombiSteamerModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCombiSteamerModeEnumeration" name="ListOfCombiSteamerModeEnumeration" nillable="true"/>\n <xs:simpleType name="CookingKettleModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Off_0"/>\n   <xs:enumeration value="Preheat_1"/>\n   <xs:enumeration value="SoftCook_2"/>\n   <xs:enumeration value="Cook_3"/>\n   <xs:enumeration value="CookSlow_4"/>\n   <xs:enumeration value="KeepWarming_5"/>\n   <xs:enumeration value="Stiring_6"/>\n   <xs:enumeration value="PresetStart_7"/>\n   <xs:enumeration value="Error_8"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CookingKettleModeEnumeration" name="CookingKettleModeEnumeration"/>\n <xs:complexType name="ListOfCookingKettleModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CookingKettleModeEnumeration" name="CookingKettleModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCookingKettleModeEnumeration" name="ListOfCookingKettleModeEnumeration" nillable="true"/>\n <xs:simpleType name="CurrentStateEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Off_0"/>\n   <xs:enumeration value="Standby_1"/>\n   <xs:enumeration value="Power_2"/>\n   <xs:enumeration value="PotDetection_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CurrentStateEnumeration" name="CurrentStateEnumeration"/>\n <xs:complexType name="ListOfCurrentStateEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CurrentStateEnumeration" name="CurrentStateEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCurrentStateEnumeration" name="ListOfCurrentStateEnumeration" nillable="true"/>\n <xs:simpleType name="EnergySourceEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Electric_0"/>\n   <xs:enumeration value="Gas_1"/>\n   <xs:enumeration value="Steam_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:EnergySourceEnumeration" name="EnergySourceEnumeration"/>\n <xs:complexType name="ListOfEnergySourceEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:EnergySourceEnumeration" name="EnergySourceEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEnergySourceEnumeration" name="ListOfEnergySourceEnumeration" nillable="true"/>\n <xs:simpleType name="FryerModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Off_0"/>\n   <xs:enumeration value="Preheat_1"/>\n   <xs:enumeration value="Melting_2"/>\n   <xs:enumeration value="Frying_3"/>\n   <xs:enumeration value="StandBy_4"/>\n   <xs:enumeration value="Filtering_5"/>\n   <xs:enumeration value="Error_6"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:FryerModeEnumeration" name="FryerModeEnumeration"/>\n <xs:complexType name="ListOfFryerModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:FryerModeEnumeration" name="FryerModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfFryerModeEnumeration" name="ListOfFryerModeEnumeration" nillable="true"/>\n <xs:simpleType name="FryingPanModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Off_0"/>\n   <xs:enumeration value="Preheat_1"/>\n   <xs:enumeration value="SoftCook_2"/>\n   <xs:enumeration value="Cook_3"/>\n   <xs:enumeration value="CookSlow_4"/>\n   <xs:enumeration value="Frying_5"/>\n   <xs:enumeration value="PressureCooking_6"/>\n   <xs:enumeration value="KeepWarming_7"/>\n   <xs:enumeration value="PresetStart_8"/>\n   <xs:enumeration value="Error_9"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:FryingPanModeEnumeration" name="FryingPanModeEnumeration"/>\n <xs:complexType name="ListOfFryingPanModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:FryingPanModeEnumeration" name="FryingPanModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfFryingPanModeEnumeration" name="ListOfFryingPanModeEnumeration" nillable="true"/>\n <xs:simpleType name="GrillingZoneStateEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Off_0"/>\n   <xs:enumeration value="Standby_1"/>\n   <xs:enumeration value="Idle_2"/>\n   <xs:enumeration value="Grilling_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:GrillingZoneStateEnumeration" name="GrillingZoneStateEnumeration"/>\n <xs:complexType name="ListOfGrillingZoneStateEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:GrillingZoneStateEnumeration" name="GrillingZoneStateEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfGrillingZoneStateEnumeration" name="ListOfGrillingZoneStateEnumeration" nillable="true"/>\n <xs:simpleType name="HygieneModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="HygieneOperationOFF_0"/>\n   <xs:enumeration value="HygieneA0_1"/>\n   <xs:enumeration value="HygieneHUE_2"/>\n   <xs:enumeration value="HygieneMU_3"/>\n   <xs:enumeration value="HygieneThermolable_4"/>\n   <xs:enumeration value="HygieneA0_TD_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:HygieneModeEnumeration" name="HygieneModeEnumeration"/>\n <xs:complexType name="ListOfHygieneModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:HygieneModeEnumeration" name="HygieneModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfHygieneModeEnumeration" name="ListOfHygieneModeEnumeration" nillable="true"/>\n <xs:simpleType name="MultiFunctionPanModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Off_0"/>\n   <xs:enumeration value="On_1"/>\n   <xs:enumeration value="Preheat_2"/>\n   <xs:enumeration value="StandBy_3"/>\n   <xs:enumeration value="PressureCooking_4"/>\n   <xs:enumeration value="SoftCooking_5"/>\n   <xs:enumeration value="Cooking_6"/>\n   <xs:enumeration value="Grilling_7"/>\n   <xs:enumeration value="Frying_8"/>\n   <xs:enumeration value="Regenerate_9"/>\n   <xs:enumeration value="DeltaTcooking_10"/>\n   <xs:enumeration value="ZoneGrilling_11"/>\n   <xs:enumeration value="ZoneCooking_12"/>\n   <xs:enumeration value="Cleaning_13"/>\n   <xs:enumeration value="PresetStart_14"/>\n   <xs:enumeration value="Error_15"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:MultiFunctionPanModeEnumeration" name="MultiFunctionPanModeEnumeration"/>\n <xs:complexType name="ListOfMultiFunctionPanModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:MultiFunctionPanModeEnumeration" name="MultiFunctionPanModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfMultiFunctionPanModeEnumeration" name="ListOfMultiFunctionPanModeEnumeration" nillable="true"/>\n <xs:simpleType name="OperatingModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Preheat_0"/>\n   <xs:enumeration value="CoolDown_1"/>\n   <xs:enumeration value="Process_2"/>\n   <xs:enumeration value="PowerSaving_3"/>\n   <xs:enumeration value="Standby_4"/>\n   <xs:enumeration value="Service_5"/>\n   <xs:enumeration value="Cleaning_6"/>\n   <xs:enumeration value="Off_7"/>\n   <xs:enumeration value="Error_8"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:OperatingModeEnumeration" name="OperatingModeEnumeration"/>\n <xs:complexType name="ListOfOperatingModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OperatingModeEnumeration" name="OperatingModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOperatingModeEnumeration" name="ListOfOperatingModeEnumeration" nillable="true"/>\n <xs:simpleType name="OperationModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Init_0"/>\n   <xs:enumeration value="MachineOff_1"/>\n   <xs:enumeration value="Filling_2"/>\n   <xs:enumeration value="FillingHeating_3"/>\n   <xs:enumeration value="Heating_4"/>\n   <xs:enumeration value="EnableOperation_5"/>\n   <xs:enumeration value="ReadyForOperation_6"/>\n   <xs:enumeration value="Operation_7"/>\n   <xs:enumeration value="Cycle_pause_8"/>\n   <xs:enumeration value="NotDefined1_9"/>\n   <xs:enumeration value="SelfCleaning_10"/>\n   <xs:enumeration value="NotDefined2_11"/>\n   <xs:enumeration value="RemoteControl_12"/>\n   <xs:enumeration value="ControllingOutputs_13"/>\n   <xs:enumeration value="NotDefined3_14"/>\n   <xs:enumeration value="Error_15"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:OperationModeEnumeration" name="OperationModeEnumeration"/>\n <xs:complexType name="ListOfOperationModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OperationModeEnumeration" name="OperationModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOperationModeEnumeration" name="ListOfOperationModeEnumeration" nillable="true"/>\n <xs:simpleType name="PastaCookerModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Off_0"/>\n   <xs:enumeration value="Preheat_1"/>\n   <xs:enumeration value="SoftCook_2"/>\n   <xs:enumeration value="Cook_3"/>\n   <xs:enumeration value="CookSlow_4"/>\n   <xs:enumeration value="KeepWarming_5"/>\n   <xs:enumeration value="PresetStart_6"/>\n   <xs:enumeration value="Error_7"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PastaCookerModeEnumeration" name="PastaCookerModeEnumeration"/>\n <xs:complexType name="ListOfPastaCookerModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PastaCookerModeEnumeration" name="PastaCookerModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPastaCookerModeEnumeration" name="ListOfPastaCookerModeEnumeration" nillable="true"/>\n <xs:simpleType name="PlatenPositionStateEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Home_0"/>\n   <xs:enumeration value="Cooking_1"/>\n   <xs:enumeration value="Idle_2"/>\n   <xs:enumeration value="Open_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PlatenPositionStateEnumeration" name="PlatenPositionStateEnumeration"/>\n <xs:complexType name="ListOfPlatenPositionStateEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PlatenPositionStateEnumeration" name="PlatenPositionStateEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPlatenPositionStateEnumeration" name="ListOfPlatenPositionStateEnumeration" nillable="true"/>\n <xs:simpleType name="PressureCookingKettleModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Off_0"/>\n   <xs:enumeration value="Preheat_1"/>\n   <xs:enumeration value="SoftCook_2"/>\n   <xs:enumeration value="Cook_3"/>\n   <xs:enumeration value="CookSlow_4"/>\n   <xs:enumeration value="Pressure_5"/>\n   <xs:enumeration value="KeepWarming_6"/>\n   <xs:enumeration value="PresetStart_7"/>\n   <xs:enumeration value="Error_8"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PressureCookingKettleModeEnumeration" name="PressureCookingKettleModeEnumeration"/>\n <xs:complexType name="ListOfPressureCookingKettleModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PressureCookingKettleModeEnumeration" name="PressureCookingKettleModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPressureCookingKettleModeEnumeration" name="ListOfPressureCookingKettleModeEnumeration" nillable="true"/>\n <xs:simpleType name="ProgramModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="OperationOFF_0"/>\n   <xs:enumeration value="PreWash_1"/>\n   <xs:enumeration value="Cleaning1_2"/>\n   <xs:enumeration value="WashTimeIncreased_3"/>\n   <xs:enumeration value="Cleaning2_4"/>\n   <xs:enumeration value="DrainingPause_5"/>\n   <xs:enumeration value="Draining_6"/>\n   <xs:enumeration value="FinalRinse_7"/>\n   <xs:enumeration value="WaitingTime_8"/>\n   <xs:enumeration value="HeatRecovery_9"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ProgramModeEnumeration" name="ProgramModeEnumeration"/>\n <xs:complexType name="ListOfProgramModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ProgramModeEnumeration" name="ProgramModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfProgramModeEnumeration" name="ListOfProgramModeEnumeration" nillable="true"/>\n <xs:simpleType name="SignalModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="SignalOff_0"/>\n   <xs:enumeration value="SignalOn_1"/>\n   <xs:enumeration value="SignalAck_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SignalModeEnumeration" name="SignalModeEnumeration"/>\n <xs:complexType name="ListOfSignalModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SignalModeEnumeration" name="SignalModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSignalModeEnumeration" name="ListOfSignalModeEnumeration" nillable="true"/>\n <xs:simpleType name="SpecialCookingModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NoSpecialMode_0"/>\n   <xs:enumeration value="Baking_1"/>\n   <xs:enumeration value="SousVide_2"/>\n   <xs:enumeration value="RestStage_3"/>\n   <xs:enumeration value="Humidification_4"/>\n   <xs:enumeration value="PerfectHold_5"/>\n   <xs:enumeration value="InfoStep_6"/>\n   <xs:enumeration value="Smoking_7"/>\n   <xs:enumeration value="LowTemp-Cooking_8"/>\n   <xs:enumeration value="DeltaTSteaming_9"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SpecialCookingModeEnumeration" name="SpecialCookingModeEnumeration"/>\n <xs:complexType name="ListOfSpecialCookingModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SpecialCookingModeEnumeration" name="SpecialCookingModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSpecialCookingModeEnumeration" name="ListOfSpecialCookingModeEnumeration" nillable="true"/>\n <xs:simpleType name="SpecialFunctionModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="LidUpDown_0"/>\n   <xs:enumeration value="PanTilt_1"/>\n   <xs:enumeration value="WaterSupply_2"/>\n   <xs:enumeration value="DrainOnOff_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SpecialFunctionModeEnumeration" name="SpecialFunctionModeEnumeration"/>\n <xs:complexType name="ListOfSpecialFunctionModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SpecialFunctionModeEnumeration" name="SpecialFunctionModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSpecialFunctionModeEnumeration" name="ListOfSpecialFunctionModeEnumeration" nillable="true"/>\n <xs:simpleType name="StatusEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="INIT_0"/>\n   <xs:enumeration value="WATER_PURGE_1"/>\n   <xs:enumeration value="PRE_CHILL_2"/>\n   <xs:enumeration value="FREEZE_3"/>\n   <xs:enumeration value="HARVEST_4"/>\n   <xs:enumeration value="BIN_FULL_5"/>\n   <xs:enumeration value="CLEAN_6"/>\n   <xs:enumeration value="OFF_7"/>\n   <xs:enumeration value="SLEEP_MODE_8"/>\n   <xs:enumeration value="STANDBY_9"/>\n   <xs:enumeration value="SAFE_MODE_10"/>\n   <xs:enumeration value="WATER_OUTAGE_11"/>\n   <xs:enumeration value="HPCO_DELAY_ACTIVE_12"/>\n   <xs:enumeration value="CURTAIN_OPEN_13"/>\n   <xs:enumeration value="PRODUCTION_TEST_14"/>\n   <xs:enumeration value="SAFE_MODE_PRECHILL_15"/>\n   <xs:enumeration value="SAFE_MODE_FREEZE_16"/>\n   <xs:enumeration value="SAFE_MODE_HARVEST_17"/>\n   <xs:enumeration value="SAFE_MODE_FULL_BIN_18"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:StatusEnumeration" name="StatusEnumeration"/>\n <xs:complexType name="ListOfStatusEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:StatusEnumeration" name="StatusEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfStatusEnumeration" name="ListOfStatusEnumeration" nillable="true"/>\n <xs:simpleType name="TrayModeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Off_0"/>\n   <xs:enumeration value="PreHeat_1"/>\n   <xs:enumeration value="PreCool_2"/>\n   <xs:enumeration value="HoldWarm_3"/>\n   <xs:enumeration value="HoldCool_4"/>\n   <xs:enumeration value="Regenerating_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:TrayModeEnumeration" name="TrayModeEnumeration"/>\n <xs:complexType name="ListOfTrayModeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:TrayModeEnumeration" name="TrayModeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfTrayModeEnumeration" name="ListOfTrayModeEnumeration" nillable="true"/>\n <xs:simpleType name="TrayTypeEnumeration">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Generic_0"/>\n   <xs:enumeration value="HeaterPlate_1"/>\n   <xs:enumeration value="CoolingPlate_2"/>\n   <xs:enumeration value="CombiPlate_3"/>\n   <xs:enumeration value="BainMarie_4"/>\n   <xs:enumeration value="HeaterCabinet_5"/>\n   <xs:enumeration value="CoolingCabinet_6"/>\n   <xs:enumeration value="HeatBridge_7"/>\n   <xs:enumeration value="CombiCabinet_8"/>\n   <xs:enumeration value="RegenCabinet_9"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:TrayTypeEnumeration" name="TrayTypeEnumeration"/>\n <xs:complexType name="ListOfTrayTypeEnumeration">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:TrayTypeEnumeration" name="TrayTypeEnumeration" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfTrayTypeEnumeration" name="ListOfTrayTypeEnumeration" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6020",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[19],
    value=[
        o6.LocalizedText("NoSpecialMode"),
        o6.LocalizedText("Off"),
        o6.LocalizedText("Autostart"),
        o6.LocalizedText("Standby"),
        o6.LocalizedText("PreHeat"),
        o6.LocalizedText("CoolDown"),
        o6.LocalizedText("Working"),
        o6.LocalizedText("Cleaning"),
        o6.LocalizedText("EnergySave"),
        o6.LocalizedText("ServiceMode"),
        o6.LocalizedText("QuickCool"),
        o6.LocalizedText("FlashFreeze"),
        o6.LocalizedText("ProofingInterruption"),
        o6.LocalizedText("ProofingDelay"),
        o6.LocalizedText("Proofing"),
        o6.LocalizedText("Setting"),
        o6.LocalizedText("Defrost"),
        o6.LocalizedText("Baking"),
        o6.LocalizedText("Steaming"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6021",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[10],
    value=[
        o6.LocalizedText("NoSpecialMode"),
        o6.LocalizedText("Baking"),
        o6.LocalizedText("SousVide"),
        o6.LocalizedText("RestStage"),
        o6.LocalizedText("Humidification"),
        o6.LocalizedText("PerfectHold"),
        o6.LocalizedText("InfoStep"),
        o6.LocalizedText("Smoking"),
        o6.LocalizedText("LowTemp-Cooking"),
        o6.LocalizedText("DeltaTSteaming"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6022",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        o6.LocalizedText("Off"),
        o6.LocalizedText("Preheat"),
        o6.LocalizedText("Melting"),
        o6.LocalizedText("Frying"),
        o6.LocalizedText("StandBy"),
        o6.LocalizedText("Filtering"),
        o6.LocalizedText("Error"),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6025",
    browseName="ns=commercial_kitchen;ActualTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6026", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6033",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.FryerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6025"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6023",
    browseName="ns=commercial_kitchen;SetTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6024", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6034",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.FryerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6023"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6027",
    browseName="ns=commercial_kitchen;SetProcessTime",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6028", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6035",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.FryerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6027"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6029",
    browseName="ns=commercial_kitchen;TimeRemaining",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6030", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6036",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.FryerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6029"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6039",
    browseName="ns=commercial_kitchen;ActualTemperature",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6040",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6041", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6043",
    browseName="ns=commercial_kitchen;SetProcessTime",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6044",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6045", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Int32,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6046",
    browseName="ns=commercial_kitchen;SetTemperature",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6047",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6048", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6050",
    browseName="ns=commercial_kitchen;TimeRemaining",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6051",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6052", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Int32,
)
commercial_kitchen_objtypes.FryerParameterType(
    nodeId="ns=commercial_kitchen;i=5005",
    browseName="ns=commercial_kitchen;FryerCup_<No.>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6039"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=commercial_kitchen;i=6042", browseName="ns=commercial_kitchen;ProgramMode", dataType=commercial_kitchen_datypes.FryerModeEnumeration
            )
        ),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6043"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6046"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=commercial_kitchen;i=6049", browseName="ns=commercial_kitchen;SignalMode", dataType=commercial_kitchen_datypes.SignalModeEnumeration
            )
        ),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6050"]),
    ],
)
o6.reference(commercial_kitchen_objtypes.FryerDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=5005"])
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6053",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[9],
    value=[
        o6.LocalizedText("Off"),
        o6.LocalizedText("Preheat"),
        o6.LocalizedText("SoftCook"),
        o6.LocalizedText("Cook"),
        o6.LocalizedText("CookSlow"),
        o6.LocalizedText("Pressure"),
        o6.LocalizedText("KeepWarming"),
        o6.LocalizedText("PresetStart"),
        o6.LocalizedText("Error"),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6064",
    browseName="ns=commercial_kitchen;SetCoreTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6065", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6066",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.FryingPanParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6064"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6067",
    browseName="ns=commercial_kitchen;ActualCoreTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6068", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6073",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.FryingPanParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6067"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6070",
    browseName="ns=commercial_kitchen;ActualPressurePan",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6071", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6074",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5063250, displayName=o6.LocalizedText("mbar"), description=o6.LocalizedText("millibar")
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.FryingPanParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6070"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6058",
    browseName="ns=commercial_kitchen;ActualTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6059", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6075",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.FryingPanParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6058"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6060",
    browseName="ns=commercial_kitchen;SetProcessTime",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6061", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6076",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.FryingPanParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6060"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6056",
    browseName="ns=commercial_kitchen;SetTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6057", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6077",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.FryingPanParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6056"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6062",
    browseName="ns=commercial_kitchen;TimeRemaining",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6063", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6078",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.FryingPanParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6062"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6081",
    browseName="ns=commercial_kitchen;ActualCoreTemperature",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6082",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6083", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6084",
    browseName="ns=commercial_kitchen;ActualTemperature",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6085",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6086", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6089",
    browseName="ns=commercial_kitchen;SetCoreTemperature",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6090",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6091", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6092",
    browseName="ns=commercial_kitchen;SetProcessTime",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6093",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6094", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Int32,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6095",
    browseName="ns=commercial_kitchen;SetTemperature",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6096",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6097", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6099",
    browseName="ns=commercial_kitchen;TimeRemaining",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6100",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6101", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Int32,
)
commercial_kitchen_objtypes.FryingPanParameterType(
    nodeId="ns=commercial_kitchen;i=5006",
    browseName="ns=commercial_kitchen;FryingPan",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6081"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6084"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6087", browseName="ns=commercial_kitchen;CookingLevel", dataType=o6.Int32)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=commercial_kitchen;i=6088", browseName="ns=commercial_kitchen;ProgramMode", dataType=commercial_kitchen_datypes.FryingPanModeEnumeration
            )
        ),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6089"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6092"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6095"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=commercial_kitchen;i=6098", browseName="ns=commercial_kitchen;SignalMode", dataType=commercial_kitchen_datypes.SignalModeEnumeration
            )
        ),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6099"]),
    ],
)
o6.reference(commercial_kitchen_objtypes.FryingPanDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=5006"])
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6102",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[9],
    value=[
        o6.LocalizedText("Off"),
        o6.LocalizedText("Preheat"),
        o6.LocalizedText("SoftCook"),
        o6.LocalizedText("Cook"),
        o6.LocalizedText("CookSlow"),
        o6.LocalizedText("KeepWarming"),
        o6.LocalizedText("Stiring"),
        o6.LocalizedText("PresetStart"),
        o6.LocalizedText("Error"),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6119",
    browseName="ns=commercial_kitchen;ActualExternalCoreTemperature_<No.>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6120", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6134",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.CombiSteamerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6119"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6128",
    browseName="ns=commercial_kitchen;ActualHumidity",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6129", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6135",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.CombiSteamerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6128"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6115",
    browseName="ns=commercial_kitchen;ActualInternalCoreTemperature_<No.>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6116", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6136",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.CombiSteamerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6115"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6107",
    browseName="ns=commercial_kitchen;ActualTemperatureChamber_<No.>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6108", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6137",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.CombiSteamerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6107"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6117",
    browseName="ns=commercial_kitchen;SetExternalCoreTemperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6118", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6138",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.CombiSteamerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6117"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6126",
    browseName="ns=commercial_kitchen;SetHumidity",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6127", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6139",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.CombiSteamerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6126"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6113",
    browseName="ns=commercial_kitchen;SetInternalCoreTemperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6114", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6140",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.CombiSteamerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6113"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6109",
    browseName="ns=commercial_kitchen;SetProcessTimeProgram",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6110", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6141",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.CombiSteamerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6109"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6122",
    browseName="ns=commercial_kitchen;SetProcessTimeStep",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6123", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6142",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.CombiSteamerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6122"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6105",
    browseName="ns=commercial_kitchen;SetTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6106", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6143",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.CombiSteamerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6105"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6111",
    browseName="ns=commercial_kitchen;TimeRemainingProgram",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6112", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6144",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.CombiSteamerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6111"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6124",
    browseName="ns=commercial_kitchen;TimeRemainingStep",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6125", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6145",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.CombiSteamerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6124"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6151",
    browseName="ns=commercial_kitchen;ActualInternalCoreTemperature_<No.>",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6152",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6153", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6154",
    browseName="ns=commercial_kitchen;ActualTemperatureChamber_<No.>",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6155",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6156", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6159",
    browseName="ns=commercial_kitchen;SetProcessTimeProgram",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6160",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6161", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Int32,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6162",
    browseName="ns=commercial_kitchen;SetTemperature",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6163",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6164", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6165",
    browseName="ns=commercial_kitchen;TimeRemainingProgram",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6166",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6167", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Int32,
)
commercial_kitchen_objtypes.CombiSteamerParameterType(
    nodeId="ns=commercial_kitchen;i=5007",
    browseName="ns=commercial_kitchen;CombiSteamer",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6151"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6154"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=commercial_kitchen;i=6157", browseName="ns=commercial_kitchen;CombiSteamerMode", dataType=commercial_kitchen_datypes.CombiSteamerModeEnumeration
            )
        ),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6158", browseName="ns=commercial_kitchen;IsDoorOpen", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6159"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6162"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6165"]),
    ],
)
o6.reference(commercial_kitchen_objtypes.CombiSteamerDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=5007"])
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6168",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[11],
    value=[
        o6.LocalizedText("Off"),
        o6.LocalizedText("On"),
        o6.LocalizedText("Preheat"),
        o6.LocalizedText("StandBy"),
        o6.LocalizedText("Steaming"),
        o6.LocalizedText("CombiSteaming"),
        o6.LocalizedText("HotAir"),
        o6.LocalizedText("Perfection"),
        o6.LocalizedText("Cleaning"),
        o6.LocalizedText("PresetStart"),
        o6.LocalizedText("Error"),
    ],
)
commercial_kitchen_objtypes.ChamberType(
    nodeId="ns=commercial_kitchen;i=5008",
    browseName="ns=commercial_kitchen;Chamber_<No.>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=commercial_kitchen;i=6205", browseName="ns=commercial_kitchen;OperationMode", dataType=commercial_kitchen_datypes.ChamberModeEnumeration
            )
        )
    ],
)
o6.reference(commercial_kitchen_objtypes.OvenDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=5008"])
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6206",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("SignalOff"), o6.LocalizedText("SignalOn"), o6.LocalizedText("SignalAck")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6253",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[10],
    value=[
        o6.LocalizedText("Off"),
        o6.LocalizedText("Preheat"),
        o6.LocalizedText("SoftCook"),
        o6.LocalizedText("Cook"),
        o6.LocalizedText("CookSlow"),
        o6.LocalizedText("Frying"),
        o6.LocalizedText("PressureCooking"),
        o6.LocalizedText("KeepWarming"),
        o6.LocalizedText("PresetStart"),
        o6.LocalizedText("Error"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6254",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("Electric"), o6.LocalizedText("Gas"), o6.LocalizedText("Steam")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6286",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[16],
    value=[
        o6.LocalizedText("Off"),
        o6.LocalizedText("On"),
        o6.LocalizedText("Preheat"),
        o6.LocalizedText("StandBy"),
        o6.LocalizedText("PressureCooking"),
        o6.LocalizedText("SoftCooking"),
        o6.LocalizedText("Cooking"),
        o6.LocalizedText("Grilling"),
        o6.LocalizedText("Frying"),
        o6.LocalizedText("Regenerate"),
        o6.LocalizedText("DeltaTcooking"),
        o6.LocalizedText("ZoneGrilling"),
        o6.LocalizedText("ZoneCooking"),
        o6.LocalizedText("Cleaning"),
        o6.LocalizedText("PresetStart"),
        o6.LocalizedText("Error"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6287",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("LidUpDown"), o6.LocalizedText("PanTilt"), o6.LocalizedText("WaterSupply"), o6.LocalizedText("DrainOnOff")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6337",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        o6.LocalizedText("Off"),
        o6.LocalizedText("Preheat"),
        o6.LocalizedText("SoftCook"),
        o6.LocalizedText("Cook"),
        o6.LocalizedText("CookSlow"),
        o6.LocalizedText("KeepWarming"),
        o6.LocalizedText("PresetStart"),
        o6.LocalizedText("Error"),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6351",
    browseName="ns=commercial_kitchen;ActualTemperature",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6352",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6353", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6356",
    browseName="ns=commercial_kitchen;SetProcessTime",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6357",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6358", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Int32,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6359",
    browseName="ns=commercial_kitchen;SetTemperature",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6360",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6361", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6363",
    browseName="ns=commercial_kitchen;TimeRemaining",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6364",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6365", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Int32,
)
commercial_kitchen_objtypes.PastaCookerParameterType(
    nodeId="ns=commercial_kitchen;i=5012",
    browseName="ns=commercial_kitchen;PastaCooker",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6351"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6354", browseName="ns=commercial_kitchen;CookingLevel", dataType=o6.Int32)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=commercial_kitchen;i=6355", browseName="ns=commercial_kitchen;ProgramMode", dataType=commercial_kitchen_datypes.PastaCookerModeEnumeration
            )
        ),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6356"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6359"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=commercial_kitchen;i=6362", browseName="ns=commercial_kitchen;SignalMode", dataType=commercial_kitchen_datypes.SignalModeEnumeration
            )
        ),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6363"]),
    ],
)
o6.reference(commercial_kitchen_objtypes.PastaCookerDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=5012"])
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6366",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("Inactive"), o6.LocalizedText("Small"), o6.LocalizedText("Large"), o6.LocalizedText("ExtraLarge")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6367",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("Off"), o6.LocalizedText("Standby"), o6.LocalizedText("Error"), o6.LocalizedText("Cleaning")],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6369",
    browseName="ns=commercial_kitchen;BoilerPressureWater",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6370", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6380",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5259596, displayName=o6.LocalizedText("Pa"), description=o6.LocalizedText("pascal")
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.CoffeeMachineParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6369"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6373",
    browseName="ns=commercial_kitchen;BoilerTempSteam",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6374", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6381", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.CoffeeMachineParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6373"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6371",
    browseName="ns=commercial_kitchen;BoilerTempWater",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6372", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6382",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.CoffeeMachineParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6371"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6378",
    browseName="ns=commercial_kitchen;GrinderRuntime_<No.>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6379", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6383",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.UInt64,
)
o6.reference(commercial_kitchen_objtypes.CoffeeMachineParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6378"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=commercial_kitchen;i=6391",
    browseName="ns=commercial_kitchen;Container",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6392", browseName="EnumStrings", dataType=o6.LocalizedText, valueRank=1))],
    dataType=o6.UInt32,
)
o6.reference(commercial_kitchen_objtypes.CoffeeMachineRecipeParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6391"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=commercial_kitchen;i=6393",
    browseName="ns=commercial_kitchen;CoffeeType",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6394", browseName="EnumStrings", dataType=o6.LocalizedText, valueRank=1))],
    dataType=o6.UInt32,
    accessLevel=3,
)
o6.reference(commercial_kitchen_objtypes.CoffeeMachineRecipeParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6393"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=commercial_kitchen;i=6395",
    browseName="ns=commercial_kitchen;RcpType",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6396", browseName="EnumStrings", dataType=o6.LocalizedText, valueRank=1))],
    dataType=o6.UInt32,
    accessLevel=3,
)
o6.reference(commercial_kitchen_objtypes.CoffeeMachineRecipeParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6395"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6384",
    browseName="ns=commercial_kitchen;BeverageSize",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6385", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=50.0, high=150.0))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6403",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
    ],
    dataType=o6.Float,
    accessLevel=3,
)
o6.reference(commercial_kitchen_objtypes.CoffeeMachineRecipeParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6384"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6399",
    browseName="ns=commercial_kitchen;FoamAmount",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6400", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6404",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5065812, displayName=o6.LocalizedText("ml"), description=o6.LocalizedText("millilitre")
                ),
            )
        ),
    ],
    dataType=o6.Float,
    accessLevel=3,
)
o6.reference(commercial_kitchen_objtypes.CoffeeMachineRecipeParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6399"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6387",
    browseName="ns=commercial_kitchen;GroundsAmount",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6388", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6405",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4674125, displayName=o6.LocalizedText("g"), description=o6.LocalizedText("gram")
                ),
            )
        ),
    ],
    dataType=o6.Float,
    accessLevel=3,
)
o6.reference(commercial_kitchen_objtypes.CoffeeMachineRecipeParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6387"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6389",
    browseName="ns=commercial_kitchen;GroundsWater",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6390", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6406",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5065812, displayName=o6.LocalizedText("ml"), description=o6.LocalizedText("millilitre")
                ),
            )
        ),
    ],
    dataType=o6.Float,
    accessLevel=3,
)
o6.reference(commercial_kitchen_objtypes.CoffeeMachineRecipeParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6389"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6397",
    browseName="ns=commercial_kitchen;MilkAmount",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6398", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6407",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5065812, displayName=o6.LocalizedText("ml"), description=o6.LocalizedText("millilitre")
                ),
            )
        ),
    ],
    dataType=o6.Float,
    accessLevel=3,
)
o6.reference(commercial_kitchen_objtypes.CoffeeMachineRecipeParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6397"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6401",
    browseName="ns=commercial_kitchen;PowderAmount",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6402", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6408",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4674125, displayName=o6.LocalizedText("g"), description=o6.LocalizedText("gram")
                ),
            )
        ),
    ],
    dataType=o6.Float,
    accessLevel=3,
)
o6.reference(commercial_kitchen_objtypes.CoffeeMachineRecipeParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6401"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6409",
    browseName="ns=commercial_kitchen;BoilerPressureWater",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6410",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5259596, displayName=o6.LocalizedText("Pa"), description=o6.LocalizedText("pascal")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6411", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6412",
    browseName="ns=commercial_kitchen;BoilerTempWater",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6413",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6414", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6418",
    browseName="ns=commercial_kitchen;BeverageSize",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6419",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6420", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=50.0, high=150.0))
        ),
    ],
    dataType=o6.Float,
    accessLevel=3,
)
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=commercial_kitchen;i=6422",
    browseName="ns=commercial_kitchen;CoffeeType",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6423", browseName="EnumStrings", dataType=o6.LocalizedText, valueRank=1))],
    dataType=o6.UInt32,
    accessLevel=3,
)
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=commercial_kitchen;i=6424",
    browseName="ns=commercial_kitchen;Container",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6425", browseName="EnumStrings", dataType=o6.LocalizedText, valueRank=1))],
    dataType=o6.UInt32,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6426",
    browseName="ns=commercial_kitchen;FoamAmount",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6427",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5065812, displayName=o6.LocalizedText("ml"), description=o6.LocalizedText("millilitre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6428", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6429",
    browseName="ns=commercial_kitchen;GroundsAmount",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6430",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4674125, displayName=o6.LocalizedText("g"), description=o6.LocalizedText("gram")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6431", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6432",
    browseName="ns=commercial_kitchen;GroundsWater",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6433",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5065812, displayName=o6.LocalizedText("ml"), description=o6.LocalizedText("millilitre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6434", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6435",
    browseName="ns=commercial_kitchen;MilkAmount",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6436",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5065812, displayName=o6.LocalizedText("ml"), description=o6.LocalizedText("millilitre")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6437", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
    accessLevel=3,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6438",
    browseName="ns=commercial_kitchen;PowderAmount",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6439",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4674125, displayName=o6.LocalizedText("g"), description=o6.LocalizedText("gram")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6440", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
    accessLevel=3,
)
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=commercial_kitchen;i=6441",
    browseName="ns=commercial_kitchen;RcpType",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6442", browseName="EnumStrings", dataType=o6.LocalizedText, valueRank=1))],
    dataType=o6.UInt32,
    accessLevel=3,
)
commercial_kitchen_objtypes.CoffeeMachineRecipeParameterType(
    nodeId="ns=commercial_kitchen;i=5014",
    browseName="ns=commercial_kitchen;<RecipeName>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6418"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=commercial_kitchen;i=6421", browseName="ns=commercial_kitchen;BeverageSML", dataType=commercial_kitchen_datypes.BeverageSMLEnumeration, accessLevel=3
            )
        ),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6422"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6424"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6426"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6429"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6432"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6435"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6438"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6441"]),
    ],
)
o6.reference(commercial_kitchen_objtypes.CoffeeMachineDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=5014"])
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6443",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[10],
    value=[
        o6.LocalizedText("OperationOFF"),
        o6.LocalizedText("PreWash"),
        o6.LocalizedText("Cleaning1"),
        o6.LocalizedText("WashTimeIncreased"),
        o6.LocalizedText("Cleaning2"),
        o6.LocalizedText("DrainingPause"),
        o6.LocalizedText("Draining"),
        o6.LocalizedText("FinalRinse"),
        o6.LocalizedText("WaitingTime"),
        o6.LocalizedText("HeatRecovery"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6444",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        o6.LocalizedText("HygieneOperationOFF"),
        o6.LocalizedText("HygieneA0"),
        o6.LocalizedText("HygieneHUE"),
        o6.LocalizedText("HygieneMU"),
        o6.LocalizedText("HygieneThermolable"),
        o6.LocalizedText("HygieneA0_TD"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6445",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[16],
    value=[
        o6.LocalizedText("Init"),
        o6.LocalizedText("MachineOff"),
        o6.LocalizedText("Filling"),
        o6.LocalizedText("FillingHeating"),
        o6.LocalizedText("Heating"),
        o6.LocalizedText("EnableOperation"),
        o6.LocalizedText("ReadyForOperation"),
        o6.LocalizedText("Operation"),
        o6.LocalizedText("Cycle_pause"),
        o6.LocalizedText("NotDefined1"),
        o6.LocalizedText("SelfCleaning"),
        o6.LocalizedText("NotDefined2"),
        o6.LocalizedText("RemoteControl"),
        o6.LocalizedText("ControllingOutputs"),
        o6.LocalizedText("NotDefined3"),
        o6.LocalizedText("Error"),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6470",
    browseName="ns=commercial_kitchen;ActualFinalRinseTemperature_<No.>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6471", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6477",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.UInt16,
)
o6.reference(commercial_kitchen_objtypes.DishWashingMachineProgramParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6470"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6464",
    browseName="ns=commercial_kitchen;ActualMainTankTemperature_<No.>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6465", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6478",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.UInt16,
)
o6.reference(commercial_kitchen_objtypes.DishWashingMachineProgramParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6464"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6461",
    browseName="ns=commercial_kitchen;ActualPreTankTemperature_<No.>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6462", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6479",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.UInt16,
)
o6.reference(commercial_kitchen_objtypes.DishWashingMachineProgramParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6461"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6467",
    browseName="ns=commercial_kitchen;ActualPumpedFinalRinseTemperature_<No.>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6468", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6480",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.UInt16,
)
o6.reference(commercial_kitchen_objtypes.DishWashingMachineProgramParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6467"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6458",
    browseName="ns=commercial_kitchen;FinalRinseTemperatureSetpoint_<No.>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6459", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6481",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.UInt16,
)
o6.reference(commercial_kitchen_objtypes.DishWashingMachineProgramParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6458"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6452",
    browseName="ns=commercial_kitchen;MainTankTemperatureSetpoint_<No.>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6453", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6482",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.UInt16,
)
o6.reference(commercial_kitchen_objtypes.DishWashingMachineProgramParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6452"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6449",
    browseName="ns=commercial_kitchen;PreTankTemperatureSetpoint_<No.>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6450", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6483",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.UInt16,
)
o6.reference(commercial_kitchen_objtypes.DishWashingMachineProgramParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6449"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6455",
    browseName="ns=commercial_kitchen;PumpedFinalRinseTemperatureSetpoint_<No.>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6456", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6484",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.UInt16,
)
o6.reference(commercial_kitchen_objtypes.DishWashingMachineProgramParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6455"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6485",
    browseName="ns=commercial_kitchen;ActualFinalRinseTemperature_<No.>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6486",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6487", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.UInt16,
)
commercial_kitchen_objtypes.DishWashingMachineProgramParameterType(
    nodeId="ns=commercial_kitchen;i=5015",
    browseName="ns=commercial_kitchen;Parameters",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6485"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6488", browseName="ns=commercial_kitchen;ActualFinalRinseTemperatureNo", dataType=o6.UInt16)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6489", browseName="ns=commercial_kitchen;ActualMainTankTemperatureNo", dataType=o6.UInt16)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6490", browseName="ns=commercial_kitchen;ActualPreTankTemperatureNo", dataType=o6.UInt16)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6491", browseName="ns=commercial_kitchen;ActualPumpedFinalRinseTemperatureNo", dataType=o6.UInt16)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6492", browseName="ns=commercial_kitchen;FinalRinseTemperatureSetpointNo", dataType=o6.UInt16)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6493", browseName="ns=commercial_kitchen;MainTankTemperatureSetpointNo", dataType=o6.UInt16)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=commercial_kitchen;i=6494", browseName="ns=commercial_kitchen;OperationMode", dataType=commercial_kitchen_datypes.OperationModeEnumeration
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6495", browseName="ns=commercial_kitchen;PreTankTemperatureSetpointNo", dataType=o6.UInt16)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6496", browseName="ns=commercial_kitchen;PumpedFinalRinseTemperatureSetpointNo", dataType=o6.UInt16)
        ),
    ],
)
o6.reference(commercial_kitchen_objtypes.DishWashingMachineDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=5015"])
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6497",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        o6.LocalizedText("Off"),
        o6.LocalizedText("PreHeat"),
        o6.LocalizedText("PreCool"),
        o6.LocalizedText("HoldWarm"),
        o6.LocalizedText("HoldCool"),
        o6.LocalizedText("Regenerating"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6498",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[10],
    value=[
        o6.LocalizedText("Generic"),
        o6.LocalizedText("HeaterPlate"),
        o6.LocalizedText("CoolingPlate"),
        o6.LocalizedText("CombiPlate"),
        o6.LocalizedText("BainMarie"),
        o6.LocalizedText("HeaterCabinet"),
        o6.LocalizedText("CoolingCabinet"),
        o6.LocalizedText("HeatBridge"),
        o6.LocalizedText("CombiCabinet"),
        o6.LocalizedText("RegenCabinet"),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6506",
    browseName="ns=commercial_kitchen;ActiveSince",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6507", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6510",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.TrayType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6506"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6500",
    browseName="ns=commercial_kitchen;ActualTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6501", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6511",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.TrayType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6500"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6508",
    browseName="ns=commercial_kitchen;OperatingCounter",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6509", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6512",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.TrayType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6508"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6502",
    browseName="ns=commercial_kitchen;SetTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6503", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6513",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
    accessLevel=3,
)
o6.reference(commercial_kitchen_objtypes.TrayType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6502"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6514",
    browseName="ns=commercial_kitchen;ActiveSince",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6515",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6516", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Int32,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6517",
    browseName="ns=commercial_kitchen;ActualTemperature",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6518",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6519", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6521",
    browseName="ns=commercial_kitchen;OperatingCounter",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6522",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6523", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Int32,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6525",
    browseName="ns=commercial_kitchen;SetTemperature",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6526",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6527", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
    accessLevel=3,
)
commercial_kitchen_objtypes.TrayType(
    nodeId="ns=commercial_kitchen;i=5016",
    browseName="ns=commercial_kitchen;Tray_<No.>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6520", browseName="ns=commercial_kitchen;Name", dataType=o6.String, accessLevel=3)),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6514"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6517"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6521"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=commercial_kitchen;i=6524", browseName="ns=commercial_kitchen;ProgramMode", dataType=commercial_kitchen_datypes.TrayModeEnumeration, accessLevel=3
            )
        ),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6525"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=commercial_kitchen;i=6528", browseName="ns=commercial_kitchen;Type", dataType=commercial_kitchen_datypes.TrayTypeEnumeration
            )
        ),
    ],
)
o6.reference(commercial_kitchen_objtypes.ServeryCounterDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=5016"])
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6529",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("Off"), o6.LocalizedText("Standby"), o6.LocalizedText("Power"), o6.LocalizedText("PotDetection")],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6540",
    browseName="ns=commercial_kitchen;ActualPower",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6541", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6545", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.CookingZoneParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6540"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6536",
    browseName="ns=commercial_kitchen;ActualProcessTime",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6537", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6546",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.CookingZoneParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6536"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6532",
    browseName="ns=commercial_kitchen;ActualTemperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6533", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6547",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.CookingZoneParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6532"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6543",
    browseName="ns=commercial_kitchen;NominalPower",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6544", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6548",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.CookingZoneParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6543"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6538",
    browseName="ns=commercial_kitchen;SetPowerValue",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6539", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=100.0))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6549",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.CookingZoneParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6538"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6534",
    browseName="ns=commercial_kitchen;SetTemperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6535", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6550",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.CookingZoneParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6534"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6553",
    browseName="ns=commercial_kitchen;NominalVoltage",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6554", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6556",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5655636, displayName=o6.LocalizedText("V"), description=o6.LocalizedText("volt")
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.CookingZoneDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6553"])
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6557",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("Home"), o6.LocalizedText("Cooking"), o6.LocalizedText("Idle"), o6.LocalizedText("Open")],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6560",
    browseName="ns=commercial_kitchen;ActualGrillTemperature_<No.>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6561", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6574",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.FryingAndGrillingParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6560"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6564",
    browseName="ns=commercial_kitchen;ActualPlatenTemperature_<No.>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6565", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6575",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.FryingAndGrillingParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6564"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6570",
    browseName="ns=commercial_kitchen;RemainingProcessTime",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6571", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6576",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.FryingAndGrillingParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6570"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6562",
    browseName="ns=commercial_kitchen;SetGrillTemperature_<No.>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6563", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6577",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.FryingAndGrillingParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6562"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6566",
    browseName="ns=commercial_kitchen;SetPlatenTemperature_<No.>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6567", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6578",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.FryingAndGrillingParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6566"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6568",
    browseName="ns=commercial_kitchen;SetProcessTime",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6569", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6579",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.FryingAndGrillingParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6568"])
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6581",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[9],
    value=[
        o6.LocalizedText("Preheat"),
        o6.LocalizedText("CoolDown"),
        o6.LocalizedText("Process"),
        o6.LocalizedText("PowerSaving"),
        o6.LocalizedText("Standby"),
        o6.LocalizedText("Service"),
        o6.LocalizedText("Cleaning"),
        o6.LocalizedText("Off"),
        o6.LocalizedText("Error"),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6582",
    browseName="ns=commercial_kitchen;ActualTemperatureChamber",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6583", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6599",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.MicrowaveCombiOvenParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6582"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6593",
    browseName="ns=commercial_kitchen;FanSpeed",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6594", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=100.0))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6600",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.MicrowaveCombiOvenParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6593"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6595",
    browseName="ns=commercial_kitchen;MicrowaveEnergy",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6596", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=100.0))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6601",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.MicrowaveCombiOvenParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6595"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6588",
    browseName="ns=commercial_kitchen;RemainingProcessTime",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6589", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6602",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.MicrowaveCombiOvenParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6588"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6590",
    browseName="ns=commercial_kitchen;RemainingProcessTimeStep",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6591", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6603",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.MicrowaveCombiOvenParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6590"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6586",
    browseName="ns=commercial_kitchen;SetProcessTime",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6587", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6604",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.MicrowaveCombiOvenParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6586"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6584",
    browseName="ns=commercial_kitchen;SetTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6585", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6605",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.MicrowaveCombiOvenParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6584"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6606",
    browseName="ns=commercial_kitchen;ActualTemperatureChamber",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6607",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6608", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6611",
    browseName="ns=commercial_kitchen;RemainingProcessTime",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6612",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6613", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Int32,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6614",
    browseName="ns=commercial_kitchen;SetProcessTime",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6615",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6616", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Int32,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6617",
    browseName="ns=commercial_kitchen;SetTemperature",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6618",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6619", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Float,
)
commercial_kitchen_objtypes.MicrowaveCombiOvenParameterType(
    nodeId="ns=commercial_kitchen;i=5019",
    browseName="ns=commercial_kitchen;MicrowaveCombiOven",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6606"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6609", browseName="ns=commercial_kitchen;IsDoorOpen", dataType=o6.Boolean, accessLevel=3)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=commercial_kitchen;i=6610", browseName="ns=commercial_kitchen;OperatingMode", dataType=commercial_kitchen_datypes.OperatingModeEnumeration
            )
        ),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6611"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6614"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6617"]),
    ],
)
o6.reference(commercial_kitchen_objtypes.MicrowaveCombiOvenDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=5019"])
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6620",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[19],
    value=[
        o6.LocalizedText("INIT"),
        o6.LocalizedText("WATER_PURGE"),
        o6.LocalizedText("PRE_CHILL"),
        o6.LocalizedText("FREEZE"),
        o6.LocalizedText("HARVEST"),
        o6.LocalizedText("BIN_FULL"),
        o6.LocalizedText("CLEAN"),
        o6.LocalizedText("OFF"),
        o6.LocalizedText("SLEEP_MODE"),
        o6.LocalizedText("STANDBY"),
        o6.LocalizedText("SAFE_MODE"),
        o6.LocalizedText("WATER_OUTAGE"),
        o6.LocalizedText("HPCO_DELAY_ACTIVE"),
        o6.LocalizedText("CURTAIN_OPEN"),
        o6.LocalizedText("PRODUCTION_TEST"),
        o6.LocalizedText("SAFE_MODE_PRECHILL"),
        o6.LocalizedText("SAFE_MODE_FREEZE"),
        o6.LocalizedText("SAFE_MODE_HARVEST"),
        o6.LocalizedText("SAFE_MODE_FULL_BIN"),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6622",
    browseName="ns=commercial_kitchen;LastFreezeTime",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6623", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6630",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.IceMachineParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6622"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6624",
    browseName="ns=commercial_kitchen;LastHarvestTime",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6625", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6631",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.IceMachineParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6624"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6628",
    browseName="ns=commercial_kitchen;Temperature_<No.>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6629", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6632",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.IceMachineParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6628"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6626",
    browseName="ns=commercial_kitchen;WaterFillTime",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6627", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6633",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.IceMachineParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6626"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6342",
    browseName="ns=commercial_kitchen;ActualTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6343", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6634",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.PastaCookerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6342"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6344",
    browseName="ns=commercial_kitchen;SetProcessTime",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6345", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6635",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.PastaCookerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6344"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6340",
    browseName="ns=commercial_kitchen;SetTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6341", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6636",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.PastaCookerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6340"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6346",
    browseName="ns=commercial_kitchen;TimeRemaining",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6347", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6637",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.PastaCookerParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6346"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6303",
    browseName="ns=commercial_kitchen;ActualCoreTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6304", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6638",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.MultiFunctionPanParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6303"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6322",
    browseName="ns=commercial_kitchen;ActualCoreTemperature",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6323", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6639",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6305",
    browseName="ns=commercial_kitchen;ActualPressureAbsolute",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6306", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6640",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5063250, displayName=o6.LocalizedText("mbar"), description=o6.LocalizedText("millibar")
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.MultiFunctionPanParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6305"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6293",
    browseName="ns=commercial_kitchen;ActualTemperatureBottom",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6294", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6641",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.MultiFunctionPanParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6293"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6324",
    browseName="ns=commercial_kitchen;ActualTemperatureBottom",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6325", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6642",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6295",
    browseName="ns=commercial_kitchen;ActualTemperatureCup",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6296", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6643",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.MultiFunctionPanParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6295"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6326",
    browseName="ns=commercial_kitchen;ActualTemperatureCup",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6327", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6644",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6313",
    browseName="ns=commercial_kitchen;ActualZoneTemperature_<No.>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6314", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6645", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.MultiFunctionPanParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6313"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6301",
    browseName="ns=commercial_kitchen;SetCoreTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6302", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6646",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.MultiFunctionPanParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6301"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6329",
    browseName="ns=commercial_kitchen;SetCoreTemperature",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6330", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6647",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6297",
    browseName="ns=commercial_kitchen;SetProcessTimeProgram",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6298", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6648",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.MultiFunctionPanParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6297"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6331",
    browseName="ns=commercial_kitchen;SetProcessTimeProgram",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6332", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6649",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6307",
    browseName="ns=commercial_kitchen;SetProcessTimeStep",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6308", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6650",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.MultiFunctionPanParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6307"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6291",
    browseName="ns=commercial_kitchen;SetTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6292", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6651",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.MultiFunctionPanParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6291"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6333",
    browseName="ns=commercial_kitchen;SetTemperature",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6334", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6652",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6311",
    browseName="ns=commercial_kitchen;SetZoneTemperature_<No.>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6312", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6653",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.MultiFunctionPanParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6311"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6299",
    browseName="ns=commercial_kitchen;TimeRemainingProgram",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6300", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6654",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.MultiFunctionPanParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6299"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6335",
    browseName="ns=commercial_kitchen;TimeRemainingProgram",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6336", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6655",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
commercial_kitchen_objtypes.MultiFunctionPanParameterType(
    nodeId="ns=commercial_kitchen;i=5011",
    browseName="ns=commercial_kitchen;MultiFunctionPan_<No.>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6322"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6324"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6326"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=commercial_kitchen;i=6328", browseName="ns=commercial_kitchen;MultiFunctionPanMode", dataType=commercial_kitchen_datypes.MultiFunctionPanModeEnumeration
            )
        ),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6329"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6331"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6333"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6335"]),
    ],
)
o6.reference(commercial_kitchen_objtypes.MultiFunctionPanDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=5011"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6309",
    browseName="ns=commercial_kitchen;TimeRemainingStep",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6310", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6656",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.MultiFunctionPanParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6309"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6265",
    browseName="ns=commercial_kitchen;ActualCoreTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6266", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6657",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.CookingKettleParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6265"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6271",
    browseName="ns=commercial_kitchen;ActualCoreTemperature",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6272", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6658",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6257",
    browseName="ns=commercial_kitchen;ActualTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6258", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6660",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.CookingKettleParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6257"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6273",
    browseName="ns=commercial_kitchen;ActualTemperature",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6274", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6661",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6659",
    browseName="ns=commercial_kitchen;BoilerPressureSteam",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6662", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.CoffeeMachineParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6659"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6263",
    browseName="ns=commercial_kitchen;SetCoreTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6264", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6663",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.CookingKettleParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6263"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6277",
    browseName="ns=commercial_kitchen;SetCoreTemperature",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6278", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6664",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6259",
    browseName="ns=commercial_kitchen;SetProcessTime",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6260", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6666",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.CookingKettleParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6259"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6279",
    browseName="ns=commercial_kitchen;SetProcessTime",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6280", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6667",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6665",
    browseName="ns=commercial_kitchen;BoilerPressureSteam",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6668", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Float,
)
commercial_kitchen_objtypes.CoffeeMachineParameterType(
    nodeId="ns=commercial_kitchen;i=5013",
    browseName="ns=commercial_kitchen;Parameters",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6409"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6412"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=commercial_kitchen;i=6415",
                browseName="ns=commercial_kitchen;CurrentState",
                dataType=commercial_kitchen_datypes.CoffeeMachineModeEnumeration,
                accessLevel=3,
            )
        ),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6416", browseName="ns=commercial_kitchen;SystemClean", dataType=o6.DateTime)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6417", browseName="ns=commercial_kitchen;TotalMix", dataType=o6.UInt64)),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6665"]),
    ],
)
o6.reference(commercial_kitchen_objtypes.CoffeeMachineDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=5013"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6255",
    browseName="ns=commercial_kitchen;SetTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6256", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6669",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.CookingKettleParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6255"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6281",
    browseName="ns=commercial_kitchen;SetTemperature",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6282", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6670",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
commercial_kitchen_objtypes.BatchInformationType(
    nodeId="ns=commercial_kitchen;i=5001",
    browseName="ns=commercial_kitchen;BatchInformation",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6017", browseName="ns=commercial_kitchen;BatchId", dataType=o6.String, accessLevel=3)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6018", browseName="ns=commercial_kitchen;LocalTime", dataType=ns0.datatypes.TimeZoneDataType, accessLevel=3)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6019", browseName="ns=commercial_kitchen;OrderId", dataType=o6.String, accessLevel=3)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6671", browseName="ns=commercial_kitchen;SystemTime", dataType=ns0.datatypes.UtcTime, accessLevel=3)
        ),
    ],
)
o6.reference(commercial_kitchen_objtypes.CommercialKitchenDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=5001"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6261",
    browseName="ns=commercial_kitchen;TimeRemaining",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6262", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6672",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.CookingKettleParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6261"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6284",
    browseName="ns=commercial_kitchen;TimeRemaining",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6285", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6673",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
commercial_kitchen_objtypes.CookingKettleParameterType(
    nodeId="ns=commercial_kitchen;i=5010",
    browseName="ns=commercial_kitchen;CookingKettle",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6271"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6273"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6275", browseName="ns=commercial_kitchen;CookingLevel", dataType=o6.Int32)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=commercial_kitchen;i=6276", browseName="ns=commercial_kitchen;ProgramMode", dataType=commercial_kitchen_datypes.CookingKettleModeEnumeration
            )
        ),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6277"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6279"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6281"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=commercial_kitchen;i=6283", browseName="ns=commercial_kitchen;SignalMode", dataType=commercial_kitchen_datypes.SignalModeEnumeration
            )
        ),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6284"]),
    ],
)
o6.reference(commercial_kitchen_objtypes.CookingKettleDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=5010"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6219",
    browseName="ns=commercial_kitchen;ActualCoreTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6220", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6675",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.PressureCookingKettleParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6219"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6230",
    browseName="ns=commercial_kitchen;ActualCoreTemperature",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6231", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6676",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6221",
    browseName="ns=commercial_kitchen;ActualPressureAbsolute",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6222", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6677",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5063250, displayName=o6.LocalizedText("mbar"), description=o6.LocalizedText("millibar")
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.PressureCookingKettleParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6221"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6232",
    browseName="ns=commercial_kitchen;ActualPressureAbsolute",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6233", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6678",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5063250, displayName=o6.LocalizedText("mbar"), description=o6.LocalizedText("millibar")
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6223",
    browseName="ns=commercial_kitchen;ActualPressureKettle",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6224", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6679",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5063250, displayName=o6.LocalizedText("mbar"), description=o6.LocalizedText("millibar")
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.PressureCookingKettleParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6223"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6234",
    browseName="ns=commercial_kitchen;ActualPressureKettle",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6235", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6680",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5063250, displayName=o6.LocalizedText("mbar"), description=o6.LocalizedText("millibar")
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6211",
    browseName="ns=commercial_kitchen;ActualTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6212", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6681",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.PressureCookingKettleParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6211"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6236",
    browseName="ns=commercial_kitchen;ActualTemperature",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6237", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6682",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6217",
    browseName="ns=commercial_kitchen;SetCoreTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6218", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6683",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.PressureCookingKettleParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6217"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6243",
    browseName="ns=commercial_kitchen;SetCoreTemperature",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6244", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6684",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6213",
    browseName="ns=commercial_kitchen;SetProcessTime",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6214", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6685",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.PressureCookingKettleParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6213"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6245",
    browseName="ns=commercial_kitchen;SetProcessTime",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6246", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6686",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6209",
    browseName="ns=commercial_kitchen;SetTemperature",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6210", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6687",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.PressureCookingKettleParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6209"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6247",
    browseName="ns=commercial_kitchen;SetTemperature",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6248", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6688",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6215",
    browseName="ns=commercial_kitchen;TimeRemaining",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6216", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6689",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.PressureCookingKettleParameterType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6215"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6250",
    browseName="ns=commercial_kitchen;TimeRemaining",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6251", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6690",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
commercial_kitchen_objtypes.PressureCookingKettleParameterType(
    nodeId="ns=commercial_kitchen;i=5009",
    browseName="ns=commercial_kitchen;PressureCookingKettle",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6230"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6232"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6234"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6236"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6238", browseName="ns=commercial_kitchen;CookingLevel", dataType=o6.Int32)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6239", browseName="ns=commercial_kitchen;IsLidLocked", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6240", browseName="ns=commercial_kitchen;IsOpenExpressActive", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6241", browseName="ns=commercial_kitchen;IsSteamActive", dataType=o6.Boolean)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=commercial_kitchen;i=6242", browseName="ns=commercial_kitchen;ProgramMode", dataType=commercial_kitchen_datypes.PressureCookingKettleModeEnumeration
            )
        ),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6243"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6245"]),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6247"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=commercial_kitchen;i=6249", browseName="ns=commercial_kitchen;SignalMode", dataType=commercial_kitchen_datypes.SignalModeEnumeration
            )
        ),
        o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6250"]),
    ],
)
o6.reference(commercial_kitchen_objtypes.PressureCookingKettleDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=5009"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6192",
    browseName="ns=commercial_kitchen;ActualBoilerTemperature_<No.>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6193", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6691",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6192"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6188",
    browseName="ns=commercial_kitchen;ActualBottomTemperature_<No.>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6189", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6692",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6188"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6182",
    browseName="ns=commercial_kitchen;ActualChamberTemperature_<No.>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6183", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6693",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6182"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6190",
    browseName="ns=commercial_kitchen;ActualCoreTemperature_<No.>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6191", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6694",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6190"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6201",
    browseName="ns=commercial_kitchen;ActualFanSpeed_<No.>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6202", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6695",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6201"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6196",
    browseName="ns=commercial_kitchen;ActualHumidity_<No.>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6197", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6696",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6196"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6186",
    browseName="ns=commercial_kitchen;ActualTopTemperature_<No.>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6187", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6697",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6186"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6180",
    browseName="ns=commercial_kitchen;SetBoilerTemperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6181", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6698",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6180"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6176",
    browseName="ns=commercial_kitchen;SetBottomTemperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6177", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6699",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6176"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6172",
    browseName="ns=commercial_kitchen;SetChamberTemperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6173", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6700",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6172"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6178",
    browseName="ns=commercial_kitchen;SetCoreTemperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6179", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6701",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6178"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6203",
    browseName="ns=commercial_kitchen;SetFanSpeed",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6204", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6702",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6203"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6194",
    browseName="ns=commercial_kitchen;SetHumidity",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6195", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6703",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6194"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6184",
    browseName="ns=commercial_kitchen;SetProcessTimeProgram",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6185", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6704",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6184"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6174",
    browseName="ns=commercial_kitchen;SetTopTemperature",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6175", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6705",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=4408652,
                    displayName=o6.LocalizedText(";C"),
                    description=o6.LocalizedText("degree Celsius"),
                ),
            )
        ),
    ],
    dataType=o6.Float,
)
o6.reference(commercial_kitchen_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6174"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6170",
    browseName="ns=commercial_kitchen;TimeRemaining",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6171", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6706",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact",
                    unitId=5457219,
                    displayName=o6.LocalizedText("s"),
                    description=o6.LocalizedText("second [unit of time]"),
                ),
            )
        ),
    ],
    dataType=o6.Int32,
)
o6.reference(commercial_kitchen_objtypes.ChamberType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=6170"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashCommercialKitchenEquipmentSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=commercial_kitchen;i=5021",
    browseName="ns=commercial_kitchen;http://opcfoundation.org/UA/CommercialKitchenEquipment/",
    description="Provides the metadata for a namespace used by the server.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6707",
                browseName="IsNamespaceSubset",
                description="If TRUE then the server only supports a subset of the namespace.",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6708",
                browseName="NamespacePublicationDate",
                description="The publication date for the namespace.",
                dataType=o6.DateTime,
                value=o6.DateTime("2019-07-12T00:00:00Z"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6709",
                browseName="NamespaceUri",
                description="The URI of the namespace.",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/CommercialKitchenEquipment/",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6710",
                browseName="NamespaceVersion",
                description="The human readable string representing version of the namespace.",
                dataType=o6.String,
                value="1.0",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6711",
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
                nodeId="ns=commercial_kitchen;i=6712",
                browseName="StaticNumericNodeIdRange",
                description="A list of ranges for numeric node ids which are the same in every server that exposes them.",
                dataType=ns0.datatypes.NumericRange,
                valueRank=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6713",
                browseName="StaticStringNodeIdPattern",
                description="A regular expression which matches string node ids are the same in every server that exposes them.",
                dataType=o6.String,
            )
        ),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=commercial_kitchen;i=6674",
    browseName="ns=commercial_kitchen;NominalPower",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=commercial_kitchen;i=6714",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=5723220, displayName=o6.LocalizedText("W"), description=o6.LocalizedText("watt")
                ),
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=commercial_kitchen;i=6715", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Int32,
)
commercial_kitchen_objtypes.CookingZoneParameterType(
    nodeId="ns=commercial_kitchen;i=5017",
    browseName="ns=commercial_kitchen;CookingZone_<No.>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=commercial_kitchen;i=6674"])],
)
o6.reference(commercial_kitchen_objtypes.CookingZoneDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=5017"])
commercial_kitchen_objtypes.FryingAndGrillingParameterType(
    nodeId="ns=commercial_kitchen;i=5018",
    browseName="ns=commercial_kitchen;GrillingZone_<No.>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=commercial_kitchen;i=6716", browseName="ns=commercial_kitchen;IsWithPlaten", dataType=o6.Boolean))],
)
o6.reference(commercial_kitchen_objtypes.FryingAndGrillingDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=commercial_kitchen;i=5018"])
ns0.vartypes.PropertyType(
    nodeId="ns=commercial_kitchen;i=6717",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=commercial_kitchen;i=3025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("Off"), o6.LocalizedText("Standby"), o6.LocalizedText("Idle"), o6.LocalizedText("Grilling")],
)


del Any, TYPE_CHECKING, uuid, o6, di, ns0, commercial_kitchen_datypes, commercial_kitchen_objtypes
