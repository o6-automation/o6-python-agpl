# Copyright (c) 2026 o6 Automation GmbH
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Generated OPC UA i4aas namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as i4aas_reftypes
from . import datatypes as i4aas_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=i4aas;i=1003", browseName="ns=i4aas;AASViewType", displayName="AASViewType")
class AASViewType(ns0.objtypes.FolderType):
    langleDataSpecificationRangle: AASReferenceType | None
    langleReferableRangle: AASReferenceType | None


@o6.objecttype(nodeId="ns=i4aas;i=1007", browseName="ns=i4aas;AASConceptDictionaryType", displayName="AASConceptDictionaryType")
class AASConceptDictionaryType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(nodeId="ns=i4aas;i=1031", browseName="ns=i4aas;ValueListType", displayName="ValueListType")
class ValueListType(ns0.objtypes.BaseObjectType):
    pass


AASConceptDictionaryType(nodeId="ns=i4aas;i=5005", browseName="ns=i4aas;<ConceptDictionary>", modellingRule="OptionalPlaceholder")
AASViewType(nodeId="ns=i4aas;i=5006", browseName="ns=i4aas;<View>", modellingRule="OptionalPlaceholder")
ValueListType(nodeId="ns=i4aas;i=5029", browseName="ns=i4aas;ValueList")
ns0.objtypes.BaseObjectType(nodeId="ns=i4aas;i=5041", browseName="ns=i4aas;<Referable>", modellingRule="OptionalPlaceholder")
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6001",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)


@o6.objecttype(nodeId="ns=i4aas;i=1004", browseName="ns=i4aas;AASReferenceType", displayName="AASReferenceType")
class AASReferenceType(ns0.objtypes.BaseObjectType):
    keys: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=i4aas;i=6001"])
    langleReferableRangle: ns0.objtypes.BaseObjectType | None = o6.hasComponent(o6.ns["ns=i4aas;i=5041"])


o6.reference(AASReferenceType, "ns=i4aas;i=4003", "ns=i4aas;i=5041")


ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6006",
    browseName="ns=i4aas;AssetKind",
    dataType=i4aas_datypes.AASAssetKindDataType,
    value=i4aas_datypes.AASAssetKindDataType.TYPE,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6009",
    browseName="ns=i4aas;ModelingKind",
    dataType=i4aas_datypes.AASModelingKindDataType,
    value=i4aas_datypes.AASModelingKindDataType.TEMPLATE,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6010", browseName="ns=i4aas;Type", dataType=o6.String, value="\n      ", accessLevel=3, userAccessLevel=1)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6013",
    browseName="ns=i4aas;ModelingKind",
    dataType=i4aas_datypes.AASModelingKindDataType,
    value=i4aas_datypes.AASModelingKindDataType.TEMPLATE,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6015",
    browseName="ns=i4aas;ValueType",
    dataType=i4aas_datypes.AASValueTypeDataType,
    value=i4aas_datypes.AASValueTypeDataType.BOOLEAN,
    accessLevel=3,
    userAccessLevel=1,
)
# WARNING: The source NodeSet value does not match the declared DataType.
# It is intentionally omitted; the server supplies a typed default.
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6017", browseName="ns=i4aas;AllowDuplicates", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6019", browseName="ns=i4aas;Value", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[1], value=[o6.LocalizedText()], accessLevel=3, userAccessLevel=1
)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6020", browseName="ns=i4aas;Value", accessLevel=3, userAccessLevel=1)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6021",
    browseName="ns=i4aas;ValueType",
    dataType=i4aas_datypes.AASValueTypeDataType,
    value=i4aas_datypes.AASValueTypeDataType.BOOLEAN,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6037", browseName="ns=i4aas;MimeType", dataType=i4aas_datypes.AASMimeDataType, value="\n      ", accessLevel=3, userAccessLevel=1)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6056",
    browseName="ns=i4aas;EntityType",
    dataType=i4aas_datypes.AASEntityTypeDataType,
    value=i4aas_datypes.AASEntityTypeDataType.CO_MANAGED_ENTITY,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6057",
    browseName="ns=i4aas;ValueType",
    dataType=i4aas_datypes.AASValueTypeDataType,
    value=i4aas_datypes.AASValueTypeDataType.BOOLEAN,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6058", browseName="ns=i4aas;Min", accessLevel=3, userAccessLevel=1)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6059", browseName="ns=i4aas;Max", accessLevel=3, userAccessLevel=1)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6065",
    browseName="ns=i4aas;Category",
    dataType=i4aas_datypes.AASCategoryDataType,
    value=i4aas_datypes.AASCategoryDataType.CONSTANT,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6066", browseName="ns=i4aas;ShortName", dataType=o6.LocalizedText, value=o6.LocalizedText(), accessLevel=3, userAccessLevel=1)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6067", browseName="ns=i4aas;SourceOfDefinition", dataType=o6.String, value="\n      ", accessLevel=3, userAccessLevel=1)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6068", browseName="ns=i4aas;Symbol", dataType=o6.String, value="\n      ", accessLevel=3, userAccessLevel=1)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6069", browseName="ns=i4aas;Unit", dataType=o6.String, value="\n      ", accessLevel=3, userAccessLevel=1)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6070", browseName="ns=i4aas;ValueFormat", dataType=o6.String, value="\n      ", accessLevel=3, userAccessLevel=1)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6071", browseName="ns=i4aas;Value", accessLevel=3, userAccessLevel=1)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6072",
    browseName="ns=i4aas;DataType",
    dataType=i4aas_datypes.AASDataTypeIEC61360DataType,
    value=i4aas_datypes.AASDataTypeIEC61360DataType.BOOLEAN,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6073", browseName="ns=i4aas;Definition", dataType=o6.LocalizedText, value=o6.LocalizedText(), accessLevel=3, userAccessLevel=1)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6074", browseName="ns=i4aas;PreferredName", dataType=o6.LocalizedText, value=o6.LocalizedText(), accessLevel=3, userAccessLevel=1)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6075",
    browseName="ns=i4aas;LevelType",
    dataType=i4aas_datypes.AASLevelTypeDataType,
    value=i4aas_datypes.AASLevelTypeDataType.MIN,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6078", browseName="ns=i4aas;Value", accessLevel=3, userAccessLevel=1)


