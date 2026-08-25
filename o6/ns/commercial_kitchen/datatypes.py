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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3002", browseName="EnergySourceEnumeration")
class EnergySourceEnumeration(ns0.datatypes.Enumeration):
    ELECTRIC = o6.enumfield(0, name="Electric")
    GAS = o6.enumfield(1, name="Gas")
    STEAM = o6.enumfield(2, name="Steam")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3003", browseName="FryerModeEnumeration")
class FryerModeEnumeration(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="Off")
    PREHEAT = o6.enumfield(1, name="Preheat")
    MELTING = o6.enumfield(2, name="Melting")
    FRYING = o6.enumfield(3, name="Frying")
    STAND_BY = o6.enumfield(4, name="StandBy")
    FILTERING = o6.enumfield(5, name="Filtering")
    ERROR = o6.enumfield(6, name="Error")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3004", browseName="SignalModeEnumeration")
class SignalModeEnumeration(ns0.datatypes.Enumeration):
    SIGNAL_OFF = o6.enumfield(0, name="SignalOff")
    SIGNAL_ON = o6.enumfield(1, name="SignalOn")
    SIGNAL_ACK = o6.enumfield(2, name="SignalAck")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3005", browseName="FryingPanModeEnumeration")
class FryingPanModeEnumeration(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="Off")
    PREHEAT = o6.enumfield(1, name="Preheat")
    SOFT_COOK = o6.enumfield(2, name="SoftCook")
    COOK = o6.enumfield(3, name="Cook")
    COOK_SLOW = o6.enumfield(4, name="CookSlow")
    FRYING = o6.enumfield(5, name="Frying")
    PRESSURE_COOKING = o6.enumfield(6, name="PressureCooking")
    KEEP_WARMING = o6.enumfield(7, name="KeepWarming")
    PRESET_START = o6.enumfield(8, name="PresetStart")
    ERROR = o6.enumfield(9, name="Error")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3006", browseName="CombiSteamerModeEnumeration")
class CombiSteamerModeEnumeration(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="Off")
    ON = o6.enumfield(1, name="On")
    PREHEAT = o6.enumfield(2, name="Preheat")
    STAND_BY = o6.enumfield(3, name="StandBy")
    STEAMING = o6.enumfield(4, name="Steaming")
    COMBI_STEAMING = o6.enumfield(5, name="CombiSteaming")
    HOT_AIR = o6.enumfield(6, name="HotAir")
    PERFECTION = o6.enumfield(7, name="Perfection")
    CLEANING = o6.enumfield(8, name="Cleaning")
    PRESET_START = o6.enumfield(9, name="PresetStart")
    ERROR = o6.enumfield(10, name="Error")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3007", browseName="SpecialCookingModeEnumeration")
class SpecialCookingModeEnumeration(ns0.datatypes.Enumeration):
    NO_SPECIAL_MODE = o6.enumfield(0, name="NoSpecialMode")
    BAKING = o6.enumfield(1, name="Baking")
    SOUS_VIDE = o6.enumfield(2, name="SousVide")
    REST_STAGE = o6.enumfield(3, name="RestStage")
    HUMIDIFICATION = o6.enumfield(4, name="Humidification")
    PERFECT_HOLD = o6.enumfield(5, name="PerfectHold")
    INFO_STEP = o6.enumfield(6, name="InfoStep")
    SMOKING = o6.enumfield(7, name="Smoking")
    LOW_TEMP__COOKING = o6.enumfield(8, name="LowTemp-Cooking")
    DELTA_T_STEAMING = o6.enumfield(9, name="DeltaTSteaming")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3008", browseName="ChamberModeEnumeration")
