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

"""Generated OPC UA wmtp namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.irdi as irdi
import o6.ns.machinery as machinery
import o6.ns.machinery_processvalues as machinery_processvalues
import o6.ns.ns0 as ns0
import o6.ns.padim as padim

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=wmtp;i=3003", browseName="ns=wmtp;WMTPOutputDataType", defaultEncodingId="ns=wmtp;i=5020")
class WMTPOutputDataType(ns0.datatypes.Structure):
    engineeringUnits: ns0.datatypes.EUInformation = o6.field(name="EngineeringUnits")
    actualValue: o6.Double = o6.field(name="ActualValue")
    typeOfMeasurement: o6.UInt32 = o6.field(name="TypeOfMeasurement")
    typeOfSample: o6.UInt32 = o6.field(name="TypeOfSample")
    instrumentRange: ns0.datatypes.Range = o6.field(name="InstrumentRange")
    eURange: ns0.datatypes.Range = o6.field(name="EURange")
    valuePrecision: o6.Double = o6.field(name="ValuePrecision")
    definition: o6.String = o6.field(name="Definition")
    signalTag: o6.String = o6.field(name="SignalTag")
    relativeUncertainty: o6.Double = o6.field(name="RelativeUncertainty")
    absoluteUncertainty: o6.Double = o6.field(name="AbsoluteUncertainty")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    index: o6.UInt32 = o6.field(name="Index")
    measurementPeriod: o6.Double = o6.field(name="MeasurementPeriod")
    internalUpdateInterval: o6.Double = o6.field(name="InternalUpdateInterval")


del Any, TYPE_CHECKING, uuid, o6, di, ia, irdi, machinery, machinery_processvalues, ns0, padim
