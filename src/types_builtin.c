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

#include "pytypedefs.h"
#include "types_internal.h"

PyObject *
pyUABuiltin_str(PyObject *self) {
    PyTypeObject *pyType = Py_TYPE(self);
    const UA_DataType *uaType = PY2UAType(pyType);
    PyUABuiltin *data = (PyUABuiltin*)self;
    UA_String buf = UA_STRING_NULL;
    switch(uaType->typeKind) {
    case UA_DATATYPEKIND_NODEID:
        UA_NodeId_print(&data->nodeId, &buf); break;
    case UA_DATATYPEKIND_DATETIME:
        UA_print(&data->dateTime, &UA_TYPES[UA_TYPES_DATETIME], &buf); break;
    case UA_DATATYPEKIND_EXPANDEDNODEID:
        UA_ExpandedNodeId_print(&data->expandedNodeId, &buf); break;
    case UA_DATATYPEKIND_QUALIFIEDNAME:
        UA_QualifiedName_print(&data->qualifiedName, &buf); break;
    case UA_DATATYPEKIND_LOCALIZEDTEXT: {
        // No locale
        if(data->localizedText.locale.length == 0)
            return PyUnicode_FromStringAndSize((char*)data->localizedText.text.data,
                                               data->localizedText.text.length);
        // Put together as 'locale:text'
        PyObject *locale =
            PyUnicode_FromStringAndSize((char*)data->localizedText.locale.data,
                                        data->localizedText.locale.length);
        PyObject *text =
            PyUnicode_FromStringAndSize((char*)data->localizedText.text.data,
                                        data->localizedText.text.length);
        if(!text || !locale) {
            Py_XDECREF(text);
            Py_XDECREF(locale);
            return NULL;
        }
        PyObject *out = PyUnicode_FromFormat("%S:%S", locale, text);
        Py_XDECREF(text);
        Py_XDECREF(locale);
        return out;
    }
    case UA_DATATYPEKIND_STATUSCODE: // Only the StatusCode name
        return PyUnicode_FromString(UA_StatusCode_name(data->statusCode));
    default:
        return PyUnicode_FromString("");
    }

    // Remove surrounding parentheses
    UA_String out = buf;
    if(out.length >= 2) {
        if(out.data[0] == '"') {
            out.data++;
            out.length--;
        }
        if(out.data[out.length-1] == '"')
            out.length--;
    }
    PyObject *str = PyUnicode_FromStringAndSize((char*)out.data, out.length);
    UA_String_clear(&buf);
    return str;
}

void
pyUABuiltin_dealloc(PyObject *self) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    PyTypeObject *pyType = Py_TYPE(self);
    const UA_DataType *uaType = PY2UAType(pyType);
    UA_clear(&data->statusCode, uaType);
    Py_TYPE(self)->tp_free(self);
}

PyObject *
pyUABuiltin_richcompare(PyObject *self, PyObject *other, int op) {
    if(op != Py_EQ) {
        Py_INCREF(Py_NotImplemented);
        return Py_NotImplemented;
    }
    PyTypeObject *type = Py_TYPE(self);
    PyTypeObject *type2 = Py_TYPE(other);
    if(type != type2)
        return Py_False;
    const UA_DataType *uaType = PY2UAType(type);
    PyUABuiltin *d1 = (PyUABuiltin*)self;
    PyUABuiltin *d2 = (PyUABuiltin*)other;
    return UA_equal(&d1->statusCode, &d2->statusCode, uaType) ? Py_True : Py_False;
}

/************/
/* DateTime */
/************/

int
pyDateTime_init(PyObject *self, PyObject *args, PyObject *kwds) {
    if(PyTuple_Size(args) > 1 || (kwds && PyDict_Size(kwds) != 0)) {
        PyErr_SetString(PyExc_TypeError, "DateTime takes a single argument");
        return -1;
    }

    PyUABuiltin *data = (PyUABuiltin*)self;
    if(PyTuple_Size(args) == 0) {
        data->dateTime = 0;
        return 0;
    }

    PyObject *res = PY2UA_datetime(PyTuple_GetItem(args, 0), &data->dateTime);
    return (res) ? 0 : -1;
}

