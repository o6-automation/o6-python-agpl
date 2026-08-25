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

from typing import Any, Sequence, SupportsFloat

import numpy as np

_Integer = int | np.integer[Any]

_Boolean = bool | np.bool_

import enum

from o6.node import ObjectNode as _ObjectNode, VariableNode as _VariableNode

import uuid

import o6

import o6.ns.ns0 as ns0

class BACnetReliability(enum.IntFlag):
    NO_FAULT_DETECTED = 0
    NO_SENSOR = 1
    OVER_RANGE = 2
    UNDER_RANGE = 3
    OPEN_LOOP = 4
    SHORTED_LOOP = 5
    NO_OUTPUT = 6
    UNRELIABLE_OTHER = 7
    PROCESS_ERROR = 8
    MULTI_STATE_FAULT = 9
    CONFIGURATION_ERROR = 10
    COMMUNICATION_FAILURE = 12
    MEMBER_FAULT = 13
    MONITORED_OBJECT_FAULT = 14
    TRIPPED = 15

class BACnetNotifyType(enum.IntFlag):
    ALARM = 0
    EVENT = 1
    ACK_NOTIFICATION = 2

class BACnetEventState(enum.IntFlag):
    NORMAL = 0
    FAULT = 1
    OFF_NORMAL = 2
    HIGH_LIMIT = 3
    LOW_LIMIT = 4
    LIFE_SAFETY_ALARM = 5

class BACnetBinaryPV(enum.IntFlag):
    INACTIVE = 0
    ACTIVE = 1

class BACnetPolarity(enum.IntFlag):
    NORMAL = 0
    REVERSE = 1

class BACnetAction(enum.IntFlag):
    DIRECT = 0
    REVERSE = 1

class BACnetElementCount:
    pass

class BACnetPropertyCount:
    pass

class BACnetObjectCount:
    pass

class BACnetDeviceCount:
    pass

class BACnetMonth(enum.IntFlag):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12
    ODD = 13
    EVEN = 14
    UNSPECIFIED = 255

class BACnetYear:
    """0 = Undefined"""

class BACnetDeviceCommunicationEnabled(enum.IntFlag):
    ENABLE = 0
    DISABLE = 1
    DISABLE_INITIATION = 2

class BACnetTime(ns0.datatypes.Structure):
    @property
    def hour(self) -> o6.Byte: ...
    @hour.setter
    def hour(self, value: _Integer) -> None: ...
    @property
    def minute(self) -> o6.Byte: ...
    @minute.setter
    def minute(self, value: _Integer) -> None: ...
    @property
    def second(self) -> o6.Byte: ...
    @second.setter
    def second(self, value: _Integer) -> None: ...
    @property
    def hundredths(self) -> o6.Byte: ...
    @hundredths.setter
    def hundredths(self, value: _Integer) -> None: ...

class BACnetObjectIdentifier:
    pass

class BACnetDay(enum.IntFlag):
    DAYS_NUMBERED_1_7 = 1
    DAYS_NUMBERED_8_14 = 2
    DAYS_NUMBERED_15_21 = 3
    DAYS_NUMBERED_22_28 = 4
    DAYS_NUMBERED_29_31 = 5
    LAST_7_DAYS_OF_THIS_MONTH = 6
    ANY_WEEK_OF_THIS_MONTH = 255

class BACnetAddress(ns0.datatypes.Structure):
    @property
    def networkNumber(self) -> o6.UInt16: ...
    @networkNumber.setter
    def networkNumber(self, value: _Integer) -> None: ...
    @property
    def macAddress(self) -> o6.ByteString: ...
    @macAddress.setter
    def macAddress(self, value: o6.ByteString) -> None: ...

class BACnetClientCOV(ns0.datatypes.Union):
    @property
    def real_increment(self) -> o6.Float: ...
    @real_increment.setter
    def real_increment(self, value: SupportsFloat) -> None: ...

class BACnetDayOfMonth(enum.IntFlag):
    LAST_DAY_OF_MONTH = 32
    ODD_DAY_OF_MONTH = 33
    EVEN_DAY_OF_MONTH = 34
    UNSPECIFIED = 255

class BACnetEventEnumType(enum.IntFlag):
    CHANGE_OF_BITSTRING = 0
    CHANGE_OF_STATE = 1
    CHANGE_OF_VALUE = 2
    COMMAND_FAILURE = 3
    FLOATING_LIMIT = 4
    OUT_OF_RANGE = 5
    CHANGE_OF_LIFE_SAFETY = 8
    EXTENDED = 9
    BUFFER_READY = 10
    UNSIGNED_RANGE = 11

class BACnetProgramRequest(enum.IntFlag):
    READY = 0
    LOAD = 1
    RUN = 2
    HALT = 3
    RESTART = 4
    UNLOAD = 5

class BACnetProgramStates(enum.IntFlag):
    IDLE = 0
    LOADING = 1
    RUNNING = 2
    WAITING = 3
    HALTED = 4
    UNLOADING = 5

class BACnetProgramError(enum.IntFlag):
    NORMAL = 0
    LOAD_FAILED = 1
    INTERNAL = 2
    PROGRAM = 3
    OTHER = 4

class BACnetDeviceStatus(enum.IntFlag):
    OPERATIONAL = 0
    OPERATIONAL_READ_ONLY = 1
    DOWNLOAD_REQUIRED = 2
    DOWNLOAD_IN_PROGRESS = 3
    NON_OPERATIONAL = 4
    BACKUP_IN_PROGRESS = 5

class BACnetLifeSafetyMode(enum.IntFlag):
    OFF = 0
    ON = 1
    TEST = 2
    MANNED = 3
    UN_MANNED = 4
    ARMED = 5
    DISARMED = 6
    PREARMED = 7
    SLOW = 8
    FAST = 9
    DISCONNECTED = 10
    ENABLED = 11
    DISABLED = 12
    AUTOMATIC_RELEASE_DISABLED = 13
    DEFAULT = 14

class BACnetLifeSafetyState(enum.IntFlag):
    QUIET = 0
    PRE_ALARM = 1
    ALARM = 2
    FAULT = 3
    FAULT_PRE_ALARM = 4
    FAULT_ALARM = 5
    NOT_READY = 6
    ACTIVE = 7
    TAMPER = 8
    TEST_ALARM = 9
    TEST_ACTIVE = 10
    TEST_FAULT = 11
    TEST_FAULT_ALARM = 12
    HOLDUP = 13
    DURESS = 14
    TAMPER_ALARM = 15
    ABNORMAL = 16
    EMERGENCY_POWER = 17
    DELAYED = 18
    BLOCKED = 19
    LOCAL_ALARM = 20
    GENERAL_ALARM = 21
    SUPERVISORY = 22
    TEST_SUPERVISORY = 23

