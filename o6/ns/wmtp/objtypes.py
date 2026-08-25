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

"""Generated OPC UA wmtp namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.irdi as irdi
import o6.ns.machinery as machinery
import o6.ns.machinery_processvalues as machinery_processvalues
import o6.ns.ns0 as ns0
import o6.ns.padim as padim
from . import datatypes as wmtp_datypes
from . import vartypes as wmtp_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.FolderType(nodeId="ns=wmtp;i=5008", browseName="ns=machinery;MachineryBuildingBlocks")


@o6.objecttype(nodeId="ns=wmtp;i=1003", browseName="ns=wmtp;WirelessMachineToolPeripheralType", displayName="WirelessMachineToolPeripheralType")
class WirelessMachineToolPeripheralType(ns0.objtypes.BaseObjectType):
    deviceConfiguration: ns0.objtypes.FolderType | None
    deviceInformation: ns0.objtypes.FolderType
    lifetimeCounters: machinery.objtypes.MachineryLifetimeCounterType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType = o6.hasComponent(o6.ns["ns=wmtp;i=5008"])
    measurements: ns0.objtypes.FolderType
    operationCounters: machinery.objtypes.MachineryOperationCounterType | None
    wMTPServiceCycleData: WMTPServiceCycleDataType | None
    wMTPWorkCycleData: WMTPWorkCycleDataType | None


ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6165",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DeleteAllStoredRecordsSuccessfull", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7005", browseName="ns=wmtp;DeleteAllStoredRecords", outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6165"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6168",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FromTimestamp", dataType=o6.DateTime, valueRank=-1), ns0.datatypes.Argument(name="ToTimestamp", dataType=o6.DateTime, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7006", browseName="ns=wmtp;DeleteStoredRecordsTime", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6168"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6172",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FromIndex", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="ToIndex", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7007", browseName="ns=wmtp;DeleteStoredRecordsIndex", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6172"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6176",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NumberOfStoredRecords", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7009", browseName="ns=wmtp;ReportNumberOfStoredRecords", outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6176"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6180",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FromTimestamp", dataType=o6.DateTime, valueRank=-1), ns0.datatypes.Argument(name="ToTimestamp", dataType=o6.DateTime, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6181",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NumberOfStoredRecords", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=wmtp;i=7010",
    browseName="ns=wmtp;ReportNumberOfStoredRecordsTime",
    inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6180"]),
    outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6181"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6233",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CombinedReport", dataType=o6.NodeId("ns=wmtp;i=3003"), valueRank=-2)],
)
o6.call(nodeId="ns=wmtp;i=7011", browseName="ns=wmtp;CombinedReportAll", outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6233"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6235",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FromIndex", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="ToIndex", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6236",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CombinedReport", dataType=o6.NodeId("ns=wmtp;i=3003"), valueRank=-2)],
)
o6.call(nodeId="ns=wmtp;i=7012", browseName="ns=wmtp;CombinedReportIndex", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6235"]), outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6236"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6237",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FromTimestamp", dataType=o6.DateTime, valueRank=-1), ns0.datatypes.Argument(name="ToTimestamp", dataType=o6.DateTime, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6238",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CombinedReport", dataType=o6.NodeId("ns=wmtp;i=3003"), valueRank=-2)],
)
o6.call(nodeId="ns=wmtp;i=7013", browseName="ns=wmtp;CombinedReportTime", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6237"]), outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6238"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6241",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CombinedReport", dataType=o6.NodeId("ns=wmtp;i=3003"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=wmtp;i=7015", browseName="ns=wmtp;CombinedReportAll", outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6241"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6243",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FromIndex", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="ToIndex", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6244",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CombinedReport", dataType=o6.NodeId("ns=wmtp;i=3003"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=wmtp;i=7016", browseName="ns=wmtp;CombinedReportIndex", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6243"]), outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6244"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6247",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FromTimestamp", dataType=o6.DateTime, valueRank=-1), ns0.datatypes.Argument(name="ToTimestamp", dataType=o6.DateTime, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6248",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CombinedReport", dataType=o6.NodeId("ns=wmtp;i=3003"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=wmtp;i=7017", browseName="ns=wmtp;CombinedReportTime", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6247"]), outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6248"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6164",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DeleteAllStoredRecordsSuccessfull", dataType=o6.Boolean, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7018", browseName="ns=wmtp;DeleteAllStoredRecords", outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6164"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6170",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FromIndex", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="ToIndex", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7019", browseName="ns=wmtp;DeleteStoredRecordsIndex", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6170"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6166",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7020",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FromTimestamp", dataType=o6.DateTime, valueRank=-1), ns0.datatypes.Argument(name="ToTimestamp", dataType=o6.DateTime, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7020", browseName="ns=wmtp;DeleteStoredRecordsTime", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6166"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6174",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NumberOfStoredRecords", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7021", browseName="ns=wmtp;ReportNumberOfStoredRecords", outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6174"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6178",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FromTimestamp", dataType=o6.DateTime, valueRank=-1), ns0.datatypes.Argument(name="ToTimestamp", dataType=o6.DateTime, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6179",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NumberOfStoredRecords", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=wmtp;i=7022",
    browseName="ns=wmtp;ReportNumberOfStoredRecordsTime",
    inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6178"]),
    outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6179"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6182",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TriggerDuration", dataType=ns0.datatypes.Duration, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7029", browseName="ns=wmtp;SetTriggerSettings", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6182"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6200",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DeltaValue", dataType=ns0.datatypes.Number, valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7030", browseName="ns=wmtp;SetDeltaCondition", inputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6200"]))


@o6.objecttype(nodeId="ns=wmtp;i=1005", browseName="ns=wmtp;WMTPMeasurementType", displayName="WMTPMeasurementType")
class WMTPMeasurementType(machinery_processvalues.objtypes.ProcessValueType):
    absoluteUncertainty: ns0.vartypes.AnalogUnitType | None
    deltaCondition: ns0.vartypes.AnalogUnitType
    index: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6048", browseName="ns=wmtp;Index", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )
    internalUpdateInterval: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6050", browseName="ns=wmtp;InternalUpdateInterval", dataType=ns0.datatypes.Duration, accessLevel=3, userAccessLevel=1)
    )
    limitCounters: machinery.objtypes.MachineryOperationCounterType | None
    measurementPeriod: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6049", browseName="ns=wmtp;MeasurementPeriod", dataType=ns0.datatypes.Duration, accessLevel=3, userAccessLevel=1)
    )
    relativeUncertainty: ns0.vartypes.AnalogUnitType | None
    setDeltaCondition: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wmtp;i=7030"])
    setTriggerSettings: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wmtp;i=7029"])
    status: ns0.vartypes.MultiStateValueDiscreteType | None
    timestamp: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=wmtp;i=6047", browseName="ns=wmtp;Timestamp", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)
    )
    triggerSettings: ns0.vartypes.AnalogUnitType
    typeOfMeasurement: ns0.vartypes.MultiStateValueDiscreteType
    typeOfSample: ns0.vartypes.MultiStateValueDiscreteType


ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6245",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7047",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CombinedReport", dataType=o6.NodeId("ns=wmtp;i=3003"), valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7047", browseName="ns=wmtp;CombinedReportLastValue", outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6245"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6239",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7048",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CombinedReport", dataType=o6.NodeId("ns=wmtp;i=3003"), valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7048", browseName="ns=wmtp;CombinedReportLastValue", outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6239"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6240",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7049",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CombinedReport", dataType=o6.NodeId("ns=wmtp;i=3003"), valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7049", browseName="ns=wmtp;CombinedReportFirstValue", outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6240"]))


@o6.objecttype(nodeId="ns=wmtp;i=1004", browseName="ns=wmtp;WMTPWorkCycleDataType", displayName="WMTPWorkCycleDataType")
class WMTPWorkCycleDataType(ns0.objtypes.BaseObjectType):
    abortOperation: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="ns=wmtp;i=7008", browseName="ns=wmtp;AbortOperation"))
    combinedReportAll: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wmtp;i=7011"])
    combinedReportFirstValue: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wmtp;i=7049"])
    combinedReportIndex: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wmtp;i=7012"])
    combinedReportLastValue: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wmtp;i=7048"])
    combinedReportTime: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wmtp;i=7013"])
    deleteAllStoredRecords: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wmtp;i=7005"])
    deleteStoredRecordsIndex: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wmtp;i=7007"])
    deleteStoredRecordsTime: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wmtp;i=7006"])
    reportNumberOfStoredRecords: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wmtp;i=7009"])
    reportNumberOfStoredRecordsTime: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wmtp;i=7010"])


ns0.vartypes.PropertyType(
    nodeId="ns=wmtp;i=6246",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wmtp;i=7050",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CombinedReport", dataType=o6.NodeId("ns=wmtp;i=3003"), valueRank=-1)],
)
o6.call(nodeId="ns=wmtp;i=7050", browseName="ns=wmtp;CombinedReportFirstValue", outputArgs=o6.hasProperty(o6.ns["ns=wmtp;i=6246"]))


@o6.objecttype(nodeId="ns=wmtp;i=1007", browseName="ns=wmtp;WMTPServiceCycleDataType", displayName="WMTPServiceCycleDataType")
class WMTPServiceCycleDataType(ns0.objtypes.BaseObjectType):
    abortOperation: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="ns=wmtp;i=7014", browseName="ns=wmtp;AbortOperation"))
    combinedReportAll: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wmtp;i=7015"])
    combinedReportFirstValue: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wmtp;i=7050"])
    combinedReportIndex: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wmtp;i=7016"])
    combinedReportLastValue: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wmtp;i=7047"])
    combinedReportTime: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wmtp;i=7017"])
    deleteAllStoredRecords: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wmtp;i=7018"])
    deleteStoredRecordsIndex: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wmtp;i=7019"])
    deleteStoredRecordsTime: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wmtp;i=7020"])
    reportNumberOfStoredRecords: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wmtp;i=7021"])
    reportNumberOfStoredRecordsTime: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wmtp;i=7022"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, irdi, machinery, machinery_processvalues, ns0, padim, wmtp_datypes, wmtp_vartypes
