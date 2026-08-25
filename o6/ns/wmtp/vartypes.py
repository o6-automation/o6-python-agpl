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
from . import datatypes as wmtp_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="ns=wmtp;i=2001", browseName="ns=wmtp;WMTPOutputType", displayName="WMTPOutputType", dataType=wmtp_datypes.WMTPOutputDataType)
class WMTPOutputType(ns0.vartypes.BaseDataVariableType):
    absoluteUncertainty: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=wmtp;i=6270", browseName="ns=wmtp;AbsoluteUncertainty", dataType=o6.Double)
    )
    actualValue: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=wmtp;i=6262", browseName="ns=wmtp;ActualValue", dataType=o6.Double)
    )
    definition: ns0.vartypes.BaseDataVariableType = o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=wmtp;i=6267", browseName="ns=wmtp;Definition", dataType=o6.String))
    eURange: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=wmtp;i=6265", browseName="ns=wmtp;EURange", dataType=ns0.datatypes.Range)
    )
    engineeringUnits: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=wmtp;i=6261", browseName="ns=wmtp;EngineeringUnits", dataType=ns0.datatypes.EUInformation)
    )
    index: ns0.vartypes.BaseDataVariableType = o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=wmtp;i=6272", browseName="ns=wmtp;Index", dataType=o6.UInt32))
    internalUpdateInterval: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=wmtp;i=6274", browseName="ns=wmtp;InternalUpdateInterval", dataType=ns0.datatypes.Duration)
    )
    measurementPeriod: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=wmtp;i=6273", browseName="ns=wmtp;MeasurementPeriod", dataType=ns0.datatypes.Duration)
    )
    relativeUncertainty: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=wmtp;i=6269", browseName="ns=wmtp;RelativeUncertainty", dataType=o6.Double)
    )
    signalTag: ns0.vartypes.BaseDataVariableType = o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=wmtp;i=6268", browseName="ns=wmtp;SignalTag", dataType=o6.String))
    timestamp: ns0.vartypes.BaseDataVariableType = o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=wmtp;i=6271", browseName="ns=wmtp;Timestamp", dataType=o6.DateTime))
    typeOfMeasurement: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=wmtp;i=6263", browseName="ns=wmtp;TypeOfMeasurement", dataType=o6.UInt32)
    )
    typeOfSample: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=wmtp;i=6264", browseName="ns=wmtp;TypeOfSample", dataType=o6.UInt32)
    )
    valuePrecision: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=wmtp;i=6266", browseName="ns=wmtp;ValuePrecision", dataType=o6.Double)
    )


del Any, TYPE_CHECKING, uuid, o6, di, ia, irdi, machinery, machinery_processvalues, ns0, padim, wmtp_datypes
