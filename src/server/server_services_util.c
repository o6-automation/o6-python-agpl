/* Copyright 2026 (c) o6 Automation GmbH */
#include "server_services_util.h"
#include "../module.h"
#include "../types_internal.h"

int
extract_nodeid(PyObject *obj, UA_NodeId *out,
               const UA_NamespaceMapping *nsMapping,
               const UA_DataTypeArray *customDataTypes) {
    UA_NodeId_init(out);
    PyObject *res = PY2UA(obj, out, &UA_TYPES[UA_TYPES_NODEID], nsMapping, customDataTypes);
    if (!res)
        return -1;
    return 0;
}

int
extract_qualifiedname(PyObject *obj, UA_QualifiedName *out,
                      const UA_NamespaceMapping *nsMapping,
                      const UA_DataTypeArray *customDataTypes) {
    UA_QualifiedName_init(out);
    PyObject *res = PY2UA(obj, out, &UA_TYPES[UA_TYPES_QUALIFIEDNAME], nsMapping, customDataTypes);
    if (!res)
        return -1;
    return 0;
}
