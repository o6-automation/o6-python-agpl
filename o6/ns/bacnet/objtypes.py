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

"""Generated OPC UA bacnet namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import datatypes as bacnet_datypes
from . import vartypes as bacnet_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=bacnet;i=1002", browseName="ns=bacnet;BACnetObjectType", displayName="BACnetObjectType", isAbstract=True)
class BACnetObjectType(ns0.objtypes.BaseObjectType):
    object_Identifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6072", browseName="ns=bacnet;Object_Identifier", dataType=bacnet_datypes.BACnetObjectIdentifier, accessLevel=3, userAccessLevel=1
        )
    )
    profile_Name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6069", browseName="ns=bacnet;Profile_Name", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1012", browseName="ns=bacnet;BACnetBinaryType", displayName="BACnetBinaryType", isAbstract=True)
class BACnetBinaryType(BACnetObjectType):
    changeOfState: BACnetChangeOfStateCountType | None
    elapsedActiveTime: BACnetElapsedActiveTimeType | None
    eventReporting: BACnetEventReportingType | None
    faultEvaluation: BACnetFaultEvaluationType | None
    out_Of_Service: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6023", browseName="ns=bacnet;Out_Of_Service", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    present_Value: ns0.vartypes.TwoStateDiscreteType
    status_Flags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6111", browseName="ns=bacnet;Status_Flags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1013", browseName="ns=bacnet;BACnetBinaryInputType", displayName="BACnetBinaryInputType")
class BACnetBinaryInputType(BACnetBinaryType):
    device_Type: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6032", browseName="ns=bacnet;Device_Type", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    eventReporting: BACnetEventReportingType | None
    polarity: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6096", browseName="ns=bacnet;Polarity", dataType=bacnet_datypes.BACnetPolarity, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1018", browseName="ns=bacnet;BACnetMultiStateType", displayName="BACnetMultiStateType", isAbstract=True)
class BACnetMultiStateType(BACnetObjectType):
    eventReporting: BACnetEventReportingType | None
    faultEvaluation: BACnetFaultEvaluationType | None
    out_Of_Service: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6109", browseName="ns=bacnet;Out_Of_Service", dataType=o6.Boolean, value=False, accessLevel=3, userAccessLevel=1)
    )
    present_Value: ns0.vartypes.MultiStateDiscreteType
    status_Flags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6135", browseName="ns=bacnet;Status_Flags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1019", browseName="ns=bacnet;BACnetMultiStateInputType", displayName="BACnetMultiStateInputType")
class BACnetMultiStateInputType(BACnetMultiStateType):
    device_Type: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6122", browseName="ns=bacnet;Device_Type", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    eventReporting: BACnetEventReportingType | None
    faultEvaluation: BACnetFaultEvaluationType | None


@o6.objecttype(nodeId="ns=bacnet;i=1021", browseName="ns=bacnet;BACnetMultiStateValueType", displayName="BACnetMultiStateValueType")
class BACnetMultiStateValueType(BACnetMultiStateType):
    eventReporting: BACnetEventReportingType | None
    faultEvaluation: BACnetFaultEvaluationType | None
    priority_Array: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6126",
            browseName="ns=bacnet;Priority_Array",
            dataType=bacnet_datypes.BACnetPriorityValue,
            valueRank=1,
            arrayDimensions=[16],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    relinquish_Default: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6127", browseName="ns=bacnet;Relinquish_Default", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1048", browseName="ns=bacnet;BACnetNotifierType", displayName="BACnetNotifierType", isAbstract=True)
class BACnetNotifierType(BACnetObjectType):
    recipient_List: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6201",
            browseName="ns=bacnet;Recipient_List",
            dataType=bacnet_datypes.BACnetDestination,
            value=bacnet_datypes.BACnetDestination(
                validDays=bacnet_datypes.BACnetDaysOfWeek(value=b"\x00", validBits=b"\x7f"),
                fromTime=bacnet_datypes.BACnetTime(hour=0, minute=0, second=0, hundredths=0),
                toTime=bacnet_datypes.BACnetTime(hour=0, minute=0, second=0, hundredths=0),
                recipient=bacnet_datypes.BACnetRecipient(device=0, address=bacnet_datypes.BACnetAddress(networkNumber=0, macAddress=b"")),
                processIdentifier=0,
                issueConfirmedNotifications=False,
                transitions=bacnet_datypes.BACnetEventTransitionBits(value=b"\x00", validBits=b"\x07"),
            ),
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=bacnet;i=1049", browseName="ns=bacnet;BACnetStructuredViewType", displayName="BACnetStructuredViewType", isAbstract=True)
class BACnetStructuredViewType(BACnetObjectType):
    langleBACnetObjectRangle: BACnetObjectType | None
    langleBACnetStructuredViewRangle: BACnetStructuredViewType | None
    node_Subtype: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6238", browseName="ns=bacnet;Node_Subtype", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    node_Type: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6057", browseName="ns=bacnet;Node_Type", dataType=bacnet_datypes.BACnetNodeType, accessLevel=3, userAccessLevel=1)
    )
    subordinate_Annotations: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6078", browseName="ns=bacnet;Subordinate_Annotations", dataType=o6.String, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
        )
    )
    subordinate_List: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6077",
            browseName="ns=bacnet;Subordinate_List",
            dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=bacnet;i=1025", browseName="ns=bacnet;BACnetFaultEvaluationType", displayName="BACnetFaultEvaluationType")
class BACnetFaultEvaluationType(ns0.objtypes.BaseObjectType):
    faultAlgorithm: BACnetFaultAlgorithmType | None
    reliability: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6304", browseName="ns=bacnet;Reliability", dataType=bacnet_datypes.BACnetReliability, accessLevel=3, userAccessLevel=1)
    )
    reliability_Evaluation_Inhibit: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6305", browseName="ns=bacnet;Reliability_Evaluation_Inhibit", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1020", browseName="ns=bacnet;BACnetMultiStateOutputType", displayName="BACnetMultiStateOutputType")
class BACnetMultiStateOutputType(BACnetMultiStateType):
    device_Type: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6123", browseName="ns=bacnet;Device_Type", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    eventReporting: BACnetEventReportingType | None
    feedback_Value: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6312", browseName="ns=bacnet;Feedback_Value", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    priority_Array: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6124",
            browseName="ns=bacnet;Priority_Array",
            dataType=bacnet_datypes.BACnetPriorityValue,
            valueRank=1,
            arrayDimensions=[16],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    relinquish_Default: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6125", browseName="ns=bacnet;Relinquish_Default", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1024", browseName="ns=bacnet;BACnetNotificationClassType", displayName="BACnetNotificationClassType")
class BACnetNotificationClassType(BACnetNotifierType):
    ack_Required: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6344", browseName="ns=bacnet;Ack_Required", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
        )
    )
    notification_Class: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6131", browseName="ns=bacnet;Notification_Class", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )
    priority: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6343", browseName="ns=bacnet;Priority", dataType=o6.Byte, valueRank=1, arrayDimensions=[3], accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1004", browseName="ns=bacnet;BACnetAnalogType", displayName="BACnetAnalogType", isAbstract=True)
class BACnetAnalogType(BACnetObjectType):
    cOV_Increment: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6068", browseName="ns=bacnet;COV_Increment", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
    )
    eventReporting: BACnetEventReportingType | None
    faultEvaluation: BACnetFaultEvaluationType | None
    out_Of_Service: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6038", browseName="ns=bacnet;Out_Of_Service", dataType=o6.Boolean, value=False, accessLevel=3, userAccessLevel=1)
    )
    present_Value: ns0.vartypes.AnalogUnitType
    resolution: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6409", browseName="ns=bacnet;Resolution", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
    )
    status_Flags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6024", browseName="ns=bacnet;Status_Flags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1005", browseName="ns=bacnet;BACnetAnalogInputType", displayName="BACnetAnalogInputType")
class BACnetAnalogInputType(BACnetAnalogType):
    device_Type: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6037", browseName="ns=bacnet;Device_Type", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1006", browseName="ns=bacnet;BACnetAnalogOutputType", displayName="BACnetAnalogOutputType")
class BACnetAnalogOutputType(BACnetAnalogType):
    device_Type: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6045", browseName="ns=bacnet;Device_Type", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    priority_Array: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6070",
            browseName="ns=bacnet;Priority_Array",
            dataType=bacnet_datypes.BACnetPriorityValue,
            valueRank=1,
            arrayDimensions=[16],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    relinquish_Default: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6086", browseName="ns=bacnet;Relinquish_Default", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1007", browseName="ns=bacnet;BACnetAnalogValueType", displayName="BACnetAnalogValueType")
class BACnetAnalogValueType(BACnetAnalogType):
    priority_Array: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6071",
            browseName="ns=bacnet;Priority_Array",
            dataType=bacnet_datypes.BACnetPriorityValue,
            valueRank=1,
            arrayDimensions=[16],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    relinquish_Default: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6087", browseName="ns=bacnet;Relinquish_Default", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1026", browseName="ns=bacnet;BACnetEventAlgorithmType", displayName="BACnetEventAlgorithmType", isAbstract=True)
class BACnetEventAlgorithmType(ns0.objtypes.BaseObjectType):
    timeDelay: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6415", browseName="ns=bacnet;TimeDelay", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )
    timeDelayNormal: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6416", browseName="ns=bacnet;TimeDelayNormal", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1009", browseName="ns=bacnet;BACnetOutOfRangeAlgorithmType", displayName="BACnetOutOfRangeAlgorithmType")
class BACnetOutOfRangeAlgorithmType(BACnetEventAlgorithmType):
    deadband: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6049", browseName="ns=bacnet;Deadband", dataType=o6.Float, value=0.0, accessLevel=3, userAccessLevel=1)
    )
    highLimit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6047", browseName="ns=bacnet;HighLimit", dataType=o6.Float, value=0.0, accessLevel=3, userAccessLevel=1)
    )
    limitEnable: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6051", browseName="ns=bacnet;LimitEnable", dataType=bacnet_datypes.BACnetLimitEnable, accessLevel=3, userAccessLevel=1)
    )
    lowLimit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6048", browseName="ns=bacnet;LowLimit", dataType=o6.Float, value=0.0, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1010", browseName="ns=bacnet;BACnetChangeOfStateAlgorithmType", displayName="BACnetChangeOfStateAlgorithmType")
class BACnetChangeOfStateAlgorithmType(BACnetEventAlgorithmType):
    alarmValues: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6016", browseName="ns=bacnet;AlarmValues", valueRank=-2, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1029", browseName="ns=bacnet;BACnetCommandFailureAlgorithmType", displayName="BACnetCommandFailureAlgorithmType")
class BACnetCommandFailureAlgorithmType(BACnetEventAlgorithmType):
    feedbackValueRef: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6017", browseName="ns=bacnet;FeedbackValueRef", dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference, accessLevel=3, userAccessLevel=1
        )
    )


@o6.objecttype(nodeId="ns=bacnet;i=1001", browseName="ns=bacnet;BACnetNotificationType", displayName="BACnetNotificationType", isAbstract=True)
class BACnetNotificationType(ns0.objtypes.AlarmConditionType):
    from_State: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6322", browseName="ns=bacnet;From_State", dataType=bacnet_datypes.BACnetEventState, accessLevel=3, userAccessLevel=1)
    )
    notification_Class: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6132", browseName="ns=bacnet;Notification_Class", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )
    notify_Type: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6133", browseName="ns=bacnet;Notify_Type", dataType=bacnet_datypes.BACnetNotifyType, accessLevel=3, userAccessLevel=1)
    )
    to_State: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6698", browseName="ns=bacnet;To_State", dataType=bacnet_datypes.BACnetEventState, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1027", browseName="ns=bacnet;BACnetFaultNotificationType", displayName="BACnetFaultNotificationType")
class BACnetFaultNotificationType(BACnetNotificationType):
    reliability: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6134", browseName="ns=bacnet;Reliability", dataType=bacnet_datypes.BACnetReliability, accessLevel=3, userAccessLevel=1)
    )
    status_Flags: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6015", browseName="ns=bacnet;Status_Flags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1028", browseName="ns=bacnet;BACnetEventNotificationType", displayName="BACnetEventNotificationType")
class BACnetEventNotificationType(BACnetNotificationType):
    event_Values: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6136", browseName="ns=bacnet;Event_Values", valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1031", browseName="ns=bacnet;BACnetOutOfRangeNotificationType", displayName="BACnetOutOfRangeNotificationType")
class BACnetOutOfRangeNotificationType(BACnetEventNotificationType):
    deadband: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6012", browseName="ns=bacnet;Deadband", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
    )
    exceedingLimit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6013", browseName="ns=bacnet;ExceedingLimit", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
    )
    exceedingValue: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6004", browseName="ns=bacnet;ExceedingValue", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
    )
    statusFlags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6014", browseName="ns=bacnet;StatusFlags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1032", browseName="ns=bacnet;BACnetSimpleNotificationType", displayName="BACnetSimpleNotificationType")
class BACnetSimpleNotificationType(BACnetFaultNotificationType):
    pass


@o6.objecttype(nodeId="ns=bacnet;i=1033", browseName="ns=bacnet;BACnetLoopNotificationType", displayName="BACnetLoopNotificationType")
class BACnetLoopNotificationType(BACnetFaultNotificationType):
    pass


@o6.objecttype(nodeId="ns=bacnet;i=1034", browseName="ns=bacnet;BACnetFeedbackNotificationType", displayName="BACnetFeedbackNotificationType")
class BACnetFeedbackNotificationType(BACnetFaultNotificationType):
    pass


@o6.objecttype(nodeId="ns=bacnet;i=1035", browseName="ns=bacnet;BACnetEventEnrollmentNotificationType", displayName="BACnetEventEnrollmentNotificationType")
class BACnetEventEnrollmentNotificationType(BACnetFaultNotificationType):
    pass


@o6.objecttype(nodeId="ns=bacnet;i=1036", browseName="ns=bacnet;BACnetChangeOfReliabilityNotificationType", displayName="BACnetChangeOfReliabilityNotificationType")
class BACnetChangeOfReliabilityNotificationType(BACnetFaultNotificationType):
    propertyValues: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6208", browseName="ns=bacnet;PropertyValues", valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1037", browseName="ns=bacnet;BACnetChangeOfBitStringNotificationType", displayName="BACnetChangeOfBitStringNotificationType")
class BACnetChangeOfBitStringNotificationType(BACnetEventNotificationType):
    referencedBitString: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6018", browseName="ns=bacnet;ReferencedBitString", dataType=o6.Boolean, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
        )
    )
    statusFlags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6026", browseName="ns=bacnet;StatusFlags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1038", browseName="ns=bacnet;BACnetChangeOfStateNotificationType", displayName="BACnetChangeOfStateNotificationType")
class BACnetChangeOfStateNotificationType(BACnetEventNotificationType):
    newState: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6029",
            browseName="ns=bacnet;NewState",
            dataType=bacnet_datypes.BACnetPropertyStates,
            value=bacnet_datypes.BACnetPropertyStates(
                booleanValue=False,
                binaryValue=bacnet_datypes.BACnetBinaryPV.INACTIVE,
                eventType=bacnet_datypes.BACnetEventEnumType.CHANGE_OF_BITSTRING,
                polarity=bacnet_datypes.BACnetPolarity.NORMAL,
                programChange=bacnet_datypes.BACnetProgramRequest.READY,
                programState=bacnet_datypes.BACnetProgramStates.IDLE,
                programError=bacnet_datypes.BACnetProgramError.NORMAL,
                reliability=bacnet_datypes.BACnetReliability.NO_FAULT_DETECTED,
                state=bacnet_datypes.BACnetEventState.NORMAL,
                systemStatus=bacnet_datypes.BACnetDeviceStatus.OPERATIONAL,
                units=ns0.datatypes.EUInformation(namespaceUri="", unitId=0, displayName=o6.LocalizedText()),
                unsignedValue=0,
                lifeSafetyMode=bacnet_datypes.BACnetLifeSafetyMode.OFF,
                lifeSafetyState=bacnet_datypes.BACnetLifeSafetyState.QUIET,
            ),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    statusFlags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6030", browseName="ns=bacnet;StatusFlags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1039", browseName="ns=bacnet;BACnetChangeOfRealValueNotificationType", displayName="BACnetChangeOfRealValueNotificationType")
class BACnetChangeOfRealValueNotificationType(BACnetEventNotificationType):
    newValue: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6031", browseName="ns=bacnet;NewValue", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
    )
    statusFlags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6039", browseName="ns=bacnet;StatusFlags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1040", browseName="ns=bacnet;BACnetCommandFailureNotificationType", displayName="BACnetCommandFailureNotificationType")
class BACnetCommandFailureNotificationType(BACnetEventNotificationType):
    commandValue: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6040", browseName="ns=bacnet;CommandValue", accessLevel=3, userAccessLevel=1)
    )
    feedbackValue: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6046", browseName="ns=bacnet;FeedbackValue", accessLevel=3, userAccessLevel=1)
    )
    statusFlags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6058", browseName="ns=bacnet;StatusFlags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1041", browseName="ns=bacnet;BACnetFloatingLimitNotificationType", displayName="BACnetFloatingLimitNotificationType")
class BACnetFloatingLimitNotificationType(BACnetEventNotificationType):
    errorLimit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6062", browseName="ns=bacnet;ErrorLimit", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
    )
    referenceValue: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6060", browseName="ns=bacnet;ReferenceValue", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
    )
    setpointValue: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6061", browseName="ns=bacnet;SetpointValue", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
    )
    statusFlags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6063", browseName="ns=bacnet;StatusFlags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1042", browseName="ns=bacnet;BACnetBufferReadyNotificationType", displayName="BACnetBufferReadyNotificationType")
class BACnetBufferReadyNotificationType(BACnetEventNotificationType):
    bufferProperty: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6085", browseName="ns=bacnet;BufferProperty", dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference, accessLevel=3, userAccessLevel=1
        )
    )
    currentNotification: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6098", browseName="ns=bacnet;CurrentNotification", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )
    previousNotification: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6093", browseName="ns=bacnet;PreviousNotification", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1043", browseName="ns=bacnet;BACnetUnsignedRangeNotificationType", displayName="BACnetUnsignedRangeNotificationType")
class BACnetUnsignedRangeNotificationType(BACnetEventNotificationType):
    exceedingLimit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6100", browseName="ns=bacnet;ExceedingLimit", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    exceedingValue: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6099", browseName="ns=bacnet;ExceedingValue", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    statusFlags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6101", browseName="ns=bacnet;StatusFlags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1044", browseName="ns=bacnet;BACnetDoubleOutOfRangeNotificationType", displayName="BACnetDoubleOutOfRangeNotificationType")
class BACnetDoubleOutOfRangeNotificationType(BACnetEventNotificationType):
    deadband: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6104", browseName="ns=bacnet;Deadband", dataType=o6.Double, accessLevel=3, userAccessLevel=1)
    )
    exceedingLimit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6112", browseName="ns=bacnet;ExceedingLimit", dataType=o6.Double, accessLevel=3, userAccessLevel=1)
    )
    exceedingValue: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6103", browseName="ns=bacnet;ExceedingValue", dataType=o6.Double, accessLevel=3, userAccessLevel=1)
    )
    statusFlags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6113", browseName="ns=bacnet;StatusFlags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1045", browseName="ns=bacnet;BACnetSignedOutOfRangeNotificationType", displayName="BACnetSignedOutOfRangeNotificationType")
class BACnetSignedOutOfRangeNotificationType(BACnetEventNotificationType):
    deadband: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6115", browseName="ns=bacnet;Deadband", dataType=ns0.datatypes.Integer, accessLevel=3, userAccessLevel=1)
    )
    exceedingLimit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6129", browseName="ns=bacnet;ExceedingLimit", dataType=ns0.datatypes.Integer, accessLevel=3, userAccessLevel=1)
    )
    exceedingValue: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6114", browseName="ns=bacnet;ExceedingValue", dataType=ns0.datatypes.Integer, accessLevel=3, userAccessLevel=1)
    )
    statusFlags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6138", browseName="ns=bacnet;StatusFlags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1046", browseName="ns=bacnet;BACnetUnsignedOutOfRangeNotificationType", displayName="BACnetUnsignedOutOfRangeNotificationType")
class BACnetUnsignedOutOfRangeNotificationType(BACnetEventNotificationType):
    deadband: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6143", browseName="ns=bacnet;Deadband", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    exceedingLimit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6144", browseName="ns=bacnet;ExceedingLimit", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    exceedingValue: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6140", browseName="ns=bacnet;ExceedingValue", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    statusFlags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6145", browseName="ns=bacnet;StatusFlags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1047", browseName="ns=bacnet;BACnetChangeOfCharacterStringNotificationType", displayName="BACnetChangeOfCharacterStringNotificationType")
class BACnetChangeOfCharacterStringNotificationType(BACnetEventNotificationType):
    alarmValue: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6156", browseName="ns=bacnet;AlarmValue", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    changedValue: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6146", browseName="ns=bacnet;ChangedValue", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    statusFlags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6157", browseName="ns=bacnet;StatusFlags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1053", browseName="ns=bacnet;BACnetChangeOfValueNotificationType", displayName="BACnetChangeOfValueNotificationType")
class BACnetChangeOfValueNotificationType(BACnetEventNotificationType):
    newValue: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6209", browseName="ns=bacnet;NewValue", dataType=ns0.datatypes.OptionSet, accessLevel=3, userAccessLevel=1)
    )
    statusFlags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6398", browseName="ns=bacnet;StatusFlags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1016", browseName="ns=bacnet;BACnetChangeOfStateCountType", displayName="BACnetChangeOfStateCountType")
class BACnetChangeOfStateCountType(ns0.objtypes.BaseObjectType):
    change_Of_State_Count: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6035", browseName="ns=bacnet;Change_Of_State_Count", dataType=o6.UInt32, value=0, accessLevel=3, userAccessLevel=1)
    )
    change_Of_State_Time: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6034", browseName="ns=bacnet;Change_Of_State_Time", dataType=bacnet_datypes.BACnetDateTime, accessLevel=3, userAccessLevel=1)
    )
    reset: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="ns=bacnet;i=7001", browseName="ns=bacnet;Reset"))
    time_Of_State_Count_Reset: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6041", browseName="ns=bacnet;Time_Of_State_Count_Reset", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1017", browseName="ns=bacnet;BACnetElapsedActiveTimeType", displayName="BACnetElapsedActiveTimeType")
class BACnetElapsedActiveTimeType(ns0.objtypes.BaseObjectType):
    elapsed_Active_Time: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6042", browseName="ns=bacnet;Elapsed_Active_Time", dataType=o6.UInt32, value=0, accessLevel=3, userAccessLevel=1)
    )
    reset: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="ns=bacnet;i=7003", browseName="ns=bacnet;Reset"))
    time_Of_Active_Time_Reset: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6043", browseName="ns=bacnet;Time_Of_Active_Time_Reset", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6083",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CalendarEntries", dataType=bacnet_datypes.BACnetCalendarEntry, valueRank=1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=106294",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="FirstFailedElementNumber",
            dataType=o6.UInt32,
            valueRank=-1,
            description=o6.LocalizedText(
                "The numerical position, starting at 1, of the failed element in the CalendarEntries. If the call succeeds or fails for other reasons, the returned value shall be 0."
            ),
        )
    ],
)
o6.call(
    nodeId="ns=bacnet;i=7005",
    browseName="ns=bacnet;AddDateListElements",
    inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6083"]),
    outputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=106294"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6084",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CalendarEntries", dataType=bacnet_datypes.BACnetCalendarEntry, valueRank=1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=106295",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FirstFailedElementNumber", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=bacnet;i=7006",
    browseName="ns=bacnet;RemoveDateListElements",
    inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6084"]),
    outputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=106295"]),
)


@o6.objecttype(nodeId="ns=bacnet;i=1008", browseName="ns=bacnet;BACnetCalendarType", displayName="BACnetCalendarType")
class BACnetCalendarType(BACnetObjectType):
    addDateListElements: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=bacnet;i=7005"])
    date_List: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6076",
            browseName="ns=bacnet;Date_List",
            dataType=bacnet_datypes.BACnetCalendarEntry,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    present_Value: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=bacnet;i=6073", browseName="ns=bacnet;Present_Value", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    removeDateListElements: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=bacnet;i=7006"])


ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6245",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BACnetIds", dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference, valueRank=1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6246",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="OpcUaIds", dataType=o6.NodeId, valueRank=1)],
)
o6.call(
    nodeId="ns=bacnet;i=7009", browseName="ns=bacnet;TranslateBACnetIds", inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6245"]), outputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6246"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6247",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="BACnetDeviceIds", dataType=bacnet_datypes.BACnetObjectIdentifier, valueRank=1),
        ns0.datatypes.Argument(name="OpcUaObjectIds", dataType=o6.NodeId, valueRank=1),
    ],
)
o6.call(nodeId="ns=bacnet;i=7010", browseName="ns=bacnet;GetDeviceIdList", outputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6247"]))

ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6248",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DeviceObject", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=bacnet;i=7011", browseName="ns=bacnet;AddDeviceById", inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6248"]))

ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6252",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Address", dataType=ns0.datatypes.BaseDataType, valueRank=-1)],
)
o6.call(nodeId="ns=bacnet;i=7012", browseName="ns=bacnet;AddDeviceByAddress", inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6252"]))

ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6254",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ObjectSpecifier", dataType=bacnet_datypes.BACnetObjectIdentifier, valueRank=-1),
        ns0.datatypes.Argument(name="ListOfInitialValues", dataType=ns0.datatypes.KeyValuePair, valueRank=1, arrayDimensions=[0]),
    ],
)
o6.call(nodeId="ns=bacnet;i=7013", browseName="ns=bacnet;CreateObject", inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6254"]))

ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6256",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ObjectIdentifier", dataType=bacnet_datypes.BACnetObjectIdentifier, valueRank=-1)],
)
o6.call(nodeId="ns=bacnet;i=7014", browseName="ns=bacnet;DeleteObject", inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6256"]))

ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6266",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="TimeDurationInMinutes", dataType=o6.UInt16, valueRank=-1),
        ns0.datatypes.Argument(name="EnableDisable", dataType=bacnet_datypes.BACnetDeviceCommunicationEnabled, valueRank=-1),
        ns0.datatypes.Argument(name="Password", dataType=o6.String, valueRank=-1),
    ],
)
o6.call(nodeId="ns=bacnet;i=7015", browseName="ns=bacnet;DeviceCommunicationControl", description="ToDo", inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6266"]))

ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6255",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ReinitializedStateofDevice", dataType=bacnet_datypes.BACnetReinitializedStateofDevice, valueRank=-1),
        ns0.datatypes.Argument(name="Password", dataType=o6.String, valueRank=-1),
    ],
)
o6.call(nodeId="ns=bacnet;i=7016", browseName="ns=bacnet;ReinitializeDevice", inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6255"]))

ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6267",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(name="SendUnconfirmed", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="TextMessageSourceDevice", dataType=bacnet_datypes.BACnetObjectIdentifier, valueRank=-1),
        ns0.datatypes.Argument(name="MessageClass", dataType=bacnet_datypes.BACnetMessageClass, valueRank=-1),
        ns0.datatypes.Argument(name="MessagePriority", dataType=bacnet_datypes.BACnetMessagePriority, valueRank=-1),
        ns0.datatypes.Argument(name="Message", dataType=o6.String, valueRank=-1),
    ],
)
o6.call(nodeId="ns=bacnet;i=7019", browseName="ns=bacnet;TextMessage", inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6267"]))

ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6662",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Time", dataType=ns0.datatypes.UtcTime, valueRank=-1)],
)
o6.call(nodeId="ns=bacnet;i=7021", browseName="ns=bacnet;TimeSynchronization", inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6662"]))

ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6660",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="WaitTimeInSeconds", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ApplyRange", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="DeviceRangeLow", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="DeviceRangeHigh", dataType=o6.UInt32, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6661",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="DeviceAddressBindings", dataType=ns0.datatypes.BaseDataType, valueRank=1),
        ns0.datatypes.Argument(name="MaxAPDULengthAccepted", dataType=o6.UInt32, valueRank=1),
        ns0.datatypes.Argument(name="SegmentationSupported", dataType=bacnet_datypes.BACnetSegmentation, valueRank=1),
        ns0.datatypes.Argument(name="VendorIdentifier", dataType=o6.UInt16, valueRank=1),
    ],
)
o6.call(nodeId="ns=bacnet;i=7023", browseName="ns=bacnet;NetworkScan", inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6660"]), outputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6661"]))


@o6.objecttype(nodeId="ns=bacnet;i=1030", browseName="ns=bacnet;BACnetInternetworkType", displayName="BACnetInternetworkType")
class BACnetInternetworkType(ns0.objtypes.BaseObjectType):
    addDeviceByAddress: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=bacnet;i=7012"])
    addDeviceById: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=bacnet;i=7011"])
    getDeviceIdList: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=bacnet;i=7010"])
    langleBACnetDeviceNameRangle: BACnetDeviceType | None
    networkScan: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=bacnet;i=7023"])
    timeSynchronization: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=bacnet;i=7021"])
    translateBACnetIds: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=bacnet;i=7009"])


ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6271",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AddressBindings", dataType=bacnet_datypes.BACnetAddressBinding, valueRank=1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6272",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FirstFailedElementNumber", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=bacnet;i=7024",
    browseName="ns=bacnet;AddDeviceAddressBindings",
    inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6271"]),
    outputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6272"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6273",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AddressBindings", dataType=bacnet_datypes.BACnetAddressBinding, valueRank=1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6274",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FirstFailedElementNumber", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=bacnet;i=7025",
    browseName="ns=bacnet;RemoveDeviceAddressBindings",
    inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6273"]),
    outputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6274"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6353",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="AddToUtcList", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="TimeSynchronizationRecipients", dataType=bacnet_datypes.BACnetRecipient, valueRank=1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6354",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FirstFailedElementNumber", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=bacnet;i=7027",
    browseName="ns=bacnet;AddTimeSynchronizationRecipients",
    inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6353"]),
    outputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6354"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6355",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7028",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="RemoveFromUtcList", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="TimeSynchronizationRecipients", dataType=bacnet_datypes.BACnetRecipient, valueRank=1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6356",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7028",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FirstFailedElementNumber", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=bacnet;i=7028",
    browseName="ns=bacnet;RemoveTimeSynchronizationRecipients",
    inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6355"]),
    outputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6356"]),
)


@o6.objecttype(nodeId="ns=bacnet;i=101025", browseName="ns=bacnet;BACnetFaultAlgorithmType", displayName="BACnetFaultAlgorithmType", isAbstract=True)
class BACnetFaultAlgorithmType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(nodeId="ns=bacnet;i=101012", browseName="ns=bacnet;BACnetFaultStatusFlagsAlgorithmType", displayName="BACnetFaultStatusFlagsAlgorithmType")
class BACnetFaultStatusFlagsAlgorithmType(BACnetFaultAlgorithmType):
    pass


@o6.objecttype(nodeId="ns=bacnet;i=101029", browseName="ns=bacnet;BACnetUnsignedRangeAlgorithmType", displayName="BACnetUnsignedRangeAlgorithmType")
class BACnetUnsignedRangeAlgorithmType(BACnetEventAlgorithmType):
    highLimit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6362", browseName="ns=bacnet;HighLimit", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    lowLimit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6363", browseName="ns=bacnet;LowLimit", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=101030", browseName="ns=bacnet;BACnetChangeOfStatusFlagsAlgorithmType", displayName="BACnetChangeOfStatusFlagsAlgorithmType")
class BACnetChangeOfStatusFlagsAlgorithmType(BACnetEventAlgorithmType):
    selectedFlags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6364", browseName="ns=bacnet;SelectedFlags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=101031", browseName="ns=bacnet;BACnetDoubleOutOfRangeAlgorithmType", displayName="BACnetDoubleOutOfRangeAlgorithmType")
class BACnetDoubleOutOfRangeAlgorithmType(BACnetEventAlgorithmType):
    deadband: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6022", browseName="ns=bacnet;Deadband", dataType=o6.Double, accessLevel=3, userAccessLevel=1)
    )
    highLimit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6249", browseName="ns=bacnet;HighLimit", dataType=o6.Double, accessLevel=3, userAccessLevel=1)
    )
    limitEnable: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6345", browseName="ns=bacnet;LimitEnable", dataType=bacnet_datypes.BACnetLimitEnable, accessLevel=3, userAccessLevel=1)
    )
    lowLimit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6399", browseName="ns=bacnet;LowLimit", dataType=o6.Double, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=101032", browseName="ns=bacnet;BACnetSignedOutOfRangeAlgorithmType", displayName="BACnetSignedOutOfRangeAlgorithmType")
class BACnetSignedOutOfRangeAlgorithmType(BACnetEventAlgorithmType):
    deadband: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6365", browseName="ns=bacnet;Deadband", dataType=ns0.datatypes.Integer, accessLevel=3, userAccessLevel=1)
    )
    highLimit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6366", browseName="ns=bacnet;HighLimit", dataType=ns0.datatypes.Integer, accessLevel=3, userAccessLevel=1)
    )
    limitEnable: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6367", browseName="ns=bacnet;LimitEnable", dataType=bacnet_datypes.BACnetLimitEnable, accessLevel=3, userAccessLevel=1)
    )
    lowLimit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6368", browseName="ns=bacnet;LowLimit", dataType=ns0.datatypes.Integer, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=101033", browseName="ns=bacnet;BACnetUnsignedOutOfRangeAlgorithmType", displayName="BACnetUnsignedOutOfRangeAlgorithmType")
class BACnetUnsignedOutOfRangeAlgorithmType(BACnetEventAlgorithmType):
    deadband: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6369", browseName="ns=bacnet;Deadband", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    highLimit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6370", browseName="ns=bacnet;HighLimit", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    limitEnable: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6371", browseName="ns=bacnet;LimitEnable", dataType=bacnet_datypes.BACnetLimitEnable, accessLevel=3, userAccessLevel=1)
    )
    lowLimit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6372", browseName="ns=bacnet;LowLimit", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=101034", browseName="ns=bacnet;BACnetChangeOfCharacterStringAlgorithmType", displayName="BACnetChangeOfCharacterStringAlgorithmType")
class BACnetChangeOfCharacterStringAlgorithmType(BACnetEventAlgorithmType):
    alarmValues: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6373", browseName="ns=bacnet;AlarmValues", dataType=o6.String, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
        )
    )


@o6.objecttype(nodeId="ns=bacnet;i=101001", browseName="ns=bacnet;BACnetLoopType", displayName="BACnetLoopType")
class BACnetLoopType(BACnetObjectType):
    action: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106033", browseName="ns=bacnet;Action", dataType=bacnet_datypes.BACnetAction, accessLevel=3, userAccessLevel=1)
    )
    bias: ns0.vartypes.AnalogUnitType | None
    cOV_Increment: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106042", browseName="ns=bacnet;COV_Increment", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
    )
    controlled_Variable_Reference: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106015",
            browseName="ns=bacnet;Controlled_Variable_Reference",
            dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    controlled_Variable_Value: ns0.vartypes.AnalogUnitType
    derivative_Constant: ns0.vartypes.AnalogUnitType | None
    eventReporting: BACnetEventReportingType | None
    faultEvaluation: BACnetFaultEvaluationType | None
    integral_Constant: ns0.vartypes.AnalogUnitType | None
    manipulated_Variable_Reference: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106014",
            browseName="ns=bacnet;Manipulated_Variable_Reference",
            dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    out_Of_Service: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106012", browseName="ns=bacnet;Out_Of_Service", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    present_Value: ns0.vartypes.AnalogUnitType
    priority_For_Writing: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106041", browseName="ns=bacnet;Priority_For_Writing", dataType=o6.Byte, accessLevel=3, userAccessLevel=1)
    )
    proportional_Constant: ns0.vartypes.AnalogUnitType | None
    setpoint: ns0.vartypes.AnalogUnitType
    setpoint_Reference: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106029", browseName="ns=bacnet;Setpoint_Reference", dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference, accessLevel=3, userAccessLevel=1
        )
    )
    status_Flags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6329", browseName="ns=bacnet;Status_Flags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=101003", browseName="ns=bacnet;BACnetChangeOfBitStringAlgorithmType", displayName="BACnetChangeOfBitStringAlgorithmType")
class BACnetChangeOfBitStringAlgorithmType(BACnetEventAlgorithmType):
    alarmValues: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106043", browseName="ns=bacnet;AlarmValues", dataType=ns0.datatypes.OptionSet, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=101004", browseName="ns=bacnet;BACnetChangeOfValueAlgorithmType", displayName="BACnetChangeOfValueAlgorithmType")
class BACnetChangeOfValueAlgorithmType(BACnetEventAlgorithmType):
    bitmask: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106049", browseName="ns=bacnet;Bitmask", dataType=ns0.datatypes.OptionSet, accessLevel=3, userAccessLevel=1)
    )
    increment: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106048", browseName="ns=bacnet;Increment", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=101005", browseName="ns=bacnet;BACnetBufferReadyAlgorithmType", displayName="BACnetBufferReadyAlgorithmType")
class BACnetBufferReadyAlgorithmType(BACnetEventAlgorithmType):
    previousCount: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106051", browseName="ns=bacnet;PreviousCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )
    threshold: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106052", browseName="ns=bacnet;Threshold", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=101024", browseName="ns=bacnet;BACnetObjectTypeUnknown", displayName="BACnetObjectTypeUnknown")
class BACnetObjectTypeUnknown(BACnetObjectType):
    object_Type: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=bacnet;i=106084", browseName="ns=bacnet;Object_Type", dataType=bacnet_datypes.BACnetObjectTypeEnum, accessLevel=3, userAccessLevel=1
        )
    )


@o6.objecttype(nodeId="ns=bacnet;i=101021", browseName="ns=bacnet;BACnetMstpMasterType", displayName="BACnetMstpMasterType")
class BACnetMstpMasterType(ns0.objtypes.BaseObjectType):
    auto_Slave_Discovery: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106114", browseName="ns=bacnet;Auto_Slave_Discovery", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    manual_Slave_Address_Binding: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106113",
            browseName="ns=bacnet;Manual_Slave_Address_Binding",
            dataType=bacnet_datypes.BACnetAddressBinding,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    max_Info_Frames: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106111", browseName="ns=bacnet;Max_Info_Frames", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    max_Master: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106110", browseName="ns=bacnet;Max_Master", dataType=o6.Byte, accessLevel=3, userAccessLevel=1)
    )
    slave_Address_Binding: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106115",
            browseName="ns=bacnet;Slave_Address_Binding",
            dataType=bacnet_datypes.BACnetAddressBinding,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    slave_Proxy_Enable: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106112", browseName="ns=bacnet;Slave_Proxy_Enable", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1011", browseName="ns=bacnet;BACnetDeviceType", displayName="BACnetDeviceType")
class BACnetDeviceType(BACnetObjectType):
    aPDU_Segment_Timeout: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106098", browseName="ns=bacnet;APDU_Segment_Timeout", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    aPDU_Timeout: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106099", browseName="ns=bacnet;APDU_Timeout", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    active_COV_Subscriptions: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106122",
            browseName="ns=bacnet;Active_COV_Subscriptions",
            dataType=bacnet_datypes.BACnetCOVSubscription,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    addDeviceAddressBindings: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=bacnet;i=7024"])
    application_Software_Version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106078", browseName="ns=bacnet;Application_Software_Version", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    backupRestore: BACnetBackupRestoreType | None
    createObject: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=bacnet;i=7013"])
    database_Revision: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106109", browseName="ns=bacnet;Database_Revision", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    deleteObject: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=bacnet;i=7014"])
    deviceCommunicationControl: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=bacnet;i=7015"])
    deviceRestart: BACnetDeviceRestartType | None
    device_Address_Binding: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106108",
            browseName="ns=bacnet;Device_Address_Binding",
            dataType=bacnet_datypes.BACnetAddressBinding,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    firmware_Revision: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106077", browseName="ns=bacnet;Firmware_Revision", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    langleNotifier_Object_NameRangle: BACnetNotifierType | None
    location: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106072", browseName="ns=bacnet;Location", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    max_APDU_Length_Accepted: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106087", browseName="ns=bacnet;Max_APDU_Length_Accepted", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    max_Segments_Accepted: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106088", browseName="ns=bacnet;Max_Segments_Accepted", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    model_Name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106071", browseName="ns=bacnet;Model_Name", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    mstpMaster: BACnetMstpMasterType | None
    number_Of_APDU_Retries: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106100", browseName="ns=bacnet;Number_Of_APDU_Retries", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    object_List: ns0.objtypes.BaseObjectType
    protocol_Object_Types_Supported: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6222",
            browseName="ns=bacnet;Protocol_Object_Types_Supported",
            dataType=bacnet_datypes.BACnetObjectTypeSupportedBits,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    protocol_Revision: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106074", browseName="ns=bacnet;Protocol_Revision", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    protocol_Services_Supported: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6213", browseName="ns=bacnet;Protocol_Services_Supported", dataType=bacnet_datypes.BACnetServicesSupportedBits, accessLevel=3, userAccessLevel=1
        )
    )
    protocol_Version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106073", browseName="ns=bacnet;Protocol_Version", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    reinitializeDevice: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=bacnet;i=7016"])
    removeDeviceAddressBindings: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=bacnet;i=7025"])
    segmentation_Supported: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106085", browseName="ns=bacnet;Segmentation_Supported", dataType=bacnet_datypes.BACnetSegmentation, accessLevel=3, userAccessLevel=1
        )
    )
    serial_Number: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106044", browseName="ns=bacnet;Serial_Number", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    structured_Object_List: ns0.objtypes.BaseObjectType | None
    system_Status: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106068", browseName="ns=bacnet;System_Status", dataType=bacnet_datypes.BACnetDeviceStatus, accessLevel=3, userAccessLevel=1)
    )
    textMessage: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=bacnet;i=7019"])
    timeManagement: BACnetTimeManagementType | None
    vendor_Identifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106070", browseName="ns=bacnet;Vendor_Identifier", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    vendor_Name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106069", browseName="ns=bacnet;Vendor_Name", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


o6.reference(BACnetDeviceType, "i=41", BACnetNotificationType)


@o6.objecttype(nodeId="ns=bacnet;i=1014", browseName="ns=bacnet;BACnetBinaryOutputType", displayName="BACnetBinaryOutputType")
class BACnetBinaryOutputType(BACnetBinaryType):
    device_Type: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6033", browseName="ns=bacnet;Device_Type", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    eventReporting: BACnetEventReportingType | None
    feedback_Value: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6291", browseName="ns=bacnet;Feedback_Value", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    minimum_Off_Time: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6089", browseName="ns=bacnet;Minimum_Off_Time", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )
    minimum_On_Time: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6090", browseName="ns=bacnet;Minimum_On_Time", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )
    polarity: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6102", browseName="ns=bacnet;Polarity", dataType=bacnet_datypes.BACnetPolarity, accessLevel=3, userAccessLevel=1)
    )
    priority_Array: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6088",
            browseName="ns=bacnet;Priority_Array",
            dataType=bacnet_datypes.BACnetPriorityValue,
            valueRank=1,
            arrayDimensions=[16],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    relinquish_Default: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106146", browseName="ns=bacnet;Relinquish_Default", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1015", browseName="ns=bacnet;BACnetBinaryValueType", displayName="BACnetBinaryValueType")
class BACnetBinaryValueType(BACnetBinaryType):
    eventReporting: BACnetEventReportingType | None
    minimum_Off_Time: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6095", browseName="ns=bacnet;Minimum_Off_Time", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )
    minimum_On_Time: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6094", browseName="ns=bacnet;Minimum_On_Time", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )
    priority_Array: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6092",
            browseName="ns=bacnet;Priority_Array",
            dataType=bacnet_datypes.BACnetPriorityValue,
            valueRank=1,
            arrayDimensions=[16],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    relinquish_Default: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106149", browseName="ns=bacnet;Relinquish_Default", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=101009", browseName="ns=bacnet;BACnetFaultCharacterStringAlgorithmType", displayName="BACnetFaultCharacterStringAlgorithmType")
class BACnetFaultCharacterStringAlgorithmType(BACnetFaultAlgorithmType):
    faultValues: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106168", browseName="ns=bacnet;FaultValues", dataType=o6.String, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
        )
    )


@o6.objecttype(nodeId="ns=bacnet;i=101011", browseName="ns=bacnet;BACnetFaultStateAlgorithmType", displayName="BACnetFaultStateAlgorithmType")
class BACnetFaultStateAlgorithmType(BACnetFaultAlgorithmType):
    faultValues: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106172", browseName="ns=bacnet;FaultValues", valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=101014", browseName="ns=bacnet;BACnetLogType", displayName="BACnetLogType", isAbstract=True)
class BACnetLogType(BACnetObjectType):
    buffer_Size: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106211", browseName="ns=bacnet;Buffer_Size", dataType=o6.UInt32))
    enable: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106206", browseName="ns=bacnet;Enable", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    eventReporting: BACnetEventReportingType
    faultEvaluation: BACnetFaultEvaluationType
    record_Count: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106213", browseName="ns=bacnet;Record_Count", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )
    records_Since_Notification: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106284", browseName="ns=bacnet;Records_Since_Notification", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )
    start_Time: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106208", browseName="ns=bacnet;Start_Time", dataType=bacnet_datypes.BACnetDateTime, accessLevel=3, userAccessLevel=1)
    )
    status_Flags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6333", browseName="ns=bacnet;Status_Flags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )
    stop_Time: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106209", browseName="ns=bacnet;Stop_Time", dataType=bacnet_datypes.BACnetDateTime, accessLevel=3, userAccessLevel=1)
    )
    stop_When_Full: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106210", browseName="ns=bacnet;Stop_When_Full", dataType=o6.Boolean))
    total_Record_Count: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106214", browseName="ns=bacnet;Total_Record_Count", dataType=o6.UInt32)
    )


@o6.objecttype(nodeId="ns=bacnet;i=101018", browseName="ns=bacnet;BACnetEventLogType", displayName="BACnetEventLogType")
class BACnetEventLogType(BACnetLogType):
    pass


@o6.objecttype(nodeId="ns=bacnet;i=101026", browseName="ns=bacnet;BACnetTrendLogBaseType", displayName="BACnetTrendLogBaseType", isAbstract=True)
class BACnetTrendLogBaseType(BACnetLogType):
    align_Intervals: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6334", browseName="ns=bacnet;Align_Intervals", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    interval_Offset: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6335", browseName="ns=bacnet;Interval_Offset", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    log_Interval: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6336", browseName="ns=bacnet;Log_Interval", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    logging_Type: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6337", browseName="ns=bacnet;Logging_Type", dataType=bacnet_datypes.BACnetLoggingType, accessLevel=3, userAccessLevel=1)
    )
    trigger: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6338", browseName="ns=bacnet;Trigger", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=101017", browseName="ns=bacnet;BACnetTrendLogType", displayName="BACnetTrendLogType")
class BACnetTrendLogType(BACnetTrendLogBaseType):
    cOV_Resubscription_Interval: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106244", browseName="ns=bacnet;COV_Resubscription_Interval", dataType=ns0.datatypes.UInteger)
    )
    client_COV_Increment: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106228",
            browseName="ns=bacnet;Client_COV_Increment",
            dataType=bacnet_datypes.BACnetClientCOV,
            value=bacnet_datypes.BACnetClientCOV(real_increment=0.0),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    log_Buffer: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=bacnet;i=6339", browseName="ns=bacnet;Log_Buffer", accessLevel=3, userAccessLevel=1)
    )
    log_DeviceObjectProperty: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106245",
            browseName="ns=bacnet;Log_DeviceObjectProperty",
            dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=bacnet;i=101015", browseName="ns=bacnet;BACnetClockAlignedTrendLogType", displayName="BACnetClockAlignedTrendLogType")
class BACnetClockAlignedTrendLogType(BACnetTrendLogType):
    align_Interval: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106216", browseName="ns=bacnet;Align_Interval", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    interval_Offset: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106217", browseName="ns=bacnet;Interval_Offset", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    log_Interval: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106207", browseName="ns=bacnet;Log_Interval", dataType=ns0.datatypes.UInteger)
    )


@o6.objecttype(nodeId="ns=bacnet;i=101027", browseName="ns=bacnet;BACnetTrendLogMultipleType", displayName="BACnetTrendLogMultipleType")
class BACnetTrendLogMultipleType(BACnetTrendLogBaseType):
    log_Buffer: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=bacnet;i=106291", browseName="ns=bacnet;Log_Buffer", valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1)
    )
    log_DeviceObjectProperty: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6340",
            browseName="ns=bacnet;Log_DeviceObjectProperty",
            dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=bacnet;i=1003", browseName="ns=bacnet;BACnetEventReportingType", displayName="BACnetEventReportingType")
class BACnetEventReportingType(ns0.objtypes.BaseObjectType):
    acked_Transitions: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6053", browseName="ns=bacnet;Acked_Transitions", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
        )
    )
    eventAlgorithm: BACnetEventAlgorithmType | None
    event_Algorithm_Inhibit: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106304", browseName="ns=bacnet;Event_Algorithm_Inhibit", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    event_Algorithm_Inhibit_Ref: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106303",
            browseName="ns=bacnet;Event_Algorithm_Inhibit_Ref",
            dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    event_Detection_Enable: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106302", browseName="ns=bacnet;Event_Detection_Enable", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    event_Enable: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6052", browseName="ns=bacnet;Event_Enable", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
        )
    )
    event_Message_Texts: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6064", browseName="ns=bacnet;Event_Message_Texts", dataType=o6.String, valueRank=1, arrayDimensions=[3], accessLevel=3, userAccessLevel=1
        )
    )
    event_Message_Texts_Config: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106063", browseName="ns=bacnet;Event_Message_Texts_Config", dataType=o6.String, valueRank=1, arrayDimensions=[3], accessLevel=3, userAccessLevel=1
        )
    )
    event_State: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6007",
            browseName="ns=bacnet;Event_State",
            dataType=bacnet_datypes.BACnetEventState,
            value=bacnet_datypes.BACnetEventState.NORMAL,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    event_Time_Stamps: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6059",
            browseName="ns=bacnet;Event_Time_Stamps",
            dataType=bacnet_datypes.BACnetTimeStamp,
            valueRank=1,
            arrayDimensions=[3],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    notification_Class: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6050", browseName="ns=bacnet;Notification_Class", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )
    notify_Type: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6091", browseName="ns=bacnet;Notify_Type", dataType=bacnet_datypes.BACnetNotifyType, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=101016", browseName="ns=bacnet;BACnetIntrinsicReportingTrendLogType", displayName="BACnetIntrinsicReportingTrendLogType")
class BACnetIntrinsicReportingTrendLogType(BACnetEventReportingType):
    recorded_Since_Notification: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106232", browseName="ns=bacnet;Recorded_Since_Notification", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=101028", browseName="ns=bacnet;BACnetChangeOfLifeSafetyAlgorithmType", displayName="BACnetChangeOfLifeSafetyAlgorithmType")
class BACnetChangeOfLifeSafetyAlgorithmType(BACnetEventAlgorithmType):
    alarmValues: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=bacnet;i=106311",
            browseName="ns=bacnet;AlarmValues",
            dataType=bacnet_datypes.BACnetLifeSafetyState,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    lifeSafetyAlarmValues: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=bacnet;i=106312",
            browseName="ns=bacnet;LifeSafetyAlarmValues",
            dataType=bacnet_datypes.BACnetLifeSafetyState,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=bacnet;i=101002", browseName="ns=bacnet;BACnetFloatingLimitAlgorithmType", displayName="BACnetFloatingLimitAlgorithmType")
class BACnetFloatingLimitAlgorithmType(BACnetEventAlgorithmType):
    deadband: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106326", browseName="ns=bacnet;Deadband", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
    )
    highDiffLimit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106325", browseName="ns=bacnet;HighDiffLimit", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
    )
    lowDiffLimit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106045", browseName="ns=bacnet;LowDiffLimit", dataType=o6.Float, accessLevel=3, userAccessLevel=1)
    )
    setpointReference: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106046", browseName="ns=bacnet;SetpointReference", dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference, accessLevel=3, userAccessLevel=1
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6346",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=107001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Time", dataType=ns0.datatypes.UtcTime, valueRank=-1)],
)
o6.call(nodeId="ns=bacnet;i=107001", browseName="ns=bacnet;TimeSynchronization", inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6346"]))


@o6.objecttype(nodeId="ns=bacnet;i=101019", browseName="ns=bacnet;BACnetTimeManagementType", displayName="BACnetTimeManagementType")
class BACnetTimeManagementType(ns0.objtypes.BaseObjectType):
    daylight_Savings_Status: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106248", browseName="ns=bacnet;Daylight_Savings_Status", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    local_Date: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106215",
            browseName="ns=bacnet;Local_Date",
            dataType=bacnet_datypes.BACnetDate,
            value=bacnet_datypes.BACnetDate(
                year=0, month=bacnet_datypes.BACnetMonth.JANUARY, dayOfMonth=bacnet_datypes.BACnetDayOfMonth(11), dayOfWeek=bacnet_datypes.BACnetDayOfWeek.MONDAY
            ),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    local_Time: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106218", browseName="ns=bacnet;Local_Time", dataType=bacnet_datypes.BACnetTime, accessLevel=3, userAccessLevel=1)
    )
    timeSynchronization: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=bacnet;i=107001"])
    uTC_Offset: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106242", browseName="ns=bacnet;UTC_Offset", dataType=o6.Int16, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=bacnet;i=1052", browseName="ns=bacnet;BACnetAutomaticTimeSynchronizationMasterType", displayName="BACnetAutomaticTimeSynchronizationMasterType")
class BACnetAutomaticTimeSynchronizationMasterType(BACnetTimeManagementType):
    addTimeSynchronizationRecipients: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=bacnet;i=7027"])
    align_Intervals: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6351", browseName="ns=bacnet;Align_Intervals", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    interval_Offset: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6352", browseName="ns=bacnet;Interval_Offset", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    removeTimeSynchronizationRecipients: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=bacnet;i=7028"])
    time_Synchronization_Interval: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6350", browseName="ns=bacnet;Time_Synchronization_Interval", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1
        )
    )
    time_Synchronization_Recipients: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6348",
            browseName="ns=bacnet;Time_Synchronization_Recipients",
            dataType=bacnet_datypes.BACnetRecipient,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    uTC_Time_Synchronization_Recipients: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=6349",
            browseName="ns=bacnet;UTC_Time_Synchronization_Recipients",
            dataType=bacnet_datypes.BACnetRecipient,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=bacnet;i=101020", browseName="ns=bacnet;BACnetBackupRestoreType", displayName="BACnetBackupRestoreType")
class BACnetBackupRestoreType(ns0.objtypes.BaseObjectType):
    bACnetBackup: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="ns=bacnet;i=107004", browseName="ns=bacnet;BACnetBackup"))
    bACnetRestore: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="ns=bacnet;i=107005", browseName="ns=bacnet;BACnetRestore"))
    backup_And_Restore_State: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106251", browseName="ns=bacnet;Backup_And_Restore_State", dataType=bacnet_datypes.BACnetBackupState, accessLevel=3, userAccessLevel=1
        )
    )
    backup_Failure_Timeout: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106132", browseName="ns=bacnet;Backup_Failure_Timeout", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    backup_Preparation_Time: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106133", browseName="ns=bacnet;Backup_Preparation_Time", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    configuration_Files: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106101",
            browseName="ns=bacnet;Configuration_Files",
            dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference,
            valueRank=1,
            arrayDimensions=[1],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    last_Restore_Time: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106131",
            browseName="ns=bacnet;Last_Restore_Time",
            dataType=bacnet_datypes.BACnetTimeStamp,
            value=bacnet_datypes.BACnetTimeStamp(
                time=bacnet_datypes.BACnetTime(hour=0, minute=0, second=0, hundredths=0),
                sequenceNumber=0,
                dateTime=bacnet_datypes.BACnetDateTime(
                    date=bacnet_datypes.BACnetDate(
                        year=0, month=bacnet_datypes.BACnetMonth(0), dayOfMonth=bacnet_datypes.BACnetDayOfMonth(0), dayOfWeek=bacnet_datypes.BACnetDayOfWeek(0)
                    ),
                    time=bacnet_datypes.BACnetTime(hour=0, minute=0, second=0, hundredths=0),
                ),
            ),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    restore_Completion_Time: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106250", browseName="ns=bacnet;Restore_Completion_Time", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    restore_Preparation_Time: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106134", browseName="ns=bacnet;Restore_Preparation_Time", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6108",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=107006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RestartNotificationRecipients", dataType=bacnet_datypes.BACnetRecipient, valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6137",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=107006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FirstFailedElementNumber", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=bacnet;i=107006",
    browseName="ns=bacnet;AddRestartRecipients",
    inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6108"]),
    outputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6137"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6141",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=107007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FirstFailedElementNumber", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6147",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=107007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RestartNotificationRecipients", dataType=bacnet_datypes.BACnetRecipient, valueRank=1, arrayDimensions=[0])],
)
o6.call(
    nodeId="ns=bacnet;i=107007",
    browseName="ns=bacnet;RemoveRestartRecipients",
    inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6147"]),
    outputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6141"]),
)


@o6.objecttype(nodeId="ns=bacnet;i=101022", browseName="ns=bacnet;BACnetDeviceRestartType", displayName="BACnetDeviceRestartType")
class BACnetDeviceRestartType(ns0.objtypes.BaseObjectType):
    addRestartRecipients: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=bacnet;i=107006"])
    last_Restart_Reason: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106104", browseName="ns=bacnet;Last_Restart_Reason", dataType=bacnet_datypes.BACnetRestartReason, accessLevel=3, userAccessLevel=1
        )
    )
    removeRestartRecipients: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=bacnet;i=107007"])
    restart_Notification_Recipients: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106117",
            browseName="ns=bacnet;Restart_Notification_Recipients",
            dataType=bacnet_datypes.BACnetRecipient,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    time_Of_Device_Restart: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106105",
            browseName="ns=bacnet;Time_Of_Device_Restart",
            dataType=bacnet_datypes.BACnetTimeStamp,
            value=bacnet_datypes.BACnetTimeStamp(
                time=bacnet_datypes.BACnetTime(hour=0, minute=0, second=0, hundredths=0),
                sequenceNumber=0,
                dateTime=bacnet_datypes.BACnetDateTime(
                    date=bacnet_datypes.BACnetDate(
                        year=0, month=bacnet_datypes.BACnetMonth(0), dayOfMonth=bacnet_datypes.BACnetDayOfMonth(0), dayOfWeek=bacnet_datypes.BACnetDayOfWeek(0)
                    ),
                    time=bacnet_datypes.BACnetTime(hour=0, minute=0, second=0, hundredths=0),
                ),
            ),
            accessLevel=3,
            userAccessLevel=1,
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6323",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=107014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DeviceObjectPropertyReferences", dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference, valueRank=1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6324",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=107014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FirstFailedElementNumber", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=bacnet;i=107014",
    browseName="ns=bacnet;AddObjectPropertyReferences",
    inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6323"]),
    outputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6324"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6325",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=107015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DeviceObjectPropertyReferences", dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference, valueRank=1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6326",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=107015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FirstFailedElementNumber", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=bacnet;i=107015",
    browseName="ns=bacnet;RemoveObjectPropertyReferences",
    inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6325"]),
    outputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6326"]),
)


@o6.objecttype(nodeId="ns=bacnet;i=1022", browseName="ns=bacnet;BACnetScheduleType", displayName="BACnetScheduleType")
class BACnetScheduleType(BACnetObjectType):
    addObjectPropertyReferences: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=bacnet;i=107014"])
    effective_Period: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6182", browseName="ns=bacnet;Effective_Period", dataType=bacnet_datypes.BACnetDateRange, accessLevel=3, userAccessLevel=1)
    )
    eventReporting: BACnetEventReportingType | None
    exception_Schedule: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106003",
            browseName="ns=bacnet;Exception_Schedule",
            dataType=bacnet_datypes.BACnetSpecialEvent,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    faultEvaluation: BACnetFaultEvaluationType | None
    list_Of_Object_Property_References: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106004",
            browseName="ns=bacnet;List_Of_Object_Property_References",
            dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    out_Of_Service: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6175", browseName="ns=bacnet;Out_Of_Service", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    present_Value: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=bacnet;i=6128", browseName="ns=bacnet;Present_Value", accessLevel=3, userAccessLevel=1)
    )
    priority_For_Writing: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6130", browseName="ns=bacnet;Priority_For_Writing", dataType=o6.Byte, accessLevel=3, userAccessLevel=1)
    )
    removeObjectPropertyReferences: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=bacnet;i=107015"])
    schedule_Default: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=bacnet;i=6321", browseName="ns=bacnet;Schedule_Default", accessLevel=3, userAccessLevel=1)
    )
    status_Flags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6176", browseName="ns=bacnet;Status_Flags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )
    weekly_Schedule: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106002",
            browseName="ns=bacnet;Weekly_Schedule",
            dataType=bacnet_datypes.BACnetDailySchedule,
            valueRank=1,
            arrayDimensions=[7],
            accessLevel=3,
            userAccessLevel=1,
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6331",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=107016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="EventParameters", dataType=bacnet_datypes.BACnetEventParameter, valueRank=-1)],
)
o6.call(nodeId="ns=bacnet;i=107016", browseName="ns=bacnet;SetEventAlgorithm", inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6331"]))

ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6332",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=107017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FaultParameters", dataType=bacnet_datypes.BACnetFaultParameter, valueRank=-1)],
)
o6.call(nodeId="ns=bacnet;i=107017", browseName="ns=bacnet;SetFaultAlgorithm", inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6332"]))


@o6.objecttype(nodeId="ns=bacnet;i=101006", browseName="ns=bacnet;BACnetEventEnrollmentType", displayName="BACnetEventEnrollmentType")
class BACnetEventEnrollmentType(BACnetObjectType):
    eventReporting: BACnetEventReportingType
    event_State: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106062", browseName="ns=bacnet;Event_State", dataType=bacnet_datypes.BACnetEventState, accessLevel=3, userAccessLevel=1)
    )
    event_Type: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106053", browseName="ns=bacnet;Event_Type", dataType=bacnet_datypes.BACnetEventType, accessLevel=3, userAccessLevel=1)
    )
    faultEvaluation: BACnetFaultEvaluationType
    fault_Type: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106079", browseName="ns=bacnet;Fault_Type", dataType=bacnet_datypes.BACnetFaultType, accessLevel=3, userAccessLevel=1)
    )
    object_Property_Reference: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=bacnet;i=106061",
            browseName="ns=bacnet;Object_Property_Reference",
            dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    setEventAlgorithm: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=bacnet;i=107016"])
    setFaultAlgorithm: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=bacnet;i=107017"])
    status_Flags: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6330", browseName="ns=bacnet;Status_Flags", dataType=bacnet_datypes.BACnetStatusFlags, accessLevel=3, userAccessLevel=1)
    )


del Any, TYPE_CHECKING, uuid, o6, ns0, bacnet_datypes, bacnet_vartypes
