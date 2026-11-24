/* Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner) */
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

#include <limits.h>
#include <math.h>
#include <stddef.h>
#include "server/ua_server_internal.h"
#include <open62541/plugin/accesscontrol_default.h>

#include "server.h"
#include "../module.h"
#include "../types_internal.h"
#include "../utils.h"
#include "server_access_control.h"

/* Helper: get config from PyServerConfig */
static UA_ServerConfig *get_config(PyServerConfig *self) {
    if (!self->py_server || !self->py_server->server)
        return NULL;
    return UA_Server_getConfig(self->py_server->server);
}

/* The build time of the extension, from __DATE__ ("Sep 29 2026") and
 * __TIME__ ("21:55:19") */
static UA_DateTime
o6_build_date(void) {
    static const char months[] = "JanFebMarAprMayJunJulAugSepOctNovDec";
    const char *date = __DATE__;
    const char *time = __TIME__;
    char month[4] = {date[0], date[1], date[2], '\0'};
    const char *pos = strstr(months, month);
    UA_DateTimeStruct dts;
    memset(&dts, 0, sizeof(dts));
    dts.year = (UA_Int16)atoi(&date[7]);
    dts.month = (UA_UInt16)(pos ? (pos - months) / 3 + 1 : 1);
    dts.day = (UA_UInt16)atoi(&date[4]);
    dts.hour = (UA_UInt16)atoi(time);
    dts.min = (UA_UInt16)atoi(&time[3]);
    dts.sec = (UA_UInt16)atoi(&time[6]);
    return UA_DateTime_fromStruct(dts);
}

/* The package version from o6.__version__. The package is imported
 * completely before a server can be created. */
static UA_String
o6_software_version(void) {
    UA_String version = UA_STRING_NULL;
    PyObject *type, *value, *traceback;
    PyErr_Fetch(&type, &value, &traceback);
    PyObject *module = PyImport_ImportModule("o6");
    PyObject *pyVersion = module ? PyObject_GetAttrString(module, "__version__") : NULL;
    const char *str = (pyVersion && PyUnicode_Check(pyVersion))
        ? PyUnicode_AsUTF8(pyVersion) : NULL;
    version = UA_STRING_ALLOC(str ? str : "unknown");
    Py_XDECREF(pyVersion);
    Py_XDECREF(module);
    PyErr_Clear();
    PyErr_Restore(type, value, traceback);
    return version;
}

void
o6_server_config_set_identity(UA_ServerConfig *cfg) {
    UA_BuildInfo_clear(&cfg->buildInfo);
    cfg->buildInfo.productUri = UA_STRING_ALLOC(O6_PRODUCT_URI);
    cfg->buildInfo.manufacturerName = UA_STRING_ALLOC(O6_MANUFACTURER_NAME);
    cfg->buildInfo.productName = UA_STRING_ALLOC(O6_PRODUCT_NAME);
    cfg->buildInfo.softwareVersion = o6_software_version();
    cfg->buildInfo.buildNumber = UA_STRING_ALLOC(__DATE__ " " __TIME__);
    cfg->buildInfo.buildDate = o6_build_date();

    UA_ApplicationDescription *ad = &cfg->applicationDescription;
    o6_set_default_application_uri(&ad->applicationUri);
    UA_String_clear(&ad->productUri);
    ad->productUri = UA_STRING_ALLOC(O6_PRODUCT_URI);
    UA_LocalizedText_clear(&ad->applicationName);
    ad->applicationName = UA_LOCALIZEDTEXT_ALLOC("en", O6_APPLICATION_NAME);
}

/* PubSub can only be enabled when the active Credential entitles it */
static void
clamp_pubsub(UA_ServerConfig *cfg) {
#ifdef UA_ENABLE_PUBSUB
    cfg->pubsubEnabled = cfg->pubsubEnabled && pubsub_enabled;
    cfg->pubSubConfig.componentLifecycleCallback =
        pubsub_enabled ? pyPubSubComponentLifecycle : NULL;
#ifdef UA_ENABLE_PUBSUB_INFORMATIONMODEL
    if(!pubsub_enabled)
        cfg->pubSubConfig.enableInformationModelMethods = false;
#endif
#endif
}

static void
restore_o6_config_invariants(UA_ServerConfig *cfg) {
    o6_server_config_set_identity(cfg);
    cfg->copyMethodsOnInstances = true;
#ifdef UA_ENABLE_PUBSUB
    cfg->pubsubEnabled = true;
#endif
    clamp_pubsub(cfg);
}

static bool
config_writable(const PyServerConfig *self, const char *name);

/* --- Logger --- */
static int
PyServerConfig_set_logger(PyServerConfig *self, PyObject *value, void *closure) {
    O6_REQUIRE_WRITABLE_CONFIG(config_writable(self, "logger"),
                               pyServerConfig_eventLoop(self), -1);
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }

    UA_Logger *logging = pyLogger(value);
    if (!logging) {
        PyErr_SetString(PyExc_RuntimeError, "Could not create the logger");
        return -1;
    }

    if (cfg->logging && cfg->logging->clear)
        cfg->logging->clear(cfg->logging);

    cfg->logging = logging;
    return 0;
}

/* --- Application Description --- */
static PyObject *
PyServerConfig_get_applicationDescription(PyServerConfig *self, void *closure) {
    O6_REQUIRE_LOOP_THREAD(pyServerConfig_eventLoop(self), NULL);
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    UA_ApplicationDescription copy;
    UA_ApplicationDescription_init(&copy);
    UA_StatusCode status = UA_ApplicationDescription_copy(
        &cfg->applicationDescription, &copy);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    PyObject *result = UA2PY(
        &copy, &UA_TYPES[UA_TYPES_APPLICATIONDESCRIPTION],
        &self->py_server->nsMapPy2UA);
    UA_ApplicationDescription_clear(&copy);
    return result;
}

static int
PyServerConfig_set_applicationDescription(PyServerConfig *self, PyObject *value,
                                          void *closure) {
    O6_REQUIRE_WRITABLE_CONFIG(pyServerConfig_notRunning(self, "modify", "applicationDescription"),
                               pyServerConfig_eventLoop(self), -1);
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }
    if (self->py_server->running) {
        PyErr_SetString(PyExc_RuntimeError,
                        "Cannot modify applicationDescription while server is running");
        return -1;
    }

    UA_ApplicationDescription tmp;
    PyObject *out = PY2UA(
        value, &tmp, &UA_TYPES[UA_TYPES_APPLICATIONDESCRIPTION],
        &self->py_server->nsMapPy2UA, cfg->customDataTypes);
    if (!out)
        return -1;

    UA_ApplicationDescription_clear(&cfg->applicationDescription);
    cfg->applicationDescription = tmp;
    return 0;
}

/* Lock-free part of config_require_stopped, checked before the loop-thread
 * guard so that a write while the server runs reports that from any thread.
 * Python sets configLocked from start() until shutdown completes. */
static bool
config_writable(const PyServerConfig *self, const char *name) {
    const PyServer *server = self->py_server;
    if(!server || !(server->configLocked || server->running))
        return true;
    PyErr_Format(PyExc_RuntimeError,
                 "Cannot modify %s unless the server is fully stopped", name);
    return false;
}

/* Before taking the lock after a conversion that can run user code, which
 * may start the server: the lifecycle check, then the loop-thread guard. */
static int
config_recheck(PyServerConfig *self, const char *name) {
    if(!config_writable(self, name))
        return -1;
    return o6_require_loop_thread(pyServerConfig_eventLoop(self));
}

/* --- Build Info (Server/ServerStatus/BuildInfo) --- */
static int config_require_stopped(PyServerConfig *self, const char *name);

static PyObject *
PyServerConfig_get_buildInfo(PyServerConfig *self, void *closure) {
    O6_REQUIRE_LOOP_THREAD(pyServerConfig_eventLoop(self), NULL);
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    UA_BuildInfo copy;
    UA_BuildInfo_init(&copy);
    lockServer(self->py_server->server);
    UA_StatusCode status = UA_BuildInfo_copy(&cfg->buildInfo, &copy);
    unlockServer(self->py_server->server);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    PyObject *result = UA2PY(&copy, &UA_TYPES[UA_TYPES_BUILDINFO],
                             &self->py_server->nsMapPy2UA);
    UA_BuildInfo_clear(&copy);
    return result;
}

static int
PyServerConfig_set_buildInfo(PyServerConfig *self, PyObject *value, void *closure) {
    O6_REQUIRE_WRITABLE_CONFIG(config_writable(self, "buildInfo"),
                               pyServerConfig_eventLoop(self), -1);
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }

    if (PY2UAType(Py_TYPE(value)) != &UA_TYPES[UA_TYPES_BUILDINFO]) {
        PyErr_SetString(PyExc_TypeError,
                        "buildInfo must be an o6.ns.ns0.datatypes.BuildInfo");
        return -1;
    }

    UA_BuildInfo tmp;
    UA_BuildInfo_init(&tmp);
    if (!PY2UA(value, &tmp, &UA_TYPES[UA_TYPES_BUILDINFO],
               &self->py_server->nsMapPy2UA, cfg->customDataTypes)) {
        UA_BuildInfo_clear(&tmp);
        return -1;
    }

    /* The conversion can run user code; check the lifecycle afterwards */
    if(config_recheck(self, "buildInfo") < 0) {
        UA_BuildInfo_clear(&tmp);
        return -1;
    }
    lockServer(self->py_server->server);
    int allowed = config_require_stopped(self, "buildInfo");
    if(allowed == 0) {
        UA_BuildInfo_clear(&cfg->buildInfo);
        cfg->buildInfo = tmp;
        UA_BuildInfo_init(&tmp);
    }
    unlockServer(self->py_server->server);
    UA_BuildInfo_clear(&tmp);
    return allowed;
}

/* --- Application URI --- */
static PyObject *
PyServerConfig_get_applicationUri(PyServerConfig *self, void *closure) {
    O6_REQUIRE_LOOP_THREAD(pyServerConfig_eventLoop(self), NULL);
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    if (cfg->applicationDescription.applicationUri.length == 0)
        return PyUnicode_FromString("");
    return PyUnicode_FromStringAndSize(
        (const char *)cfg->applicationDescription.applicationUri.data,
        cfg->applicationDescription.applicationUri.length);
}

static int
PyServerConfig_set_applicationUri(PyServerConfig *self, PyObject *value,
                                  void *closure) {
    O6_REQUIRE_WRITABLE_CONFIG(pyServerConfig_notRunning(self, "modify", "application_uri"),
                               pyServerConfig_eventLoop(self), -1);
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }
    if (self->py_server->running) {
        PyErr_SetString(PyExc_RuntimeError,
                        "Cannot modify application_uri while server is running");
        return -1;
    }
    if (!PyUnicode_Check(value)) {
        PyErr_SetString(PyExc_TypeError, "application_uri must be str");
        return -1;
    }
    const char *uri = PyUnicode_AsUTF8(value);
    UA_String_clear(&cfg->applicationDescription.applicationUri);
    cfg->applicationDescription.applicationUri = UA_STRING_ALLOC(uri);
    return 0;
}

static PyObject *
PyServerConfig_get_allow_none_policy_password(PyServerConfig *self, void *closure) {
    O6_REQUIRE_LOOP_THREAD(pyServerConfig_eventLoop(self), NULL);
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    return PyBool_FromLong(cfg->allowNonePolicyPassword);
}

