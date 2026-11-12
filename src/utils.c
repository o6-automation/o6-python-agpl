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

#include "utils.h"
#include <open62541/plugin/certificategroup_default.h>
#include <stddef.h>
#include <string.h>
#include <ctype.h>

/* An IPv6 literal between brackets, such as "[::1]" or "[fe80::1%eth0]":
 * hex digits, ':' and '.' (embedded IPv4), with at least one ':', and an
 * optional zone ID after '%'. Returns the position after ']' or NULL. */
static const char *
skip_ipv6_literal(const char *p) {
    if(*p != '[')
        return NULL;
    p++;
    const char *start = p;
    int colons = 0;
    while(isxdigit((unsigned char)*p) || *p == ':' || *p == '.') {
        if(*p == ':')
            colons++;
        p++;
    }
    if(p == start || colons < 2)
        return NULL;
    if(*p == '%') {
        p++;
        const char *zone = p;
        while(isalnum((unsigned char)*p) || *p == '.' || *p == '-' ||
              *p == '_' || *p == '~')
            p++;
        if(p == zone)
            return NULL;
    }
    return *p == ']' ? p + 1 : NULL;
}

int validate_endpoint_uri(const char *uri) {
    if(!uri) return 0;

    /* Must start with "opc.tcp://" */
    const char *prefix = "opc.tcp://";
    size_t prefixLen = strlen(prefix);
    if(strncmp(uri, prefix, prefixLen) != 0)
        return 0;

    const char *p = uri + prefixLen;

    /* Host: an IPv6 literal in brackets, or at least one character from
     * [a-zA-Z0-9.-] for a host name or an IPv4 address */
    if(*p == '[') {
        p = skip_ipv6_literal(p);
        if(!p) return 0;
    } else {
        const char *host = p;
        while(*p && (isalnum((unsigned char)*p) || *p == '.' || *p == '-'))
            p++;
        if(p == host) return 0;
    }

    /* Optional port: ":" followed by 1 to 65535 */
    if(*p == ':') {
        p++;
        if(!isdigit((unsigned char)*p)) return 0;
        unsigned long port = 0;
        while(isdigit((unsigned char)*p)) {
            port = port * 10 + (unsigned long)(*p - '0');
            if(port > 65535) return 0;
            p++;
        }
        if(port == 0) return 0;
    }

    /* Optional path starting with "/" */
    if(*p == '/')
        p += strlen(p);

    return *p == '\0';
}

/* Build the Memorystore of a certificate group. Without trusted certificates
 * it rejects every certificate: the issuer certificates only complete the
 * chains of trusted ones. The open62541 default helpers instead keep the
 * AcceptAll group of setDefaultConfig when the trust list is empty. */
UA_StatusCode
o6_set_trust_list(UA_CertificateGroup *group, UA_NodeId *groupId,
                  const UA_Logger *logging,
                  const UA_ByteString *trustList, size_t trustSize,
                  const UA_ByteString *issuerList, size_t issuerSize,
                  const UA_ByteString *revocList, size_t revocSize) {
    UA_TrustListDataType list;
    UA_TrustListDataType_init(&list);
    list.specifiedLists = UA_TRUSTLISTMASKS_TRUSTEDCERTIFICATES |
        UA_TRUSTLISTMASKS_ISSUERCERTIFICATES | UA_TRUSTLISTMASKS_TRUSTEDCRLS;
    UA_StatusCode res = UA_STATUSCODE_GOOD;
    if(trustSize > 0) {
        res = UA_Array_copy(trustList, trustSize, (void**)&list.trustedCertificates,
                            &UA_TYPES[UA_TYPES_BYTESTRING]);
        if(res == UA_STATUSCODE_GOOD)
            list.trustedCertificatesSize = trustSize;
    }
    if(res == UA_STATUSCODE_GOOD && issuerSize > 0) {
        res = UA_Array_copy(issuerList, issuerSize, (void**)&list.issuerCertificates,
                            &UA_TYPES[UA_TYPES_BYTESTRING]);
        if(res == UA_STATUSCODE_GOOD)
            list.issuerCertificatesSize = issuerSize;
    }
    if(res == UA_STATUSCODE_GOOD && revocSize > 0) {
        res = UA_Array_copy(revocList, revocSize, (void**)&list.trustedCrls,
                            &UA_TYPES[UA_TYPES_BYTESTRING]);
        if(res == UA_STATUSCODE_GOOD)
            list.trustedCrlsSize = revocSize;
    }

    UA_UInt32 maxRejected = O6_MAX_REJECTED_CERTIFICATES;
    UA_KeyValuePair param;
    param.key = UA_QUALIFIEDNAME(0, "maxRejectedListSize");
    UA_Variant_setScalar(&param.value, &maxRejected, &UA_TYPES[UA_TYPES_UINT32]);
    UA_KeyValueMap params = {1, &param};
    if(res == UA_STATUSCODE_GOOD)
        res = UA_CertificateGroup_Memorystore(group, groupId,
                                              &list, logging, &params);
    UA_TrustListDataType_clear(&list);
    return res;
}

void
o6_swap_bytes(void *a, void *b, size_t size) {
    unsigned char *x = (unsigned char *)a, *y = (unsigned char *)b;
    for(size_t i = 0; i < size; i++) {
        unsigned char t = x[i];
        x[i] = y[i];
        y[i] = t;
    }
}
