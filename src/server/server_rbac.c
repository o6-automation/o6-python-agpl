/* Copyright 2026 (c) o6 Automation GmbH */
#include "../types_internal.h"
#include "server.h"
#include "server_services_util.h"

#ifndef UA_ENABLE_RBAC
#error "o6 server support requires open62541 built with UA_ENABLE_RBAC"
#endif

static const UA_DataTypeArray *custom_types(PyServer *self) {
  return UA_Server_getConfig(self->server)->customDataTypes;
}

static int convert_array(PyServer *self, PyObject *seq, const UA_DataType *type,
                         void **out, size_t *size) {
  PyObject *fast = PySequence_Fast(seq, "expected an iterable");
  if (!fast)
    return -1;
  Py_ssize_t count = PySequence_Fast_GET_SIZE(fast);
  void *items = count ? UA_Array_new((size_t)count, type) : NULL;
  if (count && !items) {
    Py_DECREF(fast);
    PyErr_NoMemory();
    return -1;
  }
  for (Py_ssize_t i = 0; i < count; i++) {
    void *dst = (UA_Byte *)items + ((size_t)i * type->memSize);
    if (!PY2UA(PySequence_Fast_GET_ITEM(fast, i), dst, type, &self->nsMapPy2UA,
               custom_types(self))) {
      UA_Array_delete(items, (size_t)count, type);
      Py_DECREF(fast);
      return -1;
    }
  }
  Py_DECREF(fast);
  *out = items;
  *size = (size_t)count;
  return 0;
}

static int convert_permissions(PyServer *self, PyObject *mapping,
                               UA_RolePermission **out, size_t *size) {
  PyObject *items = PyMapping_Items(mapping);
  if (!items)
    return -1;
  Py_ssize_t count = PyList_GET_SIZE(items);
  UA_RolePermission *entries =
      count ? (UA_RolePermission *)UA_calloc((size_t)count,
                                             sizeof(UA_RolePermission))
            : NULL;
  if (count && !entries) {
    Py_DECREF(items);
    PyErr_NoMemory();
    return -1;
  }
  for (Py_ssize_t i = 0; i < count; i++) {
    PyObject *pair = PyList_GET_ITEM(items, i);
    PyObject *role = PyTuple_GET_ITEM(pair, 0);
    PyObject *permission = PyTuple_GET_ITEM(pair, 1);
    if (!PY2UA(role, &entries[i].roleId, &UA_TYPES[UA_TYPES_NODEID],
               &self->nsMapPy2UA, custom_types(self)))
      goto error;
    unsigned long raw = PyLong_AsUnsignedLong(permission);
    if (PyErr_Occurred())
      goto error;
    entries[i].permissions = (UA_PermissionType)raw;
  }
  Py_DECREF(items);
  *out = entries;
  *size = (size_t)count;
  return 0;
error:
  for (Py_ssize_t i = 0; i < count; i++)
    UA_NodeId_clear(&entries[i].roleId);
  UA_free(entries);
  Py_DECREF(items);
  return -1;
}

static void clear_permissions(UA_RolePermission *entries, size_t size) {
  for (size_t i = 0; i < size; i++)
    UA_NodeId_clear(&entries[i].roleId);
  UA_free(entries);
}

static PyObject *array_to_list(PyServer *self, const void *items, size_t size,
                               const UA_DataType *type) {
  PyObject *list = PyList_New((Py_ssize_t)size);
  if (!list)
    return NULL;
  for (size_t i = 0; i < size; i++) {
    void *item = (UA_Byte *)items + (i * type->memSize);
    PyObject *value = UA2PY(item, type, &self->nsMapPy2UA);
    if (!value) {
      Py_DECREF(list);
      return NULL;
    }
    PyList_SET_ITEM(list, (Py_ssize_t)i, value);
  }
  return list;
}

