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

import o6.ns.ia as ia

import o6.ns.machinery as machinery

import o6.ns.ns0 as ns0

import o6.ns.pack_ml as pack_ml

class WSOperatingModeEnumerationType(enum.IntFlag):
    """The operating mode provides information about the nature and extent of the intervention on the control equipment by the operators, and also via feedback from the equipment (DIN 19 237). This value must be coded in bit form or be documented as an integer for machines which are components of bottling systems:"""

    OFF = 1
    MANUAL = 2
    SEMI_AUTOMATIC = 4
    AUTOMATIC = 8

class WSProgramEnumerationType(enum.IntFlag):
    """The program is a consequent sequence of control instructions for a self-contained application-oriented function (DIN 19237). For bottling machines, bits or documented integer numbers must be used for machine operation with the following programs:"""

    UNDEFINED___NO__PROGRAM_ = 0
    PRODUCTION = 1
    START__UP = 2
    RUN__DOWN = 4
    CLEAN = 8
    CHANGEOVER = 16
    MAINTENANCE = 32
    BREAK = 64
