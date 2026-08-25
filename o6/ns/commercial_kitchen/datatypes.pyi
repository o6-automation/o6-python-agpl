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

from typing import Any, Sequence, SupportsFloat

import numpy as np

_Integer = int | np.integer[Any]

_Boolean = bool | np.bool_

import enum

from o6.node import ObjectNode as _ObjectNode, VariableNode as _VariableNode

import uuid

import o6

import o6.ns.di as di

import o6.ns.ns0 as ns0

class EnergySourceEnumeration(enum.IntFlag):
    ELECTRIC = 0
    GAS = 1
    STEAM = 2

class FryerModeEnumeration(enum.IntFlag):
    OFF = 0
    PREHEAT = 1
    MELTING = 2
    FRYING = 3
    STAND_BY = 4
    FILTERING = 5
    ERROR = 6

class SignalModeEnumeration(enum.IntFlag):
    SIGNAL_OFF = 0
    SIGNAL_ON = 1
    SIGNAL_ACK = 2

class FryingPanModeEnumeration(enum.IntFlag):
    OFF = 0
    PREHEAT = 1
    SOFT_COOK = 2
    COOK = 3
    COOK_SLOW = 4
    FRYING = 5
    PRESSURE_COOKING = 6
    KEEP_WARMING = 7
    PRESET_START = 8
    ERROR = 9

class CombiSteamerModeEnumeration(enum.IntFlag):
    OFF = 0
    ON = 1
    PREHEAT = 2
    STAND_BY = 3
    STEAMING = 4
    COMBI_STEAMING = 5
    HOT_AIR = 6
    PERFECTION = 7
    CLEANING = 8
    PRESET_START = 9
    ERROR = 10

class SpecialCookingModeEnumeration(enum.IntFlag):
    NO_SPECIAL_MODE = 0
    BAKING = 1
    SOUS_VIDE = 2
    REST_STAGE = 3
    HUMIDIFICATION = 4
    PERFECT_HOLD = 5
    INFO_STEP = 6
    SMOKING = 7
    LOW_TEMP__COOKING = 8
    DELTA_T_STEAMING = 9

class ChamberModeEnumeration(enum.IntFlag):
    NO_SPECIAL_MODE = 0
    OFF = 1
    AUTOSTART = 2
    STANDBY = 3
    PRE_HEAT = 4
    COOL_DOWN = 5
    WORKING = 6
    CLEANING = 7
    ENERGY_SAVE = 8
    SERVICE_MODE = 9
    QUICK_COOL = 10
    FLASH_FREEZE = 11
    PROOFING_INTERRUPTION = 12
    PROOFING_DELAY = 13
    PROOFING = 14
    SETTING = 15
    DEFROST = 16
    BAKING = 17
    STEAMING = 18

class PressureCookingKettleModeEnumeration(enum.IntFlag):
    OFF = 0
    PREHEAT = 1
    SOFT_COOK = 2
    COOK = 3
    COOK_SLOW = 4
    PRESSURE = 5
    KEEP_WARMING = 6
    PRESET_START = 7
    ERROR = 8

class CookingKettleModeEnumeration(enum.IntFlag):
    OFF = 0
    PREHEAT = 1
    SOFT_COOK = 2
    COOK = 3
    COOK_SLOW = 4
    KEEP_WARMING = 5
    STIRING = 6
    PRESET_START = 7
    ERROR = 8

class MultiFunctionPanModeEnumeration(enum.IntFlag):
    OFF = 0
    ON = 1
    PREHEAT = 2
    STAND_BY = 3
    PRESSURE_COOKING = 4
    SOFT_COOKING = 5
    COOKING = 6
    GRILLING = 7
    FRYING = 8
    REGENERATE = 9
    DELTA_TCOOKING = 10
    ZONE_GRILLING = 11
    ZONE_COOKING = 12
    CLEANING = 13
    PRESET_START = 14
    ERROR = 15

class SpecialFunctionModeEnumeration(enum.IntFlag):
    LID_UP_DOWN = 0
    PAN_TILT = 1
    WATER_SUPPLY = 2
    DRAIN_ON_OFF = 3

