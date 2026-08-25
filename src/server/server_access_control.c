/* Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner) */
#include "server_access_control.h"
#include "../module.h"
#include <open62541/plugin/accesscontrol.h>

typedef struct {
  PyObject *plugin;
  PyObject *server;
} PyAccessControlContext;

static PyObject *access_control_arg(UA_AccessControl *ac, const void *value,
                                    const UA_DataType *type);

static PyObject *access_control_session(UA_AccessControl *ac,
                                        const UA_NodeId *sessionId,
                                        void *sessionContext) {
  PyAccessControlContext *ctx = (PyAccessControlContext *)ac->context;
  if (!ctx || !ctx->plugin || !ctx->server) {
    PyErr_SetString(PyExc_RuntimeError,
                    "AccessControl plugin has been cleared");
    return NULL;
  }
  PyObject *id = access_control_arg(ac, sessionId, &UA_TYPES[UA_TYPES_NODEID]);
  if (!id)
    return NULL;
  PyObject *context = sessionContext ? (PyObject *)sessionContext : Py_None;
  PyObject *session = PyObject_CallMethod(ctx->plugin, "_make_session", "OOO",
                                          ctx->server, id, context);
  Py_DECREF(id);
  return session;
}

static PyObject *access_control_arg(UA_AccessControl *ac, const void *value,
                                    const UA_DataType *type) {
  if (!value)
    Py_RETURN_NONE;
  PyAccessControlContext *ctx = (PyAccessControlContext *)ac->context;
  if (!ctx || !ctx->server) {
    PyErr_SetString(PyExc_RuntimeError,
                    "AccessControl plugin has no attached server");
    return NULL;
  }
  void *copy = UA_new(type);
  if (!copy)
    return PyErr_NoMemory();
  UA_StatusCode status = UA_copy(value, copy, type);
  if (status != UA_STATUSCODE_GOOD) {
    UA_delete(copy, type);
    return PyErr_StatusCode(status);
  }
  PyServer *server = (PyServer *)ctx->server;
  PyObject *result = UA2PY(copy, type, &server->nsMapPy2UA);
  UA_delete(copy, type);
  return result;
}

static UA_StatusCode access_control_exception_status(void) {
  UA_StatusCode status = UA_STATUSCODE_BADINTERNALERROR;
  PyObject *type = NULL, *value = NULL, *traceback = NULL;
  PyErr_Fetch(&type, &value, &traceback);
  PyErr_NormalizeException(&type, &value, &traceback);
  if (value && PyObject_IsInstance(value, pyExc_StatusCode) == 1) {
    PyObject *code = PyObject_GetAttrString(value, "code");
    if (code) {
      unsigned long raw = PyLong_AsUnsignedLong(code);
      if (!PyErr_Occurred())
        status = (UA_StatusCode)raw;
      Py_DECREF(code);
    }
  } else {
    PyErr_Restore(type, value, traceback);
    PyErr_Print();
    return status;
  }
  Py_XDECREF(type);
  Py_XDECREF(value);
  Py_XDECREF(traceback);
  PyErr_Clear();
  return status;
}

static PyObject *access_control_call(UA_AccessControl *ac, const char *method,
                                     PyObject *args) {
  PyAccessControlContext *ctx = (PyAccessControlContext *)ac->context;
  if (!ctx || !ctx->plugin) {
    Py_DECREF(args);
    PyErr_SetString(PyExc_RuntimeError,
                    "AccessControl plugin has been cleared");
    return NULL;
  }
  PyObject *callable = PyObject_GetAttrString(ctx->plugin, "_invoke");
  if (!callable) {
    Py_DECREF(args);
    return NULL;
  }
  PyObject *method_name = PyUnicode_FromString(method);
  PyObject *prefix = method_name ? PyTuple_Pack(1, method_name) : NULL;
  PyObject *call_args = prefix ? PySequence_Concat(prefix, args) : NULL;
  Py_XDECREF(method_name);
  Py_XDECREF(prefix);
  Py_DECREF(args);
  if (!call_args) {
    Py_DECREF(callable);
    return NULL;
  }
  PyObject *result = PyObject_CallObject(callable, call_args);
  Py_DECREF(callable);
  Py_DECREF(call_args);
  return result;
}