class BACnetPropertyStates(ns0.datatypes.Structure):
    @property
    def booleanValue(self) -> o6.Boolean: ...
    @booleanValue.setter
    def booleanValue(self, value: _Boolean) -> None: ...
    @property
    def binaryValue(self) -> BACnetBinaryPV: ...
    @binaryValue.setter
    def binaryValue(self, value: _Integer) -> None: ...
    @property
    def eventType(self) -> BACnetEventEnumType: ...
    @eventType.setter
    def eventType(self, value: _Integer) -> None: ...
    @property
    def polarity(self) -> BACnetPolarity: ...
    @polarity.setter
    def polarity(self, value: _Integer) -> None: ...
    @property
    def programChange(self) -> BACnetProgramRequest: ...
    @programChange.setter
    def programChange(self, value: _Integer) -> None: ...
    @property
    def programState(self) -> BACnetProgramStates: ...
    @programState.setter
    def programState(self, value: _Integer) -> None: ...
    @property
    def programError(self) -> BACnetProgramError: ...
    @programError.setter
    def programError(self, value: _Integer) -> None: ...
    @property
    def reliability(self) -> BACnetReliability: ...
    @reliability.setter
    def reliability(self, value: _Integer) -> None: ...
    @property
    def state(self) -> BACnetEventState: ...
    @state.setter
    def state(self, value: _Integer) -> None: ...
    @property
    def systemStatus(self) -> BACnetDeviceStatus: ...
    @systemStatus.setter
    def systemStatus(self, value: _Integer) -> None: ...
    @property
    def units(self) -> ns0.datatypes.EUInformation: ...
    @units.setter
    def units(self, value: ns0.datatypes.EUInformation) -> None: ...
    @property
    def unsignedValue(self) -> o6.UInt32: ...
    @unsignedValue.setter
    def unsignedValue(self, value: _Integer) -> None: ...
    @property
    def lifeSafetyMode(self) -> BACnetLifeSafetyMode: ...
    @lifeSafetyMode.setter
    def lifeSafetyMode(self, value: _Integer) -> None: ...
    @property
    def lifeSafetyState(self) -> BACnetLifeSafetyState: ...
    @lifeSafetyState.setter
    def lifeSafetyState(self, value: _Integer) -> None: ...

class BACnetLifeSafetyOperation(enum.IntFlag):
    NONE = 0
    SILENCE = 1
    SILENCE_AUDIBLE = 2
    SILENCE_VISIBLE = 3
    RESET = 4
    RESET_ALARM = 5
    RESET_FAULT = 6
    UNSILENCE = 7
    UNSILENCE_AUDIBLE = 8
    UNSILENCE_VISIBLE = 9

class BACnetEventParameterChangeOfLifeSafety(ns0.datatypes.Structure):
    @property
    def newState(self) -> BACnetLifeSafetyState: ...
    @newState.setter
    def newState(self, value: _Integer) -> None: ...
    @property
    def newMode(self) -> BACnetLifeSafetyMode: ...
    @newMode.setter
    def newMode(self, value: _Integer) -> None: ...
    @property
    def operationExtended(self) -> BACnetLifeSafetyOperation: ...
    @operationExtended.setter
    def operationExtended(self, value: _Integer) -> None: ...

class BACnetNodeType(enum.IntFlag):
    UNKNOWN = 0
    SYSTEM = 1
    NETWORK = 2
    DEVICE = 3
    ORGANIZATIONAL = 4
    AREA = 5
    EQUIPMENT = 6
    POINT = 7
    COLLECTION = 8
    PROPERTY = 9
    FUNCTIONAL = 10
    OTHER = 11

