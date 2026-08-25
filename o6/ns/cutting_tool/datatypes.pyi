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

import o6.ns.gms as gms

import o6.ns.ia as ia

import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2

import o6.ns.machine_tool as machine_tool

import o6.ns.machinery as machinery

import o6.ns.machinery_jobs as machinery_jobs

import o6.ns.machinery_result as machinery_result

import o6.ns.ns0 as ns0

class FileFormatDataType(ns0.datatypes.Structure):
    @property
    def name(self) -> o6.String: ...
    @name.setter
    def name(self, value: o6.String) -> None: ...
    @property
    def fileExtension(self) -> o6.String: ...
    @fileExtension.setter
    def fileExtension(self, value: o6.String) -> None: ...
    @property
    def version(self) -> o6.String: ...
    @version.setter
    def version(self, value: o6.String) -> None: ...
