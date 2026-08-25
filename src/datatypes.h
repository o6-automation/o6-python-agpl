/* Copyright 2026 (c) o6 Automation GmbH */
#ifndef O6_DATATYPES_H_
#define O6_DATATYPES_H_

#include "module.h"
#include <open62541/types.h>

/* Module-global registry of custom UA_DataTypes.  Types from every namespace are appended into shared, append-only
 * UA_DataTypeArray blocks chained together into a single linked list whose head is returned by
 * `o6_datatypes_global_chain()` (open62541 matches by NodeId, so there is no need to cluster per namespace).
 * Clients and Servers point their `config->customDataTypes` at this head once, at construction time, and never touch it again.
 *
 * DataTypes are built one at a time by Python at namespace-load time.
 * Blocks are never moved once populated, so every UA_DataType* handed out stays valid for the process lifetime. */


/* Register a single custom DataType in the given namespace, optionally subclassing the Python classes in `bases`
 *
 *   namespace_name  Shortname used to qualify the generated Python type.
 *   py_descr   A `StructureDescription` or `EnumDescription` whose typeId.namespaceIndex / field data_type / default encoding id 
 *              are already resolved to canonical namespace indices.
 *   bases      `None` to use the default object-only base; 
 *              otherwise a tuple of Python classes the new C PyType should subclass via `PyType_FromSpecWithBases`.  
 *              Used by the @o6.datatype decorator to express subtype relationships through Python inheritance.  
 *              An empty tuple falls back to the default base.
 *
 * Returns a new reference to a `(NodeId, PyType)` tuple on success
 * or `NULL` with a Python exception set on error. */
PyObject *
o6_register_datatype(const char *namespace_name, PyObject *py_descr,
                     PyObject *bases);

/* Head of the global UA_DataTypeArray chain.  Suitable for assignment to
 * `UA_ClientConfig::customDataTypes` / `UA_ServerConfig::customDataTypes`.
 * The pointer is stable for the lifetime of the process. */
const UA_DataTypeArray *o6_datatypes_global_chain(void);

/* Given a namespace mapping and the current customDataTypes chain, build a
 * new UA_DataTypeArray containing deep-copied types from the global chain
 * whose namespace is mapped in *nm, with namespace indices remapped from
 * Python-global to UA-local.  The new array is chained in front of
 * *customDataTypes, which is updated in-place.
 *
 * Returns UA_STATUSCODE_GOOD on success (including no-op when no types need
 * adding), or a bad status code on failure (in which case *customDataTypes
 * is left unchanged). */
UA_StatusCode
o6_datatypes_update_custom_datatypes(const UA_NamespaceMapping *nm, UA_DataTypeArray **customDataTypes);

void
o6_datatypes_clear_custom_datatypes(UA_DataTypeArray **customDataTypes);

#endif /* O6_DATATYPES_H_ */
