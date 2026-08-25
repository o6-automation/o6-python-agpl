/* Copyright 2026 (c) o6 Automation GmbH
 *
 * Hand-maintained C-side bootstrap enums.
 * =======================================
 *
 * This file used to be generated wholesale as ``src_gen/src_cmodule_enum.c``
 * (~64 NS0 enums + StatusCode) by ``tools/generate_python_enums.py``.  Every
 * NS0 enum is now emitted as an ``@o6.enumtype`` class in ``o6/nsx/ns0.py``
 * (compiled from the NodeSet2 XML) and registered through the dedup in
 * ``src/datatypes.c``, so the bulk of that generated file became dead code.
 *
 * A few pieces genuinely need to exist on the C side before ``o6.nsx.ns0``
 * is imported, because the decorator path in that module depends on them
 * (or emits them too late in the file to satisfy an earlier use):
 *
 *   1. `StatusCode` — a core OPC UA builtin (UA_TYPES[UA_TYPES_STATUSCODE]),
 *      bound to `pyUAStatusCode` in `src/types.c` and used everywhere for
 *      encode/decode.  It is an `IntFlag` with `boundary=KEEP` so unknown
 *      wire codes survive as pseudo-members; `__str__` renders known members
 *      by name and unknown values as `0xXXXXXXXX`.  The name/value table
 *      below is transcribed from open62541's `StatusCode.csv` — these are
 *      stable OPC UA spec constants.
 *
 *   2. `_Enum` — an `EnumMeta` subclass used as the metaclass for StatusCode.  
 *      It adds a no-argument default (`StatusCode()` == GOOD),
 *      a members-only `__iter__` and a `__dir__` that exposes member
 *      names. 
 *
 *   3. `StructureType` — the enum (UA_TYPES[UA_TYPES_STRUCTURETYPE]) that
 *      backs every `StructureDefinition.structureType` field.  ns0.py emits
 *      its own `@o6.enumtype StructureType`, but only *after* the first
 *      concrete struct is registered — whose registration already needs the
 *      class to convert `structureType`.
 *
 *   4. `NodeClass` — the enum (UA_TYPES[UA_TYPES_NODECLASS]) that the
 *      decorators attache to every marker class as `_nodeclass`.   *
 * 
 * The six struct bootstrap types (StructureDescription/Definition/Field,
 * EnumDescription/Definition/Field) are also built here, programmatically
 * from open62541's UA_TYPES[] table — see create_bootstrap_struct_types().
 */

#include <open62541/types.h>
#define NO_IMPORT_ARRAY
#include "types_internal.h"

/* Set dct[key] = value, stealing references to key and value (they are
 * built inline as ``PyUnicode_FromString(...)`` / ``PyLong_From...``). */
static int
setItem(PyObject *dct, PyObject *key, PyObject *value) {
    int res = -1;
    if(key && value)
        res = PyObject_SetItem(dct, key, value);
    Py_XDECREF(key);
    Py_XDECREF(value);
    return res;
}

/* ---------------------------------------------------------------------------
 * ``_Enum`` metaclass (subclass of enum.EnumMeta)
 * ------------------------------------------------------------------------- */

/* Allow ``StatusCode()`` (no argument) to default to value 0 (GOOD). */
static PyObject *
PyUAEnum_call(PyObject *cls, PyObject *args, PyObject *kwds) {
    PyObject *call_args = NULL;
    if(PyTuple_Size(args) == 0 && (!kwds || PyDict_Size(kwds) == 0)) {
        PyObject *zero = PyLong_FromLong(0);
        if(!zero)
            return NULL;
        call_args = PyTuple_Pack(1, zero);
        if(!call_args) {
            Py_DECREF(zero);
            return NULL;
        }
        args = call_args;
    }

    PyTypeObject *meta_type = Py_TYPE(cls);
    if(!meta_type->tp_base || !meta_type->tp_base->tp_base ||
       !meta_type->tp_base->tp_base->tp_call) {
        PyErr_SetString(PyExc_TypeError, "Base tp_call not found");
        Py_XDECREF(call_args);
        return NULL;
    }

    PyObject *result = meta_type->tp_base->tp_base->tp_call(cls, args, kwds);
    Py_XDECREF(call_args);
    return result;
}

/* Iterate the enum's members (values), not the raw class dict. */
static PyObject *
PyUAEnum_iter(PyObject *cls) {
    PyObject *members = PyObject_GetAttrString(cls, "__members__");
    if(!members) return NULL;
    PyObject *values = PyMapping_Values(members);
    Py_DECREF(members);
    if(!values) return NULL;
    PyObject *it = PyObject_GetIter(values);
    Py_DECREF(values);
    return it;
}

