/* Copyright 2026 (c) o6 Automation GmbH */
#ifndef BOOTSTRAP_NS0_TYPES_H_
#define BOOTSTRAP_NS0_TYPES_H_

#include <Python.h>

// Create the hand-maintained C-side bootstrap enums (`StatusCode` and its `_Enum` metaclass) and add them to `module`.  
void create_bootstrap_enums(PyObject *module);

/* Build the six NS0 bootstrap struct PyTypes (StructureDescription/Definition/Field, EnumDescription/Definition/Field)
 * Returns 0 on success, -1 with an exception set on failure. */
int create_bootstrap_struct_types(PyObject *module);

#endif /* BOOTSTRAP_NS0_TYPES_H_ */