@o6.objecttype(nodeId="ns=i4aas;i=1032", browseName="ns=i4aas;AASQualifierType", displayName="AASQualifierType")
class AASQualifierType(ns0.objtypes.BaseObjectType):
    type: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=i4aas;i=6010"])
    value: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=i4aas;i=6078"])
    valueId: AASReferenceType | None
    valueType: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=i4aas;i=6015"])


ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6082", browseName="ns=i4aas;Category", dataType=o6.String, value="\n      ", accessLevel=3, userAccessLevel=1)


@o6.objecttype(nodeId="ns=i4aas;i=1033", browseName="ns=i4aas;IAASReferableType", displayName="IAASReferableType")
class IAASReferableType(ns0.objtypes.BaseInterfaceType):
    category: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=i4aas;i=6082"])


ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6083", browseName="ns=i4aas;Version", dataType=o6.String, value="\n      ", accessLevel=3, userAccessLevel=1)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6084", browseName="ns=i4aas;Revision", dataType=o6.String, value="\n      ", accessLevel=3, userAccessLevel=1)


@o6.objecttype(nodeId="ns=i4aas;i=1030", browseName="ns=i4aas;AASAdministrativeInformationType", displayName="AASAdministrativeInformationType")
class AASAdministrativeInformationType(ns0.objtypes.BaseObjectType):
    revision: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=i4aas;i=6084"])
    version: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=i4aas;i=6083"])


AASAdministrativeInformationType(nodeId="ns=i4aas;i=5027", browseName="ns=i4aas;Administration")
AASAdministrativeInformationType(nodeId="ns=i4aas;i=5035", browseName="ns=i4aas;Administration")


@o6.objecttype(nodeId="ns=i4aas;i=1034", browseName="ns=i4aas;IAASIdentifiableType", displayName="IAASIdentifiableType")
class IAASIdentifiableType(IAASReferableType):
    administration: AASAdministrativeInformationType = o6.hasComponent(o6.ns["ns=i4aas;i=5035"])
    identification: AASIdentifierType


@o6.objecttype(nodeId="ns=i4aas;i=1002", browseName="ns=i4aas;AASAssetAdministrationShellType", displayName="AASAssetAdministrationShellType", interfaces=[IAASIdentifiableType])
class AASAssetAdministrationShellType(ns0.objtypes.BaseObjectType):
    asset: AASAssetType
    derivedFrom: AASReferenceType | None
    langleConceptDictionaryRangle: AASConceptDictionaryType | None = o6.hasComponent(o6.ns["ns=i4aas;i=5005"])
    langleDataSpecificationRangle: AASReferenceType | None
    langleSubmodelRangle: AASSubmodelType | None
    langleSubmodelReferenceRangle: AASReferenceType | None
    langleViewRangle: AASViewType | None = o6.hasComponent(o6.ns["ns=i4aas;i=5006"])


