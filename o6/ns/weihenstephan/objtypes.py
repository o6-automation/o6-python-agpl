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

"""Generated OPC UA weihenstephan namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
import o6.ns.pack_ml as pack_ml
from . import datatypes as weihenstephan_datypes
from . import vartypes as weihenstephan_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=weihenstephan;i=1006", browseName="ns=weihenstephan;WSHeldStateMachineType", displayName="WSHeldStateMachineType")
class WSHeldStateMachineType(ns0.objtypes.FiniteStateMachineType):
    equipmentFailure: ns0.objtypes.StateType = o6.hasComponent(ns0.objtypes.StateType(nodeId="ns=weihenstephan;i=5012", browseName="ns=weihenstephan;EquipmentFailure"))
    externalFailure: ns0.objtypes.StateType = o6.hasComponent(ns0.objtypes.StateType(nodeId="ns=weihenstephan;i=5014", browseName="ns=weihenstephan;ExternalFailure"))


@o6.objecttype(nodeId="ns=weihenstephan;i=1007", browseName="ns=weihenstephan;WSSuspendedStateMachineType", displayName="WSSuspendedStateMachineType")
class WSSuspendedStateMachineType(ns0.objtypes.FiniteStateMachineType):
    lack: ns0.objtypes.StateType = o6.hasComponent(ns0.objtypes.StateType(nodeId="ns=weihenstephan;i=5016", browseName="ns=weihenstephan;Lack"))
    lackBranchLine: ns0.objtypes.StateType = o6.hasComponent(ns0.objtypes.StateType(nodeId="ns=weihenstephan;i=5018", browseName="ns=weihenstephan;LackBranchLine"))
    prepared: ns0.objtypes.StateType = o6.hasComponent(ns0.objtypes.StateType(nodeId="ns=weihenstephan;i=5020", browseName="ns=weihenstephan;Prepared"))
    tailback: ns0.objtypes.StateType = o6.hasComponent(ns0.objtypes.StateType(nodeId="ns=weihenstephan;i=5022", browseName="ns=weihenstephan;Tailback"))
    tailbackBranchLine: ns0.objtypes.StateType = o6.hasComponent(ns0.objtypes.StateType(nodeId="ns=weihenstephan;i=5024", browseName="ns=weihenstephan;TailbackBranchLine"))


WSHeldStateMachineType(nodeId="ns=weihenstephan;i=5026", browseName="ns=weihenstephan;HeldState")
WSSuspendedStateMachineType(nodeId="ns=weihenstephan;i=5027", browseName="ns=weihenstephan;SuspendedState")
ns0.objtypes.StateType(nodeId="ns=weihenstephan;i=5028", browseName="ns=pack_ml;Held")
o6.reference(o6.ns["ns=weihenstephan;i=5028"], "i=117", o6.ns["ns=weihenstephan;i=5026"])
ns0.objtypes.StateType(nodeId="ns=weihenstephan;i=5029", browseName="ns=pack_ml;Suspended")
o6.reference(o6.ns["ns=weihenstephan;i=5029"], "i=117", o6.ns["ns=weihenstephan;i=5027"])


@o6.objecttype(nodeId="ns=weihenstephan;i=1005", browseName="ns=weihenstephan;WSExecuteStateMachineType", displayName="WSExecuteStateMachineType")
class WSExecuteStateMachineType(pack_ml.objtypes.PackMLExecuteStateMachineType):
    held: ns0.objtypes.StateType = o6.hasComponent(o6.ns["ns=weihenstephan;i=5028"])
    heldState: WSHeldStateMachineType = o6.hasComponent(o6.ns["ns=weihenstephan;i=5026"])
    suspended: ns0.objtypes.StateType = o6.hasComponent(o6.ns["ns=weihenstephan;i=5029"])
    suspendedState: WSSuspendedStateMachineType = o6.hasComponent(o6.ns["ns=weihenstephan;i=5027"])


@o6.objecttype(
    nodeId="ns=weihenstephan;i=1000",
    browseName="ns=weihenstephan;WSMachineType",
    displayName="WSMachineType",
    description="Definition of a machine according to the Weihenstephan standards",
)
class WSMachineType(ns0.objtypes.BaseObjectType):
    alarms: di.objtypes.FunctionalGroupType | None = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=weihenstephan;i=5008", browseName="ns=weihenstephan;Alarms"))
    batchAndArticleTracing: di.objtypes.FunctionalGroupType | None = o6.hasComponent(
        di.objtypes.FunctionalGroupType(nodeId="ns=weihenstephan;i=5004", browseName="ns=weihenstephan;BatchAndArticleTracing")
    )
    computedValues: di.objtypes.FunctionalGroupType | None = o6.hasComponent(
        di.objtypes.FunctionalGroupType(nodeId="ns=weihenstephan;i=5002", browseName="ns=weihenstephan;ComputedValues")
    )
    counters: di.objtypes.FunctionalGroupType | None = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=weihenstephan;i=5003", browseName="ns=weihenstephan;Counters"))
    identification: machinery.objtypes.MachineIdentificationType
    measuredValues: di.objtypes.FunctionalGroupType | None = o6.hasComponent(
        di.objtypes.FunctionalGroupType(nodeId="ns=weihenstephan;i=5009", browseName="ns=weihenstephan;MeasuredValues")
    )
    operatingModes: di.objtypes.FunctionalGroupType | None = o6.hasComponent(
        di.objtypes.FunctionalGroupType(nodeId="ns=weihenstephan;i=5005", browseName="ns=weihenstephan;OperatingModes")
    )
    operatingStates: di.objtypes.FunctionalGroupType | None = o6.hasComponent(
        di.objtypes.FunctionalGroupType(nodeId="ns=weihenstephan;i=5006", browseName="ns=weihenstephan;OperatingStates")
    )
    parameters: di.objtypes.FunctionalGroupType | None = o6.hasComponent(
        di.objtypes.FunctionalGroupType(nodeId="ns=weihenstephan;i=5010", browseName="ns=weihenstephan;Parameters")
    )
    programs: di.objtypes.FunctionalGroupType | None = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=weihenstephan;i=5007", browseName="ns=weihenstephan;Programs"))
    wSMachineProfile: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=weihenstephan;i=6008", browseName="ns=weihenstephan;WSMachineProfile", dataType=o6.String, accessLevel=3)
    )
    wSVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=weihenstephan;i=6009", browseName="ns=weihenstephan;WSVersion", dataType=o6.String, accessLevel=3)
    )
    wSVersionProject: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=weihenstephan;i=6011", browseName="ns=weihenstephan;WSVersionProject", dataType=o6.String, accessLevel=3)
    )
    wSVersionVendor: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=weihenstephan;i=6010", browseName="ns=weihenstephan;WSVersionVendor", dataType=o6.String, accessLevel=3)
    )
    warnings: di.objtypes.FunctionalGroupType | None = o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=weihenstephan;i=5011", browseName="ns=weihenstephan;Warnings"))


@o6.objecttype(nodeId="ns=weihenstephan;i=1001", browseName="ns=weihenstephan;WSBaseObjectType", displayName="WSBaseObjectType")
class WSBaseObjectType(ns0.objtypes.BaseObjectType):
    wSTagNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=weihenstephan;i=6015", browseName="ns=weihenstephan;WSTagNumber", dataType=o6.UInt16, accessLevel=3)
    )


@o6.objecttype(nodeId="ns=weihenstephan;i=1002", browseName="ns=weihenstephan;WSAlarmType", displayName="WSAlarmType")
class WSAlarmType(WSBaseObjectType):
    wSAlarmCode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=weihenstephan;i=6016", browseName="ns=weihenstephan;WSAlarmCode", dataType=o6.UInt32, accessLevel=3)
    )
    wSAlarmMessage: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=weihenstephan;i=6017", browseName="ns=weihenstephan;WSAlarmMessage", dataType=o6.LocalizedText, accessLevel=3)
    )


@o6.objecttype(nodeId="ns=weihenstephan;i=1003", browseName="ns=weihenstephan;WSWarningType", displayName="WSWarningType")
class WSWarningType(WSBaseObjectType):
    wSWarningCode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=weihenstephan;i=6018", browseName="ns=weihenstephan;WSWarningCode", dataType=o6.UInt32, accessLevel=3)
    )
    wSWarningMessage: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=weihenstephan;i=6019", browseName="ns=weihenstephan;WSWarningMessage", dataType=o6.LocalizedText, accessLevel=3)
    )


@o6.objecttype(nodeId="ns=weihenstephan;i=1004", browseName="ns=weihenstephan;WSBaseStateMachineType", displayName="WSBaseStateMachineType")
class WSBaseStateMachineType(pack_ml.objtypes.PackMLBaseStateMachineType):
    wSTagNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=weihenstephan;i=6020", browseName="ns=weihenstephan;WSTagNumber", dataType=o6.UInt16, accessLevel=3)
    )


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, pack_ml, weihenstephan_datypes, weihenstephan_vartypes
