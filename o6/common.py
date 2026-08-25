# Copyright 2026 (c) o6 Automation GmbH
"""Common OPC UA definitions independent of client and server machinery."""

import enum


class Permission(enum.IntFlag):
    """OPC UA permission mask used by role-based access control."""

    BROWSE = 1 << 0
    READ_ROLE_PERMISSIONS = 1 << 1
    WRITE_ATTRIBUTE = 1 << 2
    WRITE_ROLE_PERMISSIONS = 1 << 3
    WRITE_HISTORIZING = 1 << 4
    READ = 1 << 5
    WRITE = 1 << 6
    READ_HISTORY = 1 << 7
    INSERT_HISTORY = 1 << 8
    MODIFY_HISTORY = 1 << 9
    DELETE_HISTORY = 1 << 10
    RECEIVE_EVENTS = 1 << 11
    CALL = 1 << 12
    ADD_REFERENCE = 1 << 13
    REMOVE_REFERENCE = 1 << 14
    DELETE_NODE = 1 << 15
    ADD_NODE = 1 << 16
    ALL = (1 << 17) - 1


class AttributeId(enum.IntEnum):
    """OPC UA attribute IDs (subset of `UA_AttributeId`)."""

    NODE_ID = 1
    NODE_CLASS = 2
    BROWSE_NAME = 3
    DISPLAY_NAME = 4
    DESCRIPTION = 5
    WRITE_MASK = 6
    USER_WRITE_MASK = 7
    IS_ABSTRACT = 8
    SYMMETRIC = 9
    INVERSE_NAME = 10
    CONTAINS_NO_LOOPS = 11
    EVENT_NOTIFIER = 12
    VALUE = 13
    DATA_TYPE = 14
    VALUE_RANK = 15
    ARRAY_DIMENSIONS = 16
    ACCESS_LEVEL = 17
    USER_ACCESS_LEVEL = 18
    MINIMUM_SAMPLING_INTERVAL = 19
    HISTORIZING = 20
    EXECUTABLE = 21
    USER_EXECUTABLE = 22
    DATA_TYPE_DEFINITION = 23
    ROLE_PERMISSIONS = 24
    USER_ROLE_PERMISSIONS = 25
    ACCESS_RESTRICTIONS = 26
    ACCESS_LEVEL_EX = 27


class ValueRank(enum.IntEnum):
    """Symbolic values for the most common OPC UA ValueRanks."""

    SCALAR_OR_1D = -3
    ANY = -2
    SCALAR = -1
    ARRAY_ANY = 0
    ARRAY_1D = 1
    ARRAY_2D = 2


class AccessLevel(enum.IntFlag, boundary=enum.FlagBoundary.KEEP):
    """Bitmask values for the `AccessLevel` and `UserAccessLevel` attributes."""

    READ = 0x01 << 0
    CURRENT_READ = 0x01 << 0
    WRITE = 0x01 << 1
    CURRENT_WRITE = 0x01 << 1
    HISTORY_READ = 0x01 << 2
    HISTORY_WRITE = 0x01 << 3
    SEMANTIC_CHANGE = 0x01 << 4
    STATUS_WRITE = 0x01 << 5
    TIMESTAMP_WRITE = 0x01 << 6


class WriteMask(enum.IntFlag, boundary=enum.FlagBoundary.KEEP):
    """Bitmask values for the `WriteMask` and `UserWriteMask` attributes."""

    ACCESS_LEVEL = 0x01 << 0
    ARRAY_DIMENSIONS = 0x01 << 1
    BROWSE_NAME = 0x01 << 2
    CONTAINS_NO_LOOPS = 0x01 << 3
    DATA_TYPE = 0x01 << 4
    DESCRIPTION = 0x01 << 5
    DISPLAY_NAME = 0x01 << 6
    EVENT_NOTIFIER = 0x01 << 7
    EXECUTABLE = 0x01 << 8
    HISTORIZING = 0x01 << 9
    INVERSE_NAME = 0x01 << 10
    IS_ABSTRACT = 0x01 << 11
    MINIMUM_SAMPLING_INTERVAL = 0x01 << 12
    NODE_CLASS = 0x01 << 13
    NODE_ID = 0x01 << 14
    SYMMETRIC = 0x01 << 15
    USER_ACCESS_LEVEL = 0x01 << 16
    USER_EXECUTABLE = 0x01 << 17
    USER_WRITE_MASK = 0x01 << 18
    VALUE_RANK = 0x01 << 19
    WRITE_MASK = 0x01 << 20
    VALUE_FOR_VARIABLE_TYPE = 0x01 << 21
    DATA_TYPE_DEFINITION = 0x01 << 22
    ROLE_PERMISSIONS = 0x01 << 23
    ACCESS_RESTRICTIONS = 0x01 << 24
    ACCESS_LEVEL_EX = 0x01 << 25


class SecureChannelState(enum.IntEnum):
    """Possible status of an OPC UA SecureChannel."""

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
    """Possible status of an OPC UA Session."""

    CLOSED = 0
    CREATE_REQUESTED = 1
    CREATED = 2
    ACTIVATE_REQUESTED = 3
    ACTIVATED = 4
    CLOSING = 5


class SecurityMode(enum.IntEnum):
    """OPC UA MessageSecurityMode."""

    INVALID = 0
    NONE = 1
    SIGN = 2
    SIGN_AND_ENCRYPT = 3


class SecurityPolicy(str, enum.Enum):
    """OPC UA security policy URIs."""

    NONE = "http://opcfoundation.org/UA/SecurityPolicy#None"
    BASIC128RSA15 = "http://opcfoundation.org/UA/SecurityPolicy#Basic128Rsa15"
    BASIC256 = "http://opcfoundation.org/UA/SecurityPolicy#Basic256"
    BASIC256SHA256 = "http://opcfoundation.org/UA/SecurityPolicy#Basic256Sha256"
    AES128_SHA256_RSAOAEP = "http://opcfoundation.org/UA/SecurityPolicy#Aes128_Sha256_RsaOaep"
    AES256_SHA256_RSAPSS = "http://opcfoundation.org/UA/SecurityPolicy#Aes256_Sha256_RsaPss"


__all__ = [
    "AccessLevel",
    "AttributeId",
    "Permission",
    "SecureChannelState",
    "SecurityMode",
    "SecurityPolicy",
    "SessionState",
    "ValueRank",
    "WriteMask",
]


def __dir__() -> list[str]:
    return sorted(__all__)


del enum
