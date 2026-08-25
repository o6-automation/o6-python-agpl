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

"""Generated OPC UA safety namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import datatypes as safety_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=safety;i=1004", browseName="ns=safety;SafetyObjectsType", displayName="SafetyObjectsType", description="Base type of all safety objects", isAbstract=True)
class SafetyObjectsType(ns0.objtypes.BaseObjectType):
    pass


ns0.vartypes.BaseDataVariableType(
    nodeId="ns=safety;i=6029",
    browseName="ns=safety;<RequestSPDU>",
    modellingRule="MandatoryPlaceholder",
    dataType=safety_datypes.RequestSPDUDataType,
    value=safety_datypes.RequestSPDUDataType(inSafetyConsumerID=0, inMonitoringNumber=0, inFlags=safety_datypes.InFlagsType(0)),
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=safety;i=6030", browseName="ns=safety;<ResponseSPDU>", modellingRule="MandatoryPlaceholder", dataType=safety_datypes.ResponseSPDUDataType
)


@o6.objecttype(nodeId="ns=safety;i=1007", browseName="ns=safety;SafetyPDUsType", displayName="SafetyPDUsType")
class SafetyPDUsType(ns0.objtypes.BaseObjectType):
    langleRequestSPDURangle: ns0.vartypes.BaseDataVariableType = o6.hasComponent(o6.ns["ns=safety;i=6029"])
    langleResponseSPDURangle: ns0.vartypes.BaseDataVariableType = o6.hasComponent(o6.ns["ns=safety;i=6030"])


SafetyPDUsType(nodeId="ns=safety;i=5000", browseName="ns=safety;SafetyPDUs")
o6.reference(o6.ns["ns=safety;i=5000"], "i=47", o6.ns["ns=safety;i=6029"])
o6.reference(o6.ns["ns=safety;i=5000"], "i=47", o6.ns["ns=safety;i=6030"])
SafetyPDUsType(nodeId="ns=safety;i=5007", browseName="ns=safety;SafetyPDUs")
o6.reference(o6.ns["ns=safety;i=5007"], "i=47", o6.ns["ns=safety;i=6029"])
o6.reference(o6.ns["ns=safety;i=5007"], "i=47", o6.ns["ns=safety;i=6030"])


@o6.objecttype(nodeId="ns=safety;i=1005", browseName="ns=safety;SafetyConsumerType", displayName="SafetyConsumerType")
class SafetyConsumerType(SafetyObjectsType):
    parameters: SafetyConsumerParametersType
    safetyPDUs: SafetyPDUsType | None = o6.hasComponent(o6.ns["ns=safety;i=5007"])


@o6.objecttype(
    nodeId="ns=safety;i=1002",
    browseName="ns=safety;SafetyProviderParametersType",
    displayName="SafetyProviderParametersType",
    description="Safety parameters for the SafetyProvider",
)
class SafetyProviderParametersType(ns0.objtypes.BaseObjectType):
    safetyBaseIDActive: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=safety;i=6000", browseName="ns=safety;SafetyBaseIDActive", description="Currently active Base-ID of the SafetyProvider", dataType=o6.Guid
        )
    )
    safetyBaseIDConfigured: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=safety;i=6005", browseName="ns=safety;SafetyBaseIDConfigured", description="Base-ID of the SafetyProvider as configured via the SPI", dataType=o6.Guid
        )
    )
    safetyProviderDelay: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=safety;i=6002",
            browseName="ns=safety;SafetyProviderDelay",
            description="SafetyProviderDelay is the maximum time at the SafetyProvider from receiving the RequestSPDU to start the transmission of ResponseSPDU",
            dataType=o6.UInt32,
        )
    )
    safetyProviderIDActive: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=safety;i=6062", browseName="ns=safety;SafetyProviderIDActive", description="Currently active Provider-ID of the SafetyProvider", dataType=o6.UInt32
        )
    )
    safetyProviderIDConfigured: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=safety;i=6006",
            browseName="ns=safety;SafetyProviderIDConfigured",
            description="Provider-ID of the SafetyProvider as configured via the SPI",
            dataType=o6.UInt32,
        )
    )
    safetyProviderLevel: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=safety;i=6001",
            browseName="ns=safety;SafetyProviderLevel",
            description="The maximal SIL the SafetyProvider implementation (hardware & software) is capable of",
            dataType=o6.Byte,
        )
    )
    safetyPubSubImplemented: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=safety;i=6065",
            browseName="ns=safety;SafetyPubSubImplemented",
            description="Indicates whether the SafetyProvider supports OPC UA PubSub communication",
            dataType=o6.Boolean,
        )
    )
    safetyServerImplemented: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=safety;i=6064",
            browseName="ns=safety;SafetyServerImplemented",
            description="Indicates whether the SafetyProvider supports OPC UA Client/Server communication",
            dataType=o6.Boolean,
        )
    )
    safetyStructureIdentifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=safety;i=6004", browseName="ns=safety;SafetyStructureIdentifier", description="Identifier of the structure type", dataType=o6.String)
    )
    safetyStructureSignature: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=safety;i=6039", browseName="ns=safety;SafetyStructureSignature", dataType=o6.UInt32)
    )
    safetyStructureSignatureVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=safety;i=6003",
            browseName="ns=safety;SafetyStructureSignatureVersion",
            description="Version of the algorithm for calculating the StructureSignature",
            dataType=o6.UInt16,
        )
    )


@o6.objecttype(
    nodeId="ns=safety;i=1006",
    browseName="ns=safety;SafetyConsumerParametersType",
    displayName="SafetyConsumerParametersType",
    description="Safety parameters for the SafetyProvider",
)
class SafetyConsumerParametersType(ns0.objtypes.BaseObjectType):
    safetyBaseIDActive: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=safety;i=6063", browseName="ns=safety;SafetyBaseIDActive", dataType=o6.Guid)
    )
    safetyBaseIDConfigured: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=safety;i=6042", browseName="ns=safety;SafetyBaseIDConfigured", dataType=o6.Guid)
    )
    safetyClientImplemented: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=safety;i=6068",
            browseName="ns=safety;SafetyClientImplemented",
            description="Indicates whether the SafetyClient supports OPC UA Client/Server communication",
            dataType=o6.Boolean,
        )
    )
    safetyConsumerIDActive: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=safety;i=6067", browseName="ns=safety;SafetyConsumerIDActive", dataType=o6.UInt32)
    )
    safetyConsumerIDConfigured: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=safety;i=6043", browseName="ns=safety;SafetyConsumerIDConfigured", dataType=o6.UInt32)
    )
    safetyConsumerTimeout: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=safety;i=6048", browseName="ns=safety;SafetyConsumerTimeout", dataType=o6.UInt32)
    )
    safetyErrorIntervalLimit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=safety;i=6050", browseName="ns=safety;SafetyErrorIntervalLimit", dataType=o6.UInt16)
    )
    safetyOperatorAckNecessary: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=safety;i=6049", browseName="ns=safety;SafetyOperatorAckNecessary", dataType=o6.Boolean)
    )
    safetyProviderIDActive: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=safety;i=6066", browseName="ns=safety;SafetyProviderIDActive", dataType=o6.UInt32)
    )
    safetyProviderIDConfigured: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=safety;i=6041", browseName="ns=safety;SafetyProviderIDConfigured", dataType=o6.UInt32)
    )
    safetyProviderLevel: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=safety;i=6044", browseName="ns=safety;SafetyProviderLevel", dataType=o6.Byte)
    )
    safetyPubSubImplemented: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=safety;i=6069",
            browseName="ns=safety;SafetyPubSubImplemented",
            description="Indicates whether the SafetyConsumer supports OPC UA PubSub communication",
            dataType=o6.Boolean,
        )
    )
    safetyStructureIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=safety;i=6047", browseName="ns=safety;SafetyStructureIdentifier", dataType=o6.String)
    )
    safetyStructureSignature: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=safety;i=6045", browseName="ns=safety;SafetyStructureSignature", dataType=o6.UInt32)
    )
    safetyStructureSignatureVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=safety;i=6046", browseName="ns=safety;SafetyStructureSignatureVersion", dataType=o6.UInt16)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=safety;i=6007",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=safety;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="InSafetyConsumerID", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("SafetyConsumer identifier")),
        ns0.datatypes.Argument(name="InMonitoringNumber", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("Monitoring Number of the RequestSPDU")),
        ns0.datatypes.Argument(
            name="InFlags", dataType=o6.NodeId("ns=safety;i=3005"), valueRank=-1, description=o6.LocalizedText("Byte with non-safety flags from SafetyConsumer")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=safety;i=6008",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=safety;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[9],
    value=[
        ns0.datatypes.Argument(name="OutSafetyData", dataType=ns0.datatypes.Structure, valueRank=-1, description=o6.LocalizedText("Safety Data")),
        ns0.datatypes.Argument(name="OutFlags", dataType=o6.NodeId("ns=safety;i=3006"), valueRank=-1, description=o6.LocalizedText("Byte with safety flags from SafetyProvider")),
        ns0.datatypes.Argument(name="OutSPDU_ID_1", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("Safety PDU Identifier Part1")),
        ns0.datatypes.Argument(name="OutSPDU_ID_2", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("Safety PDU Identifier Part2")),
        ns0.datatypes.Argument(name="OutSPDU_ID_3", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("Safety PDU Identifier Part3")),
        ns0.datatypes.Argument(name="OutSafetyConsumerID", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("SafetyConsumer identifier")),
        ns0.datatypes.Argument(name="OutMonitoringNumber", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("Monitoring Number of the ResponseSPDU")),
        ns0.datatypes.Argument(name="OutCRC", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("CRC-checksum over the ResponseSPDU")),
        ns0.datatypes.Argument(name="OutNonSafetyData", dataType=ns0.datatypes.Structure, valueRank=-1, description=o6.LocalizedText("Non-safe data")),
    ],
)
o6.call(nodeId="ns=safety;i=7001", browseName="ns=safety;ReadSafetyData", inputArgs=o6.hasProperty(o6.ns["ns=safety;i=6007"]), outputArgs=o6.hasProperty(o6.ns["ns=safety;i=6008"]))

ns0.vartypes.PropertyType(
    nodeId="ns=safety;i=6009",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=safety;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[12],
    value=[
        ns0.datatypes.Argument(name="InSafetyConsumerID", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("SafetyConsumer identifier")),
        ns0.datatypes.Argument(name="InMonitoringNumber", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("Monitoring Number of the RequestSPDU")),
        ns0.datatypes.Argument(
            name="InFlags", dataType=o6.NodeId("ns=safety;i=3005"), valueRank=-1, description=o6.LocalizedText("Byte with non-safety flags from SafetyConsumer")
        ),
        ns0.datatypes.Argument(name="OutSafetyData", dataType=ns0.datatypes.Structure, valueRank=-1, description=o6.LocalizedText("Safety Data")),
        ns0.datatypes.Argument(name="OutFlags", dataType=o6.NodeId("ns=safety;i=3006"), valueRank=-1, description=o6.LocalizedText("Byte with safety flags from SafetyProvider")),
        ns0.datatypes.Argument(name="OutSPDU_ID_1", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("Safety PDU Identifier Part1")),
        ns0.datatypes.Argument(name="OutSPDU_ID_2", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("Safety PDU Identifier Part2")),
        ns0.datatypes.Argument(name="OutSPDU_ID_3", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("Safety PDU Identifier Part3")),
        ns0.datatypes.Argument(name="OutSafetyConsumerID", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("SafetyConsumer identifier")),
        ns0.datatypes.Argument(name="OutMonitoringNumber", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("Monitoring Number of the ResponseSPDU")),
        ns0.datatypes.Argument(name="OutCRC", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("CRC-checksum over the ResponseSPDU")),
        ns0.datatypes.Argument(name="OutNonSafetyData", dataType=ns0.datatypes.Structure, valueRank=-1, description=o6.LocalizedText("Non-safe data")),
    ],
)
o6.call(nodeId="ns=safety;i=7002", browseName="ns=safety;ReadSafetyDiagnostics", outputArgs=o6.hasProperty(o6.ns["ns=safety;i=6009"]))


@o6.objecttype(nodeId="ns=safety;i=1003", browseName="ns=safety;SafetyProviderType", displayName="SafetyProviderType")
class SafetyProviderType(SafetyObjectsType):
    parameters: SafetyProviderParametersType
    readSafetyData: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=safety;i=7001"])
    readSafetyDiagnostics: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=safety;i=7002"])
    safetyPDUs: SafetyPDUsType | None = o6.hasComponent(o6.ns["ns=safety;i=5000"])


del Any, TYPE_CHECKING, uuid, o6, ns0, safety_datypes
