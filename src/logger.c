/* Copyright 2026 (c) o6 Automation GmbH */
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
    const char *msg;
    const char *category_str = "";
    if(!PyArg_ParseTuple(args, "Os|s", &py_logger, &msg, &category_str))
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
    {"logTrace",   py_log_trace,   METH_VARARGS, "logTrace(logger, message, category='') -- UA_LOG_TRACE"},
    {"logDebug",   py_log_debug,   METH_VARARGS, "logDebug(logger, message, category='') -- UA_LOG_DEBUG"},
    {"logInfo",    py_log_info,    METH_VARARGS, "logInfo(logger, message, category='') -- UA_LOG_INFO"},
    {"logWarning", py_log_warning, METH_VARARGS, "logWarning(logger, message, category='') -- UA_LOG_WARNING"},
    {"logError",   py_log_error,   METH_VARARGS, "logError(logger, message, category='') -- UA_LOG_ERROR"},
    {"logFatal",   py_log_fatal,   METH_VARARGS, "logFatal(logger, message, category='') -- UA_LOG_FATAL"},
    {"log_trace",   py_log_trace,   METH_VARARGS, "Deprecated alias for logTrace"},
    {"log_debug",   py_log_debug,   METH_VARARGS, "Deprecated alias for logDebug"},
    {"log_info",    py_log_info,    METH_VARARGS, "Deprecated alias for logInfo"},
    {"log_warning", py_log_warning, METH_VARARGS, "Deprecated alias for logWarning"},
    {"log_error",   py_log_error,   METH_VARARGS, "Deprecated alias for logError"},
    {"log_fatal",   py_log_fatal,   METH_VARARGS, "Deprecated alias for logFatal"},
    {NULL, NULL, 0, NULL}
};