PyObject *
pyDateTime_richcompare(PyObject *self, PyObject *other, int op) {
    if(Py_TYPE(other) != pyUADateTime)
        return Py_False;
    UA_DateTime d1 = ((PyUABuiltin*)self)->dateTime;
    UA_DateTime d2 = ((PyUABuiltin*)other)->dateTime;
    switch(op) {
    case Py_LT: return d1 < d2 ? Py_True : Py_False;
    case Py_LE: return d1 <= d2 ? Py_True : Py_False;
    case Py_EQ: return d1 == d2 ? Py_True : Py_False;
    case Py_NE: return d1 != d2 ? Py_True : Py_False;
    case Py_GT: return d1 > d2 ? Py_True : Py_False;
    case Py_GE: return d1 >= d2 ? Py_True : Py_False;
    default: break;
    }
    return Py_False;
}

// Convert to int
PyObject *
pyDateTime_int(PyObject *self) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    return PyLong_FromLongLong(data->dateTime);
}

/**************/
/* StatusCode */
/**************/

int
pyStatusCode_init(PyObject *self, PyObject *args, PyObject *kwds) {
    if(PyTuple_Size(args) > 1 || (kwds && PyDict_Size(kwds) != 0)) {
        PyErr_SetString(PyExc_TypeError, "StatusCode takes a single integer argument");
        return -1;
    }

    PyUABuiltin *data = (PyUABuiltin*)self;
    if(PyTuple_Size(args) == 0) {
        data->statusCode = UA_STATUSCODE_GOOD;
        return 0;
    }

    PyObject *res = PY2UA_statuscode(PyTuple_GetItem(args, 0), &data->statusCode);
    return (res) ? 0 : -1;
}

PyObject *
pyStatusCode_get_code(PyObject *self, void *closure) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    return PyLong_FromUnsignedLong(data->statusCode);
}

PyObject *
pyStatusCode_get_name(PyObject *self, void *closure) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    return PyUnicode_FromString(UA_StatusCode_name(data->statusCode));
}

PyGetSetDef pyStatusCode_getsets[] = {
    {"code", pyStatusCode_get_code, NULL, "Integer code", NULL},
    {"symbol", pyStatusCode_get_name, NULL, "Human-readable description", NULL},
    {NULL}
};

PyObject *
pyStatusCode_repr(PyObject *self) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    PyTypeObject *type = Py_TYPE(self);
    return PyUnicode_FromFormat("%s(code=0x%02x, symbol=%s)", type->tp_name,
                                data->statusCode, UA_StatusCode_name(data->statusCode));
}

// Convert to int
PyObject *
pyStatusCode_int(PyObject *self) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    return PyLong_FromUnsignedLong(data->statusCode);
}

/**********/
/* NodeId */
/**********/

