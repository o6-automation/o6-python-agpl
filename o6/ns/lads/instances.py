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

"""Generated OPC UA lads namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.amb as amb
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
from . import datatypes as lads_datypes
from . import objtypes as lads_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=lads;i=5042", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=lads;i=5043", browseName="Default XML")
o6.hasEncoding(lads_datypes.SampleInfoType, o6.ns["ns=lads;i=5043"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=lads;i=5044", browseName="Default JSON")
o6.hasEncoding(lads_datypes.SampleInfoType, o6.ns["ns=lads;i=5044"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=lads;i=5045", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=lads;i=5056", browseName="Default XML")
o6.hasEncoding(lads_datypes.KeyValueType, o6.ns["ns=lads;i=5056"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=lads;i=5057", browseName="Default JSON")
o6.hasEncoding(lads_datypes.KeyValueType, o6.ns["ns=lads;i=5057"])
lads_objtypes.LADSComponentsType(
    nodeId="ns=lads;i=5073",
    browseName="ns=machinery;Components",
    description="Components is used for structuring objects of type LADSComponentsType in an unordered list structure.",
    modellingRule="Optional",
)
o6.reference(lads_objtypes.LADSComponentType, ns0.reftypes.HasAddIn, o6.ns["ns=lads;i=5073"])
o6.reference(o6.ns["ns=lads;i=5073"], "i=41", "i=2133")
o6.reference(o6.ns["ns=lads;i=5088"], "i=17604", o6.ns["ns=lads;i=5073"])
lads_objtypes.FunctionSetType(
    nodeId="ns=lads;i=5006",
    browseName="ns=lads;FunctionSet",
    description="The FunctionSetType is used for organising FunctionType objects in an unordered list structure.",
    displayName="Function Set",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(
            lads_objtypes.BaseSensorFunctionType(
                nodeId="ns=lads;i=5080",
                browseName="ns=lads;<SetElement>",
                description="The BaseSensorFunctionType is an abstract ObjectType used as a base for derivation of Sensor Functions. A Sensor Function is a Function that measures data.",
                modellingRule="OptionalPlaceholder",
                _allow_abstract=True,
            )
        )
    ],
)
o6.reference(lads_objtypes.MultiSensorFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5006"])
machinery.objtypes.MachineryLifetimeCounterType(
    nodeId="ns=lads;i=5091", browseName="ns=machinery;LifetimeCounters", description="Lifetime Counter provides information about the past and estimated remaining lifetime."
)
o6.reference(lads_objtypes.LADSDeviceType, "i=17604", "ns=lads;i=5091")
ns0.objtypes.FolderType(
    nodeId="ns=lads;i=5063",
    browseName="ns=machinery;MachineryBuildingBlocks",
    description="The MachineryBuildingBlocks folder contains all machinery building blocks, especially the MachineryItemState, MachineryOperationMode, OperationCounter and Lifetime Counters.",
    modellingRule="Optional",
    references=[o6.hasAddIn(o6.ns["ns=lads;i=5091"])],
)
o6.reference(lads_objtypes.LADSDeviceType, ns0.reftypes.Organizes, o6.ns["ns=lads;i=5063"])
o6.reference(o6.ns["ns=lads;i=5063"], "i=17604", o6.ns["ns=lads;i=5089"])
o6.reference(o6.ns["ns=lads;i=5063"], "i=17604", o6.ns["ns=lads;i=5090"])
o6.reference(o6.ns["ns=lads;i=5063"], "i=17604", o6.ns["ns=lads;i=5093"])
o6.reference(o6.ns["ns=lads;i=5063"], "i=17604", o6.ns["ns=lads;i=5096"])
o6.reference(o6.ns["ns=lads;i=5063"], "i=17604", o6.ns["ns=lads;i=5111"])
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5000",
    browseName="ns=lads;OpenedToClosed",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6000", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5000"])
o6.reference(o6.ns["ns=lads;i=5000"], "i=53", o6.ns["ns=lads;i=7012"])
o6.reference(o6.ns["ns=lads;i=5000"], "i=54", "i=2311")
di.objtypes.FunctionalGroupType(
    nodeId="ns=lads;i=5030",
    browseName="ns=lads;Configuration",
    description="Configuration is used to organize parameters for configuration of the Function.",
    modellingRule="Optional",
    references=[
        o6.organizes(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6022",
                browseName="ns=lads;IsEnabled",
                description="Determnes whteher this function is currently enabled (ready to be utilized).",
                dataType=o6.Boolean,
                accessLevel=3,
            )
        )
    ],
)
o6.reference(lads_objtypes.BaseSensorFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5030"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=lads;i=6036",
    browseName="ns=lads;CalibrationValues",
    description="CalibrationValues is an array of calibration values for converting the Sensor’s raw value to the process value.",
    dataType=o6.Double,
    valueRank=1,
    arrayDimensions=[1],
    accessLevel=3,
)
o6.reference(lads_objtypes.AnalogSensorFunctionType, "i=47", "ns=lads;i=6036")
di.objtypes.FunctionalGroupType(
    nodeId="ns=lads;i=5135",
    browseName="ns=lads;Calibration",
    description="Calibration is used to organize parameters for configuration of this Function",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=lads;i=6036"])],
)
o6.reference(lads_objtypes.AnalogSensorFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5135"])
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6038", browseName="ns=lads;Damping", description="Damping is a low-pass filter parameter used for signal damping.", dataType=o6.Double, accessLevel=3
)
o6.reference(lads_objtypes.AnalogSensorFunctionType, "i=46", "ns=lads;i=6038")
di.objtypes.FunctionalGroupType(
    nodeId="ns=lads;i=5010",
    browseName="ns=lads;Tuning",
    description="Tuning is used to organize parameters for operation of this Function.",
    modellingRule="Optional",
    references=[o6.organizes(o6.ns["ns=lads;i=6038"])],
)
o6.reference(lads_objtypes.AnalogSensorFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5010"])
lads_objtypes.ResultSetType(
    nodeId="ns=lads;i=5019",
    browseName="ns=lads;ResultSet",
    description="The ResultSetType is used for organising ResultType objects in an unordered list structure.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6041",
                browseName="NodeVersion",
                description="NodeVersion and the GeneralModelChangeEventType are mechanisms to notify clients that the content of the set has changed and shall be used as defined in OPC 10000-3.",
                dataType=o6.String,
                accessLevel=3,
            )
        )
    ],
)
o6.reference(lads_objtypes.ProgramManagerType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5019"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5025",
    browseName="ns=lads;Opened",
    description="Opened is the state of the cover when it is opened.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6043", browseName="StateNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5025"])
o6.reference(o6.ns["ns=lads;i=5000"], "i=51", o6.ns["ns=lads;i=5025"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5028",
    browseName="ns=lads;Closed",
    description="Closed is the state of the cover when it is closed.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6044", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5028"])
o6.reference(o6.ns["ns=lads;i=5000"], "i=52", o6.ns["ns=lads;i=5028"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5049",
    browseName="ns=lads;Locked",
    description="Locked is the state of the cover when it is closed and locked.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6045", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5049"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5050",
    browseName="ns=lads;Error",
    description="Error is the state of the cover when it is in an error state. For example, if the locking did not work properly or there is some kind of malfunction on locking/closing the Device cover.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6046", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5050"])
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5031",
    browseName="ns=lads;IdleToStarting",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6047", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5031"])
o6.reference(o6.ns["ns=lads;i=5031"], "i=53", o6.ns["ns=lads;i=7004"])
o6.reference(o6.ns["ns=lads;i=5031"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5032",
    browseName="ns=lads;StartingToExecute",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6048", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5032"])
o6.reference(o6.ns["ns=lads;i=5032"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5033",
    browseName="ns=lads;ExecuteToCompleting",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6049", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5033"])
o6.reference(o6.ns["ns=lads;i=5033"], "i=53", o6.ns["ns=lads;i=7070"])
o6.reference(o6.ns["ns=lads;i=5033"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5034",
    browseName="ns=lads;CompletingToComplete",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6050", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5034"])
o6.reference(o6.ns["ns=lads;i=5034"], "i=54", "i=2311")
lads_objtypes.ResultSetType(
    nodeId="ns=lads;i=5022",
    browseName="ns=lads;ResultSet",
    description="The ResultSetType is used for organising ResultType objects in an unordered list structure.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6052",
                browseName="NodeVersion",
                description="NodeVersion and the GeneralModelChangeEventType are mechanisms to notify clients that the content of the set has changed and shall be used as defined in OPC 10000-3.",
                dataType=o6.String,
                accessLevel=3,
            )
        )
    ],
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashLADSSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=lads;i=5026",
    browseName="ns=lads;http://opcfoundation.org/UA/LADS/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=lads;i=6053", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6054", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2023-11-30T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6055", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/LADS/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6056", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6057", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=lads;i=6058", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6059", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5035",
    browseName="ns=lads;CompleteToResetting",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6060", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5035"])
o6.reference(o6.ns["ns=lads;i=5035"], "i=53", o6.ns["ns=lads;i=7069"])
o6.reference(o6.ns["ns=lads;i=5035"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5036",
    browseName="ns=lads;ResettingToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6061", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5036"])
o6.reference(o6.ns["ns=lads;i=5036"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5037",
    browseName="ns=lads;ExecuteToSuspending",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6070", browseName="TransitionNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5037"])
o6.reference(o6.ns["ns=lads;i=5037"], "i=53", o6.ns["ns=lads;i=7073"])
o6.reference(o6.ns["ns=lads;i=5037"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5039",
    browseName="ns=lads;SuspendingToSuspended",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6071", browseName="TransitionNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5039"])
o6.reference(o6.ns["ns=lads;i=5039"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5040",
    browseName="ns=lads;SuspendedToUnsuspending",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6072", browseName="TransitionNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5040"])
o6.reference(o6.ns["ns=lads;i=5040"], "i=53", o6.ns["ns=lads;i=7075"])
o6.reference(o6.ns["ns=lads;i=5040"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5041",
    browseName="ns=lads;UnsuspendingToExecute",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6073", browseName="TransitionNumber", dataType=o6.UInt32, value=10))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5041"])
o6.reference(o6.ns["ns=lads;i=5041"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5051",
    browseName="ns=lads;ExecuteToHolding",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6076", browseName="TransitionNumber", dataType=o6.UInt32, value=11))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5051"])
o6.reference(o6.ns["ns=lads;i=5051"], "i=53", o6.ns["ns=lads;i=7074"])
o6.reference(o6.ns["ns=lads;i=5051"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5052",
    browseName="ns=lads;HoldingToHeld",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6077", browseName="TransitionNumber", dataType=o6.UInt32, value=12))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5052"])
o6.reference(o6.ns["ns=lads;i=5052"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5053",
    browseName="ns=lads;HeldToUnholding",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6078", browseName="TransitionNumber", dataType=o6.UInt32, value=13))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5053"])
o6.reference(o6.ns["ns=lads;i=5053"], "i=53", o6.ns["ns=lads;i=7072"])
o6.reference(o6.ns["ns=lads;i=5053"], "i=54", "i=2311")
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=lads;i=6079",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6042", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
lads_objtypes.ControlFunctionStateMachineType(
    nodeId="ns=lads;i=5038",
    browseName="ns=lads;ControlFunctionState",
    description="ControlFunctionState is a state machine which represents the execution state and controls the execution of the Function.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=lads;i=6079"])],
)
o6.reference(lads_objtypes.BaseControlFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5038"])
lads_objtypes.FunctionSetType(
    nodeId="ns=lads;i=5013",
    browseName="ns=lads;FunctionSet",
    description="The FunctionSetType is used for organising FunctionType objects in an unordered list structure.",
    displayName="Function Set",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6084",
                browseName="NodeVersion",
                description="NodeVersion and the GeneralModelChangeEventType are mechanisms to notify clients that the content of the set has changed and shall be used as defined in OPC 10000-3.",
                dataType=o6.String,
                accessLevel=3,
            )
        )
    ],
)
o6.reference(lads_objtypes.FunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5013"])
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6099",
    browseName="EnumValues",
    parent="ns=lads;i=3000",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Success"), description=o6.LocalizedText("The maintenance task stopped successfully.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Failure"), description=o6.LocalizedText("The maintenance task stopped with failure.")),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("Undetermined"), description=o6.LocalizedText("The status of the maintenance task upon stopping cannot be determined.")
        ),
    ],
    accessLevel=3,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=lads;i=6100",
    browseName="CurrentState",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6101", browseName="EffectiveDisplayName", dataType=o6.LocalizedText))],
    dataType=o6.LocalizedText,
)
o6.reference(lads_objtypes.FunctionalStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=6100"])
lads_objtypes.FunctionalUnitSetType(
    nodeId="ns=lads;i=5002",
    browseName="ns=lads;FunctionalUnitSet",
    description="The FunctionalUnitSetType provides a set of a FunctionalUnit objects.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6103",
                browseName="NodeVersion",
                description="NodeVersion and the GeneralModelChangeEventType are mechanisms to notify clients that the content of the set has changed and shall be used as defined in OPC 10000-3.",
                dataType=o6.String,
                accessLevel=3,
            )
        )
    ],
)
o6.reference(lads_objtypes.LADSDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5002"])
lads_objtypes.MaintenanceSetType(
    nodeId="ns=lads;i=5092",
    browseName="ns=lads;Maintenance",
    description="The MaintenanceSetType is a set containing all maintenance tasks for a Device or Component according to the recommendations in OPC UA 10000-110.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6113",
                browseName="NodeVersion",
                description="NodeVersion and the GeneralModelChangeEventType are mechanisms to notify clients that the content of the set has changed and shall be used as defined in OPC 10000-3.",
                dataType=o6.String,
                value="NaN",
                accessLevel=3,
            )
        )
    ],
)
o6.reference(lads_objtypes.LADSDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5092"])
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5054",
    browseName="ns=lads;UnholdingToExecute",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6114", browseName="TransitionNumber", dataType=o6.UInt32, value=14))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5054"])
o6.reference(o6.ns["ns=lads;i=5054"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5129",
    browseName="ns=lads;SuspendingToHolding",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6115", browseName="TransitionNumber", dataType=o6.UInt32, value=15))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5129"])
o6.reference(o6.ns["ns=lads;i=5129"], "i=53", o6.ns["ns=lads;i=7074"])
o6.reference(o6.ns["ns=lads;i=5129"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5131",
    browseName="ns=lads;StartingToHolding",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6116", browseName="TransitionNumber", dataType=o6.UInt32, value=16))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5131"])
o6.reference(o6.ns["ns=lads;i=5131"], "i=53", o6.ns["ns=lads;i=7074"])
o6.reference(o6.ns["ns=lads;i=5131"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5132",
    browseName="ns=lads;SuspendedToHolding",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6117", browseName="TransitionNumber", dataType=o6.UInt32, value=17))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5132"])
o6.reference(o6.ns["ns=lads;i=5132"], "i=53", o6.ns["ns=lads;i=7074"])
o6.reference(o6.ns["ns=lads;i=5132"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5133",
    browseName="ns=lads;UnsuspendingToHolding",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6118", browseName="TransitionNumber", dataType=o6.UInt32, value=18))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5133"])
o6.reference(o6.ns["ns=lads;i=5133"], "i=53", o6.ns["ns=lads;i=7074"])
o6.reference(o6.ns["ns=lads;i=5133"], "i=54", "i=2311")
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=lads;i=6007",
    browseName="ns=lads;SensorValue",
    description="Boolean sensor value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6136",
                browseName="FalseState",
                description="Human readable identifier of the signals' false state.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText("off"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6137",
                browseName="TrueState",
                description="Human readable identifier of the signals' true state.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText("on"),
            )
        ),
    ],
    dataType=o6.Boolean,
)
o6.reference(lads_objtypes.TwoStateDiscreteSensorFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=6007"])
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=lads;i=6066",
    browseName="ns=lads;CurrentValue",
    description="CurrentValue is a current discrete process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6138",
                browseName="FalseState",
                description="Human readable identifier of the value false.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText("off"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6140", browseName="TrueState", description="Human readable identifier of the value true.", dataType=o6.LocalizedText, value=o6.LocalizedText("on")
            )
        ),
    ],
    dataType=o6.Boolean,
)
o6.reference(lads_objtypes.TwoStateDiscreteControlFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=6066"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=lads;i=6145", browseName="ns=lads;KeyValueType", dataType=o6.String, value="KeyValueType", accessLevel=3)
o6.reference(o6.ns["ns=lads;i=5045"], "i=39", o6.ns["ns=lads;i=6145"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=lads;i=6035",
    browseName="ns=lads;CurrentValue",
    description="Once started, the CurrentValue (aka elapsed time) counts upwards from zero until it reaches the TargetValue (aka target time).",
    displayName="Elapsed time",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6147",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4403766, displayName=o6.LocalizedText("ms"), description=o6.LocalizedText("millisecond")
                ),
            )
        )
    ],
    dataType=ns0.datatypes.Duration,
)
o6.reference(lads_objtypes.TimerControlFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=6035"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=lads;i=6012",
    browseName="ns=lads;DifferenceValue",
    description="The DifferenceValue (aka remaining time) is calculated by subtracting the CurrentValue from the TargetValue. Thus, it counts downwards from the TargetValue to zero.",
    displayName="Remaining time",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6148",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4403766, displayName=o6.LocalizedText("ms"), description=o6.LocalizedText("millisecond")
                ),
            )
        )
    ],
    dataType=ns0.datatypes.Duration,
)
o6.reference(lads_objtypes.TimerControlFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=6012"])
o6.reference(o6.ns["ns=lads;i=5113"], "i=35", o6.ns["ns=lads;i=6012"])
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=lads;i=6135",
    browseName="ns=lads;TargetValue",
    description="TargetValue is the targeted discrete set-point value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6155",
                browseName="FalseState",
                description="Human readable identifier of the value false.",
                dataType=o6.LocalizedText,
                value=o6.LocalizedText("off"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6156", browseName="TrueState", description="Human readable identifier of the value true.", dataType=o6.LocalizedText, value=o6.LocalizedText("on")
            )
        ),
    ],
    dataType=o6.Boolean,
    accessLevel=3,
)
o6.reference(lads_objtypes.TwoStateDiscreteControlFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=6135"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=lads;i=6067",
    browseName="ns=lads;CurrentValue",
    description="CurrentValue is a current discrete process value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6157", browseName="EnumStrings", description="List of human readable identifiers for the discrete values.", dataType=o6.LocalizedText, valueRank=1
            )
        )
    ],
    dataType=o6.UInt32,
)
o6.reference(lads_objtypes.MultiStateDiscreteControlFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=6067"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=lads;i=6124",
    browseName="ns=lads;TargetValue",
    description="TargetValue is the targeted discrete set-point value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6158", browseName="EnumStrings", description="List of human readable identifiers for the discrete values.", dataType=o6.LocalizedText, valueRank=1
            )
        )
    ],
    dataType=o6.UInt32,
    accessLevel=3,
)
o6.reference(lads_objtypes.MultiStateDiscreteControlFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=6124"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=lads;i=6030",
    browseName="ns=lads;SensorValue",
    description="Discrete sensor value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6160",
                browseName="EnumStrings",
                description="List of human readable identifiers for the discrete sensor values.",
                dataType=o6.LocalizedText,
                valueRank=1,
            )
        )
    ],
    dataType=o6.UInt32,
)
o6.reference(lads_objtypes.MultiStateDiscreteSensorFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=6030"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=lads;i=6034",
    browseName="ns=lads;TargetValue",
    description="The timer's target time. As soon as the CurrentValue reaches the TargetValue, the CurrentState of the TimerFunction automatically transitions to Off. This is typically accompanied by some (internal) action/effect, such as stopping the execution of a Function or similar.",
    displayName="Target time",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6161",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=4403766, displayName=o6.LocalizedText("ms"), description=o6.LocalizedText("millisecond")
                ),
            )
        )
    ],
    dataType=ns0.datatypes.Duration,
    accessLevel=3,
)
o6.reference(lads_objtypes.TimerControlFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=6034"])
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=lads;i=6122",
    browseName="ns=lads;CurrentMode",
    description="CurrentMode defines the currently selected mode. Its EnumStrings array lists the different defined modes, which shall match the names of the corresponding elements in the ControllerModeSet. Note: The EnumStrings array contains LocalizedText entries. The DisplayName of the ControllerMode is used to map the child node of the ControllerModeSet. The locale should be “en-US” or empty.",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6165", browseName="EnumStrings", dataType=o6.LocalizedText, valueRank=1))],
    dataType=o6.UInt32,
    accessLevel=3,
)
o6.reference(lads_objtypes.MultiModeAnalogControlFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=6122"])
o6.reference(o6.ns["ns=lads;i=5058"], "i=35", o6.ns["ns=lads;i=6122"])
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=lads;i=6166",
    browseName="EnabledState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6167", browseName="Id", dataType=o6.Boolean))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=lads;i=6168",
    browseName="ActiveState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6177", browseName="Id", dataType=o6.Boolean))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=lads;i=6181",
    browseName="AckedState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6182", browseName="Id", dataType=o6.Boolean))],
    dataType=o6.LocalizedText,
)
lads_objtypes.MaintenanceSetType(
    nodeId="ns=lads;i=5106",
    browseName="ns=lads;Maintenance",
    description="The MaintenanceSetType is a set containing all maintenance tasks for a Device or Component according to the recommendations in OPC UA 10000-110.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6189",
                browseName="NodeVersion",
                description="NodeVersion and the GeneralModelChangeEventType are mechanisms to notify clients that the content of the set has changed and shall be used as defined in OPC 10000-3.",
                dataType=o6.String,
                value="NaN",
                accessLevel=3,
            )
        )
    ],
)
o6.reference(lads_objtypes.LADSComponentType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5106"])
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=lads;i=6191",
    browseName="ActiveState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6192", browseName="Id", dataType=o6.Boolean))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=lads;i=6193",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6194", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.objtypes.ExclusiveLimitStateMachineType(nodeId="ns=lads;i=5070", browseName="LimitState", references=[o6.hasComponent(o6.ns["ns=lads;i=6193"])])
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=lads;i=6195",
    browseName="EnabledState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6196", browseName="Id", dataType=o6.Boolean))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=lads;i=6199",
    browseName="AckedState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6200", browseName="Id", dataType=o6.Boolean))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=lads;i=6205",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6206", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=lads;i=6210",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6211", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=lads;i=6212",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6213", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=lads;i=6224",
    browseName="ActiveState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6225", browseName="Id", dataType=o6.Boolean))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=lads;i=6226",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6227", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.objtypes.ExclusiveLimitStateMachineType(nodeId="ns=lads;i=5071", browseName="LimitState", references=[o6.hasComponent(o6.ns["ns=lads;i=6226"])])
o6.reference(o6.ns["ns=lads;i=6224"], "i=9004", o6.ns["ns=lads;i=5071"])
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=lads;i=6228",
    browseName="EnabledState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6229", browseName="Id", dataType=o6.Boolean))],
    dataType=o6.LocalizedText,
)
o6.reference(o6.ns["ns=lads;i=6228"], "i=9004", o6.ns["ns=lads;i=6224"])
ns0.vartypes.TwoStateVariableType(
    nodeId="ns=lads;i=6232",
    browseName="AckedState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6233", browseName="Id", dataType=o6.Boolean))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=lads;i=6238",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6239", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=lads;i=6243",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6244", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=lads;i=6245",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6246", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)
lads_objtypes.ProgramTemplateSetType(
    nodeId="ns=lads;i=5020",
    browseName="ns=lads;ProgramTemplateSet",
    description="The ProgramTemplateSetType is used for organising ProgramTemplateType objects in an unordered list structure.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6257",
                browseName="NodeVersion",
                description="NodeVersion and the GeneralModelChangeEventType are mechanisms to notify clients that the content of the set has changed and shall be used as defined in OPC 10000-3.",
                dataType=o6.String,
            )
        )
    ],
)
o6.reference(lads_objtypes.ProgramManagerType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5020"])
lads_objtypes.ProgramTemplateSetType(
    nodeId="ns=lads;i=5021",
    browseName="ns=lads;ProgramTemplateSet",
    description="The ProgramTemplateSetType is used for organising ProgramTemplateType objects in an unordered list structure.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=lads;i=6258",
                browseName="NodeVersion",
                description="NodeVersion and the GeneralModelChangeEventType are mechanisms to notify clients that the content of the set has changed and shall be used as defined in OPC 10000-3.",
                dataType=o6.String,
                value="NaN",
            )
        )
    ],
)
lads_objtypes.ProgramManagerType(
    nodeId="ns=lads;i=5015",
    browseName="ns=lads;ProgramManager",
    description="The ProgramManager provides the functional unit's program manager.",
    displayName="Program Manager",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=lads;i=5021"]),
        o6.hasComponent(o6.ns["ns=lads;i=5022"]),
        o6.hasComponent(
            lads_objtypes.ActiveProgramType(
                nodeId="ns=lads;i=5218",
                browseName="ns=lads;ActiveProgram",
                description="The ActiveProgram specifies the current state of operation of a FunctionalUnit. It provides context and information about the currently active program on the device. This allows users to follow the progress of a program run in a standardized fashion by organising steps into a flat, linear sequence.",
            )
        ),
    ],
)
o6.reference(lads_objtypes.FunctionalUnitType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5015"])
ns0.vartypes.ConditionVariableType(
    nodeId="ns=lads;i=6260",
    browseName="Quality",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6261", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.StatusCode,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=lads;i=6262",
    browseName="LastSeverity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6263", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.UInt16,
)
ns0.vartypes.ConditionVariableType(
    nodeId="ns=lads;i=6264",
    browseName="Comment",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6265", browseName="SourceTimestamp", dataType=ns0.datatypes.UtcTime))],
    dataType=o6.LocalizedText,
)
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5134",
    browseName="ns=lads;UnholdingToHolding",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6275", browseName="TransitionNumber", dataType=o6.UInt32, value=19))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5134"])
o6.reference(o6.ns["ns=lads;i=5134"], "i=53", o6.ns["ns=lads;i=7074"])
o6.reference(o6.ns["ns=lads;i=5134"], "i=54", "i=2311")
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=lads;i=6279",
    browseName="CurrentState",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6280", browseName="EffectiveDisplayName", dataType=o6.LocalizedText))],
    dataType=o6.LocalizedText,
)
o6.reference(lads_objtypes.FunctionalUnitStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=6279"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=lads;i=6283", browseName="ns=lads;SampleInfoType", dataType=o6.String, value="SampleInfoType", accessLevel=3)
o6.reference(o6.ns["ns=lads;i=5042"], "i=39", o6.ns["ns=lads;i=6283"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=lads;i=6131",
    browseName="ns=lads;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/LADS/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6139", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/LADS/", accessLevel=3)),
        o6.hasComponent(o6.ns["ns=lads;i=6145"]),
        o6.hasComponent(o6.ns["ns=lads;i=6283"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/LADS/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/LADS/">\n    <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n    <opc:EnumeratedType LengthInBits="32" Name="MaintenanceTaskResultEnum">\n        <opc:EnumeratedValue Name="Success" Value="0"/>\n        <opc:EnumeratedValue Name="Failure" Value="1"/>\n        <opc:EnumeratedValue Name="Undetermined" Value="2"/>\n    </opc:EnumeratedType>\n    <opc:StructuredType Name="KeyValueType">\n        <opc:Field TypeName="opc:CharArray" Name="Key"/>\n        <opc:Field TypeName="opc:CharArray" Name="Value"/>\n    </opc:StructuredType>\n    <opc:StructuredType Name="SampleInfoType">\n        <opc:Field TypeName="opc:CharArray" Name="ContainerId"/>\n        <opc:Field TypeName="opc:CharArray" Name="SampleId"/>\n        <opc:Field TypeName="opc:CharArray" Name="Position"/>\n        <opc:Field TypeName="opc:CharArray" Name="CustomData"/>\n    </opc:StructuredType>\n</opc:TypeDictionary>',
    accessLevel=3,
)
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5110",
    browseName="ns=lads;Closing",
    description="Closing is the transitive state of the cover when it is in the process of closing.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6286", browseName="StateNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5110"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5108",
    browseName="ns=lads;Locking",
    description="Locking is the transitive state of the cover when it is in the process of locking.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6287", browseName="StateNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5108"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5109",
    browseName="ns=lads;Opening",
    description="Opening is the transitive state of the cover when it is in the process of opening.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6288", browseName="StateNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5109"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5107",
    browseName="ns=lads;Unlocking",
    description="Unlocking is the transitive state of the cover when it is in the process of unlocking.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6293", browseName="StateNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5107"])
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5139",
    browseName="ns=lads;ClosedToLocking",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6294", browseName="TransitionNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5139"])
o6.reference(o6.ns["ns=lads;i=5139"], "i=51", o6.ns["ns=lads;i=5028"])
o6.reference(o6.ns["ns=lads;i=5139"], "i=52", o6.ns["ns=lads;i=5108"])
o6.reference(o6.ns["ns=lads;i=5139"], "i=53", o6.ns["ns=lads;i=7013"])
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5115",
    browseName="ns=lads;ClosedToOpening",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6295", browseName="TransitionNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5115"])
o6.reference(o6.ns["ns=lads;i=5115"], "i=51", o6.ns["ns=lads;i=5028"])
o6.reference(o6.ns["ns=lads;i=5115"], "i=52", o6.ns["ns=lads;i=5109"])
o6.reference(o6.ns["ns=lads;i=5115"], "i=53", o6.ns["ns=lads;i=7011"])
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5138",
    browseName="ns=lads;ClosingToClosed",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6296", browseName="TransitionNumber", dataType=o6.UInt32, value=10))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5138"])
o6.reference(o6.ns["ns=lads;i=5138"], "i=51", o6.ns["ns=lads;i=5110"])
o6.reference(o6.ns["ns=lads;i=5138"], "i=52", o6.ns["ns=lads;i=5028"])
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5098",
    browseName="ns=lads;LockedToUnlocking",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6300", browseName="TransitionNumber", dataType=o6.UInt32, value=11))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5098"])
o6.reference(o6.ns["ns=lads;i=5098"], "i=51", o6.ns["ns=lads;i=5049"])
o6.reference(o6.ns["ns=lads;i=5098"], "i=52", o6.ns["ns=lads;i=5107"])
o6.reference(o6.ns["ns=lads;i=5098"], "i=53", o6.ns["ns=lads;i=7014"])
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5140",
    browseName="ns=lads;LockingToLocked",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6301", browseName="TransitionNumber", dataType=o6.UInt32, value=12))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5140"])
o6.reference(o6.ns["ns=lads;i=5140"], "i=51", o6.ns["ns=lads;i=5108"])
o6.reference(o6.ns["ns=lads;i=5140"], "i=52", o6.ns["ns=lads;i=5049"])
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5137",
    browseName="ns=lads;OpenedToClosing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6302", browseName="TransitionNumber", dataType=o6.UInt32, value=13))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5137"])
o6.reference(o6.ns["ns=lads;i=5137"], "i=51", o6.ns["ns=lads;i=5025"])
o6.reference(o6.ns["ns=lads;i=5137"], "i=52", o6.ns["ns=lads;i=5110"])
o6.reference(o6.ns["ns=lads;i=5137"], "i=53", o6.ns["ns=lads;i=7012"])
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5136",
    browseName="ns=lads;OpeningToOpened",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6303", browseName="TransitionNumber", dataType=o6.UInt32, value=14))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5136"])
o6.reference(o6.ns["ns=lads;i=5136"], "i=51", o6.ns["ns=lads;i=5109"])
o6.reference(o6.ns["ns=lads;i=5136"], "i=52", o6.ns["ns=lads;i=5025"])
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5114",
    browseName="ns=lads;UnlockingToClosed",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6304", browseName="TransitionNumber", dataType=o6.UInt32, value=15))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5114"])
o6.reference(o6.ns["ns=lads;i=5114"], "i=51", o6.ns["ns=lads;i=5107"])
o6.reference(o6.ns["ns=lads;i=5114"], "i=52", o6.ns["ns=lads;i=5028"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=lads;i=6310", browseName="ns=lads;KeyValueType", dataType=o6.String, value="//xs:element[@name='KeyValueType']", accessLevel=3)
o6.reference(o6.ns["ns=lads;i=5056"], "i=39", o6.ns["ns=lads;i=6310"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=lads;i=6311", browseName="ns=lads;SampleInfoType", dataType=o6.String, value="//xs:element[@name='SampleInfoType']", accessLevel=3)
o6.reference(o6.ns["ns=lads;i=5043"], "i=39", o6.ns["ns=lads;i=6311"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=lads;i=6141",
    browseName="ns=lads;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/LADS/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=lads;i=6144", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/LADS//Types.xsd", accessLevel=3)
        ),
        o6.hasComponent(o6.ns["ns=lads;i=6310"]),
        o6.hasComponent(o6.ns["ns=lads;i=6311"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/LADS/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/LADS/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n    <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n    <xs:simpleType name="MaintenanceTaskResultEnum">\n        <xs:restriction base="xs:string">\n            <xs:enumeration value="Success_0"/>\n            <xs:enumeration value="Failure_1"/>\n            <xs:enumeration value="Undetermined_2"/>\n        </xs:restriction>\n    </xs:simpleType>\n    <xs:element type="tns:MaintenanceTaskResultEnum" name="MaintenanceTaskResultEnum"/>\n    <xs:complexType name="ListOfMaintenanceTaskResultEnum">\n        <xs:sequence>\n            <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:MaintenanceTaskResultEnum" name="MaintenanceTaskResultEnum" nillable="true"/>\n        </xs:sequence>\n    </xs:complexType>\n    <xs:element type="tns:ListOfMaintenanceTaskResultEnum" name="ListOfMaintenanceTaskResultEnum" nillable="true"/>\n    <xs:complexType name="KeyValueType">\n        <xs:sequence>\n            <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Key"/>\n            <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Value"/>\n        </xs:sequence>\n    </xs:complexType>\n    <xs:element type="tns:KeyValueType" name="KeyValueType"/>\n    <xs:complexType name="ListOfKeyValueType">\n        <xs:sequence>\n            <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:KeyValueType" name="KeyValueType" nillable="true"/>\n        </xs:sequence>\n    </xs:complexType>\n    <xs:element type="tns:ListOfKeyValueType" name="ListOfKeyValueType" nillable="true"/>\n    <xs:complexType name="SampleInfoType">\n        <xs:sequence>\n            <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ContainerId"/>\n            <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="SampleId"/>\n            <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Position"/>\n            <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="CustomData"/>\n        </xs:sequence>\n    </xs:complexType>\n    <xs:element type="tns:SampleInfoType" name="SampleInfoType"/>\n    <xs:complexType name="ListOfSampleInfoType">\n        <xs:sequence>\n            <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SampleInfoType" name="SampleInfoType" nillable="true"/>\n        </xs:sequence>\n    </xs:complexType>\n    <xs:element type="tns:ListOfSampleInfoType" name="ListOfSampleInfoType" nillable="true"/>\n</xs:schema>',
    accessLevel=3,
)
ns0.vartypes.FiniteStateVariableType(nodeId="ns=lads;i=6314", browseName="CurrentState", dataType=o6.LocalizedText)
o6.reference(o6.ns["ns=lads;i=5064"], "i=35", o6.ns["ns=lads;i=6314"])
lads_objtypes.CoverStateMachineType(
    nodeId="ns=lads;i=5055",
    browseName="ns=lads;CoverState",
    description="he CoverStateMachineType is used to control the lid, door, or cover of a laboratory device. One Device may have any arbitrary number of lids, doors, covers and their corresponding CoverFunction.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=lads;i=6314"])],
)
o6.reference(lads_objtypes.CoverFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5055"])
ns0.objtypes.InitialStateType(
    nodeId="ns=lads;i=5177",
    browseName="ns=lads;Initialization",
    description="The Device is in its initializing sequence and cannot perform any other task.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6329", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(lads_objtypes.LADSDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5177"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5178",
    browseName="ns=lads;Operate",
    description="The Device is in Operating mode. The LADS Client uses this mode for normal operation: configuration, control and data collection.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6330", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(lads_objtypes.LADSDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5178"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5180",
    browseName="ns=lads;Shutdown",
    description="The Device is in its power-down sequence and cannot perform any other Task.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6351", browseName="StateNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(lads_objtypes.LADSDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5180"])
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5181",
    browseName="ns=lads;InitializationToOperate",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6352", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(lads_objtypes.LADSDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5181"])
o6.reference(o6.ns["ns=lads;i=5181"], "i=51", o6.ns["ns=lads;i=5177"])
o6.reference(o6.ns["ns=lads;i=5181"], "i=52", o6.ns["ns=lads;i=5178"])
o6.reference(o6.ns["ns=lads;i=5181"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5184",
    browseName="ns=lads;OperateToShutdown",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6355", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(lads_objtypes.LADSDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5184"])
o6.reference(o6.ns["ns=lads;i=5184"], "i=51", o6.ns["ns=lads;i=5178"])
o6.reference(o6.ns["ns=lads;i=5184"], "i=52", o6.ns["ns=lads;i=5180"])
o6.reference(o6.ns["ns=lads;i=5184"], "i=53", o6.ns["ns=lads;i=7031"])
o6.reference(o6.ns["ns=lads;i=5184"], "i=54", "i=2311")
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5117",
    browseName="ns=lads;Starting",
    description="In state Starting the unit/device completes all steps necessary to begin execution of the active protocol. Typical steps during this state include but are not limited to inspecting system setup (checking sufficient supplies of resources and consumables), priming of fluids, homing of handling systems, or equilibration of process conditions. A Start command will cause the unit/device to transition from Idle to Starting. The unit/device will transition automatically from Starting to Execute once all required steps have been completed.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6423", browseName="StateNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5117"])
o6.reference(o6.ns["ns=lads;i=5031"], "i=52", o6.ns["ns=lads;i=5117"])
o6.reference(o6.ns["ns=lads;i=5032"], "i=51", o6.ns["ns=lads;i=5117"])
o6.reference(o6.ns["ns=lads;i=5131"], "i=51", o6.ns["ns=lads;i=5117"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5118",
    browseName="ns=lads;Suspending",
    description="The unit/device will transition from Execute to Suspending if conditions external to the unit/device require a pause in processing. Such conditions include faults to upstream or downstream equipment. The decision to Suspend may be made by a human operator supervising the process, an automated supervisory system monitoring the conditions of the overall process line/workflow, or by unit/device Sensors detecting downstream blockages or upstream scarcity of samples, etc.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6424", browseName="StateNumber", dataType=o6.UInt32, value=10))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5118"])
o6.reference(o6.ns["ns=lads;i=5037"], "i=52", o6.ns["ns=lads;i=5118"])
o6.reference(o6.ns["ns=lads;i=5039"], "i=51", o6.ns["ns=lads;i=5118"])
o6.reference(o6.ns["ns=lads;i=5129"], "i=51", o6.ns["ns=lads;i=5118"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5119",
    browseName="ns=lads;Resetting",
    description="Resetting: In response to a Reset command, the unit/device will transition to Resetting from either Stopped or Complete. In this state the unit/device attempts to clear any standing errors or stop causes. If successful, the unit/device transitions to Idle. No hazardous motion should occur while in this state.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6425", browseName="StateNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5119"])
o6.reference(o6.ns["ns=lads;i=5035"], "i=52", o6.ns["ns=lads;i=5119"])
o6.reference(o6.ns["ns=lads;i=5036"], "i=51", o6.ns["ns=lads;i=5119"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5120",
    browseName="ns=lads;Idle",
    description="In state Idle the unit/device is in an error-free state, waiting to start. The unit/device transitions automatically to Idle after all steps necessary for Resetting have been completed. All conditions achieved during Resetting are maintained. A Start command will transition the unit/device from Idle to Starting.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6426", browseName="StateNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5120"])
o6.reference(o6.ns["ns=lads;i=5031"], "i=51", o6.ns["ns=lads;i=5120"])
o6.reference(o6.ns["ns=lads;i=5036"], "i=52", o6.ns["ns=lads;i=5120"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5121",
    browseName="ns=lads;Suspended",
    description="In state Suspended the unit/device is paused, waiting for external process conditions to clear. In this state, the unit/device shall not continue processing, but may dry cycle if required (e.g., maintaining process conditions critical for the preservation of the samples or culture, including but not limited to temperature, oxygen or pH levels, etc.). Once external conditions have returned to normal, the unit/device will transition to Unsuspending, with or without operator intervention.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6427", browseName="StateNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5121"])
o6.reference(o6.ns["ns=lads;i=5039"], "i=52", o6.ns["ns=lads;i=5121"])
o6.reference(o6.ns["ns=lads;i=5040"], "i=51", o6.ns["ns=lads;i=5121"])
o6.reference(o6.ns["ns=lads;i=5132"], "i=51", o6.ns["ns=lads;i=5121"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5122",
    browseName="ns=lads;Unsuspending",
    description="Unsuspending: After all external process conditions that caused the unit/device to suspend have cleared, the unit/device completes all steps required to resume execution of the active protocol.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6428", browseName="StateNumber", dataType=o6.UInt32, value=12))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5122"])
o6.reference(o6.ns["ns=lads;i=5040"], "i=52", o6.ns["ns=lads;i=5122"])
o6.reference(o6.ns["ns=lads;i=5041"], "i=51", o6.ns["ns=lads;i=5122"])
o6.reference(o6.ns["ns=lads;i=5133"], "i=51", o6.ns["ns=lads;i=5122"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5123",
    browseName="ns=lads;Holding",
    description="In state Holding the unit/device will transition from Execute to Holding if conditions internal to the unit/device require a pause in processing. Examples of such conditions include low levels of materials required for processing (e.g., consumables, reagents, buffers, etc.) or other minor issues requiring operator service. After all steps required to hold the unit/device have been completed, the unit/device will transition automatically to the Held state.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6429", browseName="StateNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5123"])
o6.reference(o6.ns["ns=lads;i=5051"], "i=52", o6.ns["ns=lads;i=5123"])
o6.reference(o6.ns["ns=lads;i=5052"], "i=51", o6.ns["ns=lads;i=5123"])
o6.reference(o6.ns["ns=lads;i=5129"], "i=52", o6.ns["ns=lads;i=5123"])
o6.reference(o6.ns["ns=lads;i=5131"], "i=52", o6.ns["ns=lads;i=5123"])
o6.reference(o6.ns["ns=lads;i=5132"], "i=52", o6.ns["ns=lads;i=5123"])
o6.reference(o6.ns["ns=lads;i=5133"], "i=52", o6.ns["ns=lads;i=5123"])
o6.reference(o6.ns["ns=lads;i=5134"], "i=52", o6.ns["ns=lads;i=5123"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5124",
    browseName="ns=lads;Held",
    description="In state Held the unit/device is paused, waiting for internal process conditions to clear. In this state, the unit/device shall not continue processing, although it may dry cycle if required (e.g., maintaining process conditions critical for the preservation of the samples or culture). A transition to Unholding will occur once internal unit/device conditions have cleared, or if the Unhold command is initiated by an operator.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6430", browseName="StateNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5124"])
o6.reference(o6.ns["ns=lads;i=5052"], "i=52", o6.ns["ns=lads;i=5124"])
o6.reference(o6.ns["ns=lads;i=5053"], "i=51", o6.ns["ns=lads;i=5124"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5125",
    browseName="ns=lads;Unholding",
    description="Unholding: After all internal process conditions that caused the unit/device to hold have cleared, the unit/device completes all steps required to resume execution of the active protocol. Once all required actions to unhold the unit/device have been completed, the unit/device will transition automatically to the Execute state.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6431", browseName="StateNumber", dataType=o6.UInt32, value=11))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5125"])
o6.reference(o6.ns["ns=lads;i=5053"], "i=52", o6.ns["ns=lads;i=5125"])
o6.reference(o6.ns["ns=lads;i=5054"], "i=51", o6.ns["ns=lads;i=5125"])
o6.reference(o6.ns["ns=lads;i=5134"], "i=51", o6.ns["ns=lads;i=5125"])
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5126",
    browseName="ns=lads;AbortingToAborted",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6432", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(lads_objtypes.FunctionalStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5126"])
o6.reference(o6.ns["ns=lads;i=5126"], "i=54", "i=2311")
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5127",
    browseName="ns=lads;Completing",
    description="Completing: Once the process associated with the current mode has reached a defined threshold (e.g., the required number of samples for the current job have been analysed or the cultivation/fermentation process has reached is final stage in terms of cell count, product yield, cell viability, etc.), the unit/device transitions from Execute to Completing. All steps necessary to shut down the current process are carried out in this state. The unit/device then transitions automatically to the Complete state.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6433", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5127"])
o6.reference(o6.ns["ns=lads;i=5033"], "i=52", o6.ns["ns=lads;i=5127"])
o6.reference(o6.ns["ns=lads;i=5034"], "i=51", o6.ns["ns=lads;i=5127"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5128",
    browseName="ns=lads;Complete",
    description="Complete indicates that the process associated with the active protocol has come to its defined end. The unit/device will wait in this state until a Reset command is issued (in which case it will transition to Resetting), or until the unit/device is Stopped or Aborted.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6434", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5128"])
o6.reference(o6.ns["ns=lads;i=5034"], "i=52", o6.ns["ns=lads;i=5128"])
o6.reference(o6.ns["ns=lads;i=5035"], "i=51", o6.ns["ns=lads;i=5128"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5143",
    browseName="ns=lads;Clearing",
    description="Clearing is initiated by a state command to clear faults that may have occurred when Aborting that are present in the Aborted state.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6449", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(lads_objtypes.FunctionalStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5143"])
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5074",
    browseName="ns=lads;ClosedToOpened",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6463", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5074"])
o6.reference(o6.ns["ns=lads;i=5074"], "i=51", o6.ns["ns=lads;i=5028"])
o6.reference(o6.ns["ns=lads;i=5074"], "i=52", o6.ns["ns=lads;i=5025"])
o6.reference(o6.ns["ns=lads;i=5074"], "i=53", o6.ns["ns=lads;i=7011"])
o6.reference(o6.ns["ns=lads;i=5074"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5075",
    browseName="ns=lads;ClosedToLocked",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6464", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5075"])
o6.reference(o6.ns["ns=lads;i=5075"], "i=51", o6.ns["ns=lads;i=5028"])
o6.reference(o6.ns["ns=lads;i=5075"], "i=52", o6.ns["ns=lads;i=5049"])
o6.reference(o6.ns["ns=lads;i=5075"], "i=53", o6.ns["ns=lads;i=7013"])
o6.reference(o6.ns["ns=lads;i=5075"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5077",
    browseName="ns=lads;LockedToClosed",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6465", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5077"])
o6.reference(o6.ns["ns=lads;i=5077"], "i=51", o6.ns["ns=lads;i=5049"])
o6.reference(o6.ns["ns=lads;i=5077"], "i=52", o6.ns["ns=lads;i=5028"])
o6.reference(o6.ns["ns=lads;i=5077"], "i=53", o6.ns["ns=lads;i=7014"])
o6.reference(o6.ns["ns=lads;i=5077"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5078",
    browseName="ns=lads;LockedToError",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6466", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5078"])
o6.reference(o6.ns["ns=lads;i=5078"], "i=51", o6.ns["ns=lads;i=5049"])
o6.reference(o6.ns["ns=lads;i=5078"], "i=52", o6.ns["ns=lads;i=5050"])
o6.reference(o6.ns["ns=lads;i=5078"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5079",
    browseName="ns=lads;ClosedToError",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6467", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5079"])
o6.reference(o6.ns["ns=lads;i=5079"], "i=51", o6.ns["ns=lads;i=5028"])
o6.reference(o6.ns["ns=lads;i=5079"], "i=52", o6.ns["ns=lads;i=5050"])
o6.reference(o6.ns["ns=lads;i=5079"], "i=54", "i=2311")
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5159",
    browseName="ns=lads;Aborting",
    description="The Aborting state can be entered at any time in response to the Abort command or in the event of a unit/device fault. The aborting logic will bring the unit/device to a rapid safe stop.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6474", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(lads_objtypes.FunctionalStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5159"])
o6.reference(o6.ns["ns=lads;i=5126"], "i=51", o6.ns["ns=lads;i=5159"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5160",
    browseName="ns=lads;Aborted",
    description="Aborted maintains unit/device status information relevant to the Abort condition. The unit/device can only exit the Aborted state after an explicit Clear command subsequent to intervention to correct and reset the detected unit/device faults.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6475", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(lads_objtypes.FunctionalStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5160"])
o6.reference(o6.ns["ns=lads;i=5126"], "i=52", o6.ns["ns=lads;i=5160"])
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5082",
    browseName="ns=lads;ErrorToOpened",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6476", browseName="TransitionNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(lads_objtypes.CoverStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5082"])
o6.reference(o6.ns["ns=lads;i=5082"], "i=51", o6.ns["ns=lads;i=5050"])
o6.reference(o6.ns["ns=lads;i=5082"], "i=52", o6.ns["ns=lads;i=5025"])
o6.reference(o6.ns["ns=lads;i=5082"], "i=53", o6.ns["ns=lads;i=7000"])
o6.reference(o6.ns["ns=lads;i=5082"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5083",
    browseName="ns=lads;SleepToOperate",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6482", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(lads_objtypes.LADSDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5083"])
o6.reference(o6.ns["ns=lads;i=5083"], "i=52", o6.ns["ns=lads;i=5178"])
o6.reference(o6.ns["ns=lads;i=5083"], "i=53", o6.ns["ns=lads;i=7021"])
o6.reference(o6.ns["ns=lads;i=5083"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5165",
    browseName="ns=lads;AbortedToClearing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6486", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(lads_objtypes.FunctionalStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5165"])
o6.reference(o6.ns["ns=lads;i=5165"], "i=51", o6.ns["ns=lads;i=5160"])
o6.reference(o6.ns["ns=lads;i=5165"], "i=52", o6.ns["ns=lads;i=5143"])
o6.reference(o6.ns["ns=lads;i=5165"], "i=53", o6.ns["ns=lads;i=7079"])
o6.reference(o6.ns["ns=lads;i=5165"], "i=54", "i=2311")
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5168",
    browseName="ns=lads;Execute",
    description="In state Execute the unit/device is actively carrying out the behaviour or activity defined by the selected protocol and its associated processing mode. Examples of a unit/device in processing mode include when the unit/device is performing an analytical run, cultivation/fermentation in the case of a bioreactor, or another defined unit of operation provided by the instrument (e.g., separation in the case of a centrifuge).",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6489", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(lads_objtypes.RunningStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5168"])
o6.reference(o6.ns["ns=lads;i=5032"], "i=52", o6.ns["ns=lads;i=5168"])
o6.reference(o6.ns["ns=lads;i=5033"], "i=51", o6.ns["ns=lads;i=5168"])
o6.reference(o6.ns["ns=lads;i=5037"], "i=51", o6.ns["ns=lads;i=5168"])
o6.reference(o6.ns["ns=lads;i=5041"], "i=52", o6.ns["ns=lads;i=5168"])
o6.reference(o6.ns["ns=lads;i=5051"], "i=51", o6.ns["ns=lads;i=5168"])
o6.reference(o6.ns["ns=lads;i=5054"], "i=52", o6.ns["ns=lads;i=5168"])
ns0.objtypes.InitialStateType(
    nodeId="ns=lads;i=5085",
    browseName="ns=lads;Stopped",
    description="Stopped is the initial state for an ActiveProgram, FunctionalUnit or Function. It is an Idle state which means that the Function, FunctionalUnit or ActiveProgram is stopped and ready for activation.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6508", browseName="StateNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(lads_objtypes.FunctionalStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5085"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5099",
    browseName="ns=lads;Running",
    description="Running is the state when the Function or FunctionalUnit is currently running/executing.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6509", browseName="StateNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(lads_objtypes.FunctionalStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5099"])
o6.reference(o6.ns["ns=lads;i=5099"], "i=117", o6.ns["ns=lads;i=5130"])
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5100",
    browseName="ns=lads;Stopping",
    description="Stopping indicates that the ActiveProgram, FunctionalUnit, or Function is in the process of stopping. This state usually occurs when the program execution is finished or stopped, either because it has ended or has been triggered by the Stop Method.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6511", browseName="StateNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(lads_objtypes.FunctionalStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5100"])
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5101",
    browseName="ns=lads;StoppingToStopped",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6512", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(lads_objtypes.FunctionalStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5101"])
o6.reference(o6.ns["ns=lads;i=5101"], "i=51", o6.ns["ns=lads;i=5100"])
o6.reference(o6.ns["ns=lads;i=5101"], "i=52", o6.ns["ns=lads;i=5085"])
o6.reference(o6.ns["ns=lads;i=5101"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5102",
    browseName="ns=lads;StoppedToRunning",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6513", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(lads_objtypes.FunctionalStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5102"])
o6.reference(o6.ns["ns=lads;i=5102"], "i=51", o6.ns["ns=lads;i=5085"])
o6.reference(o6.ns["ns=lads;i=5102"], "i=52", o6.ns["ns=lads;i=5099"])
o6.reference(o6.ns["ns=lads;i=5102"], "i=53", o6.ns["ns=lads;i=7004"])
o6.reference(o6.ns["ns=lads;i=5102"], "i=54", "i=2311")
ns0.objtypes.StateType(
    nodeId="ns=lads;i=5259",
    browseName="ns=lads;Sleep",
    description="The Device is still powered on and its OPC UA Server is still running, but it is not ready to perform any Tasks until it transitions to the Operate state. This state can be used to represent a PowerSave state where a Device may shut down some of its Components, such as the GUI.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6525", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(lads_objtypes.LADSDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5259"])
o6.reference(o6.ns["ns=lads;i=5083"], "i=51", o6.ns["ns=lads;i=5259"])
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5103",
    browseName="ns=lads;RunningToAborting",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6528", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(lads_objtypes.FunctionalStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5103"])
o6.reference(o6.ns["ns=lads;i=5103"], "i=51", o6.ns["ns=lads;i=5099"])
o6.reference(o6.ns["ns=lads;i=5103"], "i=52", o6.ns["ns=lads;i=5159"])
o6.reference(o6.ns["ns=lads;i=5103"], "i=53", o6.ns["ns=lads;i=7078"])
o6.reference(o6.ns["ns=lads;i=5103"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5104",
    browseName="ns=lads;ClearingToStopped",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6529", browseName="TransitionNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(lads_objtypes.FunctionalStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5104"])
o6.reference(o6.ns["ns=lads;i=5104"], "i=51", o6.ns["ns=lads;i=5143"])
o6.reference(o6.ns["ns=lads;i=5104"], "i=52", o6.ns["ns=lads;i=5085"])
o6.reference(o6.ns["ns=lads;i=5104"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5105",
    browseName="ns=lads;RunningToStopping",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6534", browseName="TransitionNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(lads_objtypes.FunctionalStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5105"])
o6.reference(o6.ns["ns=lads;i=5105"], "i=51", o6.ns["ns=lads;i=5099"])
o6.reference(o6.ns["ns=lads;i=5105"], "i=52", o6.ns["ns=lads;i=5100"])
o6.reference(o6.ns["ns=lads;i=5105"], "i=53", o6.ns["ns=lads;i=7112"])
o6.reference(o6.ns["ns=lads;i=5105"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=lads;i=5260",
    browseName="ns=lads;OperateToSleep",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6556", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(lads_objtypes.LADSDeviceStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5260"])
o6.reference(o6.ns["ns=lads;i=5260"], "i=51", o6.ns["ns=lads;i=5178"])
o6.reference(o6.ns["ns=lads;i=5260"], "i=52", o6.ns["ns=lads;i=5259"])
o6.reference(o6.ns["ns=lads;i=5260"], "i=53", o6.ns["ns=lads;i=7032"])
o6.reference(o6.ns["ns=lads;i=5260"], "i=54", "i=2311")
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=lads;i=6600",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6601", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)


ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6013",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=lads;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=lads;i=7005", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=lads;i=6013"]))

ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6014",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=lads;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=lads;i=7006", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=lads;i=6014"]))

ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6015",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=lads;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6016",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=lads;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=lads;i=7007", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6015"]), outputArgs=o6.hasProperty(o6.ns["ns=lads;i=6016"]))

ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6021",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=lads;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=lads;i=7008", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=lads;i=6021"]))

di.objtypes.LockingServicesType(
    nodeId="ns=lads;i=5004",
    browseName="ns=di;Lock",
    description="Used to lock the FunctionalUnit.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6017", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6018", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6019", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6020", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=lads;i=7005"]),
        o6.hasComponent(o6.ns["ns=lads;i=7006"]),
        o6.hasComponent(o6.ns["ns=lads;i=7007"]),
        o6.hasComponent(o6.ns["ns=lads;i=7008"]),
    ],
)
o6.reference(lads_objtypes.FunctionalUnitType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5004"])


ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6305",
    browseName="InputArguments",
    description="the definition of the input argument of method 4:FunctionStateMachineTypeType.4:Start",
    modellingRule="Mandatory",
    parent="ns=lads;i=7027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="TargetValue",
            dataType=o6.Double,
            valueRank=-1,
            description=o6.LocalizedText("(Optional) The value can use to set the target value parallel with the start method."),
        )
    ],
)
o6.call(nodeId="ns=lads;i=7027", browseName="ns=lads;StartWithTargetValue", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6305"]))

lads_objtypes.ControlFunctionStateMachineType(
    nodeId="ns=lads;i=5141",
    browseName="ns=lads;ControlFunctionState",
    description="ControlFunctionState is a state machine which represents the execution state and controls the execution of the Function.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=lads;i=7027"])],
)
o6.reference(lads_objtypes.AnalogControlFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5141"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=lads;i=5046",
    browseName="ns=lads;Operational",
    description="Operational is a FunctionalGroup that shall organize the CurrentState property of the StateMachine and all its remote invocable Methods. Furthermore, it shall organize at least the CurrentValue and TargetValue variables.",
    modellingRule="Mandatory",
    references=[o6.organizes(o6.call(nodeId="ns=lads;i=7028", browseName="ns=lads;Stop")), o6.organizes(o6.call(nodeId="ns=lads;i=7029", browseName="ns=lads;Reset"))],
)
o6.reference(lads_objtypes.BaseControlFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5046"])
o6.reference(o6.ns["ns=lads;i=5046"], "i=35", o6.ns["ns=lads;i=6079"])


ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6187",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=lads;i=7030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=lads;i=7030", browseName="Acknowledge", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6187"]))

ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6201",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=lads;i=7038",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=lads;i=7038", browseName="Acknowledge", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6201"]))

ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6202",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=lads;i=7039",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=lads;i=7039", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6202"]))

ns0.objtypes.ExclusiveLevelAlarmType(
    nodeId="ns=lads;i=5069",
    browseName="ns=lads;AlarmMonitor",
    description="AlarmMonitor indicates whether the limit of an analogue Sensor is exceeded. See: 10000-9: Alarms & Conditions | ExclusiveLevelAlarmType.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6197", browseName="InputNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6198", browseName="SuppressedOrShelved", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6203", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6204", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6207", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6208", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6209", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6214", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6215", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6216", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6217", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6218", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6219", browseName="Severity", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6220", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6221", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6222", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(o6.ns["ns=lads;i=5070"]),
        o6.hasComponent(o6.ns["ns=lads;i=6191"]),
        o6.hasComponent(o6.ns["ns=lads;i=6195"]),
        o6.hasComponent(o6.ns["ns=lads;i=6199"]),
        o6.hasComponent(o6.ns["ns=lads;i=6205"]),
        o6.hasComponent(o6.ns["ns=lads;i=6210"]),
        o6.hasComponent(o6.ns["ns=lads;i=6212"]),
        o6.hasComponent(o6.ns["ns=lads;i=7038"]),
        o6.hasComponent(o6.ns["ns=lads;i=7039"]),
        o6.hasComponent(o6.call(nodeId="ns=lads;i=7040", browseName="Disable")),
        o6.hasComponent(o6.call(nodeId="ns=lads;i=7041", browseName="Enable")),
    ],
)
o6.reference(lads_objtypes.AnalogSensorFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5069"])


ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6234",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=lads;i=7042",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=lads;i=7042", browseName="Acknowledge", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6234"]))
o6.reference(o6.ns["ns=lads;i=7042"], "i=3065", "i=8944")

ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6235",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=lads;i=7043",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=lads;i=7043", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6235"]))
o6.reference(o6.ns["ns=lads;i=7043"], "i=3065", "i=2829")

o6.call(nodeId="ns=lads;i=7044", browseName="Disable")
o6.reference(o6.ns["ns=lads;i=7044"], "i=3065", "i=2803")

o6.call(nodeId="ns=lads;i=7045", browseName="Enable")
o6.reference(o6.ns["ns=lads;i=7045"], "i=3065", "i=2803")

ns0.objtypes.ExclusiveDeviationAlarmType(
    nodeId="ns=lads;i=5068",
    browseName="ns=lads;AlarmMonitor",
    description="AlarmMonitor indicates whether the deviation from a set point exceeds the limit. See: 10000-9: Alarms & Conditions | ExclusiveDeviationAlarmType.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6023", browseName="HighHighLimit", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6024", browseName="HighLimit", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6025", browseName="LowLimit", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6026", browseName="LowLowLimit", dataType=o6.Double)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6223", browseName="SetpointNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6230", browseName="InputNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6231", browseName="SuppressedOrShelved", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6236", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6237", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6240", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6241", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6242", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6247", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6248", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6249", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6250", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6251", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6252", browseName="Severity", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6253", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6254", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6255", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasComponent(o6.ns["ns=lads;i=5071"]),
        o6.hasComponent(o6.ns["ns=lads;i=6224"]),
        o6.hasComponent(o6.ns["ns=lads;i=6228"]),
        o6.hasComponent(o6.ns["ns=lads;i=6232"]),
        o6.hasComponent(o6.ns["ns=lads;i=6238"]),
        o6.hasComponent(o6.ns["ns=lads;i=6243"]),
        o6.hasComponent(o6.ns["ns=lads;i=6245"]),
        o6.hasComponent(o6.ns["ns=lads;i=7042"]),
        o6.hasComponent(o6.ns["ns=lads;i=7043"]),
        o6.hasComponent(o6.ns["ns=lads;i=7044"]),
        o6.hasComponent(o6.ns["ns=lads;i=7045"]),
    ],
)
o6.reference(lads_objtypes.BaseControlFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5068"])


ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6142",
    browseName="InputArguments",
    description="the definition of the input argument of method 4:FunctionalUnitStateMachineType.4:StartProgram",
    modellingRule="Mandatory",
    parent="ns=lads;i=7046",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(
            name="Properties", dataType=o6.NodeId("ns=lads;i=3003"), valueRank=1, description=o6.LocalizedText("A Key/Value set for parameterization of the program.")
        ),
        ns0.datatypes.Argument(name="SupervisoryJobId", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="SupervisoryTaskId", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The ID of the SupervisoryTask.")),
        ns0.datatypes.Argument(
            name="Samples",
            dataType=o6.NodeId("ns=lads;i=3002"),
            valueRank=1,
            arrayDimensions=[1],
            description=o6.LocalizedText("An array of the SampleInfoType that describes the samples processed in this program execution."),
        ),
        ns0.datatypes.Argument(
            name="ProgramTemplateId", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The ID of the program template that is used for the current execution.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6143",
    browseName="OutputArguments",
    description="the definition of the output arguments of method 4:FunctionalUnitStateMachineType.4:StartProgram",
    modellingRule="Mandatory",
    parent="ns=lads;i=7046",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DeviceProgramRunId", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The ID of the created program run."))],
)
o6.call(nodeId="ns=lads;i=7046", browseName="ns=lads;StartProgram", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6142"]), outputArgs=o6.hasProperty(o6.ns["ns=lads;i=6143"]))

di.objtypes.FunctionalGroupType(
    nodeId="ns=lads;i=5007",
    browseName="ns=lads;Operational",
    description="Parameters and Methods useful for during normal operation, like process data.",
    modellingRule="Optional",
    references=[
        o6.organizes(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6105", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.organizes(o6.call(nodeId="ns=lads;i=7019", browseName="ns=lads;Clear")),
        o6.organizes(o6.call(nodeId="ns=lads;i=7024", browseName="ns=lads;Stop")),
        o6.organizes(o6.call(nodeId="ns=lads;i=7025", browseName="ns=lads;Abort")),
        o6.organizes(o6.ns["ns=lads;i=7046"]),
    ],
)
o6.reference(lads_objtypes.FunctionalUnitType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5007"])


ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6267",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=lads;i=7049",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="EventId", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("The identifier for the event to comment.")),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The comment to add to the condition.")),
    ],
)
o6.call(nodeId="ns=lads;i=7049", browseName="AddComment", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6267"]))

lads_objtypes.MaintenanceTaskType(
    nodeId="ns=lads;i=5017",
    browseName="ns=lads;<SetElement>",
    description="The MaintenanceTaskType shall be used to implement instances of maintenance tasks applicable at both the Device and Component levels. Maintenance tasks include activities such as periodic maintenance, cleaning, calibration, and validation.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6164", browseName="NormalState", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6178", browseName="SuppressedOrShelved", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6179", browseName="InputNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6188", browseName="Retain", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6190", browseName="ConditionName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6256", browseName="BranchId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6266", browseName="ClientUserId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6268", browseName="ConditionClassId", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6269", browseName="ConditionClassName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6270", browseName="EventId", dataType=o6.ByteString)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6271", browseName="EventType", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6272", browseName="SourceNode", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6273", browseName="SourceName", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6274", browseName="Time", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6276", browseName="ReceiveTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6277", browseName="Message", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=lads;i=6278", browseName="Severity", dataType=o6.UInt16)),
        o6.hasComponent(
            amb.objtypes.MaintenanceEventStateMachineType(
                nodeId="ns=lads;i=5018",
                browseName="ns=amb;MaintenanceState",
                description="The MaintenanceState state-machine provides information, whether a maintenance activity is planned, currently in execution, of has been executed.",
            )
        ),
        o6.hasComponent(o6.ns["ns=lads;i=6166"]),
        o6.hasComponent(o6.ns["ns=lads;i=6168"]),
        o6.hasComponent(o6.ns["ns=lads;i=6181"]),
        o6.hasComponent(o6.ns["ns=lads;i=6260"]),
        o6.hasComponent(o6.ns["ns=lads;i=6262"]),
        o6.hasComponent(o6.ns["ns=lads;i=6264"]),
        o6.hasComponent(o6.ns["ns=lads;i=7030"]),
        o6.hasComponent(o6.call(nodeId="ns=lads;i=7047", browseName="Enable")),
        o6.hasComponent(o6.call(nodeId="ns=lads;i=7048", browseName="Disable")),
        o6.hasComponent(o6.ns["ns=lads;i=7049"]),
    ],
)
o6.reference(lads_objtypes.MaintenanceSetType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5017"])


ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6306",
    browseName="InputArguments",
    description="the definition of the input argument of method 4:FunctionStateMachineTypeType.4:Start",
    modellingRule="Mandatory",
    parent="ns=lads;i=7050",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="TargetValue",
            dataType=o6.UInt32,
            valueRank=-1,
            description=o6.LocalizedText("(Optional) The value can use to set the target value parallel with the start method."),
        )
    ],
)
o6.call(nodeId="ns=lads;i=7050", browseName="ns=lads;StartWithTargetValue", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6306"]))

lads_objtypes.ControlFunctionStateMachineType(
    nodeId="ns=lads;i=5142",
    browseName="ns=lads;ControlFunctionState",
    description="ControlFunctionState is a state machine which represents the execution state and controls the execution of the Function.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=lads;i=7050"])],
)
o6.reference(lads_objtypes.MultiStateDiscreteControlFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5142"])


ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6309",
    browseName="InputArguments",
    description="the definition of the input argument of method 4:FunctionStateMachineTypeType.4:Start",
    modellingRule="Mandatory",
    parent="ns=lads;i=7054",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="TargetValue",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("(Optional) The value can use to set the target value parallel with the start method."),
        )
    ],
)
o6.call(nodeId="ns=lads;i=7054", browseName="ns=lads;StartWithTargetValue", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6309"]))

lads_objtypes.ControlFunctionStateMachineType(
    nodeId="ns=lads;i=5144",
    browseName="ns=lads;ControlFunctionState",
    description="ControlFunctionState is a state machine which represents the execution state and controls the execution of the Function.",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=lads;i=7054"])],
)
o6.reference(lads_objtypes.TwoStateDiscreteControlFunctionType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5144"])
lads_objtypes.LADSDeviceStateMachineType(
    nodeId="ns=lads;i=5191",
    browseName="ns=lads;DeviceState",
    description="DeviceState represents the Device’s state of operation. It is inspired by the AnalyserDeviceStateMachineType from the Analyzer Devices Specification.",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=lads;i=6600"]),
        o6.hasComponent(o6.call(nodeId="ns=lads;i=7124", browseName="ns=lads;GotoOperate")),
        o6.hasComponent(o6.call(nodeId="ns=lads;i=7125", browseName="ns=lads;GotoShutdown")),
        o6.hasComponent(o6.call(nodeId="ns=lads;i=7126", browseName="ns=lads;GotoSleep")),
    ],
)
o6.reference(lads_objtypes.LADSDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=lads;i=5191"])


del Any, TYPE_CHECKING, uuid, o6, amb, di, ia, machinery, ns0, lads_datypes, lads_objtypes
