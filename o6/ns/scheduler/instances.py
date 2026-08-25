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

"""Generated OPC UA scheduler namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import datatypes as scheduler_datypes
from . import objtypes as scheduler_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

httpColonSlashSlashOpcfoundationDotOrgSlashUASlashSchedulerSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=scheduler;i=1",
    browseName="ns=scheduler;http://opcfoundation.org/UA/Scheduler/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scheduler;i=2", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Scheduler/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scheduler;i=3", browseName="NamespaceVersion", dataType=o6.String, value="1.05.02")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=scheduler;i=4", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2022-11-01T00:00:00Z"))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scheduler;i=5", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scheduler;i=6", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scheduler;i=7", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["1:2147483647"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scheduler;i=8", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=scheduler;i=33", browseName="DefaultRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scheduler;i=34", browseName="DefaultUserRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scheduler;i=35", browseName="DefaultAccessRestrictions", dataType=ns0.datatypes.AccessRestrictionType)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.PropertyType(
    nodeId="ns=scheduler;i=79",
    browseName="EnumStrings",
    parent="ns=scheduler;i=78",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        o6.LocalizedText("Unspecified"),
        o6.LocalizedText("Monday"),
        o6.LocalizedText("Tuesday"),
        o6.LocalizedText("Wednesday"),
        o6.LocalizedText("Thursday"),
        o6.LocalizedText("Friday"),
        o6.LocalizedText("Saturday"),
        o6.LocalizedText("Sunday"),
    ],
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=87", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=88", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=89", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=90", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=91", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=92", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=93", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=94", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=95", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=96", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=97", browseName="Default Binary")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scheduler;i=102", browseName="ns=scheduler;SpecialEventType", dataType=o6.String, value="SpecialEventType")
o6.reference(o6.ns["ns=scheduler;i=87"], "i=39", o6.ns["ns=scheduler;i=102"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scheduler;i=105", browseName="ns=scheduler;SpecialEventPeriodType", dataType=o6.String, value="SpecialEventPeriodType")
o6.reference(o6.ns["ns=scheduler;i=88"], "i=39", o6.ns["ns=scheduler;i=105"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scheduler;i=108", browseName="ns=scheduler;CalendarEntryType", dataType=o6.String, value="CalendarEntryType")
o6.reference(o6.ns["ns=scheduler;i=89"], "i=39", o6.ns["ns=scheduler;i=108"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scheduler;i=111", browseName="ns=scheduler;DateType", dataType=o6.String, value="DateType")
o6.reference(o6.ns["ns=scheduler;i=90"], "i=39", o6.ns["ns=scheduler;i=111"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scheduler;i=114", browseName="ns=scheduler;DateRangeType", dataType=o6.String, value="DateRangeType")
o6.reference(o6.ns["ns=scheduler;i=91"], "i=39", o6.ns["ns=scheduler;i=114"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scheduler;i=117", browseName="ns=scheduler;TimeActionsType", dataType=o6.String, value="TimeActionsType")
o6.reference(o6.ns["ns=scheduler;i=92"], "i=39", o6.ns["ns=scheduler;i=117"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scheduler;i=120", browseName="ns=scheduler;BaseActionType", dataType=o6.String, value="BaseActionType")
o6.reference(o6.ns["ns=scheduler;i=93"], "i=39", o6.ns["ns=scheduler;i=120"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scheduler;i=123", browseName="ns=scheduler;WriteLocalVariableActionType", dataType=o6.String, value="WriteLocalVariableActionType")
o6.reference(o6.ns["ns=scheduler;i=94"], "i=39", o6.ns["ns=scheduler;i=123"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scheduler;i=126", browseName="ns=scheduler;CallLocalMethodActionType", dataType=o6.String, value="CallLocalMethodActionType")
o6.reference(o6.ns["ns=scheduler;i=95"], "i=39", o6.ns["ns=scheduler;i=126"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scheduler;i=129", browseName="ns=scheduler;TimeType", dataType=o6.String, value="TimeType")
o6.reference(o6.ns["ns=scheduler;i=96"], "i=39", o6.ns["ns=scheduler;i=129"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scheduler;i=132", browseName="ns=scheduler;DailyScheduleType", dataType=o6.String, value="DailyScheduleType")
o6.reference(o6.ns["ns=scheduler;i=97"], "i=39", o6.ns["ns=scheduler;i=132"])
opcDotUaDotScheduler = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=scheduler;i=98",
    browseName="ns=scheduler;Opc.Ua.Scheduler",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scheduler;i=100", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Scheduler/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scheduler;i=101", browseName="Deprecated", dataType=o6.Boolean, value=True)),
        o6.hasComponent(o6.ns["ns=scheduler;i=102"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=105"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=108"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=111"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=114"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=117"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=120"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=123"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=126"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=129"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=132"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary\r\n  xmlns:opc="http://opcfoundation.org/BinarySchema/"\r\n  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\r\n  xmlns:ua="http://opcfoundation.org/UA/"\r\n  xmlns:tns="http://opcfoundation.org/UA/Scheduler/"\r\n  DefaultByteOrder="LittleEndian"\r\n  TargetNamespace="http://opcfoundation.org/UA/Scheduler/"\r\n>\r\n  <opc:Import Namespace="http://opcfoundation.org/UA/" Location="Opc.Ua.BinarySchema.bsd"/>\r\n\r\n  <opc:StructuredType Name="SpecialEventType" BaseType="ua:ExtensionObject">\r\n    <opc:Documentation>This structure contains a period, a list of time values, and a priority. It is a means to identify moments in time over one or more days.</opc:Documentation>\r\n    <opc:Field Name="Period" TypeName="tns:SpecialEventPeriodType" />\r\n    <opc:Field Name="NoOfListOfTimeActions" TypeName="opc:Int32" />\r\n    <opc:Field Name="ListOfTimeActions" TypeName="tns:TimeActionsType" LengthField="NoOfListOfTimeActions" />\r\n    <opc:Field Name="EventPriority" TypeName="opc:Byte" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="SpecialEventPeriodType" BaseType="ua:Union">\r\n    <opc:Documentation>This union contains a calendar entry or a reference to a calendar object</opc:Documentation>\r\n    <opc:Field Name="CalendarEntry" TypeName="tns:CalendarEntryType" />\r\n    <opc:Field Name="CalendarReference" TypeName="ua:NodeId" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="CalendarEntryType" BaseType="ua:Union">\r\n    <opc:Documentation>This union that defines various calendar date values</opc:Documentation>\r\n    <opc:Field Name="Date" TypeName="tns:DateType" />\r\n    <opc:Field Name="DateRange" TypeName="tns:DateRangeType" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="DateType" BaseType="ua:ExtensionObject">\r\n    <opc:Documentation>This structure defines a calendar date. It allows to define a concrete date, e.g. 2022-02-12. By using wildcards, it also allows to define repeating dates, like every Wednesday, every odd day of a month, every 24th of December, every last day of a month in 2023, etc.</opc:Documentation>\r\n    <opc:Field Name="Year" TypeName="opc:UInt16" />\r\n    <opc:Field Name="Month" TypeName="tns:Month" />\r\n    <opc:Field Name="DayOfMonth" TypeName="tns:DayOfMonth" />\r\n    <opc:Field Name="DayOfWeek" TypeName="tns:DayOfWeek" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:EnumeratedType Name="Month" LengthInBits="32">\r\n    <opc:Documentation>This enumeration indicates either a specific Gregorian calendar month, or a relative relationship ("odd", "even", and "unspecified").</opc:Documentation>\r\n    <opc:EnumeratedValue Name="Unspecified" Value="0" />\r\n    <opc:EnumeratedValue Name="January" Value="1" />\r\n    <opc:EnumeratedValue Name="February" Value="2" />\r\n    <opc:EnumeratedValue Name="March" Value="3" />\r\n    <opc:EnumeratedValue Name="April" Value="4" />\r\n    <opc:EnumeratedValue Name="May" Value="5" />\r\n    <opc:EnumeratedValue Name="June" Value="6" />\r\n    <opc:EnumeratedValue Name="July" Value="7" />\r\n    <opc:EnumeratedValue Name="August" Value="8" />\r\n    <opc:EnumeratedValue Name="September" Value="9" />\r\n    <opc:EnumeratedValue Name="October" Value="10" />\r\n    <opc:EnumeratedValue Name="November" Value="11" />\r\n    <opc:EnumeratedValue Name="December" Value="12" />\r\n    <opc:EnumeratedValue Name="Odd" Value="13" />\r\n    <opc:EnumeratedValue Name="Even" Value="14" />\r\n  </opc:EnumeratedType>\r\n\r\n  <opc:EnumeratedType Name="DayOfMonth" LengthInBits="32">\r\n    <opc:Documentation>This enumeration indicates specific days of the month by specific date ("1", "22", and so on) or by relative position ("last day of month", "even day of month", and so on).</opc:Documentation>\r\n    <opc:EnumeratedValue Name="Unspecified" Value="0" />\r\n    <opc:EnumeratedValue Name="Day1" Value="1" />\r\n    <opc:EnumeratedValue Name="Day2" Value="2" />\r\n    <opc:EnumeratedValue Name="Day3" Value="3" />\r\n    <opc:EnumeratedValue Name="Day4" Value="4" />\r\n    <opc:EnumeratedValue Name="Day5" Value="5" />\r\n    <opc:EnumeratedValue Name="Day6" Value="6" />\r\n    <opc:EnumeratedValue Name="Day7" Value="7" />\r\n    <opc:EnumeratedValue Name="Day8" Value="8" />\r\n    <opc:EnumeratedValue Name="Day9" Value="9" />\r\n    <opc:EnumeratedValue Name="Day10" Value="10" />\r\n    <opc:EnumeratedValue Name="Day11" Value="11" />\r\n    <opc:EnumeratedValue Name="Day12" Value="12" />\r\n    <opc:EnumeratedValue Name="Day13" Value="13" />\r\n    <opc:EnumeratedValue Name="Day14" Value="14" />\r\n    <opc:EnumeratedValue Name="Day15" Value="15" />\r\n    <opc:EnumeratedValue Name="Day16" Value="16" />\r\n    <opc:EnumeratedValue Name="Day17" Value="17" />\r\n    <opc:EnumeratedValue Name="Day18" Value="18" />\r\n    <opc:EnumeratedValue Name="Day19" Value="19" />\r\n    <opc:EnumeratedValue Name="Day20" Value="20" />\r\n    <opc:EnumeratedValue Name="Day21" Value="21" />\r\n    <opc:EnumeratedValue Name="Day22" Value="22" />\r\n    <opc:EnumeratedValue Name="Day23" Value="23" />\r\n    <opc:EnumeratedValue Name="Day24" Value="24" />\r\n    <opc:EnumeratedValue Name="Day25" Value="25" />\r\n    <opc:EnumeratedValue Name="Day26" Value="26" />\r\n    <opc:EnumeratedValue Name="Day27" Value="27" />\r\n    <opc:EnumeratedValue Name="Day28" Value="28" />\r\n    <opc:EnumeratedValue Name="Day29" Value="29" />\r\n    <opc:EnumeratedValue Name="Day30" Value="30" />\r\n    <opc:EnumeratedValue Name="Day31" Value="31" />\r\n    <opc:EnumeratedValue Name="LastDayOfMonth" Value="32" />\r\n    <opc:EnumeratedValue Name="OddDayOfMonth" Value="33" />\r\n    <opc:EnumeratedValue Name="EvenDayOfMonth" Value="34" />\r\n  </opc:EnumeratedType>\r\n\r\n  <opc:EnumeratedType Name="DayOfWeek" LengthInBits="32">\r\n    <opc:Documentation>This enumeration indicates each of the seven days of the week, or "unspecified".</opc:Documentation>\r\n    <opc:EnumeratedValue Name="Unspecified" Value="0" />\r\n    <opc:EnumeratedValue Name="Monday" Value="1" />\r\n    <opc:EnumeratedValue Name="Tuesday" Value="2" />\r\n    <opc:EnumeratedValue Name="Wednesday" Value="3" />\r\n    <opc:EnumeratedValue Name="Thursday" Value="4" />\r\n    <opc:EnumeratedValue Name="Friday" Value="5" />\r\n    <opc:EnumeratedValue Name="Saturday" Value="6" />\r\n    <opc:EnumeratedValue Name="Sunday" Value="7" />\r\n  </opc:EnumeratedType>\r\n\r\n  <opc:StructuredType Name="DateRangeType" BaseType="ua:ExtensionObject">\r\n    <opc:Documentation>This structure defines a time span, with absolute start and end dates. The StartDate and EndDate are limited to specific values, i.e., wild cards like odd months are not allowed. The Year field shall not be 0; the Month field shall be a value between 1 to 12; the DayOfMonth field shall be between 1 to 31 and the DayOfMonth field shall be "unspecified".</opc:Documentation>\r\n    <opc:Field Name="StartDate" TypeName="tns:DateType" />\r\n    <opc:Field Name="EndDate" TypeName="tns:DateType" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="TimeActionsType" BaseType="ua:ExtensionObject">\r\n    <opc:Documentation>This structure contains a time and an array of actions. It is used to define actions to be executed at a specific point in time.</opc:Documentation>\r\n    <opc:Field Name="Time" TypeName="tns:TimeType" />\r\n    <opc:Field Name="NoOfActions" TypeName="opc:Int32" />\r\n    <opc:Field Name="Actions" TypeName="ua:ExtensionObject" LengthField="NoOfActions" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="BaseActionType" BaseType="ua:ExtensionObject">\r\n    <opc:Documentation>This abstract structure defines the base of an action. The base only contains information, if the last execution of the action was successful.</opc:Documentation>\r\n    <opc:Field Name="LastActionResult" TypeName="ua:StatusCode" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="WriteLocalVariableActionType" BaseType="tns:BaseActionType">\r\n    <opc:Documentation>This structure defines an action to write the value of a Variable managed in the same Server where the action is used.</opc:Documentation>\r\n    <opc:Field Name="LastActionResult" TypeName="ua:StatusCode" SourceType="tns:BaseActionType" />\r\n    <opc:Field Name="Variable" TypeName="ua:NodeId" />\r\n    <opc:Field Name="Value" TypeName="ua:Variant" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="CallLocalMethodActionType" BaseType="tns:BaseActionType">\r\n    <opc:Documentation>This structure defines an action to call a Method of an Object managed in the same Server where the action is used.</opc:Documentation>\r\n    <opc:Field Name="LastActionResult" TypeName="ua:StatusCode" SourceType="tns:BaseActionType" />\r\n    <opc:Field Name="ObjectId" TypeName="ua:NodeId" />\r\n    <opc:Field Name="MethodId" TypeName="ua:NodeId" />\r\n    <opc:Field Name="NoOfInputValues" TypeName="opc:Int32" />\r\n    <opc:Field Name="InputValues" TypeName="ua:Variant" LengthField="NoOfInputValues" />\r\n    <opc:Field Name="NoOfLastOutputValues" TypeName="opc:Int32" />\r\n    <opc:Field Name="LastOutputValues" TypeName="ua:Variant" LengthField="NoOfLastOutputValues" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="TimeType" BaseType="ua:ExtensionObject">\r\n    <opc:Documentation>This structure that represents a point in time during a day</opc:Documentation>\r\n    <opc:Field Name="Hour" TypeName="opc:Byte" />\r\n    <opc:Field Name="Minute" TypeName="opc:Byte" />\r\n    <opc:Field Name="Second" TypeName="opc:Byte" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="DailyScheduleType" BaseType="ua:ExtensionObject">\r\n    <opc:Documentation>This structure defines a sequence of TimeActionsType structures. Each element in the sequence defines a time/actions pair that describes the actions to be executed at a given point in the day.</opc:Documentation>\r\n    <opc:Field Name="NoOfDaySchedule" TypeName="opc:Int32" />\r\n    <opc:Field Name="DaySchedule" TypeName="tns:TimeActionsType" LengthField="NoOfDaySchedule" />\r\n  </opc:StructuredType>\r\n\r\n</opc:TypeDictionary>',
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=135", browseName="Default XML")
o6.hasEncoding(scheduler_datypes.SpecialEventType, o6.ns["ns=scheduler;i=135"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=136", browseName="Default XML")
o6.hasEncoding(scheduler_datypes.SpecialEventPeriodType, o6.ns["ns=scheduler;i=136"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=137", browseName="Default XML")
o6.hasEncoding(scheduler_datypes.CalendarEntryType, o6.ns["ns=scheduler;i=137"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=138", browseName="Default XML")
o6.hasEncoding(scheduler_datypes.DateType, o6.ns["ns=scheduler;i=138"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=139", browseName="Default XML")
o6.hasEncoding(scheduler_datypes.DateRangeType, o6.ns["ns=scheduler;i=139"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=140", browseName="Default XML")
o6.hasEncoding(scheduler_datypes.TimeActionsType, o6.ns["ns=scheduler;i=140"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=141", browseName="Default XML")
o6.hasEncoding(scheduler_datypes.BaseActionType, o6.ns["ns=scheduler;i=141"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=142", browseName="Default XML")
o6.hasEncoding(scheduler_datypes.WriteLocalVariableActionType, o6.ns["ns=scheduler;i=142"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=143", browseName="Default XML")
o6.hasEncoding(scheduler_datypes.CallLocalMethodActionType, o6.ns["ns=scheduler;i=143"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=144", browseName="Default XML")
o6.hasEncoding(scheduler_datypes.TimeType, o6.ns["ns=scheduler;i=144"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=145", browseName="Default XML")
o6.hasEncoding(scheduler_datypes.DailyScheduleType, o6.ns["ns=scheduler;i=145"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scheduler;i=150", browseName="ns=scheduler;SpecialEventType", dataType=o6.String, value="//xs:element[@name='SpecialEventType']")
o6.reference(o6.ns["ns=scheduler;i=135"], "i=39", o6.ns["ns=scheduler;i=150"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=scheduler;i=153", browseName="ns=scheduler;SpecialEventPeriodType", dataType=o6.String, value="//xs:element[@name='SpecialEventPeriodType']"
)
o6.reference(o6.ns["ns=scheduler;i=136"], "i=39", o6.ns["ns=scheduler;i=153"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scheduler;i=156", browseName="ns=scheduler;CalendarEntryType", dataType=o6.String, value="//xs:element[@name='CalendarEntryType']")
o6.reference(o6.ns["ns=scheduler;i=137"], "i=39", o6.ns["ns=scheduler;i=156"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scheduler;i=159", browseName="ns=scheduler;DateType", dataType=o6.String, value="//xs:element[@name='DateType']")
o6.reference(o6.ns["ns=scheduler;i=138"], "i=39", o6.ns["ns=scheduler;i=159"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scheduler;i=162", browseName="ns=scheduler;DateRangeType", dataType=o6.String, value="//xs:element[@name='DateRangeType']")
o6.reference(o6.ns["ns=scheduler;i=139"], "i=39", o6.ns["ns=scheduler;i=162"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scheduler;i=165", browseName="ns=scheduler;TimeActionsType", dataType=o6.String, value="//xs:element[@name='TimeActionsType']")
o6.reference(o6.ns["ns=scheduler;i=140"], "i=39", o6.ns["ns=scheduler;i=165"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scheduler;i=168", browseName="ns=scheduler;BaseActionType", dataType=o6.String, value="//xs:element[@name='BaseActionType']")
o6.reference(o6.ns["ns=scheduler;i=141"], "i=39", o6.ns["ns=scheduler;i=168"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=scheduler;i=171", browseName="ns=scheduler;WriteLocalVariableActionType", dataType=o6.String, value="//xs:element[@name='WriteLocalVariableActionType']"
)
o6.reference(o6.ns["ns=scheduler;i=142"], "i=39", o6.ns["ns=scheduler;i=171"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=scheduler;i=174", browseName="ns=scheduler;CallLocalMethodActionType", dataType=o6.String, value="//xs:element[@name='CallLocalMethodActionType']"
)
o6.reference(o6.ns["ns=scheduler;i=143"], "i=39", o6.ns["ns=scheduler;i=174"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scheduler;i=177", browseName="ns=scheduler;TimeType", dataType=o6.String, value="//xs:element[@name='TimeType']")
o6.reference(o6.ns["ns=scheduler;i=144"], "i=39", o6.ns["ns=scheduler;i=177"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scheduler;i=180", browseName="ns=scheduler;DailyScheduleType", dataType=o6.String, value="//xs:element[@name='DailyScheduleType']")
o6.reference(o6.ns["ns=scheduler;i=145"], "i=39", o6.ns["ns=scheduler;i=180"])
opcDotUaDotScheduler_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=scheduler;i=146",
    browseName="ns=scheduler;Opc.Ua.Scheduler",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=scheduler;i=148", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Scheduler/Types.xsd")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scheduler;i=149", browseName="Deprecated", dataType=o6.Boolean, value=True)),
        o6.hasComponent(o6.ns["ns=scheduler;i=150"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=153"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=156"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=159"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=162"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=165"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=168"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=171"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=174"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=177"]),
        o6.hasComponent(o6.ns["ns=scheduler;i=180"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema\r\n  xmlns:xs="http://www.w3.org/2001/XMLSchema"\r\n  xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd"\r\n  xmlns:tns="http://opcfoundation.org/UA/Scheduler/Types.xsd"\r\n  targetNamespace="http://opcfoundation.org/UA/Scheduler/Types.xsd"\r\n  elementFormDefault="qualified"\r\n>\r\n  <xs:annotation>\r\n    <xs:appinfo>\r\n      <tns:Model ModelUri="http://opcfoundation.org/UA/Scheduler/" Version="1.05.02" PublicationDate="2022-11-01T00:00:00Z" />\r\n    </xs:appinfo>\r\n  </xs:annotation>\r\n  \r\n  <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd" />\r\n\r\n  <xs:complexType name="SpecialEventType">\r\n    <xs:annotation>\r\n      <xs:documentation>This structure contains a period, a list of time values, and a priority. It is a means to identify moments in time over one or more days.</xs:documentation>\r\n    </xs:annotation>\r\n    <xs:sequence>\r\n      <xs:element name="Period" type="tns:SpecialEventPeriodType" minOccurs="0" nillable="true" />\r\n      <xs:element name="ListOfTimeActions" type="tns:ListOfTimeActionsType" minOccurs="0" nillable="true" />\r\n      <xs:element name="EventPriority" type="xs:unsignedByte" minOccurs="0" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="SpecialEventType" type="tns:SpecialEventType" />\r\n\r\n  <xs:complexType name="ListOfSpecialEventType">\r\n    <xs:sequence>\r\n      <xs:element name="SpecialEventType" type="tns:SpecialEventType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfSpecialEventType" type="tns:ListOfSpecialEventType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="SpecialEventPeriodType">\r\n    <xs:annotation>\r\n      <xs:documentation>This union contains a calendar entry or a reference to a calendar object</xs:documentation>\r\n    </xs:annotation>\r\n    <xs:complexContent mixed="false">\r\n      <xs:extension base="ua:Union">\r\n        <xs:sequence>\r\n          <xs:element name="CalendarEntry" type="tns:CalendarEntryType" minOccurs="0" nillable="true" />\r\n          <xs:element name="CalendarReference" type="ua:NodeId" minOccurs="0" nillable="true" />\r\n        </xs:sequence>\r\n      </xs:extension>\r\n    </xs:complexContent>\r\n  </xs:complexType>\r\n  <xs:element name="SpecialEventPeriodType" type="tns:SpecialEventPeriodType" />\r\n\r\n  <xs:complexType name="ListOfSpecialEventPeriodType">\r\n    <xs:sequence>\r\n      <xs:element name="SpecialEventPeriodType" type="tns:SpecialEventPeriodType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfSpecialEventPeriodType" type="tns:ListOfSpecialEventPeriodType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="CalendarEntryType">\r\n    <xs:annotation>\r\n      <xs:documentation>This union that defines various calendar date values</xs:documentation>\r\n    </xs:annotation>\r\n    <xs:complexContent mixed="false">\r\n      <xs:extension base="ua:Union">\r\n        <xs:sequence>\r\n          <xs:element name="Date" type="tns:DateType" minOccurs="0" nillable="true" />\r\n          <xs:element name="DateRange" type="tns:DateRangeType" minOccurs="0" nillable="true" />\r\n        </xs:sequence>\r\n      </xs:extension>\r\n    </xs:complexContent>\r\n  </xs:complexType>\r\n  <xs:element name="CalendarEntryType" type="tns:CalendarEntryType" />\r\n\r\n  <xs:complexType name="ListOfCalendarEntryType">\r\n    <xs:sequence>\r\n      <xs:element name="CalendarEntryType" type="tns:CalendarEntryType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfCalendarEntryType" type="tns:ListOfCalendarEntryType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="DateType">\r\n    <xs:annotation>\r\n      <xs:documentation>This structure defines a calendar date. It allows to define a concrete date, e.g. 2022-02-12. By using wildcards, it also allows to define repeating dates, like every Wednesday, every odd day of a month, every 24th of December, every last day of a month in 2023, etc.</xs:documentation>\r\n    </xs:annotation>\r\n    <xs:sequence>\r\n      <xs:element name="Year" type="xs:unsignedShort" minOccurs="0" />\r\n      <xs:element name="Month" type="tns:Month" minOccurs="0" />\r\n      <xs:element name="DayOfMonth" type="tns:DayOfMonth" minOccurs="0" />\r\n      <xs:element name="DayOfWeek" type="tns:DayOfWeek" minOccurs="0" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="DateType" type="tns:DateType" />\r\n\r\n  <xs:complexType name="ListOfDateType">\r\n    <xs:sequence>\r\n      <xs:element name="DateType" type="tns:DateType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfDateType" type="tns:ListOfDateType" nillable="true"></xs:element>\r\n\r\n  <xs:simpleType  name="Month">\r\n    <xs:annotation>\r\n      <xs:documentation>This enumeration indicates either a specific Gregorian calendar month, or a relative relationship ("odd", "even", and "unspecified").</xs:documentation>\r\n    </xs:annotation>\r\n    <xs:restriction base="xs:string">\r\n      <xs:enumeration value="Unspecified_0" />\r\n      <xs:enumeration value="January_1" />\r\n      <xs:enumeration value="February_2" />\r\n      <xs:enumeration value="March_3" />\r\n      <xs:enumeration value="April_4" />\r\n      <xs:enumeration value="May_5" />\r\n      <xs:enumeration value="June_6" />\r\n      <xs:enumeration value="July_7" />\r\n      <xs:enumeration value="August_8" />\r\n      <xs:enumeration value="September_9" />\r\n      <xs:enumeration value="October_10" />\r\n      <xs:enumeration value="November_11" />\r\n      <xs:enumeration value="December_12" />\r\n      <xs:enumeration value="Odd_13" />\r\n      <xs:enumeration value="Even_14" />\r\n    </xs:restriction>\r\n  </xs:simpleType>\r\n  <xs:element name="Month" type="tns:Month" />\r\n\r\n  <xs:complexType name="ListOfMonth">\r\n    <xs:sequence>\r\n      <xs:element name="Month" type="tns:Month" minOccurs="0" maxOccurs="unbounded" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfMonth" type="tns:ListOfMonth" nillable="true"></xs:element>\r\n\r\n  <xs:simpleType  name="DayOfMonth">\r\n    <xs:annotation>\r\n      <xs:documentation>This enumeration indicates specific days of the month by specific date ("1", "22", and so on) or by relative position ("last day of month", "even day of month", and so on).</xs:documentation>\r\n    </xs:annotation>\r\n    <xs:restriction base="xs:string">\r\n      <xs:enumeration value="Unspecified_0" />\r\n      <xs:enumeration value="Day1_1" />\r\n      <xs:enumeration value="Day2_2" />\r\n      <xs:enumeration value="Day3_3" />\r\n      <xs:enumeration value="Day4_4" />\r\n      <xs:enumeration value="Day5_5" />\r\n      <xs:enumeration value="Day6_6" />\r\n      <xs:enumeration value="Day7_7" />\r\n      <xs:enumeration value="Day8_8" />\r\n      <xs:enumeration value="Day9_9" />\r\n      <xs:enumeration value="Day10_10" />\r\n      <xs:enumeration value="Day11_11" />\r\n      <xs:enumeration value="Day12_12" />\r\n      <xs:enumeration value="Day13_13" />\r\n      <xs:enumeration value="Day14_14" />\r\n      <xs:enumeration value="Day15_15" />\r\n      <xs:enumeration value="Day16_16" />\r\n      <xs:enumeration value="Day17_17" />\r\n      <xs:enumeration value="Day18_18" />\r\n      <xs:enumeration value="Day19_19" />\r\n      <xs:enumeration value="Day20_20" />\r\n      <xs:enumeration value="Day21_21" />\r\n      <xs:enumeration value="Day22_22" />\r\n      <xs:enumeration value="Day23_23" />\r\n      <xs:enumeration value="Day24_24" />\r\n      <xs:enumeration value="Day25_25" />\r\n      <xs:enumeration value="Day26_26" />\r\n      <xs:enumeration value="Day27_27" />\r\n      <xs:enumeration value="Day28_28" />\r\n      <xs:enumeration value="Day29_29" />\r\n      <xs:enumeration value="Day30_30" />\r\n      <xs:enumeration value="Day31_31" />\r\n      <xs:enumeration value="LastDayOfMonth_32" />\r\n      <xs:enumeration value="OddDayOfMonth_33" />\r\n      <xs:enumeration value="EvenDayOfMonth_34" />\r\n    </xs:restriction>\r\n  </xs:simpleType>\r\n  <xs:element name="DayOfMonth" type="tns:DayOfMonth" />\r\n\r\n  <xs:complexType name="ListOfDayOfMonth">\r\n    <xs:sequence>\r\n      <xs:element name="DayOfMonth" type="tns:DayOfMonth" minOccurs="0" maxOccurs="unbounded" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfDayOfMonth" type="tns:ListOfDayOfMonth" nillable="true"></xs:element>\r\n\r\n  <xs:simpleType  name="DayOfWeek">\r\n    <xs:annotation>\r\n      <xs:documentation>This enumeration indicates each of the seven days of the week, or "unspecified".</xs:documentation>\r\n    </xs:annotation>\r\n    <xs:restriction base="xs:string">\r\n      <xs:enumeration value="Unspecified_0" />\r\n      <xs:enumeration value="Monday_1" />\r\n      <xs:enumeration value="Tuesday_2" />\r\n      <xs:enumeration value="Wednesday_3" />\r\n      <xs:enumeration value="Thursday_4" />\r\n      <xs:enumeration value="Friday_5" />\r\n      <xs:enumeration value="Saturday_6" />\r\n      <xs:enumeration value="Sunday_7" />\r\n    </xs:restriction>\r\n  </xs:simpleType>\r\n  <xs:element name="DayOfWeek" type="tns:DayOfWeek" />\r\n\r\n  <xs:complexType name="ListOfDayOfWeek">\r\n    <xs:sequence>\r\n      <xs:element name="DayOfWeek" type="tns:DayOfWeek" minOccurs="0" maxOccurs="unbounded" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfDayOfWeek" type="tns:ListOfDayOfWeek" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="DateRangeType">\r\n    <xs:annotation>\r\n      <xs:documentation>This structure defines a time span, with absolute start and end dates. The StartDate and EndDate are limited to specific values, i.e., wild cards like odd months are not allowed. The Year field shall not be 0; the Month field shall be a value between 1 to 12; the DayOfMonth field shall be between 1 to 31 and the DayOfMonth field shall be "unspecified".</xs:documentation>\r\n    </xs:annotation>\r\n    <xs:sequence>\r\n      <xs:element name="StartDate" type="tns:DateType" minOccurs="0" nillable="true" />\r\n      <xs:element name="EndDate" type="tns:DateType" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="DateRangeType" type="tns:DateRangeType" />\r\n\r\n  <xs:complexType name="ListOfDateRangeType">\r\n    <xs:sequence>\r\n      <xs:element name="DateRangeType" type="tns:DateRangeType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfDateRangeType" type="tns:ListOfDateRangeType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="TimeActionsType">\r\n    <xs:annotation>\r\n      <xs:documentation>This structure contains a time and an array of actions. It is used to define actions to be executed at a specific point in time.</xs:documentation>\r\n    </xs:annotation>\r\n    <xs:sequence>\r\n      <xs:element name="Time" type="tns:TimeType" minOccurs="0" nillable="true" />\r\n      <xs:element name="Actions" type="ua:ListOfExtensionObject" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="TimeActionsType" type="tns:TimeActionsType" />\r\n\r\n  <xs:complexType name="ListOfTimeActionsType">\r\n    <xs:sequence>\r\n      <xs:element name="TimeActionsType" type="tns:TimeActionsType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfTimeActionsType" type="tns:ListOfTimeActionsType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="BaseActionType">\r\n    <xs:annotation>\r\n      <xs:documentation>This abstract structure defines the base of an action. The base only contains information, if the last execution of the action was successful.</xs:documentation>\r\n    </xs:annotation>\r\n    <xs:sequence>\r\n      <xs:element name="LastActionResult" type="ua:StatusCode" minOccurs="0" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="BaseActionType" type="tns:BaseActionType" />\r\n\r\n  <xs:complexType name="ListOfBaseActionType">\r\n    <xs:sequence>\r\n      <xs:element name="BaseActionType" type="tns:BaseActionType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfBaseActionType" type="tns:ListOfBaseActionType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="WriteLocalVariableActionType">\r\n    <xs:annotation>\r\n      <xs:documentation>This structure defines an action to write the value of a Variable managed in the same Server where the action is used.</xs:documentation>\r\n    </xs:annotation>\r\n    <xs:complexContent mixed="false">\r\n      <xs:extension base="tns:BaseActionType">\r\n        <xs:sequence>\r\n          <xs:element name="Variable" type="ua:NodeId" minOccurs="0" nillable="true" />\r\n          <xs:element name="Value" type="ua:Variant" minOccurs="0" />\r\n        </xs:sequence>\r\n      </xs:extension>\r\n    </xs:complexContent>\r\n  </xs:complexType>\r\n  <xs:element name="WriteLocalVariableActionType" type="tns:WriteLocalVariableActionType" />\r\n\r\n  <xs:complexType name="ListOfWriteLocalVariableActionType">\r\n    <xs:sequence>\r\n      <xs:element name="WriteLocalVariableActionType" type="tns:WriteLocalVariableActionType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfWriteLocalVariableActionType" type="tns:ListOfWriteLocalVariableActionType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="CallLocalMethodActionType">\r\n    <xs:annotation>\r\n      <xs:documentation>This structure defines an action to call a Method of an Object managed in the same Server where the action is used.</xs:documentation>\r\n    </xs:annotation>\r\n    <xs:complexContent mixed="false">\r\n      <xs:extension base="tns:BaseActionType">\r\n        <xs:sequence>\r\n          <xs:element name="ObjectId" type="ua:NodeId" minOccurs="0" nillable="true" />\r\n          <xs:element name="MethodId" type="ua:NodeId" minOccurs="0" nillable="true" />\r\n          <xs:element name="InputValues" type="ua:ListOfVariant" minOccurs="0" nillable="true" />\r\n          <xs:element name="LastOutputValues" type="ua:ListOfVariant" minOccurs="0" nillable="true" />\r\n        </xs:sequence>\r\n      </xs:extension>\r\n    </xs:complexContent>\r\n  </xs:complexType>\r\n  <xs:element name="CallLocalMethodActionType" type="tns:CallLocalMethodActionType" />\r\n\r\n  <xs:complexType name="ListOfCallLocalMethodActionType">\r\n    <xs:sequence>\r\n      <xs:element name="CallLocalMethodActionType" type="tns:CallLocalMethodActionType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfCallLocalMethodActionType" type="tns:ListOfCallLocalMethodActionType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="TimeType">\r\n    <xs:annotation>\r\n      <xs:documentation>This structure that represents a point in time during a day</xs:documentation>\r\n    </xs:annotation>\r\n    <xs:sequence>\r\n      <xs:element name="Hour" type="xs:unsignedByte" minOccurs="0" />\r\n      <xs:element name="Minute" type="xs:unsignedByte" minOccurs="0" />\r\n      <xs:element name="Second" type="xs:unsignedByte" minOccurs="0" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="TimeType" type="tns:TimeType" />\r\n\r\n  <xs:complexType name="ListOfTimeType">\r\n    <xs:sequence>\r\n      <xs:element name="TimeType" type="tns:TimeType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfTimeType" type="tns:ListOfTimeType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="DailyScheduleType">\r\n    <xs:annotation>\r\n      <xs:documentation>This structure defines a sequence of TimeActionsType structures. Each element in the sequence defines a time/actions pair that describes the actions to be executed at a given point in the day.</xs:documentation>\r\n    </xs:annotation>\r\n    <xs:sequence>\r\n      <xs:element name="DaySchedule" type="tns:ListOfTimeActionsType" minOccurs="0" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="DailyScheduleType" type="tns:DailyScheduleType" />\r\n\r\n  <xs:complexType name="ListOfDailyScheduleType">\r\n    <xs:sequence>\r\n      <xs:element name="DailyScheduleType" type="tns:DailyScheduleType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfDailyScheduleType" type="tns:ListOfDailyScheduleType" nillable="true"></xs:element>\r\n\r\n</xs:schema>',
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=183", browseName="Default JSON")
o6.hasEncoding(scheduler_datypes.SpecialEventType, o6.ns["ns=scheduler;i=183"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=184", browseName="Default JSON")
o6.hasEncoding(scheduler_datypes.SpecialEventPeriodType, o6.ns["ns=scheduler;i=184"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=185", browseName="Default JSON")
o6.hasEncoding(scheduler_datypes.CalendarEntryType, o6.ns["ns=scheduler;i=185"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=186", browseName="Default JSON")
o6.hasEncoding(scheduler_datypes.DateType, o6.ns["ns=scheduler;i=186"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=187", browseName="Default JSON")
o6.hasEncoding(scheduler_datypes.DateRangeType, o6.ns["ns=scheduler;i=187"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=188", browseName="Default JSON")
o6.hasEncoding(scheduler_datypes.TimeActionsType, o6.ns["ns=scheduler;i=188"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=189", browseName="Default JSON")
o6.hasEncoding(scheduler_datypes.BaseActionType, o6.ns["ns=scheduler;i=189"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=190", browseName="Default JSON")
o6.hasEncoding(scheduler_datypes.WriteLocalVariableActionType, o6.ns["ns=scheduler;i=190"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=191", browseName="Default JSON")
o6.hasEncoding(scheduler_datypes.CallLocalMethodActionType, o6.ns["ns=scheduler;i=191"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=192", browseName="Default JSON")
o6.hasEncoding(scheduler_datypes.TimeType, o6.ns["ns=scheduler;i=192"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scheduler;i=193", browseName="Default JSON")
o6.hasEncoding(scheduler_datypes.DailyScheduleType, o6.ns["ns=scheduler;i=193"])
ns0.vartypes.PropertyType(
    nodeId="ns=scheduler;i=194",
    browseName="EnumStrings",
    parent="ns=scheduler;i=74",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[15],
    value=[
        o6.LocalizedText("Unspecified"),
        o6.LocalizedText("January"),
        o6.LocalizedText("February"),
        o6.LocalizedText("March"),
        o6.LocalizedText("April"),
        o6.LocalizedText("May"),
        o6.LocalizedText("June"),
        o6.LocalizedText("July"),
        o6.LocalizedText("August"),
        o6.LocalizedText("September"),
        o6.LocalizedText("October"),
        o6.LocalizedText("November"),
        o6.LocalizedText("December"),
        o6.LocalizedText("Odd"),
        o6.LocalizedText("Even"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scheduler;i=195",
    browseName="EnumStrings",
    parent="ns=scheduler;i=76",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[35],
    value=[
        o6.LocalizedText("Unspecified"),
        o6.LocalizedText("Day1"),
        o6.LocalizedText("Day2"),
        o6.LocalizedText("Day3"),
        o6.LocalizedText("Day4"),
        o6.LocalizedText("Day5"),
        o6.LocalizedText("Day6"),
        o6.LocalizedText("Day7"),
        o6.LocalizedText("Day8"),
        o6.LocalizedText("Day9"),
        o6.LocalizedText("Day10"),
        o6.LocalizedText("Day11"),
        o6.LocalizedText("Day12"),
        o6.LocalizedText("Day13"),
        o6.LocalizedText("Day14"),
        o6.LocalizedText("Day15"),
        o6.LocalizedText("Day16"),
        o6.LocalizedText("Day17"),
        o6.LocalizedText("Day18"),
        o6.LocalizedText("Day19"),
        o6.LocalizedText("Day20"),
        o6.LocalizedText("Day21"),
        o6.LocalizedText("Day22"),
        o6.LocalizedText("Day23"),
        o6.LocalizedText("Day24"),
        o6.LocalizedText("Day25"),
        o6.LocalizedText("Day26"),
        o6.LocalizedText("Day27"),
        o6.LocalizedText("Day28"),
        o6.LocalizedText("Day29"),
        o6.LocalizedText("Day30"),
        o6.LocalizedText("Day31"),
        o6.LocalizedText("LastDayOfMonth"),
        o6.LocalizedText("OddDayOfMonth"),
        o6.LocalizedText("EvenDayOfMonth"),
    ],
)


del Any, TYPE_CHECKING, uuid, o6, ns0, scheduler_datypes, scheduler_objtypes