static PyObject *permissions_to_dict(PyServer *self, UA_RolePermission *entries,
                                     size_t size) {
  PyObject *dict = PyDict_New();
  if (!dict)
    return NULL;
  for (size_t i = 0; i < size; i++) {
    PyObject *role = UA2PY(&entries[i].roleId, &UA_TYPES[UA_TYPES_NODEID],
                           &self->nsMapPy2UA);
    PyObject *value = PyLong_FromUnsignedLong(entries[i].permissions);
    if (!role || !value || PyDict_SetItem(dict, role, value) < 0) {
      Py_XDECREF(role);
      Py_XDECREF(value);
      Py_DECREF(dict);
      return NULL;
    }
    Py_DECREF(role);
    Py_DECREF(value);
  }
  return dict;
}

static int convert_role(PyServer *self, PyObject *role_id, PyObject *name,
                        PyObject *identities, PyObject *applications,
                        int applications_exclude, PyObject *endpoints,
                        int endpoints_exclude, UA_Role *role) {
  UA_Role_init(role);
  if (role_id != Py_None &&
      !PY2UA(role_id, &role->roleId, &UA_TYPES[UA_TYPES_NODEID],
             &self->nsMapPy2UA, custom_types(self)))
    goto error;
  if (!PY2UA(name, &role->roleName, &UA_TYPES[UA_TYPES_QUALIFIEDNAME],
             &self->nsMapPy2UA, custom_types(self)))
    goto error;
  if (convert_array(self, identities,
                    &UA_TYPES[UA_TYPES_IDENTITYMAPPINGRULETYPE],
                    (void **)&role->identityMappingRules,
                    &role->identityMappingRulesSize) < 0)
    goto error;
  if (convert_array(self, applications, &UA_TYPES[UA_TYPES_STRING],
                    (void **)&role->applications, &role->applicationsSize) < 0)
    goto error;
  if (convert_array(self, endpoints, &UA_TYPES[UA_TYPES_ENDPOINTTYPE],
                    (void **)&role->endpoints, &role->endpointsSize) < 0)
    goto error;
  role->applicationsExclude = applications_exclude;
  role->endpointsExclude = endpoints_exclude;
  return 0;
error:
  UA_Role_clear(role);
  return -1;
}

static PyObject *role_to_dict(PyServer *self, const UA_Role *role) {
  PyObject *id = UA2PY((void *)&role->roleId, &UA_TYPES[UA_TYPES_NODEID],
                       &self->nsMapPy2UA);
  PyObject *name = UA2PY((void *)&role->roleName,
                         &UA_TYPES[UA_TYPES_QUALIFIEDNAME], &self->nsMapPy2UA);
  PyObject *identities = array_to_list(
      self, role->identityMappingRules, role->identityMappingRulesSize,
      &UA_TYPES[UA_TYPES_IDENTITYMAPPINGRULETYPE]);
  PyObject *apps =
      array_to_list(self, role->applications, role->applicationsSize,
                    &UA_TYPES[UA_TYPES_STRING]);
  PyObject *ends = array_to_list(self, role->endpoints, role->endpointsSize,
                                 &UA_TYPES[UA_TYPES_ENDPOINTTYPE]);
  if (!id || !name || !identities || !apps || !ends) {
    Py_XDECREF(id);
    Py_XDECREF(name);
    Py_XDECREF(identities);
    Py_XDECREF(apps);
    Py_XDECREF(ends);
    return NULL;
  }
  PyObject *out = Py_BuildValue(
      "{s:O,s:O,s:O,s:O,s:O,s:O,s:O}", "id", id, "name", name, "identities",
      identities, "applications", apps, "applications_exclude",
      role->applicationsExclude ? Py_True : Py_False, "endpoints", ends,
      "endpoints_exclude", role->endpointsExclude ? Py_True : Py_False);
  Py_DECREF(id);
  Py_DECREF(name);
  Py_DECREF(identities);
  Py_DECREF(apps);
  Py_DECREF(ends);
  return out;
}