static int
PyServerConfig_set_allow_none_policy_password(PyServerConfig *self,
                                               PyObject *value, void *closure) {
    O6_REQUIRE_WRITABLE_CONFIG(pyServerConfig_notRunning(self, "modify", "allow_none_policy_password"),
                               pyServerConfig_eventLoop(self), -1);
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }
    if (self->py_server->running) {
        PyErr_SetString(PyExc_RuntimeError,
                        "Cannot modify allow_none_policy_password while server is running");
        return -1;
    }
    int enabled = PyObject_IsTrue(value);
    if (enabled < 0)
        return -1;
    cfg->allowNonePolicyPassword = enabled ? true : false;
    return 0;
}

static int config_require_stopped(PyServerConfig *self, const char *name);

static PyObject *
PyServerConfig_get_verify_request_timestamp(PyServerConfig *self, void *closure) {
    O6_REQUIRE_LOOP_THREAD(pyServerConfig_eventLoop(self), NULL);
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    return PyBool_FromLong(cfg->verifyRequestTimestamp == UA_RULEHANDLING_DEFAULT ||
                           cfg->verifyRequestTimestamp == UA_RULEHANDLING_ABORT);
}

static int
PyServerConfig_set_verify_request_timestamp(PyServerConfig *self,
                                            PyObject *value, void *closure) {
    O6_REQUIRE_WRITABLE_CONFIG(config_writable(self, "verifyRequestTimestamp"),
                               pyServerConfig_eventLoop(self), -1);
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }
    if (!PyBool_Check(value)) {
        PyErr_SetString(PyExc_TypeError, "verifyRequestTimestamp must be bool");
        return -1;
    }
    lockServer(self->py_server->server);
    int allowed = config_require_stopped(self, "verifyRequestTimestamp");
    if(allowed == 0)
        cfg->verifyRequestTimestamp =
            (value == Py_True) ? UA_RULEHANDLING_ABORT : UA_RULEHANDLING_WARN;
    unlockServer(self->py_server->server);
    return allowed;
}

static PyObject *
PyServerConfig_get_auditing_enabled(PyServerConfig *self, void *closure) {
    O6_REQUIRE_LOOP_THREAD(pyServerConfig_eventLoop(self), NULL);
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    return PyBool_FromLong(cfg->auditingEnabled);
}

static int
PyServerConfig_set_auditing_enabled(PyServerConfig *self, PyObject *value, void *closure) {
    O6_REQUIRE_WRITABLE_CONFIG(config_writable(self, "auditingEnabled"),
                               pyServerConfig_eventLoop(self), -1);
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }
    int enabled = PyObject_IsTrue(value);
    if (enabled < 0)
        return -1;
    cfg->auditingEnabled = enabled ? true : false;
    return 0;
}

static PyObject *
PyServerConfig_get_copy_methods_on_instances(PyServerConfig *self, void *closure) {
    O6_REQUIRE_LOOP_THREAD(pyServerConfig_eventLoop(self), NULL);
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    return PyBool_FromLong(cfg->copyMethodsOnInstances);
}

static PyObject *
PyServerConfig_get_application_type(PyServerConfig *self, void *closure) {
    O6_REQUIRE_LOOP_THREAD(pyServerConfig_eventLoop(self), NULL);
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    return PyLong_FromLong((long)cfg->applicationDescription.applicationType);
}

static int
PyServerConfig_set_application_type(PyServerConfig *self, PyObject *value, void *closure) {
    O6_REQUIRE_WRITABLE_CONFIG(config_writable(self, "applicationType"),
                               pyServerConfig_eventLoop(self), -1);
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }
    long type = PyLong_AsLong(value);
    if (type == -1 && PyErr_Occurred())
        return -1;
    if (type < UA_APPLICATIONTYPE_SERVER || type > UA_APPLICATIONTYPE_DISCOVERYSERVER) {
        PyErr_SetString(PyExc_ValueError, "applicationType must be an ns0 ApplicationType member");
        return -1;
    }
    cfg->applicationDescription.applicationType = (UA_ApplicationType)type;
    /* open62541 no longer derives registration management from the
     * ApplicationType; a discovery server needs it enabled explicitly. */
    cfg->registeredServersEnabled = (type == UA_APPLICATIONTYPE_DISCOVERYSERVER);
    return 0;
}

static PyObject *
PyServerConfig_get_registered_servers_enabled(PyServerConfig *self, void *closure) {
    O6_REQUIRE_LOOP_THREAD(pyServerConfig_eventLoop(self), NULL);
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    return PyBool_FromLong(cfg->registeredServersEnabled);
}

static int
PyServerConfig_set_registered_servers_enabled(PyServerConfig *self, PyObject *value,
                                              void *closure) {
    O6_REQUIRE_WRITABLE_CONFIG(config_writable(self, "registeredServersEnabled"),
                               pyServerConfig_eventLoop(self), -1);
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }
    int enabled = PyObject_IsTrue(value);
    if (enabled < 0)
        return -1;
    cfg->registeredServersEnabled = enabled ? true : false;
    return 0;
}

static PyObject *
PyServerConfig_get_servers_on_network_enabled(PyServerConfig *self, void *closure) {
    O6_REQUIRE_LOOP_THREAD(pyServerConfig_eventLoop(self), NULL);
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    return PyBool_FromLong(cfg->serversOnNetworkEnabled);
}

static int
PyServerConfig_set_servers_on_network_enabled(PyServerConfig *self, PyObject *value,
                                              void *closure) {
    O6_REQUIRE_WRITABLE_CONFIG(config_writable(self, "serversOnNetworkEnabled"),
                               pyServerConfig_eventLoop(self), -1);
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }
    int enabled = PyObject_IsTrue(value);
    if (enabled < 0)
        return -1;
    cfg->serversOnNetworkEnabled = enabled ? true : false;
    return 0;
}

static PyObject *
PyServerConfig_get_history_enabled(PyServerConfig *self, void *closure) {
    O6_REQUIRE_LOOP_THREAD(pyServerConfig_eventLoop(self), NULL);
    (void)closure;
    if (!self->py_server)
        Py_RETURN_FALSE;
    return PyBool_FromLong(pyHistory_enabled(&self->py_server->history));
}

/* --- Native limits and listener configuration --- */
typedef enum {
    CONFIG_UINT16, CONFIG_UINT32, CONFIG_DURATION, CONFIG_BOOL,
    CONFIG_DURATION_RANGE, CONFIG_UINT32_RANGE, CONFIG_URLS, CONFIG_CAPABILITIES,
    CONFIG_RULE
} ConfigKind;

typedef struct {
    const char *name;
    ConfigKind kind;
    size_t offset;
} ConfigProperty;

#define CONFIG_PROPERTY(NAME, KIND) \
    static const ConfigProperty prop_##NAME = {#NAME, KIND, offsetof(UA_ServerConfig, NAME)}

CONFIG_PROPERTY(certificateEkuRule, CONFIG_RULE);
CONFIG_PROPERTY(maxSessions, CONFIG_UINT16);
CONFIG_PROPERTY(maxSessionTimeout, CONFIG_DURATION);
CONFIG_PROPERTY(shutdownDelay, CONFIG_DURATION);
CONFIG_PROPERTY(maxMonitoredItemsPerCall, CONFIG_UINT32);
CONFIG_PROPERTY(maxNodesPerRead, CONFIG_UINT32);
CONFIG_PROPERTY(maxNodesPerWrite, CONFIG_UINT32);
CONFIG_PROPERTY(maxNodesPerMethodCall, CONFIG_UINT32);
CONFIG_PROPERTY(maxNodesPerBrowse, CONFIG_UINT32);
CONFIG_PROPERTY(maxNodesPerRegisterNodes, CONFIG_UINT32);
CONFIG_PROPERTY(maxNodesPerTranslateBrowsePathsToNodeIds, CONFIG_UINT32);
CONFIG_PROPERTY(maxNodesPerNodeManagement, CONFIG_UINT32);
CONFIG_PROPERTY(serverUrls, CONFIG_URLS);
CONFIG_PROPERTY(serverCapabilities, CONFIG_CAPABILITIES);
#ifdef UA_ENABLE_SUBSCRIPTIONS
CONFIG_PROPERTY(maxSubscriptions, CONFIG_UINT32);
CONFIG_PROPERTY(maxSubscriptionsPerSession, CONFIG_UINT32);
CONFIG_PROPERTY(maxMonitoredItems, CONFIG_UINT32);
CONFIG_PROPERTY(maxMonitoredItemsPerSubscription, CONFIG_UINT32);
CONFIG_PROPERTY(samplingIntervalLimits, CONFIG_DURATION_RANGE);
CONFIG_PROPERTY(publishingIntervalLimits, CONFIG_DURATION_RANGE);
CONFIG_PROPERTY(queueSizeLimits, CONFIG_UINT32_RANGE);
CONFIG_PROPERTY(lifeTimeCountLimits, CONFIG_UINT32_RANGE);
CONFIG_PROPERTY(keepAliveCountLimits, CONFIG_UINT32_RANGE);
CONFIG_PROPERTY(maxPublishReqPerSession, CONFIG_UINT32);
CONFIG_PROPERTY(maxNotificationsPerPublish, CONFIG_UINT32);
CONFIG_PROPERTY(enableRetransmissionQueue, CONFIG_BOOL);
#endif
#undef CONFIG_PROPERTY

/* Call with the server lock held, including after Python conversions which can
 * execute user code and start the server. */
static int
config_require_stopped(PyServerConfig *self, const char *name) {
    PyServer *server = self->py_server;
    UA_ServerConfig *cfg = get_config(self);
    if(server->configLocked || server->configChanging || server->running ||
       server->server->state != UA_LIFECYCLESTATE_STOPPED ||
       (cfg->eventLoop && cfg->eventLoop->state == UA_EVENTLOOPSTATE_STOPPING)) {
        PyErr_Format(PyExc_RuntimeError,
                     "Cannot modify %s unless the server is fully stopped", name);
        return -1;
    }
    return 0;
}

typedef union {
    UA_RuleHandling rule;
    UA_UInt16 u16;
    UA_UInt32 u32;
    UA_UInt64 capabilities;
    UA_Double duration;
    UA_Boolean boolean;
    UA_DurationRange durations;
    UA_UInt32Range counts;
} ConfigValue;

static size_t
config_value_size(ConfigKind kind) {
    switch(kind) {
    case CONFIG_RULE: return sizeof(UA_RuleHandling);
    case CONFIG_UINT16: return sizeof(UA_UInt16);
    case CONFIG_UINT32: return sizeof(UA_UInt32);
    case CONFIG_CAPABILITIES: return sizeof(UA_UInt64);
    case CONFIG_DURATION: return sizeof(UA_Double);
    case CONFIG_BOOL: return sizeof(UA_Boolean);
    case CONFIG_DURATION_RANGE: return sizeof(UA_DurationRange);
    case CONFIG_UINT32_RANGE: return sizeof(UA_UInt32Range);
    case CONFIG_URLS: return 0;
    }
    return 0;
}