class ChamberModeEnumeration(ns0.datatypes.Enumeration):
    NO_SPECIAL_MODE = o6.enumfield(0, name="NoSpecialMode")
    OFF = o6.enumfield(1, name="Off")
    AUTOSTART = o6.enumfield(2, name="Autostart")
    STANDBY = o6.enumfield(3, name="Standby")
    PRE_HEAT = o6.enumfield(4, name="PreHeat")
    COOL_DOWN = o6.enumfield(5, name="CoolDown")
    WORKING = o6.enumfield(6, name="Working")
    CLEANING = o6.enumfield(7, name="Cleaning")
    ENERGY_SAVE = o6.enumfield(8, name="EnergySave")
    SERVICE_MODE = o6.enumfield(9, name="ServiceMode")
    QUICK_COOL = o6.enumfield(10, name="QuickCool")
    FLASH_FREEZE = o6.enumfield(11, name="FlashFreeze")
    PROOFING_INTERRUPTION = o6.enumfield(12, name="ProofingInterruption")
    PROOFING_DELAY = o6.enumfield(13, name="ProofingDelay")
    PROOFING = o6.enumfield(14, name="Proofing")
    SETTING = o6.enumfield(15, name="Setting")
    DEFROST = o6.enumfield(16, name="Defrost")
    BAKING = o6.enumfield(17, name="Baking")
    STEAMING = o6.enumfield(18, name="Steaming")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3009", browseName="PressureCookingKettleModeEnumeration")
class PressureCookingKettleModeEnumeration(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="Off")
    PREHEAT = o6.enumfield(1, name="Preheat")
    SOFT_COOK = o6.enumfield(2, name="SoftCook")
    COOK = o6.enumfield(3, name="Cook")
    COOK_SLOW = o6.enumfield(4, name="CookSlow")
    PRESSURE = o6.enumfield(5, name="Pressure")
    KEEP_WARMING = o6.enumfield(6, name="KeepWarming")
    PRESET_START = o6.enumfield(7, name="PresetStart")
    ERROR = o6.enumfield(8, name="Error")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3010", browseName="CookingKettleModeEnumeration")
class CookingKettleModeEnumeration(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="Off")
    PREHEAT = o6.enumfield(1, name="Preheat")
    SOFT_COOK = o6.enumfield(2, name="SoftCook")
    COOK = o6.enumfield(3, name="Cook")
    COOK_SLOW = o6.enumfield(4, name="CookSlow")
    KEEP_WARMING = o6.enumfield(5, name="KeepWarming")
    STIRING = o6.enumfield(6, name="Stiring")
    PRESET_START = o6.enumfield(7, name="PresetStart")
    ERROR = o6.enumfield(8, name="Error")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3011", browseName="MultiFunctionPanModeEnumeration")
class MultiFunctionPanModeEnumeration(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="Off")
    ON = o6.enumfield(1, name="On")
    PREHEAT = o6.enumfield(2, name="Preheat")
    STAND_BY = o6.enumfield(3, name="StandBy")
    PRESSURE_COOKING = o6.enumfield(4, name="PressureCooking")
    SOFT_COOKING = o6.enumfield(5, name="SoftCooking")
    COOKING = o6.enumfield(6, name="Cooking")
    GRILLING = o6.enumfield(7, name="Grilling")
    FRYING = o6.enumfield(8, name="Frying")
    REGENERATE = o6.enumfield(9, name="Regenerate")
    DELTA_TCOOKING = o6.enumfield(10, name="DeltaTcooking")
    ZONE_GRILLING = o6.enumfield(11, name="ZoneGrilling")
    ZONE_COOKING = o6.enumfield(12, name="ZoneCooking")
    CLEANING = o6.enumfield(13, name="Cleaning")
    PRESET_START = o6.enumfield(14, name="PresetStart")
    ERROR = o6.enumfield(15, name="Error")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3012", browseName="SpecialFunctionModeEnumeration")
class SpecialFunctionModeEnumeration(ns0.datatypes.Enumeration):
    LID_UP_DOWN = o6.enumfield(0, name="LidUpDown")
    PAN_TILT = o6.enumfield(1, name="PanTilt")
    WATER_SUPPLY = o6.enumfield(2, name="WaterSupply")
    DRAIN_ON_OFF = o6.enumfield(3, name="DrainOnOff")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3013", browseName="PastaCookerModeEnumeration")
class PastaCookerModeEnumeration(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="Off")
    PREHEAT = o6.enumfield(1, name="Preheat")
    SOFT_COOK = o6.enumfield(2, name="SoftCook")
    COOK = o6.enumfield(3, name="Cook")
    COOK_SLOW = o6.enumfield(4, name="CookSlow")
    KEEP_WARMING = o6.enumfield(5, name="KeepWarming")
    PRESET_START = o6.enumfield(6, name="PresetStart")
    ERROR = o6.enumfield(7, name="Error")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3014", browseName="BeverageSMLEnumeration")
