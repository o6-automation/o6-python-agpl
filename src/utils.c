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
#include <regex.h>
#include <stdbool.h>
#include <stddef.h>

int validate_endpoint_uri(const char *uri) {
    if (!uri) return 0;

    // Compiled once on first call; safe under the Python GIL
    static regex_t regex;
    static bool compiled = false;
    if (!compiled) {
        const char *pattern = "^opc\\.tcp://[a-zA-Z0-9.-]+(:[0-9]+)?(/.*)?$";
        if (regcomp(&regex, pattern, REG_EXTENDED) != 0)
            return 0;
        compiled = true;
    }

    return regexec(&regex, uri, 0, NULL, 0) == 0;
}
