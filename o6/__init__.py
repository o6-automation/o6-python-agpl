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
from __future__ import annotations

__version__ = "0.2.0"
__author__ = "O6 Development Team"
__email__ = "dev@o6project.org"
__all__ = [
    "types",
    "NodeId",
    "Client",
    "Subscription",
    "MonitoredItem",
    "StatusCodeError",
    "ClientConfig",
    "AttributeId",
    "ValueRank",
    "AccessLevel",
    "WriteMask",
    "SecurityMode",
    "SecurityPolicy",
    "crypto",
    "encryption_available",
    "log_trace",
    "log_debug",
    "log_info",
    "log_warning",
    "log_error",
    "log_fatal",
    # Type Hints
    "KeyValueMap",
    "MaybeAwaitable",
    "AwaitReturn",
    "Future",
    "HasNodeId",
    "NodeIdLike",
    "LocalizedTextLike",
    "ns",
]

from typing import (
    Optional,
    Union,
    Any,
    Awaitable,
    Generator,
    TypeAlias,
    TypeVar,
    Protocol,
)
from asyncio import Future as AsyncIOFuture
from concurrent.futures import Future as ConcurrentFuture

from . import _o6
import enum

_server_available = hasattr(_o6, "Server")

if _server_available:
    __all__ += ["Server", "ServerNode", "make_argument"]

#
# Type Hints
#

KeyValueMap: TypeAlias = dict[str, Any]

_T = TypeVar("_T")
MaybeAwaitable: TypeAlias = _T | Awaitable[_T]

_V = TypeVar("_V")
AwaitReturn: TypeAlias = Generator[Any, None, _V]

_U = TypeVar("_U")
Future: TypeAlias = AsyncIOFuture[_U] | ConcurrentFuture[_U]


# Protocol for classes with a member "_nodeid" of type NodeId. The native NodeId
# constructor checks the argument for a _nodeid member and makes a copy if
# present.
class HasNodeId(Protocol):
    _nodeid: _o6.types.NodeId


# Type that can be used to initialize a NodeId
NodeIdLike: TypeAlias = _o6.types.NodeId | str | HasNodeId

# Type that can be used to initialize a LocalizedText
LocalizedTextLike: TypeAlias = _o6.types.LocalizedText | str

#
# Define OPC UA enums that are not part of the generated datatypes
#


class AttributeId(enum.IntEnum):
    NODEID = 1
    NODECLASS = 2
    BROWSENAME = 3
    DISPLAYNAME = 4
    DESCRIPTION = 5
    WRITEMASK = 6
    USERWRITEMASK = 7
    ISABSTRACT = 8
    SYMMETRIC = 9
    INVERSENAME = 10
    CONTAINSNOLOOPS = 11
    EVENTNOTIFIER = 12
    VALUE = 13
    DATATYPE = 14
    VALUERANK = 15
    ARRAYDIMENSIONS = 16
    ACCESSLEVEL = 17
    USERACCESSLEVEL = 18
    MINIMUMSAMPLINGINTERVAL = 19
    HISTORIZING = 20
    EXECUTABLE = 21
    USEREXECUTABLE = 22
    DATATYPEDEFINITION = 23
    ROLEPERMISSIONS = 24
    USERROLEPERMISSIONS = 25
    ACCESSRESTRICTIONS = 26
    ACCESSLEVELEX = 27


class ValueRank(enum.IntEnum):
    SCALAR_OR_1D = -3
    ANY = -2
    SCALAR = -1
    ARRAY_ANY = 0
    ARRAY_1D = 1
    ARRAY_2D = 2


class AccessLevel(enum.IntFlag, boundary=enum.FlagBoundary.KEEP):
    READ = 0x01 << 0
    CURRENTREAD = 0x01 << 0
    WRITE = 0x01 << 1
    CURRENTWRITE = 0x01 << 1
    HISTORYREAD = 0x01 << 2
    HISTORYWRITE = 0x01 << 3
    SEMANTICCHANGE = 0x01 << 4
    STATUSWRITE = 0x01 << 5
    TIMESTAMPWRITE = 0x01 << 6


