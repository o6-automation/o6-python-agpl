/* Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner) */
#ifndef PYO6_SERVER_ACCESS_CONTROL_H_
#define PYO6_SERVER_ACCESS_CONTROL_H_

#include "server.h"

/* Install a Python-backed UA_AccessControl plugin on a server config. */
PyObject *PyAccessControl_install(PyServerConfig *self, PyObject *plugin);

#endif /* PYO6_SERVER_ACCESS_CONTROL_H_ */
