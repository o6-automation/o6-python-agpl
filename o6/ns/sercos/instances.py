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

"""Generated OPC UA sercos namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import vartypes as sercos_vartypes
from . import objtypes as sercos_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

httpColonSlashSlashSercosDotOrgSlashUASlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=sercos;i=6081",
    browseName="ns=sercos;http://sercos.org/UA/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=sercos;i=6082", browseName="NamespaceUri", dataType=o6.String, value="http://sercos.org/UA/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=sercos;i=6083", browseName="NamespaceVersion", dataType=o6.String, value="1.00")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=sercos;i=6084", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2017-03-13T00:00:00Z"))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=sercos;i=6085", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=sercos;i=6086", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=sercos;i=6087", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["1:65535"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=sercos;i=6088", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="\n      ")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=sercos;i=6111", browseName="DefaultRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=sercos;i=6112", browseName="DefaultUserRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=sercos;i=6113", browseName="DefaultAccessRestrictions", dataType=ns0.datatypes.AccessRestrictionType)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.Organizes,
)


del Any, TYPE_CHECKING, uuid, o6, di, ns0, sercos_vartypes, sercos_objtypes
