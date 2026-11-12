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

#ifndef UTILS_H_
#define UTILS_H_

#include <open62541/plugin/certificategroup.h>

int validate_endpoint_uri(const char* uri);

/* Rejected certificates a certificate group keeps. The open62541 default
 * config helpers pass their limits under keys the Memorystore does not read,
 * so o6 sets it explicitly. */
#define O6_MAX_REJECTED_CERTIFICATES 100

UA_StatusCode
o6_set_trust_list(UA_CertificateGroup *group, UA_NodeId *groupId,
                  const UA_Logger *logging,
                  const UA_ByteString *trustList, size_t trustSize,
                  const UA_ByteString *issuerList, size_t issuerSize,
                  const UA_ByteString *revocList, size_t revocSize);

void o6_swap_bytes(void *a, void *b, size_t size);

#endif // UTILS_H_