class WriteMask(enum.IntFlag, boundary=enum.FlagBoundary.KEEP):
    ACCESSLEVEL = 0x01 << 0
    ARRAYDIMENSIONS = 0x01 << 1
    BROWSENAME = 0x01 << 2
    CONTAINSNOLOOPS = 0x01 << 3
    DATATYPE = 0x01 << 4
    DESCRIPTION = 0x01 << 5
    DISPLAYNAME = 0x01 << 6
    EVENTNOTIFIER = 0x01 << 7
    EXECUTABLE = 0x01 << 8
    HISTORIZING = 0x01 << 9
    INVERSENAME = 0x01 << 10
    ISABSTRACT = 0x01 << 11
    MINIMUMSAMPLINGINTERVAL = 0x01 << 12
    NODECLASS = 0x01 << 13
    NODEID = 0x01 << 14
    SYMMETRIC = 0x01 << 15
    USERACCESSLEVEL = 0x01 << 16
    USEREXECUTABLE = 0x01 << 17
    USERWRITEMASK = 0x01 << 18
    VALUERANK = 0x01 << 19
    WRITEMASK = 0x01 << 20
    VALUEFORVARIABLETYPE = 0x01 << 21
    DATATYPEDEFINITION = 0x01 << 22
    ROLEPERMISSIONS = 0x01 << 23
    ACCESSRESTRICTIONS = 0x01 << 24
    ACCESSLEVELEX = 0x01 << 25


class SecureChannelState(enum.IntEnum):
    CLOSED = 0
    REVERSE_LISTENING = 1
    CONNECTING = 2
    CONNECTED = 3
    REVERSE_CONNECTED = 4
    RHE_SENT = 5
    HEL_SENT = 6
    HEL_RECEIVED = 7
    ACK_SENT = 8
    ACK_RECEIVED = 9
    OPN_SENT = 10
    OPEN = 11
    CLOSING = 12


class SessionState(enum.IntEnum):
    CLOSED = 0
    CREATE_REQUESTED = 1
    CREATED = 2
    ACTIVATE_REQUESTED = 3
    ACTIVATED = 4
    CLOSING = 5


#
# Monkey-patch the generated datatypes to add custom functionality like __init__ / __str__
#


def _patch_DataChangeFilter() -> None:
    _orig_init = _o6.types.DataChangeFilter.__init__

    def __init__(
        self,
        trigger: Optional[_o6.types.DataChangeTrigger | int] = None,
        deadband_type: Optional[int] = None,
        deadband_value: Optional[float] = None,
    ) -> None:
        _orig_init(self)
        if trigger is not None:
            if isinstance(trigger, int):
                trigger = _o6.types.DataChangeTrigger(trigger)
            self.trigger = trigger
        if deadband_type is not None:
            self.deadband_type = deadband_type
        if deadband_value is not None:
            self.deadband_value = deadband_value

    _o6.types.DataChangeFilter.__init__ = __init__  # type: ignore[assignment]


_patch_DataChangeFilter()
DataChangeFilter = _o6.types.DataChangeFilter


def _patch_RelativePath() -> None:
    _orig_init = _o6.types.RelativePath.__init__

    def __init__(self, input: Optional[str] = None) -> None:
        _orig_init(self)
        if isinstance(input, str):
            res = _o6.types._parseRelativePath(input)
            self.elements = res.elements

    def __str__(self) -> str:
        return _o6.types._printRelativePath(self)

    _o6.types.RelativePath.__init__ = __init__  # type: ignore[assignment]
    _o6.types.RelativePath.__str__ = __str__  # type: ignore[method-assign]


_patch_RelativePath()
RelativePath = _o6.types.RelativePath


def _patch_SimpleAttributeOperand() -> None:
    _orig_init = _o6.types.SimpleAttributeOperand.__init__

    def __init__(self, input: Optional[str] = None) -> None:
        _orig_init(self)
        if isinstance(input, str):
            res = _o6.types._parseSimpleAttributeOperand(input)
            self.type_definition_id = res.type_definition_id
            self.browse_path = res.browse_path
            self.attribute_id = res.attribute_id
            self.index_range = res.index_range

    def __str__(self) -> str:
        return _o6.types._printSimpleAttributeOperand(self)

    _o6.types.SimpleAttributeOperand.__init__ = __init__  # type: ignore[assignment]
    _o6.types.SimpleAttributeOperand.__str__ = __str__  # type: ignore[method-assign]


