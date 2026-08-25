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

"""Generated OPC UA pnenc namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import datatypes as pnenc_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=pnenc;i=1012", browseName="ns=pnenc;EncoderProbesType", displayName="EncoderProbesType")
class EncoderProbesType(ns0.objtypes.BaseObjectType):
    langleProbexRangle: EncoderProbeType | None


@o6.objecttype(nodeId="ns=pnenc;i=1003", browseName="ns=pnenc;LogbookEventType", displayName="LogbookEventType")
class LogbookEventType(ns0.objtypes.BaseEventType):
    logEntry: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=pnenc;i=6034",
            browseName="ns=pnenc;LogEntry",
            dataType=pnenc_datypes.LogEntryDataType,
            value=pnenc_datypes.LogEntryDataType(
                faultSituationNumber=0,
                eventNumber=0,
                eventType=pnenc_datypes.EventTypeEnumeration.FAULT,
                eventCode=0,
                eventText=o6.LocalizedText(),
                eventComing=o6.DateTime("1900-01-01T00:00:00Z"),
                eventGoing=o6.DateTime("1900-01-01T00:00:00Z"),
                eventAcknowledged=o6.DateTime("1900-01-01T00:00:00Z"),
            ),
        )
    )


@o6.objecttype(nodeId="ns=pnenc;i=1004", browseName="ns=pnenc;EncoderRefLatchEventType", displayName="EncoderRefLatchEventType")
class EncoderRefLatchEventType(ns0.objtypes.BaseEventType):
    lastLatchedPos: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6036", browseName="ns=pnenc;LastLatchedPos", dataType=ns0.datatypes.Number)
    )
    latchActive: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6035", browseName="ns=pnenc;LatchActive", dataType=o6.Boolean))


@o6.objecttype(nodeId="ns=pnenc;i=1005", browseName="ns=pnenc;EncoderProbeLatchEventType", displayName="EncoderProbeLatchEventType")
class EncoderProbeLatchEventType(ns0.objtypes.BaseEventType):
    lastLatchedPos: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6039", browseName="ns=pnenc;LastLatchedPos", dataType=ns0.datatypes.Number)
    )
    latchActive: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6038", browseName="ns=pnenc;LatchActive", dataType=o6.Boolean))
    probeName: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6037", browseName="ns=pnenc;ProbeName", dataType=o6.String))


@o6.objecttype(nodeId="ns=pnenc;i=1006", browseName="ns=pnenc;EncoderDiagnosisEventType", displayName="EncoderDiagnosisEventType")
class EncoderDiagnosisEventType(ns0.objtypes.BaseEventType):
    diagnosisType: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6041", browseName="ns=pnenc;DiagnosisType", dataType=pnenc_datypes.EventTypeEnumeration)
    )
    eventCode: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6040", browseName="ns=pnenc;EventCode", dataType=ns0.datatypes.Integer))
    eventText: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6042", browseName="ns=pnenc;EventText", dataType=o6.String))
    reason: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6043", browseName="ns=pnenc;Reason", dataType=pnenc_datypes.EncoderDiagnosisReasonEnumeration)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6002",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationTag", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=pnenc;i=7001", browseName="ns=pnenc;SetApplicationTag", inputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6002"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6052",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="SensorConfigParameters", dataType=ns0.datatypes.KeyValuePair, valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6053",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="SensorConfigParametersResult", dataType=ns0.datatypes.KeyValuePair, valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=pnenc;i=7006", browseName="ns=pnenc;SetSensorConfig", inputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6052"]), outputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6053"]))


@o6.objecttype(nodeId="ns=pnenc;i=1007", browseName="ns=pnenc;EncoderSensorConfigType", displayName="EncoderSensorConfigType")
class EncoderSensorConfigType(ns0.objtypes.BaseObjectType):
    absolutePosDeterminableRevolutions: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6051", browseName="ns=pnenc;AbsolutePosDeterminableRevolutions", dataType=ns0.datatypes.Integer)
    )
    absolutePosLinSupported: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6050", browseName="ns=pnenc;AbsolutePosLinSupported", dataType=o6.Boolean)
    )
    configType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6045", browseName="ns=pnenc;ConfigType", dataType=pnenc_datypes.EncoderConfigTypeEnumeration)
    )
    sensorAbsoluteType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6044", browseName="ns=pnenc;SensorAbsoluteType", dataType=pnenc_datypes.EncoderSensorAbsoluteTypeEnumeration)
    )
    sensorResolutionIncPerRotation: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6046", browseName="ns=pnenc;SensorResolutionIncPerRotation", dataType=ns0.datatypes.Integer)
    )
    sensorResolutionNanometerPerIncrement: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6047", browseName="ns=pnenc;SensorResolutionNanometerPerIncrement", dataType=ns0.datatypes.Integer)
    )
    setSensorConfig: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnenc;i=7006"])
    shiftFactorXIST1: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6048", browseName="ns=pnenc;ShiftFactorXIST1", dataType=ns0.datatypes.Integer)
    )
    shiftFactorXIST2: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6049", browseName="ns=pnenc;ShiftFactorXIST2", dataType=ns0.datatypes.Integer)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6057",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ControlConfigParameters", dataType=ns0.datatypes.KeyValuePair, valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6058",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ControlConfigParametersResult", dataType=ns0.datatypes.KeyValuePair, valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=pnenc;i=7007", browseName="ns=pnenc;SetControlConfig", inputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6057"]), outputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6058"]))


@o6.objecttype(nodeId="ns=pnenc;i=1008", browseName="ns=pnenc;EncoderControlConfigType", displayName="EncoderControlConfigType")
class EncoderControlConfigType(ns0.objtypes.BaseObjectType):
    alarmChannelControl: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6054", browseName="ns=pnenc;AlarmChannelControl", dataType=pnenc_datypes.EncoderAlarmChannelControlEnumeration)
    )
    setControlConfig: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnenc;i=7007"])
    signOfLifeFailuresTolerated: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6056", browseName="ns=pnenc;SignOfLifeFailuresTolerated", dataType=o6.UInt16)
    )
    xIST1PresetControl: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6055", browseName="ns=pnenc;XIST1PresetControl", dataType=pnenc_datypes.EncoderPresetControlEnumeration)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6066",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AxisConfigParameters", dataType=ns0.datatypes.KeyValuePair, valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6067",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AxisConfigParametersResult", dataType=ns0.datatypes.KeyValuePair, valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=pnenc;i=7008", browseName="ns=pnenc;SetAxisConfig", inputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6066"]), outputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6067"]))


@o6.objecttype(nodeId="ns=pnenc;i=1009", browseName="ns=pnenc;EncoderAxisConfigType", displayName="EncoderAxisConfigType")
class EncoderAxisConfigType(ns0.objtypes.BaseObjectType):
    accelerationDampingTimeConstant: ns0.vartypes.BaseAnalogType | None = o6.hasComponent(
        ns0.vartypes.BaseAnalogType(nodeId="ns=pnenc;i=6065", browseName="ns=pnenc;AccelerationDampingTimeConstant", dataType=o6.Float)
    )
    axisType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6060", browseName="ns=pnenc;AxisType", dataType=pnenc_datypes.EncoderAxisTypeEnumeration)
    )
    codeSequence: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6061", browseName="ns=pnenc;CodeSequence", dataType=pnenc_datypes.EncoderCodeSequenceEnumeration)
    )
    positionScalingFactor: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6059", browseName="ns=pnenc;PositionScalingFactor", dataType=o6.Float)
    )
    presetOrShiftValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6062", browseName="ns=pnenc;PresetOrShiftValue", dataType=o6.Float)
    )
    setAxisConfig: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnenc;i=7008"])
    velocityDampingTimeConstant: ns0.vartypes.BaseAnalogType | None = o6.hasComponent(
        ns0.vartypes.BaseAnalogType(nodeId="ns=pnenc;i=6064", browseName="ns=pnenc;VelocityDampingTimeConstant", dataType=o6.Float)
    )
    velocityReference: ns0.vartypes.BaseAnalogType | None = o6.hasComponent(
        ns0.vartypes.BaseAnalogType(nodeId="ns=pnenc;i=6063", browseName="ns=pnenc;VelocityReference", dataType=o6.Float)
    )


@o6.objecttype(nodeId="ns=pnenc;i=1002", browseName="ns=pnenc;EncoderChannelType", displayName="EncoderChannelType")
class EncoderChannelType(ns0.objtypes.BaseObjectType):
    acceleration: ns0.vartypes.AnalogUnitRangeType | None
    applicationTag: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6001", browseName="ns=pnenc;ApplicationTag", dataType=o6.String))
    axisConfig: EncoderAxisConfigType | None = o6.hasComponent(EncoderAxisConfigType(nodeId="ns=pnenc;i=5008", browseName="ns=pnenc;AxisConfig"))
    controlConfig: EncoderControlConfigType | None = o6.hasComponent(EncoderControlConfigType(nodeId="ns=pnenc;i=5009", browseName="ns=pnenc;ControlConfig"))
    encoderChannelState: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnenc;i=6009", browseName="ns=pnenc;EncoderChannelState", dataType=pnenc_datypes.EncoderChannelStateEnumeration)
    )
    encoderProfileVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6003", browseName="ns=pnenc;EncoderProfileVersion", dataType=o6.String)
    )
    g1_STW: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnenc;i=6090", browseName="ns=pnenc;G1_STW", dataType=o6.UInt16)
    )
    g1_XIST1: ns0.vartypes.BaseDataVariableType | None
    g1_XIST2: ns0.vartypes.BaseDataVariableType | None
    g1_XIST3: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnenc;i=6094", browseName="ns=pnenc;G1_XIST3", dataType=o6.UInt64)
    )
    g1_XIST_PRESET_B: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnenc;i=6097", browseName="ns=pnenc;G1_XIST_PRESET_B", dataType=o6.UInt32)
    )
    g1_XIST_PRESET_B1: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnenc;i=6099", browseName="ns=pnenc;G1_XIST_PRESET_B1", dataType=o6.UInt32)
    )
    g1_XIST_PRESET_C: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnenc;i=6098", browseName="ns=pnenc;G1_XIST_PRESET_C", dataType=o6.UInt64)
    )
    g1_ZSW: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnenc;i=6091", browseName="ns=pnenc;G1_ZSW", dataType=o6.UInt16)
    )
    lock: di.objtypes.LockingServicesType | None
    logbook: LogbookType | None
    nIST_A: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pnenc;i=6019", browseName="ns=pnenc;NIST_A", dataType=o6.Int16))
    nIST_B: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=pnenc;i=6020", browseName="ns=pnenc;NIST_B", dataType=o6.Int32))
    position: ns0.vartypes.AnalogUnitRangeType | None
    positionSensorSignalValue: ns0.vartypes.BaseDataVariableType | None
    probes: EncoderProbesType | None = o6.hasComponent(EncoderProbesType(nodeId="ns=pnenc;i=5012", browseName="ns=pnenc;Probes"))
    sTW2_ENC: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnenc;i=6095", browseName="ns=pnenc;STW2_ENC", dataType=o6.UInt16)
    )
    sensor: EncoderSensorType
    sensorConfig: EncoderSensorConfigType | None = o6.hasComponent(EncoderSensorConfigType(nodeId="ns=pnenc;i=5007", browseName="ns=pnenc;SensorConfig"))
    setApplicationTag: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnenc;i=7001"])
    temperature: ns0.vartypes.AnalogUnitRangeType | None
    velocity: ns0.vartypes.AnalogUnitRangeType | None
    zSW2_ENC: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnenc;i=6096", browseName="ns=pnenc;ZSW2_ENC", dataType=o6.UInt16)
    )


o6.reference(EncoderChannelType, "i=41", EncoderDiagnosisEventType)


ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6033",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FilteredLogEntries", dataType=o6.NodeId("ns=pnenc;i=3013"), valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6070",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="LogbookFilterOptions", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="FaultSituationNumber", dataType=o6.Byte, valueRank=-1),
        ns0.datatypes.Argument(name="EventType", dataType=o6.NodeId("ns=pnenc;i=3003"), valueRank=-1),
        ns0.datatypes.Argument(name="EventCode", dataType=o6.Int32, valueRank=-1),
        ns0.datatypes.Argument(name="EventAppearanceInterval", dataType=ns0.datatypes.Duration, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=pnenc;i=7010",
    browseName="ns=pnenc;GetFilteredLogbookEntries",
    inputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6070"]),
    outputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6033"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6071",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CurrentLogEntries", dataType=o6.NodeId("ns=pnenc;i=3013"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=pnenc;i=7011", browseName="ns=pnenc;GetCurrentFaultSituation", outputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6071"]))

ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6072",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FaultSituationNumber", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6073",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="HistoricLogEntries", dataType=o6.NodeId("ns=pnenc;i=3013"), valueRank=1, arrayDimensions=[0])],
)
o6.call(
    nodeId="ns=pnenc;i=7012",
    browseName="ns=pnenc;GetHistoricFaultSituation",
    inputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6072"]),
    outputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6073"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6074",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ActiveDiagnosis", dataType=o6.NodeId("ns=pnenc;i=3013"), valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=pnenc;i=7013", browseName="ns=pnenc;GetActiveDiagnosis", outputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6074"]))


@o6.objecttype(nodeId="ns=pnenc;i=1010", browseName="ns=pnenc;LogbookType", displayName="LogbookType")
class LogbookType(ns0.objtypes.BaseObjectType):
    deleteLogbook: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=pnenc;i=7009", browseName="ns=pnenc;DeleteLogbook"))
    getActiveDiagnosis: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnenc;i=7013"])
    getCurrentFaultSituation: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnenc;i=7011"])
    getFilteredLogbookEntries: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnenc;i=7010"])
    getHistoricFaultSituation: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnenc;i=7012"])
    logEntries: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=pnenc;i=6068",
            browseName="ns=pnenc;LogEntries",
            dataType=pnenc_datypes.LogEntryDataType,
            valueRank=1,
            arrayDimensions=[1],
            value=[
                pnenc_datypes.LogEntryDataType(
                    faultSituationNumber=0,
                    eventNumber=0,
                    eventType=pnenc_datypes.EventTypeEnumeration.FAULT,
                    eventCode=0,
                    eventText=o6.LocalizedText(),
                    eventComing=o6.DateTime("1900-01-01T00:00:00Z"),
                    eventGoing=o6.DateTime("1900-01-01T00:00:00Z"),
                    eventAcknowledged=o6.DateTime("1900-01-01T00:00:00Z"),
                )
            ],
        )
    )
    logbookSize: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pnenc;i=6069", browseName="ns=pnenc;LogbookSize", dataType=o6.UInt16))


o6.reference(LogbookType, "i=41", LogbookEventType)


@o6.objecttype(nodeId="ns=pnenc;i=1011", browseName="ns=pnenc;EncoderProbeType", displayName="EncoderProbeType")
class EncoderProbeType(ns0.objtypes.BaseObjectType):
    lastLatchedPos: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnenc;i=6085", browseName="ns=pnenc;LastLatchedPos", dataType=ns0.datatypes.Number)
    )
    latchActive: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnenc;i=6084", browseName="ns=pnenc;LatchActive", dataType=o6.Boolean)
    )
    latchStart: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=pnenc;i=7018", browseName="ns=pnenc;LatchStart"))
    lock: di.objtypes.LockingServicesType | None


o6.reference(EncoderProbeType, "i=41", EncoderProbeLatchEventType)


ns0.vartypes.PropertyType(
    nodeId="ns=pnenc;i=6086",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=pnenc;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="PresetValue", dataType=ns0.datatypes.Number, valueRank=-1)],
)
o6.call(nodeId="ns=pnenc;i=7019", browseName="ns=pnenc;PresetControl", inputArgs=o6.hasProperty(o6.ns["ns=pnenc;i=6086"]))


@o6.objecttype(nodeId="ns=pnenc;i=1013", browseName="ns=pnenc;EncoderSensorType", displayName="EncoderSensorType")
class EncoderSensorType(ns0.objtypes.BaseObjectType):
    positionOffset: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnenc;i=6087", browseName="ns=pnenc;PositionOffset", dataType=ns0.datatypes.Number)
    )
    presetControl: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pnenc;i=7019"])
    ref1LastLatchedPos: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnenc;i=6089", browseName="ns=pnenc;Ref1LastLatchedPos", dataType=ns0.datatypes.Number)
    )
    ref1LatchActive: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=pnenc;i=6088", browseName="ns=pnenc;Ref1LatchActive", dataType=o6.Boolean)
    )
    ref1LatchStart: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=pnenc;i=7020", browseName="ns=pnenc;Ref1LatchStart"))


o6.reference(EncoderSensorType, "i=41", EncoderRefLatchEventType)


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pnenc_datypes
