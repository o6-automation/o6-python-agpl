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
from . import objtypes as aml_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

automationMLInstanceHierarchies = ns0.objtypes.FolderType(
    nodeId="ns=aml;i=5005", browseName="ns=aml;AutomationMLInstanceHierarchies", parent="i=85", referenceType=ns0.reftypes.Organizes
)
automationMLFiles = ns0.objtypes.FolderType(nodeId="ns=aml;i=5006", browseName="ns=aml;AutomationMLFiles", parent="i=85", referenceType=ns0.reftypes.Organizes)
automationMLLibraries = ns0.objtypes.FolderType(
    nodeId="ns=aml;i=5007",
    browseName="ns=aml;AutomationMLLibraries",
    description="The browse entry point when looking for AutomationML libraries in the server address space.",
    references=[
        o6.organizes(ns0.objtypes.FolderType(nodeId="ns=aml;i=5008", browseName="ns=aml;InterfaceClassLibs")),
        o6.organizes(ns0.objtypes.FolderType(nodeId="ns=aml;i=5009", browseName="ns=aml;RoleClassLibs")),
        o6.organizes(ns0.objtypes.FolderType(nodeId="ns=aml;i=5010", browseName="ns=aml;SystemUnitClassLibs")),
    ],
    parent="i=88",
    referenceType=ns0.reftypes.Organizes,
)
o6.reference(automationMLLibraries, "i=35", "i=85", inverse=True)


del Any, TYPE_CHECKING, uuid, o6, ns0, aml_reftypes, aml_vartypes, aml_objtypes
