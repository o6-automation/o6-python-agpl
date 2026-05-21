/* Copyright 2026 (c) o6 Automation GmbH */

#include "module.h"
#include <stdio.h>

bool client_enabled = true;
#ifdef O6_NO_SERVER
bool server_enabled = false;
#else
bool server_enabled = true;
#endif

/* Global variable with the build information */
UA_BuildInfo buildInfo;

bool o6_check_greet() {
    /* Set the build info */
    buildInfo.softwareVersion = UA_STRING_ALLOC("o6\\Python");
    buildInfo.buildNumber = UA_STRING_ALLOC(__DATE__);

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

void o6_clean_shutdown(void) {
    UA_BuildInfo_clear(&buildInfo);
}