static void py_access_control_clear(UA_AccessControl *ac) {
  PyGILState_STATE gil = PyGILState_Ensure();
  PyAccessControlContext *ctx = (PyAccessControlContext *)ac->context;
  if (ctx) {
    if (ctx->plugin) {
      PyObject *result = PyObject_CallMethod(ctx->plugin, "clear", NULL);
      if (!result)
        PyErr_Print();
      else
        Py_DECREF(result);
      Py_DECREF(ctx->plugin);
    }
    Py_XDECREF(ctx->server);
    UA_free(ctx);
  }
  UA_Array_delete(ac->userTokenPolicies, ac->userTokenPoliciesSize,
                  &UA_TYPES[UA_TYPES_USERTOKENPOLICY]);
  memset(ac, 0, sizeof(*ac));
  PyGILState_Release(gil);
}

static UA_StatusCode py_access_control_activate_session(
    UA_Server *server, UA_AccessControl *ac,
    const UA_EndpointDescription *endpoint, const UA_ByteString *certificate,
    const UA_NodeId *sessionId, const UA_ExtensionObject *token,
    void **sessionContext) {
  PyGILState_STATE gil = PyGILState_Ensure();
  PyObject *py_endpoint =
      access_control_arg(ac, endpoint, &UA_TYPES[UA_TYPES_ENDPOINTDESCRIPTION]);
  PyObject *py_cert =
      certificate ? PyBytes_FromStringAndSize((const char *)certificate->data,
                                              (Py_ssize_t)certificate->length)
                  : PyBytes_FromStringAndSize("", 0);
  PyObject *py_session = access_control_session(ac, sessionId, NULL);
  PyObject *py_token =
      access_control_arg(ac, token, &UA_TYPES[UA_TYPES_EXTENSIONOBJECT]);
  if (py_token) {
    PyObject *body = PyObject_GetAttrString(py_token, "body");
    if (body && body != Py_None) {
      Py_DECREF(py_token);
      py_token = body;
    } else {
      Py_XDECREF(body);
      PyErr_Clear();
    }
  }
  if (!py_endpoint || !py_cert || !py_session || !py_token) {
    Py_XDECREF(py_endpoint);
    Py_XDECREF(py_cert);
    Py_XDECREF(py_session);
    Py_XDECREF(py_token);
    UA_StatusCode status = access_control_exception_status();
    PyGILState_Release(gil);
    return status;
  }
  PyObject *args = PyTuple_Pack(4, py_endpoint, py_cert, py_session, py_token);
  Py_DECREF(py_endpoint);
  Py_DECREF(py_cert);
  Py_DECREF(py_token);
  PyObject *result =
      args ? access_control_call(ac, "activateSession", args) : NULL;
  if (!result) {
    Py_DECREF(py_session);
    UA_StatusCode status = access_control_exception_status();
    PyGILState_Release(gil);
    return status;
  }
  PyAccessControlContext *acctx = (PyAccessControlContext *)ac->context;
  PyObject *context = PyObject_CallMethod(acctx->plugin, "_complete_activation",
                                          "OO", py_session, result);
  Py_DECREF(result);
  if (!context) {
    Py_DECREF(py_session);
    UA_StatusCode status = access_control_exception_status();
    PyGILState_Release(gil);
    return status;
  }
  if (PyObject_SetAttrString(py_session, "context", context) < 0) {
    Py_DECREF(py_session);
    Py_DECREF(context);
    UA_StatusCode status = access_control_exception_status();
    PyGILState_Release(gil);
    return status;
  }
  Py_DECREF(py_session);
  if (context == Py_None) {
    Py_DECREF(context);
    *sessionContext = NULL;
  } else {
    *sessionContext = context; /* strong reference, released by closeSession */
  }
  PyGILState_Release(gil);
  return UA_STATUSCODE_GOOD;
}

static void py_access_control_close_session(UA_Server *server,
                                            UA_AccessControl *ac,
                                            const UA_NodeId *sessionId,
                                            void *sessionContext) {
  PyGILState_STATE gil = PyGILState_Ensure();
  PyObject *py_session = access_control_session(ac, sessionId, sessionContext);
  if (py_session) {
    PyObject *args = PyTuple_Pack(1, py_session);
    Py_DECREF(py_session);
    PyObject *result =
        args ? access_control_call(ac, "closeSession", args) : NULL;
    if (!result)
      PyErr_Print();
    else
      Py_DECREF(result);
  } else {
    PyErr_Print();
  }
  Py_XDECREF((PyObject *)sessionContext); /* activate_session reference */
  PyGILState_Release(gil);
}

