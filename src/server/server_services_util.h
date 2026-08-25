/* Copyright 2026 (c) o6 Automation GmbH */
#ifndef PYO6_SERVER_SERVICES_UTIL_H_
#define PYO6_SERVER_SERVICES_UTIL_H_

#include "server.h"

/*
 * Helper: Extract a UA_NodeId from a Python object.
 * Converts via PY2UA and applies the optional server namespace mapping.
 * Caller must clear the NodeId.
 */
int
extract_nodeid(PyObject *obj, UA_NodeId *out,
               const UA_NamespaceMapping *nsMapping,
               const UA_DataTypeArray *customDataTypes);

/*
 * Helper: Extract a UA_QualifiedName from a Python object.
 * Converts via PY2UA and applies the optional server namespace mapping.
 * Caller must clear the QualifiedName.
 */
int
extract_qualifiedname(PyObject *obj, UA_QualifiedName *out,
                      const UA_NamespaceMapping *nsMapping,
                      const UA_DataTypeArray *customDataTypes);

#endif /* PYO6_SERVER_SERVICES_UTIL_H_ */
