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

"""Generated OPC UA gms namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machine_tool as machine_tool
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.machinery_result as machinery_result
import o6.ns.ns0 as ns0
from . import datatypes as gms_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="ns=gms;i=2002", browseName="ns=gms;AdditionalSensorType", displayName="AdditionalSensorType", dataType=ns0.datatypes.Number)
class AdditionalSensorType(ns0.vartypes.AnalogUnitType):
    class_: ns0.vartypes.MultiStateDiscreteType | None
    identifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6030", browseName="ns=gms;Identifier", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6031", browseName="ns=gms;Name", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


@o6.variabletype(nodeId="ns=gms;i=2004", browseName="ns=gms;GMSResultType", displayName="GMSResultType", dataType=machinery_result.datatypes.ResultDataType)
class GMSResultType(machinery_result.vartypes.ResultType):
    usedTools: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6047", browseName="ns=gms;UsedTools", dataType=o6.String, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1)
    )


@o6.variabletype(nodeId="ns=gms;i=2003", browseName="ns=gms;CatalogType", displayName="CatalogType", dataType=ns0.datatypes.Number, valueRank=o6.ValueRank.ANY)
class CatalogType(ns0.vartypes.MultiStateValueDiscreteType):
    catalogEntry: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6282", browseName="ns=gms;CatalogEntry", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    catalogName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=gms;i=6281", browseName="ns=gms;CatalogName", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machine_tool, machinery, machinery_jobs, machinery_result, ns0, gms_datypes