static PyObject *
PyServerConfig_get_native(PyServerConfig *self, void *closure) {
    O6_REQUIRE_LOOP_THREAD(pyServerConfig_eventLoop(self), NULL);
    const ConfigProperty *prop = closure;
    UA_ServerConfig *cfg = get_config(self);
    if(!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    ConfigValue value;
    UA_String *urls = NULL;
    size_t size = 0;
    UA_StatusCode status = UA_STATUSCODE_GOOD;
    /* lockServer enters the asyncio event-loop lock, which releases the GIL
     * while waiting. Never wait on the service mutex alone with the GIL held. */
    lockServer(self->py_server->server);
    if(prop->kind == CONFIG_URLS) {
        size = cfg->serverUrlsSize;
        status = UA_Array_copy(cfg->serverUrls, size, (void**)&urls,
                               &UA_TYPES[UA_TYPES_STRING]);
    } else {
        memcpy(&value, (char*)cfg + prop->offset, config_value_size(prop->kind));
    }
    unlockServer(self->py_server->server);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    switch(prop->kind) {
    case CONFIG_RULE:
        switch(value.rule) {
        case UA_RULEHANDLING_DEFAULT: return PyUnicode_FromString("default");
        case UA_RULEHANDLING_ABORT: return PyUnicode_FromString("abort");
        case UA_RULEHANDLING_WARN: return PyUnicode_FromString("warn");
        case UA_RULEHANDLING_ACCEPT: return PyUnicode_FromString("accept");
        }
        PyErr_SetString(PyExc_RuntimeError, "Unknown native rule handling value");
        return NULL;
    case CONFIG_UINT16: return PyLong_FromUnsignedLong(value.u16);
    case CONFIG_UINT32: return PyLong_FromUnsignedLong(value.u32);
    case CONFIG_CAPABILITIES: {
        UA_String identifiers[UA_SERVERCAPABILITIES_MAX];
        size_t count = getServerCapabilityIdentifiers(value.capabilities, identifiers);
        PyObject *result = PyList_New((Py_ssize_t)count);
        if(!result)
            return NULL;
        for(size_t i = 0; i < count; i++) {
            PyObject *identifier = PyUnicode_FromStringAndSize(
                (const char*)identifiers[i].data, (Py_ssize_t)identifiers[i].length);
            if(!identifier) {
                Py_DECREF(result);
                return NULL;
            }
            PyList_SET_ITEM(result, (Py_ssize_t)i, identifier);
        }
        return result;
    }
    case CONFIG_DURATION: return PyFloat_FromDouble(value.duration);
    case CONFIG_BOOL: return PyBool_FromLong(value.boolean);
    case CONFIG_DURATION_RANGE:
        return Py_BuildValue("(dd)", value.durations.min, value.durations.max);
    case CONFIG_UINT32_RANGE:
        return Py_BuildValue("(kk)", (unsigned long)value.counts.min,
                             (unsigned long)value.counts.max);
    case CONFIG_URLS: {
        PyObject *result = PyList_New((Py_ssize_t)size);
        if(result) {
            for(size_t i = 0; i < size; i++) {
                PyObject *url = PyUnicode_FromStringAndSize(
                    (const char*)urls[i].data, (Py_ssize_t)urls[i].length);
                if(!url) {
                    Py_CLEAR(result);
                    break;
                }
                PyList_SET_ITEM(result, (Py_ssize_t)i, url);
            }
        }
        UA_Array_delete(urls, size, &UA_TYPES[UA_TYPES_STRING]);
        return result;
    }
    }
    Py_UNREACHABLE();
}

static int
config_unsigned(PyObject *value, unsigned long long max,
                UA_UInt32 *result, const char *name) {
    unsigned long long number = PyLong_AsUnsignedLongLong(value);
    if(PyErr_Occurred())
        return -1;
    if(number > max) {
        PyErr_Format(PyExc_OverflowError, "%s exceeds its native unsigned integer width", name);
        return -1;
    }
    *result = (UA_UInt32)number;
    return 0;
}

static int
config_duration(PyObject *value, UA_Double *result, const char *name) {
    double number = PyFloat_AsDouble(value);
    if(PyErr_Occurred())
        return -1;
    if(!isfinite(number) || number < 0) {
        PyErr_Format(PyExc_ValueError, "%s must be finite and non-negative (milliseconds)", name);
        return -1;
    }
    *result = number;
    return 0;
}

static PyObject *
config_sequence(PyObject *value, const char *name) {
    if(!PyTuple_Check(value) && !PyList_Check(value)) {
        PyErr_Format(PyExc_TypeError, "%s must be a tuple or list", name);
        return NULL;
    }
    return PySequence_Tuple(value);
}

static int
config_capabilities(PyObject *value, UA_UInt64 *out) {
    PyObject *items = config_sequence(value, "serverCapabilities");
    if(!items)
        return -1;
    UA_UInt64 capabilities = 0;
    int result = -1;
    for(Py_ssize_t i = 0; i < PyTuple_GET_SIZE(items); i++) {
        PyObject *item = PyTuple_GET_ITEM(items, i);
        if(!PyUnicode_Check(item)) {
            PyErr_SetString(PyExc_TypeError, "serverCapabilities entries must be str");
            goto done;
        }
        Py_ssize_t length;
        const char *text = PyUnicode_AsUTF8AndSize(item, &length);
        if(!text)
            goto done;
        UA_String identifier = {(size_t)length, (UA_Byte*)text};
        UA_UInt64 capability = getServerCapability(&identifier);
        if(!capability) {
            PyErr_Format(PyExc_ValueError, "Unknown server capability: %R", item);
            goto done;
        }
        capabilities |= capability;
    }
    *out = capabilities;
    result = 0;
 done:
    Py_DECREF(items);
    return result;
}

static int
config_range(PyObject *value, const ConfigProperty *prop, ConfigValue *out) {
    PyObject *items = config_sequence(value, prop->name);
    if(!items)
        return -1;
    int result = -1;
    if(PyTuple_GET_SIZE(items) != 2) {
        PyErr_Format(PyExc_ValueError, "%s requires exactly (min, max)", prop->name);
        goto done;
    }
    PyObject *min = PyTuple_GET_ITEM(items, 0);
    PyObject *max = PyTuple_GET_ITEM(items, 1);
    if(prop->kind == CONFIG_DURATION_RANGE) {
        if(config_duration(min, &out->durations.min, prop->name) < 0 ||
           config_duration(max, &out->durations.max, prop->name) < 0)
            goto done;
        if(out->durations.min <= out->durations.max)
            result = 0;
    } else {
        if(config_unsigned(min, UA_UINT32_MAX, &out->counts.min, prop->name) < 0 ||
           config_unsigned(max, UA_UINT32_MAX, &out->counts.max, prop->name) < 0)
            goto done;
        if(out->counts.min <= out->counts.max)
            result = 0;
    }
    if(result < 0)
        PyErr_Format(PyExc_ValueError, "%s requires min <= max", prop->name);
 done:
    Py_DECREF(items);
    return result;
}

static int
config_urls(PyObject *value, UA_String **urls, size_t *size) {
    PyObject *items = config_sequence(value, "serverUrls");
    if(!items)
        return -1;
    *size = (size_t)PyTuple_GET_SIZE(items);
    *urls = (UA_String*)UA_Array_new(*size, &UA_TYPES[UA_TYPES_STRING]);
    if(!*urls) {
        Py_DECREF(items);
        PyErr_NoMemory();
        return -1;
    }
    int result = -1;
    for(size_t i = 0; i < *size; i++) {
        PyObject *item = PyTuple_GET_ITEM(items, (Py_ssize_t)i);
        if(!PyUnicode_Check(item)) {
            PyErr_SetString(PyExc_TypeError, "serverUrls entries must be str");
            goto done;
        }
        Py_ssize_t length;
        const char *text = PyUnicode_AsUTF8AndSize(item, &length);
        if(!text)
            goto done;
        UA_String source = {(size_t)length, (UA_Byte*)text};
        UA_StatusCode status = UA_String_copy(&source, &(*urls)[i]);
        if(status != UA_STATUSCODE_GOOD) {
            PyErr_NoMemory();
            goto done;
        }
    }
    result = 0;
 done:
    Py_DECREF(items);
    return result;
}

static int
PyServerConfig_set_native(PyServerConfig *self, PyObject *value, void *closure) {
    O6_REQUIRE_WRITABLE_CONFIG(config_writable(self, ((const ConfigProperty *)closure)->name),
                               pyServerConfig_eventLoop(self), -1);
    const ConfigProperty *prop = closure;
    if(!value) {
        PyErr_SetString(PyExc_AttributeError, "Cannot delete configuration properties");
        return -1;
    }
    UA_ServerConfig *cfg = get_config(self);
    if(!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return -1;
    }
    lockServer(self->py_server->server);
    int allowed = config_require_stopped(self, prop->name);
    unlockServer(self->py_server->server);
    if(allowed < 0)
        return -1;

    ConfigValue converted;
    UA_String *urls = NULL;
    size_t size = 0;
    UA_UInt32 integer;
    switch(prop->kind) {
    case CONFIG_RULE: {
        if(!PyUnicode_Check(value)) {
            PyErr_Format(PyExc_TypeError, "%s must be str", prop->name);
            return -1;
        }
        Py_ssize_t length;
        const char *text = PyUnicode_AsUTF8AndSize(value, &length);
        if(!text)
            return -1;
        if(length == 7 && memcmp(text, "default", 7) == 0)
            converted.rule = UA_RULEHANDLING_DEFAULT;
        else if(length == 5 && memcmp(text, "abort", 5) == 0)
            converted.rule = UA_RULEHANDLING_ABORT;
        else if(length == 4 && memcmp(text, "warn", 4) == 0)
            converted.rule = UA_RULEHANDLING_WARN;
        else if(length == 6 && memcmp(text, "accept", 6) == 0)
            converted.rule = UA_RULEHANDLING_ACCEPT;
        else {
            PyErr_Format(PyExc_ValueError,
                         "%s must be 'default', 'abort', 'warn' or 'accept'", prop->name);
            return -1;
        }
        break;
    }
    case CONFIG_UINT16:
        if(config_unsigned(value, UA_UINT16_MAX, &integer, prop->name) < 0)
            return -1;
        converted.u16 = (UA_UInt16)integer;
        break;
    case CONFIG_UINT32:
        if(config_unsigned(value, UA_UINT32_MAX, &converted.u32, prop->name) < 0)
            return -1;
        break;
    case CONFIG_CAPABILITIES:
        if(config_capabilities(value, &converted.capabilities) < 0)
            return -1;
        break;
    case CONFIG_DURATION:
        if(config_duration(value, &converted.duration, prop->name) < 0)
            return -1;
        break;
    case CONFIG_BOOL:
        if(!PyBool_Check(value)) {
            PyErr_Format(PyExc_TypeError, "%s must be bool", prop->name);
            return -1;
        }
        converted.boolean = (value == Py_True);
        break;
    case CONFIG_DURATION_RANGE:
    case CONFIG_UINT32_RANGE:
        if(config_range(value, prop, &converted) < 0)
            return -1;
        break;
    case CONFIG_URLS:
        if(config_urls(value, &urls, &size) < 0) {
            if(urls)
                UA_Array_delete(urls, size, &UA_TYPES[UA_TYPES_STRING]);
            return -1;
        }
        break;
    }

    if(config_recheck(self, prop->name) < 0) {
        if(urls)
            UA_Array_delete(urls, size, &UA_TYPES[UA_TYPES_STRING]);
        return -1;
    }
    lockServer(self->py_server->server);
    allowed = config_require_stopped(self, prop->name);
    if(allowed == 0) {
        if(prop->kind == CONFIG_URLS) {
            UA_Array_delete(cfg->serverUrls, cfg->serverUrlsSize, &UA_TYPES[UA_TYPES_STRING]);
            cfg->serverUrls = urls;
            cfg->serverUrlsSize = size;
            urls = NULL;
        } else {
            memcpy((char*)cfg + prop->offset, &converted, config_value_size(prop->kind));
        }
    }
    unlockServer(self->py_server->server);
    if(urls)
        UA_Array_delete(urls, size, &UA_TYPES[UA_TYPES_STRING]);
    return allowed;
}

#define NATIVE_CONFIG(NAME, DOC) \
    {#NAME, (getter)PyServerConfig_get_native, (setter)PyServerConfig_set_native, \
     DOC "; writable only while fully stopped", (void*)&prop_##NAME}

/* --- Property Table --- */
static PyGetSetDef PyServerConfig_getset[] = {
    {"logger", NULL, (setter)PyServerConfig_set_logger, "logger", NULL},
    {"applicationDescription",
     (getter)PyServerConfig_get_applicationDescription,
     (setter)PyServerConfig_set_applicationDescription,
     "applicationDescription", NULL},
    {"applicationUri",
     (getter)PyServerConfig_get_applicationUri,
     (setter)PyServerConfig_set_applicationUri,
     "applicationUri", NULL},
    {"buildInfo",
     (getter)PyServerConfig_get_buildInfo,
     (setter)PyServerConfig_set_buildInfo,
     "BuildInfo of Server/ServerStatus (ns0 BuildInfo); writable only while fully stopped",
     NULL},
    {"allowNonePolicyPassword",
     (getter)PyServerConfig_get_allow_none_policy_password,
     (setter)PyServerConfig_set_allow_none_policy_password,
     "Allow password tokens on SecurityPolicy None endpoints", NULL},
    {"verifyRequestTimestamp",
     (getter)PyServerConfig_get_verify_request_timestamp,
     (setter)PyServerConfig_set_verify_request_timestamp,
     "Reject requests without a RequestHeader timestamp with BadInvalidTimestamp; "
     "if False, log a warning and continue; writable only while fully stopped", NULL},
    {"auditingEnabled",
     (getter)PyServerConfig_get_auditing_enabled,
     (setter)PyServerConfig_set_auditing_enabled,
     "Generate audit application notifications for security/management activity", NULL},
    {"copyMethodsOnInstances",
     (getter)PyServerConfig_get_copy_methods_on_instances, NULL,
     "Whether instances of an ObjectType get copies of its methods", NULL},
    {"applicationType",
     (getter)PyServerConfig_get_application_type,
     (setter)PyServerConfig_set_application_type,
     "Advertised ApplicationType (ns0 ApplicationType); DISCOVERYSERVER enables "
     "registeredServersEnabled, any other type disables it", NULL},
    {"registeredServersEnabled",
     (getter)PyServerConfig_get_registered_servers_enabled,
     (setter)PyServerConfig_set_registered_servers_enabled,
     "Manage RegisteredServers (RegisterServer/RegisterServer2, FindServers); "
     "set by applicationType, writable afterwards", NULL},
    {"serversOnNetworkEnabled",
     (getter)PyServerConfig_get_servers_on_network_enabled,
     (setter)PyServerConfig_set_servers_on_network_enabled,
     "Maintain the ServerOnNetwork record list (FindServersOnNetwork, mDNS discovery)", NULL},
    {"historyEnabled",
     (getter)PyServerConfig_get_history_enabled, NULL,
     "Whether setHistoryDatabase() has configured a history database", NULL},
    NATIVE_CONFIG(certificateEkuRule, "Certificate extended-key-usage handling: default, abort, warn or accept"),
    NATIVE_CONFIG(maxSessions, "Maximum sessions (UInt16); 0 = unlimited"),
    NATIVE_CONFIG(maxSessionTimeout, "Maximum session timeout in milliseconds; finite and non-negative"),
    NATIVE_CONFIG(shutdownDelay, "Time in milliseconds stop() keeps serving with ServerStatus/State Shutdown before shutting down; finite and non-negative; 0 = none"),
    NATIVE_CONFIG(maxMonitoredItemsPerCall, "Maximum monitored items per service call (UInt32); 0 = unlimited"),
    NATIVE_CONFIG(maxNodesPerRead, "Maximum nodes per Read call (UInt32); 0 = unlimited"),
    NATIVE_CONFIG(maxNodesPerWrite, "Maximum nodes per Write call (UInt32); 0 = unlimited"),
    NATIVE_CONFIG(maxNodesPerMethodCall, "Maximum methods per Call call (UInt32); 0 = unlimited"),
    NATIVE_CONFIG(maxNodesPerBrowse, "Maximum nodes per Browse call (UInt32); 0 = unlimited"),
    NATIVE_CONFIG(maxNodesPerRegisterNodes, "Maximum nodes per RegisterNodes and UnregisterNodes call (UInt32); 0 = unlimited"),
    NATIVE_CONFIG(maxNodesPerTranslateBrowsePathsToNodeIds, "Maximum browse paths per TranslateBrowsePathsToNodeIds call (UInt32); 0 = unlimited"),
    NATIVE_CONFIG(maxNodesPerNodeManagement, "Maximum nodes per AddNodes, AddReferences, DeleteNodes and DeleteReferences call (UInt32); 0 = unlimited"),
    NATIVE_CONFIG(serverUrls, "Detached list of listener URLs; assign a list/tuple of str; [] uses wildcard TCP port 4840"),
    NATIVE_CONFIG(serverCapabilities, "Detached list of configured Part 12 capability identifiers; assign a list/tuple of str; [] uses the ApplicationType default at startup"),
#ifdef UA_ENABLE_SUBSCRIPTIONS
    NATIVE_CONFIG(maxSubscriptions, "Maximum subscriptions across sessions (UInt32); 0 = unlimited"),
    NATIVE_CONFIG(maxSubscriptionsPerSession, "Maximum subscriptions per session (UInt32); 0 = unlimited"),
    NATIVE_CONFIG(maxMonitoredItems, "Maximum monitored items across subscriptions (UInt32); 0 = unlimited"),
    NATIVE_CONFIG(maxMonitoredItemsPerSubscription, "Maximum monitored items per subscription (UInt32); 0 = unlimited"),
    NATIVE_CONFIG(samplingIntervalLimits, "Sampling (min, max) in milliseconds; finite, non-negative and ordered"),
    NATIVE_CONFIG(publishingIntervalLimits, "Publishing (min, max) in milliseconds; finite, non-negative and ordered"),
    NATIVE_CONFIG(queueSizeLimits, "Negotiated queue size (min, max); ordered UInt32 pair"),
    NATIVE_CONFIG(lifeTimeCountLimits, "Subscription lifetime (min, max); ordered UInt32 pair of publishing cycles"),
    NATIVE_CONFIG(keepAliveCountLimits, "Keepalive (min, max); ordered UInt32 pair of publishing cycles"),
    NATIVE_CONFIG(maxPublishReqPerSession, "Maximum queued Publish requests per session (UInt32); 0 = unlimited"),
    NATIVE_CONFIG(maxNotificationsPerPublish, "Maximum notifications per Publish (UInt32); 0 does not mean unlimited"),
    NATIVE_CONFIG(enableRetransmissionQueue, "Enable notification retransmission queue (bool)"),
#endif
    {NULL}
};

/* Helper: convert Python list of bytes to UA_ByteString array. */
static UA_ByteString *
pyList_to_ByteStringArray(PyObject *list, size_t *out_size) {
    if (!list || list == Py_None) {
        *out_size = 0;
        return NULL;
    }
    if (!PyList_Check(list)) {
        PyErr_SetString(PyExc_TypeError, "expected a list of bytes");
        return NULL;
    }
    Py_ssize_t n = PyList_Size(list);
    if (n == 0) {
        *out_size = 0;
        return NULL;
    }
    UA_ByteString *arr = (UA_ByteString *)UA_calloc((size_t)n, sizeof(UA_ByteString));
    if (!arr) {
        PyErr_NoMemory();
        return NULL;
    }
    for (Py_ssize_t i = 0; i < n; i++) {
        PyObject *item = PyList_GetItem(list, i);
        if (!PyBytes_Check(item)) {
            for (Py_ssize_t j = 0; j < i; j++)
                UA_ByteString_clear(&arr[j]);
            UA_free(arr);
            PyErr_SetString(PyExc_TypeError, "list entries must be bytes");
            return NULL;
        }
        char *buf;
        Py_ssize_t len;
        PyBytes_AsStringAndSize(item, &buf, &len);
        arr[i].length = (size_t)len;
        arr[i].data = (UA_Byte *)UA_malloc((size_t)len);
        if (!arr[i].data) {
            for (Py_ssize_t j = 0; j < i; j++)
                UA_ByteString_clear(&arr[j]);
            UA_free(arr);
            PyErr_NoMemory();
            return NULL;
        }
        memcpy(arr[i].data, buf, (size_t)len);
    }
    *out_size = (size_t)n;
    return arr;
}

static void
free_ByteStringArray(UA_ByteString *arr, size_t size) {
    if (!arr) return;
    for (size_t i = 0; i < size; i++)
        UA_ByteString_clear(&arr[i]);
    UA_free(arr);
}

/* --- Security configuration --- */

/* Decode the private key to DER, as the open62541 default helpers do. A
 * password-protected key needs the privateKeyPasswordCallback of the config;
 * unlike those helpers, o6 never prompts for a password on stdin. */
static UA_StatusCode
decode_private_key(UA_ServerConfig *cfg, const UA_ByteString *key,
                   UA_ByteString *derKey) {
    UA_ByteString password = UA_BYTESTRING_NULL;
    UA_StatusCode res =
        UA_CertificateUtils_decryptPrivateKey(*key, password, derKey);
    if(res != UA_STATUSCODE_GOOD && cfg->privateKeyPasswordCallback) {
        res = cfg->privateKeyPasswordCallback(cfg, &password);
        if(res == UA_STATUSCODE_GOOD)
            res = UA_CertificateUtils_decryptPrivateKey(*key, password, derKey);
        UA_ByteString_memZero(&password);
        UA_ByteString_clear(&password);
    }
    if(res != UA_STATUSCODE_GOOD)
        UA_LOG_ERROR(cfg->logging, UA_LOGCATEGORY_APPLICATION,
                     "Could not decode the private key with status code %s",
                     UA_StatusCode_name(res));
    return res;
}

typedef UA_StatusCode (*AddSecurityPolicy)(UA_ServerConfig *config,
                                           const UA_ByteString *certificate,
                                           const UA_ByteString *privateKey);

/* The SecurityPolicies that Server(securityPolicies=...) can select */
enum {
    POLICY_NONE = 1 << 0,
    POLICY_BASIC128RSA15 = 1 << 1,
    POLICY_BASIC256 = 1 << 2,
    POLICY_BASIC256SHA256 = 1 << 3,
    POLICY_AES128SHA256RSAOAEP = 1 << 4,
    POLICY_AES256SHA256RSAPSS = 1 << 5
};
/* Deprecated by the OPC UA specification. Offered only when selected. */
#define POLICIES_DEPRECATED (POLICY_BASIC128RSA15 | POLICY_BASIC256)
#define POLICIES_RSA_DEFAULT \
    (POLICY_BASIC256SHA256 | POLICY_AES128SHA256RSAOAEP | POLICY_AES256SHA256RSAPSS)

#define SECURITY_POLICY_URI_PREFIX "http://opcfoundation.org/UA/SecurityPolicy#"

static const struct {
    const char *name;
    unsigned bit;
    AddSecurityPolicy add; /* NULL for None */
    UA_Byte deprecatedSecurityLevel; /* open62541 assigns 0 to deprecated policies */
} selectableSecurityPolicies[] = {
    {"None", POLICY_NONE, NULL, 0},
    {"Basic128Rsa15", POLICY_BASIC128RSA15,
     UA_ServerConfig_addSecurityPolicyBasic128Rsa15, 1},
    {"Basic256", POLICY_BASIC256, UA_ServerConfig_addSecurityPolicyBasic256, 2},
    {"Basic256Sha256", POLICY_BASIC256SHA256,
     UA_ServerConfig_addSecurityPolicyBasic256Sha256, 0},
    {"Aes256_Sha256_RsaPss", POLICY_AES256SHA256RSAPSS,
     UA_ServerConfig_addSecurityPolicyAes256Sha256RsaPss, 0},
    {"Aes128_Sha256_RsaOaep", POLICY_AES128SHA256RSAOAEP,
     UA_ServerConfig_addSecurityPolicyAes128Sha256RsaOaep, 0},
};
#define SELECTABLE_SECURITY_POLICIES \
    (sizeof(selectableSecurityPolicies) / sizeof(selectableSecurityPolicies[0]))

/* The index in selectableSecurityPolicies of a policy URI, or -1 for any other
 * policy, such as an ECC policy */
static int
selectable_policy_index(const UA_String *uri) {
    size_t prefix = sizeof(SECURITY_POLICY_URI_PREFIX) - 1;
    if(uri->length <= prefix || memcmp(uri->data, SECURITY_POLICY_URI_PREFIX, prefix) != 0)
        return -1;
    for(size_t i = 0; i < SELECTABLE_SECURITY_POLICIES; i++) {
        const char *name = selectableSecurityPolicies[i].name;
        if(uri->length - prefix == strlen(name) &&
           memcmp(uri->data + prefix, name, uri->length - prefix) == 0)
            return (int)i;
    }
    return -1;
}

/* Convert the securityPolicies argument to a bitmask. None selects the default:
 * the RSA policies, plus None unless secureOnly. */
static int
parse_security_policies(PyObject *policies, int secure_only,
                        unsigned *mask, int *selected) {
    *selected = 0;
    if(!policies || policies == Py_None) {
        *mask = POLICIES_RSA_DEFAULT | (secure_only ? 0 : POLICY_NONE);
        return 0;
    }
    if(secure_only) {
        PyErr_SetString(PyExc_ValueError,
                        "secureOnly and securityPolicies are mutually exclusive; "
                        "omit \"None\" from securityPolicies instead");
        return -1;
    }
    if(PyUnicode_Check(policies) || PyBytes_Check(policies)) {
        PyErr_SetString(PyExc_TypeError,
                        "securityPolicies must be an iterable of SecurityPolicy names, not a str");
        return -1;
    }
    PyObject *iterator = PyObject_GetIter(policies);
    if(!iterator)
        return -1;
    unsigned result = 0;
    PyObject *item;
    while((item = PyIter_Next(iterator))) {
        Py_ssize_t length = 0;
        const char *text = PyUnicode_Check(item) ? PyUnicode_AsUTF8AndSize(item, &length) : NULL;
        if(!text) {
            if(!PyErr_Occurred())
                PyErr_SetString(PyExc_TypeError, "securityPolicies entries must be str");
            Py_DECREF(item);
            Py_DECREF(iterator);
            return -1;
        }
        size_t prefix = sizeof(SECURITY_POLICY_URI_PREFIX) - 1;
        if((size_t)length > prefix && memcmp(text, SECURITY_POLICY_URI_PREFIX, prefix) == 0) {
            text += prefix;
            length -= (Py_ssize_t)prefix;
        }
        unsigned bit = 0;
        for(size_t i = 0; i < SELECTABLE_SECURITY_POLICIES; i++) {
            if((size_t)length == strlen(selectableSecurityPolicies[i].name) &&
               memcmp(text, selectableSecurityPolicies[i].name, (size_t)length) == 0)
                bit = selectableSecurityPolicies[i].bit;
        }
        if(!bit) {
            PyErr_Format(PyExc_ValueError,
                         "Unknown SecurityPolicy %R; expected one of None, Basic128Rsa15, "
                         "Basic256, Basic256Sha256, Aes128_Sha256_RsaOaep, "
                         "Aes256_Sha256_RsaPss", item);
            Py_DECREF(item);
            Py_DECREF(iterator);
            return -1;
        }
        result |= bit;
        Py_DECREF(item);
    }
    Py_DECREF(iterator);
    if(PyErr_Occurred())
        return -1;
    if(!result) {
        PyErr_SetString(PyExc_ValueError, "securityPolicies must not be empty");
        return -1;
    }
    *mask = result;
    *selected = 1;
    return 0;
}

/* open62541 gives the deprecated SecurityPolicies SecurityLevel 0, which
 * clients and the OPC Foundation CTT treat as unusable. A policy that was
 * selected on purpose gets a low, non-zero level, below the other policies. */
static void
set_deprecated_security_levels(UA_ServerConfig *cfg) {
    for(size_t i = 0; i < cfg->endpointsSize; i++) {
        int index = selectable_policy_index(&cfg->endpoints[i].securityPolicyUri);
        if(index >= 0 && (selectableSecurityPolicies[index].bit & POLICIES_DEPRECATED))
            cfg->endpoints[i].securityLevel =
                selectableSecurityPolicies[index].deprecatedSecurityLevel;
    }
}

/* Replace the SecurityPolicies. Without an explicit selection, the open62541
 * default set would also try the ECC policies, which fail with the usual RSA
 * application certificate and log a warning each. Therefore the default is the
 * RSA policies, and only a key that no RSA policy accepts falls back to the
 * open62541 set, which includes ECC. An explicit selection offers exactly the
 * selected policies, and one that cannot be added is an error. */
static UA_StatusCode
set_security_policies(UA_ServerConfig *cfg, const UA_ByteString *certificate,
                      const UA_ByteString *derKey, unsigned mask, int selected) {
    for(size_t i = 0; i < cfg->securityPoliciesSize; i++)
        cfg->securityPolicies[i].clear(&cfg->securityPolicies[i]);
    UA_free(cfg->securityPolicies);
    cfg->securityPolicies = NULL;
    cfg->securityPoliciesSize = 0;

    UA_StatusCode results[SELECTABLE_SECURITY_POLICIES];
    size_t added = 0;
    for(size_t i = 0; i < SELECTABLE_SECURITY_POLICIES; i++) {
        results[i] = UA_STATUSCODE_GOOD;
        if(!selectableSecurityPolicies[i].add || !(mask & selectableSecurityPolicies[i].bit))
            continue;
        results[i] = selectableSecurityPolicies[i].add(cfg, certificate, derKey);
        if(results[i] == UA_STATUSCODE_GOOD)
            added++;
    }
    UA_Boolean secureOnly = !(mask & POLICY_NONE);
    if(!selected && added == 0)
        return secureOnly ?
            UA_ServerConfig_addAllSecureSecurityPolicies(cfg, certificate, derKey) :
            UA_ServerConfig_addAllSecurityPolicies(cfg, certificate, derKey);

    UA_StatusCode failed = UA_STATUSCODE_GOOD;
    for(size_t i = 0; i < SELECTABLE_SECURITY_POLICIES; i++) {
        if(results[i] == UA_STATUSCODE_GOOD)
            continue;
        UA_LOG_WARNING(cfg->logging, UA_LOGCATEGORY_APPLICATION,
                       "Could not add SecurityPolicy#%s with error code %s",
                       selectableSecurityPolicies[i].name,
                       UA_StatusCode_name(results[i]));
        failed = UA_STATUSCODE_BADCONFIGURATIONERROR;
    }
    if(selected && failed != UA_STATUSCODE_GOOD)
        return failed;
    if(secureOnly)
        return UA_STATUSCODE_GOOD;
    return UA_ServerConfig_addSecurityPolicyNone(cfg, certificate);
}

/* Keep exactly the selected SecurityPolicies of a configuration that
 * open62541 populated, and remove the others together with their Endpoints. */
static UA_StatusCode
select_security_policies(UA_ServerConfig *cfg, unsigned mask) {
    unsigned present = 0;
    for(size_t i = 0; i < cfg->securityPoliciesSize; i++) {
        int index = selectable_policy_index(&cfg->securityPolicies[i].policyUri);
        if(index >= 0)
            present |= selectableSecurityPolicies[index].bit;
    }
    for(size_t i = 0; i < SELECTABLE_SECURITY_POLICIES; i++) {
        if((mask & selectableSecurityPolicies[i].bit) & ~present) {
            UA_LOG_ERROR(cfg->logging, UA_LOGCATEGORY_APPLICATION,
                         "SecurityPolicy#%s cannot be offered with this certificate and key",
                         selectableSecurityPolicies[i].name);
            return UA_STATUSCODE_BADCONFIGURATIONERROR;
        }
    }

    size_t kept = 0;
    for(size_t i = 0; i < cfg->endpointsSize; i++) {
        int index = selectable_policy_index(&cfg->endpoints[i].securityPolicyUri);
        if(index < 0 || !(mask & selectableSecurityPolicies[index].bit)) {
            UA_EndpointDescription_clear(&cfg->endpoints[i]);
            continue;
        }
        if(kept != i)
            cfg->endpoints[kept] = cfg->endpoints[i];
        kept++;
    }
    cfg->endpointsSize = kept;
    if(kept == 0) {
        UA_free(cfg->endpoints);
        cfg->endpoints = NULL;
    }

    /* The policies hold only owned heap contexts and no pointer to themselves,
     * so they can move within the array */
    kept = 0;
    for(size_t i = 0; i < cfg->securityPoliciesSize; i++) {
        int index = selectable_policy_index(&cfg->securityPolicies[i].policyUri);
        if(index < 0 || !(mask & selectableSecurityPolicies[index].bit)) {
            cfg->securityPolicies[i].clear(&cfg->securityPolicies[i]);
            continue;
        }
        if(kept != i)
            cfg->securityPolicies[kept] = cfg->securityPolicies[i];
        kept++;
    }
    cfg->securityPoliciesSize = kept;
    set_deprecated_security_levels(cfg);
    return UA_STATUSCODE_GOOD;
}

/* The default AccessControl copies every UserTokenPolicy once per
 * SecurityPolicy when no SecurityPolicyUri is given, and every Endpoint then
 * lists the same PolicyIds several times. The server replaces the
 * SecurityPolicyUri per Endpoint anyway, so any encrypting policy gives one
 * flat list. */
static const UA_String *
user_token_policy_uri(const UA_ServerConfig *cfg) {
    for(size_t i = 0; i < cfg->securityPoliciesSize; i++) {
        if(!UA_String_equal(&cfg->securityPolicies[i].policyUri,
                            &UA_SECURITY_POLICY_NONE_URI))
            return &cfg->securityPolicies[i].policyUri;
    }
    return NULL;
}

static UA_StatusCode
set_trust_list(UA_ServerConfig *cfg,
               const UA_ByteString *trustList, size_t trustSize,
               const UA_ByteString *issuerList, size_t issuerSize,
               const UA_ByteString *revocList, size_t revocSize) {
    cfg->maxRejectedListSize = O6_MAX_REJECTED_CERTIFICATES;
    UA_NodeId applicationGroup =
        UA_NS0ID(SERVERCONFIGURATION_CERTIFICATEGROUPS_DEFAULTAPPLICATIONGROUP);
    UA_NodeId userTokenGroup =
        UA_NS0ID(SERVERCONFIGURATION_CERTIFICATEGROUPS_DEFAULTUSERTOKENGROUP);
    UA_StatusCode res =
        o6_set_trust_list(&cfg->secureChannelPKI, &applicationGroup, cfg->logging,
                          trustList, trustSize, issuerList, issuerSize,
                          revocList, revocSize);
    if(res == UA_STATUSCODE_GOOD)
        res = o6_set_trust_list(&cfg->sessionPKI, &userTokenGroup, cfg->logging,
                                trustList, trustSize, issuerList, issuerSize,
                                revocList, revocSize);
    return res;
}

/* --- Rejected certificates --- */

/* Read one DER header within [p, end). Returns the start of the content. */
static const UA_Byte *
der_header(const UA_Byte *p, const UA_Byte *end, UA_Byte *tag, size_t *length) {
    if(end - p < 2)
        return NULL;
    *tag = p[0];
    size_t len = p[1];
    p += 2;
    if(len & 0x80) {
        size_t bytes = len & 0x7f;
        if(bytes == 0 || bytes > sizeof(size_t) || (size_t)(end - p) < bytes)
            return NULL;
        len = 0;
        for(size_t i = 0; i < bytes; i++)
            len = (len << 8) | *p++;
    }
    if((size_t)(end - p) < len)
        return NULL;
    *length = len;
    return p;
}

/* The ApplicationUri, the first URI of the SubjectAltName extension (OID
 * 2.5.29.17). open62541 only compares it, so walk the DER here. The result
 * points into the certificate. */
static UA_String
certificate_application_uri(const UA_ByteString *certificate) {
    static const UA_Byte subjectAltName[] = {0x06, 0x03, 0x55, 0x1d, 0x11};
    const UA_Byte *end = certificate->data + certificate->length;
    for(const UA_Byte *p = certificate->data;
        p && end - p > (ptrdiff_t)sizeof(subjectAltName); p++) {
        if(memcmp(p, subjectAltName, sizeof(subjectAltName)) != 0)
            continue;
        UA_Byte tag;
        size_t length;
        const UA_Byte *value = der_header(p + sizeof(subjectAltName), end, &tag, &length);
        if(value && tag == 0x01) /* critical */
            value = der_header(value + length, end, &tag, &length);
        if(!value || tag != 0x04) /* extnValue */
            continue;
        const UA_Byte *names = der_header(value, value + length, &tag, &length);
        if(!names || tag != 0x30) /* GeneralNames */
            continue;
        const UA_Byte *namesEnd = names + length;
        while(names < namesEnd) {
            const UA_Byte *name = der_header(names, namesEnd, &tag, &length);
            if(!name)
                break;
            if(tag == 0x86) /* uniformResourceIdentifier */
                return (UA_String){length, (UA_Byte *)(uintptr_t)name};
            names = name + length;
        }
    }
    return UA_STRING_NULL;
}

/* Log a rejected certificate and pass it to Server.onCertificateRejected.
 * The core logs the rejection without naming the certificate. */
static void
report_rejected_certificate(PyServer *server, const UA_ServerConfig *cfg,
                            const char *kind, const UA_ByteString *certificate,
                            UA_StatusCode status) {
    UA_ByteString cert = *certificate;
    UA_String subject = UA_STRING_NULL;
    UA_CertificateUtils_getSubjectName(&cert, &subject);
    UA_Byte thumbprintData[40];
    UA_String thumbprint = {sizeof(thumbprintData), thumbprintData};
    if(UA_CertificateUtils_getThumbprint(&cert, &thumbprint) != UA_STATUSCODE_GOOD)
        thumbprint = UA_STRING_NULL;
    UA_String uri = certificate_application_uri(certificate);
    UA_LOG_WARNING(cfg->logging, UA_LOGCATEGORY_SECURITYPOLICY,
                   "Rejected the %s certificate %S (ApplicationUri %S, "
                   "thumbprint %S) with StatusCode %s", kind, subject, uri,
                   thumbprint, UA_StatusCode_name(status));
    UA_String_clear(&subject);

    PyGILState_STATE gil = PyGILState_Ensure();
    PyObject *result = PyObject_CallMethod(
        (PyObject *)server, "_certificate_rejected", "y#k",
        (const char *)certificate->data, (Py_ssize_t)certificate->length,
        (unsigned long)status);
    if(result)
        Py_DECREF(result);
    else if(PyErr_ExceptionMatches(PyExc_AttributeError))
        PyErr_Clear(); /* a native server without the Python layer */
    else
        PyErr_Print();
    PyGILState_Release(gil);
}

/* The core passes &config->secureChannelPKI or &config->sessionPKI */
static UA_StatusCode
verify_application_certificate(UA_CertificateGroup *group,
                               const UA_ByteString *certificate) {
    UA_ServerConfig *cfg = (UA_ServerConfig *)
        ((char *)group - offsetof(UA_ServerConfig, secureChannelPKI));
    PyServer *server = (PyServer *)cfg->context;
    if(!server || !server->verifyApplicationCertificate)
        return UA_STATUSCODE_BADINTERNALERROR;
    UA_StatusCode status = server->verifyApplicationCertificate(group, certificate);
    if(status != UA_STATUSCODE_GOOD)
        report_rejected_certificate(server, cfg, "application", certificate, status);
    return status;
}

static UA_StatusCode
verify_user_certificate(UA_CertificateGroup *group, const UA_ByteString *certificate) {
    UA_ServerConfig *cfg = (UA_ServerConfig *)
        ((char *)group - offsetof(UA_ServerConfig, sessionPKI));
    PyServer *server = (PyServer *)cfg->context;
    if(!server || !server->verifyUserCertificate)
        return UA_STATUSCODE_BADINTERNALERROR;
    UA_StatusCode status = server->verifyUserCertificate(group, certificate);
    if(status != UA_STATUSCODE_GOOD)
        report_rejected_certificate(server, cfg, "user", certificate, status);
    return status;
}

/* A group without verifyCertificate accepts all certificates and rejects none,
 * so it stays unwrapped */
static void
wrap_certificate_verification(PyServer *server, UA_ServerConfig *cfg) {
    if(cfg->secureChannelPKI.verifyCertificate &&
       cfg->secureChannelPKI.verifyCertificate != verify_application_certificate) {
        server->verifyApplicationCertificate = cfg->secureChannelPKI.verifyCertificate;
        cfg->secureChannelPKI.verifyCertificate = verify_application_certificate;
    }
    if(cfg->sessionPKI.verifyCertificate &&
       cfg->sessionPKI.verifyCertificate != verify_user_certificate) {
        server->verifyUserCertificate = cfg->sessionPKI.verifyCertificate;
        cfg->sessionPKI.verifyCertificate = verify_user_certificate;
    }
}

/* The rejected application certificates, oldest first */
PyObject *
pyServer_rejected_certificates(PyObject *obj, PyObject *Py_UNUSED(ignored)) {
    O6_REQUIRE_LOOP_THREAD(pyServer_eventLoop((PyServer *)obj), NULL);
    PyServer *self = (PyServer *)obj;
    if(!self->server) {
        PyErr_SetString(PyExc_RuntimeError, "Server not initialized");
        return NULL;
    }
    UA_ServerConfig *cfg = UA_Server_getConfig(self->server);
    UA_ByteString *rejected = NULL;
    size_t size = 0;
    UA_StatusCode status = UA_STATUSCODE_GOOD;
    lockServer(self->server);
    UA_CertificateGroup *group = &cfg->secureChannelPKI;
    if(group->getRejectedList) /* AcceptAll rejects nothing */
        status = group->getRejectedList(group, &rejected, &size);
    unlockServer(self->server);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    PyObject *list = PyList_New((Py_ssize_t)size);
    for(size_t i = 0; list && i < size; i++) {
        PyObject *item = PyBytes_FromStringAndSize((const char *)rejected[i].data,
                                                   (Py_ssize_t)rejected[i].length);
        if(!item) {
            Py_CLEAR(list);
            break;
        }
        PyList_SET_ITEM(list, (Py_ssize_t)i, item);
    }
    UA_Array_delete(rejected, size, &UA_TYPES[UA_TYPES_BYTESTRING]);
    return list;
}

/* --- set_encryption method --- */
static PyObject *
PyServerConfig_set_encryption(PyServerConfig *self,
                              PyObject *args, PyObject *kwds) {
    O6_REQUIRE_WRITABLE_CONFIG(pyServerConfig_notRunning(self, "configure", "encryption") &&
                                   config_writable(self, "encryption"),
                               pyServerConfig_eventLoop(self), NULL);
    static char *kwlist[] = {"certificate", "privateKey", "port",
                             "trustList", "issuerList", "revocationList",
                             "secureOnly", "securityPolicies", NULL};
    PyObject *py_cert = NULL, *py_key = NULL;
    int port = 4840;
    PyObject *py_trust = NULL, *py_issuer = NULL, *py_revoc = NULL;
    PyObject *py_policies = NULL;
    int secure_only = 0;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "SS|iOOOpO", kwlist,
                                     &py_cert, &py_key, &port,
                                     &py_trust, &py_issuer, &py_revoc,
                                     &secure_only, &py_policies))
        return NULL;

    unsigned policy_mask = 0;
    int policies_selected = 0;
    if (parse_security_policies(py_policies, secure_only, &policy_mask,
                                &policies_selected) < 0)
        return NULL;

    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    if (self->py_server->running) {
        PyErr_SetString(PyExc_RuntimeError,
                        "Cannot configure encryption while server is running");
        return NULL;
    }

    char *cert_buf, *key_buf;
    Py_ssize_t cert_len, key_len;
    PyBytes_AsStringAndSize(py_cert, &cert_buf, &cert_len);
    PyBytes_AsStringAndSize(py_key, &key_buf, &key_len);

    UA_ByteString cert = {(size_t)cert_len, (UA_Byte *)cert_buf};
    UA_ByteString key = {(size_t)key_len, (UA_Byte *)key_buf};

    size_t trustSize = 0, issuerSize = 0, revocSize = 0;
    UA_ByteString *trustList = pyList_to_ByteStringArray(py_trust, &trustSize);
    if (PyErr_Occurred()) return NULL;
    UA_ByteString *issuerList = pyList_to_ByteStringArray(py_issuer, &issuerSize);
    if (PyErr_Occurred()) {
        free_ByteStringArray(trustList, trustSize);
        return NULL;
    }
    UA_ByteString *revocList = pyList_to_ByteStringArray(py_revoc, &revocSize);
    if (PyErr_Occurred()) {
        free_ByteStringArray(trustList, trustSize);
        free_ByteStringArray(issuerList, issuerSize);
        return NULL;
    }

    lockServer(self->py_server->server);
    if(self->py_server->pushManagementEnabled) {
        unlockServer(self->py_server->server);
        free_ByteStringArray(trustList, trustSize);
        free_ByteStringArray(issuerList, issuerSize);
        free_ByteStringArray(revocList, revocSize);
        PyErr_SetString(PyExc_RuntimeError,
                        "Configure encryption before enabling PushManagement");
        return NULL;
    }
    if(config_require_stopped(self, "encryption") < 0) {
        unlockServer(self->py_server->server);
        free_ByteStringArray(trustList, trustSize);
        free_ByteStringArray(issuerList, issuerSize);
        free_ByteStringArray(revocList, revocSize);
        return NULL;
    }
    self->py_server->configChanging = true;

    /* The steps of UA_ServerConfig_setDefaultWithSecurityPolicies, with an
     * explicit SecurityPolicy and UserTokenPolicy selection. Unlike that
     * helper, a failure does not clear the config of the existing server. */
    UA_Boolean allPermissionsForAnonymous = cfg->allPermissionsForAnonymous;
    UA_ByteString derKey = UA_BYTESTRING_NULL;
    UA_StatusCode status = decode_private_key(cfg, &key, &derKey);
    if(status == UA_STATUSCODE_GOOD)
        status = UA_ServerConfig_setBasics_withPort(cfg, (UA_UInt16)port);
    if(status == UA_STATUSCODE_GOOD)
        status = set_trust_list(cfg, trustList, trustSize, issuerList, issuerSize,
                                revocList, revocSize);
    if(status == UA_STATUSCODE_GOOD)
        wrap_certificate_verification(self->py_server, cfg);
    if(status == UA_STATUSCODE_GOOD)
        status = set_security_policies(cfg, &cert, &derKey, policy_mask,
                                       policies_selected);
    if(status == UA_STATUSCODE_GOOD)
        status = UA_AccessControl_default(cfg, (policy_mask & POLICY_NONE) != 0,
                                          user_token_policy_uri(cfg), 0, NULL);
    if(status == UA_STATUSCODE_GOOD)
        status = (policy_mask & (POLICY_NONE | POLICIES_DEPRECATED)) ?
            UA_ServerConfig_addAllEndpoints(cfg) :
            UA_ServerConfig_addAllSecureEndpoints(cfg);
    if(status == UA_STATUSCODE_GOOD)
        set_deprecated_security_levels(cfg);
    UA_ByteString_memZero(&derKey);
    UA_ByteString_clear(&derKey);

    free_ByteStringArray(trustList, trustSize);
    free_ByteStringArray(issuerList, issuerSize);
    free_ByteStringArray(revocList, revocSize);

    /* The open62541 default helpers restore feature defaults. Reapply the
     * o6 nodestore and entitlement invariants before returning to Python.
     * setBasics also resets the RBAC fallback (rbacForAnonymous) to
     * permissive; keep the configured one. */
    restore_o6_config_invariants(cfg);
    if(status == UA_STATUSCODE_GOOD) {
        Py_XSETREF(self->py_server->discoveryCertificate, Py_NewRef(py_cert));
        Py_XSETREF(self->py_server->discoveryPrivateKey, Py_NewRef(py_key));
    }
    cfg->allPermissionsForAnonymous = allPermissionsForAnonymous;
    self->py_server->configChanging = false;
    unlockServer(self->py_server->server);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    Py_RETURN_NONE;
}

