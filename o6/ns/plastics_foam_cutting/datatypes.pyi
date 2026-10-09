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

from typing import Any, Sequence, SupportsFloat

import numpy as np

_Integer = int | np.integer[Any]

_Boolean = bool | np.bool_

import enum

from o6.node import ObjectNode as _ObjectNode, VariableNode as _VariableNode

import uuid

import o6

import o6.ns.di as di

import o6.ns.ia as ia

import o6.ns.machinery as machinery

import o6.ns.ns0 as ns0

import o6.ns.plastics_rubber as plastics_rubber

class GrindingUnitStateEnumeration(enum.IntEnum):
    """Provides information about the current state of the grinding unit."""

    OFF = 0
    STANDBY = 1
    RUNNING = 2

class ActiveVacuumUnitsDataType(ns0.datatypes.Structure):
    """Provides information about the position of a vacuum unit and the current vacuum power, given as a float value between 0 (off) and 1 (full power)."""

    @property
    def position(self) -> o6.String: ...
    @position.setter
    def position(self, value: o6.String) -> None: ...
    @property
    def vacuumPower(self) -> o6.Float: ...
    @vacuumPower.setter
    def vacuumPower(self, value: SupportsFloat) -> None: ...

class ProcessingModeEnumeration(enum.IntEnum):
    """Provides information about the current processing mode as addition to the MachineOperationMode state Processing."""

    MANUAL = 0
    SEMI_AUTOMATIC = 1
    AUTOMATIC = 2

class BottomFixtureEnumeration(enum.IntEnum):
    """Provides information about the type of material fixture for the material bottom."""

    NONE = 0
    MECHANICAL__FIXTURE = 1
    VACUUM__FIXTURE = 2

class SideFixtureEnumeration(enum.IntEnum):
    """Provides information about the type of material fixture for the material side."""

    NONE = 0
    RIGHT = 1
    LEFT = 2
    BOTH = 3

class TopFixtureEnumeration(enum.IntEnum):
    """Provides information about the type of material fixture for the material top."""

    NONE = 0
    PRESSURE__PAD = 1
    PRESSURE__ROLLER = 2

class MaterialSupportCategoryEnumeration(enum.IntEnum):
    """This Property provides information about the category of the material support system."""

    NONE = 0
    FIXED__MACHINE__TABLE = 1
    SLIDING__MACHINE__TABLE = 2
    CAROUSEL = 3
    CONVEYOR__BELT = 4
    TURNTABLE_90_DEGREES = 5

class PossibleDirectionEnumeration(enum.IntEnum):
    """Provides information about the possible working directions of the conveyor."""

    FORWARDS = 0
    BACKWARDS = 1
    REVERSIBLE = 2
    SIDEWARDS = 3
    ANY = 4

class LightBarrierEnumeration(enum.IntEnum):
    """Provides information about the positions of light barriers on this instance of conveyor."""

    NONE = 0
    INFEED = 1
    OUTFEED = 2
    SAFETY = 3
    OTHER = 4

class ConveyorSubCategoryEnumeration(enum.IntEnum):
    """This property provides information on what type of conveyor this instance is."""

    NONE = 0
    ALIGNMENT_BELT = 1
    TURNTABLE = 2
    SEPERATOR = 3
    STACKER = 4
    DESTACKER = 5
    POP_UP = 6
    SCISSOR_TABLE = 7
    CROSS_CONVEYOR = 8

class ConveyorCategoryEnumeration(enum.IntEnum):
    """This property provides information, if this conveyor is used for unloading, loading or transportation of material."""

    LOADING = 0
    UNLOADING = 1
    TRANSPORTATION = 2

class DirectionEnumeration(enum.IntEnum):
    """Provides information about the current transportation direction of the conveyor."""

    FORWARD = 0
    BACKWARD = 1
    SIDEWARD = 2
