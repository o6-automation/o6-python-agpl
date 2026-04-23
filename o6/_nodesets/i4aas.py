# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 7c2c1035d21ed4c6f15dd5be5c2e4f2577390b525556d68fd983b0e102f96693
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/I4AAS/"
_VERSION: str = "5.0.0"
_REQUIRED: list = [{"uri": "http://opcfoundation.org/UA/", "version": "1.04.3"}]
_STRUCTURES: list = [
    (
        "ns=1;i=3011",
        "AASKeyDataType",
        "ns=1;i=5038",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Type", "data_type": "ns=1;i=3012", "value_rank": -1},
                {"name": "Local", "data_type": "i=1", "value_rank": -1},
                {"name": "Value", "data_type": "i=12", "value_rank": -1},
                {"name": "IdType", "data_type": "ns=1;i=3002", "value_rank": -1},
            ],
        },
    )
]
_ENUMS: list = [
    (
        "ns=1;i=3003",
        "AASAssetKindDataType",
        {
            "fields": [
                {"name": "Type", "value": 0, "display_name": "Type"},
                {"name": "Instance", "value": 1, "display_name": "Instance"},
            ]
        },
    ),
    (
        "ns=1;i=3007",
        "AASCategoryDataType",
        {
            "fields": [
                {"name": "CONSTANT", "value": 0, "display_name": "CONSTANT"},
                {"name": "PARAMETER", "value": 1, "display_name": "PARAMETER"},
                {"name": "VARIABLE", "value": 2, "display_name": "VARIABLE"},
                {"name": "RELATIONSHIP", "value": 3, "display_name": "RELATIONSHIP"},
            ]
        },
    ),
    (
        "ns=1;i=3008",
        "AASDataTypeIEC61360DataType",
        {
            "fields": [
                {"name": "BOOLEAN", "value": 0, "display_name": "BOOLEAN"},
                {"name": "DATE", "value": 1, "display_name": "DATE"},
                {"name": "RATIONAL", "value": 2, "display_name": "RATIONAL"},
                {
                    "name": "RATIONAL_MEASURE",
                    "value": 3,
                    "display_name": "RATIONAL_MEASURE",
                },
                {"name": "REAL_COUNT", "value": 4, "display_name": "REAL_COUNT"},
                {"name": "REAL_CURRENCY", "value": 5, "display_name": "REAL_CURRENCY"},
                {"name": "REAL_MEASURE", "value": 6, "display_name": "REAL_MEASURE"},
                {"name": "STRING", "value": 7, "display_name": "STRING"},
                {
                    "name": "STRING_TRANSLATABLE",
                    "value": 8,
                    "display_name": "STRING_TRANSLATABLE",
                },
                {"name": "TIME", "value": 9, "display_name": "TIME"},
                {"name": "TIME_STAMP", "value": 10, "display_name": "TIME_STAMP"},
                {"name": "URL", "value": 11, "display_name": "URL"},
                {"name": "INTEGER", "value": 12, "display_name": "INTEGER"},
                {"name": "INTEGER_COUNT", "value": 13, "display_name": "INTEGER_COUNT"},
                {
                    "name": "INTEGER_CURRENCY",
                    "value": 14,
                    "display_name": "INTEGER_CURRENCY",
                },
            ]
        },
    ),
    (
        "ns=1;i=3006",
        "AASEntityTypeDataType",
        {
            "fields": [
                {
                    "name": "CoManagedEntity",
                    "value": 0,
                    "display_name": "CoManagedEntity",
                },
                {
                    "name": "SelfManagedEntity",
                    "value": 1,
                    "display_name": "SelfManagedEntity",
                },
            ]
        },
    ),
    (
        "ns=1;i=3010",
        "AASIdentifierTypeDataType",
        {
            "fields": [
                {"name": "IRDI", "value": 0, "display_name": "IRDI"},
                {"name": "IRI", "value": 1, "display_name": "IRI"},
                {"name": "Custom", "value": 2, "display_name": "Custom"},
            ]
        },
    ),
    (
        "ns=1;i=3012",
        "AASKeyElementsDataType",
        {
            "fields": [
                {
                    "name": "AccessPermissionRule",
                    "value": 0,
                    "display_name": "AccessPermissionRule",
                },
                {
                    "name": "AnnotatedRelationshipElement",
                    "value": 1,
                    "display_name": "AnnotatedRelationshipElement",
                },
                {"name": "Asset", "value": 2, "display_name": "Asset"},
                {
                    "name": "AssetAdministrationShell",
                    "value": 3,
                    "display_name": "AssetAdministrationShell",
                },
                {"name": "Blob", "value": 4, "display_name": "Blob"},
                {"name": "Capability", "value": 5, "display_name": "Capability"},
                {
                    "name": "ConceptDescription",
                    "value": 6,
                    "display_name": "ConceptDescription",
                },
                {
                    "name": "ConceptDictionary",
                    "value": 7,
                    "display_name": "ConceptDictionary",
                },
                {"name": "DataElement", "value": 8, "display_name": "DataElement"},
                {"name": "Entity", "value": 9, "display_name": "Entity"},
                {"name": "Event", "value": 10, "display_name": "Event"},
                {"name": "File", "value": 11, "display_name": "File"},
                {
                    "name": "FragmentReference",
                    "value": 12,
                    "display_name": "FragmentReference",
                },
                {
                    "name": "GlobalReference",
                    "value": 13,
                    "display_name": "GlobalReference",
                },
                {
                    "name": "MultiLanguageProperty",
                    "value": 14,
                    "display_name": "MultiLanguageProperty",
                },
                {"name": "Operation", "value": 15, "display_name": "Operation"},
                {"name": "Property", "value": 16, "display_name": "Property"},
                {"name": "Range", "value": 17, "display_name": "Range"},
                {
                    "name": "ReferenceElement",
                    "value": 18,
                    "display_name": "ReferenceElement",
                },
                {
                    "name": "RelationshipElement",
                    "value": 19,
                    "display_name": "RelationshipElement",
                },
                {"name": "Submodel", "value": 20, "display_name": "Submodel"},
                {
                    "name": "SubmodelElement",
                    "value": 21,
                    "display_name": "SubmodelElement",
                },
                {
                    "name": "SubmodelElementCollection",
                    "value": 22,
                    "display_name": "SubmodelElementCollection",
                },
                {"name": "View", "value": 23, "display_name": "View"},
            ]
        },
    ),
    (
        "ns=1;i=3002",
        "AASKeyTypeDataType",
        {
            "fields": [
                {"name": "IdShort", "value": 0, "display_name": "IdShort"},
                {"name": "FragmentId", "value": 1, "display_name": "FragmentId"},
                {"name": "Custom", "value": 2, "display_name": "Custom"},
                {"name": "IRDI", "value": 3, "display_name": "IRDI"},
                {"name": "IRI", "value": 4, "display_name": "IRI"},
            ]
        },
    ),
    (
        "ns=1;i=3009",
        "AASLevelTypeDataType",
        {
            "fields": [
                {"name": "Min", "value": 0, "display_name": "Min"},
                {"name": "Max", "value": 1, "display_name": "Max"},
                {"name": "Num", "value": 2, "display_name": "Num"},
                {"name": "Type", "value": 3, "display_name": "Type"},
            ]
        },
    ),
    (
        "ns=1;i=3015",
        "AASModelingKindDataType",
        {
            "fields": [
                {"name": "Template", "value": 0, "display_name": "Template"},
                {"name": "Instance", "value": 1, "display_name": "Instance"},
            ]
        },
    ),
    (
        "ns=1;i=3004",
        "AASValueTypeDataType",
        {
            "fields": [
                {"name": "Boolean", "value": 0, "display_name": "Boolean"},
                {"name": "SByte", "value": 1, "display_name": "SByte"},
                {"name": "Byte", "value": 2, "display_name": "Byte"},
                {"name": "Int16", "value": 3, "display_name": "Int16"},
                {"name": "UInt16", "value": 4, "display_name": "UInt16"},
                {"name": "Int32", "value": 5, "display_name": "Int32"},
                {"name": "UInt32", "value": 6, "display_name": "UInt32"},
                {"name": "Int64", "value": 7, "display_name": "Int64"},
                {"name": "UInt64", "value": 8, "display_name": "UInt64"},
                {"name": "Float", "value": 9, "display_name": "Float"},
                {"name": "Double", "value": 10, "display_name": "Double"},
                {"name": "String", "value": 11, "display_name": "String"},
                {"name": "DateTime", "value": 12, "display_name": "DateTime"},
                {"name": "ByteString", "value": 13, "display_name": "ByteString"},
                {"name": "LocalizedText", "value": 14, "display_name": "LocalizedText"},
                {"name": "UtcTime", "value": 15, "display_name": "UtcTime"},
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [("ns=1;i=3011", "ns=1;i=5038", ["ns=1;i=3012", "i=1", "i=12", "ns=1;i=3002"])],
    [
        "ns=1;i=3003",
        "ns=1;i=3007",
        "ns=1;i=3008",
        "ns=1;i=3006",
        "ns=1;i=3010",
        "ns=1;i=3012",
        "ns=1;i=3002",
        "ns=1;i=3009",
        "ns=1;i=3015",
        "ns=1;i=3004",
    ],
)
_NODES: dict = {
    "datatypes": {
        "AASAssetKindDataType": (
            "D",
            "ns=1;i=3003",
            {"EnumValues": ("V", "ns=1;i=6099", {})},
        ),
        "AASCategoryDataType": (
            "D",
            "ns=1;i=3007",
            {"EnumValues": ("V", "ns=1;i=6109", {})},
        ),
        "AASDataTypeIEC61360DataType": (
            "D",
            "ns=1;i=3008",
            {"EnumStrings": ("V", "ns=1;i=6111", {})},
        ),
        "AASEntityTypeDataType": (
            "D",
            "ns=1;i=3006",
            {"EnumValues": ("V", "ns=1;i=6103", {})},
        ),
        "AASIdentifierTypeDataType": (
            "D",
            "ns=1;i=3010",
            {"EnumValues": ("V", "ns=1;i=6093", {})},
        ),
        "AASKeyDataType": ("D", "ns=1;i=3011", {}),
        "AASKeyElementsDataType": (
            "D",
            "ns=1;i=3012",
            {"EnumValues": ("V", "ns=1;i=6101", {})},
        ),
        "AASKeyTypeDataType": (
            "D",
            "ns=1;i=3002",
            {"EnumValues": ("V", "ns=1;i=6108", {})},
        ),
        "AASLevelTypeDataType": (
            "D",
            "ns=1;i=3009",
            {"EnumValues": ("V", "ns=1;i=6102", {})},
        ),
        "AASMimeDataType": ("D", "ns=1;i=3016", {}),
        "AASModelingKindDataType": (
            "D",
            "ns=1;i=3015",
            {"EnumValues": ("V", "ns=1;i=6125", {})},
        ),
        "AASPathDataType": ("D", "ns=1;i=3005", {}),
        "AASPropertyValueDataType": ("D", "ns=1;i=3014", {}),
        "AASQualifierDataType": ("D", "ns=1;i=3013", {}),
        "AASValueTypeDataType": (
            "D",
            "ns=1;i=3004",
            {"EnumStrings": ("V", "ns=1;i=6110", {})},
        ),
    },
    "ifacetypes": {
        "IAASReferableType": (
            "OT",
            "ns=1;i=1033",
            {
                "Category": ("V", "ns=1;i=6082", {}),
                "IAASIdentifiableType": (
                    "OT",
                    "ns=1;i=1034",
                    {
                        "Administration": ("O", "ns=1;i=5035", {}),
                        "Identification": (
                            "O",
                            "ns=1;i=5034",
                            {
                                "Id": ("V", "ns=1;i=6090", {}),
                                "IdType": ("V", "ns=1;i=6089", {}),
                            },
                        ),
                    },
                ),
            },
        )
    },
    "objects": {
        "<IRDI_or_IRI_or_Custom_concept_description_entry>": ("O", "ns=1;i=5101", {}),
        "<SubmodelElement>": (
            "O",
            "ns=1;i=5042",
            {
                "Category": ("V", "ns=1;i=6131", {}),
                "IdShort": ("V", "ns=1;i=6124", {}),
                "ModelingKind": ("V", "ns=1;i=6104", {}),
            },
        ),
        "Admin-shell.io/DataSpecification/administration": ("O", "ns=1;i=5132", {}),
        "Admin-shell.io/DataSpecification/category": ("O", "ns=1;i=5133", {}),
        "Admin-shell.io/DataSpecification/idShort": ("O", "ns=1;i=5135", {}),
        "Admin-shell.io/DataSpecification/identification": ("O", "ns=1;i=5134", {}),
        "Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0": (
            "O",
            "ns=1;i=5136",
            {},
        ),
        "Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/dataType": (
            "O",
            "ns=1;i=5137",
            {},
        ),
        "Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/definition": (
            "O",
            "ns=1;i=5138",
            {},
        ),
        "Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/levelType": (
            "O",
            "ns=1;i=5139",
            {},
        ),
        "Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/preferredName": (
            "O",
            "ns=1;i=5140",
            {},
        ),
        "Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/shortName": (
            "O",
            "ns=1;i=5141",
            {},
        ),
        "Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/sourceOfDefinition": (
            "O",
            "ns=1;i=5142",
            {},
        ),
        "Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/symbol": (
            "O",
            "ns=1;i=5143",
            {},
        ),
        "Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/unit": (
            "O",
            "ns=1;i=5144",
            {},
        ),
        "Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/unitId": (
            "O",
            "ns=1;i=5145",
            {},
        ),
        "Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/value": (
            "O",
            "ns=1;i=5146",
            {},
        ),
        "Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/valueFormat": (
            "O",
            "ns=1;i=5147",
            {},
        ),
        "Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/valueId": (
            "O",
            "ns=1;i=5148",
            {},
        ),
        "Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0/valueList": (
            "O",
            "ns=1;i=5149",
            {},
        ),
        "Admin-shell.io/aas/2/0/AdministrativeInformation": ("O", "ns=1;i=5047", {}),
        "Admin-shell.io/aas/2/0/AdministrativeInformation/revision": (
            "O",
            "ns=1;i=5045",
            {},
        ),
        "Admin-shell.io/aas/2/0/AdministrativeInformation/version": (
            "O",
            "ns=1;i=5051",
            {},
        ),
        "Admin-shell.io/aas/2/0/AnnotatedRelationshipElement": ("O", "ns=1;i=5055", {}),
        "Admin-shell.io/aas/2/0/AnnotatedRelationshipElement/annotations": (
            "O",
            "ns=1;i=5056",
            {},
        ),
        "Admin-shell.io/aas/2/0/Asset": ("O", "ns=1;i=5052", {}),
        "Admin-shell.io/aas/2/0/Asset/assetIdentificationModel": (
            "O",
            "ns=1;i=5053",
            {},
        ),
        "Admin-shell.io/aas/2/0/Asset/assetKind": ("O", "ns=1;i=5054", {}),
        "Admin-shell.io/aas/2/0/Asset/billOfMaterial": ("O", "ns=1;i=5057", {}),
        "Admin-shell.io/aas/2/0/Asset/dataSpecifications": ("O", "ns=1;i=5058", {}),
        "Admin-shell.io/aas/2/0/AssetAdministrationShell": ("O", "ns=1;i=5059", {}),
        "Admin-shell.io/aas/2/0/AssetAdministrationShell/asset": (
            "O",
            "ns=1;i=5060",
            {},
        ),
        "Admin-shell.io/aas/2/0/AssetAdministrationShell/conceptDictionaries": (
            "O",
            "ns=1;i=5061",
            {},
        ),
        "Admin-shell.io/aas/2/0/AssetAdministrationShell/dataSpecifications": (
            "O",
            "ns=1;i=5062",
            {},
        ),
        "Admin-shell.io/aas/2/0/AssetAdministrationShell/derivedFrom": (
            "O",
            "ns=1;i=5063",
            {},
        ),
        "Admin-shell.io/aas/2/0/AssetAdministrationShell/submodels": (
            "O",
            "ns=1;i=5064",
            {},
        ),
        "Admin-shell.io/aas/2/0/AssetAdministrationShell/views": (
            "O",
            "ns=1;i=5065",
            {},
        ),
        "Admin-shell.io/aas/2/0/BasicEvent": ("O", "ns=1;i=5066", {}),
        "Admin-shell.io/aas/2/0/Blob": ("O", "ns=1;i=5067", {}),
        "Admin-shell.io/aas/2/0/Blob/mimeType": ("O", "ns=1;i=5068", {}),
        "Admin-shell.io/aas/2/0/Blob/value": ("O", "ns=1;i=5069", {}),
        "Admin-shell.io/aas/2/0/ConceptDescription": ("O", "ns=1;i=5070", {}),
        "Admin-shell.io/aas/2/0/ConceptDescription/IsCaseOf": ("O", "ns=1;i=5072", {}),
        "Admin-shell.io/aas/2/0/ConceptDescription/dataSpecifications": (
            "O",
            "ns=1;i=5071",
            {},
        ),
        "Admin-shell.io/aas/2/0/DataSpecification": ("O", "ns=1;i=5073", {}),
        "Admin-shell.io/aas/2/0/Entity": ("O", "ns=1;i=5074", {}),
        "Admin-shell.io/aas/2/0/Entity/asset": ("O", "ns=1;i=5075", {}),
        "Admin-shell.io/aas/2/0/Entity/entityType": ("O", "ns=1;i=5076", {}),
        "Admin-shell.io/aas/2/0/Entity/statements": ("O", "ns=1;i=5077", {}),
        "Admin-shell.io/aas/2/0/File": ("O", "ns=1;i=5078", {}),
        "Admin-shell.io/aas/2/0/File/mimeType": ("O", "ns=1;i=5079", {}),
        "Admin-shell.io/aas/2/0/File/value": ("O", "ns=1;i=5080", {}),
        "Admin-shell.io/aas/2/0/HasKind/kind": ("O", "ns=1;i=5081", {}),
        "Admin-shell.io/aas/2/0/Identifiable": ("O", "ns=1;i=5082", {}),
        "Admin-shell.io/aas/2/0/Identifiable/administration": ("O", "ns=1;i=5083", {}),
        "Admin-shell.io/aas/2/0/Identifiable/identification": ("O", "ns=1;i=5084", {}),
        "Admin-shell.io/aas/2/0/Identifier": ("O", "ns=1;i=5085", {}),
        "Admin-shell.io/aas/2/0/Identifier/id": ("O", "ns=1;i=5086", {}),
        "Admin-shell.io/aas/2/0/Identifier/idType": ("O", "ns=1;i=5087", {}),
        "Admin-shell.io/aas/2/0/IdentifierType/Custom": ("O", "ns=1;i=5088", {}),
        "Admin-shell.io/aas/2/0/IdentifierType/IRDI": ("O", "ns=1;i=5089", {}),
        "Admin-shell.io/aas/2/0/IdentifierType/IRI": ("O", "ns=1;i=5090", {}),
        "Admin-shell.io/aas/2/0/MultiLanguageProperty": ("O", "ns=1;i=5091", {}),
        "Admin-shell.io/aas/2/0/MultiLanguageProperty/value": ("O", "ns=1;i=5092", {}),
        "Admin-shell.io/aas/2/0/MultiLanguageProperty/valueId": (
            "O",
            "ns=1;i=5093",
            {},
        ),
        "Admin-shell.io/aas/2/0/Operation": ("O", "ns=1;i=5094", {}),
        "Admin-shell.io/aas/2/0/Property": ("O", "ns=1;i=5095", {}),
        "Admin-shell.io/aas/2/0/Property/value": ("O", "ns=1;i=5096", {}),
        "Admin-shell.io/aas/2/0/Property/valueId": ("O", "ns=1;i=5097", {}),
        "Admin-shell.io/aas/2/0/Property/valueType": ("O", "ns=1;i=5098", {}),
        "Admin-shell.io/aas/2/0/Qualifier": ("O", "ns=1;i=5099", {}),
        "Admin-shell.io/aas/2/0/Qualifier/type": ("O", "ns=1;i=5100", {}),
        "Admin-shell.io/aas/2/0/Qualifier/value": ("O", "ns=1;i=5102", {}),
        "Admin-shell.io/aas/2/0/Qualifier/valueType": ("O", "ns=1;i=5104", {}),
        "Admin-shell.io/aas/2/0/Range": ("O", "ns=1;i=5105", {}),
        "Admin-shell.io/aas/2/0/Range/max": ("O", "ns=1;i=5106", {}),
        "Admin-shell.io/aas/2/0/Range/min": ("O", "ns=1;i=5107", {}),
        "Admin-shell.io/aas/2/0/Range/valueType": ("O", "ns=1;i=5108", {}),
        "Admin-shell.io/aas/2/0/Referable": ("O", "ns=1;i=5109", {}),
        "Admin-shell.io/aas/2/0/Referable/category": ("O", "ns=1;i=5110", {}),
        "Admin-shell.io/aas/2/0/Reference": ("O", "ns=1;i=5111", {}),
        "Admin-shell.io/aas/2/0/Reference/keys": ("O", "ns=1;i=5112", {}),
        "Admin-shell.io/aas/2/0/ReferenceElement": ("O", "ns=1;i=5113", {}),
        "Admin-shell.io/aas/2/0/ReferenceElement/value": ("O", "ns=1;i=5114", {}),
        "Admin-shell.io/aas/2/0/RelationshipElement": ("O", "ns=1;i=5115", {}),
        "Admin-shell.io/aas/2/0/RelationshipElement/first": ("O", "ns=1;i=5116", {}),
        "Admin-shell.io/aas/2/0/RelationshipElement/second": ("O", "ns=1;i=5117", {}),
        "Admin-shell.io/aas/2/0/Submodel": ("O", "ns=1;i=5118", {}),
        "Admin-shell.io/aas/2/0/Submodel/qualifiers": ("O", "ns=1;i=5119", {}),
        "Admin-shell.io/aas/2/0/Submodel/submodelElements": ("O", "ns=1;i=5120", {}),
        "Admin-shell.io/aas/2/0/SubmodelElement": ("O", "ns=1;i=5121", {}),
        "Admin-shell.io/aas/2/0/SubmodelElement/dataSpecifications": (
            "O",
            "ns=1;i=5122",
            {},
        ),
        "Admin-shell.io/aas/2/0/SubmodelElement/idShort": ("O", "ns=1;i=5123", {}),
        "Admin-shell.io/aas/2/0/SubmodelElement/kind": ("O", "ns=1;i=5124", {}),
        "Admin-shell.io/aas/2/0/SubmodelElement/qualifiers": ("O", "ns=1;i=5125", {}),
        "Admin-shell.io/aas/2/0/SubmodelElementCollection": ("O", "ns=1;i=5126", {}),
        "Admin-shell.io/aas/2/0/SubmodelElementCollection/allowDuplicates": (
            "O",
            "ns=1;i=5127",
            {},
        ),
        "Admin-shell.io/aas/2/0/SubmodelElementCollection/values": (
            "O",
            "ns=1;i=5128",
            {},
        ),
        "Admin-shell.io/aas/2/0/View": ("O", "ns=1;i=5129", {}),
        "Admin-shell.io/aas/2/0/View/containedElements": ("O", "ns=1;i=5130", {}),
        "Admin-shell.io/aas/2/0/View/dataSpecifications": ("O", "ns=1;i=5131", {}),
        "Admin-shell.io/aas/2/0/hasDataSpecification/dataSpecification": (
            "O",
            "ns=1;i=5103",
            {},
        ),
        "Default Binary": ("O", "ns=1;i=5038", {}),
        "Default JSON": ("O", "ns=1;i=5040", {}),
        "Default XML": ("O", "ns=1;i=5039", {}),
        "TypeDictionary": (
            "V",
            "ns=1;i=6096",
            {
                "AASKeyDataType": ("V", "ns=1;i=6100", {}),
                "NamespaceUri": ("V", "ns=1;i=6097", {}),
            },
        ),
        "http://opcfoundation.org/UA/I4AAS/": (
            "O",
            "ns=1;i=5023",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=6060", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=6061", {}),
                "NamespaceUri": ("V", "ns=1;i=6062", {}),
                "NamespaceVersion": ("V", "ns=1;i=6115", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6116", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=6117", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=6118", {}),
            },
        ),
    },
    "objtypes": {
        "AASAdministrativeInformationType": (
            "OT",
            "ns=1;i=1030",
            {"Revision": ("V", "ns=1;i=6084", {}), "Version": ("V", "ns=1;i=6083", {})},
        ),
        "AASAssetAdministrationShellType": (
            "OT",
            "ns=1;i=1002",
            {
                "<ConceptDictionary>": ("O", "ns=1;i=5005", {}),
                "<DataSpecification>": (
                    "O",
                    "ns=1;i=5001",
                    {"Keys": ("V", "ns=1;i=6003", {})},
                ),
                "<Submodel>": (
                    "O",
                    "ns=1;i=5003",
                    {"ModelingKind": ("V", "ns=1;i=6011", {})},
                ),
                "<SubmodelReference>": (
                    "O",
                    "ns=1;i=5004",
                    {"Keys": ("V", "ns=1;i=6002", {})},
                ),
                "<View>": ("O", "ns=1;i=5006", {}),
                "Asset": ("O", "ns=1;i=5002", {"AssetKind": ("V", "ns=1;i=6008", {})}),
                "DerivedFrom": ("O", "ns=1;i=5007", {"Keys": ("V", "ns=1;i=6004", {})}),
            },
        ),
        "AASAssetType": (
            "OT",
            "ns=1;i=1005",
            {
                "<DataSpecification>": (
                    "O",
                    "ns=1;i=5008",
                    {"Keys": ("V", "ns=1;i=6005", {})},
                ),
                "AssetIdentificationModel": (
                    "O",
                    "ns=1;i=5049",
                    {"Keys": ("V", "ns=1;i=6112", {})},
                ),
                "AssetKind": ("V", "ns=1;i=6006", {}),
                "BillOfMaterial": (
                    "O",
                    "ns=1;i=5050",
                    {"Keys": ("V", "ns=1;i=6113", {})},
                ),
            },
        ),
        "AASConceptDictionaryType": ("OT", "ns=1;i=1007", {}),
        "AASCustomConceptDescriptionType": (
            "OT",
            "ns=1;i=1026",
            {
                "<ConceptDescription>": (
                    "O",
                    "ns=1;i=5048",
                    {"Keys": ("V", "ns=1;i=6107", {})},
                ),
                "<DataSpecification>": (
                    "O",
                    "ns=1;i=5043",
                    {"Keys": ("V", "ns=1;i=6134", {})},
                ),
            },
        ),
        "AASDataSpecificationType": (
            "OT",
            "ns=1;i=1027",
            {
                "AASDataSpecificationIEC61360Type": (
                    "OT",
                    "ns=1;i=1028",
                    {
                        "Administration": ("O", "ns=1;i=5027", {}),
                        "Category": ("V", "ns=1;i=6065", {}),
                        "DataType": ("V", "ns=1;i=6072", {}),
                        "DefaultInstanceBrowseName": ("V", "ns=1;i=6063", {}),
                        "Definition": ("V", "ns=1;i=6073", {}),
                        "Identification": (
                            "O",
                            "ns=1;i=5026",
                            {
                                "Id": ("V", "ns=1;i=6088", {}),
                                "IdType": ("V", "ns=1;i=6087", {}),
                            },
                        ),
                        "LevelType": ("V", "ns=1;i=6075", {}),
                        "PreferredName": ("V", "ns=1;i=6074", {}),
                        "ShortName": ("V", "ns=1;i=6066", {}),
                        "SourceOfDefinition": ("V", "ns=1;i=6067", {}),
                        "Symbol": ("V", "ns=1;i=6068", {}),
                        "Unit": ("V", "ns=1;i=6069", {}),
                        "UnitId": (
                            "O",
                            "ns=1;i=5028",
                            {"Keys": ("V", "ns=1;i=6076", {})},
                        ),
                        "Value": ("V", "ns=1;i=6071", {}),
                        "ValueFormat": ("V", "ns=1;i=6070", {}),
                        "ValueId": (
                            "O",
                            "ns=1;i=5030",
                            {"Keys": ("V", "ns=1;i=6077", {})},
                        ),
                        "ValueList": ("O", "ns=1;i=5029", {}),
                    },
                )
            },
        ),
        "AASIdentifierType": (
            "OT",
            "ns=1;i=1029",
            {"Id": ("V", "ns=1;i=6086", {}), "IdType": ("V", "ns=1;i=6085", {})},
        ),
        "AASIrdiConceptDescriptionType": (
            "OT",
            "ns=1;i=1024",
            {
                "<ConceptDescription>": (
                    "O",
                    "ns=1;i=5044",
                    {"Keys": ("V", "ns=1;i=6105", {})},
                ),
                "<DataSpecification>": (
                    "O",
                    "ns=1;i=5024",
                    {"Keys": ("V", "ns=1;i=6036", {})},
                ),
            },
        ),
        "AASIriConceptDescriptionType": (
            "OT",
            "ns=1;i=1025",
            {
                "<ConceptDescription>": (
                    "O",
                    "ns=1;i=5046",
                    {"Keys": ("V", "ns=1;i=6106", {})},
                ),
                "<DataSpecification>": (
                    "O",
                    "ns=1;i=5025",
                    {"Keys": ("V", "ns=1;i=6133", {})},
                ),
            },
        ),
        "AASQualifierType": (
            "OT",
            "ns=1;i=1032",
            {
                "Type": ("V", "ns=1;i=6010", {}),
                "Value": ("V", "ns=1;i=6078", {}),
                "ValueId": ("O", "ns=1;i=5033", {"Keys": ("V", "ns=1;i=6079", {})}),
                "ValueType": ("V", "ns=1;i=6015", {}),
            },
        ),
        "AASReferenceType": (
            "OT",
            "ns=1;i=1004",
            {"<Referable>": ("O", "ns=1;i=5041", {}), "Keys": ("V", "ns=1;i=6001", {})},
        ),
        "AASSubmodelElementType": (
            "OT",
            "ns=1;i=1009",
            {
                "<DataSpecification>": (
                    "O",
                    "ns=1;i=5011",
                    {"Keys": ("V", "ns=1;i=6012", {})},
                ),
                "<Qualifier>": (
                    "O",
                    "ns=1;i=5031",
                    {
                        "Type": ("V", "ns=1;i=6080", {}),
                        "ValueType": ("V", "ns=1;i=6135", {}),
                    },
                ),
                "AASBlobType": (
                    "OT",
                    "ns=1;i=1016",
                    {
                        "File": (
                            "O",
                            "ns=1;i=5015",
                            {
                                "Close": (
                                    "M",
                                    "ns=1;i=7002",
                                    {"InputArguments": ("V", "ns=1;i=6023", {})},
                                ),
                                "GetPosition": (
                                    "M",
                                    "ns=1;i=7003",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6024", {}),
                                        "OutputArguments": ("V", "ns=1;i=6025", {}),
                                    },
                                ),
                                "Open": (
                                    "M",
                                    "ns=1;i=7004",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6026", {}),
                                        "OutputArguments": ("V", "ns=1;i=6027", {}),
                                    },
                                ),
                                "OpenCount": ("V", "ns=1;i=6028", {}),
                                "Read": (
                                    "M",
                                    "ns=1;i=7005",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6029", {}),
                                        "OutputArguments": ("V", "ns=1;i=6030", {}),
                                    },
                                ),
                                "SetPosition": (
                                    "M",
                                    "ns=1;i=7006",
                                    {"InputArguments": ("V", "ns=1;i=6031", {})},
                                ),
                                "Size": ("V", "ns=1;i=6032", {}),
                                "UserWritable": ("V", "ns=1;i=6033", {}),
                                "Writable": ("V", "ns=1;i=6034", {}),
                                "Write": (
                                    "M",
                                    "ns=1;i=7007",
                                    {"InputArguments": ("V", "ns=1;i=6035", {})},
                                ),
                            },
                        )
                    },
                ),
                "AASCapabilityType": ("OT", "ns=1;i=1014", {}),
                "AASEntityType": (
                    "OT",
                    "ns=1;i=1022",
                    {
                        "<SubmodelElement>": (
                            "O",
                            "ns=1;i=5021",
                            {
                                "Category": ("V", "ns=1;i=6130", {}),
                                "IdShort": ("V", "ns=1;i=6123", {}),
                                "ModelingKind": ("V", "ns=1;i=6054", {}),
                            },
                        ),
                        "Asset": (
                            "O",
                            "ns=1;i=5022",
                            {"Keys": ("V", "ns=1;i=6055", {})},
                        ),
                        "EntityType": ("V", "ns=1;i=6056", {}),
                    },
                ),
                "AASEventType": ("OT", "ns=1;i=1021", {}),
                "AASFileType": (
                    "OT",
                    "ns=1;i=1017",
                    {
                        "File": (
                            "O",
                            "ns=1;i=5016",
                            {
                                "Close": (
                                    "M",
                                    "ns=1;i=7008",
                                    {"InputArguments": ("V", "ns=1;i=6038", {})},
                                ),
                                "GetPosition": (
                                    "M",
                                    "ns=1;i=7009",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6039", {}),
                                        "OutputArguments": ("V", "ns=1;i=6040", {}),
                                    },
                                ),
                                "Open": (
                                    "M",
                                    "ns=1;i=7010",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6041", {}),
                                        "OutputArguments": ("V", "ns=1;i=6042", {}),
                                    },
                                ),
                                "OpenCount": ("V", "ns=1;i=6043", {}),
                                "Read": (
                                    "M",
                                    "ns=1;i=7011",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6044", {}),
                                        "OutputArguments": ("V", "ns=1;i=6045", {}),
                                    },
                                ),
                                "SetPosition": (
                                    "M",
                                    "ns=1;i=7012",
                                    {"InputArguments": ("V", "ns=1;i=6046", {})},
                                ),
                                "Size": ("V", "ns=1;i=6047", {}),
                                "UserWritable": ("V", "ns=1;i=6048", {}),
                                "Writable": ("V", "ns=1;i=6049", {}),
                                "Write": (
                                    "M",
                                    "ns=1;i=7013",
                                    {"InputArguments": ("V", "ns=1;i=6050", {})},
                                ),
                            },
                        ),
                        "MimeType": ("V", "ns=1;i=6037", {}),
                        "Value": ("V", "ns=1;i=6132", {}),
                    },
                ),
                "AASMultiLanguagePropertyType": (
                    "OT",
                    "ns=1;i=1012",
                    {
                        "Value": ("V", "ns=1;i=6019", {}),
                        "ValueId": (
                            "O",
                            "ns=1;i=5013",
                            {"Keys": ("V", "ns=1;i=6018", {})},
                        ),
                    },
                ),
                "AASOperationType": (
                    "OT",
                    "ns=1;i=1015",
                    {"Operation": ("M", "ns=1;i=7001", {})},
                ),
                "AASPropertyType": (
                    "OT",
                    "ns=1;i=1013",
                    {
                        "Value": ("V", "ns=1;i=6020", {}),
                        "ValueId": (
                            "O",
                            "ns=1;i=5014",
                            {"Keys": ("V", "ns=1;i=6022", {})},
                        ),
                        "ValueType": ("V", "ns=1;i=6021", {}),
                    },
                ),
                "AASRangeType": (
                    "OT",
                    "ns=1;i=1023",
                    {
                        "Max": ("V", "ns=1;i=6059", {}),
                        "Min": ("V", "ns=1;i=6058", {}),
                        "ValueType": ("V", "ns=1;i=6057", {}),
                    },
                ),
                "AASReferenceElementType": (
                    "OT",
                    "ns=1;i=1020",
                    {"Value": ("O", "ns=1;i=5020", {"Keys": ("V", "ns=1;i=6053", {})})},
                ),
                "AASRelationshipElementType": (
                    "OT",
                    "ns=1;i=1018",
                    {
                        "AASAnnotatedRelationshipElementType": (
                            "OT",
                            "ns=1;i=1019",
                            {
                                "<DataElement>": (
                                    "O",
                                    "ns=1;i=5019",
                                    {
                                        "Category": ("V", "ns=1;i=6129", {}),
                                        "IdShort": ("V", "ns=1;i=6122", {}),
                                        "ModelingKind": ("V", "ns=1;i=6114", {}),
                                    },
                                )
                            },
                        ),
                        "First": (
                            "O",
                            "ns=1;i=5017",
                            {"Keys": ("V", "ns=1;i=6051", {})},
                        ),
                        "Second": (
                            "O",
                            "ns=1;i=5018",
                            {"Keys": ("V", "ns=1;i=6052", {})},
                        ),
                    },
                ),
                "AASSubmodelElementCollectionType": (
                    "OT",
                    "ns=1;i=1010",
                    {
                        "<SubmodelElement>": (
                            "O",
                            "ns=1;i=5012",
                            {
                                "Category": ("V", "ns=1;i=6128", {}),
                                "IdShort": ("V", "ns=1;i=6121", {}),
                                "ModelingKind": ("V", "ns=1;i=6016", {}),
                            },
                        ),
                        "AASOrderedSubmodelElementCollectionType": (
                            "OT",
                            "ns=1;i=1011",
                            {},
                        ),
                        "AllowDuplicates": ("V", "ns=1;i=6017", {}),
                    },
                ),
                "Category": ("V", "ns=1;i=6126", {}),
                "ModelingKind": ("V", "ns=1;i=6013", {}),
            },
        ),
        "AASSubmodelType": (
            "OT",
            "ns=1;i=1006",
            {
                "<DataSpecification>": (
                    "O",
                    "ns=1;i=5009",
                    {"Keys": ("V", "ns=1;i=6007", {})},
                ),
                "<Qualifier>": (
                    "O",
                    "ns=1;i=5032",
                    {
                        "Type": ("V", "ns=1;i=6081", {}),
                        "ValueType": ("V", "ns=1;i=6136", {}),
                    },
                ),
                "<SubmodelElement>": (
                    "O",
                    "ns=1;i=5010",
                    {
                        "Category": ("V", "ns=1;i=6127", {}),
                        "IdShort": ("V", "ns=1;i=6120", {}),
                        "ModelingKind": ("V", "ns=1;i=6014", {}),
                    },
                ),
                "ModelingKind": ("V", "ns=1;i=6009", {}),
            },
        ),
        "AASViewType": (
            "OT",
            "ns=1;i=1003",
            {
                "<DataSpecification>": (
                    "O",
                    "ns=1;i=5037",
                    {"Keys": ("V", "ns=1;i=6092", {})},
                ),
                "<Referable>": ("O", "ns=1;i=5036", {"Keys": ("V", "ns=1;i=6091", {})}),
            },
        ),
        "ValueListType": ("OT", "ns=1;i=1031", {}),
    },
    "reftypes": {
        "AASReference": ("RT", "ns=1;i=4003", {}),
        "HasInterface": ("RT", "ns=1;i=4002", {}),
    },
}