_patch_SimpleAttributeOperand()
SimpleAttributeOperand = _o6.types.SimpleAttributeOperand


def _patch_ReadValueId() -> None:
    _orig_init = _o6.types.ReadValueId.__init__

    def __init__(self, input: Optional[str] = None) -> None:
        _orig_init(self)
        if isinstance(input, str):
            res = _o6.types._parseReadValueId(input)
            self.nodeid = res.nodeid
            self.attribute_id = res.attribute_id
            self.index_range = res.index_range
            self.data_encoding = res.data_encoding

    def __str__(self) -> str:
        return _o6.types._printReadValueId(self)

    _o6.types.ReadValueId.__init__ = __init__  # type: ignore[assignment]
    _o6.types.ReadValueId.__str__ = __str__  # type: ignore[method-assign]


_patch_ReadValueId()
ReadValueId = _o6.types.ReadValueId


#
# Override dir() and getattr() to point into the underlying raw API from _o6
#


class SecurityMode(enum.IntEnum):
    INVALID = 0
    NONE = 1
    SIGN = 2
    SIGN_AND_ENCRYPT = 3


class SecurityPolicy(str, enum.Enum):
    NONE = "http://opcfoundation.org/UA/SecurityPolicy#None"
    BASIC128RSA15 = "http://opcfoundation.org/UA/SecurityPolicy#Basic128Rsa15"
    BASIC256 = "http://opcfoundation.org/UA/SecurityPolicy#Basic256"
    BASIC256SHA256 = "http://opcfoundation.org/UA/SecurityPolicy#Basic256Sha256"
    AES128_SHA256_RSAOAEP = (
        "http://opcfoundation.org/UA/SecurityPolicy#Aes128_Sha256_RsaOaep"
    )
    AES256_SHA256_RSAPSS = (
        "http://opcfoundation.org/UA/SecurityPolicy#Aes256_Sha256_RsaPss"
    )


def __getattr__(name):
    if name in (
        "log_trace",
        "log_debug",
        "log_info",
        "log_warning",
        "log_error",
        "log_fatal",
    ):
        return getattr(_o6, name)
    if name == "types":
        return _o6.types
    if name == "StatusCodeError":
        return _o6.StatusCodeError
    if name == "Client":
        from .client import Client

        return Client
    if name == "ClientNode":
        from .client_nodes import Node

        return Node
    if name == "Subscription":
        from .client import Subscription

        return Subscription
    if name == "MonitoredItem":
        from .client import MonitoredItem

        return MonitoredItem
    if name == "ClientConfig":
        return _o6.ClientConfig
    if name == "Server":
        if not _server_available:
            raise AttributeError("Server support is not compiled in this build")
        from .server import Server

        return Server
    if name == "ServerNode":
        if not _server_available:
            raise AttributeError("Server support is not compiled in this build")
        from .server import ServerNode

        return ServerNode
    if name == "make_argument":
        if not _server_available:
            raise AttributeError("Server support is not compiled in this build")
        from .server import make_argument

        return make_argument
    if name == "crypto":
        from . import crypto

        return crypto
    if name == "encryption_available":
        from .crypto import encryption_available

        return encryption_available
    if name == "Namespaces":
        from .namespaces import Namespaces

        return Namespaces
    if name == "ns":
        from ._ns import ns

        globals()["ns"] = ns
        return ns
    # Fall back to _o6.types so individual type names (NodeId, EventFilter, …)
    # are accessible directly on the o6 module: `from o6 import NodeId`.
    try:
        return getattr(_o6.types, name)
    except:
        raise AttributeError(f"module {__name__} has no attribute {name}")


def __dir__():
    return sorted(list(globals().keys()) + dir(_o6.types) + __all__)
