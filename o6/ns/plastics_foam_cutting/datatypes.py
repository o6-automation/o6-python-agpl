# Copyright (c) 2026 o6 Automation GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
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

"""Generated OPC UA plastics_foam_cutting namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=plastics_foam_cutting;i=3003", browseName="GrindingUnitStateEnumeration", description="Provides information about the current state of the grinding unit.")
class GrindingUnitStateEnumeration(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="Off")
    STANDBY = o6.enumfield(1, name="Standby")
    RUNNING = o6.enumfield(2, name="Running")


@o6.datatype(
    nodeId="ns=plastics_foam_cutting;i=3004",
    browseName="ActiveVacuumUnitsDataType",
    description="Provides information about the position of a vacuum unit and the current vacuum power, given as a float value between 0 (off) and 1 (full power).",
    defaultEncodingId="ns=plastics_foam_cutting;i=5073",
)
class ActiveVacuumUnitsDataType(ns0.datatypes.Structure):
    position: o6.String
    vacuumPower: o6.Float


@o6.enumtype(
    nodeId="ns=plastics_foam_cutting;i=3005",
    browseName="ProcessingModeEnumeration",
    description="Provides information about the current processing mode as addition to the MachineOperationMode state Processing.",
)
class ProcessingModeEnumeration(ns0.datatypes.Enumeration):
    MANUAL = o6.enumfield(0, name="Manual")
    SEMI_AUTOMATIC = o6.enumfield(1, name="SemiAutomatic")
    AUTOMATIC = o6.enumfield(2, name="Automatic")


@o6.enumtype(
    nodeId="ns=plastics_foam_cutting;i=3006", browseName="BottomFixtureEnumeration", description="Provides information about the type of material fixture for the material bottom."
)
class BottomFixtureEnumeration(ns0.datatypes.Enumeration):
    NONE = o6.enumfield(0, name="None")
    MECHANICAL_FIXTURE = o6.enumfield(1, name="Mechanical_Fixture")
    VACUUM_FIXTURE = o6.enumfield(2, name="Vacuum_Fixture")


@o6.enumtype(
    nodeId="ns=plastics_foam_cutting;i=3009", browseName="SideFixtureEnumeration", description="Provides information about the type of material fixture for the material side."
)
class SideFixtureEnumeration(ns0.datatypes.Enumeration):
    NONE = o6.enumfield(0, name="None")
    RIGHT = o6.enumfield(1, name="Right")
    LEFT = o6.enumfield(2, name="Left")
    BOTH = o6.enumfield(3, name="Both")


@o6.enumtype(
    nodeId="ns=plastics_foam_cutting;i=3012", browseName="TopFixtureEnumeration", description="Provides information about the type of material fixture for the material top."
)
class TopFixtureEnumeration(ns0.datatypes.Enumeration):
    NONE = o6.enumfield(0, name="None")
    PRESSURE_PAD = o6.enumfield(1, name="Pressure_Pad")
    PRESSURE_ROLLER = o6.enumfield(2, name="Pressure_Roller")


@o6.enumtype(
    nodeId="ns=plastics_foam_cutting;i=3015",
    browseName="MaterialSupportCategoryEnumeration",
    description="This Property provides information about the category of the material support system.",
)
class MaterialSupportCategoryEnumeration(ns0.datatypes.Enumeration):
    NONE = o6.enumfield(0, name="None")
    FIXED_MACHINE_TABLE = o6.enumfield(1, name="Fixed_Machine_Table")
    SLIDING_MACHINE_TABLE = o6.enumfield(2, name="Sliding_Machine_Table")
    CAROUSEL = o6.enumfield(3, name="Carousel")
    CONVEYOR_BELT = o6.enumfield(4, name="Conveyor_Belt")
    TURNTABLE_90_DEGREES = o6.enumfield(5, name="Turntable_90Degrees")


@o6.enumtype(
    nodeId="ns=plastics_foam_cutting;i=3018", browseName="PossibleDirectionEnumeration", description="Provides information about the possible working directions of the conveyor."
)
class PossibleDirectionEnumeration(ns0.datatypes.Enumeration):
    FORWARDS = o6.enumfield(0, name="Forwards")
    BACKWARDS = o6.enumfield(1, name="Backwards")
    REVERSIBLE = o6.enumfield(2, name="Reversible")
    SIDEWARDS = o6.enumfield(3, name="Sidewards")
    ANY = o6.enumfield(4, name="Any")


@o6.enumtype(
    nodeId="ns=plastics_foam_cutting;i=3021",
    browseName="LightBarrierEnumeration",
    description="Provides information about the positions of light barriers on this instance of conveyor.",
)
class LightBarrierEnumeration(ns0.datatypes.Enumeration):
    NONE = o6.enumfield(0, name="None")
    INFEED = o6.enumfield(1, name="Infeed")
    OUTFEED = o6.enumfield(2, name="Outfeed")
    SAFETY = o6.enumfield(3, name="Safety")
    OTHER = o6.enumfield(4, name="Other")


@o6.enumtype(
    nodeId="ns=plastics_foam_cutting;i=3024",
    browseName="ConveyorSubCategoryEnumeration",
    description="This property provides information on what type of conveyor this instance is.",
)
class ConveyorSubCategoryEnumeration(ns0.datatypes.Enumeration):
    NONE = o6.enumfield(0, name="None")
    ALIGNMENT_BELT = o6.enumfield(1, name="AlignmentBelt")
    TURNTABLE = o6.enumfield(2, name="Turntable")
    SEPERATOR = o6.enumfield(3, name="Seperator")
    STACKER = o6.enumfield(4, name="Stacker")
    DESTACKER = o6.enumfield(5, name="Destacker")
    POP_UP = o6.enumfield(6, name="PopUp")
    SCISSOR_TABLE = o6.enumfield(7, name="ScissorTable")
    CROSS_CONVEYOR = o6.enumfield(8, name="CrossConveyor")


@o6.enumtype(
    nodeId="ns=plastics_foam_cutting;i=3027",
    browseName="ConveyorCategoryEnumeration",
    description="This property provides information, if this conveyor is used for unloading, loading or transportation of material.",
)
class ConveyorCategoryEnumeration(ns0.datatypes.Enumeration):
    LOADING = o6.enumfield(0, name="Loading")
    UNLOADING = o6.enumfield(1, name="Unloading")
    TRANSPORTATION = o6.enumfield(2, name="Transportation")


@o6.enumtype(
    nodeId="ns=plastics_foam_cutting;i=3030", browseName="DirectionEnumeration", description="Provides information about the current transportation direction of the conveyor."
)
class DirectionEnumeration(ns0.datatypes.Enumeration):
    FORWARD = o6.enumfield(0, name="Forward")
    BACKWARD = o6.enumfield(1, name="Backward")
    SIDEWARD = o6.enumfield(2, name="Sideward")


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, plastics_rubber
