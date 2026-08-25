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
from . import vartypes as fdi_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=fdi;i=11", browseName="ns=fdi;ActionType", displayName="ActionType", isAbstract=True)
class ActionType(ns0.objtypes.BaseObjectType):
    pass


ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=23",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=22",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ActionName", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="MethodArguments", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=24",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=22",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ActionNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="InvokeActionError", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fdi;i=22", browseName="ns=fdi;InvokeAction", inputArgs=o6.hasProperty(o6.ns["ns=fdi;i=23"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi;i=24"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=26",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=25",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ActionNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="Response", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=27",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=25",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RespondActionError", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fdi;i=25", browseName="ns=fdi;RespondAction", inputArgs=o6.hasProperty(o6.ns["ns=fdi;i=26"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi;i=27"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=29",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=28",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ActionNodeId", dataType=o6.NodeId, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=30",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=28",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AbortActionError", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fdi;i=28", browseName="ns=fdi;AbortAction", inputArgs=o6.hasProperty(o6.ns["ns=fdi;i=29"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi;i=30"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=56",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=55",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ParentId", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="TargetWindowMode", dataType=o6.NodeId("ns=fdi;i=194"), valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=57",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=55",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="EditContextId", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="GetEditContextStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fdi;i=55", browseName="ns=fdi;GetEditContext", inputArgs=o6.hasProperty(o6.ns["ns=fdi;i=56"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi;i=57"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=59",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=58",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EditContextId", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="NodesToRegister", dataType=o6.NodeId("ns=fdi;i=37"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=60",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=58",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RegisterNodesStatus", dataType=o6.NodeId("ns=fdi;i=39"), valueRank=-1)],
)
o6.call(nodeId="ns=fdi;i=58", browseName="ns=fdi;RegisterNodesById", inputArgs=o6.hasProperty(o6.ns["ns=fdi;i=59"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi;i=60"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=62",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=61",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EditContextId", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="NodesToRegister", dataType=o6.NodeId("ns=fdi;i=37"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=63",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=61",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RegisterNodesStatus", dataType=o6.NodeId("ns=fdi;i=39"), valueRank=-1)],
)
o6.call(nodeId="ns=fdi;i=61", browseName="ns=fdi;RegisterNodesByRelativePath", inputArgs=o6.hasProperty(o6.ns["ns=fdi;i=62"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi;i=63"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=65",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=64",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="EditContextId", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=66",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=64",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplyStatus", dataType=o6.NodeId("ns=fdi;i=44"), valueRank=-1)],
)
o6.call(nodeId="ns=fdi;i=64", browseName="ns=fdi;Apply", inputArgs=o6.hasProperty(o6.ns["ns=fdi;i=65"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi;i=66"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=68",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=67",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="EditContextId", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=69",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=67",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ResetStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fdi;i=67", browseName="ns=fdi;Reset", inputArgs=o6.hasProperty(o6.ns["ns=fdi;i=68"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi;i=69"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=71",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=70",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="EditContextId", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=72",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=70",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DiscardStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fdi;i=70", browseName="ns=fdi;Discard", inputArgs=o6.hasProperty(o6.ns["ns=fdi;i=71"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi;i=72"]))


@o6.objecttype(nodeId="ns=fdi;i=54", browseName="ns=fdi;EditContextType", displayName="EditContextType")
class EditContextType(ns0.objtypes.BaseObjectType):
    apply: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=fdi;i=64"])
    discard: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=fdi;i=70"])
    getEditContext: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=fdi;i=55"])
    registerNodesById: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=fdi;i=58"])
    registerNodesByRelativePath: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=fdi;i=61"])
    reset: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=fdi;i=67"])


ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=84",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=83",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=85",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=83",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitDirectAccessError", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fdi;i=83", browseName="ns=fdi;InitDirectAccess", inputArgs=o6.hasProperty(o6.ns["ns=fdi;i=84"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi;i=85"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=87",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=86",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="SendData", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="ReceiveData", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=88",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=86",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TransferError", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fdi;i=86", browseName="ns=fdi;Transfer", inputArgs=o6.hasProperty(o6.ns["ns=fdi;i=87"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi;i=88"]))

ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=90",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=89",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InvalidateCache", dataType=o6.Boolean, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=fdi;i=91",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=fdi;i=89",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="EndDirectAccessError", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=fdi;i=89", browseName="ns=fdi;EndDirectAccess", inputArgs=o6.hasProperty(o6.ns["ns=fdi;i=90"]), outputArgs=o6.hasProperty(o6.ns["ns=fdi;i=91"]))


@o6.objecttype(nodeId="ns=fdi;i=82", browseName="ns=fdi;DirectDeviceAccessType", displayName="DirectDeviceAccessType")
class DirectDeviceAccessType(ns0.objtypes.BaseObjectType):
    endDirectAccess: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=fdi;i=89"])
    initDirectAccess: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=fdi;i=83"])
    transfer: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=fdi;i=86"])


@o6.objecttype(nodeId="ns=fdi;i=21", browseName="ns=fdi;ActionServiceType", displayName="ActionServiceType")
class ActionServiceType(ns0.objtypes.BaseObjectType):
    abortAction: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=fdi;i=28"])
    invokeAction: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=fdi;i=22"])
    langleActionIdentifierRangle: ActionType | None = o6.hasComponent(
        ActionType(nodeId="ns=fdi;i=181", browseName="ns=fdi;<ActionIdentifier>", modellingRule="OptionalPlaceholder", _allow_abstract=True)
    )
    respondAction: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=fdi;i=25"])


del Any, TYPE_CHECKING, uuid, o6, di, ns0, fdi_datypes, fdi_vartypes
