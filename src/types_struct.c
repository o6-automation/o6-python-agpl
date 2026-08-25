/* Copyright 2026 (c) o6 Automation GmbH */
#define NO_IMPORT_ARRAY
#include "types_internal.h"
#include <numpy/arrayobject.h>
#include "types_internal.h"
#include "types_internal.h"

/* Look up a Python dunder method on the struct's class.
 *
 * If the source python class defines a python dunder (currently only __str__, __repr__), 
 * then the user-defined method is called instead of the C default formatting.
 * Gets the original python method.
 */
static PyObject *
getUserDunder(PyObject *self, const char *name) {
    PyTypeObject *type = Py_TYPE(self);
    if(!type->tp_dict)
        return NULL;
    PyObject *fn = PyDict_GetItemString(type->tp_dict, name);
    if(!fn || Py_TYPE(fn) != &PyFunction_Type)
        return NULL;
    return fn;
}

/* Call the original python dunder method retrieved by getUserDunder with single argument `self`.
 */
static PyObject *
callUserUnaryDunder(PyObject *self, const char *name) {
    PyObject *fn = getUserDunder(self, name);
    if(!fn)
        return NULL;  /* no user dunder; PyErr is NOT set */
    return PyObject_CallOneArg(fn, self);
}

/* Look up the raw class attribute `name` on the struct's class or one of its
 * bases, without invoking its descriptor protocol.
 *
 * Borrowed reference, or NULL (with no exception set) when the name is not
 * declared anywhere in the MRO. `PyObject_GetAttr` on the class cannot answer
 * this: it returns whatever `__get__(None, cls)` produces, which for a
 * descriptor that hides itself is not the descriptor.
 */
static PyObject *
declaredClassAttribute(PyTypeObject *type, PyObject *name) {
    PyObject *mro = type->tp_mro;
    if(!mro || !PyTuple_Check(mro))
        return NULL;
    for(Py_ssize_t i = 0; i < PyTuple_GET_SIZE(mro); i++) {
        PyObject *base = PyTuple_GET_ITEM(mro, i);
        if(!PyType_Check(base) || !((PyTypeObject *)base)->tp_dict)
            continue;
        /* PyDict_GetItem does not set an exception when the key is absent. */
        PyObject *found = PyDict_GetItem(((PyTypeObject *)base)->tp_dict, name);
        if(found)
            return found;
    }
    return NULL;
}

static UA_Boolean
getStructMember(const UA_DataType *type,
                const char *name,
                size_t *outOffset,
                const UA_DataType **outMemberType,
                UA_Boolean *outIsArray,
                UA_Boolean *outIsOptional,
                size_t *outMemberIndex) {
    if(type->typeKind == UA_DATATYPEKIND_UNION) {
        for(size_t i = 0; i < type->membersSize; i++) {
            const char *memberName = type->members[i].memberName;
            if(memberName[0] && name[0] &&
               tolower((unsigned char)memberName[0]) ==
                   tolower((unsigned char)name[0]) &&
               strcmp(memberName + 1, name + 1) == 0) {
                *outOffset = type->members[i].padding;
                *outMemberType = type->members[i].memberType;
                *outIsArray = type->members[i].isArray;
                *outIsOptional = false;
                *outMemberIndex = i;
                return true;
            }
        }
        return false;
    }
    /* Try the name as-is first */
    UA_Boolean found = UA_DataType_getStructMember(type, name, outOffset,
                                                   outMemberType, outIsArray);

    /* If not found, try with the first character's case toggled.
     * This lets callers use either the original UA name (e.g. "StartingBitPosition")
     * or the canonical Python name with a lower-cased first char ("startingBitPosition"). */
    if(!found && name[0]) {
        char alt[128];
        size_t len = strlen(name);
        if(len >= sizeof(alt)) len = sizeof(alt) - 1;
        memcpy(alt, name, len);
        alt[len] = 0;
        alt[0] = (char)(isupper((unsigned char)alt[0])
                        ? tolower((unsigned char)alt[0])
                        : toupper((unsigned char)alt[0]));
        found = UA_DataType_getStructMember(type, alt, outOffset,
                                            outMemberType, outIsArray);
    }

    if(!found)
        return false;

    /* Find the member to get isOptional (not returned by UA_DataType_getStructMember) */
    *outIsOptional = false;
    for(size_t i = 0; i < type->membersSize; i++) {
        const char *mname = type->members[i].memberName;
        /* Match: first char case-insensitive, rest exact */
        if(mname[0] && name[0] &&
           tolower((unsigned char)mname[0]) == tolower((unsigned char)name[0]) &&
           strcmp(mname + 1, name + 1) == 0) {
            *outIsOptional = type->members[i].isOptional;
            *outMemberIndex = i;
            break;
        }
    }
    return true;
}

