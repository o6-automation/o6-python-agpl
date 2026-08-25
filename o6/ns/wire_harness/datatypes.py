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

"""Generated OPC UA wire_harness namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.machinery_result as machinery_result
import o6.ns.ns0 as ns0
import o6.ns.wire_harness_vec as wire_harness_vec

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=wire_harness;i=3000", browseName="ProcessInputDataType", isAbstract=True)
class ProcessInputDataType(ns0.datatypes.Structure):
    toolType: list[o6.String]
    processDescription: list[o6.String]
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness;i=3001", browseName="CutInputDataType", defaultEncodingId="ns=wire_harness;i=5007")
class CutInputDataType(ProcessInputDataType):
    toolType: list[o6.String]
    processDescription: list[o6.String]
    id: o6.String
    referencedElement: wire_harness_vec.datatypes.WireElementReferenceIdDataType
    verifyWireLength: list[o6.Boolean]


@o6.datatype(nodeId="ns=wire_harness;i=3002", browseName="ProcessOutputDataType", defaultEncodingId="ns=wire_harness;i=5011")
class ProcessOutputDataType(ns0.datatypes.Structure):
    toolInstance: o6.String


@o6.datatype(nodeId="ns=wire_harness;i=3003", browseName="CutOutputDataType", defaultEncodingId="ns=wire_harness;i=5041")
class CutOutputDataType(ProcessOutputDataType):
    toolInstance: o6.String
    actualLength: list[wire_harness_vec.datatypes.NumericalValue]


@o6.datatype(nodeId="ns=wire_harness;i=3008", browseName="ForceCurvePointDataType", defaultEncodingId="ns=wire_harness;i=5016")
class ForceCurvePointDataType(ns0.datatypes.Structure):
    x: list[o6.UInt32]
    value: list[o6.UInt32]


@o6.datatype(nodeId="ns=wire_harness;i=3018", browseName="CrimpInputDataType", defaultEncodingId="ns=wire_harness;i=5039")
class CrimpInputDataType(ProcessInputDataType):
    toolType: list[o6.String]
    processDescription: list[o6.String]
    id: o6.String
    referencedElement: wire_harness_vec.datatypes.WireMountingIdDataType
    verifyCrimpHeight: list[o6.Boolean]
    verifyCrimpWidth: list[o6.Boolean]
    verifyInsulationCrimpHeight: list[o6.Boolean]
    verifyInsulationCrimpWidth: list[o6.Boolean]
    verifyPullOutForce: list[o6.Boolean]
    crimpForceMonitoring: list[o6.Boolean]


@o6.datatype(nodeId="ns=wire_harness;i=3022", browseName="StripInputDataType", defaultEncodingId="ns=wire_harness;i=5037")
class StripInputDataType(ProcessInputDataType):
    toolType: list[o6.String]
    processDescription: list[o6.String]
    id: o6.String
    referencedElement: wire_harness_vec.datatypes.WireEndIdDataType
    strippingLengthMonitoring: list[o6.Boolean]


@o6.datatype(nodeId="ns=wire_harness;i=3026", browseName="StripOutputDataType", defaultEncodingId="ns=wire_harness;i=5059")
class StripOutputDataType(ProcessOutputDataType):
    toolInstance: o6.String
    actualStrippingLength: list[wire_harness_vec.datatypes.NumericalValue]


@o6.datatype(nodeId="ns=wire_harness;i=3033", browseName="ForceCurveDataType", defaultEncodingId="ns=wire_harness;i=5046")
class ForceCurveDataType(ns0.datatypes.Structure):
    points: list[ForceCurvePointDataType]
    engineeringUnitsX: ns0.datatypes.EUInformation
    engineeringUnitsValue: ns0.datatypes.EUInformation


@o6.datatype(nodeId="ns=wire_harness;i=3035", browseName="CrimpOutputDataType", defaultEncodingId="ns=wire_harness;i=5063")
class CrimpOutputDataType(ProcessOutputDataType):
    toolInstance: o6.String
    actualCrimpHeight: list[wire_harness_vec.datatypes.NumericalValue]
    actualCrimpWidth: list[wire_harness_vec.datatypes.NumericalValue]
    actualInsulationCrimpHeight: list[wire_harness_vec.datatypes.NumericalValue]
    actualCrimpForceCurve: list[ForceCurveDataType]
    actualCrimpPullOutForce: list[wire_harness_vec.datatypes.NumericalValue]


@o6.datatype(nodeId="ns=wire_harness;i=3049", browseName="SealInputDataType", defaultEncodingId="ns=wire_harness;i=5071")
class SealInputDataType(ProcessInputDataType):
    toolType: list[o6.String]
    processDescription: list[o6.String]
    id: o6.String
    referencedElement: wire_harness_vec.datatypes.WireMountingIdDataType
    monitorSealPosition: list[o6.Boolean]


@o6.datatype(nodeId="ns=wire_harness;i=3052", browseName="SealOutputDataType", defaultEncodingId="ns=wire_harness;i=5073")
class SealOutputDataType(ProcessOutputDataType):
    toolInstance: o6.String
    actualPosition: list[wire_harness_vec.datatypes.NumericalValue]


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, machinery_result, ns0, wire_harness_vec
