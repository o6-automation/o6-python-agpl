/* Copyright 2026 (c) o6 Automation GmbH */
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

#ifndef BOOTSTRAP_NS0_TYPES_H_
#define BOOTSTRAP_NS0_TYPES_H_

#include <Python.h>

// Create the hand-maintained C-side bootstrap enums (`StatusCode` and its `_Enum` metaclass) and add them to `module`.  
void create_bootstrap_enums(PyObject *module);

/* Build the six NS0 bootstrap struct PyTypes (StructureDescription/Definition/Field, EnumDescription/Definition/Field)
 * Returns 0 on success, -1 with an exception set on failure. */
int create_bootstrap_struct_types(PyObject *module);

#endif /* BOOTSTRAP_NS0_TYPES_H_ */
