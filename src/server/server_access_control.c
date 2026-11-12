/* Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner) */
/* SPDX-License-Identifier: AGPL-3.0-or-later
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

#include "server_access_control.h"
#include "../module.h"
#include <open62541/plugin/accesscontrol.h>
#include "server/ua_server_internal.h" /* getSessionById */
#include "server/ua_server_rbac.h" /* UA_Server_getEffectivePermissions */
#include "python_nodestore.h"

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
  PyServer *server = (PyServer *)ctx->server;
  return UA2PY(value, type, &server->nsMapPy2UA);
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

int
pyAccessControl_traverse(UA_AccessControl *ac, visitproc visit, void *arg) {
  if (ac->clear == py_access_control_clear && ac->context) {
    PyAccessControlContext *ctx = (PyAccessControlContext *)ac->context;
    Py_VISIT(ctx->plugin);
    Py_VISIT(ctx->server);
  }
  return 0;
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
  /* Part 4, 5.6.3.2: a NULL or empty UserIdentityToken is anonymous. The
   * server only lets it through if an anonymous policy is advertised. */
  UA_AnonymousIdentityToken anonymous;
  UA_ExtensionObject anonymous_token;
  if (!token || token->encoding == UA_EXTENSIONOBJECT_ENCODED_NOBODY) {
    UA_AnonymousIdentityToken_init(&anonymous);
    UA_ExtensionObject_setValueNoDelete(
        &anonymous_token, &anonymous,
        &UA_TYPES[UA_TYPES_ANONYMOUSIDENTITYTOKEN]);
    token = &anonymous_token;
  }
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
    if (pyServer_own_callback_ref((PyServer *)acctx->server, context) < 0) {
      Py_DECREF(context);
      UA_StatusCode status = access_control_exception_status();
      PyGILState_Release(gil);
      return status;
    }
    *sessionContext = context; /* borrowed from the server's GC-visible roots */
    Py_DECREF(context);
  }
  PyGILState_Release(gil);

#ifdef UA_ENABLE_SUBSCRIPTIONS
  /* As the open62541 default access control: remember the SecurityPolicy of
   * the endpoint for the anonymous case of the Subscription transfer policy */
  if (endpoint) {
    UA_Variant uri;
    UA_Variant_setScalar(&uri, (void *)(uintptr_t)&endpoint->securityPolicyUri,
                         &UA_TYPES[UA_TYPES_STRING]);
    UA_Server_setSessionAttribute(
        server, sessionId, UA_QUALIFIEDNAME(0, "channelSecurityPolicyUri"),
        &uri);
  }
#endif
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
  PyAccessControlContext *ctx = (PyAccessControlContext *)ac->context;
  pyServer_release_callback_ref((PyServer *)ctx->server, (PyObject *)sessionContext);
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
  PyAccessControlContext *ctx = (PyAccessControlContext *)ac->context;
  pyServer_release_callback_ref((PyServer *)ctx->server, (PyObject *)sessionContext);
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

/* The native fallbacks for hooks a Python plugin does not override. They are
 * ports of the default plugin (plugins/ua_accesscontrol_default.c), so node
 * and namespace RolePermissions and the session Roles stay enforced with a
 * Python AccessControl. The core masks the results with the AccessLevel,
 * WriteMask and Executable attributes of the node. The Python base hooks
 * (o6.server.AccessControl) compute the same values. */

/* UA_PERMISSIONTYPE_ALL means that no rules apply to the node (the default
 * plugin treats it as permissive). A node that cannot be resolved is not
 * restricted here either; the service fails on it anyway. */
static UA_PermissionType effective_permissions(UA_Server *server,
                                               const UA_NodeId *sid,
                                               const UA_NodeId *nid) {
  UA_PermissionType permissions = 0;
  if (UA_Server_getEffectivePermissions(server, sid, nid, &permissions) !=
      UA_STATUSCODE_GOOD)
    return UA_PERMISSIONTYPE_ALL;
  return permissions;
}