static void native_access_control_close_session(UA_Server *server,
                                                UA_AccessControl *ac,
                                                const UA_NodeId *sessionId,
                                                void *sessionContext) {
  (void)server;
  (void)ac;
  (void)sessionId;
  if (!sessionContext)
    return;
  PyGILState_STATE gil = PyGILState_Ensure();
  Py_DECREF((PyObject *)sessionContext);
  PyGILState_Release(gil);
}

static PyObject *access_control_session_args(const UA_NodeId *sessionId,
                                             void *sessionContext,
                                             const void *item,
                                             const UA_DataType *itemType,
                                             UA_AccessControl *ac) {
  PyObject *py_session = access_control_session(ac, sessionId, sessionContext);
  PyObject *py_item = access_control_arg(ac, item, itemType);
  if (!py_session || !py_item) {
    Py_XDECREF(py_session);
    Py_XDECREF(py_item);
    return NULL;
  }
  PyObject *args = PyTuple_Pack(2, py_session, py_item);
  Py_DECREF(py_session);
  Py_DECREF(py_item);
  return args;
}

static unsigned long access_control_ulong(UA_AccessControl *ac,
                                          const char *method, PyObject *args,
                                          unsigned long denied) {
  PyObject *result = args ? access_control_call(ac, method, args) : NULL;
  if (!result) {
    PyErr_Print();
    return denied;
  }
  unsigned long value = PyLong_AsUnsignedLong(result);
  Py_DECREF(result);
  if (PyErr_Occurred()) {
    PyErr_Print();
    return denied;
  }
  return value;
}

static UA_UInt32 py_access_control_rights(UA_Server *server,
                                          UA_AccessControl *ac,
                                          const UA_NodeId *sid, void *sctx,
                                          const UA_NodeId *nid, void *nctx) {
  (void)server;
  (void)nctx;
  PyGILState_STATE gil = PyGILState_Ensure();
  unsigned long out =
      access_control_ulong(ac, "getUserRightsMask",
                           access_control_session_args(
                               sid, sctx, nid, &UA_TYPES[UA_TYPES_NODEID], ac),
                           0);
  PyGILState_Release(gil);
  return (UA_UInt32)out;
}

static UA_Byte py_access_control_level(UA_Server *server, UA_AccessControl *ac,
                                       const UA_NodeId *sid, void *sctx,
                                       const UA_NodeId *nid, void *nctx) {
  (void)server;
  (void)nctx;
  PyGILState_STATE gil = PyGILState_Ensure();
  unsigned long out =
      access_control_ulong(ac, "getUserAccessLevel",
                           access_control_session_args(
                               sid, sctx, nid, &UA_TYPES[UA_TYPES_NODEID], ac),
                           0);
  PyGILState_Release(gil);
  return (UA_Byte)out;
}

static UA_Boolean access_control_bool_item(UA_AccessControl *ac,
                                           const char *method,
                                           const UA_NodeId *sid, void *sctx,
                                           const void *item,
                                           const UA_DataType *type) {
  PyGILState_STATE gil = PyGILState_Ensure();
  unsigned long out = access_control_ulong(
      ac, method, access_control_session_args(sid, sctx, item, type, ac), 0);
  PyGILState_Release(gil);
  return out ? true : false;
}

#define AC_BOOL_CALLBACK(name, method, itemtype, uatype)                       \
  static UA_Boolean name(UA_Server *server, UA_AccessControl *ac,              \
                         const UA_NodeId *sid, void *sctx,                     \
                         const itemtype *item) {                               \
    (void)server;                                                              \
    return access_control_bool_item(ac, method, sid, sctx, item,               \
                                    &UA_TYPES[uatype]);                        \
  }

AC_BOOL_CALLBACK(py_access_control_add_node, "allowAddNode", UA_AddNodesItem,
                 UA_TYPES_ADDNODESITEM)
AC_BOOL_CALLBACK(py_access_control_add_reference, "allowAddReference",
                 UA_AddReferencesItem, UA_TYPES_ADDREFERENCESITEM)
