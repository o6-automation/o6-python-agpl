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

"""Generated OPC UA di namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as di_reftypes
from . import datatypes as di_datypes
from . import vartypes as di_vartypes
from . import objtypes as di_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=di;i=5",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
di_objtypes.PrepareForUpdateStateMachineType(
    nodeId="ns=di;i=4",
    browseName="ns=di;PrepareForUpdate",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=di;i=5"]),
        o6.hasComponent(o6.call(nodeId="ns=di;i=19", browseName="ns=di;Prepare")),
        o6.hasComponent(o6.call(nodeId="ns=di;i=20", browseName="ns=di;Abort")),
    ],
)
o6.reference(di_objtypes.SoftwareUpdateType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=4"])


ns0.vartypes.PropertyType(
    nodeId="ns=di;i=37",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=36",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=38",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=36",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=36", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=di;i=37"]), outputArgs=o6.hasProperty(o6.ns["ns=di;i=38"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=62",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=39",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=39", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=di;i=62"]))

ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=di;i=41",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=42", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
di_objtypes.InstallationStateMachineType(
    nodeId="ns=di;i=40",
    browseName="ns=di;Installation",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=di;i=41"]), o6.hasComponent(o6.call(nodeId="ns=di;i=61", browseName="ns=di;Resume"))],
)
o6.reference(di_objtypes.SoftwareUpdateType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=40"])


ns0.vartypes.PropertyType(
    nodeId="ns=di;i=64",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=63",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=65",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=63",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=63", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=di;i=64"]), outputArgs=o6.hasProperty(o6.ns["ns=di;i=65"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=67",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=66",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=66", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=di;i=67"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=69",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=68",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=70",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=68",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=68", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=di;i=69"]), outputArgs=o6.hasProperty(o6.ns["ns=di;i=70"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=72",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=71",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=71", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=di;i=72"]))

ns0.objtypes.FileType(
    nodeId="ns=di;i=28",
    browseName="ns=di;<DocumentFileId>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=29", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=30", browseName="Writable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=31", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=32", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=di;i=36"]),
        o6.hasComponent(o6.ns["ns=di;i=39"]),
        o6.hasComponent(o6.ns["ns=di;i=63"]),
        o6.hasComponent(o6.ns["ns=di;i=66"]),
        o6.hasComponent(o6.ns["ns=di;i=68"]),
        o6.hasComponent(o6.ns["ns=di;i=71"]),
    ],
)
ns0.objtypes.FolderType(nodeId="ns=di;i=27", browseName="ns=di;DocumentationFiles", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=di;i=28"])])
o6.reference(di_objtypes.ISupportInfoType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=27"])
configuration = di_objtypes.FunctionalGroupType(nodeId="ns=di;i=73", browseName="ns=di;Configuration")
tuning = di_objtypes.FunctionalGroupType(nodeId="ns=di;i=74", browseName="ns=di;Tuning")
maintenance = di_objtypes.FunctionalGroupType(nodeId="ns=di;i=75", browseName="ns=di;Maintenance")
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=di;i=77",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=78", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
di_objtypes.PowerCycleStateMachineType(nodeId="ns=di;i=76", browseName="ns=di;PowerCycle", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=di;i=77"])])
o6.reference(di_objtypes.SoftwareUpdateType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=76"])
diagnostics = di_objtypes.FunctionalGroupType(nodeId="ns=di;i=90", browseName="ns=di;Diagnostics")
statistics = di_objtypes.FunctionalGroupType(nodeId="ns=di;i=91", browseName="ns=di;Statistics")
status = di_objtypes.FunctionalGroupType(nodeId="ns=di;i=92", browseName="ns=di;Status")
operational = di_objtypes.FunctionalGroupType(nodeId="ns=di;i=93", browseName="ns=di;Operational")
operationCounters = di_objtypes.FunctionalGroupType(nodeId="ns=di;i=94", browseName="ns=di;OperationCounters")
identification = di_objtypes.FunctionalGroupType(nodeId="ns=di;i=95", browseName="ns=di;Identification")
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=di;i=99",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=100", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
di_objtypes.ConfirmationStateMachineType(
    nodeId="ns=di;i=98",
    browseName="ns=di;Confirmation",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=di;i=99"]),
        o6.hasComponent(o6.call(nodeId="ns=di;i=112", browseName="ns=di;Confirm")),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=113", browseName="ns=di;ConfirmationTimeout", dataType=ns0.datatypes.Duration)),
    ],
)
o6.reference(di_objtypes.SoftwareUpdateType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=98"])


ns0.vartypes.PropertyType(
    nodeId="ns=di;i=125",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=124",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=ns0.datatypes.BaseDataType, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=126",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=124",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1),
    ],
)
o6.call(nodeId="ns=di;i=124", browseName="GenerateFileForRead", inputArgs=o6.hasProperty(o6.ns["ns=di;i=125"]), outputArgs=o6.hasProperty(o6.ns["ns=di;i=126"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=128",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=127",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=ns0.datatypes.BaseDataType, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=129",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=127",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=127", browseName="GenerateFileForWrite", inputArgs=o6.hasProperty(o6.ns["ns=di;i=128"]), outputArgs=o6.hasProperty(o6.ns["ns=di;i=129"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=131",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=130",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=132",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=130",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=130", browseName="CloseAndCommit", inputArgs=o6.hasProperty(o6.ns["ns=di;i=131"]), outputArgs=o6.hasProperty(o6.ns["ns=di;i=132"]))

ns0.objtypes.TemporaryFileTransferType(
    nodeId="ns=di;i=122",
    browseName="ns=di;Parameters",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=123", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=di;i=124"]),
        o6.hasComponent(o6.ns["ns=di;i=127"]),
        o6.hasComponent(o6.ns["ns=di;i=130"]),
    ],
)
o6.reference(di_objtypes.SoftwareUpdateType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=122"])


ns0.vartypes.PropertyType(
    nodeId="ns=di;i=143",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=142",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=ns0.datatypes.BaseDataType, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=144",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=142",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1),
    ],
)
o6.call(nodeId="ns=di;i=142", browseName="GenerateFileForRead", inputArgs=o6.hasProperty(o6.ns["ns=di;i=143"]), outputArgs=o6.hasProperty(o6.ns["ns=di;i=144"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=146",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=145",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=ns0.datatypes.BaseDataType, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=147",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=145",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=145", browseName="GenerateFileForWrite", inputArgs=o6.hasProperty(o6.ns["ns=di;i=146"]), outputArgs=o6.hasProperty(o6.ns["ns=di;i=147"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=149",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=148",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=150",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=148",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=148", browseName="CloseAndCommit", inputArgs=o6.hasProperty(o6.ns["ns=di;i=149"]), outputArgs=o6.hasProperty(o6.ns["ns=di;i=150"]))

ns0.objtypes.TemporaryFileTransferType(
    nodeId="ns=di;i=140",
    browseName="ns=di;FileTransfer",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=141", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=di;i=142"]),
        o6.hasComponent(o6.ns["ns=di;i=145"]),
        o6.hasComponent(o6.ns["ns=di;i=148"]),
    ],
)
o6.reference(di_objtypes.PackageLoadingType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=140"])


ns0.vartypes.PropertyType(
    nodeId="ns=di;i=196",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=195",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryName", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=197",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=195",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DirectoryNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=195", browseName="CreateDirectory", inputArgs=o6.hasProperty(o6.ns["ns=di;i=196"]), outputArgs=o6.hasProperty(o6.ns["ns=di;i=197"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=199",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=198",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileName", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="RequestFileOpen", dataType=o6.Boolean, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=200",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=198",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=198", browseName="CreateFile", inputArgs=o6.hasProperty(o6.ns["ns=di;i=199"]), outputArgs=o6.hasProperty(o6.ns["ns=di;i=200"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=202",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=201",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ObjectToDelete", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=201", browseName="Delete", inputArgs=o6.hasProperty(o6.ns["ns=di;i=202"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=204",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=203",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="ObjectToMoveOrCopy", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="TargetDirectory", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="CreateCopy", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="NewName", dataType=o6.String, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=205",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=203",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NewNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=203", browseName="MoveOrCopy", inputArgs=o6.hasProperty(o6.ns["ns=di;i=204"]), outputArgs=o6.hasProperty(o6.ns["ns=di;i=205"]))

ns0.objtypes.FileDirectoryType(
    nodeId="ns=di;i=194",
    browseName="FileSystem",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=di;i=195"]), o6.hasComponent(o6.ns["ns=di;i=198"]), o6.hasComponent(o6.ns["ns=di;i=201"]), o6.hasComponent(o6.ns["ns=di;i=203"])],
)
o6.reference(di_objtypes.FileSystemLoadingType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=194"])
ns0.objtypes.InitialStateType(
    nodeId="ns=di;i=231",
    browseName="ns=di;Idle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=232", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(di_objtypes.PrepareForUpdateStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=231"])
ns0.objtypes.StateType(
    nodeId="ns=di;i=233",
    browseName="ns=di;Preparing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=234", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(di_objtypes.PrepareForUpdateStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=233"])
ns0.objtypes.StateType(
    nodeId="ns=di;i=235",
    browseName="ns=di;PreparedForUpdate",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=236", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(di_objtypes.PrepareForUpdateStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=235"])
ns0.objtypes.StateType(
    nodeId="ns=di;i=237",
    browseName="ns=di;Resuming",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=238", browseName="StateNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(di_objtypes.PrepareForUpdateStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=237"])
ns0.objtypes.TransitionType(
    nodeId="ns=di;i=239",
    browseName="ns=di;IdleToPreparing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=240", browseName="TransitionNumber", dataType=o6.UInt32, value=12))],
)
o6.reference(di_objtypes.PrepareForUpdateStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=239"])
o6.reference(o6.ns["ns=di;i=239"], "i=51", o6.ns["ns=di;i=231"])
o6.reference(o6.ns["ns=di;i=239"], "i=52", o6.ns["ns=di;i=233"])
o6.reference(o6.ns["ns=di;i=239"], "i=53", o6.ns["ns=di;i=228"])
o6.reference(o6.ns["ns=di;i=239"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=di;i=241",
    browseName="ns=di;PreparingToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=242", browseName="TransitionNumber", dataType=o6.UInt32, value=21))],
)
o6.reference(di_objtypes.PrepareForUpdateStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=241"])
o6.reference(o6.ns["ns=di;i=241"], "i=51", o6.ns["ns=di;i=233"])
o6.reference(o6.ns["ns=di;i=241"], "i=52", o6.ns["ns=di;i=231"])
o6.reference(o6.ns["ns=di;i=241"], "i=53", o6.ns["ns=di;i=229"])
o6.reference(o6.ns["ns=di;i=241"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=di;i=243",
    browseName="ns=di;PreparingToPreparedForUpdate",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=244", browseName="TransitionNumber", dataType=o6.UInt32, value=23))],
)
o6.reference(di_objtypes.PrepareForUpdateStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=243"])
o6.reference(o6.ns["ns=di;i=243"], "i=51", o6.ns["ns=di;i=233"])
o6.reference(o6.ns["ns=di;i=243"], "i=52", o6.ns["ns=di;i=235"])
o6.reference(o6.ns["ns=di;i=243"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=di;i=245",
    browseName="ns=di;PreparedForUpdateToResuming",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=246", browseName="TransitionNumber", dataType=o6.UInt32, value=34))],
)
o6.reference(di_objtypes.PrepareForUpdateStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=245"])
o6.reference(o6.ns["ns=di;i=245"], "i=51", o6.ns["ns=di;i=235"])
o6.reference(o6.ns["ns=di;i=245"], "i=52", o6.ns["ns=di;i=237"])
o6.reference(o6.ns["ns=di;i=245"], "i=53", o6.ns["ns=di;i=230"])
o6.reference(o6.ns["ns=di;i=245"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=di;i=247",
    browseName="ns=di;ResumingToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=248", browseName="TransitionNumber", dataType=o6.UInt32, value=41))],
)
o6.reference(di_objtypes.PrepareForUpdateStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=247"])
o6.reference(o6.ns["ns=di;i=247"], "i=51", o6.ns["ns=di;i=237"])
o6.reference(o6.ns["ns=di;i=247"], "i=52", o6.ns["ns=di;i=231"])
o6.reference(o6.ns["ns=di;i=247"], "i=53", o6.ns["ns=di;i=229"])
o6.reference(o6.ns["ns=di;i=247"], "i=54", "i=2311")
ns0.objtypes.InitialStateType(
    nodeId="ns=di;i=271",
    browseName="ns=di;Idle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=272", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(di_objtypes.InstallationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=271"])
ns0.objtypes.StateType(
    nodeId="ns=di;i=273",
    browseName="ns=di;Installing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=274", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(di_objtypes.InstallationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=273"])
ns0.objtypes.StateType(
    nodeId="ns=di;i=275",
    browseName="ns=di;Error",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=276", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(di_objtypes.InstallationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=275"])
ns0.objtypes.TransitionType(
    nodeId="ns=di;i=279",
    browseName="ns=di;InstallingToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=280", browseName="TransitionNumber", dataType=o6.UInt32, value=21))],
)
o6.reference(di_objtypes.InstallationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=279"])
o6.reference(o6.ns["ns=di;i=279"], "i=51", o6.ns["ns=di;i=273"])
o6.reference(o6.ns["ns=di;i=279"], "i=52", o6.ns["ns=di;i=271"])
o6.reference(o6.ns["ns=di;i=279"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=di;i=281",
    browseName="ns=di;InstallingToError",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=282", browseName="TransitionNumber", dataType=o6.UInt32, value=23))],
)
o6.reference(di_objtypes.InstallationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=281"])
o6.reference(o6.ns["ns=di;i=281"], "i=51", o6.ns["ns=di;i=273"])
o6.reference(o6.ns["ns=di;i=281"], "i=52", o6.ns["ns=di;i=275"])
o6.reference(o6.ns["ns=di;i=281"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=di;i=283",
    browseName="ns=di;ErrorToIdle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=284", browseName="TransitionNumber", dataType=o6.UInt32, value=31))],
)
o6.reference(di_objtypes.InstallationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=283"])
o6.reference(o6.ns["ns=di;i=283"], "i=51", o6.ns["ns=di;i=275"])
o6.reference(o6.ns["ns=di;i=283"], "i=52", o6.ns["ns=di;i=271"])
o6.reference(o6.ns["ns=di;i=283"], "i=53", o6.ns["ns=di;i=270"])
o6.reference(o6.ns["ns=di;i=283"], "i=54", "i=2311")
ns0.objtypes.InitialStateType(
    nodeId="ns=di;i=299",
    browseName="ns=di;NotWaitingForPowerCycle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=300", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(di_objtypes.PowerCycleStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=299"])
ns0.objtypes.StateType(
    nodeId="ns=di;i=301",
    browseName="ns=di;WaitingForPowerCycle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=302", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(di_objtypes.PowerCycleStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=301"])
ns0.objtypes.TransitionType(
    nodeId="ns=di;i=303",
    browseName="ns=di;NotWaitingForPowerCycleToWaitingForPowerCycle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=304", browseName="TransitionNumber", dataType=o6.UInt32, value=12))],
)
o6.reference(di_objtypes.PowerCycleStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=303"])
o6.reference(o6.ns["ns=di;i=303"], "i=51", o6.ns["ns=di;i=299"])
o6.reference(o6.ns["ns=di;i=303"], "i=52", o6.ns["ns=di;i=301"])
o6.reference(o6.ns["ns=di;i=303"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=di;i=305",
    browseName="ns=di;WaitingForPowerCycleToNotWaitingForPowerCycle",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=306", browseName="TransitionNumber", dataType=o6.UInt32, value=21))],
)
o6.reference(di_objtypes.PowerCycleStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=305"])
o6.reference(o6.ns["ns=di;i=305"], "i=51", o6.ns["ns=di;i=301"])
o6.reference(o6.ns["ns=di;i=305"], "i=52", o6.ns["ns=di;i=299"])
o6.reference(o6.ns["ns=di;i=305"], "i=54", "i=2311")
ns0.objtypes.InitialStateType(
    nodeId="ns=di;i=323",
    browseName="ns=di;NotWaitingForConfirm",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=324", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(di_objtypes.ConfirmationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=323"])
ns0.objtypes.StateType(
    nodeId="ns=di;i=325",
    browseName="ns=di;WaitingForConfirm",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=326", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(di_objtypes.ConfirmationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=325"])
ns0.objtypes.TransitionType(
    nodeId="ns=di;i=327",
    browseName="ns=di;NotWaitingForConfirmToWaitingForConfirm",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=328", browseName="TransitionNumber", dataType=o6.UInt32, value=12))],
)
o6.reference(di_objtypes.ConfirmationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=327"])
o6.reference(o6.ns["ns=di;i=327"], "i=51", o6.ns["ns=di;i=323"])
o6.reference(o6.ns["ns=di;i=327"], "i=52", o6.ns["ns=di;i=325"])
o6.reference(o6.ns["ns=di;i=327"], "i=54", "i=2311")
ns0.objtypes.TransitionType(
    nodeId="ns=di;i=329",
    browseName="ns=di;WaitingForConfirmToNotWaitingForConfirm",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=330", browseName="TransitionNumber", dataType=o6.UInt32, value=21))],
)
o6.reference(di_objtypes.ConfirmationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=329"])
o6.reference(o6.ns["ns=di;i=329"], "i=51", o6.ns["ns=di;i=325"])
o6.reference(o6.ns["ns=di;i=329"], "i=52", o6.ns["ns=di;i=323"])
o6.reference(o6.ns["ns=di;i=329"], "i=53", o6.ns["ns=di;i=321"])
o6.reference(o6.ns["ns=di;i=329"], "i=54", "i=2311")
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=332",
    browseName="EnumStrings",
    parent="ns=di;i=331",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("Current"), o6.LocalizedText("Pending"), o6.LocalizedText("Fallback")],
)
di_objtypes.SoftwareVersionType(
    nodeId="ns=di;i=139",
    browseName="ns=di;CurrentVersion",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=345", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=346", browseName="ns=di;ManufacturerUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=347", browseName="ns=di;SoftwareRevision", dataType=o6.String)),
    ],
)
o6.reference(di_objtypes.PackageLoadingType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=139"])
di_objtypes.SoftwareVersionType(
    nodeId="ns=di;i=187",
    browseName="ns=di;PendingVersion",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=366", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=367", browseName="ns=di;ManufacturerUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=368", browseName="ns=di;SoftwareRevision", dataType=o6.String)),
    ],
)
o6.reference(di_objtypes.CachedLoadingType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=187"])
di_objtypes.SoftwareVersionType(
    nodeId="ns=di;i=188",
    browseName="ns=di;FallbackVersion",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=373", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=374", browseName="ns=di;ManufacturerUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=375", browseName="ns=di;SoftwareRevision", dataType=o6.String)),
    ],
)
o6.reference(di_objtypes.CachedLoadingType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=188"])
ns0.objtypes.TransitionType(
    nodeId="ns=di;i=277",
    browseName="ns=di;IdleToInstalling",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=387", browseName="TransitionNumber", dataType=o6.UInt32, value=12))],
)
o6.reference(di_objtypes.InstallationStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=277"])
o6.reference(o6.ns["ns=di;i=277"], "i=51", o6.ns["ns=di;i=271"])
o6.reference(o6.ns["ns=di;i=277"], "i=52", o6.ns["ns=di;i=273"])
o6.reference(o6.ns["ns=di;i=277"], "i=53", o6.ns["ns=di;i=265"])
o6.reference(o6.ns["ns=di;i=277"], "i=53", o6.ns["ns=di;i=268"])
o6.reference(o6.ns["ns=di;i=277"], "i=53", o6.ns["ns=di;i=407"])
o6.reference(o6.ns["ns=di;i=277"], "i=54", "i=2311")
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=388",
    browseName="OptionSetValues",
    parent="ns=di;i=333",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        o6.LocalizedText("KeepsParameters"),
        o6.LocalizedText("WillDisconnect"),
        o6.LocalizedText("RequiresPowerCycle"),
        o6.LocalizedText("WillReboot"),
        o6.LocalizedText("NeedsPreparation"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=409",
    browseName="EnumStrings",
    parent="ns=di;i=408",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("Firmware"), o6.LocalizedText("Application"), o6.LocalizedText("Configuration"), o6.LocalizedText("Solution")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=411",
    browseName="OptionSetValues",
    parent="ns=di;i=410",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("Visual"), o6.LocalizedText("Audible")],
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=di;i=5002",
    browseName="ns=di;ParameterSet",
    modellingRule="Optional",
    references=[o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=6017", browseName="ns=di;<ParameterIdentifier>", modellingRule="MandatoryPlaceholder"))],
)
o6.reference(di_objtypes.TopologyElementType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=5002"])
networkSet = ns0.objtypes.BaseObjectType(nodeId="ns=di;i=6078", browseName="ns=di;NetworkSet", parent="i=85", referenceType=ns0.reftypes.Organizes)
deviceTopology = ns0.objtypes.BaseObjectType(
    nodeId="ns=di;i=6094",
    browseName="ns=di;DeviceTopology",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6095", browseName="ns=di;OnlineAccess", dataType=o6.Boolean))],
    parent="i=85",
    referenceType=ns0.reftypes.Organizes,
)


ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6167",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=6166",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6168",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=6166",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=6166", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=di;i=6167"]), outputArgs=o6.hasProperty(o6.ns["ns=di;i=6168"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6170",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=6169",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=6169", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=di;i=6170"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6172",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=6171",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=6171", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=di;i=6172"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6174",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=6173",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=6173", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=di;i=6174"]))

ns0.objtypes.FolderType(
    nodeId="ns=di;i=6209",
    browseName="ns=di;DeviceTypeImage",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=6210", browseName="ns=di;<ImageIdentifier>", modellingRule="MandatoryPlaceholder", dataType=ns0.datatypes.Image)
        )
    ],
)
o6.reference(di_objtypes.DeviceType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=6209"])
ns0.objtypes.FolderType(
    nodeId="ns=di;i=6211",
    browseName="ns=di;Documentation",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=6212", browseName="ns=di;<DocumentIdentifier>", modellingRule="MandatoryPlaceholder", dataType=o6.ByteString)
        )
    ],
)
o6.reference(di_objtypes.DeviceType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=6211"])
ns0.objtypes.FolderType(
    nodeId="ns=di;i=6213",
    browseName="ns=di;ProtocolSupport",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=6214", browseName="ns=di;<ProtocolSupportIdentifier>", modellingRule="MandatoryPlaceholder", dataType=o6.ByteString)
        )
    ],
)
o6.reference(di_objtypes.DeviceType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=6213"])
ns0.objtypes.FolderType(
    nodeId="ns=di;i=6215",
    browseName="ns=di;ImageSet",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=6216", browseName="ns=di;<ImageIdentifier>", modellingRule="MandatoryPlaceholder", dataType=ns0.datatypes.Image)
        )
    ],
)
o6.reference(di_objtypes.DeviceType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=6215"])
di_objtypes.FunctionalGroupType(
    nodeId="ns=di;i=6027",
    browseName="ns=di;<GroupIdentifier>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(di_vartypes.UIElementType(nodeId="ns=di;i=6242", browseName="ns=di;UIElement", _allow_abstract=True))],
)
o6.reference(di_objtypes.FunctionalGroupType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=6027"])
langleCPIdentifierRangle = di_objtypes.ConnectionPointType(
    nodeId="ns=di;i=6248",
    browseName="ns=di;<CPIdentifier>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(di_objtypes.FunctionalGroupType(nodeId="ns=di;i=6292", browseName="ns=di;NetworkAddress"))],
    _allow_abstract=True,
)
o6.reference(di_objtypes.NetworkType, "ns=di;i=6030", "ns=di;i=6248")
o6.reference(langleCPIdentifierRangle, "i=47", o6.ns["ns=di;i=6499"])


ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6300",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=6299",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6301",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=6299",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=6299", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=di;i=6300"]), outputArgs=o6.hasProperty(o6.ns["ns=di;i=6301"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6303",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=6302",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=6302", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=di;i=6303"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6305",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=6304",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=6304", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=di;i=6305"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6307",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=6306",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=6306", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=di;i=6307"]))

maxInactiveLockTime = ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6387", browseName="ns=di;MaxInactiveLockTime", parent="i=2268", referenceType=ns0.reftypes.HasProperty, dataType=ns0.datatypes.Duration
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6450",
    browseName="EnumStrings",
    parent="ns=di;i=6244",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[5],
    value=[o6.LocalizedText("NORMAL"), o6.LocalizedText("FAILURE"), o6.LocalizedText("CHECK_FUNCTION"), o6.LocalizedText("OFF_SPEC"), o6.LocalizedText("MAINTENANCE_REQUIRED")],
)
di_objtypes.LockingServicesType(
    nodeId="ns=di;i=6161",
    browseName="ns=di;Lock",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6163", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6164", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6165", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6468", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=di;i=6166"]),
        o6.hasComponent(o6.ns["ns=di;i=6169"]),
        o6.hasComponent(o6.ns["ns=di;i=6171"]),
        o6.hasComponent(o6.ns["ns=di;i=6173"]),
    ],
)
o6.reference(di_objtypes.TopologyElementType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=6161"])
di_objtypes.LockingServicesType(
    nodeId="ns=di;i=6294",
    browseName="ns=di;Lock",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6296", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6297", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6298", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6497", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=di;i=6299"]),
        o6.hasComponent(o6.ns["ns=di;i=6302"]),
        o6.hasComponent(o6.ns["ns=di;i=6304"]),
        o6.hasComponent(o6.ns["ns=di;i=6306"]),
    ],
)
o6.reference(di_objtypes.NetworkType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=6294"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di;i=6535", browseName="Default XML")
o6.hasEncoding(di_datypes.FetchResultDataType, o6.ns["ns=di;i=6535"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di;i=6538", browseName="Default XML")
o6.hasEncoding(di_datypes.ParameterResultDataType, o6.ns["ns=di;i=6538"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=di;i=6539", browseName="ns=di;FetchResultDataType", dataType=o6.String, value="//xs:element[@name='FetchResultDataType']")
o6.reference(o6.ns["ns=di;i=6535"], "i=39", o6.ns["ns=di;i=6539"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=di;i=6548", browseName="ns=di;ParameterResultDataType", dataType=o6.String, value="//xs:element[@name='ParameterResultDataType']")
o6.reference(o6.ns["ns=di;i=6538"], "i=39", o6.ns["ns=di;i=6548"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di;i=6551", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di;i=6554", browseName="Default Binary")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=di;i=6555", browseName="ns=di;FetchResultDataType", dataType=o6.String, value="FetchResultDataType")
o6.reference(o6.ns["ns=di;i=6551"], "i=39", o6.ns["ns=di;i=6555"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=di;i=6564", browseName="ns=di;ParameterResultDataType", dataType=o6.String, value="ParameterResultDataType")
o6.reference(o6.ns["ns=di;i=6554"], "i=39", o6.ns["ns=di;i=6564"])
di_objtypes.ConnectionPointType(
    nodeId="ns=di;i=6571",
    browseName="ns=di;<CPIdentifier>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(di_objtypes.FunctionalGroupType(nodeId="ns=di;i=6592", browseName="ns=di;NetworkAddress"))],
    _allow_abstract=True,
)
o6.reference(di_objtypes.DeviceType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=6571"])
o6.reference(o6.ns["ns=di;i=6571"], "i=47", o6.ns["ns=di;i=6499"])
langleNetworkIdentifierRangle = di_objtypes.NetworkType(nodeId="ns=di;i=6599", browseName="ns=di;<NetworkIdentifier>", modellingRule="OptionalPlaceholder")
o6.reference(di_objtypes.ConnectionPointType, "ns=di;i=6030", "ns=di;i=6599")
o6.reference(langleNetworkIdentifierRangle, "i=47", o6.ns["ns=di;i=6596"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashDISlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=di;i=15001",
    browseName="ns=di;http://opcfoundation.org/UA/DI/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=489", browseName="ModelVersion", dataType=o6.String, value="1.5.0")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15002", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/DI/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15003", browseName="NamespaceVersion", dataType=o6.String, value="1.05.0")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15004", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-11-15T00:00:00Z"))),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=di;i=15005", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=di;i=15006", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=di;i=15007", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["1:2147483647"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15008", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=di;i=15031", browseName="DefaultRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=di;i=15032", browseName="DefaultUserRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15033", browseName="DefaultAccessRestrictions", dataType=ns0.datatypes.AccessRestrictionType)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
deviceSet = ns0.objtypes.BaseObjectType(
    nodeId="ns=di;i=5001",
    browseName="ns=di;DeviceSet",
    references=[o6.organizes(ns0.objtypes.BaseObjectType(nodeId="ns=di;i=15034", browseName="ns=di;DeviceFeatures"))],
    parent="i=85",
    referenceType=ns0.reftypes.Organizes,
)
ns0.objtypes.FolderType(
    nodeId="ns=di;i=15055",
    browseName="ns=di;DeviceTypeImage",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=15056", browseName="ns=di;<ImageIdentifier>", modellingRule="MandatoryPlaceholder", dataType=ns0.datatypes.Image)
        )
    ],
)
o6.reference(di_objtypes.ISupportInfoType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=15055"])
ns0.objtypes.FolderType(
    nodeId="ns=di;i=15057",
    browseName="ns=di;Documentation",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=15058", browseName="ns=di;<DocumentIdentifier>", modellingRule="MandatoryPlaceholder", dataType=o6.ByteString)
        )
    ],
)
o6.reference(di_objtypes.ISupportInfoType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=15057"])
ns0.objtypes.FolderType(
    nodeId="ns=di;i=15059",
    browseName="ns=di;ProtocolSupport",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=15060", browseName="ns=di;<ProtocolSupportIdentifier>", modellingRule="MandatoryPlaceholder", dataType=o6.ByteString)
        )
    ],
)
o6.reference(di_objtypes.ISupportInfoType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=15059"])
ns0.objtypes.FolderType(
    nodeId="ns=di;i=15061",
    browseName="ns=di;ImageSet",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=15062", browseName="ns=di;<ImageIdentifier>", modellingRule="MandatoryPlaceholder", dataType=ns0.datatypes.Image)
        )
    ],
)
o6.reference(di_objtypes.ISupportInfoType, ns0.reftypes.HasComponent, o6.ns["ns=di;i=15061"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di;i=15891", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di;i=15892", browseName="Default Binary")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=di;i=15894", browseName="ns=di;TransferResultErrorDataType", dataType=o6.String, value="TransferResultErrorDataType")
o6.reference(o6.ns["ns=di;i=15891"], "i=39", o6.ns["ns=di;i=15894"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=di;i=15897", browseName="ns=di;TransferResultDataDataType", dataType=o6.String, value="TransferResultDataDataType")
o6.reference(o6.ns["ns=di;i=15892"], "i=39", o6.ns["ns=di;i=15897"])
opcDotUaDotDi_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=di;i=6435",
    browseName="ns=di;Opc.Ua.Di",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6437", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/DI/")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=di;i=15893", browseName="Deprecated", dataType=o6.Boolean)
        ),
        o6.hasComponent(o6.ns["ns=di;i=6555"]),
        o6.hasComponent(o6.ns["ns=di;i=6564"]),
        o6.hasComponent(o6.ns["ns=di;i=15894"]),
        o6.hasComponent(o6.ns["ns=di;i=15897"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary\r\n  xmlns:opc="http://opcfoundation.org/BinarySchema/"\r\n  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\r\n  xmlns:ua="http://opcfoundation.org/UA/"\r\n  xmlns:tns="http://opcfoundation.org/UA/DI/"\r\n  DefaultByteOrder="LittleEndian"\r\n  TargetNamespace="http://opcfoundation.org/UA/DI/"\r\n>\r\n  <opc:Import Namespace="http://opcfoundation.org/UA/" Location="Opc.Ua.BinarySchema.bsd"/>\r\n\r\n  <opc:EnumeratedType Name="DeviceHealthEnumeration" LengthInBits="32">\r\n    <opc:EnumeratedValue Name="NORMAL" Value="0" />\r\n    <opc:EnumeratedValue Name="FAILURE" Value="1" />\r\n    <opc:EnumeratedValue Name="CHECK_FUNCTION" Value="2" />\r\n    <opc:EnumeratedValue Name="OFF_SPEC" Value="3" />\r\n    <opc:EnumeratedValue Name="MAINTENANCE_REQUIRED" Value="4" />\r\n  </opc:EnumeratedType>\r\n\r\n  <opc:StructuredType Name="FetchResultDataType" BaseType="ua:ExtensionObject">\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="TransferResultErrorDataType" BaseType="tns:FetchResultDataType">\r\n    <opc:Field Name="Status" TypeName="opc:Int32" />\r\n    <opc:Field Name="Diagnostics" TypeName="ua:DiagnosticInfo" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="TransferResultDataDataType" BaseType="tns:FetchResultDataType">\r\n    <opc:Field Name="SequenceNumber" TypeName="opc:Int32" />\r\n    <opc:Field Name="EndOfResults" TypeName="opc:Boolean" />\r\n    <opc:Field Name="NoOfParameterDefs" TypeName="opc:Int32" />\r\n    <opc:Field Name="ParameterDefs" TypeName="tns:ParameterResultDataType" LengthField="NoOfParameterDefs" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="ParameterResultDataType" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="NoOfNodePath" TypeName="opc:Int32" />\r\n    <opc:Field Name="NodePath" TypeName="ua:QualifiedName" LengthField="NoOfNodePath" />\r\n    <opc:Field Name="StatusCode" TypeName="ua:StatusCode" />\r\n    <opc:Field Name="Diagnostics" TypeName="ua:DiagnosticInfo" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:EnumeratedType Name="SoftwareClass" LengthInBits="32">\r\n    <opc:EnumeratedValue Name="Firmware" Value="0" />\r\n    <opc:EnumeratedValue Name="Application" Value="1" />\r\n    <opc:EnumeratedValue Name="Configuration" Value="2" />\r\n    <opc:EnumeratedValue Name="Solution" Value="3" />\r\n  </opc:EnumeratedType>\r\n\r\n  <opc:EnumeratedType Name="LocationIndicationType" LengthInBits="16" IsOptionSet="true">\r\n    <opc:EnumeratedValue Name="None" Value="0" />\r\n    <opc:EnumeratedValue Name="Visual" Value="1" />\r\n    <opc:EnumeratedValue Name="Audible" Value="2" />\r\n  </opc:EnumeratedType>\r\n\r\n  <opc:EnumeratedType Name="SoftwareVersionFileType" LengthInBits="32">\r\n    <opc:EnumeratedValue Name="Current" Value="0" />\r\n    <opc:EnumeratedValue Name="Pending" Value="1" />\r\n    <opc:EnumeratedValue Name="Fallback" Value="2" />\r\n  </opc:EnumeratedType>\r\n\r\n  <opc:EnumeratedType Name="UpdateBehavior" LengthInBits="32" IsOptionSet="true">\r\n    <opc:EnumeratedValue Name="None" Value="0" />\r\n    <opc:EnumeratedValue Name="KeepsParameters" Value="1" />\r\n    <opc:EnumeratedValue Name="WillDisconnect" Value="2" />\r\n    <opc:EnumeratedValue Name="RequiresPowerCycle" Value="4" />\r\n    <opc:EnumeratedValue Name="WillReboot" Value="8" />\r\n    <opc:EnumeratedValue Name="NeedsPreparation" Value="16" />\r\n  </opc:EnumeratedType>\r\n\r\n</opc:TypeDictionary>',
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di;i=15900", browseName="Default XML")
o6.hasEncoding(di_datypes.TransferResultErrorDataType, o6.ns["ns=di;i=15900"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di;i=15901", browseName="Default XML")
o6.hasEncoding(di_datypes.TransferResultDataDataType, o6.ns["ns=di;i=15901"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=di;i=15903", browseName="ns=di;TransferResultErrorDataType", dataType=o6.String, value="//xs:element[@name='TransferResultErrorDataType']"
)
o6.reference(o6.ns["ns=di;i=15900"], "i=39", o6.ns["ns=di;i=15903"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=di;i=15906", browseName="ns=di;TransferResultDataDataType", dataType=o6.String, value="//xs:element[@name='TransferResultDataDataType']"
)
o6.reference(o6.ns["ns=di;i=15901"], "i=39", o6.ns["ns=di;i=15906"])
opcDotUaDotDi = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=di;i=6423",
    browseName="ns=di;Opc.Ua.Di",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6425", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/DI/Types.xsd")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=di;i=15902", browseName="Deprecated", dataType=o6.Boolean)
        ),
        o6.hasComponent(o6.ns["ns=di;i=6539"]),
        o6.hasComponent(o6.ns["ns=di;i=6548"]),
        o6.hasComponent(o6.ns["ns=di;i=15903"]),
        o6.hasComponent(o6.ns["ns=di;i=15906"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema\r\n  xmlns:xs="http://www.w3.org/2001/XMLSchema"\r\n  xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd"\r\n  xmlns:tns="http://opcfoundation.org/UA/DI/Types.xsd"\r\n  targetNamespace="http://opcfoundation.org/UA/DI/Types.xsd"\r\n  elementFormDefault="qualified"\r\n>\r\n  <xs:annotation>\r\n    <xs:appinfo>\r\n      <ua:Model ModelUri="http://opcfoundation.org/UA/DI/" Version="1.05.0" PublicationDate="2025-11-15T00:00:00Z" />\r\n    </xs:appinfo>\r\n  </xs:annotation>\r\n  \r\n  <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd" />\r\n\r\n  <xs:simpleType  name="DeviceHealthEnumeration">\r\n    <xs:restriction base="xs:string">\r\n      <xs:enumeration value="NORMAL_0" />\r\n      <xs:enumeration value="FAILURE_1" />\r\n      <xs:enumeration value="CHECK_FUNCTION_2" />\r\n      <xs:enumeration value="OFF_SPEC_3" />\r\n      <xs:enumeration value="MAINTENANCE_REQUIRED_4" />\r\n    </xs:restriction>\r\n  </xs:simpleType>\r\n  <xs:element name="DeviceHealthEnumeration" type="tns:DeviceHealthEnumeration" />\r\n\r\n  <xs:complexType name="ListOfDeviceHealthEnumeration">\r\n    <xs:sequence>\r\n      <xs:element name="DeviceHealthEnumeration" type="tns:DeviceHealthEnumeration" minOccurs="0" maxOccurs="unbounded" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfDeviceHealthEnumeration" type="tns:ListOfDeviceHealthEnumeration" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="FetchResultDataType">\r\n    <xs:sequence>\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="FetchResultDataType" type="tns:FetchResultDataType" />\r\n\r\n  <xs:complexType name="ListOfFetchResultDataType">\r\n    <xs:sequence>\r\n      <xs:element name="FetchResultDataType" type="tns:FetchResultDataType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfFetchResultDataType" type="tns:ListOfFetchResultDataType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="TransferResultErrorDataType">\r\n    <xs:complexContent mixed="false">\r\n      <xs:extension base="tns:FetchResultDataType">\r\n        <xs:sequence>\r\n          <xs:element name="Status" type="xs:int" minOccurs="0" />\r\n          <xs:element name="Diagnostics" type="ua:DiagnosticInfo" minOccurs="0" nillable="true" />\r\n        </xs:sequence>\r\n      </xs:extension>\r\n    </xs:complexContent>\r\n  </xs:complexType>\r\n  <xs:element name="TransferResultErrorDataType" type="tns:TransferResultErrorDataType" />\r\n\r\n  <xs:complexType name="ListOfTransferResultErrorDataType">\r\n    <xs:sequence>\r\n      <xs:element name="TransferResultErrorDataType" type="tns:TransferResultErrorDataType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfTransferResultErrorDataType" type="tns:ListOfTransferResultErrorDataType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="TransferResultDataDataType">\r\n    <xs:complexContent mixed="false">\r\n      <xs:extension base="tns:FetchResultDataType">\r\n        <xs:sequence>\r\n          <xs:element name="SequenceNumber" type="xs:int" minOccurs="0" />\r\n          <xs:element name="EndOfResults" type="xs:boolean" minOccurs="0" />\r\n          <xs:element name="ParameterDefs" type="tns:ListOfParameterResultDataType" minOccurs="0" nillable="true" />\r\n        </xs:sequence>\r\n      </xs:extension>\r\n    </xs:complexContent>\r\n  </xs:complexType>\r\n  <xs:element name="TransferResultDataDataType" type="tns:TransferResultDataDataType" />\r\n\r\n  <xs:complexType name="ListOfTransferResultDataDataType">\r\n    <xs:sequence>\r\n      <xs:element name="TransferResultDataDataType" type="tns:TransferResultDataDataType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfTransferResultDataDataType" type="tns:ListOfTransferResultDataDataType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="ParameterResultDataType">\r\n    <xs:sequence>\r\n      <xs:element name="NodePath" type="ua:ListOfQualifiedName" minOccurs="0" nillable="true" />\r\n      <xs:element name="StatusCode" type="ua:StatusCode" minOccurs="0" />\r\n      <xs:element name="Diagnostics" type="ua:DiagnosticInfo" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ParameterResultDataType" type="tns:ParameterResultDataType" />\r\n\r\n  <xs:complexType name="ListOfParameterResultDataType">\r\n    <xs:sequence>\r\n      <xs:element name="ParameterResultDataType" type="tns:ParameterResultDataType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfParameterResultDataType" type="tns:ListOfParameterResultDataType" nillable="true"></xs:element>\r\n\r\n  <xs:simpleType  name="SoftwareClass">\r\n    <xs:restriction base="xs:string">\r\n      <xs:enumeration value="Firmware_0" />\r\n      <xs:enumeration value="Application_1" />\r\n      <xs:enumeration value="Configuration_2" />\r\n      <xs:enumeration value="Solution_3" />\r\n    </xs:restriction>\r\n  </xs:simpleType>\r\n  <xs:element name="SoftwareClass" type="tns:SoftwareClass" />\r\n\r\n  <xs:complexType name="ListOfSoftwareClass">\r\n    <xs:sequence>\r\n      <xs:element name="SoftwareClass" type="tns:SoftwareClass" minOccurs="0" maxOccurs="unbounded" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfSoftwareClass" type="tns:ListOfSoftwareClass" nillable="true"></xs:element>\r\n\r\n  <xs:simpleType  name="LocationIndicationType">\r\n    <xs:restriction base="xs:unsignedShort">\r\n    </xs:restriction>\r\n  </xs:simpleType>\r\n  <xs:element name="LocationIndicationType" type="tns:LocationIndicationType" />\r\n\r\n  <xs:complexType name="ListOfLocationIndicationType">\r\n    <xs:sequence>\r\n      <xs:element name="LocationIndicationType" type="tns:LocationIndicationType" minOccurs="0" maxOccurs="unbounded" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfLocationIndicationType" type="tns:ListOfLocationIndicationType" nillable="true"></xs:element>\r\n\r\n  <xs:simpleType  name="SoftwareVersionFileType">\r\n    <xs:restriction base="xs:string">\r\n      <xs:enumeration value="Current_0" />\r\n      <xs:enumeration value="Pending_1" />\r\n      <xs:enumeration value="Fallback_2" />\r\n    </xs:restriction>\r\n  </xs:simpleType>\r\n  <xs:element name="SoftwareVersionFileType" type="tns:SoftwareVersionFileType" />\r\n\r\n  <xs:complexType name="ListOfSoftwareVersionFileType">\r\n    <xs:sequence>\r\n      <xs:element name="SoftwareVersionFileType" type="tns:SoftwareVersionFileType" minOccurs="0" maxOccurs="unbounded" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfSoftwareVersionFileType" type="tns:ListOfSoftwareVersionFileType" nillable="true"></xs:element>\r\n\r\n  <xs:simpleType  name="UpdateBehavior">\r\n    <xs:restriction base="xs:unsignedInt">\r\n    </xs:restriction>\r\n  </xs:simpleType>\r\n  <xs:element name="UpdateBehavior" type="tns:UpdateBehavior" />\r\n\r\n  <xs:complexType name="ListOfUpdateBehavior">\r\n    <xs:sequence>\r\n      <xs:element name="UpdateBehavior" type="tns:UpdateBehavior" minOccurs="0" maxOccurs="unbounded" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfUpdateBehavior" type="tns:ListOfUpdateBehavior" nillable="true"></xs:element>\r\n\r\n</xs:schema>',
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di;i=15909", browseName="Default JSON")
o6.hasEncoding(di_datypes.FetchResultDataType, o6.ns["ns=di;i=15909"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di;i=15910", browseName="Default JSON")
o6.hasEncoding(di_datypes.TransferResultErrorDataType, o6.ns["ns=di;i=15910"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di;i=15911", browseName="Default JSON")
o6.hasEncoding(di_datypes.TransferResultDataDataType, o6.ns["ns=di;i=15911"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=di;i=15912", browseName="Default JSON")
o6.hasEncoding(di_datypes.ParameterResultDataType, o6.ns["ns=di;i=15912"])


del Any, TYPE_CHECKING, uuid, o6, ns0, di_reftypes, di_datypes, di_vartypes, di_objtypes