static UA_Boolean permits(UA_Server *server, const UA_NodeId *sid,
                          const UA_NodeId *nid, UA_PermissionType required) {
  UA_PermissionType permissions = effective_permissions(server, sid, nid);
  return permissions == UA_PERMISSIONTYPE_ALL || (permissions & required) != 0;
}

/* OPC UA Part 3, Table 8: WriteAttribute grants every WriteMask bit except
 * RolePermissions and Historizing, which have their own permission bits. */
static UA_UInt32 native_access_control_rights(UA_Server *server,
                                              UA_AccessControl *ac,
                                              const UA_NodeId *sid, void *sctx,
                                              const UA_NodeId *nid,
                                              void *nctx) {
  (void)ac;
  (void)sctx;
  (void)nctx;
  UA_PermissionType permissions = effective_permissions(server, sid, nid);
  if (permissions == UA_PERMISSIONTYPE_ALL)
    return 0xFFFFFFFFu;
  UA_UInt32 mask = 0;
  if (permissions & UA_PERMISSIONTYPE_WRITEATTRIBUTE)
    mask = 0xFFFFFFFFu &
           ~(UA_UInt32)(UA_WRITEMASK_ROLEPERMISSIONS | UA_WRITEMASK_HISTORIZING);
  if (permissions & UA_PERMISSIONTYPE_WRITEROLEPERMISSIONS)
    mask |= UA_WRITEMASK_ROLEPERMISSIONS;
  if (permissions & UA_PERMISSIONTYPE_WRITEHISTORIZING)
    mask |= UA_WRITEMASK_HISTORIZING;
  return mask;
}

/* OPC UA Part 3, Table 8. StatusWrite and TimestampWrite have no permission
 * bit and are granted only without rules. */
static UA_Byte native_access_control_level(UA_Server *server,
                                           UA_AccessControl *ac,
                                           const UA_NodeId *sid, void *sctx,
                                           const UA_NodeId *nid, void *nctx) {
  (void)ac;
  (void)sctx;
  (void)nctx;
  UA_PermissionType permissions = effective_permissions(server, sid, nid);
  if (permissions == UA_PERMISSIONTYPE_ALL)
    return 0xFFu;
  UA_Byte level = 0;
  if (permissions & UA_PERMISSIONTYPE_READ)
    level |= UA_ACCESSLEVELMASK_READ;
  if (permissions & UA_PERMISSIONTYPE_WRITE)
    level |= UA_ACCESSLEVELMASK_WRITE;
  if (permissions & UA_PERMISSIONTYPE_READHISTORY)
    level |= UA_ACCESSLEVELMASK_HISTORYREAD;
  if (permissions & (UA_PERMISSIONTYPE_INSERTHISTORY |
                     UA_PERMISSIONTYPE_MODIFYHISTORY |
                     UA_PERMISSIONTYPE_DELETEHISTORY))
    level |= UA_ACCESSLEVELMASK_HISTORYWRITE;
  return level;
}

static UA_Boolean
native_access_control_executable(UA_Server *server, UA_AccessControl *ac,
                                 const UA_NodeId *sid, void *sctx,
                                 const UA_NodeId *mid, void *mctx) {
  (void)ac;
  (void)sctx;
  (void)mctx;
  return permits(server, sid, mid, UA_PERMISSIONTYPE_CALL);
}

/* The Object and the Method must both grant Call */
static UA_Boolean native_access_control_executable_on_object(
    UA_Server *server, UA_AccessControl *ac, const UA_NodeId *sid, void *sctx,
    const UA_NodeId *mid, void *mctx, const UA_NodeId *oid, void *octx) {
  (void)ac;
  (void)sctx;
  (void)mctx;
  (void)octx;
  return permits(server, sid, oid, UA_PERMISSIONTYPE_CALL) &&
         permits(server, sid, mid, UA_PERMISSIONTYPE_CALL);
}