@o6.objecttype(nodeId="ns=i4aas;i=1005", browseName="ns=i4aas;AASAssetType", displayName="AASAssetType", interfaces=[IAASIdentifiableType])
class AASAssetType(ns0.objtypes.BaseObjectType):
    assetIdentificationModel: AASReferenceType | None
    assetKind: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=i4aas;i=6006"])
    billOfMaterial: AASReferenceType | None
    langleDataSpecificationRangle: AASReferenceType | None


@o6.objecttype(nodeId="ns=i4aas;i=1006", browseName="ns=i4aas;AASSubmodelType", displayName="AASSubmodelType", interfaces=[IAASIdentifiableType])
class AASSubmodelType(ns0.objtypes.BaseObjectType):
    langleDataSpecificationRangle: AASReferenceType | None
    langleQualifierRangle: AASQualifierType | None
    langleSubmodelElementRangle: AASSubmodelElementType | None
    modelingKind: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=i4aas;i=6009"])


@o6.objecttype(nodeId="ns=i4aas;i=1024", browseName="ns=i4aas;AASIrdiConceptDescriptionType", displayName="AASIrdiConceptDescriptionType", interfaces=[IAASIdentifiableType])
class AASIrdiConceptDescriptionType(ns0.objtypes.IrdiDictionaryEntryType):
    langleConceptDescriptionRangle: AASReferenceType | None
    langleDataSpecificationRangle: AASReferenceType | None


@o6.objecttype(nodeId="ns=i4aas;i=1025", browseName="ns=i4aas;AASIriConceptDescriptionType", displayName="AASIriConceptDescriptionType", interfaces=[IAASIdentifiableType])
class AASIriConceptDescriptionType(ns0.objtypes.UriDictionaryEntryType):
    langleConceptDescriptionRangle: AASReferenceType | None
    langleDataSpecificationRangle: AASReferenceType | None


@o6.objecttype(nodeId="ns=i4aas;i=1026", browseName="ns=i4aas;AASCustomConceptDescriptionType", displayName="AASCustomConceptDescriptionType", interfaces=[IAASIdentifiableType])
class AASCustomConceptDescriptionType(ns0.objtypes.DictionaryEntryType):
    langleConceptDescriptionRangle: AASReferenceType | None
    langleDataSpecificationRangle: AASReferenceType | None


@o6.objecttype(nodeId="ns=i4aas;i=1027", browseName="ns=i4aas;AASDataSpecificationType", displayName="AASDataSpecificationType", isAbstract=True, interfaces=[IAASIdentifiableType])
class AASDataSpecificationType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(nodeId="ns=i4aas;i=1028", browseName="ns=i4aas;AASDataSpecificationIEC61360Type", displayName="AASDataSpecificationIEC61360Type")
class AASDataSpecificationIEC61360Type(AASDataSpecificationType):
    administration: AASAdministrativeInformationType = o6.hasComponent(o6.ns["ns=i4aas;i=5027"])
    category: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=i4aas;i=6065"])
    dataType: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=i4aas;i=6072"])
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=i4aas;i=6063", browseName="ns=i4aas;DefaultInstanceBrowseName", dataType=o6.String, value="DataSpecificationIEC61360", accessLevel=3, userAccessLevel=1
        )
    )
    definition: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=i4aas;i=6073"])
    identification: AASIdentifierType
    levelType: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=i4aas;i=6075"])
    preferredName: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=i4aas;i=6074"])
    shortName: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=i4aas;i=6066"])
    sourceOfDefinition: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=i4aas;i=6067"])
    symbol: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=i4aas;i=6068"])
    unit: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=i4aas;i=6069"])
    unitId: AASReferenceType | None
    value: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=i4aas;i=6071"])
    valueFormat: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=i4aas;i=6070"])
    valueId: AASReferenceType | None
    valueList: ValueListType | None = o6.hasComponent(o6.ns["ns=i4aas;i=5029"])


ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6085",
    browseName="ns=i4aas;IdType",
    dataType=i4aas_datypes.AASIdentifierTypeDataType,
    value=i4aas_datypes.AASIdentifierTypeDataType.IRDI,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6086", browseName="ns=i4aas;Id", dataType=o6.String, value="\n      ", accessLevel=3, userAccessLevel=1)


@o6.objecttype(nodeId="ns=i4aas;i=1029", browseName="ns=i4aas;AASIdentifierType", displayName="AASIdentifierType")
class AASIdentifierType(ns0.objtypes.BaseObjectType):
    id: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=i4aas;i=6086"])
    idType: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=i4aas;i=6085"])