int
pyUAStruct_traverse(PyObject *self, visitproc visit, void *arg) {
    PyUAStruct *data = (PyUAStruct*)self;
    Py_VISIT(data->dict);
    return 0;
}

int
pyUAStruct_clear(PyObject *self) {
    PyUAStruct *data = (PyUAStruct*)self;
    Py_CLEAR(data->dict);
    return 0;
}

static PyObject *
__pyUAStruct_str(PyObject *self) {
    PyTypeObject *type = Py_TYPE(self);
    const UA_DataType *uaType = PY2UAType(type);
    UA_UInt32 unionSelection = 0;
    size_t outputSize = uaType->membersSize;
    if(uaType->typeKind == UA_DATATYPEKIND_UNION) {
        unionSelection = *(UA_UInt32*)((PyUAStruct*)self)->data;
        outputSize = unionSelection == 0 ? 0 : 1;
    }

    PyObject *parts = PyList_New(outputSize);
    if(!parts)
        return NULL;

    // Add the struct members
    size_t outputIndex = 0;
    for(size_t i = 0; i < uaType->membersSize; i++) {
        if(uaType->typeKind == UA_DATATYPEKIND_UNION &&
           unionSelection != i + 1)
            continue;
        char snakeName[128];
        lcFirst(uaType->members[i].memberName, snakeName);
        PyObject *name = PyUnicode_FromString(snakeName);
        if(!name) {
            Py_DECREF(parts);
            return NULL;
        }
        PyObject *value = PyObject_GetAttr(self, name);  // New ref
        if(!value) {
            Py_DECREF(name);
            Py_DECREF(parts);
            return NULL;
        }

        // Print the member in "canonical form".
        PyObject *entry;
        const UA_DataType *memberType = uaType->members[i].memberType;
        if(memberType == &UA_TYPES[UA_TYPES_STRING]) {
            // Wrap strings with quotes
            entry = PyUnicode_FromFormat("%U=%R", name, value);
        } else if(memberType == &UA_TYPES[UA_TYPES_NODEID] ||
                  memberType == &UA_TYPES[UA_TYPES_EXPANDEDNODEID] ||
                  memberType == &UA_TYPES[UA_TYPES_QUALIFIEDNAME] ||
                  memberType == &UA_TYPES[UA_TYPES_LOCALIZEDTEXT]) {
            // NodeIds always as a string representation.
            entry = PyUnicode_FromFormat("%U='%S'", name, value);
        } else {
            entry = PyUnicode_FromFormat("%U=%S", name, value);
        }
        Py_DECREF(name);
        Py_DECREF(value);

        if (!entry) {
            Py_DECREF(parts);
            return NULL;
        }
        PyList_SET_ITEM(parts, outputIndex++, entry);
    }

    PyObject *joined = PyUnicode_Join(PyUnicode_FromString(", "), parts);
    Py_DECREF(parts);
    return joined;
}