/* --- setDefaultWithFilestore method --- */
static PyObject *
PyServerConfig_set_filestore(PyServerConfig *self, PyObject *args, PyObject *kwds) {
    O6_REQUIRE_WRITABLE_CONFIG(config_writable(self, "filestore"),
                               pyServerConfig_eventLoop(self), NULL);
    static char *kwlist[] = {"certificate", "privateKey", "storePath", "port",
                             "securityPolicies", NULL};
    PyObject *py_cert, *py_key, *py_path;
    PyObject *py_policies = NULL;
    const char *path;
    Py_ssize_t path_len;
    int port = 4840;
    if(!PyArg_ParseTupleAndKeywords(args, kwds, "SSU|iO", kwlist,
                                    &py_cert, &py_key, &py_path, &port, &py_policies))
        return NULL;
    unsigned policy_mask = 0;
    int policies_selected = 0;
    if(parse_security_policies(py_policies, 0, &policy_mask, &policies_selected) < 0)
        return NULL;
    path = PyUnicode_AsUTF8AndSize(py_path, &path_len);
    if(!path)
        return NULL;
    if(port < 0 || port > UINT16_MAX) {
        PyErr_SetString(PyExc_ValueError, "port must be between 0 and 65535");
        return NULL;
    }
    if(path_len == 0 || memchr(path, '\0', (size_t)path_len)) {
        PyErr_SetString(PyExc_ValueError, "storePath must be nonempty and contain no NUL");
        return NULL;
    }
#if defined(__APPLE__)
    PyErr_SetString(PyExc_NotImplementedError,
                    "Durable GDS filestore configuration is not supported on macOS yet");
    return NULL;
#elif !defined(UA_ENABLE_ENCRYPTION) || !(defined(__linux__) || defined(UA_ARCHITECTURE_WIN32))
    PyErr_SetString(PyExc_NotImplementedError,
                    "This SDK/platform build does not support encrypted filestore configuration");
    return NULL;
#else
    UA_ServerConfig *cfg = get_config(self);
    if(!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    UA_ByteString cert = {(size_t)PyBytes_GET_SIZE(py_cert),
                          (UA_Byte*)PyBytes_AS_STRING(py_cert)};
    UA_ByteString key = {(size_t)PyBytes_GET_SIZE(py_key),
                         (UA_Byte*)PyBytes_AS_STRING(py_key)};
    UA_String storePath = {(size_t)path_len, (UA_Byte*)path};
    lockServer(self->py_server->server);
    if(config_require_stopped(self, "filestore") < 0) {
        unlockServer(self->py_server->server);
        return NULL;
    }
    if(self->py_server->pushManagementEnabled) {
        unlockServer(self->py_server->server);
        PyErr_SetString(PyExc_RuntimeError,
                        "Configure filestore before enabling PushManagement");
        return NULL;
    }
    self->py_server->configChanging = true;
    /* SDK helpers append policies/endpoints to an existing configuration.
     * Replace them so constructor credentials cannot remain selectable. */
    UA_Array_delete(cfg->endpoints, cfg->endpointsSize,
                    &UA_TYPES[UA_TYPES_ENDPOINTDESCRIPTION]);
    cfg->endpoints = NULL;
    cfg->endpointsSize = 0;
    for(size_t i = 0; i < cfg->securityPoliciesSize; i++)
        cfg->securityPolicies[i].clear(&cfg->securityPolicies[i]);
    UA_free(cfg->securityPolicies);
    cfg->securityPolicies = NULL;
    cfg->securityPoliciesSize = 0;
    /* setBasics resets the RBAC fallback (rbacForAnonymous) to permissive */
    UA_Boolean allPermissionsForAnonymous = cfg->allPermissionsForAnonymous;
    UA_StatusCode status = UA_ServerConfig_setDefaultWithFilestore(
        cfg, (UA_UInt16)port, &cert, &key, storePath);
    /* open62541 offers every policy it can build, including None and the
     * deprecated ones. An explicit selection keeps exactly the selected ones. */
    if(status == UA_STATUSCODE_GOOD && policies_selected)
        status = select_security_policies(cfg, policy_mask);
    /* The filestore replaced the certificate groups */
    if(status == UA_STATUSCODE_GOOD)
        wrap_certificate_verification(self->py_server, cfg);
    /* Native setup can reset defaults before a later filesystem error. */
    restore_o6_config_invariants(cfg);
    if(status == UA_STATUSCODE_GOOD) {
        Py_XSETREF(self->py_server->discoveryCertificate, Py_NewRef(py_cert));
        Py_XSETREF(self->py_server->discoveryPrivateKey, Py_NewRef(py_key));
    }
    cfg->allPermissionsForAnonymous = allPermissionsForAnonymous;
    self->py_server->configChanging = false;
    unlockServer(self->py_server->server);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
#endif
}

#ifdef UA_ENABLE_JSON_ENCODING
/* --- _loadJson method: the JSON configuration format of open62541 --- */

#define TRANSPLANT(field) \
    o6_swap_bytes(&live->field, &tmp->field, sizeof(live->field))

/* Move the plugins, callbacks and runtime state that o6 installs into the
 * scratch config. The JSON format has no keys for them. Review this list when
 * open62541 adds a plugin or callback field to UA_ServerConfig. */
static void
transplant_o6_plugins(UA_ServerConfig *live, UA_ServerConfig *tmp) {
    TRANSPLANT(context);
    TRANSPLANT(notifyLifecycleState);
    TRANSPLANT(customDataTypes);
    TRANSPLANT(eventLoop);
    TRANSPLANT(externalEventLoop);
    TRANSPLANT(globalNotificationCallback);
    TRANSPLANT(lifecycleNotificationCallback);
    TRANSPLANT(secureChannelNotificationCallback);
    TRANSPLANT(sessionNotificationCallback);
    TRANSPLANT(serviceNotificationCallback);
    TRANSPLANT(subscriptionNotificationCallback);
    TRANSPLANT(discoveryNotificationCallback);
#ifdef UA_ENABLE_AUDITING
    TRANSPLANT(auditNotificationCallback);
#endif
    TRANSPLANT(nodestore);
    TRANSPLANT(nodeLifecycle);
    TRANSPLANT(asyncOperationCancelCallback);
#ifdef UA_ENABLE_PUBSUB
    TRANSPLANT(pubSubConfig.componentLifecycleCallback);
    TRANSPLANT(pubSubConfig.beforeStateChangeCallback);
    TRANSPLANT(pubSubConfig.stateChangeCallback);
    TRANSPLANT(pubSubConfig.securityPolicies);
    TRANSPLANT(pubSubConfig.securityPoliciesSize);
#endif
#ifdef UA_ENABLE_HISTORIZING
    TRANSPLANT(historyDatabase);
#endif
#ifdef UA_ENABLE_ENCRYPTION
    TRANSPLANT(privateKeyPasswordCallback);
#endif
#ifdef UA_ENABLE_RBAC
    TRANSPLANT(rolePermissionPresets);
    TRANSPLANT(rolePermissionPresetsSize);
    TRANSPLANT(roles);
    TRANSPLANT(rolesSize);
    TRANSPLANT(allPermissionsForAnonymous);
#endif
    /* A Python AccessControl is kept. The open62541 default access control
     * of the scratch config matches its security policies and replaces the
     * previous default one. */
    if(pyAccessControl_isPython(&live->accessControl))
        TRANSPLANT(accessControl);
}

#undef TRANSPLANT

/* Endpoints for every security policy, as setEncryption creates them. The
 * file adds its policies without endpoints. The default access control is
 * rebuilt so that user tokens use the most secure policy. */
static UA_StatusCode
add_policy_endpoints(UA_ServerConfig *cfg) {
    UA_Array_delete(cfg->endpoints, cfg->endpointsSize,
                    &UA_TYPES[UA_TYPES_ENDPOINTDESCRIPTION]);
    cfg->endpoints = NULL;
    cfg->endpointsSize = 0;
    if(!pyAccessControl_isPython(&cfg->accessControl)) {
        UA_Boolean allPermissionsForAnonymous = cfg->allPermissionsForAnonymous;
        UA_StatusCode status =
            UA_AccessControl_default(cfg, true, user_token_policy_uri(cfg), 0, NULL);
        cfg->allPermissionsForAnonymous = allPermissionsForAnonymous;
        if(status != UA_STATUSCODE_GOOD)
            return status;
    }
    return UA_ServerConfig_addAllEndpoints(cfg);
}

/* Parse a JSON document into a scratch config only, to find invalid settings */
static PyObject *
check_json(PyObject *arg) {
    Py_buffer view;
    if(PyObject_GetBuffer(arg, &view, PyBUF_SIMPLE) < 0)
        return NULL;
    UA_ByteString json = {(size_t)view.len, (UA_Byte *)view.buf};
    UA_ServerConfig tmp;
    UA_StatusCode status = UA_ServerConfig_loadFromFile(&tmp, json);
    if(status == UA_STATUSCODE_GOOD)
        UA_ServerConfig_clear(&tmp);
    PyBuffer_Release(&view);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}

static PyObject *
PyServerConfig_load_json(PyServerConfig *self, PyObject *args, PyObject *kwds) {
    O6_REQUIRE_WRITABLE_CONFIG(config_writable(self, "the configuration"),
                               pyServerConfig_eventLoop(self), NULL);
    static char *kwlist[] = {"json", "addEndpoints", "dryRun", NULL};
    PyObject *arg;
    int add_endpoints = 0, dry_run = 0;
    if(!PyArg_ParseTupleAndKeywords(args, kwds, "O|$pp", kwlist,
                                    &arg, &add_endpoints, &dry_run))
        return NULL;
    if(dry_run)
        return check_json(arg);

    UA_ServerConfig *live = get_config(self);
    if(!live) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    PyServer *server = self->py_server;
    /* History owns the history capabilities of the config once enabled */
    if(pyHistory_enabled(&server->history)) {
        PyErr_SetString(PyExc_RuntimeError,
                        "Load the configuration before enabling history");
        return NULL;
    }
    Py_buffer view;
    if(PyObject_GetBuffer(arg, &view, PyBUF_SIMPLE) < 0)
        return NULL;

    lockServer(server->server);
    if(server->pushManagementEnabled) {
        unlockServer(server->server);
        PyBuffer_Release(&view);
        PyErr_SetString(PyExc_RuntimeError,
                        "Load the configuration before enabling PushManagement");
        return NULL;
    }
    if(config_require_stopped(self, "the configuration") < 0) {
        unlockServer(server->server);
        PyBuffer_Release(&view);
        return NULL;
    }
    server->configChanging = true;

    UA_ByteString json = {(size_t)view.len, (UA_Byte *)view.buf};
    UA_ServerConfig tmp;
    UA_StatusCode status = UA_ServerConfig_loadFromFile(&tmp, json);
    if(status == UA_STATUSCODE_GOOD && !tmp.logging)
        status = UA_STATUSCODE_BADOUTOFMEMORY;
    if(status == UA_STATUSCODE_GOOD) {
        /* The security policies and certificate groups of the scratch config
         * keep a pointer to its stdout logger. Turn that logger into the
         * Python logger and keep it, so they log to Python. */
        pyLogger_init(tmp.logging, (PyObject *)live->logging->context);
        if(live->eventLoop && live->eventLoop->logger == live->logging)
            live->eventLoop->logger = tmp.logging;

        transplant_o6_plugins(live, &tmp);
        UA_ServerConfig old = *live;
        *live = tmp;
        /* Frees the scratch defaults (event loop, nodestore, access control)
         * and the replaced settings, security and logger */
        UA_ServerConfig_clear(&old);

        if(add_endpoints)
            status = add_policy_endpoints(live);
        wrap_certificate_verification(server, live);
        clamp_pubsub(live);
        /* The security configuration came from the file */
        Py_CLEAR(server->discoveryCertificate);
        Py_CLEAR(server->discoveryPrivateKey);
    }
    server->configChanging = false;
    unlockServer(server->server);
    PyBuffer_Release(&view);
    if(status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);
    Py_RETURN_NONE;
}
#endif /* UA_ENABLE_JSON_ENCODING */

/* --- set_accept_all_certificates method --- */
static PyObject *
PyServerConfig_set_accept_all(PyServerConfig *self, PyObject *args) {
    O6_REQUIRE_WRITABLE_CONFIG(pyServerConfig_notRunning(self, "modify", "certificate policy"),
                               pyServerConfig_eventLoop(self), NULL);
    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    if (self->py_server->running) {
        PyErr_SetString(PyExc_RuntimeError,
                        "Cannot modify certificate policy while server is running");
        return NULL;
    }

    cfg->secureChannelPKI.clear(&cfg->secureChannelPKI);
    UA_CertificateGroup_AcceptAll(&cfg->secureChannelPKI);
    cfg->sessionPKI.clear(&cfg->sessionPKI);
    UA_CertificateGroup_AcceptAll(&cfg->sessionPKI);

    Py_RETURN_NONE;
}

/* --- set_history_database method --- */
static PyObject *
PyServerConfig_set_history_database(PyServerConfig *self,
                                    PyObject *args, PyObject *kwds) {
    O6_REQUIRE_WRITABLE_CONFIG(pyServerConfig_notRunning(self, "configure", "history database"),
                               pyServerConfig_eventLoop(self), NULL);
    static char *kwlist[] = {"maxNodes", "capacity", "maxResponseSize",
                             "backend", NULL};
    int max_nodes = PYO6_HISTORY_MAX_NODES_DEFAULT;
    int capacity = INT_MIN;
    int max_response = PYO6_HISTORY_RESPONSE_DEFAULT;
    PyObject *py_backend = NULL;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|iiiO", kwlist, &max_nodes,
                                     &capacity, &max_response, &py_backend))
        return NULL;
    if (py_backend == Py_None)
        py_backend = NULL;

    if (max_nodes <= 0 || max_response <= 0) {
        PyErr_SetString(PyExc_ValueError,
                        "maxNodes and maxResponseSize must be positive");
        return NULL;
    }
    if (py_backend == NULL && capacity != INT_MIN && capacity <= 0) {
        PyErr_SetString(PyExc_ValueError, "capacity must be positive");
        return NULL;
    }

    UA_ServerConfig *cfg = get_config(self);
    if (!cfg) {
        PyErr_SetString(PyExc_RuntimeError, "No UA_Server attached");
        return NULL;
    }
    if (self->py_server->running) {
        PyErr_SetString(PyExc_RuntimeError,
                        "Cannot configure history database while server is running");
        return NULL;
    }
    if (pyHistory_enabled(&self->py_server->history)) {
        PyErr_SetString(PyExc_RuntimeError,
                        "History database already configured");
        return NULL;
    }

    if (py_backend) {
        UA_StatusCode status = pyHistory_enableCustom(
            &self->py_server->history, self->py_server->server, cfg, py_backend,
            (PyObject *)self->py_server, (size_t)max_nodes, (size_t)max_response);
        if (status != UA_STATUSCODE_GOOD) {
            if (!PyErr_Occurred())
                return PyErr_StatusCode(status);
            return NULL;
        }
        Py_RETURN_NONE;
    }

    if (capacity == INT_MIN)
        capacity = PYO6_HISTORY_CAPACITY_DEFAULT;
    UA_StatusCode status =
        pyHistory_enable(&self->py_server->history, self->py_server->server, cfg,
                         (size_t)max_nodes, (size_t)capacity,
                         (size_t)max_response);
    if (status != UA_STATUSCODE_GOOD)
        return PyErr_StatusCode(status);

    Py_RETURN_NONE;
}