class BeverageSMLEnumeration(ns0.datatypes.Enumeration):
    INACTIVE = o6.enumfield(0, name="Inactive")
    SMALL = o6.enumfield(1, name="Small")
    LARGE = o6.enumfield(2, name="Large")
    EXTRA_LARGE = o6.enumfield(3, name="ExtraLarge")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3015", browseName="CoffeeMachineModeEnumeration")
class CoffeeMachineModeEnumeration(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="Off")
    STANDBY = o6.enumfield(1, name="Standby")
    ERROR = o6.enumfield(2, name="Error")
    CLEANING = o6.enumfield(3, name="Cleaning")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3016", browseName="ProgramModeEnumeration")
class ProgramModeEnumeration(ns0.datatypes.Enumeration):
    OPERATION_OFF = o6.enumfield(0, name="OperationOFF")
    PRE_WASH = o6.enumfield(1, name="PreWash")
    CLEANING1 = o6.enumfield(2, name="Cleaning1")
    WASH_TIME_INCREASED = o6.enumfield(3, name="WashTimeIncreased")
    CLEANING2 = o6.enumfield(4, name="Cleaning2")
    DRAINING_PAUSE = o6.enumfield(5, name="DrainingPause")
    DRAINING = o6.enumfield(6, name="Draining")
    FINAL_RINSE = o6.enumfield(7, name="FinalRinse")
    WAITING_TIME = o6.enumfield(8, name="WaitingTime")
    HEAT_RECOVERY = o6.enumfield(9, name="HeatRecovery")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3017", browseName="HygieneModeEnumeration")
class HygieneModeEnumeration(ns0.datatypes.Enumeration):
    HYGIENE_OPERATION_OFF = o6.enumfield(0, name="HygieneOperationOFF")
    HYGIENE_A0 = o6.enumfield(1, name="HygieneA0")
    HYGIENE_HUE = o6.enumfield(2, name="HygieneHUE")
    HYGIENE_MU = o6.enumfield(3, name="HygieneMU")
    HYGIENE_THERMOLABLE = o6.enumfield(4, name="HygieneThermolable")
    HYGIENE_A0_TD = o6.enumfield(5, name="HygieneA0_TD")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3018", browseName="OperationModeEnumeration")
class OperationModeEnumeration(ns0.datatypes.Enumeration):
    INIT = o6.enumfield(0, name="Init")
    MACHINE_OFF = o6.enumfield(1, name="MachineOff")
    FILLING = o6.enumfield(2, name="Filling")
    FILLING_HEATING = o6.enumfield(3, name="FillingHeating")
    HEATING = o6.enumfield(4, name="Heating")
    ENABLE_OPERATION = o6.enumfield(5, name="EnableOperation")
    READY_FOR_OPERATION = o6.enumfield(6, name="ReadyForOperation")
    OPERATION = o6.enumfield(7, name="Operation")
    CYCLE_PAUSE = o6.enumfield(8, name="Cycle_pause")
    NOT_DEFINED1 = o6.enumfield(9, name="NotDefined1")
    SELF_CLEANING = o6.enumfield(10, name="SelfCleaning")
    NOT_DEFINED2 = o6.enumfield(11, name="NotDefined2")
    REMOTE_CONTROL = o6.enumfield(12, name="RemoteControl")
    CONTROLLING_OUTPUTS = o6.enumfield(13, name="ControllingOutputs")
    NOT_DEFINED3 = o6.enumfield(14, name="NotDefined3")
    ERROR = o6.enumfield(15, name="Error")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3019", browseName="TrayModeEnumeration")
class TrayModeEnumeration(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="Off")
    PRE_HEAT = o6.enumfield(1, name="PreHeat")
    PRE_COOL = o6.enumfield(2, name="PreCool")
    HOLD_WARM = o6.enumfield(3, name="HoldWarm")
    HOLD_COOL = o6.enumfield(4, name="HoldCool")
    REGENERATING = o6.enumfield(5, name="Regenerating")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3020", browseName="TrayTypeEnumeration")
