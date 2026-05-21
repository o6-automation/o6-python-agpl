/* Copyright (c) 2026 o6 Automation GmbH
 *
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
#include <stdbool.h>
#include <stddef.h>
#include <string.h>
#include <ctype.h>

int validate_endpoint_uri(const char *uri) {
    if(!uri) return 0;

    /* Must start with "opc.tcp://" */
    const char *prefix = "opc.tcp://";
    size_t prefixLen = strlen(prefix);
    if(strncmp(uri, prefix, prefixLen) != 0)
        return 0;

    const char *p = uri + prefixLen;

    /* Host: at least one character from [a-zA-Z0-9.-] */
    if(!*p) return 0;
    while(*p && (isalnum((unsigned char)*p) || *p == '.' || *p == '-'))
        p++;

    /* No host characters consumed before separator */
    if(p == uri + prefixLen) return 0;

    /* Optional port: ":" followed by digits */
    if(*p == ':') {
        p++;
        if(!isdigit((unsigned char)*p)) return 0;
        while(isdigit((unsigned char)*p)) p++;
    }

    /* Optional path starting with "/" */
    if(*p == '/')
        p += strlen(p);

    return *p == '\0';
}
