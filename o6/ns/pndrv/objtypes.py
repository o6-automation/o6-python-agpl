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

"""Generated OPC UA pndrv namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.pnenc as pnenc
from . import vartypes as pndrv_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

di.objtypes.LockingServicesType(nodeId="ns=pndrv;i=5002", browseName="ns=pndrv;Lock")
o6.reference(o6.ns["ns=pndrv;i=5002"], "i=46", "ns=di;i=6390")
o6.reference(o6.ns["ns=pndrv;i=5002"], "i=46", "ns=di;i=6391")
o6.reference(o6.ns["ns=pndrv;i=5002"], "i=46", "ns=di;i=6392")
o6.reference(o6.ns["ns=pndrv;i=5002"], "i=46", "ns=di;i=6534")
o6.reference(o6.ns["ns=pndrv;i=5002"], "i=47", "ns=di;i=6393")
o6.reference(o6.ns["ns=pndrv;i=5002"], "i=47", "ns=di;i=6396")
o6.reference(o6.ns["ns=pndrv;i=5002"], "i=47", "ns=di;i=6398")
o6.reference(o6.ns["ns=pndrv;i=5002"], "i=47", "ns=di;i=6400")
pnenc.objtypes.LogbookType(nodeId="ns=pndrv;i=5007", browseName="ns=pndrv;Logbook")
o6.reference(o6.ns["ns=pndrv;i=5007"], "i=41", "ns=pnenc;i=1003")
o6.reference(o6.ns["ns=pndrv;i=5007"], "i=46", "ns=pnenc;i=6069")
o6.reference(o6.ns["ns=pndrv;i=5007"], "i=47", "ns=pnenc;i=6068")
ns0.objtypes.FileType(nodeId="ns=pndrv;i=5027", browseName="ns=pndrv;MotionProgram")
o6.reference(o6.ns["ns=pndrv;i=5027"], "i=46", "i=11576")
o6.reference(o6.ns["ns=pndrv;i=5027"], "i=46", "i=11579")
o6.reference(o6.ns["ns=pndrv;i=5027"], "i=46", "i=12686")
o6.reference(o6.ns["ns=pndrv;i=5027"], "i=46", "i=12687")
o6.reference(o6.ns["ns=pndrv;i=5027"], "i=47", "i=11580")
o6.reference(o6.ns["ns=pndrv;i=5027"], "i=47", "i=11583")
o6.reference(o6.ns["ns=pndrv;i=5027"], "i=47", "i=11585")
o6.reference(o6.ns["ns=pndrv;i=5027"], "i=47", "i=11588")
o6.reference(o6.ns["ns=pndrv;i=5027"], "i=47", "i=11590")
o6.reference(o6.ns["ns=pndrv;i=5027"], "i=47", "i=11593")
pnenc.objtypes.EncoderChannelType(nodeId="ns=pndrv;i=5031", browseName="ns=pndrv;EncoderChannelMotor")
o6.reference(o6.ns["ns=pndrv;i=5031"], "i=41", "ns=pnenc;i=1006")
o6.reference(o6.ns["ns=pndrv;i=5031"], "i=47", "ns=pnenc;i=5011")
pnenc.objtypes.EncoderChannelType(nodeId="ns=pndrv;i=5033", browseName="ns=pndrv;<EncoderChannelAuxiliary>", modellingRule="OptionalPlaceholder")
o6.reference(o6.ns["ns=pndrv;i=5033"], "i=41", "ns=pnenc;i=1006")
o6.reference(o6.ns["ns=pndrv;i=5033"], "i=47", "ns=pnenc;i=5011")
ns0.objtypes.FolderType(nodeId="ns=pndrv;i=5035", browseName="ns=pndrv;CharacteristicsConverter")


@o6.objecttype(nodeId="ns=pndrv;i=1012", browseName="ns=pndrv;DiagnosisAlarmType", displayName="DiagnosisAlarmType")
class DiagnosisAlarmType(ns0.objtypes.AlarmConditionType):
    logEntry: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6026", browseName="ns=pndrv;LogEntry", dataType=pnenc.datatypes.LogEntryDataType)
    )


ns0.vartypes.BaseDataVariableType(nodeId="ns=pndrv;i=6092", browseName="ns=pndrv;TraversingTaskNumber", dataType=o6.Int32)
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6093", browseName="ns=pndrv;TargetPosition", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6093"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6094", browseName="ns=pndrv;Velocity", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6094"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6095", browseName="ns=pndrv;Acceleration", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6095"], "i=46", "i=17502")
ns0.vartypes.AnalogUnitType(nodeId="ns=pndrv;i=6096", browseName="ns=pndrv;Deceleration", dataType=o6.Float)
o6.reference(o6.ns["ns=pndrv;i=6096"], "i=46", "i=17502")


@o6.objecttype(nodeId="ns=pndrv;i=1007", browseName="ns=pndrv;TraversingTaskType", displayName="TraversingTaskType")
class TraversingTaskType(ns0.objtypes.BaseObjectType):
    acceleration: ns0.vartypes.AnalogUnitType | None = o6.hasComponent(o6.ns["ns=pndrv;i=6095"])
    deceleration: ns0.vartypes.AnalogUnitType | None = o6.hasComponent(o6.ns["ns=pndrv;i=6096"])
    positioningMode: ns0.vartypes.MultiStateDiscreteType
    targetPosition: ns0.vartypes.AnalogUnitType | None = o6.hasComponent(o6.ns["ns=pndrv;i=6093"])
    traversingTaskNumber: ns0.vartypes.BaseDataVariableType = o6.hasComponent(o6.ns["ns=pndrv;i=6092"])
    velocity: ns0.vartypes.AnalogUnitType | None = o6.hasComponent(o6.ns["ns=pndrv;i=6094"])


pndrv_vartypes.AxisTypeVariableType(nodeId="ns=pndrv;i=6153", browseName="ns=pndrv;AxisType", dataType=o6.Byte)
o6.reference(o6.ns["ns=pndrv;i=6153"], "i=46", o6.ns["ns=pndrv;i=6152"])


@o6.objecttype(nodeId="ns=pndrv;i=1018", browseName="ns=pndrv;SafetyFunctionType", displayName="SafetyFunctionType")
class SafetyFunctionType(ns0.objtypes.BaseObjectType):
    activationState: ns0.vartypes.MultiStateDiscreteType
    limit: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6155", browseName="ns=pndrv;Limit", dataType=o6.Float))
    selectionState: ns0.vartypes.MultiStateDiscreteType


SafetyFunctionType(nodeId="ns=pndrv;i=5046", browseName="ns=pndrv;STO")
SafetyFunctionType(nodeId="ns=pndrv;i=5047", browseName="ns=pndrv;SS1")
SafetyFunctionType(nodeId="ns=pndrv;i=5048", browseName="ns=pndrv;SS2")
SafetyFunctionType(nodeId="ns=pndrv;i=5049", browseName="ns=pndrv;SOS")
SafetyFunctionType(nodeId="ns=pndrv;i=5050", browseName="ns=pndrv;SLS")
SafetyFunctionType(nodeId="ns=pndrv;i=5051", browseName="ns=pndrv;SDI")
SafetyFunctionType(nodeId="ns=pndrv;i=5052", browseName="ns=pndrv;SLA")
SafetyFunctionType(nodeId="ns=pndrv;i=5053", browseName="ns=pndrv;SLP")


@o6.objecttype(nodeId="ns=pndrv;i=1015", browseName="ns=pndrv;SafetyType", displayName="SafetyType")
class SafetyType(ns0.objtypes.BaseObjectType):
    sDI: SafetyFunctionType | None = o6.hasComponent(o6.ns["ns=pndrv;i=5051"])
    sLA: SafetyFunctionType | None = o6.hasComponent(o6.ns["ns=pndrv;i=5052"])
    sLP: SafetyFunctionType | None = o6.hasComponent(o6.ns["ns=pndrv;i=5053"])
    sLS: SafetyFunctionType | None = o6.hasComponent(o6.ns["ns=pndrv;i=5050"])
    sOS: SafetyFunctionType | None = o6.hasComponent(o6.ns["ns=pndrv;i=5049"])
    sS1: SafetyFunctionType | None = o6.hasComponent(o6.ns["ns=pndrv;i=5047"])
    sS2: SafetyFunctionType | None = o6.hasComponent(o6.ns["ns=pndrv;i=5048"])
    sTO: SafetyFunctionType = o6.hasComponent(o6.ns["ns=pndrv;i=5046"])


SafetyType(nodeId="ns=pndrv;i=5045", browseName="ns=pndrv;Safety")
o6.reference(o6.ns["ns=pndrv;i=5045"], "i=47", o6.ns["ns=pndrv;i=5046"])


@o6.objecttype(nodeId="ns=pndrv;i=1001", browseName="ns=pndrv;AxisEventType", displayName="AxisEventType", isAbstract=True)
class AxisEventType(ns0.objtypes.BaseEventType):
    axisState: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6136", browseName="ns=pndrv;AxisState", dataType=o6.UInt16))
    brakeResistorTemperature: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6269", browseName="ns=pndrv;BrakeResistorTemperature", dataType=o6.Float)
    )
    controlMode: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6263", browseName="ns=pndrv;ControlMode", dataType=o6.UInt16))
    controlPriority: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6150", browseName="ns=pndrv;ControlPriority", dataType=o6.UInt16))
    converterTemperature: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6190", browseName="ns=pndrv;ConverterTemperature", dataType=o6.Float)
    )
    dcBusVoltage: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6214", browseName="ns=pndrv;DcBusVoltage", dataType=o6.Float))
    deviceTemperature: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6191", browseName="ns=pndrv;DeviceTemperature", dataType=o6.Float)
    )
    force: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6172", browseName="ns=pndrv;Force", dataType=o6.Float))
    langleFeedbackSensor1DotDot3TemperatureRangle: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6268", browseName="ns=pndrv;<FeedbackSensor1..3Temperature>", modellingRule="OptionalPlaceholder", dataType=o6.Float)
    )
    motorTemperature: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6179", browseName="ns=pndrv;MotorTemperature", dataType=o6.Float)
    )
    outputCurrent: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6167", browseName="ns=pndrv;OutputCurrent", dataType=o6.Float))
    positionFollowingError: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6227", browseName="ns=pndrv;PositionFollowingError", dataType=o6.Float)
    )
    power: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6178", browseName="ns=pndrv;Power", dataType=o6.Float))
    torque: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6171", browseName="ns=pndrv;Torque", dataType=o6.Float))
    velocityFollowingError: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6261", browseName="ns=pndrv;VelocityFollowingError", dataType=o6.Float)
    )


@o6.objecttype(nodeId="ns=pndrv;i=1013", browseName="ns=pndrv;AxisSwOvertravelEventType", displayName="AxisSwOvertravelEventType")
class AxisSwOvertravelEventType(AxisEventType):
    isUpperSwLimit: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6147", browseName="ns=pndrv;IsUpperSwLimit", dataType=o6.Boolean))


@o6.objecttype(nodeId="ns=pndrv;i=1014", browseName="ns=pndrv;AxisHwOvertravelEventType", displayName="AxisHwOvertravelEventType")
class AxisHwOvertravelEventType(AxisEventType):
    isUpperHwLimit: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6148", browseName="ns=pndrv;IsUpperHwLimit", dataType=o6.Boolean))


@o6.objecttype(nodeId="ns=pndrv;i=1016", browseName="ns=pndrv;TorqueLimitEventType", displayName="TorqueLimitEventType")
class TorqueLimitEventType(AxisEventType):
    torque: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6271", browseName="ns=pndrv;Torque", dataType=o6.Float))
    torqueLimit: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6270", browseName="ns=pndrv;TorqueLimit", dataType=o6.Float))


@o6.objecttype(nodeId="ns=pndrv;i=1019", browseName="ns=pndrv;ForceLimitEventType", displayName="ForceLimitEventType")
class ForceLimitEventType(AxisEventType):
    force: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6272", browseName="ns=pndrv;Force", dataType=o6.Float))
    forceLimit: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6201", browseName="ns=pndrv;ForceLimit", dataType=o6.Float))


@o6.objecttype(nodeId="ns=pndrv;i=1017", browseName="ns=pndrv;MotorCurrentLimitEventType", displayName="MotorCurrentLimitEventType")
class MotorCurrentLimitEventType(AxisEventType):
    motorCurrentLimitHigh: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6164", browseName="ns=pndrv;MotorCurrentLimitHigh", dataType=o6.Float)
    )
    outputCurrent: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6273", browseName="ns=pndrv;OutputCurrent", dataType=o6.Float))


ns0.vartypes.PropertyType(
    nodeId="ns=pndrv;i=6038",
    browseName="InputArguments",
    description="the definition of the input argument of method 3:DriveAxisType.3:SetApplicationTag",
    modellingRule="Mandatory",
    parent="ns=pndrv;i=7000",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ApplicationTag", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=pndrv;i=7000", browseName="ns=pndrv;SetApplicationTag", inputArgs=o6.hasProperty(o6.ns["ns=pndrv;i=6038"]))


@o6.objecttype(nodeId="ns=pndrv;i=1000", browseName="ns=pndrv;DriveAxisType", displayName="DriveAxisType", isAbstract=True)
class DriveAxisType(ns0.objtypes.BaseObjectType):
    applicationTag: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=pndrv;i=6020", browseName="ns=pndrv;ApplicationTag", dataType=o6.String))
    axisType: pndrv_vartypes.AxisTypeVariableType = o6.hasProperty(o6.ns["ns=pndrv;i=6153"])
    characteristicsConverter: ns0.objtypes.FolderType
    characteristicsMotorAndControl: ns0.objtypes.FolderType | None
    limitSupervision: ns0.objtypes.FolderType | None = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=pndrv;i=5006", browseName="ns=pndrv;LimitSupervision"))
    lock: di.objtypes.LockingServicesType | None = o6.hasComponent(o6.ns["ns=pndrv;i=5002"])
    logbook: pnenc.objtypes.LogbookType | None = o6.hasComponent(o6.ns["ns=pndrv;i=5007"])
    maintenance: ns0.objtypes.FolderType
    monitoring: ns0.objtypes.FolderType
    pNSignals: ns0.objtypes.FolderType | None
    safety: SafetyType | None = o6.hasComponent(o6.ns["ns=pndrv;i=5045"])
    setApplicationTag: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=pndrv;i=7000"])
    velocityProfile: ns0.objtypes.FolderType


o6.reference(DriveAxisType, "i=41", DiagnosisAlarmType)


@o6.objecttype(nodeId="ns=pndrv;i=1002", browseName="ns=pndrv;VelocityDriveAxisType", displayName="VelocityDriveAxisType")
class VelocityDriveAxisType(DriveAxisType):
    limitSupervision: ns0.objtypes.FolderType | None
    monitoring: ns0.objtypes.FolderType
    velocityProfile: ns0.objtypes.FolderType


o6.reference(VelocityDriveAxisType, "i=41", TorqueLimitEventType)
o6.reference(VelocityDriveAxisType, "i=41", MotorCurrentLimitEventType)


@o6.objecttype(nodeId="ns=pndrv;i=1005", browseName="ns=pndrv;FrequencyDriveAxisType", displayName="FrequencyDriveAxisType")
class FrequencyDriveAxisType(DriveAxisType):
    limitSupervision: ns0.objtypes.FolderType | None
    monitoring: ns0.objtypes.FolderType
    velocityProfile: ns0.objtypes.FolderType


o6.reference(FrequencyDriveAxisType, "i=41", MotorCurrentLimitEventType)


@o6.objecttype(nodeId="ns=pndrv;i=1006", browseName="ns=pndrv;PositioningDriveAxisType", displayName="PositioningDriveAxisType")
class PositioningDriveAxisType(DriveAxisType):
    characteristicsMechanics: ns0.objtypes.FolderType
    characteristicsMotorAndControl: ns0.objtypes.FolderType
    homing: ns0.objtypes.FolderType | None
    limitSupervision: ns0.objtypes.FolderType
    monitoring: ns0.objtypes.FolderType
    motionProgram: ns0.objtypes.FileType | None = o6.hasComponent(o6.ns["ns=pndrv;i=5027"])
    velocityProfile: ns0.objtypes.FolderType


o6.reference(PositioningDriveAxisType, "i=41", TorqueLimitEventType)
o6.reference(PositioningDriveAxisType, "i=41", MotorCurrentLimitEventType)


@o6.objecttype(nodeId="ns=pndrv;i=1008", browseName="ns=pndrv;VelocityServoDriveAxisType", displayName="VelocityServoDriveAxisType")
class VelocityServoDriveAxisType(DriveAxisType):
    encoderChannelMechanic: pnenc.objtypes.EncoderChannelType | None
    encoderChannelMotor: pnenc.objtypes.EncoderChannelType = o6.hasComponent(o6.ns["ns=pndrv;i=5031"])
    homing: ns0.objtypes.FolderType
    langleEncoderChannelAuxiliaryRangle: pnenc.objtypes.EncoderChannelType | None
    limitSupervision: ns0.objtypes.FolderType | None
    monitoring: ns0.objtypes.FolderType


o6.reference(VelocityServoDriveAxisType, "i=41", AxisSwOvertravelEventType)
o6.reference(VelocityServoDriveAxisType, "i=41", AxisHwOvertravelEventType)
o6.reference(VelocityServoDriveAxisType, "i=41", TorqueLimitEventType)


@o6.objecttype(nodeId="ns=pndrv;i=1009", browseName="ns=pndrv;PositionServoDriveAxisType", displayName="PositionServoDriveAxisType")
class PositionServoDriveAxisType(DriveAxisType):
    characteristicsConverter: ns0.objtypes.FolderType = o6.hasComponent(o6.ns["ns=pndrv;i=5035"])
    characteristicsMotorAndControl: ns0.objtypes.FolderType
    encoderChannelMechanic: pnenc.objtypes.EncoderChannelType | None
    encoderChannelMotor: pnenc.objtypes.EncoderChannelType
    homing: ns0.objtypes.FolderType | None
    langleEncoderChannelAuxiliaryRangle: pnenc.objtypes.EncoderChannelType | None = o6.hasComponent(o6.ns["ns=pndrv;i=5033"])
    limitSupervision: ns0.objtypes.FolderType | None
    monitoring: ns0.objtypes.FolderType


o6.reference(PositionServoDriveAxisType, "i=41", AxisSwOvertravelEventType)
o6.reference(PositionServoDriveAxisType, "i=41", AxisHwOvertravelEventType)
o6.reference(PositionServoDriveAxisType, "i=41", TorqueLimitEventType)


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pnenc, pndrv_vartypes
