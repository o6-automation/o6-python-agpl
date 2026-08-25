# Copyright 2026 (c) o6 Automation GmbH
from __future__ import annotations

# =============================================================================
# Imports
# =============================================================================

from datetime import datetime
from pathlib import Path
from typing import (
    TYPE_CHECKING,
    Any,
    Awaitable,
    Generator,
    Optional,
    Protocol,
    TypeAlias,
    TypeVar,
    Union,
    overload,
)
from uuid import UUID

from . import _o6  # type: ignore[attr-defined]
from .common import (
    AccessLevel,
    AttributeId,
    Permission,
    SecureChannelState,
    SecurityMode,
    SecurityPolicy,
    SessionState,
    ValueRank,
    WriteMask,
)

# =============================================================================
# Package metadata
# =============================================================================

__version__ = "2.0.1"
__author__ = "o6 Automation GmbH"
__email__ = "contact@o6-automation.com"

# =============================================================================
# Native public API
# =============================================================================

if TYPE_CHECKING:
    import enum

    import numpy as np
    from .ns import ns0

    _types: Any

    Boolean = np.bool_
    SByte = np.int8
    Byte = np.uint8
    Int16 = np.int16
    UInt16 = np.uint16
    Int32 = np.int32
    UInt32 = np.uint32
    Int64 = np.int64
    UInt64 = np.uint64
    Float = np.float32
    Double = np.float64
    String = str

    class DateTime:
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, date: datetime, /) -> None: ...
        @overload
        def __init__(self, date: DateTime | int | str, /) -> None: ...
        def __init__(self, *args: Any, **kwargs: Any) -> None: ...
        def __int__(self) -> int: ...
        def __eq__(self, other: object, /) -> bool: ...
        def __ne__(self, other: object, /) -> bool: ...
        def __lt__(self, other: object, /) -> bool: ...
        def __le__(self, other: object, /) -> bool: ...
        def __gt__(self, other: object, /) -> bool: ...
        def __ge__(self, other: object, /) -> bool: ...

    # These OPC UA builtin types use compatible Python stdlib types. XmlElement is
    # a distinct str subclass so its datatype identity does not collapse to String.
    Guid = UUID
    ByteString = bytes

    class XmlElement(str): ...

    class StatusCode(enum.IntFlag):
        """OPC UA StatusCode (32-bit bitfield).

        Severity (bits 31-30) | SubCode (bits 29-16) | InfoBits (bits 15-0).
        Members are generated from deps/open62541/tools/schema/StatusCode.csv.
        """

        def check(self, expected: StatusCode = ..., message: str | None = None) -> None: ...

        # fmt: off
        GOOD = 0x00000000  # The operation succeeded.
        UNCERTAIN = 0x40000000  # The operation was uncertain.
        BAD = 0x80000000  # The operation failed.
        BAD_UNEXPECTED_ERROR = 0x80010000  # An unexpected error occurred.
        BAD_INTERNAL_ERROR = 0x80020000  # An internal error occurred as a result of a programming or configuration error.
        BAD_OUT_OF_MEMORY = 0x80030000  # Not enough memory to complete the operation.
        BAD_RESOURCE_UNAVAILABLE = 0x80040000  # An operating system resource is not available.
        BAD_COMMUNICATION_ERROR = 0x80050000  # A low level communication error occurred.
        BAD_ENCODING_ERROR = 0x80060000  # Encoding halted because of invalid data in the objects being serialized.
        BAD_DECODING_ERROR = 0x80070000  # Decoding halted because of invalid data in the stream.
        BAD_ENCODING_LIMITS_EXCEEDED = 0x80080000  # The message encoding/decoding limits imposed by the stack have been exceeded.
        BAD_REQUEST_TOO_LARGE = 0x80B80000  # The request message size exceeds limits set by the server.
        BAD_RESPONSE_TOO_LARGE = 0x80B90000  # The response message size exceeds limits set by the client.
        BAD_UNKNOWN_RESPONSE = 0x80090000  # An unrecognized response was received from the server.
        BAD_TIMEOUT = 0x800A0000  # The operation timed out.
        BAD_SERVICE_UNSUPPORTED = 0x800B0000  # The server does not support the requested service.
        BAD_SHUTDOWN = 0x800C0000  # The operation was cancelled because the application is shutting down.
        BAD_SERVER_NOT_CONNECTED = 0x800D0000  # The operation could not complete because the client is not connected to the server.
        BAD_SERVER_HALTED = 0x800E0000  # The server has stopped and cannot process any requests.
        BAD_NOTHING_TO_DO = 0x800F0000  # There was nothing to do because the client passed a list of operations with no elements.
        BAD_TOO_MANY_OPERATIONS = 0x80100000  # The request could not be processed because it specified too many operations.
        BAD_TOO_MANY_MONITORED_ITEMS = 0x80DB0000  # The request could not be processed because there are too many monitored items in the subscription.
        BAD_DATA_TYPE_ID_UNKNOWN = 0x80110000  # The extension object cannot be (de)serialized because the data type id is not recognized.
        BAD_CERTIFICATE_INVALID = 0x80120000  # The certificate provided as a parameter is not valid.
        BAD_SECURITY_CHECKS_FAILED = 0x80130000  # An error occurred verifying security.
        BAD_CERTIFICATE_POLICY_CHECK_FAILED = 0x81140000  # The certificate does not meet the requirements of the security policy.
        BAD_CERTIFICATE_TIME_INVALID = 0x80140000  # The certificate has expired or is not yet valid.
        BAD_CERTIFICATE_ISSUER_TIME_INVALID = 0x80150000  # An issuer certificate has expired or is not yet valid.
        BAD_CERTIFICATE_HOST_NAME_INVALID = 0x80160000  # The HostName used to connect to a server does not match a HostName in the certificate.
        BAD_CERTIFICATE_URI_INVALID = 0x80170000  # The URI specified in the ApplicationDescription does not match the URI in the certificate.
        BAD_CERTIFICATE_USE_NOT_ALLOWED = 0x80180000  # The certificate may not be used for the requested operation.
        BAD_CERTIFICATE_ISSUER_USE_NOT_ALLOWED = 0x80190000  # The issuer certificate may not be used for the requested operation.
        BAD_CERTIFICATE_UNTRUSTED = 0x801A0000  # The certificate is not trusted.
        BAD_CERTIFICATE_REVOCATION_UNKNOWN = 0x801B0000  # It was not possible to determine if the certificate has been revoked.
        BAD_CERTIFICATE_ISSUER_REVOCATION_UNKNOWN = 0x801C0000  # It was not possible to determine if the issuer certificate has been revoked.
        BAD_CERTIFICATE_REVOKED = 0x801D0000  # The certificate has been revoked.
        BAD_CERTIFICATE_ISSUER_REVOKED = 0x801E0000  # The issuer certificate has been revoked.
        BAD_CERTIFICATE_CHAIN_INCOMPLETE = 0x810D0000  # The certificate chain is incomplete.
        BAD_USER_ACCESS_DENIED = 0x801F0000  # User does not have permission to perform the requested operation.
        BAD_IDENTITY_TOKEN_INVALID = 0x80200000  # The user identity token is not valid.
        BAD_IDENTITY_TOKEN_REJECTED = 0x80210000  # The user identity token is valid but the server has rejected it.
        BAD_SECURE_CHANNEL_ID_INVALID = 0x80220000  # The specified secure channel is no longer valid.
        BAD_INVALID_TIMESTAMP = 0x80230000  # The timestamp is outside the range allowed by the server.
        BAD_NONCE_INVALID = 0x80240000  # The nonce does appear to be not a random value or it is not the correct length.
        BAD_SESSION_ID_INVALID = 0x80250000  # The session id is not valid.
        BAD_SESSION_CLOSED = 0x80260000  # The session was closed by the client.
        BAD_SESSION_NOT_ACTIVATED = 0x80270000  # The session cannot be used because ActivateSession has not been called.
        BAD_SUBSCRIPTION_ID_INVALID = 0x80280000  # The subscription id is not valid.
        BAD_REQUEST_HEADER_INVALID = 0x802A0000  # The header for the request is missing or invalid.
        BAD_TIMESTAMPS_TO_RETURN_INVALID = 0x802B0000  # The timestamps to return parameter is invalid.
        BAD_REQUEST_CANCELLED_BY_CLIENT = 0x802C0000  # The request was cancelled by the client.
        BAD_TOO_MANY_ARGUMENTS = 0x80E50000  # Too many arguments were provided.
        BAD_LICENSE_EXPIRED = 0x810E0000  # The server requires a license to operate in general or to perform a service or operation, but existing license is expired.
        BAD_LICENSE_LIMITS_EXCEEDED = 0x810F0000  # The server has limits on number of allowed operations / objects, based on installed licenses, and these limits where exceeded.
        BAD_LICENSE_NOT_AVAILABLE = 0x81100000  # The server does not have a license which is required to operate in general or to perform a service or operation.
        GOOD_SUBSCRIPTION_TRANSFERRED = 0x002D0000  # The subscription was transferred to another session.
        GOOD_COMPLETES_ASYNCHRONOUSLY = 0x002E0000  # The processing will complete asynchronously.
        GOOD_OVERLOAD = 0x002F0000  # Sampling has slowed down due to resource limitations.
        GOOD_CLAMPED = 0x00300000  # The value written was accepted but was clamped.
        BAD_NO_COMMUNICATION = 0x80310000  # Communication with the data source is defined, but not established, and there is no last known value available.
        BAD_WAITING_FOR_INITIAL_DATA = 0x80320000  # Waiting for the server to obtain values from the underlying data source.
        BAD_NODE_ID_INVALID = 0x80330000  # The syntax of the node id is not valid.
        BAD_NODE_ID_UNKNOWN = 0x80340000  # The node id refers to a node that does not exist in the server address space.
        BAD_ATTRIBUTE_ID_INVALID = 0x80350000  # The attribute is not supported for the specified Node.
        BAD_INDEX_RANGE_INVALID = 0x80360000  # The syntax of the index range parameter is invalid.
        BAD_INDEX_RANGE_NO_DATA = 0x80370000  # No data exists within the range of indexes specified.
        BAD_DATA_ENCODING_INVALID = 0x80380000  # The data encoding is invalid.
        BAD_DATA_ENCODING_UNSUPPORTED = 0x80390000  # The server does not support the requested data encoding for the node.
        BAD_NOT_READABLE = 0x803A0000  # The access level does not allow reading or subscribing to the Node.
        BAD_NOT_WRITABLE = 0x803B0000  # The access level does not allow writing to the Node.
        BAD_OUT_OF_RANGE = 0x803C0000  # The value was out of range.
        BAD_NOT_SUPPORTED = 0x803D0000  # The requested operation is not supported.
        BAD_NOT_FOUND = 0x803E0000  # A requested item was not found or a search operation ended without success.
        BAD_OBJECT_DELETED = 0x803F0000  # The object cannot be used because it has been deleted.
        BAD_NOT_IMPLEMENTED = 0x80400000  # Requested operation is not implemented.
        BAD_MONITORING_MODE_INVALID = 0x80410000  # The monitoring mode is invalid.
        BAD_MONITORED_ITEM_ID_INVALID = 0x80420000  # The monitoring item id does not refer to a valid monitored item.
        BAD_MONITORED_ITEM_FILTER_INVALID = 0x80430000  # The monitored item filter parameter is not valid.
        BAD_MONITORED_ITEM_FILTER_UNSUPPORTED = 0x80440000  # The server does not support the requested monitored item filter.
        BAD_FILTER_NOT_ALLOWED = 0x80450000  # A monitoring filter cannot be used in combination with the attribute specified.
        BAD_STRUCTURE_MISSING = 0x80460000  # A mandatory structured parameter was missing or null.
        BAD_EVENT_FILTER_INVALID = 0x80470000  # The event filter is not valid.
        BAD_CONTENT_FILTER_INVALID = 0x80480000  # The content filter is not valid.
        BAD_FILTER_OPERATOR_INVALID = 0x80C10000  # An unrecognized operator was provided in a filter.
        BAD_FILTER_OPERATOR_UNSUPPORTED = 0x80C20000  # A valid operator was provided, but the server does not provide support for this filter operator.
        BAD_FILTER_OPERAND_COUNT_MISMATCH = 0x80C30000  # The number of operands provided for the filter operator was less then expected for the operand provided.
        BAD_FILTER_OPERAND_INVALID = 0x80490000  # The operand used in a content filter is not valid.
        BAD_FILTER_ELEMENT_INVALID = 0x80C40000  # The referenced element is not a valid element in the content filter.
        BAD_FILTER_LITERAL_INVALID = 0x80C50000  # The referenced literal is not a valid value.
        BAD_CONTINUATION_POINT_INVALID = 0x804A0000  # The continuation point provide is longer valid.
        BAD_NO_CONTINUATION_POINTS = 0x804B0000  # The operation could not be processed because all continuation points have been allocated.
        BAD_REFERENCE_TYPE_ID_INVALID = 0x804C0000  # The reference type id does not refer to a valid reference type node.
        BAD_BROWSE_DIRECTION_INVALID = 0x804D0000  # The browse direction is not valid.
        BAD_NODE_NOT_IN_VIEW = 0x804E0000  # The node is not part of the view.
        BAD_NUMERIC_OVERFLOW = 0x81120000  # The number was not accepted because of a numeric overflow.
        BAD_SERVER_URI_INVALID = 0x804F0000  # The ServerUri is not a valid URI.
        BAD_SERVER_NAME_MISSING = 0x80500000  # No ServerName was specified.
        BAD_DISCOVERY_URL_MISSING = 0x80510000  # No DiscoveryUrl was specified.
        BAD_SEMAPHORE_FILE_MISSING = 0x80520000  # The semaphore file specified by the client is not valid.
        BAD_REQUEST_TYPE_INVALID = 0x80530000  # The security token request type is not valid.
        BAD_SECURITY_MODE_REJECTED = 0x80540000  # The security mode does not meet the requirements set by the server.
        BAD_SECURITY_POLICY_REJECTED = 0x80550000  # The security policy does not meet the requirements set by the server.
        BAD_TOO_MANY_SESSIONS = 0x80560000  # The server has reached its maximum number of sessions.
        BAD_USER_SIGNATURE_INVALID = 0x80570000  # The user token signature is missing or invalid.
        BAD_APPLICATION_SIGNATURE_INVALID = 0x80580000  # The signature generated with the client certificate is missing or invalid.
        BAD_NO_VALID_CERTIFICATES = 0x80590000  # The client did not provide at least one software certificate that is valid and meets the profile requirements for the server.
        BAD_IDENTITY_CHANGE_NOT_SUPPORTED = 0x80C60000  # The server does not support changing the user identity assigned to the session.
        BAD_REQUEST_CANCELLED_BY_REQUEST = 0x805A0000  # The request was cancelled by the client with the Cancel service.
        BAD_PARENT_NODE_ID_INVALID = 0x805B0000  # The parent node id does not to refer to a valid node.
        BAD_REFERENCE_NOT_ALLOWED = 0x805C0000  # The reference could not be created because it violates constraints imposed by the data model.
        BAD_NODE_ID_REJECTED = 0x805D0000  # The requested node id was reject because it was either invalid or server does not allow node ids to be specified by the client.
        BAD_NODE_ID_EXISTS = 0x805E0000  # The requested node id is already used by another node.
        BAD_NODE_CLASS_INVALID = 0x805F0000  # The node class is not valid.
        BAD_BROWSE_NAME_INVALID = 0x80600000  # The browse name is invalid.
        BAD_BROWSE_NAME_DUPLICATED = 0x80610000  # The browse name is not unique among nodes that share the same relationship with the parent.
        BAD_NODE_ATTRIBUTES_INVALID = 0x80620000  # The node attributes are not valid for the node class.
        BAD_TYPE_DEFINITION_INVALID = 0x80630000  # The type definition node id does not reference an appropriate type node.
        BAD_SOURCE_NODE_ID_INVALID = 0x80640000  # The source node id does not reference a valid node.
        BAD_TARGET_NODE_ID_INVALID = 0x80650000  # The target node id does not reference a valid node.
        BAD_DUPLICATE_REFERENCE_NOT_ALLOWED = 0x80660000  # The reference type between the nodes is already defined.
        BAD_INVALID_SELF_REFERENCE = 0x80670000  # The server does not allow this type of self reference on this node.
        BAD_REFERENCE_LOCAL_ONLY = 0x80680000  # The reference type is not valid for a reference to a remote server.
        BAD_NO_DELETE_RIGHTS = 0x80690000  # The server will not allow the node to be deleted.
        UNCERTAIN_REFERENCE_NOT_DELETED = 0x40BC0000  # The server was not able to delete all target references.
        BAD_SERVER_INDEX_INVALID = 0x806A0000  # The server index is not valid.
        BAD_VIEW_ID_UNKNOWN = 0x806B0000  # The view id does not refer to a valid view node.
        BAD_VIEW_TIMESTAMP_INVALID = 0x80C90000  # The view timestamp is not available or not supported.
        BAD_VIEW_PARAMETER_MISMATCH = 0x80CA0000  # The view parameters are not consistent with each other.
        BAD_VIEW_VERSION_INVALID = 0x80CB0000  # The view version is not available or not supported.
        UNCERTAIN_NOT_ALL_NODES_AVAILABLE = 0x40C00000  # The list of references may not be complete because the underlying system is not available.
        GOOD_RESULTS_MAY_BE_INCOMPLETE = 0x00BA0000  # The server should have followed a reference to a node in a remote server but did not. The result set may be incomplete.
        BAD_NOT_TYPE_DEFINITION = 0x80C80000  # The provided Nodeid was not a type definition nodeid.
        UNCERTAIN_REFERENCE_OUT_OF_SERVER = 0x406C0000  # One of the references to follow in the relative path references to a node in the address space in another server.
        BAD_TOO_MANY_MATCHES = 0x806D0000  # The requested operation has too many matches to return.
        BAD_QUERY_TOO_COMPLEX = 0x806E0000  # The requested operation requires too many resources in the server.
        BAD_NO_MATCH = 0x806F0000  # The requested operation has no match to return.
        BAD_MAX_AGE_INVALID = 0x80700000  # The max age parameter is invalid.
        BAD_SECURITY_MODE_INSUFFICIENT = 0x80E60000  # The operation is not permitted over the current secure channel.
        BAD_HISTORY_OPERATION_INVALID = 0x80710000  # The history details parameter is not valid.
        BAD_HISTORY_OPERATION_UNSUPPORTED = 0x80720000  # The server does not support the requested operation.
        BAD_INVALID_TIMESTAMP_ARGUMENT = 0x80BD0000  # The defined timestamp to return was invalid.
        BAD_WRITE_NOT_SUPPORTED = 0x80730000  # The server does not support writing the combination of value, status and timestamps provided.
        BAD_TYPE_MISMATCH = 0x80740000  # The value supplied for the attribute is not of the same type as the attribute's value.
        BAD_METHOD_INVALID = 0x80750000  # The method id does not refer to a method for the specified object.
        BAD_ARGUMENTS_MISSING = 0x80760000  # The client did not specify all of the input arguments for the method.
        BAD_NOT_EXECUTABLE = 0x81110000  # The executable attribute does not allow the execution of the method.
        BAD_TOO_MANY_SUBSCRIPTIONS = 0x80770000  # The server has reached its maximum number of subscriptions.
        BAD_TOO_MANY_PUBLISH_REQUESTS = 0x80780000  # The server has reached the maximum number of queued publish requests.
        BAD_NO_SUBSCRIPTION = 0x80790000  # There is no subscription available for this session.
        BAD_SEQUENCE_NUMBER_UNKNOWN = 0x807A0000  # The sequence number is unknown to the server.
        GOOD_RETRANSMISSION_QUEUE_NOT_SUPPORTED = 0x00DF0000  # The Server does not support retransmission queue and acknowledgement of sequence numbers is not available.
        BAD_MESSAGE_NOT_AVAILABLE = 0x807B0000  # The requested notification message is no longer available.
        BAD_INSUFFICIENT_CLIENT_PROFILE = 0x807C0000  # The client of the current session does not support one or more Profiles that are necessary for the subscription.
        BAD_STATE_NOT_ACTIVE = 0x80BF0000  # The sub-state machine is not currently active.
        BAD_ALREADY_EXISTS = 0x81150000  # An equivalent rule already exists.
        BAD_TCP_SERVER_TOO_BUSY = 0x807D0000  # The server cannot process the request because it is too busy.
        BAD_TCP_MESSAGE_TYPE_INVALID = 0x807E0000  # The type of the message specified in the header invalid.
        BAD_TCP_SECURE_CHANNEL_UNKNOWN = 0x807F0000  # The SecureChannelId and/or TokenId are not currently in use.
        BAD_TCP_MESSAGE_TOO_LARGE = 0x80800000  # The size of the message chunk specified in the header is too large.
        BAD_TCP_NOT_ENOUGH_RESOURCES = 0x80810000  # There are not enough resources to process the request.
        BAD_TCP_INTERNAL_ERROR = 0x80820000  # An internal error occurred.
        BAD_TCP_ENDPOINT_URL_INVALID = 0x80830000  # The server does not recognize the QueryString specified.
        BAD_REQUEST_INTERRUPTED = 0x80840000  # The request could not be sent because of a network interruption.
        BAD_REQUEST_TIMEOUT = 0x80850000  # Timeout occurred while processing the request.
        BAD_SECURE_CHANNEL_CLOSED = 0x80860000  # The secure channel has been closed.
        BAD_SECURE_CHANNEL_TOKEN_UNKNOWN = 0x80870000  # The token has expired or is not recognized.
        BAD_SEQUENCE_NUMBER_INVALID = 0x80880000  # The sequence number is not valid.
        BAD_PROTOCOL_VERSION_UNSUPPORTED = 0x80BE0000  # The applications do not have compatible protocol versions.
        BAD_CONFIGURATION_ERROR = 0x80890000  # There is a problem with the configuration that affects the usefulness of the value.
        BAD_NOT_CONNECTED = 0x808A0000  # The variable should receive its value from another variable, but has never been configured to do so.
        BAD_DEVICE_FAILURE = 0x808B0000  # There has been a failure in the device/data source that generates the value that has affected the value.
        BAD_SENSOR_FAILURE = 0x808C0000  # There has been a failure in the sensor from which the value is derived by the device/data source.
        BAD_OUT_OF_SERVICE = 0x808D0000  # The source of the data is not operational.
        BAD_DEADBAND_FILTER_INVALID = 0x808E0000  # The deadband filter is not valid.
        UNCERTAIN_NO_COMMUNICATION_LAST_USABLE_VALUE = 0x408F0000  # Communication to the data source has failed. The variable value is the last value that had a good quality.
        UNCERTAIN_LAST_USABLE_VALUE = 0x40900000  # Whatever was updating this value has stopped doing so.
        UNCERTAIN_SUBSTITUTE_VALUE = 0x40910000  # The value is an operational value that was manually overwritten.
        UNCERTAIN_INITIAL_VALUE = 0x40920000  # The value is an initial value for a variable that normally receives its value from another variable.
        UNCERTAIN_SENSOR_NOT_ACCURATE = 0x40930000  # The value is at one of the sensor limits.
        UNCERTAIN_ENGINEERING_UNITS_EXCEEDED = 0x40940000  # The value is outside of the range of values defined for this parameter.
        UNCERTAIN_SUB_NORMAL = 0x40950000  # The value is derived from multiple sources and has less than the required number of Good sources.
        GOOD_LOCAL_OVERRIDE = 0x00960000  # The value has been overridden.
        BAD_REFRESH_IN_PROGRESS = 0x80970000  # This Condition refresh failed, a Condition refresh operation is already in progress.
        BAD_CONDITION_ALREADY_DISABLED = 0x80980000  # This condition has already been disabled.
        BAD_CONDITION_ALREADY_ENABLED = 0x80CC0000  # This condition has already been enabled.
        BAD_CONDITION_DISABLED = 0x80990000  # Property not available, this condition is disabled.
        BAD_EVENT_ID_UNKNOWN = 0x809A0000  # The specified event id is not recognized.
        BAD_EVENT_NOT_ACKNOWLEDGEABLE = 0x80BB0000  # The event cannot be acknowledged.
        BAD_DIALOG_NOT_ACTIVE = 0x80CD0000  # The dialog condition is not active.
        BAD_DIALOG_RESPONSE_INVALID = 0x80CE0000  # The response is not valid for the dialog.
        BAD_CONDITION_BRANCH_ALREADY_ACKED = 0x80CF0000  # The condition branch has already been acknowledged.
        BAD_CONDITION_BRANCH_ALREADY_CONFIRMED = 0x80D00000  # The condition branch has already been confirmed.
        BAD_CONDITION_ALREADY_SHELVED = 0x80D10000  # The condition has already been shelved.
        BAD_CONDITION_NOT_SHELVED = 0x80D20000  # The condition is not currently shelved.
        BAD_SHELVING_TIME_OUT_OF_RANGE = 0x80D30000  # The shelving time not within an acceptable range.
        BAD_NO_DATA = 0x809B0000  # No data exists for the requested time range or event filter.
        BAD_BOUND_NOT_FOUND = 0x80D70000  # No data found to provide upper or lower bound value.
        BAD_BOUND_NOT_SUPPORTED = 0x80D80000  # The server cannot retrieve a bound for the variable.
        BAD_DATA_LOST = 0x809D0000  # Data is missing due to collection started/stopped/lost.
        BAD_DATA_UNAVAILABLE = 0x809E0000  # Expected data is unavailable for the requested time range due to an un-mounted volume, an off-line archive or tape, or similar reason for temporary unavailability.
        BAD_ENTRY_EXISTS = 0x809F0000  # The data or event was not successfully inserted because a matching entry exists.
        BAD_NO_ENTRY_EXISTS = 0x80A00000  # The data or event was not successfully updated because no matching entry exists.
        BAD_TIMESTAMP_NOT_SUPPORTED = 0x80A10000  # The client requested history using a timestamp format the server does not support (i.e requested ServerTimestamp when server only supports SourceTimestamp).
        GOOD_ENTRY_INSERTED = 0x00A20000  # The data or event was successfully inserted into the historical database.
        GOOD_ENTRY_REPLACED = 0x00A30000  # The data or event field was successfully replaced in the historical database.
        UNCERTAIN_DATA_SUB_NORMAL = 0x40A40000  # The value is derived from multiple values and has less than the required number of Good values.
        GOOD_NO_DATA = 0x00A50000  # No data exists for the requested time range or event filter.
        GOOD_MORE_DATA = 0x00A60000  # The data or event field was successfully replaced in the historical database.
        BAD_AGGREGATE_LIST_MISMATCH = 0x80D40000  # The requested number of Aggregates does not match the requested number of NodeIds.
        BAD_AGGREGATE_NOT_SUPPORTED = 0x80D50000  # The requested Aggregate is not support by the server.
        BAD_AGGREGATE_INVALID_INPUTS = 0x80D60000  # The aggregate value could not be derived due to invalid data inputs.
        BAD_AGGREGATE_CONFIGURATION_REJECTED = 0x80DA0000  # The aggregate configuration is not valid for specified node.
        GOOD_DATA_IGNORED = 0x00D90000  # The request specifies fields which are not valid for the EventType or cannot be saved by the historian.
        BAD_REQUEST_NOT_ALLOWED = 0x80E40000  # The request was rejected by the server because it did not meet the criteria set by the server.
        BAD_REQUEST_NOT_COMPLETE = 0x81130000  # The request has not been processed by the server yet.
        BAD_TRANSACTION_PENDING = 0x80E80000  # The operation is not allowed because a transaction is in progress.
        BAD_TICKET_REQUIRED = 0x811F0000  # The device identity needs a ticket before it can be accepted.
        BAD_TICKET_INVALID = 0x81200000  # The device identity needs a ticket before it can be accepted.
        GOOD_EDITED = 0x00DC0000  # The value does not come from the real source and has been edited by the server.
        GOOD_POST_ACTION_FAILED = 0x00DD0000  # There was an error in execution of these post-actions.
        UNCERTAIN_DOMINANT_VALUE_CHANGED = 0x40DE0000  # The related EngineeringUnit has been changed but the Variable Value is still provided based on the previous unit.
        GOOD_DEPENDENT_VALUE_CHANGED = 0x00E00000  # A dependent value has been changed but the change has not been applied to the device.
        BAD_DOMINANT_VALUE_CHANGED = 0x80E10000  # The related EngineeringUnit has been changed but this change has not been applied to the device. The Variable Value is still dependent on the previous unit but its status is currently Bad.
        UNCERTAIN_DEPENDENT_VALUE_CHANGED = 0x40E20000  # A dependent value has been changed but the change has not been applied to the device. The quality of the dominant variable is uncertain.
        BAD_DEPENDENT_VALUE_CHANGED = 0x80E30000  # A dependent value has been changed but the change has not been applied to the device. The quality of the dominant variable is Bad.
        GOOD_EDITED_DEPENDENT_VALUE_CHANGED = 0x01160000  # It is delivered with a dominant Variable value when a dependent Variable has changed but the change has not been applied.
        GOOD_EDITED_DOMINANT_VALUE_CHANGED = 0x01170000  # It is delivered with a dependent Variable value when a dominant Variable has changed but the change has not been applied.
        GOOD_EDITED_DOMINANT_VALUE_CHANGED_DEPENDENT_VALUE_CHANGED = 0x01180000  # It is delivered with a dependent Variable value when a dominant or dependent Variable has changed but change has not been applied.
        BAD_EDITED_OUT_OF_RANGE = 0x81190000  # It is delivered with a Variable value when Variable has changed but the value is not legal.
        BAD_INITIAL_VALUE_OUT_OF_RANGE = 0x811A0000  # It is delivered with a Variable value when a source Variable has changed but the value is not legal.
        BAD_OUT_OF_RANGE_DOMINANT_VALUE_CHANGED = 0x811B0000  # It is delivered with a dependent Variable value when a dominant Variable has changed and the value is not legal.
        BAD_EDITED_OUT_OF_RANGE_DOMINANT_VALUE_CHANGED = 0x811C0000  # It is delivered with a dependent Variable value when a dominant Variable has changed, the value is not legal and the change has not been applied.
        BAD_OUT_OF_RANGE_DOMINANT_VALUE_CHANGED_DEPENDENT_VALUE_CHANGED = 0x811D0000  # It is delivered with a dependent Variable value when a dominant or dependent Variable has changed and the value is not legal.
        BAD_EDITED_OUT_OF_RANGE_DOMINANT_VALUE_CHANGED_DEPENDENT_VALUE_CHANGED = 0x811E0000  # It is delivered with a dependent Variable value when a dominant or dependent Variable has changed, the value is not legal and the change has not been applied.
        GOOD_COMMUNICATION_EVENT = 0x00A70000  # The communication layer has raised an event.
        GOOD_SHUTDOWN_EVENT = 0x00A80000  # The system is shutting down.
        GOOD_CALL_AGAIN = 0x00A90000  # The operation is not finished and needs to be called again.
        GOOD_NON_CRITICAL_TIMEOUT = 0x00AA0000  # A non-critical timeout occurred.
        BAD_INVALID_ARGUMENT = 0x80AB0000  # One or more arguments are invalid.
        BAD_CONNECTION_REJECTED = 0x80AC0000  # Could not establish a network connection to remote server.
        BAD_DISCONNECT = 0x80AD0000  # The server has disconnected from the client.
        BAD_CONNECTION_CLOSED = 0x80AE0000  # The network connection has been closed.
        BAD_INVALID_STATE = 0x80AF0000  # The operation cannot be completed because the object is closed, uninitialized or in some other invalid state.
        BAD_END_OF_STREAM = 0x80B00000  # Cannot move beyond end of the stream.
        BAD_NO_DATA_AVAILABLE = 0x80B10000  # No data is currently available for reading from a non-blocking stream.
        BAD_WAITING_FOR_RESPONSE = 0x80B20000  # The asynchronous operation is waiting for a response.
        BAD_OPERATION_ABANDONED = 0x80B30000  # The asynchronous operation was abandoned by the caller.
        BAD_EXPECTED_STREAM_TO_BLOCK = 0x80B40000  # The stream did not return all data requested (possibly because it is a non-blocking stream).
        BAD_WOULD_BLOCK = 0x80B50000  # Non blocking behaviour is required and the operation would block.
        BAD_SYNTAX_ERROR = 0x80B60000  # A value had an invalid syntax.
        BAD_MAX_CONNECTIONS_REACHED = 0x80B70000  # The operation could not be finished because all available connections are in use.
        # fmt: on

    class NodeId:
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, numericNs0Id: int, /) -> None: ...
        @overload
        def __init__(self, parseStr: str, /) -> None: ...
        @overload
        def __init__(self, hasNodeId: HasNodeId, /) -> None: ...
        @overload
        def __init__(self, registeredType: type[Any], /) -> None: ...
        @overload
        def __init__(self, other: NodeId, /) -> None: ...
        @overload
        def __init__(self, expandedNodeId: ExpandedNodeId, /) -> None: ...
        @overload
        def __init__(self, nop: None, /) -> None: ...
        @overload
        def __init__(self, *, ns: int = 0, i: int) -> None: ...
        @overload
        def __init__(self, *, ns: int = 0, s: str) -> None: ...
        @overload
        def __init__(self, *, ns: int = 0, b: bytes) -> None: ...
        @overload
        def __init__(self, *, ns: int = 0, g: UUID) -> None: ...
        def __init__(self, *args: Any, **kwargs: Any) -> None: ...
        @property
        def ns(self) -> NamespaceModule | int: ...
        @property
        def id(self) -> int | str | bytes | UUID: ...
        def __eq__(self, other: object, /) -> bool: ...
        def __ne__(self, other: object, /) -> bool: ...
        def __hash__(self) -> int: ...
        def __str__(self) -> str: ...
        def __repr__(self) -> str: ...

    class ExpandedNodeId:
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, parseStr: str, /) -> None: ...
        @overload
        def __init__(self, nodeId: NodeId, /) -> None: ...
        def __init__(self, *args: Any, **kwargs: Any) -> None: ...
        @property
        def ns(self) -> NamespaceModule | int: ...
        @property
        def id(self) -> int | str | bytes | UUID: ...
        @property
        def nsu(self) -> str: ...
        @property
        def svr(self) -> int: ...

    class QualifiedName:
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, ns: int, name: str, /) -> None: ...
        @overload
        def __init__(self, name: str, /) -> None: ...
        def __init__(self, *args: Any, **kwargs: Any) -> None: ...
        @property
        def ns(self) -> NamespaceModule | int: ...
        @property
        def name(self) -> str: ...

    class LocalizedText:
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, lt: LocalizedText, /) -> None: ...
        @overload
        def __init__(self, text: str, /) -> None: ...
        @overload
        def __init__(self, locale: str, text: str, /) -> None: ...
        def __init__(self, *args: Any, **kwargs: Any) -> None: ...
        @property
        def locale(self) -> str: ...
        @property
        def text(self) -> str: ...

    class ExtensionObject:
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, body: Any | None, /) -> None: ...
        @overload
        def __init__(self, typeId: NodeIdLike, body: str | bytes, /) -> None: ...
        def __init__(self, *args: Any, **kwargs: Any) -> None: ...
        @property
        def typeId(self) -> NodeId | None: ...
        @property
        def body(self) -> Any | None: ...

    class DataValue:
        def __init__(self) -> None: ...
        @property
        def value(self) -> Any: ...
        @value.setter
        def value(self, val: Any, /) -> None: ...
        @property
        def status(self) -> StatusCode | None: ...
        @status.setter
        def status(self, val: StatusCode | None, /) -> None: ...
        @property
        def sourceTimestamp(self) -> DateTime | None: ...
        @sourceTimestamp.setter
        def sourceTimestamp(self, val: DateTime | None, /) -> None: ...
        @property
        def serverTimestamp(self) -> DateTime | None: ...
        @serverTimestamp.setter
        def serverTimestamp(self, val: DateTime | None, /) -> None: ...
        @property
        def sourcePicoseconds(self) -> int | None: ...
        @sourcePicoseconds.setter
        def sourcePicoseconds(self, val: int | None, /) -> None: ...
        @property
        def serverPicoseconds(self) -> int | None: ...
        @serverPicoseconds.setter
        def serverPicoseconds(self, val: int | None, /) -> None: ...

    class DiagnosticInfo:
        """OPC UA DiagnosticInfo (builtin type).

        Each of the fields below is optional: the underlying UA_DiagnosticInfo
        carries a per-field ``has*`` bit, so reading a field that is not set
        returns ``None`` and writing ``None`` clears the field.
        """

        def __init__(
            self,
            symbolicId: int | None = ...,
            namespaceUri: int | None = ...,
            localizedText: int | None = ...,
            locale: int | None = ...,
            additionalInfo: str | None = ...,
            innerStatusCode: StatusCode | None = ...,
            innerDiagnosticInfo: DiagnosticInfo | None = ...,
        ) -> None: ...
        @property
        def symbolicId(self) -> int | None: ...
        @symbolicId.setter
        def symbolicId(self, val: int | None, /) -> None: ...
        @property
        def namespaceUri(self) -> int | None: ...
        @namespaceUri.setter
        def namespaceUri(self, val: int | None, /) -> None: ...
        @property
        def localizedText(self) -> int | None: ...
        @localizedText.setter
        def localizedText(self, val: int | None, /) -> None: ...
        @property
        def locale(self) -> int | None: ...
        @locale.setter
        def locale(self, val: int | None, /) -> None: ...
        @property
        def additionalInfo(self) -> str | None: ...
        @additionalInfo.setter
        def additionalInfo(self, val: str | None, /) -> None: ...
        @property
        def innerStatusCode(self) -> StatusCode: ...
        @innerStatusCode.setter
        def innerStatusCode(self, val: StatusCode | None, /) -> None: ...
        @property
        def innerDiagnosticInfo(self) -> DiagnosticInfo | None: ...
        @innerDiagnosticInfo.setter
        def innerDiagnosticInfo(self, val: DiagnosticInfo | None, /) -> None: ...

    _NativeT = TypeVar("_NativeT")

    def encodeBinary(obj: Any) -> bytes: ...
    def decodeBinary(data: bytes, datatype: type[_NativeT]) -> _NativeT: ...
    def encodeXml(obj: Any) -> bytes: ...
    def decodeXml(data: bytes | str, datatype: type[_NativeT]) -> _NativeT: ...
    def encodeJson(obj: Any) -> bytes: ...
    def decodeJson(data: bytes, dataType: type[_NativeT]) -> _NativeT: ...

    import logging

    class ClientConfig:
        logger: logging.Logger  # write-only
        timeout: int
        endpointUrl: str
        endpoint: ns0.datatypes.EndpointDescription
        securityMode: int
        securityPolicyUri: str
        securityPolicy: str  # enum-friendly alias; setter also accepts SecurityPolicy
        applicationUri: str
        applicationDescription: ns0.datatypes.ApplicationDescription
        userIdentityToken: Any
        userTokenPolicy: ns0.datatypes.UserTokenPolicy
        noSession: bool
        noReconnect: bool
        noNewSession: bool
        tcpReuseAddr: bool
        allowNonePolicyPassword: bool
        sessionName: str
        secureChannelLifeTime: int
        requestedSessionTimeout: int
        connectivityCheckInterval: int
        outstandingPublishRequests: int
        authSecurityPolicyUri: str
        maxTrustListSize: int
        maxRejectedListSize: int
        sessionLocaleIds: list[str]
        namespaces: list[str]
        sendBufferSize: int
        recvBufferSize: int
        localMaxMessageSize: int
        localMaxChunkCount: int

        @property
        def certificate(self) -> bytes | None: ...
        @certificate.setter
        def certificate(self, value: str | Path | bytes | None) -> None: ...
        @property
        def privateKey(self) -> bytes | None: ...
        @privateKey.setter
        def privateKey(self, value: str | Path | bytes | None) -> None: ...
        @property
        def trustList(self) -> list[bytes]: ...
        @trustList.setter
        def trustList(self, value: list[str | Path | bytes] | None) -> None: ...
        @property
        def revocationList(self) -> list[bytes]: ...
        @revocationList.setter
        def revocationList(self, value: list[str | Path | bytes] | None) -> None: ...
        def setUsernamePassword(self, username: str, password: str) -> None: ...
        def setCredentials(self, username: str, password: str) -> None: ...
        def _finalize_encryption(self) -> None: ...
        def setEncryption(
            self,
            certificate: bytes,
            privateKey: bytes,
            trustList: list[bytes],
            revocationList: list[bytes],
        ) -> None: ...
        def setAuthenticationCert(self, certificate: bytes, privateKey: bytes) -> None: ...

    class StatusCodeError(Exception):
        code: int
        symbol: str

        def __init__(self, status_code: StatusCode | int) -> None: ...

    class NamespaceModule(Protocol):
        shortname: str
        uri: str
        scope: str
        version: str
        publicationDate: str
        index: int

    class _NamespacePackage(Protocol):
        def register(
            self,
            shortname: str,
            uri: str,
            *,
            scope: str | None = None,
            version: str | None = None,
            publicationDate: str | None = None,
        ) -> NamespaceModule: ...

        def filter(
            self,
            *,
            uri: str | None = None,
            scope: str | None = None,
            version: str | None = None,
        ) -> list[NamespaceModule]: ...

        def __getitem__(self, key: int | str | NodeId) -> NamespaceModule | Any: ...
        def __contains__(self, key: object) -> bool: ...
        def __iter__(self) -> Generator[str, None, None]: ...
        def __len__(self) -> int: ...
        def namespace(
            self,
            shortname: str,
            uri: str,
            version: str = "1.0",
            publicationDate: str = "",
        ) -> None: ...

    ns: _NamespacePackage

    def logTrace(logger: logging.Logger, message: str, category: str = "") -> None: ...
    def logDebug(logger: logging.Logger, message: str, category: str = "") -> None: ...
    def logInfo(logger: logging.Logger, message: str, category: str = "") -> None: ...
    def logWarning(logger: logging.Logger, message: str, category: str = "") -> None: ...
    def logError(logger: logging.Logger, message: str, category: str = "") -> None: ...
    def logFatal(logger: logging.Logger, message: str, category: str = "") -> None: ...


