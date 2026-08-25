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

"""Generated OPC UA pack_ml namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as pack_ml_reftypes
from . import datatypes as pack_ml_datypes
from . import objtypes as pack_ml_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=pack_ml;i=69", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pack_ml;i=70", browseName="Default XML")
o6.hasEncoding(pack_ml_datypes.PackMLCountDataType, o6.ns["ns=pack_ml;i=70"])
packMLObjects = ns0.objtypes.FolderType(nodeId="ns=pack_ml;i=72", browseName="ns=pack_ml;PackMLObjects", parent="i=85", referenceType=ns0.reftypes.Organizes)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pack_ml;i=74", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pack_ml;i=76", browseName="Default XML")
o6.hasEncoding(pack_ml_datypes.PackMLAlarmDataType, o6.ns["ns=pack_ml;i=76"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pack_ml;i=77", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pack_ml;i=78", browseName="Default XML")
o6.hasEncoding(pack_ml_datypes.PackMLDescriptorDataType, o6.ns["ns=pack_ml;i=78"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pack_ml;i=79", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pack_ml;i=80", browseName="Default XML")
o6.hasEncoding(pack_ml_datypes.PackMLIngredientsDataType, o6.ns["ns=pack_ml;i=80"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pack_ml;i=81", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pack_ml;i=82", browseName="Default XML")
o6.hasEncoding(pack_ml_datypes.PackMLProductDataType, o6.ns["ns=pack_ml;i=82"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pack_ml;i=83", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=pack_ml;i=84", browseName="Default XML")
o6.hasEncoding(pack_ml_datypes.PackMLRemoteInterfaceDataType, o6.ns["ns=pack_ml;i=84"])
ns0.objtypes.StateType(
    nodeId="ns=pack_ml;i=27",
    browseName="ns=pack_ml;Resetting",
    description="will typically cause a machine to sound a horn and place the machine in a state where components are energized awaiting a START command",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=127", browseName="StateNumber", dataType=o6.UInt32, value=15))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=27"])
ns0.objtypes.StateType(
    nodeId="ns=pack_ml;i=28",
    browseName="ns=pack_ml;Idle",
    description="This is a state which indicates that RESETTING is complete. This state maintains the machine conditions which were achieved during the RESETTING state, and performs operations required when the machine is in IDLE.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=128", browseName="StateNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=28"])
ns0.objtypes.StateType(
    nodeId="ns=pack_ml;i=29",
    browseName="ns=pack_ml;Starting",
    description="This state provides the steps needed to start the machine and is a result of a starting type command (local or remote). Following this command, the machine will begin to Execute",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=129", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=29"])
ns0.objtypes.StateType(
    nodeId="ns=pack_ml;i=30",
    browseName="ns=pack_ml;Suspending",
    description="This state is a result of a change in monitored conditions due to process conditions or factors. The trigger event will cause a temporary suspension of the EXECUTE state. SUSPENDING is typically the result of starvation of upstream material in-feeds (i.e., container feed, beverage feed, crown feed, lubricant feed, etc.) that is outside the dynamic speed control range or a downstream out-feed blockage that prevents the machine from EXECUTING continued steady production",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=130", browseName="StateNumber", dataType=o6.UInt32, value=13))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=30"])
ns0.objtypes.StateType(
    nodeId="ns=pack_ml;i=31",
    browseName="ns=pack_ml;Suspended",
    description="The machine may be running at a relevant set point speed, but there is no product being produced while the machine is waiting for external process conditions to return to normal.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=131", browseName="StateNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=31"])
ns0.objtypes.StateType(
    nodeId="ns=pack_ml;i=32",
    browseName="ns=pack_ml;Unsuspending",
    description="This state is a result of a machine generated request from SUSPENDED state to go back to the EXECUTE state. The actions of this state may include ramping up speeds, turning on vacuums, and the re-engagement of clutches.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=132", browseName="StateNumber", dataType=o6.UInt32, value=14))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=32"])
ns0.objtypes.StateType(
    nodeId="ns=pack_ml;i=33",
    browseName="ns=pack_ml;Holding",
    description="Issuing the Unhold command will retrieve the saved set-points and return the status conditions to prepare the machine to re-enter the normal EXECUTE state",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=133", browseName="StateNumber", dataType=o6.UInt32, value=10))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=33"])
ns0.objtypes.StateType(
    nodeId="ns=pack_ml;i=34",
    browseName="ns=pack_ml;Held",
    description="The HELD state holds the machine's operation while material blockages are cleared, or to stop throughput while a downstream problem is resolved, or enable the safe correction of an equipment fault before the production may be resumed.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=134", browseName="StateNumber", dataType=o6.UInt32, value=11))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=34"])
ns0.objtypes.StateType(
    nodeId="ns=pack_ml;i=35",
    browseName="ns=pack_ml;Unholding",
    description="The UNHOLDING state is a response to an operator command to resume the EXECUTE state. Issuing the Unhold command will retrieve the saved set-points and return the status conditions to prepare the machine to re-enter the normal EXECUTE state",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=135", browseName="StateNumber", dataType=o6.UInt32, value=12))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=35"])
ns0.objtypes.StateType(
    nodeId="ns=pack_ml;i=36",
    browseName="ns=pack_ml;Execute",
    description="Once the machine is processing materials it is deemed to be executing or in the EXECUTE state.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=136", browseName="StateNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=36"])
ns0.objtypes.StateType(
    nodeId="ns=pack_ml;i=37",
    browseName="ns=pack_ml;Completing",
    description="Normal operation has run to completion (i.e., processing of material at the infeed will stop).",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=137", browseName="StateNumber", dataType=o6.UInt32, value=16))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=37"])
ns0.objtypes.StateType(
    nodeId="ns=pack_ml;i=38",
    browseName="ns=pack_ml;Complete",
    description="The machine has finished the COMPLETING state and is now waiting for a Reset command before transitioning to the RESETTING state",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=138", browseName="StateNumber", dataType=o6.UInt32, value=17))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=38"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=39",
    browseName="ns=pack_ml;ResettingToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=139", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=39"])
o6.reference(o6.ns["ns=pack_ml;i=39"], "i=51", o6.ns["ns=pack_ml;i=27"])
o6.reference(o6.ns["ns=pack_ml;i=39"], "i=52", o6.ns["ns=pack_ml;i=28"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=40",
    browseName="ns=pack_ml;IdleToStarting",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=140", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=40"])
o6.reference(o6.ns["ns=pack_ml;i=40"], "i=51", o6.ns["ns=pack_ml;i=28"])
o6.reference(o6.ns["ns=pack_ml;i=40"], "i=52", o6.ns["ns=pack_ml;i=29"])
o6.reference(o6.ns["ns=pack_ml;i=40"], "i=53", o6.ns["ns=pack_ml;i=369"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=41",
    browseName="ns=pack_ml;StartingToExecute",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=141", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=41"])
o6.reference(o6.ns["ns=pack_ml;i=41"], "i=51", o6.ns["ns=pack_ml;i=29"])
o6.reference(o6.ns["ns=pack_ml;i=41"], "i=52", o6.ns["ns=pack_ml;i=36"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=42",
    browseName="ns=pack_ml;ExecuteToSuspending",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=142", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=42"])
o6.reference(o6.ns["ns=pack_ml;i=42"], "i=51", o6.ns["ns=pack_ml;i=36"])
o6.reference(o6.ns["ns=pack_ml;i=42"], "i=52", o6.ns["ns=pack_ml;i=30"])
o6.reference(o6.ns["ns=pack_ml;i=42"], "i=53", o6.ns["ns=pack_ml;i=367"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=43",
    browseName="ns=pack_ml;SuspendingToSuspended",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=143", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=43"])
o6.reference(o6.ns["ns=pack_ml;i=43"], "i=51", o6.ns["ns=pack_ml;i=30"])
o6.reference(o6.ns["ns=pack_ml;i=43"], "i=52", o6.ns["ns=pack_ml;i=31"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=44",
    browseName="ns=pack_ml;UnsuspendingToExecute",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=144", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=44"])
o6.reference(o6.ns["ns=pack_ml;i=44"], "i=51", o6.ns["ns=pack_ml;i=32"])
o6.reference(o6.ns["ns=pack_ml;i=44"], "i=52", o6.ns["ns=pack_ml;i=36"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=45",
    browseName="ns=pack_ml;ExecuteToHolding",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=145", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=45"])
o6.reference(o6.ns["ns=pack_ml;i=45"], "i=51", o6.ns["ns=pack_ml;i=36"])
o6.reference(o6.ns["ns=pack_ml;i=45"], "i=52", o6.ns["ns=pack_ml;i=33"])
o6.reference(o6.ns["ns=pack_ml;i=45"], "i=53", o6.ns["ns=pack_ml;i=366"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=46",
    browseName="ns=pack_ml;HoldingToHeld",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=146", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=46"])
o6.reference(o6.ns["ns=pack_ml;i=46"], "i=51", o6.ns["ns=pack_ml;i=33"])
o6.reference(o6.ns["ns=pack_ml;i=46"], "i=52", o6.ns["ns=pack_ml;i=34"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=47",
    browseName="ns=pack_ml;HeldToUnholding",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=147", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=47"])
o6.reference(o6.ns["ns=pack_ml;i=47"], "i=51", o6.ns["ns=pack_ml;i=34"])
o6.reference(o6.ns["ns=pack_ml;i=47"], "i=52", o6.ns["ns=pack_ml;i=35"])
o6.reference(o6.ns["ns=pack_ml;i=47"], "i=53", o6.ns["ns=pack_ml;i=368"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=48",
    browseName="ns=pack_ml;UnholdingToExecute",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=148", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=48"])
o6.reference(o6.ns["ns=pack_ml;i=48"], "i=51", o6.ns["ns=pack_ml;i=35"])
o6.reference(o6.ns["ns=pack_ml;i=48"], "i=52", o6.ns["ns=pack_ml;i=36"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=49",
    browseName="ns=pack_ml;ExecuteToCompleting",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=149", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=49"])
o6.reference(o6.ns["ns=pack_ml;i=49"], "i=51", o6.ns["ns=pack_ml;i=36"])
o6.reference(o6.ns["ns=pack_ml;i=49"], "i=52", o6.ns["ns=pack_ml;i=37"])
o6.reference(o6.ns["ns=pack_ml;i=49"], "i=53", o6.ns["ns=pack_ml;i=365"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=50",
    browseName="ns=pack_ml;CompletingToComplete",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=150", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=50"])
o6.reference(o6.ns["ns=pack_ml;i=50"], "i=51", o6.ns["ns=pack_ml;i=37"])
o6.reference(o6.ns["ns=pack_ml;i=50"], "i=52", o6.ns["ns=pack_ml;i=38"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=51",
    browseName="ns=pack_ml;CompleteToResetting",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=151", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=51"])
o6.reference(o6.ns["ns=pack_ml;i=51"], "i=51", o6.ns["ns=pack_ml;i=38"])
o6.reference(o6.ns["ns=pack_ml;i=51"], "i=52", o6.ns["ns=pack_ml;i=27"])
o6.reference(o6.ns["ns=pack_ml;i=51"], "i=53", o6.ns["ns=pack_ml;i=361"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=52",
    browseName="ns=pack_ml;SuspendedToUnsuspending",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=152", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=52"])
o6.reference(o6.ns["ns=pack_ml;i=52"], "i=51", o6.ns["ns=pack_ml;i=31"])
o6.reference(o6.ns["ns=pack_ml;i=52"], "i=52", o6.ns["ns=pack_ml;i=32"])
o6.reference(o6.ns["ns=pack_ml;i=52"], "i=53", o6.ns["ns=pack_ml;i=372"])
ns0.objtypes.StateType(
    nodeId="ns=pack_ml;i=53",
    browseName="ns=pack_ml;Stopped",
    description="The machine is powered and stationary after completing the STOPPING state. All communications with other systems are functioning (if applicable).",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=155", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(pack_ml_objtypes.PackMLMachineStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=53"])
ns0.objtypes.StateType(
    nodeId="ns=pack_ml;i=54",
    browseName="ns=pack_ml;Stopping",
    description="This state executes the logic which brings the machine to a controlled stop as reflected by the STOPPED state.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=156", browseName="StateNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(pack_ml_objtypes.PackMLMachineStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=54"])
ns0.objtypes.StateType(
    nodeId="ns=pack_ml;i=55",
    browseName="ns=pack_ml;Clearing",
    description="Initiated by a state command to clear faults that may have occurred when ABORTING, and are present in the ABORTED state.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=157", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(pack_ml_objtypes.PackMLMachineStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=55"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=pack_ml;i=161",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=162", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=57",
    browseName="ns=pack_ml;StoppingToStopped",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=163", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLMachineStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=57"])
o6.reference(o6.ns["ns=pack_ml;i=57"], "i=51", o6.ns["ns=pack_ml;i=54"])
o6.reference(o6.ns["ns=pack_ml;i=57"], "i=52", o6.ns["ns=pack_ml;i=53"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=58",
    browseName="ns=pack_ml;ClearingToStopped",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=164", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLMachineStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=58"])
o6.reference(o6.ns["ns=pack_ml;i=58"], "i=51", o6.ns["ns=pack_ml;i=55"])
o6.reference(o6.ns["ns=pack_ml;i=58"], "i=52", o6.ns["ns=pack_ml;i=53"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=59",
    browseName="ns=pack_ml;StoppedToRunning",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=165", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLMachineStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=59"])
o6.reference(o6.ns["ns=pack_ml;i=59"], "i=51", o6.ns["ns=pack_ml;i=53"])
o6.reference(o6.ns["ns=pack_ml;i=59"], "i=53", o6.ns["ns=pack_ml;i=376"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=60",
    browseName="ns=pack_ml;RunningToStopping",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=166", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLMachineStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=60"])
o6.reference(o6.ns["ns=pack_ml;i=60"], "i=52", o6.ns["ns=pack_ml;i=54"])
o6.reference(o6.ns["ns=pack_ml;i=60"], "i=53", o6.ns["ns=pack_ml;i=375"])
ns0.objtypes.StateType(
    nodeId="ns=pack_ml;i=61",
    browseName="ns=pack_ml;Aborting",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=168", browseName="StateNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(pack_ml_objtypes.PackMLBaseStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=61"])
ns0.objtypes.StateType(
    nodeId="ns=pack_ml;i=62",
    browseName="ns=pack_ml;Aborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=169", browseName="StateNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(pack_ml_objtypes.PackMLBaseStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=62"])
ns0.objtypes.StateType(
    nodeId="ns=pack_ml;i=75",
    browseName="ns=pack_ml;Running",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=171", browseName="StateNumber", dataType=o6.UInt32, value=18))],
)
o6.reference(pack_ml_objtypes.PackMLMachineStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=75"])
o6.reference(o6.ns["ns=pack_ml;i=59"], "i=52", o6.ns["ns=pack_ml;i=75"])
o6.reference(o6.ns["ns=pack_ml;i=60"], "i=51", o6.ns["ns=pack_ml;i=75"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=pack_ml;i=172",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=173", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=65",
    browseName="ns=pack_ml;AbortedToCleared",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=174", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLBaseStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=65"])
o6.reference(o6.ns["ns=pack_ml;i=65"], "i=51", o6.ns["ns=pack_ml;i=62"])
o6.reference(o6.ns["ns=pack_ml;i=65"], "i=53", o6.ns["ns=pack_ml;i=363"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=66",
    browseName="ns=pack_ml;AbortingToAborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=175", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLBaseStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=66"])
o6.reference(o6.ns["ns=pack_ml;i=66"], "i=51", o6.ns["ns=pack_ml;i=61"])
o6.reference(o6.ns["ns=pack_ml;i=66"], "i=52", o6.ns["ns=pack_ml;i=62"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=67",
    browseName="ns=pack_ml;ClearedToAborting",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=176", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLBaseStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=67"])
o6.reference(o6.ns["ns=pack_ml;i=67"], "i=52", o6.ns["ns=pack_ml;i=61"])
o6.reference(o6.ns["ns=pack_ml;i=67"], "i=53", o6.ns["ns=pack_ml;i=364"])
pack_ml_objtypes.PackMLExecuteStateMachineType(
    nodeId="ns=pack_ml;i=56",
    browseName="ns=pack_ml;ExecuteState",
    description="StateMachine that provides additional sube",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=160", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(o6.ns["ns=pack_ml;i=161"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=177", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
    ],
)
o6.reference(pack_ml_objtypes.PackMLMachineStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=56"])
o6.reference(o6.ns["ns=pack_ml;i=75"], "i=117", o6.ns["ns=pack_ml;i=56"])
ns0.objtypes.StateType(
    nodeId="ns=pack_ml;i=71",
    browseName="ns=pack_ml;Cleared",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=178", browseName="StateNumber", dataType=o6.UInt32, value=19))],
)
o6.reference(pack_ml_objtypes.PackMLBaseStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=71"])
o6.reference(o6.ns["ns=pack_ml;i=65"], "i=52", o6.ns["ns=pack_ml;i=71"])
o6.reference(o6.ns["ns=pack_ml;i=67"], "i=51", o6.ns["ns=pack_ml;i=71"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=99",
    browseName="ns=pack_ml;StartingToHolding",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=179", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=99"])
o6.reference(o6.ns["ns=pack_ml;i=99"], "i=51", o6.ns["ns=pack_ml;i=29"])
o6.reference(o6.ns["ns=pack_ml;i=99"], "i=52", o6.ns["ns=pack_ml;i=33"])
o6.reference(o6.ns["ns=pack_ml;i=99"], "i=53", o6.ns["ns=pack_ml;i=366"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pack_ml;i=180", browseName="ns=pack_ml;PackMLCountDataType", dataType=o6.String, value="PackMLCountDataType")
o6.reference(o6.ns["ns=pack_ml;i=69"], "i=39", o6.ns["ns=pack_ml;i=180"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pack_ml;i=181", browseName="ns=pack_ml;PackMLCountDataType", dataType=o6.String, value="//xs:element[@name='PackMLCountDataType']")
o6.reference(o6.ns["ns=pack_ml;i=70"], "i=39", o6.ns["ns=pack_ml;i=181"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pack_ml;i=182", browseName="ns=pack_ml;PackMLAlarmDataType", dataType=o6.String, value="PackMLAlarmDataType")
o6.reference(o6.ns["ns=pack_ml;i=74"], "i=39", o6.ns["ns=pack_ml;i=182"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pack_ml;i=183", browseName="ns=pack_ml;PackMLAlarmDataType", dataType=o6.String, value="//xs:element[@name='PackMLAlarmDataType']")
o6.reference(o6.ns["ns=pack_ml;i=76"], "i=39", o6.ns["ns=pack_ml;i=183"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pack_ml;i=184", browseName="ns=pack_ml;PackMLDescriptorDataType", dataType=o6.String, value="PackMLDescriptorDataType")
o6.reference(o6.ns["ns=pack_ml;i=77"], "i=39", o6.ns["ns=pack_ml;i=184"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pack_ml;i=185", browseName="ns=pack_ml;PackMLDescriptorDataType", dataType=o6.String, value="//xs:element[@name='PackMLDescriptorDataType']"
)
o6.reference(o6.ns["ns=pack_ml;i=78"], "i=39", o6.ns["ns=pack_ml;i=185"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pack_ml;i=186", browseName="ns=pack_ml;PackMLIngredientsDataType", dataType=o6.String, value="PackMLIngredientsDataType")
o6.reference(o6.ns["ns=pack_ml;i=79"], "i=39", o6.ns["ns=pack_ml;i=186"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pack_ml;i=187", browseName="ns=pack_ml;PackMLRemoteInterfaceDataType", dataType=o6.String, value="PackMLRemoteInterfaceDataType")
o6.reference(o6.ns["ns=pack_ml;i=83"], "i=39", o6.ns["ns=pack_ml;i=187"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pack_ml;i=188", browseName="ns=pack_ml;PackMLRemoteInterfaceDataType", dataType=o6.String, value="//xs:element[@name='PackMLRemoteInterfaceDataType']"
)
o6.reference(o6.ns["ns=pack_ml;i=84"], "i=39", o6.ns["ns=pack_ml;i=188"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pack_ml;i=189", browseName="ns=pack_ml;PackMLIngredientsDataType", dataType=o6.String, value="//xs:element[@name='PackMLIngredientsDataType']"
)
o6.reference(o6.ns["ns=pack_ml;i=80"], "i=39", o6.ns["ns=pack_ml;i=189"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=pack_ml;i=190", browseName="ns=pack_ml;PackMLProductDataType", dataType=o6.String, value="PackMLProductDataType")
o6.reference(o6.ns["ns=pack_ml;i=81"], "i=39", o6.ns["ns=pack_ml;i=190"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=pack_ml;i=191", browseName="ns=pack_ml;PackMLProductDataType", dataType=o6.String, value="//xs:element[@name='PackMLProductDataType']"
)
o6.reference(o6.ns["ns=pack_ml;i=82"], "i=39", o6.ns["ns=pack_ml;i=191"])
ns0.vartypes.PropertyType(
    nodeId="ns=pack_ml;i=194",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=pack_ml;i=11",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Invalid"), description=o6.LocalizedText("This is an invalid mode")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Produce"), description=o6.LocalizedText("Machine is in production mode")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Maintenance"), description=o6.LocalizedText("Machine is in maintenance mode")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Manual"), description=o6.LocalizedText("Machine is in manual mode")),
    ],
)
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=pack_ml;i=195",
    browseName="ns=pack_ml;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PackML",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pack_ml;i=196",
                browseName="NamespaceUri",
                description="A URI that uniquely identifies the dictionary.",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PackML/",
            )
        ),
        o6.hasComponent(o6.ns["ns=pack_ml;i=180"]),
        o6.hasComponent(o6.ns["ns=pack_ml;i=182"]),
        o6.hasComponent(o6.ns["ns=pack_ml;i=184"]),
        o6.hasComponent(o6.ns["ns=pack_ml;i=186"]),
        o6.hasComponent(o6.ns["ns=pack_ml;i=187"]),
        o6.hasComponent(o6.ns["ns=pack_ml;i=190"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/PackML/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/PackML/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="PackMLAlarmDataType">\n  <opc:Field TypeName="opc:Int32" Name="ID"/>\n  <opc:Field TypeName="opc:Int32" Name="Value"/>\n  <opc:Field TypeName="opc:CharArray" Name="Message"/>\n  <opc:Field TypeName="opc:Int32" Name="Category"/>\n  <opc:Field TypeName="opc:DateTime" Name="DateTime"/>\n  <opc:Field TypeName="opc:DateTime" Name="AckDateTime"/>\n  <opc:Field TypeName="opc:Boolean" Name="Trigger"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="PackMLCountDataType">\n  <opc:Field TypeName="opc:Int32" Name="ID"/>\n  <opc:Field TypeName="opc:CharArray" Name="Name"/>\n  <opc:Field TypeName="ua:EUInformation" Name="Unit"/>\n  <opc:Field TypeName="opc:Int32" Name="Count"/>\n  <opc:Field TypeName="opc:Int32" Name="AccCount"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="PackMLDescriptorDataType">\n  <opc:Field TypeName="opc:Int32" Name="ID"/>\n  <opc:Field TypeName="opc:CharArray" Name="Name"/>\n  <opc:Field TypeName="ua:EUInformation" Name="Unit"/>\n  <opc:Field TypeName="opc:Float" Name="Value"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="PackMLIngredientsDataType">\n  <opc:Field TypeName="opc:Int32" Name="IngredientID"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfParameter"/>\n  <opc:Field LengthField="NoOfParameter" TypeName="tns:PackMLDescriptorDataType" Name="Parameter"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="PackMLProductDataType">\n  <opc:Field TypeName="opc:Int32" Name="ProductID"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfProcessVariables"/>\n  <opc:Field LengthField="NoOfProcessVariables" TypeName="tns:PackMLDescriptorDataType" Name="ProcessVariables"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfIngredients"/>\n  <opc:Field LengthField="NoOfIngredients" TypeName="tns:PackMLIngredientsDataType" Name="Ingredients"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="PackMLRemoteInterfaceDataType">\n  <opc:Field TypeName="opc:Int32" Name="Number"/>\n  <opc:Field TypeName="opc:Int32" Name="ControlCmdNumber"/>\n  <opc:Field TypeName="opc:Int32" Name="CmdValue"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfParameter"/>\n  <opc:Field LengthField="NoOfParameter" TypeName="tns:PackMLDescriptorDataType" Name="Parameter"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="ProductionMaintenanceModeEnum">\n  <opc:EnumeratedValue Name="Invalid" Value="0"/>\n  <opc:EnumeratedValue Name="Produce" Value="1"/>\n  <opc:EnumeratedValue Name="Maintenance" Value="2"/>\n  <opc:EnumeratedValue Name="Manual" Value="3"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=pack_ml;i=197",
    browseName="ns=pack_ml;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/PackML",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=pack_ml;i=198",
                browseName="NamespaceUri",
                description="A URI that uniquely identifies the dictionary.",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/PackML/Types.xsd",
            )
        ),
        o6.hasComponent(o6.ns["ns=pack_ml;i=181"]),
        o6.hasComponent(o6.ns["ns=pack_ml;i=183"]),
        o6.hasComponent(o6.ns["ns=pack_ml;i=185"]),
        o6.hasComponent(o6.ns["ns=pack_ml;i=188"]),
        o6.hasComponent(o6.ns["ns=pack_ml;i=189"]),
        o6.hasComponent(o6.ns["ns=pack_ml;i=191"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/PackML/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/PackML/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="ProductionMaintenanceModeEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Invalid_0"/>\n   <xs:enumeration value="Produce_1"/>\n   <xs:enumeration value="Maintenance_2"/>\n   <xs:enumeration value="Manual_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ProductionMaintenanceModeEnum" name="ProductionMaintenanceModeEnum"/>\n <xs:complexType name="ListOfProductionMaintenanceModeEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ProductionMaintenanceModeEnum" name="ProductionMaintenanceModeEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfProductionMaintenanceModeEnum" name="ListOfProductionMaintenanceModeEnum" nillable="true"/>\n <xs:complexType name="PackMLAlarmDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="ID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="Value"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Message"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="Category"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="DateTime"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="AckDateTime"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="Trigger"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:PackMLAlarmDataType" name="PackMLAlarmDataType"/>\n <xs:complexType name="ListOfPackMLAlarmDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PackMLAlarmDataType" name="PackMLAlarmDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPackMLAlarmDataType" name="ListOfPackMLAlarmDataType" nillable="true"/>\n <xs:complexType name="PackMLCountDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="ID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Name"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="Unit"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="Count"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="AccCount"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:PackMLCountDataType" name="PackMLCountDataType"/>\n <xs:complexType name="ListOfPackMLCountDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PackMLCountDataType" name="PackMLCountDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPackMLCountDataType" name="ListOfPackMLCountDataType" nillable="true"/>\n <xs:complexType name="PackMLDescriptorDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="ID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Name"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="Unit"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="Value"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:PackMLDescriptorDataType" name="PackMLDescriptorDataType"/>\n <xs:complexType name="ListOfPackMLDescriptorDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PackMLDescriptorDataType" name="PackMLDescriptorDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPackMLDescriptorDataType" name="ListOfPackMLDescriptorDataType" nillable="true"/>\n <xs:complexType name="PackMLIngredientsDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="IngredientID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfPackMLDescriptorDataType" name="Parameter"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:PackMLIngredientsDataType" name="PackMLIngredientsDataType"/>\n <xs:complexType name="ListOfPackMLIngredientsDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PackMLIngredientsDataType" name="PackMLIngredientsDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPackMLIngredientsDataType" name="ListOfPackMLIngredientsDataType" nillable="true"/>\n <xs:complexType name="PackMLProductDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="ProductID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfPackMLDescriptorDataType" name="ProcessVariables"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfPackMLIngredientsDataType" name="Ingredients"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:PackMLProductDataType" name="PackMLProductDataType"/>\n <xs:complexType name="ListOfPackMLProductDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PackMLProductDataType" name="PackMLProductDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPackMLProductDataType" name="ListOfPackMLProductDataType" nillable="true"/>\n <xs:complexType name="PackMLRemoteInterfaceDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="Number"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="ControlCmdNumber"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="CmdValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfPackMLDescriptorDataType" name="Parameter"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:PackMLRemoteInterfaceDataType" name="PackMLRemoteInterfaceDataType"/>\n <xs:complexType name="ListOfPackMLRemoteInterfaceDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PackMLRemoteInterfaceDataType" name="PackMLRemoteInterfaceDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPackMLRemoteInterfaceDataType" name="ListOfPackMLRemoteInterfaceDataType" nillable="true"/>\n</xs:schema>\n',
)
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=100",
    browseName="ns=pack_ml;UnsuspendingToHolding",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=208", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=100"])
o6.reference(o6.ns["ns=pack_ml;i=100"], "i=51", o6.ns["ns=pack_ml;i=32"])
o6.reference(o6.ns["ns=pack_ml;i=100"], "i=52", o6.ns["ns=pack_ml;i=33"])
o6.reference(o6.ns["ns=pack_ml;i=100"], "i=53", o6.ns["ns=pack_ml;i=366"])
pack_ml_objtypes.PackMLMachineStateMachineType(
    nodeId="ns=pack_ml;i=64",
    browseName="ns=pack_ml;MachineState",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=pack_ml;i=172"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=204", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=212", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
    ],
)
o6.reference(pack_ml_objtypes.PackMLBaseStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=64"])
o6.reference(o6.ns["ns=pack_ml;i=71"], "i=117", o6.ns["ns=pack_ml;i=64"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=101",
    browseName="ns=pack_ml;SuspendedToHolding",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=215", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=101"])
o6.reference(o6.ns["ns=pack_ml;i=101"], "i=51", o6.ns["ns=pack_ml;i=31"])
o6.reference(o6.ns["ns=pack_ml;i=101"], "i=52", o6.ns["ns=pack_ml;i=33"])
o6.reference(o6.ns["ns=pack_ml;i=101"], "i=53", o6.ns["ns=pack_ml;i=366"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=102",
    browseName="ns=pack_ml;SuspendingToHolding",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=216", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=102"])
o6.reference(o6.ns["ns=pack_ml;i=102"], "i=51", o6.ns["ns=pack_ml;i=30"])
o6.reference(o6.ns["ns=pack_ml;i=102"], "i=52", o6.ns["ns=pack_ml;i=33"])
o6.reference(o6.ns["ns=pack_ml;i=102"], "i=53", o6.ns["ns=pack_ml;i=366"])
ns0.objtypes.TransitionType(
    nodeId="ns=pack_ml;i=103",
    browseName="ns=pack_ml;UnholdingToHolding",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=217", browseName="TransitionNumber", dataType=o6.UInt32))],
)
o6.reference(pack_ml_objtypes.PackMLExecuteStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=103"])
o6.reference(o6.ns["ns=pack_ml;i=103"], "i=51", o6.ns["ns=pack_ml;i=35"])
o6.reference(o6.ns["ns=pack_ml;i=103"], "i=52", o6.ns["ns=pack_ml;i=33"])
o6.reference(o6.ns["ns=pack_ml;i=103"], "i=53", o6.ns["ns=pack_ml;i=366"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=pack_ml;i=219",
    browseName="ns=pack_ml;MachSpeed",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=220", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Float,
)
o6.reference(pack_ml_objtypes.PackMLStatusObjectType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=219"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=pack_ml;i=232",
    browseName="ns=pack_ml;CurMachSpeed",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=233", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Float,
)
o6.reference(pack_ml_objtypes.PackMLStatusObjectType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=232"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=pack_ml;i=255",
    browseName="ns=pack_ml;CurMachSpeed",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=256", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Float,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=pack_ml;i=257",
    browseName="ns=pack_ml;MachSpeed",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=258", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=o6.Float,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=pack_ml;i=262",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=263", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=pack_ml;i=266",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=227", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
pack_ml_objtypes.PackMLExecuteStateMachineType(
    nodeId="ns=pack_ml;i=90",
    browseName="ns=pack_ml;ExecuteState",
    description="StateMachine that provides additional sube",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=222", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=223", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(o6.ns["ns=pack_ml;i=266"]),
    ],
)
pack_ml_objtypes.PackMLMachineStateMachineType(
    nodeId="ns=pack_ml;i=89",
    browseName="ns=pack_ml;MachineState",
    references=[
        o6.hasComponent(o6.ns["ns=pack_ml;i=90"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=213", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=214", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(o6.ns["ns=pack_ml;i=262"]),
    ],
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=pack_ml;i=272",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=273", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
pack_ml_objtypes.PackMLBaseStateMachineType(
    nodeId="ns=pack_ml;i=88",
    browseName="ns=pack_ml;BaseStateMachine",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=pack_ml;i=89"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=202", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=259", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(o6.ns["ns=pack_ml;i=272"]),
    ],
)
o6.reference(pack_ml_objtypes.PackMLBaseObjectType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=88"])
pack_ml_objtypes.PackMLStatusObjectType(
    nodeId="ns=pack_ml;i=87",
    browseName="ns=pack_ml;Status",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=290", browseName="ns=pack_ml;UnitSupportedModes", dataType=o6.NodeId)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=225", browseName="ns=pack_ml;UnitModeCurrent", dataType=ns0.datatypes.Enumeration)),
        o6.hasComponent(o6.ns["ns=pack_ml;i=255"]),
        o6.hasComponent(o6.ns["ns=pack_ml;i=257"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=274", browseName="ns=pack_ml;EquipmentBlocked", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pack_ml;i=275", browseName="ns=pack_ml;EquipmentStarved", dataType=o6.Boolean)),
    ],
)
o6.reference(pack_ml_objtypes.PackMLBaseObjectType, ns0.reftypes.HasComponent, o6.ns["ns=pack_ml;i=87"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPackMLSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=pack_ml;i=117",
    browseName="ns=pack_ml;http://opcfoundation.org/UA/PackML/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=354", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=355", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2020-10-08T11:08:00Z"))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=356", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PackML/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=357", browseName="NamespaceVersion", dataType=o6.String, value="1.01")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=358", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=359", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pack_ml;i=360", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)


del Any, TYPE_CHECKING, uuid, o6, ns0, pack_ml_reftypes, pack_ml_datypes, pack_ml_objtypes
