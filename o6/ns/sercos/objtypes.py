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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=sercos;i=6012", browseName="ns=sercos;FunctionalGroupType", displayName="FunctionalGroupType")
class FunctionalGroupType(ns0.objtypes.FolderType):
    pass


@o6.objecttype(nodeId="ns=sercos;i=1002", browseName="ns=sercos;SercosProfileType", displayName="SercosProfileType")
class SercosProfileType(FunctionalGroupType):
    pass


@o6.objecttype(nodeId="ns=sercos;i=1003", browseName="ns=sercos;SercosClassType", displayName="SercosClassType")
class SercosClassType(FunctionalGroupType):
    pass


@o6.objecttype(nodeId="ns=sercos;i=1004", browseName="ns=sercos;SercosFunctionGroupType", displayName="SercosFunctionGroupType")
class SercosFunctionGroupType(FunctionalGroupType):
    pass


@o6.objecttype(nodeId="ns=sercos;i=1001", browseName="ns=sercos;SercosDeviceType", displayName="SercosDeviceType")
class SercosDeviceType(di.objtypes.DeviceType):
    classSet: FunctionalGroupType = o6.hasComponent(FunctionalGroupType(nodeId="ns=sercos;i=5002", browseName="ns=sercos;ClassSet"))
    functionGroupSet: FunctionalGroupType = o6.hasComponent(FunctionalGroupType(nodeId="ns=sercos;i=5003", browseName="ns=sercos;FunctionGroupSet"))
    parameterSet: FunctionalGroupType = o6.hasComponent(FunctionalGroupType(nodeId="ns=sercos;i=5007", browseName="ns=sercos;ParameterSet", description="Flat list of Parameters"))
    profileSet: FunctionalGroupType = o6.hasComponent(FunctionalGroupType(nodeId="ns=sercos;i=5001", browseName="ns=sercos;ProfileSet"))


@o6.objecttype(nodeId="ns=sercos;i=6075", browseName="ns=sercos;ProfileSet", displayName="ProfileSet")
class ProfileSet(FunctionalGroupType):
    langleSercosProfileIdentifierRangle: SercosProfileType | None = o6.hasComponent(
        SercosProfileType(nodeId="ns=sercos;i=6076", browseName="ns=sercos;<SercosProfileIdentifier>", modellingRule="OptionalPlaceholder")
    )


@o6.objecttype(nodeId="ns=sercos;i=6077", browseName="ns=sercos;ClassSet", displayName="ClassSet")
class ClassSet(FunctionalGroupType):
    langleSercosClassIdentifierRangle: SercosClassType | None = o6.hasComponent(
        SercosClassType(nodeId="ns=sercos;i=6078", browseName="ns=sercos;<SercosClassIdentifier>", modellingRule="OptionalPlaceholder")
    )


@o6.objecttype(nodeId="ns=sercos;i=6079", browseName="ns=sercos;FunctionGroupSet", displayName="FunctionGroupSet")
class FunctionGroupSet(FunctionalGroupType):
    langleFunctionGroupIdentifierRangle: SercosFunctionGroupType | None = o6.hasComponent(
        SercosFunctionGroupType(nodeId="ns=sercos;i=6080", browseName="ns=sercos;<FunctionGroupIdentifier>", modellingRule="OptionalPlaceholder")
    )


del Any, TYPE_CHECKING, uuid, o6, di, ns0, sercos_vartypes