class TrayTypeEnumeration(ns0.datatypes.Enumeration):
    GENERIC = o6.enumfield(0, name="Generic")
    HEATER_PLATE = o6.enumfield(1, name="HeaterPlate")
    COOLING_PLATE = o6.enumfield(2, name="CoolingPlate")
    COMBI_PLATE = o6.enumfield(3, name="CombiPlate")
    BAIN_MARIE = o6.enumfield(4, name="BainMarie")
    HEATER_CABINET = o6.enumfield(5, name="HeaterCabinet")
    COOLING_CABINET = o6.enumfield(6, name="CoolingCabinet")
    HEAT_BRIDGE = o6.enumfield(7, name="HeatBridge")
    COMBI_CABINET = o6.enumfield(8, name="CombiCabinet")
    REGEN_CABINET = o6.enumfield(9, name="RegenCabinet")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3021", browseName="CurrentStateEnumeration")
class CurrentStateEnumeration(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="Off")
    STANDBY = o6.enumfield(1, name="Standby")
    POWER = o6.enumfield(2, name="Power")
    POT_DETECTION = o6.enumfield(3, name="PotDetection")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3022", browseName="PlatenPositionStateEnumeration")
class PlatenPositionStateEnumeration(ns0.datatypes.Enumeration):
    HOME = o6.enumfield(0, name="Home")
    COOKING = o6.enumfield(1, name="Cooking")
    IDLE = o6.enumfield(2, name="Idle")
    OPEN = o6.enumfield(3, name="Open")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3023", browseName="OperatingModeEnumeration")
class OperatingModeEnumeration(ns0.datatypes.Enumeration):
    PREHEAT = o6.enumfield(0, name="Preheat")
    COOL_DOWN = o6.enumfield(1, name="CoolDown")
    PROCESS = o6.enumfield(2, name="Process")
    POWER_SAVING = o6.enumfield(3, name="PowerSaving")
    STANDBY = o6.enumfield(4, name="Standby")
    SERVICE = o6.enumfield(5, name="Service")
    CLEANING = o6.enumfield(6, name="Cleaning")
    OFF = o6.enumfield(7, name="Off")
    ERROR = o6.enumfield(8, name="Error")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3024", browseName="StatusEnumeration")
class StatusEnumeration(ns0.datatypes.Enumeration):
    INIT = o6.enumfield(0, name="INIT")
    WATER_PURGE = o6.enumfield(1, name="WATER_PURGE")
    PRE_CHILL = o6.enumfield(2, name="PRE_CHILL")
    FREEZE = o6.enumfield(3, name="FREEZE")
    HARVEST = o6.enumfield(4, name="HARVEST")
    BIN_FULL = o6.enumfield(5, name="BIN_FULL")
    CLEAN = o6.enumfield(6, name="CLEAN")
    OFF = o6.enumfield(7, name="OFF")
    SLEEP_MODE = o6.enumfield(8, name="SLEEP_MODE")
    STANDBY = o6.enumfield(9, name="STANDBY")
    SAFE_MODE = o6.enumfield(10, name="SAFE_MODE")
    WATER_OUTAGE = o6.enumfield(11, name="WATER_OUTAGE")
    HPCO_DELAY_ACTIVE = o6.enumfield(12, name="HPCO_DELAY_ACTIVE")
    CURTAIN_OPEN = o6.enumfield(13, name="CURTAIN_OPEN")
    PRODUCTION_TEST = o6.enumfield(14, name="PRODUCTION_TEST")
    SAFE_MODE_PRECHILL = o6.enumfield(15, name="SAFE_MODE_PRECHILL")
    SAFE_MODE_FREEZE = o6.enumfield(16, name="SAFE_MODE_FREEZE")
    SAFE_MODE_HARVEST = o6.enumfield(17, name="SAFE_MODE_HARVEST")
    SAFE_MODE_FULL_BIN = o6.enumfield(18, name="SAFE_MODE_FULL_BIN")


@o6.enumtype(nodeId="ns=commercial_kitchen;i=3025", browseName="GrillingZoneStateEnumeration")
class GrillingZoneStateEnumeration(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="Off")
    STANDBY = o6.enumfield(1, name="Standby")
    IDLE = o6.enumfield(2, name="Idle")
    GRILLING = o6.enumfield(3, name="Grilling")


del Any, TYPE_CHECKING, uuid, o6, di, ns0
