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

"""Generated OPC UA ia namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as ia_reftypes
from . import datatypes as ia_datypes
from . import vartypes as ia_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=ia;i=1004",
    browseName="ns=ia;StackRunningType",
    displayName="StackRunningType",
    description="Contains information relevant to a stacklight operating as a running light. This base type does not define any specific information, but can be extended.",
)
class StackRunningType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(
    nodeId="ns=ia;i=1014",
    browseName="ns=ia;BaseCalibrationTargetCategoryType",
    displayName="BaseCalibrationTargetCategoryType",
    description="Abstract base type for categorizing calibration targets. Subtypes define the concrete categories.",
    isAbstract=True,
)
class BaseCalibrationTargetCategoryType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(
    nodeId="ns=ia;i=1015",
    browseName="ns=ia;ReusableCalibrationTargetCategoryType",
    displayName="ReusableCalibrationTargetCategoryType",
    description="Categorizes a calibration target to be reused several times. For example, a calibration target like a meter, that is bought specifically for calibration and not destroyed by an individual usage is of this category.",
)
class ReusableCalibrationTargetCategoryType(BaseCalibrationTargetCategoryType):
    pass


@o6.objecttype(
    nodeId="ns=ia;i=1016",
    browseName="ns=ia;ReusableDeviceCalibrationTargetCategoryType",
    displayName="ReusableDeviceCalibrationTargetCategoryType",
    description="Categorizes a calibration target to be a reusable device that produces a certain environment like pressure that can be used for calibration.",
)
class ReusableDeviceCalibrationTargetCategoryType(ReusableCalibrationTargetCategoryType):
    pass


@o6.objecttype(
    nodeId="ns=ia;i=1017",
    browseName="ns=ia;OneTimeCalibrationTargetCategoryType",
    displayName="OneTimeCalibrationTargetCategoryType",
    description="Categorizes a calibration target to be used only once, for example because the calibration destroys the target. Typically, Objects of this ObjectType do not represent one individual calibration target, but a batch of calibration targets with the same characteristics.",
)
class OneTimeCalibrationTargetCategoryType(BaseCalibrationTargetCategoryType):
    pass


@o6.objecttype(
    nodeId="ns=ia;i=1018",
    browseName="ns=ia;DynamicCalibrationTargetCategoryType",
    displayName="DynamicCalibrationTargetCategoryType",
    description="Characterizes a calibration target to be used together with a measurement instrument, that determines the values to be calibrated. It can be a piece created during the normal production process or an item specifically created for calibration purposes. The calibration target represents an individual piece or item, that is, if a new piece should be used or item is created, a new Object of this ObjectType is created.",
)
class DynamicCalibrationTargetCategoryType(BaseCalibrationTargetCategoryType):
    pass


@o6.objecttype(
    nodeId="ns=ia;i=1002",
    browseName="ns=ia;BasicStacklightType",
    displayName="BasicStacklightType",
    description="Entry point to a stacklight containing elements of the stacklight as well as additional information valid for the whole unit.",
)
class BasicStacklightType(ns0.objtypes.OrderedListType):
    langleOrderedObjectRangle: StackElementType | None
    stackLevel: StackLevelType | None
    stackRunning: StackRunningType | None = o6.hasComponent(
        StackRunningType(nodeId="ns=ia;i=5005", browseName="ns=ia;StackRunning", description="Valid if the stacklight is used in “Running_Light” StacklightMode.")
    )
    stacklightMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ia;i=6009",
            browseName="ns=ia;StacklightMode",
            description="Shows in what way (stack of individual lights, level meter, running light) the stacklight unit is used.",
            dataType=ia_datypes.StacklightOperationMode,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=ia;i=1003",
    browseName="ns=ia;StackLevelType",
    displayName="StackLevelType",
    description="Contains information relevant to a stacklight operating as a level meter. The whole stack is controlled by a percentual value.",
)
class StackLevelType(ns0.objtypes.BaseObjectType):
    displayMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=ia;i=6012",
            browseName="ns=ia;DisplayMode",
            description="Indicates in what way the percentual value is displayed with the stacklight.",
            dataType=ia_datypes.LevelDisplayMode,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    levelPercent: ns0.vartypes.AnalogItemType


@o6.objecttype(
    nodeId="ns=ia;i=1005",
    browseName="ns=ia;StackElementType",
    displayName="StackElementType",
    description="Base class for elements in a stacklight.",
    isAbstract=True,
    interfaces=[ns0.objtypes.IOrderedObjectType],
)
class StackElementType(ns0.objtypes.BaseObjectType):
    isPartOfBase: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ia;i=6014",
            browseName="ns=ia;IsPartOfBase",
            description="Indicates, if the element is contained in the mounting base of the stacklight. All elements contained in the mounting base shall be at the beginning of the list of stack elements.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    numberInList: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ia;i=6015",
            browseName="NumberInList",
            description="Enumerate the stacklight elements counting upwards beginning from the base of the stacklight.",
            dataType=ns0.datatypes.UInteger,
        )
    )
    signalOn: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ia;i=6013",
            browseName="ns=ia;SignalOn",
            description="Indicates if the signal emitted by the stack element is currently switched on or not.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=ia;i=1007", browseName="ns=ia;StackElementAcousticType", displayName="StackElementAcousticType", description="Represents an acoustic element in a stacklight."
)
class StackElementAcousticType(StackElementType):
    acousticSignals: ns0.objtypes.OrderedListType
    intensity: ns0.vartypes.AnalogItemType | None
    operationMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=ia;i=6020",
            browseName="ns=ia;OperationMode",
            description="Indicates what signal of the list of AcousticSignalType nodes is played when the acoustic element is switched on. It shall contain an index into the NumberInList of the respective AcousticSignalType Object of AcousticSignals.",
            dataType=ns0.datatypes.UInteger,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=ia;i=1008",
    browseName="ns=ia;ControlChannelType",
    displayName="ControlChannelType",
    description="Used for control channels of single colour elements within a stack element (e.g. RGB elements would use three ControlChannels, one for each controllable colour).",
)
class ControlChannelType(ns0.objtypes.BaseObjectType):
    channelColor: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=ia;i=6024",
            browseName="ns=ia;ChannelColor",
            description="Indicates in what mode (continuously on, blinking, flashing) the channel operates when switched on.",
            dataType=ia_datypes.SignalColor,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    intensity: ns0.vartypes.AnalogItemType | None
    signalMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=ia;i=6025",
            browseName="ns=ia;SignalMode",
            description="Contains a list of audio signals used by this acoustic stacklight element.",
            dataType=ia_datypes.SignalModeLight,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    signalOn: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ia;i=6023", browseName="ns=ia;SignalOn", description="Indicates if the colour is switched on.", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
        )
    )


@o6.objecttype(
    nodeId="ns=ia;i=1009",
    browseName="ns=ia;AcousticSignalType",
    displayName="AcousticSignalType",
    description="Represents an acoustic signal.",
    interfaces=[ns0.objtypes.IOrderedObjectType],
)
class AcousticSignalType(ns0.objtypes.BaseObjectType):
    audioSample: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=ia;i=6029",
            browseName="ns=ia;AudioSample",
            description="Contains the audio data, e.g. for devices capable of audio playback.",
            dataType=ns0.datatypes.AudioDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    numberInList: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ia;i=6028",
            browseName="NumberInList",
            description="Enumerate the acoustic signals. Instances of StackElementAcousticType index into this number using the OperationMode Property.",
            dataType=ns0.datatypes.UInteger,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=ia;i=1010",
    browseName="ns=ia;StacklightType",
    displayName="StacklightType",
    description="Entry point to a stacklight with the possibility to show the stacklight’s health status.",
    interfaces=[di.objtypes.IDeviceHealthType],
)
class StacklightType(BasicStacklightType):
    deviceHealth: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=ia;i=6038",
            browseName="ns=di;DeviceHealth",
            description="Contains the health status information of the stacklight.",
            dataType=di.datatypes.DeviceHealthEnumeration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    deviceHealthAlarms: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(
            nodeId="ns=ia;i=5007",
            browseName="ns=di;DeviceHealthAlarms",
            description="Contains alarms of the stacklights providing more detailed information on the health of the stacklight.",
        )
    )


@o6.objecttype(nodeId="ns=ia;i=1006", browseName="ns=ia;StackElementLightType", displayName="StackElementLightType", description="Represents a lamp element in a stacklight.")
class StackElementLightType(StackElementType):
    intensity: ns0.vartypes.AnalogItemType | None
    langleControlChannelRangle: ControlChannelType | None
    signalColor: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=ia;i=6016",
            browseName="ns=ia;SignalColor",
            description="Indicates the colour the lamp element has when switched on.",
            dataType=ia_datypes.SignalColor,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    signalMode: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=ia;i=6017",
            browseName="ns=ia;SignalMode",
            description="Shows in what way the lamp is used (continuous light, flashing, blinking) when switched on.",
            dataType=ia_datypes.SignalModeLight,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    signalRGBWValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=ia;i=6052", browseName="ns=ia;SignalRGBWValue", dataType=ia_datypes.RGBWDataType, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=ia;i=1019", browseName="ns=ia;CalibrationTargetType", displayName="CalibrationTargetType", description="Provides information about a calibration target.")
class CalibrationTargetType(ns0.objtypes.BaseObjectType):
    calibrationTargetCategory: BaseCalibrationTargetCategoryType = o6.hasComponent(
        BaseCalibrationTargetCategoryType(
            nodeId="ns=ia;i=5011", browseName="ns=ia;CalibrationTargetCategory", description="Defines what category the calibration target is of.", _allow_abstract=True
        )
    )
    calibrationTargetFeatures: ns0.objtypes.FolderType
    certificateUri: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ia;i=6063",
            browseName="ns=ia;CertificateUri",
            description="Contains the Uri of a certificate of the calibration target, in case the calibration target is certified and the information available. Otherwise, the Property should be omitted.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    identification: di.objtypes.FunctionalGroupType
    lastValidationDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ia;i=6060",
            browseName="ns=ia;LastValidationDate",
            description="Provides the date, the calibration target was validated the last time. If there is no specific validation date known, the date when the calibration target was bought or created should be used.",
            dataType=ns0.datatypes.UtcTime,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    nextValidationDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ia;i=6061",
            browseName="ns=ia;NextValidationDate",
            description="Provides the date, when the calibration target should be validated the next time. If this date is not known, the Property should be omitted. Note: Potentially the NextValidationDate is in the past, when the next validation did not take place.",
            dataType=ns0.datatypes.UtcTime,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    operationalConditions: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(
            nodeId="ns=ia;i=5012",
            browseName="ns=ia;OperationalConditions",
            description="A folder containing information about operational conditions of the calibration target. For example, it might provide in what ranges of humidity the calibration target can be operated. It might also provide correction information, for example, depending on the temperature the calibration values need to be corrected (in case of a length, the length might increase with high temperatures). If no operational conditions are provided, this folder should be omitted.",
        )
    )
    quality: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ia;i=6062",
            browseName="ns=ia;Quality",
            description="Provides the quality of the calibration target in percentage, this is, the value shall be between 0 and 100. 100 means the highest quality, 0 the lowest. The semantic of the quality is application-specific.",
            dataType=o6.Byte,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=ia;i=1011", browseName="ns=ia;IStatisticsType", displayName="IStatisticsType", description="Base interface for managing statistical data.", isAbstract=True
)
class IStatisticsType(ns0.objtypes.BaseInterfaceType):
    resetStatistics: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=ia;i=7001", browseName="ns=ia;ResetStatistics", description="Restarts all statistical data, including a reset of the StartTime to the current time.")
    )
    startTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ia;i=6046",
            browseName="ns=ia;StartTime",
            description="Indicates the point in time at which the collection of the statistical data has been started.",
            dataType=o6.DateTime,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=ia;i=1012",
    browseName="ns=ia;IAggregateStatisticsType",
    displayName="IAggregateStatisticsType",
    description="Base interface for managing statistical data that is not rolled over. All data from the start of tracking the statistical data are considered, until the tracking gets reset.",
    isAbstract=True,
)
class IAggregateStatisticsType(IStatisticsType):
    resetCondition: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ia;i=6047",
            browseName="ns=ia;ResetCondition",
            description="The reason and context for the reset of the statistics, which is done without a trigger from an OPC UA Client, like calling the ResetStatistics Method. ResetCondition is a vendor-specific, human readable string. ResetCondition is non-localized and might contain an expression that can be parsed by certain clients. Examples are: “AFTER 4 HOURS”, “AFTER 1000 ITEMS”, “OPERATOR”. “OPERATOR” means, that an operator resets the statistics on a local HMI.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=ia;i=1013",
    browseName="ns=ia;IRollingStatisticsType",
    displayName="IRollingStatisticsType",
    description="Base interface for managing statistical data that is rolled over, i.e. only a certain amount of data is considered for statistical data.",
    isAbstract=True,
)
class IRollingStatisticsType(IStatisticsType):
    windowDuration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ia;i=6048",
            browseName="ns=ia;WindowDuration",
            description="The duration after the statistical data are rolled over. Only the data that were gathered during that duration are considered for the statistical data, even if the time interval between the StartTime and the current time is longer.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    windowNumberOfValues: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=ia;i=6049",
            browseName="ns=ia;WindowNumberOfValues",
            description="The number of values before the data gets rolled over. For the statistical data, only the data fitting into the number of values is considered, even if more data were gathered since StartTime.",
            dataType=o6.UInt32,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


del Any, TYPE_CHECKING, uuid, o6, di, ns0, ia_reftypes, ia_datypes, ia_vartypes