@o6.objecttype(nodeId="ns=i4aas;i=1009", browseName="ns=i4aas;AASSubmodelElementType", displayName="AASSubmodelElementType", isAbstract=True, interfaces=[IAASReferableType])
class AASSubmodelElementType(ns0.objtypes.BaseObjectType):
    category: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6126", browseName="ns=i4aas;Category", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    langleDataSpecificationRangle: AASReferenceType | None
    langleQualifierRangle: AASQualifierType | None
    modelingKind: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=i4aas;i=6013"])


@o6.objecttype(nodeId="ns=i4aas;i=1010", browseName="ns=i4aas;AASSubmodelElementCollectionType", displayName="AASSubmodelElementCollectionType")
class AASSubmodelElementCollectionType(AASSubmodelElementType):
    allowDuplicates: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=i4aas;i=6017"])
    langleSubmodelElementRangle: AASSubmodelElementType | None


@o6.objecttype(nodeId="ns=i4aas;i=1011", browseName="ns=i4aas;AASOrderedSubmodelElementCollectionType", displayName="AASOrderedSubmodelElementCollectionType")
class AASOrderedSubmodelElementCollectionType(AASSubmodelElementCollectionType):
    langleSubmodelElementRangle: AASSubmodelElementType | None


@o6.objecttype(nodeId="ns=i4aas;i=1012", browseName="ns=i4aas;AASMultiLanguagePropertyType", displayName="AASMultiLanguagePropertyType")
class AASMultiLanguagePropertyType(AASSubmodelElementType):
    value: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=i4aas;i=6019"])
    valueId: AASReferenceType | None


@o6.objecttype(nodeId="ns=i4aas;i=1013", browseName="ns=i4aas;AASPropertyType", displayName="AASPropertyType")
class AASPropertyType(AASSubmodelElementType):
    value: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=i4aas;i=6020"])
    valueId: AASReferenceType | None
    valueType: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=i4aas;i=6021"])


@o6.objecttype(nodeId="ns=i4aas;i=1014", browseName="ns=i4aas;AASCapabilityType", displayName="AASCapabilityType")
class AASCapabilityType(AASSubmodelElementType):
    pass


@o6.objecttype(nodeId="ns=i4aas;i=1016", browseName="ns=i4aas;AASBlobType", displayName="AASBlobType")
class AASBlobType(AASSubmodelElementType):
    file: ns0.objtypes.FileType


@o6.objecttype(nodeId="ns=i4aas;i=1018", browseName="ns=i4aas;AASRelationshipElementType", displayName="AASRelationshipElementType")
class AASRelationshipElementType(AASSubmodelElementType):
    first: AASReferenceType
    second: AASReferenceType


@o6.objecttype(nodeId="ns=i4aas;i=1019", browseName="ns=i4aas;AASAnnotatedRelationshipElementType", displayName="AASAnnotatedRelationshipElementType")
class AASAnnotatedRelationshipElementType(AASRelationshipElementType):
    langleDataElementRangle: AASSubmodelElementType | None


@o6.objecttype(nodeId="ns=i4aas;i=1020", browseName="ns=i4aas;AASReferenceElementType", displayName="AASReferenceElementType")
class AASReferenceElementType(AASSubmodelElementType):
    value: AASReferenceType


@o6.objecttype(nodeId="ns=i4aas;i=1021", browseName="ns=i4aas;AASEventType", displayName="AASEventType")
class AASEventType(AASSubmodelElementType):
    pass


@o6.objecttype(nodeId="ns=i4aas;i=1022", browseName="ns=i4aas;AASEntityType", displayName="AASEntityType")
class AASEntityType(AASSubmodelElementType):
    asset: AASReferenceType | None
    entityType: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=i4aas;i=6056"])
    langleSubmodelElementRangle: AASSubmodelElementType | None


@o6.objecttype(nodeId="ns=i4aas;i=1023", browseName="ns=i4aas;AASRangeType", displayName="AASRangeType")
class AASRangeType(AASSubmodelElementType):
    max: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=i4aas;i=6059"])
    min: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=i4aas;i=6058"])
    valueType: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=i4aas;i=6057"])


@o6.objecttype(nodeId="ns=i4aas;i=1017", browseName="ns=i4aas;AASFileType", displayName="AASFileType")
class AASFileType(AASSubmodelElementType):
    file: ns0.objtypes.FileType | None
    mimeType: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=i4aas;i=6037"])
    value: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6132", browseName="ns=i4aas;Value", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=i4aas;i=1015", browseName="ns=i4aas;AASOperationType", displayName="AASOperationType")
class AASOperationType(AASSubmodelElementType):
    operation: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="ns=i4aas;i=7001", browseName="ns=i4aas;Operation", modellingRule="MandatoryPlaceholder"))


del Any, TYPE_CHECKING, uuid, o6, ns0, i4aas_reftypes, i4aas_datypes
