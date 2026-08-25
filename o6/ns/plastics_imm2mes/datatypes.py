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

"""Generated OPC UA plastics_imm2mes namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(
    nodeId="ns=plastics_imm2mes;i=3004",
    browseName="IMMMessageClassificationEnumeration",
    description="This Enumeration specifies the values to be used in the Classification property in the MessageConditionType and related logbook events of OPC 40083",
)
class IMMMessageClassificationEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    IMM_INJECTION_UNIT = o6.enumfield(100, name="IMM_INJECTION_UNIT")
    IMM_CLAMPING_UNIT = o6.enumfield(101, name="IMM_CLAMPING_UNIT")
    IMM_HARDWARE = o6.enumfield(102, name="IMM_HARDWARE")
    IMM_COMPRESSED_AIR_CONTROL = o6.enumfield(103, name="IMM_COMPRESSED_AIR_CONTROL")
    IMM_MACHINE_MONITORING = o6.enumfield(104, name="IMM_MACHINE_MONITORING")
    IMM_MOULD = o6.enumfield(105, name="IMM_MOULD")
    IMM_EJECTOR = o6.enumfield(106, name="IMM_EJECTOR")
    IMM_CORE_PULL = o6.enumfield(107, name="IMM_CORE_PULL")
    IMM_TABLE = o6.enumfield(108, name="IMM_TABLE")
    IMM_INJECTION_PROGRAM = o6.enumfield(109, name="IMM_INJECTION_PROGRAM")
    IMM_HYDRAULIC_TEMPERATURE_CONTROL = o6.enumfield(110, name="IMM_HYDRAULIC_TEMPERATURE_CONTROL")
    IMM_CYLINDER_TEMPERATURE_CONTROL = o6.enumfield(111, name="IMM_CYLINDER_TEMPERATURE_CONTROL")
    IMM_MOULD_TEMPERATURE_CONTROL = o6.enumfield(112, name="IMM_MOULD_TEMPERATURE_CONTROL")
    IMM_HOT_RUNNER = o6.enumfield(113, name="IMM_HOT_RUNNER")
    IMM_INTERFACES = o6.enumfield(114, name="IMM_INTERFACES")
    IMM_MEASURING_SYSTEM = o6.enumfield(115, name="IMM_MEASURING_SYSTEM")
    IMM_ROBOTIC_SYSTEM_INTERFACE = o6.enumfield(116, name="IMM_ROBOTIC_SYSTEM_INTERFACE")
    IMM_SPECIAL_PURPOSE_SIGNALS = o6.enumfield(117, name="IMM_SPECIAL_PURPOSE_SIGNALS")
    IMM_REAL_TIME_ETHERNET_SYSTEM = o6.enumfield(118, name="IMM_REAL_TIME_ETHERNET_SYSTEM")
    IMM_MACHINE_CONTROLLER = o6.enumfield(119, name="IMM_MACHINE_CONTROLLER")
    IMM_SOFTWARE_MONITORING = o6.enumfield(120, name="IMM_SOFTWARE_MONITORING")
    PERIPHERAL_EXTERNAL_DEVICE_INTERFACE = o6.enumfield(200, name="PERIPHERAL_EXTERNAL_DEVICE_INTERFACE")
    PERIPHERAL_TEMPERATURE_CONTROL_UNIT = o6.enumfield(201, name="PERIPHERAL_TEMPERATURE_CONTROL_UNIT")
    PERIPHERAL_ROBOTICS_SYSTEM = o6.enumfield(202, name="PERIPHERAL_ROBOTICS_SYSTEM")
    PERIPHERAL_LSR = o6.enumfield(203, name="PERIPHERAL_LSR")
    PERIPHERAL_STRIPPER_UNIT = o6.enumfield(204, name="PERIPHERAL_STRIPPER_UNIT")
    PERIPHERAL_DRYER = o6.enumfield(205, name="PERIPHERAL_DRYER")
    PERIPHERAL_CONVEYOR_BELT = o6.enumfield(206, name="PERIPHERAL_CONVEYOR_BELT")
    PERIPHERAL_SORTER_UNIT = o6.enumfield(207, name="PERIPHERAL_SORTER_UNIT")
    PERIPHERAL_COLOURING_UNIT = o6.enumfield(208, name="PERIPHERAL_COLOURING_UNIT")
    PERIPHERAL_FEEDING = o6.enumfield(209, name="PERIPHERAL_FEEDING")
    PERIPHERAL_EXTERNAL_ALARMS = o6.enumfield(210, name="PERIPHERAL_EXTERNAL_ALARMS")
    PERIPHERAL_VACUUM_CONTROL = o6.enumfield(211, name="PERIPHERAL_VACUUM_CONTROL")
    PERIPHERAL_PRINTER_INTERFACE = o6.enumfield(212, name="PERIPHERAL_PRINTER_INTERFACE")
    OPERATION_QUALITY_MONITORING = o6.enumfield(300, name="OPERATION_QUALITY_MONITORING")
    OPERATION_MANUAL_OPERATION = o6.enumfield(301, name="OPERATION_MANUAL_OPERATION")
    OPERATION_EMERGENCY_STOP = o6.enumfield(302, name="OPERATION_EMERGENCY_STOP")
    OPERATION_JOB_STATUS = o6.enumfield(303, name="OPERATION_JOB_STATUS")


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_rubber
