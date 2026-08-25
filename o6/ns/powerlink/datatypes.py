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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=powerlink;i=24", browseName="PowerlinkNMTStateEnumeration", description="This DataType is an enumeration that represents the NMT State")
class PowerlinkNMTStateEnumeration(ns0.datatypes.Enumeration):
    NMT_GS_OFF_ = o6.enumfield(0, name="NMT_GS_OFF ")
    NMT_GS_INITIALISING = o6.enumfield(25, name="NMT_GS_INITIALISING")
    NMT_XS_NOT_ACTIVE = o6.enumfield(28, name="NMT_XS_NOT_ACTIVE")
    NMT_XS_PRE_OPERATIONAL_1 = o6.enumfield(29, name="NMT_XS_PRE_OPERATIONAL_1")
    NMT_XS_BASIC_ETHERNET = o6.enumfield(30, name="NMT_XS_BASIC_ETHERNET")
    NMT_GS_RESET_APPLICATION = o6.enumfield(41, name="NMT_GS_RESET_APPLICATION")
    NMT_GS_RESET_COMMUNICATION = o6.enumfield(57, name="NMT_GS_RESET_COMMUNICATION")
    NMT_CS_STOPPED = o6.enumfield(77, name="NMT_CS_STOPPED")
    NMT_XS_PRE_OPERATIONAL_2 = o6.enumfield(93, name="NMT_XS_PRE_OPERATIONAL_2")
    NMT_XS_READY_TO_OPERATE = o6.enumfield(109, name="NMT_XS_READY_TO_OPERATE")
    NMT_GS_RESET_CONFIGURATION = o6.enumfield(121, name="NMT_GS_RESET_CONFIGURATION")
    NMT_XS_OPERATIONAL = o6.enumfield(253, name="NMT_XS_OPERATIONAL")


@o6.datatype(nodeId="ns=powerlink;i=25", browseName="PowerlinkAttribute", description="Represents the POWERLINK entry attributes", defaultEncodingId="ns=powerlink;i=33")
class PowerlinkAttribute(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString


@o6.datatype(nodeId="ns=powerlink;i=26", browseName="ErrorRegisterBits", description="Represents the values of the POWERLINK ErrorRegister", defaultEncodingId="ns=powerlink;i=36")
class ErrorRegisterBits(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString


@o6.datatype(
    nodeId="ns=powerlink;i=27",
    browseName="PowerlinkErrorEntryDataType",
    description="Represents the entries of the POWERLINK Object ERR_History_ADOM (Object 1003h, SubIndex 1..254)",
    defaultEncodingId="ns=powerlink;i=53",
)
class PowerlinkErrorEntryDataType(ns0.datatypes.Structure):
    entryType: o6.UInt16
    errorCode: o6.UInt16
    timeStamp: o6.UInt64
    additionalInformation: o6.UInt64


@o6.enumtype(
    nodeId="ns=powerlink;i=28", browseName="PowerlinkNMTResetCmdEnumeration", description="This DataType is an Enumeration that represents the NMT reset commands for POWERLINK"
)
class PowerlinkNMTResetCmdEnumeration(ns0.datatypes.Enumeration):
    NMT_RESET_NODE = o6.enumfield(40, name="NMTResetNode")
    NMT_RESET_COMMUNICATION = o6.enumfield(41, name="NMTResetCommunication")
    NMT_RESET_CONFIGURATION = o6.enumfield(42, name="NMTResetConfiguration")
    NMT_SW_RESET = o6.enumfield(43, name="NMTSwReset")
    NMT_INVALID_SERVICE = o6.enumfield(255, name="NMTInvalidService")


@o6.datatype(
    nodeId="ns=powerlink;i=29",
    browseName="PowerlinkIpAddressDataType",
    description="Structure DataType PowerlinkIpAddressDataType to represent POWERLINK Objects of the POWERLINK data type IP_ADDRESS",
    defaultEncodingId="ns=powerlink;i=32",
)
class PowerlinkIpAddressDataType(ns0.datatypes.Structure):
    b1: o6.Byte
    b2: o6.Byte
    b3: o6.Byte
    b4: o6.Byte


@o6.datatype(
    nodeId="ns=powerlink;i=30",
    browseName="PowerlinkPDOMappingEntryDataType",
    description="Structure DataType PowerlinkPDOMappingEntryDataType to represent the entries of POWERLINK Objects like PDO_RxCommParam_00h_REC",
    defaultEncodingId="ns=powerlink;i=40",
)
class PowerlinkPDOMappingEntryDataType(ns0.datatypes.Structure):
    length: o6.UInt16
    offset: o6.UInt16
    reserved: o6.Byte
    subIndex: o6.Byte
    index: o6.UInt16


del Any, TYPE_CHECKING, uuid, o6, di, ns0