static PyMethodDef PyServerConfig_methods[] = {
    {"setAccessControl", (PyCFunction)PyAccessControl_install,
     METH_O, "Install a Python AccessControl plugin before server startup."},
#ifdef UA_ENABLE_JSON_ENCODING
    {"loadFromFile", (PyCFunction)pyJsonConfig_load, METH_O,
     "Replace the configuration with the settings of a JSON5 file, and the\n"
     "o6 defaults for everything it leaves out."},
    {"_loadJson", (PyCFunction)PyServerConfig_load_json, METH_VARARGS | METH_KEYWORDS,
     "Replace the configuration with the settings of a JSON document (bytes),\n"
     "keeping the plugins and callbacks. Use loadFromFile."},
#endif
    {"setEncryption", (PyCFunction)PyServerConfig_set_encryption,
     METH_VARARGS | METH_KEYWORDS,
     "Configure security policies with certificate and private key.\n\n"
     "Args:\n"
     "    certificate: Server certificate as bytes (DER or PEM)\n"
     "    private_key: Private key as bytes (DER or PEM)\n"
     "    port: Server port (default: 4840)\n"
     "    trust_list: Optional list of trusted certificates (bytes); without\n"
     "        one, every client certificate is rejected\n"
     "    issuer_list: Optional list of issuer certificates (bytes) that only\n"
     "        complete the chains of trusted certificates\n"
     "    revocation_list: Optional list of CRLs (bytes)\n"
     "    secure_only: If True, do not offer unencrypted endpoints"},
    {"setDefaultWithFilestore", (PyCFunction)PyServerConfig_set_filestore,
     METH_VARARGS | METH_KEYWORDS,
     "Configure persistent certificates and trust lists before startup (Linux/Windows).\n\n"
     "Args:\n"
     "    certificate: Explicit startup certificate as DER or PEM bytes.\n"
     "    privateKey: Matching private key as DER or PEM bytes.\n"
     "    storePath: PKI root path as str.\n"
     "    port: UInt16 listener port (default: 4840).\n\n"
     "Loads application and user-token trust from the PKI directories. Resets\n"
     "server settings, security and access control; configure application identity,\n"
     "authentication and custom limits afterwards, then enable PushManagement.\n"
     "Saved credentials do not override supplied bytes. Filesystem errors raise\n"
     "StatusCodeError and may leave partial configuration. Protect the store\n"
     "with a restrictive directory/umask on Linux or Windows ACLs; private-key files\n"
     "use OS defaults. This method does not change process permissions."},
    {"setAcceptAllCertificates", (PyCFunction)PyServerConfig_set_accept_all,
     METH_NOARGS,
     "Accept all client certificates without validation, replacing the trust\n"
     "list (testing only). Call it after setEncryption()."},
    {"setHistoryDatabase", (PyCFunction)PyServerConfig_set_history_database,
     METH_VARARGS | METH_KEYWORDS,
     "Configure the in-memory history database.\n\n"
     "Every historized node gets a ring buffer of a fixed size, so one node\n"
     "costs capacity samples and never more. Must be called before start().\n\n"
     "Args:\n"
     "    maxNodes: Node table size to allocate up front. The table grows as\n"
     "        further nodes are historized, so this is a hint (default: 10)\n"
     "    capacity: Samples buffered per node, unless the node overrides it\n"
     "        (default: 100)\n"
     "    maxResponseSize: Values per HistoryRead response before the server\n"
     "        continues with a continuation point (default: 100)"},
    {NULL, NULL, 0, NULL}
};