PyObject *pyServer_close_session(PyObject *obj, PyObject *args) {
  PyServer *self = (PyServer *)obj;
  PyObject *sid;
  UA_NodeId id;
  if (!PyArg_ParseTuple(args, "O", &sid) ||
      extract_nodeid(sid, &id, &self->nsMapPy2UA, custom_types(self)) < 0)
    return NULL;
  UA_StatusCode sc = UA_Server_closeSession(self->server, &id);
  UA_NodeId_clear(&id);
  if (sc)
    return PyErr_StatusCode(sc);
  Py_RETURN_NONE;
}

static int session_key(PyServer *self, PyObject *sid, PyObject *key,
                       UA_NodeId *id, UA_QualifiedName *qn) {
  if (extract_nodeid(sid, id, &self->nsMapPy2UA, custom_types(self)) < 0)
    return -1;
  if (extract_qualifiedname(key, qn, &self->nsMapPy2UA, custom_types(self)) <
      0) {
    UA_NodeId_clear(id);
    return -1;
  }
  return 0;
}

PyObject *pyServer_get_session_attribute(PyObject *obj, PyObject *args) {
  PyServer *self = (PyServer *)obj;
  PyObject *sid, *key;
  UA_NodeId id;
  UA_QualifiedName qn;
  UA_Variant value;
  UA_Variant_init(&value);
  if (!PyArg_ParseTuple(args, "OO", &sid, &key) ||
      session_key(self, sid, key, &id, &qn) < 0)
    return NULL;
  UA_StatusCode sc =
      UA_Server_getSessionAttributeCopy(self->server, &id, qn, &value);
  UA_NodeId_clear(&id);
  UA_QualifiedName_clear(&qn);
  if (sc)
    return PyErr_StatusCode(sc);
  PyObject *out = UA2PY(&value, &UA_TYPES[UA_TYPES_VARIANT], &self->nsMapPy2UA);
  UA_Variant_clear(&value);
  return out;
}

PyObject *pyServer_set_session_attribute(PyObject *obj, PyObject *args) {
  PyServer *self = (PyServer *)obj;
  PyObject *sid, *key, *pyvalue;
  UA_NodeId id;
  UA_QualifiedName qn;
  UA_Variant value;
  UA_Variant_init(&value);
  if (!PyArg_ParseTuple(args, "OOO", &sid, &key, &pyvalue) ||
      session_key(self, sid, key, &id, &qn) < 0)
    return NULL;
  if (!PY2UA(pyvalue, &value, &UA_TYPES[UA_TYPES_VARIANT], &self->nsMapPy2UA,
             custom_types(self))) {
    UA_NodeId_clear(&id);
    UA_QualifiedName_clear(&qn);
    return NULL;
  }
  UA_StatusCode sc =
      UA_Server_setSessionAttribute(self->server, &id, qn, &value);
  UA_Variant_clear(&value);
  UA_NodeId_clear(&id);
  UA_QualifiedName_clear(&qn);
  if (sc)
    return PyErr_StatusCode(sc);
  Py_RETURN_NONE;
}

PyObject *pyServer_delete_session_attribute(PyObject *obj, PyObject *args) {
  PyServer *self = (PyServer *)obj;
  PyObject *sid, *key;
  UA_NodeId id;
  UA_QualifiedName qn;
  if (!PyArg_ParseTuple(args, "OO", &sid, &key) ||
      session_key(self, sid, key, &id, &qn) < 0)
    return NULL;
  UA_StatusCode sc = UA_Server_deleteSessionAttribute(self->server, &id, qn);
  UA_NodeId_clear(&id);
  UA_QualifiedName_clear(&qn);
  if (sc)
    return PyErr_StatusCode(sc);
  Py_RETURN_NONE;
}