AC_BOOL_CALLBACK(py_access_control_delete_node, "allowDeleteNode",
                 UA_DeleteNodesItem, UA_TYPES_DELETENODESITEM)
AC_BOOL_CALLBACK(py_access_control_delete_reference, "allowDeleteReference",
                 UA_DeleteReferencesItem, UA_TYPES_DELETEREFERENCESITEM)

static UA_Boolean py_access_control_browse(UA_Server *server,
                                           UA_AccessControl *ac,
                                           const UA_NodeId *sid, void *sctx,
                                           const UA_NodeId *nid, void *nctx) {
  (void)server;
  (void)nctx;
  return access_control_bool_item(ac, "allowBrowseNode", sid, sctx, nid,
                                  &UA_TYPES[UA_TYPES_NODEID]);
}

static UA_Boolean py_access_control_executable(UA_Server *server,
                                               UA_AccessControl *ac,
                                               const UA_NodeId *sid, void *sctx,
                                               const UA_NodeId *mid,
                                               void *mctx) {
  (void)server;
  (void)mctx;
  return access_control_bool_item(ac, "getUserExecutable", sid, sctx, mid,
                                  &UA_TYPES[UA_TYPES_NODEID]);
}

static UA_Boolean py_access_control_executable_on_object(
    UA_Server *server, UA_AccessControl *ac, const UA_NodeId *sid, void *sctx,
    const UA_NodeId *mid, void *mctx, const UA_NodeId *oid, void *octx) {
  (void)server;
  (void)mctx;
  (void)octx;
  PyGILState_STATE gil = PyGILState_Ensure();
  PyObject *base = access_control_session_args(sid, sctx, mid,
                                               &UA_TYPES[UA_TYPES_NODEID], ac);
  PyObject *py_object = access_control_arg(ac, oid, &UA_TYPES[UA_TYPES_NODEID]);
  PyObject *args = NULL;
  if (base && py_object) {
    args = PyTuple_Pack(3, PyTuple_GET_ITEM(base, 0), PyTuple_GET_ITEM(base, 1),
                        py_object);
  }
  Py_XDECREF(base);
  Py_XDECREF(py_object);
  unsigned long out =
      access_control_ulong(ac, "getUserExecutableOnObject", args, 0);
  PyGILState_Release(gil);
  return out ? true : false;
}

static UA_UInt32 native_access_control_rights(UA_Server *server,
                                              UA_AccessControl *ac,
                                              const UA_NodeId *sid, void *sctx,
                                              const UA_NodeId *nid,
                                              void *nctx) {
  (void)server;
  (void)ac;
  (void)sid;
  (void)sctx;
  (void)nid;
  (void)nctx;
  return 0xFFFFFFFFu;
}

static UA_Byte native_access_control_level(UA_Server *server,
                                           UA_AccessControl *ac,
                                           const UA_NodeId *sid, void *sctx,
                                           const UA_NodeId *nid, void *nctx) {
  (void)server;
  (void)ac;
  (void)sid;
  (void)sctx;
  (void)nid;
  (void)nctx;
  return 0xFFu;
}

static UA_Boolean
native_access_control_executable(UA_Server *server, UA_AccessControl *ac,
                                 const UA_NodeId *sid, void *sctx,
                                 const UA_NodeId *mid, void *mctx) {
  (void)server;
  (void)ac;
  (void)sid;
  (void)sctx;
  (void)mid;
  (void)mctx;
  return true;
}

static UA_Boolean native_access_control_executable_on_object(
    UA_Server *server, UA_AccessControl *ac, const UA_NodeId *sid, void *sctx,
    const UA_NodeId *mid, void *mctx, const UA_NodeId *oid, void *octx) {
  (void)server;
  (void)ac;
  (void)sid;
  (void)sctx;
  (void)mid;
  (void)mctx;
  (void)oid;
  (void)octx;
  return true;
}

#define NATIVE_AC_ALLOW(name, itemtype)                                        \
  static UA_Boolean name(UA_Server *server, UA_AccessControl *ac,              \
                         const UA_NodeId *sid, void *sctx,                     \
                         const itemtype *item) {                               \
    (void)server;                                                              \
    (void)ac;                                                                  \
    (void)sid;                                                                 \
    (void)sctx;                                                                \
    (void)item;                                                                \
    return true;                                                               \
  }

