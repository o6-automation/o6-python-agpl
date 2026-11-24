# Copyright (c) 2026 o6 Automation GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
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

"""Generated OPC UA cnc namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import datatypes as cnc_datypes
from . import vartypes as cnc_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=cnc;i=1001",
    browseName="ns=cnc;CncComponentType",
    displayName="CncComponentType",
    description="Base component for soft- or hardware elements of a CNC system.",
    isAbstract=True,
)
class CncComponentType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(nodeId="ns=cnc;i=1008", browseName="ns=cnc;CncAxisListType", displayName="CncAxisListType", description="List of CNC axis objects.")
class CncAxisListType(ns0.objtypes.BaseObjectType):
    cncAxis_: CncAxisType | None


o6.reference(CncAxisListType, "i=41", "i=2133")


@o6.objecttype(nodeId="ns=cnc;i=1009", browseName="ns=cnc;CncSpindleListType", displayName="CncSpindleListType", description="List of CNC spindle objects.")
class CncSpindleListType(ns0.objtypes.BaseObjectType):
    cncSpindle_: CncSpindleType | None


o6.reference(CncSpindleListType, "i=41", "i=2133")


@o6.objecttype(nodeId="ns=cnc;i=1010", browseName="ns=cnc;CncChannelListType", displayName="CncChannelListType", description="List of CNC channel objects.")
class CncChannelListType(ns0.objtypes.BaseObjectType):
    cncChannel_: CncChannelType | None


o6.reference(CncChannelListType, "i=41", "i=2133")


@o6.objecttype(nodeId="ns=cnc;i=1011", browseName="ns=cnc;CncMessageType", displayName="CncMessageType", description="Event transmitting simple information messages.")
class CncMessageType(ns0.objtypes.BaseEventType):
    pass


@o6.objecttype(
    nodeId="ns=cnc;i=1003",
    browseName="ns=cnc;CncDriveType",
    displayName="CncDriveType",
    description="Base component for CNC specific drive componentes (e.g. axis or spindle).",
    isAbstract=True,
)
class CncDriveType(CncComponentType):
    actChannel: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6059",
            browseName="ns=cnc;ActChannel",
            description="NodeId of the channel object (CncChannelType) that administrates this drive to expose drive’s channel affiliation.",
            modellingRule="Mandatory",
            dataType=o6.NodeId,
            value=o6.NodeId("i=0"),
            accessLevel=3,
        )
    )
    actLoad: ns0.vartypes.AnalogItemType
    actPower: ns0.vartypes.AnalogItemType
    actTorque: ns0.vartypes.AnalogItemType
    cmdTorque: ns0.vartypes.AnalogItemType
    isInactive: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6200",
            browseName="ns=cnc;IsInactive",
            description="Drive inactive state (true in case of inactive drive, else false).",
            modellingRule="Mandatory",
            dataType=o6.Boolean,
            value=False,
            accessLevel=3,
        )
    )
    isVirtual: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6189",
            browseName="ns=cnc;IsVirtual",
            description="Virtual axis (no hardware present; true in case of virtual axis, else fals).",
            modellingRule="Mandatory",
            dataType=o6.Boolean,
            value=False,
            accessLevel=3,
        )
    )


@o6.objecttype(nodeId="ns=cnc;i=1005", browseName="ns=cnc;CncSpindleType", displayName="CncSpindleType", description="CNC spindle component.")
class CncSpindleType(CncDriveType):
    actGear: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6128", browseName="ns=cnc;ActGear", description="Gear stage actual value.", modellingRule="Mandatory", dataType=o6.UInt32, value=0, accessLevel=3
        )
    )
    actOverride: ns0.vartypes.AnalogItemType
    actSpeed: ns0.vartypes.AnalogItemType
    actStatus: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6135",
            browseName="ns=cnc;ActStatus",
            description="Actual spindle state.",
            modellingRule="Mandatory",
            dataType=cnc_datypes.CncSpindleStatus,
            value=cnc_datypes.CncSpindleStatus.STOPPED,
            accessLevel=3,
        )
    )
    actTurnDirection: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6132",
            browseName="ns=cnc;ActTurnDirection",
            description="Turn direction actual value.",
            modellingRule="Mandatory",
            dataType=cnc_datypes.CncSpindleTurnDirection,
            value=cnc_datypes.CncSpindleTurnDirection.NONE,
            accessLevel=3,
        )
    )
    anglePos: cnc_vartypes.CncPositionVariableType
    cmdGear: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6130", browseName="ns=cnc;CmdGear", description="Gear stage setpoint value.", modellingRule="Mandatory", dataType=o6.UInt32, value=0, accessLevel=3
        )
    )
    cmdOverride: ns0.vartypes.AnalogItemType
    cmdSpeed: ns0.vartypes.AnalogItemType


@o6.objecttype(nodeId="ns=cnc;i=1004", browseName="ns=cnc;CncAxisType", displayName="CncAxisType", description="CNC axis component.")
class CncAxisType(CncDriveType):
    actStatus: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6102",
            browseName="ns=cnc;ActStatus",
            description="Actual axis state.",
            modellingRule="Mandatory",
            dataType=cnc_datypes.CncAxisStatus,
            value=cnc_datypes.CncAxisStatus.IN_POSITION,
            accessLevel=3,
        )
    )
    isReferenced: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6182",
            browseName="ns=cnc;IsReferenced",
            description="Axis reference state (true in case of successfully refereneced axis, else false).",
            modellingRule="Mandatory",
            dataType=o6.Boolean,
            value=False,
            accessLevel=3,
        )
    )
    isRotational: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6211",
            browseName="ns=cnc;IsRotational",
            description="Axis type (true in case of rotational axis, in case of linear type or other false).",
            modellingRule="Mandatory",
            dataType=o6.Boolean,
            value=False,
            accessLevel=3,
        )
    )
    posDirect: cnc_vartypes.CncPositionVariableType
    posIndirect: cnc_vartypes.CncPositionVariableType
    zeroOffset: ns0.vartypes.AnalogItemType


@o6.objecttype(nodeId="ns=cnc;i=1007", browseName="ns=cnc;CncInterfaceType", displayName="CncInterfaceType", description="Entry point to CNC data interface.")
class CncInterfaceType(ns0.objtypes.BaseObjectType):
    cncAxisList: CncAxisListType = o6.hasComponent(
        CncAxisListType(nodeId="ns=cnc;i=5026", browseName="ns=cnc;CncAxisList", description="List of CNC axis objects.", modellingRule="Mandatory")
    )
    cncChannelList: CncChannelListType = o6.hasComponent(
        CncChannelListType(nodeId="ns=cnc;i=5028", browseName="ns=cnc;CncChannelList", description="List of CNC channel objects.", modellingRule="Mandatory")
    )
    cncSpindleList: CncSpindleListType = o6.hasComponent(
        CncSpindleListType(nodeId="ns=cnc;i=5027", browseName="ns=cnc;CncSpindleList", description="List of CNC spindle objects.", modellingRule="Mandatory")
    )
    cncTypeName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=cnc;i=6092", browseName="ns=cnc;CncTypeName", modellingRule="Optional", dataType=o6.String, accessLevel=3)
    )
    fix: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cnc;i=6618",
            browseName="ns=cnc;Fix",
            description="Version of CNC interface considering changes in implementation (Bug Fix).",
            modellingRule="Optional",
            dataType=o6.String,
            value="\n      ",
            accessLevel=3,
        )
    )
    vendorName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cnc;i=6620",
            browseName="ns=cnc;VendorName",
            description="Name of CNC system vendor. Format and content may be chosen by vendor.",
            modellingRule="Mandatory",
            dataType=o6.String,
            value="\n      ",
            accessLevel=3,
        )
    )
    vendorRevision: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cnc;i=6621",
            browseName="ns=cnc;VendorRevision",
            description="Vendor revision of CNC interface. Format and content may be chosen by vendor.",
            modellingRule="Mandatory",
            dataType=o6.String,
            value="\n      ",
            accessLevel=3,
        )
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cnc;i=6616",
            browseName="ns=cnc;Version",
            description="Version of CNC interface - corresponds to version of OPC UA companion standard.",
            modellingRule="Mandatory",
            dataType=o6.String,
            value="\n      ",
            accessLevel=3,
        )
    )


o6.reference(CncInterfaceType, "i=41", CncMessageType)


@o6.objecttype(nodeId="ns=cnc;i=1002", browseName="ns=cnc;CncChannelType", displayName="CncChannelType", description="CNC channel component.")
class CncChannelType(CncComponentType):
    actFeedrate: ns0.vartypes.AnalogItemType
    actGFunctions: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6028",
            browseName="ns=cnc;ActGFunctions",
            description="Array of active G functions; there can be several G functions active at a time (modal and non-modal G functions).",
            modellingRule="Mandatory",
            dataType=o6.UInt32,
            valueRank=1,
            arrayDimensions=[0],
            value=[],
            accessLevel=3,
        )
    )
    actJogIncrement: ns0.vartypes.AnalogItemType
    actMFunctions: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6177",
            browseName="ns=cnc;ActMFunctions",
            description="Array of active M functions: there can be several M functions active at a time (modal and non-modal M functions).",
            modellingRule="Mandatory",
            dataType=o6.UInt32,
            valueRank=1,
            arrayDimensions=[0],
            value=[],
            accessLevel=3,
        )
    )
    actMainProgramFile: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6682",
            browseName="ns=cnc;ActMainProgramFile",
            description="Path of active CNC main program.",
            modellingRule="Mandatory",
            dataType=o6.String,
            value="\n      ",
            accessLevel=3,
        )
    )
    actMainProgramFileOffset: ns0.vartypes.DataItemType | None = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6694",
            browseName="ns=cnc;ActMainProgramFileOffset",
            description="File offset of active CNC main program file.",
            modellingRule="Optional",
            dataType=o6.UInt32,
            value=0,
            accessLevel=3,
        )
    )
    actMainProgramLine: ns0.vartypes.DataItemType | None = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6688",
            browseName="ns=cnc;ActMainProgramLine",
            description="Line number of active CNC main program.",
            modellingRule="Optional",
            dataType=o6.String,
            value="\n      ",
            accessLevel=3,
        )
    )
    actMainProgramName: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6031",
            browseName="ns=cnc;ActMainProgramName",
            description="Name of active CNC main program.",
            modellingRule="Mandatory",
            dataType=o6.String,
            value="\n      ",
            accessLevel=3,
        )
    )
    actModalOffsetFunction: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6029",
            browseName="ns=cnc;ActModalOffsetFunction",
            description="Active zero offset function.",
            modellingRule="Mandatory",
            dataType=o6.UInt32,
            value=0,
            accessLevel=3,
        )
    )
    actOperationMode: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6055",
            browseName="ns=cnc;ActOperationMode",
            description="Channel's active mode of operation.",
            modellingRule="Mandatory",
            dataType=cnc_datypes.CncOperationMode,
            value=cnc_datypes.CncOperationMode.MANUAL,
            accessLevel=3,
        )
    )
    actOverride: ns0.vartypes.AnalogItemType
    actProgramBlock: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6033",
            browseName="ns=cnc;ActProgramBlock",
            description="Block of lines containing the previous, actual and subsequent lines of a CNC part program.",
            modellingRule="Mandatory",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[3],
            value=[],
            accessLevel=3,
        )
    )
    actProgramFile: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6034",
            browseName="ns=cnc;ActProgramFile",
            description="Path of active CNC program file (main or subprogram).",
            modellingRule="Mandatory",
            dataType=o6.String,
            value="\n      ",
            accessLevel=3,
        )
    )
    actProgramFileOffset: ns0.vartypes.DataItemType | None = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6032",
            browseName="ns=cnc;ActProgramFileOffset",
            description="File offset of active CNC program file (main or subprogram).",
            modellingRule="Optional",
            dataType=o6.UInt32,
            value=0,
            accessLevel=3,
        )
    )
    actProgramLine: ns0.vartypes.DataItemType | None = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6047",
            browseName="ns=cnc;ActProgramLine",
            description="Line number of active CNC program (main or subprogram).",
            modellingRule="Optional",
            dataType=o6.String,
            value="\n      ",
            accessLevel=3,
        )
    )
    actProgramName: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6030",
            browseName="ns=cnc;ActProgramName",
            description="Name of active CNC program (main or subprogram).",
            modellingRule="Mandatory",
            dataType=o6.String,
            value="\n      ",
            accessLevel=3,
        )
    )
    actProgramStatus: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6023",
            browseName="ns=cnc;ActProgramStatus",
            description="Active channel program status",
            modellingRule="Mandatory",
            dataType=cnc_datypes.CncChannelProgramStatus,
            value=cnc_datypes.CncChannelProgramStatus.RUNNING,
            accessLevel=3,
        )
    )
    actStatus: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6048",
            browseName="ns=cnc;ActStatus",
            description="Active status of channel.",
            modellingRule="Mandatory",
            dataType=cnc_datypes.CncChannelStatus,
            value=cnc_datypes.CncChannelStatus.RESET,
            accessLevel=3,
        )
    )
    blockMode: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6049",
            browseName="ns=cnc;BlockMode",
            description="Block mode status (true in case of block mode is active, else false).",
            modellingRule="Mandatory",
            dataType=o6.Boolean,
            value=False,
            accessLevel=3,
        )
    )
    cmdFeedrate: ns0.vartypes.AnalogItemType
    cmdOperationMode: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6543",
            browseName="ns=cnc;CmdOperationMode",
            description="Channel’s mode of operation setpoint value.",
            modellingRule="Mandatory",
            dataType=cnc_datypes.CncOperationMode,
            value=cnc_datypes.CncOperationMode.MANUAL,
            accessLevel=3,
        )
    )
    cmdOverride: ns0.vartypes.AnalogItemType
    cncAxis_: CncAxisType | None
    cncSpindle_: CncSpindleType | None
    dryRunFeed: ns0.vartypes.AnalogItemType
    feedHold: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6009",
            browseName="ns=cnc;FeedHold",
            description="Feed status (true in case of feed hold active, else false).",
            modellingRule="Mandatory",
            dataType=o6.Boolean,
            value=False,
            accessLevel=3,
        )
    )
    id: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cnc;i=6016", browseName="ns=cnc;Id", description="Unique numeric channel identifier.", modellingRule="Mandatory", dataType=o6.UInt32, value=0, accessLevel=3
        )
    )
    posTcpBcsA: cnc_vartypes.CncPositionVariableType
    posTcpBcsB: cnc_vartypes.CncPositionVariableType
    posTcpBcsC: cnc_vartypes.CncPositionVariableType
    posTcpBcsX: cnc_vartypes.CncPositionVariableType
    posTcpBcsY: cnc_vartypes.CncPositionVariableType
    posTcpBcsZ: cnc_vartypes.CncPositionVariableType
    posTcpWcsA: cnc_vartypes.CncPositionVariableType
    posTcpWcsB: cnc_vartypes.CncPositionVariableType
    posTcpWcsC: cnc_vartypes.CncPositionVariableType
    posTcpWcsX: cnc_vartypes.CncPositionVariableType
    posTcpWcsY: cnc_vartypes.CncPositionVariableType
    posTcpWcsZ: cnc_vartypes.CncPositionVariableType
    toolId: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=cnc;i=6056",
            browseName="ns=cnc;ToolId",
            description="ID of active tool; returns zero if no tool is present.",
            modellingRule="Mandatory",
            dataType=o6.UInt32,
            value=0,
            accessLevel=3,
        )
    )


o6.reference(CncChannelType, "i=41", "i=2133")
o6.reference(CncChannelType, "i=41", CncMessageType)


@o6.objecttype(nodeId="ns=cnc;i=1006", browseName="ns=cnc;CncAlarmType", displayName="CncAlarmType", description="Event transmitting Alarms within a CNC system.")
class CncAlarmType(ns0.objtypes.DiscreteAlarmType):
    alarmIdentifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cnc;i=6865",
            browseName="ns=cnc;AlarmIdentifier",
            description="Unique alarm number.",
            modellingRule="Mandatory",
            dataType=o6.String,
            value="\n      ",
            accessLevel=3,
        )
    )
    auxParameters: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cnc;i=6862",
            browseName="ns=cnc;AuxParameters",
            description="Array of auxiliary parameter for additional alarm description.",
            modellingRule="Optional",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[0],
            value=[],
            accessLevel=3,
        )
    )
    helpSource: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=cnc;i=6854",
            browseName="ns=cnc;HelpSource",
            description="Additional information to message giving information on how to solve problem that caused the alarm.",
            modellingRule="Optional",
            dataType=o6.String,
            value="\n      ",
            accessLevel=3,
        )
    )


o6.reference(CncInterfaceType, "i=41", CncAlarmType)


del Any, TYPE_CHECKING, uuid, o6, ns0, cnc_datypes, cnc_vartypes
