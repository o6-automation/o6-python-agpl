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

"""Generated OPC UA machine_tool namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=machine_tool;i=62", browseName="ProcessIrregularity")
class ProcessIrregularity(ns0.datatypes.Enumeration):
    CAPABILITY_UNAVAILABLE = o6.enumfield(0, name="CapabilityUnavailable")
    DETECTED = o6.enumfield(1, name="Detected")
    NOT_DETECTED = o6.enumfield(2, name="NotDetected")
    NOT_YET_DETERMINED = o6.enumfield(3, name="NotYetDetermined")


@o6.enumtype(nodeId="ns=machine_tool;i=63", browseName="PartQuality")
class PartQuality(ns0.datatypes.Enumeration):
    CAPABILITY_UNAVAILABLE = o6.enumfield(0, name="CapabilityUnavailable")
    GOOD = o6.enumfield(1, name="Good")
    BAD = o6.enumfield(2, name="Bad")
    NOT_YET_MEASURED = o6.enumfield(3, name="NotYetMeasured")
    WILL_NOT_BE_MEASURED = o6.enumfield(4, name="WillNotBeMeasured")


@o6.enumtype(nodeId="ns=machine_tool;i=64", browseName="ChannelState")
class ChannelState(ns0.datatypes.Enumeration):
    ACTIVE = o6.enumfield(0, name="Active")
    INTERRUPTED = o6.enumfield(1, name="Interrupted")
    RESET = o6.enumfield(2, name="Reset")


@o6.enumtype(nodeId="ns=machine_tool;i=65", browseName="MachineOperationMode")
class MachineOperationMode(ns0.datatypes.Enumeration):
    MANUAL = o6.enumfield(0, name="Manual")
    AUTOMATIC = o6.enumfield(1, name="Automatic")
    SETUP = o6.enumfield(2, name="Setup")
    AUTO_WITH_MANUAL_INTERVENTION = o6.enumfield(3, name="AutoWithManualIntervention")
    SERVICE = o6.enumfield(4, name="Service")
    OTHER = o6.enumfield(5, name="Other")


@o6.enumtype(nodeId="ns=machine_tool;i=66", browseName="ToolLocked")
class ToolLocked(ns0.datatypes.Enumeration):
    CAPABILITY_UNAVAILABLE = o6.enumfield(0, name="CapabilityUnavailable")
    BY_OPERATOR = o6.enumfield(1, name="ByOperator")
    TOOL_BREAK = o6.enumfield(2, name="ToolBreak")
    TOOL_LIFE = o6.enumfield(3, name="ToolLife")
    MEASUREMENT_ERROR = o6.enumfield(4, name="MeasurementError")
    OTHER = o6.enumfield(5, name="Other")


@o6.enumtype(nodeId="ns=machine_tool;i=67", browseName="ChannelMode")
class ChannelMode(ns0.datatypes.Enumeration):
    AUTOMATIC = o6.enumfield(0, name="Automatic")
    MDA_MDI = o6.enumfield(1, name="MdaMdi")
    JOG_MANUAL = o6.enumfield(2, name="JogManual")
    JOG_INCREMENT = o6.enumfield(3, name="JogIncrement")
    TEACHING_HANDLE = o6.enumfield(4, name="TeachingHandle")
    REMOTE = o6.enumfield(5, name="Remote")
    REFERENCE = o6.enumfield(6, name="Reference")
    OTHER = o6.enumfield(7, name="Other")


@o6.enumtype(nodeId="ns=machine_tool;i=68", browseName="ToolLifeIndication")
class ToolLifeIndication(ns0.datatypes.Enumeration):
    TIME = o6.enumfield(0, name="Time")
    NUMBER_OF_PARTS = o6.enumfield(1, name="NumberOfParts")
    NUMBER_OF_USAGES = o6.enumfield(2, name="NumberOfUsages")
    FEED__DISTANCE = o6.enumfield(3, name="Feed_Distance")
    CUTTING__DISTANCE = o6.enumfield(4, name="Cutting_Distance")
    LENGTH = o6.enumfield(5, name="Length")
    DIAMETER = o6.enumfield(6, name="Diameter")
    OTHER = o6.enumfield(7, name="Other")


@o6.enumtype(nodeId="ns=machine_tool;i=69", browseName="ToolManagement")
class ToolManagement(ns0.datatypes.Enumeration):
    NUMBER_BASED = o6.enumfield(0, name="NumberBased")
    GROUP_BASED = o6.enumfield(1, name="GroupBased")
    OTHER = o6.enumfield(2, name="Other")


@o6.enumtype(nodeId="ns=machine_tool;i=70", browseName="LaserState")
class LaserState(ns0.datatypes.Enumeration):
    UNDEFINED = o6.enumfield(0, name="Undefined")
    READY = o6.enumfield(1, name="Ready")
    ACTIVE = o6.enumfield(2, name="Active")
    ERROR = o6.enumfield(3, name="Error")


@o6.enumtype(nodeId="ns=machine_tool;i=71", browseName="EDMGeneratorState")
class EDMGeneratorState(ns0.datatypes.Enumeration):
    UNDEFINED = o6.enumfield(0, name="Undefined")
    READY = o6.enumfield(1, name="Ready")
    ACTIVE__LOW__VOLTAGE = o6.enumfield(2, name="Active_Low_Voltage")
    ACTIVE__HIGH__VOLTAGE = o6.enumfield(3, name="Active_High_Voltage")
    ERROR = o6.enumfield(4, name="Error")


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, ns0