class BACnetPropertyIdentifier(enum.IntFlag):
    ACKED_TRANSITIONS = 0
    ACK_REQUIRED = 1
    ACTION = 2
    ACTION_TEXT = 3
    ACTIVE_TEXT = 4
    ACTIVE_VT_SESSIONS = 5
    ALARM_VALUE = 6
    ALARM_VALUES = 7
    ALL = 8
    ALL_WRITES_SUCCESSFUL = 9
    APDU_SEGMENT_TIMEOUT = 10
    APDU_TIMEOUT = 11
    APPLICATION_SOFTWARE_VERSION = 12
    ARCHIVE = 13
    BIAS = 14
    CHANGE_OF_STATE_COUNT = 15
    CHANGE_OF_STATE_TIME = 16
    NOTIFICATION_CLASS = 17
    THIS_PROPERTY_DELETED = 18
    CONTROLLED_VARIABLE_REFERENCE = 19
    CONTROLLED_VARIABLE_UNITS = 20
    CONTROLLED_VARIABLE_VALUE = 21
    COV_INCREMENT = 22
    DATE_LIST = 23
    DAYLIGHT_SAVINGS_STATUS = 24
    DEADBAND = 25
    DERIVATIVE_CONSTANT = 26
    DERIVATIVE_CONSTANT_UNITS = 27
    DESCRIPTION = 28
    DESCRIPTION_OF_HALT = 29
    DEVICE_ADDRESS_BINDING = 30
    DEVICE_TYPE = 31
    EFFECTIVE_PERIOD = 32
    ELAPSED_ACTIVE_TIME = 33
    ERROR_LIMIT = 34
    EVENT_ENABLE = 35
    EVENT_STATE = 36
    EVENT_TYPE = 37
    EXCEPTION_SCHEDULE = 38
    FAULT_VALUES = 39
    FEEDBACK_VALUE = 40
    FILE_ACCESS_METHOD = 41
    FILE_SIZE = 42
    FILE_TYPE = 43
    FIRMWARE_REVISION = 44
    HIGH_LIMIT = 45
    INACTIVE_TEXT = 46
    IN_PROCESS = 47
    INSTANCE_OF = 48
    INTEGRAL_CONSTANT = 49
    INTEGRAL_CONSTANT_UNITS = 50
    REMOVED__IN__VERSION_1__REVISION_4_51 = 51
    LIMIT_ENABLE = 52
    LIST_OF_GROUP_MEMBERS = 53
    LIST_OF_OBJECT_PROPERTY_REFERENCES = 54
    UNASSIGNED_55 = 55
    LOCAL_DATE = 56
    LOCAL_TIME = 57
    LOCATION = 58
    LOW_LIMIT = 59
    MANIPULATED_VARIABLE_REFERENCE = 60
    MAXIMUM_OUTPUT = 61
    MAX_APDU_LENGTH_ACCEPTED = 62
    MAX_INFO_FRAMES = 63
    MAX_MASTER = 64
    MAX_PRES_VALUE = 65
    MINIMUM_OFF_TIME = 66
    MINIMUM_ON_TIME = 67
    MINIMUM_OUTPUT = 68
    MIN_PRES_VALUE = 69
    MODEL_NAME = 70
    MODIFICATION_DATE = 71
    NOTIFY_TYPE = 72
    NUMBER_OF_APDU_RETRIES = 73
    NUMBER_OF_STATES = 74
    OBJECT_IDENTIFIER = 75
    OBJECT_LIST = 76
    OBJECT_NAME = 77
    OBJECT_PROPERTY_REFERENCE = 78
    OBJECT_TYPE = 79
    OPTIONAL = 80
    OUT_OF_SERVICE = 81
    OUTPUT_UNITS = 82
    EVENT_PARAMETERS = 83
    POLARITY = 84
    PRESENT_VALUE = 85
    PRIORITY = 86
    PRIORITY_ARRAY = 87
    PRIORITY_FOR_WRITING = 88
    PROCESS_IDENTIFIER = 89
    PROGRAM_CHANGE = 90
    PROGRAM_LOCATION = 91
    PROGRAM_STATE = 92
    PROPORTIONAL_CONSTANT = 93
    PROPORTIONAL_CONSTANT_UNITS = 94
    REMOVED__IN__VERSION_1__REVISION_2_95 = 95
    PROTOCOL_OBJECT_TYPES_SUPPORTED = 96
    PROTOCOL_SERVICES_SUPPORTED = 97
    PROTOCOL_VERSION = 98
    READ_ONLY = 99
    REASON_FOR_HALT = 100
    REMOVED__IN__VERSION_1__REVISION_4_101 = 101
    RECIPIENT_LIST = 102
    RELIABILITY = 103
    RELINQUISH_DEFAULT = 104
    REQUIRED = 105
    RESOLUTION = 106
    SEGMENTATION_SUPPORTED = 107
    SETPOINT = 108
    SETPOINT_REFERENCE = 109
    STATE_TEXT = 110
    STATUS_FLAGS = 111
    SYSTEM_STATUS = 112
    TIME_DELAY = 113
    TIME_OF_ACTIVE_TIME_RESET = 114
    TIME_OF_STATE_COUNT_RESET = 115
    TIME_SYNCHRONIZATION_RECIPIENTS = 116
    UNITS = 117
    UPDATE_INTERVAL = 118
    UTC_OFFSET = 119
    VENDOR_IDENTIFIER = 120
    VENDOR_NAME = 121
    VT_CLASSES_SUPPORTED = 122
    WEEKLY_SCHEDULE = 123
    ATTEMPTED_SAMPLES = 124
    AVERAGE_VALUE = 125
    BUFFER_SIZE = 126
    CLIENT_COV_INCREMENT = 127
    COV_RESUBSCRIPTION_INTERVAL = 128
    REMOVED__IN__VERSION_1__REVISION_3_129 = 129
    EVENT_TIME_STAMPS = 130
    LOG_BUFFER = 131
    LOG_DEVICE_OBJECT_PROPERTY = 132
    ENABLE = 133
    LOG_INTERVAL = 134
    MAXIMUM_VALUE = 135
    MINIMUM_VALUE = 136
    NOTIFICATION_THRESHOLD = 137
    REMOVED__IN__VERSION_1__REVISION_3_138 = 138
    PROTOCOL_REVISION = 139
    RECORDS_SINCE_NOTIFICATION = 140
    RECORD_COUNT = 141
    START_TIME = 142
    STOP_TIME = 143
    STOP_WHEN_FULL = 144
    TOTAL_RECORD_COUNT = 145
    VALID_SAMPLES = 146
    WINDOW_INTERVAL = 147
    WINDOW_SAMPLES = 148
    MAXIMUM_VALUE_TIMESTAMP = 149
    MINIMUM_VALUE_TIMESTAMP = 150
    VARIANCE_VALUE = 151
    ACTIVE_COV_SUBSCRIPTIONS = 152
    BACKUP_FAILURE_TIMEOUT = 153
    CONFIGURATION_FILES = 154
    DATABASE_REVISION = 155
    DIRECT_READING = 156
    LAST_RESTORE_TIME = 157
    MAINTENANCE_REQUIRED = 158
    MEMBER_OF = 159
    MODE = 160
    OPERATION_EXPECTED = 161
    SETTING = 162
    SILENCED = 163
    TRACKING_VALUE = 164
    ZONE_MEMBERS = 165
    LIFE_SAFETY_ALARM_VALUES = 166
    MAX_SEGMENTS_ACCEPTED = 167
    PROFILE_NAME = 168
    AUTO_SLAVE_DISCOVERY = 169
    MANUAL_SLAVE_ADDRESS_BINDING = 170
    SLAVE_ADDRESS_BINDING = 171
    SLAVE_PROXY_ENABLE = 172
    LAST_NOTIFY_RECORD = 173
    SCHEDULE_DEFAULT = 174
    ACCEPTED_MODES = 175
    ADJUST_VALUE = 176
    COUNT = 177
    COUNT_BEFORE_CHANGE = 178
    COUNT_CHANGE_TIME = 179
    COV_PERIOD = 180
    INPUT_REFERENCE = 181
    LIMIT_MONITORING_INTERVAL = 182
    LOGGING_OBJECT = 183
    LOGGING_RECORD = 184
    PRESCALE = 185
    PULSE_RATE = 186
    SCALE = 187
    SCALE_FACTOR = 188
    UPDATE_TIME = 189
    VALUE_BEFORE_CHANGE = 190
    VALUE_SET = 191
    VALUE_CHANGE_TIME = 192
    ALIGN_INTERVALS = 193
    UNASSIGNED_194 = 194
    INTERVAL_OFFSET = 195
    LAST_RESTART_REASON = 196
    LOGGING_TYPE = 197
    UNASSIGNED_198 = 198
    UNASSIGNED_199 = 199
    UNASSIGNED_200 = 200
    UNASSIGNED_201 = 201
    RESTART_NOTIFICATION_RECIPIENTS = 202
    TIME_OF_DEVICE_RESTART = 203
    TIME_SYNCHRONIZATION_INTERVAL = 204
    TRIGGER = 205
    UTC_TIME_SYNCHRONIZATION_RECIPIENTS = 206
    NODE_SUBTYPE = 207
    NODE_TYPE = 208
    STRUCTURED_OBJECT_LIST = 209
    SUBORDINATE_ANNOTATIONS = 210
    SUBORDINATE_LIST = 211
    ACTUAL_SHED_LEVEL = 212
    DUTY_WINDOW = 213
    EXPECTED_SHED_LEVEL = 214
    FULL_DUTY_BASELINE = 215
    UNASSIGNED_216 = 216
    UNASSIGNED_217 = 217
    REQUESTED_SHED_LEVEL = 218
    SHED_DURATION = 219
    SHED_LEVEL_DESCRIPTIONS = 220
    SHED_LEVELS = 221
    STATE_DESCRIPTION = 222
    UNASSIGNED_223 = 223
    UNASSIGNED_224 = 224
    UNASSIGNED_225 = 225
    DOOR_ALARM_STATE = 226
    DOOR_EXTENDED_PULSE_TIME = 227
    DOOR_MEMBERS = 228
    DOOR_OPEN_TOO_LONG_TIME = 229
    DOOR_PULSE_TIME = 230
    DOOR_STATUS = 231
    DOOR_UNLOCK_DELAY_TIME = 232
    LOCK_STATUS = 233
    MASKED_ALARM_VALUES = 234
    SECURED_STATUS = 235
    UNASSIGNED_236 = 236
    UNASSIGNED_237 = 237
    UNASSIGNED_238 = 238
    UNASSIGNED_239 = 239
    UNASSIGNED_240 = 240
    UNASSIGNED_241 = 241
    UNASSIGNED_242 = 242
    UNASSIGNED_243 = 243
    ABSENTEE_LIMIT = 244
    ACCESS_ALARM_EVENTS = 245
    ACCESS_DOORS = 246
    ACCESS_EVENT = 247
    ACCESS_EVENT_AUTHENTICATION_FACTOR = 248
    ACCESS_EVENT_CREDENTIAL = 249
    ACCESS_EVENT_TIME = 250
    ACCESS_TRANSACTION_EVENTS = 251
    ACCOMPANIMENT = 252
    ACCOMPANIMENT_TIME = 253
    ACTIVATION_TIME = 254
    ACTIVE_AUTHENTICATION_POLICY = 255
    ASSIGNED_ACCESS_RIGHTS = 256
    AUTHENTICATION_FACTORS = 257
    AUTHENTICATION_POLICY_LIST = 258
    AUTHENTICATION_POLICY_NAMES = 259
    AUTHENTICATION_STATUS = 260
    AUTHORIZATION_MODE = 261
    BELONGS_TO = 262
    CREDENTIAL_DISABLE = 263
    CREDENTIAL_STATUS = 264
    CREDENTIALS = 265
    CREDENTIALS_IN_ZONE = 266
    DAYS_REMAINING = 267
    ENTRY_POINTS = 268
    EXIT_POINTS = 269
    EXPIRY_TIME = 270
    EXTENDED_TIME_ENABLE = 271
    FAILED_ATTEMPT_EVENTS = 272
    FAILED_ATTEMPTS = 273
    FAILED_ATTEMPTS_TIME = 274
    LAST_ACCESS_EVENT = 275
    LAST_ACCESS_POINT = 276
    LAST_CREDENTIAL_ADDED = 277
    LAST_CREDENTIAL_ADDED_TIME = 278
    LAST_CREDENTIAL_REMOVED = 279
    LAST_CREDENTIAL_REMOVED_TIME = 280
    LAST_USE_TIME = 281
    LOCKOUT = 282
    LOCKOUT_RELINQUISH_TIME = 283
    REMOVED__IN__VERSION_1__REVISION_13_284 = 284
    MAX_FAILED_ATTEMPTS = 285
    MEMBERS = 286
    MUSTER_POINT = 287
    NEGATIVE_ACCESS_RULES = 288
    NUMBER_OF_AUTHENTICATION_POLICIES = 289
    OCCUPANCY_COUNT = 290
    OCCUPANCY_COUNT_ADJUST = 291
    OCCUPANCY_COUNT_ENABLE = 292
    REMOVED__IN__VERSION_1__REVISION_13_293 = 293
    OCCUPANCY_LOWER_LIMIT = 294
    OCCUPANCY_LOWER_LIMIT_ENFORCED = 295
    OCCUPANCY_STATE = 296
    OCCUPANCY_UPPER_LIMIT = 297
    OCCUPANCY_UPPER_LIMIT_ENFORCED = 298
    REMOVED__IN__VERSION_1__REVISION_13_299 = 299
    PASSBACK_MODE = 300
    PASSBACK_TIMEOUT = 301
    POSITIVE_ACCESS_RULES = 302
    REASON_FOR_DISABLE = 303
    SUPPORTED_FORMATS = 304
    SUPPORTED_FORMAT_CLASSES = 305
    THREAT_AUTHORITY = 306
    THREAT_LEVEL = 307
    TRACE_FLAG = 308
    TRANSACTION_NOTIFICATION_CLASS = 309
    USER_EXTERNAL_IDENTIFIER = 310
    USER_INFORMATION_REFERENCE = 311
    UNASSIGNED_312 = 312
    UNASSIGNED_313 = 313
    UNASSIGNED_314 = 314
    UNASSIGNED_315 = 315
    UNASSIGNED_316 = 316
    USER_NAME = 317
    USER_TYPE = 318
    USES_REMAINING = 319
    ZONE_FROM = 320
    ZONE_TO = 321
    ACCESS_EVENT_TAG = 322
    GLOBAL_IDENTIFIER = 323
    UNASSIGNED_324 = 324
    UNASSIGNED_325 = 325
    VERIFICATION_TIME = 326
    BASE_DEVICE_SECURITY_POLICY = 327
    DISTRIBUTION_KEY_REVISION = 328
    DO_NOT_HIDE = 329
    KEY_SETS = 330
    LAST_KEY_SERVER = 331
    NETWORK_ACCESS_SECURITY_POLICIES = 332
    PACKET_REORDER_TIME = 333
    SECURITY_PDU_TIMEOUT = 334
    SECURITY_TIME_WINDOW = 335
    SUPPORTED_SECURITY_ALGORITHMS = 336
    UPDATE_KEY_SET_TIMEOUT = 337
    BACKUP_AND_RESTORE_STATE = 338
    BACKUP_PREPARATION_TIME = 339
    RESTORE_COMPLETION_TIME = 340
    RESTORE_PREPARATION_TIME = 341
    BIT_MASK = 342
    BIT_TEXT = 343
    IS_UTC = 344
    GROUP_MEMBERS = 345
    GROUP_MEMBER_NAMES = 346
    MEMBER_STATUS_FLAGS = 347
    REQUESTED_UPDATE_INTERVAL = 348
    COVU_PERIOD = 349
    COVU_RECIPIENTS = 350
    EVENT_MESSAGE_TEXTS = 351
    EVENT_MESSAGE_TEXTS_CONFIG = 352
    EVENT_DETECTION_ENABLE = 353
    EVENT_ALGORITHM_INHIBIT = 354
    EVENT_ALGORITHM_INHIBIT_REF = 355
    TIME_DELAY_NORMAL = 356
    RELIABILITY_EVALUATION_INHIBIT = 357
    FAULT_PARAMETERS = 358
    FAULT_TYPE = 359
    LOCAL_FORWARDING_ONLY = 360
    PROCESS_IDENTIFIER_FILTER = 361
    SUBSCRIBED_RECIPIENTS = 362
    PORT_FILTER = 363
    AUTHORIZATION_EXEMPTIONS = 364
    ALLOW_GROUP_DELAY_INHIBIT = 365
    CHANNEL_NUMBER = 366
    CONTROL_GROUPS = 367
    EXECUTION_DELAY = 368
    LAST_PRIORITY = 369
    WRITE_STATUS = 370
    PROPERTY_LIST = 371
    SERIAL_NUMBER = 372
    BLINK_WARN_ENABLE = 373
    DEFAULT_FADE_TIME = 374
    DEFAULT_RAMP_RATE = 375
    DEFAULT_STEP_INCREMENT = 376
    EGRESS_TIME = 377
    IN_PROGRESS = 378
    INSTANTANEOUS_POWER = 379
    LIGHTING_COMMAND = 380
    LIGHTING_COMMAND_DEFAULT_PRIORITY = 381
    MAX_ACTUAL_VALUE = 382
    MIN_ACTUAL_VALUE = 383
    POWER = 384
    TRANSITION = 385
    EGRESS_ACTIVE = 386