// Accepts either:
//   NodeId(6)                  - ns=0 numeric identifier (shorthand)
//   NodeId("ns=1;i=5")         - parse string
//   NodeId(existing_nodeid)    - copy
//   NodeId(obj._nodeid)        - Object with member _nodeid
//   NodeId(ns=1, i=5)          - numeric identifier
//   NodeId(ns=1, s="Temp")     - string identifier
//   NodeId(ns=1, b=b"...")     - bytestring identifier
//   NodeId(ns=1, g=uuid_obj)   - GUID identifier
int
pyNodeId_init(PyObject *self, PyObject *args, PyObject *kwds) {
    PyUABuiltin *data = (PyUABuiltin*)self;

    /* Keyword-argument form */
    if(kwds && PyDict_Size(kwds) != 0) {
        if(PyTuple_Size(args) != 0) {
            PyErr_SetString(PyExc_TypeError,
                            "NodeId: positional and keyword arguments cannot be mixed");
            return -1;
        }

        static char *kwlist[] = {"ns", "i", "s", "b", "g", NULL};
        PyObject *ns_obj = NULL, *i_obj = NULL, *s_obj = NULL,
                 *b_obj = NULL, *g_obj = NULL;
        if(!PyArg_ParseTupleAndKeywords(args, kwds, "|OOOOO", kwlist,
                                        &ns_obj, &i_obj, &s_obj, &b_obj, &g_obj))
            return -1;

        UA_UInt16 ns = 0;
        if(ns_obj) {
            long v = PyLong_AsLong(ns_obj);
            if(v == -1 && PyErr_Occurred()) return -1;
            ns = (UA_UInt16)v;
        }

        /* Exactly one of i/s/b/g must be given */
        int given = (i_obj != NULL) + (s_obj != NULL) + (b_obj != NULL) + (g_obj != NULL);
        if(given != 1) {
            PyErr_SetString(PyExc_TypeError,
                            "NodeId: exactly one of 'i', 's', 'b', or 'g' must be given");
            return -1;
        }

        UA_NodeId tmp;
        if(i_obj) {
            unsigned long id = PyLong_AsUnsignedLong(i_obj);
            if(id == (unsigned long)-1 && PyErr_Occurred()) return -1;
            tmp = UA_NODEID_NUMERIC(ns, (UA_UInt32)id);
        } else if(s_obj) {
            if(!PyUnicode_Check(s_obj)) {
                PyErr_SetString(PyExc_TypeError, "NodeId 's' must be a string");
                return -1;
            }
            const char *str = PyUnicode_AsUTF8(s_obj);
            if(!str) return -1;
            tmp = UA_NODEID_STRING_ALLOC(ns, str);
        } else if(b_obj) {
            if(!PyBytes_Check(b_obj)) {
                PyErr_SetString(PyExc_TypeError, "NodeId 'b' must be bytes");
                return -1;
            }
            char *buf; Py_ssize_t len;
            if(PyBytes_AsStringAndSize(b_obj, &buf, &len) < 0) return -1;
            UA_ByteString bs = {(size_t)len, (UA_Byte*)buf};
            tmp = UA_NODEID_NUMERIC(ns, 0); /* init */
            tmp.identifierType = UA_NODEIDTYPE_BYTESTRING;
            UA_ByteString_copy(&bs, &tmp.identifier.byteString);
        } else { /* g_obj */
            UA_Guid guid;
            PyObject *res = PY2UA_guid(g_obj, &guid);
            if(!res) return -1;
            tmp = UA_NODEID_GUID(ns, guid);
        }

        UA_NodeId_clear(&data->nodeId);
        data->nodeId = tmp;
        return 0;
    }

    /* Positional-argument form: 0 or 1 args */
    if(PyTuple_Size(args) > 1) {
        PyErr_SetString(PyExc_TypeError, "Too many arguments for NodeId");
        return -1;
    }

    if(PyTuple_Size(args) == 0) {
        UA_NodeId_clear(&data->nodeId);
        return 0;
    }

    PyObject *v = PyTuple_GetItem(args, 0); /* Does not increase refcount */

    /* None argument -> ns=0;i=0 */
    if(v == Py_None) {
        UA_NodeId_clear(&data->nodeId);
        return 0;
    }

    /* TypeObject. Check if this is a known DataType */
    UA_NodeId tmp;
    if(PyType_Check(v)) {
        const UA_DataType *dt = PY2UAType((PyTypeObject*)v);
        if(dt) {
            UA_StatusCode r = UA_NodeId_copy(&dt->typeId, &tmp);
            if(r != UA_STATUSCODE_GOOD) {
                PyErr_NoMemory();
                return -1;
            }
            UA_NodeId_clear(&data->nodeId);
            data->nodeId = tmp;
            return 0;
        }
    }

    /* For objects with a _nodeid member, use that */
    int has_attr = PyObject_HasAttrString(v, "_nodeid");
    if(has_attr)
        v = PyObject_GetAttrString(v, "_nodeid");

    /* Try to cast into a NodeId */
    PyObject *res = PY2UA_nodeid(v, &tmp);
    if(has_attr)
        Py_DECREF(v);
    if(!res)
        return -1;
    UA_NodeId_clear(&data->nodeId);
    data->nodeId = tmp;
    return 0;
}

