/* Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner) */
#include "ua_extension_namespacemapping.h"
#include <string.h>

static UA_StatusCode
grow_uri_array(UA_String **arr, size_t *size, size_t needed) {
    if(*size >= needed)
        return UA_STATUSCODE_GOOD;
    /* UA_Array_resize zero-inits new slots via UA_init -> UA_STRING_NULL. */
    return UA_Array_resize((void **)arr, size, needed, &UA_TYPES[UA_TYPES_STRING]);
}

static UA_StatusCode
grow_u16_identity_array(UA_UInt16 **arr, size_t *size, size_t needed) {
    if(*size >= needed)
        return UA_STATUSCODE_GOOD;
    UA_UInt16 *grown = (UA_UInt16 *)UA_realloc(*arr, needed * sizeof(UA_UInt16));
    if(!grown)
        return UA_STATUSCODE_BADOUTOFMEMORY;
    for(size_t i = *size; i < needed; i++)
        grown[i] = (UA_UInt16)i;
    *arr = grown;
    *size = needed;
    return UA_STATUSCODE_GOOD;
}

UA_StatusCode
ua_extension_namespace_mapping_set(UA_NamespaceMapping *nm,
                                   UA_String uri,
                                   UA_UInt16 python_idx,
                                   UA_UInt16 ua_idx) {
    UA_StatusCode st = grow_uri_array(&nm->namespaceUris, &nm->namespaceUrisSize,
                                      (size_t)python_idx + 1);
    if(st != UA_STATUSCODE_GOOD)
        return st;

    st = grow_u16_identity_array(&nm->local2remote, &nm->local2remoteSize,
                                 (size_t)python_idx + 1);
    if(st != UA_STATUSCODE_GOOD)
        return st;

    st = grow_u16_identity_array(&nm->remote2local, &nm->remote2localSize,
                                 (size_t)ua_idx + 1);
    if(st != UA_STATUSCODE_GOOD)
        return st;

    UA_String_clear(&nm->namespaceUris[python_idx]);
    st = UA_String_copy(&uri, &nm->namespaceUris[python_idx]);
    if(st != UA_STATUSCODE_GOOD)
        return st;

    nm->local2remote[python_idx] = ua_idx;
    nm->remote2local[ua_idx] = python_idx;

    return UA_STATUSCODE_GOOD;
}

UA_UInt16
UA_NamespaceMapping_Python2UA(const UA_NamespaceMapping *nm, UA_UInt16 python_idx) {
    /* Explicitly mapped python-side index */
    if(python_idx < nm->namespaceUrisSize &&
       nm->namespaceUris[python_idx].length > 0)
        return UA_NamespaceMapping_local2Remote(nm, python_idx);

    /* Resolve scoped/versioned aliases through their canonical Python
     * namespace module. All callers enter from Python with the GIL held. */
    assertGIL();
    PyObject *namespace = o6_namespace_module(python_idx);
    if(namespace && !PyLong_Check(namespace)) {
        PyObject *uriObject = PyObject_GetAttrString(namespace, "uri");
        if(uriObject) {
            Py_ssize_t length;
            const char *data = PyUnicode_AsUTF8AndSize(uriObject, &length);
            if(data) {
                UA_String uri = {(size_t)length, (UA_Byte *)(uintptr_t)data};
                UA_UInt16 mapped;
                if(UA_NamespaceMapping_uri2Index(nm, uri, &mapped) == UA_STATUSCODE_GOOD) {
                    Py_DECREF(uriObject);
                    Py_DECREF(namespace);
                    return UA_NamespaceMapping_local2Remote(nm, mapped);
                }
            }
            Py_DECREF(uriObject);
        }
    }
    Py_XDECREF(namespace);
    PyErr_Clear();
    return UA_NamespaceMapping_local2Remote(nm, python_idx);
}

UA_UInt16
UA_NamespaceMapping_UA2Python(const UA_NamespaceMapping *nm, UA_UInt16 ua_idx) {
    return UA_NamespaceMapping_remote2Local(nm, ua_idx);
}