/* dir(EnumClass) = super().__dir__() ∪ member names. */
static PyObject *
PyUAEnum_dir(PyObject *cls, PyObject *Py_UNUSED(ignored)) {
    PyTypeObject *enum_meta = Py_TYPE(cls)->tp_base;
    if(!enum_meta) return NULL;

    PyObject *dir_func = PyObject_GetAttrString((PyObject*)enum_meta, "__dir__");
    if(!dir_func) return NULL;

    PyObject *super_dir = PyObject_CallFunctionObjArgs(dir_func, cls, NULL);
    Py_DECREF(dir_func);
    if(!super_dir) return NULL;

    PyObject *members_prop = PyObject_GetAttrString(cls, "__members__");
    if(!members_prop) {
        Py_DECREF(super_dir);
        return NULL;
    }

    PyObject *member_names = PyMapping_Keys(members_prop);
    Py_DECREF(members_prop);
    if(!member_names) {
        Py_DECREF(super_dir);
        return NULL;
    }

    PyObject *set = PySet_New(super_dir);
    Py_DECREF(super_dir);
    if(!set) {
        Py_DECREF(member_names);
        return NULL;
    }

    if(PyObject_CallMethod(set, "update", "O", member_names) == NULL) {
        Py_DECREF(set);
        Py_DECREF(member_names);
        return NULL;
    }

    Py_DECREF(member_names);
    PyObject *lst = PySequence_List(set);
    Py_DECREF(set);
    return lst;
}

static PyMethodDef PyUAEnum_methods[] = {
    {"__dir__", (PyCFunction)PyUAEnum_dir, METH_NOARGS, "Custom __dir__"},
    {NULL, NULL, 0, NULL}
};

static PyType_Slot PyUAEnum_slots[] = {
    {Py_tp_call, PyUAEnum_call},
    {Py_tp_iter, PyUAEnum_iter},
    {Py_tp_methods, PyUAEnum_methods},
    {0, NULL}
};

static PyType_Spec PyUAEnum_spec = {
    .name = "o6.types._Enum",
    .basicsize = 0,  /* set dynamically from EnumMeta below */
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .slots = PyUAEnum_slots,
};

/* ---------------------------------------------------------------------------
 * StatusCode
 * ------------------------------------------------------------------------- */

static PyObject *
pyStatusCode_str(PyObject *self, PyObject *Py_UNUSED(ignored)) {
    /* For known IntFlag members, _name_ holds the member name string.
     * For unknown values (boundary=KEEP), _name_ is None. */
    PyObject *name = PyObject_GetAttrString(self, "_name_");
    if(name && name != Py_None && PyUnicode_Check(name))
        return name;
    Py_XDECREF(name);
    /* Unknown value: format as 0xXXXXXXXX (treat as unsigned 32-bit). */
    unsigned long v = PyLong_AsUnsignedLongMask(self);
    if(v == (unsigned long)-1 && PyErr_Occurred())
        return NULL;
    return PyUnicode_FromFormat("0x%08lx", v & 0xFFFFFFFFUL);
}

static PyMethodDef pyStatusCode_str_def = {
    "__str__", (PyCFunction)pyStatusCode_str, METH_NOARGS, NULL
};

