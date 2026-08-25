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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="ns=aml;i=3001", browseName="ns=aml;AMLBaseVariableType", displayName="AMLBaseVariableType")
class AMLBaseVariableType(ns0.vartypes.BaseVariableType):
    iD: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml;i=1010", browseName="ns=aml;ID", dataType=o6.String))
    version: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=aml;i=1011", browseName="ns=aml;Version", dataType=o6.String))


@o6.variabletype(nodeId="ns=aml;i=3002", browseName="ns=aml;AMLOpcUaConnectionType", displayName="AMLOpcUaConnectionType")
class AMLOpcUaConnectionType(AMLBaseVariableType):
    serverAddress: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=aml;i=1014", browseName="ns=aml;ServerAddress", dataType=o6.String)
    )
    serverAlias: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=aml;i=1015", browseName="ns=aml;ServerAlias", dataType=o6.String)
    )
    variableName: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=aml;i=1013", browseName="ns=aml;VariableName", dataType=o6.String)
    )
    variableNodeId: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=aml;i=1012", browseName="ns=aml;VariableNodeId", dataType=o6.String)
    )


del Any, TYPE_CHECKING, uuid, o6, ns0, aml_reftypes
