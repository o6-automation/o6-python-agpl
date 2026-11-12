/* Copyright 2026 (c) o6 Automation GmbH */
/* JSON5 documents for the file-based server and client configuration */
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

#include "types_internal.h"

#ifdef UA_ENABLE_JSON_ENCODING
#include "cj5.h"

/* The token limit of the open62541 JSON config loader (ua_config_json.c), so
 * that every document accepted here also fits there */
#define JSON5_MAX_TOKENS 1024

/* Copy the source text of a token into a NUL-terminated buffer */
static char *
json5_token_text(const cj5_result *r, const cj5_token *tok) {
    size_t len = (size_t)(tok->end - tok->start) + 1;
    char *buf = (char *)PyMem_Malloc(len + 1);
    if(!buf) {
        PyErr_NoMemory();
        return NULL;
    }
    memcpy(buf, &r->json5[tok->start], len);
    buf[len] = 0;
    return buf;
}

static PyObject *
json5_number(const cj5_result *r, unsigned int index) {
    char *text = json5_token_text(r, &r->tokens[index]);
    if(!text)
        return NULL;
    /* Integers, including hex, keep full precision as Python ints. Base 0
     * accepts the 0x prefix and an explicit sign. */
    const char *digits = (text[0] == '+' || text[0] == '-') ? text + 1 : text;
    UA_Boolean hex = digits[0] == '0' && (digits[1] == 'x' || digits[1] == 'X');
    PyObject *result = NULL;
    if(hex || !strpbrk(digits, ".eEIN")) {
        result = PyLong_FromString(text, NULL, 0);
    } else {
        double value;
        if(cj5_get_float(r, index, &value) == CJ5_ERROR_NONE)
            result = PyFloat_FromDouble(value);
        else
            PyErr_Format(PyExc_ValueError, "Invalid JSON5 number '%s'", text);
    }
    PyMem_Free(text);
    return result;
}

/* An object key that fails to decode, such as an unpaired surrogate escape,
 * keeps its decoded prefix like in the open62541 loader, which then skips it
 * as an unknown field. A value that fails to decode is an error. */
static PyObject *
json5_string(const cj5_result *r, unsigned int index, UA_Boolean key) {
    char *buf = (char *)PyMem_Malloc(r->tokens[index].size + 1);
    if(!buf)
        return PyErr_NoMemory();
    unsigned int len = 0;
    PyObject *result = NULL;
    if(cj5_get_str(r, index, buf, &len) == CJ5_ERROR_NONE || key)
        result = PyUnicode_DecodeUTF8(buf, (Py_ssize_t)len, key ? "replace" : "strict");
    else
        PyErr_SetString(PyExc_ValueError, "Invalid JSON5 string");
    PyMem_Free(buf);
    return result;
}

/* Convert the token at *index and its children; advances *index past them.
 * Tokens are stored depth-first, so the children follow their parent. */
static PyObject *
json5_value(const cj5_result *r, unsigned int *index) {
    const cj5_token *tok = &r->tokens[*index];
    unsigned int self = (*index)++;
    switch(tok->type) {
    case CJ5_TOKEN_OBJECT: {
        PyObject *dict = PyDict_New();
        for(unsigned int i = 0; dict && i < tok->size / 2; i++) {
            PyObject *key = json5_string(r, (*index)++, true);
            PyObject *value = key ? json5_value(r, index) : NULL;
            if(!value || PyDict_SetItem(dict, key, value) < 0)
                Py_CLEAR(dict);
            Py_XDECREF(key);
            Py_XDECREF(value);
        }
        return dict;
    }
    case CJ5_TOKEN_ARRAY: {
        PyObject *list = PyList_New((Py_ssize_t)tok->size);
        for(unsigned int i = 0; list && i < tok->size; i++) {
            PyObject *value = json5_value(r, index);
            if(!value)
                Py_CLEAR(list);
            else
                PyList_SET_ITEM(list, (Py_ssize_t)i, value);
        }
        return list;
    }
    case CJ5_TOKEN_NUMBER:
        return json5_number(r, self);
    case CJ5_TOKEN_STRING:
        return json5_string(r, self, false);
    case CJ5_TOKEN_BOOL: {
        bool value = false;
        cj5_get_bool(r, self, &value);
        return PyBool_FromLong(value);
    }
    case CJ5_TOKEN_NULL:
    default:
        Py_RETURN_NONE;
    }
}

/* Parse a JSON5 document with the cj5 parser that the open62541 JSON config
 * loader uses, so both accept exactly the same syntax. The root must be an
 * object, as for a server or client configuration. */
PyObject *
pyJson5_parse(PyObject *self, PyObject *arg) {
    Py_buffer view;
    if(PyObject_GetBuffer(arg, &view, PyBUF_SIMPLE) < 0)
        return NULL;
    cj5_token *tokens = (cj5_token *)PyMem_Malloc(sizeof(cj5_token) * JSON5_MAX_TOKENS);
    if(!tokens) {
        PyBuffer_Release(&view);
        return PyErr_NoMemory();
    }
    cj5_result r = cj5_parse((const char *)view.buf, (unsigned int)view.len,
                             tokens, JSON5_MAX_TOKENS, NULL);
    PyObject *result = NULL;
    if(r.error == CJ5_ERROR_OVERFLOW) {
        PyErr_Format(PyExc_ValueError,
                     "JSON5 document exceeds %d tokens", JSON5_MAX_TOKENS);
    } else if(r.error != CJ5_ERROR_NONE) {
        PyErr_Format(PyExc_ValueError, "Invalid JSON5 at position %u",
                     r.error_pos);
    } else if(r.num_tokens == 0 || tokens[0].type != CJ5_TOKEN_OBJECT) {
        PyErr_SetString(PyExc_ValueError, "JSON5 document must be an object");
    } else {
        unsigned int index = 0;
        result = json5_value(&r, &index);
    }
    PyMem_Free(tokens);
    PyBuffer_Release(&view);
    return result;
}

/* ServerConfig.loadFromFile and ClientConfig.loadFromFile: read, prepare and
 * load a JSON5 file in o6/_json_config.py */
PyObject *
pyJsonConfig_load(PyObject *config, PyObject *path) {
    PyObject *module = PyImport_ImportModule("o6._json_config");
    if(!module)
        return NULL;
    PyObject *result = PyObject_CallMethod(module, "load", "OO", config, path);
    Py_DECREF(module);
    return result;
}

#endif /* UA_ENABLE_JSON_ENCODING */