/* AddNode is checked on the parent, AddReference and RemoveReference on the
 * source node, DeleteNode on the node itself */
static UA_Boolean native_access_control_add_node(UA_Server *server,
                                                 UA_AccessControl *ac,
                                                 const UA_NodeId *sid,
                                                 void *sctx,
                                                 const UA_AddNodesItem *item) {
  (void)ac;
  (void)sctx;
  return permits(server, sid, &item->parentNodeId.nodeId,
                 UA_PERMISSIONTYPE_ADDNODE);
}

static UA_Boolean
native_access_control_add_reference(UA_Server *server, UA_AccessControl *ac,
                                    const UA_NodeId *sid, void *sctx,
                                    const UA_AddReferencesItem *item) {
  (void)ac;
  (void)sctx;
  return permits(server, sid, &item->sourceNodeId,
                 UA_PERMISSIONTYPE_ADDREFERENCE);
}

static UA_Boolean
native_access_control_delete_node(UA_Server *server, UA_AccessControl *ac,
                                  const UA_NodeId *sid, void *sctx,
                                  const UA_DeleteNodesItem *item) {
  (void)ac;
  (void)sctx;
  return permits(server, sid, &item->nodeId, UA_PERMISSIONTYPE_DELETENODE);
}

static UA_Boolean
native_access_control_delete_reference(UA_Server *server, UA_AccessControl *ac,
                                       const UA_NodeId *sid, void *sctx,
                                       const UA_DeleteReferencesItem *item) {
  (void)ac;
  (void)sctx;
  return permits(server, sid, &item->sourceNodeId,
                 UA_PERMISSIONTYPE_REMOVEREFERENCE);
}