class BACnetReinitializedStateofDevice(enum.IntFlag):
    COLDSTART = 0
    WARMSTART = 1
    STARTBACKUP = 2
    ENDBACKUP = 3
    STARTRESTORE = 4
    ENDRESTORE = 5
    ABORTRESTORE = 6

class BACnetMessageClass(ns0.datatypes.Union):
    @property
    def unsigned(self) -> o6.ExtensionObject: ...
    @unsigned.setter
    def unsigned(self, value: Any) -> None: ...
    @property
    def string(self) -> o6.String: ...
    @string.setter
    def string(self, value: o6.String) -> None: ...

class BACnetPriorityValue(ns0.datatypes.Union):
    @property
    def real(self) -> o6.Float: ...
    @real.setter
    def real(self, value: SupportsFloat) -> None: ...
    @property
    def enumerated(self) -> o6.Int32: ...
    @enumerated.setter
    def enumerated(self, value: _Integer) -> None: ...
    @property
    def unsigned(self) -> o6.ExtensionObject: ...
    @unsigned.setter
    def unsigned(self, value: Any) -> None: ...
    @property
    def boolean(self) -> o6.Boolean: ...
    @boolean.setter
    def boolean(self, value: _Boolean) -> None: ...
    @property
    def signed(self) -> o6.ExtensionObject: ...
    @signed.setter
    def signed(self, value: Any) -> None: ...
    @property
    def double(self) -> o6.Double: ...
    @double.setter
    def double(self, value: SupportsFloat) -> None: ...

class BACnetRecipient(ns0.datatypes.Union):
    @property
    def device(self) -> o6.UInt32: ...
    @device.setter
    def device(self, value: _Integer) -> None: ...
    @property
    def address(self) -> BACnetAddress: ...
    @address.setter
    def address(self, value: BACnetAddress) -> None: ...

class BACnetMessagePriority(enum.IntFlag):
    NORMAL = 0
    URGENT = 1

class BACnetEventParameterDoubleOutOfRange(ns0.datatypes.Structure):
    @property
    def time_delay(self) -> o6.UInt32: ...
    @time_delay.setter
    def time_delay(self, value: _Integer) -> None: ...
    @property
    def low_limit(self) -> o6.Double: ...
    @low_limit.setter
    def low_limit(self, value: SupportsFloat) -> None: ...
    @property
    def high_limit(self) -> o6.Double: ...
    @high_limit.setter
    def high_limit(self, value: SupportsFloat) -> None: ...
    @property
    def deadband(self) -> o6.Double: ...
    @deadband.setter
    def deadband(self, value: SupportsFloat) -> None: ...