/* Getter methods for the attributes "ns" and "id" */
PyObject *
pyNodeId_get_ns(PyObject *self, void *closure) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    return PyLong_FromUnsignedLong(data->nodeId.namespaceIndex);
}

PyObject *
_pyNodeId_get_id(UA_NodeId *id) {
    switch(id->identifierType) {
    case UA_NODEIDTYPE_NUMERIC:
        return PyLong_FromUnsignedLong(id->identifier.numeric);
    case UA_NODEIDTYPE_STRING:
        return PyUnicode_FromStringAndSize((char*)id->identifier.string.data,
                                           id->identifier.string.length);
    case UA_NODEIDTYPE_BYTESTRING:
        return PyBytes_FromStringAndSize((char*)id->identifier.string.data,
                                         id->identifier.string.length);
    case UA_NODEIDTYPE_GUID:
        return UA2PY_guid(&id->identifier.guid);
    default:
        PyErr_SetString(PyExc_TypeError, "Unknown NodeId type");
        return NULL;
    }
}

PyObject *
pyNodeId_get_id(PyObject *self, void *closure) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    return _pyNodeId_get_id(&data->nodeId);
}

PyGetSetDef pyNodeId_getsets[] = {
    {"ns", pyNodeId_get_ns, NULL, "NamespaceIndex", NULL},
    {"id", pyNodeId_get_id, NULL, "Identifier", NULL},
    {NULL}
};

Py_hash_t
pyNodeId_hash(PyObject *self) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    UA_UInt32 h = UA_NodeId_hash(&data->nodeId);
    return (Py_hash_t)(h>>1); /* Return a non-negative number */
}

/******************/
/* ExpandedNodeId */
/******************/

// Accepts a single string argument and parses it into a NodeId
// TODO: Accept key-value arguments
int
pyExpandedNodeId_init(PyObject *self, PyObject *args, PyObject *kwds) {
    if(PyTuple_Size(args) > 1 || (kwds && PyDict_Size(kwds) != 0)) {
        PyErr_SetString(PyExc_TypeError, "Too many arguments for ExpandedNodeId");
        return -1;
    }

    PyUABuiltin *data = (PyUABuiltin*)self;
    if(PyTuple_Size(args) == 0) {
        UA_ExpandedNodeId_clear(&data->expandedNodeId);
        return 0;
    }

    UA_ExpandedNodeId tmp;
    PyObject *res = PY2UA_expandednodeid(PyTuple_GetItem(args, 0), &tmp);
    if(!res)
        return -1;
    UA_ExpandedNodeId_clear(&data->expandedNodeId);
    data->expandedNodeId = tmp;
    return 0;
}

PyObject *
pyExpandedNodeId_get_ns(PyObject *self, void *closure) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    return PyLong_FromUnsignedLong(data->expandedNodeId.nodeId.namespaceIndex);
}

PyObject *
pyExpandedNodeId_get_id(PyObject *self, void *closure) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    return _pyNodeId_get_id(&data->expandedNodeId.nodeId);
}

PyObject *
pyExpandedNodeId_get_uri(PyObject *self, void *closure) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    return PyUnicode_FromStringAndSize((char*)data->expandedNodeId.namespaceUri.data,
                                       data->expandedNodeId.namespaceUri.length);
}

PyObject *
pyExpandedNodeId_get_svr(PyObject *self, void *closure) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    return PyLong_FromUnsignedLong(data->expandedNodeId.serverIndex);
}

PyGetSetDef pyExpandedNodeId_getsets[] = {
    {"ns", pyExpandedNodeId_get_ns, NULL, "Namespace Index", NULL},
    {"id", pyExpandedNodeId_get_id, NULL, "Identifier", NULL},
    {"nsu", pyExpandedNodeId_get_uri, NULL, "Namespace Uri", NULL},
    {"svr", pyExpandedNodeId_get_svr, NULL, "Server Index", NULL},
    {NULL}
};

Py_hash_t
pyExpandedNodeId_hash(PyObject *self) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    UA_UInt32 h = UA_ExpandedNodeId_hash(&data->expandedNodeId);
    return (Py_hash_t)(h>>1); /* Return a non-negative number */
}

