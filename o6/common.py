# Copyright 2026 (c) o6 Automation GmbH
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
    """OPC UA security policy URIs.

    `Client(securityPolicy=...)`, `ClientConfig.securityPolicy`, and the
    `securityPolicy` arguments of `Server.registerDiscovery()` and
    `Server.deregisterDiscovery()` also accept short names after `#`,
    case-insensitively and ignoring `_`, e.g. `"Basic256Sha256"`.
    Discovery registration supports only the RSA policies and `NONE`.
    Fields named `securityPolicyUri` require the full URI.
    """

    NONE = "http://opcfoundation.org/UA/SecurityPolicy#None"
    BASIC128RSA15 = "http://opcfoundation.org/UA/SecurityPolicy#Basic128Rsa15"
    BASIC256 = "http://opcfoundation.org/UA/SecurityPolicy#Basic256"
    BASIC256SHA256 = "http://opcfoundation.org/UA/SecurityPolicy#Basic256Sha256"
    AES128_SHA256_RSAOAEP = "http://opcfoundation.org/UA/SecurityPolicy#Aes128_Sha256_RsaOaep"
    AES256_SHA256_RSAPSS = "http://opcfoundation.org/UA/SecurityPolicy#Aes256_Sha256_RsaPss"
    ECC_NISTP256 = "http://opcfoundation.org/UA/SecurityPolicy#ECC_nistP256"
    ECC_NISTP384 = "http://opcfoundation.org/UA/SecurityPolicy#ECC_nistP384"
    ECC_BRAINPOOLP256R1 = "http://opcfoundation.org/UA/SecurityPolicy#ECC_brainpoolP256r1"
    ECC_BRAINPOOLP384R1 = "http://opcfoundation.org/UA/SecurityPolicy#ECC_brainpoolP384r1"
    ECC_CURVE25519 = "http://opcfoundation.org/UA/SecurityPolicy#ECC_curve25519"
    ECC_CURVE448 = "http://opcfoundation.org/UA/SecurityPolicy#ECC_curve448"
    ECC_NISTP256_AESGCM = "http://opcfoundation.org/UA/SecurityPolicy#ECC_nistP256_AesGcm"
    ECC_NISTP256_CHACHAPOLY = "http://opcfoundation.org/UA/SecurityPolicy#ECC_nistP256_ChaChaPoly"


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
