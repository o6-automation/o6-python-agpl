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
done:
    Py_DECREF(enum_module);
    Py_XDECREF(EnumMeta);
    Py_XDECREF(IntFlag);
    Py_XDECREF(bases);
    Py_XDECREF(UAEnum_Type);
    Py_XDECREF(prepare);
}
// Enum: NamingRuleType
static void create_NamingRuleType_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("NamingRuleType"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;
    setItem(enum_dict, PyUnicode_FromString("MANDATORY"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("OPTIONAL"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("CONSTRAINT"), PyLong_FromLong(3));
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
    setItem(enum_dict, PyUnicode_FromString("PRIMARYWITHBACKUP"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("PRIMARYONLY"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("BACKUPREADY"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("BACKUPNOTREADY"), PyLong_FromLong(3));
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
    setItem(enum_dict, PyUnicode_FromString("READ"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("WRITE"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("ERASEEXISTING"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("APPEND"), PyLong_FromLong(8));
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
    setItem(enum_dict, PyUnicode_FromString("USERNAME"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("THUMBPRINT"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("ROLE"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("GROUPID"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("ANONYMOUS"), PyLong_FromLong(5));
    setItem(enum_dict, PyUnicode_FromString("AUTHENTICATEDUSER"), PyLong_FromLong(6));
    setItem(enum_dict, PyUnicode_FromString("APPLICATION"), PyLong_FromLong(7));
    setItem(enum_dict, PyUnicode_FromString("X509SUBJECT"), PyLong_FromLong(8));
    setItem(enum_dict, PyUnicode_FromString("TRUSTEDAPPLICATION"), PyLong_FromLong(9));
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
    setItem(enum_dict, PyUnicode_FromString("NOCONVERSION"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("LIMITED"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("UNLIMITED"), PyLong_FromLong(2));
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
    setItem(enum_dict, PyUnicode_FromString("ACTIVE"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("UNACKNOWLEDGED"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("UNCONFIRMED"), PyLong_FromLong(2));
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
    setItem(enum_dict, PyUnicode_FromString("SUPPRESSCERTIFICATEEXPIRED"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("SUPPRESSHOSTNAMEINVALID"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("SUPPRESSREVOCATIONSTATUSUNKNOWN"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("SUPPRESSISSUERCERTIFICATEEXPIRED"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("SUPPRESSISSUERREVOCATIONSTATUSUNKNOWN"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("CHECKREVOCATIONSTATUSONLINE"), PyLong_FromLong(5));
    setItem(enum_dict, PyUnicode_FromString("CHECKREVOCATIONSTATUSOFFLINE"), PyLong_FromLong(6));
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
    setItem(enum_dict, PyUnicode_FromString("NONE"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("TRUSTEDCERTIFICATES"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("TRUSTEDCRLS"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("ISSUERCERTIFICATES"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("ISSUERCRLS"), PyLong_FromLong(8));
    setItem(enum_dict, PyUnicode_FromString("ALL"), PyLong_FromLong(15));
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
    setItem(enum_dict, PyUnicode_FromString("DISABLED"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("PAUSED"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("OPERATIONAL"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("ERROR"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("PREOPERATIONAL"), PyLong_FromLong(4));
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
    setItem(enum_dict, PyUnicode_FromString("PROMOTEDFIELD"), PyLong_FromLong(0));
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
    setItem(enum_dict, PyUnicode_FromString("IDLE"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("EXECUTING"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("DONE"), PyLong_FromLong(2));
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
    setItem(enum_dict, PyUnicode_FromString("STATUSCODE"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("SOURCETIMESTAMP"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("SERVERTIMESTAMP"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("SOURCEPICOSECONDS"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("SERVERPICOSECONDS"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("RAWDATA"), PyLong_FromLong(5));
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
    setItem(enum_dict, PyUnicode_FromString("DISABLED"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("LASTUSABLEVALUE"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("OVERRIDEVALUE"), PyLong_FromLong(2));
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
    setItem(enum_dict, PyUnicode_FromString("UNDEFINED"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("ASCENDINGWRITERID"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("ASCENDINGWRITERIDSINGLE"), PyLong_FromLong(2));
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
    setItem(enum_dict, PyUnicode_FromString("PUBLISHERID"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("GROUPHEADER"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("WRITERGROUPID"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("GROUPVERSION"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("NETWORKMESSAGENUMBER"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("SEQUENCENUMBER"), PyLong_FromLong(5));
    setItem(enum_dict, PyUnicode_FromString("PAYLOADHEADER"), PyLong_FromLong(6));
    setItem(enum_dict, PyUnicode_FromString("TIMESTAMP"), PyLong_FromLong(7));
    setItem(enum_dict, PyUnicode_FromString("PICOSECONDS"), PyLong_FromLong(8));
    setItem(enum_dict, PyUnicode_FromString("DATASETCLASSID"), PyLong_FromLong(9));
    setItem(enum_dict, PyUnicode_FromString("PROMOTEDFIELDS"), PyLong_FromLong(10));
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
    setItem(enum_dict, PyUnicode_FromString("TIMESTAMP"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("PICOSECONDS"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("STATUS"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("MAJORVERSION"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("MINORVERSION"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("SEQUENCENUMBER"), PyLong_FromLong(5));
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
    setItem(enum_dict, PyUnicode_FromString("NETWORKMESSAGEHEADER"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("DATASETMESSAGEHEADER"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("SINGLEDATASETMESSAGE"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("PUBLISHERID"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("DATASETCLASSID"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("REPLYTO"), PyLong_FromLong(5));
    setItem(enum_dict, PyUnicode_FromString("WRITERGROUPNAME"), PyLong_FromLong(6));
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
    setItem(enum_dict, PyUnicode_FromString("DATASETWRITERID"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("METADATAVERSION"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("SEQUENCENUMBER"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("TIMESTAMP"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("STATUS"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("MESSAGETYPE"), PyLong_FromLong(5));
    setItem(enum_dict, PyUnicode_FromString("DATASETWRITERNAME"), PyLong_FromLong(6));
    setItem(enum_dict, PyUnicode_FromString("FIELDENCODING1"), PyLong_FromLong(7));
    setItem(enum_dict, PyUnicode_FromString("PUBLISHERID"), PyLong_FromLong(8));
    setItem(enum_dict, PyUnicode_FromString("WRITERGROUPNAME"), PyLong_FromLong(9));
    setItem(enum_dict, PyUnicode_FromString("MINORVERSION"), PyLong_FromLong(10));
    setItem(enum_dict, PyUnicode_FromString("FIELDENCODING2"), PyLong_FromLong(11));
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
    setItem(enum_dict, PyUnicode_FromString("NOTSPECIFIED"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("BESTEFFORT"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("ATLEASTONCE"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("ATMOSTONCE"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("EXACTLYONCE"), PyLong_FromLong(4));
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
    setItem(enum_dict, PyUnicode_FromString("ELEMENTADD"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("ELEMENTMATCH"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("ELEMENTMODIFY"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("ELEMENTREMOVE"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("REFERENCEWRITER"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("REFERENCEREADER"), PyLong_FromLong(5));
    setItem(enum_dict, PyUnicode_FromString("REFERENCEWRITERGROUP"), PyLong_FromLong(6));
    setItem(enum_dict, PyUnicode_FromString("REFERENCEREADERGROUP"), PyLong_FromLong(7));
    setItem(enum_dict, PyUnicode_FromString("REFERENCECONNECTION"), PyLong_FromLong(8));
    setItem(enum_dict, PyUnicode_FromString("REFERENCEPUBDATASET"), PyLong_FromLong(9));
    setItem(enum_dict, PyUnicode_FromString("REFERENCESUBDATASET"), PyLong_FromLong(10));
    setItem(enum_dict, PyUnicode_FromString("REFERENCESECURITYGROUP"), PyLong_FromLong(11));
    setItem(enum_dict, PyUnicode_FromString("REFERENCEPUSHTARGET"), PyLong_FromLong(12));
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
    setItem(enum_dict, PyUnicode_FromString("BASIC"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("ADVANCED"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("INFO"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("LOG"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("DEBUG"), PyLong_FromLong(4));
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
    setItem(enum_dict, PyUnicode_FromString("INFORMATION"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("ERROR"), PyLong_FromLong(1));
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
    setItem(enum_dict, PyUnicode_FromString("SUPPORTINITIALPASSWORDCHANGE"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("SUPPORTDISABLEUSER"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("SUPPORTDISABLEDELETEFORUSER"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("SUPPORTNOCHANGEFORUSER"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("SUPPORTDESCRIPTIONFORUSER"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("REQUIRESUPPERCASECHARACTERS"), PyLong_FromLong(5));
    setItem(enum_dict, PyUnicode_FromString("REQUIRESLOWERCASECHARACTERS"), PyLong_FromLong(6));
    setItem(enum_dict, PyUnicode_FromString("REQUIRESDIGITCHARACTERS"), PyLong_FromLong(7));
    setItem(enum_dict, PyUnicode_FromString("REQUIRESSPECIALCHARACTERS"), PyLong_FromLong(8));
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
    setItem(enum_dict, PyUnicode_FromString("NODELETE"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("DISABLED"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("NOCHANGEBYUSER"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("MUSTCHANGEPASSWORD"), PyLong_FromLong(3));
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
    setItem(enum_dict, PyUnicode_FromString("FULL"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("HALF"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("UNKNOWN"), PyLong_FromLong(2));
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
    setItem(enum_dict, PyUnicode_FromString("UP"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("DOWN"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("TESTING"), PyLong_FromLong(2));
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
    setItem(enum_dict, PyUnicode_FromString("UP"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("DOWN"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("TESTING"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("UNKNOWN"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("DORMANT"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("NOTPRESENT"), PyLong_FromLong(5));
    setItem(enum_dict, PyUnicode_FromString("LOWERLAYERDOWN"), PyLong_FromLong(6));
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
    setItem(enum_dict, PyUnicode_FromString("INPROGRESS"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("COMPLETE"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("FAILED"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("UNKNOWN"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("NONEGOTIATION"), PyLong_FromLong(4));
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
    setItem(enum_dict, PyUnicode_FromString("NOFAILURE"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("INSUFFICIENTBANDWIDTH"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("INSUFFICIENTRESOURCES"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("INSUFFICIENTTRAFFICCLASSBANDWIDTH"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("STREAMIDINUSE"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("STREAMDESTINATIONADDRESSINUSE"), PyLong_FromLong(5));
    setItem(enum_dict, PyUnicode_FromString("STREAMPREEMPTEDBYHIGHERRANK"), PyLong_FromLong(6));
    setItem(enum_dict, PyUnicode_FromString("LATENCYHASCHANGED"), PyLong_FromLong(7));
    setItem(enum_dict, PyUnicode_FromString("EGRESSPORTNOTAVBCAPABLE"), PyLong_FromLong(8));
    setItem(enum_dict, PyUnicode_FromString("USEDIFFERENTDESTINATIONADDRESS"), PyLong_FromLong(9));
    setItem(enum_dict, PyUnicode_FromString("OUTOFMSRPRESOURCES"), PyLong_FromLong(10));
    setItem(enum_dict, PyUnicode_FromString("OUTOFMMRPRESOURCES"), PyLong_FromLong(11));
    setItem(enum_dict, PyUnicode_FromString("CANNOTSTOREDESTINATIONADDRESS"), PyLong_FromLong(12));
    setItem(enum_dict, PyUnicode_FromString("PRIORITYISNOTANSRCCLASS"), PyLong_FromLong(13));
    setItem(enum_dict, PyUnicode_FromString("MAXFRAMESIZETOOLARGE"), PyLong_FromLong(14));
    setItem(enum_dict, PyUnicode_FromString("MAXFANINPORTSLIMITREACHED"), PyLong_FromLong(15));
    setItem(enum_dict, PyUnicode_FromString("FIRSTVALUECHANGEDFORSTREAMID"), PyLong_FromLong(16));
    setItem(enum_dict, PyUnicode_FromString("VLANBLOCKEDONEGRESS"), PyLong_FromLong(17));
    setItem(enum_dict, PyUnicode_FromString("VLANTAGGINGDISABLEDONEGRESS"), PyLong_FromLong(18));
    setItem(enum_dict, PyUnicode_FromString("SRCLASSPRIORITYMISMATCH"), PyLong_FromLong(19));
    setItem(enum_dict, PyUnicode_FromString("FEATURENOTPROPAGATED"), PyLong_FromLong(20));
    setItem(enum_dict, PyUnicode_FromString("MAXLATENCYEXCEEDED"), PyLong_FromLong(21));
    setItem(enum_dict, PyUnicode_FromString("BRIDGEDOESNOTPROVIDENETWORKID"), PyLong_FromLong(22));
    setItem(enum_dict, PyUnicode_FromString("STREAMTRANSFORMNOTSUPPORTED"), PyLong_FromLong(23));
    setItem(enum_dict, PyUnicode_FromString("STREAMIDTYPENOTSUPPORTED"), PyLong_FromLong(24));
    setItem(enum_dict, PyUnicode_FromString("FEATURENOTSUPPORTED"), PyLong_FromLong(25));
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
    setItem(enum_dict, PyUnicode_FromString("DISABLED"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("CONFIGURING"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("READY"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("OPERATIONAL"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("ERROR"), PyLong_FromLong(4));
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
    setItem(enum_dict, PyUnicode_FromString("NONE"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("READY"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("FAILED"), PyLong_FromLong(2));
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
    setItem(enum_dict, PyUnicode_FromString("NONE"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("READY"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("PARTIALFAILED"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("FAILED"), PyLong_FromLong(3));
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
    setItem(enum_dict, PyUnicode_FromString("CHASSISCOMPONENT"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("INTERFACEALIAS"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("PORTCOMPONENT"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("MACADDRESS"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("NETWORKADDRESS"), PyLong_FromLong(5));
    setItem(enum_dict, PyUnicode_FromString("INTERFACENAME"), PyLong_FromLong(6));
    setItem(enum_dict, PyUnicode_FromString("LOCAL"), PyLong_FromLong(7));
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
    setItem(enum_dict, PyUnicode_FromString("INTERFACEALIAS"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("PORTCOMPONENT"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("MACADDRESS"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("NETWORKADDRESS"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("INTERFACENAME"), PyLong_FromLong(5));
    setItem(enum_dict, PyUnicode_FromString("AGENTCIRCUITID"), PyLong_FromLong(6));
    setItem(enum_dict, PyUnicode_FromString("LOCAL"), PyLong_FromLong(7));
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
    setItem(enum_dict, PyUnicode_FromString("NONE"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("UNKNOWN"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("PORTREF"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("SYSTEMPORTNUMBER"), PyLong_FromLong(3));
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
    setItem(enum_dict, PyUnicode_FromString("OTHER"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("REPEATER"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("BRIDGE"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("WLANACCESSPOINT"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("ROUTER"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("TELEPHONE"), PyLong_FromLong(5));
    setItem(enum_dict, PyUnicode_FromString("DOCSISCABLEDEVICE"), PyLong_FromLong(6));
    setItem(enum_dict, PyUnicode_FromString("STATIONONLY"), PyLong_FromLong(7));
    setItem(enum_dict, PyUnicode_FromString("CVLANCOMPONENT"), PyLong_FromLong(8));
    setItem(enum_dict, PyUnicode_FromString("SVLANCOMPONENT"), PyLong_FromLong(9));
    setItem(enum_dict, PyUnicode_FromString("TWOPORTMACRELAY"), PyLong_FromLong(10));
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
    setItem(enum_dict, PyUnicode_FromString("NUMERIC"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("STRING"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("GUID"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("OPAQUE"), PyLong_FromLong(3));
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
    setItem(enum_dict, PyUnicode_FromString("UNSPECIFIED"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("OBJECT"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("VARIABLE"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("METHOD"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("OBJECTTYPE"), PyLong_FromLong(8));
    setItem(enum_dict, PyUnicode_FromString("VARIABLETYPE"), PyLong_FromLong(16));
    setItem(enum_dict, PyUnicode_FromString("REFERENCETYPE"), PyLong_FromLong(32));
    setItem(enum_dict, PyUnicode_FromString("DATATYPE"), PyLong_FromLong(64));
    setItem(enum_dict, PyUnicode_FromString("VIEW"), PyLong_FromLong(128));
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
    setItem(enum_dict, PyUnicode_FromString("BROWSE"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("READROLEPERMISSIONS"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("WRITEATTRIBUTE"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("WRITEROLEPERMISSIONS"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("WRITEHISTORIZING"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("READ"), PyLong_FromLong(5));
    setItem(enum_dict, PyUnicode_FromString("WRITE"), PyLong_FromLong(6));
    setItem(enum_dict, PyUnicode_FromString("READHISTORY"), PyLong_FromLong(7));
    setItem(enum_dict, PyUnicode_FromString("INSERTHISTORY"), PyLong_FromLong(8));
    setItem(enum_dict, PyUnicode_FromString("MODIFYHISTORY"), PyLong_FromLong(9));
    setItem(enum_dict, PyUnicode_FromString("DELETEHISTORY"), PyLong_FromLong(10));
    setItem(enum_dict, PyUnicode_FromString("RECEIVEEVENTS"), PyLong_FromLong(11));
    setItem(enum_dict, PyUnicode_FromString("CALL"), PyLong_FromLong(12));
    setItem(enum_dict, PyUnicode_FromString("ADDREFERENCE"), PyLong_FromLong(13));
    setItem(enum_dict, PyUnicode_FromString("REMOVEREFERENCE"), PyLong_FromLong(14));
    setItem(enum_dict, PyUnicode_FromString("DELETENODE"), PyLong_FromLong(15));
    setItem(enum_dict, PyUnicode_FromString("ADDNODE"), PyLong_FromLong(16));
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
    setItem(enum_dict, PyUnicode_FromString("CURRENTREAD"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("CURRENTWRITE"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("HISTORYREAD"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("HISTORYWRITE"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("SEMANTICCHANGE"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("STATUSWRITE"), PyLong_FromLong(5));
    setItem(enum_dict, PyUnicode_FromString("TIMESTAMPWRITE"), PyLong_FromLong(6));
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
    setItem(enum_dict, PyUnicode_FromString("CURRENTREAD"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("CURRENTWRITE"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("HISTORYREAD"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("HISTORYWRITE"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("SEMANTICCHANGE"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("STATUSWRITE"), PyLong_FromLong(5));
    setItem(enum_dict, PyUnicode_FromString("TIMESTAMPWRITE"), PyLong_FromLong(6));
    setItem(enum_dict, PyUnicode_FromString("NONATOMICREAD"), PyLong_FromLong(8));
    setItem(enum_dict, PyUnicode_FromString("NONATOMICWRITE"), PyLong_FromLong(9));
    setItem(enum_dict, PyUnicode_FromString("WRITEFULLARRAYONLY"), PyLong_FromLong(10));
    setItem(enum_dict, PyUnicode_FromString("NOSUBDATATYPES"), PyLong_FromLong(11));
    setItem(enum_dict, PyUnicode_FromString("NONVOLATILE"), PyLong_FromLong(12));
    setItem(enum_dict, PyUnicode_FromString("CONSTANT"), PyLong_FromLong(13));
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
    setItem(enum_dict, PyUnicode_FromString("SUBSCRIBETOEVENTS"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("HISTORYREAD"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("HISTORYWRITE"), PyLong_FromLong(3));
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
    setItem(enum_dict, PyUnicode_FromString("SIGNINGREQUIRED"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("ENCRYPTIONREQUIRED"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("SESSIONREQUIRED"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("APPLYRESTRICTIONSTOBROWSE"), PyLong_FromLong(3));
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
    setItem(enum_dict, PyUnicode_FromString("STRUCTURE"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("STRUCTUREWITHOPTIONALFIELDS"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("UNION"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("STRUCTUREWITHSUBTYPEDVALUES"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("UNIONWITHSUBTYPEDVALUES"), PyLong_FromLong(4));
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
    setItem(enum_dict, PyUnicode_FromString("SERVER"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("CLIENT"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("CLIENTANDSERVER"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("DISCOVERYSERVER"), PyLong_FromLong(3));
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
    setItem(enum_dict, PyUnicode_FromString("INVALID"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("NONE"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("SIGN"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("SIGNANDENCRYPT"), PyLong_FromLong(3));
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
    setItem(enum_dict, PyUnicode_FromString("ANONYMOUS"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("USERNAME"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("CERTIFICATE"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("ISSUEDTOKEN"), PyLong_FromLong(3));
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
    setItem(enum_dict, PyUnicode_FromString("ISSUE"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("RENEW"), PyLong_FromLong(1));
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
    setItem(enum_dict, PyUnicode_FromString("NONE"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("ACCESSLEVEL"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("ARRAYDIMENSIONS"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("BROWSENAME"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("CONTAINSNOLOOPS"), PyLong_FromLong(8));
    setItem(enum_dict, PyUnicode_FromString("DATATYPE"), PyLong_FromLong(16));
    setItem(enum_dict, PyUnicode_FromString("DESCRIPTION"), PyLong_FromLong(32));
    setItem(enum_dict, PyUnicode_FromString("DISPLAYNAME"), PyLong_FromLong(64));
    setItem(enum_dict, PyUnicode_FromString("EVENTNOTIFIER"), PyLong_FromLong(128));
    setItem(enum_dict, PyUnicode_FromString("EXECUTABLE"), PyLong_FromLong(256));
    setItem(enum_dict, PyUnicode_FromString("HISTORIZING"), PyLong_FromLong(512));
    setItem(enum_dict, PyUnicode_FromString("INVERSENAME"), PyLong_FromLong(1024));
    setItem(enum_dict, PyUnicode_FromString("ISABSTRACT"), PyLong_FromLong(2048));
    setItem(enum_dict, PyUnicode_FromString("MINIMUMSAMPLINGINTERVAL"), PyLong_FromLong(4096));
    setItem(enum_dict, PyUnicode_FromString("NODECLASS"), PyLong_FromLong(8192));
    setItem(enum_dict, PyUnicode_FromString("NODEID"), PyLong_FromLong(16384));
    setItem(enum_dict, PyUnicode_FromString("SYMMETRIC"), PyLong_FromLong(32768));
    setItem(enum_dict, PyUnicode_FromString("USERACCESSLEVEL"), PyLong_FromLong(65536));
    setItem(enum_dict, PyUnicode_FromString("USEREXECUTABLE"), PyLong_FromLong(131072));
    setItem(enum_dict, PyUnicode_FromString("USERWRITEMASK"), PyLong_FromLong(262144));
    setItem(enum_dict, PyUnicode_FromString("VALUERANK"), PyLong_FromLong(524288));
    setItem(enum_dict, PyUnicode_FromString("WRITEMASK"), PyLong_FromLong(1048576));
    setItem(enum_dict, PyUnicode_FromString("VALUE"), PyLong_FromLong(2097152));
    setItem(enum_dict, PyUnicode_FromString("DATATYPEDEFINITION"), PyLong_FromLong(4194304));
    setItem(enum_dict, PyUnicode_FromString("ROLEPERMISSIONS"), PyLong_FromLong(8388608));
    setItem(enum_dict, PyUnicode_FromString("ACCESSRESTRICTIONS"), PyLong_FromLong(16777216));
    setItem(enum_dict, PyUnicode_FromString("ALL"), PyLong_FromLong(33554431));
    setItem(enum_dict, PyUnicode_FromString("BASENODE"), PyLong_FromLong(26501220));
    setItem(enum_dict, PyUnicode_FromString("OBJECT"), PyLong_FromLong(26501348));
    setItem(enum_dict, PyUnicode_FromString("OBJECTTYPE"), PyLong_FromLong(26503268));
    setItem(enum_dict, PyUnicode_FromString("VARIABLE"), PyLong_FromLong(26571383));
    setItem(enum_dict, PyUnicode_FromString("VARIABLETYPE"), PyLong_FromLong(28600438));
    setItem(enum_dict, PyUnicode_FromString("METHOD"), PyLong_FromLong(26632548));
    setItem(enum_dict, PyUnicode_FromString("REFERENCETYPE"), PyLong_FromLong(26537060));
    setItem(enum_dict, PyUnicode_FromString("VIEW"), PyLong_FromLong(26501356));
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
    setItem(enum_dict, PyUnicode_FromString("ACCESSLEVEL"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("ARRAYDIMENSIONS"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("BROWSENAME"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("CONTAINSNOLOOPS"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("DATATYPE"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("DESCRIPTION"), PyLong_FromLong(5));
    setItem(enum_dict, PyUnicode_FromString("DISPLAYNAME"), PyLong_FromLong(6));
    setItem(enum_dict, PyUnicode_FromString("EVENTNOTIFIER"), PyLong_FromLong(7));
    setItem(enum_dict, PyUnicode_FromString("EXECUTABLE"), PyLong_FromLong(8));
    setItem(enum_dict, PyUnicode_FromString("HISTORIZING"), PyLong_FromLong(9));
    setItem(enum_dict, PyUnicode_FromString("INVERSENAME"), PyLong_FromLong(10));
    setItem(enum_dict, PyUnicode_FromString("ISABSTRACT"), PyLong_FromLong(11));
    setItem(enum_dict, PyUnicode_FromString("MINIMUMSAMPLINGINTERVAL"), PyLong_FromLong(12));
    setItem(enum_dict, PyUnicode_FromString("NODECLASS"), PyLong_FromLong(13));
    setItem(enum_dict, PyUnicode_FromString("NODEID"), PyLong_FromLong(14));
    setItem(enum_dict, PyUnicode_FromString("SYMMETRIC"), PyLong_FromLong(15));
    setItem(enum_dict, PyUnicode_FromString("USERACCESSLEVEL"), PyLong_FromLong(16));
    setItem(enum_dict, PyUnicode_FromString("USEREXECUTABLE"), PyLong_FromLong(17));
    setItem(enum_dict, PyUnicode_FromString("USERWRITEMASK"), PyLong_FromLong(18));
    setItem(enum_dict, PyUnicode_FromString("VALUERANK"), PyLong_FromLong(19));
    setItem(enum_dict, PyUnicode_FromString("WRITEMASK"), PyLong_FromLong(20));
    setItem(enum_dict, PyUnicode_FromString("VALUEFORVARIABLETYPE"), PyLong_FromLong(21));
    setItem(enum_dict, PyUnicode_FromString("DATATYPEDEFINITION"), PyLong_FromLong(22));
    setItem(enum_dict, PyUnicode_FromString("ROLEPERMISSIONS"), PyLong_FromLong(23));
    setItem(enum_dict, PyUnicode_FromString("ACCESSRESTRICTIONS"), PyLong_FromLong(24));
    setItem(enum_dict, PyUnicode_FromString("ACCESSLEVELEX"), PyLong_FromLong(25));
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
    setItem(enum_dict, PyUnicode_FromString("EQUALS"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("ISNULL"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("GREATERTHAN"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("LESSTHAN"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("GREATERTHANOREQUAL"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("LESSTHANOREQUAL"), PyLong_FromLong(5));
    setItem(enum_dict, PyUnicode_FromString("LIKE"), PyLong_FromLong(6));
    setItem(enum_dict, PyUnicode_FromString("NOT"), PyLong_FromLong(7));
    setItem(enum_dict, PyUnicode_FromString("BETWEEN"), PyLong_FromLong(8));
    setItem(enum_dict, PyUnicode_FromString("INLIST"), PyLong_FromLong(9));
    setItem(enum_dict, PyUnicode_FromString("AND"), PyLong_FromLong(10));
    setItem(enum_dict, PyUnicode_FromString("OR"), PyLong_FromLong(11));
    setItem(enum_dict, PyUnicode_FromString("CAST"), PyLong_FromLong(12));
    setItem(enum_dict, PyUnicode_FromString("INVIEW"), PyLong_FromLong(13));
    setItem(enum_dict, PyUnicode_FromString("OFTYPE"), PyLong_FromLong(14));
    setItem(enum_dict, PyUnicode_FromString("RELATEDTO"), PyLong_FromLong(15));
    setItem(enum_dict, PyUnicode_FromString("BITWISEAND"), PyLong_FromLong(16));
    setItem(enum_dict, PyUnicode_FromString("BITWISEOR"), PyLong_FromLong(17));
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
    setItem(enum_dict, PyUnicode_FromString("INSERT"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("REPLACE"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("UPDATE"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("DELETE"), PyLong_FromLong(4));
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
    setItem(enum_dict, PyUnicode_FromString("INSERT"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("REPLACE"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("UPDATE"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("REMOVE"), PyLong_FromLong(4));
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
    setItem(enum_dict, PyUnicode_FromString("NONE"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("COLD"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("WARM"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("HOT"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("TRANSPARENT"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("HOTANDMIRRORED"), PyLong_FromLong(5));
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
    setItem(enum_dict, PyUnicode_FromString("RUNNING"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("FAILED"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("NOCONFIGURATION"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("SUSPENDED"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("SHUTDOWN"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("TEST"), PyLong_FromLong(5));
    setItem(enum_dict, PyUnicode_FromString("COMMUNICATIONFAULT"), PyLong_FromLong(6));
    setItem(enum_dict, PyUnicode_FromString("UNKNOWN"), PyLong_FromLong(7));
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
    setItem(enum_dict, PyUnicode_FromString("LINEAR"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("LOG"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("LN"), PyLong_FromLong(2));
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
    setItem(enum_dict, PyUnicode_FromString("ABSOLUTEVALUE"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("PERCENTOFVALUE"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("PERCENTOFRANGE"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("PERCENTOFEURANGE"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("UNKNOWN"), PyLong_FromLong(4));
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
    setItem(enum_dict, PyUnicode_FromString("FORWARD"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("INVERSE"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("BOTH"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("INVALID"), PyLong_FromLong(3));
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
    setItem(enum_dict, PyUnicode_FromString("NONE"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("REFERENCETYPEID"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("ISFORWARD"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("NODECLASS"), PyLong_FromLong(4));
    setItem(enum_dict, PyUnicode_FromString("BROWSENAME"), PyLong_FromLong(8));
    setItem(enum_dict, PyUnicode_FromString("DISPLAYNAME"), PyLong_FromLong(16));
    setItem(enum_dict, PyUnicode_FromString("TYPEDEFINITION"), PyLong_FromLong(32));
    setItem(enum_dict, PyUnicode_FromString("ALL"), PyLong_FromLong(63));
    setItem(enum_dict, PyUnicode_FromString("REFERENCETYPEINFO"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("TARGETINFO"), PyLong_FromLong(60));
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
    setItem(enum_dict, PyUnicode_FromString("SOURCE"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("SERVER"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("BOTH"), PyLong_FromLong(2));
    setItem(enum_dict, PyUnicode_FromString("NEITHER"), PyLong_FromLong(3));
    setItem(enum_dict, PyUnicode_FromString("INVALID"), PyLong_FromLong(4));
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
    setItem(enum_dict, PyUnicode_FromString("DISABLED"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("SAMPLING"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("REPORTING"), PyLong_FromLong(2));
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
    setItem(enum_dict, PyUnicode_FromString("STATUS"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("STATUSVALUE"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("STATUSVALUETIMESTAMP"), PyLong_FromLong(2));
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
    setItem(enum_dict, PyUnicode_FromString("NONE"), PyLong_FromLong(0));
    setItem(enum_dict, PyUnicode_FromString("ABSOLUTE"), PyLong_FromLong(1));
    setItem(enum_dict, PyUnicode_FromString("PERCENT"), PyLong_FromLong(2));
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