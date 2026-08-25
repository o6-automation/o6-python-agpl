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

"""Generated OPC UA adi namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as adi_reftypes
from . import datatypes as adi_datypes
from . import vartypes as adi_vartypes
from . import objtypes as adi_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=9444",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=adi;i=9443",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ConfigData", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=adi;i=9443", browseName="ns=adi;GetConfiguration", outputArgs=o6.hasProperty(o6.ns["ns=adi;i=9444"]))

ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=9446",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=adi;i=9445",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ConfigData", dataType=o6.ByteString, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=9447",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=adi;i=9445",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ConfigDataDigest", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=adi;i=9445", browseName="ns=adi;SetConfiguration", inputArgs=o6.hasProperty(o6.ns["ns=adi;i=9446"]), outputArgs=o6.hasProperty(o6.ns["ns=adi;i=9447"]))

ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=9449",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=adi;i=9448",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ConfigDataDigest", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=adi;i=9448", browseName="ns=adi;GetConfigDataDigest", outputArgs=o6.hasProperty(o6.ns["ns=adi;i=9449"]))

ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=9451",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=adi;i=9450",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ConfigDataDigest", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=9452",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=adi;i=9450",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="IsEqual", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=adi;i=9450", browseName="ns=adi;CompareConfigDataDigest", inputArgs=o6.hasProperty(o6.ns["ns=adi;i=9451"]), outputArgs=o6.hasProperty(o6.ns["ns=adi;i=9452"]))

o6.call(
    nodeId="ns=adi;i=9457",
    browseName="ns=adi;GotoOperating",
    description="AnalyserDeviceStateMachine to go to Operating state, forcing all AnalyserChannels to leave the SlaveMode state and go to the Operating state.",
)

o6.call(
    nodeId="ns=adi;i=9458",
    browseName="ns=adi;GotoMaintenance",
    description="AnalyserDeviceStateMachine to go to Maintenance state, forcing all AnalyserChannels to SlaveMode state.",
)

ns0.objtypes.BaseObjectType(
    nodeId="ns=adi;i=9382",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=adi;i=9443"]),
        o6.hasComponent(o6.ns["ns=adi;i=9445"]),
        o6.hasComponent(o6.ns["ns=adi;i=9448"]),
        o6.hasComponent(o6.ns["ns=adi;i=9450"]),
        o6.hasComponent(o6.call(nodeId="ns=adi;i=9453", browseName="ns=adi;ResetAllChannels", description="Reset all AnalyserChannels belonging to this AnalyserDevice.")),
        o6.hasComponent(o6.call(nodeId="ns=adi;i=9454", browseName="ns=adi;StartAllChannels", description="Start all AnalyserChannels belonging to this AnalyserDevice.")),
        o6.hasComponent(o6.call(nodeId="ns=adi;i=9455", browseName="ns=adi;StopAllChannels", description="Stop all AnalyserChannels belonging to this AnalyserDevice.")),
        o6.hasComponent(o6.call(nodeId="ns=adi;i=9456", browseName="ns=adi;AbortAllChannels", description="Abort all AnalyserChannels belonging to this AnalyserDevice.")),
        o6.hasComponent(o6.ns["ns=adi;i=9457"]),
        o6.hasComponent(o6.ns["ns=adi;i=9458"]),
    ],
)
o6.reference(adi_objtypes.AnalyserDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9382"])
ns0.vartypes.DataItemType(
    nodeId="ns=adi;i=9459", browseName="ns=adi;DiagnosticStatus", description="General health status of the analyser", dataType=di.datatypes.DeviceHealthEnumeration
)
o6.reference(o6.ns["ns=adi;i=5001"], "i=47", o6.ns["ns=adi;i=9459"])


ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=9468",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=adi;i=9467",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=9469",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=adi;i=9467",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=adi;i=9467", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=adi;i=9468"]), outputArgs=o6.hasProperty(o6.ns["ns=adi;i=9469"]))

ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=9471",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=adi;i=9470",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=adi;i=9470", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=adi;i=9471"]))

ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=9473",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=adi;i=9472",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=9474",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=adi;i=9472",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=adi;i=9472", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=adi;i=9473"]), outputArgs=o6.hasProperty(o6.ns["ns=adi;i=9474"]))

ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=9476",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=adi;i=9475",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=adi;i=9475", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=adi;i=9476"]))

ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=9478",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=adi;i=9477",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=9479",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=adi;i=9477",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=adi;i=9477", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=adi;i=9478"]), outputArgs=o6.hasProperty(o6.ns["ns=adi;i=9479"]))

ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=9481",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=adi;i=9480",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=adi;i=9480", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=adi;i=9481"]))

di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=9484", browseName="ns=adi;Status", modellingRule="Mandatory", references=[o6.organizes(o6.ns["ns=adi;i=9459"])])
o6.reference(adi_objtypes.AnalyserDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9484"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=adi;i=9489",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9490", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
adi_objtypes.AnalyserDeviceStateMachineType(
    nodeId="ns=adi;i=9488", browseName="ns=adi;AnalyserStateMachine", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=adi;i=9489"])]
)
o6.reference(adi_objtypes.AnalyserDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9488"])


ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=9524",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=adi;i=9523",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ExecutionCycle", dataType=o6.NodeId("ns=adi;i=9378"), valueRank=-1),
        ns0.datatypes.Argument(name="ExecutionCycleSubcode", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="SelectedStream", dataType=o6.String, valueRank=-1),
    ],
)
o6.call(nodeId="ns=adi;i=9523", browseName="ns=adi;StartSingleAcquisition", inputArgs=o6.hasProperty(o6.ns["ns=adi;i=9524"]))

ns0.objtypes.BaseObjectType(
    nodeId="ns=adi;i=9503",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    references=[
        o6.hasComponent(o6.call(nodeId="ns=adi;i=9521", browseName="ns=adi;GotoOperating", description="Transitions the AnalyserChannel to Operating mode.")),
        o6.hasComponent(o6.call(nodeId="ns=adi;i=9522", browseName="ns=adi;GotoMaintenance", description="Transitions the AnalyserChannel to Maintenance mode.")),
        o6.hasComponent(o6.ns["ns=adi;i=9523"]),
        o6.hasComponent(o6.call(nodeId="ns=adi;i=9525", browseName="ns=adi;Reset", description="Causes transition to the Resetting state.")),
        o6.hasComponent(o6.call(nodeId="ns=adi;i=9526", browseName="ns=adi;Start", description="Causes transition to the Starting state.")),
        o6.hasComponent(o6.call(nodeId="ns=adi;i=9527", browseName="ns=adi;Stop", description="Causes transition to the Stopping state.")),
        o6.hasComponent(o6.call(nodeId="ns=adi;i=9528", browseName="ns=adi;Hold", description="Causes transition to the Holding state.")),
        o6.hasComponent(o6.call(nodeId="ns=adi;i=9529", browseName="ns=adi;Unhold", description="Causes transition to the Unholding state.")),
        o6.hasComponent(o6.call(nodeId="ns=adi;i=9530", browseName="ns=adi;Suspend", description="Causes transition to the Suspending state.")),
        o6.hasComponent(o6.call(nodeId="ns=adi;i=9531", browseName="ns=adi;Unsuspend", description="Causes transition to the Unsuspending state.")),
        o6.hasComponent(o6.call(nodeId="ns=adi;i=9532", browseName="ns=adi;Abort", description="Causes transition to the Aborting state.")),
        o6.hasComponent(o6.call(nodeId="ns=adi;i=9533", browseName="ns=adi;Clear", description="Causes transition to the Clearing state.")),
    ],
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=adi;i=9551",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9552", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=adi;i=9563",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9564", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=adi;i=9575",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9576", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType(
    nodeId="ns=adi;i=9574", browseName="ns=adi;OperatingExecuteSubStateMachine", references=[o6.hasComponent(o6.ns["ns=adi;i=9575"])]
)
adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType(
    nodeId="ns=adi;i=9562", browseName="ns=adi;OperatingSubStateMachine", references=[o6.hasComponent(o6.ns["ns=adi;i=9563"]), o6.hasComponent(o6.ns["ns=adi;i=9574"])]
)
adi_objtypes.AnalyserChannelStateMachineType(
    nodeId="ns=adi;i=9550", browseName="ns=adi;ChannelStateMachine", references=[o6.hasComponent(o6.ns["ns=adi;i=9551"]), o6.hasComponent(o6.ns["ns=adi;i=9562"])], eventNotifier=1
)
adi_objtypes.AnalyserChannelType(
    nodeId="ns=adi;i=9500",
    browseName="ns=adi;<ChannelIdentifier>",
    description="Channel definition",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=adi;i=9503"]),
        o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=9546", browseName="ns=adi;Configuration")),
        o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=9548", browseName="ns=adi;Status")),
        o6.hasComponent(o6.ns["ns=adi;i=9550"]),
    ],
)
o6.reference(adi_objtypes.AnalyserDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9500"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=adi;i=9615",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9616", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
adi_objtypes.AccessorySlotStateMachineType(nodeId="ns=adi;i=9614", browseName="ns=adi;AccessorySlotStateMachine", references=[o6.hasComponent(o6.ns["ns=adi;i=9615"])])
adi_objtypes.AccessorySlotType(
    nodeId="ns=adi;i=9610",
    browseName="ns=adi;<AccessorySlotIdentifier>",
    description="AccessorySlot definition",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=adi;i=9612",
                browseName="ns=adi;IsHotSwappable",
                description="True if an accessory can be inserted in the accessory slot while it is powered",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=adi;i=9613", browseName="ns=adi;IsEnabled", description="True if this accessory slot is capable of accepting an accessory in it", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=adi;i=9611",
                browseName="ns=di;SupportedTypes",
                description="Folder maintaining the set of (sub-types of) BaseObjectTypes that can be instantiated in the ConfigurableComponent",
            )
        ),
        o6.hasComponent(o6.ns["ns=adi;i=9614"]),
    ],
)
o6.reference(adi_objtypes.AnalyserDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9610"])
ns0.objtypes.InitialStateType(
    nodeId="ns=adi;i=9647",
    browseName="ns=adi;Powerup",
    description="The AnalyserDevice is in its power-up sequence and cannot perform any other task.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9648", browseName="StateNumber", dataType=o6.UInt32, value=100))],
)
o6.reference(adi_objtypes.AnalyserDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9647"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=9649",
    browseName="ns=adi;Operating",
    description="The AnalyserDevice is in the Operating mode.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9650", browseName="StateNumber", dataType=o6.UInt32, value=200))],
)
o6.reference(adi_objtypes.AnalyserDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9649"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=9651",
    browseName="ns=adi;Local",
    description="The AnalyserDevice is in the Local mode. This mode is normally used to perform local physical maintenance on the analyser.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9652", browseName="StateNumber", dataType=o6.UInt32, value=300))],
)
o6.reference(adi_objtypes.AnalyserDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9651"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=9653",
    browseName="ns=adi;Maintenance",
    description="The AnalyserDevice is in the Maintenance mode. This mode is used to perform remote maintenance on the analyser like firmware upgrade.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9654", browseName="StateNumber", dataType=o6.UInt32, value=400))],
)
o6.reference(adi_objtypes.AnalyserDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9653"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=9655",
    browseName="ns=adi;Shutdown",
    description="The AnalyserDevice is in its power-down sequence and cannot perform any other task.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9656", browseName="StateNumber", dataType=o6.UInt32, value=500))],
)
o6.reference(adi_objtypes.AnalyserDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9655"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=9657",
    browseName="ns=adi;PowerupToOperatingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9658", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(adi_objtypes.AnalyserDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9657"])
o6.reference(o6.ns["ns=adi;i=9657"], "i=51", o6.ns["ns=adi;i=9647"])
o6.reference(o6.ns["ns=adi;i=9657"], "i=52", o6.ns["ns=adi;i=9649"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=9659",
    browseName="ns=adi;OperatingToLocalTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9660", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(adi_objtypes.AnalyserDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9659"])
o6.reference(o6.ns["ns=adi;i=9659"], "i=51", o6.ns["ns=adi;i=9649"])
o6.reference(o6.ns["ns=adi;i=9659"], "i=52", o6.ns["ns=adi;i=9651"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=9661",
    browseName="ns=adi;OperatingToMaintenanceTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9662", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(adi_objtypes.AnalyserDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9661"])
o6.reference(o6.ns["ns=adi;i=9661"], "i=51", o6.ns["ns=adi;i=9649"])
o6.reference(o6.ns["ns=adi;i=9661"], "i=52", o6.ns["ns=adi;i=9653"])
o6.reference(o6.ns["ns=adi;i=9661"], "i=53", o6.ns["ns=adi;i=9458"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=9663",
    browseName="ns=adi;LocalToOperatingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9664", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(adi_objtypes.AnalyserDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9663"])
o6.reference(o6.ns["ns=adi;i=9663"], "i=51", o6.ns["ns=adi;i=9651"])
o6.reference(o6.ns["ns=adi;i=9663"], "i=52", o6.ns["ns=adi;i=9649"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=9665",
    browseName="ns=adi;LocalToMaintenanceTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9666", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(adi_objtypes.AnalyserDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9665"])
o6.reference(o6.ns["ns=adi;i=9665"], "i=51", o6.ns["ns=adi;i=9651"])
o6.reference(o6.ns["ns=adi;i=9665"], "i=52", o6.ns["ns=adi;i=9653"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=9667",
    browseName="ns=adi;MaintenanceToOperatingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9668", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(adi_objtypes.AnalyserDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9667"])
o6.reference(o6.ns["ns=adi;i=9667"], "i=51", o6.ns["ns=adi;i=9653"])
o6.reference(o6.ns["ns=adi;i=9667"], "i=52", o6.ns["ns=adi;i=9649"])
o6.reference(o6.ns["ns=adi;i=9667"], "i=53", o6.ns["ns=adi;i=9457"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=9669",
    browseName="ns=adi;MaintenanceToLocalTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9670", browseName="TransitionNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(adi_objtypes.AnalyserDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9669"])
o6.reference(o6.ns["ns=adi;i=9669"], "i=51", o6.ns["ns=adi;i=9653"])
o6.reference(o6.ns["ns=adi;i=9669"], "i=52", o6.ns["ns=adi;i=9651"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=9671",
    browseName="ns=adi;OperatingToShutdownTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9672", browseName="TransitionNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(adi_objtypes.AnalyserDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9671"])
o6.reference(o6.ns["ns=adi;i=9671"], "i=51", o6.ns["ns=adi;i=9649"])
o6.reference(o6.ns["ns=adi;i=9671"], "i=52", o6.ns["ns=adi;i=9655"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=9673",
    browseName="ns=adi;LocalToShutdownTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9674", browseName="TransitionNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(adi_objtypes.AnalyserDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9673"])
o6.reference(o6.ns["ns=adi;i=9673"], "i=51", o6.ns["ns=adi;i=9651"])
o6.reference(o6.ns["ns=adi;i=9673"], "i=52", o6.ns["ns=adi;i=9655"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=9675",
    browseName="ns=adi;MaintenanceToShutdownTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9676", browseName="TransitionNumber", dataType=o6.UInt32, value=10))],
)
o6.reference(adi_objtypes.AnalyserDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9675"])
o6.reference(o6.ns["ns=adi;i=9675"], "i=51", o6.ns["ns=adi;i=9653"])
o6.reference(o6.ns["ns=adi;i=9675"], "i=52", o6.ns["ns=adi;i=9655"])


o6.call(nodeId="ns=adi;i=9699", browseName="ns=adi;GotoOperating", description="Transitions the AnalyserChannel to Operating mode.")

o6.call(nodeId="ns=adi;i=9700", browseName="ns=adi;GotoMaintenance", description="Transitions the AnalyserChannel to Maintenance mode.")

ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=9702",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=adi;i=9701",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ExecutionCycle", dataType=o6.NodeId("ns=adi;i=9378"), valueRank=-1),
        ns0.datatypes.Argument(name="ExecutionCycleSubcode", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="SelectedStream", dataType=o6.String, valueRank=-1),
    ],
)
o6.call(nodeId="ns=adi;i=9701", browseName="ns=adi;StartSingleAcquisition", inputArgs=o6.hasProperty(o6.ns["ns=adi;i=9702"]))

o6.call(nodeId="ns=adi;i=9703", browseName="ns=adi;Reset", description="Causes transition to the Resetting state.")

o6.call(nodeId="ns=adi;i=9704", browseName="ns=adi;Start", description="Causes transition to the Starting state.")

o6.call(nodeId="ns=adi;i=9705", browseName="ns=adi;Stop", description="Causes transition to the Stopping state.")

o6.call(nodeId="ns=adi;i=9706", browseName="ns=adi;Hold", description="Causes transition to the Holding state.")

o6.call(nodeId="ns=adi;i=9707", browseName="ns=adi;Unhold", description="Causes transition to the Unholding state.")

o6.call(nodeId="ns=adi;i=9708", browseName="ns=adi;Suspend", description="Causes transition to the Suspending state.")

o6.call(nodeId="ns=adi;i=9709", browseName="ns=adi;Unsuspend", description="Causes transition to the Unsuspending state.")

o6.call(nodeId="ns=adi;i=9710", browseName="ns=adi;Abort", description="Causes transition to the Aborting state.")

o6.call(nodeId="ns=adi;i=9711", browseName="ns=adi;Clear", description="Causes transition to the Clearing state.")

ns0.objtypes.BaseObjectType(
    nodeId="ns=adi;i=9679",
    browseName="ns=di;MethodSet",
    description="Flat list of Methods",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=adi;i=9699"]),
        o6.hasComponent(o6.ns["ns=adi;i=9700"]),
        o6.hasComponent(o6.ns["ns=adi;i=9701"]),
        o6.hasComponent(o6.ns["ns=adi;i=9703"]),
        o6.hasComponent(o6.ns["ns=adi;i=9704"]),
        o6.hasComponent(o6.ns["ns=adi;i=9705"]),
        o6.hasComponent(o6.ns["ns=adi;i=9706"]),
        o6.hasComponent(o6.ns["ns=adi;i=9707"]),
        o6.hasComponent(o6.ns["ns=adi;i=9708"]),
        o6.hasComponent(o6.ns["ns=adi;i=9709"]),
        o6.hasComponent(o6.ns["ns=adi;i=9710"]),
        o6.hasComponent(o6.ns["ns=adi;i=9711"]),
    ],
)
o6.reference(adi_objtypes.AnalyserChannelType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9679"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=adi;i=9677",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Optional",
    references=[o6.hasComponent(ns0.vartypes.DataItemType(nodeId="ns=adi;i=9712", browseName="ns=adi;ChannelId", description="Channel Id defined by user", dataType=o6.String))],
)
o6.reference(adi_objtypes.AnalyserChannelType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9677"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=9715", browseName="ns=adi;IsEnabled", description="True if the channel is enabled and accepting commands", dataType=o6.Boolean)
o6.reference(o6.ns["ns=adi;i=9677"], "i=47", o6.ns["ns=adi;i=9715"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=9718", browseName="ns=adi;DiagnosticStatus", description="AnalyserChannel health status", dataType=di.datatypes.DeviceHealthEnumeration)
o6.reference(o6.ns["ns=adi;i=9677"], "i=47", o6.ns["ns=adi;i=9718"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=9721", browseName="ns=adi;ActiveStream", description="Active stream for this AnalyserChannel", dataType=o6.String)
o6.reference(o6.ns["ns=adi;i=9677"], "i=47", o6.ns["ns=adi;i=9721"])
di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=9724", browseName="ns=adi;Configuration", modellingRule="Mandatory", references=[o6.organizes(o6.ns["ns=adi;i=9715"])])
o6.reference(adi_objtypes.AnalyserChannelType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9724"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=adi;i=9726", browseName="ns=adi;Status", modellingRule="Mandatory", references=[o6.organizes(o6.ns["ns=adi;i=9718"]), o6.organizes(o6.ns["ns=adi;i=9721"])]
)
o6.reference(adi_objtypes.AnalyserChannelType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9726"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=adi;i=9729",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9730", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=adi;i=9741",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9742", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=adi;i=9753",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9754", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType(
    nodeId="ns=adi;i=9752", browseName="ns=adi;OperatingExecuteSubStateMachine", references=[o6.hasComponent(o6.ns["ns=adi;i=9753"])]
)
adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType(
    nodeId="ns=adi;i=9740", browseName="ns=adi;OperatingSubStateMachine", references=[o6.hasComponent(o6.ns["ns=adi;i=9741"]), o6.hasComponent(o6.ns["ns=adi;i=9752"])]
)
adi_objtypes.AnalyserChannelStateMachineType(
    nodeId="ns=adi;i=9728",
    browseName="ns=adi;ChannelStateMachine",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=adi;i=9729"]), o6.hasComponent(o6.ns["ns=adi;i=9740"])],
    eventNotifier=1,
)
o6.reference(adi_objtypes.AnalyserChannelType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9728"])
adi_objtypes.StreamType(
    nodeId="ns=adi;i=9790",
    browseName="ns=adi;<StreamIdentifier>",
    description="Stream definition",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=9902", browseName="ns=adi;Configuration")),
        o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=9904", browseName="ns=adi;Status")),
        o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=9906", browseName="ns=adi;AcquisitionSettings")),
        o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=9908", browseName="ns=adi;AcquisitionStatus")),
        o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=9910", browseName="ns=adi;AcquisitionData")),
        o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=9912", browseName="ns=adi;ChemometricModelSettings")),
        o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=9914", browseName="ns=adi;Context")),
    ],
)
o6.reference(adi_objtypes.AnalyserChannelType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9790"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=adi;i=9921",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9922", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
adi_objtypes.AccessorySlotStateMachineType(nodeId="ns=adi;i=9920", browseName="ns=adi;AccessorySlotStateMachine", references=[o6.hasComponent(o6.ns["ns=adi;i=9921"])])
adi_objtypes.AccessorySlotType(
    nodeId="ns=adi;i=9916",
    browseName="ns=adi;<AccessorySlotIdentifier>",
    description="AccessorySlot definition",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=adi;i=9918",
                browseName="ns=adi;IsHotSwappable",
                description="True if an accessory can be inserted in the accessory slot while it is powered",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=adi;i=9919", browseName="ns=adi;IsEnabled", description="True if this accessory slot is capable of accepting an accessory in it", dataType=o6.Boolean
            )
        ),
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=adi;i=9917",
                browseName="ns=di;SupportedTypes",
                description="Folder maintaining the set of (sub-types of) BaseObjectTypes that can be instantiated in the ConfigurableComponent",
            )
        ),
        o6.hasComponent(o6.ns["ns=adi;i=9920"]),
    ],
)
o6.reference(adi_objtypes.AnalyserChannelType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9916"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=adi;i=9949",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9950", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=adi;i=9961",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9962", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType(
    nodeId="ns=adi;i=9960", browseName="ns=adi;OperatingExecuteSubStateMachine", references=[o6.hasComponent(o6.ns["ns=adi;i=9961"])]
)
adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType(
    nodeId="ns=adi;i=9948",
    browseName="ns=adi;OperatingSubStateMachine",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=adi;i=9949"]), o6.hasComponent(o6.ns["ns=adi;i=9960"])],
)
o6.reference(adi_objtypes.AnalyserChannelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9948"])
o6.reference(adi_objtypes.AnalyserChannelOperatingStateType, "i=117", "ns=adi;i=9948")
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=adi;i=9973",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9974", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.objtypes.FiniteStateMachineType(
    nodeId="ns=adi;i=9972", browseName="ns=adi;LocalSubStateMachine", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=adi;i=9973"])], _allow_abstract=True
)
o6.reference(adi_objtypes.AnalyserChannelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9972"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=adi;i=9985",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9986", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.objtypes.FiniteStateMachineType(
    nodeId="ns=adi;i=9984", browseName="ns=adi;MaintenanceSubStateMachine", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=adi;i=9985"])], _allow_abstract=True
)
o6.reference(adi_objtypes.AnalyserChannelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9984"])
ns0.objtypes.InitialStateType(
    nodeId="ns=adi;i=9996",
    browseName="ns=adi;SlaveMode",
    description="The AnalyserDevice is in Local or Maintenance mode and all AnalyserChannels are in SlaveMode",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9997", browseName="StateNumber", dataType=o6.UInt32, value=100))],
)
o6.reference(adi_objtypes.AnalyserChannelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9996"])
adi_objtypes.AnalyserChannelOperatingStateType(
    nodeId="ns=adi;i=9998",
    browseName="ns=adi;Operating",
    description="The AnalyserChannel is in the Operating mode.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9999", browseName="StateNumber", dataType=o6.UInt32, value=200))],
    eventNotifier=1,
)
o6.reference(adi_objtypes.AnalyserChannelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9998"])
o6.reference(o6.ns["ns=adi;i=9998"], "i=117", o6.ns["ns=adi;i=9948"])
adi_objtypes.AnalyserChannelLocalStateType(
    nodeId="ns=adi;i=10000",
    browseName="ns=adi;Local",
    description="The AnalyserChannel is in the Local mode. This mode is normally used to perform local physical maintenance on the analyser.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10001", browseName="StateNumber", dataType=o6.UInt32, value=300))],
)
o6.reference(adi_objtypes.AnalyserChannelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10000"])
o6.reference(o6.ns["ns=adi;i=10000"], "i=117", o6.ns["ns=adi;i=9972"])
adi_objtypes.AnalyserChannelMaintenanceStateType(
    nodeId="ns=adi;i=10002",
    browseName="ns=adi;Maintenance",
    description="The AnalyserChannel is in the Maintenance mode. This mode is used to perform remote maintenance on the analyser like firmware upgrade.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10003", browseName="StateNumber", dataType=o6.UInt32, value=400))],
)
o6.reference(adi_objtypes.AnalyserChannelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10002"])
o6.reference(o6.ns["ns=adi;i=10002"], "i=117", o6.ns["ns=adi;i=9984"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10004",
    browseName="ns=adi;SlaveModeToOperatingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10005", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(adi_objtypes.AnalyserChannelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10004"])
o6.reference(o6.ns["ns=adi;i=10004"], "i=51", o6.ns["ns=adi;i=9996"])
o6.reference(o6.ns["ns=adi;i=10004"], "i=52", o6.ns["ns=adi;i=9998"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10006",
    browseName="ns=adi;OperatingToLocalTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10007", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(adi_objtypes.AnalyserChannelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10006"])
o6.reference(o6.ns["ns=adi;i=10006"], "i=51", o6.ns["ns=adi;i=9998"])
o6.reference(o6.ns["ns=adi;i=10006"], "i=52", o6.ns["ns=adi;i=10000"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10008",
    browseName="ns=adi;OperatingToMaintenanceTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10009", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(adi_objtypes.AnalyserChannelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10008"])
o6.reference(o6.ns["ns=adi;i=10008"], "i=51", o6.ns["ns=adi;i=9998"])
o6.reference(o6.ns["ns=adi;i=10008"], "i=52", o6.ns["ns=adi;i=10002"])
o6.reference(o6.ns["ns=adi;i=10008"], "i=53", o6.ns["ns=adi;i=9700"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10010",
    browseName="ns=adi;LocalToOperatingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10011", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(adi_objtypes.AnalyserChannelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10010"])
o6.reference(o6.ns["ns=adi;i=10010"], "i=51", o6.ns["ns=adi;i=10000"])
o6.reference(o6.ns["ns=adi;i=10010"], "i=52", o6.ns["ns=adi;i=9998"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10012",
    browseName="ns=adi;LocalToMaintenanceTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10013", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(adi_objtypes.AnalyserChannelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10012"])
o6.reference(o6.ns["ns=adi;i=10012"], "i=51", o6.ns["ns=adi;i=10000"])
o6.reference(o6.ns["ns=adi;i=10012"], "i=52", o6.ns["ns=adi;i=10002"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10014",
    browseName="ns=adi;MaintenanceToOperatingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10015", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(adi_objtypes.AnalyserChannelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10014"])
o6.reference(o6.ns["ns=adi;i=10014"], "i=51", o6.ns["ns=adi;i=10002"])
o6.reference(o6.ns["ns=adi;i=10014"], "i=52", o6.ns["ns=adi;i=9998"])
o6.reference(o6.ns["ns=adi;i=10014"], "i=53", o6.ns["ns=adi;i=9699"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10016",
    browseName="ns=adi;MaintenanceToLocalTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10017", browseName="TransitionNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(adi_objtypes.AnalyserChannelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10016"])
o6.reference(o6.ns["ns=adi;i=10016"], "i=51", o6.ns["ns=adi;i=10002"])
o6.reference(o6.ns["ns=adi;i=10016"], "i=52", o6.ns["ns=adi;i=10000"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10018",
    browseName="ns=adi;OperatingToSlaveModeTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10019", browseName="TransitionNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(adi_objtypes.AnalyserChannelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10018"])
o6.reference(o6.ns["ns=adi;i=10018"], "i=51", o6.ns["ns=adi;i=9998"])
o6.reference(o6.ns["ns=adi;i=10018"], "i=52", o6.ns["ns=adi;i=9996"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10020",
    browseName="ns=adi;LocalToSlaveModeTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10021", browseName="TransitionNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(adi_objtypes.AnalyserChannelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10020"])
o6.reference(o6.ns["ns=adi;i=10020"], "i=51", o6.ns["ns=adi;i=10000"])
o6.reference(o6.ns["ns=adi;i=10020"], "i=52", o6.ns["ns=adi;i=9996"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10022",
    browseName="ns=adi;MaintenanceToSlaveModeTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10023", browseName="TransitionNumber", dataType=o6.UInt32, value=10))],
)
o6.reference(adi_objtypes.AnalyserChannelStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10022"])
o6.reference(o6.ns["ns=adi;i=10022"], "i=51", o6.ns["ns=adi;i=10002"])
o6.reference(o6.ns["ns=adi;i=10022"], "i=52", o6.ns["ns=adi;i=9996"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=adi;i=10037",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10038", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType(
    nodeId="ns=adi;i=10036", browseName="ns=adi;OperatingExecuteSubStateMachine", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=adi;i=10037"])]
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10036"])
o6.reference(adi_objtypes.AnalyserChannelOperatingExecuteStateType, "i=117", "ns=adi;i=10036")
ns0.objtypes.InitialStateType(
    nodeId="ns=adi;i=10048",
    browseName="ns=adi;Stopped",
    description="This is the initial state after AnalyserDeviceStateMachine state Powerup",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10049", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10048"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10050",
    browseName="ns=adi;Resetting",
    description="This state is the result of a Reset or SetConfiguration Method call from the Stopped state.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10051", browseName="StateNumber", dataType=o6.UInt32, value=15))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10050"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10052",
    browseName="ns=adi;Idle",
    description="The Resetting state is completed, all parameters have been committed and ready to start acquisition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10053", browseName="StateNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10052"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10054",
    browseName="ns=adi;Starting",
    description="The analyser has received the Start or SingleAcquisitionStart Method call and it is preparing to enter in Execute state.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10055", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10054"])
adi_objtypes.AnalyserChannelOperatingExecuteStateType(
    nodeId="ns=adi;i=10056",
    browseName="ns=adi;Execute",
    description="All repetitive acquisition cycles are done in this state:",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10057", browseName="StateNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10056"])
o6.reference(o6.ns["ns=adi;i=10056"], "i=117", o6.ns["ns=adi;i=10036"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10058",
    browseName="ns=adi;Completing",
    description="This state is an automatic or commanded exit from the Execute state.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10059", browseName="StateNumber", dataType=o6.UInt32, value=16))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10058"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10060",
    browseName="ns=adi;Complete",
    description="At this point, the Completing state is done and it transitions automatically to Stopped state to wait.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10061", browseName="StateNumber", dataType=o6.UInt32, value=17))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10060"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10062",
    browseName="ns=adi;Suspending",
    description="This state is a result of a change in monitored conditions due to process conditions or factors.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10063", browseName="StateNumber", dataType=o6.UInt32, value=13))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10062"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10064",
    browseName="ns=adi;Suspended",
    description="The analyser or channel may be running but no results are being generated while the analyser or channel is waiting for external process conditions to return to normal.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10065", browseName="StateNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10064"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10066",
    browseName="ns=adi;Unsuspending",
    description="This state is a result of a device request from Suspended state to transition back to the Execute state by calling the Unsuspend Method.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10067", browseName="StateNumber", dataType=o6.UInt32, value=14))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10066"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10068",
    browseName="ns=adi;Holding",
    description="Brings the analyser or channel to a controlled stop or to a state which represents Held for the particular unit control mode",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10069", browseName="StateNumber", dataType=o6.UInt32, value=10))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10068"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10070",
    browseName="ns=adi;Held",
    description="The Held state holds the analyser or channel's operation. At this state, no acquisition cycle is performed.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10071", browseName="StateNumber", dataType=o6.UInt32, value=11))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10070"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10072",
    browseName="ns=adi;Unholding",
    description="The Unholding state is a response to an operator command to resume the Execute state.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10073", browseName="StateNumber", dataType=o6.UInt32, value=12))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10072"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10074",
    browseName="ns=adi;Stopping",
    description="Initiated by a Stop Method call, this state:",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10075", browseName="StateNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10074"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10076",
    browseName="ns=adi;Aborting",
    description="The Aborting state can be entered at any time in response to the Abort command or on the occurrence of a machine fault.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10077", browseName="StateNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10076"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10078",
    browseName="ns=adi;Aborted",
    description="This state maintains machine status information relevant to the Abort condition.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10079", browseName="StateNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10078"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10080",
    browseName="ns=adi;Clearing",
    description="Clears faults that may have occurred when Aborting and are present in the Aborted state before proceeding to a Stopped state",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10081", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10080"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10082",
    browseName="ns=adi;StoppedToResettingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10083", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10082"])
o6.reference(o6.ns["ns=adi;i=10082"], "i=51", o6.ns["ns=adi;i=10048"])
o6.reference(o6.ns["ns=adi;i=10082"], "i=52", o6.ns["ns=adi;i=10050"])
o6.reference(o6.ns["ns=adi;i=10082"], "i=53", o6.ns["ns=adi;i=9445"])
o6.reference(o6.ns["ns=adi;i=10082"], "i=53", o6.ns["ns=adi;i=9703"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10084",
    browseName="ns=adi;ResettingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10085", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10084"])
o6.reference(o6.ns["ns=adi;i=10084"], "i=51", o6.ns["ns=adi;i=10050"])
o6.reference(o6.ns["ns=adi;i=10084"], "i=52", o6.ns["ns=adi;i=10050"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10086",
    browseName="ns=adi;ResettingToIdleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10087", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10086"])
o6.reference(o6.ns["ns=adi;i=10086"], "i=51", o6.ns["ns=adi;i=10050"])
o6.reference(o6.ns["ns=adi;i=10086"], "i=52", o6.ns["ns=adi;i=10052"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10088",
    browseName="ns=adi;IdleToStartingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10089", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10088"])
o6.reference(o6.ns["ns=adi;i=10088"], "i=51", o6.ns["ns=adi;i=10052"])
o6.reference(o6.ns["ns=adi;i=10088"], "i=52", o6.ns["ns=adi;i=10054"])
o6.reference(o6.ns["ns=adi;i=10088"], "i=53", o6.ns["ns=adi;i=9701"])
o6.reference(o6.ns["ns=adi;i=10088"], "i=53", o6.ns["ns=adi;i=9704"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10090",
    browseName="ns=adi;StartingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10091", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10090"])
o6.reference(o6.ns["ns=adi;i=10090"], "i=51", o6.ns["ns=adi;i=10054"])
o6.reference(o6.ns["ns=adi;i=10090"], "i=52", o6.ns["ns=adi;i=10054"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10092",
    browseName="ns=adi;StartingToExecuteTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10093", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10092"])
o6.reference(o6.ns["ns=adi;i=10092"], "i=51", o6.ns["ns=adi;i=10054"])
o6.reference(o6.ns["ns=adi;i=10092"], "i=52", o6.ns["ns=adi;i=10056"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10094",
    browseName="ns=adi;ExecuteToCompletingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10095", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10094"])
o6.reference(o6.ns["ns=adi;i=10094"], "i=51", o6.ns["ns=adi;i=10056"])
o6.reference(o6.ns["ns=adi;i=10094"], "i=52", o6.ns["ns=adi;i=10058"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10096",
    browseName="ns=adi;CompletingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10097", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10096"])
o6.reference(o6.ns["ns=adi;i=10096"], "i=51", o6.ns["ns=adi;i=10058"])
o6.reference(o6.ns["ns=adi;i=10096"], "i=52", o6.ns["ns=adi;i=10058"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10098",
    browseName="ns=adi;CompletingToCompleteTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10099", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10098"])
o6.reference(o6.ns["ns=adi;i=10098"], "i=51", o6.ns["ns=adi;i=10058"])
o6.reference(o6.ns["ns=adi;i=10098"], "i=52", o6.ns["ns=adi;i=10060"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10100",
    browseName="ns=adi;CompleteToStoppedTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10101", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=10))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10100"])
o6.reference(o6.ns["ns=adi;i=10100"], "i=51", o6.ns["ns=adi;i=10060"])
o6.reference(o6.ns["ns=adi;i=10100"], "i=52", o6.ns["ns=adi;i=10048"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10102",
    browseName="ns=adi;ExecuteToHoldingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10103", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=11))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10102"])
o6.reference(o6.ns["ns=adi;i=10102"], "i=51", o6.ns["ns=adi;i=10056"])
o6.reference(o6.ns["ns=adi;i=10102"], "i=52", o6.ns["ns=adi;i=10068"])
o6.reference(o6.ns["ns=adi;i=10102"], "i=53", o6.ns["ns=adi;i=9706"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10104",
    browseName="ns=adi;HoldingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10105", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=12))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10104"])
o6.reference(o6.ns["ns=adi;i=10104"], "i=51", o6.ns["ns=adi;i=10068"])
o6.reference(o6.ns["ns=adi;i=10104"], "i=52", o6.ns["ns=adi;i=10068"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10106",
    browseName="ns=adi;HoldingToHeldTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10107", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=13))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10106"])
o6.reference(o6.ns["ns=adi;i=10106"], "i=51", o6.ns["ns=adi;i=10068"])
o6.reference(o6.ns["ns=adi;i=10106"], "i=52", o6.ns["ns=adi;i=10070"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10108",
    browseName="ns=adi;HeldToUnholdingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10109", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=14))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10108"])
o6.reference(o6.ns["ns=adi;i=10108"], "i=51", o6.ns["ns=adi;i=10070"])
o6.reference(o6.ns["ns=adi;i=10108"], "i=52", o6.ns["ns=adi;i=10072"])
o6.reference(o6.ns["ns=adi;i=10108"], "i=53", o6.ns["ns=adi;i=9707"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10110",
    browseName="ns=adi;UnholdingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10111", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=15))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10110"])
o6.reference(o6.ns["ns=adi;i=10110"], "i=51", o6.ns["ns=adi;i=10072"])
o6.reference(o6.ns["ns=adi;i=10110"], "i=52", o6.ns["ns=adi;i=10072"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10112",
    browseName="ns=adi;UnholdingToHoldingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10113", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=16))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10112"])
o6.reference(o6.ns["ns=adi;i=10112"], "i=51", o6.ns["ns=adi;i=10072"])
o6.reference(o6.ns["ns=adi;i=10112"], "i=52", o6.ns["ns=adi;i=10068"])
o6.reference(o6.ns["ns=adi;i=10112"], "i=53", o6.ns["ns=adi;i=9706"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10114",
    browseName="ns=adi;UnholdingToExecuteTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10115", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=17))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10114"])
o6.reference(o6.ns["ns=adi;i=10114"], "i=51", o6.ns["ns=adi;i=10072"])
o6.reference(o6.ns["ns=adi;i=10114"], "i=52", o6.ns["ns=adi;i=10056"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10116",
    browseName="ns=adi;ExecuteToSuspendingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10117", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=18))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10116"])
o6.reference(o6.ns["ns=adi;i=10116"], "i=51", o6.ns["ns=adi;i=10056"])
o6.reference(o6.ns["ns=adi;i=10116"], "i=52", o6.ns["ns=adi;i=10062"])
o6.reference(o6.ns["ns=adi;i=10116"], "i=53", o6.ns["ns=adi;i=9708"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10118",
    browseName="ns=adi;SuspendingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10119", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=19))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10118"])
o6.reference(o6.ns["ns=adi;i=10118"], "i=51", o6.ns["ns=adi;i=10062"])
o6.reference(o6.ns["ns=adi;i=10118"], "i=52", o6.ns["ns=adi;i=10062"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10120",
    browseName="ns=adi;SuspendingToSuspendedTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10121", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=20))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10120"])
o6.reference(o6.ns["ns=adi;i=10120"], "i=51", o6.ns["ns=adi;i=10062"])
o6.reference(o6.ns["ns=adi;i=10120"], "i=52", o6.ns["ns=adi;i=10064"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10122",
    browseName="ns=adi;SuspendedToUnsuspendingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10123", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=21))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10122"])
o6.reference(o6.ns["ns=adi;i=10122"], "i=51", o6.ns["ns=adi;i=10064"])
o6.reference(o6.ns["ns=adi;i=10122"], "i=52", o6.ns["ns=adi;i=10066"])
o6.reference(o6.ns["ns=adi;i=10122"], "i=53", o6.ns["ns=adi;i=9709"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10124",
    browseName="ns=adi;UnsuspendingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10125", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=22))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10124"])
o6.reference(o6.ns["ns=adi;i=10124"], "i=51", o6.ns["ns=adi;i=10066"])
o6.reference(o6.ns["ns=adi;i=10124"], "i=52", o6.ns["ns=adi;i=10066"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10126",
    browseName="ns=adi;UnsuspendingToSuspendingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10127", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=23))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10126"])
o6.reference(o6.ns["ns=adi;i=10126"], "i=51", o6.ns["ns=adi;i=10066"])
o6.reference(o6.ns["ns=adi;i=10126"], "i=52", o6.ns["ns=adi;i=10062"])
o6.reference(o6.ns["ns=adi;i=10126"], "i=53", o6.ns["ns=adi;i=9708"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10128",
    browseName="ns=adi;UnsuspendingToExecuteTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10129", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=24))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10128"])
o6.reference(o6.ns["ns=adi;i=10128"], "i=51", o6.ns["ns=adi;i=10066"])
o6.reference(o6.ns["ns=adi;i=10128"], "i=52", o6.ns["ns=adi;i=10056"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10130",
    browseName="ns=adi;StoppingToStoppedTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10131", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=25))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10130"])
o6.reference(o6.ns["ns=adi;i=10130"], "i=51", o6.ns["ns=adi;i=10074"])
o6.reference(o6.ns["ns=adi;i=10130"], "i=52", o6.ns["ns=adi;i=10048"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10132",
    browseName="ns=adi;AbortingToAbortedTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10133", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=26))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10132"])
o6.reference(o6.ns["ns=adi;i=10132"], "i=51", o6.ns["ns=adi;i=10076"])
o6.reference(o6.ns["ns=adi;i=10132"], "i=52", o6.ns["ns=adi;i=10078"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10134",
    browseName="ns=adi;AbortedToClearingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10135", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=27))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10134"])
o6.reference(o6.ns["ns=adi;i=10134"], "i=51", o6.ns["ns=adi;i=10078"])
o6.reference(o6.ns["ns=adi;i=10134"], "i=52", o6.ns["ns=adi;i=10080"])
o6.reference(o6.ns["ns=adi;i=10134"], "i=53", o6.ns["ns=adi;i=9711"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10136",
    browseName="ns=adi;ClearingToStoppedTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10137", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=28))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10136"])
o6.reference(o6.ns["ns=adi;i=10136"], "i=51", o6.ns["ns=adi;i=10080"])
o6.reference(o6.ns["ns=adi;i=10136"], "i=52", o6.ns["ns=adi;i=10048"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10138",
    browseName="ns=adi;ResettingToStoppingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10139", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=29))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10138"])
o6.reference(o6.ns["ns=adi;i=10138"], "i=51", o6.ns["ns=adi;i=10050"])
o6.reference(o6.ns["ns=adi;i=10138"], "i=52", o6.ns["ns=adi;i=10074"])
o6.reference(o6.ns["ns=adi;i=10138"], "i=53", o6.ns["ns=adi;i=9705"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10140",
    browseName="ns=adi;IdleToStoppingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10141", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=30))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10140"])
o6.reference(o6.ns["ns=adi;i=10140"], "i=51", o6.ns["ns=adi;i=10052"])
o6.reference(o6.ns["ns=adi;i=10140"], "i=52", o6.ns["ns=adi;i=10074"])
o6.reference(o6.ns["ns=adi;i=10140"], "i=53", o6.ns["ns=adi;i=9705"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10142",
    browseName="ns=adi;StartingToStoppingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10143", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=31))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10142"])
o6.reference(o6.ns["ns=adi;i=10142"], "i=51", o6.ns["ns=adi;i=10054"])
o6.reference(o6.ns["ns=adi;i=10142"], "i=52", o6.ns["ns=adi;i=10074"])
o6.reference(o6.ns["ns=adi;i=10142"], "i=53", o6.ns["ns=adi;i=9705"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10144",
    browseName="ns=adi;ExecuteToStoppingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10145", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=32))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10144"])
o6.reference(o6.ns["ns=adi;i=10144"], "i=51", o6.ns["ns=adi;i=10056"])
o6.reference(o6.ns["ns=adi;i=10144"], "i=52", o6.ns["ns=adi;i=10074"])
o6.reference(o6.ns["ns=adi;i=10144"], "i=53", o6.ns["ns=adi;i=9705"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10146",
    browseName="ns=adi;CompletingToStoppingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10147", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=33))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10146"])
o6.reference(o6.ns["ns=adi;i=10146"], "i=51", o6.ns["ns=adi;i=10058"])
o6.reference(o6.ns["ns=adi;i=10146"], "i=52", o6.ns["ns=adi;i=10074"])
o6.reference(o6.ns["ns=adi;i=10146"], "i=53", o6.ns["ns=adi;i=9705"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10148",
    browseName="ns=adi;CompleteToStoppingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10149", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=34))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10148"])
o6.reference(o6.ns["ns=adi;i=10148"], "i=51", o6.ns["ns=adi;i=10060"])
o6.reference(o6.ns["ns=adi;i=10148"], "i=52", o6.ns["ns=adi;i=10074"])
o6.reference(o6.ns["ns=adi;i=10148"], "i=53", o6.ns["ns=adi;i=9705"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10150",
    browseName="ns=adi;SuspendingToStoppingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10151", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=35))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10150"])
o6.reference(o6.ns["ns=adi;i=10150"], "i=51", o6.ns["ns=adi;i=10062"])
o6.reference(o6.ns["ns=adi;i=10150"], "i=52", o6.ns["ns=adi;i=10074"])
o6.reference(o6.ns["ns=adi;i=10150"], "i=53", o6.ns["ns=adi;i=9705"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10152",
    browseName="ns=adi;SuspendedToStoppingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10153", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=36))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10152"])
o6.reference(o6.ns["ns=adi;i=10152"], "i=51", o6.ns["ns=adi;i=10064"])
o6.reference(o6.ns["ns=adi;i=10152"], "i=52", o6.ns["ns=adi;i=10074"])
o6.reference(o6.ns["ns=adi;i=10152"], "i=53", o6.ns["ns=adi;i=9705"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10154",
    browseName="ns=adi;UnsuspendingToStoppingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10155", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=37))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10154"])
o6.reference(o6.ns["ns=adi;i=10154"], "i=51", o6.ns["ns=adi;i=10066"])
o6.reference(o6.ns["ns=adi;i=10154"], "i=52", o6.ns["ns=adi;i=10074"])
o6.reference(o6.ns["ns=adi;i=10154"], "i=53", o6.ns["ns=adi;i=9705"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10156",
    browseName="ns=adi;HoldingToStoppingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10157", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=38))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10156"])
o6.reference(o6.ns["ns=adi;i=10156"], "i=51", o6.ns["ns=adi;i=10068"])
o6.reference(o6.ns["ns=adi;i=10156"], "i=52", o6.ns["ns=adi;i=10074"])
o6.reference(o6.ns["ns=adi;i=10156"], "i=53", o6.ns["ns=adi;i=9705"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10158",
    browseName="ns=adi;HeldToStoppingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10159", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=39))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10158"])
o6.reference(o6.ns["ns=adi;i=10158"], "i=51", o6.ns["ns=adi;i=10070"])
o6.reference(o6.ns["ns=adi;i=10158"], "i=52", o6.ns["ns=adi;i=10074"])
o6.reference(o6.ns["ns=adi;i=10158"], "i=53", o6.ns["ns=adi;i=9705"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10160",
    browseName="ns=adi;UnholdingToStoppingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10161", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=40))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10160"])
o6.reference(o6.ns["ns=adi;i=10160"], "i=51", o6.ns["ns=adi;i=10072"])
o6.reference(o6.ns["ns=adi;i=10160"], "i=52", o6.ns["ns=adi;i=10074"])
o6.reference(o6.ns["ns=adi;i=10160"], "i=53", o6.ns["ns=adi;i=9705"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10162",
    browseName="ns=adi;StoppedToAbortingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10163", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=41))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10162"])
o6.reference(o6.ns["ns=adi;i=10162"], "i=51", o6.ns["ns=adi;i=10048"])
o6.reference(o6.ns["ns=adi;i=10162"], "i=52", o6.ns["ns=adi;i=10076"])
o6.reference(o6.ns["ns=adi;i=10162"], "i=53", o6.ns["ns=adi;i=9710"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10164",
    browseName="ns=adi;ResettingToAbortingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10165", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=42))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10164"])
o6.reference(o6.ns["ns=adi;i=10164"], "i=51", o6.ns["ns=adi;i=10050"])
o6.reference(o6.ns["ns=adi;i=10164"], "i=52", o6.ns["ns=adi;i=10076"])
o6.reference(o6.ns["ns=adi;i=10164"], "i=53", o6.ns["ns=adi;i=9710"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10166",
    browseName="ns=adi;IdleToAbortingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10167", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=43))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10166"])
o6.reference(o6.ns["ns=adi;i=10166"], "i=51", o6.ns["ns=adi;i=10052"])
o6.reference(o6.ns["ns=adi;i=10166"], "i=52", o6.ns["ns=adi;i=10076"])
o6.reference(o6.ns["ns=adi;i=10166"], "i=53", o6.ns["ns=adi;i=9710"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10168",
    browseName="ns=adi;StartingToAbortingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10169", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=44))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10168"])
o6.reference(o6.ns["ns=adi;i=10168"], "i=51", o6.ns["ns=adi;i=10054"])
o6.reference(o6.ns["ns=adi;i=10168"], "i=52", o6.ns["ns=adi;i=10076"])
o6.reference(o6.ns["ns=adi;i=10168"], "i=53", o6.ns["ns=adi;i=9710"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10170",
    browseName="ns=adi;ExecuteToAbortingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10171", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=45))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10170"])
o6.reference(o6.ns["ns=adi;i=10170"], "i=51", o6.ns["ns=adi;i=10056"])
o6.reference(o6.ns["ns=adi;i=10170"], "i=52", o6.ns["ns=adi;i=10076"])
o6.reference(o6.ns["ns=adi;i=10170"], "i=53", o6.ns["ns=adi;i=9710"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10172",
    browseName="ns=adi;CompletingToAbortingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10173", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=46))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10172"])
o6.reference(o6.ns["ns=adi;i=10172"], "i=51", o6.ns["ns=adi;i=10058"])
o6.reference(o6.ns["ns=adi;i=10172"], "i=52", o6.ns["ns=adi;i=10076"])
o6.reference(o6.ns["ns=adi;i=10172"], "i=53", o6.ns["ns=adi;i=9710"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10174",
    browseName="ns=adi;CompleteToAbortingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10175", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=47))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10174"])
o6.reference(o6.ns["ns=adi;i=10174"], "i=51", o6.ns["ns=adi;i=10060"])
o6.reference(o6.ns["ns=adi;i=10174"], "i=52", o6.ns["ns=adi;i=10076"])
o6.reference(o6.ns["ns=adi;i=10174"], "i=53", o6.ns["ns=adi;i=9710"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10176",
    browseName="ns=adi;SuspendingToAbortingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10177", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=48))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10176"])
o6.reference(o6.ns["ns=adi;i=10176"], "i=51", o6.ns["ns=adi;i=10062"])
o6.reference(o6.ns["ns=adi;i=10176"], "i=52", o6.ns["ns=adi;i=10076"])
o6.reference(o6.ns["ns=adi;i=10176"], "i=53", o6.ns["ns=adi;i=9710"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10178",
    browseName="ns=adi;SuspendedToAbortingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10179", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=49))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10178"])
o6.reference(o6.ns["ns=adi;i=10178"], "i=51", o6.ns["ns=adi;i=10064"])
o6.reference(o6.ns["ns=adi;i=10178"], "i=52", o6.ns["ns=adi;i=10076"])
o6.reference(o6.ns["ns=adi;i=10178"], "i=53", o6.ns["ns=adi;i=9710"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10180",
    browseName="ns=adi;UnsuspendingToAbortingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10181", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=50))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10180"])
o6.reference(o6.ns["ns=adi;i=10180"], "i=51", o6.ns["ns=adi;i=10066"])
o6.reference(o6.ns["ns=adi;i=10180"], "i=52", o6.ns["ns=adi;i=10076"])
o6.reference(o6.ns["ns=adi;i=10180"], "i=53", o6.ns["ns=adi;i=9710"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10182",
    browseName="ns=adi;HoldingToAbortingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10183", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=51))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10182"])
o6.reference(o6.ns["ns=adi;i=10182"], "i=51", o6.ns["ns=adi;i=10068"])
o6.reference(o6.ns["ns=adi;i=10182"], "i=52", o6.ns["ns=adi;i=10076"])
o6.reference(o6.ns["ns=adi;i=10182"], "i=53", o6.ns["ns=adi;i=9710"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10184",
    browseName="ns=adi;HeldToAbortingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10185", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=52))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10184"])
o6.reference(o6.ns["ns=adi;i=10184"], "i=51", o6.ns["ns=adi;i=10070"])
o6.reference(o6.ns["ns=adi;i=10184"], "i=52", o6.ns["ns=adi;i=10076"])
o6.reference(o6.ns["ns=adi;i=10184"], "i=53", o6.ns["ns=adi;i=9710"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10186",
    browseName="ns=adi;UnholdingToAbortingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10187", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=53))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10186"])
o6.reference(o6.ns["ns=adi;i=10186"], "i=51", o6.ns["ns=adi;i=10072"])
o6.reference(o6.ns["ns=adi;i=10186"], "i=52", o6.ns["ns=adi;i=10076"])
o6.reference(o6.ns["ns=adi;i=10186"], "i=53", o6.ns["ns=adi;i=9710"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10188",
    browseName="ns=adi;StoppingToAbortingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10189", browseName="ns=adi;TransitionNumber", dataType=o6.UInt32, value=54))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10188"])
o6.reference(o6.ns["ns=adi;i=10188"], "i=51", o6.ns["ns=adi;i=10074"])
o6.reference(o6.ns["ns=adi;i=10188"], "i=52", o6.ns["ns=adi;i=10076"])
o6.reference(o6.ns["ns=adi;i=10188"], "i=53", o6.ns["ns=adi;i=9710"])
ns0.objtypes.InitialStateType(
    nodeId="ns=adi;i=10201",
    browseName="ns=adi;SelectExecutionCycle",
    description="This pseudo-state is used to decide which execution path shall be taken.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10202", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=100))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10201"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10203",
    browseName="ns=adi;WaitForCalibrationTrigger",
    description="Wait until the analyser channel is ready to perform the Calibration acquisition cycle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10204", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=200))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10203"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10205",
    browseName="ns=adi;ExtractCalibrationSample",
    description="Collect / setup the sampling system to perform the acquisition cycle of a Calibration cycle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10206", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=300))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10205"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10207",
    browseName="ns=adi;PrepareCalibrationSample",
    description="Prepare the Calibration sample for the AnalyseCalibrationSample state",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10208", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=400))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10207"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10209",
    browseName="ns=adi;AnalyseCalibrationSample",
    description="Perform the analysis of the Calibration Sample",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10210", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=500))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10209"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10211",
    browseName="ns=adi;WaitForValidationTrigger",
    description="Wait until the analyser channel is ready to perform the Validation acquisition cycle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10212", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=600))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10211"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10213",
    browseName="ns=adi;ExtractValidationSample",
    description="Collect / setup the sampling system to perform the acquisition cycle of a Validation cycle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10214", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=700))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10213"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10215",
    browseName="ns=adi;PrepareValidationSample",
    description="Prepare the Validation sample for the AnalyseValidationSample state",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10216", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=800))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10215"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10217",
    browseName="ns=adi;AnalyseValidationSample",
    description="Perform the analysis of the Validation Sample",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10218", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=900))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10217"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10219",
    browseName="ns=adi;WaitForSampleTrigger",
    description="Wait until the analyser channel is ready to perform the Sample acquisition cycle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10220", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=1000))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10219"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10221",
    browseName="ns=adi;ExtractSample",
    description="Collect the Sample from the process",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10222", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=1100))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10221"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10223",
    browseName="ns=adi;PrepareSample",
    description="Prepare the Sample for the AnalyseSample state",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10224", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=1200))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10223"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10225",
    browseName="ns=adi;AnalyseSample",
    description="Perform the analysis of the Sample",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10226", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=1300))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10225"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10227",
    browseName="ns=adi;WaitForDiagnosticTrigger",
    description="Wait until the analyser channel is ready to perform the diagnostic cycle,",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10228", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=1400))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10227"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10229",
    browseName="ns=adi;Diagnostic",
    description="Perform the diagnostic cycle.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10230", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=1500))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10229"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10231",
    browseName="ns=adi;WaitForCleaningTrigger",
    description="Wait until the analyser channel is ready to perform the cleaning cycle,",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10232", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=1600))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10231"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10233",
    browseName="ns=adi;Cleaning",
    description="Perform the cleaning cycle.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10234", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=1700))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10233"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10235",
    browseName="ns=adi;PublishResults",
    description="Publish the results of the previous acquisition cycle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10236", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=1800))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10235"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10237",
    browseName="ns=adi;EjectGrabSample",
    description="The Sample that was just analysed is ejected from the system to allow the operator or another system to grab it",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10238", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=1900))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10237"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=10239",
    browseName="ns=adi;CleanupSamplingSystem",
    description="Cleanup the sampling sub-system to be ready for the next acquisition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10240", browseName="ns=adi;StateNumber", dataType=o6.UInt32, value=2000))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10239"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10241",
    browseName="ns=adi;SelectExecutionCycleToWaitForCalibrationTriggerTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10242", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10241"])
o6.reference(o6.ns["ns=adi;i=10241"], "i=51", o6.ns["ns=adi;i=10201"])
o6.reference(o6.ns["ns=adi;i=10241"], "i=52", o6.ns["ns=adi;i=10203"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10243",
    browseName="ns=adi;WaitForCalibrationTriggerToExtractCalibrationSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10244", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10243"])
o6.reference(o6.ns["ns=adi;i=10243"], "i=51", o6.ns["ns=adi;i=10203"])
o6.reference(o6.ns["ns=adi;i=10243"], "i=52", o6.ns["ns=adi;i=10205"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10245",
    browseName="ns=adi;ExtractCalibrationSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10246", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10245"])
o6.reference(o6.ns["ns=adi;i=10245"], "i=51", o6.ns["ns=adi;i=10205"])
o6.reference(o6.ns["ns=adi;i=10245"], "i=52", o6.ns["ns=adi;i=10205"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10247",
    browseName="ns=adi;ExtractCalibrationSampleToPrepareCalibrationSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10248", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10247"])
o6.reference(o6.ns["ns=adi;i=10247"], "i=51", o6.ns["ns=adi;i=10205"])
o6.reference(o6.ns["ns=adi;i=10247"], "i=52", o6.ns["ns=adi;i=10207"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10249",
    browseName="ns=adi;PrepareCalibrationSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10250", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10249"])
o6.reference(o6.ns["ns=adi;i=10249"], "i=51", o6.ns["ns=adi;i=10207"])
o6.reference(o6.ns["ns=adi;i=10249"], "i=52", o6.ns["ns=adi;i=10207"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10251",
    browseName="ns=adi;PrepareCalibrationSampleToAnalyseCalibrationSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10252", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10251"])
o6.reference(o6.ns["ns=adi;i=10251"], "i=51", o6.ns["ns=adi;i=10207"])
o6.reference(o6.ns["ns=adi;i=10251"], "i=52", o6.ns["ns=adi;i=10209"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10253",
    browseName="ns=adi;AnalyseCalibrationSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10254", browseName="TransitionNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10253"])
o6.reference(o6.ns["ns=adi;i=10253"], "i=51", o6.ns["ns=adi;i=10209"])
o6.reference(o6.ns["ns=adi;i=10253"], "i=52", o6.ns["ns=adi;i=10209"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10255",
    browseName="ns=adi;AnalyseCalibrationSampleToPublishResultsTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10256", browseName="TransitionNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10255"])
o6.reference(o6.ns["ns=adi;i=10255"], "i=51", o6.ns["ns=adi;i=10209"])
o6.reference(o6.ns["ns=adi;i=10255"], "i=52", o6.ns["ns=adi;i=10235"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10257",
    browseName="ns=adi;SelectExecutionCycleToWaitForValidationTriggerTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10258", browseName="TransitionNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10257"])
o6.reference(o6.ns["ns=adi;i=10257"], "i=51", o6.ns["ns=adi;i=10201"])
o6.reference(o6.ns["ns=adi;i=10257"], "i=52", o6.ns["ns=adi;i=10211"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10259",
    browseName="ns=adi;WaitForValidationTriggerToExtractValidationSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10260", browseName="TransitionNumber", dataType=o6.UInt32, value=10))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10259"])
o6.reference(o6.ns["ns=adi;i=10259"], "i=51", o6.ns["ns=adi;i=10211"])
o6.reference(o6.ns["ns=adi;i=10259"], "i=52", o6.ns["ns=adi;i=10213"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10261",
    browseName="ns=adi;ExtractValidationSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10262", browseName="TransitionNumber", dataType=o6.UInt32, value=11))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10261"])
o6.reference(o6.ns["ns=adi;i=10261"], "i=51", o6.ns["ns=adi;i=10213"])
o6.reference(o6.ns["ns=adi;i=10261"], "i=52", o6.ns["ns=adi;i=10213"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10263",
    browseName="ns=adi;ExtractValidationSampleToPrepareValidationSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10264", browseName="TransitionNumber", dataType=o6.UInt32, value=12))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10263"])
o6.reference(o6.ns["ns=adi;i=10263"], "i=51", o6.ns["ns=adi;i=10213"])
o6.reference(o6.ns["ns=adi;i=10263"], "i=52", o6.ns["ns=adi;i=10215"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10265",
    browseName="ns=adi;PrepareValidationSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10266", browseName="TransitionNumber", dataType=o6.UInt32, value=13))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10265"])
o6.reference(o6.ns["ns=adi;i=10265"], "i=51", o6.ns["ns=adi;i=10215"])
o6.reference(o6.ns["ns=adi;i=10265"], "i=52", o6.ns["ns=adi;i=10215"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10267",
    browseName="ns=adi;PrepareValidationSampleToAnalyseValidationSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10268", browseName="TransitionNumber", dataType=o6.UInt32, value=14))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10267"])
o6.reference(o6.ns["ns=adi;i=10267"], "i=51", o6.ns["ns=adi;i=10215"])
o6.reference(o6.ns["ns=adi;i=10267"], "i=52", o6.ns["ns=adi;i=10217"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10269",
    browseName="ns=adi;AnalyseValidationSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10270", browseName="TransitionNumber", dataType=o6.UInt32, value=15))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10269"])
o6.reference(o6.ns["ns=adi;i=10269"], "i=51", o6.ns["ns=adi;i=10217"])
o6.reference(o6.ns["ns=adi;i=10269"], "i=52", o6.ns["ns=adi;i=10217"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10271",
    browseName="ns=adi;AnalyseValidationSampleToPublishResultsTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10272", browseName="TransitionNumber", dataType=o6.UInt32, value=16))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10271"])
o6.reference(o6.ns["ns=adi;i=10271"], "i=51", o6.ns["ns=adi;i=10217"])
o6.reference(o6.ns["ns=adi;i=10271"], "i=52", o6.ns["ns=adi;i=10235"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10273",
    browseName="ns=adi;SelectExecutionCycleToWaitForSampleTriggerTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10274", browseName="TransitionNumber", dataType=o6.UInt32, value=17))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10273"])
o6.reference(o6.ns["ns=adi;i=10273"], "i=51", o6.ns["ns=adi;i=10201"])
o6.reference(o6.ns["ns=adi;i=10273"], "i=52", o6.ns["ns=adi;i=10219"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10275",
    browseName="ns=adi;WaitForSampleTriggerToExtractSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10276", browseName="TransitionNumber", dataType=o6.UInt32, value=18))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10275"])
o6.reference(o6.ns["ns=adi;i=10275"], "i=51", o6.ns["ns=adi;i=10219"])
o6.reference(o6.ns["ns=adi;i=10275"], "i=52", o6.ns["ns=adi;i=10221"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10277",
    browseName="ns=adi;ExtractSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10278", browseName="TransitionNumber", dataType=o6.UInt32, value=19))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10277"])
o6.reference(o6.ns["ns=adi;i=10277"], "i=51", o6.ns["ns=adi;i=10221"])
o6.reference(o6.ns["ns=adi;i=10277"], "i=52", o6.ns["ns=adi;i=10221"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10279",
    browseName="ns=adi;ExtractSampleToPrepareSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10280", browseName="TransitionNumber", dataType=o6.UInt32, value=20))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10279"])
o6.reference(o6.ns["ns=adi;i=10279"], "i=51", o6.ns["ns=adi;i=10221"])
o6.reference(o6.ns["ns=adi;i=10279"], "i=52", o6.ns["ns=adi;i=10223"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10281",
    browseName="ns=adi;PrepareSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10282", browseName="TransitionNumber", dataType=o6.UInt32, value=21))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10281"])
o6.reference(o6.ns["ns=adi;i=10281"], "i=51", o6.ns["ns=adi;i=10223"])
o6.reference(o6.ns["ns=adi;i=10281"], "i=52", o6.ns["ns=adi;i=10223"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10283",
    browseName="ns=adi;PrepareSampleToAnalyseSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10284", browseName="TransitionNumber", dataType=o6.UInt32, value=22))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10283"])
o6.reference(o6.ns["ns=adi;i=10283"], "i=51", o6.ns["ns=adi;i=10223"])
o6.reference(o6.ns["ns=adi;i=10283"], "i=52", o6.ns["ns=adi;i=10225"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10285",
    browseName="ns=adi;AnalyseSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10286", browseName="TransitionNumber", dataType=o6.UInt32, value=23))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10285"])
o6.reference(o6.ns["ns=adi;i=10285"], "i=51", o6.ns["ns=adi;i=10225"])
o6.reference(o6.ns["ns=adi;i=10285"], "i=52", o6.ns["ns=adi;i=10225"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10287",
    browseName="ns=adi;AnalyseSampleToPublishResultsTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10288", browseName="TransitionNumber", dataType=o6.UInt32, value=24))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10287"])
o6.reference(o6.ns["ns=adi;i=10287"], "i=51", o6.ns["ns=adi;i=10225"])
o6.reference(o6.ns["ns=adi;i=10287"], "i=52", o6.ns["ns=adi;i=10235"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10289",
    browseName="ns=adi;SelectExecutionCycleToWaitForDiagnosticTriggerTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10290", browseName="TransitionNumber", dataType=o6.UInt32, value=25))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10289"])
o6.reference(o6.ns["ns=adi;i=10289"], "i=51", o6.ns["ns=adi;i=10201"])
o6.reference(o6.ns["ns=adi;i=10289"], "i=52", o6.ns["ns=adi;i=10227"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10291",
    browseName="ns=adi;WaitForDiagnosticTriggerToDiagnosticTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10292", browseName="TransitionNumber", dataType=o6.UInt32, value=26))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10291"])
o6.reference(o6.ns["ns=adi;i=10291"], "i=51", o6.ns["ns=adi;i=10227"])
o6.reference(o6.ns["ns=adi;i=10291"], "i=52", o6.ns["ns=adi;i=10229"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10293",
    browseName="ns=adi;DiagnosticTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10294", browseName="TransitionNumber", dataType=o6.UInt32, value=27))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10293"])
o6.reference(o6.ns["ns=adi;i=10293"], "i=51", o6.ns["ns=adi;i=10229"])
o6.reference(o6.ns["ns=adi;i=10293"], "i=52", o6.ns["ns=adi;i=10229"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10295",
    browseName="ns=adi;DiagnosticToPublishResultsTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10296", browseName="TransitionNumber", dataType=o6.UInt32, value=28))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10295"])
o6.reference(o6.ns["ns=adi;i=10295"], "i=51", o6.ns["ns=adi;i=10229"])
o6.reference(o6.ns["ns=adi;i=10295"], "i=52", o6.ns["ns=adi;i=10235"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10297",
    browseName="ns=adi;SelectExecutionCycleToWaitForCleaningTriggerTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10298", browseName="TransitionNumber", dataType=o6.UInt32, value=29))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10297"])
o6.reference(o6.ns["ns=adi;i=10297"], "i=51", o6.ns["ns=adi;i=10201"])
o6.reference(o6.ns["ns=adi;i=10297"], "i=52", o6.ns["ns=adi;i=10231"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10299",
    browseName="ns=adi;WaitForCleaningTriggerToCleaningTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10300", browseName="TransitionNumber", dataType=o6.UInt32, value=30))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10299"])
o6.reference(o6.ns["ns=adi;i=10299"], "i=51", o6.ns["ns=adi;i=10231"])
o6.reference(o6.ns["ns=adi;i=10299"], "i=52", o6.ns["ns=adi;i=10233"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10301",
    browseName="ns=adi;CleaningTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10302", browseName="TransitionNumber", dataType=o6.UInt32, value=31))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10301"])
o6.reference(o6.ns["ns=adi;i=10301"], "i=51", o6.ns["ns=adi;i=10233"])
o6.reference(o6.ns["ns=adi;i=10301"], "i=52", o6.ns["ns=adi;i=10233"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10303",
    browseName="ns=adi;CleaningToPublishResultsTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10304", browseName="TransitionNumber", dataType=o6.UInt32, value=32))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10303"])
o6.reference(o6.ns["ns=adi;i=10303"], "i=51", o6.ns["ns=adi;i=10233"])
o6.reference(o6.ns["ns=adi;i=10303"], "i=52", o6.ns["ns=adi;i=10235"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10305",
    browseName="ns=adi;PublishResultsToCleanupSamplingSystemTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10306", browseName="TransitionNumber", dataType=o6.UInt32, value=33))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10305"])
o6.reference(o6.ns["ns=adi;i=10305"], "i=51", o6.ns["ns=adi;i=10235"])
o6.reference(o6.ns["ns=adi;i=10305"], "i=52", o6.ns["ns=adi;i=10239"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10307",
    browseName="ns=adi;PublishResultsToEjectGrabSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10308", browseName="TransitionNumber", dataType=o6.UInt32, value=34))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10307"])
o6.reference(o6.ns["ns=adi;i=10307"], "i=51", o6.ns["ns=adi;i=10235"])
o6.reference(o6.ns["ns=adi;i=10307"], "i=52", o6.ns["ns=adi;i=10237"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10309",
    browseName="ns=adi;EjectGrabSampleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10310", browseName="TransitionNumber", dataType=o6.UInt32, value=35))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10309"])
o6.reference(o6.ns["ns=adi;i=10309"], "i=51", o6.ns["ns=adi;i=10237"])
o6.reference(o6.ns["ns=adi;i=10309"], "i=52", o6.ns["ns=adi;i=10237"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10311",
    browseName="ns=adi;EjectGrabSampleToCleanupSamplingSystemTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10312", browseName="TransitionNumber", dataType=o6.UInt32, value=36))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10311"])
o6.reference(o6.ns["ns=adi;i=10311"], "i=51", o6.ns["ns=adi;i=10237"])
o6.reference(o6.ns["ns=adi;i=10311"], "i=52", o6.ns["ns=adi;i=10239"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10313",
    browseName="ns=adi;CleanupSamplingSystemTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10314", browseName="TransitionNumber", dataType=o6.UInt32, value=37))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10313"])
o6.reference(o6.ns["ns=adi;i=10313"], "i=51", o6.ns["ns=adi;i=10239"])
o6.reference(o6.ns["ns=adi;i=10313"], "i=52", o6.ns["ns=adi;i=10239"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=10315",
    browseName="ns=adi;CleanupSamplingSystemToSelectExecutionCycleTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10316", browseName="TransitionNumber", dataType=o6.UInt32, value=38))],
)
o6.reference(adi_objtypes.AnalyserChannel_OperatingModeExecuteSubStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10315"])
o6.reference(o6.ns["ns=adi;i=10315"], "i=51", o6.ns["ns=adi;i=10239"])
o6.reference(o6.ns["ns=adi;i=10315"], "i=52", o6.ns["ns=adi;i=10201"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10339", browseName="ns=adi;IsEnabled", description="True if this stream maybe used to perform acquisition", dataType=o6.Boolean)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10339"])
ns0.vartypes.DataItemType(
    nodeId="ns=adi;i=10342",
    browseName="ns=adi;IsForced",
    description="True if this stream is forced, which means that is the only Stream on this AnalyserChannel that can be used to perform acquisition",
    dataType=o6.Boolean,
)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10342"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10345", browseName="ns=adi;DiagnosticStatus", description="Stream health status", dataType=di.datatypes.DeviceHealthEnumeration)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10345"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10348", browseName="ns=adi;LastCalibrationTime", description="Time at which the last calibration was run", dataType=o6.DateTime)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10348"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10351", browseName="ns=adi;LastValidationTime", description="Time at which the last validation was run", dataType=o6.DateTime)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10351"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10354", browseName="ns=adi;LastSampleTime", description="Time at which the last sample was acquired", dataType=o6.DateTime)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10354"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=adi;i=10357",
    browseName="ns=adi;TimeBetweenSamples",
    description="Number of milliseconds between two consecutive starts of acquisition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10361", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=ns0.datatypes.Duration,
)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10357"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10363", browseName="ns=adi;IsActive", description="True if this stream is actually running, acquiring data", dataType=o6.Boolean)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10363"])
ns0.vartypes.DataItemType(
    nodeId="ns=adi;i=10366", browseName="ns=adi;ExecutionCycle", description="Indicates which Execution cycle is in progress", dataType=adi_datypes.ExecutionCycleEnumeration
)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10366"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=adi;i=10369",
    browseName="ns=adi;ExecutionCycleSubcode",
    description="Indicates which Execution cycle subcode is in progress",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10372", browseName="EnumStrings", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.UInteger,
)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10369"])
ns0.vartypes.DataItemType(
    nodeId="ns=adi;i=10373",
    browseName="ns=adi;Progress",
    description="Indicates the progress of an acquisition in terms of percentage of completion. Its value shall be between 0 and 100.",
    dataType=o6.Float,
)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10373"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=adi;i=10376",
    browseName="ns=adi;AcquisitionCounter",
    description="Simple counter incremented after each Sampling acquisition performed on this Stream",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10380", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=ns0.datatypes.Counter,
)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10376"])
ns0.vartypes.DataItemType(
    nodeId="ns=adi;i=10382", browseName="ns=adi;AcquisitionResultStatus", description="Quality of the acquisition", dataType=adi_datypes.AcquisitionResultStatusEnumeration
)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10382"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10385", browseName="ns=adi;RawData", description="Raw data produced as a result of data acquisition on the Stream")
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10385"])
ns0.vartypes.DataItemType(
    nodeId="ns=adi;i=10388", browseName="ns=adi;ScaledData", description="Scaled data produced as a result of data acquisition on the Stream and application of the analyser model"
)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10388"])
ns0.vartypes.DataItemType(
    nodeId="ns=adi;i=10391",
    browseName="ns=adi;Offset",
    description="Difference in milliseconds between the start of sample extraction and the start of the analysis.",
    dataType=ns0.datatypes.Duration,
)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10391"])
ns0.vartypes.DataItemType(
    nodeId="ns=adi;i=10394",
    browseName="ns=adi;AcquisitionEndTime",
    description="The end time of the AnalyseSample or AnalyseCalibrationSample or AnalyseValidationSample state of the AnalyserChannel_OperatingModeExecuteSubStateMachine state machine",
    dataType=o6.DateTime,
)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10394"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10397", browseName="ns=adi;CampaignId", description="Defines the current campaign", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10397"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10400", browseName="ns=adi;BatchId", description="Defines the current batch", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10400"])
ns0.vartypes.DataItemType(
    nodeId="ns=adi;i=10403", browseName="ns=adi;SubBatchId", description="Defines the current sub-batch", dataType=o6.String, accessLevel=3, userAccessLevel=1
)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10403"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10406", browseName="ns=adi;LotId", description="Defines the current lot", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10406"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10409", browseName="ns=adi;MaterialId", description="Defines the current material", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10409"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10412", browseName="ns=adi;Process", description="Current Process name", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10412"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10415", browseName="ns=adi;Unit", description="Current Unit name", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10415"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10418", browseName="ns=adi;Operation", description="Current Operation name", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10418"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10421", browseName="ns=adi;Phase", description="Current Phase name", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10421"])
ns0.vartypes.DataItemType(
    nodeId="ns=adi;i=10424",
    browseName="ns=adi;UserId",
    description="Login name of the user who is logged on at the device console",
    dataType=o6.String,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10424"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10427", browseName="ns=adi;SampleId", description="Identifier for the sample", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=adi;i=10317"], "i=47", o6.ns["ns=adi;i=10427"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=adi;i=10430", browseName="ns=adi;Configuration", modellingRule="Mandatory", references=[o6.organizes(o6.ns["ns=adi;i=10339"]), o6.organizes(o6.ns["ns=adi;i=10342"])]
)
o6.reference(adi_objtypes.StreamType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10430"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=adi;i=10432",
    browseName="ns=adi;Status",
    modellingRule="Mandatory",
    references=[o6.organizes(o6.ns["ns=adi;i=10345"]), o6.organizes(o6.ns["ns=adi;i=10348"]), o6.organizes(o6.ns["ns=adi;i=10351"]), o6.organizes(o6.ns["ns=adi;i=10354"])],
)
o6.reference(adi_objtypes.StreamType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10432"])
di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=10434", browseName="ns=adi;AcquisitionSettings", modellingRule="Mandatory", references=[o6.organizes(o6.ns["ns=adi;i=10357"])])
o6.reference(adi_objtypes.StreamType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10434"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=adi;i=10436",
    browseName="ns=adi;AcquisitionStatus",
    modellingRule="Mandatory",
    references=[o6.organizes(o6.ns["ns=adi;i=10363"]), o6.organizes(o6.ns["ns=adi;i=10366"]), o6.organizes(o6.ns["ns=adi;i=10369"]), o6.organizes(o6.ns["ns=adi;i=10373"])],
)
o6.reference(adi_objtypes.StreamType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10436"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=adi;i=10438",
    browseName="ns=adi;AcquisitionData",
    modellingRule="Mandatory",
    references=[
        o6.organizes(o6.ns["ns=adi;i=10376"]),
        o6.organizes(o6.ns["ns=adi;i=10382"]),
        o6.organizes(o6.ns["ns=adi;i=10385"]),
        o6.organizes(o6.ns["ns=adi;i=10388"]),
        o6.organizes(o6.ns["ns=adi;i=10391"]),
        o6.organizes(o6.ns["ns=adi;i=10394"]),
    ],
)
o6.reference(adi_objtypes.StreamType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10438"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=adi;i=10442",
    browseName="ns=adi;Context",
    modellingRule="Mandatory",
    references=[
        o6.organizes(o6.ns["ns=adi;i=10397"]),
        o6.organizes(o6.ns["ns=adi;i=10400"]),
        o6.organizes(o6.ns["ns=adi;i=10403"]),
        o6.organizes(o6.ns["ns=adi;i=10406"]),
        o6.organizes(o6.ns["ns=adi;i=10409"]),
        o6.organizes(o6.ns["ns=adi;i=10412"]),
        o6.organizes(o6.ns["ns=adi;i=10415"]),
        o6.organizes(o6.ns["ns=adi;i=10418"]),
        o6.organizes(o6.ns["ns=adi;i=10421"]),
        o6.organizes(o6.ns["ns=adi;i=10424"]),
        o6.organizes(o6.ns["ns=adi;i=10427"]),
    ],
)
o6.reference(adi_objtypes.StreamType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10442"])
ns0.vartypes.YArrayItemType(
    nodeId="ns=adi;i=10575",
    browseName="ns=adi;ActiveBackground",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10579", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10580", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10581", browseName="Title", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10582", browseName="AxisScaleType", dataType=ns0.datatypes.AxisScaleEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10583", browseName="XAxisDefinition", dataType=ns0.datatypes.AxisInformation)),
    ],
    dataType=o6.Float,
)
o6.reference(o6.ns["ns=adi;i=10446"], "i=47", o6.ns["ns=adi;i=10575"])
ns0.vartypes.YArrayItemType(
    nodeId="ns=adi;i=10584",
    browseName="ns=adi;ActiveBackground1",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10588", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10589", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10590", browseName="Title", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10591", browseName="AxisScaleType", dataType=ns0.datatypes.AxisScaleEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10592", browseName="XAxisDefinition", dataType=ns0.datatypes.AxisInformation)),
    ],
    dataType=o6.Float,
)
o6.reference(o6.ns["ns=adi;i=10446"], "i=47", o6.ns["ns=adi;i=10584"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=adi;i=10559", browseName="ns=adi;Configuration", modellingRule="Mandatory", references=[o6.organizes(o6.ns["ns=adi;i=10575"]), o6.organizes(o6.ns["ns=adi;i=10584"])]
)
o6.reference(adi_objtypes.SpectrometerDeviceStreamType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10559"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10593", browseName="ns=adi;SpectralRange", dataType=ns0.datatypes.Range, valueRank=1, arrayDimensions=[0])
o6.reference(o6.ns["ns=adi;i=10446"], "i=47", o6.ns["ns=adi;i=10593"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10596", browseName="ns=adi;Resolution")
o6.reference(o6.ns["ns=adi;i=10446"], "i=47", o6.ns["ns=adi;i=10596"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10599", browseName="ns=adi;RequestedNumberOfScans", dataType=o6.Int32)
o6.reference(o6.ns["ns=adi;i=10446"], "i=47", o6.ns["ns=adi;i=10599"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10602", browseName="ns=adi;Gain")
o6.reference(o6.ns["ns=adi;i=10446"], "i=47", o6.ns["ns=adi;i=10602"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10605", browseName="ns=adi;TransmittanceCutoff", dataType=ns0.datatypes.Range)
o6.reference(o6.ns["ns=adi;i=10446"], "i=47", o6.ns["ns=adi;i=10605"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10608", browseName="ns=adi;AbsorbanceCutoff", dataType=ns0.datatypes.Range)
o6.reference(o6.ns["ns=adi;i=10446"], "i=47", o6.ns["ns=adi;i=10608"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=adi;i=10563",
    browseName="ns=adi;AcquisitionSettings",
    modellingRule="Mandatory",
    references=[
        o6.organizes(o6.ns["ns=adi;i=10593"]),
        o6.organizes(o6.ns["ns=adi;i=10596"]),
        o6.organizes(o6.ns["ns=adi;i=10599"]),
        o6.organizes(o6.ns["ns=adi;i=10602"]),
        o6.organizes(o6.ns["ns=adi;i=10605"]),
        o6.organizes(o6.ns["ns=adi;i=10608"]),
    ],
)
o6.reference(adi_objtypes.SpectrometerDeviceStreamType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10563"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10611", browseName="ns=adi;NumberOfScansDone", dataType=o6.Int32)
o6.reference(o6.ns["ns=adi;i=10446"], "i=47", o6.ns["ns=adi;i=10611"])
di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=10565", browseName="ns=adi;AcquisitionStatus", modellingRule="Mandatory", references=[o6.organizes(o6.ns["ns=adi;i=10611"])])
o6.reference(adi_objtypes.SpectrometerDeviceStreamType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10565"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10614", browseName="ns=adi;TotalNumberOfScansDone", dataType=o6.Int32)
o6.reference(o6.ns["ns=adi;i=10446"], "i=47", o6.ns["ns=adi;i=10614"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10617", browseName="ns=adi;BackgroundAcquisitionTime", dataType=o6.DateTime)
o6.reference(o6.ns["ns=adi;i=10446"], "i=47", o6.ns["ns=adi;i=10617"])
ns0.vartypes.YArrayItemType(
    nodeId="ns=adi;i=10620",
    browseName="ns=adi;PendingBackground",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10624", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10625", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10626", browseName="Title", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10627", browseName="AxisScaleType", dataType=ns0.datatypes.AxisScaleEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10628", browseName="XAxisDefinition", dataType=ns0.datatypes.AxisInformation)),
    ],
    dataType=o6.Float,
)
o6.reference(o6.ns["ns=adi;i=10446"], "i=47", o6.ns["ns=adi;i=10620"])
ns0.vartypes.YArrayItemType(
    nodeId="ns=adi;i=10629",
    browseName="ns=adi;PendingBackground1",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10633", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10634", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10635", browseName="Title", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10636", browseName="AxisScaleType", dataType=ns0.datatypes.AxisScaleEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10637", browseName="XAxisDefinition", dataType=ns0.datatypes.AxisInformation)),
    ],
    dataType=o6.Float,
)
o6.reference(o6.ns["ns=adi;i=10446"], "i=47", o6.ns["ns=adi;i=10629"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=adi;i=10567",
    browseName="ns=adi;AcquisitionData",
    modellingRule="Mandatory",
    references=[o6.organizes(o6.ns["ns=adi;i=10614"]), o6.organizes(o6.ns["ns=adi;i=10617"]), o6.organizes(o6.ns["ns=adi;i=10620"]), o6.organizes(o6.ns["ns=adi;i=10629"])],
)
o6.reference(adi_objtypes.SpectrometerDeviceStreamType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10567"])
ns0.vartypes.YArrayItemType(
    nodeId="ns=adi;i=10897",
    browseName="ns=adi;Background",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10901", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10902", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10903", browseName="Title", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10904", browseName="AxisScaleType", dataType=ns0.datatypes.AxisScaleEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10905", browseName="XAxisDefinition", dataType=ns0.datatypes.AxisInformation)),
    ],
    dataType=o6.Float,
)
o6.reference(o6.ns["ns=adi;i=10768"], "i=47", o6.ns["ns=adi;i=10897"])
ns0.vartypes.YArrayItemType(
    nodeId="ns=adi;i=10906",
    browseName="ns=adi;SizeDistribution",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10910", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10911", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10912", browseName="Title", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10913", browseName="AxisScaleType", dataType=ns0.datatypes.AxisScaleEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=10914", browseName="XAxisDefinition", dataType=ns0.datatypes.AxisInformation)),
    ],
    dataType=o6.Float,
)
o6.reference(o6.ns["ns=adi;i=10768"], "i=47", o6.ns["ns=adi;i=10906"])
ns0.vartypes.DataItemType(nodeId="ns=adi;i=10915", browseName="ns=adi;BackgroundAcquisitionTime", dataType=o6.DateTime)
o6.reference(o6.ns["ns=adi;i=10768"], "i=47", o6.ns["ns=adi;i=10915"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=adi;i=10889",
    browseName="ns=adi;AcquisitionData",
    modellingRule="Mandatory",
    references=[o6.organizes(o6.ns["ns=adi;i=10897"]), o6.organizes(o6.ns["ns=adi;i=10906"]), o6.organizes(o6.ns["ns=adi;i=10915"])],
)
o6.reference(adi_objtypes.ParticleSizeMonitorDeviceStreamType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=10889"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=adi;i=11305",
    browseName="ns=di;ParameterSet",
    description="Flat list of Parameters",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.DataItemType(nodeId="ns=adi;i=11551", browseName="ns=adi;SpectralRange", dataType=ns0.datatypes.Range, valueRank=1, arrayDimensions=[0]))
    ],
)
o6.reference(adi_objtypes.SpectrometerDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=11305"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=adi;i=12789",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12790", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
adi_objtypes.AccessorySlotStateMachineType(
    nodeId="ns=adi;i=12788", browseName="ns=adi;AccessorySlotStateMachine", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=adi;i=12789"])]
)
o6.reference(adi_objtypes.AccessorySlotType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12788"])
adi_objtypes.AccessoryType(
    nodeId="ns=adi;i=12800",
    browseName="ns=adi;<AccessoryIdentifier>",
    description="Accessory definition",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=adi;i=12827",
                browseName="ns=adi;IsHotSwappable",
                description="True if this accessory can be inserted in the accessory slot while it is powered",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12828", browseName="ns=adi;IsReady", description="True if this accessory is ready for use", dataType=o6.Boolean)),
        o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=12821", browseName="ns=adi;Configuration")),
        o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=12823", browseName="ns=adi;Status")),
        o6.hasComponent(di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=12825", browseName="ns=adi;FactorySettings")),
    ],
)
o6.reference(adi_objtypes.AccessorySlotType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12800"])
ns0.objtypes.InitialStateType(
    nodeId="ns=adi;i=12840",
    browseName="ns=adi;Powerup",
    description="The AccessorySlot is in its power-up sequence and cannot perform any other task.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12841", browseName="StateNumber", dataType=o6.UInt32, value=100))],
)
o6.reference(adi_objtypes.AccessorySlotStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12840"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=12842",
    browseName="ns=adi;Empty",
    description="This represents an AccessorySlot where no Accessory is installed.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12843", browseName="StateNumber", dataType=o6.UInt32, value=200))],
)
o6.reference(adi_objtypes.AccessorySlotStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12842"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=12844",
    browseName="ns=adi;Inserting",
    description="This represents an AccessorySlot when an Accessory is being inserted and initializing.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12845", browseName="StateNumber", dataType=o6.UInt32, value=300))],
)
o6.reference(adi_objtypes.AccessorySlotStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12844"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=12846",
    browseName="ns=adi;Installed",
    description="This represents an AccessorySlot where an Accessory is installed and ready to use.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12847", browseName="StateNumber", dataType=o6.UInt32, value=400))],
)
o6.reference(adi_objtypes.AccessorySlotStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12846"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=12848",
    browseName="ns=adi;Removing",
    description="This represents an AccessorySlot where no Accessory is installed.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12849", browseName="StateNumber", dataType=o6.UInt32, value=500))],
)
o6.reference(adi_objtypes.AccessorySlotStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12848"])
ns0.objtypes.StateType(
    nodeId="ns=adi;i=12850",
    browseName="ns=adi;Shutdown",
    description="The AccessorySlot is in its power-down sequence and cannot perform any other task.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12851", browseName="StateNumber", dataType=o6.UInt32, value=600))],
)
o6.reference(adi_objtypes.AccessorySlotStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12850"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=12852",
    browseName="ns=adi;PowerupToEmptyTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12853", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(adi_objtypes.AccessorySlotStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12852"])
o6.reference(o6.ns["ns=adi;i=12852"], "i=51", o6.ns["ns=adi;i=12840"])
o6.reference(o6.ns["ns=adi;i=12852"], "i=52", o6.ns["ns=adi;i=12842"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=12854",
    browseName="ns=adi;EmptyToInsertingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12855", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(adi_objtypes.AccessorySlotStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12854"])
o6.reference(o6.ns["ns=adi;i=12854"], "i=51", o6.ns["ns=adi;i=12842"])
o6.reference(o6.ns["ns=adi;i=12854"], "i=52", o6.ns["ns=adi;i=12844"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=12856",
    browseName="ns=adi;InsertingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12857", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(adi_objtypes.AccessorySlotStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12856"])
o6.reference(o6.ns["ns=adi;i=12856"], "i=51", o6.ns["ns=adi;i=12844"])
o6.reference(o6.ns["ns=adi;i=12856"], "i=52", o6.ns["ns=adi;i=12844"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=12858",
    browseName="ns=adi;InsertingToRemovingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12859", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(adi_objtypes.AccessorySlotStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12858"])
o6.reference(o6.ns["ns=adi;i=12858"], "i=51", o6.ns["ns=adi;i=12844"])
o6.reference(o6.ns["ns=adi;i=12858"], "i=52", o6.ns["ns=adi;i=12848"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=12860",
    browseName="ns=adi;InsertingToInstalledTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12861", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(adi_objtypes.AccessorySlotStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12860"])
o6.reference(o6.ns["ns=adi;i=12860"], "i=51", o6.ns["ns=adi;i=12844"])
o6.reference(o6.ns["ns=adi;i=12860"], "i=52", o6.ns["ns=adi;i=12846"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=12862",
    browseName="ns=adi;InstalledToRemovingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12863", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(adi_objtypes.AccessorySlotStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12862"])
o6.reference(o6.ns["ns=adi;i=12862"], "i=51", o6.ns["ns=adi;i=12846"])
o6.reference(o6.ns["ns=adi;i=12862"], "i=52", o6.ns["ns=adi;i=12848"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=12864",
    browseName="ns=adi;RemovingTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12865", browseName="TransitionNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(adi_objtypes.AccessorySlotStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12864"])
o6.reference(o6.ns["ns=adi;i=12864"], "i=51", o6.ns["ns=adi;i=12848"])
o6.reference(o6.ns["ns=adi;i=12864"], "i=52", o6.ns["ns=adi;i=12848"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=12866",
    browseName="ns=adi;RemovingToEmptyTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12867", browseName="TransitionNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(adi_objtypes.AccessorySlotStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12866"])
o6.reference(o6.ns["ns=adi;i=12866"], "i=51", o6.ns["ns=adi;i=12848"])
o6.reference(o6.ns["ns=adi;i=12866"], "i=52", o6.ns["ns=adi;i=12842"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=12868",
    browseName="ns=adi;EmptyToShutdownTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12869", browseName="TransitionNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(adi_objtypes.AccessorySlotStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12868"])
o6.reference(o6.ns["ns=adi;i=12868"], "i=51", o6.ns["ns=adi;i=12842"])
o6.reference(o6.ns["ns=adi;i=12868"], "i=52", o6.ns["ns=adi;i=12850"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=12870",
    browseName="ns=adi;InsertingToShutdownTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12871", browseName="TransitionNumber", dataType=o6.UInt32, value=10))],
)
o6.reference(adi_objtypes.AccessorySlotStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12870"])
o6.reference(o6.ns["ns=adi;i=12870"], "i=51", o6.ns["ns=adi;i=12844"])
o6.reference(o6.ns["ns=adi;i=12870"], "i=52", o6.ns["ns=adi;i=12850"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=12872",
    browseName="ns=adi;InstalledToShutdownTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12873", browseName="TransitionNumber", dataType=o6.UInt32, value=11))],
)
o6.reference(adi_objtypes.AccessorySlotStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12872"])
o6.reference(o6.ns["ns=adi;i=12872"], "i=51", o6.ns["ns=adi;i=12846"])
o6.reference(o6.ns["ns=adi;i=12872"], "i=52", o6.ns["ns=adi;i=12850"])
ns0.objtypes.TransitionType(
    nodeId="ns=adi;i=12874",
    browseName="ns=adi;RemovingToShutdownTransition",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=12875", browseName="TransitionNumber", dataType=o6.UInt32, value=12))],
)
o6.reference(adi_objtypes.AccessorySlotStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=12874"])
o6.reference(o6.ns["ns=adi;i=12874"], "i=51", o6.ns["ns=adi;i=12848"])
o6.reference(o6.ns["ns=adi;i=12874"], "i=52", o6.ns["ns=adi;i=12850"])
ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=13026",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=adi;i=9378",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[11],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("IDLE", "\n                "),
            description=o6.LocalizedText("Idle, no cleaning or acquisition cycle in progress", "\n                "),
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("DIAGNOSTIC", "\n                "),
            description=o6.LocalizedText("Scquisition cycle collecting data for diagnostic purpose", "\n                "),
        ),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("CLEANING", "\n                "), description=o6.LocalizedText("Cleaning cycle", "\n                ")),
        ns0.datatypes.EnumValueType(
            value=4, displayName=o6.LocalizedText("CALIBRATION", "\n                "), description=o6.LocalizedText("Calibration acquisition cycle", "\n                ")
        ),
        ns0.datatypes.EnumValueType(
            value=8, displayName=o6.LocalizedText("VALIDATION", "\n                "), description=o6.LocalizedText("Validation acquisition cycle", "\n                ")
        ),
        ns0.datatypes.EnumValueType(
            value=16, displayName=o6.LocalizedText("SAMPLING", "\n                "), description=o6.LocalizedText("Sample acquisition cycle", "\n                ")
        ),
        ns0.datatypes.EnumValueType(
            value=32769,
            displayName=o6.LocalizedText("DIAGNOSTIC_WITH_GRAB_SAMPLE", "\n                "),
            description=o6.LocalizedText(
                "Scquisition cycle collecting data for diagnostic purpose and sample is extracted from the process to be sent in control lab", "\n                "
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=32770,
            displayName=o6.LocalizedText("CLEANING_WITH_GRAB_SAMPLE", "\n                "),
            description=o6.LocalizedText("Cleaning cycle with or without acquisition and sample is extracted from the process to be sent in control lab", "\n                "),
        ),
        ns0.datatypes.EnumValueType(
            value=32772,
            displayName=o6.LocalizedText("CALIBRATION_WITH_GRAB_SAMPLE", "\n                "),
            description=o6.LocalizedText("Calibration acquisition cycle and sample is extracted from the process to be sent in control lab", "\n                "),
        ),
        ns0.datatypes.EnumValueType(
            value=32776,
            displayName=o6.LocalizedText("VALIDATION_WITH_GRAB_SAMPLE", "\n                "),
            description=o6.LocalizedText("Validation acquisition cycle and sample is extracted from the process to be sent in control lab", "\n                "),
        ),
        ns0.datatypes.EnumValueType(
            value=32784,
            displayName=o6.LocalizedText("SAMPLING_WITH_GRAB_SAMPLE", "\n                "),
            description=o6.LocalizedText("Sample acquisition cycle and sample is extracted from the process to be sent in control lab", "\n                "),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=13027",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=adi;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        o6.LocalizedText("NOT_USED", "\n          "),
        o6.LocalizedText("GOOD", "\n          "),
        o6.LocalizedText("BAD", "\n          "),
        o6.LocalizedText("UNKNOWN", "\n          "),
        o6.LocalizedText("PARTIAL", "\n          "),
    ],
)
adi_vartypes.MVAOutputParameterType(
    nodeId="ns=adi;i=13045",
    browseName="ns=adi;<User defined Output#>",
    description="Point to model output parameters",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=13049", browseName="ns=adi;AlarmState", dataType=adi_datypes.AlarmStateEnumeration))],
)
o6.reference(adi_vartypes.MVAModelType, adi_reftypes.HasOutput, o6.ns["ns=adi;i=13045"])
adi_vartypes.MVAOutputParameterType(
    nodeId="ns=adi;i=13058",
    browseName="ns=adi;Statistics",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=13059", browseName="ns=adi;WarningLimits", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=13060", browseName="ns=adi;AlarmLimits", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=13061", browseName="ns=adi;AlarmState", dataType=adi_datypes.AlarmStateEnumeration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=13062", browseName="ns=adi;VendorSpecificError", dataType=o6.String)),
    ],
    valueRank=1,
    arrayDimensions=[0],
)
o6.reference(adi_vartypes.MVAOutputParameterType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=13058"])
ns0.vartypes.PropertyType(
    nodeId="ns=adi;i=13063",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=adi;i=3009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("NORMAL_0", "\n                "), description=o6.LocalizedText("Normal", "\n                ")),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("WARNING_LOW_1", "\n                "), description=o6.LocalizedText("In low warning range", "\n                ")
        ),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("WARNING_HIGH_2", "\n                "), description=o6.LocalizedText("In high warning range", "\n                ")
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("WARNING_4", "\n                "),
            description=o6.LocalizedText("In warning range (low or high) or some other warning cause", "\n                "),
        ),
        ns0.datatypes.EnumValueType(
            value=8, displayName=o6.LocalizedText("ALARM_LOW_8", "\n                "), description=o6.LocalizedText("In low alarm range", "\n                ")
        ),
        ns0.datatypes.EnumValueType(
            value=16, displayName=o6.LocalizedText("ALARM_HIGH_16", "\n                "), description=o6.LocalizedText("In high alarm range", "\n                ")
        ),
        ns0.datatypes.EnumValueType(
            value=32,
            displayName=o6.LocalizedText("ALARM_32", "\n                "),
            description=o6.LocalizedText("In alarm range (low or high) or some other alarm cause", "\n                "),
        ),
    ],
)
opcDotUaDotAdi = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=adi;i=13064",
    browseName="ns=adi;Opc.Ua.Adi",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=8003", browseName="Deprecated", dataType=o6.Boolean, value=True)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=13066", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/ADI/Types.xsd")),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema\r\n  xmlns:DI="http://opcfoundation.org/UA/DI/Types.xsd"\r\n  xmlns:xs="http://www.w3.org/2001/XMLSchema"\r\n  xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd"\r\n  xmlns:tns="http://opcfoundation.org/UA/ADI/Types.xsd"\r\n  targetNamespace="http://opcfoundation.org/UA/ADI/Types.xsd"\r\n  elementFormDefault="qualified"\r\n>\r\n  <xs:import namespace="http://opcfoundation.org/UA/DI/Types.xsd" />\r\n  <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd" />\r\n\r\n  <xs:simpleType  name="ExecutionCycleEnumeration">\r\n    <xs:restriction base="xs:string">\r\n      <xs:enumeration value="IDLE_0" />\r\n      <xs:enumeration value="DIAGNOSTIC_1" />\r\n      <xs:enumeration value="CLEANING_2" />\r\n      <xs:enumeration value="CALIBRATION_4" />\r\n      <xs:enumeration value="VALIDATION_8" />\r\n      <xs:enumeration value="SAMPLING_16" />\r\n      <xs:enumeration value="DIAGNOSTIC_WITH_GRAB_SAMPLE_32769" />\r\n      <xs:enumeration value="CLEANING_WITH_GRAB_SAMPLE_32770" />\r\n      <xs:enumeration value="CALIBRATION_WITH_GRAB_SAMPLE_32772" />\r\n      <xs:enumeration value="VALIDATION_WITH_GRAB_SAMPLE_32776" />\r\n      <xs:enumeration value="SAMPLING_WITH_GRAB_SAMPLE_32784" />\r\n    </xs:restriction>\r\n  </xs:simpleType>\r\n  <xs:element name="ExecutionCycleEnumeration" type="tns:ExecutionCycleEnumeration" />\r\n\r\n  <xs:complexType name="ListOfExecutionCycleEnumeration">\r\n    <xs:sequence>\r\n      <xs:element name="ExecutionCycleEnumeration" type="tns:ExecutionCycleEnumeration" minOccurs="0" maxOccurs="unbounded" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfExecutionCycleEnumeration" type="tns:ListOfExecutionCycleEnumeration" nillable="true"></xs:element>\r\n\r\n  <xs:simpleType  name="AcquisitionResultStatusEnumeration">\r\n    <xs:restriction base="xs:string">\r\n      <xs:enumeration value="NOT_USED_0" />\r\n      <xs:enumeration value="GOOD_1" />\r\n      <xs:enumeration value="BAD_2" />\r\n      <xs:enumeration value="UNKNOWN_3" />\r\n      <xs:enumeration value="PARTIAL_4" />\r\n    </xs:restriction>\r\n  </xs:simpleType>\r\n  <xs:element name="AcquisitionResultStatusEnumeration" type="tns:AcquisitionResultStatusEnumeration" />\r\n\r\n  <xs:complexType name="ListOfAcquisitionResultStatusEnumeration">\r\n    <xs:sequence>\r\n      <xs:element name="AcquisitionResultStatusEnumeration" type="tns:AcquisitionResultStatusEnumeration" minOccurs="0" maxOccurs="unbounded" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfAcquisitionResultStatusEnumeration" type="tns:ListOfAcquisitionResultStatusEnumeration" nillable="true"></xs:element>\r\n\r\n  <xs:simpleType  name="AlarmStateEnumeration">\r\n    <xs:restriction base="xs:string">\r\n      <xs:enumeration value="NORMAL_0" />\r\n      <xs:enumeration value="WARNING_LOW_1" />\r\n      <xs:enumeration value="WARNING_HIGH_2" />\r\n      <xs:enumeration value="WARNING_4" />\r\n      <xs:enumeration value="ALARM_LOW_8" />\r\n      <xs:enumeration value="ALARM_HIGH_16" />\r\n      <xs:enumeration value="ALARM_32" />\r\n    </xs:restriction>\r\n  </xs:simpleType>\r\n  <xs:element name="AlarmStateEnumeration" type="tns:AlarmStateEnumeration" />\r\n\r\n  <xs:complexType name="ListOfAlarmStateEnumeration">\r\n    <xs:sequence>\r\n      <xs:element name="AlarmStateEnumeration" type="tns:AlarmStateEnumeration" minOccurs="0" maxOccurs="unbounded" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfAlarmStateEnumeration" type="tns:ListOfAlarmStateEnumeration" nillable="true"></xs:element>\r\n\r\n</xs:schema>',
)
opcDotUaDotAdi_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=adi;i=13067",
    browseName="ns=adi;Opc.Ua.Adi",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=8001", browseName="Deprecated", dataType=o6.Boolean, value=True)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=13069", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/ADI/")),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary\r\n  xmlns:DI="http://opcfoundation.org/UA/DI/"\r\n  xmlns:opc="http://opcfoundation.org/BinarySchema/"\r\n  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\r\n  xmlns:ua="http://opcfoundation.org/UA/"\r\n  xmlns:tns="http://opcfoundation.org/UA/ADI/"\r\n  DefaultByteOrder="LittleEndian"\r\n  TargetNamespace="http://opcfoundation.org/UA/ADI/"\r\n>\r\n  <opc:Import Namespace="http://opcfoundation.org/UA/DI/" Location="Opc.Ua.Di.BinarySchema.bsd"/>\r\n  <opc:Import Namespace="http://opcfoundation.org/UA/" Location="Opc.Ua.BinarySchema.bsd"/>\r\n\r\n  <opc:EnumeratedType Name="ExecutionCycleEnumeration" LengthInBits="32">\r\n    <opc:EnumeratedValue Name="IDLE" Value="0" />\r\n    <opc:EnumeratedValue Name="DIAGNOSTIC" Value="1" />\r\n    <opc:EnumeratedValue Name="CLEANING" Value="2" />\r\n    <opc:EnumeratedValue Name="CALIBRATION" Value="4" />\r\n    <opc:EnumeratedValue Name="VALIDATION" Value="8" />\r\n    <opc:EnumeratedValue Name="SAMPLING" Value="16" />\r\n    <opc:EnumeratedValue Name="DIAGNOSTIC_WITH_GRAB_SAMPLE" Value="32769" />\r\n    <opc:EnumeratedValue Name="CLEANING_WITH_GRAB_SAMPLE" Value="32770" />\r\n    <opc:EnumeratedValue Name="CALIBRATION_WITH_GRAB_SAMPLE" Value="32772" />\r\n    <opc:EnumeratedValue Name="VALIDATION_WITH_GRAB_SAMPLE" Value="32776" />\r\n    <opc:EnumeratedValue Name="SAMPLING_WITH_GRAB_SAMPLE" Value="32784" />\r\n  </opc:EnumeratedType>\r\n\r\n  <opc:EnumeratedType Name="AcquisitionResultStatusEnumeration" LengthInBits="32">\r\n    <opc:EnumeratedValue Name="NOT_USED" Value="0" />\r\n    <opc:EnumeratedValue Name="GOOD" Value="1" />\r\n    <opc:EnumeratedValue Name="BAD" Value="2" />\r\n    <opc:EnumeratedValue Name="UNKNOWN" Value="3" />\r\n    <opc:EnumeratedValue Name="PARTIAL" Value="4" />\r\n  </opc:EnumeratedType>\r\n\r\n  <opc:EnumeratedType Name="AlarmStateEnumeration" LengthInBits="32">\r\n    <opc:EnumeratedValue Name="NORMAL_0" Value="0" />\r\n    <opc:EnumeratedValue Name="WARNING_LOW_1" Value="1" />\r\n    <opc:EnumeratedValue Name="WARNING_HIGH_2" Value="2" />\r\n    <opc:EnumeratedValue Name="WARNING_4" Value="4" />\r\n    <opc:EnumeratedValue Name="ALARM_LOW_8" Value="8" />\r\n    <opc:EnumeratedValue Name="ALARM_HIGH_16" Value="16" />\r\n    <opc:EnumeratedValue Name="ALARM_32" Value="32" />\r\n  </opc:EnumeratedType>\r\n\r\n</opc:TypeDictionary>',
)
ns0.objtypes.FileType(
    nodeId="ns=adi;i=9462",
    browseName="ns=adi;ConfigData",
    description="Optional analyser device large configuration",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9463", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=9466", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=13070", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=13071", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=adi;i=9467"]),
        o6.hasComponent(o6.ns["ns=adi;i=9470"]),
        o6.hasComponent(o6.ns["ns=adi;i=9472"]),
        o6.hasComponent(o6.ns["ns=adi;i=9475"]),
        o6.hasComponent(o6.ns["ns=adi;i=9477"]),
        o6.hasComponent(o6.ns["ns=adi;i=9480"]),
    ],
)
o6.reference(o6.ns["ns=adi;i=5001"], "i=47", o6.ns["ns=adi;i=9462"])
di.objtypes.FunctionalGroupType(nodeId="ns=adi;i=9482", browseName="ns=adi;Configuration", modellingRule="Mandatory", references=[o6.organizes(o6.ns["ns=adi;i=9462"])])
o6.reference(adi_objtypes.AnalyserDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=adi;i=9482"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashADISlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=adi;i=15001",
    browseName="ns=adi;http://opcfoundation.org/UA/ADI/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=15002", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/ADI/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=15003", browseName="NamespaceVersion", dataType=o6.String, value="1.01")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=15004", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2013-07-31T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=15005", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=adi;i=15006", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=adi;i=15007", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["1:65535"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=15008", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="\n      ")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=adi;i=15031", browseName="DefaultRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=adi;i=15032", browseName="DefaultUserRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=15033", browseName="DefaultAccessRestrictions", dataType=ns0.datatypes.AccessRestrictionType)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)


del Any, TYPE_CHECKING, uuid, o6, di, ns0, adi_reftypes, adi_datypes, adi_vartypes, adi_objtypes