class BACnetEventParameterSignedOutOfRange(ns0.datatypes.Structure):
    @property
    def time_delay(self) -> o6.UInt32: ...
    @time_delay.setter
    def time_delay(self, value: _Integer) -> None: ...
    @property
    def low_limit(self) -> o6.Int32: ...
    @low_limit.setter
    def low_limit(self, value: _Integer) -> None: ...
    @property
    def high_limit(self) -> o6.Int32: ...
    @high_limit.setter
    def high_limit(self, value: _Integer) -> None: ...
    @property
    def deadband(self) -> o6.UInt32: ...
    @deadband.setter
    def deadband(self, value: _Integer) -> None: ...

class BACnetDaysOfWeek(ns0.datatypes.OptionSet):
    @property
    def value(self) -> o6.ByteString: ...
    @value.setter
    def value(self, value: o6.ByteString) -> None: ...
    @property
    def validBits(self) -> o6.ByteString: ...
    @validBits.setter
    def validBits(self, value: o6.ByteString) -> None: ...

class BACnetEventTransitionBits(ns0.datatypes.OptionSet):
    @property
    def value(self) -> o6.ByteString: ...
    @value.setter
    def value(self, value: o6.ByteString) -> None: ...
    @property
    def validBits(self) -> o6.ByteString: ...
    @validBits.setter
    def validBits(self, value: o6.ByteString) -> None: ...

class BACnetLimitEnable(ns0.datatypes.OptionSet):
    @property
    def value(self) -> o6.ByteString: ...
    @value.setter
    def value(self, value: o6.ByteString) -> None: ...
    @property
    def validBits(self) -> o6.ByteString: ...
    @validBits.setter
    def validBits(self, value: o6.ByteString) -> None: ...

class BACnetObjectTypeSupportedBits(ns0.datatypes.OptionSet):
    @property
    def value(self) -> o6.ByteString: ...
    @value.setter
    def value(self, value: o6.ByteString) -> None: ...
    @property
    def validBits(self) -> o6.ByteString: ...
    @validBits.setter
    def validBits(self, value: o6.ByteString) -> None: ...

class BACnetServicesSupportedBits(ns0.datatypes.OptionSet):
    @property
    def value(self) -> o6.ByteString: ...
    @value.setter
    def value(self, value: o6.ByteString) -> None: ...
    @property
    def validBits(self) -> o6.ByteString: ...
    @validBits.setter
    def validBits(self, value: o6.ByteString) -> None: ...

class BACnetStatusFlags(ns0.datatypes.OptionSet):
    @property
    def value(self) -> o6.ByteString: ...
    @value.setter
    def value(self, value: o6.ByteString) -> None: ...
    @property
    def validBits(self) -> o6.ByteString: ...
    @validBits.setter
    def validBits(self, value: o6.ByteString) -> None: ...

class BACnetEventParameterChangeOfCharacterString(ns0.datatypes.Structure):
    @property
    def time_delay(self) -> o6.UInt32: ...
    @time_delay.setter
    def time_delay(self, value: _Integer) -> None: ...
    @property
    def alarmValues(self) -> list[o6.String]: ...
    @alarmValues.setter
    def alarmValues(self, value: Sequence[o6.String]) -> None: ...

class BACnetEventParameterUnsignedRange(ns0.datatypes.Structure):
    @property
    def time_delay(self) -> o6.UInt32: ...
    @time_delay.setter
    def time_delay(self, value: _Integer) -> None: ...
    @property
    def low_limit(self) -> o6.UInt32: ...
    @low_limit.setter
    def low_limit(self, value: _Integer) -> None: ...
    @property
    def high_limit(self) -> o6.UInt32: ...
    @high_limit.setter
    def high_limit(self, value: _Integer) -> None: ...

class BACnetDeviceObjectPropertyReference(ns0.datatypes.Structure):
    @property
    def objectIdentifier(self) -> o6.UInt32: ...
    @objectIdentifier.setter
    def objectIdentifier(self, value: _Integer) -> None: ...
    @property
    def propertyIdentifier(self) -> BACnetPropertyIdentifier | None: ...
    @propertyIdentifier.setter
    def propertyIdentifier(self, value: _Integer | None) -> None: ...
    @property
    def propertyArrayIndex(self) -> o6.UInt32 | None: ...
    @propertyArrayIndex.setter
    def propertyArrayIndex(self, value: _Integer | None) -> None: ...
    @property
    def deviceIdentifier(self) -> o6.UInt32 | None: ...
    @deviceIdentifier.setter
    def deviceIdentifier(self, value: _Integer | None) -> None: ...

class BACnetEventParameterChangeOfBitstring(ns0.datatypes.Structure):
    @property
    def time_delay(self) -> o6.UInt32: ...
    @time_delay.setter
    def time_delay(self, value: _Integer) -> None: ...
    @property
    def bitmask(self) -> ns0.datatypes.OptionSet: ...
    @bitmask.setter
    def bitmask(self, value: ns0.datatypes.OptionSet) -> None: ...
    @property
    def list_of_bitstring_values(self) -> list[ns0.datatypes.OptionSet]: ...
    @list_of_bitstring_values.setter
    def list_of_bitstring_values(self, value: Sequence[ns0.datatypes.OptionSet]) -> None: ...

class BACnetEventParameterChangeOfState(ns0.datatypes.Structure):
    @property
    def time_delay(self) -> o6.UInt32: ...
    @time_delay.setter
    def time_delay(self, value: _Integer) -> None: ...
    @property
    def list_of_values(self) -> list[BACnetPropertyStates]: ...
    @list_of_values.setter
    def list_of_values(self, value: Sequence[BACnetPropertyStates]) -> None: ...

class BACnetTimeValueValue(ns0.datatypes.Structure):
    @property
    def booleanValue(self) -> o6.Boolean: ...
    @booleanValue.setter
    def booleanValue(self, value: _Boolean) -> None: ...
    @property
    def unsignedValue(self) -> o6.ExtensionObject: ...
    @unsignedValue.setter
    def unsignedValue(self, value: Any) -> None: ...
    @property
    def signedValue(self) -> o6.ExtensionObject: ...
    @signedValue.setter
    def signedValue(self, value: Any) -> None: ...
    @property
    def octedStringValue(self) -> o6.ByteString: ...
    @octedStringValue.setter
    def octedStringValue(self, value: o6.ByteString) -> None: ...
    @property
    def charStringValue(self) -> o6.String: ...
    @charStringValue.setter
    def charStringValue(self, value: o6.String) -> None: ...
    @property
    def objectIdentifierValue(self) -> o6.UInt32: ...
    @objectIdentifierValue.setter
    def objectIdentifierValue(self, value: _Integer) -> None: ...
    @property
    def enumerationValue(self) -> o6.Int32: ...
    @enumerationValue.setter
    def enumerationValue(self, value: _Integer) -> None: ...
    @property
    def bitStringValue(self) -> ns0.datatypes.OptionSet: ...
    @bitStringValue.setter
    def bitStringValue(self, value: ns0.datatypes.OptionSet) -> None: ...

class BACnetTimeValue(ns0.datatypes.Structure):
    @property
    def time(self) -> BACnetTime: ...
    @time.setter
    def time(self, value: BACnetTime) -> None: ...
    @property
    def value(self) -> BACnetTimeValueValue: ...
    @value.setter
    def value(self, value: BACnetTimeValueValue) -> None: ...

class BACnetDailySchedule(ns0.datatypes.Structure):
    @property
    def day_schedule(self) -> list[BACnetTimeValue]: ...
    @day_schedule.setter
    def day_schedule(self, value: Sequence[BACnetTimeValue]) -> None: ...

class BACnetSegmentation(enum.IntFlag):
    SEGMENTED_BOTH = 0
    SEGMENTED_TRANSMIT = 1
    SEGMENTED_RECEIVE = 2
    NO_SEGMENTATION = 3

