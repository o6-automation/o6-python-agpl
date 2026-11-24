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

#include "module.h"
#include <stdio.h>

bool client_enabled = true;
bool server_enabled = true;
bool pubsub_enabled = true;

bool o6_check_greet() {
    /* Greet the user */
    printf("         _______        ____        __  __\n");
    printf("  ____  / ___/\\ \\      / __ \\__  __/ /_/ /_  ____  ____\n");
    printf(" / __ \\/ __ \\  \\ \\    / /_/ / / / / __/ __ \\/ __ \\/ __ \\\n");
    printf("/ /_/ / /_/ /   \\ \\  / ____/ /_/ / /_/ / / / /_/ / / / /\n");
    printf("\\____/\\____/     \\_\\/_/    \\__, /\\__/_/ /_/\\____/_/ /_/\n");
    printf("                          /____/    o6 Automation GmbH\n");
    printf("AGPL Edition (see https://www.o6-automation.com)\n");

    /* Version compatible */
    return true;
}

/* The AGPL edition has no Credentials: every compiled feature is enabled and
 * no Script Mode timer runs. */
PyObject *o6_license_status(void) {
    return Py_BuildValue("{s:s,s:O,s:O,s:O,s:O,s:O,s:O,s:O,s:O,s:O,s:O,s:O}",
                         "edition", "agpl",
                         "licensed", Py_False,
                         "scriptMode", Py_False,
                         "holder", Py_None,
                         "usageScope", Py_None,
                         "licenseId", Py_None,
                         "client", Py_True,
                         "server", Py_True,
                         "pubsub", Py_True,
                         "validFrom", Py_None,
                         "validTo", Py_None,
                         "rejectionReason", Py_None);
}

void o6_clean_shutdown(void) {
}