# =============================================================================
# Native runtime bindings
# =============================================================================

# Re-export the OPC UA builtin types at the top level so that `o6.NodeId`, `o6.Int32` etc. work without going through `o6.ns.ns0`.
# These are the 25 primitive types from `UA_DATATYPEKIND_*`; non-builtin NS0 struct and enum types live under `o6.ns.ns0` instead.
if not TYPE_CHECKING:
    from o6._o6 import types as _types

    # Primitive types
    Boolean = _types.Boolean
    SByte = _types.SByte
    Byte = _types.Byte
    Int16 = _types.Int16
    UInt16 = _types.UInt16
    Int32 = _types.Int32
    UInt32 = _types.UInt32
    Int64 = _types.Int64
    UInt64 = _types.UInt64
    Float = _types.Float
    Double = _types.Double
    String = _types.String
    DateTime = _types.DateTime
    Guid = _types.Guid
    ByteString = _types.ByteString
    XmlElement = _types.XmlElement
    # opc ua specific types
    NodeId = _types.NodeId
    ExpandedNodeId = _types.ExpandedNodeId
    StatusCode = _types.StatusCode
    QualifiedName = _types.QualifiedName
    LocalizedText = _types.LocalizedText
    # abscract umbrella types
    ExtensionObject = _types.ExtensionObject
    DataValue = _types.DataValue
    DiagnosticInfo = _types.DiagnosticInfo

    # Encoding / decoding helpers exposed by the C extension's types
    # submodule.  These aren't types themselves but they are useful as
    # ``o6.encodeBinary(x)`` / ``o6.decodeBinary(s, T)`` shortcuts.
    encodeBinary = _types.encodeBinary
    decodeBinary = _types.decodeBinary
    encodeXml = _types.encodeXml
    decodeXml = _types.decodeXml
    encodeJson = _types.encodeJson
    decodeJson = _types.decodeJson

    StatusCodeError = _o6.StatusCodeError

    def _status_code_check(
        self: StatusCode,
        expected: StatusCode = StatusCode.GOOD,
        message: str | None = None,
    ) -> None:
        if self == expected:
            return
        error = StatusCodeError(self)
        if message:
            error.add_note(message)
        raise error

    StatusCode.check = _status_code_check
    del _status_code_check

    ClientConfig = _o6.ClientConfig
    logTrace = _o6.logTrace
    logDebug = _o6.logDebug
    logInfo = _o6.logInfo
    logWarning = _o6.logWarning
    logError = _o6.logError
    logFatal = _o6.logFatal


