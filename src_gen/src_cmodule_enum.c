/* Copyright (c) 2026 o6 Automation GmbH
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published
 * by the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program. If not, see <https://www.gnu.org/licenses/>.
 */

#include <Python.h>
#include <setobject.h>

// Forward declarations for enum creation functions
static void create_NamingRuleType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_RedundantServerMode_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_OpenFileMode_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_IdentityCriteriaType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_ConversionLimitEnum_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_AlarmMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_TrustListValidationOptions_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_TrustListMasks_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_PubSubState_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_DataSetFieldFlags_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_ActionState_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_DataSetFieldContentMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_OverrideValueHandling_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_DataSetOrderingType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_UadpNetworkMessageContentMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_UadpDataSetMessageContentMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_JsonNetworkMessageContentMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_JsonDataSetMessageContentMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_BrokerTransportQualityOfService_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_PubSubConfigurationRefMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_DiagnosticsLevel_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_PubSubDiagnosticsCounterClassification_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_PasswordOptionsMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_UserConfigurationMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_Duplex_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_InterfaceAdminStatus_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_InterfaceOperStatus_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_NegotiationStatus_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_TsnFailureCode_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_TsnStreamState_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_TsnTalkerStatus_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_TsnListenerStatus_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_ChassisIdSubtype_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_PortIdSubtype_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_ManAddrIfSubtype_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_LldpSystemCapabilitiesMap_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_IdType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_NodeClass_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_PermissionType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_AccessLevelType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_AccessLevelExType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_EventNotifierType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_AccessRestrictionType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_StructureType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_ApplicationType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_MessageSecurityMode_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_UserTokenType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_SecurityTokenRequestType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_NodeAttributesMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_AttributeWriteMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_FilterOperator_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_HistoryUpdateType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_PerformUpdateType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_RedundancySupport_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_ServerState_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_AxisScaleEnumeration_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_ExceptionDeviationFormat_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_BrowseDirection_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_BrowseResultMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_TimestampsToReturn_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_MonitoringMode_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_DataChangeTrigger_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_DeadbandType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);
static void create_StatusCode_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);


// add elements to the dictionary and release key+value
// for inline operations
static int
setItem(PyObject *dct, PyObject *key, PyObject *value) {
    int res = -1;
    if(key && value)
        res = PyObject_SetItem(dct, key, value);
    Py_XDECREF(key);
    Py_XDECREF(value);
    return res;
}

// Overload __call__ for enums to allow initialization without a value (default = 0)
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

static PyObject *
PyUAEnum_iter(PyObject *cls) {
    PyObject *members = PyObject_GetAttrString(cls, "__members__");
    if (!members) return NULL;
    PyObject *values = PyMapping_Values(members);
    Py_DECREF(members);
    if(!values) return NULL;
    PyObject *it = PyObject_GetIter(values);
    Py_DECREF(values);
    return it;
}

static PyObject *
PyUAEnum_dir(PyObject *cls, PyObject *Py_UNUSED(ignored)) {
    PyTypeObject *enum_meta = Py_TYPE(cls)->tp_base;
    if(!enum_meta) return NULL;

    PyObject *dir_func = PyObject_GetAttrString((PyObject*)enum_meta, "__dir__");
    if(!dir_func) return NULL;

    PyObject *super_dir = PyObject_CallFunctionObjArgs(dir_func, cls, NULL);
    Py_DECREF(dir_func);
    if(!super_dir) {
        PyErr_Print();
        return NULL;
    }

    PyObject *members_prop = PyObject_GetAttrString(cls, "__members__");
    if(!members_prop) {
        PyErr_Print();
        Py_DECREF(super_dir);
        return NULL;
    }

    PyObject *member_names = PyMapping_Keys(members_prop);
    Py_DECREF(members_prop);
    if(!member_names) {
        PyErr_Print();
        Py_DECREF(super_dir);
        return NULL;
    }

    PyObject *set = PySet_New(super_dir);
    Py_DECREF(super_dir);
    if(!set) {
        PyErr_Print();
        Py_DECREF(member_names);
        return NULL;
    }

    if(PyObject_CallMethod(set, "update", "O", member_names) == NULL) {
        PyErr_Print();
        Py_DECREF(set);
        Py_DECREF(member_names);
        return NULL;
    }

    Py_DECREF(member_names);
    return PySequence_List(set);
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
    .basicsize = 0, // set dynamically
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .slots = PyUAEnum_slots,
};

// Function to create all enums and add them to the module
void create_all_enums(PyObject *module) {
    PyObject *enum_module = PyImport_ImportModule("enum");
    if(!enum_module) return;
    PyObject *EnumMeta = NULL, *IntFlag = NULL, *bases = NULL,
             *UAEnum_Type = NULL, *prepare = NULL;
    EnumMeta = PyObject_GetAttrString(enum_module, "EnumMeta");
    IntFlag = PyObject_GetAttrString(enum_module, "IntFlag");
    if(!EnumMeta || !IntFlag) goto done;
    bases = PyTuple_Pack(1, EnumMeta);
    if(!bases) goto done;
    Py_INCREF(enum_module); // Counter-act the reference stolen in PyTuple_Pack
    PyUAEnum_spec.basicsize = ((PyTypeObject *)EnumMeta)->tp_basicsize;
    UAEnum_Type = PyType_FromSpecWithBases(&PyUAEnum_spec, bases);
    if(!UAEnum_Type) goto done;
    if(PyModule_AddObject(module, "_Enum", UAEnum_Type) < 0) goto done;
    Py_INCREF(UAEnum_Type); // Counter the reference stolen in PyModule_AddObject
    Py_DECREF(bases);
    bases = PyTuple_Pack(1, IntFlag);
    if(!bases) goto done;
    Py_INCREF(IntFlag); // Counter-act the reference stolen in PyTuple_Pack
    prepare = PyObject_GetAttrString(EnumMeta, "__prepare__");
    if(!prepare) goto done;
    create_NamingRuleType_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_RedundantServerMode_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_OpenFileMode_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_IdentityCriteriaType_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_ConversionLimitEnum_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_AlarmMask_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_TrustListValidationOptions_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_TrustListMasks_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_PubSubState_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_DataSetFieldFlags_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_ActionState_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_DataSetFieldContentMask_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_OverrideValueHandling_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_DataSetOrderingType_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_UadpNetworkMessageContentMask_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_UadpDataSetMessageContentMask_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_JsonNetworkMessageContentMask_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_JsonDataSetMessageContentMask_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_BrokerTransportQualityOfService_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_PubSubConfigurationRefMask_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_DiagnosticsLevel_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_PubSubDiagnosticsCounterClassification_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_PasswordOptionsMask_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_UserConfigurationMask_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_Duplex_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_InterfaceAdminStatus_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_InterfaceOperStatus_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_NegotiationStatus_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_TsnFailureCode_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_TsnStreamState_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_TsnTalkerStatus_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_TsnListenerStatus_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_ChassisIdSubtype_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_PortIdSubtype_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_ManAddrIfSubtype_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_LldpSystemCapabilitiesMap_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_IdType_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_NodeClass_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_PermissionType_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_AccessLevelType_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_AccessLevelExType_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_EventNotifierType_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_AccessRestrictionType_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_StructureType_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_ApplicationType_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_MessageSecurityMode_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_UserTokenType_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_SecurityTokenRequestType_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_NodeAttributesMask_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_AttributeWriteMask_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_FilterOperator_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_HistoryUpdateType_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_PerformUpdateType_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_RedundancySupport_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_ServerState_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_AxisScaleEnumeration_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_ExceptionDeviationFormat_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_BrowseDirection_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_BrowseResultMask_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_TimestampsToReturn_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_MonitoringMode_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_DataChangeTrigger_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_DeadbandType_enum(module, enum_module, UAEnum_Type, bases, prepare);
    create_StatusCode_enum(module, enum_module, UAEnum_Type, bases, prepare);
done:
    Py_DECREF(enum_module);
    Py_XDECREF(EnumMeta);
    Py_XDECREF(IntFlag);
    Py_XDECREF(bases);
    Py_XDECREF(UAEnum_Type);
    Py_XDECREF(prepare);
}

static PyObject *
pyStatusCode_str(PyObject *self, PyObject *Py_UNUSED(ignored)) {
    // For known IntFlag members, _name_ holds the member name string.
    // For unknown values (boundary=KEEP), _name_ is None.
    PyObject *name = PyObject_GetAttrString(self, "_name_");
    if (name && name != Py_None && PyUnicode_Check(name))
        return name;
    Py_XDECREF(name);
    // Unknown value: format as 0xXXXXXXXX (treat as unsigned 32-bit).
    unsigned long v = PyLong_AsUnsignedLongMask(self);
    if (v == (unsigned long)-1 && PyErr_Occurred())
        return NULL;
    return PyUnicode_FromFormat("0x%08lx", v & 0xFFFFFFFFUL);
}

static PyMethodDef pyStatusCode_str_def = {
    "__str__", (PyCFunction)pyStatusCode_str, METH_NOARGS, NULL
};