/*******************/
/* ExtensionObject */
/*******************/

int
pyExtensionObject_init(PyObject *self, PyObject *args, PyObject *kwds) {
    Py_ssize_t argsSize = PyTuple_Size(args);
    if(argsSize < 0 || argsSize > 2) {
        PyErr_SetString(PyExc_TypeError, "Wrong number of arguments for ExtensionObject");
        return -1;
    }

    PyUABuiltin *data = (PyUABuiltin*)self;
    if(argsSize == 0) {
        UA_ExtensionObject_clear(&data->eo);
        return 0;
    }

    UA_ExtensionObject tmp;
    UA_ExtensionObject_init(&tmp);

    // One Argument
    PyObject *args0 = PyTuple_GetItem(args, 0);
    if(argsSize == 1) {
        // None
        if(args0 == Py_None) {
            UA_ExtensionObject_clear(&data->eo);
            return 0;
        }

        // Existing ExtensionObject
        if(Py_TYPE(args0) == pyUAExtensionObject) {
            PyObject *res = PY2UA_extensionobject(args0, &tmp);
            if(!res)
                return -1;
            UA_ExtensionObject_clear(&data->eo);
            data->eo = tmp;
            return 0;
        }

        // Initialize from a known OPC UA type — wrap as decoded ExtensionObject
        PyObject *res = PY2UA_extensionobject(args0, &tmp);
        if(!res) {
            PyErr_SetString(PyExc_TypeError,
                            "If only one argument is given, it must be an "
                            "ExtensionObject or an instance of a known "
                            "OPC UA data type");
            return -1;
        }
        UA_ExtensionObject_clear(&data->eo);
        data->eo = tmp;
        return 0;
    }

    // Two arguments
    assert(argsSize == 2);

    // First argument: type_id
    PyObject *success = PY2UA_nodeid(args0, &tmp.content.encoded.typeId);
    if(!success)
        return -1;

    // Second argument: body
    char *buf;
    Py_ssize_t size;
    PyObject *body = PyTuple_GetItem(args, 1);
    if(PyObject_IsInstance(body, (PyObject*)&PyBytes_Type)) {
        // Binary
        int res = PyBytes_AsStringAndSize(body, &buf, &size);
        if(res != 0)
            goto errout;
        tmp.encoding = UA_EXTENSIONOBJECT_ENCODED_BYTESTRING;
    } else if(PyObject_IsInstance(body, (PyObject*)&PyUnicode_Type)) {
        // XML
        buf = (char*)(uintptr_t)PyUnicode_AsUTF8AndSize(body, &size);
        if(size < 0)
            goto errout;
        tmp.encoding = UA_EXTENSIONOBJECT_ENCODED_XML;
    } else {
        goto errout;
    }
    UA_ByteString binary = {(size_t)size, (UA_Byte*)buf};
    UA_StatusCode rv = UA_ByteString_copy(&binary, &tmp.content.encoded.body);
    if(rv != UA_STATUSCODE_GOOD) {
        PyErr_NoMemory();
        goto errout;
    }

    UA_ExtensionObject_clear(&data->eo);
    data->eo = tmp;
    return 0;

 errout:
    UA_NodeId_clear(&tmp.content.encoded.typeId);
    return -1;
}

PyObject *
pyExtensionObject_get_typeId(PyObject *self, void *closure) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    if(data->eo.encoding == UA_EXTENSIONOBJECT_DECODED ||
       data->eo.encoding == UA_EXTENSIONOBJECT_DECODED_NODELETE) {
        const UA_DataType *type = data->eo.content.decoded.type;
        PyTypeObject *nIdType = pyUANodeId;
        PyUABuiltin *nId = (PyUABuiltin*)nIdType->tp_new(nIdType, NULL, NULL);
        if(!nId)
            return PyErr_NoMemory();
        UA_StatusCode res = UA_NodeId_copy(&type->typeId, &nId->nodeId);
        if(res != UA_STATUSCODE_GOOD) {
            Py_DECREF(nId);
            return PyErr_NoMemory();
        }
        return (PyObject*)nId;
    }
    if(data->eo.encoding != UA_EXTENSIONOBJECT_ENCODED_BYTESTRING &&
       data->eo.encoding != UA_EXTENSIONOBJECT_ENCODED_XML)
        return Py_None;
    return UA2PY(&data->eo.content.encoded.typeId, &UA_TYPES[UA_TYPES_NODEID]);
}

