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

#ifndef O6_UA_EXTENSION_NAMESPACEMAPPING_H_
#define O6_UA_EXTENSION_NAMESPACEMAPPING_H_

#include "module.h"

/* Set one namespace mapping entry and grow arrays as needed.
 *
 * python_idx is the Python/global namespace index.
 * ua_idx is the runtime UA namespace index (client-local or server-local).
 */
UA_StatusCode
ua_extension_namespace_mapping_set(UA_NamespaceMapping *nm,
                                   UA_String uri,
                                   UA_UInt16 python_idx,
                                   UA_UInt16 ua_idx);

UA_UInt16
UA_NamespaceMapping_Python2UA(const UA_NamespaceMapping *nm, UA_UInt16 python_idx);

UA_UInt16
UA_NamespaceMapping_UA2Python(const UA_NamespaceMapping *nm, UA_UInt16 ua_idx);

#endif /* O6_UA_EXTENSION_NAMESPACEMAPPING_H_ */