class BACnetAddressBinding(ns0.datatypes.Structure):
    @property
    def deviceObjectIdentifier(self) -> o6.UInt32: ...
    @deviceObjectIdentifier.setter
    def deviceObjectIdentifier(self, value: _Integer) -> None: ...
    @property
    def deviceAddress(self) -> BACnetAddress: ...
    @deviceAddress.setter
    def deviceAddress(self, value: BACnetAddress) -> None: ...

class BACnetBackupState(enum.IntFlag):
    IDLE = 0
    PREPARING__FOR__BACKUP = 1
    PREPARING__FOR__RESTORE = 2
    PERFORMING_A__BACKUP = 3
    PERFORMING_A__RESTORE = 4
    BACKUP__FAILURE = 5
    RESTORE__FAILURE = 6

class BACnetRecipientProcess(ns0.datatypes.Structure):
    @property
    def recipient(self) -> BACnetRecipient: ...
    @recipient.setter
    def recipient(self, value: BACnetRecipient) -> None: ...
    @property
    def processIdentifier(self) -> o6.UInt32: ...
    @processIdentifier.setter
    def processIdentifier(self, value: _Integer) -> None: ...

class BACnetCOVSubscription(ns0.datatypes.Structure):
    @property
    def recipient(self) -> BACnetRecipientProcess: ...
    @recipient.setter
    def recipient(self, value: BACnetRecipientProcess) -> None: ...
    @property
    def monitoredPropertyReference(self) -> BACnetDeviceObjectPropertyReference: ...
    @monitoredPropertyReference.setter
    def monitoredPropertyReference(self, value: BACnetDeviceObjectPropertyReference) -> None: ...
    @property
    def issueConfirmedNotifications(self) -> o6.Boolean: ...
    @issueConfirmedNotifications.setter
    def issueConfirmedNotifications(self, value: _Boolean) -> None: ...
    @property
    def timeRemaining(self) -> o6.UInt32: ...
    @timeRemaining.setter
    def timeRemaining(self, value: _Integer) -> None: ...
    @property
    def covIncrement(self) -> o6.Float | None: ...
    @covIncrement.setter
    def covIncrement(self, value: SupportsFloat | None) -> None: ...

class BACnetRestartReason(enum.IntFlag):
    UNKNOWN = 0
    COLDSTART = 1
    WARMSTART = 2
    DETECTED_POWER_LOST = 3
    DETECTED_POWERED_OFF = 4
    HARDWARE_WATCHDOG = 5
    SOFTWARE_WATCHDOG = 6
    SUSPENDED = 7

class BACnetDestination(ns0.datatypes.Structure):
    @property
    def validDays(self) -> BACnetDaysOfWeek: ...
    @validDays.setter
    def validDays(self, value: BACnetDaysOfWeek) -> None: ...
    @property
    def fromTime(self) -> BACnetTime: ...
    @fromTime.setter
    def fromTime(self, value: BACnetTime) -> None: ...
    @property
    def toTime(self) -> BACnetTime: ...
    @toTime.setter
    def toTime(self, value: BACnetTime) -> None: ...
    @property
    def recipient(self) -> BACnetRecipient: ...
    @recipient.setter
    def recipient(self, value: BACnetRecipient) -> None: ...
    @property
    def processIdentifier(self) -> o6.UInt32: ...
    @processIdentifier.setter
    def processIdentifier(self, value: _Integer) -> None: ...
    @property
    def issueConfirmedNotifications(self) -> o6.Boolean: ...
    @issueConfirmedNotifications.setter
    def issueConfirmedNotifications(self, value: _Boolean) -> None: ...
    @property
    def transitions(self) -> BACnetEventTransitionBits: ...
    @transitions.setter
    def transitions(self, value: BACnetEventTransitionBits) -> None: ...

class BACnetFaultType(enum.IntFlag):
    NONE = 0
    FAULT_CHARACTERSTRING = 1
    FAULT_EXENDED = 2
    FAULT_LIFE_SAFETY = 3
    FAULT_STATE = 4
    FAULT_STATUS_FLAGS = 5

class BACnetFaultParameterFaultCharacterstring(ns0.datatypes.Structure):
    @property
    def fault_characterstring(self) -> o6.String: ...
    @fault_characterstring.setter
    def fault_characterstring(self, value: o6.String) -> None: ...

class BACnetFaultParameterFaultLifeSafety(ns0.datatypes.Structure):
    @property
    def list_of_fault_values(self) -> list[BACnetLifeSafetyState]: ...
    @list_of_fault_values.setter
    def list_of_fault_values(self, value: Sequence[_Integer]) -> None: ...
    @property
    def mode_property_reference(self) -> BACnetDeviceObjectPropertyReference: ...
    @mode_property_reference.setter
    def mode_property_reference(self, value: BACnetDeviceObjectPropertyReference) -> None: ...

class BACnetFaultParameterFaultState(ns0.datatypes.Structure):
    @property
    def list_of_fault_values(self) -> list[BACnetProgramStates]: ...
    @list_of_fault_values.setter
    def list_of_fault_values(self, value: Sequence[_Integer]) -> None: ...

class BACnetFaultParameterFaultStatusFlags(ns0.datatypes.Structure):
    @property
    def status_flags_reference(self) -> list[BACnetDeviceObjectPropertyReference]: ...
    @status_flags_reference.setter
    def status_flags_reference(self, value: Sequence[BACnetDeviceObjectPropertyReference]) -> None: ...

class BACnetDayOfWeek(enum.IntFlag):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    UNSPECIFIED = 255

class BACnetDate(ns0.datatypes.Structure):
    @property
    def year(self) -> o6.UInt16: ...
    @year.setter
    def year(self, value: _Integer) -> None: ...
    @property
    def month(self) -> BACnetMonth: ...
    @month.setter
    def month(self, value: _Integer) -> None: ...
    @property
    def dayOfMonth(self) -> BACnetDayOfMonth: ...
    @dayOfMonth.setter
    def dayOfMonth(self, value: _Integer) -> None: ...
    @property
    def dayOfWeek(self) -> BACnetDayOfWeek: ...
    @dayOfWeek.setter
    def dayOfWeek(self, value: _Integer) -> None: ...

class BACnetDateTime(ns0.datatypes.Structure):
    @property
    def date(self) -> BACnetDate: ...
    @date.setter
    def date(self, value: BACnetDate) -> None: ...
    @property
    def time(self) -> BACnetTime: ...
    @time.setter
    def time(self, value: BACnetTime) -> None: ...

class BACnetDateRange(ns0.datatypes.Structure):
    @property
    def startDate(self) -> BACnetDate: ...
    @startDate.setter
    def startDate(self, value: BACnetDate) -> None: ...
    @property
    def endTime(self) -> BACnetDate: ...
    @endTime.setter
    def endTime(self, value: BACnetDate) -> None: ...

class BACnetWeekNDay(ns0.datatypes.Structure):
    @property
    def month(self) -> BACnetMonth: ...
    @month.setter
    def month(self, value: _Integer) -> None: ...
    @property
    def day(self) -> BACnetDay: ...
    @day.setter
    def day(self, value: _Integer) -> None: ...
    @property
    def dayOfWeek(self) -> BACnetDayOfWeek: ...
    @dayOfWeek.setter
    def dayOfWeek(self, value: _Integer) -> None: ...

class BACnetCalendarEntry(ns0.datatypes.Union):
    @property
    def date(self) -> BACnetDate: ...
    @date.setter
    def date(self, value: BACnetDate) -> None: ...
    @property
    def dateRange(self) -> BACnetDateRange: ...
    @dateRange.setter
    def dateRange(self, value: BACnetDateRange) -> None: ...
    @property
    def weekNDay(self) -> BACnetWeekNDay: ...
    @weekNDay.setter
    def weekNDay(self, value: BACnetWeekNDay) -> None: ...

