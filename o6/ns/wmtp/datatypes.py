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


@o6.datatype(nodeId="ns=wmtp;i=3003", browseName="WMTPOutputDataType", defaultEncodingId="ns=wmtp;i=5020")
class WMTPOutputDataType(ns0.datatypes.Structure):
    engineeringUnits: ns0.datatypes.EUInformation
    actualValue: o6.Double
    typeOfMeasurement: o6.UInt32
    typeOfSample: o6.UInt32
    instrumentRange: ns0.datatypes.Range
    eURange: ns0.datatypes.Range
    valuePrecision: o6.Double
    definition: o6.String
    signalTag: o6.String
    relativeUncertainty: o6.Double
    absoluteUncertainty: o6.Double
    timestamp: o6.DateTime
    index: o6.UInt32
    measurementPeriod: o6.Double
    internalUpdateInterval: o6.Double


del Any, TYPE_CHECKING, uuid, o6, di, ia, irdi, machinery, machinery_processvalues, ns0, padim
