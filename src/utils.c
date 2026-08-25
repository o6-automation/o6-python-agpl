/* Copyright 2026 (c) o6 Automation GmbH */
#include "utils.h"
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