# =============================================================================
# Public protocols and type aliases
# =============================================================================

_T = TypeVar("_T")
MaybeAwaitable: TypeAlias = _T | Awaitable[_T]

IndexRange: TypeAlias = None | str | slice | tuple[slice, ...]
"""No range, an OPC UA index-range string, or a Python slice representation.

For example, ``"2:5"``, ``slice(2, 6)``, and ``(slice(2, 6),)`` describe the
same range. A bare slice is shorthand for a one-dimensional range.
Multi-dimensional range ``"1:3,4:6"`` is equivalent to
``(slice(1, 4), slice(4, 7))``. Slice steps and open-ended slices are not
supported because OPC UA NumericRange dimensions require explicit bounds.
``None`` selects the complete value.
"""


# Protocol for classes with a member "_nodeid" of type NodeId. The native NodeId
# constructor checks the argument for a _nodeid member and makes a copy if
# present.
class HasNodeId(Protocol):
    """Anything that carries a ``_nodeid`` attribute of type [`NodeId`](../types-addrspace/bulitin/address-types/#nodeId).

    The native `NodeId` constructor recognises this protocol and copies
    the wrapped NodeId when a ``HasNodeId`` is passed inside."""

    _nodeid: NodeId


# Type that can be used to initialize a NodeId
NodeIdLike: TypeAlias = NodeId | str | HasNodeId | ExpandedNodeId | type[Any]