/* Name/value pairs transcribed from open62541's StatusCode.csv. */
static const struct { const char *name; unsigned long long value; }
STATUS_CODES[] = {
    {"GOOD", 0ULL},
    {"UNCERTAIN", 1073741824ULL},
    {"BAD", 2147483648ULL},
    {"BAD_UNEXPECTED_ERROR", 2147549184ULL},
    {"BAD_INTERNAL_ERROR", 2147614720ULL},
    {"BAD_OUT_OF_MEMORY", 2147680256ULL},
    {"BAD_RESOURCE_UNAVAILABLE", 2147745792ULL},
    {"BAD_COMMUNICATION_ERROR", 2147811328ULL},
    {"BAD_ENCODING_ERROR", 2147876864ULL},
    {"BAD_DECODING_ERROR", 2147942400ULL},
    {"BAD_ENCODING_LIMITS_EXCEEDED", 2148007936ULL},
    {"BAD_REQUEST_TOO_LARGE", 2159542272ULL},
    {"BAD_RESPONSE_TOO_LARGE", 2159607808ULL},
    {"BAD_UNKNOWN_RESPONSE", 2148073472ULL},
    {"BAD_TIMEOUT", 2148139008ULL},
    {"BAD_SERVICE_UNSUPPORTED", 2148204544ULL},
    {"BAD_SHUTDOWN", 2148270080ULL},
    {"BAD_SERVER_NOT_CONNECTED", 2148335616ULL},
    {"BAD_SERVER_HALTED", 2148401152ULL},
    {"BAD_NOTHING_TO_DO", 2148466688ULL},
    {"BAD_TOO_MANY_OPERATIONS", 2148532224ULL},
    {"BAD_TOO_MANY_MONITORED_ITEMS", 2161836032ULL},
    {"BAD_DATA_TYPE_ID_UNKNOWN", 2148597760ULL},
    {"BAD_CERTIFICATE_INVALID", 2148663296ULL},
    {"BAD_SECURITY_CHECKS_FAILED", 2148728832ULL},
    {"BAD_CERTIFICATE_POLICY_CHECK_FAILED", 2165571584ULL},
    {"BAD_CERTIFICATE_TIME_INVALID", 2148794368ULL},
    {"BAD_CERTIFICATE_ISSUER_TIME_INVALID", 2148859904ULL},
    {"BAD_CERTIFICATE_HOST_NAME_INVALID", 2148925440ULL},
    {"BAD_CERTIFICATE_URI_INVALID", 2148990976ULL},
    {"BAD_CERTIFICATE_USE_NOT_ALLOWED", 2149056512ULL},
    {"BAD_CERTIFICATE_ISSUER_USE_NOT_ALLOWED", 2149122048ULL},
    {"BAD_CERTIFICATE_UNTRUSTED", 2149187584ULL},
    {"BAD_CERTIFICATE_REVOCATION_UNKNOWN", 2149253120ULL},
    {"BAD_CERTIFICATE_ISSUER_REVOCATION_UNKNOWN", 2149318656ULL},
    {"BAD_CERTIFICATE_REVOKED", 2149384192ULL},
    {"BAD_CERTIFICATE_ISSUER_REVOKED", 2149449728ULL},
    {"BAD_CERTIFICATE_CHAIN_INCOMPLETE", 2165112832ULL},
    {"BAD_USER_ACCESS_DENIED", 2149515264ULL},
    {"BAD_IDENTITY_TOKEN_INVALID", 2149580800ULL},
    {"BAD_IDENTITY_TOKEN_REJECTED", 2149646336ULL},
    {"BAD_SECURE_CHANNEL_ID_INVALID", 2149711872ULL},
    {"BAD_INVALID_TIMESTAMP", 2149777408ULL},
    {"BAD_NONCE_INVALID", 2149842944ULL},
    {"BAD_SESSION_ID_INVALID", 2149908480ULL},
    {"BAD_SESSION_CLOSED", 2149974016ULL},
    {"BAD_SESSION_NOT_ACTIVATED", 2150039552ULL},
    {"BAD_SUBSCRIPTION_ID_INVALID", 2150105088ULL},
    {"BAD_REQUEST_HEADER_INVALID", 2150236160ULL},
    {"BAD_TIMESTAMPS_TO_RETURN_INVALID", 2150301696ULL},
    {"BAD_REQUEST_CANCELLED_BY_CLIENT", 2150367232ULL},
    {"BAD_TOO_MANY_ARGUMENTS", 2162491392ULL},
    {"BAD_LICENSE_EXPIRED", 2165178368ULL},
    {"BAD_LICENSE_LIMITS_EXCEEDED", 2165243904ULL},
    {"BAD_LICENSE_NOT_AVAILABLE", 2165309440ULL},
    {"GOOD_SUBSCRIPTION_TRANSFERRED", 2949120ULL},
    {"GOOD_COMPLETES_ASYNCHRONOUSLY", 3014656ULL},
    {"GOOD_OVERLOAD", 3080192ULL},
    {"GOOD_CLAMPED", 3145728ULL},
    {"BAD_NO_COMMUNICATION", 2150694912ULL},
    {"BAD_WAITING_FOR_INITIAL_DATA", 2150760448ULL},
    {"BAD_NODE_ID_INVALID", 2150825984ULL},
    {"BAD_NODE_ID_UNKNOWN", 2150891520ULL},
    {"BAD_ATTRIBUTE_ID_INVALID", 2150957056ULL},
    {"BAD_INDEX_RANGE_INVALID", 2151022592ULL},
    {"BAD_INDEX_RANGE_NO_DATA", 2151088128ULL},
    {"BAD_DATA_ENCODING_INVALID", 2151153664ULL},
    {"BAD_DATA_ENCODING_UNSUPPORTED", 2151219200ULL},
    {"BAD_NOT_READABLE", 2151284736ULL},
    {"BAD_NOT_WRITABLE", 2151350272ULL},
    {"BAD_OUT_OF_RANGE", 2151415808ULL},
    {"BAD_NOT_SUPPORTED", 2151481344ULL},
    {"BAD_NOT_FOUND", 2151546880ULL},
    {"BAD_OBJECT_DELETED", 2151612416ULL},
    {"BAD_NOT_IMPLEMENTED", 2151677952ULL},
    {"BAD_MONITORING_MODE_INVALID", 2151743488ULL},
    {"BAD_MONITORED_ITEM_ID_INVALID", 2151809024ULL},
    {"BAD_MONITORED_ITEM_FILTER_INVALID", 2151874560ULL},
    {"BAD_MONITORED_ITEM_FILTER_UNSUPPORTED", 2151940096ULL},
    {"BAD_FILTER_NOT_ALLOWED", 2152005632ULL},
    {"BAD_STRUCTURE_MISSING", 2152071168ULL},
    {"BAD_EVENT_FILTER_INVALID", 2152136704ULL},
    {"BAD_CONTENT_FILTER_INVALID", 2152202240ULL},
    {"BAD_FILTER_OPERATOR_INVALID", 2160132096ULL},
    {"BAD_FILTER_OPERATOR_UNSUPPORTED", 2160197632ULL},
    {"BAD_FILTER_OPERAND_COUNT_MISMATCH", 2160263168ULL},
    {"BAD_FILTER_OPERAND_INVALID", 2152267776ULL},
    {"BAD_FILTER_ELEMENT_INVALID", 2160328704ULL},
    {"BAD_FILTER_LITERAL_INVALID", 2160394240ULL},
    {"BAD_CONTINUATION_POINT_INVALID", 2152333312ULL},
    {"BAD_NO_CONTINUATION_POINTS", 2152398848ULL},
    {"BAD_REFERENCE_TYPE_ID_INVALID", 2152464384ULL},
    {"BAD_BROWSE_DIRECTION_INVALID", 2152529920ULL},
    {"BAD_NODE_NOT_IN_VIEW", 2152595456ULL},
    {"BAD_NUMERIC_OVERFLOW", 2165440512ULL},
    {"BAD_SERVER_URI_INVALID", 2152660992ULL},
    {"BAD_SERVER_NAME_MISSING", 2152726528ULL},
    {"BAD_DISCOVERY_URL_MISSING", 2152792064ULL},
    {"BAD_SEMAPHORE_FILE_MISSING", 2152857600ULL},
    {"BAD_REQUEST_TYPE_INVALID", 2152923136ULL},
    {"BAD_SECURITY_MODE_REJECTED", 2152988672ULL},
    {"BAD_SECURITY_POLICY_REJECTED", 2153054208ULL},
    {"BAD_TOO_MANY_SESSIONS", 2153119744ULL},
    {"BAD_USER_SIGNATURE_INVALID", 2153185280ULL},
    {"BAD_APPLICATION_SIGNATURE_INVALID", 2153250816ULL},
    {"BAD_NO_VALID_CERTIFICATES", 2153316352ULL},
    {"BAD_IDENTITY_CHANGE_NOT_SUPPORTED", 2160459776ULL},
    {"BAD_REQUEST_CANCELLED_BY_REQUEST", 2153381888ULL},
    {"BAD_PARENT_NODE_ID_INVALID", 2153447424ULL},
    {"BAD_REFERENCE_NOT_ALLOWED", 2153512960ULL},
    {"BAD_NODE_ID_REJECTED", 2153578496ULL},
    {"BAD_NODE_ID_EXISTS", 2153644032ULL},
    {"BAD_NODE_CLASS_INVALID", 2153709568ULL},
    {"BAD_BROWSE_NAME_INVALID", 2153775104ULL},
    {"BAD_BROWSE_NAME_DUPLICATED", 2153840640ULL},
    {"BAD_NODE_ATTRIBUTES_INVALID", 2153906176ULL},
    {"BAD_TYPE_DEFINITION_INVALID", 2153971712ULL},
    {"BAD_SOURCE_NODE_ID_INVALID", 2154037248ULL},
    {"BAD_TARGET_NODE_ID_INVALID", 2154102784ULL},
    {"BAD_DUPLICATE_REFERENCE_NOT_ALLOWED", 2154168320ULL},
    {"BAD_INVALID_SELF_REFERENCE", 2154233856ULL},
    {"BAD_REFERENCE_LOCAL_ONLY", 2154299392ULL},
    {"BAD_NO_DELETE_RIGHTS", 2154364928ULL},
    {"UNCERTAIN_REFERENCE_NOT_DELETED", 1086062592ULL},
    {"BAD_SERVER_INDEX_INVALID", 2154430464ULL},
    {"BAD_VIEW_ID_UNKNOWN", 2154496000ULL},
    {"BAD_VIEW_TIMESTAMP_INVALID", 2160656384ULL},
    {"BAD_VIEW_PARAMETER_MISMATCH", 2160721920ULL},
    {"BAD_VIEW_VERSION_INVALID", 2160787456ULL},
    {"UNCERTAIN_NOT_ALL_NODES_AVAILABLE", 1086324736ULL},
    {"GOOD_RESULTS_MAY_BE_INCOMPLETE", 12189696ULL},
    {"BAD_NOT_TYPE_DEFINITION", 2160590848ULL},
    {"UNCERTAIN_REFERENCE_OUT_OF_SERVER", 1080819712ULL},
    {"BAD_TOO_MANY_MATCHES", 2154627072ULL},
    {"BAD_QUERY_TOO_COMPLEX", 2154692608ULL},
    {"BAD_NO_MATCH", 2154758144ULL},
    {"BAD_MAX_AGE_INVALID", 2154823680ULL},
    {"BAD_SECURITY_MODE_INSUFFICIENT", 2162556928ULL},
    {"BAD_HISTORY_OPERATION_INVALID", 2154889216ULL},
    {"BAD_HISTORY_OPERATION_UNSUPPORTED", 2154954752ULL},
    {"BAD_INVALID_TIMESTAMP_ARGUMENT", 2159869952ULL},
    {"BAD_WRITE_NOT_SUPPORTED", 2155020288ULL},
    {"BAD_TYPE_MISMATCH", 2155085824ULL},
    {"BAD_METHOD_INVALID", 2155151360ULL},
    {"BAD_ARGUMENTS_MISSING", 2155216896ULL},
    {"BAD_NOT_EXECUTABLE", 2165374976ULL},
    {"BAD_TOO_MANY_SUBSCRIPTIONS", 2155282432ULL},
    {"BAD_TOO_MANY_PUBLISH_REQUESTS", 2155347968ULL},
    {"BAD_NO_SUBSCRIPTION", 2155413504ULL},
    {"BAD_SEQUENCE_NUMBER_UNKNOWN", 2155479040ULL},
    {"GOOD_RETRANSMISSION_QUEUE_NOT_SUPPORTED", 14614528ULL},
    {"BAD_MESSAGE_NOT_AVAILABLE", 2155544576ULL},
    {"BAD_INSUFFICIENT_CLIENT_PROFILE", 2155610112ULL},
    {"BAD_STATE_NOT_ACTIVE", 2160001024ULL},
    {"BAD_ALREADY_EXISTS", 2165637120ULL},
    {"BAD_TCP_SERVER_TOO_BUSY", 2155675648ULL},
    {"BAD_TCP_MESSAGE_TYPE_INVALID", 2155741184ULL},
    {"BAD_TCP_SECURE_CHANNEL_UNKNOWN", 2155806720ULL},
    {"BAD_TCP_MESSAGE_TOO_LARGE", 2155872256ULL},
    {"BAD_TCP_NOT_ENOUGH_RESOURCES", 2155937792ULL},
    {"BAD_TCP_INTERNAL_ERROR", 2156003328ULL},
    {"BAD_TCP_ENDPOINT_URL_INVALID", 2156068864ULL},
    {"BAD_REQUEST_INTERRUPTED", 2156134400ULL},
    {"BAD_REQUEST_TIMEOUT", 2156199936ULL},
    {"BAD_SECURE_CHANNEL_CLOSED", 2156265472ULL},
    {"BAD_SECURE_CHANNEL_TOKEN_UNKNOWN", 2156331008ULL},
    {"BAD_SEQUENCE_NUMBER_INVALID", 2156396544ULL},
    {"BAD_PROTOCOL_VERSION_UNSUPPORTED", 2159935488ULL},
    {"BAD_CONFIGURATION_ERROR", 2156462080ULL},
    {"BAD_NOT_CONNECTED", 2156527616ULL},
    {"BAD_DEVICE_FAILURE", 2156593152ULL},
    {"BAD_SENSOR_FAILURE", 2156658688ULL},
    {"BAD_OUT_OF_SERVICE", 2156724224ULL},
    {"BAD_DEADBAND_FILTER_INVALID", 2156789760ULL},
    {"UNCERTAIN_NO_COMMUNICATION_LAST_USABLE_VALUE", 1083113472ULL},
    {"UNCERTAIN_LAST_USABLE_VALUE", 1083179008ULL},
    {"UNCERTAIN_SUBSTITUTE_VALUE", 1083244544ULL},
    {"UNCERTAIN_INITIAL_VALUE", 1083310080ULL},
    {"UNCERTAIN_SENSOR_NOT_ACCURATE", 1083375616ULL},
    {"UNCERTAIN_ENGINEERING_UNITS_EXCEEDED", 1083441152ULL},
    {"UNCERTAIN_SUB_NORMAL", 1083506688ULL},
    {"GOOD_LOCAL_OVERRIDE", 9830400ULL},
    {"BAD_REFRESH_IN_PROGRESS", 2157379584ULL},
    {"BAD_CONDITION_ALREADY_DISABLED", 2157445120ULL},
    {"BAD_CONDITION_ALREADY_ENABLED", 2160852992ULL},
    {"BAD_CONDITION_DISABLED", 2157510656ULL},
    {"BAD_EVENT_ID_UNKNOWN", 2157576192ULL},
    {"BAD_EVENT_NOT_ACKNOWLEDGEABLE", 2159738880ULL},
    {"BAD_DIALOG_NOT_ACTIVE", 2160918528ULL},
    {"BAD_DIALOG_RESPONSE_INVALID", 2160984064ULL},
    {"BAD_CONDITION_BRANCH_ALREADY_ACKED", 2161049600ULL},
    {"BAD_CONDITION_BRANCH_ALREADY_CONFIRMED", 2161115136ULL},
    {"BAD_CONDITION_ALREADY_SHELVED", 2161180672ULL},
    {"BAD_CONDITION_NOT_SHELVED", 2161246208ULL},
    {"BAD_SHELVING_TIME_OUT_OF_RANGE", 2161311744ULL},
    {"BAD_NO_DATA", 2157641728ULL},
    {"BAD_BOUND_NOT_FOUND", 2161573888ULL},
    {"BAD_BOUND_NOT_SUPPORTED", 2161639424ULL},
    {"BAD_DATA_LOST", 2157772800ULL},
    {"BAD_DATA_UNAVAILABLE", 2157838336ULL},
    {"BAD_ENTRY_EXISTS", 2157903872ULL},
    {"BAD_NO_ENTRY_EXISTS", 2157969408ULL},
    {"BAD_TIMESTAMP_NOT_SUPPORTED", 2158034944ULL},
    {"GOOD_ENTRY_INSERTED", 10616832ULL},
    {"GOOD_ENTRY_REPLACED", 10682368ULL},
    {"UNCERTAIN_DATA_SUB_NORMAL", 1084489728ULL},
    {"GOOD_NO_DATA", 10813440ULL},
    {"GOOD_MORE_DATA", 10878976ULL},
    {"BAD_AGGREGATE_LIST_MISMATCH", 2161377280ULL},
    {"BAD_AGGREGATE_NOT_SUPPORTED", 2161442816ULL},
    {"BAD_AGGREGATE_INVALID_INPUTS", 2161508352ULL},
    {"BAD_AGGREGATE_CONFIGURATION_REJECTED", 2161770496ULL},
    {"GOOD_DATA_IGNORED", 14221312ULL},
    {"BAD_REQUEST_NOT_ALLOWED", 2162425856ULL},
    {"BAD_REQUEST_NOT_COMPLETE", 2165506048ULL},
    {"BAD_TRANSACTION_PENDING", 2162688000ULL},
    {"BAD_TICKET_REQUIRED", 2166292480ULL},
    {"BAD_TICKET_INVALID", 2166358016ULL},
    {"GOOD_EDITED", 14417920ULL},
    {"GOOD_POST_ACTION_FAILED", 14483456ULL},
    {"UNCERTAIN_DOMINANT_VALUE_CHANGED", 1088290816ULL},
    {"GOOD_DEPENDENT_VALUE_CHANGED", 14680064ULL},
    {"BAD_DOMINANT_VALUE_CHANGED", 2162229248ULL},
    {"UNCERTAIN_DEPENDENT_VALUE_CHANGED", 1088552960ULL},
    {"BAD_DEPENDENT_VALUE_CHANGED", 2162360320ULL},
    {"GOOD_EDITED_DEPENDENT_VALUE_CHANGED", 18219008ULL},
    {"GOOD_EDITED_DOMINANT_VALUE_CHANGED", 18284544ULL},
    {"GOOD_EDITED_DOMINANT_VALUE_CHANGED_DEPENDENT_VALUE_CHANGED", 18350080ULL},
    {"BAD_EDITED_OUT_OF_RANGE", 2165899264ULL},
    {"BAD_INITIAL_VALUE_OUT_OF_RANGE", 2165964800ULL},
    {"BAD_OUT_OF_RANGE_DOMINANT_VALUE_CHANGED", 2166030336ULL},
    {"BAD_EDITED_OUT_OF_RANGE_DOMINANT_VALUE_CHANGED", 2166095872ULL},
    {"BAD_OUT_OF_RANGE_DOMINANT_VALUE_CHANGED_DEPENDENT_VALUE_CHANGED", 2166161408ULL},
    {"BAD_EDITED_OUT_OF_RANGE_DOMINANT_VALUE_CHANGED_DEPENDENT_VALUE_CHANGED", 2166226944ULL},
    {"GOOD_COMMUNICATION_EVENT", 10944512ULL},
    {"GOOD_SHUTDOWN_EVENT", 11010048ULL},
    {"GOOD_CALL_AGAIN", 11075584ULL},
    {"GOOD_NON_CRITICAL_TIMEOUT", 11141120ULL},
    {"BAD_INVALID_ARGUMENT", 2158690304ULL},
    {"BAD_CONNECTION_REJECTED", 2158755840ULL},
    {"BAD_DISCONNECT", 2158821376ULL},
    {"BAD_CONNECTION_CLOSED", 2158886912ULL},
    {"BAD_INVALID_STATE", 2158952448ULL},
    {"BAD_END_OF_STREAM", 2159017984ULL},
    {"BAD_NO_DATA_AVAILABLE", 2159083520ULL},
    {"BAD_WAITING_FOR_RESPONSE", 2159149056ULL},
    {"BAD_OPERATION_ABANDONED", 2159214592ULL},
    {"BAD_EXPECTED_STREAM_TO_BLOCK", 2159280128ULL},
    {"BAD_WOULD_BLOCK", 2159345664ULL},
    {"BAD_SYNTAX_ERROR", 2159411200ULL},
    {"BAD_MAX_CONNECTIONS_REACHED", 2159476736ULL},
};

