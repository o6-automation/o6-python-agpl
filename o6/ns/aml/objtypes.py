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

"""Generated OPC UA aml namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as aml_reftypes
from . import vartypes as aml_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=aml;i=1006", browseName="ns=aml;CAEXBasicObjectType", displayName="CAEXBasicObjectType")
class CAEXBasicObjectType(ns0.objtypes.BaseObjectType):
    version: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml;i=6001", browseName="ns=aml;Version", dataType=o6.String))


@o6.objecttype(nodeId="ns=aml;i=1005", browseName="ns=aml;CAEXFileType", displayName="CAEXFileType")
class CAEXFileType(CAEXBasicObjectType):
    instanceHierarchies: ns0.objtypes.FolderType = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=aml;i=5001", browseName="ns=aml;InstanceHierarchies"))
    interfaceClassLibs: ns0.objtypes.FolderType = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=aml;i=5002", browseName="ns=aml;InterfaceClassLibs"))
    roleClassLibs: ns0.objtypes.FolderType = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=aml;i=5003", browseName="ns=aml;RoleClassLibs"))
    systemUnitClassLibs: ns0.objtypes.FolderType = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=aml;i=5004", browseName="ns=aml;SystemUnitClassLibs"))


@o6.objecttype(nodeId="ns=aml;i=1001", browseName="ns=aml;CAEXObjectType", displayName="CAEXObjectType")
class CAEXObjectType(CAEXBasicObjectType):
    iD: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml;i=6002", browseName="ns=aml;ID", dataType=o6.String))


@o6.objecttype(nodeId="ns=aml;i=1002", browseName="ns=aml;AutomationMLBaseInterface", displayName="AutomationMLBaseInterface")
class AutomationMLBaseInterface(CAEXObjectType):
    pass


@o6.objecttype(nodeId="ns=aml;i=1003", browseName="ns=aml;AutomationMLBaseRole", displayName="AutomationMLBaseRole")
class AutomationMLBaseRole(CAEXObjectType):
    pass


@o6.objecttype(nodeId="ns=aml;i=1004", browseName="ns=aml;AutomationMLBaseSystemUnit", displayName="AutomationMLBaseSystemUnit")
class AutomationMLBaseSystemUnit(CAEXObjectType):
    pass


del Any, TYPE_CHECKING, uuid, o6, ns0, aml_reftypes, aml_vartypes