PyObject *pyUAStruct_str(PyObject *self) {
    // Honour a user-defined Python `__str__`
    PyObject *result = callUserUnaryDunder(self, "__str__");
    if(result || PyErr_Occurred())
        return result;  /* user-defined: return result, or propagate error */

    PyObject *internal = __pyUAStruct_str(self);
    if(!internal)
        return NULL;
    PyObject *out = PyUnicode_FromFormat("{%U}", internal);
    Py_DECREF(internal);
    return out;
}


PyObject *pyUAStruct_repr(PyObject *self) {
    // Honour a user-defined Python `__repr__`
    PyObject *result = callUserUnaryDunder(self, "__repr__");
    if(result || PyErr_Occurred())
        return result;  /* user-defined: return result, or propagate error */

    PyObject *internal = __pyUAStruct_str(self);
    if(!internal)
        return NULL;
    PyObject *out = PyUnicode_FromFormat("%s(%U)", Py_TYPE(self)->tp_name, internal);
    Py_DECREF(internal);
    return out;
}

void
pyUAStruct_dealloc(PyObject *self) {
    PyUAStruct *struct_self = (PyUAStruct *)self;
    PyObject_GC_UnTrack(self);
    Py_XDECREF(struct_self->dict);
    struct_self->dict = NULL;
    Py_TYPE(self)->tp_free(self);
}

PyObject *
pyUAStruct_dir(PyObject *self, PyObject *Py_UNUSED(ignored)) {
    PyTypeObject *type = Py_TYPE(self);

    // Initialize the dict of not already done
    PyUAStruct *s = (PyUAStruct*)self;
    if(!s->dict) {
        s->dict = PyDict_New();
        if(!s->dict)
            return NULL;
    }

    // call object.__dir__(self)
    PyObject *unbound = PyObject_GetAttrString((PyObject *)&PyBaseObject_Type, "__dir__");
    if(!unbound)
        return NULL;
    PyObject *bound = PyObject_CallMethod(unbound, "__get__", "OO", self, (PyObject *)type);
    Py_DECREF(unbound);
    if(!bound)
        return NULL;
    PyObject *out = PyObject_CallNoArgs(bound);
    Py_DECREF(bound);
    if(!out)
        return NULL;

    // Add the struct members
    const UA_DataType *uaType = PY2UAType(type);
    for(size_t i = 0; i < uaType->membersSize; i++) {
        char snakeName[128];
        lcFirst(uaType->members[i].memberName, snakeName);
        PyObject *name = PyUnicode_FromString(snakeName);
        if(!name)
            continue;
        if(!listContains(out, name))
            PyList_Append(out, name);
        Py_DECREF(name);
    }

    return out;
}