// Enum: NamingRuleType
static void create_NamingRuleType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("NamingRuleType"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("MANDATORY"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("OPTIONAL"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("CONSTRAINT"), PyLong_FromUnsignedLongLong(3ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("NamingRuleType"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "NamingRuleType", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: RedundantServerMode
static void create_RedundantServerMode_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("RedundantServerMode"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("PRIMARYWITHBACKUP"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("PRIMARYONLY"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("BACKUPREADY"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("BACKUPNOTREADY"), PyLong_FromUnsignedLongLong(3ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("RedundantServerMode"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "RedundantServerMode", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: OpenFileMode
static void create_OpenFileMode_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("OpenFileMode"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("READ"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("WRITE"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("ERASEEXISTING"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("APPEND"), PyLong_FromUnsignedLongLong(8ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("OpenFileMode"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "OpenFileMode", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: IdentityCriteriaType
static void create_IdentityCriteriaType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("IdentityCriteriaType"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("USERNAME"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("THUMBPRINT"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("ROLE"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("GROUPID"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("ANONYMOUS"), PyLong_FromUnsignedLongLong(5ULL));
    setItem(enum_dict, PyUnicode_FromString("AUTHENTICATEDUSER"), PyLong_FromUnsignedLongLong(6ULL));
    setItem(enum_dict, PyUnicode_FromString("APPLICATION"), PyLong_FromUnsignedLongLong(7ULL));
    setItem(enum_dict, PyUnicode_FromString("X509SUBJECT"), PyLong_FromUnsignedLongLong(8ULL));
    setItem(enum_dict, PyUnicode_FromString("TRUSTEDAPPLICATION"), PyLong_FromUnsignedLongLong(9ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("IdentityCriteriaType"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "IdentityCriteriaType", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: ConversionLimitEnum
static void create_ConversionLimitEnum_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("ConversionLimitEnum"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("NOCONVERSION"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("LIMITED"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("UNLIMITED"), PyLong_FromUnsignedLongLong(2ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("ConversionLimitEnum"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "ConversionLimitEnum", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: AlarmMask
static void create_AlarmMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("AlarmMask"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("ACTIVE"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("UNACKNOWLEDGED"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("UNCONFIRMED"), PyLong_FromUnsignedLongLong(2ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("AlarmMask"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "AlarmMask", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: TrustListValidationOptions
static void create_TrustListValidationOptions_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("TrustListValidationOptions"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("SUPPRESSCERTIFICATEEXPIRED"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("SUPPRESSHOSTNAMEINVALID"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("SUPPRESSREVOCATIONSTATUSUNKNOWN"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("SUPPRESSISSUERCERTIFICATEEXPIRED"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("SUPPRESSISSUERREVOCATIONSTATUSUNKNOWN"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("CHECKREVOCATIONSTATUSONLINE"), PyLong_FromUnsignedLongLong(5ULL));
    setItem(enum_dict, PyUnicode_FromString("CHECKREVOCATIONSTATUSOFFLINE"), PyLong_FromUnsignedLongLong(6ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("TrustListValidationOptions"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "TrustListValidationOptions", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: TrustListMasks
static void create_TrustListMasks_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("TrustListMasks"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("NONE"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("TRUSTEDCERTIFICATES"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("TRUSTEDCRLS"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("ISSUERCERTIFICATES"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("ISSUERCRLS"), PyLong_FromUnsignedLongLong(8ULL));
    setItem(enum_dict, PyUnicode_FromString("ALL"), PyLong_FromUnsignedLongLong(15ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("TrustListMasks"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "TrustListMasks", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: PubSubState
static void create_PubSubState_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("PubSubState"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("DISABLED"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("PAUSED"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("OPERATIONAL"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("ERROR"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("PREOPERATIONAL"), PyLong_FromUnsignedLongLong(4ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("PubSubState"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "PubSubState", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: DataSetFieldFlags
static void create_DataSetFieldFlags_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("DataSetFieldFlags"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("PROMOTEDFIELD"), PyLong_FromUnsignedLongLong(0ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("DataSetFieldFlags"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "DataSetFieldFlags", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: ActionState
static void create_ActionState_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("ActionState"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("IDLE"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("EXECUTING"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("DONE"), PyLong_FromUnsignedLongLong(2ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("ActionState"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "ActionState", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: DataSetFieldContentMask
static void create_DataSetFieldContentMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("DataSetFieldContentMask"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("STATUSCODE"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("SOURCETIMESTAMP"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("SERVERTIMESTAMP"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("SOURCEPICOSECONDS"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("SERVERPICOSECONDS"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("RAWDATA"), PyLong_FromUnsignedLongLong(5ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("DataSetFieldContentMask"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "DataSetFieldContentMask", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: OverrideValueHandling
static void create_OverrideValueHandling_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("OverrideValueHandling"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("DISABLED"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("LASTUSABLEVALUE"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("OVERRIDEVALUE"), PyLong_FromUnsignedLongLong(2ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("OverrideValueHandling"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "OverrideValueHandling", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: DataSetOrderingType
static void create_DataSetOrderingType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("DataSetOrderingType"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("UNDEFINED"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("ASCENDINGWRITERID"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("ASCENDINGWRITERIDSINGLE"), PyLong_FromUnsignedLongLong(2ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("DataSetOrderingType"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "DataSetOrderingType", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: UadpNetworkMessageContentMask
static void create_UadpNetworkMessageContentMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("UadpNetworkMessageContentMask"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("PUBLISHERID"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("GROUPHEADER"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("WRITERGROUPID"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("GROUPVERSION"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("NETWORKMESSAGENUMBER"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("SEQUENCENUMBER"), PyLong_FromUnsignedLongLong(5ULL));
    setItem(enum_dict, PyUnicode_FromString("PAYLOADHEADER"), PyLong_FromUnsignedLongLong(6ULL));
    setItem(enum_dict, PyUnicode_FromString("TIMESTAMP"), PyLong_FromUnsignedLongLong(7ULL));
    setItem(enum_dict, PyUnicode_FromString("PICOSECONDS"), PyLong_FromUnsignedLongLong(8ULL));
    setItem(enum_dict, PyUnicode_FromString("DATASETCLASSID"), PyLong_FromUnsignedLongLong(9ULL));
    setItem(enum_dict, PyUnicode_FromString("PROMOTEDFIELDS"), PyLong_FromUnsignedLongLong(10ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("UadpNetworkMessageContentMask"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "UadpNetworkMessageContentMask", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: UadpDataSetMessageContentMask
static void create_UadpDataSetMessageContentMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("UadpDataSetMessageContentMask"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("TIMESTAMP"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("PICOSECONDS"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("STATUS"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("MAJORVERSION"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("MINORVERSION"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("SEQUENCENUMBER"), PyLong_FromUnsignedLongLong(5ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("UadpDataSetMessageContentMask"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "UadpDataSetMessageContentMask", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: JsonNetworkMessageContentMask
static void create_JsonNetworkMessageContentMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("JsonNetworkMessageContentMask"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("NETWORKMESSAGEHEADER"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("DATASETMESSAGEHEADER"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("SINGLEDATASETMESSAGE"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("PUBLISHERID"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("DATASETCLASSID"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("REPLYTO"), PyLong_FromUnsignedLongLong(5ULL));
    setItem(enum_dict, PyUnicode_FromString("WRITERGROUPNAME"), PyLong_FromUnsignedLongLong(6ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("JsonNetworkMessageContentMask"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "JsonNetworkMessageContentMask", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: JsonDataSetMessageContentMask
static void create_JsonDataSetMessageContentMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("JsonDataSetMessageContentMask"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("DATASETWRITERID"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("METADATAVERSION"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("SEQUENCENUMBER"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("TIMESTAMP"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("STATUS"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("MESSAGETYPE"), PyLong_FromUnsignedLongLong(5ULL));
    setItem(enum_dict, PyUnicode_FromString("DATASETWRITERNAME"), PyLong_FromUnsignedLongLong(6ULL));
    setItem(enum_dict, PyUnicode_FromString("FIELDENCODING1"), PyLong_FromUnsignedLongLong(7ULL));
    setItem(enum_dict, PyUnicode_FromString("PUBLISHERID"), PyLong_FromUnsignedLongLong(8ULL));
    setItem(enum_dict, PyUnicode_FromString("WRITERGROUPNAME"), PyLong_FromUnsignedLongLong(9ULL));
    setItem(enum_dict, PyUnicode_FromString("MINORVERSION"), PyLong_FromUnsignedLongLong(10ULL));
    setItem(enum_dict, PyUnicode_FromString("FIELDENCODING2"), PyLong_FromUnsignedLongLong(11ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("JsonDataSetMessageContentMask"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "JsonDataSetMessageContentMask", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: BrokerTransportQualityOfService
static void create_BrokerTransportQualityOfService_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("BrokerTransportQualityOfService"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("NOTSPECIFIED"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("BESTEFFORT"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("ATLEASTONCE"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("ATMOSTONCE"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("EXACTLYONCE"), PyLong_FromUnsignedLongLong(4ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("BrokerTransportQualityOfService"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "BrokerTransportQualityOfService", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: PubSubConfigurationRefMask
static void create_PubSubConfigurationRefMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("PubSubConfigurationRefMask"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("ELEMENTADD"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("ELEMENTMATCH"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("ELEMENTMODIFY"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("ELEMENTREMOVE"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("REFERENCEWRITER"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("REFERENCEREADER"), PyLong_FromUnsignedLongLong(5ULL));
    setItem(enum_dict, PyUnicode_FromString("REFERENCEWRITERGROUP"), PyLong_FromUnsignedLongLong(6ULL));
    setItem(enum_dict, PyUnicode_FromString("REFERENCEREADERGROUP"), PyLong_FromUnsignedLongLong(7ULL));
    setItem(enum_dict, PyUnicode_FromString("REFERENCECONNECTION"), PyLong_FromUnsignedLongLong(8ULL));
    setItem(enum_dict, PyUnicode_FromString("REFERENCEPUBDATASET"), PyLong_FromUnsignedLongLong(9ULL));
    setItem(enum_dict, PyUnicode_FromString("REFERENCESUBDATASET"), PyLong_FromUnsignedLongLong(10ULL));
    setItem(enum_dict, PyUnicode_FromString("REFERENCESECURITYGROUP"), PyLong_FromUnsignedLongLong(11ULL));
    setItem(enum_dict, PyUnicode_FromString("REFERENCEPUSHTARGET"), PyLong_FromUnsignedLongLong(12ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("PubSubConfigurationRefMask"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "PubSubConfigurationRefMask", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: DiagnosticsLevel
static void create_DiagnosticsLevel_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("DiagnosticsLevel"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("BASIC"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("ADVANCED"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("INFO"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("LOG"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("DEBUG"), PyLong_FromUnsignedLongLong(4ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("DiagnosticsLevel"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "DiagnosticsLevel", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: PubSubDiagnosticsCounterClassification
static void create_PubSubDiagnosticsCounterClassification_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("PubSubDiagnosticsCounterClassification"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("INFORMATION"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("ERROR"), PyLong_FromUnsignedLongLong(1ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("PubSubDiagnosticsCounterClassification"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "PubSubDiagnosticsCounterClassification", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: PasswordOptionsMask
static void create_PasswordOptionsMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("PasswordOptionsMask"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("SUPPORTINITIALPASSWORDCHANGE"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("SUPPORTDISABLEUSER"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("SUPPORTDISABLEDELETEFORUSER"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("SUPPORTNOCHANGEFORUSER"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("SUPPORTDESCRIPTIONFORUSER"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("REQUIRESUPPERCASECHARACTERS"), PyLong_FromUnsignedLongLong(5ULL));
    setItem(enum_dict, PyUnicode_FromString("REQUIRESLOWERCASECHARACTERS"), PyLong_FromUnsignedLongLong(6ULL));
    setItem(enum_dict, PyUnicode_FromString("REQUIRESDIGITCHARACTERS"), PyLong_FromUnsignedLongLong(7ULL));
    setItem(enum_dict, PyUnicode_FromString("REQUIRESSPECIALCHARACTERS"), PyLong_FromUnsignedLongLong(8ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("PasswordOptionsMask"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "PasswordOptionsMask", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: UserConfigurationMask
static void create_UserConfigurationMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("UserConfigurationMask"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("NODELETE"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("DISABLED"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("NOCHANGEBYUSER"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("MUSTCHANGEPASSWORD"), PyLong_FromUnsignedLongLong(3ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("UserConfigurationMask"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "UserConfigurationMask", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: Duplex
static void create_Duplex_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("Duplex"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("FULL"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("HALF"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("UNKNOWN"), PyLong_FromUnsignedLongLong(2ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("Duplex"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "Duplex", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: InterfaceAdminStatus
static void create_InterfaceAdminStatus_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("InterfaceAdminStatus"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("UP"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("DOWN"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("TESTING"), PyLong_FromUnsignedLongLong(2ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("InterfaceAdminStatus"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "InterfaceAdminStatus", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: InterfaceOperStatus
static void create_InterfaceOperStatus_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("InterfaceOperStatus"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("UP"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("DOWN"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("TESTING"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("UNKNOWN"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("DORMANT"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("NOTPRESENT"), PyLong_FromUnsignedLongLong(5ULL));
    setItem(enum_dict, PyUnicode_FromString("LOWERLAYERDOWN"), PyLong_FromUnsignedLongLong(6ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("InterfaceOperStatus"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "InterfaceOperStatus", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: NegotiationStatus
static void create_NegotiationStatus_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("NegotiationStatus"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("INPROGRESS"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("COMPLETE"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("FAILED"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("UNKNOWN"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("NONEGOTIATION"), PyLong_FromUnsignedLongLong(4ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("NegotiationStatus"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "NegotiationStatus", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: TsnFailureCode
static void create_TsnFailureCode_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("TsnFailureCode"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("NOFAILURE"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("INSUFFICIENTBANDWIDTH"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("INSUFFICIENTRESOURCES"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("INSUFFICIENTTRAFFICCLASSBANDWIDTH"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("STREAMIDINUSE"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("STREAMDESTINATIONADDRESSINUSE"), PyLong_FromUnsignedLongLong(5ULL));
    setItem(enum_dict, PyUnicode_FromString("STREAMPREEMPTEDBYHIGHERRANK"), PyLong_FromUnsignedLongLong(6ULL));
    setItem(enum_dict, PyUnicode_FromString("LATENCYHASCHANGED"), PyLong_FromUnsignedLongLong(7ULL));
    setItem(enum_dict, PyUnicode_FromString("EGRESSPORTNOTAVBCAPABLE"), PyLong_FromUnsignedLongLong(8ULL));
    setItem(enum_dict, PyUnicode_FromString("USEDIFFERENTDESTINATIONADDRESS"), PyLong_FromUnsignedLongLong(9ULL));
    setItem(enum_dict, PyUnicode_FromString("OUTOFMSRPRESOURCES"), PyLong_FromUnsignedLongLong(10ULL));
    setItem(enum_dict, PyUnicode_FromString("OUTOFMMRPRESOURCES"), PyLong_FromUnsignedLongLong(11ULL));
    setItem(enum_dict, PyUnicode_FromString("CANNOTSTOREDESTINATIONADDRESS"), PyLong_FromUnsignedLongLong(12ULL));
    setItem(enum_dict, PyUnicode_FromString("PRIORITYISNOTANSRCCLASS"), PyLong_FromUnsignedLongLong(13ULL));
    setItem(enum_dict, PyUnicode_FromString("MAXFRAMESIZETOOLARGE"), PyLong_FromUnsignedLongLong(14ULL));
    setItem(enum_dict, PyUnicode_FromString("MAXFANINPORTSLIMITREACHED"), PyLong_FromUnsignedLongLong(15ULL));
    setItem(enum_dict, PyUnicode_FromString("FIRSTVALUECHANGEDFORSTREAMID"), PyLong_FromUnsignedLongLong(16ULL));
    setItem(enum_dict, PyUnicode_FromString("VLANBLOCKEDONEGRESS"), PyLong_FromUnsignedLongLong(17ULL));
    setItem(enum_dict, PyUnicode_FromString("VLANTAGGINGDISABLEDONEGRESS"), PyLong_FromUnsignedLongLong(18ULL));
    setItem(enum_dict, PyUnicode_FromString("SRCLASSPRIORITYMISMATCH"), PyLong_FromUnsignedLongLong(19ULL));
    setItem(enum_dict, PyUnicode_FromString("FEATURENOTPROPAGATED"), PyLong_FromUnsignedLongLong(20ULL));
    setItem(enum_dict, PyUnicode_FromString("MAXLATENCYEXCEEDED"), PyLong_FromUnsignedLongLong(21ULL));
    setItem(enum_dict, PyUnicode_FromString("BRIDGEDOESNOTPROVIDENETWORKID"), PyLong_FromUnsignedLongLong(22ULL));
    setItem(enum_dict, PyUnicode_FromString("STREAMTRANSFORMNOTSUPPORTED"), PyLong_FromUnsignedLongLong(23ULL));
    setItem(enum_dict, PyUnicode_FromString("STREAMIDTYPENOTSUPPORTED"), PyLong_FromUnsignedLongLong(24ULL));
    setItem(enum_dict, PyUnicode_FromString("FEATURENOTSUPPORTED"), PyLong_FromUnsignedLongLong(25ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("TsnFailureCode"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "TsnFailureCode", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: TsnStreamState
static void create_TsnStreamState_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("TsnStreamState"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("DISABLED"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("CONFIGURING"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("READY"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("OPERATIONAL"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("ERROR"), PyLong_FromUnsignedLongLong(4ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("TsnStreamState"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "TsnStreamState", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: TsnTalkerStatus
static void create_TsnTalkerStatus_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("TsnTalkerStatus"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("NONE"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("READY"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("FAILED"), PyLong_FromUnsignedLongLong(2ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("TsnTalkerStatus"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "TsnTalkerStatus", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: TsnListenerStatus
static void create_TsnListenerStatus_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("TsnListenerStatus"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("NONE"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("READY"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("PARTIALFAILED"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("FAILED"), PyLong_FromUnsignedLongLong(3ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("TsnListenerStatus"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "TsnListenerStatus", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: ChassisIdSubtype
static void create_ChassisIdSubtype_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("ChassisIdSubtype"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("CHASSISCOMPONENT"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("INTERFACEALIAS"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("PORTCOMPONENT"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("MACADDRESS"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("NETWORKADDRESS"), PyLong_FromUnsignedLongLong(5ULL));
    setItem(enum_dict, PyUnicode_FromString("INTERFACENAME"), PyLong_FromUnsignedLongLong(6ULL));
    setItem(enum_dict, PyUnicode_FromString("LOCAL"), PyLong_FromUnsignedLongLong(7ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("ChassisIdSubtype"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "ChassisIdSubtype", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: PortIdSubtype
static void create_PortIdSubtype_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("PortIdSubtype"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("INTERFACEALIAS"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("PORTCOMPONENT"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("MACADDRESS"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("NETWORKADDRESS"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("INTERFACENAME"), PyLong_FromUnsignedLongLong(5ULL));
    setItem(enum_dict, PyUnicode_FromString("AGENTCIRCUITID"), PyLong_FromUnsignedLongLong(6ULL));
    setItem(enum_dict, PyUnicode_FromString("LOCAL"), PyLong_FromUnsignedLongLong(7ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("PortIdSubtype"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "PortIdSubtype", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: ManAddrIfSubtype
static void create_ManAddrIfSubtype_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("ManAddrIfSubtype"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("NONE"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("UNKNOWN"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("PORTREF"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("SYSTEMPORTNUMBER"), PyLong_FromUnsignedLongLong(3ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("ManAddrIfSubtype"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "ManAddrIfSubtype", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: LldpSystemCapabilitiesMap
static void create_LldpSystemCapabilitiesMap_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("LldpSystemCapabilitiesMap"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("OTHER"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("REPEATER"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("BRIDGE"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("WLANACCESSPOINT"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("ROUTER"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("TELEPHONE"), PyLong_FromUnsignedLongLong(5ULL));
    setItem(enum_dict, PyUnicode_FromString("DOCSISCABLEDEVICE"), PyLong_FromUnsignedLongLong(6ULL));
    setItem(enum_dict, PyUnicode_FromString("STATIONONLY"), PyLong_FromUnsignedLongLong(7ULL));
    setItem(enum_dict, PyUnicode_FromString("CVLANCOMPONENT"), PyLong_FromUnsignedLongLong(8ULL));
    setItem(enum_dict, PyUnicode_FromString("SVLANCOMPONENT"), PyLong_FromUnsignedLongLong(9ULL));
    setItem(enum_dict, PyUnicode_FromString("TWOPORTMACRELAY"), PyLong_FromUnsignedLongLong(10ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("LldpSystemCapabilitiesMap"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "LldpSystemCapabilitiesMap", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: IdType
static void create_IdType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("IdType"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("NUMERIC"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("STRING"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("GUID"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("OPAQUE"), PyLong_FromUnsignedLongLong(3ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("IdType"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "IdType", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: NodeClass
static void create_NodeClass_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("NodeClass"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("UNSPECIFIED"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("OBJECT"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("VARIABLE"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("METHOD"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("OBJECTTYPE"), PyLong_FromUnsignedLongLong(8ULL));
    setItem(enum_dict, PyUnicode_FromString("VARIABLETYPE"), PyLong_FromUnsignedLongLong(16ULL));
    setItem(enum_dict, PyUnicode_FromString("REFERENCETYPE"), PyLong_FromUnsignedLongLong(32ULL));
    setItem(enum_dict, PyUnicode_FromString("DATATYPE"), PyLong_FromUnsignedLongLong(64ULL));
    setItem(enum_dict, PyUnicode_FromString("VIEW"), PyLong_FromUnsignedLongLong(128ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("NodeClass"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "NodeClass", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: PermissionType
static void create_PermissionType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("PermissionType"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("BROWSE"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("READROLEPERMISSIONS"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("WRITEATTRIBUTE"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("WRITEROLEPERMISSIONS"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("WRITEHISTORIZING"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("READ"), PyLong_FromUnsignedLongLong(5ULL));
    setItem(enum_dict, PyUnicode_FromString("WRITE"), PyLong_FromUnsignedLongLong(6ULL));
    setItem(enum_dict, PyUnicode_FromString("READHISTORY"), PyLong_FromUnsignedLongLong(7ULL));
    setItem(enum_dict, PyUnicode_FromString("INSERTHISTORY"), PyLong_FromUnsignedLongLong(8ULL));
    setItem(enum_dict, PyUnicode_FromString("MODIFYHISTORY"), PyLong_FromUnsignedLongLong(9ULL));
    setItem(enum_dict, PyUnicode_FromString("DELETEHISTORY"), PyLong_FromUnsignedLongLong(10ULL));
    setItem(enum_dict, PyUnicode_FromString("RECEIVEEVENTS"), PyLong_FromUnsignedLongLong(11ULL));
    setItem(enum_dict, PyUnicode_FromString("CALL"), PyLong_FromUnsignedLongLong(12ULL));
    setItem(enum_dict, PyUnicode_FromString("ADDREFERENCE"), PyLong_FromUnsignedLongLong(13ULL));
    setItem(enum_dict, PyUnicode_FromString("REMOVEREFERENCE"), PyLong_FromUnsignedLongLong(14ULL));
    setItem(enum_dict, PyUnicode_FromString("DELETENODE"), PyLong_FromUnsignedLongLong(15ULL));
    setItem(enum_dict, PyUnicode_FromString("ADDNODE"), PyLong_FromUnsignedLongLong(16ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("PermissionType"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "PermissionType", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: AccessLevelType
static void create_AccessLevelType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("AccessLevelType"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("CURRENTREAD"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("CURRENTWRITE"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("HISTORYREAD"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("HISTORYWRITE"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("SEMANTICCHANGE"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("STATUSWRITE"), PyLong_FromUnsignedLongLong(5ULL));
    setItem(enum_dict, PyUnicode_FromString("TIMESTAMPWRITE"), PyLong_FromUnsignedLongLong(6ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("AccessLevelType"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "AccessLevelType", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: AccessLevelExType
static void create_AccessLevelExType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("AccessLevelExType"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("CURRENTREAD"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("CURRENTWRITE"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("HISTORYREAD"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("HISTORYWRITE"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("SEMANTICCHANGE"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("STATUSWRITE"), PyLong_FromUnsignedLongLong(5ULL));
    setItem(enum_dict, PyUnicode_FromString("TIMESTAMPWRITE"), PyLong_FromUnsignedLongLong(6ULL));
    setItem(enum_dict, PyUnicode_FromString("NONATOMICREAD"), PyLong_FromUnsignedLongLong(8ULL));
    setItem(enum_dict, PyUnicode_FromString("NONATOMICWRITE"), PyLong_FromUnsignedLongLong(9ULL));
    setItem(enum_dict, PyUnicode_FromString("WRITEFULLARRAYONLY"), PyLong_FromUnsignedLongLong(10ULL));
    setItem(enum_dict, PyUnicode_FromString("NOSUBDATATYPES"), PyLong_FromUnsignedLongLong(11ULL));
    setItem(enum_dict, PyUnicode_FromString("NONVOLATILE"), PyLong_FromUnsignedLongLong(12ULL));
    setItem(enum_dict, PyUnicode_FromString("CONSTANT"), PyLong_FromUnsignedLongLong(13ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("AccessLevelExType"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "AccessLevelExType", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: EventNotifierType
static void create_EventNotifierType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("EventNotifierType"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("SUBSCRIBETOEVENTS"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("HISTORYREAD"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("HISTORYWRITE"), PyLong_FromUnsignedLongLong(3ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("EventNotifierType"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "EventNotifierType", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: AccessRestrictionType
static void create_AccessRestrictionType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("AccessRestrictionType"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("SIGNINGREQUIRED"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("ENCRYPTIONREQUIRED"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("SESSIONREQUIRED"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("APPLYRESTRICTIONSTOBROWSE"), PyLong_FromUnsignedLongLong(3ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("AccessRestrictionType"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "AccessRestrictionType", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: StructureType
static void create_StructureType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("StructureType"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("STRUCTURE"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("STRUCTUREWITHOPTIONALFIELDS"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("UNION"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("STRUCTUREWITHSUBTYPEDVALUES"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("UNIONWITHSUBTYPEDVALUES"), PyLong_FromUnsignedLongLong(4ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("StructureType"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "StructureType", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: ApplicationType
static void create_ApplicationType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("ApplicationType"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("SERVER"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("CLIENT"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("CLIENTANDSERVER"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("DISCOVERYSERVER"), PyLong_FromUnsignedLongLong(3ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("ApplicationType"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "ApplicationType", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: MessageSecurityMode
static void create_MessageSecurityMode_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("MessageSecurityMode"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("INVALID"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("NONE"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("SIGN"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("SIGNANDENCRYPT"), PyLong_FromUnsignedLongLong(3ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("MessageSecurityMode"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "MessageSecurityMode", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: UserTokenType
static void create_UserTokenType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("UserTokenType"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("ANONYMOUS"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("USERNAME"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("CERTIFICATE"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("ISSUEDTOKEN"), PyLong_FromUnsignedLongLong(3ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("UserTokenType"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "UserTokenType", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: SecurityTokenRequestType
static void create_SecurityTokenRequestType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("SecurityTokenRequestType"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("ISSUE"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("RENEW"), PyLong_FromUnsignedLongLong(1ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("SecurityTokenRequestType"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "SecurityTokenRequestType", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: NodeAttributesMask
static void create_NodeAttributesMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("NodeAttributesMask"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("NONE"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("ACCESSLEVEL"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("ARRAYDIMENSIONS"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("BROWSENAME"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("CONTAINSNOLOOPS"), PyLong_FromUnsignedLongLong(8ULL));
    setItem(enum_dict, PyUnicode_FromString("DATATYPE"), PyLong_FromUnsignedLongLong(16ULL));
    setItem(enum_dict, PyUnicode_FromString("DESCRIPTION"), PyLong_FromUnsignedLongLong(32ULL));
    setItem(enum_dict, PyUnicode_FromString("DISPLAYNAME"), PyLong_FromUnsignedLongLong(64ULL));
    setItem(enum_dict, PyUnicode_FromString("EVENTNOTIFIER"), PyLong_FromUnsignedLongLong(128ULL));
    setItem(enum_dict, PyUnicode_FromString("EXECUTABLE"), PyLong_FromUnsignedLongLong(256ULL));
    setItem(enum_dict, PyUnicode_FromString("HISTORIZING"), PyLong_FromUnsignedLongLong(512ULL));
    setItem(enum_dict, PyUnicode_FromString("INVERSENAME"), PyLong_FromUnsignedLongLong(1024ULL));
    setItem(enum_dict, PyUnicode_FromString("ISABSTRACT"), PyLong_FromUnsignedLongLong(2048ULL));
    setItem(enum_dict, PyUnicode_FromString("MINIMUMSAMPLINGINTERVAL"), PyLong_FromUnsignedLongLong(4096ULL));
    setItem(enum_dict, PyUnicode_FromString("NODECLASS"), PyLong_FromUnsignedLongLong(8192ULL));
    setItem(enum_dict, PyUnicode_FromString("NODEID"), PyLong_FromUnsignedLongLong(16384ULL));
    setItem(enum_dict, PyUnicode_FromString("SYMMETRIC"), PyLong_FromUnsignedLongLong(32768ULL));
    setItem(enum_dict, PyUnicode_FromString("USERACCESSLEVEL"), PyLong_FromUnsignedLongLong(65536ULL));
    setItem(enum_dict, PyUnicode_FromString("USEREXECUTABLE"), PyLong_FromUnsignedLongLong(131072ULL));
    setItem(enum_dict, PyUnicode_FromString("USERWRITEMASK"), PyLong_FromUnsignedLongLong(262144ULL));
    setItem(enum_dict, PyUnicode_FromString("VALUERANK"), PyLong_FromUnsignedLongLong(524288ULL));
    setItem(enum_dict, PyUnicode_FromString("WRITEMASK"), PyLong_FromUnsignedLongLong(1048576ULL));
    setItem(enum_dict, PyUnicode_FromString("VALUE"), PyLong_FromUnsignedLongLong(2097152ULL));
    setItem(enum_dict, PyUnicode_FromString("DATATYPEDEFINITION"), PyLong_FromUnsignedLongLong(4194304ULL));
    setItem(enum_dict, PyUnicode_FromString("ROLEPERMISSIONS"), PyLong_FromUnsignedLongLong(8388608ULL));
    setItem(enum_dict, PyUnicode_FromString("ACCESSRESTRICTIONS"), PyLong_FromUnsignedLongLong(16777216ULL));
    setItem(enum_dict, PyUnicode_FromString("ALL"), PyLong_FromUnsignedLongLong(33554431ULL));
    setItem(enum_dict, PyUnicode_FromString("BASENODE"), PyLong_FromUnsignedLongLong(26501220ULL));
    setItem(enum_dict, PyUnicode_FromString("OBJECT"), PyLong_FromUnsignedLongLong(26501348ULL));
    setItem(enum_dict, PyUnicode_FromString("OBJECTTYPE"), PyLong_FromUnsignedLongLong(26503268ULL));
    setItem(enum_dict, PyUnicode_FromString("VARIABLE"), PyLong_FromUnsignedLongLong(26571383ULL));
    setItem(enum_dict, PyUnicode_FromString("VARIABLETYPE"), PyLong_FromUnsignedLongLong(28600438ULL));
    setItem(enum_dict, PyUnicode_FromString("METHOD"), PyLong_FromUnsignedLongLong(26632548ULL));
    setItem(enum_dict, PyUnicode_FromString("REFERENCETYPE"), PyLong_FromUnsignedLongLong(26537060ULL));
    setItem(enum_dict, PyUnicode_FromString("VIEW"), PyLong_FromUnsignedLongLong(26501356ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("NodeAttributesMask"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "NodeAttributesMask", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: AttributeWriteMask
static void create_AttributeWriteMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("AttributeWriteMask"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("ACCESSLEVEL"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("ARRAYDIMENSIONS"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("BROWSENAME"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("CONTAINSNOLOOPS"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("DATATYPE"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("DESCRIPTION"), PyLong_FromUnsignedLongLong(5ULL));
    setItem(enum_dict, PyUnicode_FromString("DISPLAYNAME"), PyLong_FromUnsignedLongLong(6ULL));
    setItem(enum_dict, PyUnicode_FromString("EVENTNOTIFIER"), PyLong_FromUnsignedLongLong(7ULL));
    setItem(enum_dict, PyUnicode_FromString("EXECUTABLE"), PyLong_FromUnsignedLongLong(8ULL));
    setItem(enum_dict, PyUnicode_FromString("HISTORIZING"), PyLong_FromUnsignedLongLong(9ULL));
    setItem(enum_dict, PyUnicode_FromString("INVERSENAME"), PyLong_FromUnsignedLongLong(10ULL));
    setItem(enum_dict, PyUnicode_FromString("ISABSTRACT"), PyLong_FromUnsignedLongLong(11ULL));
    setItem(enum_dict, PyUnicode_FromString("MINIMUMSAMPLINGINTERVAL"), PyLong_FromUnsignedLongLong(12ULL));
    setItem(enum_dict, PyUnicode_FromString("NODECLASS"), PyLong_FromUnsignedLongLong(13ULL));
    setItem(enum_dict, PyUnicode_FromString("NODEID"), PyLong_FromUnsignedLongLong(14ULL));
    setItem(enum_dict, PyUnicode_FromString("SYMMETRIC"), PyLong_FromUnsignedLongLong(15ULL));
    setItem(enum_dict, PyUnicode_FromString("USERACCESSLEVEL"), PyLong_FromUnsignedLongLong(16ULL));
    setItem(enum_dict, PyUnicode_FromString("USEREXECUTABLE"), PyLong_FromUnsignedLongLong(17ULL));
    setItem(enum_dict, PyUnicode_FromString("USERWRITEMASK"), PyLong_FromUnsignedLongLong(18ULL));
    setItem(enum_dict, PyUnicode_FromString("VALUERANK"), PyLong_FromUnsignedLongLong(19ULL));
    setItem(enum_dict, PyUnicode_FromString("WRITEMASK"), PyLong_FromUnsignedLongLong(20ULL));
    setItem(enum_dict, PyUnicode_FromString("VALUEFORVARIABLETYPE"), PyLong_FromUnsignedLongLong(21ULL));
    setItem(enum_dict, PyUnicode_FromString("DATATYPEDEFINITION"), PyLong_FromUnsignedLongLong(22ULL));
    setItem(enum_dict, PyUnicode_FromString("ROLEPERMISSIONS"), PyLong_FromUnsignedLongLong(23ULL));
    setItem(enum_dict, PyUnicode_FromString("ACCESSRESTRICTIONS"), PyLong_FromUnsignedLongLong(24ULL));
    setItem(enum_dict, PyUnicode_FromString("ACCESSLEVELEX"), PyLong_FromUnsignedLongLong(25ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("AttributeWriteMask"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "AttributeWriteMask", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: FilterOperator
static void create_FilterOperator_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("FilterOperator"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("EQUALS"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("ISNULL"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("GREATERTHAN"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("LESSTHAN"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("GREATERTHANOREQUAL"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("LESSTHANOREQUAL"), PyLong_FromUnsignedLongLong(5ULL));
    setItem(enum_dict, PyUnicode_FromString("LIKE"), PyLong_FromUnsignedLongLong(6ULL));
    setItem(enum_dict, PyUnicode_FromString("NOT"), PyLong_FromUnsignedLongLong(7ULL));
    setItem(enum_dict, PyUnicode_FromString("BETWEEN"), PyLong_FromUnsignedLongLong(8ULL));
    setItem(enum_dict, PyUnicode_FromString("INLIST"), PyLong_FromUnsignedLongLong(9ULL));
    setItem(enum_dict, PyUnicode_FromString("AND"), PyLong_FromUnsignedLongLong(10ULL));
    setItem(enum_dict, PyUnicode_FromString("OR"), PyLong_FromUnsignedLongLong(11ULL));
    setItem(enum_dict, PyUnicode_FromString("CAST"), PyLong_FromUnsignedLongLong(12ULL));
    setItem(enum_dict, PyUnicode_FromString("INVIEW"), PyLong_FromUnsignedLongLong(13ULL));
    setItem(enum_dict, PyUnicode_FromString("OFTYPE"), PyLong_FromUnsignedLongLong(14ULL));
    setItem(enum_dict, PyUnicode_FromString("RELATEDTO"), PyLong_FromUnsignedLongLong(15ULL));
    setItem(enum_dict, PyUnicode_FromString("BITWISEAND"), PyLong_FromUnsignedLongLong(16ULL));
    setItem(enum_dict, PyUnicode_FromString("BITWISEOR"), PyLong_FromUnsignedLongLong(17ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("FilterOperator"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "FilterOperator", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: HistoryUpdateType
static void create_HistoryUpdateType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("HistoryUpdateType"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("INSERT"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("REPLACE"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("UPDATE"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("DELETE"), PyLong_FromUnsignedLongLong(4ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("HistoryUpdateType"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "HistoryUpdateType", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: PerformUpdateType
static void create_PerformUpdateType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("PerformUpdateType"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("INSERT"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("REPLACE"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("UPDATE"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("REMOVE"), PyLong_FromUnsignedLongLong(4ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("PerformUpdateType"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "PerformUpdateType", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: RedundancySupport
static void create_RedundancySupport_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("RedundancySupport"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("NONE"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("COLD"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("WARM"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("HOT"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("TRANSPARENT"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("HOTANDMIRRORED"), PyLong_FromUnsignedLongLong(5ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("RedundancySupport"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "RedundancySupport", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: ServerState
static void create_ServerState_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("ServerState"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("RUNNING"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("FAILED"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("NOCONFIGURATION"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("SUSPENDED"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("SHUTDOWN"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("TEST"), PyLong_FromUnsignedLongLong(5ULL));
    setItem(enum_dict, PyUnicode_FromString("COMMUNICATIONFAULT"), PyLong_FromUnsignedLongLong(6ULL));
    setItem(enum_dict, PyUnicode_FromString("UNKNOWN"), PyLong_FromUnsignedLongLong(7ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("ServerState"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "ServerState", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: AxisScaleEnumeration
static void create_AxisScaleEnumeration_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("AxisScaleEnumeration"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("LINEAR"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("LOG"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("LN"), PyLong_FromUnsignedLongLong(2ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("AxisScaleEnumeration"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "AxisScaleEnumeration", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: ExceptionDeviationFormat
static void create_ExceptionDeviationFormat_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("ExceptionDeviationFormat"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("ABSOLUTEVALUE"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("PERCENTOFVALUE"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("PERCENTOFRANGE"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("PERCENTOFEURANGE"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("UNKNOWN"), PyLong_FromUnsignedLongLong(4ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("ExceptionDeviationFormat"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "ExceptionDeviationFormat", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: BrowseDirection
static void create_BrowseDirection_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("BrowseDirection"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("FORWARD"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("INVERSE"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("BOTH"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("INVALID"), PyLong_FromUnsignedLongLong(3ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("BrowseDirection"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "BrowseDirection", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: BrowseResultMask
static void create_BrowseResultMask_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("BrowseResultMask"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("NONE"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("REFERENCETYPEID"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("ISFORWARD"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("NODECLASS"), PyLong_FromUnsignedLongLong(4ULL));
    setItem(enum_dict, PyUnicode_FromString("BROWSENAME"), PyLong_FromUnsignedLongLong(8ULL));
    setItem(enum_dict, PyUnicode_FromString("DISPLAYNAME"), PyLong_FromUnsignedLongLong(16ULL));
    setItem(enum_dict, PyUnicode_FromString("TYPEDEFINITION"), PyLong_FromUnsignedLongLong(32ULL));
    setItem(enum_dict, PyUnicode_FromString("ALL"), PyLong_FromUnsignedLongLong(63ULL));
    setItem(enum_dict, PyUnicode_FromString("REFERENCETYPEINFO"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("TARGETINFO"), PyLong_FromUnsignedLongLong(60ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("BrowseResultMask"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "BrowseResultMask", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: TimestampsToReturn
static void create_TimestampsToReturn_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("TimestampsToReturn"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("SOURCE"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("SERVER"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("BOTH"), PyLong_FromUnsignedLongLong(2ULL));
    setItem(enum_dict, PyUnicode_FromString("NEITHER"), PyLong_FromUnsignedLongLong(3ULL));
    setItem(enum_dict, PyUnicode_FromString("INVALID"), PyLong_FromUnsignedLongLong(4ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("TimestampsToReturn"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "TimestampsToReturn", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: MonitoringMode
static void create_MonitoringMode_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("MonitoringMode"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("DISABLED"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("SAMPLING"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("REPORTING"), PyLong_FromUnsignedLongLong(2ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("MonitoringMode"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "MonitoringMode", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: DataChangeTrigger
static void create_DataChangeTrigger_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("DataChangeTrigger"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("STATUS"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("STATUSVALUE"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("STATUSVALUETIMESTAMP"), PyLong_FromUnsignedLongLong(2ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("DataChangeTrigger"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "DataChangeTrigger", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: DeadbandType
static void create_DeadbandType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("DeadbandType"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("NONE"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("ABSOLUTE"), PyLong_FromUnsignedLongLong(1ULL));
    setItem(enum_dict, PyUnicode_FromString("PERCENT"), PyLong_FromUnsignedLongLong(2ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("DeadbandType"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "DeadbandType", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}
// Enum: StatusCode
static void create_StatusCode_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("StatusCode"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("Good"), PyLong_FromUnsignedLongLong(0ULL));
    setItem(enum_dict, PyUnicode_FromString("Uncertain"), PyLong_FromUnsignedLongLong(1073741824ULL));
    setItem(enum_dict, PyUnicode_FromString("Bad"), PyLong_FromUnsignedLongLong(2147483648ULL));
    setItem(enum_dict, PyUnicode_FromString("BadUnexpectedError"), PyLong_FromUnsignedLongLong(2147549184ULL));
    setItem(enum_dict, PyUnicode_FromString("BadInternalError"), PyLong_FromUnsignedLongLong(2147614720ULL));
    setItem(enum_dict, PyUnicode_FromString("BadOutOfMemory"), PyLong_FromUnsignedLongLong(2147680256ULL));
    setItem(enum_dict, PyUnicode_FromString("BadResourceUnavailable"), PyLong_FromUnsignedLongLong(2147745792ULL));
    setItem(enum_dict, PyUnicode_FromString("BadCommunicationError"), PyLong_FromUnsignedLongLong(2147811328ULL));
    setItem(enum_dict, PyUnicode_FromString("BadEncodingError"), PyLong_FromUnsignedLongLong(2147876864ULL));
    setItem(enum_dict, PyUnicode_FromString("BadDecodingError"), PyLong_FromUnsignedLongLong(2147942400ULL));
    setItem(enum_dict, PyUnicode_FromString("BadEncodingLimitsExceeded"), PyLong_FromUnsignedLongLong(2148007936ULL));
    setItem(enum_dict, PyUnicode_FromString("BadRequestTooLarge"), PyLong_FromUnsignedLongLong(2159542272ULL));
    setItem(enum_dict, PyUnicode_FromString("BadResponseTooLarge"), PyLong_FromUnsignedLongLong(2159607808ULL));
    setItem(enum_dict, PyUnicode_FromString("BadUnknownResponse"), PyLong_FromUnsignedLongLong(2148073472ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTimeout"), PyLong_FromUnsignedLongLong(2148139008ULL));
    setItem(enum_dict, PyUnicode_FromString("BadServiceUnsupported"), PyLong_FromUnsignedLongLong(2148204544ULL));
    setItem(enum_dict, PyUnicode_FromString("BadShutdown"), PyLong_FromUnsignedLongLong(2148270080ULL));
    setItem(enum_dict, PyUnicode_FromString("BadServerNotConnected"), PyLong_FromUnsignedLongLong(2148335616ULL));
    setItem(enum_dict, PyUnicode_FromString("BadServerHalted"), PyLong_FromUnsignedLongLong(2148401152ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNothingToDo"), PyLong_FromUnsignedLongLong(2148466688ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTooManyOperations"), PyLong_FromUnsignedLongLong(2148532224ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTooManyMonitoredItems"), PyLong_FromUnsignedLongLong(2161836032ULL));
    setItem(enum_dict, PyUnicode_FromString("BadDataTypeIdUnknown"), PyLong_FromUnsignedLongLong(2148597760ULL));
    setItem(enum_dict, PyUnicode_FromString("BadCertificateInvalid"), PyLong_FromUnsignedLongLong(2148663296ULL));
    setItem(enum_dict, PyUnicode_FromString("BadSecurityChecksFailed"), PyLong_FromUnsignedLongLong(2148728832ULL));
    setItem(enum_dict, PyUnicode_FromString("BadCertificatePolicyCheckFailed"), PyLong_FromUnsignedLongLong(2165571584ULL));
    setItem(enum_dict, PyUnicode_FromString("BadCertificateTimeInvalid"), PyLong_FromUnsignedLongLong(2148794368ULL));
    setItem(enum_dict, PyUnicode_FromString("BadCertificateIssuerTimeInvalid"), PyLong_FromUnsignedLongLong(2148859904ULL));
    setItem(enum_dict, PyUnicode_FromString("BadCertificateHostNameInvalid"), PyLong_FromUnsignedLongLong(2148925440ULL));
    setItem(enum_dict, PyUnicode_FromString("BadCertificateUriInvalid"), PyLong_FromUnsignedLongLong(2148990976ULL));
    setItem(enum_dict, PyUnicode_FromString("BadCertificateUseNotAllowed"), PyLong_FromUnsignedLongLong(2149056512ULL));
    setItem(enum_dict, PyUnicode_FromString("BadCertificateIssuerUseNotAllowed"), PyLong_FromUnsignedLongLong(2149122048ULL));
    setItem(enum_dict, PyUnicode_FromString("BadCertificateUntrusted"), PyLong_FromUnsignedLongLong(2149187584ULL));
    setItem(enum_dict, PyUnicode_FromString("BadCertificateRevocationUnknown"), PyLong_FromUnsignedLongLong(2149253120ULL));
    setItem(enum_dict, PyUnicode_FromString("BadCertificateIssuerRevocationUnknown"), PyLong_FromUnsignedLongLong(2149318656ULL));
    setItem(enum_dict, PyUnicode_FromString("BadCertificateRevoked"), PyLong_FromUnsignedLongLong(2149384192ULL));
    setItem(enum_dict, PyUnicode_FromString("BadCertificateIssuerRevoked"), PyLong_FromUnsignedLongLong(2149449728ULL));
    setItem(enum_dict, PyUnicode_FromString("BadCertificateChainIncomplete"), PyLong_FromUnsignedLongLong(2165112832ULL));
    setItem(enum_dict, PyUnicode_FromString("BadUserAccessDenied"), PyLong_FromUnsignedLongLong(2149515264ULL));
    setItem(enum_dict, PyUnicode_FromString("BadIdentityTokenInvalid"), PyLong_FromUnsignedLongLong(2149580800ULL));
    setItem(enum_dict, PyUnicode_FromString("BadIdentityTokenRejected"), PyLong_FromUnsignedLongLong(2149646336ULL));
    setItem(enum_dict, PyUnicode_FromString("BadSecureChannelIdInvalid"), PyLong_FromUnsignedLongLong(2149711872ULL));
    setItem(enum_dict, PyUnicode_FromString("BadInvalidTimestamp"), PyLong_FromUnsignedLongLong(2149777408ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNonceInvalid"), PyLong_FromUnsignedLongLong(2149842944ULL));
    setItem(enum_dict, PyUnicode_FromString("BadSessionIdInvalid"), PyLong_FromUnsignedLongLong(2149908480ULL));
    setItem(enum_dict, PyUnicode_FromString("BadSessionClosed"), PyLong_FromUnsignedLongLong(2149974016ULL));
    setItem(enum_dict, PyUnicode_FromString("BadSessionNotActivated"), PyLong_FromUnsignedLongLong(2150039552ULL));
    setItem(enum_dict, PyUnicode_FromString("BadSubscriptionIdInvalid"), PyLong_FromUnsignedLongLong(2150105088ULL));
    setItem(enum_dict, PyUnicode_FromString("BadRequestHeaderInvalid"), PyLong_FromUnsignedLongLong(2150236160ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTimestampsToReturnInvalid"), PyLong_FromUnsignedLongLong(2150301696ULL));
    setItem(enum_dict, PyUnicode_FromString("BadRequestCancelledByClient"), PyLong_FromUnsignedLongLong(2150367232ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTooManyArguments"), PyLong_FromUnsignedLongLong(2162491392ULL));
    setItem(enum_dict, PyUnicode_FromString("BadLicenseExpired"), PyLong_FromUnsignedLongLong(2165178368ULL));
    setItem(enum_dict, PyUnicode_FromString("BadLicenseLimitsExceeded"), PyLong_FromUnsignedLongLong(2165243904ULL));
    setItem(enum_dict, PyUnicode_FromString("BadLicenseNotAvailable"), PyLong_FromUnsignedLongLong(2165309440ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodSubscriptionTransferred"), PyLong_FromUnsignedLongLong(2949120ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodCompletesAsynchronously"), PyLong_FromUnsignedLongLong(3014656ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodOverload"), PyLong_FromUnsignedLongLong(3080192ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodClamped"), PyLong_FromUnsignedLongLong(3145728ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNoCommunication"), PyLong_FromUnsignedLongLong(2150694912ULL));
    setItem(enum_dict, PyUnicode_FromString("BadWaitingForInitialData"), PyLong_FromUnsignedLongLong(2150760448ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNodeIdInvalid"), PyLong_FromUnsignedLongLong(2150825984ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNodeIdUnknown"), PyLong_FromUnsignedLongLong(2150891520ULL));
    setItem(enum_dict, PyUnicode_FromString("BadAttributeIdInvalid"), PyLong_FromUnsignedLongLong(2150957056ULL));
    setItem(enum_dict, PyUnicode_FromString("BadIndexRangeInvalid"), PyLong_FromUnsignedLongLong(2151022592ULL));
    setItem(enum_dict, PyUnicode_FromString("BadIndexRangeNoData"), PyLong_FromUnsignedLongLong(2151088128ULL));
    setItem(enum_dict, PyUnicode_FromString("BadDataEncodingInvalid"), PyLong_FromUnsignedLongLong(2151153664ULL));
    setItem(enum_dict, PyUnicode_FromString("BadDataEncodingUnsupported"), PyLong_FromUnsignedLongLong(2151219200ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNotReadable"), PyLong_FromUnsignedLongLong(2151284736ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNotWritable"), PyLong_FromUnsignedLongLong(2151350272ULL));
    setItem(enum_dict, PyUnicode_FromString("BadOutOfRange"), PyLong_FromUnsignedLongLong(2151415808ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNotSupported"), PyLong_FromUnsignedLongLong(2151481344ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNotFound"), PyLong_FromUnsignedLongLong(2151546880ULL));
    setItem(enum_dict, PyUnicode_FromString("BadObjectDeleted"), PyLong_FromUnsignedLongLong(2151612416ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNotImplemented"), PyLong_FromUnsignedLongLong(2151677952ULL));
    setItem(enum_dict, PyUnicode_FromString("BadMonitoringModeInvalid"), PyLong_FromUnsignedLongLong(2151743488ULL));
    setItem(enum_dict, PyUnicode_FromString("BadMonitoredItemIdInvalid"), PyLong_FromUnsignedLongLong(2151809024ULL));
    setItem(enum_dict, PyUnicode_FromString("BadMonitoredItemFilterInvalid"), PyLong_FromUnsignedLongLong(2151874560ULL));
    setItem(enum_dict, PyUnicode_FromString("BadMonitoredItemFilterUnsupported"), PyLong_FromUnsignedLongLong(2151940096ULL));
    setItem(enum_dict, PyUnicode_FromString("BadFilterNotAllowed"), PyLong_FromUnsignedLongLong(2152005632ULL));
    setItem(enum_dict, PyUnicode_FromString("BadStructureMissing"), PyLong_FromUnsignedLongLong(2152071168ULL));
    setItem(enum_dict, PyUnicode_FromString("BadEventFilterInvalid"), PyLong_FromUnsignedLongLong(2152136704ULL));
    setItem(enum_dict, PyUnicode_FromString("BadContentFilterInvalid"), PyLong_FromUnsignedLongLong(2152202240ULL));
    setItem(enum_dict, PyUnicode_FromString("BadFilterOperatorInvalid"), PyLong_FromUnsignedLongLong(2160132096ULL));
    setItem(enum_dict, PyUnicode_FromString("BadFilterOperatorUnsupported"), PyLong_FromUnsignedLongLong(2160197632ULL));
    setItem(enum_dict, PyUnicode_FromString("BadFilterOperandCountMismatch"), PyLong_FromUnsignedLongLong(2160263168ULL));
    setItem(enum_dict, PyUnicode_FromString("BadFilterOperandInvalid"), PyLong_FromUnsignedLongLong(2152267776ULL));
    setItem(enum_dict, PyUnicode_FromString("BadFilterElementInvalid"), PyLong_FromUnsignedLongLong(2160328704ULL));
    setItem(enum_dict, PyUnicode_FromString("BadFilterLiteralInvalid"), PyLong_FromUnsignedLongLong(2160394240ULL));
    setItem(enum_dict, PyUnicode_FromString("BadContinuationPointInvalid"), PyLong_FromUnsignedLongLong(2152333312ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNoContinuationPoints"), PyLong_FromUnsignedLongLong(2152398848ULL));
    setItem(enum_dict, PyUnicode_FromString("BadReferenceTypeIdInvalid"), PyLong_FromUnsignedLongLong(2152464384ULL));
    setItem(enum_dict, PyUnicode_FromString("BadBrowseDirectionInvalid"), PyLong_FromUnsignedLongLong(2152529920ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNodeNotInView"), PyLong_FromUnsignedLongLong(2152595456ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNumericOverflow"), PyLong_FromUnsignedLongLong(2165440512ULL));
    setItem(enum_dict, PyUnicode_FromString("BadServerUriInvalid"), PyLong_FromUnsignedLongLong(2152660992ULL));
    setItem(enum_dict, PyUnicode_FromString("BadServerNameMissing"), PyLong_FromUnsignedLongLong(2152726528ULL));
    setItem(enum_dict, PyUnicode_FromString("BadDiscoveryUrlMissing"), PyLong_FromUnsignedLongLong(2152792064ULL));
    setItem(enum_dict, PyUnicode_FromString("BadSemaphoreFileMissing"), PyLong_FromUnsignedLongLong(2152857600ULL));
    setItem(enum_dict, PyUnicode_FromString("BadRequestTypeInvalid"), PyLong_FromUnsignedLongLong(2152923136ULL));
    setItem(enum_dict, PyUnicode_FromString("BadSecurityModeRejected"), PyLong_FromUnsignedLongLong(2152988672ULL));
    setItem(enum_dict, PyUnicode_FromString("BadSecurityPolicyRejected"), PyLong_FromUnsignedLongLong(2153054208ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTooManySessions"), PyLong_FromUnsignedLongLong(2153119744ULL));
    setItem(enum_dict, PyUnicode_FromString("BadUserSignatureInvalid"), PyLong_FromUnsignedLongLong(2153185280ULL));
    setItem(enum_dict, PyUnicode_FromString("BadApplicationSignatureInvalid"), PyLong_FromUnsignedLongLong(2153250816ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNoValidCertificates"), PyLong_FromUnsignedLongLong(2153316352ULL));
    setItem(enum_dict, PyUnicode_FromString("BadIdentityChangeNotSupported"), PyLong_FromUnsignedLongLong(2160459776ULL));
    setItem(enum_dict, PyUnicode_FromString("BadRequestCancelledByRequest"), PyLong_FromUnsignedLongLong(2153381888ULL));
    setItem(enum_dict, PyUnicode_FromString("BadParentNodeIdInvalid"), PyLong_FromUnsignedLongLong(2153447424ULL));
    setItem(enum_dict, PyUnicode_FromString("BadReferenceNotAllowed"), PyLong_FromUnsignedLongLong(2153512960ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNodeIdRejected"), PyLong_FromUnsignedLongLong(2153578496ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNodeIdExists"), PyLong_FromUnsignedLongLong(2153644032ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNodeClassInvalid"), PyLong_FromUnsignedLongLong(2153709568ULL));
    setItem(enum_dict, PyUnicode_FromString("BadBrowseNameInvalid"), PyLong_FromUnsignedLongLong(2153775104ULL));
    setItem(enum_dict, PyUnicode_FromString("BadBrowseNameDuplicated"), PyLong_FromUnsignedLongLong(2153840640ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNodeAttributesInvalid"), PyLong_FromUnsignedLongLong(2153906176ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTypeDefinitionInvalid"), PyLong_FromUnsignedLongLong(2153971712ULL));
    setItem(enum_dict, PyUnicode_FromString("BadSourceNodeIdInvalid"), PyLong_FromUnsignedLongLong(2154037248ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTargetNodeIdInvalid"), PyLong_FromUnsignedLongLong(2154102784ULL));
    setItem(enum_dict, PyUnicode_FromString("BadDuplicateReferenceNotAllowed"), PyLong_FromUnsignedLongLong(2154168320ULL));
    setItem(enum_dict, PyUnicode_FromString("BadInvalidSelfReference"), PyLong_FromUnsignedLongLong(2154233856ULL));
    setItem(enum_dict, PyUnicode_FromString("BadReferenceLocalOnly"), PyLong_FromUnsignedLongLong(2154299392ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNoDeleteRights"), PyLong_FromUnsignedLongLong(2154364928ULL));
    setItem(enum_dict, PyUnicode_FromString("UncertainReferenceNotDeleted"), PyLong_FromUnsignedLongLong(1086062592ULL));
    setItem(enum_dict, PyUnicode_FromString("BadServerIndexInvalid"), PyLong_FromUnsignedLongLong(2154430464ULL));
    setItem(enum_dict, PyUnicode_FromString("BadViewIdUnknown"), PyLong_FromUnsignedLongLong(2154496000ULL));
    setItem(enum_dict, PyUnicode_FromString("BadViewTimestampInvalid"), PyLong_FromUnsignedLongLong(2160656384ULL));
    setItem(enum_dict, PyUnicode_FromString("BadViewParameterMismatch"), PyLong_FromUnsignedLongLong(2160721920ULL));
    setItem(enum_dict, PyUnicode_FromString("BadViewVersionInvalid"), PyLong_FromUnsignedLongLong(2160787456ULL));
    setItem(enum_dict, PyUnicode_FromString("UncertainNotAllNodesAvailable"), PyLong_FromUnsignedLongLong(1086324736ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodResultsMayBeIncomplete"), PyLong_FromUnsignedLongLong(12189696ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNotTypeDefinition"), PyLong_FromUnsignedLongLong(2160590848ULL));
    setItem(enum_dict, PyUnicode_FromString("UncertainReferenceOutOfServer"), PyLong_FromUnsignedLongLong(1080819712ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTooManyMatches"), PyLong_FromUnsignedLongLong(2154627072ULL));
    setItem(enum_dict, PyUnicode_FromString("BadQueryTooComplex"), PyLong_FromUnsignedLongLong(2154692608ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNoMatch"), PyLong_FromUnsignedLongLong(2154758144ULL));
    setItem(enum_dict, PyUnicode_FromString("BadMaxAgeInvalid"), PyLong_FromUnsignedLongLong(2154823680ULL));
    setItem(enum_dict, PyUnicode_FromString("BadSecurityModeInsufficient"), PyLong_FromUnsignedLongLong(2162556928ULL));
    setItem(enum_dict, PyUnicode_FromString("BadHistoryOperationInvalid"), PyLong_FromUnsignedLongLong(2154889216ULL));
    setItem(enum_dict, PyUnicode_FromString("BadHistoryOperationUnsupported"), PyLong_FromUnsignedLongLong(2154954752ULL));
    setItem(enum_dict, PyUnicode_FromString("BadInvalidTimestampArgument"), PyLong_FromUnsignedLongLong(2159869952ULL));
    setItem(enum_dict, PyUnicode_FromString("BadWriteNotSupported"), PyLong_FromUnsignedLongLong(2155020288ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTypeMismatch"), PyLong_FromUnsignedLongLong(2155085824ULL));
    setItem(enum_dict, PyUnicode_FromString("BadMethodInvalid"), PyLong_FromUnsignedLongLong(2155151360ULL));
    setItem(enum_dict, PyUnicode_FromString("BadArgumentsMissing"), PyLong_FromUnsignedLongLong(2155216896ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNotExecutable"), PyLong_FromUnsignedLongLong(2165374976ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTooManySubscriptions"), PyLong_FromUnsignedLongLong(2155282432ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTooManyPublishRequests"), PyLong_FromUnsignedLongLong(2155347968ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNoSubscription"), PyLong_FromUnsignedLongLong(2155413504ULL));
    setItem(enum_dict, PyUnicode_FromString("BadSequenceNumberUnknown"), PyLong_FromUnsignedLongLong(2155479040ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodRetransmissionQueueNotSupported"), PyLong_FromUnsignedLongLong(14614528ULL));
    setItem(enum_dict, PyUnicode_FromString("BadMessageNotAvailable"), PyLong_FromUnsignedLongLong(2155544576ULL));
    setItem(enum_dict, PyUnicode_FromString("BadInsufficientClientProfile"), PyLong_FromUnsignedLongLong(2155610112ULL));
    setItem(enum_dict, PyUnicode_FromString("BadStateNotActive"), PyLong_FromUnsignedLongLong(2160001024ULL));
    setItem(enum_dict, PyUnicode_FromString("BadAlreadyExists"), PyLong_FromUnsignedLongLong(2165637120ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTcpServerTooBusy"), PyLong_FromUnsignedLongLong(2155675648ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTcpMessageTypeInvalid"), PyLong_FromUnsignedLongLong(2155741184ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTcpSecureChannelUnknown"), PyLong_FromUnsignedLongLong(2155806720ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTcpMessageTooLarge"), PyLong_FromUnsignedLongLong(2155872256ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTcpNotEnoughResources"), PyLong_FromUnsignedLongLong(2155937792ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTcpInternalError"), PyLong_FromUnsignedLongLong(2156003328ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTcpEndpointUrlInvalid"), PyLong_FromUnsignedLongLong(2156068864ULL));
    setItem(enum_dict, PyUnicode_FromString("BadRequestInterrupted"), PyLong_FromUnsignedLongLong(2156134400ULL));
    setItem(enum_dict, PyUnicode_FromString("BadRequestTimeout"), PyLong_FromUnsignedLongLong(2156199936ULL));
    setItem(enum_dict, PyUnicode_FromString("BadSecureChannelClosed"), PyLong_FromUnsignedLongLong(2156265472ULL));
    setItem(enum_dict, PyUnicode_FromString("BadSecureChannelTokenUnknown"), PyLong_FromUnsignedLongLong(2156331008ULL));
    setItem(enum_dict, PyUnicode_FromString("BadSequenceNumberInvalid"), PyLong_FromUnsignedLongLong(2156396544ULL));
    setItem(enum_dict, PyUnicode_FromString("BadProtocolVersionUnsupported"), PyLong_FromUnsignedLongLong(2159935488ULL));
    setItem(enum_dict, PyUnicode_FromString("BadConfigurationError"), PyLong_FromUnsignedLongLong(2156462080ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNotConnected"), PyLong_FromUnsignedLongLong(2156527616ULL));
    setItem(enum_dict, PyUnicode_FromString("BadDeviceFailure"), PyLong_FromUnsignedLongLong(2156593152ULL));
    setItem(enum_dict, PyUnicode_FromString("BadSensorFailure"), PyLong_FromUnsignedLongLong(2156658688ULL));
    setItem(enum_dict, PyUnicode_FromString("BadOutOfService"), PyLong_FromUnsignedLongLong(2156724224ULL));
    setItem(enum_dict, PyUnicode_FromString("BadDeadbandFilterInvalid"), PyLong_FromUnsignedLongLong(2156789760ULL));
    setItem(enum_dict, PyUnicode_FromString("UncertainNoCommunicationLastUsableValue"), PyLong_FromUnsignedLongLong(1083113472ULL));
    setItem(enum_dict, PyUnicode_FromString("UncertainLastUsableValue"), PyLong_FromUnsignedLongLong(1083179008ULL));
    setItem(enum_dict, PyUnicode_FromString("UncertainSubstituteValue"), PyLong_FromUnsignedLongLong(1083244544ULL));
    setItem(enum_dict, PyUnicode_FromString("UncertainInitialValue"), PyLong_FromUnsignedLongLong(1083310080ULL));
    setItem(enum_dict, PyUnicode_FromString("UncertainSensorNotAccurate"), PyLong_FromUnsignedLongLong(1083375616ULL));
    setItem(enum_dict, PyUnicode_FromString("UncertainEngineeringUnitsExceeded"), PyLong_FromUnsignedLongLong(1083441152ULL));
    setItem(enum_dict, PyUnicode_FromString("UncertainSubNormal"), PyLong_FromUnsignedLongLong(1083506688ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodLocalOverride"), PyLong_FromUnsignedLongLong(9830400ULL));
    setItem(enum_dict, PyUnicode_FromString("BadRefreshInProgress"), PyLong_FromUnsignedLongLong(2157379584ULL));
    setItem(enum_dict, PyUnicode_FromString("BadConditionAlreadyDisabled"), PyLong_FromUnsignedLongLong(2157445120ULL));
    setItem(enum_dict, PyUnicode_FromString("BadConditionAlreadyEnabled"), PyLong_FromUnsignedLongLong(2160852992ULL));
    setItem(enum_dict, PyUnicode_FromString("BadConditionDisabled"), PyLong_FromUnsignedLongLong(2157510656ULL));
    setItem(enum_dict, PyUnicode_FromString("BadEventIdUnknown"), PyLong_FromUnsignedLongLong(2157576192ULL));
    setItem(enum_dict, PyUnicode_FromString("BadEventNotAcknowledgeable"), PyLong_FromUnsignedLongLong(2159738880ULL));
    setItem(enum_dict, PyUnicode_FromString("BadDialogNotActive"), PyLong_FromUnsignedLongLong(2160918528ULL));
    setItem(enum_dict, PyUnicode_FromString("BadDialogResponseInvalid"), PyLong_FromUnsignedLongLong(2160984064ULL));
    setItem(enum_dict, PyUnicode_FromString("BadConditionBranchAlreadyAcked"), PyLong_FromUnsignedLongLong(2161049600ULL));
    setItem(enum_dict, PyUnicode_FromString("BadConditionBranchAlreadyConfirmed"), PyLong_FromUnsignedLongLong(2161115136ULL));
    setItem(enum_dict, PyUnicode_FromString("BadConditionAlreadyShelved"), PyLong_FromUnsignedLongLong(2161180672ULL));
    setItem(enum_dict, PyUnicode_FromString("BadConditionNotShelved"), PyLong_FromUnsignedLongLong(2161246208ULL));
    setItem(enum_dict, PyUnicode_FromString("BadShelvingTimeOutOfRange"), PyLong_FromUnsignedLongLong(2161311744ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNoData"), PyLong_FromUnsignedLongLong(2157641728ULL));
    setItem(enum_dict, PyUnicode_FromString("BadBoundNotFound"), PyLong_FromUnsignedLongLong(2161573888ULL));
    setItem(enum_dict, PyUnicode_FromString("BadBoundNotSupported"), PyLong_FromUnsignedLongLong(2161639424ULL));
    setItem(enum_dict, PyUnicode_FromString("BadDataLost"), PyLong_FromUnsignedLongLong(2157772800ULL));
    setItem(enum_dict, PyUnicode_FromString("BadDataUnavailable"), PyLong_FromUnsignedLongLong(2157838336ULL));
    setItem(enum_dict, PyUnicode_FromString("BadEntryExists"), PyLong_FromUnsignedLongLong(2157903872ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNoEntryExists"), PyLong_FromUnsignedLongLong(2157969408ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTimestampNotSupported"), PyLong_FromUnsignedLongLong(2158034944ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodEntryInserted"), PyLong_FromUnsignedLongLong(10616832ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodEntryReplaced"), PyLong_FromUnsignedLongLong(10682368ULL));
    setItem(enum_dict, PyUnicode_FromString("UncertainDataSubNormal"), PyLong_FromUnsignedLongLong(1084489728ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodNoData"), PyLong_FromUnsignedLongLong(10813440ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodMoreData"), PyLong_FromUnsignedLongLong(10878976ULL));
    setItem(enum_dict, PyUnicode_FromString("BadAggregateListMismatch"), PyLong_FromUnsignedLongLong(2161377280ULL));
    setItem(enum_dict, PyUnicode_FromString("BadAggregateNotSupported"), PyLong_FromUnsignedLongLong(2161442816ULL));
    setItem(enum_dict, PyUnicode_FromString("BadAggregateInvalidInputs"), PyLong_FromUnsignedLongLong(2161508352ULL));
    setItem(enum_dict, PyUnicode_FromString("BadAggregateConfigurationRejected"), PyLong_FromUnsignedLongLong(2161770496ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodDataIgnored"), PyLong_FromUnsignedLongLong(14221312ULL));
    setItem(enum_dict, PyUnicode_FromString("BadRequestNotAllowed"), PyLong_FromUnsignedLongLong(2162425856ULL));
    setItem(enum_dict, PyUnicode_FromString("BadRequestNotComplete"), PyLong_FromUnsignedLongLong(2165506048ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTransactionPending"), PyLong_FromUnsignedLongLong(2162688000ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTicketRequired"), PyLong_FromUnsignedLongLong(2166292480ULL));
    setItem(enum_dict, PyUnicode_FromString("BadTicketInvalid"), PyLong_FromUnsignedLongLong(2166358016ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodEdited"), PyLong_FromUnsignedLongLong(14417920ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodPostActionFailed"), PyLong_FromUnsignedLongLong(14483456ULL));
    setItem(enum_dict, PyUnicode_FromString("UncertainDominantValueChanged"), PyLong_FromUnsignedLongLong(1088290816ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodDependentValueChanged"), PyLong_FromUnsignedLongLong(14680064ULL));
    setItem(enum_dict, PyUnicode_FromString("BadDominantValueChanged"), PyLong_FromUnsignedLongLong(2162229248ULL));
    setItem(enum_dict, PyUnicode_FromString("UncertainDependentValueChanged"), PyLong_FromUnsignedLongLong(1088552960ULL));
    setItem(enum_dict, PyUnicode_FromString("BadDependentValueChanged"), PyLong_FromUnsignedLongLong(2162360320ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodEdited_DependentValueChanged"), PyLong_FromUnsignedLongLong(18219008ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodEdited_DominantValueChanged"), PyLong_FromUnsignedLongLong(18284544ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodEdited_DominantValueChanged_DependentValueChanged"), PyLong_FromUnsignedLongLong(18350080ULL));
    setItem(enum_dict, PyUnicode_FromString("BadEdited_OutOfRange"), PyLong_FromUnsignedLongLong(2165899264ULL));
    setItem(enum_dict, PyUnicode_FromString("BadInitialValue_OutOfRange"), PyLong_FromUnsignedLongLong(2165964800ULL));
    setItem(enum_dict, PyUnicode_FromString("BadOutOfRange_DominantValueChanged"), PyLong_FromUnsignedLongLong(2166030336ULL));
    setItem(enum_dict, PyUnicode_FromString("BadEdited_OutOfRange_DominantValueChanged"), PyLong_FromUnsignedLongLong(2166095872ULL));
    setItem(enum_dict, PyUnicode_FromString("BadOutOfRange_DominantValueChanged_DependentValueChanged"), PyLong_FromUnsignedLongLong(2166161408ULL));
    setItem(enum_dict, PyUnicode_FromString("BadEdited_OutOfRange_DominantValueChanged_DependentValueChanged"), PyLong_FromUnsignedLongLong(2166226944ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodCommunicationEvent"), PyLong_FromUnsignedLongLong(10944512ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodShutdownEvent"), PyLong_FromUnsignedLongLong(11010048ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodCallAgain"), PyLong_FromUnsignedLongLong(11075584ULL));
    setItem(enum_dict, PyUnicode_FromString("GoodNonCriticalTimeout"), PyLong_FromUnsignedLongLong(11141120ULL));
    setItem(enum_dict, PyUnicode_FromString("BadInvalidArgument"), PyLong_FromUnsignedLongLong(2158690304ULL));
    setItem(enum_dict, PyUnicode_FromString("BadConnectionRejected"), PyLong_FromUnsignedLongLong(2158755840ULL));
    setItem(enum_dict, PyUnicode_FromString("BadDisconnect"), PyLong_FromUnsignedLongLong(2158821376ULL));
    setItem(enum_dict, PyUnicode_FromString("BadConnectionClosed"), PyLong_FromUnsignedLongLong(2158886912ULL));
    setItem(enum_dict, PyUnicode_FromString("BadInvalidState"), PyLong_FromUnsignedLongLong(2158952448ULL));
    setItem(enum_dict, PyUnicode_FromString("BadEndOfStream"), PyLong_FromUnsignedLongLong(2159017984ULL));
    setItem(enum_dict, PyUnicode_FromString("BadNoDataAvailable"), PyLong_FromUnsignedLongLong(2159083520ULL));
    setItem(enum_dict, PyUnicode_FromString("BadWaitingForResponse"), PyLong_FromUnsignedLongLong(2159149056ULL));
    setItem(enum_dict, PyUnicode_FromString("BadOperationAbandoned"), PyLong_FromUnsignedLongLong(2159214592ULL));
    setItem(enum_dict, PyUnicode_FromString("BadExpectedStreamToBlock"), PyLong_FromUnsignedLongLong(2159280128ULL));
    setItem(enum_dict, PyUnicode_FromString("BadWouldBlock"), PyLong_FromUnsignedLongLong(2159345664ULL));
    setItem(enum_dict, PyUnicode_FromString("BadSyntaxError"), PyLong_FromUnsignedLongLong(2159411200ULL));
    setItem(enum_dict, PyUnicode_FromString("BadMaxConnectionsReached"), PyLong_FromUnsignedLongLong(2159476736ULL));
    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("StatusCode"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    // Install __str__ as a real method descriptor on the enum class so
    // str(StatusCode.X) returns the member name (e.g. "Good") instead of the
    // numeric value inherited from int.
    {
        PyObject *descr = PyDescr_NewMethod((PyTypeObject *)enum_class, &pyStatusCode_str_def);
        if(descr) {
            if(PyObject_SetAttrString(enum_class, "__str__", descr) == 0)
                PyType_Modified((PyTypeObject *)enum_class);
            Py_DECREF(descr);
        }
    }
    PyModule_AddObject(module, "StatusCode", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}