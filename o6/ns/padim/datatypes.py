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

"""Generated OPC UA padim namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.irdi as irdi
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=padim;i=1156", browseName="ResetModeEnum")
class ResetModeEnum(ns0.datatypes.Enumeration):
    APPLICATION = o6.enumfield(1, name="Application")
    COMMUNICATION = o6.enumfield(2712, name="Communication")
    FACTORY = o6.enumfield(2713, name="Factory")


@o6.enumtype(nodeId="ns=padim;i=1158", browseName="ExecutionModeEnum")
class ExecutionModeEnum(ns0.datatypes.Enumeration):
    START = o6.enumfield(2, name="Start")
    ABORT = o6.enumfield(255, name="Abort")


@o6.enumtype(nodeId="ns=padim;i=1276", browseName="PatDictionaryEnum")
class PatDictionaryEnum(ns0.datatypes.Enumeration):
    CAS = o6.enumfield(0, name="CAS")
    PAT = o6.enumfield(1, name="PAT")
    USER_DEFINED = o6.enumfield(2, name="User-defined")


@o6.datatype(nodeId="ns=padim;i=1275", browseName="ChemicalSubstanceDataType", defaultEncodingId="ns=padim;i=1277")
class ChemicalSubstanceDataType(ns0.datatypes.Structure):
    patDictionary: PatDictionaryEnum
    label: o6.LocalizedText
    id: o6.LocalizedText


del Any, TYPE_CHECKING, uuid, o6, di, irdi, ns0
