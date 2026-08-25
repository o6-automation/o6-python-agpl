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

"""Generated OPC UA powerlink namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import datatypes as powerlink_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(
    nodeId="ns=powerlink;i=7",
    browseName="ns=powerlink;PowerlinkRecordType",
    displayName="PowerlinkRecordType",
    description="represents POWERLINK Objects of the type RECORD",
    isAbstract=True,
    dataType=o6.Byte,
    value=0,
)
class PowerlinkRecordType(ns0.vartypes.BaseDataVariableType):
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=85", browseName="ns=powerlink;Index", description="Index of the object in the POWERLINK Object Dictionary", dataType=o6.UInt16, value=0
        )
    )
    numberOfEntries: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=86", browseName="ns=powerlink;NumberOfEntries", description="SubIndex 0 of the POWERLINK Object", dataType=o6.Byte, value=0
        )
    )


@o6.variabletype(
    nodeId="ns=powerlink;i=14",
    browseName="ns=powerlink;NMT_ParameterStorage_Type",
    displayName="NMT_ParameterStorage_Type",
    description="Variable Type to represent the POWERLINK Record NMT_ParameterStorage_TYPE",
)
class NMT_ParameterStorage_Type(PowerlinkRecordType):
    allParam_U32: PowerlinkVariableType
    applicationParam_U32: PowerlinkVariableType | None
    communicationParam_U32: PowerlinkVariableType | None
    langleManufacturerParam_XXh_U32Rangle: PowerlinkVariableType | None


@o6.variabletype(
    nodeId="ns=powerlink;i=8", browseName="ns=powerlink;PowerlinkVariableType", displayName="PowerlinkVariableType", description="represents POWERLINK Objects of the type VAR"
)
class PowerlinkVariableType(ns0.vartypes.BaseDataVariableType):
    defaultValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powerlink;i=280", browseName="ns=powerlink;DefaultValue", description="Default value of POWERLINK Object")
    )
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=277", browseName="ns=powerlink;Index", description="Index of the object in the POWERLINK Object Dictionary", dataType=o6.UInt16, value=0
        )
    )
    powerlinkAttributes: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=93",
            browseName="ns=powerlink;PowerlinkAttributes",
            description="provides the information of the XML-Attribute ‘accessType’ from the POWERLINK XML Device Description",
            dataType=powerlink_datypes.PowerlinkAttribute,
            value=powerlink_datypes.PowerlinkAttribute(value=b"\x00\x00", validBits=b"\x80\x03"),
        )
    )
    range: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=279",
            browseName="ns=powerlink;Range",
            description="Value range of the POWERLINK Object",
            dataType=ns0.datatypes.Range,
            value=ns0.datatypes.Range(low=0.0, high=0.0),
        )
    )
    subIndex: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=278", browseName="ns=powerlink;SubIndex", description="SubIndex of the object in the POWERLINK Object Dictionary", dataType=o6.Byte, value=0
        )
    )


@o6.variabletype(
    nodeId="ns=powerlink;i=22",
    browseName="ns=powerlink;DIA_ERRStatistics_Type",
    displayName="DIA_ERRStatistics_Type",
    description="Variable Type to represent the POWERLINK Record DIA_ERRStatistics_TYPE",
    dataType=o6.Byte,
)
class DIA_ERRStatistics_Type(PowerlinkRecordType):
    emergencyQueueOverflow_U32: PowerlinkVariableType | None
    emergencyQueueWrite_U32: PowerlinkVariableType | None
    exceptionNewEdge_U32: PowerlinkVariableType | None
    exceptionResetEdgePos_U32: PowerlinkVariableType | None
    historyEntryWrite_U32: PowerlinkVariableType | None
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=2494", browseName="ns=powerlink;Index", description="Index of the object in the POWERLINK Object Dictionary", dataType=o6.UInt16, value=4354
        )
    )
    numberOfEntries: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=2495", browseName="ns=powerlink;NumberOfEntries", description="SubIndex 0 of the POWERLINK Object", dataType=o6.Byte, value=7
        )
    )
    staticErrorBitFieldChanged_U32: PowerlinkVariableType | None
    statusEntryChanged_U32: PowerlinkVariableType | None


@o6.variabletype(
    nodeId="ns=powerlink;i=21",
    browseName="ns=powerlink;DIA_NMTTelegrCount_Type",
    displayName="DIA_NMTTelegrCount_Type",
    description="Variable Type to represent the POWERLINK Record DIA_NMTTelegrCount_TYPE",
    dataType=o6.Byte,
)
class DIA_NMTTelegrCount_Type(PowerlinkRecordType):
    asyncRx_U32: PowerlinkVariableType | None
    asyncTx_U32: PowerlinkVariableType | None
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=2496", browseName="ns=powerlink;Index", description="Index of the object in the POWERLINK Object Dictionary", dataType=o6.UInt16, value=4353
        )
    )
    isochrCyc_U32: PowerlinkVariableType
    isochrRx_U32: PowerlinkVariableType | None
    isochrTx_U32: PowerlinkVariableType | None
    numberOfEntries: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=2497", browseName="ns=powerlink;NumberOfEntries", description="SubIndex 0 of the POWERLINK Object", dataType=o6.Byte, value=8
        )
    )
    sdoRx_U32: PowerlinkVariableType | None
    sdoTx_U32: PowerlinkVariableType | None
    status_U32: PowerlinkVariableType | None


@o6.variabletype(
    nodeId="ns=powerlink;i=20",
    browseName="ns=powerlink;DLL_ErrorCntRec_Type",
    displayName="DLL_ErrorCntRec_Type",
    description="Variable Type to represent the POWERLINK Record DLL_ErrorCntRec_TYPE",
    dataType=o6.Byte,
)
class DLL_ErrorCntRec_Type(PowerlinkRecordType):
    cumulativeCnt_U32: PowerlinkVariableType
    numberOfEntries: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=2512", browseName="ns=powerlink;NumberOfEntries", description="SubIndex 0 of the POWERLINK Object", dataType=o6.Byte, value=3
        )
    )
    thresholdCnt_U32: PowerlinkVariableType | None
    threshold_U32: PowerlinkVariableType | None


@o6.variabletype(
    nodeId="ns=powerlink;i=19",
    browseName="ns=powerlink;IDENTITY_Type",
    displayName="IDENTITY_Type",
    description="Variable Type to represent the POWERLINK Record IDENTITY",
    dataType=o6.Byte,
    value=0,
)
class IDENTITY_Type(PowerlinkRecordType):
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=2586", browseName="ns=powerlink;Index", description="Index of the object in the POWERLINK Object Dictionary", dataType=o6.UInt16, value=4120
        )
    )
    numberOfEntries: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=2587", browseName="ns=powerlink;NumberOfEntries", description="SubIndex 0 of the POWERLINK Object", dataType=o6.Byte, value=4
        )
    )
    productCode_U32: PowerlinkVariableType | None
    revisionNo_U32: PowerlinkVariableType | None
    serialNo_U32: PowerlinkVariableType | None
    vendorId_U32: PowerlinkVariableType


@o6.variabletype(
    nodeId="ns=powerlink;i=18",
    browseName="ns=powerlink;INP_ProcessImage_Type",
    displayName="INP_ProcessImage_Type",
    description="Variable Type to represent the POWERLINK Record INP_ProcessImage_TYPE",
    dataType=o6.Byte,
)
class INP_ProcessImage_Type(PowerlinkRecordType):
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=2624", browseName="ns=powerlink;Index", description="Index of the object in the POWERLINK Object Dictionary", dataType=o6.UInt16, value=8048
        )
    )
    numberOfEntries: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=2625", browseName="ns=powerlink;NumberOfEntries", description="SubIndex 0 of the POWERLINK Object", dataType=o6.Byte, value=2
        )
    )
    processImageDomain_DOM: PowerlinkVariableType
    selectedRange_U32: PowerlinkVariableType


@o6.variabletype(
    nodeId="ns=powerlink;i=16",
    browseName="ns=powerlink;NMT_BootTime_Type",
    displayName="NMT_BootTime_Type",
    description="Variable Type to represent the POWERLINK Record NMT_BootTime_TYPE",
    dataType=o6.Byte,
)
class NMT_BootTime_Type(PowerlinkRecordType):
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=2630", browseName="ns=powerlink;Index", description="Index of the object in the POWERLINK Object Dictionary", dataType=o6.UInt16, value=8073
        )
    )
    mNConfigurationTimeout_U32: PowerlinkVariableType | None
    mNIdentificationTimeout_U32: PowerlinkVariableType | None
    mNSoftwareTimeout_U32: PowerlinkVariableType | None
    mNStartCNTimeout_U32: PowerlinkVariableType | None
    mNSwitchOverCycleDivider_U32: PowerlinkVariableType | None
    mNSwitchOverDelay_U32: PowerlinkVariableType | None
    mNSwitchOverPriority_U32: PowerlinkVariableType | None
    mNTimeoutPreOp1_U32: PowerlinkVariableType
    mNTimeoutPreOp2_U32: PowerlinkVariableType
    mNTimeoutReadyToOp_U32: PowerlinkVariableType
    mNWaitNotAct_U32: PowerlinkVariableType
    mNWaitPreOp1_U32: PowerlinkVariableType | None
    numberOfEntries: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=2631", browseName="ns=powerlink;NumberOfEntries", description="SubIndex 0 of the POWERLINK Object", dataType=o6.Byte, value=12
        )
    )


@o6.variabletype(
    nodeId="ns=powerlink;i=11",
    browseName="ns=powerlink;PowerlinkArrayType",
    displayName="PowerlinkArrayType",
    description="represents POWERLINK Objects of the type ARRAY",
    valueRank=o6.ValueRank.ARRAY_1D,
)
class PowerlinkArrayType(ns0.vartypes.BaseDataVariableType):
    defaultValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powerlink;i=2725", browseName="ns=powerlink;DefaultValue", description="Default value of array elements")
    )
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=99", browseName="ns=powerlink;Index", description="Index of the object in the POWERLINK Object Dictionary", dataType=o6.UInt16, value=0
        )
    )
    numberOfEntries: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=100", browseName="ns=powerlink;NumberOfEntries", description="SubIndex 0 of the POWERLINK Object", dataType=o6.Byte, value=0, accessLevel=3
        )
    )
    powerlinkAttributes: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=101",
            browseName="ns=powerlink;PowerlinkAttributes",
            description="provides the information of the XML-Attribute ‘accessType’ from the POWERLINK XML Device Description",
            dataType=powerlink_datypes.PowerlinkAttribute,
            value=powerlink_datypes.PowerlinkAttribute(value=b"\x00\x00", validBits=b"\x80\x03"),
        )
    )
    range: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=2726",
            browseName="ns=powerlink;Range",
            description="Value range of the array elements",
            dataType=ns0.datatypes.Range,
            value=ns0.datatypes.Range(low=0.0, high=0.0),
            accessLevel=3,
        )
    )


@o6.variabletype(
    nodeId="ns=powerlink;i=17",
    browseName="ns=powerlink;NMT_CycleTiming_Type",
    displayName="NMT_CycleTiming_Type",
    description="Variable Type to represent the POWERLINK Record NMT_CycleTiming_TYPE",
    dataType=o6.Byte,
)
class NMT_CycleTiming_Type(PowerlinkRecordType):
    aSndMaxLatency_U32: PowerlinkVariableType | None
    asyncMTU_U16: PowerlinkVariableType
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=2732", browseName="ns=powerlink;Index", description="Index of the object in the POWERLINK Object Dictionary", dataType=o6.UInt16, value=8088
        )
    )
    isochrRxMaxPayload_U16: PowerlinkVariableType
    isochrTxMaxPayload_U16: PowerlinkVariableType
    leaseTime_U32: PowerlinkVariableType | None
    multiplCycleCnt_U8: PowerlinkVariableType
    numberOfEntries: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=2733", browseName="ns=powerlink;NumberOfEntries", description="SubIndex 0 of the POWERLINK Object", dataType=o6.Byte, value=15
        )
    )
    pReqActPayloadLimit_U16: PowerlinkVariableType | None
    pResActPayloadLimit_U16: PowerlinkVariableType | None
    pResMaxLatency_U32: PowerlinkVariableType | None
    pResMode_U8: PowerlinkVariableType | None
    pResTimeFirst_U32: PowerlinkVariableType | None
    pResTimeSecond_U32: PowerlinkVariableType | None
    prescaler_U16: PowerlinkVariableType | None
    syncMNDelayFirst_U32: PowerlinkVariableType | None
    syncMNDelaySecond_U32: PowerlinkVariableType | None


@o6.variabletype(
    nodeId="ns=powerlink;i=9",
    browseName="ns=powerlink;NMT_EPLNodeID_Type",
    displayName="NMT_EPLNodeID_Type",
    description="Variable Type to represent the POWERLINK Record NMT_EPLNodeID_TYPE",
    dataType=o6.Byte,
)
class NMT_EPLNodeID_Type(PowerlinkRecordType):
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=2898", browseName="ns=powerlink;Index", description="Index of the object in the POWERLINK Object Dictionary", dataType=o6.UInt16, value=8083
        )
    )
    nodeIDByHW_BOOL: PowerlinkVariableType
    nodeID_U8: PowerlinkVariableType
    numberOfEntries: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=2899", browseName="ns=powerlink;NumberOfEntries", description="SubIndex 0 of the POWERLINK Object", dataType=o6.Byte, value=3
        )
    )
    sWNodeID_U8: PowerlinkVariableType | None


@o6.variabletype(
    nodeId="ns=powerlink;i=12",
    browseName="ns=powerlink;NWL_IpAddrTable_Type",
    displayName="NWL_IpAddrTable_Type",
    description="Variable Type to represent the POWERLINK Record NWL_IpAddrTable_TYPE",
    dataType=o6.Byte,
)
class NWL_IpAddrTable_Type(PowerlinkRecordType):
    addr_IPAD: PowerlinkVariableType
    defaultGateway_IPAD: PowerlinkVariableType
    ifIndex_U16: PowerlinkVariableType
    netMask_IPAD: PowerlinkVariableType
    numberOfEntries: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=2963", browseName="ns=powerlink;NumberOfEntries", description="SubIndex 0 of the POWERLINK Object", dataType=o6.Byte, value=5
        )
    )
    reasmMaxSize_U16: PowerlinkVariableType


@o6.variabletype(
    nodeId="ns=powerlink;i=10",
    browseName="ns=powerlink;PDO_CommParamRecord_Type",
    displayName="PDO_CommParamRecord_Type",
    description="Variable Type to represent the POWERLINK Record PDO_CommParamRecord_TYPE",
    dataType=o6.Byte,
)
class PDO_CommParamRecord_Type(PowerlinkRecordType):
    mappingVersion_U8: PowerlinkVariableType
    nodeID_U8: PowerlinkVariableType
    numberOfEntries: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=2970", browseName="ns=powerlink;NumberOfEntries", description="SubIndex 0 of the POWERLINK Object", dataType=o6.Byte, value=2
        )
    )


@o6.variabletype(
    nodeId="ns=powerlink;i=13",
    browseName="ns=powerlink;NMT_RequestCmd_Type",
    displayName="NMT_RequestCmd_Type",
    description="Variable Type to represent the POWERLINK Record NMT_RequestCmd_TYPE",
    dataType=o6.Byte,
)
class NMT_RequestCmd_Type(PowerlinkRecordType):
    cmdData_DOM: PowerlinkVariableType | None
    cmdID_U8: PowerlinkVariableType
    cmdTarget_U8: PowerlinkVariableType
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=3069", browseName="ns=powerlink;Index", description="Index of the object in the POWERLINK Object Dictionary", dataType=o6.UInt16, value=8095
        )
    )
    numberOfEntries: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=3070", browseName="ns=powerlink;NumberOfEntries", description="SubIndex 0 of the POWERLINK Object", dataType=o6.Byte, value=4
        )
    )
    release_BOOL: PowerlinkVariableType


@o6.variabletype(
    nodeId="ns=powerlink;i=15",
    browseName="ns=powerlink;NMT_InterfaceGroup_Type",
    displayName="NMT_InterfaceGroup_Type",
    description="Variable Type to represent the POWERLINK Record NMT_InterfaceGroup_Xh_TYPE",
    dataType=o6.Byte,
    value=0,
)
class NMT_InterfaceGroup_Type(PowerlinkRecordType):
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=3180", browseName="ns=powerlink;Index", description="Index of the object in the POWERLINK Object Dictionary", dataType=o6.UInt16, value=4144
        )
    )
    interfaceAdminState_U8: PowerlinkVariableType
    interfaceDescription_VSTR: PowerlinkVariableType
    interfaceIndex_U16: PowerlinkVariableType
    interfaceMtu_U16: PowerlinkVariableType
    interfaceName_VSTR: PowerlinkVariableType
    interfaceOperStatus_U8: PowerlinkVariableType
    interfacePhysAddress_OSTR: PowerlinkVariableType
    interfaceType_U8: PowerlinkVariableType
    numberOfEntries: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=2916", browseName="ns=powerlink;NumberOfEntries", description="SubIndex 0 of the POWERLINK Object", dataType=o6.Byte, value=10
        )
    )
    portEnableMask_U64: PowerlinkVariableType | None
    valid_BOOL: PowerlinkVariableType


@o6.variabletype(
    nodeId="ns=powerlink;i=23",
    browseName="ns=powerlink;NMT_MNCycleTiming_Type",
    displayName="NMT_MNCycleTiming_Type",
    description="Variable Type to represent the POWERLINK Record NMT_MNCycleTiming_TYPE",
    dataType=o6.Byte,
)
class NMT_MNCycleTiming_Type(PowerlinkRecordType):
    aSndMaxNumber: PowerlinkVariableType | None
    asyncSlotTimeout_U32: PowerlinkVariableType | None
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=3209", browseName="ns=powerlink;Index", description="Index of the object in the POWERLINK Object Dictionary", dataType=o6.UInt16, value=8074
        )
    )
    minRedCycleTime_U32: PowerlinkVariableType | None
    numberOfEntries: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powerlink;i=3210", browseName="ns=powerlink;NumberOfEntries", description="SubIndex 0 of the POWERLINK Object", dataType=o6.Byte, value=4
        )
    )
    waitSoCPReq_U32: PowerlinkVariableType


del Any, TYPE_CHECKING, uuid, o6, di, ns0, powerlink_datypes