# Type that can be used to initialize a LocalizedText
LocalizedTextLike: TypeAlias = LocalizedText | str

# =============================================================================
# Generated NS0 enhancements
# =============================================================================


def _patch_DataChangeFilter(_DCF: Any, _DataChangeTrigger: type) -> None:
    _orig_init = _DCF.__init__

    def __init__(
        self,
        trigger=None,
        deadbandType: Optional[int] = None,
        deadbandValue: Optional[float] = None,
    ) -> None:
        _orig_init(self)
        if trigger is not None:
            if isinstance(trigger, int):
                trigger = _DataChangeTrigger(trigger)
            self.trigger = trigger
        if deadbandType is not None:
            self.deadbandType = deadbandType
        if deadbandValue is not None:
            self.deadbandValue = deadbandValue

    _DCF.__init__ = __init__  # type: ignore[assignment]


def _patch_RelativePath(_RP: Any) -> None:
    _orig_init = _RP.__init__
    parse = _types._parseRelativePath
    print_value = _types._printRelativePath

    def __init__(self, input: Optional[str] = None) -> None:
        _orig_init(self)
        if isinstance(input, str):
            res = parse(input)
            self.elements = res.elements

    def __str__(self) -> str:
        return print_value(self)

    _RP.__init__ = __init__  # type: ignore[assignment]
    _RP.__str__ = __str__  # type: ignore[method-assign]