PyObject *pyServer_get_session_roles(PyObject *obj, PyObject *args) {
  PyServer *self = (PyServer *)obj;
  PyObject *sid;
  UA_NodeId id;
  size_t size = 0;
  UA_QualifiedName *names = NULL;
  if (!PyArg_ParseTuple(args, "O", &sid) ||
      extract_nodeid(sid, &id, &self->nsMapPy2UA, custom_types(self)) < 0)
    return NULL;
  UA_StatusCode sc =
      UA_Server_getSessionRoleNames(self->server, id, &size, &names);
  UA_NodeId_clear(&id);
  if (sc)
    return PyErr_StatusCode(sc);
  PyObject *out = PyList_New((Py_ssize_t)size);
  for (size_t i = 0; out && i < size; i++)
    PyList_SET_ITEM(
        out, (Py_ssize_t)i,
        UA2PY(&names[i], &UA_TYPES[UA_TYPES_QUALIFIEDNAME], &self->nsMapPy2UA));
  UA_Array_delete(names, size, &UA_TYPES[UA_TYPES_QUALIFIEDNAME]);
  return out;
}

PyObject *pyServer_set_session_roles(PyObject *obj, PyObject *args) {
  PyServer *self = (PyServer *)obj;
  PyObject *sid, *roles;
  UA_NodeId id, *ids = NULL;
  size_t size = 0;
  if (!PyArg_ParseTuple(args, "OO", &sid, &roles) ||
      extract_nodeid(sid, &id, &self->nsMapPy2UA, custom_types(self)) < 0)
    return NULL;
  if (convert_array(self, roles, &UA_TYPES[UA_TYPES_NODEID], (void **)&ids,
                    &size) < 0) {
    UA_NodeId_clear(&id);
    return NULL;
  }
  UA_Variant v;
  UA_Variant_init(&v);
  UA_Variant_setArray(&v, ids, size, &UA_TYPES[UA_TYPES_NODEID]);
  UA_StatusCode sc = UA_Server_setSessionAttribute(
      self->server, &id, UA_QUALIFIEDNAME(0, "roles"), &v);
  v.data = NULL;
  UA_Array_delete(ids, size, &UA_TYPES[UA_TYPES_NODEID]);
  UA_NodeId_clear(&id);
  if (sc)
    return PyErr_StatusCode(sc);
  Py_RETURN_NONE;
}

static int parse_role(PyServer *self, PyObject *args, UA_Role *role) {
  PyObject *id, *name, *identities, *apps, *ends;
  int appx, endx;
  if (!PyArg_ParseTuple(args, "OOOOpOp", &id, &name, &identities, &apps, &appx,
                        &ends, &endx))
    return -1;
  return convert_role(self, id, name, identities, apps, appx, ends, endx, role);
}

