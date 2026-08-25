# Copyright 2026 (c) o6 Automation GmbH
"""Common OPC UA definitions independent of client and server machinery."""

import enum


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
    "AttributeId",
    "SecureChannelState",
    "SecurityMode",
    "SecurityPolicy",
    "SessionState",
    "ValueRank",
]


def __dir__() -> list[str]:
    return sorted(__all__)


del enum