NATIVE_AC_ALLOW(native_access_control_add_node, UA_AddNodesItem)
NATIVE_AC_ALLOW(native_access_control_add_reference, UA_AddReferencesItem)
NATIVE_AC_ALLOW(native_access_control_delete_node, UA_DeleteNodesItem)
NATIVE_AC_ALLOW(native_access_control_delete_reference, UA_DeleteReferencesItem)

static UA_Boolean native_access_control_browse(UA_Server *server,
                                               UA_AccessControl *ac,
                                               const UA_NodeId *sid, void *sctx,
                                               const UA_NodeId *nid,
                                               void *nctx) {
  (void)server;
  (void)ac;
  (void)sid;
  (void)sctx;
  (void)nid;
  (void)nctx;
  return true;
}

#ifdef UA_ENABLE_SUBSCRIPTIONS
static UA_Boolean py_access_control_create_subscription(UA_Server *server,
                                                        UA_AccessControl *ac,
                                                        const UA_NodeId *sid,
                                                        void *sctx) {
  (void)server;
  PyGILState_STATE gil = PyGILState_Ensure();
  PyObject *py_session = access_control_session(ac, sid, sctx);
  PyObject *args = NULL;
  if (py_session)
    args = PyTuple_Pack(1, py_session);
  Py_XDECREF(py_session);
  unsigned long out =
      access_control_ulong(ac, "allowCreateSubscription", args, 0);
  PyGILState_Release(gil);
  return out ? true : false;
}

static UA_Boolean native_access_control_create_subscription(
    UA_Server *server, UA_AccessControl *ac, const UA_NodeId *sid, void *sctx) {
  (void)server;
  (void)ac;
  (void)sid;
  (void)sctx;
  return true;
}

static UA_Boolean
py_access_control_transfer_subscription(UA_Server *server, UA_AccessControl *ac,
                                        const UA_NodeId *oldSid, void *oldCtx,
                                        const UA_NodeId *newSid, void *newCtx) {
  (void)server;
  PyGILState_STATE gil = PyGILState_Ensure();
  PyObject *old_id = access_control_session(ac, oldSid, oldCtx);
  PyObject *new_id = access_control_session(ac, newSid, newCtx);
  PyObject *args = NULL;
  if (old_id && new_id)
    args = PyTuple_Pack(2, old_id, new_id);
  Py_XDECREF(old_id);
  Py_XDECREF(new_id);
  unsigned long out =
      access_control_ulong(ac, "allowTransferSubscription", args, 0);
  PyGILState_Release(gil);
  return out ? true : false;
}

static UA_Boolean native_access_control_transfer_subscription(
    UA_Server *server, UA_AccessControl *ac, const UA_NodeId *oldSid,
    void *oldCtx, const UA_NodeId *newSid, void *newCtx) {
  (void)server;
  (void)ac;
  (void)oldSid;
  (void)newSid;
  return oldCtx == newCtx;
}
#endif

#ifdef UA_ENABLE_HISTORIZING
static UA_Boolean py_access_control_history_update(
    UA_Server *server, UA_AccessControl *ac, const UA_NodeId *sid, void *sctx,
    const UA_NodeId *nid, UA_PerformUpdateType perform,
    const UA_DataValue *value) {
  (void)server;
  PyGILState_STATE gil = PyGILState_Ensure();
  PyObject *base = access_control_session_args(sid, sctx, nid,
                                               &UA_TYPES[UA_TYPES_NODEID], ac);
  PyObject *py_perform = PyLong_FromLong((long)perform);
  PyObject *py_value = access_control_arg(ac, value, &UA_TYPES[UA_TYPES_DATAVALUE]);
  PyObject *args = NULL;
  if (base && py_perform && py_value)
    args = PyTuple_Pack(4, PyTuple_GET_ITEM(base, 0), PyTuple_GET_ITEM(base, 1),
                        py_perform, py_value);
  Py_XDECREF(base);
  Py_XDECREF(py_perform);
  Py_XDECREF(py_value);
  unsigned long out = access_control_ulong(ac, "allowHistoryUpdate", args, 0);
  PyGILState_Release(gil);
  return out ? true : false;
}

