/* Copyright 2026 (c) o6 Automation GmbH */
#include "./services_subscriptions.h"

MonitoredItemBundle *
monitoredItemBundle_new(PyClient *pyClient,
                        PyServer *pyServer,
                        UA_Server *server,
                        PyObject *notification_cb,
                        PyObject *context,
                        PyObject *deleted_cb) {
    MonitoredItemBundle *bundle =
        (MonitoredItemBundle *)UA_calloc(1, sizeof(MonitoredItemBundle));
    if (!bundle) {
        PyErr_NoMemory();
        return NULL;
    }

    bundle->pyClient = pyClient;
    bundle->pyServer = pyServer;
    bundle->server = server;

    bundle->notification_cb = notification_cb;
    bundle->context = context;
    bundle->deleted_cb = deleted_cb;

    if (pyServer) {
        if (pyServer_own_callback_ref(pyServer, notification_cb) < 0 ||
            pyServer_own_callback_ref(pyServer, context) < 0 ||
            pyServer_own_callback_ref(pyServer, deleted_cb) < 0) {
            pyServer_release_callback_ref(pyServer, notification_cb);
            pyServer_release_callback_ref(pyServer, context);
            pyServer_release_callback_ref(pyServer, deleted_cb);
            UA_free(bundle);
            return NULL;
        }
    } else {
        Py_XINCREF(notification_cb);
        Py_XINCREF(context);
        Py_XINCREF(deleted_cb);
    }

    return bundle;
}

void
monitoredItemBundle_free(MonitoredItemBundle *bundle) {
    if (!bundle)
        return;

    if (bundle->pyServer) {
        pyServer_release_callback_ref(bundle->pyServer, bundle->notification_cb);
        pyServer_release_callback_ref(bundle->pyServer, bundle->context);
        pyServer_release_callback_ref(bundle->pyServer, bundle->deleted_cb);
    } else {
        Py_XDECREF(bundle->notification_cb);
        Py_XDECREF(bundle->context);
        Py_XDECREF(bundle->deleted_cb);
    }
    UA_free(bundle);
}


/* Convert a UA_KeyValueMap to a Python dict {str: Any}.
 * Returns a new reference, or NULL on error. */
PyObject *
keyValueMap_to_pydict(const UA_KeyValueMap *payload,
                      const UA_NamespaceMapping *nsMapping) {
    PyObject *pyDict = PyDict_New();
    if (!pyDict)
        return NULL;
    for (size_t i = 0; i < payload->mapSize; i++) {
        UA_QualifiedName *key = &payload->map[i].key;
        PyObject *pyKey = PyUnicode_FromStringAndSize(
            (char *)key->name.data, (Py_ssize_t)key->name.length);
        if (!pyKey) {
            Py_DECREF(pyDict);
            return NULL;
        }
        PyObject *pyVal = UA2PY((void *)&payload->map[i].value,
                                &UA_TYPES[UA_TYPES_VARIANT],
                                nsMapping);
        if (!pyVal) {
            Py_DECREF(pyKey);
            Py_DECREF(pyDict);
            return NULL;
        }
        int rc = PyDict_SetItem(pyDict, pyKey, pyVal);
        Py_DECREF(pyKey);
        Py_DECREF(pyVal);
        if (rc < 0) {
            Py_DECREF(pyDict);
            return NULL;
        }
    }
    return pyDict;
}

void
monitoredItemBundle_remove_from_list(struct MonitoredItemBundleList *list,
                                     UA_UInt32 id,
                                     UA_Server *server) {
    MonitoredItemBundle *b, *tmp;
    SLIST_FOREACH_SAFE(b, list, entry, tmp) {
        if (b->monitoredItemId == id && b->server == server) {
            SLIST_REMOVE(list, b, MonitoredItemBundle, entry);
            monitoredItemBundle_free(b);
            return;
        }
    }
}

void
monitoredItemBundle_clear_server_from_list(struct MonitoredItemBundleList *list,
                                           UA_Server *server) {
    MonitoredItemBundle *b, *tmp;
    SLIST_FOREACH_SAFE(b, list, entry, tmp) {
        if (b->server == server) {
            SLIST_REMOVE(list, b, MonitoredItemBundle, entry);
            monitoredItemBundle_free(b);
        }
    }
}

void
handleServerCallbackResult(UA_Server *server, PyObject *result) {
    if (!result) {
        PyErr_Print();
        return;
    }

    if (PyCoro_CheckExact(result)) {
        UA_ServerConfig *config = UA_Server_getConfig(server);
        if (config->eventLoop) {
            AsyncIOLoop *el = (AsyncIOLoop *)config->eventLoop;
            if (!el->tearingDown) {
                PyObject *task =
                    PyObject_CallMethod(el->pyLoop, "create_task", "O", result);
                Py_XDECREF(task);
            }
        }
    }

    Py_DECREF(result);
}

void
callPyCallbackOneArg(PyObject *callback, PyObject *arg) {
    PyObject *result = PyObject_CallOneArg(callback, arg);
    if (!result) {
        PyErr_Print();
        PyErr_Clear();
        return;
    }
    Py_DECREF(result);
}

void
callPyCallbackTwoArgs(PyObject *callback, PyObject *arg1, PyObject *arg2) {
    PyObject *result = PyObject_CallFunctionObjArgs(callback, arg1, arg2, NULL);
    if (!result) {
        PyErr_Print();
        PyErr_Clear();
        return;
    }
    Py_DECREF(result);
}