def _patch_SimpleAttributeOperand(_SAO: Any) -> None:
    _orig_init = _SAO.__init__
    parse = _types._parseSimpleAttributeOperand
    print_value = _types._printSimpleAttributeOperand

    def __init__(self, input: Optional[str] = None) -> None:
        _orig_init(self)
        if isinstance(input, str):
            res = parse(input)
            self.typeDefinitionId = res.typeDefinitionId
            self.browsePath = res.browsePath
            self.attributeId = res.attributeId
            self.indexRange = res.indexRange

    def __str__(self) -> str:
        return print_value(self)

    _SAO.__init__ = __init__  # type: ignore[assignment]
    _SAO.__str__ = __str__  # type: ignore[method-assign]


def _patch_ReadValueId(_RVI: Any) -> None:
    _orig_init = _RVI.__init__
    parse = _types._parseReadValueId
    print_value = _types._printReadValueId

    def __init__(self, input: Optional[str] = None) -> None:
        _orig_init(self)
        if isinstance(input, str):
            res = parse(input)
            self.nodeId = res.nodeId
            self.attributeId = res.attributeId
            self.indexRange = res.indexRange
            self.dataEncoding = res.dataEncoding

    def __str__(self) -> str:
        return print_value(self)

    _RVI.__init__ = __init__  # type: ignore[assignment]
    _RVI.__str__ = __str__  # type: ignore[method-assign]


