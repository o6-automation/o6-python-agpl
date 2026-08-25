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

class StacklightOperationMode(enum.IntFlag):
    """Contains the values used to indicate how a stacklight (as a whole unit) is used."""

    SEGMENTED = 0
    LEVELMETER = 1
    RUNNING__LIGHT = 2
    OTHER = 3

class LevelDisplayMode(enum.IntFlag):
    """Contains the values used to indicate how a percentual value is displayed if the stacklight unit works in Levelmeter mode."""

    DIMMED = 0
    BLINKING = 1
    OTHER = 2

class SignalColor(enum.IntFlag):
    """Holds the possible colour values for stacklight lamps."""

    OFF = 0
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    PURPLE = 5
    CYAN = 6
    WHITE = 7

class SignalModeLight(enum.IntFlag):
    """Contains the values used to indicate in what way a lamp behaves when switched on."""

    CONTINUOUS = 0
    BLINKING = 1
    FLASHING = 2
    OTHER = 3

class RGBWDataType(ns0.datatypes.Structure):
    @property
    def red(self) -> o6.Byte: ...
    @red.setter
    def red(self, value: _Integer) -> None: ...
    @property
    def green(self) -> o6.Byte: ...
    @green.setter
    def green(self, value: _Integer) -> None: ...
    @property
    def blue(self) -> o6.Byte: ...
    @blue.setter
    def blue(self, value: _Integer) -> None: ...
    @property
    def white(self) -> o6.Byte | None: ...
    @white.setter
    def white(self, value: _Integer | None) -> None: ...
