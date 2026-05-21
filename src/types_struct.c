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

#define NO_IMPORT_ARRAY
#include "types_internal.h"
#include <numpy/arrayobject.h>
#include "types_internal.h"
#include "types_internal.h"

static UA_Boolean
getSnakeCaseStructMember(const UA_DataType *type,
                         const char *snakeName,
                         size_t *outOffset,
                         const UA_DataType **outMemberType,
                         UA_Boolean *outIsArray,
                         UA_Boolean *outIsOptional) {
    char cname[128];
    makeCamlName(snakeName, cname);

    const char *lookupName = cname;
    UA_Boolean found = UA_DataType_getStructMember(type, cname, outOffset,
                                                   outMemberType, outIsArray);

    /* Fallback: if the CamelCase name didn't match, try the original
     * snake_case name directly.  This handles member names that are already
     * lowercase (e.g. single-char names like "x", "y" from custom types
     * built via UA_DataType_fromDescription). */
    if(!found) {
        found = UA_DataType_getStructMember(type, snakeName, outOffset,
                                            outMemberType, outIsArray);
        if(!found)
            return false;
        lookupName = snakeName;
    } else {
        // Check that we have the same name when converting back.
        // This avoids adding half-caml-names to the dict.
        char snakeName2[128];
        makeSnakeName(cname, snakeName2);
        if(strcmp(snakeName, snakeName2) != 0)
            return false;
    }

    // Find the member to get isOptional (not returned by UA_DataType_getStructMember)
    *outIsOptional = false;
    for(size_t i = 0; i < type->membersSize; i++) {
        if(strcmp(type->members[i].memberName, lookupName) == 0) {
            *outIsOptional = type->members[i].isOptional;
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

    PyObject *parts = PyList_New(uaType->membersSize);
    if(!parts)
        return NULL;

    // Add the struct members
    for(size_t i = 0; i < uaType->membersSize; i++) {
        char snakeName[128];
        makeSnakeName(uaType->members[i].memberName, snakeName);
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
        PyList_SET_ITEM(parts, i, entry);
    }

    PyObject *joined = PyUnicode_Join(PyUnicode_FromString(", "), parts);
    Py_DECREF(parts);
    return joined;
}

PyObject *pyUAStruct_str(PyObject *self) {
    PyObject *internal = __pyUAStruct_str(self);
    if(!internal)
        return NULL;
    PyObject *out = PyUnicode_FromFormat("{%U}", internal);
    Py_DECREF(internal);
    return out;
}


PyObject *pyUAStruct_repr(PyObject *self) {
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
        makeSnakeName(uaType->members[i].memberName, snakeName);
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
    const UA_DataType *memberType;
    UA_Boolean isArray;
    UA_Boolean isOptional;
    UA_Boolean found =
        getSnakeCaseStructMember(uaType, snakeName, &outOffset, &memberType,
                                 &isArray, &isOptional);
    if(!found) {
        PyErr_Format(PyExc_AttributeError, "Attribute '%s' not defined for %s",
                     snakeName, type->tp_name);
        return -1;
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
    PyUAStruct *s = (PyUAStruct*)self;
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
        PyObject *element = UA2PY(elementPtr, type);
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
            PyObject *dict = ((PyUAStruct *)self)->dict;
            Py_XINCREF(dict);
            return dict;
        }
        return PyObject_GenericGetAttr(self, name);
    }

    // Is the member defined for the OPC UA type?
    size_t outOffset;
    const UA_DataType *memberType;
    UA_Boolean isArray;
    UA_Boolean isOptional;
    UA_Boolean found =
        getSnakeCaseStructMember(uaType, snakeName, &outOffset,
                                 &memberType, &isArray, &isOptional);
    if(!found) {
        PyErr_Format(PyExc_AttributeError, "Attribute '%s' not defined for %s",
                     snakeName, type->tp_name);
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
            res = UA2PY(ptr, memberType);
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
        res = UA2PY(&s->data[outOffset], memberType);
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

    // Flush any remaining C-struct data into the Python dict by
    // reading all fields, which triggers the lazy conversion in getattro.
    for(size_t i = 0; i < uaType->membersSize; i++) {
        char snakeName[128];
        makeSnakeName(uaType->members[i].memberName, snakeName);
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
    if(src->dict) {
        dst->dict = PyDict_Copy(src->dict);
        if(!dst->dict) {
            Py_DECREF(newobj);
            return NULL;
        }
    }
    return newobj;
}
