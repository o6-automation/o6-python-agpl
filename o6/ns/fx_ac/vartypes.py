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

"""Generated OPC UA fx_ac namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.fx_data as fx_data
import o6.ns.ns0 as ns0
from . import reftypes as fx_ac_reftypes
from . import datatypes as fx_ac_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(
    nodeId="ns=fx_ac;i=2001",
    browseName="ns=fx_ac;AggregatedHealthType",
    displayName="AggregatedHealthType",
    dataType=fx_ac_datypes.AggregatedHealthDataType,
    value=fx_ac_datypes.AggregatedHealthDataType(
        aggregatedDeviceHealth=fx_ac_datypes.DeviceHealthOptionSet.DEVICE_FAILURE, aggregatedOperationalHealth=fx_ac_datypes.OperationalHealthOptionSet(0)
    ),
)
class AggregatedHealthType(ns0.vartypes.BaseDataVariableType):
    aggregatedDeviceHealth: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6052", browseName="ns=fx_ac;AggregatedDeviceHealth", dataType=fx_ac_datypes.DeviceHealthOptionSet)
    )
    aggregatedOperationalHealth: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_ac;i=6053", browseName="ns=fx_ac;AggregatedOperationalHealth", dataType=fx_ac_datypes.OperationalHealthOptionSet)
    )


del Any, TYPE_CHECKING, uuid, o6, di, fx_data, ns0, fx_ac_reftypes, fx_ac_datypes