static UA_Boolean py_access_control_history_delete(
    UA_Server *server, UA_AccessControl *ac, const UA_NodeId *sid, void *sctx,
    const UA_NodeId *nid, UA_DateTime start, UA_DateTime end, bool modified) {
  (void)server;
  PyGILState_STATE gil = PyGILState_Ensure();
  PyObject *base = access_control_session_args(sid, sctx, nid,
                                               &UA_TYPES[UA_TYPES_NODEID], ac);
  PyObject *py_start = access_control_arg(ac, &start, &UA_TYPES[UA_TYPES_DATETIME]);
  PyObject *py_end = access_control_arg(ac, &end, &UA_TYPES[UA_TYPES_DATETIME]);
  PyObject *args = NULL;
  if (base && py_start && py_end)
    args = PyTuple_Pack(5, PyTuple_GET_ITEM(base, 0), PyTuple_GET_ITEM(base, 1),
                        py_start, py_end, modified ? Py_True : Py_False);
  Py_XDECREF(base);
  Py_XDECREF(py_start);
  Py_XDECREF(py_end);
  unsigned long out = access_control_ulong(ac, "allowHistoryDelete", args, 0);
  PyGILState_Release(gil);
  return out ? true : false;
}

static UA_Boolean native_access_control_history_update(
    UA_Server *server, UA_AccessControl *ac, const UA_NodeId *sid, void *sctx,
    const UA_NodeId *nid, UA_PerformUpdateType perform,
    const UA_DataValue *value) {
  (void)server;
  (void)ac;
  (void)sid;
  (void)sctx;
  (void)nid;
  (void)perform;
  (void)value;
  return true;
}

static UA_Boolean native_access_control_history_delete(
    UA_Server *server, UA_AccessControl *ac, const UA_NodeId *sid, void *sctx,
    const UA_NodeId *nid, UA_DateTime start, UA_DateTime end, bool modified) {
  (void)server;
  (void)ac;
  (void)sid;
  (void)sctx;
  (void)nid;
  (void)start;
  (void)end;
  (void)modified;
  return true;
}
#endif

static int access_control_override(PyObject *overrides, const char *name) {
  PyObject *key = PyUnicode_FromString(name);
  if (!key)
    return 0;
  int contains = PySet_Contains(overrides, key);
  Py_DECREF(key);
  return contains > 0;
}

