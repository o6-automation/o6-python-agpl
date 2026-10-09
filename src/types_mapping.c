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

#include "ua_extension_namespacemapping.h"
#include "datatypes.h"


typedef UA_UInt16 (*mapIndexSignature)(const UA_NamespaceMapping *nm, UA_UInt16 index);

typedef struct MapUAContext {
    const UA_NamespaceMapping *nm;
    const UA_DataTypeArray *customTypesArray;
    mapIndexSignature map;
    UA_StatusCode status;
} MapUAContext;

typedef void (*mapSignature)(void *p, const UA_DataType *type, MapUAContext *ctx);
extern const mapSignature mapJumpTable[UA_DATATYPEKINDS];


static const UA_DataType *
findMappedDatatype(const UA_DataType *type, MapUAContext *ctx) {
    UA_NodeId typeId = type->typeId;
    typeId.namespaceIndex = ctx->map(ctx->nm, typeId.namespaceIndex);
    const UA_DataType* dt = UA_findDataTypeWithCustom(&typeId, ctx->customTypesArray);
    return dt;
}

static void
mapNop(void *p, const UA_DataType *_, MapUAContext *ctx) {}

static void
mapNodeId(void *p, const UA_DataType *_, MapUAContext *ctx) {
    UA_NodeId *id = (UA_NodeId*)p;
    id->namespaceIndex = ctx->map(ctx->nm, id->namespaceIndex);
}

static void
mapExpandedNodeId(void *p, const UA_DataType *_, MapUAContext *ctx) {
    UA_ExpandedNodeId *id = (UA_ExpandedNodeId*)p;
    if(id->nodeId.namespaceIndex != 0)
        id->nodeId.namespaceIndex = ctx->map(ctx->nm, id->nodeId.namespaceIndex);
}

static void
mapQualifiedName(void *p, const UA_DataType *_, MapUAContext *ctx) {
    UA_QualifiedName *qn= (UA_QualifiedName*)p;
    qn->namespaceIndex = ctx->map(ctx->nm, qn->namespaceIndex);
}

static void
mapExtensionObject(void *p, const UA_DataType *_, MapUAContext *ctx) {
    UA_ExtensionObject *eo = (UA_ExtensionObject*)p;
    switch(eo->encoding) {
    case UA_EXTENSIONOBJECT_ENCODED_NOBODY:
    default:
        break;
    case UA_EXTENSIONOBJECT_ENCODED_BYTESTRING:
    case UA_EXTENSIONOBJECT_ENCODED_XML:
        eo->content.encoded.typeId.namespaceIndex =
            ctx->map(ctx->nm, eo->content.encoded.typeId.namespaceIndex);
        break;
    case UA_EXTENSIONOBJECT_DECODED:
    case UA_EXTENSIONOBJECT_DECODED_NODELETE:
        // Every datatype from the mapped namespaces exists both in the
        // client-local config and the global config. The only difference
        // is the NodeId namespaceIndex. The ctx->customTypesArray is the
        // search target: for py->ua it is the client/server-local chain,
        // for ua->py it is the global chain.
        {
            const UA_DataType *sourceType = eo->content.decoded.type;
            UA_NodeId typeId = sourceType->typeId;
            typeId.namespaceIndex = ctx->map(ctx->nm, typeId.namespaceIndex);
            const UA_DataType *targetType =
                UA_findDataTypeWithCustom(&typeId, ctx->customTypesArray);
            if(targetType)
                eo->content.decoded.type = targetType;

            /* The decoded value is part of the surrounding value graph. Its
             * type pointer and every namespace-qualified value inside it must
             * cross the namespace boundary together. */
            const UA_DataType *contentType = eo->content.decoded.type;
            if(eo->content.decoded.data)
                mapJumpTable[contentType->typeKind](eo->content.decoded.data,
                                                    contentType, ctx);
        }
        break;
    }
}

static void
mapArray(void *p, size_t size, const UA_DataType *type, MapUAContext *ctx);

static void
mapVariant(void *p, const UA_DataType *_, MapUAContext *ctx) {
    UA_Variant *v = (UA_Variant*)p;
    const UA_DataType *type = v->type;
    if(!type)
        return;

    UA_NodeId typeId = type->typeId;
    typeId.namespaceIndex = ctx->map(ctx->nm, typeId.namespaceIndex);
    const UA_DataType *targetType =
        UA_findDataTypeWithCustom(&typeId, ctx->customTypesArray);
    v->type = targetType ? targetType : type;

    mapArray(v->data, UA_Variant_isScalar(v) ? 1 : v->arrayLength, v->type, ctx);
}

static void
mapDataValue(void *p, const UA_DataType *_, MapUAContext *ctx) {
    UA_DataValue *dv = (UA_DataValue*)p;
    if(dv->hasValue)
        mapVariant(&dv->value, NULL, ctx);
}

static void
mapArray(void *p, size_t size, const UA_DataType *type, MapUAContext *ctx) {
    if(mapJumpTable[type->typeKind] == mapNop)
        return; /* Nothing to do */
    uintptr_t ptr = (uintptr_t)p;
    mapSignature mapFunc = mapJumpTable[type->typeKind];
    for(size_t i = 0; i < size && ctx->status == UA_STATUSCODE_GOOD; ++i) {
        mapFunc((void*)ptr, type, ctx);
        ptr += type->memSize;
    }
}