int
pyUAStruct_setattro(PyObject *self, PyObject *name, PyObject *value) {
    // Get the member
    PyTypeObject *type = Py_TYPE(self);
    const UA_DataType *uaType = PY2UAType(type);
    char *snakeName = (char*)(uintptr_t)PyUnicode_AsUTF8(name);
    if(!snakeName)
        return -1;

    size_t outOffset;
    size_t memberIndex = 0;
    const UA_DataType *memberType;
    UA_Boolean isArray;
    UA_Boolean isOptional;
    UA_Boolean found =
        getStructMember(uaType, snakeName, &outOffset, &memberType,
                        &isArray, &isOptional, &memberIndex);
    if(!found) {
        /* Delegate to the interpreter: data descriptors own the name, and
         * generated struct types have no managed dict.  The strict error
         * survives only for subclasses with a managed dict, where the
         * interpreter would silently absorb the name. */
        PyObject *declared = declaredClassAttribute(type, name);
        if(declared && Py_TYPE(declared)->tp_descr_set)
            return PyObject_GenericSetAttr(self, name, value);
        if(type->tp_dictoffset == 0)
            return PyObject_GenericSetAttr(self, name, value);
        PyErr_Format(PyExc_AttributeError, "Attribute '%s' not defined for %s",
                     snakeName, type->tp_name);
        return -1;
    }

    PyUAStruct *s = (PyUAStruct*)self;
    if(value == NULL) {
        /* ``del instance.member``: the interpreter signals deletion via NULL.
         * Struct members always carry a value on the wire; the match / write
         * steps below dereference ``value`` unconditionally. */
        PyErr_Format(PyExc_AttributeError,
                     "Cannot delete required member '%s' of %s; OPC UA "
                     "structure members always carry a value",
                     snakeName, type->tp_name);
        return -1;
    }
    if(uaType->typeKind == UA_DATATYPEKIND_UNION) {
        UA_clear(s->data, uaType);
        memset(s->data, 0, uaType->memSize);
        if(s->dict)
            PyDict_Clear(s->dict);
        *(UA_UInt32*)s->data = (UA_UInt32)(memberIndex + 1);
    }

    PyUATypeMatch match = PY2UAMatch(value);
    if(isArray) {
        if(match.dimension == PYVALUEDIMENSION_SCALAR) {
            PyErr_Format(PyExc_TypeError, "Attribute '%s' must be a one-dimensional array, but is a scalar", snakeName);
            return -1;
        }

        if(match.dimension == PYVALUEDIMENSION_NDARRAY) {
            PyArrayObject *arr = (PyArrayObject*) value;
            int ndim = PyArray_NDIM(arr);
            if(ndim != 1) {
                PyErr_Format(PyExc_TypeError, "Attribute '%s' must be a one-dimensional array", snakeName);
                return -1;
            }
        }
    }

    // Initialize the dict if not already done
    if(!s->dict) {
        s->dict = PyDict_New();
        if(!s->dict)
            return -1;
    }

    // Set the new value in the dict
    if(value == Py_None || (isArray && PySequence_Length(value) == 0)) {
        // Remove the value
        PyDict_DelItem(s->dict, name);
        PyErr_Clear(); // If the key didn't exist
        // Continue clearing the entry in the structure below
    } else if(memberType == match.uaType) {
        // Matching type and dimensions. Set the attribute in the dict.
        int res = PyDict_SetItemString(s->dict, snakeName, value);
        if(res < 0)
            return res;
    } else if(memberType == &UA_TYPES[UA_TYPES_VARIANT]) {
        // Variants can be everything. But the value needs a unique UA type.
        /* if(!match.uaType) { */
        /*     PyErr_Format(PyExc_TypeError, "Variant value '%s' needs to have a " */
        /*                  "well-defined UA type", snakeName); */
        /*     return -1; */
        /* } */
        /* // Set the attribute in the dict */
        int res = PyDict_SetItemString(s->dict, snakeName, value);
        if(res < 0)
            return -1;
    } else {
        // Find the target Python type to cast the value
        PyTypeObject *targetPyType = UA2PYType(memberType);
        if(!targetPyType) {
            PyErr_Format(PyExc_TypeError,
                         "Attribute '%s' has unknown type '%s'",
                         snakeName, memberType->typeName);
            return -1;
        }

        int isInstance = PyObject_IsInstance(value, (PyObject*)targetPyType);
        if(isInstance < 0)
            return -1;
        if(isInstance) {
            int res = PyDict_SetItemString(s->dict, snakeName, value);
            if(res < 0)
                return res;
            goto array_cleanup;
        }

        // Don't auto-cast arrays of non-numeric types. This is unexpected behavior,
        // e.g. when the original array is edited afterwards.
        // For numeric types (bool, integers, floats) accept compatible sequences —
        // the per-element PY2UA conversion during serialization handles the cast.
        if(isArray) {
            UA_Boolean memberIsNumeric =
                (memberType->typeKind <= UA_DATATYPEKIND_DOUBLE);
            UA_Boolean matchIsNumeric =
                (match.uaType && match.uaType->typeKind <= UA_DATATYPEKIND_DOUBLE);
            if(memberIsNumeric && (matchIsNumeric || !match.uaType)) {
                int res = PyDict_SetItemString(s->dict, snakeName, value);
                if(res < 0)
                    return -1;
            } else {
                PyErr_Format(PyExc_TypeError,
                             "Attribute '%s' is an array and its members "
                             "need to be of type '%s'", snakeName, memberType->typeName);
                return -1;
            }
            goto array_cleanup;
        }

        // Cast to an instance of the target type
        PyObject *instance = PyObject_CallFunctionObjArgs((PyObject *)targetPyType, value, NULL);
        if(!instance)
            return -1;

        // Set the attribute in the dict
        int res = PyDict_SetItemString(s->dict, snakeName, instance);
        Py_DECREF(instance);
        if(res < 0)
            return res;
    }

    // Clean up the entry in the C structure and convert from Python
    // Use the dict entry instead of the C structure entry
    array_cleanup:
    if(isArray) {
        size_t size = *(size_t*)&s->data[outOffset];
        void **arr = (void**)&s->data[outOffset + sizeof(size_t)];
        UA_Array_delete(*arr, size, memberType);
        *(size_t*)&s->data[outOffset] = 0;
        *arr = NULL;
    } else if(isOptional) {
        void **ptr = (void**)&s->data[outOffset];
        if(*ptr) {
            UA_clear(*ptr, memberType);
            UA_free(*ptr);
            *ptr = NULL;
        }
    } else {
        UA_clear((void*)&s->data[outOffset], memberType);
    }
    return 0;
}

