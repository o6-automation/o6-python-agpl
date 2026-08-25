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

"""Generated OPC UA fdi namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import datatypes as fdi_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="ns=fdi;i=1", browseName="ns=fdi;UIDescriptionType", displayName="UIDescriptionType", dataType=o6.String)
class UIDescriptionType(di.vartypes.UIElementType):
    pass


@o6.variabletype(nodeId="ns=fdi;i=2", browseName="ns=fdi;UIPlugInType", displayName="UIPlugInType", dataType=o6.Byte, valueRank=o6.ValueRank.ARRAY_1D, arrayDimensions=[0])
class UIPlugInType(di.vartypes.UIElementType):
    cpuInformation: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi;i=6", browseName="ns=fdi;CpuInformation", dataType=o6.String))
    documentation: ns0.objtypes.FolderType | None = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=fdi;i=10", browseName="ns=fdi;Documentation"))
    fDITechnologyVersion: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi;i=4", browseName="ns=fdi;FDITechnologyVersion", dataType=o6.String))
    platformId: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi;i=7", browseName="ns=fdi;PlatformId", dataType=o6.String))
    runtimeId: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi;i=5", browseName="ns=fdi;RuntimeId", dataType=o6.String))
    startElementName: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi;i=9", browseName="ns=fdi;StartElementName", dataType=o6.String))
    style: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi;i=8", browseName="ns=fdi;Style", dataType=fdi_datypes.StyleType))
    uIPVariantVersion: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi;i=3", browseName="ns=fdi;UIPVariantVersion", dataType=o6.String))


del Any, TYPE_CHECKING, uuid, o6, di, ns0, fdi_datypes
