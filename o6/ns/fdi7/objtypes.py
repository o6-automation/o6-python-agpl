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

"""Generated OPC UA fdi7 namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import datatypes as fdi7_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=fdi7;i=11", browseName="ns=fdi7;CommunicationServerType", displayName="CommunicationServerType")
class CommunicationServerType(di.objtypes.DeviceType):
    methodSet: ns0.objtypes.BaseObjectType
    parameterSet: ns0.objtypes.BaseObjectType | None = o6.hasComponent(
        ns0.objtypes.BaseObjectType(nodeId="ns=fdi7;i=12", browseName="ns=di;ParameterSet", description="Flat list of Parameters")
    )
    subDevices: ns0.objtypes.FolderType = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=fdi7;i=85", browseName="ns=fdi7;SubDevices"))


@o6.objecttype(nodeId="ns=fdi7;i=233", browseName="ns=fdi7;ServerCommunicationServiceType", displayName="ServerCommunicationServiceType", isAbstract=True)
class ServerCommunicationServiceType(di.objtypes.DeviceType):
    methodSet: ns0.objtypes.BaseObjectType


@o6.objecttype(nodeId="ns=fdi7;i=997", browseName="ns=fdi7;ServerCommunicationFFH1ServiceType", displayName="ServerCommunicationFFH1ServiceType")
class ServerCommunicationFFH1ServiceType(ServerCommunicationServiceType):
    methodSet: ns0.objtypes.BaseObjectType


@o6.objecttype(nodeId="ns=fdi7;i=1073", browseName="ns=fdi7;ServerCommunicationFFHSEServiceType", displayName="ServerCommunicationFFHSEServiceType")
class ServerCommunicationFFHSEServiceType(ServerCommunicationServiceType):
    methodSet: ns0.objtypes.BaseObjectType


@o6.objecttype(nodeId="ns=fdi7;i=1149", browseName="ns=fdi7;ServerCommunicationPROFIBUSServiceType", displayName="ServerCommunicationPROFIBUSServiceType")
class ServerCommunicationPROFIBUSServiceType(ServerCommunicationServiceType):
    methodSet: ns0.objtypes.BaseObjectType


@o6.objecttype(nodeId="ns=fdi7;i=1222", browseName="ns=fdi7;ServerCommunicationPROFINETServiceType", displayName="ServerCommunicationPROFINETServiceType")
class ServerCommunicationPROFINETServiceType(ServerCommunicationServiceType):
    methodSet: ns0.objtypes.BaseObjectType


@o6.objecttype(nodeId="ns=fdi7;i=1295", browseName="ns=fdi7;ServerCommunicationHARTServiceType", displayName="ServerCommunicationHARTServiceType")
class ServerCommunicationHARTServiceType(ServerCommunicationServiceType):
    methodSet: ns0.objtypes.BaseObjectType


@o6.objecttype(nodeId="ns=fdi7;i=1371", browseName="ns=fdi7;Foundation_H1", displayName="Foundation_H1")
class Foundation_H1(di.objtypes.ProtocolType):
    pass


@o6.objecttype(nodeId="ns=fdi7;i=1372", browseName="ns=fdi7;Foundation_HSE", displayName="Foundation_HSE")
class Foundation_HSE(di.objtypes.ProtocolType):
    pass


@o6.objecttype(nodeId="ns=fdi7;i=1373", browseName="ns=fdi7;Profibus_DP", displayName="Profibus_DP")
class Profibus_DP(di.objtypes.ProtocolType):
    pass


@o6.objecttype(nodeId="ns=fdi7;i=1374", browseName="ns=fdi7;Profibus_PA", displayName="Profibus_PA")
class Profibus_PA(di.objtypes.ProtocolType):
    pass


@o6.objecttype(nodeId="ns=fdi7;i=1375", browseName="ns=fdi7;Profinet_IO", displayName="Profinet_IO")
class Profinet_IO(di.objtypes.ProtocolType):
    pass


@o6.objecttype(nodeId="ns=fdi7;i=1376", browseName="ns=fdi7;HART", displayName="HART")
class HART(di.objtypes.ProtocolType):
    pass


@o6.objecttype(nodeId="ns=fdi7;i=1377", browseName="ns=fdi7;ISA100_Wireless", displayName="ISA100_Wireless")
class ISA100_Wireless(di.objtypes.ProtocolType):
    pass


@o6.objecttype(nodeId="ns=fdi7;i=1378", browseName="ns=fdi7;GenericProtocol", displayName="GenericProtocol")
class GenericProtocol(di.objtypes.ProtocolType):
    protocolIdentifier: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1379", browseName="ns=fdi7;ProtocolIdentifier", dataType=o6.String))


@o6.objecttype(nodeId="ns=fdi7;i=1380", browseName="ns=fdi7;ConnectionPoint_Foundation_H1", displayName="ConnectionPoint_Foundation_H1")
class ConnectionPoint_Foundation_H1(di.objtypes.ConnectionPointType):
    address: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1421", browseName="ns=fdi7;Address", dataType=o6.Byte))
    ordinalNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1422", browseName="ns=fdi7;OrdinalNumber", dataType=o6.Int32))
    sIFConnection: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1423", browseName="ns=fdi7;SIFConnection", dataType=o6.Boolean))


@o6.objecttype(nodeId="ns=fdi7;i=1424", browseName="ns=fdi7;ConnectionPoint_Foundation_HSE", displayName="ConnectionPoint_Foundation_HSE")
class ConnectionPoint_Foundation_HSE(di.objtypes.ConnectionPointType):
    address: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1465", browseName="ns=fdi7;Address", dataType=o6.Byte, valueRank=1, arrayDimensions=[16])
    )
    ordinalNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1466", browseName="ns=fdi7;OrdinalNumber", dataType=o6.Int32))


@o6.objecttype(nodeId="ns=fdi7;i=1467", browseName="ns=fdi7;ConnectionPoint_Profibus_DP", displayName="ConnectionPoint_Profibus_DP")
class ConnectionPoint_Profibus_DP(di.objtypes.ConnectionPointType):
    address: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1508", browseName="ns=fdi7;Address", dataType=o6.Byte))


@o6.objecttype(nodeId="ns=fdi7;i=1509", browseName="ns=fdi7;ConnectionPoint_Profinet_IO", displayName="ConnectionPoint_Profinet_IO")
class ConnectionPoint_Profinet_IO(di.objtypes.ConnectionPointType):
    dNSNAME: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1552", browseName="ns=fdi7;DNSNAME", dataType=o6.String))
    iPv4: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1551", browseName="ns=fdi7;IPv4", dataType=o6.Byte, valueRank=1, arrayDimensions=[4])
    )
    mAC: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1550", browseName="ns=fdi7;MAC", dataType=o6.Byte, valueRank=1, arrayDimensions=[16])
    )
    vALID: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1553", browseName="ns=fdi7;VALID", dataType=o6.Boolean))


@o6.objecttype(nodeId="ns=fdi7;i=1554", browseName="ns=fdi7;ConnectionPoint_HART_TP5", displayName="ConnectionPoint_HART_TP5")
class ConnectionPoint_HART_TP5(di.objtypes.ConnectionPointType):
    devAddr: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1595", browseName="ns=fdi7;DevAddr", dataType=o6.Byte, valueRank=1, arrayDimensions=[5])
    )
    devMfg: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1596", browseName="ns=fdi7;DevMfg", dataType=o6.UInt16))
    devPollAddr: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1600", browseName="ns=fdi7;DevPollAddr", dataType=o6.Byte))
    devRev: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1598", browseName="ns=fdi7;DevRev", dataType=o6.UInt16))
    devTag: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1599", browseName="ns=fdi7;DevTag", dataType=o6.String))
    devType: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1597", browseName="ns=fdi7;DevType", dataType=o6.UInt16))


@o6.objecttype(nodeId="ns=fdi7;i=1601", browseName="ns=fdi7;ConnectionPoint_HART_TP6", displayName="ConnectionPoint_HART_TP6")
class ConnectionPoint_HART_TP6(di.objtypes.ConnectionPointType):
    devAddr: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1642", browseName="ns=fdi7;DevAddr", dataType=o6.Byte, valueRank=1, arrayDimensions=[5])
    )
    devMfg: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1643", browseName="ns=fdi7;DevMfg", dataType=o6.UInt16))
    devPollAddr: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1647", browseName="ns=fdi7;DevPollAddr", dataType=o6.Byte))
    devRev: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1645", browseName="ns=fdi7;DevRev", dataType=o6.UInt16))
    devTag: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1646", browseName="ns=fdi7;DevTag", dataType=o6.String))
    devType: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1644", browseName="ns=fdi7;DevType", dataType=o6.UInt16))


@o6.objecttype(nodeId="ns=fdi7;i=1648", browseName="ns=fdi7;ConnectionPoint_HART_TP7", displayName="ConnectionPoint_HART_TP7")
class ConnectionPoint_HART_TP7(di.objtypes.ConnectionPointType):
    devAddr: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1689", browseName="ns=fdi7;DevAddr", dataType=o6.Byte, valueRank=1, arrayDimensions=[5])
    )
    devMfg: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1690", browseName="ns=fdi7;DevMfg", dataType=o6.UInt16))
    devPollAddr: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1694", browseName="ns=fdi7;DevPollAddr", dataType=o6.Byte))
    devRev: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1692", browseName="ns=fdi7;DevRev", dataType=o6.UInt16))
    devTag: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1693", browseName="ns=fdi7;DevTag", dataType=o6.String))
    devType: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1691", browseName="ns=fdi7;DevType", dataType=o6.UInt16))


@o6.objecttype(nodeId="ns=fdi7;i=1695", browseName="ns=fdi7;ConnectionPoint_ISA100_Wireless", displayName="ConnectionPoint_ISA100_Wireless")
class ConnectionPoint_ISA100_Wireless(di.objtypes.ConnectionPointType):
    devMfg: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1737", browseName="ns=fdi7;DevMfg", dataType=o6.UInt32))
    devPollAddr: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1741", browseName="ns=fdi7;DevPollAddr", dataType=o6.Byte))
    devRev: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1739", browseName="ns=fdi7;DevRev", dataType=o6.UInt16))
    devTag: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1740", browseName="ns=fdi7;DevTag", dataType=o6.String))
    devType: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1738", browseName="ns=fdi7;DevType", dataType=o6.UInt16))
    iPAddress: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1736", browseName="ns=fdi7;IPAddress", dataType=o6.ByteString))


@o6.objecttype(nodeId="ns=fdi7;i=1742", browseName="ns=fdi7;GenericConnectionPoint", displayName="GenericConnectionPoint")
class GenericConnectionPoint(di.objtypes.ConnectionPointType):
    address: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1783", browseName="ns=fdi7;Address", dataType=o6.ByteString))
    protocolIdentifier: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1784", browseName="ns=fdi7;ProtocolIdentifier", dataType=o6.String))


@o6.objecttype(nodeId="ns=fdi7;i=2057", browseName="ns=fdi7;ServerCommunicationISA100_WirelessServiceType", displayName="ServerCommunicationISA100_WirelessServiceType")
class ServerCommunicationISA100_WirelessServiceType(ServerCommunicationServiceType):
    methodSet: ns0.objtypes.BaseObjectType


@o6.objecttype(nodeId="ns=fdi7;i=2133", browseName="ns=fdi7;ServerCommunicationGENERICServiceType", displayName="ServerCommunicationGENERICServiceType")
class ServerCommunicationGENERICServiceType(ServerCommunicationServiceType):
    methodSet: ns0.objtypes.BaseObjectType


@o6.objecttype(nodeId="ns=fdi7;i=93", browseName="ns=fdi7;ServerCommunicationDeviceType", displayName="ServerCommunicationDeviceType", isAbstract=True)
class ServerCommunicationDeviceType(di.objtypes.DeviceType):
    listOfCommunicationProfiles: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=15001", browseName="ns=fdi7;ListOfCommunicationProfiles", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    methodSet: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=fdi7;i=324", browseName="ns=fdi7;ServerCommunicationFFH1DeviceType", displayName="ServerCommunicationFFH1DeviceType")
class ServerCommunicationFFH1DeviceType(ServerCommunicationDeviceType):
    methodSet: ns0.objtypes.BaseObjectType | None
    serviceProvider: ServerCommunicationFFH1ServiceType


@o6.objecttype(nodeId="ns=fdi7;i=452", browseName="ns=fdi7;ServerCommunicationFFHSEDeviceType", displayName="ServerCommunicationFFHSEDeviceType")
class ServerCommunicationFFHSEDeviceType(ServerCommunicationDeviceType):
    methodSet: ns0.objtypes.BaseObjectType | None
    serviceProvider: ServerCommunicationFFHSEServiceType


@o6.objecttype(nodeId="ns=fdi7;i=580", browseName="ns=fdi7;ServerCommunicationPROFIBUSDeviceType", displayName="ServerCommunicationPROFIBUSDeviceType")
class ServerCommunicationPROFIBUSDeviceType(ServerCommunicationDeviceType):
    methodSet: ns0.objtypes.BaseObjectType | None
    serviceProvider: ServerCommunicationPROFIBUSServiceType


@o6.objecttype(nodeId="ns=fdi7;i=705", browseName="ns=fdi7;ServerCommunicationPROFINETDeviceType", displayName="ServerCommunicationPROFINETDeviceType")
class ServerCommunicationPROFINETDeviceType(ServerCommunicationDeviceType):
    methodSet: ns0.objtypes.BaseObjectType | None
    serviceProvider: ServerCommunicationPROFINETServiceType


@o6.objecttype(nodeId="ns=fdi7;i=830", browseName="ns=fdi7;ServerCommunicationHARType", displayName="ServerCommunicationHARType")
class ServerCommunicationHARType(ServerCommunicationDeviceType):
    methodSet: ns0.objtypes.BaseObjectType | None
    serviceProvider: ServerCommunicationHARTServiceType


@o6.objecttype(nodeId="ns=fdi7;i=1788", browseName="ns=fdi7;ServerCommunicationISA100_WirelessDeviceType", displayName="ServerCommunicationISA100_WirelessDeviceType")
class ServerCommunicationISA100_WirelessDeviceType(ServerCommunicationDeviceType):
    serviceProvider: ServerCommunicationISA100_WirelessServiceType


@o6.objecttype(nodeId="ns=fdi7;i=1913", browseName="ns=fdi7;ServerCommunicationGENERICDeviceType", displayName="ServerCommunicationGENERICDeviceType")
class ServerCommunicationGENERICDeviceType(ServerCommunicationDeviceType):
    methodSet: ns0.objtypes.BaseObjectType | None
    protocolIdentifier: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=fdi7;i=1987", browseName="ns=fdi7;ProtocolIdentifier", dataType=o6.String))
    serviceProvider: ServerCommunicationGENERICServiceType


del Any, TYPE_CHECKING, uuid, o6, di, ns0, fdi7_datypes
