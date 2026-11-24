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

"""Generated OPC UA fdt namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as fdt_reftypes
from . import datatypes as fdt_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="ns=fdt;i=2002", browseName="ns=fdt;FdtParameter", displayName="FdtParameter", valueRank=o6.ValueRank.ANY)
class FdtParameter(ns0.vartypes.DataItemType):
    alarmDataRef: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6013", browseName="ns=fdt;AlarmDataRef", modellingRule="Optional", dataType=fdt_datypes.DataRefType, accessLevel=3, userAccessLevel=1
        )
    )
    alarmType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6020", browseName="ns=fdt;AlarmType", modellingRule="Optional", dataType=fdt_datypes.AlarmType, accessLevel=3, userAccessLevel=1)
    )
    applicationId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6021", browseName="ns=fdt;ApplicationId", modellingRule="Optional", dataType=fdt_datypes.ApplicationIdEnumeration, accessLevel=3, userAccessLevel=1
        )
    )
    dataRef: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6010", browseName="ns=fdt;DataRef", modellingRule="Optional", dataType=fdt_datypes.DataRefType, accessLevel=3, userAccessLevel=1)
    )
    displayFormat: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6031", browseName="ns=fdt;DisplayFormat", modellingRule="Optional", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    eURange: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6034", browseName="ns=fdt;EURange", modellingRule="Optional", dataType=ns0.datatypes.Range, accessLevel=3, userAccessLevel=1)
    )
    engineeringUnits: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6032", browseName="ns=fdt;EngineeringUnits", modellingRule="Optional", dataType=ns0.datatypes.EUInformation, accessLevel=3, userAccessLevel=1
        )
    )
    enumStrings: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6033",
            browseName="ns=fdt;EnumStrings",
            modellingRule="Optional",
            dataType=o6.LocalizedText,
            valueRank=1,
            arrayDimensions=[1],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    rangeDataRef: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6015", browseName="ns=fdt;RangeDataRef", modellingRule="Optional", dataType=fdt_datypes.DataRefType, accessLevel=3, userAccessLevel=1
        )
    )
    rangeType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdt;i=6035", browseName="ns=fdt;RangeType", modellingRule="Optional", dataType=fdt_datypes.RangeType, accessLevel=3, userAccessLevel=1)
    )
    semanticInfo: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6055", browseName="ns=fdt;SemanticInfo", modellingRule="Optional", dataType=fdt_datypes.SemanticInfoType, accessLevel=3, userAccessLevel=1
        )
    )
    substituteDataRef: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6017", browseName="ns=fdt;SubstituteDataRef", modellingRule="Optional", dataType=fdt_datypes.DataRefType, accessLevel=3, userAccessLevel=1
        )
    )
    substitutionType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=fdt;i=6036", browseName="ns=fdt;SubstitutionType", modellingRule="Optional", dataType=fdt_datypes.SubstitutionType, accessLevel=3, userAccessLevel=1
        )
    )


del Any, TYPE_CHECKING, uuid, o6, di, ns0, fdt_reftypes, fdt_datypes
