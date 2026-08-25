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
from . import objtypes as safety_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

safetyACSet = ns0.objtypes.FolderType(
    nodeId="ns=safety;i=5002",
    browseName="ns=safety;SafetyACSet",
    description="Contains all instances of safety objects (SafetyProvider or SafetyConsumer)",
    parent="i=85",
    referenceType=ns0.reftypes.Organizes,
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=safety;i=5003", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=safety;i=5004", browseName="Default XML")
o6.hasEncoding(safety_datypes.NonSafetyDataPlaceholderDataType, o6.ns["ns=safety;i=5004"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=safety;i=5005", browseName="Default JSON")
o6.hasEncoding(safety_datypes.NonSafetyDataPlaceholderDataType, o6.ns["ns=safety;i=5005"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=safety;i=5010", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=safety;i=5011", browseName="Default XML")
o6.hasEncoding(safety_datypes.RequestSPDUDataType, o6.ns["ns=safety;i=5011"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=safety;i=5012", browseName="Default JSON")
o6.hasEncoding(safety_datypes.RequestSPDUDataType, o6.ns["ns=safety;i=5012"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashSafety = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=safety;i=5006",
    browseName="ns=safety;http://opcfoundation.org/UA/Safety",
    description="Provides the metadata for a namespace used by the server.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=safety;i=6022",
                browseName="IsNamespaceSubset",
                description="If TRUE then the server only supports a subset of the namespace.",
                dataType=o6.Boolean,
                value=False,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=safety;i=6023",
                browseName="NamespacePublicationDate",
                description="The publication date for the namespace.",
                dataType=o6.DateTime,
                value=o6.DateTime("2025-02-05T00:00:00Z"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=safety;i=6024", browseName="NamespaceUri", description="The URI of the namespace.", dataType=o6.String, value="http://opcfoundation.org/UA/Safety"
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=safety;i=6025",
                browseName="NamespaceVersion",
                description="The human readable string representing version of the namespace.",
                dataType=o6.String,
                value="1.05.04",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=safety;i=6026",
                browseName="StaticNodeIdTypes",
                description="A list of IdTypes for nodes which are the same in every server that exposes them.",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=safety;i=6027",
                browseName="StaticNumericNodeIdRange",
                description="A list of ranges for numeric node ids which are the same in every server that exposes them.",
                dataType=ns0.datatypes.NumericRange,
                valueRank=1,
                arrayDimensions=[1],
                value=["1:2147483647"],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=safety;i=6028",
                browseName="StaticStringNodeIdPattern",
                description="A regular expression which matches string node ids are the same in every server that exposes them.",
                dataType=o6.String,
                value="",
            )
        ),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.PropertyType(
    nodeId="ns=safety;i=6059",
    browseName="OptionSetValues",
    parent="ns=safety;i=3005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("CommunicationError"), o6.LocalizedText("OperatorAckRequested"), o6.LocalizedText("FSV_Activated")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=safety;i=6060",
    browseName="OptionSetValues",
    parent="ns=safety;i=3006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("OperatorAckProvider"), o6.LocalizedText("ActivateFSV"), o6.LocalizedText("TestModeActivated")],
)
safety_objtypes.SafetyProviderParametersType(
    nodeId="ns=safety;i=5001",
    browseName="ns=safety;Parameters",
    description="Safety parameters of this SafetyProvider",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=safety;i=6019", browseName="ns=safety;SafetyBaseIDActive", description="Currently active Base-ID of the SafetyProvider", dataType=o6.Guid
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=safety;i=6020", browseName="ns=safety;SafetyBaseIDConfigured", description="Base-ID of the SafetyProvider as configured via the SPI", dataType=o6.Guid
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=safety;i=6021",
                browseName="ns=safety;SafetyProviderDelay",
                description="SafetyProviderDelay is the maximum time at the SafetyProvider from receiving the RequestSPDU to start the transmission of ResponseSPDU",
                dataType=o6.UInt32,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=safety;i=6031", browseName="ns=safety;SafetyProviderIDActive", description="Currently active Provider-ID of the SafetyProvider", dataType=o6.UInt32
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=safety;i=6032",
                browseName="ns=safety;SafetyProviderIDConfigured",
                description="Provider-ID of the SafetyProvider as configured via the SPI",
                dataType=o6.UInt32,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=safety;i=6033",
                browseName="ns=safety;SafetyProviderLevel",
                description="The maximal SIL the SafetyProvider implementation (hardware & software) is capable of",
                dataType=o6.Byte,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=safety;i=6034",
                browseName="ns=safety;SafetyPubSubImplemented",
                description="Indicates whether the SafetyProvider supports OPC UA PubSub communication",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=safety;i=6040",
                browseName="ns=safety;SafetyServerImplemented",
                description="Indicates whether the SafetyProvider supports OPC UA Client/Server communication",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=safety;i=6061", browseName="ns=safety;SafetyStructureIdentifier", description="Identifier of the structure type", dataType=o6.String
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=safety;i=6070", browseName="ns=safety;SafetyStructureSignature", dataType=o6.UInt32)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=safety;i=6071",
                browseName="ns=safety;SafetyStructureSignatureVersion",
                description="Version of the algorithm for calculating the StructureSignature",
                dataType=o6.UInt16,
            )
        ),
    ],
)
o6.reference(safety_objtypes.SafetyProviderType, ns0.reftypes.HasComponent, o6.ns["ns=safety;i=5001"])
safety_objtypes.SafetyConsumerParametersType(
    nodeId="ns=safety;i=5009",
    browseName="ns=safety;Parameters",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=safety;i=6072", browseName="ns=safety;SafetyBaseIDActive", dataType=o6.Guid)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=safety;i=6073", browseName="ns=safety;SafetyBaseIDConfigured", dataType=o6.Guid)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=safety;i=6074",
                browseName="ns=safety;SafetyClientImplemented",
                description="Indicates whether the SafetyClient supports OPC UA Client/Server communication",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=safety;i=6075", browseName="ns=safety;SafetyConsumerIDActive", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=safety;i=6076", browseName="ns=safety;SafetyConsumerIDConfigured", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=safety;i=6077", browseName="ns=safety;SafetyConsumerTimeout", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=safety;i=6078", browseName="ns=safety;SafetyErrorIntervalLimit", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=safety;i=6079", browseName="ns=safety;SafetyOperatorAckNecessary", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=safety;i=6080", browseName="ns=safety;SafetyProviderIDActive", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=safety;i=6081", browseName="ns=safety;SafetyProviderIDConfigured", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=safety;i=6082", browseName="ns=safety;SafetyProviderLevel", dataType=o6.Byte)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=safety;i=6083",
                browseName="ns=safety;SafetyPubSubImplemented",
                description="Indicates whether the SafetyConsumer supports OPC UA PubSub communication",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=safety;i=6084", browseName="ns=safety;SafetyStructureIdentifier", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=safety;i=6085", browseName="ns=safety;SafetyStructureSignature", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=safety;i=6086", browseName="ns=safety;SafetyStructureSignatureVersion", dataType=o6.UInt16)),
    ],
)
o6.reference(safety_objtypes.SafetyConsumerType, ns0.reftypes.HasComponent, o6.ns["ns=safety;i=5009"])


del Any, TYPE_CHECKING, uuid, o6, ns0, safety_datypes, safety_objtypes
