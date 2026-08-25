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

"""Generated OPC UA pnem namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as pnem_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=pnem;i=3002", browseName="StandbyModeTransitionDataType", defaultEncodingId="ns=pnem;i=5001")
class StandbyModeTransitionDataType(ns0.datatypes.Structure):
    iDDestination: o6.Byte
    currentTimeToDestination: o6.Double
    currentTimeToOperate: o6.Double
    energyConsumptionToDestination: o6.Float


@o6.datatype(nodeId="ns=pnem;i=3003", browseName="EnergyStateInformationDataType", defaultEncodingId="ns=pnem;i=5004")
class EnergyStateInformationDataType(ns0.datatypes.Structure):
    iDSource: o6.Byte
    iDDestination: o6.Byte
    regularTimeToOperate: o6.Double
    modePowerConsumption: o6.Float


@o6.datatype(nodeId="ns=pnem;i=3004", browseName="PeVersionDataType", defaultEncodingId="ns=pnem;i=5007")
class PeVersionDataType(ns0.datatypes.Structure):
    majorVersion: o6.Byte
    minorVersion: o6.Byte
    revision: o6.Byte


@o6.datatype(nodeId="ns=pnem;i=3005", browseName="AcPeDataType", defaultEncodingId="ns=pnem;i=5010")
class AcPeDataType(ns0.datatypes.Structure):
    a: o6.Float
    b: o6.Float
    c: o6.Float


@o6.datatype(nodeId="ns=pnem;i=3006", browseName="AcPpDataType", defaultEncodingId="ns=pnem;i=5013")
class AcPpDataType(ns0.datatypes.Structure):
    a_b: o6.Float
    b_c: o6.Float
    c_a: o6.Float


@o6.enumtype(nodeId="ns=pnem;i=3007", browseName="PeClassEnumeration")
class PeClassEnumeration(ns0.datatypes.Enumeration):
    PE_CLASS1 = o6.enumfield(0, name="PE_CLASS1")
    PE_CLASS2 = o6.enumfield(1, name="PE_CLASS2")
    PE_CLASS3 = o6.enumfield(2, name="PE_CLASS3")


@o6.enumtype(nodeId="ns=pnem;i=3008", browseName="PeSubclassEnumeration")
class PeSubclassEnumeration(ns0.datatypes.Enumeration):
    PE_SUBCLASS1 = o6.enumfield(0, name="PE_SUBCLASS1")
    PE_SUBCLASS2 = o6.enumfield(1, name="PE_SUBCLASS2")


@o6.enumtype(nodeId="ns=pnem;i=3009", browseName="AccuracyClassEnumeration")
class AccuracyClassEnumeration(ns0.datatypes.Enumeration):
    ACCURACY_CLASS_0 = o6.enumfield(0, name="ACCURACY_CLASS_0")
    ACCURACY_CLASS_1 = o6.enumfield(1, name="ACCURACY_CLASS_1")
    ACCURACY_CLASS_2 = o6.enumfield(2, name="ACCURACY_CLASS_2")
    ACCURACY_CLASS_3 = o6.enumfield(3, name="ACCURACY_CLASS_3")
    ACCURACY_CLASS_4 = o6.enumfield(4, name="ACCURACY_CLASS_4")
    ACCURACY_CLASS_5 = o6.enumfield(5, name="ACCURACY_CLASS_5")
    ACCURACY_CLASS_6 = o6.enumfield(6, name="ACCURACY_CLASS_6")
    ACCURACY_CLASS_7 = o6.enumfield(7, name="ACCURACY_CLASS_7")
    ACCURACY_CLASS_8 = o6.enumfield(8, name="ACCURACY_CLASS_8")
    ACCURACY_CLASS_9 = o6.enumfield(9, name="ACCURACY_CLASS_9")
    ACCURACY_CLASS_10 = o6.enumfield(10, name="ACCURACY_CLASS_10")
    ACCURACY_CLASS_11 = o6.enumfield(11, name="ACCURACY_CLASS_11")
    ACCURACY_CLASS_12 = o6.enumfield(12, name="ACCURACY_CLASS_12")
    ACCURACY_CLASS_13 = o6.enumfield(13, name="ACCURACY_CLASS_13")
    ACCURACY_CLASS_14 = o6.enumfield(14, name="ACCURACY_CLASS_14")
    ACCURACY_CLASS_15 = o6.enumfield(15, name="ACCURACY_CLASS_15")


@o6.enumtype(nodeId="ns=pnem;i=3010", browseName="AccuracyDomainEnumeration")
class AccuracyDomainEnumeration(ns0.datatypes.Enumeration):
    ACCURACY_DOMAIN_RESERVED = o6.enumfield(0, name="ACCURACY_DOMAIN_RESERVED")
    ACCURACY_DOMAIN_PERCENT_FULL_SCALE = o6.enumfield(1, name="ACCURACY_DOMAIN_PERCENT_FULL_SCALE")
    ACCURACY_DOMAIN_PERCENT_ACTUAL_READING = o6.enumfield(2, name="ACCURACY_DOMAIN_PERCENT_ACTUAL_READING")
    ACCURACY_DOMAIN_IEC = o6.enumfield(3, name="ACCURACY_DOMAIN_IEC")
    ACCURACY_DOMAIN_EN = o6.enumfield(4, name="ACCURACY_DOMAIN_EN")


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pnem_reftypes