class PastaCookerModeEnumeration(enum.IntFlag):
    OFF = 0
    PREHEAT = 1
    SOFT_COOK = 2
    COOK = 3
    COOK_SLOW = 4
    KEEP_WARMING = 5
    PRESET_START = 6
    ERROR = 7

class BeverageSMLEnumeration(enum.IntFlag):
    INACTIVE = 0
    SMALL = 1
    LARGE = 2
    EXTRA_LARGE = 3

class CoffeeMachineModeEnumeration(enum.IntFlag):
    OFF = 0
    STANDBY = 1
    ERROR = 2
    CLEANING = 3

class ProgramModeEnumeration(enum.IntFlag):
    OPERATION_OFF = 0
    PRE_WASH = 1
    CLEANING1 = 2
    WASH_TIME_INCREASED = 3
    CLEANING2 = 4
    DRAINING_PAUSE = 5
    DRAINING = 6
    FINAL_RINSE = 7
    WAITING_TIME = 8
    HEAT_RECOVERY = 9

class HygieneModeEnumeration(enum.IntFlag):
    HYGIENE_OPERATION_OFF = 0
    HYGIENE_A0 = 1
    HYGIENE_HUE = 2
    HYGIENE_MU = 3
    HYGIENE_THERMOLABLE = 4
    HYGIENE_A0_TD = 5

class OperationModeEnumeration(enum.IntFlag):
    INIT = 0
    MACHINE_OFF = 1
    FILLING = 2
    FILLING_HEATING = 3
    HEATING = 4
    ENABLE_OPERATION = 5
    READY_FOR_OPERATION = 6
    OPERATION = 7
    CYCLE_PAUSE = 8
    NOT_DEFINED1 = 9
    SELF_CLEANING = 10
    NOT_DEFINED2 = 11
    REMOTE_CONTROL = 12
    CONTROLLING_OUTPUTS = 13
    NOT_DEFINED3 = 14
    ERROR = 15

class TrayModeEnumeration(enum.IntFlag):
    OFF = 0
    PRE_HEAT = 1
    PRE_COOL = 2
    HOLD_WARM = 3
    HOLD_COOL = 4
    REGENERATING = 5

class TrayTypeEnumeration(enum.IntFlag):
    GENERIC = 0
    HEATER_PLATE = 1
    COOLING_PLATE = 2
    COMBI_PLATE = 3
    BAIN_MARIE = 4
    HEATER_CABINET = 5
    COOLING_CABINET = 6
    HEAT_BRIDGE = 7
    COMBI_CABINET = 8
    REGEN_CABINET = 9

class CurrentStateEnumeration(enum.IntFlag):
    OFF = 0
    STANDBY = 1
    POWER = 2
    POT_DETECTION = 3

class PlatenPositionStateEnumeration(enum.IntFlag):
    HOME = 0
    COOKING = 1
    IDLE = 2
    OPEN = 3

class OperatingModeEnumeration(enum.IntFlag):
    PREHEAT = 0
    COOL_DOWN = 1
    PROCESS = 2
    POWER_SAVING = 3
    STANDBY = 4
    SERVICE = 5
    CLEANING = 6
    OFF = 7
    ERROR = 8

class StatusEnumeration(enum.IntFlag):
    INIT = 0
    WATER_PURGE = 1
    PRE_CHILL = 2
    FREEZE = 3
    HARVEST = 4
    BIN_FULL = 5
    CLEAN = 6
    OFF = 7
    SLEEP_MODE = 8
    STANDBY = 9
    SAFE_MODE = 10
    WATER_OUTAGE = 11
    HPCO_DELAY_ACTIVE = 12
    CURTAIN_OPEN = 13
    PRODUCTION_TEST = 14
    SAFE_MODE_PRECHILL = 15
    SAFE_MODE_FREEZE = 16
    SAFE_MODE_HARVEST = 17
    SAFE_MODE_FULL_BIN = 18

class GrillingZoneStateEnumeration(enum.IntFlag):
    OFF = 0
    STANDBY = 1
    IDLE = 2
    GRILLING = 3