PyObject *
pyExtensionObject_get_body(PyObject *self, void *closure) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    if(data->eo.encoding == UA_EXTENSIONOBJECT_DECODED ||
       data->eo.encoding == UA_EXTENSIONOBJECT_DECODED_NODELETE) {
        return UA2PY(data->eo.content.decoded.data,
                     data->eo.content.decoded.type);
    }
    if(data->eo.encoding == UA_EXTENSIONOBJECT_ENCODED_BYTESTRING)
        return PyBytes_FromStringAndSize((char*)data->eo.content.encoded.body.data,
                                         data->eo.content.encoded.body.length);
    if(data->eo.encoding == UA_EXTENSIONOBJECT_ENCODED_XML)
        return PyUnicode_FromStringAndSize((char*)data->eo.content.encoded.body.data,
                                           data->eo.content.encoded.body.length);
    return Py_None;
}

PyGetSetDef pyExtensionObject_getsets[] = {
    {"type_id", pyExtensionObject_get_typeId, NULL, "NodeId of the datatype", NULL},
    {"body", pyExtensionObject_get_body, NULL, "Encoded value as binary or XML string", NULL},
    {NULL}
};

static PyObject *
pyUAExtensionObject_str_payload(PyObject *self) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    if(data->eo.encoding == UA_EXTENSIONOBJECT_ENCODED_NOBODY)
        return PyUnicode_FromString("None");

    PyObject *typeId = pyExtensionObject_get_typeId(self, NULL);
    PyObject *body = pyExtensionObject_get_body(self, NULL);
    if(!typeId || !body) {
        Py_XDECREF(typeId);
        Py_XDECREF(body);
        return NULL;
    }

    PyObject *out;
    if(typeId == Py_None)
        out = PyUnicode_FromFormat("type_id=None, body=%R", body);
    else
        out = PyUnicode_FromFormat("type_id='%S', body=%R", typeId, body);
    Py_XDECREF(typeId);
    Py_XDECREF(body);
    return out;
}

PyObject *
pyUAExtensionObject_str(PyObject *self) {
    PyObject *str = pyUAExtensionObject_str_payload(self);
    if(!str)
        return NULL;
    PyObject *result = PyUnicode_FromFormat("ExtensionObject(%U)", str);
    Py_DECREF(str);
    return result;
}

PyObject *
pyUAExtensionObject_repr(PyObject *self) {
    PyObject *str = pyUAExtensionObject_str_payload(self);
    if(!str)
        return NULL;
    PyObject *result = PyUnicode_FromFormat("%s(%U)", Py_TYPE(self)->tp_name, str);
    Py_DECREF(str);
    return result;
}

/*****************/
/* QualifiedName */
/*****************/