static PyObject *
UA2PY_array(void *p, const UA_DataType *type) {
    // Extract array size and data pointer
    size_t arraySize = *(size_t*)p;
    void *arrayData = *(void**)((char*)p + sizeof(size_t));

    // Create Python list
    PyObject *list = PyList_New(arraySize);
    if (!list) {
        return NULL;
    }

    // Convert each element
    for (size_t i = 0; i < arraySize; i++) {
        void *elementPtr = (char*)arrayData + (i * type->memSize);
        PyObject *element = UA2PY(elementPtr, type, NULL);
        if (!element) {
            Py_DECREF(list);
            return NULL;
        }
        PyList_SetItem(list, i, element);  // Steals reference
    }

    return list;
}

PyObject *
pyUAStruct_getattro(PyObject *self, PyObject *name) {
    PyTypeObject *type = Py_TYPE(self);
    const UA_DataType *uaType = PY2UAType(type);

    // Get the member name
    char *snakeName = (char*)(uintptr_t)PyUnicode_AsUTF8(name);
    if(!snakeName)
        return NULL;

    // Special handling of dunder members - especially the dict!
    if(snakeName[0] == '_') {
        int cmp = PyUnicode_CompareWithASCIIString(name, "__dict__");
        if(cmp == 0) {
            PyUAStruct *s = (PyUAStruct *)self;
            if(!s->dict) {
                s->dict = PyDict_New();
                if(!s->dict)
                    return NULL;
            }
            PyObject *dict = s->dict;
            Py_INCREF(dict);
            return dict;
        }
        return PyObject_GenericGetAttr(self, name);
    }

    // Is the member defined for the OPC UA type?
    size_t outOffset;
    size_t memberIndex = 0;
    const UA_DataType *memberType;
    UA_Boolean isArray;
    UA_Boolean isOptional;
    UA_Boolean found =
        getStructMember(uaType, snakeName, &outOffset,
                        &memberType, &isArray, &isOptional, &memberIndex);
    if(!found) {
        // Not a struct member. 
        // Fall through to normal attribute lookup, so that user methods attached to the class via ``setattr`` are reachable
        // PyObject_GenericGetAttr consults the type's `tp_dict` (the class `__dict__`) and then the instance `__dict__`, mirroring the dunder path above. 
        return PyObject_GenericGetAttr(self, name);
    }
    if(uaType->typeKind == UA_DATATYPEKIND_UNION &&
       *(UA_UInt32*)((PyUAStruct*)self)->data != memberIndex + 1) {
        PyErr_Format(PyExc_AttributeError,
                     "Union member '%s' is not active", snakeName);
        return NULL;
    }

    // Initialize the dict if not already done
    PyUAStruct *s = (PyUAStruct*)self;
    if(!s->dict) {
        s->dict = PyDict_New();
        if(!s->dict)
            return NULL;
    }

    // First check if the attribute is already in our custom dict
    PyObject *res = PyDict_GetItem(s->dict, name);
    if(res) {
        Py_INCREF(res);
        return res;
    }

    // PyDict_GetItem does not set exceptions
    // PyErr_Clear();
    
    if(isArray) {
        res = UA2PY_array(&s->data[outOffset], memberType);
        if(!res)
            return NULL;
        if(PyDict_SetItem(s->dict, name, res) < 0) {
            Py_DECREF(res);
            return NULL;
        }

        // Clean up the entry in the C structure
        size_t *arrSize = (size_t*)&s->data[outOffset];
        void **arr = (void**)&s->data[outOffset + sizeof(size_t)];
        UA_Array_delete(*arr, *arrSize, memberType);
        *arrSize = 0;
        *arr = NULL;
    } else if(isOptional) {
        void *ptr = *(void**)&s->data[outOffset];
        if(!ptr) {
            Py_INCREF(Py_None);
            res = Py_None;
        } else {
            res = UA2PY(ptr, memberType, NULL);
            if(!res)
                return NULL;
            // Clean up the pointed-to value
            UA_clear(ptr, memberType);
            UA_free(ptr);
            *(void**)&s->data[outOffset] = NULL;
        }
        if(PyDict_SetItem(s->dict, name, res) < 0) {
            Py_DECREF(res);
            return NULL;
        }
    } else {
        res = UA2PY(&s->data[outOffset], memberType, NULL);
        if(!res)
            return NULL;
        if(PyDict_SetItem(s->dict, name, res) < 0) {
            Py_DECREF(res);
            return NULL;
        }

        // Clean up the entry in the C structure
        UA_clear((void*)&s->data[outOffset], memberType);
    }

    return res;
}

