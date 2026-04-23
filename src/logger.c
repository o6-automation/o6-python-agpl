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

#include "module.h"
#include <open62541/plugin/log.h>

const char *syslogCategoryNames[UA_LOGCATEGORIES] =
    {"network", "channel", "session", "server", "client",
     "userland", "security", "eventloop", "pubsub", "discovery"};

static void
pyLog_log(void *context, UA_LogLevel level, UA_LogCategory category,
          const char *msg, va_list args) {
    if(context == NULL)
        return;

#define LOGBUFSIZE 511
    char logbuf[LOGBUFSIZE + 1];

    UA_String buf = {LOGBUFSIZE, (UA_Byte*)logbuf};
    UA_String_format(&buf, "%s / ", syslogCategoryNames[category]);

    UA_String buf2 = {LOGBUFSIZE - buf.length, buf.data + buf.length};
    UA_String_vformat(&buf2, msg, args);
    buf2.data[buf2.length] = 0;

    // Get the log method
    PyObject *logger = (PyObject*)context;
    PyObject *log_method;
    switch(level) {
    case UA_LOGLEVEL_DEBUG:
        log_method = PyObject_GetAttrString(logger, "debug");
        break;
    case UA_LOGLEVEL_INFO:
        log_method = PyObject_GetAttrString(logger, "info");
        break;
    case UA_LOGLEVEL_WARNING:
        log_method = PyObject_GetAttrString(logger, "warning");
        break;
    case UA_LOGLEVEL_ERROR:
        log_method = PyObject_GetAttrString(logger, "error");
        break;
    case UA_LOGLEVEL_FATAL:
        log_method = PyObject_GetAttrString(logger, "critical");
        break;
    case UA_LOGLEVEL_TRACE:
    default:
        return;
    }

    if(!log_method || !PyCallable_Check(log_method)) {
        fprintf(stderr, "logger is not callable\n");
        Py_XDECREF(log_method);
        return;
    }

    // Create a Python string from the C string
    PyObject *py_msg = PyUnicode_FromString(logbuf);
    if(!py_msg) {
        fprintf(stderr, "Failed to create Python string from message.\n");
        Py_DECREF(log_method);
        return;
    }

    // Call the debug method with the message
    PyObject *result = PyObject_CallFunctionObjArgs(log_method, py_msg, NULL);

    // Cleanup
    Py_DECREF(log_method);
    Py_DECREF(py_msg);
    Py_XDECREF(result);
}

static void
pyLog_clear(UA_Logger *logger) {
    Py_XDECREF((PyObject*)logger->context);
    //UA_free(logger);
}

UA_Logger * pyLogger(PyObject *pyLog) {
    UA_Logger *logger = (UA_Logger*)UA_malloc(sizeof(UA_Logger));
    if(!logger)
        return NULL;
    logger->context = pyLog;
    logger->clear = pyLog_clear;
    logger->log = pyLog_log;
    Py_INCREF(pyLog);
    return logger;
}

/******************************/
/* Python free-floating LOG   */
/* functions (module methods) */
/******************************/

static UA_LogCategory
parse_log_category(const char *name) {
    for(UA_LogCategory i = 0; i < UA_LOGCATEGORIES; i++) {
        if(strcmp(syslogCategoryNames[i], name) == 0)
            return i;
    }
    return UA_LOGCATEGORY_USERLAND;
}

static PyObject *
py_log_generic(UA_LogLevel level, PyObject *args) {
    PyObject *py_logger;
    const char *category_str;
    const char *msg;
    if(!PyArg_ParseTuple(args, "Oss", &py_logger, &category_str, &msg))
        return NULL;

    /* Stack-allocated UA_Logger — no heap alloc, no refcount change needed */
    UA_Logger logger = {pyLog_log, py_logger, NULL};
    UA_LogCategory cat = parse_log_category(category_str);

    switch(level) {
    case UA_LOGLEVEL_TRACE:   UA_LOG_TRACE(&logger, cat, "%s", msg);   break;
    case UA_LOGLEVEL_DEBUG:   UA_LOG_DEBUG(&logger, cat, "%s", msg);   break;
    case UA_LOGLEVEL_INFO:    UA_LOG_INFO(&logger, cat, "%s", msg);    break;
    case UA_LOGLEVEL_WARNING: UA_LOG_WARNING(&logger, cat, "%s", msg); break;
    case UA_LOGLEVEL_ERROR:   UA_LOG_ERROR(&logger, cat, "%s", msg);   break;
    case UA_LOGLEVEL_FATAL:   UA_LOG_FATAL(&logger, cat, "%s", msg);   break;
    default: break;
    }
    Py_RETURN_NONE;
}

static PyObject *
py_log_trace(PyObject *self, PyObject *args)   { return py_log_generic(UA_LOGLEVEL_TRACE,   args); }

static PyObject *
py_log_debug(PyObject *self, PyObject *args)   { return py_log_generic(UA_LOGLEVEL_DEBUG,   args); }

static PyObject *
py_log_info(PyObject *self, PyObject *args)    { return py_log_generic(UA_LOGLEVEL_INFO,    args); }

static PyObject *
py_log_warning(PyObject *self, PyObject *args) { return py_log_generic(UA_LOGLEVEL_WARNING, args); }

static PyObject *
py_log_error(PyObject *self, PyObject *args)   { return py_log_generic(UA_LOGLEVEL_ERROR,   args); }

static PyObject *
py_log_fatal(PyObject *self, PyObject *args)   { return py_log_generic(UA_LOGLEVEL_FATAL,   args); }

PyMethodDef pyLoggingMethods[] = {
    {"log_trace",   py_log_trace,   METH_VARARGS, "log_trace(logger, category, msg) -- UA_LOG_TRACE"},
    {"log_debug",   py_log_debug,   METH_VARARGS, "log_debug(logger, category, msg) -- UA_LOG_DEBUG"},
    {"log_info",    py_log_info,    METH_VARARGS, "log_info(logger, category, msg) -- UA_LOG_INFO"},
    {"log_warning", py_log_warning, METH_VARARGS, "log_warning(logger, category, msg) -- UA_LOG_WARNING"},
    {"log_error",   py_log_error,   METH_VARARGS, "log_error(logger, category, msg) -- UA_LOG_ERROR"},
    {"log_fatal",   py_log_fatal,   METH_VARARGS, "log_fatal(logger, category, msg) -- UA_LOG_FATAL"},
    {NULL, NULL, 0, NULL}
};
