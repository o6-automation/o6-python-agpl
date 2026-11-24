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


@o6.datatype(nodeId="ns=wire_harness;i=3000", browseName="ns=wire_harness;ProcessInputDataType", isAbstract=True)
class ProcessInputDataType(ns0.datatypes.Structure):
    toolType: list[o6.String] = o6.field(name="ToolType", arrayDimensions=[1])
    processDescription: list[o6.String] = o6.field(name="ProcessDescription", arrayDimensions=[1])
    id: o6.String = o6.field(name="Id")


@o6.datatype(nodeId="ns=wire_harness;i=3001", browseName="ns=wire_harness;CutInputDataType", defaultEncodingId="ns=wire_harness;i=5007")
class CutInputDataType(ProcessInputDataType):
    toolType: list[o6.String] = o6.field(name="ToolType", arrayDimensions=[1])
    processDescription: list[o6.String] = o6.field(name="ProcessDescription", arrayDimensions=[1])
    id: o6.String = o6.field(name="Id")
    referencedElement: wire_harness_vec.datatypes.WireElementReferenceIdDataType = o6.field(name="ReferencedElement")
    verifyWireLength: list[o6.Boolean] = o6.field(name="VerifyWireLength", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness;i=3002", browseName="ns=wire_harness;ProcessOutputDataType", defaultEncodingId="ns=wire_harness;i=5011")
class ProcessOutputDataType(ns0.datatypes.Structure):
    toolInstance: o6.String = o6.field(name="ToolInstance")


@o6.datatype(nodeId="ns=wire_harness;i=3003", browseName="ns=wire_harness;CutOutputDataType", defaultEncodingId="ns=wire_harness;i=5041")
class CutOutputDataType(ProcessOutputDataType):
    toolInstance: o6.String = o6.field(name="ToolInstance")
    actualLength: list[wire_harness_vec.datatypes.NumericalValue] = o6.field(name="ActualLength", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness;i=3008", browseName="ns=wire_harness;ForceCurvePointDataType", defaultEncodingId="ns=wire_harness;i=5016")
class ForceCurvePointDataType(ns0.datatypes.Structure):
    x: list[o6.UInt32] = o6.field(name="X", arrayDimensions=[0])
    value: list[o6.UInt32] = o6.field(name="Value", arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness;i=3018", browseName="ns=wire_harness;CrimpInputDataType", defaultEncodingId="ns=wire_harness;i=5039")
class CrimpInputDataType(ProcessInputDataType):
    toolType: list[o6.String] = o6.field(name="ToolType", arrayDimensions=[1])
    processDescription: list[o6.String] = o6.field(name="ProcessDescription", arrayDimensions=[1])
    id: o6.String = o6.field(name="Id")
    referencedElement: wire_harness_vec.datatypes.WireMountingIdDataType = o6.field(name="ReferencedElement")
    verifyCrimpHeight: list[o6.Boolean] = o6.field(name="VerifyCrimpHeight", arrayDimensions=[1])
    verifyCrimpWidth: list[o6.Boolean] = o6.field(name="VerifyCrimpWidth", arrayDimensions=[1])
    verifyInsulationCrimpHeight: list[o6.Boolean] = o6.field(name="VerifyInsulationCrimpHeight", arrayDimensions=[1])
    verifyInsulationCrimpWidth: list[o6.Boolean] = o6.field(name="VerifyInsulationCrimpWidth", arrayDimensions=[1])
    verifyPullOutForce: list[o6.Boolean] = o6.field(name="VerifyPullOutForce", arrayDimensions=[1])
    crimpForceMonitoring: list[o6.Boolean] = o6.field(name="CrimpForceMonitoring", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness;i=3022", browseName="ns=wire_harness;StripInputDataType", defaultEncodingId="ns=wire_harness;i=5037")
class StripInputDataType(ProcessInputDataType):
    toolType: list[o6.String] = o6.field(name="ToolType", arrayDimensions=[1])
    processDescription: list[o6.String] = o6.field(name="ProcessDescription", arrayDimensions=[1])
    id: o6.String = o6.field(name="Id")
    referencedElement: wire_harness_vec.datatypes.WireEndIdDataType = o6.field(name="ReferencedElement")
    strippingLengthMonitoring: list[o6.Boolean] = o6.field(name="StrippingLengthMonitoring", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness;i=3026", browseName="ns=wire_harness;StripOutputDataType", defaultEncodingId="ns=wire_harness;i=5059")
class StripOutputDataType(ProcessOutputDataType):
    toolInstance: o6.String = o6.field(name="ToolInstance")
    actualStrippingLength: list[wire_harness_vec.datatypes.NumericalValue] = o6.field(name="ActualStrippingLength", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness;i=3033", browseName="ns=wire_harness;ForceCurveDataType", defaultEncodingId="ns=wire_harness;i=5046")
class ForceCurveDataType(ns0.datatypes.Structure):
    points: list[ForceCurvePointDataType] = o6.field(name="Points", arrayDimensions=[0])
    engineeringUnitsX: ns0.datatypes.EUInformation = o6.field(name="EngineeringUnitsX")
    engineeringUnitsValue: ns0.datatypes.EUInformation = o6.field(name="EngineeringUnitsValue")


@o6.datatype(nodeId="ns=wire_harness;i=3035", browseName="ns=wire_harness;CrimpOutputDataType", defaultEncodingId="ns=wire_harness;i=5063")
class CrimpOutputDataType(ProcessOutputDataType):
    toolInstance: o6.String = o6.field(name="ToolInstance")
    actualCrimpHeight: list[wire_harness_vec.datatypes.NumericalValue] = o6.field(name="ActualCrimpHeight", arrayDimensions=[1])
    actualCrimpWidth: list[wire_harness_vec.datatypes.NumericalValue] = o6.field(name="ActualCrimpWidth", arrayDimensions=[1])
    actualInsulationCrimpHeight: list[wire_harness_vec.datatypes.NumericalValue] = o6.field(name="ActualInsulationCrimpHeight", arrayDimensions=[1])
    actualCrimpForceCurve: list[ForceCurveDataType] = o6.field(name="ActualCrimpForceCurve", arrayDimensions=[1])
    actualCrimpPullOutForce: list[wire_harness_vec.datatypes.NumericalValue] = o6.field(name="ActualCrimpPullOutForce", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness;i=3049", browseName="ns=wire_harness;SealInputDataType", defaultEncodingId="ns=wire_harness;i=5071")
class SealInputDataType(ProcessInputDataType):
    toolType: list[o6.String] = o6.field(name="ToolType", arrayDimensions=[1])
    processDescription: list[o6.String] = o6.field(name="ProcessDescription", arrayDimensions=[1])
    id: o6.String = o6.field(name="Id")
    referencedElement: wire_harness_vec.datatypes.WireMountingIdDataType = o6.field(name="ReferencedElement")
    monitorSealPosition: list[o6.Boolean] = o6.field(name="MonitorSealPosition", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness;i=3052", browseName="ns=wire_harness;SealOutputDataType", defaultEncodingId="ns=wire_harness;i=5073")
class SealOutputDataType(ProcessOutputDataType):
    toolInstance: o6.String = o6.field(name="ToolInstance")
    actualPosition: list[wire_harness_vec.datatypes.NumericalValue] = o6.field(name="ActualPosition", arrayDimensions=[1])


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, machinery_result, ns0, wire_harness_vec