PyObject *
pyUAStruct_copy(PyObject *self, PyObject *Py_UNUSED(ignored)) {
    PyTypeObject *type = Py_TYPE(self);
    const UA_DataType *uaType = PY2UAType(type);
    UA_UInt32 unionSelection = 0;
    if(uaType->typeKind == UA_DATATYPEKIND_UNION)
        unionSelection = *(UA_UInt32*)((PyUAStruct*)self)->data;

    // Flush any remaining C-struct data into the Python dict by
    // reading all fields, which triggers the lazy conversion in getattro.
    for(size_t i = 0; i < uaType->membersSize; i++) {
        if(uaType->typeKind == UA_DATATYPEKIND_UNION &&
           unionSelection != i + 1)
            continue;
        char snakeName[128];
        lcFirst(uaType->members[i].memberName, snakeName);
        PyObject *name = PyUnicode_FromString(snakeName);
        if(!name)
            return NULL;
        PyObject *val = PyObject_GetAttr(self, name);
        Py_DECREF(name);
        if(!val)
            return NULL;
        Py_DECREF(val);
    }

    // Allocate a new zeroed instance of the same type and copy the dict.
    PyObject *newobj = type->tp_alloc(type, 0);
    if(!newobj)
        return NULL;

    PyUAStruct *src = (PyUAStruct *)self;
    PyUAStruct *dst = (PyUAStruct *)newobj;
    if(uaType->typeKind == UA_DATATYPEKIND_UNION)
        *(UA_UInt32*)dst->data = unionSelection;
    if(src->dict) {
        dst->dict = PyDict_Copy(src->dict);
        if(!dst->dict) {
            Py_DECREF(newobj);
            return NULL;
        }
    }
    return newobj;
}
