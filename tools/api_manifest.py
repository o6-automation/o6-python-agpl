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

"""Structured companion to ``dev_docs/api_manifest.md``.

The Markdown document is the reviewed contract.  This module gives tests and
documentation tooling an exact, machine-readable inventory of public names.
"""

PUBLIC_MODULES = (
    "client",
    "common",
    "node",
    "ns",
    "pubsub",
    "server",
    "subscription",
    "util",
)

ROOT_DEFINED = (
    "Boolean",
    "Byte",
    "ByteString",
    "ClientConfig",
    "DataValue",
    "DateTime",
    "DiagnosticInfo",
    "Double",
    "ExpandedNodeId",
    "ExtensionObject",
    "Float",
    "Guid",
    "HasNodeId",
    "IndexRange",
    "Int16",
    "Int32",
    "Int64",
    "LocalizedText",
    "LocalizedTextLike",
    "MaybeAwaitable",
    "NodeId",
    "NodeIdLike",
    "QualifiedName",
    "SByte",
    "StatusCode",
    "StatusCodeError",
    "String",
    "UInt16",
    "UInt32",
    "UInt64",
    "XmlElement",
    "decodeBinary",
    "decodeJson",
    "decodeXml",
    "encodeBinary",
    "encodeJson",
    "encodeXml",
    "logDebug",
    "logError",
    "logFatal",
    "logInfo",
    "logTrace",
    "logWarning",
)

AUTHORING_FUNCTIONS = (
    "datatype",
    "enumfield",
    "enumtype",
    "field",
    "call",
    "objecttype",
    "read",
    "referencetype",
    "variabletype",
    "view",
    "write",
)

REFERENCE_FUNCTIONS = (
    "addInOf",
    "componentOf",
    "eventSourceOf",
    "generatedBy",
    "generatesEvent",
    "hasAddIn",
    "hasComponent",
    "hasCondition",
    "hasEncoding",
    "hasEventSource",
    "hasInterface",
    "hasNotifier",
    "hasOrderedComponent",
    "hasProperty",
    "interfaceOf",
    "isConditionOf",
    "notifierOf",
    "orderedComponentOf",
    "organizedBy",
    "organizes",
    "propertyOf",
    "reference",
)

ROOT_ALIASES = {
    "AccessLevel": "o6.common.AccessLevel",
    "AccessControl": "o6.server.AccessControl",
    "AttributeId": "o6.common.AttributeId",
    "Client": "o6.client.Client",
    "Event": "o6.server.Event",
    "MonitoredItem": "o6.subscription.MonitoredItem",
    "Node": "o6.node.Node",
    "NodePermissions": "o6.server.NodePermissions",
    "Permission": "o6.common.Permission",
    "Role": "o6.server.Role",
    "Server": "o6.server.Server",
    "SecureChannelState": "o6.common.SecureChannelState",
    "SecurityMode": "o6.common.SecurityMode",
    "SecurityPolicy": "o6.common.SecurityPolicy",
    "Session": "o6.server.Session",
    "SessionActivation": "o6.server.SessionActivation",
    "SessionState": "o6.common.SessionState",
    "Subscription": "o6.subscription.Subscription",
    "ValueRank": "o6.common.ValueRank",
    "WriteMask": "o6.common.WriteMask",
    "roles": "o6.server.roles",
}

MODULE_EXPORTS = {
    "o6.client": ("Client",),
    "o6.common": (
        "AccessLevel",
        "AttributeId",
        "Permission",
        "SecureChannelState",
        "SecurityMode",
        "SecurityPolicy",
        "SessionState",
        "ValueRank",
        "WriteMask",
    ),
    "o6.node": (
        "AwaitableNode",
        "DataTypeNode",
        "MethodNode",
        "Node",
        "ObjectNode",
        "ObjectTypeNode",
        "ReferenceTypeNode",
        "VariableNode",
        "VariableTypeNode",
        "ViewNode",
    ),
    "o6.ns": ("NamespaceModule", "filter", "namespace", "register"),
    "o6.pubsub": (
        "Offset",
        "OffsetTable",
        "OffsetType",
        "StateMachine",
        "offsetTable",
        "publish",
        "setStateMachine",
    ),
    "o6.server": (
        "AccessControl",
        "Event",
        "MethodCallback",
        "NodePermissions",
        "Role",
        "Server",
        "Session",
        "SessionActivation",
        "VariableReadCallback",
        "VariableWriteCallback",
        "roles",
    ),
    "o6.subscription": ("MonitoredItem", "Subscription"),
    "o6.util": (
        "createSelfSignedCertificate",
        "loadCertificate",
        "loadPrivateKey",
    ),
}

PRIVATE_MODULES = (
    "o6._datatype_registration",
    "o6._declarations",
    "o6._decorators",
    "o6._node_backend",
    "o6._references",
    "o6._server_construction",
    "o6._server_materialization",
    "o6._server_types",
)

REMOVED_PUBLIC_LOOKING_MODULES = (
    "o6.datatype_registration",
    "o6.declarations",
    "o6.decorators",
    "o6.references",
)

ROOT_EXPORTS = tuple(
    sorted(
        set(PUBLIC_MODULES)
        | set(ROOT_DEFINED)
        | set(AUTHORING_FUNCTIONS)
        | set(REFERENCE_FUNCTIONS)
        | set(ROOT_ALIASES)
    )
)

CANONICAL_PATHS = tuple(
    sorted(
        {f"o6.{name}" for name in ROOT_DEFINED + AUTHORING_FUNCTIONS + REFERENCE_FUNCTIONS}
        | set(ROOT_ALIASES.values())
        | set(f"{module}.{name}" for module, names in MODULE_EXPORTS.items() for name in names)
        | {f"o6.{module}" for module in PUBLIC_MODULES}
    )
)