PyObject *pyServer_add_role(PyObject *obj, PyObject *args) {
  PyServer *self = (PyServer *)obj;
  UA_Role role;
  UA_NodeId out;
  UA_NodeId_init(&out);
  if (parse_role(self, args, &role) < 0)
    return NULL;
  UA_StatusCode sc = UA_Server_addRole(self->server, &role, &out);
  UA_Role_clear(&role);
  if (sc)
    return PyErr_StatusCode(sc);
  PyObject *py = UA2PY(&out, &UA_TYPES[UA_TYPES_NODEID], &self->nsMapPy2UA);
  UA_NodeId_clear(&out);
  return py;
}
PyObject *pyServer_update_role(PyObject *obj, PyObject *args) {
  PyServer *self = (PyServer *)obj;
  UA_Role role;
  if (parse_role(self, args, &role) < 0)
    return NULL;
  UA_StatusCode sc = UA_Server_updateRole(self->server, &role);
  UA_Role_clear(&role);
  if (sc)
    return PyErr_StatusCode(sc);
  Py_RETURN_NONE;
}
PyObject *pyServer_remove_role(PyObject *obj, PyObject *args) {
  PyServer *self = (PyServer *)obj;
  PyObject *name;
  UA_QualifiedName qn;
  if (!PyArg_ParseTuple(args, "O", &name) ||
      extract_qualifiedname(name, &qn, &self->nsMapPy2UA, custom_types(self)) <
          0)
    return NULL;
  UA_StatusCode sc = UA_Server_removeRole(self->server, qn);
  UA_QualifiedName_clear(&qn);
  if (sc)
    return PyErr_StatusCode(sc);
  Py_RETURN_NONE;
}
PyObject *pyServer_get_role(PyObject *obj, PyObject *args) {
  PyServer *self = (PyServer *)obj;
  PyObject *key;
  int byid;
  UA_Role role;
  UA_Role_init(&role);
  if (!PyArg_ParseTuple(args, "Op", &key, &byid))
    return NULL;
  UA_StatusCode sc;
  if (byid) {
    UA_NodeId id;
    if (extract_nodeid(key, &id, &self->nsMapPy2UA, custom_types(self)) < 0)
      return NULL;
    sc = UA_Server_getRoleById(self->server, id, &role);
    UA_NodeId_clear(&id);
  } else {
    UA_QualifiedName qn;
    if (extract_qualifiedname(key, &qn, &self->nsMapPy2UA, custom_types(self)) <
        0)
      return NULL;
    sc = UA_Server_getRole(self->server, qn, &role);
    UA_QualifiedName_clear(&qn);
  }
  if (sc)
    return PyErr_StatusCode(sc);
  PyObject *out = role_to_dict(self, &role);
  UA_Role_clear(&role);
  return out;
}
PyObject *pyServer_get_roles(PyObject *obj, PyObject *args) {
  (void)args;
  PyServer *self = (PyServer *)obj;
  size_t size = 0;
  UA_QualifiedName *names = NULL;
  UA_StatusCode sc = UA_Server_getRoles(self->server, &size, &names);
  if (sc)
    return PyErr_StatusCode(sc);
  PyObject *out = PyList_New((Py_ssize_t)size);
  for (size_t i = 0; out && i < size; i++)
    PyList_SET_ITEM(
        out, (Py_ssize_t)i,
        UA2PY(&names[i], &UA_TYPES[UA_TYPES_QUALIFIEDNAME], &self->nsMapPy2UA));
  UA_Array_delete(names, size, &UA_TYPES[UA_TYPES_QUALIFIEDNAME]);
  return out;
}