def _patch_EventFilter_parse(ns0_module) -> None:
    """Expose ``EventFilter.parse(query, logger=...)`` on the decorated
    ``EventFilter`` class.  The C extension attaches this classmethod to its
    own ``EventFilter`` type; it builds the result via ``UA2PY`` (which
    resolves to the decorated class), so we just delegate to it.  Only
    present when the C extension was built with event-subscription + JSON
    support."""
    c_parse = getattr(_types, "_parseEventFilter", None)
    if c_parse is None:
        return

    def parse(cls, query: str, logger: Any = None) -> Any:
        return c_parse(query, logger=logger)

    ns0_module.EventFilter.parse = classmethod(parse)


# =============================================================================
# Declarative API
# =============================================================================

# NS0 uses these decorators while it is imported below, so bind them before
# bootstrapping the generated namespace.
from ._decorators import (
    call,
    objecttype,
    referencetype,
    variabletype,
    view,
)
from ._datatype_registration import datatype, enumfield, enumtype, field
from ._server_types import read, write
from ._references import (
    addInOf,
    componentOf,
    eventSourceOf,
    generatedBy,
    generatesEvent,
    hasAddIn,
    hasComponent,
    hasCondition,
    hasEncoding,
    hasEventSource,
    hasInterface,
    hasNotifier,
    hasOrderedComponent,
    hasProperty,
    interfaceOf,
    isConditionOf,
    notifierOf,
    orderedComponentOf,
    organizedBy,
    organizes,
    propertyOf,
    reference,
)