class BACnetSpecialEventPeriod(ns0.datatypes.Union):
    @property
    def calendarEntry(self) -> BACnetCalendarEntry: ...
    @calendarEntry.setter
    def calendarEntry(self, value: BACnetCalendarEntry) -> None: ...
    @property
    def calendarReference(self) -> o6.UInt32: ...
    @calendarReference.setter
    def calendarReference(self, value: _Integer) -> None: ...

class BACnetTimeStamp(ns0.datatypes.Union):
    @property
    def time(self) -> BACnetTime: ...
    @time.setter
    def time(self, value: BACnetTime) -> None: ...
    @property
    def sequenceNumber(self) -> o6.UInt16: ...
    @sequenceNumber.setter
    def sequenceNumber(self, value: _Integer) -> None: ...
    @property
    def dateTime(self) -> BACnetDateTime: ...
    @dateTime.setter
    def dateTime(self, value: BACnetDateTime) -> None: ...

class BACnetEventParameterExtendedParameters(ns0.datatypes.Union):
    @property
    def real(self) -> o6.Double: ...
    @real.setter
    def real(self, value: SupportsFloat) -> None: ...
    @property
    def unsigned(self) -> o6.UInt32: ...
    @unsigned.setter
    def unsigned(self, value: _Integer) -> None: ...
    @property
    def boolean(self) -> o6.Boolean: ...
    @boolean.setter
    def boolean(self, value: _Boolean) -> None: ...
    @property
    def double(self) -> o6.Double: ...
    @double.setter
    def double(self, value: SupportsFloat) -> None: ...
    @property
    def octed(self) -> list[o6.Byte]: ...
    @octed.setter
    def octed(self, value: Sequence[_Integer]) -> None: ...
    @property
    def characterString(self) -> o6.String: ...
    @characterString.setter
    def characterString(self, value: o6.String) -> None: ...
    @property
    def bitString(self) -> ns0.datatypes.OptionSet: ...
    @bitString.setter
    def bitString(self, value: ns0.datatypes.OptionSet) -> None: ...
    @property
    def enum(self) -> o6.UInt32: ...
    @enum.setter
    def enum(self, value: _Integer) -> None: ...
    @property
    def date(self) -> BACnetDate: ...
    @date.setter
    def date(self, value: BACnetDate) -> None: ...
    @property
    def time(self) -> BACnetTime: ...
    @time.setter
    def time(self, value: BACnetTime) -> None: ...
    @property
    def objectIdentifier(self) -> o6.UInt32: ...
    @objectIdentifier.setter
    def objectIdentifier(self, value: _Integer) -> None: ...
    @property
    def reference(self) -> BACnetDeviceObjectPropertyReference: ...
    @reference.setter
    def reference(self, value: BACnetDeviceObjectPropertyReference) -> None: ...
    @property
    def integer(self) -> o6.Int32: ...
    @integer.setter
    def integer(self, value: _Integer) -> None: ...

class BACnetSpecialEvent(ns0.datatypes.Structure):
    @property
    def period(self) -> BACnetSpecialEventPeriod: ...
    @period.setter
    def period(self, value: BACnetSpecialEventPeriod) -> None: ...
    @property
    def listOfTimeValues(self) -> list[BACnetTimeValue]: ...
    @listOfTimeValues.setter
    def listOfTimeValues(self, value: Sequence[BACnetTimeValue]) -> None: ...
    @property
    def eventPriority(self) -> o6.Byte: ...
    @eventPriority.setter
    def eventPriority(self, value: _Integer) -> None: ...

class BACnetEventFaultParameterExtended(ns0.datatypes.Structure):
    @property
    def vendorId(self) -> o6.UInt16: ...
    @vendorId.setter
    def vendorId(self, value: _Integer) -> None: ...
    @property
    def extended_fault_type(self) -> o6.ExtensionObject: ...
    @extended_fault_type.setter
    def extended_fault_type(self, value: Any) -> None: ...
    @property
    def parameters(self) -> list[BACnetEventParameterExtendedParameters]: ...
    @parameters.setter
    def parameters(self, value: Sequence[BACnetEventParameterExtendedParameters]) -> None: ...

class BACnetFaultParameter(ns0.datatypes.Union):
    @property
    def fault_characterstring(self) -> BACnetFaultParameterFaultCharacterstring: ...
    @fault_characterstring.setter
    def fault_characterstring(self, value: BACnetFaultParameterFaultCharacterstring) -> None: ...
    @property
    def fault_life_safety(self) -> BACnetFaultParameterFaultLifeSafety: ...
    @fault_life_safety.setter
    def fault_life_safety(self, value: BACnetFaultParameterFaultLifeSafety) -> None: ...
    @property
    def fault_state(self) -> BACnetFaultParameterFaultState: ...
    @fault_state.setter
    def fault_state(self, value: BACnetFaultParameterFaultState) -> None: ...
    @property
    def fault_status_flags(self) -> BACnetFaultParameterFaultStatusFlags: ...
    @fault_status_flags.setter
    def fault_status_flags(self, value: BACnetFaultParameterFaultStatusFlags) -> None: ...
    @property
    def fault_extended(self) -> BACnetEventFaultParameterExtended: ...
    @fault_extended.setter
    def fault_extended(self, value: BACnetEventFaultParameterExtended) -> None: ...

class BACnetEventParameterChangeOfValue(ns0.datatypes.Structure):
    @property
    def time_delay(self) -> o6.UInt32: ...
    @time_delay.setter
    def time_delay(self, value: _Integer) -> None: ...
    @property
    def cov_criteria_bitmask(self) -> ns0.datatypes.OptionSet: ...
    @cov_criteria_bitmask.setter
    def cov_criteria_bitmask(self, value: ns0.datatypes.OptionSet) -> None: ...
    @property
    def cov_criteria_referenced_property_increment(self) -> o6.Float: ...
    @cov_criteria_referenced_property_increment.setter
    def cov_criteria_referenced_property_increment(self, value: SupportsFloat) -> None: ...

class BACnetEventParameterCommandFailure(ns0.datatypes.Structure):
    @property
    def time_delay(self) -> o6.UInt32: ...
    @time_delay.setter
    def time_delay(self, value: _Integer) -> None: ...
    @property
    def feedback_property_reference(self) -> BACnetDeviceObjectPropertyReference: ...
    @feedback_property_reference.setter
    def feedback_property_reference(self, value: BACnetDeviceObjectPropertyReference) -> None: ...

class BACnetEventParameterFloatingLimit(ns0.datatypes.Structure):
    @property
    def time_delay(self) -> o6.UInt32: ...
    @time_delay.setter
    def time_delay(self, value: _Integer) -> None: ...
    @property
    def setpoint_reference(self) -> BACnetDeviceObjectPropertyReference: ...
    @setpoint_reference.setter
    def setpoint_reference(self, value: BACnetDeviceObjectPropertyReference) -> None: ...
    @property
    def low_diff_limit(self) -> o6.Double: ...
    @low_diff_limit.setter
    def low_diff_limit(self, value: SupportsFloat) -> None: ...
    @property
    def high_diff_limit(self) -> o6.Double: ...
    @high_diff_limit.setter
    def high_diff_limit(self, value: SupportsFloat) -> None: ...
    @property
    def deadband(self) -> o6.Double: ...
    @deadband.setter
    def deadband(self, value: SupportsFloat) -> None: ...

