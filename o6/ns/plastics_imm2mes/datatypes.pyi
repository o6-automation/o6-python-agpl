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

import o6.ns.plastics_rubber as plastics_rubber

class IMMMessageClassificationEnumeration(enum.IntFlag):
    """This Enumeration specifies the values to be used in the Classification property in the MessageConditionType and related logbook events of OPC 40083"""

    OTHER = 0
    IMM_INJECTION_UNIT = 100
    IMM_CLAMPING_UNIT = 101
    IMM_HARDWARE = 102
    IMM_COMPRESSED_AIR_CONTROL = 103
    IMM_MACHINE_MONITORING = 104
    IMM_MOULD = 105
    IMM_EJECTOR = 106
    IMM_CORE_PULL = 107
    IMM_TABLE = 108
    IMM_INJECTION_PROGRAM = 109
    IMM_HYDRAULIC_TEMPERATURE_CONTROL = 110
    IMM_CYLINDER_TEMPERATURE_CONTROL = 111
    IMM_MOULD_TEMPERATURE_CONTROL = 112
    IMM_HOT_RUNNER = 113
    IMM_INTERFACES = 114
    IMM_MEASURING_SYSTEM = 115
    IMM_ROBOTIC_SYSTEM_INTERFACE = 116
    IMM_SPECIAL_PURPOSE_SIGNALS = 117
    IMM_REAL_TIME_ETHERNET_SYSTEM = 118
    IMM_MACHINE_CONTROLLER = 119
    IMM_SOFTWARE_MONITORING = 120
    PERIPHERAL_EXTERNAL_DEVICE_INTERFACE = 200
    PERIPHERAL_TEMPERATURE_CONTROL_UNIT = 201
    PERIPHERAL_ROBOTICS_SYSTEM = 202
    PERIPHERAL_LSR = 203
    PERIPHERAL_STRIPPER_UNIT = 204
    PERIPHERAL_DRYER = 205
    PERIPHERAL_CONVEYOR_BELT = 206
    PERIPHERAL_SORTER_UNIT = 207
    PERIPHERAL_COLOURING_UNIT = 208
    PERIPHERAL_FEEDING = 209
    PERIPHERAL_EXTERNAL_ALARMS = 210
    PERIPHERAL_VACUUM_CONTROL = 211
    PERIPHERAL_PRINTER_INTERFACE = 212
    OPERATION_QUALITY_MONITORING = 300
    OPERATION_MANUAL_OPERATION = 301
    OPERATION_EMERGENCY_STOP = 302
    OPERATION_JOB_STATUS = 303