/* Build the StatusCode IntFlag (boundary=KEEP) and add it to ``module``.
 *   metaclass : ``_Enum`` (EnumClass)
 *   bases     : (IntFlag,)
 *   prepare   : EnumMeta.__prepare__ (produces the special enum namespace) */
static void
create_statuscode_enum(PyObject *module, PyObject *enum_module,
                       PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args = NULL, *kwargs = NULL;
    PyObject *flag_boundary = NULL, *keep = NULL;

    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("StatusCode"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0)
        goto error;
    for(size_t i = 0; i < sizeof(STATUS_CODES) / sizeof(STATUS_CODES[0]); i++) {
        if(setItem(enum_dict, PyUnicode_FromString(STATUS_CODES[i].name),
                   PyLong_FromUnsignedLongLong(STATUS_CODES[i].value)) < 0)
            goto error;
    }

    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("StatusCode"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL;  /* references taken over by PyTuple_Pack */
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;

    /* Install __str__ as a real method descriptor on the enum class so
     * str(StatusCode.X) returns the member name instead of the numeric
     * value inherited from int. */
    {
        PyObject *descr = PyDescr_NewMethod((PyTypeObject *)enum_class, &pyStatusCode_str_def);
        if(descr) {
            if(PyObject_SetAttrString(enum_class, "__str__", descr) == 0)
                PyType_Modified((PyTypeObject *)enum_class);
            Py_DECREF(descr);
        }
    }
    PyModule_AddObject(module, "StatusCode", enum_class);
    enum_class = NULL;  /* reference taken by PyModule_AddObject */
  error:
    if(PyErr_Occurred())
        PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}

/* ---------------------------------------------------------------------------
 * StructureType
 * ---------------------------------------------------------------------------
 *
 * `StructureType` (UA_TYPES[UA_TYPES_STRUCTURETYPE], ns=0;i=98) is the enum
 * carried by the `structureType` field of every `StructureDefinition`.
 * When `o6.nsx.ns0` registers its very first `@o6.datatype` the C setter
 * for `_StructureDefinition.structureType` auto-converts the raw int to a
 * StructureType member, which means `UA2PYType()` must already be able to
 * resolve `UA_TYPES[UA_TYPES_STRUCTURETYPE]` to a Python class. */
static void
create_structuretype_enum(PyObject *module) {
    PyObject *enum_module = PyImport_ImportModule("enum");
    if(!enum_module) return;
    PyObject *IntEnum = PyObject_GetAttrString(enum_module, "IntEnum");
    if(IntEnum) {
        PyObject *members = PyDict_New();
        if(members) {
            setItem(members, PyUnicode_FromString("STRUCTURE"),
                    PyLong_FromLong(UA_STRUCTURETYPE_STRUCTURE));
            setItem(members, PyUnicode_FromString("STRUCTURE_WITH_OPTIONAL_FIELDS"),
                    PyLong_FromLong(UA_STRUCTURETYPE_STRUCTUREWITHOPTIONALFIELDS));
            setItem(members, PyUnicode_FromString("UNION"),
                    PyLong_FromLong(UA_STRUCTURETYPE_UNION));
            setItem(members, PyUnicode_FromString("STRUCTURE_WITH_SUBTYPED_VALUES"),
                    PyLong_FromLong(UA_STRUCTURETYPE_STRUCTUREWITHSUBTYPEDVALUES));
            setItem(members, PyUnicode_FromString("UNION_WITH_SUBTYPED_VALUES"),
                    PyLong_FromLong(UA_STRUCTURETYPE_UNIONWITHSUBTYPEDVALUES));
            PyObject *cls =
                PyObject_CallFunction(IntEnum, "sO", "StructureType", members);
            if(cls) {
                PyTypeObject_setUAType((PyTypeObject *)cls,
                                       &UA_TYPES[UA_TYPES_STRUCTURETYPE]);
                /* pyUATypes[] borrows; the module below keeps the ref alive. */
                pyUATypes[UA_TYPES_STRUCTURETYPE] = (PyTypeObject *)cls;
                PyModule_AddObject(module, "StructureType", cls);
            } else {
                PyErr_Clear();
            }
            Py_DECREF(members);
        }
        Py_DECREF(IntEnum);
    }
    Py_DECREF(enum_module);
    PyErr_Clear();  /* non-fatal if anything above failed */
}

/* ---------------------------------------------------------------------------
 * NodeClass
 * ---------------------------------------------------------------------------
 *
 * `NodeClass` (UA_TYPES[UA_TYPES_NODECLASS], ns=0;i=257) is the enum
 * every decorator marker carries as `_nodeclass` (so the
 * `@o6.referencetype` decorator can store the UA_NodeClass alongside
 * the marker class for the address-space injection). */
static void
create_nodeclass_enum(PyObject *module) {
    PyObject *enum_module = PyImport_ImportModule("enum");
    if(!enum_module) return;
    PyObject *IntEnum = PyObject_GetAttrString(enum_module, "IntEnum");
    if(IntEnum) {
        PyObject *members = PyDict_New();
        if(members) {
            setItem(members, PyUnicode_FromString("UNSPECIFIED"),
                    PyLong_FromLong(UA_NODECLASS_UNSPECIFIED));
            setItem(members, PyUnicode_FromString("OBJECT"),
                    PyLong_FromLong(UA_NODECLASS_OBJECT));
            setItem(members, PyUnicode_FromString("VARIABLE"),
                    PyLong_FromLong(UA_NODECLASS_VARIABLE));
            setItem(members, PyUnicode_FromString("METHOD"),
                    PyLong_FromLong(UA_NODECLASS_METHOD));
            setItem(members, PyUnicode_FromString("OBJECT_TYPE"),
                    PyLong_FromLong(UA_NODECLASS_OBJECTTYPE));
            setItem(members, PyUnicode_FromString("VARIABLE_TYPE"),
                    PyLong_FromLong(UA_NODECLASS_VARIABLETYPE));
            setItem(members, PyUnicode_FromString("REFERENCE_TYPE"),
                    PyLong_FromLong(UA_NODECLASS_REFERENCETYPE));
            setItem(members, PyUnicode_FromString("DATA_TYPE"),
                    PyLong_FromLong(UA_NODECLASS_DATATYPE));
            setItem(members, PyUnicode_FromString("VIEW"),
                    PyLong_FromLong(UA_NODECLASS_VIEW));
            PyObject *cls =
                PyObject_CallFunction(IntEnum, "sO", "NodeClass", members);
            if(cls) {
                PyTypeObject_setUAType((PyTypeObject *)cls,
                                       &UA_TYPES[UA_TYPES_NODECLASS]);
                /* pyUATypes[] borrows; the module below keeps the ref alive. */
                pyUATypes[UA_TYPES_NODECLASS] = (PyTypeObject *)cls;
                PyModule_AddObject(module, "NodeClass", cls);
            } else {
                PyErr_Clear();
            }
            Py_DECREF(members);
        }
        Py_DECREF(IntEnum);
    }
    Py_DECREF(enum_module);
    PyErr_Clear();  /* non-fatal if anything above failed */
}

void
create_bootstrap_enums(PyObject *module) {
    PyObject *enum_module = PyImport_ImportModule("enum");
    if(!enum_module) return;
    PyObject *EnumMeta = NULL, *IntFlag = NULL, *bases = NULL,
             *UAEnum_Type = NULL, *prepare = NULL;
    EnumMeta = PyObject_GetAttrString(enum_module, "EnumMeta");
    IntFlag = PyObject_GetAttrString(enum_module, "IntFlag");
    if(!EnumMeta || !IntFlag) goto done;

    /* Build the ``_Enum`` metaclass as a subclass of EnumMeta. */
    bases = PyTuple_Pack(1, EnumMeta);
    if(!bases) goto done;
    Py_INCREF(enum_module);  /* counter the reference stolen by PyTuple_Pack */
    PyUAEnum_spec.basicsize = ((PyTypeObject *)EnumMeta)->tp_basicsize;
    UAEnum_Type = PyType_FromSpecWithBases(&PyUAEnum_spec, bases);
    if(!UAEnum_Type) goto done;
    if(PyModule_AddObject(module, "_Enum", UAEnum_Type) < 0) goto done;
    Py_INCREF(UAEnum_Type);  /* counter the reference stolen by PyModule_AddObject */
    Py_DECREF(bases);

    /* StatusCode members subclass IntFlag; the ``_Enum`` metaclass wraps it. */
    bases = PyTuple_Pack(1, IntFlag);
    if(!bases) goto done;
    Py_INCREF(IntFlag);  /* counter the reference stolen by PyTuple_Pack */
    prepare = PyObject_GetAttrString(EnumMeta, "__prepare__");
    if(!prepare) goto done;

    create_statuscode_enum(module, enum_module, UAEnum_Type, bases, prepare);

    /* StructureType — needed before ns0's first @o6.datatype registration. */
    create_structuretype_enum(module);

    /* NodeClass — needed before the first @o6.referencetype at the top of
     * ns0.py can attach ``_nodeclass = NodeClass.REFERENCE_TYPE``. */
    create_nodeclass_enum(module);
done:
    Py_DECREF(enum_module);
    Py_XDECREF(EnumMeta);
    Py_XDECREF(IntFlag);
    Py_XDECREF(bases);
    Py_XDECREF(UAEnum_Type);
    Py_XDECREF(prepare);
}

/* ---------------------------------------------------------------------------
 * NS0 bootstrap struct types
 * ------------------------------------------------------------------------- */

/* The six UA_TYPES[] indices we build, in declaration order. */
static const unsigned bootstrapTypeIndices[] = {
    UA_TYPES_STRUCTUREDESCRIPTION,
    UA_TYPES_STRUCTUREDEFINITION,
    UA_TYPES_STRUCTUREFIELD,
    UA_TYPES_ENUMDESCRIPTION,
    UA_TYPES_ENUMDEFINITION,
    UA_TYPES_ENUMFIELD,
};

int
create_bootstrap_struct_types(PyObject *module) {
    static PyMethodDef struct_methods[] = {
        {"__dir__", (PyCFunction)pyUAStruct_dir, METH_NOARGS, NULL},
        {"__copy__", (PyCFunction)pyUAStruct_copy, METH_NOARGS, NULL},
        {"__deepcopy__", (PyCFunction)pyUA_deepcopy, METH_O, NULL},
        {NULL}
    };

    static PyType_Slot pyUAStruct_slots[] = {
        {Py_tp_dealloc, (void *)pyUAStruct_dealloc},
        {Py_tp_traverse, (void *)pyUAStruct_traverse},
        {Py_tp_clear, (void *)pyUAStruct_clear},
        {Py_tp_new, (void *)PyType_GenericNew},
        {Py_tp_alloc, (void *)PyType_GenericAlloc},
        {Py_tp_str, (void *)pyUAStruct_str},
        {Py_tp_repr, (void *)pyUAStruct_repr},
        {Py_tp_getattro, (void *)pyUAStruct_getattro},
        {Py_tp_setattro, (void *)pyUAStruct_setattro},
        {Py_tp_methods, (void *)struct_methods},
        {0, NULL}  // terminator
    };

    for(size_t k = 0; k < sizeof(bootstrapTypeIndices) / sizeof(bootstrapTypeIndices[0]); k++) {
        unsigned i = bootstrapTypeIndices[k];
        /* Strip any namespace qualifier (e.g. "1:Foo" -> "Foo"); ns0 names
         * like "StructureDescription" are already unqualified. */
        const char *rawName = UA_TYPES[i].typeName;
        const char *colon = strchr(rawName, ':');
        const char *shortName = colon ? colon + 1 : rawName;

        /* PyType_Spec.name must outlive the type; keep a per-type buffer. */
        static char pyTypeNames[sizeof(bootstrapTypeIndices) / sizeof(bootstrapTypeIndices[0])][64];
        snprintf(pyTypeNames[k], sizeof(pyTypeNames[k]), "o6.%s", shortName);

        PyType_Spec structSpec = {
            .name = pyTypeNames[k],
            .basicsize = sizeof(PyUAStruct),
            .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC | Py_TPFLAGS_BASETYPE,
            .slots = pyUAStruct_slots
        };

        PyObject *pyType = PyType_FromSpec(&structSpec);
        if(!pyType)
            return -1;
        PyTypeObject_setUAType((PyTypeObject*)pyType, &UA_TYPES[i]);
        pyUATypes[i] = (PyTypeObject*)pyType;

        /* Expose directly as ``o6._o6.types.<ShortName>`` so Python can bind
         * the six types by name (o6.namespace) without an array lookup. */
        int rc = PyModule_AddObjectRef(module, shortName, pyType);
        Py_DECREF(pyType);
        if(rc < 0)
            return -1;
    }

    return 0;
}