int
pyQualifiedName_init(PyObject *self, PyObject *args, PyObject *kwds) {
    Py_ssize_t nargs = PyTuple_Size(args);
    if(nargs > 2 || (kwds && PyDict_Size(kwds) != 0)) {
        PyErr_SetString(PyExc_TypeError,
                        "QualifiedName takes 0-2 positional arguments: "
                        "QualifiedName(), QualifiedName(name), or "
                        "QualifiedName(ns, name)");
        return -1;
    }

    PyUABuiltin *data = (PyUABuiltin*)self;
    if(nargs == 0) {
        UA_QualifiedName_clear(&data->qualifiedName);
        return 0;
    }

    if(nargs == 2) {
        /* QualifiedName(ns, name) */
        PyObject *nsArg = PyTuple_GetItem(args, 0);
        PyObject *nameArg = PyTuple_GetItem(args, 1);
        if(!PyLong_Check(nsArg) || !PyUnicode_Check(nameArg)) {
            PyErr_SetString(PyExc_TypeError,
                            "QualifiedName(ns, name) requires int and str arguments");
            return -1;
        }
        long ns = PyLong_AsLong(nsArg);
        if(ns < 0 || ns > UINT16_MAX) {
            PyErr_SetString(PyExc_ValueError,
                            "Namespace index must be between 0 and 65535");
            return -1;
        }
        UA_String nameStr;
        UA_StatusCode sc = Unicode2String(nameArg, &nameStr);
        if(sc != UA_STATUSCODE_GOOD) {
            PyErr_SetString(PyExc_TypeError, "Could not convert name string");
            return -1;
        }
        UA_QualifiedName_clear(&data->qualifiedName);
        data->qualifiedName.namespaceIndex = (UA_UInt16)ns;
        sc = UA_String_copy(&nameStr, &data->qualifiedName.name);
        if(sc != UA_STATUSCODE_GOOD) {
            PyErr_SetString(PyExc_RuntimeError, "Could not create QualifiedName");
            return -1;
        }
        return 0;
    }

    /* QualifiedName(name) - single string argument */
    UA_QualifiedName tmp;
    PyObject *res = PY2UA_qualifiedname(PyTuple_GetItem(args, 0), &tmp);
    if(!res)
        return -1;
    UA_QualifiedName_clear(&data->qualifiedName);
    data->qualifiedName = tmp;
    return 0;
}

PyObject *
pyQualifiedName_get_ns(PyObject *self, void *closure) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    return PyLong_FromUnsignedLong(data->qualifiedName.namespaceIndex);
}

PyObject *
pyQualifiedName_get_name(PyObject *self, void *closure) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    return PyUnicode_FromStringAndSize((char*)data->qualifiedName.name.data,
                                       data->qualifiedName.name.length);
}

PyGetSetDef pyQualifiedName_getsets[] = {
    {"ns", pyQualifiedName_get_ns, NULL, "Namespace Index", NULL},
    {"name", pyQualifiedName_get_name, NULL, "Name", NULL},
    {NULL}
};

/*****************/
/* LocalizedText */
/*****************/

int
pyLocalizedText_init(PyObject *self, PyObject *args, PyObject *kwds) {
    if(PyTuple_Size(args) > 2 || (kwds && PyDict_Size(kwds) != 0)) {
        PyErr_SetString(PyExc_TypeError, "LocalizedText takes 1-2 arguments: text and optional locale");
        return -1;
    }

    PyUABuiltin *data = (PyUABuiltin*)self;
    if(PyTuple_Size(args) == 0) {
        UA_LocalizedText_clear(&data->localizedText);
        return 0;
    }

    PyObject *textArg = PyTuple_GetItem(args, 0);
    
    // If first argument is already a LocalizedText, copy it
    if(Py_TYPE(textArg) == pyUALocalizedText) {
        UA_LocalizedText tmp;
        PyObject *res = PY2UA_localizedtext(textArg, &tmp);
        if(!res)
            return -1;
        UA_LocalizedText_clear(&data->localizedText);
        data->localizedText = tmp;
        return 0;
    }
    
    // Handle string input
    if(!PyUnicode_Check(textArg)) {
        PyErr_SetString(PyExc_TypeError, "First argument must be a string or LocalizedText");
        return -1;
    }

    UA_LocalizedText_init(&data->localizedText);
    
    // Single string argument: try to deconstruct 'locale:text'
    if(PyTuple_Size(args) == 1) {
        UA_String combined;
        UA_StatusCode res = Unicode2String(textArg, &combined);
        if(res != UA_STATUSCODE_GOOD) {
            PyErr_SetString(PyExc_TypeError, "Could not convert text to string");
            return -1;
        }

        // Find the first colon
        size_t colonPos = 0;
        UA_Boolean hasColon = false;
        for(size_t i = 0; i < combined.length; i++) {
            if(combined.data[i] == ':') {
                colonPos = i;
                hasColon = true;
                break;
            }
        }

        if(hasColon) {
            // locale is before the colon, text is after
            UA_String localeStr = {colonPos, combined.data};
            UA_String textStr = {combined.length - colonPos - 1,
                                 combined.data + colonPos + 1};
            res = UA_String_copy(&localeStr, &data->localizedText.locale);
            if(res != UA_STATUSCODE_GOOD) {
                PyErr_NoMemory();
                return -1;
            }
            res = UA_String_copy(&textStr, &data->localizedText.text);
            if(res != UA_STATUSCODE_GOOD) {
                UA_LocalizedText_clear(&data->localizedText);
                PyErr_NoMemory();
                return -1;
            }
        } else {
            // No colon: entire string is the text, locale stays empty
            res = UA_String_copy(&combined, &data->localizedText.text);
            if(res != UA_STATUSCODE_GOOD) {
                PyErr_NoMemory();
                return -1;
            }
        }
    } else {
        // Two arguments: text and locale
        UA_String textStr;
        UA_StatusCode res = Unicode2String(textArg, &textStr);
        if(res != UA_STATUSCODE_GOOD) {
            PyErr_SetString(PyExc_TypeError, "Could not convert text to string");
            return -1;
        }
        res = UA_String_copy(&textStr, &data->localizedText.text);
        if(res != UA_STATUSCODE_GOOD) {
            PyErr_NoMemory();
            return -1;
        }

        PyObject *localeArg = PyTuple_GetItem(args, 1);
        if(!PyUnicode_Check(localeArg)) {
            PyErr_SetString(PyExc_TypeError, "Locale argument must be a string");
            UA_LocalizedText_clear(&data->localizedText);
            return -1;
        }
        
        UA_String localeStr;
        res = Unicode2String(localeArg, &localeStr);
        if(res != UA_STATUSCODE_GOOD) {
            PyErr_SetString(PyExc_TypeError, "Could not convert locale to string");
            UA_LocalizedText_clear(&data->localizedText);
            return -1;
        }
        res = UA_String_copy(&localeStr, &data->localizedText.locale);
        if(res != UA_STATUSCODE_GOOD) {
            PyErr_NoMemory();
            UA_LocalizedText_clear(&data->localizedText);
            return -1;
        }
    }
    
    return 0;
}