static int node_and_role(PyServer *self, PyObject *node, PyObject *role,
                         UA_NodeId *n, UA_NodeId *r) {
  if (extract_nodeid(node, n, &self->nsMapPy2UA, custom_types(self)) < 0)
    return -1;
  if (extract_nodeid(role, r, &self->nsMapPy2UA, custom_types(self)) < 0) {
    UA_NodeId_clear(n);
    return -1;
  }
  return 0;
}
PyObject *pyServer_set_node_role_permissions(PyObject *obj, PyObject *args) {
  PyServer *self = (PyServer *)obj;
  PyObject *node, *mapping;
  int recursive;
  UA_NodeId id;
  UA_RolePermission *p = NULL;
  size_t size = 0;
  if (!PyArg_ParseTuple(args, "OOp", &node, &mapping, &recursive) ||
      extract_nodeid(node, &id, &self->nsMapPy2UA, custom_types(self)) < 0)
    return NULL;
  if (convert_permissions(self, mapping, &p, &size) < 0) {
    UA_NodeId_clear(&id);
    return NULL;
  }
  UA_StatusCode sc = UA_Server_setNodeRolePermissions(self->server, id, size, p,
                                                      recursive, NULL);
  clear_permissions(p, size);
  UA_NodeId_clear(&id);
  if (sc)
    return PyErr_StatusCode(sc);
  Py_RETURN_NONE;
}
PyObject *pyServer_get_node_role_permissions(PyObject *obj, PyObject *args) {
  PyServer *self = (PyServer *)obj;
  PyObject *node;
  UA_NodeId id;
  UA_RolePermission *p = NULL;
  size_t size = 0;
  if (!PyArg_ParseTuple(args, "O", &node) ||
      extract_nodeid(node, &id, &self->nsMapPy2UA, custom_types(self)) < 0)
    return NULL;
  UA_StatusCode sc =
      UA_Server_getNodeRolePermissions(self->server, id, &size, &p);
  UA_NodeId_clear(&id);
  if (sc)
    return PyErr_StatusCode(sc);
  PyObject *out = permissions_to_dict(self, p, size);
  clear_permissions(p, size);
  return out;
}
PyObject *pyServer_remove_node_role_permissions(PyObject *obj, PyObject *args) {
  PyServer *self = (PyServer *)obj;
  PyObject *node;
  int rec;
  UA_NodeId id;
  if (!PyArg_ParseTuple(args, "Op", &node, &rec) ||
      extract_nodeid(node, &id, &self->nsMapPy2UA, custom_types(self)) < 0)
    return NULL;
  UA_StatusCode sc = UA_Server_removeNodeRolePermissions(self->server, id, rec);
  UA_NodeId_clear(&id);
  if (sc)
    return PyErr_StatusCode(sc);
  Py_RETURN_NONE;
}
PyObject *pyServer_add_role_permissions(PyObject *obj, PyObject *args) {
  PyServer *self = (PyServer *)obj;
  PyObject *node, *role;
  unsigned long perms;
  int overwrite, rec;
  UA_NodeId n, r;
  if (!PyArg_ParseTuple(args, "OOkpp", &node, &role, &perms, &overwrite,
                        &rec) ||
      node_and_role(self, node, role, &n, &r) < 0)
    return NULL;
  UA_StatusCode sc = UA_Server_addRolePermissions(
      self->server, n, r, (UA_PermissionType)perms, overwrite, rec);
  UA_NodeId_clear(&n);
  UA_NodeId_clear(&r);
  if (sc)
    return PyErr_StatusCode(sc);
  Py_RETURN_NONE;
}
PyObject *pyServer_remove_role_permissions(PyObject *obj, PyObject *args) {
  PyServer *self = (PyServer *)obj;
  PyObject *node, *role;
  unsigned long perms;
  int rec;
  UA_NodeId n, r;
  if (!PyArg_ParseTuple(args, "OOkp", &node, &role, &perms, &rec) ||
      node_and_role(self, node, role, &n, &r) < 0)
    return NULL;
  UA_StatusCode sc = UA_Server_removeRolePermissions(
      self->server, n, r, (UA_PermissionType)perms, rec);
  UA_NodeId_clear(&n);
  UA_NodeId_clear(&r);
  if (sc)
    return PyErr_StatusCode(sc);
  Py_RETURN_NONE;
}
PyObject *pyServer_set_namespace_role_permissions(PyObject *obj,
                                                  PyObject *args) {
  PyServer *self = (PyServer *)obj;
  unsigned int ns;
  PyObject *mapping;
  UA_RolePermission *p = NULL;
  size_t size = 0;
  if (!PyArg_ParseTuple(args, "IO", &ns, &mapping) ||
      convert_permissions(self, mapping, &p, &size) < 0)
    return NULL;
  UA_StatusCode sc = UA_Server_setNamespaceDefaultRolePermissions(
      self->server, (UA_UInt16)ns, size, p);
  clear_permissions(p, size);
  if (sc)
    return PyErr_StatusCode(sc);
  Py_RETURN_NONE;
}
PyObject *pyServer_get_namespace_role_permissions(PyObject *obj,
                                                  PyObject *args) {
  PyServer *self = (PyServer *)obj;
  unsigned int ns;
  UA_RolePermission *p = NULL;
  size_t size = 0;
  if (!PyArg_ParseTuple(args, "I", &ns))
    return NULL;
  UA_StatusCode sc = UA_Server_getNamespaceDefaultRolePermissions(
      self->server, (UA_UInt16)ns, &size, &p);
  if (sc)
    return PyErr_StatusCode(sc);
  PyObject *out = permissions_to_dict(self, p, size);
  clear_permissions(p, size);
  return out;
}
PyObject *pyServer_set_all_permissions_for_anonymous(PyObject *obj,
                                                     PyObject *args) {
  PyServer *self = (PyServer *)obj;
  int enabled;
  if (!PyArg_ParseTuple(args, "p", &enabled))
    return NULL;
  UA_Server_getConfig(self->server)->allPermissionsForAnonymous = enabled;
  Py_RETURN_NONE;
}