# =============================================================================
# NS0 bootstrap
# =============================================================================

# Import the auto-generated NS0 nodeset so all 45 NS0 enums and 367 NS0
# structures are registered via the @o6.datatype / @o6.enumtype decorators.
# Each @o6.enumtype registration dedups against the canonical UA_TYPES[]
from .ns import ns0 as _ns0

# Now that the decorated NS0 classes exist, patch the special helper types
# in place.
_patch_DataChangeFilter(_ns0.datatypes.DataChangeFilter, _ns0.datatypes.DataChangeTrigger)
_patch_RelativePath(_ns0.datatypes.RelativePath)
_patch_SimpleAttributeOperand(_ns0.datatypes.SimpleAttributeOperand)
_patch_ReadValueId(_ns0.datatypes.ReadValueId)
_patch_EventFilter_parse(_ns0.datatypes)


# =============================================================================
# High-level API
# =============================================================================

from . import client, common, node, ns, pubsub, server, subscription, util
from .node import Node
from .subscription import MonitoredItem, Subscription
from .client import Client
from .server import (
    AccessControl,
    Event,
    NodePermissions,
    Role,
    Server,
    Session,
    SessionActivation,
    roles,
)


def __dir__() -> list[str]:
    return sorted(__all__)


__all__ = [
    "AccessControl",
    "AccessLevel",
    "AttributeId",
    "Boolean",
    "Byte",
    "ByteString",
    "Client",
    "ClientConfig",
    "DataValue",
    "DateTime",
    "DiagnosticInfo",
    "Double",
    "Event",
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
    "MonitoredItem",
    "Node",
    "NodeId",
    "NodeIdLike",
    "NodePermissions",
    "Permission",
    "QualifiedName",
    "Role",
    "SByte",
    "SecureChannelState",
    "SecurityMode",
    "SecurityPolicy",
    "Server",
    "Session",
    "SessionActivation",
    "SessionState",
    "StatusCode",
    "StatusCodeError",
    "String",
    "Subscription",
    "UInt16",
    "UInt32",
    "UInt64",
    "ValueRank",
    "WriteMask",
    "XmlElement",
    "addInOf",
    "call",
    "client",
    "common",
    "componentOf",
    "datatype",
    "decodeBinary",
    "decodeJson",
    "decodeXml",
    "encodeBinary",
    "encodeJson",
    "encodeXml",
    "enumfield",
    "enumtype",
    "eventSourceOf",
    "field",
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
    "logDebug",
    "logError",
    "logFatal",
    "logInfo",
    "logTrace",
    "logWarning",
    "node",
    "notifierOf",
    "ns",
    "objecttype",
    "orderedComponentOf",
    "organizedBy",
    "organizes",
    "propertyOf",
    "pubsub",
    "read",
    "reference",
    "referencetype",
    "roles",
    "server",
    "subscription",
    "util",
    "variabletype",
    "view",
    "write",
]

# =============================================================================
# Private cleanup
# =============================================================================

# The native extension is an implementation detail. Public native types have
# already been installed above.
del _o6, _types, _ns0, annotations
del datetime, Path, UUID
del (
    TYPE_CHECKING,
    Any,
    Awaitable,
    Generator,
    Optional,
    Protocol,
    TypeAlias,
    TypeVar,
    Union,
    overload,
)
