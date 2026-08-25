/* Copyright 2026 (c) o6 Automation GmbH */
#include "../types_internal.h"
#include "server.h"
#include "server_services_util.h"

#ifndef UA_ENABLE_SUBSCRIPTIONS_EVENTS
#error "o6 server support requires open62541 event subscriptions"
#endif

static const UA_DataTypeArray *event_custom_types(PyServer *self) {
  return UA_Server_getConfig(self->server)->customDataTypes;
}

static int event_fields_from_mapping(PyServer *self, PyObject *mapping,
                                     UA_KeyValueMap *fields) {
  PyObject *items = PyMapping_Items(mapping);
  if (!items)
    return -1;

  Py_ssize_t count = PyList_GET_SIZE(items);
  for (Py_ssize_t i = 0; i < count; i++) {
    PyObject *pair = PyList_GET_ITEM(items, i);
    PyObject *py_key = PyTuple_GET_ITEM(pair, 0);
    PyObject *py_value = PyTuple_GET_ITEM(pair, 1);
    UA_QualifiedName key;
    UA_QualifiedName_init(&key);
    if (PyUnicode_Check(py_key)) {
      key.namespaceIndex = 0;
      if (Unicode2String(py_key, &key.name) != UA_STATUSCODE_GOOD) {
        Py_DECREF(items);
        return -1;
      }
    } else if (extract_qualifiedname(py_key, &key, &self->nsMapPy2UA,
                                     event_custom_types(self)) < 0) {
      Py_DECREF(items);
      return -1;
    }

    UA_Variant value;
    UA_Variant_init(&value);
    if (!PY2UA(py_value, &value, &UA_TYPES[UA_TYPES_VARIANT], &self->nsMapPy2UA,
               event_custom_types(self))) {
      UA_QualifiedName_clear(&key);
      Py_DECREF(items);
      return -1;
    }
    UA_StatusCode sc = UA_KeyValueMap_set(fields, key, &value);
    UA_Variant_clear(&value);
    if (sc != UA_STATUSCODE_GOOD) {
      UA_QualifiedName_clear(&key);
      Py_DECREF(items);
      PyErr_StatusCode(sc);
      return -1;
    }
  }
  Py_DECREF(items);
  return 0;
}

PyObject *pyServer_emit_event(PyObject *obj, PyObject *args) {
  PyServer *self = (PyServer *)obj;
  PyObject *py_source;
  PyObject *py_type;
  unsigned int severity;
  PyObject *py_message;
  PyObject *py_fields;
  PyObject *py_payload_source;
  if (!PyArg_ParseTuple(args, "OOIOOO", &py_source, &py_type, &severity,
                        &py_message, &py_fields, &py_payload_source))
    return NULL;

  UA_NodeId source;
  UA_NodeId type;
  UA_LocalizedText message;
  UA_NodeId_init(&source);
  UA_NodeId_init(&type);
  UA_LocalizedText_init(&message);
  if (extract_nodeid(py_source, &source, &self->nsMapPy2UA,
                     event_custom_types(self)) < 0 ||
      extract_nodeid(py_type, &type, &self->nsMapPy2UA,
                     event_custom_types(self)) < 0 ||
      !PY2UA(py_message, &message, &UA_TYPES[UA_TYPES_LOCALIZEDTEXT],
             &self->nsMapPy2UA, event_custom_types(self))) {
    UA_NodeId_clear(&source);
    UA_NodeId_clear(&type);
    UA_LocalizedText_clear(&message);
    return NULL;
  }

  UA_KeyValueMap fields = UA_KEYVALUEMAP_NULL;
  if (event_fields_from_mapping(self, py_fields, &fields) < 0) {
    UA_NodeId_clear(&source);
    UA_NodeId_clear(&type);
    UA_LocalizedText_clear(&message);
    UA_KeyValueMap_clear(&fields);
    return NULL;
  }

  UA_NodeId payload_source;
  UA_NodeId_init(&payload_source);
  const UA_NodeId *payload_source_ptr = NULL;
  if (py_payload_source != Py_None) {
    if (extract_nodeid(py_payload_source, &payload_source, &self->nsMapPy2UA,
                       event_custom_types(self)) < 0) {
      UA_NodeId_clear(&source);
      UA_NodeId_clear(&type);
      UA_LocalizedText_clear(&message);
      UA_KeyValueMap_clear(&fields);
      return NULL;
    }
    payload_source_ptr = &payload_source;
  }

  UA_ByteString event_id;
  UA_ByteString_init(&event_id);
  UA_StatusCode sc =
      UA_Server_createEvent(self->server, source, type, (UA_UInt16)severity,
                            message, &fields, payload_source_ptr, &event_id);
  UA_NodeId_clear(&source);
  UA_NodeId_clear(&type);
  UA_LocalizedText_clear(&message);
  UA_NodeId_clear(&payload_source);
  UA_KeyValueMap_clear(&fields);
  if (sc != UA_STATUSCODE_GOOD) {
    UA_ByteString_clear(&event_id);
    return PyErr_StatusCode(sc);
  }

  PyObject *out = PyBytes_FromStringAndSize((const char *)event_id.data,
                                            (Py_ssize_t)event_id.length);
  UA_ByteString_clear(&event_id);
  return out;
}