PyObject *PyAccessControl_install(PyServerConfig *self, PyObject *plugin) {
  UA_ServerConfig *cfg = (self->py_server && self->py_server->server)
                             ? UA_Server_getConfig(self->py_server->server)
                             : NULL;
  if (!cfg) {
    PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
    return NULL;
  }
  if (self->py_server->running) {
    PyErr_SetString(PyExc_RuntimeError,
                    "Cannot modify access control while server is running");
    return NULL;
  }
  PyObject *overrides =
      PyObject_CallMethod(plugin, "_overridden_callbacks", NULL);
  if (!overrides)
    return NULL;
  if (!PyAnySet_Check(overrides)) {
    Py_DECREF(overrides);
    PyErr_SetString(PyExc_TypeError,
                    "AccessControl._overridden_callbacks() must return a set");
    return NULL;
  }
  PyObject *policies_obj =
      PyObject_GetAttrString(plugin, "user_token_policies");
  if (!policies_obj) {
    Py_DECREF(overrides);
    return NULL;
  }
  PyObject *policies = PySequence_Fast(
      policies_obj, "AccessControl.user_token_policies must be a sequence");
  Py_DECREF(policies_obj);
  if (!policies) {
    Py_DECREF(overrides);
    return NULL;
  }
  Py_ssize_t count = PySequence_Fast_GET_SIZE(policies);
  if (count <= 0) {
    Py_DECREF(policies);
    Py_DECREF(overrides);
    PyErr_SetString(
        PyExc_ValueError,
        "AccessControl must advertise at least one user token policy");
    return NULL;
  }

  UA_UserTokenPolicy *ua_policies = (UA_UserTokenPolicy *)UA_Array_new(
      (size_t)count, &UA_TYPES[UA_TYPES_USERTOKENPOLICY]);
  if (!ua_policies) {
    Py_DECREF(policies);
    Py_DECREF(overrides);
    return PyErr_NoMemory();
  }
  for (Py_ssize_t i = 0; i < count; i++) {
    PyObject *item = PySequence_Fast_GET_ITEM(policies, i);
    if (!PY2UA(item, &ua_policies[i], &UA_TYPES[UA_TYPES_USERTOKENPOLICY],
               &self->py_server->nsMapPy2UA, cfg->customDataTypes)) {
      UA_Array_delete(ua_policies, (size_t)count,
                      &UA_TYPES[UA_TYPES_USERTOKENPOLICY]);
      Py_DECREF(policies);
      Py_DECREF(overrides);
      return NULL;
    }
  }
  Py_DECREF(policies);

  PyAccessControlContext *ctx =
      (PyAccessControlContext *)UA_calloc(1, sizeof(*ctx));
  if (!ctx) {
    UA_Array_delete(ua_policies, (size_t)count,
                    &UA_TYPES[UA_TYPES_USERTOKENPOLICY]);
    Py_DECREF(overrides);
    return PyErr_NoMemory();
  }
  Py_INCREF(plugin);
  ctx->plugin = plugin;
  ctx->server = (PyObject *)self->py_server;
  Py_INCREF(ctx->server);

  if (cfg->accessControl.clear)
    cfg->accessControl.clear(&cfg->accessControl);
  memset(&cfg->accessControl, 0, sizeof(cfg->accessControl));
  cfg->accessControl.context = ctx;
  cfg->accessControl.clear = py_access_control_clear;
  cfg->accessControl.userTokenPolicies = ua_policies;
  cfg->accessControl.userTokenPoliciesSize = (size_t)count;
  cfg->accessControl.activateSession = py_access_control_activate_session;
#define OVERRIDDEN(name) access_control_override(overrides, name)
  cfg->accessControl.closeSession = OVERRIDDEN("closeSession")
                                        ? py_access_control_close_session
                                        : native_access_control_close_session;
  cfg->accessControl.getUserRightsMask = OVERRIDDEN("getUserRightsMask")
                                             ? py_access_control_rights
                                             : native_access_control_rights;
  cfg->accessControl.getUserAccessLevel = OVERRIDDEN("getUserAccessLevel")
                                              ? py_access_control_level
                                              : native_access_control_level;
  cfg->accessControl.getUserExecutable = OVERRIDDEN("getUserExecutable")
                                             ? py_access_control_executable
                                             : native_access_control_executable;
  cfg->accessControl.getUserExecutableOnObject =
      OVERRIDDEN("getUserExecutableOnObject")
          ? py_access_control_executable_on_object
          : native_access_control_executable_on_object;
  cfg->accessControl.allowAddNode = OVERRIDDEN("allowAddNode")
                                        ? py_access_control_add_node
                                        : native_access_control_add_node;
  cfg->accessControl.allowAddReference =
      OVERRIDDEN("allowAddReference") ? py_access_control_add_reference
                                        : native_access_control_add_reference;
  cfg->accessControl.allowDeleteNode = OVERRIDDEN("allowDeleteNode")
                                           ? py_access_control_delete_node
                                           : native_access_control_delete_node;
  cfg->accessControl.allowDeleteReference =
      OVERRIDDEN("allowDeleteReference")
          ? py_access_control_delete_reference
          : native_access_control_delete_reference;
  cfg->accessControl.allowBrowseNode = OVERRIDDEN("allowBrowseNode")
                                           ? py_access_control_browse
                                           : native_access_control_browse;
#ifdef UA_ENABLE_SUBSCRIPTIONS
  cfg->accessControl.allowCreateSubscription =
      OVERRIDDEN("allowCreateSubscription")
          ? py_access_control_create_subscription
          : native_access_control_create_subscription;
  cfg->accessControl.allowTransferSubscription =
      OVERRIDDEN("allowTransferSubscription")
          ? py_access_control_transfer_subscription
          : native_access_control_transfer_subscription;
#endif
#ifdef UA_ENABLE_HISTORIZING
  cfg->accessControl.allowHistoryUpdateUpdateData =
      OVERRIDDEN("allowHistoryUpdate") ? py_access_control_history_update
                                         : native_access_control_history_update;
  cfg->accessControl.allowHistoryUpdateDeleteRawModified =
      OVERRIDDEN("allowHistoryDelete") ? py_access_control_history_delete
                                         : native_access_control_history_delete;
#endif
#undef OVERRIDDEN
  Py_DECREF(overrides);
  Py_RETURN_NONE;
}