/* --- Type Lifecycle --- */
static void
PyServerConfig_dealloc(PyServerConfig *self) {
    Py_XDECREF(self->py_server);
    Py_TYPE(self)->tp_free((PyObject *)self);
}

static PyObject *
PyServerConfig_new(PyTypeObject *type, PyObject *args, PyObject *kwds) {
    PyServerConfig *self = (PyServerConfig *)type->tp_alloc(type, 0);
    self->py_server = NULL;
    return (PyObject *)self;
}

static int
PyServerConfig_init(PyServerConfig *self, PyObject *args, PyObject *kwds) {
    PyErr_SetString(PyExc_TypeError,
                    "ServerConfig cannot be instantiated directly");
    return -1;
}

PyTypeObject PyServerConfigType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "o6.ServerConfig",
    .tp_basicsize = sizeof(PyServerConfig),
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyServerConfig_new,
    .tp_init = (initproc)PyServerConfig_init,
    .tp_dealloc = (destructor)PyServerConfig_dealloc,
    .tp_getset = PyServerConfig_getset,
    .tp_methods = PyServerConfig_methods,
};

PyObject *
PyServerConfig_New(PyServer *py_server) {
    PyServerConfig *obj =
        (PyServerConfig *)PyServerConfigType.tp_alloc(&PyServerConfigType, 0);
    if (!obj)
        return NULL;
    Py_INCREF(py_server);
    obj->py_server = py_server;
    return (PyObject *)obj;
}
