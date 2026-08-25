/* Copyright 2026 (c) o6 Automation GmbH */
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