static void
mapStructure(void *p, const UA_DataType *type, MapUAContext *ctx) {
    uintptr_t ptr = (uintptr_t)p;
    for(size_t i = 0; i < type->membersSize && ctx->status == UA_STATUSCODE_GOOD; ++i) {
        const UA_DataTypeMember *m = &type->members[i];
        const UA_DataType *mt = m->memberType;
        ptr += m->padding;
        if(!m->isOptional) {
            if(!m->isArray) {
                mapJumpTable[mt->typeKind]((void *)ptr, mt, ctx);
                ptr += mt->memSize;
            } else {
                size_t size = *(size_t*)ptr;
                ptr += sizeof(size_t);
                mapArray(*(void**)ptr, size, mt, ctx);
                ptr += sizeof(void*);
            }
        } else {
            if(!m->isArray) {
                if(*(void**)ptr != NULL)
                    mapArray(*(void**)ptr, 1, mt, ctx);
            } else {
                if(*(void**)(ptr+sizeof(size_t)) != NULL) {
                    const size_t size = *(const size_t*)ptr;
                    ptr += sizeof(size_t);
                    mapArray(*(void**)ptr, size, mt, ctx);
                } else {
                    ptr += sizeof(size_t);
                }
            }
            ptr += sizeof(void*);
        }
    }
}

static void
mapUnion(void *p, const UA_DataType *type, MapUAContext *ctx) {
    uintptr_t ptr = (uintptr_t)p;
    UA_UInt32 selection = *(UA_UInt32 *)ptr;
    if(selection == 0)
        return;
    if(selection > type->membersSize) {
        /* Keep failed mapping safe for the native cleanup path. */
        *(UA_UInt32*)ptr = 0;
        ctx->status = UA_STATUSCODE_BADDECODINGERROR;
        return;
    }
    const UA_DataTypeMember *m = &type->members[selection-1];
    const UA_DataType *mt = m->memberType;
    ptr += m->padding;
    if(m->isArray) {
        const size_t size = *(size_t*)ptr;
        ptr += sizeof(size_t);
        mapArray(*(void**)ptr, size, mt, ctx);
    } else {
        mapJumpTable[mt->typeKind]((void*)ptr, mt, ctx);
    }
}

const mapSignature mapJumpTable[UA_DATATYPEKINDS] = {
    (mapSignature)mapNop, /* Boolean */
    (mapSignature)mapNop, /* SByte */
    (mapSignature)mapNop, /* Byte */
    (mapSignature)mapNop, /* Int16 */
    (mapSignature)mapNop, /* UInt16 */
    (mapSignature)mapNop, /* Int32 */
    (mapSignature)mapNop, /* UInt32 */
    (mapSignature)mapNop, /* Int64 */
    (mapSignature)mapNop, /* UInt64 */
    (mapSignature)mapNop, /* Float */
    (mapSignature)mapNop, /* Double */
    (mapSignature)mapNop, /* String */
    (mapSignature)mapNop, /* DateTime */
    (mapSignature)mapNop, /* Guid */
    (mapSignature)mapNop, /* ByteString */
    (mapSignature)mapNop, /* XmlElement */
    (mapSignature)mapNodeId,
    (mapSignature)mapExpandedNodeId,
    (mapSignature)mapNop, /* StatusCode */
    (mapSignature)mapQualifiedName,
    (mapSignature)mapNop, /* LocalizedText */
    (mapSignature)mapExtensionObject,
    (mapSignature)mapDataValue,
    (mapSignature)mapVariant,
    (mapSignature)mapNop, /* DiagnosticInfo */
    (mapSignature)mapNop, /* Decimal */
    (mapSignature)mapNop, /* Enumeration */
    (mapSignature)mapStructure,
    (mapSignature)mapStructure, /* Structure with Optional Fields */
    (mapSignature)mapUnion, /* Union */
    (mapSignature)mapNop    /* BitfieldCluster*/
};

static UA_StatusCode
mapUA(void *p, const UA_DataType **type, MapUAContext *ctx) {
    const UA_DataType *mappedType = findMappedDatatype(*type, ctx);

    if(!mappedType)
        return UA_STATUSCODE_GOOD;

    *type = mappedType;

    /* Guard: an uninitialized mapping (all sizes zero) would map every index
     * to UA_UINT16_MAX - idx, which is a nonsensical namespace index for the
     * server and would corrupt wire-format data.  In that "no namespace
     * has been registered yet" state, just leave the indices alone. */
    if(!ctx->nm->local2remoteSize && !ctx->nm->remote2localSize)
        return UA_STATUSCODE_GOOD;
    mapJumpTable[(*type)->typeKind](p, *type, ctx);
    return ctx->status;
}

// ua->py look for typeId in globalTypesArray
UA_StatusCode mapNamespaceUA2Py(void *p, const UA_DataType **type, const UA_NamespaceMapping *nm) {
    MapUAContext ctx = {0};
    ctx.nm = nm;
    ctx.customTypesArray = o6_datatypes_global_chain();
    ctx.map = UA_NamespaceMapping_UA2Python;
    return mapUA(p, type, &ctx);
}

// py->ua look for typeId in localTypesArray (client/server customDataTypes)
UA_StatusCode mapNamespacePy2UA(void *p, const UA_DataType **type, const UA_NamespaceMapping *nm, const UA_DataTypeArray *customDataTypes) {
    MapUAContext ctx = {0};
    ctx.nm = nm;
    ctx.customTypesArray = customDataTypes;
    ctx.map = &UA_NamespaceMapping_Python2UA;
    return mapUA(p, type, &ctx);
}