class BACnetEventParameterOutOfRange(ns0.datatypes.Structure):
    @property
    def time_delay(self) -> o6.UInt32: ...
    @time_delay.setter
    def time_delay(self, value: _Integer) -> None: ...
    @property
    def low_limit(self) -> o6.Double: ...
    @low_limit.setter
    def low_limit(self, value: SupportsFloat) -> None: ...
    @property
    def high_limit(self) -> o6.Double: ...
    @high_limit.setter
    def high_limit(self, value: SupportsFloat) -> None: ...
    @property
    def deadband(self) -> o6.Double: ...
    @deadband.setter
    def deadband(self, value: SupportsFloat) -> None: ...

class BACnetEventParameterBufferReady(ns0.datatypes.Structure):
    @property
    def notification_threshold(self) -> o6.UInt32: ...
    @notification_threshold.setter
    def notification_threshold(self, value: _Integer) -> None: ...
    @property
    def previous_notification_count(self) -> o6.UInt32: ...
    @previous_notification_count.setter
    def previous_notification_count(self, value: _Integer) -> None: ...

class BACnetEventParameterUnsignedOutOfRange(ns0.datatypes.Structure):
    @property
    def time_delay(self) -> o6.UInt32: ...
    @time_delay.setter
    def time_delay(self, value: _Integer) -> None: ...
    @property
    def low_limit(self) -> o6.UInt32: ...
    @low_limit.setter
    def low_limit(self, value: _Integer) -> None: ...
    @property
    def high_limit(self) -> o6.UInt32: ...
    @high_limit.setter
    def high_limit(self, value: _Integer) -> None: ...
    @property
    def deadband(self) -> o6.UInt32: ...
    @deadband.setter
    def deadband(self, value: _Integer) -> None: ...

class BACnetEventParameter(ns0.datatypes.Union):
    @property
    def change_of_bitstring(self) -> BACnetEventParameterChangeOfBitstring: ...
    @change_of_bitstring.setter
    def change_of_bitstring(self, value: BACnetEventParameterChangeOfBitstring) -> None: ...
    @property
    def change_of_state(self) -> BACnetEventParameterChangeOfState: ...
    @change_of_state.setter
    def change_of_state(self, value: BACnetEventParameterChangeOfState) -> None: ...
    @property
    def change_of_value(self) -> BACnetEventParameterChangeOfValue: ...
    @change_of_value.setter
    def change_of_value(self, value: BACnetEventParameterChangeOfValue) -> None: ...
    @property
    def command_failure(self) -> BACnetEventParameterCommandFailure: ...
    @command_failure.setter
    def command_failure(self, value: BACnetEventParameterCommandFailure) -> None: ...
    @property
    def floating_limit(self) -> BACnetEventParameterFloatingLimit: ...
    @floating_limit.setter
    def floating_limit(self, value: BACnetEventParameterFloatingLimit) -> None: ...
    @property
    def out_of_range(self) -> BACnetEventParameterOutOfRange: ...
    @out_of_range.setter
    def out_of_range(self, value: BACnetEventParameterOutOfRange) -> None: ...
    @property
    def extended(self) -> BACnetEventFaultParameterExtended: ...
    @extended.setter
    def extended(self, value: BACnetEventFaultParameterExtended) -> None: ...
    @property
    def buffer_ready(self) -> BACnetEventParameterBufferReady: ...
    @buffer_ready.setter
    def buffer_ready(self, value: BACnetEventParameterBufferReady) -> None: ...
    @property
    def unsigned_range(self) -> BACnetEventParameterUnsignedRange: ...
    @unsigned_range.setter
    def unsigned_range(self, value: BACnetEventParameterUnsignedRange) -> None: ...
    @property
    def double_out_of_range(self) -> BACnetEventParameterDoubleOutOfRange: ...
    @double_out_of_range.setter
    def double_out_of_range(self, value: BACnetEventParameterDoubleOutOfRange) -> None: ...
    @property
    def signed_out_of_range(self) -> BACnetEventParameterSignedOutOfRange: ...
    @signed_out_of_range.setter
    def signed_out_of_range(self, value: BACnetEventParameterSignedOutOfRange) -> None: ...
    @property
    def unsigned_out_of_range(self) -> BACnetEventParameterUnsignedOutOfRange: ...
    @unsigned_out_of_range.setter
    def unsigned_out_of_range(self, value: BACnetEventParameterUnsignedOutOfRange) -> None: ...
    @property
    def change_of_characterstring(self) -> BACnetEventParameterChangeOfCharacterString: ...
    @change_of_characterstring.setter
    def change_of_characterstring(self, value: BACnetEventParameterChangeOfCharacterString) -> None: ...
    @property
    def change_of_life_safety(self) -> BACnetEventParameterChangeOfLifeSafety: ...
    @change_of_life_safety.setter
    def change_of_life_safety(self, value: BACnetEventParameterChangeOfLifeSafety) -> None: ...

class BACnetLoggingType(enum.IntFlag):
    POLLED = 0
    COV = 1
    TRIGGERED = 2

class BACnetObjectTypeEnum(enum.IntFlag):
    ANALOG_INPUT = 0
    ANALOG_OUTPUT = 1
    ANALOG_VALUE = 2
    BINARY_INPUT = 3
    BINARY_OUTPUT = 4
    BINARY_VALUE = 5
    CALENDAR = 6
    COMMAND = 7
    DEVICE = 8
    EVENT_ENROLLMENT = 9
    FILE = 10
    GROUP = 11
    LOOP = 12
    MULTI_STATE_INPUT = 13
    MULTI_STATE_OUTPUT = 14
    NOTIFICATION_CLASS = 15
    PROGRAM = 16
    SCHEDULE = 17
    AVERAGING = 18
    MULTI_STATE_VALUE = 19
    TREND_LOG = 20
    LIFE_SAFETY_POINT = 21
    LIFE_SAFETY_ZONE = 22
    ACCUMULATOR = 23
    PULSE_CONVERTER = 24
    EVENT_LOG = 25
    GLOBAL_GROUP = 26
    TREND_LOG_MULTIPLE = 27
    LOAD_CONTROL = 28
    STRUCTURED_VIEW = 29
    ACCESS_DOOR = 30
    UNASSIGNED = 31
    ACCESS_CREDENTIAL = 32
    ACCESS_POINT = 33
    ACCESS_RIGHTS = 34
    ACCESS_USER = 35
    ACCESS_ZONE = 36
    CREDENTIONAL_DATA_INPUT = 37
    NETWORK_SECURITY = 38
    BITSTRING_VALUE = 39
    CHARACTERSTRING_VALUE = 40
    DATE_PATTERN_VALUE = 41
    DATE_VALUE = 42
    DATETIME_PATTERN_VALUE = 43
    DATETIME_VALUE = 44
    INTEGER_VALUE = 45
    LARGE_ANALOG_VALUE = 46
    OCTETSTRING_VALUE = 47
    POSITIVE_INTEGER_VALUE = 48
    TIME_PATTERN_VALUE = 49
    TIME_VALUE = 50
    NOTIFICATION_FORWARDER = 51
    ALERT_ENROLLMENT = 52
    CHANNEL = 53
    LIGHTING_OUTPUT = 54

class BACnetEventType(enum.IntFlag):
    CHANGE_OF_BITSTRING = 0
    CHANGE_OF_STATE = 1
    CHANGE_OF_VALUE = 2
    COMMAND_FAILURE = 3
    FLOATING_LIMIT = 4
    OUT_OF_RANGE = 5
    CHANGE_OF_LIFE_SAFETY = 8
    EXTENDED = 9
    BUFFER_READY = 10
    UNSIGNED_RANGE = 11
    ACCESS_EVENT = 13
    DOUBLE_OUT_OF_RANGE = 14
    SIGNED_OUT_OF_RANGE = 15
    UNSIGNED_OUT_OF_RANGE = 16
    CHANGE_OF_CHARACTERSTRING = 17
    CHANGE_OF_STATUS_FLAGS = 18
