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

"""Generated OPC UA plcopen namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as plcopen_reftypes
from . import datatypes as plcopen_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=plcopen;i=1007", browseName="ns=plcopen;SFCType", displayName="SFCType")
class SFCType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(nodeId="ns=plcopen;i=1001", browseName="ns=plcopen;CtrlConfigurationType", displayName="CtrlConfigurationType")
class CtrlConfigurationType(di.objtypes.TopologyElementType):
    accessVars: di.objtypes.FunctionalGroupType | None = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=plcopen;i=5007", browseName="ns=plcopen;AccessVars"))
    configVars: di.objtypes.FunctionalGroupType | None = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=plcopen;i=5008", browseName="ns=plcopen;ConfigVars"))
    configuration: di.objtypes.FunctionalGroupType | None = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=plcopen;i=5009", browseName="ns=plcopen;Configuration"))
    globalVars: di.objtypes.FunctionalGroupType | None = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=plcopen;i=5006", browseName="ns=plcopen;GlobalVars"))
    identification: di.objtypes.FunctionalGroupType | None = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=plcopen;i=5003", browseName="ns=di;Identification"))
    methodSet: ns0.objtypes.BaseObjectType | None
    parameterSet: ns0.objtypes.BaseObjectType | None
    resources: di.objtypes.ConfigurableObjectType
    status: di.objtypes.FunctionalGroupType | None = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=plcopen;i=5010", browseName="ns=plcopen;Status"))


@o6.objecttype(nodeId="ns=plcopen;i=1002", browseName="ns=plcopen;CtrlResourceType", displayName="CtrlResourceType")
class CtrlResourceType(di.objtypes.DeviceType):
    configuration: di.objtypes.FunctionalGroupType | None = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=plcopen;i=5019", browseName="ns=plcopen;Configuration"))
    globalVars: di.objtypes.FunctionalGroupType | None = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=plcopen;i=5018", browseName="ns=plcopen;GlobalVars"))
    methodSet: ns0.objtypes.BaseObjectType | None
    programs: di.objtypes.ConfigurableObjectType
    status: di.objtypes.FunctionalGroupType | None = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=plcopen;i=5020", browseName="ns=plcopen;Status"))
    tasks: di.objtypes.ConfigurableObjectType


@o6.objecttype(nodeId="ns=plcopen;i=1003", browseName="ns=plcopen;CtrlProgramOrganizationUnitType", displayName="CtrlProgramOrganizationUnitType", isAbstract=True)
class CtrlProgramOrganizationUnitType(di.objtypes.BlockType):
    body: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plcopen;i=6001", browseName="ns=plcopen;Body", dataType=o6.XmlElement)
    )
    langleBlockNameRangle: CtrlFunctionBlockType | None
    langleSFCNameRangle: SFCType | None
    langleVarExternalNameRangle: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plcopen;i=1015", browseName="ns=plcopen;<VarExternalName>", modellingRule="OptionalPlaceholder", accessLevel=3),
        "ns=plcopen;i=4005",
    )
    langleVarInOutNameRangle: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plcopen;i=1011", browseName="ns=plcopen;<VarInOutName>", modellingRule="OptionalPlaceholder", accessLevel=3),
        "ns=plcopen;i=4003",
    )
    langleVarInputNameRangle: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plcopen;i=1012", browseName="ns=plcopen;<VarInputName>", modellingRule="OptionalPlaceholder", accessLevel=3),
        "ns=plcopen;i=4001",
    )
    langleVarLocalNameRangle: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plcopen;i=1014", browseName="ns=plcopen;<VarLocalName>", modellingRule="OptionalPlaceholder", accessLevel=3),
        "ns=plcopen;i=4004",
    )
    langleVarOutputNameRangle: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plcopen;i=1013", browseName="ns=plcopen;<VarOutputName>", modellingRule="OptionalPlaceholder", accessLevel=3),
        "ns=plcopen;i=4002",
    )


@o6.objecttype(nodeId="ns=plcopen;i=1004", browseName="ns=plcopen;CtrlProgramType", displayName="CtrlProgramType", isAbstract=True)
class CtrlProgramType(CtrlProgramOrganizationUnitType):
    program: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plcopen;i=6002", browseName="ns=plcopen;Program", dataType=ns0.datatypes.Structure)
    )


@o6.objecttype(nodeId="ns=plcopen;i=1005", browseName="ns=plcopen;CtrlFunctionBlockType", displayName="CtrlFunctionBlockType", isAbstract=True)
class CtrlFunctionBlockType(CtrlProgramOrganizationUnitType):
    functionBlock: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=plcopen;i=6003", browseName="ns=plcopen;FunctionBlock"))
    langleFunctionBlockInOutNameRangle: CtrlFunctionBlockType | None
    langleFunctionBlockInputNameRangle: CtrlFunctionBlockType | None
    langleFunctionBlockOutputNameRangle: CtrlFunctionBlockType | None


@o6.objecttype(nodeId="ns=plcopen;i=1006", browseName="ns=plcopen;CtrlTaskType", displayName="CtrlTaskType")
class CtrlTaskType(ns0.objtypes.BaseObjectType):
    interval: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plcopen;i=6005", browseName="ns=plcopen;Interval", dataType=o6.String))
    priority: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plcopen;i=6004", browseName="ns=plcopen;Priority", dataType=o6.UInt32))
    single: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plcopen;i=6006", browseName="ns=plcopen;Single", dataType=o6.String))


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plcopen_reftypes, plcopen_datypes
