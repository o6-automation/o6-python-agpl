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

"""Generated OPC UA mdis namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as mdis_reftypes
from . import datatypes as mdis_datypes
from . import vartypes as mdis_vartypes
from . import objtypes as mdis_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=6",
    browseName="EnumValues",
    parent="ns=mdis;i=5",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("SEM_A"), description=o6.LocalizedText("Valve move command selection SEM A")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("SEM_B"), description=o6.LocalizedText("Valve move command selection SEM B")),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("Auto"),
            description=o6.LocalizedText(
                "Subsea equipment vendor decides how to send the command. In some cases, this would be both SEMs, in others it would mean a subsea system&#8217;s choice of a SEM."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=603",
    browseName="EnumValues",
    parent="ns=mdis;i=602",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Moving"), description=o6.LocalizedText("The choke is currently moving (in progress)")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Stopped"), description=o6.LocalizedText("The move has stopped")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=616",
    browseName="EnumValues",
    parent="ns=mdis;i=3",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Close"), description=o6.LocalizedText("The last command to the valve was Close")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Open"), description=o6.LocalizedText("The last command to the valve was Open")),
        ns0.datatypes.EnumValueType(
            value=4, displayName=o6.LocalizedText("None"), description=o6.LocalizedText("No known command has been sent to the valve. The initial setting on start-up of a server.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=700",
    browseName="EnumValues",
    parent="ns=mdis;i=699",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("NotAvailable"), description=o6.LocalizedText("The profile / signature is not available (in progress)")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Completed"), description=o6.LocalizedText("The profile / signature request has completed")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Failed"), description=o6.LocalizedText("The profile / signature request has failed")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=702",
    browseName="EnumValues",
    parent="ns=mdis;i=701",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Close"), description=o6.LocalizedText("The command to the Choke is Close")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Open"), description=o6.LocalizedText("The command to the Choke is Open")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=704",
    browseName="EnumValues",
    parent="ns=mdis;i=703",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Closed"), description=o6.LocalizedText("The Valve is Closed")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Open"), description=o6.LocalizedText("The Valve is Open")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Moving"), description=o6.LocalizedText("The Valve is Moving")),
        ns0.datatypes.EnumValueType(
            value=8,
            displayName=o6.LocalizedText("Unknown"),
            description=o6.LocalizedText(
                "The Valve is in an unknown state. This value can be used when a subsea vendor does not have any last command information and does not know the state of the valve."
            ),
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=mdis;i=1052",
    browseName="ns=mdis;ProcessVariable",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=1056", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=1057", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Float,
)
o6.reference(mdis_objtypes.MDISInstrumentObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=1052"])
ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=1288",
    browseName="EnumValues",
    parent="ns=mdis;i=1287",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Initial"), description=o6.LocalizedText("no command (initial state)")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Inprogress"), description=o6.LocalizedText("command in progress")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Complete"), description=o6.LocalizedText("command completed")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Fault"), description=o6.LocalizedText("command fault")),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=1300",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=1299",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=1301",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=1299",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=mdis;i=1299", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=1300"]), outputArgs=o6.hasProperty(o6.ns["ns=mdis;i=1301"]))

ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=1303",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=1302",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=mdis;i=1302", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=1303"]))

ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=1305",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=1304",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=1306",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=1304",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=mdis;i=1304", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=1305"]), outputArgs=o6.hasProperty(o6.ns["ns=mdis;i=1306"]))

ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=1308",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=1307",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=mdis;i=1307", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=1308"]))

ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=1310",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=1309",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=1311",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=1309",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=mdis;i=1309", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=1310"]), outputArgs=o6.hasProperty(o6.ns["ns=mdis;i=1311"]))

ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=1313",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=1312",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=mdis;i=1312", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=1313"]))

ns0.objtypes.FileType(
    nodeId="ns=mdis;i=1294",
    browseName="ns=mdis;<ValveSignature>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=1295", browseName="Size", description="The size of the file in bytes.", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=1296", browseName="Writable", description="Whether the file is writable.", dataType=o6.Boolean)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=mdis;i=1297", browseName="UserWritable", description="Whether the file is writable by the current user.", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=1298", browseName="OpenCount", description="The current number of open file handles.", dataType=o6.UInt16)),
        o6.hasComponent(o6.ns["ns=mdis;i=1299"]),
        o6.hasComponent(o6.ns["ns=mdis;i=1302"]),
        o6.hasComponent(o6.ns["ns=mdis;i=1304"]),
        o6.hasComponent(o6.ns["ns=mdis;i=1307"]),
        o6.hasComponent(o6.ns["ns=mdis;i=1309"]),
        o6.hasComponent(o6.ns["ns=mdis;i=1312"]),
    ],
)
o6.reference(mdis_objtypes.MDISValveObjectType, mdis_reftypes.HasSignature, o6.ns["ns=mdis;i=1294"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=mdis;i=1333",
    browseName="ns=mdis;ProcessVariable",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=1337", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=1338", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Float,
)
mdis_objtypes.MDISInstrumentObjectType(
    nodeId="ns=mdis;i=1324",
    browseName="ns=mdis;<InstrumentPlaceholder>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=1325", browseName="ns=mdis;Fault", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=mdis;i=1333"]),
    ],
)
o6.reference(mdis_objtypes.MDISAggregateObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=1324"])
mdis_objtypes.MDISDigitalInstrumentObjectType(
    nodeId="ns=mdis;i=1347",
    browseName="ns=mdis;<DigitalPlaceholder>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=1348", browseName="ns=mdis;Fault", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=1356", browseName="ns=mdis;State", dataType=o6.Boolean)),
    ],
)
o6.reference(mdis_objtypes.MDISAggregateObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=1347"])
mdis_objtypes.MDISDiscreteInstrumentObjectType(
    nodeId="ns=mdis;i=1357",
    browseName="ns=mdis;<DiscretePlaceholder>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=1358", browseName="ns=mdis;Fault", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=1366", browseName="ns=mdis;State", dataType=o6.UInt32)),
    ],
)
o6.reference(mdis_objtypes.MDISAggregateObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=1357"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=mdis;i=1376",
    browseName="ns=mdis;ProcessVariable",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=1380", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=1381", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Float,
)


ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=1391",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=1390",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Value", dataType=o6.Float, valueRank=-1, description=o6.LocalizedText("Float value that is being written to the object"))],
)
o6.call(nodeId="ns=mdis;i=1390", browseName="ns=mdis;WriteValue", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=1391"]))

mdis_objtypes.MDISInstrumentOutObjectType(
    nodeId="ns=mdis;i=1367",
    browseName="ns=mdis;<InstrumentOutPlaceholder>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=1368", browseName="ns=mdis;Fault", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=mdis;i=1376"]),
        o6.hasComponent(o6.ns["ns=mdis;i=1390"]),
    ],
)
o6.reference(mdis_objtypes.MDISAggregateObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=1367"])


ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=1403",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=1402",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="State", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("Boolean state that is being written to the object"))],
)
o6.call(nodeId="ns=mdis;i=1402", browseName="ns=mdis;WriteState", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=1403"]))

mdis_objtypes.MDISDigitalOutObjectType(
    nodeId="ns=mdis;i=1392",
    browseName="ns=mdis;<DigitalOutPlaceholder>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=1393", browseName="ns=mdis;Fault", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=1401", browseName="ns=mdis;State", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=mdis;i=1402"]),
    ],
)
o6.reference(mdis_objtypes.MDISAggregateObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=1392"])


ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=1415",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=1414",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="State", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("Unit32 state that is being written to the object"))],
)
o6.call(nodeId="ns=mdis;i=1414", browseName="ns=mdis;WriteValue", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=1415"]))

mdis_objtypes.MDISDiscreteOutObjectType(
    nodeId="ns=mdis;i=1404",
    browseName="ns=mdis;<DiscreteOutPlaceholder>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=1405", browseName="ns=mdis;Fault", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=1413", browseName="ns=mdis;State", dataType=o6.UInt32)),
        o6.hasComponent(o6.ns["ns=mdis;i=1414"]),
    ],
)
o6.reference(mdis_objtypes.MDISAggregateObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=1404"])


ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=1434",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=1433",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(
            name="Direction",
            dataType=mdis_datypes.CommandEnum,
            valueRank=-1,
            description=o6.LocalizedText("The enumeration indicates whether the command is to open the valve or to close the valve"),
        ),
        ns0.datatypes.Argument(
            name="OverrideInterlock",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("Boolean indicating if the open or close command should override any defeat able interlocks"),
        ),
        ns0.datatypes.Argument(name="SEM", dataType=mdis_datypes.SEMEnum, valueRank=-1, description=o6.LocalizedText("The selection of which SEM to send the command to")),
        ns0.datatypes.Argument(
            name="Signature", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("Boolean indicating if a profile should be generated by this move command request")
        ),
        ns0.datatypes.Argument(
            name="ShutdownRequest", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("Boolean indicates that this command is a shutdown move command")
        ),
    ],
)
o6.call(nodeId="ns=mdis;i=1433", browseName="ns=mdis;Move", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=1434"]))

mdis_objtypes.MDISValveObjectType(
    nodeId="ns=mdis;i=1416",
    browseName="ns=mdis;<ValvePlaceholder>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=1417", browseName="ns=mdis;Fault", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=1425", browseName="ns=mdis;Position", dataType=mdis_datypes.ValvePositionEnum)),
        o6.hasComponent(o6.ns["ns=mdis;i=1433"]),
    ],
)
o6.reference(mdis_objtypes.MDISAggregateObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=1416"])


ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=1456",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=1455",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Position", dataType=o6.Float, valueRank=-1, description=o6.LocalizedText("A number (in percent) indicating the percent open")),
        ns0.datatypes.Argument(
            name="OverrideInterlocks",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("Boolean indicating if the open or close command should override any defeat able interlocks"),
        ),
        ns0.datatypes.Argument(name="SEM", dataType=mdis_datypes.SEMEnum, valueRank=-1, description=o6.LocalizedText("The selection of which SEM to send the command to")),
    ],
)
o6.call(nodeId="ns=mdis;i=1455", browseName="ns=mdis;Move", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=1456"]))

ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=1461",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=1460",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.Float, valueRank=-1, description=o6.LocalizedText("A number (in percent) indicating the percent open"))],
)
o6.call(nodeId="ns=mdis;i=1460", browseName="ns=mdis;SetCalculatedPosition", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=1461"]))

mdis_objtypes.MDISChokeObjectType(
    nodeId="ns=mdis;i=1437",
    browseName="ns=mdis;<ChokePlaceholder>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=1438", browseName="ns=mdis;Fault", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=1446", browseName="ns=mdis;CalculatedPosition", dataType=o6.Float)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=1449", browseName="ns=mdis;Moving", dataType=mdis_datypes.ChokeMoveEnum)),
        o6.hasComponent(o6.ns["ns=mdis;i=1455"]),
        o6.hasComponent(o6.call(nodeId="ns=mdis;i=1459", browseName="ns=mdis;Abort")),
        o6.hasComponent(o6.ns["ns=mdis;i=1460"]),
    ],
)
o6.reference(mdis_objtypes.MDISAggregateObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=1437"])


ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=1474",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=1473",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="TargetTime", dataType=ns0.datatypes.UtcTime, valueRank=-1, description=o6.LocalizedText("The UTC Time that the Server shall use to update its internal clock.")
        )
    ],
)
o6.call(nodeId="ns=mdis;i=1473", browseName="ns=mdis;SetTime", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=1474"]))

mdis_objtypes.MDISTimeSyncObjectType(
    nodeId="ns=mdis;i=1472", browseName="ns=mdis;TimeSynchronization", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=mdis;i=1473"])]
)
o6.reference(mdis_objtypes.MDISInformationObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=1472"])
mdis_vartypes.MDISVersionVariableType(
    nodeId="ns=mdis;i=1476",
    browseName="ns=mdis;MDISVersion",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=1477", browseName="ns=mdis;MajorVersion", dataType=o6.Byte)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=1478", browseName="ns=mdis;MinorVersion", dataType=o6.Byte)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=1479", browseName="ns=mdis;Build", dataType=o6.Byte)),
    ],
    dataType=mdis_datypes.MDISVersionDataType,
)
o6.reference(mdis_objtypes.MDISInformationObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=1476"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mdis;i=1480", browseName="Default XML")
o6.hasEncoding(mdis_datypes.MDISVersionDataType, o6.ns["ns=mdis;i=1480"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=mdis;i=1481", browseName="ns=mdis;MDISVersionDataType", dataType=o6.String, value="//xs:element[@name='MDISVersionDataType']")
o6.reference(o6.ns["ns=mdis;i=1480"], "i=39", o6.ns["ns=mdis;i=1481"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mdis;i=1484", browseName="Default Binary")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=mdis;i=1485", browseName="ns=mdis;MDISVersionDataType", dataType=o6.String, value="MDISVersionDataType")
o6.reference(o6.ns["ns=mdis;i=1484"], "i=39", o6.ns["ns=mdis;i=1485"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMDIS = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=mdis;i=5001",
    browseName="ns=mdis;http://opcfoundation.org/UA/MDIS",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=6001", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=6002", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2024-11-19T12:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=6003", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/MDIS")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=6004", browseName="NamespaceVersion", dataType=o6.String, value="1.3")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mdis;i=6005", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mdis;i=6006", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["0:5000"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=6007", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
opcDotMDIS_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=mdis;i=374",
    browseName="ns=mdis;Opc.MDIS",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mdis;i=376",
                browseName="NamespaceUri",
                description="A URI that uniquely identifies the dictionary.",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/MDIS",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mdis;i=15002",
                browseName="Deprecated",
                description="Indicates that all of the definitions for the dictionary are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
                value=True,
            )
        ),
        o6.hasComponent(o6.ns["ns=mdis;i=1485"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:ua="http://opcfoundation.org/UA/" xmlns:tns="http://opcfoundation.org/UA/MDIS" xmlns:opc="http://opcfoundation.org/BinarySchema/" TargetNamespace="http://opcfoundation.org/UA/MDIS" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" DefaultByteOrder="LittleEndian">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="MDISVersionDataType">\n  <opc:Field TypeName="opc:Byte" Name="MajorVersion"/>\n  <opc:Field TypeName="opc:Byte" Name="MinorVersion"/>\n  <opc:Field TypeName="opc:Byte" Name="Build"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="ArbitrationModeEnum">\n  <opc:EnumeratedValue Value="1" Name="Average"/>\n  <opc:EnumeratedValue Value="2" Name="DefaultA"/>\n  <opc:EnumeratedValue Value="4" Name="DefaultB"/>\n  <opc:EnumeratedValue Value="8" Name="ForceA"/>\n  <opc:EnumeratedValue Value="16" Name="ForceB"/>\n  <opc:EnumeratedValue Value="32" Name="High"/>\n  <opc:EnumeratedValue Value="64" Name="Low"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ChokeCommandEnum">\n  <opc:EnumeratedValue Value="1" Name="Close"/>\n  <opc:EnumeratedValue Value="2" Name="Open"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ChokeMoveEnum">\n  <opc:EnumeratedValue Value="1" Name="Moving"/>\n  <opc:EnumeratedValue Value="2" Name="Stopped"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="CIMVMoveEnum">\n  <opc:EnumeratedValue Value="1" Name="MoveClose"/>\n  <opc:EnumeratedValue Value="2" Name="MoveOpen"/>\n  <opc:EnumeratedValue Value="4" Name="Stop"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="CIMVOperationModeEnum">\n  <opc:EnumeratedValue Value="1" Name="Position"/>\n  <opc:EnumeratedValue Value="2" Name="Flow"/>\n  <opc:EnumeratedValue Value="4" Name="Manual"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="CommandEnum">\n  <opc:EnumeratedValue Value="1" Name="Close"/>\n  <opc:EnumeratedValue Value="2" Name="Open"/>\n  <opc:EnumeratedValue Value="4" Name="None"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="MotorOperationEnum">\n  <opc:EnumeratedValue Value="1" Name="Off"/>\n  <opc:EnumeratedValue Value="2" Name="Auto"/>\n  <opc:EnumeratedValue Value="4" Name="Manual"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="MotorStateEnum">\n  <opc:EnumeratedValue Value="1" Name="Active"/>\n  <opc:EnumeratedValue Value="2" Name="NonActive"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="SEMEnum">\n  <opc:EnumeratedValue Value="1" Name="SEM_A"/>\n  <opc:EnumeratedValue Value="2" Name="SEM_B"/>\n  <opc:EnumeratedValue Value="4" Name="Auto"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="SetCalculatedPositionEnum">\n  <opc:EnumeratedValue Value="0" Name="Initial"/>\n  <opc:EnumeratedValue Value="1" Name="Inprogress"/>\n  <opc:EnumeratedValue Value="2" Name="Complete"/>\n  <opc:EnumeratedValue Value="4" Name="Fault"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="SignatureStatusEnum">\n  <opc:EnumeratedValue Value="1" Name="NotAvailable"/>\n  <opc:EnumeratedValue Value="2" Name="Completed"/>\n  <opc:EnumeratedValue Value="4" Name="Failed"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ValvePositionEnum">\n  <opc:EnumeratedValue Value="1" Name="Closed"/>\n  <opc:EnumeratedValue Value="2" Name="Open"/>\n  <opc:EnumeratedValue Value="4" Name="Moving"/>\n  <opc:EnumeratedValue Value="8" Name="Unknown"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
opcDotMDIS = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=mdis;i=367",
    browseName="ns=mdis;Opc.MDIS",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mdis;i=369",
                browseName="NamespaceUri",
                description="A URI that uniquely identifies the dictionary.",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/MDIS/Types.xsd",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mdis;i=15003",
                browseName="Deprecated",
                description="Indicates that all of the definitions for the dictionary are available through a DataTypeDefinition Attribute.",
                dataType=o6.Boolean,
                value=True,
            )
        ),
        o6.hasComponent(o6.ns["ns=mdis;i=1481"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/MDIS/Types.xsd" targetNamespace="http://opcfoundation.org/UA/MDIS/Types.xsd" elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="ArbitrationModeEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Average_1"/>\n   <xs:enumeration value="DefaultA_2"/>\n   <xs:enumeration value="DefaultB_4"/>\n   <xs:enumeration value="ForceA_8"/>\n   <xs:enumeration value="ForceB_16"/>\n   <xs:enumeration value="High_32"/>\n   <xs:enumeration value="Low_64"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ArbitrationModeEnum" name="ArbitrationModeEnum"/>\n <xs:complexType name="ListOfArbitrationModeEnum">\n  <xs:sequence>\n   <xs:element type="tns:ArbitrationModeEnum" minOccurs="0" maxOccurs="unbounded" nillable="true" name="ArbitrationModeEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfArbitrationModeEnum" nillable="true" name="ListOfArbitrationModeEnum"/>\n <xs:simpleType name="ChokeCommandEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Close_1"/>\n   <xs:enumeration value="Open_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ChokeCommandEnum" name="ChokeCommandEnum"/>\n <xs:complexType name="ListOfChokeCommandEnum">\n  <xs:sequence>\n   <xs:element type="tns:ChokeCommandEnum" minOccurs="0" maxOccurs="unbounded" nillable="true" name="ChokeCommandEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfChokeCommandEnum" nillable="true" name="ListOfChokeCommandEnum"/>\n <xs:simpleType name="ChokeMoveEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Moving_1"/>\n   <xs:enumeration value="Stopped_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ChokeMoveEnum" name="ChokeMoveEnum"/>\n <xs:complexType name="ListOfChokeMoveEnum">\n  <xs:sequence>\n   <xs:element type="tns:ChokeMoveEnum" minOccurs="0" maxOccurs="unbounded" nillable="true" name="ChokeMoveEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfChokeMoveEnum" nillable="true" name="ListOfChokeMoveEnum"/>\n <xs:simpleType name="CIMVMoveEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="MoveClose_1"/>\n   <xs:enumeration value="MoveOpen_2"/>\n   <xs:enumeration value="Stop_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CIMVMoveEnum" name="CIMVMoveEnum"/>\n <xs:complexType name="ListOfCIMVMoveEnum">\n  <xs:sequence>\n   <xs:element type="tns:CIMVMoveEnum" minOccurs="0" maxOccurs="unbounded" nillable="true" name="CIMVMoveEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCIMVMoveEnum" nillable="true" name="ListOfCIMVMoveEnum"/>\n <xs:simpleType name="CIMVOperationModeEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Position_1"/>\n   <xs:enumeration value="Flow_2"/>\n   <xs:enumeration value="Manual_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CIMVOperationModeEnum" name="CIMVOperationModeEnum"/>\n <xs:complexType name="ListOfCIMVOperationModeEnum">\n  <xs:sequence>\n   <xs:element type="tns:CIMVOperationModeEnum" minOccurs="0" maxOccurs="unbounded" nillable="true" name="CIMVOperationModeEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCIMVOperationModeEnum" nillable="true" name="ListOfCIMVOperationModeEnum"/>\n <xs:simpleType name="CommandEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Close_1"/>\n   <xs:enumeration value="Open_2"/>\n   <xs:enumeration value="None_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CommandEnum" name="CommandEnum"/>\n <xs:complexType name="ListOfCommandEnum">\n  <xs:sequence>\n   <xs:element type="tns:CommandEnum" minOccurs="0" maxOccurs="unbounded" nillable="true" name="CommandEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCommandEnum" nillable="true" name="ListOfCommandEnum"/>\n <xs:simpleType name="MotorOperationEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Off_1"/>\n   <xs:enumeration value="Auto_2"/>\n   <xs:enumeration value="Manual_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:MotorOperationEnum" name="MotorOperationEnum"/>\n <xs:complexType name="ListOfMotorOperationEnum">\n  <xs:sequence>\n   <xs:element type="tns:MotorOperationEnum" minOccurs="0" maxOccurs="unbounded" nillable="true" name="MotorOperationEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfMotorOperationEnum" nillable="true" name="ListOfMotorOperationEnum"/>\n <xs:simpleType name="MotorStateEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Active_1"/>\n   <xs:enumeration value="NonActive_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:MotorStateEnum" name="MotorStateEnum"/>\n <xs:complexType name="ListOfMotorStateEnum">\n  <xs:sequence>\n   <xs:element type="tns:MotorStateEnum" minOccurs="0" maxOccurs="unbounded" nillable="true" name="MotorStateEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfMotorStateEnum" nillable="true" name="ListOfMotorStateEnum"/>\n <xs:simpleType name="SEMEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="SEM_A_1"/>\n   <xs:enumeration value="SEM_B_2"/>\n   <xs:enumeration value="Auto_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SEMEnum" name="SEMEnum"/>\n <xs:complexType name="ListOfSEMEnum">\n  <xs:sequence>\n   <xs:element type="tns:SEMEnum" minOccurs="0" maxOccurs="unbounded" nillable="true" name="SEMEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSEMEnum" nillable="true" name="ListOfSEMEnum"/>\n <xs:simpleType name="SetCalculatedPositionEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Initial_0"/>\n   <xs:enumeration value="Inprogress_1"/>\n   <xs:enumeration value="Complete_2"/>\n   <xs:enumeration value="Fault_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SetCalculatedPositionEnum" name="SetCalculatedPositionEnum"/>\n <xs:complexType name="ListOfSetCalculatedPositionEnum">\n  <xs:sequence>\n   <xs:element type="tns:SetCalculatedPositionEnum" minOccurs="0" maxOccurs="unbounded" nillable="true" name="SetCalculatedPositionEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSetCalculatedPositionEnum" nillable="true" name="ListOfSetCalculatedPositionEnum"/>\n <xs:simpleType name="SignatureStatusEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="NotAvailable_1"/>\n   <xs:enumeration value="Completed_2"/>\n   <xs:enumeration value="Failed_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:SignatureStatusEnum" name="SignatureStatusEnum"/>\n <xs:complexType name="ListOfSignatureStatusEnum">\n  <xs:sequence>\n   <xs:element type="tns:SignatureStatusEnum" minOccurs="0" maxOccurs="unbounded" nillable="true" name="SignatureStatusEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSignatureStatusEnum" nillable="true" name="ListOfSignatureStatusEnum"/>\n <xs:simpleType name="ValvePositionEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Closed_1"/>\n   <xs:enumeration value="Open_2"/>\n   <xs:enumeration value="Moving_4"/>\n   <xs:enumeration value="Unknown_8"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ValvePositionEnum" name="ValvePositionEnum"/>\n <xs:complexType name="ListOfValvePositionEnum">\n  <xs:sequence>\n   <xs:element type="tns:ValvePositionEnum" minOccurs="0" maxOccurs="unbounded" nillable="true" name="ValvePositionEnum"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfValvePositionEnum" nillable="true" name="ListOfValvePositionEnum"/>\n <xs:complexType name="MDISVersionDataType">\n  <xs:sequence>\n   <xs:element type="xs:unsignedByte" minOccurs="0" maxOccurs="1" name="MajorVersion"/>\n   <xs:element type="xs:unsignedByte" minOccurs="0" maxOccurs="1" name="MinorVersion"/>\n   <xs:element type="xs:unsignedByte" minOccurs="0" maxOccurs="1" name="Build"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:MDISVersionDataType" name="MDISVersionDataType"/>\n <xs:complexType name="ListOfMDISVersionDataType">\n  <xs:sequence>\n   <xs:element type="tns:MDISVersionDataType" minOccurs="0" maxOccurs="unbounded" nillable="true" name="MDISVersionDataType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfMDISVersionDataType" nillable="true" name="ListOfMDISVersionDataType"/>\n</xs:schema>\n',
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mdis;i=15004", browseName="Default JSON")
o6.hasEncoding(mdis_datypes.MDISVersionDataType, o6.ns["ns=mdis;i=15004"])
ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=15008",
    browseName="EnumValues",
    parent="ns=mdis;i=15007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("MoveClose"), description=o6.LocalizedText("The CIMV is moving in the close direction")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("MoveOpen"), description=o6.LocalizedText("The CIMV is moving in the open direction")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Stop"), description=o6.LocalizedText("The CIMV is not moving")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=15010",
    browseName="EnumValues",
    parent="ns=mdis;i=15009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[7],
    value=[
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Average"), description=o6.LocalizedText("Build the average of both values (if both available)")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("DefaultA"), description=o6.LocalizedText("Select SourceA (if available), else SourceB")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("DefaultB"), description=o6.LocalizedText("Select SourceB (if available), else SourceA")),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("ForceA"), description=o6.LocalizedText("Always select SourceA")),
        ns0.datatypes.EnumValueType(value=16, displayName=o6.LocalizedText("ForceB"), description=o6.LocalizedText("Always select SourceB")),
        ns0.datatypes.EnumValueType(value=32, displayName=o6.LocalizedText("High"), description=o6.LocalizedText("Highest Value (for digital this is an OR operation)")),
        ns0.datatypes.EnumValueType(value=64, displayName=o6.LocalizedText("Low"), description=o6.LocalizedText("Lowest Value (for digital this is an AND operation)")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=15012",
    browseName="EnumValues",
    parent="ns=mdis;i=15011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Active"), description=o6.LocalizedText("The Motor is in active state")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("NonActive"), description=o6.LocalizedText("The Motor is not in active state")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=15014",
    browseName="EnumValues",
    parent="ns=mdis;i=15013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Off"), description=o6.LocalizedText("The Motor cannot be started either automatically or manually")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Auto"), description=o6.LocalizedText("The Motor works automatically")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Manual"), description=o6.LocalizedText("The Motor is controlled manually")),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=15047",
    browseName="InputArguments",
    parent="ns=mdis;i=15046",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="TargetTime", dataType=ns0.datatypes.UtcTime, valueRank=-1, description=o6.LocalizedText("The UTC Time that the Server shall use to update its internal clock.")
        )
    ],
)
o6.call(nodeId="ns=mdis;i=15046", browseName="ns=mdis;SetTime", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=15047"]))

mdis_objtypes.MDISTimeSyncObjectType(nodeId="ns=mdis;i=15045", browseName="ns=mdis;TimeSynchronization", references=[o6.hasComponent(o6.ns["ns=mdis;i=15046"])])
mdis_vartypes.MDISVersionVariableType(
    nodeId="ns=mdis;i=15049",
    browseName="ns=mdis;MDISVersion",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15050", browseName="ns=mdis;MajorVersion", dataType=o6.Byte, value=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15051", browseName="ns=mdis;MinorVersion", dataType=o6.Byte, value=3)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15052", browseName="ns=mdis;Build", dataType=o6.Byte, value=1)),
    ],
    dataType=mdis_datypes.MDISVersionDataType,
)
mDISInformation = mdis_objtypes.MDISInformationObjectType(
    nodeId="ns=mdis;i=15044",
    browseName="ns=mdis;MDISInformation",
    description="The well known MDIS standard information object instance",
    references=[
        o6.hasComponent(o6.ns["ns=mdis;i=15045"]),
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=mdis;i=15048", browseName="ns=mdis;Signatures")),
        o6.hasComponent(o6.ns["ns=mdis;i=15049"]),
    ],
    parent="i=85",
    referenceType=ns0.reftypes.Organizes,
)
ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=15103",
    browseName="EnumValues",
    parent="ns=mdis;i=15102",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("Position"), description=o6.LocalizedText("The CIMV is in closed-loop Position control mode. Sending fix position")
        ),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Flow"), description=o6.LocalizedText("The CIMV is in closed-loop Flow control mode (auto regulate)")),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("Manual"),
            description=o6.LocalizedText(
                "The CIMV is in open-loop Manual mode (compare it to step mode &#8211; i.e., move some increment relative to current). Note: some CIMV instance may not support this mode.",
                "",
            ),
        ),
    ],
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=mdis;i=15124",
    browseName="ns=mdis;FlowRate",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15128", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15129", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Float,
)
o6.reference(mdis_objtypes.MDISCIMVObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=15124"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=mdis;i=15130",
    browseName="ns=mdis;TotalFlow",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15134", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15135", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Float,
)
o6.reference(mdis_objtypes.MDISCIMVObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=15130"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=mdis;i=15138",
    browseName="ns=mdis;DeviceCurrent",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15142", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15143", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Float,
)
o6.reference(mdis_objtypes.MDISCIMVObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=15138"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=mdis;i=15144",
    browseName="ns=mdis;InletPressure",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15148", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15149", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Float,
)
o6.reference(mdis_objtypes.MDISCIMVObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=15144"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=mdis;i=15150",
    browseName="ns=mdis;InternalPressure",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15154", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15155", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Float,
)
o6.reference(mdis_objtypes.MDISCIMVObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=15150"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=mdis;i=15156",
    browseName="ns=mdis;OutletPressure",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15160", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15161", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Float,
)
o6.reference(mdis_objtypes.MDISCIMVObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=15156"])


ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=15179",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=15178",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Initial", dataType=ns0.datatypes.Number, valueRank=-1, description=o6.LocalizedText("The value to initialize the Object Count to, default is 0")
        )
    ],
)
o6.call(nodeId="ns=mdis;i=15178", browseName="ns=mdis;SetCount", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=15179"]))

mdis_objtypes.MDISCounterObjectType(
    nodeId="ns=mdis;i=15005",
    browseName="ns=mdis;TotalMotorRuntime",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15006", browseName="ns=mdis;Count", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=mdis;i=15178"]),
    ],
)
o6.reference(mdis_objtypes.MDISCIMVObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=15005"])


ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=15183",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=15182",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Initial", dataType=ns0.datatypes.Number, valueRank=-1, description=o6.LocalizedText("The value to initialize the Object Count to, default is 0")
        )
    ],
)
o6.call(nodeId="ns=mdis;i=15182", browseName="ns=mdis;SetCount", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=15183"]))

mdis_objtypes.MDISCounterObjectType(
    nodeId="ns=mdis;i=15180",
    browseName="ns=mdis;MotorOperationsCount",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15181", browseName="ns=mdis;Count", dataType=o6.UInt32)),
        o6.hasComponent(o6.ns["ns=mdis;i=15182"]),
    ],
)
o6.reference(mdis_objtypes.MDISCIMVObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=15180"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=mdis;i=15221",
    browseName="ns=mdis;ProcessVariable",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15225", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15226", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Float,
)
mdis_objtypes.MDISInstrumentArbitrationObjectType(
    nodeId="ns=mdis;i=15212",
    browseName="ns=mdis;<InstrumentArbitrationPlaceholder>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15213", browseName="ns=mdis;Fault", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=mdis;i=15221"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15235", browseName="ns=mdis;SourceA", dataType=o6.Float)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15236", browseName="ns=mdis;SourceB", dataType=o6.Float)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15237", browseName="ns=mdis;ArbitrationMode", dataType=mdis_datypes.ArbitrationModeEnum)),
    ],
)
o6.reference(mdis_objtypes.MDISAggregateObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=15212"])
mdis_objtypes.MDISDigitalArbitrationObjectType(
    nodeId="ns=mdis;i=15241",
    browseName="ns=mdis;<DigitalArbitrationPlaceholder>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15242", browseName="ns=mdis;Fault", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15250", browseName="ns=mdis;State", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15251", browseName="ns=mdis;SourceA", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15252", browseName="ns=mdis;SourceB", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15253", browseName="ns=mdis;ArbitrationMode", dataType=mdis_datypes.ArbitrationModeEnum)),
    ],
)
o6.reference(mdis_objtypes.MDISAggregateObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=15241"])
mdis_objtypes.MDISDiscreteArbitrationObjectType(
    nodeId="ns=mdis;i=15256",
    browseName="ns=mdis;<DiscreteArbitrationPlaceholder>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15257", browseName="ns=mdis;Fault", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15265", browseName="ns=mdis;State", dataType=o6.UInt32)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15266", browseName="ns=mdis;SourceA", dataType=o6.UInt32)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15267", browseName="ns=mdis;SourceB", dataType=o6.UInt32)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15268", browseName="ns=mdis;ArbitrationMode", dataType=mdis_datypes.ArbitrationModeEnum)),
    ],
)
o6.reference(mdis_objtypes.MDISAggregateObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=15256"])


ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=15288",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=15287",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Position", dataType=o6.Float, valueRank=-1, description=o6.LocalizedText("A number (in percent) indicating the percent open")),
        ns0.datatypes.Argument(
            name="OverrideInterlocks",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("Boolean indicating if the open or close command should override any defeat able interlocks"),
        ),
        ns0.datatypes.Argument(name="SEM", dataType=mdis_datypes.SEMEnum, valueRank=-1, description=o6.LocalizedText("The selection of which SEM to send the command to")),
    ],
)
o6.call(nodeId="ns=mdis;i=15287", browseName="ns=mdis;Move", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=15288"]))

mdis_objtypes.MDISElectricChokeObjectType(
    nodeId="ns=mdis;i=15271",
    browseName="ns=mdis;<ElectricChokePlaceholder>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15272", browseName="ns=mdis;Fault", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15280", browseName="ns=mdis;ActualPosition", dataType=o6.Float)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15281", browseName="ns=mdis;Moving", dataType=mdis_datypes.ChokeMoveEnum)),
        o6.hasComponent(o6.ns["ns=mdis;i=15287"]),
        o6.hasComponent(o6.call(nodeId="ns=mdis;i=15289", browseName="ns=mdis;Abort")),
    ],
)
o6.reference(mdis_objtypes.MDISAggregateObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=15271"])
mdis_objtypes.MDISMotorObjectType(
    nodeId="ns=mdis;i=15290",
    browseName="ns=mdis;<MotorPlaceholder>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15291", browseName="ns=mdis;Fault", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15299", browseName="ns=mdis;Running", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15300", browseName="ns=mdis;Operation", dataType=mdis_datypes.MotorOperationEnum)),
    ],
)
o6.reference(mdis_objtypes.MDISAggregateObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=15290"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=mdis;i=15202",
    browseName="ns=mdis;TargetFlowRate",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15302", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15303", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Float,
)
o6.reference(mdis_objtypes.MDISCIMVObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=15202"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=mdis;i=15329",
    browseName="ns=mdis;FlowRate",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15333", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15334", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Float,
)


ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=15374",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=15373",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="Mode", dataType=mdis_datypes.CIMVOperationModeEnum, valueRank=-1, description=o6.LocalizedText("Enumeration indicating the requested operation mode")
        ),
        ns0.datatypes.Argument(name="SEM", dataType=mdis_datypes.SEMEnum, valueRank=-1, description=o6.LocalizedText("The selection of which SEM to send the command to")),
        ns0.datatypes.Argument(
            name="ShutdownRequest",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("Boolean indicating if the open or close command should override any interlocks"),
        ),
    ],
)
o6.call(nodeId="ns=mdis;i=15373", browseName="ns=mdis;SetOperationMode", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=15374"]))

ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=15376",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=15375",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="FlowRate", dataType=o6.Float, valueRank=-1, description=o6.LocalizedText("Target flow rate. The CIMV will automatically maintain this target flow")
        ),
        ns0.datatypes.Argument(name="SEM", dataType=mdis_datypes.SEMEnum, valueRank=-1, description=o6.LocalizedText("The selection of which SEM to send the command to")),
        ns0.datatypes.Argument(
            name="ShutdownRequest", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("Boolean indicates that this command is part of a shutdown sequence. ")
        ),
    ],
)
o6.call(nodeId="ns=mdis;i=15375", browseName="ns=mdis;SetFlowRate", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=15376"]))

ns0.vartypes.PropertyType(
    nodeId="ns=mdis;i=15378",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=mdis;i=15377",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="Position", dataType=o6.Float, valueRank=-1, description=o6.LocalizedText("Target position as percent of open. The CIMV will automatically maintain this position")
        ),
        ns0.datatypes.Argument(name="SEM", dataType=mdis_datypes.SEMEnum, valueRank=-1, description=o6.LocalizedText("The selection of which SEM to send the command to")),
        ns0.datatypes.Argument(
            name="ShutdownRequest",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("Boolean indicating if the open or close command should override any interlocks"),
        ),
    ],
)
o6.call(nodeId="ns=mdis;i=15377", browseName="ns=mdis;SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=mdis;i=15378"]))

mdis_objtypes.MDISCounterObjectType(
    nodeId="ns=mdis;i=15382",
    browseName="ns=mdis;<CounterPlaceholder>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15383", browseName="ns=mdis;Count", dataType=ns0.datatypes.Number))],
)
o6.reference(mdis_objtypes.MDISAggregateObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=15382"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=mdis;i=15403",
    browseName="ns=mdis;TargetFlowRate",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15407", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mdis;i=15408", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Float,
)
mdis_objtypes.MDISCIMVObjectType(
    nodeId="ns=mdis;i=15311",
    browseName="ns=mdis;<CIMVPlaceholder>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15312", browseName="ns=mdis;Fault", dataType=o6.Boolean)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15328", browseName="ns=mdis;OperationMode", dataType=mdis_datypes.CIMVOperationModeEnum)),
        o6.hasComponent(o6.ns["ns=mdis;i=15329"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15341", browseName="ns=mdis;Position", dataType=o6.Float)),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15342", browseName="ns=mdis;Moving", dataType=mdis_datypes.CIMVMoveEnum)),
        o6.hasComponent(o6.ns["ns=mdis;i=15373"]),
        o6.hasComponent(o6.ns["ns=mdis;i=15375"]),
        o6.hasComponent(o6.ns["ns=mdis;i=15377"]),
        o6.hasComponent(o6.call(nodeId="ns=mdis;i=15381", browseName="ns=mdis;Abort")),
        o6.hasComponent(o6.ns["ns=mdis;i=15403"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=mdis;i=15409", browseName="ns=mdis;TargetPosition", dataType=o6.Float)),
    ],
)
o6.reference(mdis_objtypes.MDISAggregateObjectType, ns0.reftypes.HasComponent, o6.ns["ns=mdis;i=15311"])


del Any, TYPE_CHECKING, uuid, o6, ns0, mdis_reftypes, mdis_datypes, mdis_vartypes, mdis_objtypes
