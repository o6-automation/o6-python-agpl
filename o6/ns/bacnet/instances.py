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
from . import objtypes as bacnet_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5002", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5003", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetCalendarEntry, o6.ns["ns=bacnet;i=5003"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5005", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5006", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetDateTime, o6.ns["ns=bacnet;i=5006"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5010", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5011", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5012", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetClientCOV, o6.ns["ns=bacnet;i=5012"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5013", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5014", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetWeekNDay, o6.ns["ns=bacnet;i=5014"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5015", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5016", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetEventParameter, o6.ns["ns=bacnet;i=5016"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5017", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5018", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetDateRange, o6.ns["ns=bacnet;i=5018"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5019", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5020", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetDate, o6.ns["ns=bacnet;i=5020"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5021", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5022", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetTime, o6.ns["ns=bacnet;i=5022"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5023", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5024", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5025", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetFaultParameter, o6.ns["ns=bacnet;i=5025"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5027", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterChangeOfLifeSafety, o6.ns["ns=bacnet;i=5027"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5028", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5029", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetMessageClass, o6.ns["ns=bacnet;i=5029"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5030", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5031", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetPriorityValue, o6.ns["ns=bacnet;i=5031"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5032", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5033", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetRecipient, o6.ns["ns=bacnet;i=5033"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5034", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5035", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetSpecialEventPeriod, o6.ns["ns=bacnet;i=5035"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5041", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5042", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetAddress, o6.ns["ns=bacnet;i=5042"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5045", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetAddress, o6.ns["ns=bacnet;i=5045"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5046", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetAddressBinding, o6.ns["ns=bacnet;i=5046"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5047", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5048", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetPropertyStates, o6.ns["ns=bacnet;i=5048"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5049", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetCOVSubscription, o6.ns["ns=bacnet;i=5049"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5050", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetDailySchedule, o6.ns["ns=bacnet;i=5050"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5051", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetDate, o6.ns["ns=bacnet;i=5051"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5052", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetDateRange, o6.ns["ns=bacnet;i=5052"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5053", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetDateTime, o6.ns["ns=bacnet;i=5053"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5054", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetDestination, o6.ns["ns=bacnet;i=5054"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5055", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetDeviceObjectPropertyReference, o6.ns["ns=bacnet;i=5055"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5056", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetEventFaultParameterExtended, o6.ns["ns=bacnet;i=5056"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5057", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterBufferReady, o6.ns["ns=bacnet;i=5057"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5058", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterChangeOfBitstring, o6.ns["ns=bacnet;i=5058"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5059", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterChangeOfCharacterString, o6.ns["ns=bacnet;i=5059"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5060", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterChangeOfLifeSafety, o6.ns["ns=bacnet;i=5060"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5061", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterChangeOfState, o6.ns["ns=bacnet;i=5061"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5062", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterChangeOfValue, o6.ns["ns=bacnet;i=5062"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5063", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterDoubleOutOfRange, o6.ns["ns=bacnet;i=5063"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5064", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5065", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterCommandFailure, o6.ns["ns=bacnet;i=5065"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5066", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterDoubleOutOfRange, o6.ns["ns=bacnet;i=5066"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5067", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterFloatingLimit, o6.ns["ns=bacnet;i=5067"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5068", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterOutOfRange, o6.ns["ns=bacnet;i=5068"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5069", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5070", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetTimeStamp, o6.ns["ns=bacnet;i=5070"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5080", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterSignedOutOfRange, o6.ns["ns=bacnet;i=5080"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5081", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5082", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterChangeOfCharacterString, o6.ns["ns=bacnet;i=5082"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5083", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5084", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterUnsignedRange, o6.ns["ns=bacnet;i=5084"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5085", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5086", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterExtendedParameters, o6.ns["ns=bacnet;i=5086"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5087", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterSignedOutOfRange, o6.ns["ns=bacnet;i=5087"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5088", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterUnsignedOutOfRange, o6.ns["ns=bacnet;i=5088"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5089", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterUnsignedRange, o6.ns["ns=bacnet;i=5089"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5090", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetFaultParameterFaultCharacterstring, o6.ns["ns=bacnet;i=5090"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5091", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetFaultParameterFaultLifeSafety, o6.ns["ns=bacnet;i=5091"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5092", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetFaultParameterFaultState, o6.ns["ns=bacnet;i=5092"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5093", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetFaultParameterFaultStatusFlags, o6.ns["ns=bacnet;i=5093"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5094", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetPropertyStates, o6.ns["ns=bacnet;i=5094"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5095", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetRecipientProcess, o6.ns["ns=bacnet;i=5095"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5096", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetSpecialEvent, o6.ns["ns=bacnet;i=5096"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5097", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetTime, o6.ns["ns=bacnet;i=5097"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5098", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetTimeValue, o6.ns["ns=bacnet;i=5098"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5099", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetTimeValueValue, o6.ns["ns=bacnet;i=5099"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5100", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetWeekNDay, o6.ns["ns=bacnet;i=5100"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5101", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetDaysOfWeek, o6.ns["ns=bacnet;i=5101"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5102", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetEventTransitionBits, o6.ns["ns=bacnet;i=5102"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5103", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetLimitEnable, o6.ns["ns=bacnet;i=5103"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5104", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetObjectTypeSupportedBits, o6.ns["ns=bacnet;i=5104"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5105", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetServicesSupportedBits, o6.ns["ns=bacnet;i=5105"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5106", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetStatusFlags, o6.ns["ns=bacnet;i=5106"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5107", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetCalendarEntry, o6.ns["ns=bacnet;i=5107"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5108", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetClientCOV, o6.ns["ns=bacnet;i=5108"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5109", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetEventParameter, o6.ns["ns=bacnet;i=5109"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5110", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterExtendedParameters, o6.ns["ns=bacnet;i=5110"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5111", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetFaultParameter, o6.ns["ns=bacnet;i=5111"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5112", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetMessageClass, o6.ns["ns=bacnet;i=5112"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5113", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetPriorityValue, o6.ns["ns=bacnet;i=5113"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5114", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetRecipient, o6.ns["ns=bacnet;i=5114"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5115", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetSpecialEventPeriod, o6.ns["ns=bacnet;i=5115"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5116", browseName="Default JSON")
o6.hasEncoding(bacnet_datypes.BACnetTimeStamp, o6.ns["ns=bacnet;i=5116"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5125", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5127", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetDaysOfWeek, o6.ns["ns=bacnet;i=5127"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5129", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5130", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetEventTransitionBits, o6.ns["ns=bacnet;i=5130"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5131", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5132", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetLimitEnable, o6.ns["ns=bacnet;i=5132"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5133", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5134", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetObjectTypeSupportedBits, o6.ns["ns=bacnet;i=5134"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5135", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5136", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetServicesSupportedBits, o6.ns["ns=bacnet;i=5136"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5146", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=5147", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetStatusFlags, o6.ns["ns=bacnet;i=5147"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=bacnet;i=6002",
    browseName="ns=bacnet;Present_Value",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6003", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(bacnet_objtypes.BACnetAnalogType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=6002"])
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6008",
    browseName="EnumStrings",
    parent="ns=bacnet;i=3005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("Inactive"), o6.LocalizedText("Active")],
)
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=bacnet;i=6019",
    browseName="ns=bacnet;Present_Value",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6020", browseName="FalseState", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6021", browseName="TrueState", dataType=o6.LocalizedText)),
    ],
    dataType=o6.Boolean,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(bacnet_objtypes.BACnetBinaryType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=6019"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=bacnet;i=6025",
    browseName="ns=bacnet;Present_Value",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6027", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(bacnet_objtypes.BACnetLoopType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=6025"])
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6044",
    browseName="EnumStrings",
    parent="ns=bacnet;i=3045",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[12],
    value=[
        o6.LocalizedText("UNKNOWN"),
        o6.LocalizedText("SYSTEM"),
        o6.LocalizedText("NETWORK"),
        o6.LocalizedText("DEVICE"),
        o6.LocalizedText("ORGANIZATIONAL"),
        o6.LocalizedText("AREA"),
        o6.LocalizedText("EQUIPMENT"),
        o6.LocalizedText("POINT"),
        o6.LocalizedText("COLLECTION"),
        o6.LocalizedText("PROPERTY"),
        o6.LocalizedText("FUNCTIONAL"),
        o6.LocalizedText("OTHER"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6054",
    browseName="EnumStrings",
    parent="ns=bacnet;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("Alarm"), o6.LocalizedText("Event"), o6.LocalizedText("AckNotification")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6055",
    browseName="EnumStrings",
    parent="ns=bacnet;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        o6.LocalizedText("Normal"),
        o6.LocalizedText("Fault"),
        o6.LocalizedText("OffNormal"),
        o6.LocalizedText("HighLimit"),
        o6.LocalizedText("LowLimit"),
        o6.LocalizedText("LifeSafetyAlarm"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6097",
    browseName="EnumStrings",
    parent="ns=bacnet;i=3007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("Normal"), o6.LocalizedText("Reverse")],
)
ns0.vartypes.MultiStateDiscreteType(
    nodeId="ns=bacnet;i=6106",
    browseName="ns=bacnet;Present_Value",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6107", browseName="EnumStrings", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0]))],
    dataType=ns0.datatypes.UInteger,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(bacnet_objtypes.BACnetMultiStateType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=6106"])
bacnet_objtypes.BACnetEventReportingType(
    nodeId="ns=bacnet;i=5009",
    browseName="ns=bacnet;EventReporting",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6105", browseName="ns=bacnet;Acked_Transitions", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6116", browseName="ns=bacnet;Event_Enable", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6117",
                browseName="ns=bacnet;Event_State",
                dataType=bacnet_datypes.BACnetEventState,
                value=bacnet_datypes.BACnetEventState.NORMAL,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6118",
                browseName="ns=bacnet;Event_Time_Stamps",
                dataType=bacnet_datypes.BACnetTimeStamp,
                valueRank=1,
                arrayDimensions=[3],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6119", browseName="ns=bacnet;Notification_Class", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6120", browseName="ns=bacnet;Notify_Type", dataType=bacnet_datypes.BACnetNotifyType, accessLevel=3, userAccessLevel=1)
        ),
    ],
)
o6.reference(bacnet_objtypes.BACnetMultiStateType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=5009"])
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6121",
    browseName="EnumStrings",
    parent="ns=bacnet;i=3008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("direct"), o6.LocalizedText("reverse")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6151",
    browseName="EnumStrings",
    parent="ns=bacnet;i=3030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[6],
    value=[o6.LocalizedText("Ready"), o6.LocalizedText("Load"), o6.LocalizedText("Run"), o6.LocalizedText("Halt"), o6.LocalizedText("Restart"), o6.LocalizedText("Unload")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6152",
    browseName="EnumValues",
    parent="ns=bacnet;i=3029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[10],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("ChangeOfBitstring")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("ChangeOfState")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("ChangeOfValue")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("CommandFailure")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("FloatingLimit")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("OutOfRange")),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("ChangeOfLifeSafety")),
        ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("Extended")),
        ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("BufferReady")),
        ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("UnsignedRange")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6153",
    browseName="EnumStrings",
    parent="ns=bacnet;i=3031",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        o6.LocalizedText("Idle"),
        o6.LocalizedText("Loading"),
        o6.LocalizedText("Running"),
        o6.LocalizedText("Waiting"),
        o6.LocalizedText("Halted"),
        o6.LocalizedText("Unloading"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6154",
    browseName="EnumStrings",
    parent="ns=bacnet;i=3032",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[5],
    value=[o6.LocalizedText("Normal"), o6.LocalizedText("LoadFailed"), o6.LocalizedText("Internal"), o6.LocalizedText("Program"), o6.LocalizedText("Other")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6155",
    browseName="EnumStrings",
    parent="ns=bacnet;i=3033",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        o6.LocalizedText("Operational"),
        o6.LocalizedText("OperationalReadOnly"),
        o6.LocalizedText("DownloadRequired"),
        o6.LocalizedText("DownloadInProgress"),
        o6.LocalizedText("NonOperational"),
        o6.LocalizedText("BackupInProgress"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6159",
    browseName="EnumValues",
    parent="ns=bacnet;i=3025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[35],
    value=[
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("1")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("2")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("3")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("4")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("5")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("6")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("7")),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("8")),
        ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("9")),
        ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("10")),
        ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("11")),
        ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("12")),
        ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("13")),
        ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("14")),
        ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("15")),
        ns0.datatypes.EnumValueType(value=16, displayName=o6.LocalizedText("16")),
        ns0.datatypes.EnumValueType(value=17, displayName=o6.LocalizedText("17")),
        ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("18")),
        ns0.datatypes.EnumValueType(value=19, displayName=o6.LocalizedText("19")),
        ns0.datatypes.EnumValueType(value=20, displayName=o6.LocalizedText("20")),
        ns0.datatypes.EnumValueType(value=21, displayName=o6.LocalizedText("21")),
        ns0.datatypes.EnumValueType(value=22, displayName=o6.LocalizedText("22")),
        ns0.datatypes.EnumValueType(value=23, displayName=o6.LocalizedText("23")),
        ns0.datatypes.EnumValueType(value=24, displayName=o6.LocalizedText("24")),
        ns0.datatypes.EnumValueType(value=25, displayName=o6.LocalizedText("25")),
        ns0.datatypes.EnumValueType(value=26, displayName=o6.LocalizedText("26")),
        ns0.datatypes.EnumValueType(value=27, displayName=o6.LocalizedText("27")),
        ns0.datatypes.EnumValueType(value=28, displayName=o6.LocalizedText("28")),
        ns0.datatypes.EnumValueType(value=29, displayName=o6.LocalizedText("29")),
        ns0.datatypes.EnumValueType(value=30, displayName=o6.LocalizedText("30")),
        ns0.datatypes.EnumValueType(value=31, displayName=o6.LocalizedText("31")),
        ns0.datatypes.EnumValueType(value=32, displayName=o6.LocalizedText("Last day of month")),
        ns0.datatypes.EnumValueType(value=33, displayName=o6.LocalizedText("Odd day of month")),
        ns0.datatypes.EnumValueType(value=34, displayName=o6.LocalizedText("Even day of month")),
        ns0.datatypes.EnumValueType(value=255, displayName=o6.LocalizedText("Unspecified")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6160",
    browseName="EnumStrings",
    parent="ns=bacnet;i=3035",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[15],
    value=[
        o6.LocalizedText("Off"),
        o6.LocalizedText("On"),
        o6.LocalizedText("Test"),
        o6.LocalizedText("Manned"),
        o6.LocalizedText("UnManned"),
        o6.LocalizedText("Armed"),
        o6.LocalizedText("Disarmed"),
        o6.LocalizedText("Prearmed"),
        o6.LocalizedText("Slow"),
        o6.LocalizedText("Fast"),
        o6.LocalizedText("Disconnected"),
        o6.LocalizedText("Enabled"),
        o6.LocalizedText("Disabled"),
        o6.LocalizedText("AutomaticReleaseDisabled"),
        o6.LocalizedText("Default"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6161",
    browseName="EnumStrings",
    parent="ns=bacnet;i=3036",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[24],
    value=[
        o6.LocalizedText("Quiet"),
        o6.LocalizedText("PreAlarm"),
        o6.LocalizedText("Alarm"),
        o6.LocalizedText("Fault"),
        o6.LocalizedText("FaultPreAlarm"),
        o6.LocalizedText("FaultAlarm"),
        o6.LocalizedText("NotReady"),
        o6.LocalizedText("Active"),
        o6.LocalizedText("Tamper"),
        o6.LocalizedText("TestAlarm"),
        o6.LocalizedText("TestActive"),
        o6.LocalizedText("TestFault"),
        o6.LocalizedText("TestFaultAlarm"),
        o6.LocalizedText("Holdup"),
        o6.LocalizedText("Duress"),
        o6.LocalizedText("TamperAlarm"),
        o6.LocalizedText("Abnormal"),
        o6.LocalizedText("EmergencyPower"),
        o6.LocalizedText("Delayed"),
        o6.LocalizedText("Blocked"),
        o6.LocalizedText("LocalAlarm"),
        o6.LocalizedText("GeneralAlarm"),
        o6.LocalizedText("Supervisory"),
        o6.LocalizedText("TestSupervisory"),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6163", browseName="ns=bacnet;BACnetAddress", dataType=o6.String, value="BACnetAddress")
o6.reference(o6.ns["ns=bacnet;i=5041"], "i=39", o6.ns["ns=bacnet;i=6163"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6164", browseName="ns=bacnet;BACnetAddress", dataType=o6.String, value="//xs:element[@name='BACnetAddress']")
o6.reference(o6.ns["ns=bacnet;i=5042"], "i=39", o6.ns["ns=bacnet;i=6164"])
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6165",
    browseName="EnumValues",
    parent="ns=bacnet;i=3021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("days numbered 1-7")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("days numbered 8-14")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("days numbered 15-21")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("days numbered 22-28")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("days numbered 29-31")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("last 7 days of this month")),
        ns0.datatypes.EnumValueType(value=255, displayName=o6.LocalizedText("any week of this month")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6166",
    browseName="EnumStrings",
    parent="ns=bacnet;i=3018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("Enable"), o6.LocalizedText("Disable"), o6.LocalizedText("DisableInitiation")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6167",
    browseName="EnumValues",
    parent="ns=bacnet;i=3014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[15],
    value=[
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("January")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("February")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("March")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("April")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("May")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("June")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("July")),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("August")),
        ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("September")),
        ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("October")),
        ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("November")),
        ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("December")),
        ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("Odd")),
        ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("Even")),
        ns0.datatypes.EnumValueType(value=255, displayName=o6.LocalizedText("Unspecified")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6168",
    browseName="EnumStrings",
    parent="ns=bacnet;i=3049",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        o6.LocalizedText("Coldstart"),
        o6.LocalizedText("Warmstart"),
        o6.LocalizedText("Startbackup"),
        o6.LocalizedText("Endbackup"),
        o6.LocalizedText("Startrestore"),
        o6.LocalizedText("Endrestore"),
        o6.LocalizedText("Abortrestore"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6169",
    browseName="OptionSetValues",
    parent="ns=bacnet;i=3060",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        o6.LocalizedText("monday"),
        o6.LocalizedText("tuesday"),
        o6.LocalizedText("wednesday"),
        o6.LocalizedText("thursday"),
        o6.LocalizedText("friday"),
        o6.LocalizedText("saturday"),
        o6.LocalizedText("sunday"),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6170", browseName="ns=bacnet;BACnetAddressBinding", dataType=o6.String, value="BACnetAddressBinding")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6171", browseName="ns=bacnet;BACnetAddressBinding", dataType=o6.String, value="//xs:element[@name='BACnetAddressBinding']")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6172", browseName="ns=bacnet;BACnetCOVSubscription", dataType=o6.String, value="BACnetCOVSubscription")
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6173", browseName="ns=bacnet;BACnetCOVSubscription", dataType=o6.String, value="//xs:element[@name='BACnetCOVSubscription']"
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6174", browseName="ns=bacnet;BACnetDailySchedule", dataType=o6.String, value="BACnetDailySchedule")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6177", browseName="ns=bacnet;BACnetDailySchedule", dataType=o6.String, value="//xs:element[@name='BACnetDailySchedule']")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6178", browseName="ns=bacnet;BACnetDate", dataType=o6.String, value="BACnetDate")
o6.reference(o6.ns["ns=bacnet;i=5019"], "i=39", o6.ns["ns=bacnet;i=6178"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6179", browseName="ns=bacnet;BACnetDate", dataType=o6.String, value="//xs:element[@name='BACnetDate']")
o6.reference(o6.ns["ns=bacnet;i=5020"], "i=39", o6.ns["ns=bacnet;i=6179"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6180", browseName="ns=bacnet;BACnetDateRange", dataType=o6.String, value="BACnetDateRange")
o6.reference(o6.ns["ns=bacnet;i=5017"], "i=39", o6.ns["ns=bacnet;i=6180"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6181", browseName="ns=bacnet;BACnetDateRange", dataType=o6.String, value="//xs:element[@name='BACnetDateRange']")
o6.reference(o6.ns["ns=bacnet;i=5018"], "i=39", o6.ns["ns=bacnet;i=6181"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6183", browseName="ns=bacnet;BACnetDateTime", dataType=o6.String, value="BACnetDateTime")
o6.reference(o6.ns["ns=bacnet;i=5005"], "i=39", o6.ns["ns=bacnet;i=6183"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6184", browseName="ns=bacnet;BACnetDateTime", dataType=o6.String, value="//xs:element[@name='BACnetDateTime']")
o6.reference(o6.ns["ns=bacnet;i=5006"], "i=39", o6.ns["ns=bacnet;i=6184"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6185", browseName="ns=bacnet;BACnetDestination", dataType=o6.String, value="BACnetDestination")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6186", browseName="ns=bacnet;BACnetDestination", dataType=o6.String, value="//xs:element[@name='BACnetDestination']")
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6187", browseName="ns=bacnet;BACnetDeviceObjectPropertyReference", dataType=o6.String, value="BACnetDeviceObjectPropertyReference"
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6188", browseName="ns=bacnet;BACnetDeviceObjectPropertyReference", dataType=o6.String, value="//xs:element[@name='BACnetDeviceObjectPropertyReference']"
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6189", browseName="ns=bacnet;BACnetEventFaultParameterExtended", dataType=o6.String, value="BACnetEventFaultParameterExtended"
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6190", browseName="ns=bacnet;BACnetEventFaultParameterExtended", dataType=o6.String, value="//xs:element[@name='BACnetEventFaultParameterExtended']"
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6191", browseName="ns=bacnet;BACnetEventParameterBufferReady", dataType=o6.String, value="BACnetEventParameterBufferReady")
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6192", browseName="ns=bacnet;BACnetEventParameterBufferReady", dataType=o6.String, value="//xs:element[@name='BACnetEventParameterBufferReady']"
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6193", browseName="ns=bacnet;BACnetEventParameterChangeOfBitstring", dataType=o6.String, value="BACnetEventParameterChangeOfBitstring"
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6194", browseName="ns=bacnet;BACnetEventParameterChangeOfBitstring", dataType=o6.String, value="//xs:element[@name='BACnetEventParameterChangeOfBitstring']"
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6195", browseName="ns=bacnet;BACnetEventParameterChangeOfCharacterString", dataType=o6.String, value="BACnetEventParameterChangeOfCharacterString"
)
o6.reference(o6.ns["ns=bacnet;i=5081"], "i=39", o6.ns["ns=bacnet;i=6195"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6196",
    browseName="ns=bacnet;BACnetEventParameterChangeOfCharacterString",
    dataType=o6.String,
    value="//xs:element[@name='BACnetEventParameterChangeOfCharacterString']",
)
o6.reference(o6.ns["ns=bacnet;i=5082"], "i=39", o6.ns["ns=bacnet;i=6196"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6197", browseName="ns=bacnet;BACnetEventParameterChangeOfState", dataType=o6.String, value="BACnetEventParameterChangeOfState"
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6198", browseName="ns=bacnet;BACnetEventParameterChangeOfState", dataType=o6.String, value="//xs:element[@name='BACnetEventParameterChangeOfState']"
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6199", browseName="ns=bacnet;BACnetEventParameterChangeOfValue", dataType=o6.String, value="BACnetEventParameterChangeOfValue"
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6200", browseName="ns=bacnet;BACnetEventParameterChangeOfValue", dataType=o6.String, value="//xs:element[@name='BACnetEventParameterChangeOfValue']"
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6202", browseName="ns=bacnet;BACnetEventParameterCommandFailure", dataType=o6.String, value="BACnetEventParameterCommandFailure"
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6203", browseName="ns=bacnet;BACnetEventParameterCommandFailure", dataType=o6.String, value="//xs:element[@name='BACnetEventParameterCommandFailure']"
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6204", browseName="ns=bacnet;BACnetEventParameterDoubleOutOfRange", dataType=o6.String, value="BACnetEventParameterDoubleOutOfRange"
)
o6.reference(o6.ns["ns=bacnet;i=5010"], "i=39", o6.ns["ns=bacnet;i=6204"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6205", browseName="ns=bacnet;BACnetEventParameterDoubleOutOfRange", dataType=o6.String, value="//xs:element[@name='BACnetEventParameterDoubleOutOfRange']"
)
o6.reference(o6.ns["ns=bacnet;i=5063"], "i=39", o6.ns["ns=bacnet;i=6205"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6207", browseName="ns=bacnet;BACnetEventParameterFloatingLimit", dataType=o6.String, value="BACnetEventParameterFloatingLimit"
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6210",
    browseName="EnumStrings",
    parent="ns=bacnet;i=3046",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[387],
    value=[
        o6.LocalizedText("AckedTransitions"),
        o6.LocalizedText("AckRequired"),
        o6.LocalizedText("Action"),
        o6.LocalizedText("ActionText"),
        o6.LocalizedText("ActiveText"),
        o6.LocalizedText("ActiveVtSessions"),
        o6.LocalizedText("AlarmValue"),
        o6.LocalizedText("AlarmValues"),
        o6.LocalizedText("All"),
        o6.LocalizedText("AllWritesSuccessful"),
        o6.LocalizedText("ApduSegmentTimeout"),
        o6.LocalizedText("ApduTimeout"),
        o6.LocalizedText("ApplicationSoftwareVersion"),
        o6.LocalizedText("Archive"),
        o6.LocalizedText("Bias"),
        o6.LocalizedText("ChangeOfStateCount"),
        o6.LocalizedText("ChangeOfStateTime"),
        o6.LocalizedText("NotificationClass"),
        o6.LocalizedText("this property deleted"),
        o6.LocalizedText("ControlledVariableReference"),
        o6.LocalizedText("ControlledVariableUnits"),
        o6.LocalizedText("ControlledVariableValue"),
        o6.LocalizedText("CovIncrement"),
        o6.LocalizedText("DateList"),
        o6.LocalizedText("DaylightSavingsStatus"),
        o6.LocalizedText("Deadband"),
        o6.LocalizedText("DerivativeConstant"),
        o6.LocalizedText("DerivativeConstantUnits"),
        o6.LocalizedText("Description"),
        o6.LocalizedText("DescriptionOfHalt"),
        o6.LocalizedText("DeviceAddressBinding"),
        o6.LocalizedText("DeviceType"),
        o6.LocalizedText("EffectivePeriod"),
        o6.LocalizedText("ElapsedActiveTime"),
        o6.LocalizedText("ErrorLimit"),
        o6.LocalizedText("EventEnable"),
        o6.LocalizedText("EventState"),
        o6.LocalizedText("EventType"),
        o6.LocalizedText("ExceptionSchedule"),
        o6.LocalizedText("FaultValues"),
        o6.LocalizedText("FeedbackValue"),
        o6.LocalizedText("FileAccessMethod"),
        o6.LocalizedText("FileSize"),
        o6.LocalizedText("FileType"),
        o6.LocalizedText("FirmwareRevision"),
        o6.LocalizedText("HighLimit"),
        o6.LocalizedText("InactiveText"),
        o6.LocalizedText("InProcess"),
        o6.LocalizedText("InstanceOf"),
        o6.LocalizedText("IntegralConstant"),
        o6.LocalizedText("IntegralConstantUnits"),
        o6.LocalizedText("Removed In Version 1 Revision 4_51"),
        o6.LocalizedText("LimitEnable"),
        o6.LocalizedText("ListOfGroupMembers"),
        o6.LocalizedText("ListOfObjectPropertyReferences"),
        o6.LocalizedText("Unassigned_55"),
        o6.LocalizedText("LocalDate"),
        o6.LocalizedText("LocalTime"),
        o6.LocalizedText("Location"),
        o6.LocalizedText("LowLimit"),
        o6.LocalizedText("ManipulatedVariableReference"),
        o6.LocalizedText("MaximumOutput"),
        o6.LocalizedText("MaxApduLengthAccepted"),
        o6.LocalizedText("MaxInfoFrames"),
        o6.LocalizedText("MaxMaster"),
        o6.LocalizedText("MaxPresValue"),
        o6.LocalizedText("MinimumOffTime"),
        o6.LocalizedText("MinimumOnTime"),
        o6.LocalizedText("MinimumOutput"),
        o6.LocalizedText("MinPresValue"),
        o6.LocalizedText("ModelName"),
        o6.LocalizedText("ModificationDate"),
        o6.LocalizedText("NotifyType"),
        o6.LocalizedText("NumberOfApduRetries"),
        o6.LocalizedText("NumberOfStates"),
        o6.LocalizedText("ObjectIdentifier"),
        o6.LocalizedText("ObjectList"),
        o6.LocalizedText("ObjectName"),
        o6.LocalizedText("ObjectPropertyReference"),
        o6.LocalizedText("ObjectType"),
        o6.LocalizedText("Optional"),
        o6.LocalizedText("OutOfService"),
        o6.LocalizedText("OutputUnits"),
        o6.LocalizedText("EventParameters"),
        o6.LocalizedText("Polarity"),
        o6.LocalizedText("PresentValue"),
        o6.LocalizedText("Priority"),
        o6.LocalizedText("PriorityArray"),
        o6.LocalizedText("PriorityForWriting"),
        o6.LocalizedText("ProcessIdentifier"),
        o6.LocalizedText("ProgramChange"),
        o6.LocalizedText("ProgramLocation"),
        o6.LocalizedText("ProgramState"),
        o6.LocalizedText("ProportionalConstant"),
        o6.LocalizedText("ProportionalConstantUnits"),
        o6.LocalizedText("Removed In Version 1 Revision 2_95"),
        o6.LocalizedText("ProtocolObjectTypesSupported"),
        o6.LocalizedText("ProtocolServicesSupported"),
        o6.LocalizedText("ProtocolVersion"),
        o6.LocalizedText("ReadOnly"),
        o6.LocalizedText("ReasonForHalt"),
        o6.LocalizedText("Removed In Version 1 Revision 4_101"),
        o6.LocalizedText("RecipientList"),
        o6.LocalizedText("Reliability"),
        o6.LocalizedText("RelinquishDefault"),
        o6.LocalizedText("Required"),
        o6.LocalizedText("Resolution"),
        o6.LocalizedText("SegmentationSupported"),
        o6.LocalizedText("Setpoint"),
        o6.LocalizedText("SetpointReference"),
        o6.LocalizedText("StateText"),
        o6.LocalizedText("StatusFlags"),
        o6.LocalizedText("SystemStatus"),
        o6.LocalizedText("TimeDelay"),
        o6.LocalizedText("TimeOfActiveTimeReset"),
        o6.LocalizedText("TimeOfStateCountReset"),
        o6.LocalizedText("TimeSynchronizationRecipients"),
        o6.LocalizedText("Units"),
        o6.LocalizedText("UpdateInterval"),
        o6.LocalizedText("UtcOffset"),
        o6.LocalizedText("VendorIdentifier"),
        o6.LocalizedText("VendorName"),
        o6.LocalizedText("VtClassesSupported"),
        o6.LocalizedText("WeeklySchedule"),
        o6.LocalizedText("AttemptedSamples"),
        o6.LocalizedText("AverageValue"),
        o6.LocalizedText("BufferSize"),
        o6.LocalizedText("ClientCovIncrement"),
        o6.LocalizedText("CovResubscriptionInterval"),
        o6.LocalizedText("Removed In Version 1 Revision 3_129"),
        o6.LocalizedText("EventTimeStamps"),
        o6.LocalizedText("LogBuffer"),
        o6.LocalizedText("LogDeviceObjectProperty"),
        o6.LocalizedText("Enable"),
        o6.LocalizedText("LogInterval"),
        o6.LocalizedText("MaximumValue"),
        o6.LocalizedText("MinimumValue"),
        o6.LocalizedText("NotificationThreshold"),
        o6.LocalizedText("Removed In Version 1 Revision 3_138"),
        o6.LocalizedText("ProtocolRevision"),
        o6.LocalizedText("RecordsSinceNotification"),
        o6.LocalizedText("RecordCount"),
        o6.LocalizedText("StartTime"),
        o6.LocalizedText("StopTime"),
        o6.LocalizedText("StopWhenFull"),
        o6.LocalizedText("TotalRecordCount"),
        o6.LocalizedText("ValidSamples"),
        o6.LocalizedText("WindowInterval"),
        o6.LocalizedText("WindowSamples"),
        o6.LocalizedText("MaximumValueTimestamp"),
        o6.LocalizedText("MinimumValueTimestamp"),
        o6.LocalizedText("VarianceValue"),
        o6.LocalizedText("ActiveCovSubscriptions"),
        o6.LocalizedText("BackupFailureTimeout"),
        o6.LocalizedText("ConfigurationFiles"),
        o6.LocalizedText("DatabaseRevision"),
        o6.LocalizedText("DirectReading"),
        o6.LocalizedText("LastRestoreTime"),
        o6.LocalizedText("MaintenanceRequired"),
        o6.LocalizedText("MemberOf"),
        o6.LocalizedText("Mode"),
        o6.LocalizedText("OperationExpected"),
        o6.LocalizedText("Setting"),
        o6.LocalizedText("Silenced"),
        o6.LocalizedText("TrackingValue"),
        o6.LocalizedText("ZoneMembers"),
        o6.LocalizedText("LifeSafetyAlarmValues"),
        o6.LocalizedText("MaxSegmentsAccepted"),
        o6.LocalizedText("ProfileName"),
        o6.LocalizedText("AutoSlaveDiscovery"),
        o6.LocalizedText("ManualSlaveAddressBinding"),
        o6.LocalizedText("SlaveAddressBinding"),
        o6.LocalizedText("SlaveProxyEnable"),
        o6.LocalizedText("LastNotifyRecord"),
        o6.LocalizedText("ScheduleDefault"),
        o6.LocalizedText("AcceptedModes"),
        o6.LocalizedText("AdjustValue"),
        o6.LocalizedText("Count"),
        o6.LocalizedText("CountBeforeChange"),
        o6.LocalizedText("CountChangeTime"),
        o6.LocalizedText("CovPeriod"),
        o6.LocalizedText("InputReference"),
        o6.LocalizedText("LimitMonitoringInterval"),
        o6.LocalizedText("LoggingObject"),
        o6.LocalizedText("LoggingRecord"),
        o6.LocalizedText("Prescale"),
        o6.LocalizedText("PulseRate"),
        o6.LocalizedText("Scale"),
        o6.LocalizedText("ScaleFactor"),
        o6.LocalizedText("UpdateTime"),
        o6.LocalizedText("ValueBeforeChange"),
        o6.LocalizedText("ValueSet"),
        o6.LocalizedText("ValueChangeTime"),
        o6.LocalizedText("AlignIntervals"),
        o6.LocalizedText("Unassigned_194"),
        o6.LocalizedText("IntervalOffset"),
        o6.LocalizedText("LastRestartReason"),
        o6.LocalizedText("LoggingType"),
        o6.LocalizedText("Unassigned_198"),
        o6.LocalizedText("Unassigned_199"),
        o6.LocalizedText("Unassigned_200"),
        o6.LocalizedText("Unassigned_201"),
        o6.LocalizedText("RestartNotificationRecipients"),
        o6.LocalizedText("TimeOfDeviceRestart"),
        o6.LocalizedText("TimeSynchronizationInterval"),
        o6.LocalizedText("Trigger"),
        o6.LocalizedText("UtcTimeSynchronizationRecipients"),
        o6.LocalizedText("NodeSubtype"),
        o6.LocalizedText("NodeType"),
        o6.LocalizedText("StructuredObjectList"),
        o6.LocalizedText("SubordinateAnnotations"),
        o6.LocalizedText("SubordinateList"),
        o6.LocalizedText("ActualShedLevel"),
        o6.LocalizedText("DutyWindow"),
        o6.LocalizedText("ExpectedShedLevel"),
        o6.LocalizedText("FullDutyBaseline"),
        o6.LocalizedText("Unassigned_216"),
        o6.LocalizedText("Unassigned_217"),
        o6.LocalizedText("RequestedShedLevel"),
        o6.LocalizedText("ShedDuration"),
        o6.LocalizedText("ShedLevelDescriptions"),
        o6.LocalizedText("ShedLevels"),
        o6.LocalizedText("StateDescription"),
        o6.LocalizedText("Unassigned_223"),
        o6.LocalizedText("Unassigned_224"),
        o6.LocalizedText("Unassigned_225"),
        o6.LocalizedText("DoorAlarmState"),
        o6.LocalizedText("DoorExtendedPulseTime"),
        o6.LocalizedText("DoorMembers"),
        o6.LocalizedText("DoorOpenTooLongTime"),
        o6.LocalizedText("DoorPulseTime"),
        o6.LocalizedText("DoorStatus"),
        o6.LocalizedText("DoorUnlockDelayTime"),
        o6.LocalizedText("LockStatus"),
        o6.LocalizedText("MaskedAlarmValues"),
        o6.LocalizedText("SecuredStatus"),
        o6.LocalizedText("Unassigned_236"),
        o6.LocalizedText("Unassigned_237"),
        o6.LocalizedText("Unassigned_238"),
        o6.LocalizedText("Unassigned_239"),
        o6.LocalizedText("Unassigned_240"),
        o6.LocalizedText("Unassigned_241"),
        o6.LocalizedText("Unassigned_242"),
        o6.LocalizedText("Unassigned_243"),
        o6.LocalizedText("AbsenteeLimit"),
        o6.LocalizedText("AccessAlarmEvents"),
        o6.LocalizedText("AccessDoors"),
        o6.LocalizedText("AccessEvent"),
        o6.LocalizedText("AccessEventAuthenticationFactor"),
        o6.LocalizedText("AccessEventCredential"),
        o6.LocalizedText("AccessEventTime"),
        o6.LocalizedText("AccessTransactionEvents"),
        o6.LocalizedText("Accompaniment"),
        o6.LocalizedText("AccompanimentTime"),
        o6.LocalizedText("ActivationTime"),
        o6.LocalizedText("ActiveAuthenticationPolicy"),
        o6.LocalizedText("AssignedAccessRights"),
        o6.LocalizedText("AuthenticationFactors"),
        o6.LocalizedText("AuthenticationPolicyList"),
        o6.LocalizedText("AuthenticationPolicyNames"),
        o6.LocalizedText("AuthenticationStatus"),
        o6.LocalizedText("AuthorizationMode"),
        o6.LocalizedText("BelongsTo"),
        o6.LocalizedText("CredentialDisable"),
        o6.LocalizedText("CredentialStatus"),
        o6.LocalizedText("Credentials"),
        o6.LocalizedText("CredentialsInZone"),
        o6.LocalizedText("DaysRemaining"),
        o6.LocalizedText("EntryPoints"),
        o6.LocalizedText("ExitPoints"),
        o6.LocalizedText("ExpiryTime"),
        o6.LocalizedText("ExtendedTimeEnable"),
        o6.LocalizedText("FailedAttemptEvents"),
        o6.LocalizedText("FailedAttempts"),
        o6.LocalizedText("FailedAttemptsTime"),
        o6.LocalizedText("LastAccessEvent"),
        o6.LocalizedText("LastAccessPoint"),
        o6.LocalizedText("LastCredentialAdded"),
        o6.LocalizedText("LastCredentialAddedTime"),
        o6.LocalizedText("LastCredentialRemoved"),
        o6.LocalizedText("LastCredentialRemovedTime"),
        o6.LocalizedText("LastUseTime"),
        o6.LocalizedText("Lockout"),
        o6.LocalizedText("LockoutRelinquishTime"),
        o6.LocalizedText("Removed In Version 1 Revision 13_284"),
        o6.LocalizedText("MaxFailedAttempts"),
        o6.LocalizedText("Members"),
        o6.LocalizedText("MusterPoint"),
        o6.LocalizedText("NegativeAccessRules"),
        o6.LocalizedText("NumberOfAuthenticationPolicies"),
        o6.LocalizedText("OccupancyCount"),
        o6.LocalizedText("OccupancyCountAdjust"),
        o6.LocalizedText("OccupancyCountEnable"),
        o6.LocalizedText("Removed In Version 1 Revision 13_293"),
        o6.LocalizedText("OccupancyLowerLimit"),
        o6.LocalizedText("OccupancyLowerLimitEnforced"),
        o6.LocalizedText("OccupancyState"),
        o6.LocalizedText("OccupancyUpperLimit"),
        o6.LocalizedText("OccupancyUpperLimitEnforced"),
        o6.LocalizedText("Removed In Version 1 Revision 13_299"),
        o6.LocalizedText("PassbackMode"),
        o6.LocalizedText("PassbackTimeout"),
        o6.LocalizedText("PositiveAccessRules"),
        o6.LocalizedText("ReasonForDisable"),
        o6.LocalizedText("SupportedFormats"),
        o6.LocalizedText("SupportedFormatClasses"),
        o6.LocalizedText("ThreatAuthority"),
        o6.LocalizedText("ThreatLevel"),
        o6.LocalizedText("TraceFlag"),
        o6.LocalizedText("TransactionNotificationClass"),
        o6.LocalizedText("UserExternalIdentifier"),
        o6.LocalizedText("UserInformationReference"),
        o6.LocalizedText("Unassigned_312"),
        o6.LocalizedText("Unassigned_313"),
        o6.LocalizedText("Unassigned_314"),
        o6.LocalizedText("Unassigned_315"),
        o6.LocalizedText("Unassigned_316"),
        o6.LocalizedText("UserName"),
        o6.LocalizedText("UserType"),
        o6.LocalizedText("UsesRemaining"),
        o6.LocalizedText("ZoneFrom"),
        o6.LocalizedText("ZoneTo"),
        o6.LocalizedText("AccessEventTag"),
        o6.LocalizedText("GlobalIdentifier"),
        o6.LocalizedText("Unassigned_324"),
        o6.LocalizedText("Unassigned_325"),
        o6.LocalizedText("VerificationTime"),
        o6.LocalizedText("BaseDeviceSecurityPolicy"),
        o6.LocalizedText("DistributionKeyRevision"),
        o6.LocalizedText("DoNotHide"),
        o6.LocalizedText("KeySets"),
        o6.LocalizedText("LastKeyServer"),
        o6.LocalizedText("NetworkAccessSecurityPolicies"),
        o6.LocalizedText("PacketReorderTime"),
        o6.LocalizedText("SecurityPduTimeout"),
        o6.LocalizedText("SecurityTimeWindow"),
        o6.LocalizedText("SupportedSecurityAlgorithms"),
        o6.LocalizedText("UpdateKeySetTimeout"),
        o6.LocalizedText("BackupAndRestoreState"),
        o6.LocalizedText("BackupPreparationTime"),
        o6.LocalizedText("RestoreCompletionTime"),
        o6.LocalizedText("RestorePreparationTime"),
        o6.LocalizedText("BitMask"),
        o6.LocalizedText("BitText"),
        o6.LocalizedText("IsUtc"),
        o6.LocalizedText("GroupMembers"),
        o6.LocalizedText("GroupMemberNames"),
        o6.LocalizedText("MemberStatusFlags"),
        o6.LocalizedText("RequestedUpdateInterval"),
        o6.LocalizedText("CovuPeriod"),
        o6.LocalizedText("CovuRecipients"),
        o6.LocalizedText("EventMessageTexts"),
        o6.LocalizedText("EventMessageTextsConfig"),
        o6.LocalizedText("EventDetectionEnable"),
        o6.LocalizedText("EventAlgorithmInhibit"),
        o6.LocalizedText("EventAlgorithmInhibitRef"),
        o6.LocalizedText("TimeDelayNormal"),
        o6.LocalizedText("ReliabilityEvaluationInhibit"),
        o6.LocalizedText("FaultParameters"),
        o6.LocalizedText("FaultType"),
        o6.LocalizedText("LocalForwardingOnly"),
        o6.LocalizedText("ProcessIdentifierFilter"),
        o6.LocalizedText("SubscribedRecipients"),
        o6.LocalizedText("PortFilter"),
        o6.LocalizedText("AuthorizationExemptions"),
        o6.LocalizedText("AllowGroupDelayInhibit"),
        o6.LocalizedText("ChannelNumber"),
        o6.LocalizedText("ControlGroups"),
        o6.LocalizedText("ExecutionDelay"),
        o6.LocalizedText("LastPriority"),
        o6.LocalizedText("WriteStatus"),
        o6.LocalizedText("PropertyList"),
        o6.LocalizedText("SerialNumber"),
        o6.LocalizedText("BlinkWarnEnable"),
        o6.LocalizedText("DefaultFadeTime"),
        o6.LocalizedText("DefaultRampRate"),
        o6.LocalizedText("DefaultStepIncrement"),
        o6.LocalizedText("EgressTime"),
        o6.LocalizedText("InProgress"),
        o6.LocalizedText("InstantaneousPower"),
        o6.LocalizedText("LightingCommand"),
        o6.LocalizedText("LightingCommandDefaultPriority"),
        o6.LocalizedText("MaxActualValue"),
        o6.LocalizedText("MinActualValue"),
        o6.LocalizedText("Power"),
        o6.LocalizedText("Transition"),
        o6.LocalizedText("EgressActive"),
    ],
)
bacnet_objtypes.BACnetNotifierType(
    nodeId="ns=bacnet;i=5036",
    browseName="ns=bacnet;<Notifier_Object_Name>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6206",
                browseName="ns=bacnet;Recipient_List",
                dataType=bacnet_datypes.BACnetDestination,
                value=bacnet_datypes.BACnetDestination(
                    validDays=bacnet_datypes.BACnetDaysOfWeek(value=b"\x00", validBits=b"\x7f"),
                    fromTime=bacnet_datypes.BACnetTime(hour=0, minute=0, second=0, hundredths=0),
                    toTime=bacnet_datypes.BACnetTime(hour=0, minute=0, second=0, hundredths=0),
                    recipient=bacnet_datypes.BACnetRecipient(),
                    processIdentifier=0,
                    issueConfirmedNotifications=False,
                    transitions=bacnet_datypes.BACnetEventTransitionBits(value=b"\x00", validBits=b"\x07"),
                ),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6211", browseName="ns=bacnet;Object_Identifier", dataType=bacnet_datypes.BACnetObjectIdentifier, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
    _allow_abstract=True,
)
o6.reference(bacnet_objtypes.BACnetDeviceType, ns0.reftypes.HasNotifier, o6.ns["ns=bacnet;i=5036"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6212", browseName="ns=bacnet;BACnetEventParameterFloatingLimit", dataType=o6.String, value="//xs:element[@name='BACnetEventParameterFloatingLimit']"
)
bacnet_objtypes.BACnetObjectType(
    nodeId="ns=bacnet;i=5037",
    browseName="ns=bacnet;<BACnetObjectName>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6231", browseName="ns=bacnet;Object_Identifier", dataType=bacnet_datypes.BACnetObjectIdentifier, accessLevel=3, userAccessLevel=1
            )
        )
    ],
    _allow_abstract=True,
)
bacnet_objtypes.BACnetObjectType(
    nodeId="ns=bacnet;i=5038",
    browseName="ns=bacnet;<BACnetObjectName>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6232", browseName="ns=bacnet;Object_Identifier", dataType=bacnet_datypes.BACnetObjectIdentifier, accessLevel=3, userAccessLevel=1
            )
        )
    ],
    _allow_abstract=True,
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6234", browseName="ns=bacnet;BACnetEventParameterOutOfRange", dataType=o6.String, value="BACnetEventParameterOutOfRange")
bacnet_objtypes.BACnetStructuredViewType(
    nodeId="ns=bacnet;i=5043",
    browseName="ns=bacnet;<BACnetStructuredView>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6081", browseName="ns=bacnet;Node_Type", dataType=bacnet_datypes.BACnetNodeType, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6082",
                browseName="ns=bacnet;Subordinate_List",
                dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6236", browseName="ns=bacnet;Object_Identifier", dataType=bacnet_datypes.BACnetObjectIdentifier, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
    _allow_abstract=True,
)
o6.reference(bacnet_objtypes.BACnetStructuredViewType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=5043"])
bacnet_objtypes.BACnetObjectType(
    nodeId="ns=bacnet;i=5044",
    browseName="ns=bacnet;<BACnetObject>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6237", browseName="ns=bacnet;Object_Identifier", dataType=bacnet_datypes.BACnetObjectIdentifier, accessLevel=3, userAccessLevel=1
            )
        )
    ],
    _allow_abstract=True,
)
o6.reference(bacnet_objtypes.BACnetStructuredViewType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=5044"])
bacnet_objtypes.BACnetStructuredViewType(
    nodeId="ns=bacnet;i=5039",
    browseName="ns=bacnet;<BACnetStructuredViewName>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6079", browseName="ns=bacnet;Node_Type", dataType=bacnet_datypes.BACnetNodeType, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6080",
                browseName="ns=bacnet;Subordinate_List",
                dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6239", browseName="ns=bacnet;Object_Identifier", dataType=bacnet_datypes.BACnetObjectIdentifier, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
    _allow_abstract=True,
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6250", browseName="ns=bacnet;BACnetEventParameterOutOfRange", dataType=o6.String, value="//xs:element[@name='BACnetEventParameterOutOfRange']"
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6251", browseName="ns=bacnet;BACnetEventParameterSignedOutOfRange", dataType=o6.String, value="BACnetEventParameterSignedOutOfRange"
)
o6.reference(o6.ns["ns=bacnet;i=5064"], "i=39", o6.ns["ns=bacnet;i=6251"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6257", browseName="ns=bacnet;BACnetEventParameterSignedOutOfRange", dataType=o6.String, value="//xs:element[@name='BACnetEventParameterSignedOutOfRange']"
)
o6.reference(o6.ns["ns=bacnet;i=5080"], "i=39", o6.ns["ns=bacnet;i=6257"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6258", browseName="ns=bacnet;BACnetEventParameterUnsignedOutOfRange", dataType=o6.String, value="BACnetEventParameterUnsignedOutOfRange"
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=bacnet;i=6268",
    browseName="ns=bacnet;Controlled_Variable_Value",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6269", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(bacnet_objtypes.BACnetLoopType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=6268"])
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6270",
    browseName="EnumStrings",
    parent="ns=bacnet;i=3057",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("normal"), o6.LocalizedText("urgent")],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=bacnet;i=6327",
    browseName="ns=bacnet;Setpoint",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6328", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(bacnet_objtypes.BACnetLoopType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=6327"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6341",
    browseName="ns=bacnet;BACnetEventParameterUnsignedOutOfRange",
    dataType=o6.String,
    value="//xs:element[@name='BACnetEventParameterUnsignedOutOfRange']",
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6342", browseName="ns=bacnet;BACnetEventParameterUnsignedRange", dataType=o6.String, value="BACnetEventParameterUnsignedRange"
)
o6.reference(o6.ns["ns=bacnet;i=5083"], "i=39", o6.ns["ns=bacnet;i=6342"])
bacnet_objtypes.BACnetFaultAlgorithmType(
    nodeId="ns=bacnet;i=5071",
    browseName="ns=bacnet;FaultAlgorithm",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6379", browseName="ns=bacnet;Object_Identifier", dataType=bacnet_datypes.BACnetObjectIdentifier, accessLevel=3, userAccessLevel=1
            )
        )
    ],
    _allow_abstract=True,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=bacnet;i=6382",
    browseName="ns=bacnet;Proportional_Constant",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6383", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(bacnet_objtypes.BACnetLoopType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=6382"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=bacnet;i=6384",
    browseName="ns=bacnet;Integral_Constant",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6385", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(bacnet_objtypes.BACnetLoopType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=6384"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=bacnet;i=6386",
    browseName="ns=bacnet;Bias",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6387", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(bacnet_objtypes.BACnetLoopType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=6386"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=bacnet;i=6388",
    browseName="ns=bacnet;Derivative_Constant",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6389", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Float,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(bacnet_objtypes.BACnetLoopType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=6388"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashBACnet_V2Slash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=bacnet;i=5004",
    browseName="ns=bacnet;http://opcfoundation.org/UA/BACnet_V2/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6390", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6391", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2023-05-17T00:00:00Z"))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6392", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/BACnet_V2/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6393", browseName="NamespaceVersion", dataType=o6.String, value="2.00.1")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6394", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6395", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6396", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6400", browseName="ns=bacnet;BACnetEventParameterUnsignedRange", dataType=o6.String, value="//xs:element[@name='BACnetEventParameterUnsignedRange']"
)
o6.reference(o6.ns["ns=bacnet;i=5084"], "i=39", o6.ns["ns=bacnet;i=6400"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6401", browseName="ns=bacnet;BACnetFaultParameterFaultCharacterstring", dataType=o6.String, value="BACnetFaultParameterFaultCharacterstring"
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6402",
    browseName="ns=bacnet;BACnetFaultParameterFaultCharacterstring",
    dataType=o6.String,
    value="//xs:element[@name='BACnetFaultParameterFaultCharacterstring']",
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6403", browseName="ns=bacnet;BACnetFaultParameterFaultLifeSafety", dataType=o6.String, value="BACnetFaultParameterFaultLifeSafety"
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6404", browseName="ns=bacnet;BACnetFaultParameterFaultLifeSafety", dataType=o6.String, value="//xs:element[@name='BACnetFaultParameterFaultLifeSafety']"
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6405", browseName="ns=bacnet;BACnetFaultParameterFaultState", dataType=o6.String, value="BACnetFaultParameterFaultState")
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6406", browseName="ns=bacnet;BACnetFaultParameterFaultState", dataType=o6.String, value="//xs:element[@name='BACnetFaultParameterFaultState']"
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6407", browseName="ns=bacnet;BACnetFaultParameterFaultStatusFlags", dataType=o6.String, value="BACnetFaultParameterFaultStatusFlags"
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6408", browseName="ns=bacnet;BACnetFaultParameterFaultStatusFlags", dataType=o6.String, value="//xs:element[@name='BACnetFaultParameterFaultStatusFlags']"
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6410", browseName="ns=bacnet;BACnetPropertyStates", dataType=o6.String, value="BACnetPropertyStates")
o6.reference(o6.ns["ns=bacnet;i=5047"], "i=39", o6.ns["ns=bacnet;i=6410"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6411", browseName="ns=bacnet;BACnetPropertyStates", dataType=o6.String, value="//xs:element[@name='BACnetPropertyStates']")
o6.reference(o6.ns["ns=bacnet;i=5048"], "i=39", o6.ns["ns=bacnet;i=6411"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6412", browseName="ns=bacnet;BACnetRecipientProcess", dataType=o6.String, value="BACnetRecipientProcess")
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6413", browseName="ns=bacnet;BACnetRecipientProcess", dataType=o6.String, value="//xs:element[@name='BACnetRecipientProcess']"
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6414", browseName="ns=bacnet;BACnetSpecialEvent", dataType=o6.String, value="BACnetSpecialEvent")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6417", browseName="ns=bacnet;BACnetSpecialEvent", dataType=o6.String, value="//xs:element[@name='BACnetSpecialEvent']")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6418", browseName="ns=bacnet;BACnetTime", dataType=o6.String, value="BACnetTime")
o6.reference(o6.ns["ns=bacnet;i=5021"], "i=39", o6.ns["ns=bacnet;i=6418"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6419", browseName="ns=bacnet;BACnetTime", dataType=o6.String, value="//xs:element[@name='BACnetTime']")
o6.reference(o6.ns["ns=bacnet;i=5022"], "i=39", o6.ns["ns=bacnet;i=6419"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6420", browseName="ns=bacnet;BACnetTimeValue", dataType=o6.String, value="BACnetTimeValue")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6421", browseName="ns=bacnet;BACnetTimeValue", dataType=o6.String, value="//xs:element[@name='BACnetTimeValue']")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6422", browseName="ns=bacnet;BACnetTimeValueValue", dataType=o6.String, value="BACnetTimeValueValue")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6423", browseName="ns=bacnet;BACnetTimeValueValue", dataType=o6.String, value="//xs:element[@name='BACnetTimeValueValue']")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6424", browseName="ns=bacnet;BACnetWeekNDay", dataType=o6.String, value="BACnetWeekNDay")
o6.reference(o6.ns["ns=bacnet;i=5013"], "i=39", o6.ns["ns=bacnet;i=6424"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6425", browseName="ns=bacnet;BACnetWeekNDay", dataType=o6.String, value="//xs:element[@name='BACnetWeekNDay']")
o6.reference(o6.ns["ns=bacnet;i=5014"], "i=39", o6.ns["ns=bacnet;i=6425"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6426", browseName="ns=bacnet;BACnetDaysOfWeek", dataType=o6.String, value="BACnetDaysOfWeek")
o6.reference(o6.ns["ns=bacnet;i=5125"], "i=39", o6.ns["ns=bacnet;i=6426"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6427", browseName="ns=bacnet;BACnetDaysOfWeek", dataType=o6.String, value="//xs:element[@name='BACnetDaysOfWeek']")
o6.reference(o6.ns["ns=bacnet;i=5127"], "i=39", o6.ns["ns=bacnet;i=6427"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6428", browseName="ns=bacnet;BACnetEventTransitionBits", dataType=o6.String, value="BACnetEventTransitionBits")
o6.reference(o6.ns["ns=bacnet;i=5129"], "i=39", o6.ns["ns=bacnet;i=6428"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6429", browseName="ns=bacnet;BACnetEventTransitionBits", dataType=o6.String, value="//xs:element[@name='BACnetEventTransitionBits']"
)
o6.reference(o6.ns["ns=bacnet;i=5130"], "i=39", o6.ns["ns=bacnet;i=6429"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6430", browseName="ns=bacnet;BACnetLimitEnable", dataType=o6.String, value="BACnetLimitEnable")
o6.reference(o6.ns["ns=bacnet;i=5131"], "i=39", o6.ns["ns=bacnet;i=6430"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6431", browseName="ns=bacnet;BACnetLimitEnable", dataType=o6.String, value="//xs:element[@name='BACnetLimitEnable']")
o6.reference(o6.ns["ns=bacnet;i=5132"], "i=39", o6.ns["ns=bacnet;i=6431"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6432", browseName="ns=bacnet;BACnetObjectTypeSupportedBits", dataType=o6.String, value="BACnetObjectTypeSupportedBits")
o6.reference(o6.ns["ns=bacnet;i=5133"], "i=39", o6.ns["ns=bacnet;i=6432"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6433", browseName="ns=bacnet;BACnetObjectTypeSupportedBits", dataType=o6.String, value="//xs:element[@name='BACnetObjectTypeSupportedBits']"
)
o6.reference(o6.ns["ns=bacnet;i=5134"], "i=39", o6.ns["ns=bacnet;i=6433"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6435", browseName="ns=bacnet;BACnetServicesSupportedBits", dataType=o6.String, value="BACnetServicesSupportedBits")
o6.reference(o6.ns["ns=bacnet;i=5135"], "i=39", o6.ns["ns=bacnet;i=6435"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6436", browseName="ns=bacnet;BACnetServicesSupportedBits", dataType=o6.String, value="//xs:element[@name='BACnetServicesSupportedBits']"
)
o6.reference(o6.ns["ns=bacnet;i=5136"], "i=39", o6.ns["ns=bacnet;i=6436"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6437", browseName="ns=bacnet;BACnetStatusFlags", dataType=o6.String, value="BACnetStatusFlags")
o6.reference(o6.ns["ns=bacnet;i=5146"], "i=39", o6.ns["ns=bacnet;i=6437"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6438", browseName="ns=bacnet;BACnetStatusFlags", dataType=o6.String, value="//xs:element[@name='BACnetStatusFlags']")
o6.reference(o6.ns["ns=bacnet;i=5147"], "i=39", o6.ns["ns=bacnet;i=6438"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6439", browseName="ns=bacnet;BACnetCalendarEntry", dataType=o6.String, value="BACnetCalendarEntry")
o6.reference(o6.ns["ns=bacnet;i=5002"], "i=39", o6.ns["ns=bacnet;i=6439"])
bacnet_objtypes.BACnetEventAlgorithmType(
    nodeId="ns=bacnet;i=5026",
    browseName="ns=bacnet;EventAlgorithm",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6440", browseName="ns=bacnet;TimeDelay", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6441", browseName="ns=bacnet;TimeDelayNormal", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
    ],
    _allow_abstract=True,
)
o6.reference(bacnet_objtypes.BACnetEventReportingType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=5026"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6442", browseName="ns=bacnet;BACnetCalendarEntry", dataType=o6.String, value="//xs:element[@name='BACnetCalendarEntry']")
o6.reference(o6.ns["ns=bacnet;i=5003"], "i=39", o6.ns["ns=bacnet;i=6442"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6443", browseName="ns=bacnet;BACnetClientCOV", dataType=o6.String, value="BACnetClientCOV")
o6.reference(o6.ns["ns=bacnet;i=5011"], "i=39", o6.ns["ns=bacnet;i=6443"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6444", browseName="ns=bacnet;BACnetClientCOV", dataType=o6.String, value="//xs:element[@name='BACnetClientCOV']")
o6.reference(o6.ns["ns=bacnet;i=5012"], "i=39", o6.ns["ns=bacnet;i=6444"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6445", browseName="ns=bacnet;BACnetEventParameter", dataType=o6.String, value="BACnetEventParameter")
o6.reference(o6.ns["ns=bacnet;i=5015"], "i=39", o6.ns["ns=bacnet;i=6445"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6446", browseName="ns=bacnet;BACnetEventParameter", dataType=o6.String, value="//xs:element[@name='BACnetEventParameter']")
o6.reference(o6.ns["ns=bacnet;i=5016"], "i=39", o6.ns["ns=bacnet;i=6446"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6447", browseName="ns=bacnet;BACnetEventParameterExtendedParameters", dataType=o6.String, value="BACnetEventParameterExtendedParameters"
)
o6.reference(o6.ns["ns=bacnet;i=5085"], "i=39", o6.ns["ns=bacnet;i=6447"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6448",
    browseName="ns=bacnet;BACnetEventParameterExtendedParameters",
    dataType=o6.String,
    value="//xs:element[@name='BACnetEventParameterExtendedParameters']",
)
o6.reference(o6.ns["ns=bacnet;i=5086"], "i=39", o6.ns["ns=bacnet;i=6448"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6449", browseName="ns=bacnet;BACnetFaultParameter", dataType=o6.String, value="BACnetFaultParameter")
o6.reference(o6.ns["ns=bacnet;i=5023"], "i=39", o6.ns["ns=bacnet;i=6449"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6450", browseName="ns=bacnet;BACnetFaultParameter", dataType=o6.String, value="//xs:element[@name='BACnetFaultParameter']")
o6.reference(o6.ns["ns=bacnet;i=5025"], "i=39", o6.ns["ns=bacnet;i=6450"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6451", browseName="ns=bacnet;BACnetMessageClass", dataType=o6.String, value="BACnetMessageClass")
o6.reference(o6.ns["ns=bacnet;i=5028"], "i=39", o6.ns["ns=bacnet;i=6451"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6452", browseName="ns=bacnet;BACnetMessageClass", dataType=o6.String, value="//xs:element[@name='BACnetMessageClass']")
o6.reference(o6.ns["ns=bacnet;i=5029"], "i=39", o6.ns["ns=bacnet;i=6452"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6453", browseName="ns=bacnet;BACnetPriorityValue", dataType=o6.String, value="BACnetPriorityValue")
o6.reference(o6.ns["ns=bacnet;i=5030"], "i=39", o6.ns["ns=bacnet;i=6453"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6454", browseName="ns=bacnet;BACnetPriorityValue", dataType=o6.String, value="//xs:element[@name='BACnetPriorityValue']")
o6.reference(o6.ns["ns=bacnet;i=5031"], "i=39", o6.ns["ns=bacnet;i=6454"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6455", browseName="ns=bacnet;BACnetRecipient", dataType=o6.String, value="BACnetRecipient")
o6.reference(o6.ns["ns=bacnet;i=5032"], "i=39", o6.ns["ns=bacnet;i=6455"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6456", browseName="ns=bacnet;BACnetRecipient", dataType=o6.String, value="//xs:element[@name='BACnetRecipient']")
o6.reference(o6.ns["ns=bacnet;i=5033"], "i=39", o6.ns["ns=bacnet;i=6456"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6457", browseName="ns=bacnet;BACnetSpecialEventPeriod", dataType=o6.String, value="BACnetSpecialEventPeriod")
o6.reference(o6.ns["ns=bacnet;i=5034"], "i=39", o6.ns["ns=bacnet;i=6457"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6458", browseName="ns=bacnet;BACnetSpecialEventPeriod", dataType=o6.String, value="//xs:element[@name='BACnetSpecialEventPeriod']"
)
o6.reference(o6.ns["ns=bacnet;i=5035"], "i=39", o6.ns["ns=bacnet;i=6458"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6459", browseName="ns=bacnet;BACnetTimeStamp", dataType=o6.String, value="BACnetTimeStamp")
o6.reference(o6.ns["ns=bacnet;i=5069"], "i=39", o6.ns["ns=bacnet;i=6459"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=bacnet;i=6460", browseName="ns=bacnet;BACnetTimeStamp", dataType=o6.String, value="//xs:element[@name='BACnetTimeStamp']")
o6.reference(o6.ns["ns=bacnet;i=5070"], "i=39", o6.ns["ns=bacnet;i=6460"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6461", browseName="ns=bacnet;BACnetEventParameterChangeOfLifeSafety", dataType=o6.String, value="BACnetEventParameterChangeOfLifeSafety"
)
o6.reference(o6.ns["ns=bacnet;i=5024"], "i=39", o6.ns["ns=bacnet;i=6461"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=bacnet;i=6149",
    browseName="ns=bacnet;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/BACnet_V2/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6150", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/BACnet_V2/")),
        o6.hasComponent(o6.ns["ns=bacnet;i=6163"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6170"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6172"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6174"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6178"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6180"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6183"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6185"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6187"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6189"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6191"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6193"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6195"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6197"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6199"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6202"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6204"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6207"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6234"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6251"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6258"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6342"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6401"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6403"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6405"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6407"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6410"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6412"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6414"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6418"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6420"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6422"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6424"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6426"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6428"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6430"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6432"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6435"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6437"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6439"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6443"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6445"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6447"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6449"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6451"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6453"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6455"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6457"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6459"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6461"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/BACnet_V2/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/BACnet_V2/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetAddress">\n  <opc:Field TypeName="opc:UInt16" Name="NetworkNumber"/>\n  <opc:Field TypeName="opc:ByteString" Name="MacAddress"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetAddressBinding">\n  <opc:Field TypeName="opc:UInt32" Name="DeviceObjectIdentifier"/>\n  <opc:Field TypeName="tns:BACnetAddress" Name="DeviceAddress"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetCOVSubscription">\n  <opc:Field TypeName="opc:Bit" Name="CovIncrementSpecified"/>\n  <opc:Field Length="31" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="tns:BACnetRecipientProcess" Name="Recipient"/>\n  <opc:Field TypeName="tns:BACnetDeviceObjectPropertyReference" Name="MonitoredPropertyReference"/>\n  <opc:Field TypeName="opc:Boolean" Name="IssueConfirmedNotifications"/>\n  <opc:Field TypeName="opc:UInt32" Name="TimeRemaining"/>\n  <opc:Field SwitchField="CovIncrementSpecified" TypeName="opc:Float" Name="CovIncrement"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetDailySchedule">\n  <opc:Field TypeName="opc:Int32" Name="NoOfDay-schedule"/>\n  <opc:Field LengthField="NoOfDay-schedule" TypeName="tns:BACnetTimeValue" Name="Day-schedule"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetDate">\n  <opc:Field TypeName="opc:UInt16" Name="Year"/>\n  <opc:Field TypeName="tns:BACnetMonth" Name="Month"/>\n  <opc:Field TypeName="tns:BACnetDayOfMonth" Name="DayOfMonth"/>\n  <opc:Field TypeName="tns:BACnetDayOfWeek" Name="DayOfWeek"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetDateRange">\n  <opc:Field TypeName="tns:BACnetDate" Name="StartDate"/>\n  <opc:Field TypeName="tns:BACnetDate" Name="EndTime"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetDateTime">\n  <opc:Field TypeName="tns:BACnetDate" Name="Date"/>\n  <opc:Field TypeName="tns:BACnetTime" Name="Time"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetDestination">\n  <opc:Field TypeName="tns:BACnetDaysOfWeek" Name="ValidDays"/>\n  <opc:Field TypeName="tns:BACnetTime" Name="FromTime"/>\n  <opc:Field TypeName="tns:BACnetTime" Name="ToTime"/>\n  <opc:Field TypeName="tns:BACnetRecipient" Name="Recipient"/>\n  <opc:Field TypeName="opc:UInt32" Name="ProcessIdentifier"/>\n  <opc:Field TypeName="opc:Boolean" Name="IssueConfirmedNotifications"/>\n  <opc:Field TypeName="tns:BACnetEventTransitionBits" Name="Transitions"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetDeviceObjectPropertyReference">\n  <opc:Field TypeName="opc:Bit" Name="PropertyIdentifierSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="PropertyArrayIndexSpecified"/>\n  <opc:Field TypeName="opc:Bit" Name="DeviceIdentifierSpecified"/>\n  <opc:Field Length="29" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:UInt32" Name="ObjectIdentifier"/>\n  <opc:Field SwitchField="PropertyIdentifierSpecified" TypeName="tns:BACnetPropertyIdentifier" Name="PropertyIdentifier"/>\n  <opc:Field SwitchField="PropertyArrayIndexSpecified" TypeName="opc:UInt32" Name="PropertyArrayIndex"/>\n  <opc:Field SwitchField="DeviceIdentifierSpecified" TypeName="opc:UInt32" Name="DeviceIdentifier"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetEventFaultParameterExtended">\n  <opc:Field TypeName="opc:UInt16" Name="VendorId"/>\n  <opc:Field TypeName="ua:Variant" Name="Extended-fault-type"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfParameters"/>\n  <opc:Field LengthField="NoOfParameters" TypeName="tns:BACnetEventParameterExtendedParameters" Name="Parameters"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetEventParameterBufferReady">\n  <opc:Field TypeName="opc:UInt32" Name="Notification-threshold"/>\n  <opc:Field TypeName="opc:UInt32" Name="Previous-notification-count"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetEventParameterChangeOfBitstring">\n  <opc:Field TypeName="opc:UInt32" Name="Time-delay"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="Bitmask"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfList-of-bitstring-values"/>\n  <opc:Field LengthField="NoOfList-of-bitstring-values" TypeName="ua:ExtensionObject" Name="List-of-bitstring-values"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetEventParameterChangeOfCharacterString">\n  <opc:Field TypeName="opc:UInt32" Name="Time-delay"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfAlarmValues"/>\n  <opc:Field LengthField="NoOfAlarmValues" TypeName="opc:CharArray" Name="AlarmValues"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetEventParameterChangeOfLifeSafety">\n  <opc:Field TypeName="tns:BACnetLifeSafetyState" Name="NewState"/>\n  <opc:Field TypeName="tns:BACnetLifeSafetyMode" Name="NewMode"/>\n  <opc:Field TypeName="tns:BACnetLifeSafetyOperation" Name="OperationExtended"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetEventParameterChangeOfState">\n  <opc:Field TypeName="opc:UInt32" Name="Time-delay"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfList-of-values"/>\n  <opc:Field LengthField="NoOfList-of-values" TypeName="tns:BACnetPropertyStates" Name="List-of-values"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetEventParameterChangeOfValue">\n  <opc:Field TypeName="opc:UInt32" Name="Time-delay"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="Cov-criteria-bitmask"/>\n  <opc:Field TypeName="opc:Float" Name="Cov-criteria-referenced-property-increment"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetEventParameterCommandFailure">\n  <opc:Field TypeName="opc:UInt32" Name="Time-delay"/>\n  <opc:Field TypeName="tns:BACnetDeviceObjectPropertyReference" Name="Feedback-property-reference"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetEventParameterDoubleOutOfRange">\n  <opc:Field TypeName="opc:UInt32" Name="Time-delay"/>\n  <opc:Field TypeName="opc:Double" Name="Low-limit"/>\n  <opc:Field TypeName="opc:Double" Name="High-limit"/>\n  <opc:Field TypeName="opc:Double" Name="Deadband"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetEventParameterFloatingLimit">\n  <opc:Field TypeName="opc:UInt32" Name="Time-delay"/>\n  <opc:Field TypeName="tns:BACnetDeviceObjectPropertyReference" Name="Setpoint-reference"/>\n  <opc:Field TypeName="opc:Double" Name="Low-diff-limit"/>\n  <opc:Field TypeName="opc:Double" Name="High-diff-limit"/>\n  <opc:Field TypeName="opc:Double" Name="Deadband"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetEventParameterOutOfRange">\n  <opc:Field TypeName="opc:UInt32" Name="Time-delay"/>\n  <opc:Field TypeName="opc:Double" Name="Low-limit"/>\n  <opc:Field TypeName="opc:Double" Name="High-limit"/>\n  <opc:Field TypeName="opc:Double" Name="Deadband"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetEventParameterSignedOutOfRange">\n  <opc:Field TypeName="opc:UInt32" Name="Time-delay"/>\n  <opc:Field TypeName="opc:Int32" Name="Low-limit"/>\n  <opc:Field TypeName="opc:Int32" Name="High-limit"/>\n  <opc:Field TypeName="opc:UInt32" Name="Deadband"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetEventParameterUnsignedOutOfRange">\n  <opc:Field TypeName="opc:UInt32" Name="Time-delay"/>\n  <opc:Field TypeName="opc:UInt32" Name="Low-limit"/>\n  <opc:Field TypeName="opc:UInt32" Name="High-limit"/>\n  <opc:Field TypeName="opc:UInt32" Name="Deadband"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetEventParameterUnsignedRange">\n  <opc:Field TypeName="opc:UInt32" Name="Time-delay"/>\n  <opc:Field TypeName="opc:UInt32" Name="Low-limit"/>\n  <opc:Field TypeName="opc:UInt32" Name="High-limit"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetFaultParameterFaultCharacterstring">\n  <opc:Field TypeName="opc:CharArray" Name="Fault-characterstring"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetFaultParameterFaultLifeSafety">\n  <opc:Field TypeName="opc:Int32" Name="NoOfList-of-fault-values"/>\n  <opc:Field LengthField="NoOfList-of-fault-values" TypeName="tns:BACnetLifeSafetyState" Name="List-of-fault-values"/>\n  <opc:Field TypeName="tns:BACnetDeviceObjectPropertyReference" Name="Mode-property-reference"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetFaultParameterFaultState">\n  <opc:Field TypeName="opc:Int32" Name="NoOfList-of-fault-values"/>\n  <opc:Field LengthField="NoOfList-of-fault-values" TypeName="tns:BACnetProgramStates" Name="List-of-fault-values"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetFaultParameterFaultStatusFlags">\n  <opc:Field TypeName="opc:Int32" Name="NoOfStatus-flags-reference"/>\n  <opc:Field LengthField="NoOfStatus-flags-reference" TypeName="tns:BACnetDeviceObjectPropertyReference" Name="Status-flags-reference"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetPropertyStates">\n  <opc:Field TypeName="opc:Boolean" Name="BooleanValue"/>\n  <opc:Field TypeName="tns:BACnetBinaryPV" Name="BinaryValue"/>\n  <opc:Field TypeName="tns:BACnetEventEnumType" Name="EventType"/>\n  <opc:Field TypeName="tns:BACnetPolarity" Name="Polarity"/>\n  <opc:Field TypeName="tns:BACnetProgramRequest" Name="ProgramChange"/>\n  <opc:Field TypeName="tns:BACnetProgramStates" Name="ProgramState"/>\n  <opc:Field TypeName="tns:BACnetProgramError" Name="ProgramError"/>\n  <opc:Field TypeName="tns:BACnetReliability" Name="Reliability"/>\n  <opc:Field TypeName="tns:BACnetEventState" Name="State"/>\n  <opc:Field TypeName="tns:BACnetDeviceStatus" Name="SystemStatus"/>\n  <opc:Field TypeName="ua:EUInformation" Name="Units"/>\n  <opc:Field TypeName="opc:UInt32" Name="UnsignedValue"/>\n  <opc:Field TypeName="tns:BACnetLifeSafetyMode" Name="LifeSafetyMode"/>\n  <opc:Field TypeName="tns:BACnetLifeSafetyState" Name="LifeSafetyState"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetRecipientProcess">\n  <opc:Field TypeName="tns:BACnetRecipient" Name="Recipient"/>\n  <opc:Field TypeName="opc:UInt32" Name="ProcessIdentifier"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetSpecialEvent">\n  <opc:Field TypeName="tns:BACnetSpecialEventPeriod" Name="Period"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfListOfTimeValues"/>\n  <opc:Field LengthField="NoOfListOfTimeValues" TypeName="tns:BACnetTimeValue" Name="ListOfTimeValues"/>\n  <opc:Field TypeName="opc:Byte" Name="EventPriority"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetTime">\n  <opc:Field TypeName="opc:Byte" Name="Hour"/>\n  <opc:Field TypeName="opc:Byte" Name="Minute"/>\n  <opc:Field TypeName="opc:Byte" Name="Second"/>\n  <opc:Field TypeName="opc:Byte" Name="Hundredths"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetTimeValue">\n  <opc:Field TypeName="tns:BACnetTime" Name="Time"/>\n  <opc:Field TypeName="tns:BACnetTimeValueValue" Name="Value"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetTimeValueValue">\n  <opc:Field TypeName="opc:Boolean" Name="BooleanValue"/>\n  <opc:Field TypeName="ua:Variant" Name="UnsignedValue"/>\n  <opc:Field TypeName="ua:Variant" Name="SignedValue"/>\n  <opc:Field TypeName="opc:ByteString" Name="OctedStringValue"/>\n  <opc:Field TypeName="opc:CharArray" Name="CharStringValue"/>\n  <opc:Field TypeName="opc:UInt32" Name="ObjectIdentifierValue"/>\n  <opc:Field TypeName="opc:Int32" Name="EnumerationValue"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="BitStringValue"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="BACnetWeekNDay">\n  <opc:Field TypeName="tns:BACnetMonth" Name="Month"/>\n  <opc:Field TypeName="tns:BACnetDay" Name="Day"/>\n  <opc:Field TypeName="tns:BACnetDayOfWeek" Name="DayOfWeek"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:OptionSet" Name="BACnetDaysOfWeek">\n  <opc:Field TypeName="opc:ByteString" Name="Value"/>\n  <opc:Field TypeName="opc:ByteString" Name="ValidBits"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:OptionSet" Name="BACnetEventTransitionBits">\n  <opc:Field TypeName="opc:ByteString" Name="Value"/>\n  <opc:Field TypeName="opc:ByteString" Name="ValidBits"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:OptionSet" Name="BACnetLimitEnable">\n  <opc:Field TypeName="opc:ByteString" Name="Value"/>\n  <opc:Field TypeName="opc:ByteString" Name="ValidBits"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:OptionSet" Name="BACnetObjectTypeSupportedBits">\n  <opc:Field TypeName="opc:ByteString" Name="Value"/>\n  <opc:Field TypeName="opc:ByteString" Name="ValidBits"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:OptionSet" Name="BACnetServicesSupportedBits">\n  <opc:Field TypeName="opc:ByteString" Name="Value"/>\n  <opc:Field TypeName="opc:ByteString" Name="ValidBits"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:OptionSet" Name="BACnetStatusFlags">\n  <opc:Field TypeName="opc:ByteString" Name="Value"/>\n  <opc:Field TypeName="opc:ByteString" Name="ValidBits"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:Union" Name="BACnetCalendarEntry">\n  <opc:Field TypeName="opc:UInt32" Name="SwitchField"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetDate" SwitchValue="1" Name="Date"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetDateRange" SwitchValue="2" Name="DateRange"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetWeekNDay" SwitchValue="3" Name="WeekNDay"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:Union" Name="BACnetClientCOV">\n  <opc:Field TypeName="opc:UInt32" Name="SwitchField"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Float" SwitchValue="1" Name="Real-increment"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:Union" Name="BACnetEventParameter">\n  <opc:Field TypeName="opc:UInt32" Name="SwitchField"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetEventParameterChangeOfBitstring" SwitchValue="1" Name="Change-of-bitstring"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetEventParameterChangeOfState" SwitchValue="2" Name="Change-of-state"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetEventParameterChangeOfValue" SwitchValue="3" Name="Change-of-value"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetEventParameterCommandFailure" SwitchValue="4" Name="Command-failure"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetEventParameterFloatingLimit" SwitchValue="5" Name="Floating-limit"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetEventParameterOutOfRange" SwitchValue="6" Name="Out-of-range"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetEventFaultParameterExtended" SwitchValue="7" Name="Extended"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetEventParameterBufferReady" SwitchValue="8" Name="Buffer-ready"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetEventParameterUnsignedRange" SwitchValue="9" Name="Unsigned-range"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetEventParameterDoubleOutOfRange" SwitchValue="10" Name="Double-out-of-range"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetEventParameterSignedOutOfRange" SwitchValue="11" Name="Signed-out-of-range"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetEventParameterUnsignedOutOfRange" SwitchValue="12" Name="Unsigned-out-of-range"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetEventParameterChangeOfCharacterString" SwitchValue="13" Name="Change-of-characterstring"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetEventParameterChangeOfLifeSafety" SwitchValue="14" Name="Change-of-life-safety"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:Union" Name="BACnetEventParameterExtendedParameters">\n  <opc:Field TypeName="opc:UInt32" Name="SwitchField"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Double" SwitchValue="1" Name="Real"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:UInt32" SwitchValue="2" Name="Unsigned"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Boolean" SwitchValue="3" Name="Boolean"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Double" SwitchValue="4" Name="Double"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Int32" SwitchValue="5" Name="NoOfOcted"/>\n  <opc:Field LengthField="NoOfOcted" SwitchField="SwitchField" TypeName="opc:Byte" SwitchValue="5" Name="Octed"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:CharArray" SwitchValue="6" Name="CharacterString"/>\n  <opc:Field SwitchField="SwitchField" TypeName="ua:ExtensionObject" SwitchValue="7" Name="BitString"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:UInt32" SwitchValue="8" Name="Enum"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetDate" SwitchValue="9" Name="Date"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetTime" SwitchValue="10" Name="Time"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:UInt32" SwitchValue="11" Name="ObjectIdentifier"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetDeviceObjectPropertyReference" SwitchValue="12" Name="Reference"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Int32" SwitchValue="13" Name="Integer"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:Union" Name="BACnetFaultParameter">\n  <opc:Field TypeName="opc:UInt32" Name="SwitchField"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetFaultParameterFaultCharacterstring" SwitchValue="1" Name="Fault-characterstring"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetFaultParameterFaultLifeSafety" SwitchValue="2" Name="Fault-life-safety"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetFaultParameterFaultState" SwitchValue="3" Name="Fault-state"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetFaultParameterFaultStatusFlags" SwitchValue="4" Name="Fault-status-flags"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetEventFaultParameterExtended" SwitchValue="5" Name="Fault-extended"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:Union" Name="BACnetMessageClass">\n  <opc:Field TypeName="opc:UInt32" Name="SwitchField"/>\n  <opc:Field SwitchField="SwitchField" TypeName="ua:Variant" SwitchValue="1" Name="Unsigned"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:CharArray" SwitchValue="2" Name="String"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:Union" Name="BACnetPriorityValue">\n  <opc:Field TypeName="opc:UInt32" Name="SwitchField"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Float" SwitchValue="1" Name="Real"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Int32" SwitchValue="2" Name="Enumerated"/>\n  <opc:Field SwitchField="SwitchField" TypeName="ua:Variant" SwitchValue="3" Name="Unsigned"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Boolean" SwitchValue="4" Name="Boolean"/>\n  <opc:Field SwitchField="SwitchField" TypeName="ua:Variant" SwitchValue="5" Name="Signed"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:Double" SwitchValue="6" Name="Double"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:Union" Name="BACnetRecipient">\n  <opc:Field TypeName="opc:UInt32" Name="SwitchField"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:UInt32" SwitchValue="1" Name="Device"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetAddress" SwitchValue="2" Name="Address"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:Union" Name="BACnetSpecialEventPeriod">\n  <opc:Field TypeName="opc:UInt32" Name="SwitchField"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetCalendarEntry" SwitchValue="1" Name="CalendarEntry"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:UInt32" SwitchValue="2" Name="CalendarReference"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:Union" Name="BACnetTimeStamp">\n  <opc:Field TypeName="opc:UInt32" Name="SwitchField"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetTime" SwitchValue="1" Name="Time"/>\n  <opc:Field SwitchField="SwitchField" TypeName="opc:UInt16" SwitchValue="2" Name="SequenceNumber"/>\n  <opc:Field SwitchField="SwitchField" TypeName="tns:BACnetDateTime" SwitchValue="3" Name="DateTime"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetAction">\n  <opc:EnumeratedValue Name="direct" Value="0"/>\n  <opc:EnumeratedValue Name="reverse" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetBackupState">\n  <opc:EnumeratedValue Name="Idle" Value="0"/>\n  <opc:EnumeratedValue Name="Preparing_For_Backup" Value="1"/>\n  <opc:EnumeratedValue Name="Preparing_For_Restore" Value="2"/>\n  <opc:EnumeratedValue Name="Performing_A_Backup" Value="3"/>\n  <opc:EnumeratedValue Name="Performing_A_Restore" Value="4"/>\n  <opc:EnumeratedValue Name="Backup_Failure" Value="5"/>\n  <opc:EnumeratedValue Name="Restore_Failure" Value="6"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetBinaryPV">\n  <opc:EnumeratedValue Name="Inactive" Value="0"/>\n  <opc:EnumeratedValue Name="Active" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetDay">\n  <opc:EnumeratedValue Name="days numbered 1-7" Value="1"/>\n  <opc:EnumeratedValue Name="days numbered 8-14" Value="2"/>\n  <opc:EnumeratedValue Name="days numbered 15-21" Value="3"/>\n  <opc:EnumeratedValue Name="days numbered 22-28" Value="4"/>\n  <opc:EnumeratedValue Name="days numbered 29-31" Value="5"/>\n  <opc:EnumeratedValue Name="last 7 days of this month" Value="6"/>\n  <opc:EnumeratedValue Name="any week of this month" Value="255"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetDayOfMonth">\n  <opc:EnumeratedValue Name="1" Value="1"/>\n  <opc:EnumeratedValue Name="2" Value="2"/>\n  <opc:EnumeratedValue Name="3" Value="3"/>\n  <opc:EnumeratedValue Name="4" Value="4"/>\n  <opc:EnumeratedValue Name="5" Value="5"/>\n  <opc:EnumeratedValue Name="6" Value="6"/>\n  <opc:EnumeratedValue Name="7" Value="7"/>\n  <opc:EnumeratedValue Name="8" Value="8"/>\n  <opc:EnumeratedValue Name="9" Value="9"/>\n  <opc:EnumeratedValue Name="10" Value="10"/>\n  <opc:EnumeratedValue Name="11" Value="11"/>\n  <opc:EnumeratedValue Name="12" Value="12"/>\n  <opc:EnumeratedValue Name="13" Value="13"/>\n  <opc:EnumeratedValue Name="14" Value="14"/>\n  <opc:EnumeratedValue Name="15" Value="15"/>\n  <opc:EnumeratedValue Name="16" Value="16"/>\n  <opc:EnumeratedValue Name="17" Value="17"/>\n  <opc:EnumeratedValue Name="18" Value="18"/>\n  <opc:EnumeratedValue Name="19" Value="19"/>\n  <opc:EnumeratedValue Name="20" Value="20"/>\n  <opc:EnumeratedValue Name="21" Value="21"/>\n  <opc:EnumeratedValue Name="22" Value="22"/>\n  <opc:EnumeratedValue Name="23" Value="23"/>\n  <opc:EnumeratedValue Name="24" Value="24"/>\n  <opc:EnumeratedValue Name="25" Value="25"/>\n  <opc:EnumeratedValue Name="26" Value="26"/>\n  <opc:EnumeratedValue Name="27" Value="27"/>\n  <opc:EnumeratedValue Name="28" Value="28"/>\n  <opc:EnumeratedValue Name="29" Value="29"/>\n  <opc:EnumeratedValue Name="30" Value="30"/>\n  <opc:EnumeratedValue Name="31" Value="31"/>\n  <opc:EnumeratedValue Name="Last day of month" Value="32"/>\n  <opc:EnumeratedValue Name="Odd day of month" Value="33"/>\n  <opc:EnumeratedValue Name="Even day of month" Value="34"/>\n  <opc:EnumeratedValue Name="Unspecified" Value="255"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetDayOfWeek">\n  <opc:EnumeratedValue Name="Monday" Value="1"/>\n  <opc:EnumeratedValue Name="Tuesday" Value="2"/>\n  <opc:EnumeratedValue Name="Wednesday" Value="3"/>\n  <opc:EnumeratedValue Name="Thursday" Value="4"/>\n  <opc:EnumeratedValue Name="Friday" Value="5"/>\n  <opc:EnumeratedValue Name="Saturday" Value="6"/>\n  <opc:EnumeratedValue Name="Sunday" Value="7"/>\n  <opc:EnumeratedValue Name="unspecified" Value="255"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetDeviceCommunicationEnabled">\n  <opc:EnumeratedValue Name="Enable" Value="0"/>\n  <opc:EnumeratedValue Name="Disable" Value="1"/>\n  <opc:EnumeratedValue Name="DisableInitiation" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetDeviceStatus">\n  <opc:EnumeratedValue Name="Operational" Value="0"/>\n  <opc:EnumeratedValue Name="OperationalReadOnly" Value="1"/>\n  <opc:EnumeratedValue Name="DownloadRequired" Value="2"/>\n  <opc:EnumeratedValue Name="DownloadInProgress" Value="3"/>\n  <opc:EnumeratedValue Name="NonOperational" Value="4"/>\n  <opc:EnumeratedValue Name="BackupInProgress" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetEventEnumType">\n  <opc:EnumeratedValue Name="ChangeOfBitstring" Value="0"/>\n  <opc:EnumeratedValue Name="ChangeOfState" Value="1"/>\n  <opc:EnumeratedValue Name="ChangeOfValue" Value="2"/>\n  <opc:EnumeratedValue Name="CommandFailure" Value="3"/>\n  <opc:EnumeratedValue Name="FloatingLimit" Value="4"/>\n  <opc:EnumeratedValue Name="OutOfRange" Value="5"/>\n  <opc:EnumeratedValue Name="ChangeOfLifeSafety" Value="8"/>\n  <opc:EnumeratedValue Name="Extended" Value="9"/>\n  <opc:EnumeratedValue Name="BufferReady" Value="10"/>\n  <opc:EnumeratedValue Name="UnsignedRange" Value="11"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetEventState">\n  <opc:EnumeratedValue Name="Normal" Value="0"/>\n  <opc:EnumeratedValue Name="Fault" Value="1"/>\n  <opc:EnumeratedValue Name="OffNormal" Value="2"/>\n  <opc:EnumeratedValue Name="HighLimit" Value="3"/>\n  <opc:EnumeratedValue Name="LowLimit" Value="4"/>\n  <opc:EnumeratedValue Name="LifeSafetyAlarm" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetEventType">\n  <opc:EnumeratedValue Name="change-of-bitstring" Value="0"/>\n  <opc:EnumeratedValue Name="change-of-state" Value="1"/>\n  <opc:EnumeratedValue Name="change-of-value" Value="2"/>\n  <opc:EnumeratedValue Name="command-failure" Value="3"/>\n  <opc:EnumeratedValue Name="out-of-range" Value="5"/>\n  <opc:EnumeratedValue Name="change-of-life-safety" Value="8"/>\n  <opc:EnumeratedValue Name="floating-limit" Value="4"/>\n  <opc:EnumeratedValue Name="extended" Value="9"/>\n  <opc:EnumeratedValue Name="buffer-ready" Value="10"/>\n  <opc:EnumeratedValue Name="unsigned-range" Value="11"/>\n  <opc:EnumeratedValue Name="access-event" Value="13"/>\n  <opc:EnumeratedValue Name="double-out-of-range" Value="14"/>\n  <opc:EnumeratedValue Name="signed-out-of-range" Value="15"/>\n  <opc:EnumeratedValue Name="unsigned-out-of-range" Value="16"/>\n  <opc:EnumeratedValue Name="change-of-characterstring" Value="17"/>\n  <opc:EnumeratedValue Name="change-of-status-flags" Value="18"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetFaultType">\n  <opc:EnumeratedValue Name="none" Value="0"/>\n  <opc:EnumeratedValue Name="fault-characterstring" Value="1"/>\n  <opc:EnumeratedValue Name="fault-exended" Value="2"/>\n  <opc:EnumeratedValue Name="fault-life-safety" Value="3"/>\n  <opc:EnumeratedValue Name="fault-state" Value="4"/>\n  <opc:EnumeratedValue Name="fault-status-flags" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetLifeSafetyMode">\n  <opc:EnumeratedValue Name="Off" Value="0"/>\n  <opc:EnumeratedValue Name="On" Value="1"/>\n  <opc:EnumeratedValue Name="Test" Value="2"/>\n  <opc:EnumeratedValue Name="Manned" Value="3"/>\n  <opc:EnumeratedValue Name="UnManned" Value="4"/>\n  <opc:EnumeratedValue Name="Armed" Value="5"/>\n  <opc:EnumeratedValue Name="Disarmed" Value="6"/>\n  <opc:EnumeratedValue Name="Prearmed" Value="7"/>\n  <opc:EnumeratedValue Name="Slow" Value="8"/>\n  <opc:EnumeratedValue Name="Fast" Value="9"/>\n  <opc:EnumeratedValue Name="Disconnected" Value="10"/>\n  <opc:EnumeratedValue Name="Enabled" Value="11"/>\n  <opc:EnumeratedValue Name="Disabled" Value="12"/>\n  <opc:EnumeratedValue Name="AutomaticReleaseDisabled" Value="13"/>\n  <opc:EnumeratedValue Name="Default" Value="14"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetLifeSafetyOperation">\n  <opc:EnumeratedValue Name="None" Value="0"/>\n  <opc:EnumeratedValue Name="Silence" Value="1"/>\n  <opc:EnumeratedValue Name="SilenceAudible" Value="2"/>\n  <opc:EnumeratedValue Name="SilenceVisible" Value="3"/>\n  <opc:EnumeratedValue Name="Reset" Value="4"/>\n  <opc:EnumeratedValue Name="ResetAlarm" Value="5"/>\n  <opc:EnumeratedValue Name="ResetFault" Value="6"/>\n  <opc:EnumeratedValue Name="Unsilence" Value="7"/>\n  <opc:EnumeratedValue Name="UnsilenceAudible" Value="8"/>\n  <opc:EnumeratedValue Name="UnsilenceVisible" Value="9"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetLifeSafetyState">\n  <opc:EnumeratedValue Name="Quiet" Value="0"/>\n  <opc:EnumeratedValue Name="PreAlarm" Value="1"/>\n  <opc:EnumeratedValue Name="Alarm" Value="2"/>\n  <opc:EnumeratedValue Name="Fault" Value="3"/>\n  <opc:EnumeratedValue Name="FaultPreAlarm" Value="4"/>\n  <opc:EnumeratedValue Name="FaultAlarm" Value="5"/>\n  <opc:EnumeratedValue Name="NotReady" Value="6"/>\n  <opc:EnumeratedValue Name="Active" Value="7"/>\n  <opc:EnumeratedValue Name="Tamper" Value="8"/>\n  <opc:EnumeratedValue Name="TestAlarm" Value="9"/>\n  <opc:EnumeratedValue Name="TestActive" Value="10"/>\n  <opc:EnumeratedValue Name="TestFault" Value="11"/>\n  <opc:EnumeratedValue Name="TestFaultAlarm" Value="12"/>\n  <opc:EnumeratedValue Name="Holdup" Value="13"/>\n  <opc:EnumeratedValue Name="Duress" Value="14"/>\n  <opc:EnumeratedValue Name="TamperAlarm" Value="15"/>\n  <opc:EnumeratedValue Name="Abnormal" Value="16"/>\n  <opc:EnumeratedValue Name="EmergencyPower" Value="17"/>\n  <opc:EnumeratedValue Name="Delayed" Value="18"/>\n  <opc:EnumeratedValue Name="Blocked" Value="19"/>\n  <opc:EnumeratedValue Name="LocalAlarm" Value="20"/>\n  <opc:EnumeratedValue Name="GeneralAlarm" Value="21"/>\n  <opc:EnumeratedValue Name="Supervisory" Value="22"/>\n  <opc:EnumeratedValue Name="TestSupervisory" Value="23"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetLoggingType">\n  <opc:EnumeratedValue Name="Polled" Value="0"/>\n  <opc:EnumeratedValue Name="COV" Value="1"/>\n  <opc:EnumeratedValue Name="Triggered" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetMessagePriority">\n  <opc:EnumeratedValue Name="normal" Value="0"/>\n  <opc:EnumeratedValue Name="urgent" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetMonth">\n  <opc:EnumeratedValue Name="January" Value="1"/>\n  <opc:EnumeratedValue Name="February" Value="2"/>\n  <opc:EnumeratedValue Name="March" Value="3"/>\n  <opc:EnumeratedValue Name="April" Value="4"/>\n  <opc:EnumeratedValue Name="May" Value="5"/>\n  <opc:EnumeratedValue Name="June" Value="6"/>\n  <opc:EnumeratedValue Name="July" Value="7"/>\n  <opc:EnumeratedValue Name="August" Value="8"/>\n  <opc:EnumeratedValue Name="September" Value="9"/>\n  <opc:EnumeratedValue Name="October" Value="10"/>\n  <opc:EnumeratedValue Name="November" Value="11"/>\n  <opc:EnumeratedValue Name="December" Value="12"/>\n  <opc:EnumeratedValue Name="Odd" Value="13"/>\n  <opc:EnumeratedValue Name="Even" Value="14"/>\n  <opc:EnumeratedValue Name="Unspecified" Value="255"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetNodeType">\n  <opc:EnumeratedValue Name="UNKNOWN" Value="0"/>\n  <opc:EnumeratedValue Name="SYSTEM" Value="1"/>\n  <opc:EnumeratedValue Name="NETWORK" Value="2"/>\n  <opc:EnumeratedValue Name="DEVICE" Value="3"/>\n  <opc:EnumeratedValue Name="ORGANIZATIONAL" Value="4"/>\n  <opc:EnumeratedValue Name="AREA" Value="5"/>\n  <opc:EnumeratedValue Name="EQUIPMENT" Value="6"/>\n  <opc:EnumeratedValue Name="POINT" Value="7"/>\n  <opc:EnumeratedValue Name="COLLECTION" Value="8"/>\n  <opc:EnumeratedValue Name="PROPERTY" Value="9"/>\n  <opc:EnumeratedValue Name="FUNCTIONAL" Value="10"/>\n  <opc:EnumeratedValue Name="OTHER" Value="11"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetNotifyType">\n  <opc:EnumeratedValue Name="Alarm" Value="0"/>\n  <opc:EnumeratedValue Name="Event" Value="1"/>\n  <opc:EnumeratedValue Name="AckNotification" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetObjectTypeEnum">\n  <opc:EnumeratedValue Name="analog-input" Value="0"/>\n  <opc:EnumeratedValue Name="analog-output" Value="1"/>\n  <opc:EnumeratedValue Name="analog-value" Value="2"/>\n  <opc:EnumeratedValue Name="binary-input" Value="3"/>\n  <opc:EnumeratedValue Name="binary-output" Value="4"/>\n  <opc:EnumeratedValue Name="binary-value" Value="5"/>\n  <opc:EnumeratedValue Name="calendar" Value="6"/>\n  <opc:EnumeratedValue Name="command" Value="7"/>\n  <opc:EnumeratedValue Name="device" Value="8"/>\n  <opc:EnumeratedValue Name="event-enrollment" Value="9"/>\n  <opc:EnumeratedValue Name="file" Value="10"/>\n  <opc:EnumeratedValue Name="group" Value="11"/>\n  <opc:EnumeratedValue Name="loop" Value="12"/>\n  <opc:EnumeratedValue Name="multi-state-input" Value="13"/>\n  <opc:EnumeratedValue Name="multi-state-output" Value="14"/>\n  <opc:EnumeratedValue Name="notification-class" Value="15"/>\n  <opc:EnumeratedValue Name="program" Value="16"/>\n  <opc:EnumeratedValue Name="schedule" Value="17"/>\n  <opc:EnumeratedValue Name="averaging" Value="18"/>\n  <opc:EnumeratedValue Name="multi-state-value" Value="19"/>\n  <opc:EnumeratedValue Name="trend-log" Value="20"/>\n  <opc:EnumeratedValue Name="life-safety-point" Value="21"/>\n  <opc:EnumeratedValue Name="life-safety-zone" Value="22"/>\n  <opc:EnumeratedValue Name="accumulator" Value="23"/>\n  <opc:EnumeratedValue Name="pulse-converter" Value="24"/>\n  <opc:EnumeratedValue Name="event-log" Value="25"/>\n  <opc:EnumeratedValue Name="global-group" Value="26"/>\n  <opc:EnumeratedValue Name="trend-log-multiple" Value="27"/>\n  <opc:EnumeratedValue Name="load-control" Value="28"/>\n  <opc:EnumeratedValue Name="structured-view" Value="29"/>\n  <opc:EnumeratedValue Name="access-door" Value="30"/>\n  <opc:EnumeratedValue Name="unassigned" Value="31"/>\n  <opc:EnumeratedValue Name="access-credential" Value="32"/>\n  <opc:EnumeratedValue Name="access-point" Value="33"/>\n  <opc:EnumeratedValue Name="access-rights" Value="34"/>\n  <opc:EnumeratedValue Name="access-user" Value="35"/>\n  <opc:EnumeratedValue Name="access-zone" Value="36"/>\n  <opc:EnumeratedValue Name="credentional-data-input" Value="37"/>\n  <opc:EnumeratedValue Name="network-security" Value="38"/>\n  <opc:EnumeratedValue Name="bitstring-value" Value="39"/>\n  <opc:EnumeratedValue Name="characterstring-value" Value="40"/>\n  <opc:EnumeratedValue Name="date-pattern-value" Value="41"/>\n  <opc:EnumeratedValue Name="date-value" Value="42"/>\n  <opc:EnumeratedValue Name="datetime-pattern-value" Value="43"/>\n  <opc:EnumeratedValue Name="datetime-value" Value="44"/>\n  <opc:EnumeratedValue Name="integer-value" Value="45"/>\n  <opc:EnumeratedValue Name="large-analog-value" Value="46"/>\n  <opc:EnumeratedValue Name="octetstring-value" Value="47"/>\n  <opc:EnumeratedValue Name="positive-integer-value" Value="48"/>\n  <opc:EnumeratedValue Name="time-pattern-value" Value="49"/>\n  <opc:EnumeratedValue Name="time-value" Value="50"/>\n  <opc:EnumeratedValue Name="notification-forwarder" Value="51"/>\n  <opc:EnumeratedValue Name="alert-enrollment" Value="52"/>\n  <opc:EnumeratedValue Name="channel" Value="53"/>\n  <opc:EnumeratedValue Name="lighting-output" Value="54"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetPolarity">\n  <opc:EnumeratedValue Name="Normal" Value="0"/>\n  <opc:EnumeratedValue Name="Reverse" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetProgramError">\n  <opc:EnumeratedValue Name="Normal" Value="0"/>\n  <opc:EnumeratedValue Name="LoadFailed" Value="1"/>\n  <opc:EnumeratedValue Name="Internal" Value="2"/>\n  <opc:EnumeratedValue Name="Program" Value="3"/>\n  <opc:EnumeratedValue Name="Other" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetProgramRequest">\n  <opc:EnumeratedValue Name="Ready" Value="0"/>\n  <opc:EnumeratedValue Name="Load" Value="1"/>\n  <opc:EnumeratedValue Name="Run" Value="2"/>\n  <opc:EnumeratedValue Name="Halt" Value="3"/>\n  <opc:EnumeratedValue Name="Restart" Value="4"/>\n  <opc:EnumeratedValue Name="Unload" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetProgramStates">\n  <opc:EnumeratedValue Name="Idle" Value="0"/>\n  <opc:EnumeratedValue Name="Loading" Value="1"/>\n  <opc:EnumeratedValue Name="Running" Value="2"/>\n  <opc:EnumeratedValue Name="Waiting" Value="3"/>\n  <opc:EnumeratedValue Name="Halted" Value="4"/>\n  <opc:EnumeratedValue Name="Unloading" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetPropertyIdentifier">\n  <opc:EnumeratedValue Name="AckedTransitions" Value="0"/>\n  <opc:EnumeratedValue Name="AckRequired" Value="1"/>\n  <opc:EnumeratedValue Name="Action" Value="2"/>\n  <opc:EnumeratedValue Name="ActionText" Value="3"/>\n  <opc:EnumeratedValue Name="ActiveText" Value="4"/>\n  <opc:EnumeratedValue Name="ActiveVtSessions" Value="5"/>\n  <opc:EnumeratedValue Name="AlarmValue" Value="6"/>\n  <opc:EnumeratedValue Name="AlarmValues" Value="7"/>\n  <opc:EnumeratedValue Name="All" Value="8"/>\n  <opc:EnumeratedValue Name="AllWritesSuccessful" Value="9"/>\n  <opc:EnumeratedValue Name="ApduSegmentTimeout" Value="10"/>\n  <opc:EnumeratedValue Name="ApduTimeout" Value="11"/>\n  <opc:EnumeratedValue Name="ApplicationSoftwareVersion" Value="12"/>\n  <opc:EnumeratedValue Name="Archive" Value="13"/>\n  <opc:EnumeratedValue Name="Bias" Value="14"/>\n  <opc:EnumeratedValue Name="ChangeOfStateCount" Value="15"/>\n  <opc:EnumeratedValue Name="ChangeOfStateTime" Value="16"/>\n  <opc:EnumeratedValue Name="NotificationClass" Value="17"/>\n  <opc:EnumeratedValue Name="this property deleted" Value="18"/>\n  <opc:EnumeratedValue Name="ControlledVariableReference" Value="19"/>\n  <opc:EnumeratedValue Name="ControlledVariableUnits" Value="20"/>\n  <opc:EnumeratedValue Name="ControlledVariableValue" Value="21"/>\n  <opc:EnumeratedValue Name="CovIncrement" Value="22"/>\n  <opc:EnumeratedValue Name="DateList" Value="23"/>\n  <opc:EnumeratedValue Name="DaylightSavingsStatus" Value="24"/>\n  <opc:EnumeratedValue Name="Deadband" Value="25"/>\n  <opc:EnumeratedValue Name="DerivativeConstant" Value="26"/>\n  <opc:EnumeratedValue Name="DerivativeConstantUnits" Value="27"/>\n  <opc:EnumeratedValue Name="Description" Value="28"/>\n  <opc:EnumeratedValue Name="DescriptionOfHalt" Value="29"/>\n  <opc:EnumeratedValue Name="DeviceAddressBinding" Value="30"/>\n  <opc:EnumeratedValue Name="DeviceType" Value="31"/>\n  <opc:EnumeratedValue Name="EffectivePeriod" Value="32"/>\n  <opc:EnumeratedValue Name="ElapsedActiveTime" Value="33"/>\n  <opc:EnumeratedValue Name="ErrorLimit" Value="34"/>\n  <opc:EnumeratedValue Name="EventEnable" Value="35"/>\n  <opc:EnumeratedValue Name="EventState" Value="36"/>\n  <opc:EnumeratedValue Name="EventType" Value="37"/>\n  <opc:EnumeratedValue Name="ExceptionSchedule" Value="38"/>\n  <opc:EnumeratedValue Name="FaultValues" Value="39"/>\n  <opc:EnumeratedValue Name="FeedbackValue" Value="40"/>\n  <opc:EnumeratedValue Name="FileAccessMethod" Value="41"/>\n  <opc:EnumeratedValue Name="FileSize" Value="42"/>\n  <opc:EnumeratedValue Name="FileType" Value="43"/>\n  <opc:EnumeratedValue Name="FirmwareRevision" Value="44"/>\n  <opc:EnumeratedValue Name="HighLimit" Value="45"/>\n  <opc:EnumeratedValue Name="InactiveText" Value="46"/>\n  <opc:EnumeratedValue Name="InProcess" Value="47"/>\n  <opc:EnumeratedValue Name="InstanceOf" Value="48"/>\n  <opc:EnumeratedValue Name="IntegralConstant" Value="49"/>\n  <opc:EnumeratedValue Name="IntegralConstantUnits" Value="50"/>\n  <opc:EnumeratedValue Name="Removed In Version 1 Revision 4_51" Value="51"/>\n  <opc:EnumeratedValue Name="LimitEnable" Value="52"/>\n  <opc:EnumeratedValue Name="ListOfGroupMembers" Value="53"/>\n  <opc:EnumeratedValue Name="ListOfObjectPropertyReferences" Value="54"/>\n  <opc:EnumeratedValue Name="Unassigned_55" Value="55"/>\n  <opc:EnumeratedValue Name="LocalDate" Value="56"/>\n  <opc:EnumeratedValue Name="LocalTime" Value="57"/>\n  <opc:EnumeratedValue Name="Location" Value="58"/>\n  <opc:EnumeratedValue Name="LowLimit" Value="59"/>\n  <opc:EnumeratedValue Name="ManipulatedVariableReference" Value="60"/>\n  <opc:EnumeratedValue Name="MaximumOutput" Value="61"/>\n  <opc:EnumeratedValue Name="MaxApduLengthAccepted" Value="62"/>\n  <opc:EnumeratedValue Name="MaxInfoFrames" Value="63"/>\n  <opc:EnumeratedValue Name="MaxMaster" Value="64"/>\n  <opc:EnumeratedValue Name="MaxPresValue" Value="65"/>\n  <opc:EnumeratedValue Name="MinimumOffTime" Value="66"/>\n  <opc:EnumeratedValue Name="MinimumOnTime" Value="67"/>\n  <opc:EnumeratedValue Name="MinimumOutput" Value="68"/>\n  <opc:EnumeratedValue Name="MinPresValue" Value="69"/>\n  <opc:EnumeratedValue Name="ModelName" Value="70"/>\n  <opc:EnumeratedValue Name="ModificationDate" Value="71"/>\n  <opc:EnumeratedValue Name="NotifyType" Value="72"/>\n  <opc:EnumeratedValue Name="NumberOfApduRetries" Value="73"/>\n  <opc:EnumeratedValue Name="NumberOfStates" Value="74"/>\n  <opc:EnumeratedValue Name="ObjectIdentifier" Value="75"/>\n  <opc:EnumeratedValue Name="ObjectList" Value="76"/>\n  <opc:EnumeratedValue Name="ObjectName" Value="77"/>\n  <opc:EnumeratedValue Name="ObjectPropertyReference" Value="78"/>\n  <opc:EnumeratedValue Name="ObjectType" Value="79"/>\n  <opc:EnumeratedValue Name="Optional" Value="80"/>\n  <opc:EnumeratedValue Name="OutOfService" Value="81"/>\n  <opc:EnumeratedValue Name="OutputUnits" Value="82"/>\n  <opc:EnumeratedValue Name="EventParameters" Value="83"/>\n  <opc:EnumeratedValue Name="Polarity" Value="84"/>\n  <opc:EnumeratedValue Name="PresentValue" Value="85"/>\n  <opc:EnumeratedValue Name="Priority" Value="86"/>\n  <opc:EnumeratedValue Name="PriorityArray" Value="87"/>\n  <opc:EnumeratedValue Name="PriorityForWriting" Value="88"/>\n  <opc:EnumeratedValue Name="ProcessIdentifier" Value="89"/>\n  <opc:EnumeratedValue Name="ProgramChange" Value="90"/>\n  <opc:EnumeratedValue Name="ProgramLocation" Value="91"/>\n  <opc:EnumeratedValue Name="ProgramState" Value="92"/>\n  <opc:EnumeratedValue Name="ProportionalConstant" Value="93"/>\n  <opc:EnumeratedValue Name="ProportionalConstantUnits" Value="94"/>\n  <opc:EnumeratedValue Name="Removed In Version 1 Revision 2_95" Value="95"/>\n  <opc:EnumeratedValue Name="ProtocolObjectTypesSupported" Value="96"/>\n  <opc:EnumeratedValue Name="ProtocolServicesSupported" Value="97"/>\n  <opc:EnumeratedValue Name="ProtocolVersion" Value="98"/>\n  <opc:EnumeratedValue Name="ReadOnly" Value="99"/>\n  <opc:EnumeratedValue Name="ReasonForHalt" Value="100"/>\n  <opc:EnumeratedValue Name="Removed In Version 1 Revision 4_101" Value="101"/>\n  <opc:EnumeratedValue Name="RecipientList" Value="102"/>\n  <opc:EnumeratedValue Name="Reliability" Value="103"/>\n  <opc:EnumeratedValue Name="RelinquishDefault" Value="104"/>\n  <opc:EnumeratedValue Name="Required" Value="105"/>\n  <opc:EnumeratedValue Name="Resolution" Value="106"/>\n  <opc:EnumeratedValue Name="SegmentationSupported" Value="107"/>\n  <opc:EnumeratedValue Name="Setpoint" Value="108"/>\n  <opc:EnumeratedValue Name="SetpointReference" Value="109"/>\n  <opc:EnumeratedValue Name="StateText" Value="110"/>\n  <opc:EnumeratedValue Name="StatusFlags" Value="111"/>\n  <opc:EnumeratedValue Name="SystemStatus" Value="112"/>\n  <opc:EnumeratedValue Name="TimeDelay" Value="113"/>\n  <opc:EnumeratedValue Name="TimeOfActiveTimeReset" Value="114"/>\n  <opc:EnumeratedValue Name="TimeOfStateCountReset" Value="115"/>\n  <opc:EnumeratedValue Name="TimeSynchronizationRecipients" Value="116"/>\n  <opc:EnumeratedValue Name="Units" Value="117"/>\n  <opc:EnumeratedValue Name="UpdateInterval" Value="118"/>\n  <opc:EnumeratedValue Name="UtcOffset" Value="119"/>\n  <opc:EnumeratedValue Name="VendorIdentifier" Value="120"/>\n  <opc:EnumeratedValue Name="VendorName" Value="121"/>\n  <opc:EnumeratedValue Name="VtClassesSupported" Value="122"/>\n  <opc:EnumeratedValue Name="WeeklySchedule" Value="123"/>\n  <opc:EnumeratedValue Name="AttemptedSamples" Value="124"/>\n  <opc:EnumeratedValue Name="AverageValue" Value="125"/>\n  <opc:EnumeratedValue Name="BufferSize" Value="126"/>\n  <opc:EnumeratedValue Name="ClientCovIncrement" Value="127"/>\n  <opc:EnumeratedValue Name="CovResubscriptionInterval" Value="128"/>\n  <opc:EnumeratedValue Name="Removed In Version 1 Revision 3_129" Value="129"/>\n  <opc:EnumeratedValue Name="EventTimeStamps" Value="130"/>\n  <opc:EnumeratedValue Name="LogBuffer" Value="131"/>\n  <opc:EnumeratedValue Name="LogDeviceObjectProperty" Value="132"/>\n  <opc:EnumeratedValue Name="Enable" Value="133"/>\n  <opc:EnumeratedValue Name="LogInterval" Value="134"/>\n  <opc:EnumeratedValue Name="MaximumValue" Value="135"/>\n  <opc:EnumeratedValue Name="MinimumValue" Value="136"/>\n  <opc:EnumeratedValue Name="NotificationThreshold" Value="137"/>\n  <opc:EnumeratedValue Name="Removed In Version 1 Revision 3_138" Value="138"/>\n  <opc:EnumeratedValue Name="ProtocolRevision" Value="139"/>\n  <opc:EnumeratedValue Name="RecordsSinceNotification" Value="140"/>\n  <opc:EnumeratedValue Name="RecordCount" Value="141"/>\n  <opc:EnumeratedValue Name="StartTime" Value="142"/>\n  <opc:EnumeratedValue Name="StopTime" Value="143"/>\n  <opc:EnumeratedValue Name="StopWhenFull" Value="144"/>\n  <opc:EnumeratedValue Name="TotalRecordCount" Value="145"/>\n  <opc:EnumeratedValue Name="ValidSamples" Value="146"/>\n  <opc:EnumeratedValue Name="WindowInterval" Value="147"/>\n  <opc:EnumeratedValue Name="WindowSamples" Value="148"/>\n  <opc:EnumeratedValue Name="MaximumValueTimestamp" Value="149"/>\n  <opc:EnumeratedValue Name="MinimumValueTimestamp" Value="150"/>\n  <opc:EnumeratedValue Name="VarianceValue" Value="151"/>\n  <opc:EnumeratedValue Name="ActiveCovSubscriptions" Value="152"/>\n  <opc:EnumeratedValue Name="BackupFailureTimeout" Value="153"/>\n  <opc:EnumeratedValue Name="ConfigurationFiles" Value="154"/>\n  <opc:EnumeratedValue Name="DatabaseRevision" Value="155"/>\n  <opc:EnumeratedValue Name="DirectReading" Value="156"/>\n  <opc:EnumeratedValue Name="LastRestoreTime" Value="157"/>\n  <opc:EnumeratedValue Name="MaintenanceRequired" Value="158"/>\n  <opc:EnumeratedValue Name="MemberOf" Value="159"/>\n  <opc:EnumeratedValue Name="Mode" Value="160"/>\n  <opc:EnumeratedValue Name="OperationExpected" Value="161"/>\n  <opc:EnumeratedValue Name="Setting" Value="162"/>\n  <opc:EnumeratedValue Name="Silenced" Value="163"/>\n  <opc:EnumeratedValue Name="TrackingValue" Value="164"/>\n  <opc:EnumeratedValue Name="ZoneMembers" Value="165"/>\n  <opc:EnumeratedValue Name="LifeSafetyAlarmValues" Value="166"/>\n  <opc:EnumeratedValue Name="MaxSegmentsAccepted" Value="167"/>\n  <opc:EnumeratedValue Name="ProfileName" Value="168"/>\n  <opc:EnumeratedValue Name="AutoSlaveDiscovery" Value="169"/>\n  <opc:EnumeratedValue Name="ManualSlaveAddressBinding" Value="170"/>\n  <opc:EnumeratedValue Name="SlaveAddressBinding" Value="171"/>\n  <opc:EnumeratedValue Name="SlaveProxyEnable" Value="172"/>\n  <opc:EnumeratedValue Name="LastNotifyRecord" Value="173"/>\n  <opc:EnumeratedValue Name="ScheduleDefault" Value="174"/>\n  <opc:EnumeratedValue Name="AcceptedModes" Value="175"/>\n  <opc:EnumeratedValue Name="AdjustValue" Value="176"/>\n  <opc:EnumeratedValue Name="Count" Value="177"/>\n  <opc:EnumeratedValue Name="CountBeforeChange" Value="178"/>\n  <opc:EnumeratedValue Name="CountChangeTime" Value="179"/>\n  <opc:EnumeratedValue Name="CovPeriod" Value="180"/>\n  <opc:EnumeratedValue Name="InputReference" Value="181"/>\n  <opc:EnumeratedValue Name="LimitMonitoringInterval" Value="182"/>\n  <opc:EnumeratedValue Name="LoggingObject" Value="183"/>\n  <opc:EnumeratedValue Name="LoggingRecord" Value="184"/>\n  <opc:EnumeratedValue Name="Prescale" Value="185"/>\n  <opc:EnumeratedValue Name="PulseRate" Value="186"/>\n  <opc:EnumeratedValue Name="Scale" Value="187"/>\n  <opc:EnumeratedValue Name="ScaleFactor" Value="188"/>\n  <opc:EnumeratedValue Name="UpdateTime" Value="189"/>\n  <opc:EnumeratedValue Name="ValueBeforeChange" Value="190"/>\n  <opc:EnumeratedValue Name="ValueSet" Value="191"/>\n  <opc:EnumeratedValue Name="ValueChangeTime" Value="192"/>\n  <opc:EnumeratedValue Name="AlignIntervals" Value="193"/>\n  <opc:EnumeratedValue Name="Unassigned_194" Value="194"/>\n  <opc:EnumeratedValue Name="IntervalOffset" Value="195"/>\n  <opc:EnumeratedValue Name="LastRestartReason" Value="196"/>\n  <opc:EnumeratedValue Name="LoggingType" Value="197"/>\n  <opc:EnumeratedValue Name="Unassigned_198" Value="198"/>\n  <opc:EnumeratedValue Name="Unassigned_199" Value="199"/>\n  <opc:EnumeratedValue Name="Unassigned_200" Value="200"/>\n  <opc:EnumeratedValue Name="Unassigned_201" Value="201"/>\n  <opc:EnumeratedValue Name="RestartNotificationRecipients" Value="202"/>\n  <opc:EnumeratedValue Name="TimeOfDeviceRestart" Value="203"/>\n  <opc:EnumeratedValue Name="TimeSynchronizationInterval" Value="204"/>\n  <opc:EnumeratedValue Name="Trigger" Value="205"/>\n  <opc:EnumeratedValue Name="UtcTimeSynchronizationRecipients" Value="206"/>\n  <opc:EnumeratedValue Name="NodeSubtype" Value="207"/>\n  <opc:EnumeratedValue Name="NodeType" Value="208"/>\n  <opc:EnumeratedValue Name="StructuredObjectList" Value="209"/>\n  <opc:EnumeratedValue Name="SubordinateAnnotations" Value="210"/>\n  <opc:EnumeratedValue Name="SubordinateList" Value="211"/>\n  <opc:EnumeratedValue Name="ActualShedLevel" Value="212"/>\n  <opc:EnumeratedValue Name="DutyWindow" Value="213"/>\n  <opc:EnumeratedValue Name="ExpectedShedLevel" Value="214"/>\n  <opc:EnumeratedValue Name="FullDutyBaseline" Value="215"/>\n  <opc:EnumeratedValue Name="Unassigned_216" Value="216"/>\n  <opc:EnumeratedValue Name="Unassigned_217" Value="217"/>\n  <opc:EnumeratedValue Name="RequestedShedLevel" Value="218"/>\n  <opc:EnumeratedValue Name="ShedDuration" Value="219"/>\n  <opc:EnumeratedValue Name="ShedLevelDescriptions" Value="220"/>\n  <opc:EnumeratedValue Name="ShedLevels" Value="221"/>\n  <opc:EnumeratedValue Name="StateDescription" Value="222"/>\n  <opc:EnumeratedValue Name="Unassigned_223" Value="223"/>\n  <opc:EnumeratedValue Name="Unassigned_224" Value="224"/>\n  <opc:EnumeratedValue Name="Unassigned_225" Value="225"/>\n  <opc:EnumeratedValue Name="DoorAlarmState" Value="226"/>\n  <opc:EnumeratedValue Name="DoorExtendedPulseTime" Value="227"/>\n  <opc:EnumeratedValue Name="DoorMembers" Value="228"/>\n  <opc:EnumeratedValue Name="DoorOpenTooLongTime" Value="229"/>\n  <opc:EnumeratedValue Name="DoorPulseTime" Value="230"/>\n  <opc:EnumeratedValue Name="DoorStatus" Value="231"/>\n  <opc:EnumeratedValue Name="DoorUnlockDelayTime" Value="232"/>\n  <opc:EnumeratedValue Name="LockStatus" Value="233"/>\n  <opc:EnumeratedValue Name="MaskedAlarmValues" Value="234"/>\n  <opc:EnumeratedValue Name="SecuredStatus" Value="235"/>\n  <opc:EnumeratedValue Name="Unassigned_236" Value="236"/>\n  <opc:EnumeratedValue Name="Unassigned_237" Value="237"/>\n  <opc:EnumeratedValue Name="Unassigned_238" Value="238"/>\n  <opc:EnumeratedValue Name="Unassigned_239" Value="239"/>\n  <opc:EnumeratedValue Name="Unassigned_240" Value="240"/>\n  <opc:EnumeratedValue Name="Unassigned_241" Value="241"/>\n  <opc:EnumeratedValue Name="Unassigned_242" Value="242"/>\n  <opc:EnumeratedValue Name="Unassigned_243" Value="243"/>\n  <opc:EnumeratedValue Name="AbsenteeLimit" Value="244"/>\n  <opc:EnumeratedValue Name="AccessAlarmEvents" Value="245"/>\n  <opc:EnumeratedValue Name="AccessDoors" Value="246"/>\n  <opc:EnumeratedValue Name="AccessEvent" Value="247"/>\n  <opc:EnumeratedValue Name="AccessEventAuthenticationFactor" Value="248"/>\n  <opc:EnumeratedValue Name="AccessEventCredential" Value="249"/>\n  <opc:EnumeratedValue Name="AccessEventTime" Value="250"/>\n  <opc:EnumeratedValue Name="AccessTransactionEvents" Value="251"/>\n  <opc:EnumeratedValue Name="Accompaniment" Value="252"/>\n  <opc:EnumeratedValue Name="AccompanimentTime" Value="253"/>\n  <opc:EnumeratedValue Name="ActivationTime" Value="254"/>\n  <opc:EnumeratedValue Name="ActiveAuthenticationPolicy" Value="255"/>\n  <opc:EnumeratedValue Name="AssignedAccessRights" Value="256"/>\n  <opc:EnumeratedValue Name="AuthenticationFactors" Value="257"/>\n  <opc:EnumeratedValue Name="AuthenticationPolicyList" Value="258"/>\n  <opc:EnumeratedValue Name="AuthenticationPolicyNames" Value="259"/>\n  <opc:EnumeratedValue Name="AuthenticationStatus" Value="260"/>\n  <opc:EnumeratedValue Name="AuthorizationMode" Value="261"/>\n  <opc:EnumeratedValue Name="BelongsTo" Value="262"/>\n  <opc:EnumeratedValue Name="CredentialDisable" Value="263"/>\n  <opc:EnumeratedValue Name="CredentialStatus" Value="264"/>\n  <opc:EnumeratedValue Name="Credentials" Value="265"/>\n  <opc:EnumeratedValue Name="CredentialsInZone" Value="266"/>\n  <opc:EnumeratedValue Name="DaysRemaining" Value="267"/>\n  <opc:EnumeratedValue Name="EntryPoints" Value="268"/>\n  <opc:EnumeratedValue Name="ExitPoints" Value="269"/>\n  <opc:EnumeratedValue Name="ExpiryTime" Value="270"/>\n  <opc:EnumeratedValue Name="ExtendedTimeEnable" Value="271"/>\n  <opc:EnumeratedValue Name="FailedAttemptEvents" Value="272"/>\n  <opc:EnumeratedValue Name="FailedAttempts" Value="273"/>\n  <opc:EnumeratedValue Name="FailedAttemptsTime" Value="274"/>\n  <opc:EnumeratedValue Name="LastAccessEvent" Value="275"/>\n  <opc:EnumeratedValue Name="LastAccessPoint" Value="276"/>\n  <opc:EnumeratedValue Name="LastCredentialAdded" Value="277"/>\n  <opc:EnumeratedValue Name="LastCredentialAddedTime" Value="278"/>\n  <opc:EnumeratedValue Name="LastCredentialRemoved" Value="279"/>\n  <opc:EnumeratedValue Name="LastCredentialRemovedTime" Value="280"/>\n  <opc:EnumeratedValue Name="LastUseTime" Value="281"/>\n  <opc:EnumeratedValue Name="Lockout" Value="282"/>\n  <opc:EnumeratedValue Name="LockoutRelinquishTime" Value="283"/>\n  <opc:EnumeratedValue Name="Removed In Version 1 Revision 13_284" Value="284"/>\n  <opc:EnumeratedValue Name="MaxFailedAttempts" Value="285"/>\n  <opc:EnumeratedValue Name="Members" Value="286"/>\n  <opc:EnumeratedValue Name="MusterPoint" Value="287"/>\n  <opc:EnumeratedValue Name="NegativeAccessRules" Value="288"/>\n  <opc:EnumeratedValue Name="NumberOfAuthenticationPolicies" Value="289"/>\n  <opc:EnumeratedValue Name="OccupancyCount" Value="290"/>\n  <opc:EnumeratedValue Name="OccupancyCountAdjust" Value="291"/>\n  <opc:EnumeratedValue Name="OccupancyCountEnable" Value="292"/>\n  <opc:EnumeratedValue Name="Removed In Version 1 Revision 13_293" Value="293"/>\n  <opc:EnumeratedValue Name="OccupancyLowerLimit" Value="294"/>\n  <opc:EnumeratedValue Name="OccupancyLowerLimitEnforced" Value="295"/>\n  <opc:EnumeratedValue Name="OccupancyState" Value="296"/>\n  <opc:EnumeratedValue Name="OccupancyUpperLimit" Value="297"/>\n  <opc:EnumeratedValue Name="OccupancyUpperLimitEnforced" Value="298"/>\n  <opc:EnumeratedValue Name="Removed In Version 1 Revision 13_299" Value="299"/>\n  <opc:EnumeratedValue Name="PassbackMode" Value="300"/>\n  <opc:EnumeratedValue Name="PassbackTimeout" Value="301"/>\n  <opc:EnumeratedValue Name="PositiveAccessRules" Value="302"/>\n  <opc:EnumeratedValue Name="ReasonForDisable" Value="303"/>\n  <opc:EnumeratedValue Name="SupportedFormats" Value="304"/>\n  <opc:EnumeratedValue Name="SupportedFormatClasses" Value="305"/>\n  <opc:EnumeratedValue Name="ThreatAuthority" Value="306"/>\n  <opc:EnumeratedValue Name="ThreatLevel" Value="307"/>\n  <opc:EnumeratedValue Name="TraceFlag" Value="308"/>\n  <opc:EnumeratedValue Name="TransactionNotificationClass" Value="309"/>\n  <opc:EnumeratedValue Name="UserExternalIdentifier" Value="310"/>\n  <opc:EnumeratedValue Name="UserInformationReference" Value="311"/>\n  <opc:EnumeratedValue Name="Unassigned_312" Value="312"/>\n  <opc:EnumeratedValue Name="Unassigned_313" Value="313"/>\n  <opc:EnumeratedValue Name="Unassigned_314" Value="314"/>\n  <opc:EnumeratedValue Name="Unassigned_315" Value="315"/>\n  <opc:EnumeratedValue Name="Unassigned_316" Value="316"/>\n  <opc:EnumeratedValue Name="UserName" Value="317"/>\n  <opc:EnumeratedValue Name="UserType" Value="318"/>\n  <opc:EnumeratedValue Name="UsesRemaining" Value="319"/>\n  <opc:EnumeratedValue Name="ZoneFrom" Value="320"/>\n  <opc:EnumeratedValue Name="ZoneTo" Value="321"/>\n  <opc:EnumeratedValue Name="AccessEventTag" Value="322"/>\n  <opc:EnumeratedValue Name="GlobalIdentifier" Value="323"/>\n  <opc:EnumeratedValue Name="Unassigned_324" Value="324"/>\n  <opc:EnumeratedValue Name="Unassigned_325" Value="325"/>\n  <opc:EnumeratedValue Name="VerificationTime" Value="326"/>\n  <opc:EnumeratedValue Name="BaseDeviceSecurityPolicy" Value="327"/>\n  <opc:EnumeratedValue Name="DistributionKeyRevision" Value="328"/>\n  <opc:EnumeratedValue Name="DoNotHide" Value="329"/>\n  <opc:EnumeratedValue Name="KeySets" Value="330"/>\n  <opc:EnumeratedValue Name="LastKeyServer" Value="331"/>\n  <opc:EnumeratedValue Name="NetworkAccessSecurityPolicies" Value="332"/>\n  <opc:EnumeratedValue Name="PacketReorderTime" Value="333"/>\n  <opc:EnumeratedValue Name="SecurityPduTimeout" Value="334"/>\n  <opc:EnumeratedValue Name="SecurityTimeWindow" Value="335"/>\n  <opc:EnumeratedValue Name="SupportedSecurityAlgorithms" Value="336"/>\n  <opc:EnumeratedValue Name="UpdateKeySetTimeout" Value="337"/>\n  <opc:EnumeratedValue Name="BackupAndRestoreState" Value="338"/>\n  <opc:EnumeratedValue Name="BackupPreparationTime" Value="339"/>\n  <opc:EnumeratedValue Name="RestoreCompletionTime" Value="340"/>\n  <opc:EnumeratedValue Name="RestorePreparationTime" Value="341"/>\n  <opc:EnumeratedValue Name="BitMask" Value="342"/>\n  <opc:EnumeratedValue Name="BitText" Value="343"/>\n  <opc:EnumeratedValue Name="IsUtc" Value="344"/>\n  <opc:EnumeratedValue Name="GroupMembers" Value="345"/>\n  <opc:EnumeratedValue Name="GroupMemberNames" Value="346"/>\n  <opc:EnumeratedValue Name="MemberStatusFlags" Value="347"/>\n  <opc:EnumeratedValue Name="RequestedUpdateInterval" Value="348"/>\n  <opc:EnumeratedValue Name="CovuPeriod" Value="349"/>\n  <opc:EnumeratedValue Name="CovuRecipients" Value="350"/>\n  <opc:EnumeratedValue Name="EventMessageTexts" Value="351"/>\n  <opc:EnumeratedValue Name="EventMessageTextsConfig" Value="352"/>\n  <opc:EnumeratedValue Name="EventDetectionEnable" Value="353"/>\n  <opc:EnumeratedValue Name="EventAlgorithmInhibit" Value="354"/>\n  <opc:EnumeratedValue Name="EventAlgorithmInhibitRef" Value="355"/>\n  <opc:EnumeratedValue Name="TimeDelayNormal" Value="356"/>\n  <opc:EnumeratedValue Name="ReliabilityEvaluationInhibit" Value="357"/>\n  <opc:EnumeratedValue Name="FaultParameters" Value="358"/>\n  <opc:EnumeratedValue Name="FaultType" Value="359"/>\n  <opc:EnumeratedValue Name="LocalForwardingOnly" Value="360"/>\n  <opc:EnumeratedValue Name="ProcessIdentifierFilter" Value="361"/>\n  <opc:EnumeratedValue Name="SubscribedRecipients" Value="362"/>\n  <opc:EnumeratedValue Name="PortFilter" Value="363"/>\n  <opc:EnumeratedValue Name="AuthorizationExemptions" Value="364"/>\n  <opc:EnumeratedValue Name="AllowGroupDelayInhibit" Value="365"/>\n  <opc:EnumeratedValue Name="ChannelNumber" Value="366"/>\n  <opc:EnumeratedValue Name="ControlGroups" Value="367"/>\n  <opc:EnumeratedValue Name="ExecutionDelay" Value="368"/>\n  <opc:EnumeratedValue Name="LastPriority" Value="369"/>\n  <opc:EnumeratedValue Name="WriteStatus" Value="370"/>\n  <opc:EnumeratedValue Name="PropertyList" Value="371"/>\n  <opc:EnumeratedValue Name="SerialNumber" Value="372"/>\n  <opc:EnumeratedValue Name="BlinkWarnEnable" Value="373"/>\n  <opc:EnumeratedValue Name="DefaultFadeTime" Value="374"/>\n  <opc:EnumeratedValue Name="DefaultRampRate" Value="375"/>\n  <opc:EnumeratedValue Name="DefaultStepIncrement" Value="376"/>\n  <opc:EnumeratedValue Name="EgressTime" Value="377"/>\n  <opc:EnumeratedValue Name="InProgress" Value="378"/>\n  <opc:EnumeratedValue Name="InstantaneousPower" Value="379"/>\n  <opc:EnumeratedValue Name="LightingCommand" Value="380"/>\n  <opc:EnumeratedValue Name="LightingCommandDefaultPriority" Value="381"/>\n  <opc:EnumeratedValue Name="MaxActualValue" Value="382"/>\n  <opc:EnumeratedValue Name="MinActualValue" Value="383"/>\n  <opc:EnumeratedValue Name="Power" Value="384"/>\n  <opc:EnumeratedValue Name="Transition" Value="385"/>\n  <opc:EnumeratedValue Name="EgressActive" Value="386"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetReinitializedStateofDevice">\n  <opc:EnumeratedValue Name="Coldstart" Value="0"/>\n  <opc:EnumeratedValue Name="Warmstart" Value="1"/>\n  <opc:EnumeratedValue Name="Startbackup" Value="2"/>\n  <opc:EnumeratedValue Name="Endbackup" Value="3"/>\n  <opc:EnumeratedValue Name="Startrestore" Value="4"/>\n  <opc:EnumeratedValue Name="Endrestore" Value="5"/>\n  <opc:EnumeratedValue Name="Abortrestore" Value="6"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetReliability">\n  <opc:EnumeratedValue Name="NoFaultDetected" Value="0"/>\n  <opc:EnumeratedValue Name="NoSensor" Value="1"/>\n  <opc:EnumeratedValue Name="OverRange" Value="2"/>\n  <opc:EnumeratedValue Name="UnderRange" Value="3"/>\n  <opc:EnumeratedValue Name="OpenLoop" Value="4"/>\n  <opc:EnumeratedValue Name="ShortedLoop" Value="5"/>\n  <opc:EnumeratedValue Name="NoOutput" Value="6"/>\n  <opc:EnumeratedValue Name="UnreliableOther" Value="7"/>\n  <opc:EnumeratedValue Name="ProcessError" Value="8"/>\n  <opc:EnumeratedValue Name="MultiStateFault" Value="9"/>\n  <opc:EnumeratedValue Name="ConfigurationError" Value="10"/>\n  <opc:EnumeratedValue Name="CommunicationFailure" Value="12"/>\n  <opc:EnumeratedValue Name="MemberFault" Value="13"/>\n  <opc:EnumeratedValue Name="MONITORED_OBJECT_FAULT" Value="14"/>\n  <opc:EnumeratedValue Name="TRIPPED" Value="15"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetRestartReason">\n  <opc:EnumeratedValue Name="unknown" Value="0"/>\n  <opc:EnumeratedValue Name="coldstart" Value="1"/>\n  <opc:EnumeratedValue Name="warmstart" Value="2"/>\n  <opc:EnumeratedValue Name="detected_power_lost" Value="3"/>\n  <opc:EnumeratedValue Name="detected_powered_off" Value="4"/>\n  <opc:EnumeratedValue Name="hardware_watchdog" Value="5"/>\n  <opc:EnumeratedValue Name="software_watchdog" Value="6"/>\n  <opc:EnumeratedValue Name="suspended" Value="7"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="BACnetSegmentation">\n  <opc:EnumeratedValue Name="segmented-both" Value="0"/>\n  <opc:EnumeratedValue Name="segmented-transmit" Value="1"/>\n  <opc:EnumeratedValue Name="segmented-receive" Value="2"/>\n  <opc:EnumeratedValue Name="no-segmentation" Value="3"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=bacnet;i=6462",
    browseName="ns=bacnet;BACnetEventParameterChangeOfLifeSafety",
    dataType=o6.String,
    value="//xs:element[@name='BACnetEventParameterChangeOfLifeSafety']",
)
o6.reference(o6.ns["ns=bacnet;i=5027"], "i=39", o6.ns["ns=bacnet;i=6462"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=bacnet;i=6158",
    browseName="ns=bacnet;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/BACnet_V2/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6162", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/BACnet_V2/Types.xsd")
        ),
        o6.hasComponent(o6.ns["ns=bacnet;i=6164"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6171"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6173"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6177"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6179"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6181"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6184"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6186"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6188"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6190"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6192"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6194"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6196"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6198"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6200"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6203"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6205"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6212"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6250"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6257"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6341"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6400"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6402"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6404"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6406"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6408"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6411"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6413"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6417"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6419"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6421"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6423"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6425"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6427"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6429"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6431"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6433"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6436"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6438"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6442"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6444"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6446"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6448"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6450"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6452"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6454"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6456"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6458"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6460"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=6462"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/BACnet_V2/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/BACnet_V2/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="BACnetAction">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="direct_0"/>\n   <xs:enumeration value="reverse_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetAction" name="BACnetAction"/>\n <xs:complexType name="ListOfBACnetAction">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetAction" name="BACnetAction" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetAction" name="ListOfBACnetAction" nillable="true"/>\n <xs:simpleType name="BACnetBackupState">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Idle_0"/>\n   <xs:enumeration value="Preparing_For_Backup_1"/>\n   <xs:enumeration value="Preparing_For_Restore_2"/>\n   <xs:enumeration value="Performing_A_Backup_3"/>\n   <xs:enumeration value="Performing_A_Restore_4"/>\n   <xs:enumeration value="Backup_Failure_5"/>\n   <xs:enumeration value="Restore_Failure_6"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetBackupState" name="BACnetBackupState"/>\n <xs:complexType name="ListOfBACnetBackupState">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetBackupState" name="BACnetBackupState" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetBackupState" name="ListOfBACnetBackupState" nillable="true"/>\n <xs:simpleType name="BACnetBinaryPV">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Inactive_0"/>\n   <xs:enumeration value="Active_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetBinaryPV" name="BACnetBinaryPV"/>\n <xs:complexType name="ListOfBACnetBinaryPV">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetBinaryPV" name="BACnetBinaryPV" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetBinaryPV" name="ListOfBACnetBinaryPV" nillable="true"/>\n <xs:simpleType name="BACnetDay">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="days numbered 1-7_1"/>\n   <xs:enumeration value="days numbered 8-14_2"/>\n   <xs:enumeration value="days numbered 15-21_3"/>\n   <xs:enumeration value="days numbered 22-28_4"/>\n   <xs:enumeration value="days numbered 29-31_5"/>\n   <xs:enumeration value="last 7 days of this month_6"/>\n   <xs:enumeration value="any week of this month_255"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetDay" name="BACnetDay"/>\n <xs:complexType name="ListOfBACnetDay">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetDay" name="BACnetDay" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetDay" name="ListOfBACnetDay" nillable="true"/>\n <xs:simpleType name="BACnetDayOfMonth">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="1_1"/>\n   <xs:enumeration value="2_2"/>\n   <xs:enumeration value="3_3"/>\n   <xs:enumeration value="4_4"/>\n   <xs:enumeration value="5_5"/>\n   <xs:enumeration value="6_6"/>\n   <xs:enumeration value="7_7"/>\n   <xs:enumeration value="8_8"/>\n   <xs:enumeration value="9_9"/>\n   <xs:enumeration value="10_10"/>\n   <xs:enumeration value="11_11"/>\n   <xs:enumeration value="12_12"/>\n   <xs:enumeration value="13_13"/>\n   <xs:enumeration value="14_14"/>\n   <xs:enumeration value="15_15"/>\n   <xs:enumeration value="16_16"/>\n   <xs:enumeration value="17_17"/>\n   <xs:enumeration value="18_18"/>\n   <xs:enumeration value="19_19"/>\n   <xs:enumeration value="20_20"/>\n   <xs:enumeration value="21_21"/>\n   <xs:enumeration value="22_22"/>\n   <xs:enumeration value="23_23"/>\n   <xs:enumeration value="24_24"/>\n   <xs:enumeration value="25_25"/>\n   <xs:enumeration value="26_26"/>\n   <xs:enumeration value="27_27"/>\n   <xs:enumeration value="28_28"/>\n   <xs:enumeration value="29_29"/>\n   <xs:enumeration value="30_30"/>\n   <xs:enumeration value="31_31"/>\n   <xs:enumeration value="Last day of month_32"/>\n   <xs:enumeration value="Odd day of month_33"/>\n   <xs:enumeration value="Even day of month_34"/>\n   <xs:enumeration value="Unspecified_255"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetDayOfMonth" name="BACnetDayOfMonth"/>\n <xs:complexType name="ListOfBACnetDayOfMonth">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetDayOfMonth" name="BACnetDayOfMonth" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetDayOfMonth" name="ListOfBACnetDayOfMonth" nillable="true"/>\n <xs:simpleType name="BACnetDayOfWeek">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Monday_1"/>\n   <xs:enumeration value="Tuesday_2"/>\n   <xs:enumeration value="Wednesday_3"/>\n   <xs:enumeration value="Thursday_4"/>\n   <xs:enumeration value="Friday_5"/>\n   <xs:enumeration value="Saturday_6"/>\n   <xs:enumeration value="Sunday_7"/>\n   <xs:enumeration value="unspecified_255"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetDayOfWeek" name="BACnetDayOfWeek"/>\n <xs:complexType name="ListOfBACnetDayOfWeek">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetDayOfWeek" name="BACnetDayOfWeek" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetDayOfWeek" name="ListOfBACnetDayOfWeek" nillable="true"/>\n <xs:simpleType name="BACnetDeviceCommunicationEnabled">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Enable_0"/>\n   <xs:enumeration value="Disable_1"/>\n   <xs:enumeration value="DisableInitiation_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetDeviceCommunicationEnabled" name="BACnetDeviceCommunicationEnabled"/>\n <xs:complexType name="ListOfBACnetDeviceCommunicationEnabled">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetDeviceCommunicationEnabled" name="BACnetDeviceCommunicationEnabled" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetDeviceCommunicationEnabled" name="ListOfBACnetDeviceCommunicationEnabled" nillable="true"/>\n <xs:simpleType name="BACnetDeviceStatus">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Operational_0"/>\n   <xs:enumeration value="OperationalReadOnly_1"/>\n   <xs:enumeration value="DownloadRequired_2"/>\n   <xs:enumeration value="DownloadInProgress_3"/>\n   <xs:enumeration value="NonOperational_4"/>\n   <xs:enumeration value="BackupInProgress_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetDeviceStatus" name="BACnetDeviceStatus"/>\n <xs:complexType name="ListOfBACnetDeviceStatus">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetDeviceStatus" name="BACnetDeviceStatus" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetDeviceStatus" name="ListOfBACnetDeviceStatus" nillable="true"/>\n <xs:simpleType name="BACnetEventEnumType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="ChangeOfBitstring_0"/>\n   <xs:enumeration value="ChangeOfState_1"/>\n   <xs:enumeration value="ChangeOfValue_2"/>\n   <xs:enumeration value="CommandFailure_3"/>\n   <xs:enumeration value="FloatingLimit_4"/>\n   <xs:enumeration value="OutOfRange_5"/>\n   <xs:enumeration value="ChangeOfLifeSafety_8"/>\n   <xs:enumeration value="Extended_9"/>\n   <xs:enumeration value="BufferReady_10"/>\n   <xs:enumeration value="UnsignedRange_11"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetEventEnumType" name="BACnetEventEnumType"/>\n <xs:complexType name="ListOfBACnetEventEnumType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventEnumType" name="BACnetEventEnumType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventEnumType" name="ListOfBACnetEventEnumType" nillable="true"/>\n <xs:simpleType name="BACnetEventState">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Normal_0"/>\n   <xs:enumeration value="Fault_1"/>\n   <xs:enumeration value="OffNormal_2"/>\n   <xs:enumeration value="HighLimit_3"/>\n   <xs:enumeration value="LowLimit_4"/>\n   <xs:enumeration value="LifeSafetyAlarm_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetEventState" name="BACnetEventState"/>\n <xs:complexType name="ListOfBACnetEventState">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventState" name="BACnetEventState" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventState" name="ListOfBACnetEventState" nillable="true"/>\n <xs:simpleType name="BACnetEventType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="change-of-bitstring_0"/>\n   <xs:enumeration value="change-of-state_1"/>\n   <xs:enumeration value="change-of-value_2"/>\n   <xs:enumeration value="command-failure_3"/>\n   <xs:enumeration value="out-of-range_5"/>\n   <xs:enumeration value="change-of-life-safety_8"/>\n   <xs:enumeration value="floating-limit_4"/>\n   <xs:enumeration value="extended_9"/>\n   <xs:enumeration value="buffer-ready_10"/>\n   <xs:enumeration value="unsigned-range_11"/>\n   <xs:enumeration value="access-event_13"/>\n   <xs:enumeration value="double-out-of-range_14"/>\n   <xs:enumeration value="signed-out-of-range_15"/>\n   <xs:enumeration value="unsigned-out-of-range_16"/>\n   <xs:enumeration value="change-of-characterstring_17"/>\n   <xs:enumeration value="change-of-status-flags_18"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetEventType" name="BACnetEventType"/>\n <xs:complexType name="ListOfBACnetEventType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventType" name="BACnetEventType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventType" name="ListOfBACnetEventType" nillable="true"/>\n <xs:simpleType name="BACnetFaultType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="none_0"/>\n   <xs:enumeration value="fault-characterstring_1"/>\n   <xs:enumeration value="fault-exended_2"/>\n   <xs:enumeration value="fault-life-safety_3"/>\n   <xs:enumeration value="fault-state_4"/>\n   <xs:enumeration value="fault-status-flags_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetFaultType" name="BACnetFaultType"/>\n <xs:complexType name="ListOfBACnetFaultType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetFaultType" name="BACnetFaultType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetFaultType" name="ListOfBACnetFaultType" nillable="true"/>\n <xs:simpleType name="BACnetLifeSafetyMode">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Off_0"/>\n   <xs:enumeration value="On_1"/>\n   <xs:enumeration value="Test_2"/>\n   <xs:enumeration value="Manned_3"/>\n   <xs:enumeration value="UnManned_4"/>\n   <xs:enumeration value="Armed_5"/>\n   <xs:enumeration value="Disarmed_6"/>\n   <xs:enumeration value="Prearmed_7"/>\n   <xs:enumeration value="Slow_8"/>\n   <xs:enumeration value="Fast_9"/>\n   <xs:enumeration value="Disconnected_10"/>\n   <xs:enumeration value="Enabled_11"/>\n   <xs:enumeration value="Disabled_12"/>\n   <xs:enumeration value="AutomaticReleaseDisabled_13"/>\n   <xs:enumeration value="Default_14"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetLifeSafetyMode" name="BACnetLifeSafetyMode"/>\n <xs:complexType name="ListOfBACnetLifeSafetyMode">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetLifeSafetyMode" name="BACnetLifeSafetyMode" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetLifeSafetyMode" name="ListOfBACnetLifeSafetyMode" nillable="true"/>\n <xs:simpleType name="BACnetLifeSafetyOperation">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="None_0"/>\n   <xs:enumeration value="Silence_1"/>\n   <xs:enumeration value="SilenceAudible_2"/>\n   <xs:enumeration value="SilenceVisible_3"/>\n   <xs:enumeration value="Reset_4"/>\n   <xs:enumeration value="ResetAlarm_5"/>\n   <xs:enumeration value="ResetFault_6"/>\n   <xs:enumeration value="Unsilence_7"/>\n   <xs:enumeration value="UnsilenceAudible_8"/>\n   <xs:enumeration value="UnsilenceVisible_9"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetLifeSafetyOperation" name="BACnetLifeSafetyOperation"/>\n <xs:complexType name="ListOfBACnetLifeSafetyOperation">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetLifeSafetyOperation" name="BACnetLifeSafetyOperation" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetLifeSafetyOperation" name="ListOfBACnetLifeSafetyOperation" nillable="true"/>\n <xs:simpleType name="BACnetLifeSafetyState">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Quiet_0"/>\n   <xs:enumeration value="PreAlarm_1"/>\n   <xs:enumeration value="Alarm_2"/>\n   <xs:enumeration value="Fault_3"/>\n   <xs:enumeration value="FaultPreAlarm_4"/>\n   <xs:enumeration value="FaultAlarm_5"/>\n   <xs:enumeration value="NotReady_6"/>\n   <xs:enumeration value="Active_7"/>\n   <xs:enumeration value="Tamper_8"/>\n   <xs:enumeration value="TestAlarm_9"/>\n   <xs:enumeration value="TestActive_10"/>\n   <xs:enumeration value="TestFault_11"/>\n   <xs:enumeration value="TestFaultAlarm_12"/>\n   <xs:enumeration value="Holdup_13"/>\n   <xs:enumeration value="Duress_14"/>\n   <xs:enumeration value="TamperAlarm_15"/>\n   <xs:enumeration value="Abnormal_16"/>\n   <xs:enumeration value="EmergencyPower_17"/>\n   <xs:enumeration value="Delayed_18"/>\n   <xs:enumeration value="Blocked_19"/>\n   <xs:enumeration value="LocalAlarm_20"/>\n   <xs:enumeration value="GeneralAlarm_21"/>\n   <xs:enumeration value="Supervisory_22"/>\n   <xs:enumeration value="TestSupervisory_23"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetLifeSafetyState" name="BACnetLifeSafetyState"/>\n <xs:complexType name="ListOfBACnetLifeSafetyState">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetLifeSafetyState" name="BACnetLifeSafetyState" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetLifeSafetyState" name="ListOfBACnetLifeSafetyState" nillable="true"/>\n <xs:simpleType name="BACnetLoggingType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Polled_0"/>\n   <xs:enumeration value="COV_1"/>\n   <xs:enumeration value="Triggered_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetLoggingType" name="BACnetLoggingType"/>\n <xs:complexType name="ListOfBACnetLoggingType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetLoggingType" name="BACnetLoggingType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetLoggingType" name="ListOfBACnetLoggingType" nillable="true"/>\n <xs:simpleType name="BACnetMessagePriority">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="normal_0"/>\n   <xs:enumeration value="urgent_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetMessagePriority" name="BACnetMessagePriority"/>\n <xs:complexType name="ListOfBACnetMessagePriority">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetMessagePriority" name="BACnetMessagePriority" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetMessagePriority" name="ListOfBACnetMessagePriority" nillable="true"/>\n <xs:simpleType name="BACnetMonth">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="January_1"/>\n   <xs:enumeration value="February_2"/>\n   <xs:enumeration value="March_3"/>\n   <xs:enumeration value="April_4"/>\n   <xs:enumeration value="May_5"/>\n   <xs:enumeration value="June_6"/>\n   <xs:enumeration value="July_7"/>\n   <xs:enumeration value="August_8"/>\n   <xs:enumeration value="September_9"/>\n   <xs:enumeration value="October_10"/>\n   <xs:enumeration value="November_11"/>\n   <xs:enumeration value="December_12"/>\n   <xs:enumeration value="Odd_13"/>\n   <xs:enumeration value="Even_14"/>\n   <xs:enumeration value="Unspecified_255"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetMonth" name="BACnetMonth"/>\n <xs:complexType name="ListOfBACnetMonth">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetMonth" name="BACnetMonth" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetMonth" name="ListOfBACnetMonth" nillable="true"/>\n <xs:simpleType name="BACnetNodeType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="UNKNOWN_0"/>\n   <xs:enumeration value="SYSTEM_1"/>\n   <xs:enumeration value="NETWORK_2"/>\n   <xs:enumeration value="DEVICE_3"/>\n   <xs:enumeration value="ORGANIZATIONAL_4"/>\n   <xs:enumeration value="AREA_5"/>\n   <xs:enumeration value="EQUIPMENT_6"/>\n   <xs:enumeration value="POINT_7"/>\n   <xs:enumeration value="COLLECTION_8"/>\n   <xs:enumeration value="PROPERTY_9"/>\n   <xs:enumeration value="FUNCTIONAL_10"/>\n   <xs:enumeration value="OTHER_11"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetNodeType" name="BACnetNodeType"/>\n <xs:complexType name="ListOfBACnetNodeType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetNodeType" name="BACnetNodeType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetNodeType" name="ListOfBACnetNodeType" nillable="true"/>\n <xs:simpleType name="BACnetNotifyType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Alarm_0"/>\n   <xs:enumeration value="Event_1"/>\n   <xs:enumeration value="AckNotification_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetNotifyType" name="BACnetNotifyType"/>\n <xs:complexType name="ListOfBACnetNotifyType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetNotifyType" name="BACnetNotifyType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetNotifyType" name="ListOfBACnetNotifyType" nillable="true"/>\n <xs:simpleType name="BACnetObjectTypeEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="analog-input_0"/>\n   <xs:enumeration value="analog-output_1"/>\n   <xs:enumeration value="analog-value_2"/>\n   <xs:enumeration value="binary-input_3"/>\n   <xs:enumeration value="binary-output_4"/>\n   <xs:enumeration value="binary-value_5"/>\n   <xs:enumeration value="calendar_6"/>\n   <xs:enumeration value="command_7"/>\n   <xs:enumeration value="device_8"/>\n   <xs:enumeration value="event-enrollment_9"/>\n   <xs:enumeration value="file_10"/>\n   <xs:enumeration value="group_11"/>\n   <xs:enumeration value="loop_12"/>\n   <xs:enumeration value="multi-state-input_13"/>\n   <xs:enumeration value="multi-state-output_14"/>\n   <xs:enumeration value="notification-class_15"/>\n   <xs:enumeration value="program_16"/>\n   <xs:enumeration value="schedule_17"/>\n   <xs:enumeration value="averaging_18"/>\n   <xs:enumeration value="multi-state-value_19"/>\n   <xs:enumeration value="trend-log_20"/>\n   <xs:enumeration value="life-safety-point_21"/>\n   <xs:enumeration value="life-safety-zone_22"/>\n   <xs:enumeration value="accumulator_23"/>\n   <xs:enumeration value="pulse-converter_24"/>\n   <xs:enumeration value="event-log_25"/>\n   <xs:enumeration value="global-group_26"/>\n   <xs:enumeration value="trend-log-multiple_27"/>\n   <xs:enumeration value="load-control_28"/>\n   <xs:enumeration value="structured-view_29"/>\n   <xs:enumeration value="access-door_30"/>\n   <xs:enumeration value="unassigned_31"/>\n   <xs:enumeration value="access-credential_32"/>\n   <xs:enumeration value="access-point_33"/>\n   <xs:enumeration value="access-rights_34"/>\n   <xs:enumeration value="access-user_35"/>\n   <xs:enumeration value="access-zone_36"/>\n   <xs:enumeration value="credentional-data-input_37"/>\n   <xs:enumeration value="network-security_38"/>\n   <xs:enumeration value="bitstring-value_39"/>\n   <xs:enumeration value="characterstring-value_40"/>\n   <xs:enumeration value="date-pattern-value_41"/>\n   <xs:enumeration value="date-value_42"/>\n   <xs:enumeration value="datetime-pattern-value_43"/>\n   <xs:enumeration value="datetime-value_44"/>\n   <xs:enumeration value="integer-value_45"/>\n   <xs:enumeration value="large-analog-value_46"/>\n   <xs:enumeration value="octetstring-value_47"/>\n   <xs:enumeration value="positive-integer-value_48"/>\n   <xs:enumeration value="time-pattern-value_49"/>\n   <xs:enumeration value="time-value_50"/>\n   <xs:enumeration value="notification-forwarder_51"/>\n   <xs:enumeration value="alert-enrollment_52"/>\n   <xs:enumeration value="channel_53"/>\n   <xs:enumeration value="lighting-output_54"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetObjectTypeEnum" name="BACnetObjectTypeEnum"/>\n <xs:complexType name="ListOfBACnetObjectTypeEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetObjectTypeEnum" name="BACnetObjectTypeEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetObjectTypeEnum" name="ListOfBACnetObjectTypeEnum" nillable="true"/>\n <xs:simpleType name="BACnetPolarity">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Normal_0"/>\n   <xs:enumeration value="Reverse_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetPolarity" name="BACnetPolarity"/>\n <xs:complexType name="ListOfBACnetPolarity">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetPolarity" name="BACnetPolarity" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetPolarity" name="ListOfBACnetPolarity" nillable="true"/>\n <xs:simpleType name="BACnetProgramError">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Normal_0"/>\n   <xs:enumeration value="LoadFailed_1"/>\n   <xs:enumeration value="Internal_2"/>\n   <xs:enumeration value="Program_3"/>\n   <xs:enumeration value="Other_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetProgramError" name="BACnetProgramError"/>\n <xs:complexType name="ListOfBACnetProgramError">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetProgramError" name="BACnetProgramError" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetProgramError" name="ListOfBACnetProgramError" nillable="true"/>\n <xs:simpleType name="BACnetProgramRequest">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Ready_0"/>\n   <xs:enumeration value="Load_1"/>\n   <xs:enumeration value="Run_2"/>\n   <xs:enumeration value="Halt_3"/>\n   <xs:enumeration value="Restart_4"/>\n   <xs:enumeration value="Unload_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetProgramRequest" name="BACnetProgramRequest"/>\n <xs:complexType name="ListOfBACnetProgramRequest">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetProgramRequest" name="BACnetProgramRequest" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetProgramRequest" name="ListOfBACnetProgramRequest" nillable="true"/>\n <xs:simpleType name="BACnetProgramStates">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Idle_0"/>\n   <xs:enumeration value="Loading_1"/>\n   <xs:enumeration value="Running_2"/>\n   <xs:enumeration value="Waiting_3"/>\n   <xs:enumeration value="Halted_4"/>\n   <xs:enumeration value="Unloading_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetProgramStates" name="BACnetProgramStates"/>\n <xs:complexType name="ListOfBACnetProgramStates">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetProgramStates" name="BACnetProgramStates" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetProgramStates" name="ListOfBACnetProgramStates" nillable="true"/>\n <xs:simpleType name="BACnetPropertyIdentifier">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="AckedTransitions_0"/>\n   <xs:enumeration value="AckRequired_1"/>\n   <xs:enumeration value="Action_2"/>\n   <xs:enumeration value="ActionText_3"/>\n   <xs:enumeration value="ActiveText_4"/>\n   <xs:enumeration value="ActiveVtSessions_5"/>\n   <xs:enumeration value="AlarmValue_6"/>\n   <xs:enumeration value="AlarmValues_7"/>\n   <xs:enumeration value="All_8"/>\n   <xs:enumeration value="AllWritesSuccessful_9"/>\n   <xs:enumeration value="ApduSegmentTimeout_10"/>\n   <xs:enumeration value="ApduTimeout_11"/>\n   <xs:enumeration value="ApplicationSoftwareVersion_12"/>\n   <xs:enumeration value="Archive_13"/>\n   <xs:enumeration value="Bias_14"/>\n   <xs:enumeration value="ChangeOfStateCount_15"/>\n   <xs:enumeration value="ChangeOfStateTime_16"/>\n   <xs:enumeration value="NotificationClass_17"/>\n   <xs:enumeration value="this property deleted_18"/>\n   <xs:enumeration value="ControlledVariableReference_19"/>\n   <xs:enumeration value="ControlledVariableUnits_20"/>\n   <xs:enumeration value="ControlledVariableValue_21"/>\n   <xs:enumeration value="CovIncrement_22"/>\n   <xs:enumeration value="DateList_23"/>\n   <xs:enumeration value="DaylightSavingsStatus_24"/>\n   <xs:enumeration value="Deadband_25"/>\n   <xs:enumeration value="DerivativeConstant_26"/>\n   <xs:enumeration value="DerivativeConstantUnits_27"/>\n   <xs:enumeration value="Description_28"/>\n   <xs:enumeration value="DescriptionOfHalt_29"/>\n   <xs:enumeration value="DeviceAddressBinding_30"/>\n   <xs:enumeration value="DeviceType_31"/>\n   <xs:enumeration value="EffectivePeriod_32"/>\n   <xs:enumeration value="ElapsedActiveTime_33"/>\n   <xs:enumeration value="ErrorLimit_34"/>\n   <xs:enumeration value="EventEnable_35"/>\n   <xs:enumeration value="EventState_36"/>\n   <xs:enumeration value="EventType_37"/>\n   <xs:enumeration value="ExceptionSchedule_38"/>\n   <xs:enumeration value="FaultValues_39"/>\n   <xs:enumeration value="FeedbackValue_40"/>\n   <xs:enumeration value="FileAccessMethod_41"/>\n   <xs:enumeration value="FileSize_42"/>\n   <xs:enumeration value="FileType_43"/>\n   <xs:enumeration value="FirmwareRevision_44"/>\n   <xs:enumeration value="HighLimit_45"/>\n   <xs:enumeration value="InactiveText_46"/>\n   <xs:enumeration value="InProcess_47"/>\n   <xs:enumeration value="InstanceOf_48"/>\n   <xs:enumeration value="IntegralConstant_49"/>\n   <xs:enumeration value="IntegralConstantUnits_50"/>\n   <xs:enumeration value="Removed In Version 1 Revision 4_51_51"/>\n   <xs:enumeration value="LimitEnable_52"/>\n   <xs:enumeration value="ListOfGroupMembers_53"/>\n   <xs:enumeration value="ListOfObjectPropertyReferences_54"/>\n   <xs:enumeration value="Unassigned_55_55"/>\n   <xs:enumeration value="LocalDate_56"/>\n   <xs:enumeration value="LocalTime_57"/>\n   <xs:enumeration value="Location_58"/>\n   <xs:enumeration value="LowLimit_59"/>\n   <xs:enumeration value="ManipulatedVariableReference_60"/>\n   <xs:enumeration value="MaximumOutput_61"/>\n   <xs:enumeration value="MaxApduLengthAccepted_62"/>\n   <xs:enumeration value="MaxInfoFrames_63"/>\n   <xs:enumeration value="MaxMaster_64"/>\n   <xs:enumeration value="MaxPresValue_65"/>\n   <xs:enumeration value="MinimumOffTime_66"/>\n   <xs:enumeration value="MinimumOnTime_67"/>\n   <xs:enumeration value="MinimumOutput_68"/>\n   <xs:enumeration value="MinPresValue_69"/>\n   <xs:enumeration value="ModelName_70"/>\n   <xs:enumeration value="ModificationDate_71"/>\n   <xs:enumeration value="NotifyType_72"/>\n   <xs:enumeration value="NumberOfApduRetries_73"/>\n   <xs:enumeration value="NumberOfStates_74"/>\n   <xs:enumeration value="ObjectIdentifier_75"/>\n   <xs:enumeration value="ObjectList_76"/>\n   <xs:enumeration value="ObjectName_77"/>\n   <xs:enumeration value="ObjectPropertyReference_78"/>\n   <xs:enumeration value="ObjectType_79"/>\n   <xs:enumeration value="Optional_80"/>\n   <xs:enumeration value="OutOfService_81"/>\n   <xs:enumeration value="OutputUnits_82"/>\n   <xs:enumeration value="EventParameters_83"/>\n   <xs:enumeration value="Polarity_84"/>\n   <xs:enumeration value="PresentValue_85"/>\n   <xs:enumeration value="Priority_86"/>\n   <xs:enumeration value="PriorityArray_87"/>\n   <xs:enumeration value="PriorityForWriting_88"/>\n   <xs:enumeration value="ProcessIdentifier_89"/>\n   <xs:enumeration value="ProgramChange_90"/>\n   <xs:enumeration value="ProgramLocation_91"/>\n   <xs:enumeration value="ProgramState_92"/>\n   <xs:enumeration value="ProportionalConstant_93"/>\n   <xs:enumeration value="ProportionalConstantUnits_94"/>\n   <xs:enumeration value="Removed In Version 1 Revision 2_95_95"/>\n   <xs:enumeration value="ProtocolObjectTypesSupported_96"/>\n   <xs:enumeration value="ProtocolServicesSupported_97"/>\n   <xs:enumeration value="ProtocolVersion_98"/>\n   <xs:enumeration value="ReadOnly_99"/>\n   <xs:enumeration value="ReasonForHalt_100"/>\n   <xs:enumeration value="Removed In Version 1 Revision 4_101_101"/>\n   <xs:enumeration value="RecipientList_102"/>\n   <xs:enumeration value="Reliability_103"/>\n   <xs:enumeration value="RelinquishDefault_104"/>\n   <xs:enumeration value="Required_105"/>\n   <xs:enumeration value="Resolution_106"/>\n   <xs:enumeration value="SegmentationSupported_107"/>\n   <xs:enumeration value="Setpoint_108"/>\n   <xs:enumeration value="SetpointReference_109"/>\n   <xs:enumeration value="StateText_110"/>\n   <xs:enumeration value="StatusFlags_111"/>\n   <xs:enumeration value="SystemStatus_112"/>\n   <xs:enumeration value="TimeDelay_113"/>\n   <xs:enumeration value="TimeOfActiveTimeReset_114"/>\n   <xs:enumeration value="TimeOfStateCountReset_115"/>\n   <xs:enumeration value="TimeSynchronizationRecipients_116"/>\n   <xs:enumeration value="Units_117"/>\n   <xs:enumeration value="UpdateInterval_118"/>\n   <xs:enumeration value="UtcOffset_119"/>\n   <xs:enumeration value="VendorIdentifier_120"/>\n   <xs:enumeration value="VendorName_121"/>\n   <xs:enumeration value="VtClassesSupported_122"/>\n   <xs:enumeration value="WeeklySchedule_123"/>\n   <xs:enumeration value="AttemptedSamples_124"/>\n   <xs:enumeration value="AverageValue_125"/>\n   <xs:enumeration value="BufferSize_126"/>\n   <xs:enumeration value="ClientCovIncrement_127"/>\n   <xs:enumeration value="CovResubscriptionInterval_128"/>\n   <xs:enumeration value="Removed In Version 1 Revision 3_129_129"/>\n   <xs:enumeration value="EventTimeStamps_130"/>\n   <xs:enumeration value="LogBuffer_131"/>\n   <xs:enumeration value="LogDeviceObjectProperty_132"/>\n   <xs:enumeration value="Enable_133"/>\n   <xs:enumeration value="LogInterval_134"/>\n   <xs:enumeration value="MaximumValue_135"/>\n   <xs:enumeration value="MinimumValue_136"/>\n   <xs:enumeration value="NotificationThreshold_137"/>\n   <xs:enumeration value="Removed In Version 1 Revision 3_138_138"/>\n   <xs:enumeration value="ProtocolRevision_139"/>\n   <xs:enumeration value="RecordsSinceNotification_140"/>\n   <xs:enumeration value="RecordCount_141"/>\n   <xs:enumeration value="StartTime_142"/>\n   <xs:enumeration value="StopTime_143"/>\n   <xs:enumeration value="StopWhenFull_144"/>\n   <xs:enumeration value="TotalRecordCount_145"/>\n   <xs:enumeration value="ValidSamples_146"/>\n   <xs:enumeration value="WindowInterval_147"/>\n   <xs:enumeration value="WindowSamples_148"/>\n   <xs:enumeration value="MaximumValueTimestamp_149"/>\n   <xs:enumeration value="MinimumValueTimestamp_150"/>\n   <xs:enumeration value="VarianceValue_151"/>\n   <xs:enumeration value="ActiveCovSubscriptions_152"/>\n   <xs:enumeration value="BackupFailureTimeout_153"/>\n   <xs:enumeration value="ConfigurationFiles_154"/>\n   <xs:enumeration value="DatabaseRevision_155"/>\n   <xs:enumeration value="DirectReading_156"/>\n   <xs:enumeration value="LastRestoreTime_157"/>\n   <xs:enumeration value="MaintenanceRequired_158"/>\n   <xs:enumeration value="MemberOf_159"/>\n   <xs:enumeration value="Mode_160"/>\n   <xs:enumeration value="OperationExpected_161"/>\n   <xs:enumeration value="Setting_162"/>\n   <xs:enumeration value="Silenced_163"/>\n   <xs:enumeration value="TrackingValue_164"/>\n   <xs:enumeration value="ZoneMembers_165"/>\n   <xs:enumeration value="LifeSafetyAlarmValues_166"/>\n   <xs:enumeration value="MaxSegmentsAccepted_167"/>\n   <xs:enumeration value="ProfileName_168"/>\n   <xs:enumeration value="AutoSlaveDiscovery_169"/>\n   <xs:enumeration value="ManualSlaveAddressBinding_170"/>\n   <xs:enumeration value="SlaveAddressBinding_171"/>\n   <xs:enumeration value="SlaveProxyEnable_172"/>\n   <xs:enumeration value="LastNotifyRecord_173"/>\n   <xs:enumeration value="ScheduleDefault_174"/>\n   <xs:enumeration value="AcceptedModes_175"/>\n   <xs:enumeration value="AdjustValue_176"/>\n   <xs:enumeration value="Count_177"/>\n   <xs:enumeration value="CountBeforeChange_178"/>\n   <xs:enumeration value="CountChangeTime_179"/>\n   <xs:enumeration value="CovPeriod_180"/>\n   <xs:enumeration value="InputReference_181"/>\n   <xs:enumeration value="LimitMonitoringInterval_182"/>\n   <xs:enumeration value="LoggingObject_183"/>\n   <xs:enumeration value="LoggingRecord_184"/>\n   <xs:enumeration value="Prescale_185"/>\n   <xs:enumeration value="PulseRate_186"/>\n   <xs:enumeration value="Scale_187"/>\n   <xs:enumeration value="ScaleFactor_188"/>\n   <xs:enumeration value="UpdateTime_189"/>\n   <xs:enumeration value="ValueBeforeChange_190"/>\n   <xs:enumeration value="ValueSet_191"/>\n   <xs:enumeration value="ValueChangeTime_192"/>\n   <xs:enumeration value="AlignIntervals_193"/>\n   <xs:enumeration value="Unassigned_194_194"/>\n   <xs:enumeration value="IntervalOffset_195"/>\n   <xs:enumeration value="LastRestartReason_196"/>\n   <xs:enumeration value="LoggingType_197"/>\n   <xs:enumeration value="Unassigned_198_198"/>\n   <xs:enumeration value="Unassigned_199_199"/>\n   <xs:enumeration value="Unassigned_200_200"/>\n   <xs:enumeration value="Unassigned_201_201"/>\n   <xs:enumeration value="RestartNotificationRecipients_202"/>\n   <xs:enumeration value="TimeOfDeviceRestart_203"/>\n   <xs:enumeration value="TimeSynchronizationInterval_204"/>\n   <xs:enumeration value="Trigger_205"/>\n   <xs:enumeration value="UtcTimeSynchronizationRecipients_206"/>\n   <xs:enumeration value="NodeSubtype_207"/>\n   <xs:enumeration value="NodeType_208"/>\n   <xs:enumeration value="StructuredObjectList_209"/>\n   <xs:enumeration value="SubordinateAnnotations_210"/>\n   <xs:enumeration value="SubordinateList_211"/>\n   <xs:enumeration value="ActualShedLevel_212"/>\n   <xs:enumeration value="DutyWindow_213"/>\n   <xs:enumeration value="ExpectedShedLevel_214"/>\n   <xs:enumeration value="FullDutyBaseline_215"/>\n   <xs:enumeration value="Unassigned_216_216"/>\n   <xs:enumeration value="Unassigned_217_217"/>\n   <xs:enumeration value="RequestedShedLevel_218"/>\n   <xs:enumeration value="ShedDuration_219"/>\n   <xs:enumeration value="ShedLevelDescriptions_220"/>\n   <xs:enumeration value="ShedLevels_221"/>\n   <xs:enumeration value="StateDescription_222"/>\n   <xs:enumeration value="Unassigned_223_223"/>\n   <xs:enumeration value="Unassigned_224_224"/>\n   <xs:enumeration value="Unassigned_225_225"/>\n   <xs:enumeration value="DoorAlarmState_226"/>\n   <xs:enumeration value="DoorExtendedPulseTime_227"/>\n   <xs:enumeration value="DoorMembers_228"/>\n   <xs:enumeration value="DoorOpenTooLongTime_229"/>\n   <xs:enumeration value="DoorPulseTime_230"/>\n   <xs:enumeration value="DoorStatus_231"/>\n   <xs:enumeration value="DoorUnlockDelayTime_232"/>\n   <xs:enumeration value="LockStatus_233"/>\n   <xs:enumeration value="MaskedAlarmValues_234"/>\n   <xs:enumeration value="SecuredStatus_235"/>\n   <xs:enumeration value="Unassigned_236_236"/>\n   <xs:enumeration value="Unassigned_237_237"/>\n   <xs:enumeration value="Unassigned_238_238"/>\n   <xs:enumeration value="Unassigned_239_239"/>\n   <xs:enumeration value="Unassigned_240_240"/>\n   <xs:enumeration value="Unassigned_241_241"/>\n   <xs:enumeration value="Unassigned_242_242"/>\n   <xs:enumeration value="Unassigned_243_243"/>\n   <xs:enumeration value="AbsenteeLimit_244"/>\n   <xs:enumeration value="AccessAlarmEvents_245"/>\n   <xs:enumeration value="AccessDoors_246"/>\n   <xs:enumeration value="AccessEvent_247"/>\n   <xs:enumeration value="AccessEventAuthenticationFactor_248"/>\n   <xs:enumeration value="AccessEventCredential_249"/>\n   <xs:enumeration value="AccessEventTime_250"/>\n   <xs:enumeration value="AccessTransactionEvents_251"/>\n   <xs:enumeration value="Accompaniment_252"/>\n   <xs:enumeration value="AccompanimentTime_253"/>\n   <xs:enumeration value="ActivationTime_254"/>\n   <xs:enumeration value="ActiveAuthenticationPolicy_255"/>\n   <xs:enumeration value="AssignedAccessRights_256"/>\n   <xs:enumeration value="AuthenticationFactors_257"/>\n   <xs:enumeration value="AuthenticationPolicyList_258"/>\n   <xs:enumeration value="AuthenticationPolicyNames_259"/>\n   <xs:enumeration value="AuthenticationStatus_260"/>\n   <xs:enumeration value="AuthorizationMode_261"/>\n   <xs:enumeration value="BelongsTo_262"/>\n   <xs:enumeration value="CredentialDisable_263"/>\n   <xs:enumeration value="CredentialStatus_264"/>\n   <xs:enumeration value="Credentials_265"/>\n   <xs:enumeration value="CredentialsInZone_266"/>\n   <xs:enumeration value="DaysRemaining_267"/>\n   <xs:enumeration value="EntryPoints_268"/>\n   <xs:enumeration value="ExitPoints_269"/>\n   <xs:enumeration value="ExpiryTime_270"/>\n   <xs:enumeration value="ExtendedTimeEnable_271"/>\n   <xs:enumeration value="FailedAttemptEvents_272"/>\n   <xs:enumeration value="FailedAttempts_273"/>\n   <xs:enumeration value="FailedAttemptsTime_274"/>\n   <xs:enumeration value="LastAccessEvent_275"/>\n   <xs:enumeration value="LastAccessPoint_276"/>\n   <xs:enumeration value="LastCredentialAdded_277"/>\n   <xs:enumeration value="LastCredentialAddedTime_278"/>\n   <xs:enumeration value="LastCredentialRemoved_279"/>\n   <xs:enumeration value="LastCredentialRemovedTime_280"/>\n   <xs:enumeration value="LastUseTime_281"/>\n   <xs:enumeration value="Lockout_282"/>\n   <xs:enumeration value="LockoutRelinquishTime_283"/>\n   <xs:enumeration value="Removed In Version 1 Revision 13_284_284"/>\n   <xs:enumeration value="MaxFailedAttempts_285"/>\n   <xs:enumeration value="Members_286"/>\n   <xs:enumeration value="MusterPoint_287"/>\n   <xs:enumeration value="NegativeAccessRules_288"/>\n   <xs:enumeration value="NumberOfAuthenticationPolicies_289"/>\n   <xs:enumeration value="OccupancyCount_290"/>\n   <xs:enumeration value="OccupancyCountAdjust_291"/>\n   <xs:enumeration value="OccupancyCountEnable_292"/>\n   <xs:enumeration value="Removed In Version 1 Revision 13_293_293"/>\n   <xs:enumeration value="OccupancyLowerLimit_294"/>\n   <xs:enumeration value="OccupancyLowerLimitEnforced_295"/>\n   <xs:enumeration value="OccupancyState_296"/>\n   <xs:enumeration value="OccupancyUpperLimit_297"/>\n   <xs:enumeration value="OccupancyUpperLimitEnforced_298"/>\n   <xs:enumeration value="Removed In Version 1 Revision 13_299_299"/>\n   <xs:enumeration value="PassbackMode_300"/>\n   <xs:enumeration value="PassbackTimeout_301"/>\n   <xs:enumeration value="PositiveAccessRules_302"/>\n   <xs:enumeration value="ReasonForDisable_303"/>\n   <xs:enumeration value="SupportedFormats_304"/>\n   <xs:enumeration value="SupportedFormatClasses_305"/>\n   <xs:enumeration value="ThreatAuthority_306"/>\n   <xs:enumeration value="ThreatLevel_307"/>\n   <xs:enumeration value="TraceFlag_308"/>\n   <xs:enumeration value="TransactionNotificationClass_309"/>\n   <xs:enumeration value="UserExternalIdentifier_310"/>\n   <xs:enumeration value="UserInformationReference_311"/>\n   <xs:enumeration value="Unassigned_312_312"/>\n   <xs:enumeration value="Unassigned_313_313"/>\n   <xs:enumeration value="Unassigned_314_314"/>\n   <xs:enumeration value="Unassigned_315_315"/>\n   <xs:enumeration value="Unassigned_316_316"/>\n   <xs:enumeration value="UserName_317"/>\n   <xs:enumeration value="UserType_318"/>\n   <xs:enumeration value="UsesRemaining_319"/>\n   <xs:enumeration value="ZoneFrom_320"/>\n   <xs:enumeration value="ZoneTo_321"/>\n   <xs:enumeration value="AccessEventTag_322"/>\n   <xs:enumeration value="GlobalIdentifier_323"/>\n   <xs:enumeration value="Unassigned_324_324"/>\n   <xs:enumeration value="Unassigned_325_325"/>\n   <xs:enumeration value="VerificationTime_326"/>\n   <xs:enumeration value="BaseDeviceSecurityPolicy_327"/>\n   <xs:enumeration value="DistributionKeyRevision_328"/>\n   <xs:enumeration value="DoNotHide_329"/>\n   <xs:enumeration value="KeySets_330"/>\n   <xs:enumeration value="LastKeyServer_331"/>\n   <xs:enumeration value="NetworkAccessSecurityPolicies_332"/>\n   <xs:enumeration value="PacketReorderTime_333"/>\n   <xs:enumeration value="SecurityPduTimeout_334"/>\n   <xs:enumeration value="SecurityTimeWindow_335"/>\n   <xs:enumeration value="SupportedSecurityAlgorithms_336"/>\n   <xs:enumeration value="UpdateKeySetTimeout_337"/>\n   <xs:enumeration value="BackupAndRestoreState_338"/>\n   <xs:enumeration value="BackupPreparationTime_339"/>\n   <xs:enumeration value="RestoreCompletionTime_340"/>\n   <xs:enumeration value="RestorePreparationTime_341"/>\n   <xs:enumeration value="BitMask_342"/>\n   <xs:enumeration value="BitText_343"/>\n   <xs:enumeration value="IsUtc_344"/>\n   <xs:enumeration value="GroupMembers_345"/>\n   <xs:enumeration value="GroupMemberNames_346"/>\n   <xs:enumeration value="MemberStatusFlags_347"/>\n   <xs:enumeration value="RequestedUpdateInterval_348"/>\n   <xs:enumeration value="CovuPeriod_349"/>\n   <xs:enumeration value="CovuRecipients_350"/>\n   <xs:enumeration value="EventMessageTexts_351"/>\n   <xs:enumeration value="EventMessageTextsConfig_352"/>\n   <xs:enumeration value="EventDetectionEnable_353"/>\n   <xs:enumeration value="EventAlgorithmInhibit_354"/>\n   <xs:enumeration value="EventAlgorithmInhibitRef_355"/>\n   <xs:enumeration value="TimeDelayNormal_356"/>\n   <xs:enumeration value="ReliabilityEvaluationInhibit_357"/>\n   <xs:enumeration value="FaultParameters_358"/>\n   <xs:enumeration value="FaultType_359"/>\n   <xs:enumeration value="LocalForwardingOnly_360"/>\n   <xs:enumeration value="ProcessIdentifierFilter_361"/>\n   <xs:enumeration value="SubscribedRecipients_362"/>\n   <xs:enumeration value="PortFilter_363"/>\n   <xs:enumeration value="AuthorizationExemptions_364"/>\n   <xs:enumeration value="AllowGroupDelayInhibit_365"/>\n   <xs:enumeration value="ChannelNumber_366"/>\n   <xs:enumeration value="ControlGroups_367"/>\n   <xs:enumeration value="ExecutionDelay_368"/>\n   <xs:enumeration value="LastPriority_369"/>\n   <xs:enumeration value="WriteStatus_370"/>\n   <xs:enumeration value="PropertyList_371"/>\n   <xs:enumeration value="SerialNumber_372"/>\n   <xs:enumeration value="BlinkWarnEnable_373"/>\n   <xs:enumeration value="DefaultFadeTime_374"/>\n   <xs:enumeration value="DefaultRampRate_375"/>\n   <xs:enumeration value="DefaultStepIncrement_376"/>\n   <xs:enumeration value="EgressTime_377"/>\n   <xs:enumeration value="InProgress_378"/>\n   <xs:enumeration value="InstantaneousPower_379"/>\n   <xs:enumeration value="LightingCommand_380"/>\n   <xs:enumeration value="LightingCommandDefaultPriority_381"/>\n   <xs:enumeration value="MaxActualValue_382"/>\n   <xs:enumeration value="MinActualValue_383"/>\n   <xs:enumeration value="Power_384"/>\n   <xs:enumeration value="Transition_385"/>\n   <xs:enumeration value="EgressActive_386"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetPropertyIdentifier" name="BACnetPropertyIdentifier"/>\n <xs:complexType name="ListOfBACnetPropertyIdentifier">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetPropertyIdentifier" name="BACnetPropertyIdentifier" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetPropertyIdentifier" name="ListOfBACnetPropertyIdentifier" nillable="true"/>\n <xs:simpleType name="BACnetReinitializedStateofDevice">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Coldstart_0"/>\n   <xs:enumeration value="Warmstart_1"/>\n   <xs:enumeration value="Startbackup_2"/>\n   <xs:enumeration value="Endbackup_3"/>\n   <xs:enumeration value="Startrestore_4"/>\n   <xs:enumeration value="Endrestore_5"/>\n   <xs:enumeration value="Abortrestore_6"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetReinitializedStateofDevice" name="BACnetReinitializedStateofDevice"/>\n <xs:complexType name="ListOfBACnetReinitializedStateofDevice">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetReinitializedStateofDevice" name="BACnetReinitializedStateofDevice" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetReinitializedStateofDevice" name="ListOfBACnetReinitializedStateofDevice" nillable="true"/>\n <xs:simpleType name="BACnetReliability">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NoFaultDetected_0"/>\n   <xs:enumeration value="NoSensor_1"/>\n   <xs:enumeration value="OverRange_2"/>\n   <xs:enumeration value="UnderRange_3"/>\n   <xs:enumeration value="OpenLoop_4"/>\n   <xs:enumeration value="ShortedLoop_5"/>\n   <xs:enumeration value="NoOutput_6"/>\n   <xs:enumeration value="UnreliableOther_7"/>\n   <xs:enumeration value="ProcessError_8"/>\n   <xs:enumeration value="MultiStateFault_9"/>\n   <xs:enumeration value="ConfigurationError_10"/>\n   <xs:enumeration value="CommunicationFailure_12"/>\n   <xs:enumeration value="MemberFault_13"/>\n   <xs:enumeration value="MONITORED_OBJECT_FAULT_14"/>\n   <xs:enumeration value="TRIPPED_15"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetReliability" name="BACnetReliability"/>\n <xs:complexType name="ListOfBACnetReliability">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetReliability" name="BACnetReliability" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetReliability" name="ListOfBACnetReliability" nillable="true"/>\n <xs:simpleType name="BACnetRestartReason">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="unknown_0"/>\n   <xs:enumeration value="coldstart_1"/>\n   <xs:enumeration value="warmstart_2"/>\n   <xs:enumeration value="detected_power_lost_3"/>\n   <xs:enumeration value="detected_powered_off_4"/>\n   <xs:enumeration value="hardware_watchdog_5"/>\n   <xs:enumeration value="software_watchdog_6"/>\n   <xs:enumeration value="suspended_7"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetRestartReason" name="BACnetRestartReason"/>\n <xs:complexType name="ListOfBACnetRestartReason">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetRestartReason" name="BACnetRestartReason" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetRestartReason" name="ListOfBACnetRestartReason" nillable="true"/>\n <xs:simpleType name="BACnetSegmentation">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="segmented-both_0"/>\n   <xs:enumeration value="segmented-transmit_1"/>\n   <xs:enumeration value="segmented-receive_2"/>\n   <xs:enumeration value="no-segmentation_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:BACnetSegmentation" name="BACnetSegmentation"/>\n <xs:complexType name="ListOfBACnetSegmentation">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetSegmentation" name="BACnetSegmentation" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetSegmentation" name="ListOfBACnetSegmentation" nillable="true"/>\n <xs:complexType name="BACnetAddress">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="NetworkNumber"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:base64Binary" name="MacAddress"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetAddress" name="BACnetAddress"/>\n <xs:complexType name="ListOfBACnetAddress">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetAddress" name="BACnetAddress" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetAddress" name="ListOfBACnetAddress" nillable="true"/>\n <xs:complexType name="BACnetAddressBinding">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="DeviceObjectIdentifier"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetAddress" name="DeviceAddress"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetAddressBinding" name="BACnetAddressBinding"/>\n <xs:complexType name="ListOfBACnetAddressBinding">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetAddressBinding" name="BACnetAddressBinding" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetAddressBinding" name="ListOfBACnetAddressBinding" nillable="true"/>\n <xs:complexType name="BACnetCOVSubscription">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetRecipientProcess" name="Recipient"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetDeviceObjectPropertyReference" name="MonitoredPropertyReference"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="IssueConfirmedNotifications"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="TimeRemaining"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="CovIncrement"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetCOVSubscription" name="BACnetCOVSubscription"/>\n <xs:complexType name="ListOfBACnetCOVSubscription">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetCOVSubscription" name="BACnetCOVSubscription" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetCOVSubscription" name="ListOfBACnetCOVSubscription" nillable="true"/>\n <xs:complexType name="BACnetDailySchedule">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfBACnetTimeValue" name="Day-schedule"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetDailySchedule" name="BACnetDailySchedule"/>\n <xs:complexType name="ListOfBACnetDailySchedule">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetDailySchedule" name="BACnetDailySchedule" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetDailySchedule" name="ListOfBACnetDailySchedule" nillable="true"/>\n <xs:complexType name="BACnetDate">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="Year"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetMonth" name="Month"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetDayOfMonth" name="DayOfMonth"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetDayOfWeek" name="DayOfWeek"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetDate" name="BACnetDate"/>\n <xs:complexType name="ListOfBACnetDate">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetDate" name="BACnetDate" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetDate" name="ListOfBACnetDate" nillable="true"/>\n <xs:complexType name="BACnetDateRange">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetDate" name="StartDate"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetDate" name="EndTime"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetDateRange" name="BACnetDateRange"/>\n <xs:complexType name="ListOfBACnetDateRange">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetDateRange" name="BACnetDateRange" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetDateRange" name="ListOfBACnetDateRange" nillable="true"/>\n <xs:complexType name="BACnetDateTime">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetDate" name="Date"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetTime" name="Time"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetDateTime" name="BACnetDateTime"/>\n <xs:complexType name="ListOfBACnetDateTime">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetDateTime" name="BACnetDateTime" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetDateTime" name="ListOfBACnetDateTime" nillable="true"/>\n <xs:complexType name="BACnetDestination">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetDaysOfWeek" name="ValidDays"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetTime" name="FromTime"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetTime" name="ToTime"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetRecipient" name="Recipient"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="ProcessIdentifier"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="IssueConfirmedNotifications"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetEventTransitionBits" name="Transitions"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetDestination" name="BACnetDestination"/>\n <xs:complexType name="ListOfBACnetDestination">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetDestination" name="BACnetDestination" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetDestination" name="ListOfBACnetDestination" nillable="true"/>\n <xs:complexType name="BACnetDeviceObjectPropertyReference">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="ObjectIdentifier"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetPropertyIdentifier" name="PropertyIdentifier"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="PropertyArrayIndex"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="DeviceIdentifier"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetDeviceObjectPropertyReference" name="BACnetDeviceObjectPropertyReference"/>\n <xs:complexType name="ListOfBACnetDeviceObjectPropertyReference">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetDeviceObjectPropertyReference" name="BACnetDeviceObjectPropertyReference" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetDeviceObjectPropertyReference" name="ListOfBACnetDeviceObjectPropertyReference" nillable="true"/>\n <xs:complexType name="BACnetEventFaultParameterExtended">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="VendorId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:Variant" name="Extended-fault-type"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfBACnetEventParameterExtendedParameters" name="Parameters"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetEventFaultParameterExtended" name="BACnetEventFaultParameterExtended"/>\n <xs:complexType name="ListOfBACnetEventFaultParameterExtended">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventFaultParameterExtended" name="BACnetEventFaultParameterExtended" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventFaultParameterExtended" name="ListOfBACnetEventFaultParameterExtended" nillable="true"/>\n <xs:complexType name="BACnetEventParameterBufferReady">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Notification-threshold"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Previous-notification-count"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetEventParameterBufferReady" name="BACnetEventParameterBufferReady"/>\n <xs:complexType name="ListOfBACnetEventParameterBufferReady">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventParameterBufferReady" name="BACnetEventParameterBufferReady" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventParameterBufferReady" name="ListOfBACnetEventParameterBufferReady" nillable="true"/>\n <xs:complexType name="BACnetEventParameterChangeOfBitstring">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Time-delay"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="Bitmask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="List-of-bitstring-values"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetEventParameterChangeOfBitstring" name="BACnetEventParameterChangeOfBitstring"/>\n <xs:complexType name="ListOfBACnetEventParameterChangeOfBitstring">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventParameterChangeOfBitstring" name="BACnetEventParameterChangeOfBitstring" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventParameterChangeOfBitstring" name="ListOfBACnetEventParameterChangeOfBitstring" nillable="true"/>\n <xs:complexType name="BACnetEventParameterChangeOfCharacterString">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Time-delay"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="AlarmValues"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetEventParameterChangeOfCharacterString" name="BACnetEventParameterChangeOfCharacterString"/>\n <xs:complexType name="ListOfBACnetEventParameterChangeOfCharacterString">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventParameterChangeOfCharacterString" name="BACnetEventParameterChangeOfCharacterString" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventParameterChangeOfCharacterString" name="ListOfBACnetEventParameterChangeOfCharacterString" nillable="true"/>\n <xs:complexType name="BACnetEventParameterChangeOfLifeSafety">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetLifeSafetyState" name="NewState"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetLifeSafetyMode" name="NewMode"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetLifeSafetyOperation" name="OperationExtended"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetEventParameterChangeOfLifeSafety" name="BACnetEventParameterChangeOfLifeSafety"/>\n <xs:complexType name="ListOfBACnetEventParameterChangeOfLifeSafety">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventParameterChangeOfLifeSafety" name="BACnetEventParameterChangeOfLifeSafety" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventParameterChangeOfLifeSafety" name="ListOfBACnetEventParameterChangeOfLifeSafety" nillable="true"/>\n <xs:complexType name="BACnetEventParameterChangeOfState">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Time-delay"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfBACnetPropertyStates" name="List-of-values"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetEventParameterChangeOfState" name="BACnetEventParameterChangeOfState"/>\n <xs:complexType name="ListOfBACnetEventParameterChangeOfState">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventParameterChangeOfState" name="BACnetEventParameterChangeOfState" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventParameterChangeOfState" name="ListOfBACnetEventParameterChangeOfState" nillable="true"/>\n <xs:complexType name="BACnetEventParameterChangeOfValue">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Time-delay"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="Cov-criteria-bitmask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="Cov-criteria-referenced-property-increment"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetEventParameterChangeOfValue" name="BACnetEventParameterChangeOfValue"/>\n <xs:complexType name="ListOfBACnetEventParameterChangeOfValue">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventParameterChangeOfValue" name="BACnetEventParameterChangeOfValue" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventParameterChangeOfValue" name="ListOfBACnetEventParameterChangeOfValue" nillable="true"/>\n <xs:complexType name="BACnetEventParameterCommandFailure">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Time-delay"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetDeviceObjectPropertyReference" name="Feedback-property-reference"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetEventParameterCommandFailure" name="BACnetEventParameterCommandFailure"/>\n <xs:complexType name="ListOfBACnetEventParameterCommandFailure">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventParameterCommandFailure" name="BACnetEventParameterCommandFailure" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventParameterCommandFailure" name="ListOfBACnetEventParameterCommandFailure" nillable="true"/>\n <xs:complexType name="BACnetEventParameterDoubleOutOfRange">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Time-delay"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Low-limit"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="High-limit"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Deadband"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetEventParameterDoubleOutOfRange" name="BACnetEventParameterDoubleOutOfRange"/>\n <xs:complexType name="ListOfBACnetEventParameterDoubleOutOfRange">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventParameterDoubleOutOfRange" name="BACnetEventParameterDoubleOutOfRange" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventParameterDoubleOutOfRange" name="ListOfBACnetEventParameterDoubleOutOfRange" nillable="true"/>\n <xs:complexType name="BACnetEventParameterFloatingLimit">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Time-delay"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetDeviceObjectPropertyReference" name="Setpoint-reference"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Low-diff-limit"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="High-diff-limit"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Deadband"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetEventParameterFloatingLimit" name="BACnetEventParameterFloatingLimit"/>\n <xs:complexType name="ListOfBACnetEventParameterFloatingLimit">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventParameterFloatingLimit" name="BACnetEventParameterFloatingLimit" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventParameterFloatingLimit" name="ListOfBACnetEventParameterFloatingLimit" nillable="true"/>\n <xs:complexType name="BACnetEventParameterOutOfRange">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Time-delay"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Low-limit"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="High-limit"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Deadband"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetEventParameterOutOfRange" name="BACnetEventParameterOutOfRange"/>\n <xs:complexType name="ListOfBACnetEventParameterOutOfRange">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventParameterOutOfRange" name="BACnetEventParameterOutOfRange" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventParameterOutOfRange" name="ListOfBACnetEventParameterOutOfRange" nillable="true"/>\n <xs:complexType name="BACnetEventParameterSignedOutOfRange">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Time-delay"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="Low-limit"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="High-limit"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Deadband"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetEventParameterSignedOutOfRange" name="BACnetEventParameterSignedOutOfRange"/>\n <xs:complexType name="ListOfBACnetEventParameterSignedOutOfRange">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventParameterSignedOutOfRange" name="BACnetEventParameterSignedOutOfRange" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventParameterSignedOutOfRange" name="ListOfBACnetEventParameterSignedOutOfRange" nillable="true"/>\n <xs:complexType name="BACnetEventParameterUnsignedOutOfRange">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Time-delay"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Low-limit"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="High-limit"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Deadband"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetEventParameterUnsignedOutOfRange" name="BACnetEventParameterUnsignedOutOfRange"/>\n <xs:complexType name="ListOfBACnetEventParameterUnsignedOutOfRange">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventParameterUnsignedOutOfRange" name="BACnetEventParameterUnsignedOutOfRange" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventParameterUnsignedOutOfRange" name="ListOfBACnetEventParameterUnsignedOutOfRange" nillable="true"/>\n <xs:complexType name="BACnetEventParameterUnsignedRange">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Time-delay"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Low-limit"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="High-limit"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetEventParameterUnsignedRange" name="BACnetEventParameterUnsignedRange"/>\n <xs:complexType name="ListOfBACnetEventParameterUnsignedRange">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventParameterUnsignedRange" name="BACnetEventParameterUnsignedRange" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventParameterUnsignedRange" name="ListOfBACnetEventParameterUnsignedRange" nillable="true"/>\n <xs:complexType name="BACnetFaultParameterFaultCharacterstring">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Fault-characterstring"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetFaultParameterFaultCharacterstring" name="BACnetFaultParameterFaultCharacterstring"/>\n <xs:complexType name="ListOfBACnetFaultParameterFaultCharacterstring">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetFaultParameterFaultCharacterstring" name="BACnetFaultParameterFaultCharacterstring" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetFaultParameterFaultCharacterstring" name="ListOfBACnetFaultParameterFaultCharacterstring" nillable="true"/>\n <xs:complexType name="BACnetFaultParameterFaultLifeSafety">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfBACnetLifeSafetyState" name="List-of-fault-values"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetDeviceObjectPropertyReference" name="Mode-property-reference"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetFaultParameterFaultLifeSafety" name="BACnetFaultParameterFaultLifeSafety"/>\n <xs:complexType name="ListOfBACnetFaultParameterFaultLifeSafety">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetFaultParameterFaultLifeSafety" name="BACnetFaultParameterFaultLifeSafety" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetFaultParameterFaultLifeSafety" name="ListOfBACnetFaultParameterFaultLifeSafety" nillable="true"/>\n <xs:complexType name="BACnetFaultParameterFaultState">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfBACnetProgramStates" name="List-of-fault-values"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetFaultParameterFaultState" name="BACnetFaultParameterFaultState"/>\n <xs:complexType name="ListOfBACnetFaultParameterFaultState">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetFaultParameterFaultState" name="BACnetFaultParameterFaultState" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetFaultParameterFaultState" name="ListOfBACnetFaultParameterFaultState" nillable="true"/>\n <xs:complexType name="BACnetFaultParameterFaultStatusFlags">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfBACnetDeviceObjectPropertyReference" name="Status-flags-reference"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetFaultParameterFaultStatusFlags" name="BACnetFaultParameterFaultStatusFlags"/>\n <xs:complexType name="ListOfBACnetFaultParameterFaultStatusFlags">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetFaultParameterFaultStatusFlags" name="BACnetFaultParameterFaultStatusFlags" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetFaultParameterFaultStatusFlags" name="ListOfBACnetFaultParameterFaultStatusFlags" nillable="true"/>\n <xs:complexType name="BACnetPropertyStates">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="BooleanValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetBinaryPV" name="BinaryValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetEventEnumType" name="EventType"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetPolarity" name="Polarity"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetProgramRequest" name="ProgramChange"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetProgramStates" name="ProgramState"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetProgramError" name="ProgramError"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetReliability" name="Reliability"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetEventState" name="State"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetDeviceStatus" name="SystemStatus"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:EUInformation" name="Units"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="UnsignedValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetLifeSafetyMode" name="LifeSafetyMode"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetLifeSafetyState" name="LifeSafetyState"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetPropertyStates" name="BACnetPropertyStates"/>\n <xs:complexType name="ListOfBACnetPropertyStates">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetPropertyStates" name="BACnetPropertyStates" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetPropertyStates" name="ListOfBACnetPropertyStates" nillable="true"/>\n <xs:complexType name="BACnetRecipientProcess">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetRecipient" name="Recipient"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="ProcessIdentifier"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetRecipientProcess" name="BACnetRecipientProcess"/>\n <xs:complexType name="ListOfBACnetRecipientProcess">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetRecipientProcess" name="BACnetRecipientProcess" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetRecipientProcess" name="ListOfBACnetRecipientProcess" nillable="true"/>\n <xs:complexType name="BACnetSpecialEvent">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetSpecialEventPeriod" name="Period"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfBACnetTimeValue" name="ListOfTimeValues"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="EventPriority"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetSpecialEvent" name="BACnetSpecialEvent"/>\n <xs:complexType name="ListOfBACnetSpecialEvent">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetSpecialEvent" name="BACnetSpecialEvent" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetSpecialEvent" name="ListOfBACnetSpecialEvent" nillable="true"/>\n <xs:complexType name="BACnetTime">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="Hour"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="Minute"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="Second"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedByte" name="Hundredths"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetTime" name="BACnetTime"/>\n <xs:complexType name="ListOfBACnetTime">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetTime" name="BACnetTime" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetTime" name="ListOfBACnetTime" nillable="true"/>\n <xs:complexType name="BACnetTimeValue">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetTime" name="Time"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetTimeValueValue" name="Value"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetTimeValue" name="BACnetTimeValue"/>\n <xs:complexType name="ListOfBACnetTimeValue">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetTimeValue" name="BACnetTimeValue" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetTimeValue" name="ListOfBACnetTimeValue" nillable="true"/>\n <xs:complexType name="BACnetTimeValueValue">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="BooleanValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:Variant" name="UnsignedValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:Variant" name="SignedValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:base64Binary" name="OctedStringValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="CharStringValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="ObjectIdentifierValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="EnumerationValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="BitStringValue"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetTimeValueValue" name="BACnetTimeValueValue"/>\n <xs:complexType name="ListOfBACnetTimeValueValue">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetTimeValueValue" name="BACnetTimeValueValue" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetTimeValueValue" name="ListOfBACnetTimeValueValue" nillable="true"/>\n <xs:complexType name="BACnetWeekNDay">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetMonth" name="Month"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetDay" name="Day"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetDayOfWeek" name="DayOfWeek"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetWeekNDay" name="BACnetWeekNDay"/>\n <xs:complexType name="ListOfBACnetWeekNDay">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetWeekNDay" name="BACnetWeekNDay" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetWeekNDay" name="ListOfBACnetWeekNDay" nillable="true"/>\n <xs:complexType name="BACnetDaysOfWeek">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence/>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:BACnetDaysOfWeek" name="BACnetDaysOfWeek"/>\n <xs:complexType name="ListOfBACnetDaysOfWeek">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetDaysOfWeek" name="BACnetDaysOfWeek" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetDaysOfWeek" name="ListOfBACnetDaysOfWeek" nillable="true"/>\n <xs:complexType name="BACnetEventTransitionBits">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence/>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:BACnetEventTransitionBits" name="BACnetEventTransitionBits"/>\n <xs:complexType name="ListOfBACnetEventTransitionBits">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventTransitionBits" name="BACnetEventTransitionBits" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventTransitionBits" name="ListOfBACnetEventTransitionBits" nillable="true"/>\n <xs:complexType name="BACnetLimitEnable">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence/>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:BACnetLimitEnable" name="BACnetLimitEnable"/>\n <xs:complexType name="ListOfBACnetLimitEnable">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetLimitEnable" name="BACnetLimitEnable" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetLimitEnable" name="ListOfBACnetLimitEnable" nillable="true"/>\n <xs:complexType name="BACnetObjectTypeSupportedBits">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence/>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:BACnetObjectTypeSupportedBits" name="BACnetObjectTypeSupportedBits"/>\n <xs:complexType name="ListOfBACnetObjectTypeSupportedBits">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetObjectTypeSupportedBits" name="BACnetObjectTypeSupportedBits" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetObjectTypeSupportedBits" name="ListOfBACnetObjectTypeSupportedBits" nillable="true"/>\n <xs:complexType name="BACnetServicesSupportedBits">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence/>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:BACnetServicesSupportedBits" name="BACnetServicesSupportedBits"/>\n <xs:complexType name="ListOfBACnetServicesSupportedBits">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetServicesSupportedBits" name="BACnetServicesSupportedBits" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetServicesSupportedBits" name="ListOfBACnetServicesSupportedBits" nillable="true"/>\n <xs:complexType name="BACnetStatusFlags">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence/>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:BACnetStatusFlags" name="BACnetStatusFlags"/>\n <xs:complexType name="ListOfBACnetStatusFlags">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetStatusFlags" name="BACnetStatusFlags" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetStatusFlags" name="ListOfBACnetStatusFlags" nillable="true"/>\n <xs:complexType name="BACnetCalendarEntry">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="SwitchField"/>\n   <xs:choice>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetDate" name="Date"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetDateRange" name="DateRange"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetWeekNDay" name="WeekNDay"/>\n   </xs:choice>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetCalendarEntry" name="BACnetCalendarEntry"/>\n <xs:complexType name="ListOfBACnetCalendarEntry">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetCalendarEntry" name="BACnetCalendarEntry" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetCalendarEntry" name="ListOfBACnetCalendarEntry" nillable="true"/>\n <xs:complexType name="BACnetClientCOV">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="SwitchField"/>\n   <xs:choice>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="Real-increment"/>\n   </xs:choice>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetClientCOV" name="BACnetClientCOV"/>\n <xs:complexType name="ListOfBACnetClientCOV">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetClientCOV" name="BACnetClientCOV" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetClientCOV" name="ListOfBACnetClientCOV" nillable="true"/>\n <xs:complexType name="BACnetEventParameter">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="SwitchField"/>\n   <xs:choice>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetEventParameterChangeOfBitstring" name="Change-of-bitstring"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetEventParameterChangeOfState" name="Change-of-state"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetEventParameterChangeOfValue" name="Change-of-value"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetEventParameterCommandFailure" name="Command-failure"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetEventParameterFloatingLimit" name="Floating-limit"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetEventParameterOutOfRange" name="Out-of-range"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetEventFaultParameterExtended" name="Extended"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetEventParameterBufferReady" name="Buffer-ready"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetEventParameterUnsignedRange" name="Unsigned-range"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetEventParameterDoubleOutOfRange" name="Double-out-of-range"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetEventParameterSignedOutOfRange" name="Signed-out-of-range"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetEventParameterUnsignedOutOfRange" name="Unsigned-out-of-range"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetEventParameterChangeOfCharacterString" name="Change-of-characterstring"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetEventParameterChangeOfLifeSafety" name="Change-of-life-safety"/>\n   </xs:choice>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetEventParameter" name="BACnetEventParameter"/>\n <xs:complexType name="ListOfBACnetEventParameter">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventParameter" name="BACnetEventParameter" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventParameter" name="ListOfBACnetEventParameter" nillable="true"/>\n <xs:complexType name="BACnetEventParameterExtendedParameters">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="SwitchField"/>\n   <xs:choice>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Real"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Unsigned"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="Boolean"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Double"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfByte" name="Octed"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="CharacterString"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="BitString"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Enum"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetDate" name="Date"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetTime" name="Time"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="ObjectIdentifier"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetDeviceObjectPropertyReference" name="Reference"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="Integer"/>\n   </xs:choice>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetEventParameterExtendedParameters" name="BACnetEventParameterExtendedParameters"/>\n <xs:complexType name="ListOfBACnetEventParameterExtendedParameters">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetEventParameterExtendedParameters" name="BACnetEventParameterExtendedParameters" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetEventParameterExtendedParameters" name="ListOfBACnetEventParameterExtendedParameters" nillable="true"/>\n <xs:complexType name="BACnetFaultParameter">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="SwitchField"/>\n   <xs:choice>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetFaultParameterFaultCharacterstring" name="Fault-characterstring"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetFaultParameterFaultLifeSafety" name="Fault-life-safety"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetFaultParameterFaultState" name="Fault-state"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetFaultParameterFaultStatusFlags" name="Fault-status-flags"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetEventFaultParameterExtended" name="Fault-extended"/>\n   </xs:choice>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetFaultParameter" name="BACnetFaultParameter"/>\n <xs:complexType name="ListOfBACnetFaultParameter">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetFaultParameter" name="BACnetFaultParameter" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetFaultParameter" name="ListOfBACnetFaultParameter" nillable="true"/>\n <xs:complexType name="BACnetMessageClass">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="SwitchField"/>\n   <xs:choice>\n    <xs:element minOccurs="0" maxOccurs="1" type="ua:Variant" name="Unsigned"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="String"/>\n   </xs:choice>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetMessageClass" name="BACnetMessageClass"/>\n <xs:complexType name="ListOfBACnetMessageClass">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetMessageClass" name="BACnetMessageClass" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetMessageClass" name="ListOfBACnetMessageClass" nillable="true"/>\n <xs:complexType name="BACnetPriorityValue">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="SwitchField"/>\n   <xs:choice>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:float" name="Real"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:int" name="Enumerated"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="ua:Variant" name="Unsigned"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="Boolean"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="ua:Variant" name="Signed"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Double"/>\n   </xs:choice>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetPriorityValue" name="BACnetPriorityValue"/>\n <xs:complexType name="ListOfBACnetPriorityValue">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetPriorityValue" name="BACnetPriorityValue" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetPriorityValue" name="ListOfBACnetPriorityValue" nillable="true"/>\n <xs:complexType name="BACnetRecipient">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="SwitchField"/>\n   <xs:choice>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Device"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetAddress" name="Address"/>\n   </xs:choice>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetRecipient" name="BACnetRecipient"/>\n <xs:complexType name="ListOfBACnetRecipient">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetRecipient" name="BACnetRecipient" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetRecipient" name="ListOfBACnetRecipient" nillable="true"/>\n <xs:complexType name="BACnetSpecialEventPeriod">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="SwitchField"/>\n   <xs:choice>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetCalendarEntry" name="CalendarEntry"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="CalendarReference"/>\n   </xs:choice>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetSpecialEventPeriod" name="BACnetSpecialEventPeriod"/>\n <xs:complexType name="ListOfBACnetSpecialEventPeriod">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetSpecialEventPeriod" name="BACnetSpecialEventPeriod" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetSpecialEventPeriod" name="ListOfBACnetSpecialEventPeriod" nillable="true"/>\n <xs:complexType name="BACnetTimeStamp">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="SwitchField"/>\n   <xs:choice>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetTime" name="Time"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedShort" name="SequenceNumber"/>\n    <xs:element minOccurs="0" maxOccurs="1" type="tns:BACnetDateTime" name="DateTime"/>\n   </xs:choice>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:BACnetTimeStamp" name="BACnetTimeStamp"/>\n <xs:complexType name="ListOfBACnetTimeStamp">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BACnetTimeStamp" name="BACnetTimeStamp" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBACnetTimeStamp" name="ListOfBACnetTimeStamp" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6500",
    browseName="EnumStrings",
    parent="ns=bacnet;i=3044",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[10],
    value=[
        o6.LocalizedText("None"),
        o6.LocalizedText("Silence"),
        o6.LocalizedText("SilenceAudible"),
        o6.LocalizedText("SilenceVisible"),
        o6.LocalizedText("Reset"),
        o6.LocalizedText("ResetAlarm"),
        o6.LocalizedText("ResetFault"),
        o6.LocalizedText("Unsilence"),
        o6.LocalizedText("UnsilenceAudible"),
        o6.LocalizedText("UnsilenceVisible"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6641",
    browseName="OptionSetValues",
    parent="ns=bacnet;i=3063",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[55],
    value=[
        o6.LocalizedText("analog-input"),
        o6.LocalizedText("analog-output"),
        o6.LocalizedText("analog-value"),
        o6.LocalizedText("binary-input"),
        o6.LocalizedText("binary-output"),
        o6.LocalizedText("binary-value"),
        o6.LocalizedText("calendar"),
        o6.LocalizedText("command"),
        o6.LocalizedText("device"),
        o6.LocalizedText("event-enrollment"),
        o6.LocalizedText("file"),
        o6.LocalizedText("group"),
        o6.LocalizedText("loop"),
        o6.LocalizedText("multi-state-input"),
        o6.LocalizedText("multi-state-output"),
        o6.LocalizedText("notification-class"),
        o6.LocalizedText("program"),
        o6.LocalizedText("schedule"),
        o6.LocalizedText("averaging"),
        o6.LocalizedText("multi-state-value"),
        o6.LocalizedText("trend-log"),
        o6.LocalizedText("life-safety-point"),
        o6.LocalizedText("life-safety-zone"),
        o6.LocalizedText("accumulator"),
        o6.LocalizedText("pulse-converter"),
        o6.LocalizedText("event-log"),
        o6.LocalizedText("global-group"),
        o6.LocalizedText("trend-log-multiple"),
        o6.LocalizedText("load-control"),
        o6.LocalizedText("structured-view"),
        o6.LocalizedText("access-door"),
        o6.LocalizedText("UNASSIGNED_31"),
        o6.LocalizedText("access-credential"),
        o6.LocalizedText("access-point"),
        o6.LocalizedText("access-rights"),
        o6.LocalizedText("access-user"),
        o6.LocalizedText("access-zone"),
        o6.LocalizedText("credential-data-input"),
        o6.LocalizedText("network-security"),
        o6.LocalizedText("bitstring-value"),
        o6.LocalizedText("characterstring-value"),
        o6.LocalizedText("date-pattern-value"),
        o6.LocalizedText("date-value"),
        o6.LocalizedText("datetime-pattern-value"),
        o6.LocalizedText("datetime-value"),
        o6.LocalizedText("integer-value"),
        o6.LocalizedText("large-analog-value"),
        o6.LocalizedText("octetstring-value"),
        o6.LocalizedText("positive-integer-value"),
        o6.LocalizedText("time-pattern-value"),
        o6.LocalizedText("time-value"),
        o6.LocalizedText("notification-forwarder"),
        o6.LocalizedText("alert-enrollment"),
        o6.LocalizedText("channel"),
        o6.LocalizedText("lighting-output"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6647",
    browseName="OptionSetValues",
    parent="ns=bacnet;i=3064",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[40],
    value=[
        o6.LocalizedText("acknowledgeAlarm"),
        o6.LocalizedText("confirmedCOVNotification"),
        o6.LocalizedText("confirmedEventNotification"),
        o6.LocalizedText("getAlarmSummary"),
        o6.LocalizedText("getEnrollmentSummary"),
        o6.LocalizedText("subscribeCOV"),
        o6.LocalizedText("atomicReadFile"),
        o6.LocalizedText("atomicWriteFile"),
        o6.LocalizedText("addListElement"),
        o6.LocalizedText("removeListElement"),
        o6.LocalizedText("createObject"),
        o6.LocalizedText("deleteObject"),
        o6.LocalizedText("readProperty"),
        o6.LocalizedText("UNASSIGNED_13"),
        o6.LocalizedText("readPropertyMultiple"),
        o6.LocalizedText("writeProperty"),
        o6.LocalizedText("writePropertyMultiple"),
        o6.LocalizedText("deviceCommunicationControl"),
        o6.LocalizedText("confirmedPrivateTransfer"),
        o6.LocalizedText("reinitializeDevice"),
        o6.LocalizedText("vtOpen"),
        o6.LocalizedText("vtClose"),
        o6.LocalizedText("vtData"),
        o6.LocalizedText("UNASSIGNED_24"),
        o6.LocalizedText("UNASSIGNED_25"),
        o6.LocalizedText("i-Am"),
        o6.LocalizedText("i-Have"),
        o6.LocalizedText("unconfirmedCOVNotification"),
        o6.LocalizedText("unconfirmedEventNotification"),
        o6.LocalizedText("unconfirmedPrivateTransfer"),
        o6.LocalizedText("unconfirmedTextMessage"),
        o6.LocalizedText("timeSynchronization"),
        o6.LocalizedText("who-Has"),
        o6.LocalizedText("who-Is"),
        o6.LocalizedText("readRange"),
        o6.LocalizedText("utcTimeSynchronization"),
        o6.LocalizedText("lifeSafetyOperation"),
        o6.LocalizedText("subscribeCOVProperty"),
        o6.LocalizedText("getEventInformation"),
        o6.LocalizedText("writeGroup"),
    ],
)
bacnet_objtypes.BACnetChangeOfStateAlgorithmType(
    nodeId="ns=bacnet;i=5137",
    browseName="ns=bacnet;EventAlgorithm",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6434", browseName="ns=bacnet;AlarmValues", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6663", browseName="ns=bacnet;TimeDelay", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6664", browseName="ns=bacnet;TimeDelayNormal", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
    ],
)
bacnet_objtypes.BACnetEventReportingType(
    nodeId="ns=bacnet;i=5072",
    browseName="ns=bacnet;EventReporting",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6279", browseName="ns=bacnet;Acked_Transitions", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6280", browseName="ns=bacnet;Event_Enable", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6281",
                browseName="ns=bacnet;Event_State",
                dataType=bacnet_datypes.BACnetEventState,
                value=bacnet_datypes.BACnetEventState.NORMAL,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6282",
                browseName="ns=bacnet;Event_Time_Stamps",
                dataType=bacnet_datypes.BACnetTimeStamp,
                valueRank=1,
                arrayDimensions=[3],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6283", browseName="ns=bacnet;Notification_Class", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6284", browseName="ns=bacnet;Notify_Type", dataType=bacnet_datypes.BACnetNotifyType, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=bacnet;i=5137"]),
    ],
)
o6.reference(bacnet_objtypes.BACnetBinaryInputType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=5072"])
bacnet_objtypes.BACnetCommandFailureAlgorithmType(
    nodeId="ns=bacnet;i=5138",
    browseName="ns=bacnet;EventAlgorithm",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6665", browseName="ns=bacnet;FeedbackValueRef", dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6666", browseName="ns=bacnet;TimeDelay", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6667", browseName="ns=bacnet;TimeDelayNormal", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
    ],
)
bacnet_objtypes.BACnetEventReportingType(
    nodeId="ns=bacnet;i=5073",
    browseName="ns=bacnet;EventReporting",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6285", browseName="ns=bacnet;Acked_Transitions", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6286", browseName="ns=bacnet;Event_Enable", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6287",
                browseName="ns=bacnet;Event_State",
                dataType=bacnet_datypes.BACnetEventState,
                value=bacnet_datypes.BACnetEventState.NORMAL,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6288",
                browseName="ns=bacnet;Event_Time_Stamps",
                dataType=bacnet_datypes.BACnetTimeStamp,
                valueRank=1,
                arrayDimensions=[3],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6289", browseName="ns=bacnet;Notification_Class", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6290", browseName="ns=bacnet;Notify_Type", dataType=bacnet_datypes.BACnetNotifyType, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=bacnet;i=5138"]),
    ],
)
o6.reference(bacnet_objtypes.BACnetBinaryOutputType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=5073"])
bacnet_objtypes.BACnetChangeOfStateAlgorithmType(
    nodeId="ns=bacnet;i=5139",
    browseName="ns=bacnet;EventAlgorithm",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6668", browseName="ns=bacnet;AlarmValues", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6669", browseName="ns=bacnet;TimeDelay", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6670", browseName="ns=bacnet;TimeDelayNormal", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
    ],
)
bacnet_objtypes.BACnetEventReportingType(
    nodeId="ns=bacnet;i=5074",
    browseName="ns=bacnet;EventReporting",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6292", browseName="ns=bacnet;Acked_Transitions", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6293", browseName="ns=bacnet;Event_Enable", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6294",
                browseName="ns=bacnet;Event_State",
                dataType=bacnet_datypes.BACnetEventState,
                value=bacnet_datypes.BACnetEventState.NORMAL,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6295",
                browseName="ns=bacnet;Event_Time_Stamps",
                dataType=bacnet_datypes.BACnetTimeStamp,
                valueRank=1,
                arrayDimensions=[3],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6296", browseName="ns=bacnet;Notification_Class", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6297", browseName="ns=bacnet;Notify_Type", dataType=bacnet_datypes.BACnetNotifyType, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=bacnet;i=5139"]),
    ],
)
o6.reference(bacnet_objtypes.BACnetBinaryValueType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=5074"])
bacnet_objtypes.BACnetChangeOfStateAlgorithmType(
    nodeId="ns=bacnet;i=5140",
    browseName="ns=bacnet;EventAlgorithm",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6671", browseName="ns=bacnet;AlarmValues", dataType=ns0.datatypes.UInteger, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6672", browseName="ns=bacnet;TimeDelay", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6673", browseName="ns=bacnet;TimeDelayNormal", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
    ],
)
bacnet_objtypes.BACnetEventReportingType(
    nodeId="ns=bacnet;i=5075",
    browseName="ns=bacnet;EventReporting",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6298", browseName="ns=bacnet;Acked_Transitions", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6299", browseName="ns=bacnet;Event_Enable", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6300",
                browseName="ns=bacnet;Event_State",
                dataType=bacnet_datypes.BACnetEventState,
                value=bacnet_datypes.BACnetEventState.NORMAL,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6301",
                browseName="ns=bacnet;Event_Time_Stamps",
                dataType=bacnet_datypes.BACnetTimeStamp,
                valueRank=1,
                arrayDimensions=[3],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6302", browseName="ns=bacnet;Notification_Class", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6303", browseName="ns=bacnet;Notify_Type", dataType=bacnet_datypes.BACnetNotifyType, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=bacnet;i=5140"]),
    ],
)
o6.reference(bacnet_objtypes.BACnetMultiStateInputType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=5075"])
bacnet_objtypes.BACnetFaultStateAlgorithmType(
    nodeId="ns=bacnet;i=5141",
    browseName="ns=bacnet;FaultAlgorithm",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6674", browseName="ns=bacnet;FaultValues", dataType=ns0.datatypes.UInteger, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
            )
        )
    ],
)
bacnet_objtypes.BACnetFaultEvaluationType(
    nodeId="ns=bacnet;i=5076",
    browseName="ns=bacnet;FaultEvaluation",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6319", browseName="ns=bacnet;Reliability", dataType=bacnet_datypes.BACnetReliability, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=bacnet;i=5141"]),
    ],
)
o6.reference(bacnet_objtypes.BACnetMultiStateInputType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=5076"])
bacnet_objtypes.BACnetCommandFailureAlgorithmType(
    nodeId="ns=bacnet;i=5142",
    browseName="ns=bacnet;EventAlgorithm",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6675", browseName="ns=bacnet;FeedbackValueRef", dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6676", browseName="ns=bacnet;TimeDelay", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6677", browseName="ns=bacnet;TimeDelayNormal", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
    ],
)
bacnet_objtypes.BACnetEventReportingType(
    nodeId="ns=bacnet;i=5077",
    browseName="ns=bacnet;EventReporting",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6306", browseName="ns=bacnet;Acked_Transitions", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6307", browseName="ns=bacnet;Event_Enable", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6308",
                browseName="ns=bacnet;Event_State",
                dataType=bacnet_datypes.BACnetEventState,
                value=bacnet_datypes.BACnetEventState.NORMAL,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6309",
                browseName="ns=bacnet;Event_Time_Stamps",
                dataType=bacnet_datypes.BACnetTimeStamp,
                valueRank=1,
                arrayDimensions=[3],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6310", browseName="ns=bacnet;Notification_Class", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6311", browseName="ns=bacnet;Notify_Type", dataType=bacnet_datypes.BACnetNotifyType, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=bacnet;i=5142"]),
    ],
)
o6.reference(bacnet_objtypes.BACnetMultiStateOutputType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=5077"])
bacnet_objtypes.BACnetChangeOfStateAlgorithmType(
    nodeId="ns=bacnet;i=5143",
    browseName="ns=bacnet;EventAlgorithm",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6678", browseName="ns=bacnet;AlarmValues", dataType=ns0.datatypes.UInteger, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6679", browseName="ns=bacnet;TimeDelay", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6680", browseName="ns=bacnet;TimeDelayNormal", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
    ],
)
bacnet_objtypes.BACnetEventReportingType(
    nodeId="ns=bacnet;i=5078",
    browseName="ns=bacnet;EventReporting",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6313", browseName="ns=bacnet;Acked_Transitions", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6314", browseName="ns=bacnet;Event_Enable", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6315",
                browseName="ns=bacnet;Event_State",
                dataType=bacnet_datypes.BACnetEventState,
                value=bacnet_datypes.BACnetEventState.NORMAL,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6316",
                browseName="ns=bacnet;Event_Time_Stamps",
                dataType=bacnet_datypes.BACnetTimeStamp,
                valueRank=1,
                arrayDimensions=[3],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6317", browseName="ns=bacnet;Notification_Class", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6318", browseName="ns=bacnet;Notify_Type", dataType=bacnet_datypes.BACnetNotifyType, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=bacnet;i=5143"]),
    ],
)
o6.reference(bacnet_objtypes.BACnetMultiStateValueType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=5078"])
bacnet_objtypes.BACnetFaultStateAlgorithmType(
    nodeId="ns=bacnet;i=5144",
    browseName="ns=bacnet;FaultAlgorithm",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6681", browseName="ns=bacnet;FaultValues", dataType=ns0.datatypes.UInteger, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
            )
        )
    ],
)
bacnet_objtypes.BACnetFaultEvaluationType(
    nodeId="ns=bacnet;i=5079",
    browseName="ns=bacnet;FaultEvaluation",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6320", browseName="ns=bacnet;Reliability", dataType=bacnet_datypes.BACnetReliability, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=bacnet;i=5144"]),
    ],
)
o6.reference(bacnet_objtypes.BACnetMultiStateValueType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=5079"])
bacnet_objtypes.BACnetFloatingLimitAlgorithmType(
    nodeId="ns=bacnet;i=5145",
    browseName="ns=bacnet;EventAlgorithm",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6683", browseName="ns=bacnet;Deadband", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6684", browseName="ns=bacnet;HighDiffLimit", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6685", browseName="ns=bacnet;LowDiffLimit", dataType=o6.Float, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6686", browseName="ns=bacnet;SetpointReference", dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6687", browseName="ns=bacnet;TimeDelay", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6688", browseName="ns=bacnet;TimeDelayNormal", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6700",
    browseName="OptionSetValues",
    parent="ns=bacnet;i=3065",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("InAlarm"), o6.LocalizedText("Fault"), o6.LocalizedText("Overriden"), o6.LocalizedText("OutOfService")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6701",
    browseName="OptionSetValues",
    parent="ns=bacnet;i=3062",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("lowLimitEnable"), o6.LocalizedText("highLimitEnable")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6702",
    browseName="OptionSetValues",
    parent="ns=bacnet;i=3061",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("to-offnormal"), o6.LocalizedText("to-fault"), o6.LocalizedText("to-normal")],
)
bacnet_objtypes.BACnetChangeOfStateCountType(
    nodeId="ns=bacnet;i=5007",
    browseName="ns=bacnet;ChangeOfState",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6065", browseName="ns=bacnet;Change_Of_State_Count", dataType=o6.UInt32, value=0, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6066", browseName="ns=bacnet;Change_Of_State_Time", dataType=bacnet_datypes.BACnetDateTime, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6067", browseName="ns=bacnet;Time_Of_State_Count_Reset", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.call(nodeId="ns=bacnet;i=7002", browseName="ns=bacnet;Reset")),
    ],
)
o6.reference(bacnet_objtypes.BACnetBinaryType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=5007"])
bacnet_objtypes.BACnetElapsedActiveTimeType(
    nodeId="ns=bacnet;i=5008",
    browseName="ns=bacnet;ElapsedActiveTime",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6074", browseName="ns=bacnet;Elapsed_Active_Time", dataType=o6.UInt32, value=0, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6075", browseName="ns=bacnet;Time_Of_Active_Time_Reset", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.call(nodeId="ns=bacnet;i=7004", browseName="ns=bacnet;Reset")),
    ],
)
o6.reference(bacnet_objtypes.BACnetBinaryType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=5008"])


ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6347",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=7026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Time", dataType=ns0.datatypes.UtcTime, valueRank=-1)],
)
o6.call(nodeId="ns=bacnet;i=7026", browseName="ns=bacnet;TimeSynchronization", inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6347"]))

ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105001", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105001"], "i=39", o6.ns["ns=bacnet;i=6174"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105002", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetDailySchedule, o6.ns["ns=bacnet;i=105002"])
o6.reference(o6.ns["ns=bacnet;i=105002"], "i=39", o6.ns["ns=bacnet;i=6177"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105003", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105003"], "i=39", o6.ns["ns=bacnet;i=6187"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105004", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetDeviceObjectPropertyReference, o6.ns["ns=bacnet;i=105004"])
o6.reference(o6.ns["ns=bacnet;i=105004"], "i=39", o6.ns["ns=bacnet;i=6188"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105005", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105005"], "i=39", o6.ns["ns=bacnet;i=6414"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105006", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetSpecialEvent, o6.ns["ns=bacnet;i=105006"])
o6.reference(o6.ns["ns=bacnet;i=105006"], "i=39", o6.ns["ns=bacnet;i=6417"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105007", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105007"], "i=39", o6.ns["ns=bacnet;i=6420"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105008", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetTimeValue, o6.ns["ns=bacnet;i=105008"])
o6.reference(o6.ns["ns=bacnet;i=105008"], "i=39", o6.ns["ns=bacnet;i=6421"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105009", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105009"], "i=39", o6.ns["ns=bacnet;i=6193"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105010", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterChangeOfBitstring, o6.ns["ns=bacnet;i=105010"])
o6.reference(o6.ns["ns=bacnet;i=105010"], "i=39", o6.ns["ns=bacnet;i=6194"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105017", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105017"], "i=39", o6.ns["ns=bacnet;i=6197"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105018", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterChangeOfState, o6.ns["ns=bacnet;i=105018"])
o6.reference(o6.ns["ns=bacnet;i=105018"], "i=39", o6.ns["ns=bacnet;i=6198"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105019", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105019"], "i=39", o6.ns["ns=bacnet;i=6422"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105020", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetTimeValueValue, o6.ns["ns=bacnet;i=105020"])
o6.reference(o6.ns["ns=bacnet;i=105020"], "i=39", o6.ns["ns=bacnet;i=6423"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105025", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105025"], "i=39", o6.ns["ns=bacnet;i=6170"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105026", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetAddressBinding, o6.ns["ns=bacnet;i=105026"])
o6.reference(o6.ns["ns=bacnet;i=105026"], "i=39", o6.ns["ns=bacnet;i=6171"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105027", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105027"], "i=39", o6.ns["ns=bacnet;i=6172"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105028", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetCOVSubscription, o6.ns["ns=bacnet;i=105028"])
o6.reference(o6.ns["ns=bacnet;i=105028"], "i=39", o6.ns["ns=bacnet;i=6173"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105029", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105029"], "i=39", o6.ns["ns=bacnet;i=6412"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105030", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetRecipientProcess, o6.ns["ns=bacnet;i=105030"])
o6.reference(o6.ns["ns=bacnet;i=105030"], "i=39", o6.ns["ns=bacnet;i=6413"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105031", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105031"], "i=39", o6.ns["ns=bacnet;i=6185"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105032", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetDestination, o6.ns["ns=bacnet;i=105032"])
o6.reference(o6.ns["ns=bacnet;i=105032"], "i=39", o6.ns["ns=bacnet;i=6186"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105036", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105036"], "i=39", o6.ns["ns=bacnet;i=6401"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105037", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetFaultParameterFaultCharacterstring, o6.ns["ns=bacnet;i=105037"])
o6.reference(o6.ns["ns=bacnet;i=105037"], "i=39", o6.ns["ns=bacnet;i=6402"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105038", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105038"], "i=39", o6.ns["ns=bacnet;i=6189"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105039", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetEventFaultParameterExtended, o6.ns["ns=bacnet;i=105039"])
o6.reference(o6.ns["ns=bacnet;i=105039"], "i=39", o6.ns["ns=bacnet;i=6190"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105040", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105040"], "i=39", o6.ns["ns=bacnet;i=6403"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105041", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetFaultParameterFaultLifeSafety, o6.ns["ns=bacnet;i=105041"])
o6.reference(o6.ns["ns=bacnet;i=105041"], "i=39", o6.ns["ns=bacnet;i=6404"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105042", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105042"], "i=39", o6.ns["ns=bacnet;i=6405"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105043", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetFaultParameterFaultState, o6.ns["ns=bacnet;i=105043"])
o6.reference(o6.ns["ns=bacnet;i=105043"], "i=39", o6.ns["ns=bacnet;i=6406"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105044", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105044"], "i=39", o6.ns["ns=bacnet;i=6407"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105045", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetFaultParameterFaultStatusFlags, o6.ns["ns=bacnet;i=105045"])
o6.reference(o6.ns["ns=bacnet;i=105045"], "i=39", o6.ns["ns=bacnet;i=6408"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105048", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105048"], "i=39", o6.ns["ns=bacnet;i=6199"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105049", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterChangeOfValue, o6.ns["ns=bacnet;i=105049"])
o6.reference(o6.ns["ns=bacnet;i=105049"], "i=39", o6.ns["ns=bacnet;i=6200"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105052", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105052"], "i=39", o6.ns["ns=bacnet;i=6202"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105053", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterCommandFailure, o6.ns["ns=bacnet;i=105053"])
o6.reference(o6.ns["ns=bacnet;i=105053"], "i=39", o6.ns["ns=bacnet;i=6203"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105054", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105054"], "i=39", o6.ns["ns=bacnet;i=6207"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105055", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterFloatingLimit, o6.ns["ns=bacnet;i=105055"])
o6.reference(o6.ns["ns=bacnet;i=105055"], "i=39", o6.ns["ns=bacnet;i=6212"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105056", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105056"], "i=39", o6.ns["ns=bacnet;i=6234"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105057", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterOutOfRange, o6.ns["ns=bacnet;i=105057"])
o6.reference(o6.ns["ns=bacnet;i=105057"], "i=39", o6.ns["ns=bacnet;i=6250"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105058", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105058"], "i=39", o6.ns["ns=bacnet;i=6191"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105059", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterBufferReady, o6.ns["ns=bacnet;i=105059"])
o6.reference(o6.ns["ns=bacnet;i=105059"], "i=39", o6.ns["ns=bacnet;i=6192"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105060", browseName="Default Binary")
o6.reference(o6.ns["ns=bacnet;i=105060"], "i=39", o6.ns["ns=bacnet;i=6258"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=bacnet;i=105061", browseName="Default XML")
o6.hasEncoding(bacnet_datypes.BACnetEventParameterUnsignedOutOfRange, o6.ns["ns=bacnet;i=105061"])
o6.reference(o6.ns["ns=bacnet;i=105061"], "i=39", o6.ns["ns=bacnet;i=6341"])
bacnet_objtypes.BACnetFaultEvaluationType(
    nodeId="ns=bacnet;i=105070",
    browseName="ns=bacnet;FaultEvaluation",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6374", browseName="ns=bacnet;Reliability", dataType=bacnet_datypes.BACnetReliability, accessLevel=3, userAccessLevel=1)
        )
    ],
)
o6.reference(bacnet_objtypes.BACnetMultiStateType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=105070"])
bacnet_objtypes.BACnetFaultEvaluationType(
    nodeId="ns=bacnet;i=105071",
    browseName="ns=bacnet;FaultEvaluation",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6375", browseName="ns=bacnet;Reliability", dataType=bacnet_datypes.BACnetReliability, accessLevel=3, userAccessLevel=1)
        )
    ],
)
o6.reference(bacnet_objtypes.BACnetScheduleType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=105071"])
bacnet_objtypes.BACnetFaultEvaluationType(
    nodeId="ns=bacnet;i=105072",
    browseName="ns=bacnet;FaultEvaluation",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6376", browseName="ns=bacnet;Reliability", dataType=bacnet_datypes.BACnetReliability, accessLevel=3, userAccessLevel=1)
        )
    ],
)
o6.reference(bacnet_objtypes.BACnetLoopType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=105072"])
bacnet_objtypes.BACnetFaultEvaluationType(
    nodeId="ns=bacnet;i=105074",
    browseName="ns=bacnet;FaultEvaluation",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6377", browseName="ns=bacnet;Reliability", dataType=bacnet_datypes.BACnetReliability, accessLevel=3, userAccessLevel=1)
        )
    ],
)
o6.reference(bacnet_objtypes.BACnetEventEnrollmentType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=105074"])
bacnet_objtypes.BACnetFaultEvaluationType(
    nodeId="ns=bacnet;i=105075",
    browseName="ns=bacnet;FaultEvaluation",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6378", browseName="ns=bacnet;Reliability", dataType=bacnet_datypes.BACnetReliability, accessLevel=3, userAccessLevel=1)
        )
    ],
)
o6.reference(bacnet_objtypes.BACnetLogType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=105075"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=bacnet;i=105084",
    browseName="ns=bacnet;Object_List",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6230",
                browseName="ns=bacnet;Object_List",
                dataType=bacnet_datypes.BACnetObjectIdentifier,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=bacnet;i=5037"]),
    ],
)
o6.reference(bacnet_objtypes.BACnetDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=105084"])
bacnet_objtypes.BACnetTimeManagementType(
    nodeId="ns=bacnet;i=105085",
    browseName="ns=bacnet;TimeManagement",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6240",
                browseName="ns=bacnet;Local_Date",
                dataType=bacnet_datypes.BACnetDate,
                value=bacnet_datypes.BACnetDate(
                    year=0, month=bacnet_datypes.BACnetMonth.JANUARY, dayOfMonth=bacnet_datypes.BACnetDayOfMonth(11), dayOfWeek=bacnet_datypes.BACnetDayOfWeek.MONDAY
                ),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6241", browseName="ns=bacnet;Local_Time", dataType=bacnet_datypes.BACnetTime, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6242", browseName="ns=bacnet;UTC_Offse", dataType=o6.Int16, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6243", browseName="ns=bacnet;Daylight_Savings_Status", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=bacnet;i=7026"]),
    ],
)
o6.reference(bacnet_objtypes.BACnetDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=105085"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=bacnet;i=105094",
    browseName="ns=bacnet;Structured_Object_List",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6235",
                browseName="ns=bacnet;Structured_Object_List",
                dataType=bacnet_datypes.BACnetObjectIdentifier,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=bacnet;i=5039"]),
    ],
)
o6.reference(bacnet_objtypes.BACnetDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=105094"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=bacnet;i=105095",
    browseName="ns=bacnet;Object_List",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6233",
                browseName="ns=bacnet;Object_List",
                dataType=bacnet_datypes.BACnetObjectIdentifier,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=bacnet;i=5038"]),
    ],
)
bacnet_objtypes.BACnetDeviceType(
    nodeId="ns=bacnet;i=5040",
    browseName="ns=bacnet;<BACnetDeviceName>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6028", browseName="ns=bacnet;Object_Identifier", dataType=bacnet_datypes.BACnetObjectIdentifier, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6214", browseName="ns=bacnet;Serial_Number", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6215", browseName="ns=bacnet;Vendor_Name", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6216", browseName="ns=bacnet;Vendor_Identifier", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6217", browseName="ns=bacnet;Model_Name", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6218", browseName="ns=bacnet;Protocol_Version", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6219", browseName="ns=bacnet;Protocol_Revision", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6220", browseName="ns=bacnet;Firmware_Revision", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6221", browseName="ns=bacnet;Application_Software_Version", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6223", browseName="ns=bacnet;Segmentation_Supported", dataType=bacnet_datypes.BACnetSegmentation, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6224", browseName="ns=bacnet;Max_APDU_Length_Accepted", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6225", browseName="ns=bacnet;APDU_Timeout", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6226", browseName="ns=bacnet;Number_Of_APDU_Retries", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6227", browseName="ns=bacnet;Protocol_Services_Supported", dataType=bacnet_datypes.BACnetServicesSupportedBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6228",
                browseName="ns=bacnet;Device_Address_Binding",
                dataType=bacnet_datypes.BACnetAddressBinding,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6229", browseName="ns=bacnet;Database_Revision", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6244", browseName="ns=bacnet;System_Status", dataType=bacnet_datypes.BACnetDeviceStatus, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6397",
                browseName="ns=bacnet;Protocol_Object_Types_Supported",
                dataType=bacnet_datypes.BACnetObjectTypeSupportedBits,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=bacnet;i=105095"]),
    ],
)
o6.reference(bacnet_objtypes.BACnetInternetworkType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=5040"])
bacnet_objtypes.BACnetFaultEvaluationType(
    nodeId="ns=bacnet;i=105097",
    browseName="ns=bacnet;FaultEvaluation",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6380", browseName="ns=bacnet;Reliability", dataType=bacnet_datypes.BACnetReliability, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=bacnet;i=5071"]),
    ],
)
o6.reference(bacnet_objtypes.BACnetAnalogType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=105097"])
bacnet_objtypes.BACnetFaultEvaluationType(
    nodeId="ns=bacnet;i=105098",
    browseName="ns=bacnet;FaultEvaluation",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6381", browseName="ns=bacnet;Reliability", dataType=bacnet_datypes.BACnetReliability, accessLevel=3, userAccessLevel=1)
        )
    ],
)
o6.reference(bacnet_objtypes.BACnetBinaryType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=105098"])
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=106001",
    browseName="EnumValues",
    parent="ns=bacnet;i=3001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[15],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("NoFaultDetected"), description=o6.LocalizedText("The present value is reliable; that is, no other fault has been detected.")
        ),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("NoSensor"), description=o6.LocalizedText("No sensor is connected to the Input object.")),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("OverRange"),
            description=o6.LocalizedText(
                "The sensor connected to the Input is reading a value higher than the normal operating range. If the object is a Binary Input, this is possible when the Binary state is derived from an analog sensor or a binary input equipped with electrical loop supervision circuits."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("UnderRange"),
            description=o6.LocalizedText(
                "The sensor connected to the Input is reading a value lower than the normal operating range. If the object is a Binary Input, this is possible when the Binary Input is actually a binary state calculated from an analog sensor."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("OpenLoop"),
            description=o6.LocalizedText("The connection between the defined object and the physical device is providing a value indicating an open circuit condition."),
        ),
        ns0.datatypes.EnumValueType(
            value=5,
            displayName=o6.LocalizedText("ShortedLoop"),
            description=o6.LocalizedText("The connection between the defined object and the physical device is providing a value indicating a short circuit condition."),
        ),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("NoOutput"), description=o6.LocalizedText("No physical device is connected to the Output object.")),
        ns0.datatypes.EnumValueType(
            value=7,
            displayName=o6.LocalizedText("UnreliableOther"),
            description=o6.LocalizedText(
                "The controller has detected that the present value is unreliable, but none of the other conditions describe the nature of the problem. A generic fault other than those listed above has been detected, e.g., a Binary Input is not cycling as expected."
            ),
        ),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("ProcessError"), description=o6.LocalizedText("A processing error was encountered.")),
        ns0.datatypes.EnumValueType(
            value=9,
            displayName=o6.LocalizedText("MultiStateFault"),
            description=o6.LocalizedText("The FAULT_STATE, FAULT_LIFE_SAFETY or FAULT_CHARACTERSTRING fault algorithm has evaluated a fault condition."),
        ),
        ns0.datatypes.EnumValueType(
            value=10, displayName=o6.LocalizedText("ConfigurationError"), description=o6.LocalizedText("The object's properties are not in a consistent state.")
        ),
        ns0.datatypes.EnumValueType(
            value=12,
            displayName=o6.LocalizedText("CommunicationFailure"),
            description=o6.LocalizedText(
                "Proper operation of the object is dependent on communication with a remote sensor or device and communication with the remote sensor or device has been lost."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=13,
            displayName=o6.LocalizedText("MemberFault"),
            description=o6.LocalizedText(
                "Indicates that the set of referenced member objects includes one or more Status_Flags properties whose FAULT flag value is equal to TRUE."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=14, displayName=o6.LocalizedText("MONITORED_OBJECT_FAULT"), description=o6.LocalizedText("Indicates that the monitored object is in fault.")
        ),
        ns0.datatypes.EnumValueType(
            value=15,
            displayName=o6.LocalizedText("TRIPPED"),
            description=o6.LocalizedText(
                "The end device, such as an actuator, is not responding to commands, prevented by a tripped condition or by being mechanically held open."
            ),
        ),
    ],
)
bacnet_objtypes.BACnetEventReportingType(
    nodeId="ns=bacnet;i=105013",
    browseName="ns=bacnet;EventReporting",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6357",
                browseName="ns=bacnet;Event_State",
                dataType=bacnet_datypes.BACnetEventState,
                value=bacnet_datypes.BACnetEventState.NORMAL,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106016", browseName="ns=bacnet;Acked_Transitions", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106023", browseName="ns=bacnet;Event_Enable", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106025",
                browseName="ns=bacnet;Event_Time_Stamps",
                dataType=bacnet_datypes.BACnetTimeStamp,
                valueRank=1,
                arrayDimensions=[3],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106026", browseName="ns=bacnet;Notification_Class", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106027", browseName="ns=bacnet;Notify_Type", dataType=bacnet_datypes.BACnetNotifyType, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(o6.ns["ns=bacnet;i=5145"]),
    ],
)
o6.reference(bacnet_objtypes.BACnetLoopType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=105013"])
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=106083",
    browseName="EnumStrings",
    parent="ns=bacnet;i=103028",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        o6.LocalizedText("none"),
        o6.LocalizedText("fault-characterstring"),
        o6.LocalizedText("fault-exended"),
        o6.LocalizedText("fault-life-safety"),
        o6.LocalizedText("fault-state"),
        o6.LocalizedText("fault-status-flags"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=106086",
    browseName="EnumStrings",
    parent="ns=bacnet;i=103011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("segmented-both"), o6.LocalizedText("segmented-transmit"), o6.LocalizedText("segmented-receive"), o6.LocalizedText("no-segmentation")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=106116",
    browseName="EnumStrings",
    parent="ns=bacnet;i=103016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        o6.LocalizedText("Idle"),
        o6.LocalizedText("Preparing_For_Backup"),
        o6.LocalizedText("Preparing_For_Restore"),
        o6.LocalizedText("Performing_A_Backup"),
        o6.LocalizedText("Performing_A_Restore"),
        o6.LocalizedText("Backup_Failure"),
        o6.LocalizedText("Restore_Failure"),
    ],
)
bacnet_objtypes.BACnetMstpMasterType(
    nodeId="ns=bacnet;i=105087",
    browseName="ns=bacnet;MstpMaster",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6262", browseName="ns=bacnet;Auto_Slave_Discovery", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6263",
                browseName="ns=bacnet;Manual_Slave_Address_Binding",
                dataType=bacnet_datypes.BACnetAddressBinding,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6264",
                browseName="ns=bacnet;Slave_Address_Binding",
                dataType=bacnet_datypes.BACnetAddressBinding,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6265", browseName="ns=bacnet;Slave_Proxy_Enable", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106125", browseName="ns=bacnet;Max_Info_Frames", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106126", browseName="ns=bacnet;Max_Master", dataType=o6.Byte, accessLevel=3, userAccessLevel=1)),
    ],
)
o6.reference(bacnet_objtypes.BACnetDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=105087"])
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=106127",
    browseName="EnumStrings",
    parent="ns=bacnet;i=103019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        o6.LocalizedText("unknown"),
        o6.LocalizedText("coldstart"),
        o6.LocalizedText("warmstart"),
        o6.LocalizedText("detected_power_lost"),
        o6.LocalizedText("detected_powered_off"),
        o6.LocalizedText("hardware_watchdog"),
        o6.LocalizedText("software_watchdog"),
        o6.LocalizedText("suspended"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=106169",
    browseName="EnumValues",
    parent="ns=bacnet;i=103036",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Monday")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Tuesday")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Wednesday")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Thursday")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Friday")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("Saturday")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("Sunday")),
        ns0.datatypes.EnumValueType(value=255, displayName=o6.LocalizedText("unspecified")),
    ],
)
bacnet_objtypes.BACnetBufferReadyAlgorithmType(
    nodeId="ns=bacnet;i=105077",
    browseName="ns=bacnet;EventAlgorithm",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6654", browseName="ns=bacnet;TimeDelay", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6655", browseName="ns=bacnet;TimeDelayNormal", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106230", browseName="ns=bacnet;Threshold", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106231", browseName="ns=bacnet;PreviousCount", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
    ],
)
bacnet_objtypes.BACnetEventReportingType(
    nodeId="ns=bacnet;i=105076",
    browseName="ns=bacnet;EventReporting",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6359",
                browseName="ns=bacnet;Event_State",
                dataType=bacnet_datypes.BACnetEventState,
                value=bacnet_datypes.BACnetEventState.NORMAL,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106220", browseName="ns=bacnet;Event_Message_Texts", dataType=o6.String, valueRank=1, arrayDimensions=[3], accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106221", browseName="ns=bacnet;Acked_Transitions", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106222", browseName="ns=bacnet;Event_Enable", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106224",
                browseName="ns=bacnet;Event_Time_Stamps",
                dataType=bacnet_datypes.BACnetTimeStamp,
                valueRank=1,
                arrayDimensions=[3],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106225", browseName="ns=bacnet;Notification_Class", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106226", browseName="ns=bacnet;Notify_Type", dataType=bacnet_datypes.BACnetNotifyType, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106227",
                browseName="ns=bacnet;Event_Message_Texts_Config",
                dataType=o6.String,
                valueRank=1,
                arrayDimensions=[3],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=bacnet;i=105077"]),
    ],
)
o6.reference(bacnet_objtypes.BACnetLogType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=105076"])
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=106235",
    browseName="EnumStrings",
    parent="ns=bacnet;i=103048",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("Polled"), o6.LocalizedText("COV"), o6.LocalizedText("Triggered")],
)
bacnet_objtypes.BACnetOutOfRangeAlgorithmType(
    nodeId="ns=bacnet;i=105068",
    browseName="ns=bacnet;EventAlgorithm",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6650", browseName="ns=bacnet;TimeDelay", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6651", browseName="ns=bacnet;TimeDelayNormal", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106257", browseName="ns=bacnet;Deadband", dataType=o6.Float, value=0.0, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106258", browseName="ns=bacnet;HighLimit", dataType=o6.Float, value=0.0, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106259", browseName="ns=bacnet;LimitEnable", dataType=bacnet_datypes.BACnetLimitEnable, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106260", browseName="ns=bacnet;LowLimit", dataType=o6.Float, value=0.0, accessLevel=3, userAccessLevel=1)),
    ],
)
bacnet_objtypes.BACnetEventReportingType(
    nodeId="ns=bacnet;i=5001",
    browseName="ns=bacnet;EventReporting",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6005", browseName="ns=bacnet;Acked_Transitions", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6006", browseName="ns=bacnet;Event_Enable", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6009",
                browseName="ns=bacnet;Event_Time_Stamps",
                dataType=bacnet_datypes.BACnetTimeStamp,
                valueRank=1,
                arrayDimensions=[3],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6010", browseName="ns=bacnet;Notification_Class", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6011", browseName="ns=bacnet;Notify_Type", dataType=bacnet_datypes.BACnetNotifyType, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6036", browseName="ns=bacnet;Event_Algorithm_Inhibit", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6056",
                browseName="ns=bacnet;Event_State",
                dataType=bacnet_datypes.BACnetEventState,
                value=bacnet_datypes.BACnetEventState.NORMAL,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6275",
                browseName="ns=bacnet;Event_Algorithm_Inhibit_Ref",
                dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6276", browseName="ns=bacnet;Event_Detection_Enable", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6277", browseName="ns=bacnet;Event_Message_Texts", dataType=o6.String, valueRank=1, arrayDimensions=[3], accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6278", browseName="ns=bacnet;Event_Message_Texts_Config", dataType=o6.String, valueRank=1, arrayDimensions=[3], accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=bacnet;i=105068"]),
    ],
)
o6.reference(bacnet_objtypes.BACnetAnalogType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=5001"])
bacnet_objtypes.BACnetEventReportingType(
    nodeId="ns=bacnet;i=105092",
    browseName="ns=bacnet;EventReporting",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6360",
                browseName="ns=bacnet;Event_State",
                dataType=bacnet_datypes.BACnetEventState,
                value=bacnet_datypes.BACnetEventState.NORMAL,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106264", browseName="ns=bacnet;Acked_Transitions", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106265", browseName="ns=bacnet;Event_Enable", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106267",
                browseName="ns=bacnet;Event_Time_Stamps",
                dataType=bacnet_datypes.BACnetTimeStamp,
                valueRank=1,
                arrayDimensions=[3],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106268", browseName="ns=bacnet;Notification_Class", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106269", browseName="ns=bacnet;Notify_Type", dataType=bacnet_datypes.BACnetNotifyType, accessLevel=3, userAccessLevel=1)
        ),
    ],
)
o6.reference(bacnet_objtypes.BACnetBinaryType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=105092"])
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=106272",
    browseName="EnumStrings",
    parent="ns=bacnet;i=103053",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[55],
    value=[
        o6.LocalizedText("analog-input"),
        o6.LocalizedText("analog-output"),
        o6.LocalizedText("analog-value"),
        o6.LocalizedText("binary-input"),
        o6.LocalizedText("binary-output"),
        o6.LocalizedText("binary-value"),
        o6.LocalizedText("calendar"),
        o6.LocalizedText("command"),
        o6.LocalizedText("device"),
        o6.LocalizedText("event-enrollment"),
        o6.LocalizedText("file"),
        o6.LocalizedText("group"),
        o6.LocalizedText("loop"),
        o6.LocalizedText("multi-state-input"),
        o6.LocalizedText("multi-state-output"),
        o6.LocalizedText("notification-class"),
        o6.LocalizedText("program"),
        o6.LocalizedText("schedule"),
        o6.LocalizedText("averaging"),
        o6.LocalizedText("multi-state-value"),
        o6.LocalizedText("trend-log"),
        o6.LocalizedText("life-safety-point"),
        o6.LocalizedText("life-safety-zone"),
        o6.LocalizedText("accumulator"),
        o6.LocalizedText("pulse-converter"),
        o6.LocalizedText("event-log"),
        o6.LocalizedText("global-group"),
        o6.LocalizedText("trend-log-multiple"),
        o6.LocalizedText("load-control"),
        o6.LocalizedText("structured-view"),
        o6.LocalizedText("access-door"),
        o6.LocalizedText("unassigned"),
        o6.LocalizedText("access-credential"),
        o6.LocalizedText("access-point"),
        o6.LocalizedText("access-rights"),
        o6.LocalizedText("access-user"),
        o6.LocalizedText("access-zone"),
        o6.LocalizedText("credentional-data-input"),
        o6.LocalizedText("network-security"),
        o6.LocalizedText("bitstring-value"),
        o6.LocalizedText("characterstring-value"),
        o6.LocalizedText("date-pattern-value"),
        o6.LocalizedText("date-value"),
        o6.LocalizedText("datetime-pattern-value"),
        o6.LocalizedText("datetime-value"),
        o6.LocalizedText("integer-value"),
        o6.LocalizedText("large-analog-value"),
        o6.LocalizedText("octetstring-value"),
        o6.LocalizedText("positive-integer-value"),
        o6.LocalizedText("time-pattern-value"),
        o6.LocalizedText("time-value"),
        o6.LocalizedText("notification-forwarder"),
        o6.LocalizedText("alert-enrollment"),
        o6.LocalizedText("channel"),
        o6.LocalizedText("lighting-output"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=106277",
    browseName="EnumValues",
    parent="ns=bacnet;i=103054",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[16],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("change-of-bitstring")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("change-of-state")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("change-of-value")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("command-failure")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("out-of-range")),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("change-of-life-safety")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("floating-limit")),
        ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("extended")),
        ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("buffer-ready")),
        ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("unsigned-range")),
        ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("access-event")),
        ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("double-out-of-range")),
        ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("signed-out-of-range")),
        ns0.datatypes.EnumValueType(value=16, displayName=o6.LocalizedText("unsigned-out-of-range")),
        ns0.datatypes.EnumValueType(value=17, displayName=o6.LocalizedText("change-of-characterstring")),
        ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("change-of-status-flags")),
    ],
)
bacnet_objtypes.BACnetEventReportingType(
    nodeId="ns=bacnet;i=105073",
    browseName="ns=bacnet;EventReporting",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6358",
                browseName="ns=bacnet;Event_State",
                dataType=bacnet_datypes.BACnetEventState,
                value=bacnet_datypes.BACnetEventState.NORMAL,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106054", browseName="ns=bacnet;Acked_Transitions", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106192", browseName="ns=bacnet;Event_Enable", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106278",
                browseName="ns=bacnet;Event_Time_Stamps",
                dataType=bacnet_datypes.BACnetTimeStamp,
                valueRank=1,
                arrayDimensions=[3],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106279", browseName="ns=bacnet;Notification_Class", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106280", browseName="ns=bacnet;Notify_Type", dataType=bacnet_datypes.BACnetNotifyType, accessLevel=3, userAccessLevel=1)
        ),
    ],
)
o6.reference(bacnet_objtypes.BACnetEventEnrollmentType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=105073"])
bacnet_objtypes.BACnetEventReportingType(
    nodeId="ns=bacnet;i=105093",
    browseName="ns=bacnet;EventReporting",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=6361",
                browseName="ns=bacnet;Event_State",
                dataType=bacnet_datypes.BACnetEventState,
                value=bacnet_datypes.BACnetEventState.NORMAL,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106296", browseName="ns=bacnet;Acked_Transitions", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106297", browseName="ns=bacnet;Event_Enable", dataType=bacnet_datypes.BACnetEventTransitionBits, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106299",
                browseName="ns=bacnet;Event_Time_Stamps",
                dataType=bacnet_datypes.BACnetTimeStamp,
                valueRank=1,
                arrayDimensions=[3],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106300", browseName="ns=bacnet;Notification_Class", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=106301", browseName="ns=bacnet;Notify_Type", dataType=bacnet_datypes.BACnetNotifyType, accessLevel=3, userAccessLevel=1)
        ),
    ],
)
o6.reference(bacnet_objtypes.BACnetScheduleType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=105093"])
bacnet_objtypes.BACnetFaultAlgorithmType(
    nodeId="ns=bacnet;i=105096",
    browseName="ns=bacnet;FaultAlgorithm",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106329", browseName="ns=bacnet;Object_Identifier", dataType=bacnet_datypes.BACnetObjectIdentifier, accessLevel=3, userAccessLevel=1
            )
        )
    ],
    _allow_abstract=True,
)
o6.reference(bacnet_objtypes.BACnetFaultEvaluationType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=105096"])
bacnet_objtypes.BACnetBackupRestoreType(
    nodeId="ns=bacnet;i=105086",
    browseName="ns=bacnet;BackupRestore",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6253", browseName="ns=bacnet;Backup_Failure_Timeout", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6259", browseName="ns=bacnet;Backup_Preparation_Time", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6260", browseName="ns=bacnet;Restore_Preparation_Time", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=bacnet;i=6261", browseName="ns=bacnet;Restore_Completion_Time", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106082", browseName="ns=bacnet;Backup_And_Restore_State", dataType=bacnet_datypes.BACnetBackupState, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106123",
                browseName="ns=bacnet;Configuration_Files",
                dataType=bacnet_datypes.BACnetDeviceObjectPropertyReference,
                valueRank=1,
                arrayDimensions=[1],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106124",
                browseName="ns=bacnet;Last_Restore_Time",
                dataType=bacnet_datypes.BACnetTimeStamp,
                value=bacnet_datypes.BACnetTimeStamp(),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=bacnet;i=107008", browseName="ns=bacnet;BACnetBackup")),
        o6.hasComponent(o6.call(nodeId="ns=bacnet;i=107009", browseName="ns=bacnet;BACnetRestore")),
    ],
)
o6.reference(bacnet_objtypes.BACnetDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=105086"])


ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6110",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=107010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RestartNotificationRecipients", dataType=o6.NodeId("ns=bacnet;i=3054"), valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6139",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=107010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FirstFailedElementNumber", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=bacnet;i=107010",
    browseName="ns=bacnet;AddRestartRecipients",
    inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6110"]),
    outputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6139"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6142",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=107011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FirstFailedElementNumber", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=bacnet;i=6148",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=bacnet;i=107011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RestartNotificationRecipients", dataType=o6.NodeId("ns=bacnet;i=3054"), valueRank=1, arrayDimensions=[0])],
)
o6.call(
    nodeId="ns=bacnet;i=107011",
    browseName="ns=bacnet;RemoveRestartRecipients",
    inputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6148"]),
    outputArgs=o6.hasProperty(o6.ns["ns=bacnet;i=6142"]),
)

bacnet_objtypes.BACnetDeviceRestartType(
    nodeId="ns=bacnet;i=105088",
    browseName="ns=bacnet;DeviceRestart",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106128", browseName="ns=bacnet;Last_Restart_Reason", dataType=bacnet_datypes.BACnetRestartReason, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106129",
                browseName="ns=bacnet;Restart_Notification_Recipients",
                dataType=bacnet_datypes.BACnetRecipient,
                valueRank=1,
                arrayDimensions=[0],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=bacnet;i=106130",
                browseName="ns=bacnet;Time_Of_Device_Restart",
                dataType=bacnet_datypes.BACnetTimeStamp,
                value=bacnet_datypes.BACnetTimeStamp(),
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=bacnet;i=107010"]),
        o6.hasComponent(o6.ns["ns=bacnet;i=107011"]),
    ],
)
o6.reference(bacnet_objtypes.BACnetDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=bacnet;i=105088"])


del Any, TYPE_CHECKING, uuid, o6, ns0, bacnet_datypes, bacnet_vartypes, bacnet_objtypes