static UA_Boolean native_access_control_browse(UA_Server *server,
                                               UA_AccessControl *ac,
                                               const UA_NodeId *sid, void *sctx,
                                               const UA_NodeId *nid,
                                               void *nctx) {
  (void)ac;
  (void)sctx;
  (void)nctx;
  return permits(server, sid, nid, UA_PERMISSIONTYPE_BROWSE);
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

/* Copy a String session attribute; an unset attribute yields an empty
 * String. Returns false if the session is unknown or the attribute is set to
 * a value of another type. */
static UA_Boolean session_string_attribute(UA_Server *server,
                                           const UA_NodeId *sid,
                                           const char *key, UA_String *out) {
  UA_String_init(out);
  UA_Variant value;
  UA_Variant_init(&value);
  UA_StatusCode sc = UA_Server_getSessionAttributeCopy(
      server, sid, UA_QUALIFIEDNAME(0, (char *)(uintptr_t)key), &value);
  if (sc == UA_STATUSCODE_BADNOTFOUND)
    return true;
  UA_Boolean ok = sc == UA_STATUSCODE_GOOD &&
                  UA_Variant_hasScalarType(&value, &UA_TYPES[UA_TYPES_STRING]);
  if (ok) {
    *out = *(UA_String *)value.data;
    UA_String_init((UA_String *)value.data);
  }
  UA_Variant_clear(&value);
  return ok;
}

static UA_Boolean session_application_uri(UA_Server *server,
                                          const UA_NodeId *sid,
                                          UA_String *out) {
  UA_String_init(out);
  UA_Variant value;
  UA_Variant_init(&value);
  UA_Server_getSessionAttributeCopy(
      server, sid, UA_QUALIFIEDNAME(0, "clientDescription"), &value);
  UA_Boolean ok = UA_Variant_hasScalarType(
      &value, &UA_TYPES[UA_TYPES_APPLICATIONDESCRIPTION]);
  if (ok) {
    UA_ApplicationDescription *desc = (UA_ApplicationDescription *)value.data;
    *out = desc->applicationUri;
    UA_String_init(&desc->applicationUri);
  }
  UA_Variant_clear(&value);
  return ok;
}

/* The transfer policy of the open62541 default access control. Sessions of
 * the same user may take over each other's Subscriptions. Anonymous sessions
 * have no user to compare; they must both use an encrypting SecurityPolicy
 * (the session attribute channelSecurityPolicyUri, see
 * py_access_control_activate_session) and the same ApplicationUri, which is
 * then backed by the client certificate. For detached Subscriptions, the
 * server verifies the saved owner identity before invoking this hook. */
UA_Boolean pyAccessControl_allowTransferSubscription(UA_Server *server,
                                                     const UA_NodeId *oldSid,
                                                     const UA_NodeId *newSid) {
  if (!newSid || UA_NodeId_isNull(newSid))
    return false;

  /* The server has already checked the detached Subscription owner. */
  if (!oldSid || UA_NodeId_isNull(oldSid))
    return true;

  UA_String user1, user2;
  UA_Boolean result = false;
  if (!session_string_attribute(server, oldSid, "clientUserId", &user1))
    return false;
  if (!session_string_attribute(server, newSid, "clientUserId", &user2)) {
    UA_String_clear(&user1);
    return false;
  }

  if (user1.length > 0 || user2.length > 0) {
    result = UA_String_equal(&user1, &user2);
  } else {
    UA_String sp1, sp2;
    UA_Boolean haveSp1 = session_string_attribute(
        server, oldSid, "channelSecurityPolicyUri", &sp1);
    UA_Boolean haveSp2 = session_string_attribute(
        server, newSid, "channelSecurityPolicyUri", &sp2);
    UA_Boolean bothSecure =
        haveSp1 && haveSp2 && sp1.length > 0 && sp2.length > 0 &&
        !UA_String_equal(&sp1, &UA_SECURITY_POLICY_NONE_URI) &&
        !UA_String_equal(&sp2, &UA_SECURITY_POLICY_NONE_URI);
    UA_String_clear(&sp1);
    UA_String_clear(&sp2);
    if (bothSecure) {
      UA_String uri1, uri2;
      UA_Boolean haveUri1 = session_application_uri(server, oldSid, &uri1);
      UA_Boolean haveUri2 = session_application_uri(server, newSid, &uri2);
      result = haveUri1 && haveUri2 && uri1.length > 0 &&
               UA_String_equal(&uri1, &uri2);
      UA_String_clear(&uri1);
      UA_String_clear(&uri2);
    }
  }
  UA_String_clear(&user1);
  UA_String_clear(&user2);
  return result;
}

static UA_Boolean native_access_control_transfer_subscription(
    UA_Server *server, UA_AccessControl *ac, const UA_NodeId *oldSid,
    void *oldCtx, const UA_NodeId *newSid, void *newCtx) {
  (void)ac;
  (void)oldCtx;
  (void)newCtx;
  return pyAccessControl_allowTransferSubscription(server, oldSid, newSid);
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

/* Insert needs InsertHistory, Replace and Update need ModifyHistory */
static UA_Boolean native_access_control_history_update(
    UA_Server *server, UA_AccessControl *ac, const UA_NodeId *sid, void *sctx,
    const UA_NodeId *nid, UA_PerformUpdateType perform,
    const UA_DataValue *value) {
  (void)ac;
  (void)sctx;
  (void)value;
  if (perform == UA_PERFORMUPDATETYPE_INSERT)
    return permits(server, sid, nid, UA_PERMISSIONTYPE_INSERTHISTORY);
  if (perform == UA_PERFORMUPDATETYPE_REPLACE ||
      perform == UA_PERFORMUPDATETYPE_UPDATE)
    return permits(server, sid, nid, UA_PERMISSIONTYPE_MODIFYHISTORY);
  return true;
}

static UA_Boolean native_access_control_history_delete(
    UA_Server *server, UA_AccessControl *ac, const UA_NodeId *sid, void *sctx,
    const UA_NodeId *nid, UA_DateTime start, UA_DateTime end, bool modified) {
  (void)ac;
  (void)sctx;
  (void)start;
  (void)end;
  (void)modified;
  return permits(server, sid, nid, UA_PERMISSIONTYPE_DELETEHISTORY);
}
#endif

/* AccessRestrictions (OPC UA Part 3, 5.2.11, AccessRestrictionType 8.56).
 * The bundled open62541 neither stores nor evaluates the Attribute. o6 keeps
 * it in the nodestore and wraps the authorization hooks of the installed
 * AccessControl, the default plugin or a Python one: a node whose
 * restrictions the session's SecureChannel does not meet gets no
 * UserAccessLevel, UserWriteMask or UserExecutable, and no node management.
 * Browse is restricted only with ApplyRestrictionsToBrowse. Every service
 * that reaches these hooks needs a Session (open62541 implements no
 * SessionlessInvoke), so SessionRequired is always met. The hooks run with
 * the server lock held. */

static PyServer *restricted_server(UA_Server *server) {
  return (PyServer *)UA_Server_getConfig(server)->context;
}

static UA_Boolean restrictions_met(UA_Server *server, PyServer *self,
                                   const UA_NodeId *sid, const UA_NodeId *nid,
                                   UA_Boolean browse) {
  UA_UInt16 restrictions =
      self ? pyNodeStore_accessRestrictions(self, nid) : 0;
  if (browse &&
      !(restrictions & UA_ACCESSRESTRICTIONTYPE_APPLYRESTRICTIONSTOBROWSE))
    return true;
  if (!(restrictions & (UA_ACCESSRESTRICTIONTYPE_SIGNINGREQUIRED |
                        UA_ACCESSRESTRICTIONTYPE_ENCRYPTIONREQUIRED)))
    return true;
  const UA_Session *session = sid ? getSessionById(server, sid) : NULL;
  UA_MessageSecurityMode mode = (session && session->channel)
                                    ? session->channel->securityMode
                                    : UA_MESSAGESECURITYMODE_INVALID;
  if (restrictions & UA_ACCESSRESTRICTIONTYPE_ENCRYPTIONREQUIRED)
    return mode == UA_MESSAGESECURITYMODE_SIGNANDENCRYPT;
  return mode == UA_MESSAGESECURITYMODE_SIGN ||
         mode == UA_MESSAGESECURITYMODE_SIGNANDENCRYPT;
}

static UA_UInt32 restricted_rights(UA_Server *server, UA_AccessControl *ac,
                                   const UA_NodeId *sid, void *sctx,
                                   const UA_NodeId *nid, void *nctx) {
  PyServer *self = restricted_server(server);
  if (!self || !restrictions_met(server, self, sid, nid, false))
    return 0;
  return self->restrictedAccessControl.getUserRightsMask(server, ac, sid, sctx,
                                                         nid, nctx);
}

static UA_Byte restricted_level(UA_Server *server, UA_AccessControl *ac,
                                const UA_NodeId *sid, void *sctx,
                                const UA_NodeId *nid, void *nctx) {
  PyServer *self = restricted_server(server);
  if (!self || !restrictions_met(server, self, sid, nid, false))
    return 0;
  return self->restrictedAccessControl.getUserAccessLevel(server, ac, sid, sctx,
                                                          nid, nctx);
}

static UA_Boolean restricted_executable(UA_Server *server, UA_AccessControl *ac,
                                        const UA_NodeId *sid, void *sctx,
                                        const UA_NodeId *mid, void *mctx) {
  PyServer *self = restricted_server(server);
  if (!self || !restrictions_met(server, self, sid, mid, false))
    return false;
  return self->restrictedAccessControl.getUserExecutable(server, ac, sid, sctx,
                                                         mid, mctx);
}

/* Calling a Method on an Object accesses both */
static UA_Boolean restricted_executable_on_object(
    UA_Server *server, UA_AccessControl *ac, const UA_NodeId *sid, void *sctx,
    const UA_NodeId *mid, void *mctx, const UA_NodeId *oid, void *octx) {
  PyServer *self = restricted_server(server);
  if (!self || !restrictions_met(server, self, sid, mid, false) ||
      !restrictions_met(server, self, sid, oid, false))
    return false;
  return self->restrictedAccessControl.getUserExecutableOnObject(
      server, ac, sid, sctx, mid, mctx, oid, octx);
}

static UA_Boolean restricted_add_node(UA_Server *server, UA_AccessControl *ac,
                                      const UA_NodeId *sid, void *sctx,
                                      const UA_AddNodesItem *item) {
  PyServer *self = restricted_server(server);
  if (!self ||
      !restrictions_met(server, self, sid, &item->parentNodeId.nodeId, false))
    return false;
  return self->restrictedAccessControl.allowAddNode(server, ac, sid, sctx, item);
}

static UA_Boolean restricted_add_reference(UA_Server *server,
                                           UA_AccessControl *ac,
                                           const UA_NodeId *sid, void *sctx,
                                           const UA_AddReferencesItem *item) {
  PyServer *self = restricted_server(server);
  if (!self || !restrictions_met(server, self, sid, &item->sourceNodeId, false))
    return false;
  return self->restrictedAccessControl.allowAddReference(server, ac, sid, sctx,
                                                         item);
}

static UA_Boolean restricted_delete_node(UA_Server *server,
                                         UA_AccessControl *ac,
                                         const UA_NodeId *sid, void *sctx,
                                         const UA_DeleteNodesItem *item) {
  PyServer *self = restricted_server(server);
  if (!self || !restrictions_met(server, self, sid, &item->nodeId, false))
    return false;
  return self->restrictedAccessControl.allowDeleteNode(server, ac, sid, sctx,
                                                       item);
}

static UA_Boolean
restricted_delete_reference(UA_Server *server, UA_AccessControl *ac,
                            const UA_NodeId *sid, void *sctx,
                            const UA_DeleteReferencesItem *item) {
  PyServer *self = restricted_server(server);
  if (!self || !restrictions_met(server, self, sid, &item->sourceNodeId, false))
    return false;
  return self->restrictedAccessControl.allowDeleteReference(server, ac, sid,
                                                            sctx, item);
}

static UA_Boolean restricted_browse(UA_Server *server, UA_AccessControl *ac,
                                    const UA_NodeId *sid, void *sctx,
                                    const UA_NodeId *nid, void *nctx) {
  PyServer *self = restricted_server(server);
  if (!self || !restrictions_met(server, self, sid, nid, true))
    return false;
  return self->restrictedAccessControl.allowBrowseNode(server, ac, sid, sctx,
                                                       nid, nctx);
}

void pyAccessRestrictions_wrap(PyServer *server) {
  UA_AccessControl *ac = &UA_Server_getConfig(server->server)->accessControl;
  /* Already wrapped: the plugin has not been replaced since the last start */
  if (ac->getUserAccessLevel == restricted_level)
    return;
  server->restrictedAccessControl = *ac;
  if (ac->getUserRightsMask)
    ac->getUserRightsMask = restricted_rights;
  if (ac->getUserAccessLevel)
    ac->getUserAccessLevel = restricted_level;
  if (ac->getUserExecutable)
    ac->getUserExecutable = restricted_executable;
  if (ac->getUserExecutableOnObject)
    ac->getUserExecutableOnObject = restricted_executable_on_object;
  if (ac->allowAddNode)
    ac->allowAddNode = restricted_add_node;
  if (ac->allowAddReference)
    ac->allowAddReference = restricted_add_reference;
  if (ac->allowDeleteNode)
    ac->allowDeleteNode = restricted_delete_node;
  if (ac->allowDeleteReference)
    ac->allowDeleteReference = restricted_delete_reference;
  if (ac->allowBrowseNode)
    ac->allowBrowseNode = restricted_browse;
}

UA_Boolean pyAccessControl_isPython(const UA_AccessControl *ac) {
  return ac->clear == py_access_control_clear;
}

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