PyObject *
pyLocalizedText_get_locale(PyObject *self, void *closure) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    if(data->localizedText.locale.length == 0)
        return PyUnicode_FromString("");
    return PyUnicode_FromStringAndSize((char*)data->localizedText.locale.data,
                                       data->localizedText.locale.length);
}

PyObject *
pyLocalizedText_get_text(PyObject *self, void *closure) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    if(data->localizedText.text.length == 0)
        return PyUnicode_FromString("");
    return PyUnicode_FromStringAndSize((char*)data->localizedText.text.data,
                                       data->localizedText.text.length);
}

int
pyLocalizedText_set_locale(PyObject *self, PyObject *value, void *closure) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    
    if (!PyUnicode_Check(value)) {
        PyErr_SetString(PyExc_TypeError, "locale must be a string");
        return -1;
    }
    
    const char *locale_str = PyUnicode_AsUTF8(value);
    if (!locale_str) {
        return -1;
    }
    
    // Clear existing locale and set new one
    UA_String_clear(&data->localizedText.locale);
    data->localizedText.locale = UA_STRING_ALLOC(locale_str);
    
    return 0;
}

int
pyLocalizedText_set_text(PyObject *self, PyObject *value, void *closure) {
    PyUABuiltin *data = (PyUABuiltin*)self;
    
    if (!PyUnicode_Check(value)) {
        PyErr_SetString(PyExc_TypeError, "text must be a string");
        return -1;
    }
    
    const char *text_str = PyUnicode_AsUTF8(value);
    if (!text_str) {
        return -1;
    }
    
    // Clear existing text and set new one
    UA_String_clear(&data->localizedText.text);
    data->localizedText.text = UA_STRING_ALLOC(text_str);
    
    return 0;
}

PyGetSetDef pyLocalizedText_getsets[] = {
    {"locale", pyLocalizedText_get_locale, pyLocalizedText_set_locale, "Locale", NULL},
    {"text", pyLocalizedText_get_text, pyLocalizedText_set_text, "Text", NULL},
    {NULL}
};
