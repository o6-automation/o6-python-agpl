# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 79d4e0d787cac6234acfe72d48d370b316ec811176bf912c7f1ed199a4c94d5a
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/"
_VERSION: str = "1.05.06"
_REQUIRED: list = []
_STRUCTURES: list = []
_ENUMS: list = []
_ORIGINAL_NODEIDS: tuple = ([], [])
_NODES: dict = {
    "datatypes": {
        "BaseDataType": (
            "D",
            "i=24",
            {
                "Boolean": ("D", "i=1", {}),
                "ByteString": (
                    "D",
                    "i=15",
                    {
                        "ApplicationInstanceCertificate": ("D", "i=311", {}),
                        "AudioDataType": ("D", "i=16307", {}),
                        "ContinuationPoint": ("D", "i=521", {}),
                        "Image": (
                            "D",
                            "i=30",
                            {
                                "ImageBMP": ("D", "i=2000", {}),
                                "ImageGIF": ("D", "i=2001", {}),
                                "ImageJPG": ("D", "i=2002", {}),
                                "ImagePNG": ("D", "i=2003", {}),
                            },
                        ),
                    },
                ),
                "DataValue": ("D", "i=23", {}),
                "DateTime": ("D", "i=13", {"UtcTime": ("D", "i=294", {})}),
                "DiagnosticInfo": ("D", "i=25", {}),
                "Enumeration": (
                    "D",
                    "i=29",
                    {
                        "ActionState": (
                            "D",
                            "i=18595",
                            {"EnumStrings": ("V", "i=18596", {})},
                        ),
                        "ApplicationType": (
                            "D",
                            "i=307",
                            {"EnumStrings": ("V", "i=7597", {})},
                        ),
                        "AxisScaleEnumeration": (
                            "D",
                            "i=12077",
                            {"EnumStrings": ("V", "i=12078", {})},
                        ),
                        "BrokerTransportQualityOfService": (
                            "D",
                            "i=15008",
                            {"EnumStrings": ("V", "i=15009", {})},
                        ),
                        "ChassisIdSubtype": (
                            "D",
                            "i=18947",
                            {"EnumValues": ("V", "i=18948", {})},
                        ),
                        "ConfigurationUpdateType": (
                            "D",
                            "i=15539",
                            {"EnumValues": ("V", "i=15540", {})},
                        ),
                        "ConversionLimitEnum": (
                            "D",
                            "i=32436",
                            {"EnumStrings": ("V", "i=32437", {})},
                        ),
                        "DataSetOrderingType": (
                            "D",
                            "i=20408",
                            {"EnumStrings": ("V", "i=15641", {})},
                        ),
                        "DiagnosticsLevel": (
                            "D",
                            "i=19723",
                            {"EnumStrings": ("V", "i=19724", {})},
                        ),
                        "Duplex": (
                            "D",
                            "i=24210",
                            {"EnumValues": ("V", "i=24235", {})},
                        ),
                        "ExceptionDeviationFormat": (
                            "D",
                            "i=890",
                            {"EnumStrings": ("V", "i=7614", {})},
                        ),
                        "FilterOperator": (
                            "D",
                            "i=576",
                            {"EnumStrings": ("V", "i=7605", {})},
                        ),
                        "HistoryUpdateType": (
                            "D",
                            "i=11234",
                            {"EnumValues": ("V", "i=11884", {})},
                        ),
                        "IdType": ("D", "i=256", {"EnumStrings": ("V", "i=7591", {})}),
                        "IdentityCriteriaType": (
                            "D",
                            "i=15632",
                            {"EnumValues": ("V", "i=15633", {})},
                        ),
                        "InterfaceAdminStatus": (
                            "D",
                            "i=24212",
                            {"EnumValues": ("V", "i=24236", {})},
                        ),
                        "InterfaceOperStatus": (
                            "D",
                            "i=24214",
                            {"EnumValues": ("V", "i=24237", {})},
                        ),
                        "ManAddrIfSubtype": (
                            "D",
                            "i=18951",
                            {"EnumValues": ("V", "i=18952", {})},
                        ),
                        "MessageSecurityMode": (
                            "D",
                            "i=302",
                            {"EnumStrings": ("V", "i=7595", {})},
                        ),
                        "NamingRuleType": (
                            "D",
                            "i=120",
                            {"EnumValues": ("V", "i=12169", {})},
                        ),
                        "NegotiationStatus": (
                            "D",
                            "i=24216",
                            {"EnumValues": ("V", "i=24238", {})},
                        ),
                        "NodeAttributesMask": (
                            "D",
                            "i=348",
                            {"EnumValues": ("V", "i=11881", {})},
                        ),
                        "NodeClass": (
                            "D",
                            "i=257",
                            {"EnumValues": ("V", "i=11878", {})},
                        ),
                        "OpenFileMode": (
                            "D",
                            "i=11939",
                            {"EnumValues": ("V", "i=11940", {})},
                        ),
                        "OverrideValueHandling": (
                            "D",
                            "i=15874",
                            {"EnumStrings": ("V", "i=15875", {})},
                        ),
                        "PerformUpdateType": (
                            "D",
                            "i=11293",
                            {"EnumValues": ("V", "i=11885", {})},
                        ),
                        "PortIdSubtype": (
                            "D",
                            "i=18949",
                            {"EnumValues": ("V", "i=18950", {})},
                        ),
                        "PubSubDiagnosticsCounterClassification": (
                            "D",
                            "i=19730",
                            {"EnumStrings": ("V", "i=19731", {})},
                        ),
                        "PubSubState": (
                            "D",
                            "i=14647",
                            {"EnumStrings": ("V", "i=14648", {})},
                        ),
                        "RedundancySupport": (
                            "D",
                            "i=851",
                            {"EnumStrings": ("V", "i=7611", {})},
                        ),
                        "RedundantServerMode": (
                            "D",
                            "i=32417",
                            {"EnumStrings": ("V", "i=32418", {})},
                        ),
                        "SecurityTokenRequestType": (
                            "D",
                            "i=315",
                            {"EnumStrings": ("V", "i=7598", {})},
                        ),
                        "ServerState": (
                            "D",
                            "i=852",
                            {"EnumStrings": ("V", "i=7612", {})},
                        ),
                        "StructureType": (
                            "D",
                            "i=98",
                            {"EnumStrings": ("V", "i=14528", {})},
                        ),
                        "TrustListMasks": (
                            "D",
                            "i=12552",
                            {"EnumValues": ("V", "i=12553", {})},
                        ),
                        "TsnFailureCode": (
                            "D",
                            "i=24218",
                            {"EnumValues": ("V", "i=24239", {})},
                        ),
                        "TsnListenerStatus": (
                            "D",
                            "i=24224",
                            {"EnumValues": ("V", "i=24242", {})},
                        ),
                        "TsnStreamState": (
                            "D",
                            "i=24220",
                            {"EnumValues": ("V", "i=24240", {})},
                        ),
                        "TsnTalkerStatus": (
                            "D",
                            "i=24222",
                            {"EnumValues": ("V", "i=24241", {})},
                        ),
                        "UserTokenType": (
                            "D",
                            "i=303",
                            {"EnumStrings": ("V", "i=7596", {})},
                        ),
                    },
                ),
                "ExpandedNodeId": ("D", "i=18", {}),
                "Guid": ("D", "i=14", {}),
                "LocalizedText": ("D", "i=21", {}),
                "NodeId": (
                    "D",
                    "i=17",
                    {"SessionAuthenticationToken": ("D", "i=388", {})},
                ),
                "Number": (
                    "D",
                    "i=26",
                    {
                        "Decimal": ("D", "i=50", {}),
                        "Double": ("D", "i=11", {"Duration": ("D", "i=290", {})}),
                        "Float": ("D", "i=10", {}),
                        "Integer": (
                            "D",
                            "i=27",
                            {
                                "Int16": ("D", "i=4", {}),
                                "Int32": ("D", "i=6", {}),
                                "Int64": ("D", "i=8", {}),
                                "SByte": ("D", "i=2", {}),
                            },
                        ),
                        "UInteger": (
                            "D",
                            "i=28",
                            {
                                "Byte": (
                                    "D",
                                    "i=3",
                                    {
                                        "AccessLevelType": (
                                            "D",
                                            "i=15031",
                                            {"OptionSetValues": ("V", "i=15032", {})},
                                        ),
                                        "EventNotifierType": (
                                            "D",
                                            "i=15033",
                                            {"OptionSetValues": ("V", "i=15034", {})},
                                        ),
                                    },
                                ),
                                "UInt16": (
                                    "D",
                                    "i=5",
                                    {
                                        "AccessRestrictionType": (
                                            "D",
                                            "i=95",
                                            {"OptionSetValues": ("V", "i=15035", {})},
                                        ),
                                        "AlarmMask": (
                                            "D",
                                            "i=32251",
                                            {"OptionSetValues": ("V", "i=32252", {})},
                                        ),
                                        "DataSetFieldFlags": (
                                            "D",
                                            "i=15904",
                                            {"OptionSetValues": ("V", "i=15577", {})},
                                        ),
                                    },
                                ),
                                "UInt32": (
                                    "D",
                                    "i=7",
                                    {
                                        "AccessLevelExType": (
                                            "D",
                                            "i=15406",
                                            {"OptionSetValues": ("V", "i=15407", {})},
                                        ),
                                        "AttributeWriteMask": (
                                            "D",
                                            "i=347",
                                            {"OptionSetValues": ("V", "i=15036", {})},
                                        ),
                                        "Counter": ("D", "i=289", {}),
                                        "DataSetFieldContentMask": (
                                            "D",
                                            "i=15583",
                                            {"OptionSetValues": ("V", "i=15584", {})},
                                        ),
                                        "Handle": ("D", "i=31917", {}),
                                        "Index": ("D", "i=17588", {}),
                                        "IntegerId": ("D", "i=288", {}),
                                        "JsonDataSetMessageContentMask": (
                                            "D",
                                            "i=15658",
                                            {"OptionSetValues": ("V", "i=15659", {})},
                                        ),
                                        "JsonNetworkMessageContentMask": (
                                            "D",
                                            "i=15654",
                                            {"OptionSetValues": ("V", "i=15655", {})},
                                        ),
                                        "LldpSystemCapabilitiesMap": (
                                            "D",
                                            "i=18956",
                                            {"OptionSetValues": ("V", "i=18957", {})},
                                        ),
                                        "LogRecordMask": (
                                            "D",
                                            "i=19749",
                                            {"OptionSetValues": ("V", "i=19750", {})},
                                        ),
                                        "PasswordOptionsMask": (
                                            "D",
                                            "i=24277",
                                            {"OptionSetValues": ("V", "i=24278", {})},
                                        ),
                                        "PermissionType": (
                                            "D",
                                            "i=94",
                                            {"OptionSetValues": ("V", "i=15030", {})},
                                        ),
                                        "PubSubConfigurationRefMask": (
                                            "D",
                                            "i=25517",
                                            {"OptionSetValues": ("V", "i=25518", {})},
                                        ),
                                        "TrustListValidationOptions": (
                                            "D",
                                            "i=23564",
                                            {"OptionSetValues": ("V", "i=23565", {})},
                                        ),
                                        "UadpDataSetMessageContentMask": (
                                            "D",
                                            "i=15646",
                                            {"OptionSetValues": ("V", "i=15647", {})},
                                        ),
                                        "UadpNetworkMessageContentMask": (
                                            "D",
                                            "i=15642",
                                            {"OptionSetValues": ("V", "i=15643", {})},
                                        ),
                                        "UserConfigurationMask": (
                                            "D",
                                            "i=24279",
                                            {"OptionSetValues": ("V", "i=24280", {})},
                                        ),
                                        "VersionTime": ("D", "i=20998", {}),
                                    },
                                ),
                                "UInt64": (
                                    "D",
                                    "i=9",
                                    {"BitFieldMaskDataType": ("D", "i=11737", {})},
                                ),
                            },
                        ),
                    },
                ),
                "QualifiedName": ("D", "i=20", {}),
                "StatusCode": ("D", "i=19", {}),
                "String": (
                    "D",
                    "i=12",
                    {
                        "DateString": ("D", "i=12881", {}),
                        "DecimalString": ("D", "i=12878", {}),
                        "DurationString": ("D", "i=12879", {}),
                        "EncodedTicket": ("D", "i=25726", {}),
                        "LocaleId": ("D", "i=295", {}),
                        "NormalizedString": ("D", "i=12877", {}),
                        "NumericRange": ("D", "i=291", {}),
                        "SemanticVersionString": ("D", "i=24263", {}),
                        "TimeString": ("D", "i=12880", {}),
                        "TrimmedString": ("D", "i=31918", {}),
                        "UriString": ("D", "i=23751", {}),
                    },
                ),
                "Structure": (
                    "D",
                    "i=22",
                    {
                        "ActionMethodDataType": ("D", "i=18597", {}),
                        "ActionTargetDataType": ("D", "i=18593", {}),
                        "AddNodesItem": ("D", "i=376", {}),
                        "AddReferencesItem": ("D", "i=379", {}),
                        "AdditionalParametersType": ("D", "i=16313", {}),
                        "AggregateConfiguration": ("D", "i=948", {}),
                        "AliasNameDataType": ("D", "i=23468", {}),
                        "Annotation": ("D", "i=891", {}),
                        "AnnotationDataType": ("D", "i=32434", {}),
                        "ApplicationDescription": ("D", "i=308", {}),
                        "Argument": ("D", "i=296", {}),
                        "AxisInformation": ("D", "i=12079", {}),
                        "BaseConfigurationDataType": (
                            "D",
                            "i=15434",
                            {"ApplicationConfigurationDataType": ("D", "i=23743", {})},
                        ),
                        "BaseConfigurationRecordDataType": (
                            "D",
                            "i=15435",
                            {
                                "ApplicationIdentityDataType": ("D", "i=15556", {}),
                                "AuthorizationServiceConfigurationDataType": (
                                    "D",
                                    "i=23744",
                                    {},
                                ),
                                "CertificateGroupDataType": ("D", "i=15436", {}),
                                "EndpointDataType": (
                                    "D",
                                    "i=15557",
                                    {"ServerEndpointDataType": ("D", "i=15558", {})},
                                ),
                                "SecuritySettingsDataType": ("D", "i=15559", {}),
                                "UserTokenSettingsDataType": ("D", "i=15560", {}),
                            },
                        ),
                        "BitFieldDefinition": ("D", "i=32421", {}),
                        "BuildInfo": ("D", "i=338", {}),
                        "CartesianCoordinates": (
                            "D",
                            "i=18809",
                            {"3DCartesianCoordinates": ("D", "i=18810", {})},
                        ),
                        "ComplexNumberType": ("D", "i=12171", {}),
                        "ConfigurationUpdateTargetType": ("D", "i=15538", {}),
                        "ConfigurationVersionDataType": ("D", "i=14593", {}),
                        "ConnectionTransportDataType": (
                            "D",
                            "i=15618",
                            {
                                "BrokerConnectionTransportDataType": (
                                    "D",
                                    "i=15007",
                                    {},
                                ),
                                "DatagramConnectionTransportDataType": (
                                    "D",
                                    "i=17467",
                                    {
                                        "DatagramConnectionTransport2DataType": (
                                            "D",
                                            "i=23612",
                                            {},
                                        )
                                    },
                                ),
                            },
                        ),
                        "ContentFilter": ("D", "i=586", {}),
                        "ContentFilterElement": ("D", "i=583", {}),
                        "CurrencyUnitType": ("D", "i=23498", {}),
                        "DataSetReaderDataType": ("D", "i=15623", {}),
                        "DataSetReaderMessageDataType": (
                            "D",
                            "i=15629",
                            {
                                "JsonDataSetReaderMessageDataType": (
                                    "D",
                                    "i=15665",
                                    {},
                                ),
                                "UadpDataSetReaderMessageDataType": (
                                    "D",
                                    "i=15653",
                                    {},
                                ),
                            },
                        ),
                        "DataSetReaderTransportDataType": (
                            "D",
                            "i=15628",
                            {
                                "BrokerDataSetReaderTransportDataType": (
                                    "D",
                                    "i=15670",
                                    {},
                                ),
                                "DatagramDataSetReaderTransportDataType": (
                                    "D",
                                    "i=23614",
                                    {},
                                ),
                            },
                        ),
                        "DataSetWriterDataType": ("D", "i=15597", {}),
                        "DataSetWriterMessageDataType": (
                            "D",
                            "i=15605",
                            {
                                "JsonDataSetWriterMessageDataType": (
                                    "D",
                                    "i=15664",
                                    {},
                                ),
                                "UadpDataSetWriterMessageDataType": (
                                    "D",
                                    "i=15652",
                                    {},
                                ),
                            },
                        ),
                        "DataSetWriterTransportDataType": (
                            "D",
                            "i=15598",
                            {
                                "BrokerDataSetWriterTransportDataType": (
                                    "D",
                                    "i=15669",
                                    {},
                                )
                            },
                        ),
                        "DataTypeDefinition": (
                            "D",
                            "i=97",
                            {
                                "EnumDefinition": ("D", "i=100", {}),
                                "StructureDefinition": ("D", "i=99", {}),
                            },
                        ),
                        "DataTypeDescription": (
                            "D",
                            "i=14525",
                            {
                                "EnumDescription": ("D", "i=15488", {}),
                                "SimpleTypeDescription": ("D", "i=15005", {}),
                                "StructureDescription": ("D", "i=15487", {}),
                            },
                        ),
                        "DataTypeSchemaHeader": (
                            "D",
                            "i=15534",
                            {
                                "DataSetMetaDataType": ("D", "i=14523", {}),
                                "UABinaryFileDataType": ("D", "i=15006", {}),
                            },
                        ),
                        "DeleteNodesItem": ("D", "i=382", {}),
                        "DeleteReferencesItem": ("D", "i=385", {}),
                        "DiscoveryConfiguration": (
                            "D",
                            "i=12890",
                            {"MdnsDiscoveryConfiguration": ("D", "i=12891", {})},
                        ),
                        "DoubleComplexNumberType": ("D", "i=12172", {}),
                        "DtlsPubSubConnectionDataType": ("D", "i=18794", {}),
                        "EUInformation": ("D", "i=887", {}),
                        "EndpointConfiguration": ("D", "i=331", {}),
                        "EndpointDescription": ("D", "i=312", {}),
                        "EndpointType": ("D", "i=15528", {}),
                        "EndpointUrlListDataType": ("D", "i=11943", {}),
                        "EnumValueType": (
                            "D",
                            "i=7594",
                            {"EnumField": ("D", "i=102", {})},
                        ),
                        "EphemeralKeyType": ("D", "i=17548", {}),
                        "FieldMetaData": ("D", "i=14524", {}),
                        "FieldTargetDataType": ("D", "i=14744", {}),
                        "FilterOperand": (
                            "D",
                            "i=589",
                            {
                                "AttributeOperand": ("D", "i=598", {}),
                                "ElementOperand": ("D", "i=592", {}),
                                "LiteralOperand": ("D", "i=595", {}),
                                "SimpleAttributeOperand": ("D", "i=601", {}),
                            },
                        ),
                        "Frame": ("D", "i=18813", {"3DFrame": ("D", "i=18814", {})}),
                        "HistoryEvent": (
                            "D",
                            "i=659",
                            {"HistoryModifiedEvent": ("D", "i=32824", {})},
                        ),
                        "HistoryEventFieldList": ("D", "i=920", {}),
                        "IdentityMappingRuleType": ("D", "i=15634", {}),
                        "KeyValuePair": ("D", "i=14533", {}),
                        "LinearConversionDataType": ("D", "i=32435", {}),
                        "LldpManagementAddressTxPortType": ("D", "i=18953", {}),
                        "LldpManagementAddressType": ("D", "i=18954", {}),
                        "LldpTlvType": ("D", "i=18955", {}),
                        "LogRecord": ("D", "i=19361", {}),
                        "LogRecordsDataType": ("D", "i=19745", {}),
                        "ModelChangeStructureDataType": ("D", "i=877", {}),
                        "ModificationInfo": ("D", "i=11216", {}),
                        "MonitoringFilter": (
                            "D",
                            "i=719",
                            {"EventFilter": ("D", "i=725", {})},
                        ),
                        "NameValuePair": ("D", "i=19748", {}),
                        "NetworkAddressDataType": (
                            "D",
                            "i=15502",
                            {"NetworkAddressUrlDataType": ("D", "i=15510", {})},
                        ),
                        "NetworkGroupDataType": ("D", "i=11944", {}),
                        "OptionSet": ("D", "i=12755", {}),
                        "Orientation": (
                            "D",
                            "i=18811",
                            {"3DOrientation": ("D", "i=18812", {})},
                        ),
                        "PortableNodeId": ("D", "i=24106", {}),
                        "PortableQualifiedName": ("D", "i=24105", {}),
                        "PriorityMappingEntryType": ("D", "i=25220", {}),
                        "ProgramDiagnostic2DataType": ("D", "i=24033", {}),
                        "ProgramDiagnosticDataType": ("D", "i=894", {}),
                        "PubSubConfigurationDataType": (
                            "D",
                            "i=15530",
                            {"PubSubConfiguration2DataType": ("D", "i=23602", {})},
                        ),
                        "PubSubConfigurationRefDataType": ("D", "i=25519", {}),
                        "PubSubConfigurationValueDataType": ("D", "i=25520", {}),
                        "PubSubConnectionDataType": ("D", "i=15617", {}),
                        "PubSubGroupDataType": (
                            "D",
                            "i=15609",
                            {
                                "ReaderGroupDataType": ("D", "i=15520", {}),
                                "WriterGroupDataType": ("D", "i=15480", {}),
                            },
                        ),
                        "PubSubKeyPushTargetDataType": ("D", "i=25270", {}),
                        "PublishedDataSetDataType": ("D", "i=15578", {}),
                        "PublishedDataSetSourceDataType": (
                            "D",
                            "i=15580",
                            {
                                "PublishedActionDataType": (
                                    "D",
                                    "i=18594",
                                    {
                                        "PublishedActionMethodDataType": (
                                            "D",
                                            "i=18793",
                                            {},
                                        )
                                    },
                                ),
                                "PublishedDataItemsDataType": ("D", "i=15581", {}),
                                "PublishedDataSetCustomSourceDataType": (
                                    "D",
                                    "i=25269",
                                    {},
                                ),
                                "PublishedEventsDataType": ("D", "i=15582", {}),
                            },
                        ),
                        "PublishedVariableDataType": ("D", "i=14273", {}),
                        "QosDataType": (
                            "D",
                            "i=23603",
                            {
                                "ReceiveQosDataType": (
                                    "D",
                                    "i=23608",
                                    {
                                        "ReceiveQosPriorityDataType": (
                                            "D",
                                            "i=23609",
                                            {},
                                        )
                                    },
                                ),
                                "TransmitQosDataType": (
                                    "D",
                                    "i=23604",
                                    {
                                        "TransmitQosPriorityDataType": (
                                            "D",
                                            "i=23605",
                                            {},
                                        )
                                    },
                                ),
                            },
                        ),
                        "QuantityDimension": ("D", "i=32438", {}),
                        "Range": ("D", "i=884", {}),
                        "RationalNumber": ("D", "i=18806", {}),
                        "ReaderGroupMessageDataType": ("D", "i=15622", {}),
                        "ReaderGroupTransportDataType": ("D", "i=15621", {}),
                        "RedundantServerDataType": ("D", "i=853", {}),
                        "ReferenceDescriptionDataType": ("D", "i=32659", {}),
                        "ReferenceListEntryDataType": ("D", "i=32660", {}),
                        "RegisteredServer": ("D", "i=432", {}),
                        "RelativePath": ("D", "i=540", {}),
                        "RelativePathElement": ("D", "i=537", {}),
                        "RolePermissionType": ("D", "i=96", {}),
                        "SamplingIntervalDiagnosticsDataType": ("D", "i=856", {}),
                        "SecurityGroupDataType": ("D", "i=23601", {}),
                        "SemanticChangeStructureDataType": ("D", "i=897", {}),
                        "ServerDiagnosticsSummaryDataType": ("D", "i=859", {}),
                        "ServerOnNetwork": ("D", "i=12189", {}),
                        "ServerStatusDataType": ("D", "i=862", {}),
                        "ServiceCertificateDataType": ("D", "i=23724", {}),
                        "ServiceCounterDataType": ("D", "i=871", {}),
                        "SessionDiagnosticsDataType": ("D", "i=865", {}),
                        "SessionSecurityDiagnosticsDataType": ("D", "i=868", {}),
                        "SignedSoftwareCertificate": ("D", "i=344", {}),
                        "SpanContextDataType": (
                            "D",
                            "i=19746",
                            {"TraceContextDataType": ("D", "i=19747", {})},
                        ),
                        "StatusResult": ("D", "i=299", {}),
                        "StructureField": ("D", "i=101", {}),
                        "SubscribedDataSetDataType": (
                            "D",
                            "i=15630",
                            {
                                "StandaloneSubscribedDataSetDataType": (
                                    "D",
                                    "i=23600",
                                    {},
                                ),
                                "StandaloneSubscribedDataSetRefDataType": (
                                    "D",
                                    "i=23599",
                                    {},
                                ),
                                "SubscribedDataSetMirrorDataType": ("D", "i=15635", {}),
                                "TargetVariablesDataType": ("D", "i=15631", {}),
                            },
                        ),
                        "SubscriptionDiagnosticsDataType": ("D", "i=874", {}),
                        "TimeZoneDataType": ("D", "i=8912", {}),
                        "TransactionErrorType": ("D", "i=32285", {}),
                        "TrustListDataType": ("D", "i=12554", {}),
                        "Union": ("D", "i=12756", {}),
                        "UnsignedRationalNumber": ("D", "i=24107", {}),
                        "UserIdentityToken": (
                            "D",
                            "i=316",
                            {
                                "AnonymousIdentityToken": ("D", "i=319", {}),
                                "IssuedIdentityToken": ("D", "i=938", {}),
                                "UserNameIdentityToken": ("D", "i=322", {}),
                                "X509IdentityToken": ("D", "i=325", {}),
                            },
                        ),
                        "UserManagementDataType": ("D", "i=24281", {}),
                        "UserTokenPolicy": ("D", "i=304", {}),
                        "Vector": ("D", "i=18807", {"3DVector": ("D", "i=18808", {})}),
                        "WriterGroupMessageDataType": (
                            "D",
                            "i=15616",
                            {
                                "JsonWriterGroupMessageDataType": ("D", "i=15657", {}),
                                "UadpWriterGroupMessageDataType": ("D", "i=15645", {}),
                            },
                        ),
                        "WriterGroupTransportDataType": (
                            "D",
                            "i=15611",
                            {
                                "BrokerWriterGroupTransportDataType": (
                                    "D",
                                    "i=15667",
                                    {},
                                ),
                                "DatagramWriterGroupTransportDataType": (
                                    "D",
                                    "i=15532",
                                    {
                                        "DatagramWriterGroupTransport2DataType": (
                                            "D",
                                            "i=23613",
                                            {},
                                        )
                                    },
                                ),
                            },
                        ),
                        "XVType": ("D", "i=12080", {}),
                    },
                ),
                "XmlElement": ("D", "i=16", {}),
            },
        )
    },
    "objects": {
        "<AlarmCondition>": (
            "O",
            "i=19847",
            {
                "AckedState": ("V", "i=20038", {"Id": ("V", "i=20039", {})}),
                "Acknowledge": (
                    "M",
                    "i=23493",
                    {"InputArguments": ("V", "i=23561", {})},
                ),
                "ActiveState": (
                    "V",
                    "i=23579",
                    {
                        "FalseState": ("V", "i=23587", {}),
                        "Id": ("V", "i=23580", {}),
                        "TrueState": ("V", "i=23586", {}),
                    },
                ),
                "AddComment": (
                    "M",
                    "i=20036",
                    {"InputArguments": ("V", "i=20037", {})},
                ),
                "BranchId": ("V", "i=19970", {}),
                "ClientUserId": ("V", "i=20033", {}),
                "Comment": ("V", "i=20031", {"SourceTimestamp": ("V", "i=20032", {})}),
                "ConditionClassId": ("V", "i=19913", {}),
                "ConditionClassName": ("V", "i=19914", {}),
                "ConditionName": ("V", "i=19969", {}),
                "Disable": ("M", "i=20034", {}),
                "Enable": ("M", "i=20035", {}),
                "EnabledState": ("V", "i=19972", {"Id": ("V", "i=19973", {})}),
                "EventId": ("V", "i=19904", {}),
                "EventType": ("V", "i=19905", {}),
                "InputNode": ("V", "i=23588", {}),
                "LastSeverity": (
                    "V",
                    "i=20029",
                    {"SourceTimestamp": ("V", "i=20030", {})},
                ),
                "Message": ("V", "i=19911", {}),
                "Quality": ("V", "i=19981", {"SourceTimestamp": ("V", "i=20028", {})}),
                "ReceiveTime": ("V", "i=19909", {}),
                "Retain": ("V", "i=19971", {}),
                "Severity": ("V", "i=19912", {}),
                "SourceName": ("V", "i=19907", {}),
                "SourceNode": ("V", "i=19906", {}),
                "SuppressedOrShelved": ("V", "i=23662", {}),
                "Time": ("V", "i=19908", {}),
            },
        ),
        "<AlarmConditionInstance>": (
            "O",
            "i=16406",
            {
                "AckedState": ("V", "i=16443", {"Id": ("V", "i=16444", {})}),
                "Acknowledge": (
                    "M",
                    "i=16461",
                    {"InputArguments": ("V", "i=16462", {})},
                ),
                "ActiveState": (
                    "V",
                    "i=16465",
                    {
                        "FalseState": ("V", "i=16473", {}),
                        "Id": ("V", "i=16466", {}),
                        "TrueState": ("V", "i=16472", {}),
                    },
                ),
                "AddComment": (
                    "M",
                    "i=16441",
                    {"InputArguments": ("V", "i=16442", {})},
                ),
                "BranchId": ("V", "i=16421", {}),
                "ClientUserId": ("V", "i=16438", {}),
                "Comment": ("V", "i=16436", {"SourceTimestamp": ("V", "i=16437", {})}),
                "ConditionClassId": ("V", "i=16416", {}),
                "ConditionClassName": ("V", "i=16417", {}),
                "ConditionName": ("V", "i=16420", {}),
                "Disable": ("M", "i=16439", {}),
                "Enable": ("M", "i=16440", {}),
                "EnabledState": ("V", "i=16423", {"Id": ("V", "i=16424", {})}),
                "EventId": ("V", "i=16407", {}),
                "EventType": ("V", "i=16408", {}),
                "InputNode": ("V", "i=16474", {}),
                "LastSeverity": (
                    "V",
                    "i=16434",
                    {"SourceTimestamp": ("V", "i=16435", {})},
                ),
                "Message": ("V", "i=16414", {}),
                "Quality": ("V", "i=16432", {"SourceTimestamp": ("V", "i=16433", {})}),
                "ReceiveTime": ("V", "i=16412", {}),
                "Retain": ("V", "i=16422", {}),
                "Severity": ("V", "i=16415", {}),
                "SourceName": ("V", "i=16410", {}),
                "SourceNode": ("V", "i=16409", {}),
                "SuppressedOrShelved": ("V", "i=16519", {}),
                "Time": ("V", "i=16411", {}),
            },
        ),
        "<AlarmGroup>": ("O", "i=16399", {}),
        "<ConnectionName>": (
            "O",
            "i=14417",
            {
                "Address": (
                    "O",
                    "i=14423",
                    {
                        "NetworkInterface": (
                            "V",
                            "i=15533",
                            {"Selections": ("V", "i=17503", {})},
                        )
                    },
                ),
                "ConnectionProperties": ("V", "i=17478", {}),
                "PublisherId": ("V", "i=14418", {}),
                "Status": ("O", "i=14419", {"State": ("V", "i=14420", {})}),
                "TransportProfileUri": (
                    "V",
                    "i=17292",
                    {"Selections": ("V", "i=17706", {})},
                ),
            },
        ),
        "<DataSetReaderName>": (
            "O",
            "i=18076",
            {
                "DataSetFieldContentMask": ("V", "i=18081", {}),
                "DataSetMetaData": ("V", "i=18080", {}),
                "DataSetReaderProperties": ("V", "i=17492", {}),
                "DataSetWriterId": ("V", "i=18079", {}),
                "HeaderLayoutUri": ("V", "i=17562", {}),
                "KeyFrameCount": ("V", "i=17560", {}),
                "MessageReceiveTimeout": ("V", "i=18082", {}),
                "PublisherId": ("V", "i=18077", {}),
                "Status": ("O", "i=18088", {"State": ("V", "i=18089", {})}),
                "SubscribedDataSet": ("O", "i=21006", {}),
                "WriterGroupId": ("V", "i=18078", {}),
            },
        ),
        "<DataSetWriterName>": (
            "O",
            "i=17743",
            {
                "DataSetFieldContentMask": ("V", "i=17745", {}),
                "DataSetWriterId": ("V", "i=17744", {}),
                "DataSetWriterProperties": ("V", "i=17490", {}),
                "Status": ("O", "i=17749", {"State": ("V", "i=17750", {})}),
            },
        ),
        "<DigitalVariable>": ("V", "i=32226", {}),
        "<FieldDescription>": ("V", "i=19823", {}),
        "<InterfaceName>": ("O", "i=25226", {}),
        "<OrderedObject>": ("O", "i=23519", {"NumberInList": ("V", "i=23521", {})}),
        "<ReaderGroupName>": (
            "O",
            "i=17325",
            {
                "GroupProperties": ("V", "i=17487", {}),
                "MaxNetworkMessageSize": ("V", "i=17302", {}),
                "SecurityMode": ("V", "i=17326", {}),
                "Status": ("O", "i=17329", {"State": ("V", "i=17330", {})}),
            },
        ),
        "<SecurityGroupName>": (
            "O",
            "i=25626",
            {
                "KeyLifetime": ("V", "i=25628", {}),
                "MaxFutureKeyCount": ("V", "i=25630", {}),
                "MaxPastKeyCount": ("V", "i=25631", {}),
                "SecurityGroupId": ("V", "i=25627", {}),
                "SecurityPolicyUri": ("V", "i=25629", {}),
            },
        ),
        "<WriterGroupName>": (
            "O",
            "i=17310",
            {
                "GroupProperties": ("V", "i=17486", {}),
                "HeaderLayoutUri": ("V", "i=17558", {}),
                "KeepAliveTime": ("V", "i=17319", {}),
                "LocaleIds": ("V", "i=17322", {}),
                "MaxNetworkMessageSize": ("V", "i=17204", {}),
                "Priority": ("V", "i=17321", {}),
                "PublishingInterval": ("V", "i=17318", {}),
                "SecurityMode": ("V", "i=17311", {}),
                "Status": ("O", "i=17314", {"State": ("V", "i=17315", {})}),
                "WriterGroupId": ("V", "i=17214", {}),
            },
        ),
        "AllowNulls": ("V", "i=3070", {}),
        "AnnotationCount": ("O", "i=2351", {}),
        "Annotations": ("V", "i=11214", {}),
        "Average": ("O", "i=2342", {}),
        "Count": ("O", "i=2352", {}),
        "CurrencyUnit": ("V", "i=23501", {}),
        "CurrentServerId": ("V", "i=11312", {}),
        "Default Binary": ("O", "i=893", {}),
        "Default JSON": ("O", "i=15382", {}),
        "Default XML": ("O", "i=892", {}),
        "DefaultInstanceBrowseName": ("V", "i=17605", {}),
        "Delta": ("O", "i=2359", {}),
        "DeltaBounds": ("O", "i=11507", {}),
        "DurationBad": ("O", "i=2361", {}),
        "DurationGood": ("O", "i=2360", {}),
        "DurationInStateNonZero": ("O", "i=11308", {}),
        "DurationInStateZero": ("O", "i=11307", {}),
        "End": ("O", "i=2358", {}),
        "EndBound": ("O", "i=11506", {}),
        "EngineeringUnits": ("V", "i=11513", {}),
        "EnumStrings": ("V", "i=11432", {}),
        "EnumValues": ("V", "i=3071", {}),
        "ExposesItsArray": ("O", "i=83", {}),
        "FileSystem": (
            "O",
            "i=16314",
            {
                "CreateDirectory": (
                    "M",
                    "i=16348",
                    {
                        "InputArguments": ("V", "i=16349", {}),
                        "OutputArguments": ("V", "i=16350", {}),
                    },
                ),
                "CreateFile": (
                    "M",
                    "i=16351",
                    {
                        "InputArguments": ("V", "i=16352", {}),
                        "OutputArguments": ("V", "i=16353", {}),
                    },
                ),
                "Delete": ("M", "i=16354", {"InputArguments": ("V", "i=16355", {})}),
                "MoveOrCopy": (
                    "M",
                    "i=16356",
                    {
                        "InputArguments": ("V", "i=16357", {}),
                        "OutputArguments": ("V", "i=16358", {}),
                    },
                ),
            },
        ),
        "HA Configuration": (
            "O",
            "i=11202",
            {
                "AggregateConfiguration": (
                    "O",
                    "i=11203",
                    {
                        "PercentDataBad": ("V", "i=11205", {}),
                        "PercentDataGood": ("V", "i=11206", {}),
                        "TreatUncertainAsBad": ("V", "i=11204", {}),
                        "UseSlopedExtrapolation": ("V", "i=11207", {}),
                    },
                ),
                "Stepped": ("V", "i=11208", {}),
            },
        ),
        "HistoricalEventFilter": ("V", "i=11215", {}),
        "Icon": ("V", "i=3067", {}),
        "InputArguments": ("V", "i=3072", {}),
        "Interpolative": ("O", "i=2341", {}),
        "LocalTime": ("V", "i=3069", {}),
        "Mandatory": ("O", "i=78", {}),
        "MandatoryPlaceholder": ("O", "i=11510", {}),
        "MaxArrayLength": ("V", "i=11512", {}),
        "MaxByteStringLength": ("V", "i=12908", {}),
        "MaxCharacters": ("V", "i=15002", {}),
        "MaxStringLength": ("V", "i=11498", {}),
        "Maximum": ("O", "i=2347", {}),
        "Maximum2": ("O", "i=11287", {}),
        "MaximumActualTime": ("O", "i=2349", {}),
        "MaximumActualTime2": ("O", "i=11306", {}),
        "Minimum": ("O", "i=2346", {}),
        "Minimum2": ("O", "i=11286", {}),
        "MinimumActualTime": ("O", "i=2348", {}),
        "MinimumActualTime2": ("O", "i=11305", {}),
        "NodeVersion": ("V", "i=3068", {}),
        "NumberOfTransitions": ("O", "i=2355", {}),
        "OptionSetLength": ("V", "i=32750", {}),
        "OptionSetValues": ("V", "i=12745", {}),
        "Optional": ("O", "i=80", {}),
        "OptionalPlaceholder": ("O", "i=11508", {}),
        "OutputArguments": ("V", "i=3073", {}),
        "PercentBad": ("O", "i=2363", {}),
        "PercentGood": ("O", "i=2362", {}),
        "Range": ("O", "i=2350", {}),
        "Range2": ("O", "i=11288", {}),
        "Root": (
            "O",
            "i=84",
            {
                "Objects": (
                    "O",
                    "i=85",
                    {
                        "Aliases": (
                            "O",
                            "i=23470",
                            {
                                "FindAlias": (
                                    "M",
                                    "i=23476",
                                    {
                                        "InputArguments": ("V", "i=23477", {}),
                                        "OutputArguments": ("V", "i=23478", {}),
                                    },
                                ),
                                "LastChange": ("V", "i=32852", {}),
                                "TagVariables": (
                                    "O",
                                    "i=23479",
                                    {
                                        "FindAlias": (
                                            "M",
                                            "i=23485",
                                            {
                                                "InputArguments": ("V", "i=23486", {}),
                                                "OutputArguments": ("V", "i=23487", {}),
                                            },
                                        )
                                    },
                                ),
                                "Topics": (
                                    "O",
                                    "i=23488",
                                    {
                                        "FindAlias": (
                                            "M",
                                            "i=23494",
                                            {
                                                "InputArguments": ("V", "i=23495", {}),
                                                "OutputArguments": ("V", "i=23496", {}),
                                            },
                                        )
                                    },
                                ),
                            },
                        ),
                        "Locations": ("O", "i=31915", {}),
                        "Server": (
                            "O",
                            "i=2253",
                            {
                                "Auditing": ("V", "i=2994", {}),
                                "DefaultHAConfiguration": (
                                    "O",
                                    "i=32637",
                                    {
                                        "AggregateConfiguration": (
                                            "O",
                                            "i=32638",
                                            {
                                                "PercentDataBad": ("V", "i=32640", {}),
                                                "PercentDataGood": ("V", "i=32641", {}),
                                                "TreatUncertainAsBad": (
                                                    "V",
                                                    "i=32639",
                                                    {},
                                                ),
                                                "UseSlopedExtrapolation": (
                                                    "V",
                                                    "i=32642",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "AggregateFunctions": ("O", "i=32643", {}),
                                        "Definition": ("V", "i=32645", {}),
                                        "ExceptionDeviation": ("V", "i=32648", {}),
                                        "ExceptionDeviationFormat": (
                                            "V",
                                            "i=32649",
                                            {},
                                        ),
                                        "MaxCountStoredValues": ("V", "i=32753", {}),
                                        "MaxTimeInterval": ("V", "i=32646", {}),
                                        "MaxTimeStoredValues": ("V", "i=32752", {}),
                                        "MinTimeInterval": ("V", "i=32647", {}),
                                        "ServerTimestampSupported": (
                                            "V",
                                            "i=32682",
                                            {},
                                        ),
                                        "StartOfArchive": ("V", "i=32650", {}),
                                        "StartOfOnlineArchive": ("V", "i=32656", {}),
                                        "Stepped": ("V", "i=32644", {}),
                                    },
                                ),
                                "DefaultHEConfiguration": (
                                    "O",
                                    "i=32754",
                                    {
                                        "EventTypes": ("O", "i=32755", {}),
                                        "StartOfArchive": ("V", "i=32756", {}),
                                        "StartOfOnlineArchive": ("V", "i=32757", {}),
                                    },
                                ),
                                "Dictionaries": ("O", "i=17594", {}),
                                "EstimatedReturnTime": ("V", "i=12885", {}),
                                "GetMonitoredItems": (
                                    "M",
                                    "i=11492",
                                    {
                                        "InputArguments": ("V", "i=11493", {}),
                                        "OutputArguments": ("V", "i=11494", {}),
                                    },
                                ),
                                "LocalTime": ("V", "i=17634", {}),
                                "NamespaceArray": ("V", "i=2255", {}),
                                "Namespaces": (
                                    "O",
                                    "i=11715",
                                    {
                                        "http://opcfoundation.org/UA/": (
                                            "O",
                                            "i=15957",
                                            {
                                                "DefaultAccessRestrictions": (
                                                    "V",
                                                    "i=16136",
                                                    {},
                                                ),
                                                "DefaultRolePermissions": (
                                                    "V",
                                                    "i=16134",
                                                    {},
                                                ),
                                                "DefaultUserRolePermissions": (
                                                    "V",
                                                    "i=16135",
                                                    {},
                                                ),
                                                "IsNamespaceSubset": (
                                                    "V",
                                                    "i=15961",
                                                    {},
                                                ),
                                                "ModelVersion": ("V", "i=32408", {}),
                                                "NamespacePublicationDate": (
                                                    "V",
                                                    "i=15960",
                                                    {},
                                                ),
                                                "NamespaceUri": ("V", "i=15958", {}),
                                                "NamespaceVersion": (
                                                    "V",
                                                    "i=15959",
                                                    {},
                                                ),
                                                "StaticNodeIdTypes": (
                                                    "V",
                                                    "i=15962",
                                                    {},
                                                ),
                                                "StaticNumericNodeIdRange": (
                                                    "V",
                                                    "i=15963",
                                                    {},
                                                ),
                                                "StaticStringNodeIdPattern": (
                                                    "V",
                                                    "i=15964",
                                                    {},
                                                ),
                                            },
                                        )
                                    },
                                ),
                                "PublishSubscribe": (
                                    "O",
                                    "i=14443",
                                    {
                                        "AddConnection": (
                                            "M",
                                            "i=17366",
                                            {
                                                "InputArguments": ("V", "i=17367", {}),
                                                "OutputArguments": ("V", "i=17368", {}),
                                            },
                                        ),
                                        "ConfigurationProperties": ("V", "i=32404", {}),
                                        "ConfigurationVersion": ("V", "i=25481", {}),
                                        "DataSetClasses": ("O", "i=23685", {}),
                                        "DefaultDatagramPublisherId": (
                                            "V",
                                            "i=25480",
                                            {},
                                        ),
                                        "DefaultSecurityKeyServices": (
                                            "V",
                                            "i=32403",
                                            {},
                                        ),
                                        "Diagnostics": (
                                            "O",
                                            "i=17409",
                                            {
                                                "Counters": (
                                                    "O",
                                                    "i=17423",
                                                    {
                                                        "StateDisabledByMethod": (
                                                            "V",
                                                            "i=17451",
                                                            {
                                                                "Active": (
                                                                    "V",
                                                                    "i=17452",
                                                                    {},
                                                                ),
                                                                "Classification": (
                                                                    "V",
                                                                    "i=17453",
                                                                    {},
                                                                ),
                                                                "DiagnosticsLevel": (
                                                                    "V",
                                                                    "i=17454",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "StateError": (
                                                            "V",
                                                            "i=17424",
                                                            {
                                                                "Active": (
                                                                    "V",
                                                                    "i=17425",
                                                                    {},
                                                                ),
                                                                "Classification": (
                                                                    "V",
                                                                    "i=17426",
                                                                    {},
                                                                ),
                                                                "DiagnosticsLevel": (
                                                                    "V",
                                                                    "i=17429",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "StateOperationalByMethod": (
                                                            "V",
                                                            "i=17431",
                                                            {
                                                                "Active": (
                                                                    "V",
                                                                    "i=17432",
                                                                    {},
                                                                ),
                                                                "Classification": (
                                                                    "V",
                                                                    "i=17433",
                                                                    {},
                                                                ),
                                                                "DiagnosticsLevel": (
                                                                    "V",
                                                                    "i=17434",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "StateOperationalByParent": (
                                                            "V",
                                                            "i=17436",
                                                            {
                                                                "Active": (
                                                                    "V",
                                                                    "i=17437",
                                                                    {},
                                                                ),
                                                                "Classification": (
                                                                    "V",
                                                                    "i=17438",
                                                                    {},
                                                                ),
                                                                "DiagnosticsLevel": (
                                                                    "V",
                                                                    "i=17439",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "StateOperationalFromError": (
                                                            "V",
                                                            "i=17441",
                                                            {
                                                                "Active": (
                                                                    "V",
                                                                    "i=17442",
                                                                    {},
                                                                ),
                                                                "Classification": (
                                                                    "V",
                                                                    "i=17443",
                                                                    {},
                                                                ),
                                                                "DiagnosticsLevel": (
                                                                    "V",
                                                                    "i=17444",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "StatePausedByParent": (
                                                            "V",
                                                            "i=17446",
                                                            {
                                                                "Active": (
                                                                    "V",
                                                                    "i=17447",
                                                                    {},
                                                                ),
                                                                "Classification": (
                                                                    "V",
                                                                    "i=17448",
                                                                    {},
                                                                ),
                                                                "DiagnosticsLevel": (
                                                                    "V",
                                                                    "i=17449",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                    },
                                                ),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=17410",
                                                    {},
                                                ),
                                                "LiveValues": (
                                                    "O",
                                                    "i=17457",
                                                    {
                                                        "ConfiguredDataSetReaders": (
                                                            "V",
                                                            "i=17460",
                                                            {
                                                                "DiagnosticsLevel": (
                                                                    "V",
                                                                    "i=17461",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "ConfiguredDataSetWriters": (
                                                            "V",
                                                            "i=17458",
                                                            {
                                                                "DiagnosticsLevel": (
                                                                    "V",
                                                                    "i=17459",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "OperationalDataSetReaders": (
                                                            "V",
                                                            "i=17464",
                                                            {
                                                                "DiagnosticsLevel": (
                                                                    "V",
                                                                    "i=17466",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "OperationalDataSetWriters": (
                                                            "V",
                                                            "i=17462",
                                                            {
                                                                "DiagnosticsLevel": (
                                                                    "V",
                                                                    "i=17463",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                    },
                                                ),
                                                "Reset": ("M", "i=17421", {}),
                                                "SubError": ("V", "i=17422", {}),
                                                "TotalError": (
                                                    "V",
                                                    "i=17416",
                                                    {
                                                        "Active": ("V", "i=17417", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=17418",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=17419",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "TotalInformation": (
                                                    "V",
                                                    "i=17411",
                                                    {
                                                        "Active": ("V", "i=17412", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=17413",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=17414",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                            },
                                        ),
                                        "GetSecurityGroup": (
                                            "M",
                                            "i=15440",
                                            {
                                                "InputArguments": ("V", "i=15441", {}),
                                                "OutputArguments": ("V", "i=15442", {}),
                                            },
                                        ),
                                        "GetSecurityKeys": (
                                            "M",
                                            "i=15215",
                                            {
                                                "InputArguments": ("V", "i=15216", {}),
                                                "OutputArguments": ("V", "i=15217", {}),
                                            },
                                        ),
                                        "KeyPushTargets": (
                                            "O",
                                            "i=25440",
                                            {
                                                "AddPushTarget": (
                                                    "M",
                                                    "i=25441",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=25442",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=25443",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "RemovePushTarget": (
                                                    "M",
                                                    "i=25444",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=25445",
                                                            {},
                                                        )
                                                    },
                                                ),
                                            },
                                        ),
                                        "PubSubCapablities": (
                                            "O",
                                            "i=23678",
                                            {
                                                "MaxDataSetReaders": (
                                                    "V",
                                                    "i=23683",
                                                    {},
                                                ),
                                                "MaxDataSetWriters": (
                                                    "V",
                                                    "i=23682",
                                                    {},
                                                ),
                                                "MaxDataSetWritersPerGroup": (
                                                    "V",
                                                    "i=32398",
                                                    {},
                                                ),
                                                "MaxFieldsPerDataSet": (
                                                    "V",
                                                    "i=23684",
                                                    {},
                                                ),
                                                "MaxNetworkMessageSizeBroker": (
                                                    "V",
                                                    "i=32400",
                                                    {},
                                                ),
                                                "MaxNetworkMessageSizeDatagram": (
                                                    "V",
                                                    "i=32399",
                                                    {},
                                                ),
                                                "MaxPubSubConnections": (
                                                    "V",
                                                    "i=23679",
                                                    {},
                                                ),
                                                "MaxPublishedDataSets": (
                                                    "V",
                                                    "i=32841",
                                                    {},
                                                ),
                                                "MaxPushTargets": ("V", "i=32840", {}),
                                                "MaxReaderGroups": ("V", "i=23681", {}),
                                                "MaxSecurityGroups": (
                                                    "V",
                                                    "i=32839",
                                                    {},
                                                ),
                                                "MaxStandaloneSubscribedDataSets": (
                                                    "V",
                                                    "i=32842",
                                                    {},
                                                ),
                                                "MaxWriterGroups": ("V", "i=23680", {}),
                                                "SupportSecurityKeyPull": (
                                                    "V",
                                                    "i=32401",
                                                    {},
                                                ),
                                                "SupportSecurityKeyPush": (
                                                    "V",
                                                    "i=32402",
                                                    {},
                                                ),
                                                "SupportSecurityKeyServer": (
                                                    "V",
                                                    "i=32843",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "PubSubConfiguration": (
                                            "O",
                                            "i=25451",
                                            {
                                                "Close": (
                                                    "M",
                                                    "i=25462",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=25463",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "CloseAndUpdate": (
                                                    "M",
                                                    "i=25477",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=25478",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=25479",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "GetPosition": (
                                                    "M",
                                                    "i=25469",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=25470",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=25471",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "Open": (
                                                    "M",
                                                    "i=25459",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=25460",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=25461",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "OpenCount": ("V", "i=25455", {}),
                                                "Read": (
                                                    "M",
                                                    "i=25464",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=25465",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=25466",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "ReserveIds": (
                                                    "M",
                                                    "i=25474",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=25475",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=25476",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "SetPosition": (
                                                    "M",
                                                    "i=25472",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=25473",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Size": ("V", "i=25452", {}),
                                                "UserWritable": ("V", "i=25454", {}),
                                                "Writable": ("V", "i=25453", {}),
                                                "Write": (
                                                    "M",
                                                    "i=25467",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=25468",
                                                            {},
                                                        )
                                                    },
                                                ),
                                            },
                                        ),
                                        "PublishedDataSets": ("O", "i=17371", {}),
                                        "RemoveConnection": (
                                            "M",
                                            "i=17369",
                                            {"InputArguments": ("V", "i=17370", {})},
                                        ),
                                        "SecurityGroups": (
                                            "O",
                                            "i=15443",
                                            {
                                                "AddSecurityGroup": (
                                                    "M",
                                                    "i=15444",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=15445",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=15446",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "RemoveSecurityGroup": (
                                                    "M",
                                                    "i=15447",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=15448",
                                                            {},
                                                        )
                                                    },
                                                ),
                                            },
                                        ),
                                        "SetSecurityKeys": (
                                            "M",
                                            "i=17364",
                                            {"InputArguments": ("V", "i=17365", {})},
                                        ),
                                        "Status": (
                                            "O",
                                            "i=17405",
                                            {"State": ("V", "i=17406", {})},
                                        ),
                                        "SubscribedDataSets": ("O", "i=23658", {}),
                                        "SupportedTransportProfiles": (
                                            "V",
                                            "i=17481",
                                            {},
                                        ),
                                    },
                                ),
                                "Quantities": ("O", "i=32530", {}),
                                "RequestServerStateChange": (
                                    "M",
                                    "i=12886",
                                    {"InputArguments": ("V", "i=12887", {})},
                                ),
                                "ResendData": (
                                    "M",
                                    "i=12873",
                                    {"InputArguments": ("V", "i=12874", {})},
                                ),
                                "Resources": (
                                    "O",
                                    "i=24226",
                                    {
                                        "Communication": (
                                            "O",
                                            "i=24227",
                                            {
                                                "LLDP": (
                                                    "O",
                                                    "i=18958",
                                                    {
                                                        "LocalSystemData": (
                                                            "O",
                                                            "i=18965",
                                                            {
                                                                "ChassisId": (
                                                                    "V",
                                                                    "i=18967",
                                                                    {},
                                                                ),
                                                                "ChassisIdSubtype": (
                                                                    "V",
                                                                    "i=18966",
                                                                    {},
                                                                ),
                                                                "SystemDescription": (
                                                                    "V",
                                                                    "i=18969",
                                                                    {},
                                                                ),
                                                                "SystemName": (
                                                                    "V",
                                                                    "i=18968",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "Ports": ("O", "i=18972", {}),
                                                    },
                                                ),
                                                "MappingTables": ("O", "i=24228", {}),
                                                "NetworkInterfaces": (
                                                    "O",
                                                    "i=24229",
                                                    {},
                                                ),
                                                "Streams": (
                                                    "O",
                                                    "i=24230",
                                                    {
                                                        "ListenerStreams": (
                                                            "O",
                                                            "i=24232",
                                                            {},
                                                        ),
                                                        "TalkerStreams": (
                                                            "O",
                                                            "i=24231",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                            },
                                        ),
                                        "Logs": ("O", "i=19378", {}),
                                        "ManagedApplications": ("O", "i=16706", {}),
                                        "ProvisionableDevice": (
                                            "O",
                                            "i=29878",
                                            {
                                                "IsSingleton": ("V", "i=29879", {}),
                                                "RequestTickets": (
                                                    "M",
                                                    "i=29880",
                                                    {
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=29881",
                                                            {},
                                                        )
                                                    },
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "ServerArray": ("V", "i=2254", {}),
                                "ServerCapabilities": (
                                    "O",
                                    "i=2268",
                                    {
                                        "AggregateFunctions": ("O", "i=2997", {}),
                                        "ConformanceUnits": ("V", "i=24101", {}),
                                        "HistoryServerCapabilities": (
                                            "O",
                                            "i=11192",
                                            {
                                                "AccessHistoryDataCapability": (
                                                    "V",
                                                    "i=11193",
                                                    {},
                                                ),
                                                "AccessHistoryEventsCapability": (
                                                    "V",
                                                    "i=11242",
                                                    {},
                                                ),
                                                "AggregateFunctions": (
                                                    "O",
                                                    "i=11201",
                                                    {},
                                                ),
                                                "DeleteAtTimeCapability": (
                                                    "V",
                                                    "i=11200",
                                                    {},
                                                ),
                                                "DeleteEventCapability": (
                                                    "V",
                                                    "i=11502",
                                                    {},
                                                ),
                                                "DeleteRawCapability": (
                                                    "V",
                                                    "i=11199",
                                                    {},
                                                ),
                                                "InsertAnnotationCapability": (
                                                    "V",
                                                    "i=11275",
                                                    {},
                                                ),
                                                "InsertDataCapability": (
                                                    "V",
                                                    "i=11196",
                                                    {},
                                                ),
                                                "InsertEventCapability": (
                                                    "V",
                                                    "i=11281",
                                                    {},
                                                ),
                                                "MaxReturnDataValues": (
                                                    "V",
                                                    "i=11273",
                                                    {},
                                                ),
                                                "MaxReturnEventValues": (
                                                    "V",
                                                    "i=11274",
                                                    {},
                                                ),
                                                "ReplaceDataCapability": (
                                                    "V",
                                                    "i=11197",
                                                    {},
                                                ),
                                                "ReplaceEventCapability": (
                                                    "V",
                                                    "i=11282",
                                                    {},
                                                ),
                                                "ServerTimestampSupported": (
                                                    "V",
                                                    "i=19091",
                                                    {},
                                                ),
                                                "UpdateDataCapability": (
                                                    "V",
                                                    "i=11198",
                                                    {},
                                                ),
                                                "UpdateEventCapability": (
                                                    "V",
                                                    "i=11283",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "LocaleIdArray": ("V", "i=2271", {}),
                                        "MaxArrayLength": ("V", "i=11702", {}),
                                        "MaxBrowseContinuationPoints": (
                                            "V",
                                            "i=2735",
                                            {},
                                        ),
                                        "MaxByteStringLength": ("V", "i=12911", {}),
                                        "MaxHistoryContinuationPoints": (
                                            "V",
                                            "i=2737",
                                            {},
                                        ),
                                        "MaxMonitoredItems": ("V", "i=24097", {}),
                                        "MaxMonitoredItemsPerSubscription": (
                                            "V",
                                            "i=24104",
                                            {},
                                        ),
                                        "MaxMonitoredItemsQueueSize": (
                                            "V",
                                            "i=31916",
                                            {},
                                        ),
                                        "MaxQueryContinuationPoints": (
                                            "V",
                                            "i=2736",
                                            {},
                                        ),
                                        "MaxSelectClauseParameters": (
                                            "V",
                                            "i=24099",
                                            {},
                                        ),
                                        "MaxSessions": ("V", "i=24095", {}),
                                        "MaxStringLength": ("V", "i=11703", {}),
                                        "MaxSubscriptions": ("V", "i=24096", {}),
                                        "MaxSubscriptionsPerSession": (
                                            "V",
                                            "i=24098",
                                            {},
                                        ),
                                        "MaxWhereClauseParameters": (
                                            "V",
                                            "i=24100",
                                            {},
                                        ),
                                        "MinSupportedSampleRate": ("V", "i=2272", {}),
                                        "ModellingRules": ("O", "i=2996", {}),
                                        "OperationLimits": (
                                            "O",
                                            "i=11704",
                                            {
                                                "MaxMonitoredItemsPerCall": (
                                                    "V",
                                                    "i=11714",
                                                    {},
                                                ),
                                                "MaxNodesPerBrowse": (
                                                    "V",
                                                    "i=11710",
                                                    {},
                                                ),
                                                "MaxNodesPerHistoryReadData": (
                                                    "V",
                                                    "i=12165",
                                                    {},
                                                ),
                                                "MaxNodesPerHistoryReadEvents": (
                                                    "V",
                                                    "i=12166",
                                                    {},
                                                ),
                                                "MaxNodesPerHistoryUpdateData": (
                                                    "V",
                                                    "i=12167",
                                                    {},
                                                ),
                                                "MaxNodesPerHistoryUpdateEvents": (
                                                    "V",
                                                    "i=12168",
                                                    {},
                                                ),
                                                "MaxNodesPerMethodCall": (
                                                    "V",
                                                    "i=11709",
                                                    {},
                                                ),
                                                "MaxNodesPerNodeManagement": (
                                                    "V",
                                                    "i=11713",
                                                    {},
                                                ),
                                                "MaxNodesPerRead": ("V", "i=11705", {}),
                                                "MaxNodesPerRegisterNodes": (
                                                    "V",
                                                    "i=11711",
                                                    {},
                                                ),
                                                "MaxNodesPerTranslateBrowsePathsToNodeIds": (
                                                    "V",
                                                    "i=11712",
                                                    {},
                                                ),
                                                "MaxNodesPerWrite": (
                                                    "V",
                                                    "i=11707",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "RoleSet": (
                                            "O",
                                            "i=15606",
                                            {
                                                "AddRole": (
                                                    "M",
                                                    "i=16301",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=16302",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=16303",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "Anonymous": (
                                                    "O",
                                                    "i=15644",
                                                    {
                                                        "Identities": (
                                                            "V",
                                                            "i=16192",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "AuthenticatedUser": (
                                                    "O",
                                                    "i=15656",
                                                    {
                                                        "Identities": (
                                                            "V",
                                                            "i=16203",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "ConfigureAdmin": (
                                                    "O",
                                                    "i=15716",
                                                    {
                                                        "AddApplication": (
                                                            "M",
                                                            "i=16272",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16273",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "AddEndpoint": (
                                                            "M",
                                                            "i=16276",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16277",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "AddIdentity": (
                                                            "M",
                                                            "i=15720",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=15721",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "Applications": (
                                                            "V",
                                                            "i=16270",
                                                            {},
                                                        ),
                                                        "ApplicationsExclude": (
                                                            "V",
                                                            "i=15428",
                                                            {},
                                                        ),
                                                        "CustomConfiguration": (
                                                            "V",
                                                            "i=24146",
                                                            {},
                                                        ),
                                                        "Endpoints": (
                                                            "V",
                                                            "i=16271",
                                                            {},
                                                        ),
                                                        "EndpointsExclude": (
                                                            "V",
                                                            "i=15429",
                                                            {},
                                                        ),
                                                        "Identities": (
                                                            "V",
                                                            "i=16269",
                                                            {},
                                                        ),
                                                        "RemoveApplication": (
                                                            "M",
                                                            "i=16274",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16275",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "RemoveEndpoint": (
                                                            "M",
                                                            "i=16278",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16279",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "RemoveIdentity": (
                                                            "M",
                                                            "i=15722",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=15723",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                    },
                                                ),
                                                "Engineer": (
                                                    "O",
                                                    "i=16036",
                                                    {
                                                        "AddApplication": (
                                                            "M",
                                                            "i=16239",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16240",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "AddEndpoint": (
                                                            "M",
                                                            "i=16243",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16244",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "AddIdentity": (
                                                            "M",
                                                            "i=16041",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16042",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "Applications": (
                                                            "V",
                                                            "i=16237",
                                                            {},
                                                        ),
                                                        "ApplicationsExclude": (
                                                            "V",
                                                            "i=15424",
                                                            {},
                                                        ),
                                                        "CustomConfiguration": (
                                                            "V",
                                                            "i=24144",
                                                            {},
                                                        ),
                                                        "Endpoints": (
                                                            "V",
                                                            "i=16238",
                                                            {},
                                                        ),
                                                        "EndpointsExclude": (
                                                            "V",
                                                            "i=15425",
                                                            {},
                                                        ),
                                                        "Identities": (
                                                            "V",
                                                            "i=16236",
                                                            {},
                                                        ),
                                                        "RemoveApplication": (
                                                            "M",
                                                            "i=16241",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16242",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "RemoveEndpoint": (
                                                            "M",
                                                            "i=16245",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16246",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "RemoveIdentity": (
                                                            "M",
                                                            "i=16043",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16044",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                    },
                                                ),
                                                "Observer": (
                                                    "O",
                                                    "i=15668",
                                                    {
                                                        "AddApplication": (
                                                            "M",
                                                            "i=16217",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16218",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "AddEndpoint": (
                                                            "M",
                                                            "i=16221",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16222",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "AddIdentity": (
                                                            "M",
                                                            "i=15672",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=15673",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "Applications": (
                                                            "V",
                                                            "i=16215",
                                                            {},
                                                        ),
                                                        "ApplicationsExclude": (
                                                            "V",
                                                            "i=15416",
                                                            {},
                                                        ),
                                                        "CustomConfiguration": (
                                                            "V",
                                                            "i=24142",
                                                            {},
                                                        ),
                                                        "Endpoints": (
                                                            "V",
                                                            "i=16216",
                                                            {},
                                                        ),
                                                        "EndpointsExclude": (
                                                            "V",
                                                            "i=15417",
                                                            {},
                                                        ),
                                                        "Identities": (
                                                            "V",
                                                            "i=16214",
                                                            {},
                                                        ),
                                                        "RemoveApplication": (
                                                            "M",
                                                            "i=16219",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16220",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "RemoveEndpoint": (
                                                            "M",
                                                            "i=16223",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16224",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "RemoveIdentity": (
                                                            "M",
                                                            "i=15674",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=15675",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                    },
                                                ),
                                                "Operator": (
                                                    "O",
                                                    "i=15680",
                                                    {
                                                        "AddApplication": (
                                                            "M",
                                                            "i=16228",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16229",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "AddEndpoint": (
                                                            "M",
                                                            "i=16232",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16233",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "AddIdentity": (
                                                            "M",
                                                            "i=15684",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=15685",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "Applications": (
                                                            "V",
                                                            "i=16226",
                                                            {},
                                                        ),
                                                        "ApplicationsExclude": (
                                                            "V",
                                                            "i=15418",
                                                            {},
                                                        ),
                                                        "CustomConfiguration": (
                                                            "V",
                                                            "i=24143",
                                                            {},
                                                        ),
                                                        "Endpoints": (
                                                            "V",
                                                            "i=16227",
                                                            {},
                                                        ),
                                                        "EndpointsExclude": (
                                                            "V",
                                                            "i=15423",
                                                            {},
                                                        ),
                                                        "Identities": (
                                                            "V",
                                                            "i=16225",
                                                            {},
                                                        ),
                                                        "RemoveApplication": (
                                                            "M",
                                                            "i=16230",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16231",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "RemoveEndpoint": (
                                                            "M",
                                                            "i=16234",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16235",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "RemoveIdentity": (
                                                            "M",
                                                            "i=15686",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=15687",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                    },
                                                ),
                                                "RemoveRole": (
                                                    "M",
                                                    "i=16304",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=16305",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "SecurityAdmin": (
                                                    "O",
                                                    "i=15704",
                                                    {
                                                        "AddApplication": (
                                                            "M",
                                                            "i=16261",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16262",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "AddEndpoint": (
                                                            "M",
                                                            "i=16265",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16266",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "AddIdentity": (
                                                            "M",
                                                            "i=15708",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=15709",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "Applications": (
                                                            "V",
                                                            "i=16259",
                                                            {},
                                                        ),
                                                        "ApplicationsExclude": (
                                                            "V",
                                                            "i=15430",
                                                            {},
                                                        ),
                                                        "CustomConfiguration": (
                                                            "V",
                                                            "i=24147",
                                                            {},
                                                        ),
                                                        "Endpoints": (
                                                            "V",
                                                            "i=16260",
                                                            {},
                                                        ),
                                                        "EndpointsExclude": (
                                                            "V",
                                                            "i=15527",
                                                            {},
                                                        ),
                                                        "Identities": (
                                                            "V",
                                                            "i=16258",
                                                            {},
                                                        ),
                                                        "RemoveApplication": (
                                                            "M",
                                                            "i=16263",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16264",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "RemoveEndpoint": (
                                                            "M",
                                                            "i=16267",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16268",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "RemoveIdentity": (
                                                            "M",
                                                            "i=15710",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=15711",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                    },
                                                ),
                                                "SecurityKeyServerAccess": (
                                                    "O",
                                                    "i=25603",
                                                    {
                                                        "AddApplication": (
                                                            "M",
                                                            "i=25614",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=25615",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "AddEndpoint": (
                                                            "M",
                                                            "i=25618",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=25619",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "AddIdentity": (
                                                            "M",
                                                            "i=25610",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=25611",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "Applications": (
                                                            "V",
                                                            "i=25606",
                                                            {},
                                                        ),
                                                        "ApplicationsExclude": (
                                                            "V",
                                                            "i=25605",
                                                            {},
                                                        ),
                                                        "CustomConfiguration": (
                                                            "V",
                                                            "i=25609",
                                                            {},
                                                        ),
                                                        "Endpoints": (
                                                            "V",
                                                            "i=25608",
                                                            {},
                                                        ),
                                                        "EndpointsExclude": (
                                                            "V",
                                                            "i=25607",
                                                            {},
                                                        ),
                                                        "Identities": (
                                                            "V",
                                                            "i=25604",
                                                            {},
                                                        ),
                                                        "RemoveApplication": (
                                                            "M",
                                                            "i=25616",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=25617",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "RemoveEndpoint": (
                                                            "M",
                                                            "i=25620",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=25621",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "RemoveIdentity": (
                                                            "M",
                                                            "i=25612",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=25613",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                    },
                                                ),
                                                "SecurityKeyServerAdmin": (
                                                    "O",
                                                    "i=25565",
                                                    {
                                                        "AddApplication": (
                                                            "M",
                                                            "i=25576",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=25577",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "AddEndpoint": (
                                                            "M",
                                                            "i=25580",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=25581",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "AddIdentity": (
                                                            "M",
                                                            "i=25572",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=25573",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "Applications": (
                                                            "V",
                                                            "i=25568",
                                                            {},
                                                        ),
                                                        "ApplicationsExclude": (
                                                            "V",
                                                            "i=25567",
                                                            {},
                                                        ),
                                                        "CustomConfiguration": (
                                                            "V",
                                                            "i=25571",
                                                            {},
                                                        ),
                                                        "Endpoints": (
                                                            "V",
                                                            "i=25570",
                                                            {},
                                                        ),
                                                        "EndpointsExclude": (
                                                            "V",
                                                            "i=25569",
                                                            {},
                                                        ),
                                                        "Identities": (
                                                            "V",
                                                            "i=25566",
                                                            {},
                                                        ),
                                                        "RemoveApplication": (
                                                            "M",
                                                            "i=25578",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=25579",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "RemoveEndpoint": (
                                                            "M",
                                                            "i=25582",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=25583",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "RemoveIdentity": (
                                                            "M",
                                                            "i=25574",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=25575",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                    },
                                                ),
                                                "SecurityKeyServerPush": (
                                                    "O",
                                                    "i=25584",
                                                    {
                                                        "AddApplication": (
                                                            "M",
                                                            "i=25595",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=25596",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "AddEndpoint": (
                                                            "M",
                                                            "i=25599",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=25600",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "AddIdentity": (
                                                            "M",
                                                            "i=25591",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=25592",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "Applications": (
                                                            "V",
                                                            "i=25587",
                                                            {},
                                                        ),
                                                        "ApplicationsExclude": (
                                                            "V",
                                                            "i=25586",
                                                            {},
                                                        ),
                                                        "CustomConfiguration": (
                                                            "V",
                                                            "i=25590",
                                                            {},
                                                        ),
                                                        "Endpoints": (
                                                            "V",
                                                            "i=25589",
                                                            {},
                                                        ),
                                                        "EndpointsExclude": (
                                                            "V",
                                                            "i=25588",
                                                            {},
                                                        ),
                                                        "Identities": (
                                                            "V",
                                                            "i=25585",
                                                            {},
                                                        ),
                                                        "RemoveApplication": (
                                                            "M",
                                                            "i=25597",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=25598",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "RemoveEndpoint": (
                                                            "M",
                                                            "i=25601",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=25602",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "RemoveIdentity": (
                                                            "M",
                                                            "i=25593",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=25594",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                    },
                                                ),
                                                "Supervisor": (
                                                    "O",
                                                    "i=15692",
                                                    {
                                                        "AddApplication": (
                                                            "M",
                                                            "i=16250",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16251",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "AddEndpoint": (
                                                            "M",
                                                            "i=16254",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16255",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "AddIdentity": (
                                                            "M",
                                                            "i=15696",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=15697",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "Applications": (
                                                            "V",
                                                            "i=16248",
                                                            {},
                                                        ),
                                                        "ApplicationsExclude": (
                                                            "V",
                                                            "i=15426",
                                                            {},
                                                        ),
                                                        "CustomConfiguration": (
                                                            "V",
                                                            "i=24145",
                                                            {},
                                                        ),
                                                        "Endpoints": (
                                                            "V",
                                                            "i=16249",
                                                            {},
                                                        ),
                                                        "EndpointsExclude": (
                                                            "V",
                                                            "i=15427",
                                                            {},
                                                        ),
                                                        "Identities": (
                                                            "V",
                                                            "i=16247",
                                                            {},
                                                        ),
                                                        "RemoveApplication": (
                                                            "M",
                                                            "i=16252",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16253",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "RemoveEndpoint": (
                                                            "M",
                                                            "i=16256",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=16257",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "RemoveIdentity": (
                                                            "M",
                                                            "i=15698",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=15699",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                    },
                                                ),
                                                "TrustedApplication": (
                                                    "O",
                                                    "i=18625",
                                                    {
                                                        "Identities": (
                                                            "V",
                                                            "i=18626",
                                                            {},
                                                        )
                                                    },
                                                ),
                                            },
                                        ),
                                        "ServerProfileArray": ("V", "i=2269", {}),
                                        "SoftwareCertificates": ("V", "i=3704", {}),
                                    },
                                ),
                                "ServerConfiguration": (
                                    "O",
                                    "i=12637",
                                    {
                                        "ApplicationType": ("V", "i=25707", {}),
                                        "ApplicationUri": ("V", "i=25706", {}),
                                        "ApplyChanges": ("M", "i=12740", {}),
                                        "AuthorizationServices": ("O", "i=17732", {}),
                                        "CancelChanges": ("M", "i=25708", {}),
                                        "CertificateGroups": (
                                            "O",
                                            "i=14053",
                                            {
                                                "DefaultApplicationGroup": (
                                                    "O",
                                                    "i=14156",
                                                    {
                                                        "CertificateTypes": (
                                                            "V",
                                                            "i=14161",
                                                            {},
                                                        ),
                                                        "TrustList": (
                                                            "O",
                                                            "i=12642",
                                                            {
                                                                "AddCertificate": (
                                                                    "M",
                                                                    "i=12668",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=12669",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "Close": (
                                                                    "M",
                                                                    "i=12650",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=12651",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "CloseAndUpdate": (
                                                                    "M",
                                                                    "i=12666",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14160",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=12667",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "GetPosition": (
                                                                    "M",
                                                                    "i=12657",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=12658",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=12659",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "LastUpdateTime": (
                                                                    "V",
                                                                    "i=12662",
                                                                    {},
                                                                ),
                                                                "Open": (
                                                                    "M",
                                                                    "i=12647",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=12648",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=12649",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "OpenCount": (
                                                                    "V",
                                                                    "i=12646",
                                                                    {},
                                                                ),
                                                                "OpenWithMasks": (
                                                                    "M",
                                                                    "i=12663",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=12664",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=12665",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "Read": (
                                                                    "M",
                                                                    "i=12652",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=12653",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=12654",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "RemoveCertificate": (
                                                                    "M",
                                                                    "i=12670",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=12671",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "SetPosition": (
                                                                    "M",
                                                                    "i=12660",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=12661",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "Size": (
                                                                    "V",
                                                                    "i=12643",
                                                                    {},
                                                                ),
                                                                "UserWritable": (
                                                                    "V",
                                                                    "i=14158",
                                                                    {},
                                                                ),
                                                                "Writable": (
                                                                    "V",
                                                                    "i=14157",
                                                                    {},
                                                                ),
                                                                "Write": (
                                                                    "M",
                                                                    "i=12655",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=12656",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                            },
                                                        ),
                                                    },
                                                ),
                                                "DefaultHttpsGroup": (
                                                    "O",
                                                    "i=14088",
                                                    {
                                                        "CertificateTypes": (
                                                            "V",
                                                            "i=14121",
                                                            {},
                                                        ),
                                                        "TrustList": (
                                                            "O",
                                                            "i=14089",
                                                            {
                                                                "AddCertificate": (
                                                                    "M",
                                                                    "i=14117",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14118",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "Close": (
                                                                    "M",
                                                                    "i=14098",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14099",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "CloseAndUpdate": (
                                                                    "M",
                                                                    "i=14114",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14115",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=14116",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "GetPosition": (
                                                                    "M",
                                                                    "i=14105",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14106",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=14107",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "LastUpdateTime": (
                                                                    "V",
                                                                    "i=14110",
                                                                    {},
                                                                ),
                                                                "Open": (
                                                                    "M",
                                                                    "i=14095",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14096",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=14097",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "OpenCount": (
                                                                    "V",
                                                                    "i=14093",
                                                                    {},
                                                                ),
                                                                "OpenWithMasks": (
                                                                    "M",
                                                                    "i=14111",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14112",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=14113",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "Read": (
                                                                    "M",
                                                                    "i=14100",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14101",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=14102",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "RemoveCertificate": (
                                                                    "M",
                                                                    "i=14119",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14120",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "SetPosition": (
                                                                    "M",
                                                                    "i=14108",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14109",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "Size": (
                                                                    "V",
                                                                    "i=14090",
                                                                    {},
                                                                ),
                                                                "UserWritable": (
                                                                    "V",
                                                                    "i=14092",
                                                                    {},
                                                                ),
                                                                "Writable": (
                                                                    "V",
                                                                    "i=14091",
                                                                    {},
                                                                ),
                                                                "Write": (
                                                                    "M",
                                                                    "i=14103",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14104",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                            },
                                                        ),
                                                    },
                                                ),
                                                "DefaultUserTokenGroup": (
                                                    "O",
                                                    "i=14122",
                                                    {
                                                        "CertificateTypes": (
                                                            "V",
                                                            "i=14155",
                                                            {},
                                                        ),
                                                        "TrustList": (
                                                            "O",
                                                            "i=14123",
                                                            {
                                                                "AddCertificate": (
                                                                    "M",
                                                                    "i=14151",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14152",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "Close": (
                                                                    "M",
                                                                    "i=14132",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14133",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "CloseAndUpdate": (
                                                                    "M",
                                                                    "i=14148",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14149",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=14150",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "GetPosition": (
                                                                    "M",
                                                                    "i=14139",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14140",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=14141",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "LastUpdateTime": (
                                                                    "V",
                                                                    "i=14144",
                                                                    {},
                                                                ),
                                                                "Open": (
                                                                    "M",
                                                                    "i=14129",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14130",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=14131",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "OpenCount": (
                                                                    "V",
                                                                    "i=14127",
                                                                    {},
                                                                ),
                                                                "OpenWithMasks": (
                                                                    "M",
                                                                    "i=14145",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14146",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=14147",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "Read": (
                                                                    "M",
                                                                    "i=14134",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14135",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=14136",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "RemoveCertificate": (
                                                                    "M",
                                                                    "i=14153",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14154",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "SetPosition": (
                                                                    "M",
                                                                    "i=14142",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14143",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "Size": (
                                                                    "V",
                                                                    "i=14124",
                                                                    {},
                                                                ),
                                                                "UserWritable": (
                                                                    "V",
                                                                    "i=14126",
                                                                    {},
                                                                ),
                                                                "Writable": (
                                                                    "V",
                                                                    "i=14125",
                                                                    {},
                                                                ),
                                                                "Write": (
                                                                    "M",
                                                                    "i=14137",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=14138",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                            },
                                                        ),
                                                    },
                                                ),
                                            },
                                        ),
                                        "ConfigurationFile": (
                                            "O",
                                            "i=15892",
                                            {
                                                "ActivityTimeout": ("V", "i=16315", {}),
                                                "AvailableNetworks": (
                                                    "V",
                                                    "i=16652",
                                                    {},
                                                ),
                                                "AvailablePorts": ("V", "i=16653", {}),
                                                "CertificateGroupPurposes": (
                                                    "V",
                                                    "i=19444",
                                                    {},
                                                ),
                                                "CertificateTypes": (
                                                    "V",
                                                    "i=16656",
                                                    {},
                                                ),
                                                "Close": (
                                                    "M",
                                                    "i=16060",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=16061",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "CloseAndUpdate": (
                                                    "M",
                                                    "i=16317",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=16318",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=16319",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "ConfirmUpdate": (
                                                    "M",
                                                    "i=16320",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=16321",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "CurrentVersion": ("V", "i=16306", {}),
                                                "GetPosition": (
                                                    "M",
                                                    "i=16103",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=16122",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=16123",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "LastUpdateTime": ("V", "i=16283", {}),
                                                "MaxCertificateGroups": (
                                                    "V",
                                                    "i=19443",
                                                    {},
                                                ),
                                                "MaxEndpoints": ("V", "i=19442", {}),
                                                "Open": (
                                                    "M",
                                                    "i=16013",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=16020",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=16059",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "OpenCount": ("V", "i=15938", {}),
                                                "Read": (
                                                    "M",
                                                    "i=16074",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=16075",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=16076",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "SecurityPolicyUris": (
                                                    "V",
                                                    "i=16654",
                                                    {},
                                                ),
                                                "SetPosition": (
                                                    "M",
                                                    "i=16124",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=16160",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Size": ("V", "i=15893", {}),
                                                "SupportedDataType": (
                                                    "V",
                                                    "i=16316",
                                                    {},
                                                ),
                                                "UserTokenTypes": ("V", "i=16655", {}),
                                                "UserWritable": ("V", "i=15937", {}),
                                                "Writable": ("V", "i=15894", {}),
                                                "Write": (
                                                    "M",
                                                    "i=16101",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=16102",
                                                            {},
                                                        )
                                                    },
                                                ),
                                            },
                                        ),
                                        "CreateSigningRequest": (
                                            "M",
                                            "i=12737",
                                            {
                                                "InputArguments": ("V", "i=12738", {}),
                                                "OutputArguments": ("V", "i=12739", {}),
                                            },
                                        ),
                                        "GetRejectedList": (
                                            "M",
                                            "i=12777",
                                            {"OutputArguments": ("V", "i=12778", {})},
                                        ),
                                        "HasSecureElement": ("V", "i=23597", {}),
                                        "KeyCredentialConfiguration": (
                                            "O",
                                            "i=18155",
                                            {
                                                "CreateCredential": (
                                                    "M",
                                                    "i=17528",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=17529",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=17530",
                                                            {},
                                                        ),
                                                    },
                                                )
                                            },
                                        ),
                                        "MaxTrustListSize": ("V", "i=12640", {}),
                                        "MulticastDnsEnabled": ("V", "i=12641", {}),
                                        "ProductUri": ("V", "i=25725", {}),
                                        "ResetToServerDefaults": ("M", "i=25709", {}),
                                        "ServerCapabilities": ("V", "i=12710", {}),
                                        "SupportedPrivateKeyFormats": (
                                            "V",
                                            "i=12639",
                                            {},
                                        ),
                                        "TransactionDiagnostics": (
                                            "O",
                                            "i=32336",
                                            {
                                                "AffectedCertificateGroups": (
                                                    "V",
                                                    "i=32341",
                                                    {},
                                                ),
                                                "AffectedTrustLists": (
                                                    "V",
                                                    "i=32340",
                                                    {},
                                                ),
                                                "EndTime": ("V", "i=32338", {}),
                                                "Errors": ("V", "i=32342", {}),
                                                "Result": ("V", "i=32339", {}),
                                                "StartTime": ("V", "i=32337", {}),
                                            },
                                        ),
                                        "UpdateCertificate": (
                                            "M",
                                            "i=13737",
                                            {
                                                "InputArguments": ("V", "i=13738", {}),
                                                "OutputArguments": ("V", "i=13739", {}),
                                            },
                                        ),
                                        "UserManagement": (
                                            "O",
                                            "i=24290",
                                            {
                                                "AddUser": (
                                                    "M",
                                                    "i=24304",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=24305",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "ChangePassword": (
                                                    "M",
                                                    "i=24310",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=24311",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "ModifyUser": (
                                                    "M",
                                                    "i=24306",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=24307",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "PasswordLength": ("V", "i=24302", {}),
                                                "PasswordOptions": ("V", "i=24303", {}),
                                                "PasswordRestrictions": (
                                                    "V",
                                                    "i=24291",
                                                    {},
                                                ),
                                                "RemoveUser": (
                                                    "M",
                                                    "i=24308",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=24309",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Users": ("V", "i=24301", {}),
                                            },
                                        ),
                                    },
                                ),
                                "ServerDiagnostics": (
                                    "O",
                                    "i=2274",
                                    {
                                        "EnabledFlag": ("V", "i=2294", {}),
                                        "SamplingIntervalDiagnosticsArray": (
                                            "V",
                                            "i=2289",
                                            {},
                                        ),
                                        "ServerDiagnosticsSummary": (
                                            "V",
                                            "i=2275",
                                            {
                                                "CumulatedSessionCount": (
                                                    "V",
                                                    "i=2278",
                                                    {},
                                                ),
                                                "CumulatedSubscriptionCount": (
                                                    "V",
                                                    "i=2286",
                                                    {},
                                                ),
                                                "CurrentSessionCount": (
                                                    "V",
                                                    "i=2277",
                                                    {},
                                                ),
                                                "CurrentSubscriptionCount": (
                                                    "V",
                                                    "i=2285",
                                                    {},
                                                ),
                                                "PublishingIntervalCount": (
                                                    "V",
                                                    "i=2284",
                                                    {},
                                                ),
                                                "RejectedRequestsCount": (
                                                    "V",
                                                    "i=2288",
                                                    {},
                                                ),
                                                "RejectedSessionCount": (
                                                    "V",
                                                    "i=3705",
                                                    {},
                                                ),
                                                "SecurityRejectedRequestsCount": (
                                                    "V",
                                                    "i=2287",
                                                    {},
                                                ),
                                                "SecurityRejectedSessionCount": (
                                                    "V",
                                                    "i=2279",
                                                    {},
                                                ),
                                                "ServerViewCount": ("V", "i=2276", {}),
                                                "SessionAbortCount": (
                                                    "V",
                                                    "i=2282",
                                                    {},
                                                ),
                                                "SessionTimeoutCount": (
                                                    "V",
                                                    "i=2281",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "SessionsDiagnosticsSummary": (
                                            "O",
                                            "i=3706",
                                            {
                                                "SessionDiagnosticsArray": (
                                                    "V",
                                                    "i=3707",
                                                    {},
                                                ),
                                                "SessionSecurityDiagnosticsArray": (
                                                    "V",
                                                    "i=3708",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "SubscriptionDiagnosticsArray": (
                                            "V",
                                            "i=2290",
                                            {},
                                        ),
                                    },
                                ),
                                "ServerLog": (
                                    "O",
                                    "i=19372",
                                    {
                                        "GetRecords": (
                                            "M",
                                            "i=19373",
                                            {
                                                "InputArguments": ("V", "i=19374", {}),
                                                "OutputArguments": ("V", "i=19375", {}),
                                            },
                                        ),
                                        "MaxRecords": ("V", "i=19376", {}),
                                        "MaxStorageDuration": ("V", "i=19377", {}),
                                        "MinimumSeverity": ("V", "i=19751", {}),
                                    },
                                ),
                                "ServerRedundancy": (
                                    "O",
                                    "i=2296",
                                    {
                                        "RedundancySupport": ("V", "i=3709", {}),
                                        "RedundantServerArray": ("V", "i=11313", {}),
                                    },
                                ),
                                "ServerStatus": (
                                    "V",
                                    "i=2256",
                                    {
                                        "BuildInfo": (
                                            "V",
                                            "i=2260",
                                            {
                                                "BuildDate": ("V", "i=2266", {}),
                                                "BuildNumber": ("V", "i=2265", {}),
                                                "ManufacturerName": ("V", "i=2263", {}),
                                                "ProductName": ("V", "i=2261", {}),
                                                "ProductUri": ("V", "i=2262", {}),
                                                "SoftwareVersion": ("V", "i=2264", {}),
                                            },
                                        ),
                                        "CurrentTime": ("V", "i=2258", {}),
                                        "SecondsTillShutdown": ("V", "i=2992", {}),
                                        "ShutdownReason": ("V", "i=2993", {}),
                                        "StartTime": ("V", "i=2257", {}),
                                        "State": ("V", "i=2259", {}),
                                    },
                                ),
                                "ServiceLevel": ("V", "i=2267", {}),
                                "SetSubscriptionDurable": (
                                    "M",
                                    "i=12749",
                                    {
                                        "InputArguments": ("V", "i=12750", {}),
                                        "OutputArguments": ("V", "i=12751", {}),
                                    },
                                ),
                                "UrisVersion": ("V", "i=15004", {}),
                                "VendorServerInfo": ("O", "i=2295", {}),
                            },
                        ),
                    },
                ),
                "Types": (
                    "O",
                    "i=86",
                    {
                        "DataTypes": (
                            "O",
                            "i=90",
                            {
                                "OPC Binary": (
                                    "O",
                                    "i=93",
                                    {
                                        "Opc.Ua": (
                                            "V",
                                            "i=7617",
                                            {
                                                "3DCartesianCoordinates": (
                                                    "V",
                                                    "i=18836",
                                                    {},
                                                ),
                                                "3DFrame": ("V", "i=18848", {}),
                                                "3DOrientation": ("V", "i=18842", {}),
                                                "3DVector": ("V", "i=18830", {}),
                                                "ActionMethodDataType": (
                                                    "V",
                                                    "i=18607",
                                                    {},
                                                ),
                                                "ActionTargetDataType": (
                                                    "V",
                                                    "i=18601",
                                                    {},
                                                ),
                                                "AddNodesItem": ("V", "i=7728", {}),
                                                "AddReferencesItem": (
                                                    "V",
                                                    "i=7731",
                                                    {},
                                                ),
                                                "AdditionalParametersType": (
                                                    "V",
                                                    "i=17538",
                                                    {},
                                                ),
                                                "AggregateConfiguration": (
                                                    "V",
                                                    "i=8076",
                                                    {},
                                                ),
                                                "AliasNameDataType": (
                                                    "V",
                                                    "i=23502",
                                                    {},
                                                ),
                                                "Annotation": ("V", "i=8244", {}),
                                                "AnnotationDataType": (
                                                    "V",
                                                    "i=32563",
                                                    {},
                                                ),
                                                "AnonymousIdentityToken": (
                                                    "V",
                                                    "i=7674",
                                                    {},
                                                ),
                                                "ApplicationConfigurationDataType": (
                                                    "V",
                                                    "i=23756",
                                                    {},
                                                ),
                                                "ApplicationDescription": (
                                                    "V",
                                                    "i=7665",
                                                    {},
                                                ),
                                                "ApplicationIdentityDataType": (
                                                    "V",
                                                    "i=16567",
                                                    {},
                                                ),
                                                "Argument": ("V", "i=7650", {}),
                                                "AttributeOperand": ("V", "i=7944", {}),
                                                "AuthorizationServiceConfigurationDataType": (
                                                    "V",
                                                    "i=23759",
                                                    {},
                                                ),
                                                "AxisInformation": ("V", "i=12091", {}),
                                                "BaseConfigurationDataType": (
                                                    "V",
                                                    "i=16548",
                                                    {},
                                                ),
                                                "BaseConfigurationRecordDataType": (
                                                    "V",
                                                    "i=16551",
                                                    {},
                                                ),
                                                "BitFieldDefinition": (
                                                    "V",
                                                    "i=32423",
                                                    {},
                                                ),
                                                "BrokerConnectionTransportDataType": (
                                                    "V",
                                                    "i=15524",
                                                    {},
                                                ),
                                                "BrokerDataSetReaderTransportDataType": (
                                                    "V",
                                                    "i=15946",
                                                    {},
                                                ),
                                                "BrokerDataSetWriterTransportDataType": (
                                                    "V",
                                                    "i=15943",
                                                    {},
                                                ),
                                                "BrokerWriterGroupTransportDataType": (
                                                    "V",
                                                    "i=15940",
                                                    {},
                                                ),
                                                "BuildInfo": ("V", "i=7692", {}),
                                                "CartesianCoordinates": (
                                                    "V",
                                                    "i=18833",
                                                    {},
                                                ),
                                                "CertificateGroupDataType": (
                                                    "V",
                                                    "i=16554",
                                                    {},
                                                ),
                                                "ComplexNumberType": (
                                                    "V",
                                                    "i=12183",
                                                    {},
                                                ),
                                                "ConfigurationUpdateTargetType": (
                                                    "V",
                                                    "i=16557",
                                                    {},
                                                ),
                                                "ConfigurationVersionDataType": (
                                                    "V",
                                                    "i=14876",
                                                    {},
                                                ),
                                                "ConnectionTransportDataType": (
                                                    "V",
                                                    "i=15860",
                                                    {},
                                                ),
                                                "ContentFilter": ("V", "i=7932", {}),
                                                "ContentFilterElement": (
                                                    "V",
                                                    "i=7929",
                                                    {},
                                                ),
                                                "CurrencyUnitType": (
                                                    "V",
                                                    "i=23514",
                                                    {},
                                                ),
                                                "DataSetMetaDataType": (
                                                    "V",
                                                    "i=14849",
                                                    {},
                                                ),
                                                "DataSetReaderDataType": (
                                                    "V",
                                                    "i=15872",
                                                    {},
                                                ),
                                                "DataSetReaderMessageDataType": (
                                                    "V",
                                                    "i=15880",
                                                    {},
                                                ),
                                                "DataSetReaderTransportDataType": (
                                                    "V",
                                                    "i=15877",
                                                    {},
                                                ),
                                                "DataSetWriterDataType": (
                                                    "V",
                                                    "i=15778",
                                                    {},
                                                ),
                                                "DataSetWriterMessageDataType": (
                                                    "V",
                                                    "i=15784",
                                                    {},
                                                ),
                                                "DataSetWriterTransportDataType": (
                                                    "V",
                                                    "i=15781",
                                                    {},
                                                ),
                                                "DataTypeDefinition": (
                                                    "V",
                                                    "i=18178",
                                                    {},
                                                ),
                                                "DataTypeDescription": (
                                                    "V",
                                                    "i=14855",
                                                    {},
                                                ),
                                                "DataTypeSchemaHeader": (
                                                    "V",
                                                    "i=15741",
                                                    {},
                                                ),
                                                "DatagramConnectionTransport2DataType": (
                                                    "V",
                                                    "i=23909",
                                                    {},
                                                ),
                                                "DatagramConnectionTransportDataType": (
                                                    "V",
                                                    "i=17469",
                                                    {},
                                                ),
                                                "DatagramDataSetReaderTransportDataType": (
                                                    "V",
                                                    "i=23915",
                                                    {},
                                                ),
                                                "DatagramWriterGroupTransport2DataType": (
                                                    "V",
                                                    "i=23912",
                                                    {},
                                                ),
                                                "DatagramWriterGroupTransportDataType": (
                                                    "V",
                                                    "i=21171",
                                                    {},
                                                ),
                                                "DeleteNodesItem": ("V", "i=7734", {}),
                                                "DeleteReferencesItem": (
                                                    "V",
                                                    "i=7737",
                                                    {},
                                                ),
                                                "Deprecated": ("V", "i=15037", {}),
                                                "DiscoveryConfiguration": (
                                                    "V",
                                                    "i=12902",
                                                    {},
                                                ),
                                                "DoubleComplexNumberType": (
                                                    "V",
                                                    "i=12186",
                                                    {},
                                                ),
                                                "DtlsPubSubConnectionDataType": (
                                                    "V",
                                                    "i=18934",
                                                    {},
                                                ),
                                                "EUInformation": ("V", "i=8241", {}),
                                                "ElementOperand": ("V", "i=7938", {}),
                                                "EndpointConfiguration": (
                                                    "V",
                                                    "i=7686",
                                                    {},
                                                ),
                                                "EndpointDataType": (
                                                    "V",
                                                    "i=16570",
                                                    {},
                                                ),
                                                "EndpointDescription": (
                                                    "V",
                                                    "i=7668",
                                                    {},
                                                ),
                                                "EndpointType": ("V", "i=15734", {}),
                                                "EndpointUrlListDataType": (
                                                    "V",
                                                    "i=11959",
                                                    {},
                                                ),
                                                "EnumDefinition": ("V", "i=18187", {}),
                                                "EnumDescription": ("V", "i=15602", {}),
                                                "EnumField": ("V", "i=14870", {}),
                                                "EnumValueType": ("V", "i=7656", {}),
                                                "EphemeralKeyType": (
                                                    "V",
                                                    "i=17550",
                                                    {},
                                                ),
                                                "EventFilter": ("V", "i=8073", {}),
                                                "FieldMetaData": ("V", "i=14852", {}),
                                                "FieldTargetDataType": (
                                                    "V",
                                                    "i=21002",
                                                    {},
                                                ),
                                                "FilterOperand": ("V", "i=7935", {}),
                                                "Frame": ("V", "i=18845", {}),
                                                "HistoryEvent": ("V", "i=8004", {}),
                                                "HistoryEventFieldList": (
                                                    "V",
                                                    "i=8172",
                                                    {},
                                                ),
                                                "HistoryModifiedEvent": (
                                                    "V",
                                                    "i=32826",
                                                    {},
                                                ),
                                                "IdentityMappingRuleType": (
                                                    "V",
                                                    "i=15738",
                                                    {},
                                                ),
                                                "IssuedIdentityToken": (
                                                    "V",
                                                    "i=7683",
                                                    {},
                                                ),
                                                "JsonDataSetReaderMessageDataType": (
                                                    "V",
                                                    "i=15931",
                                                    {},
                                                ),
                                                "JsonDataSetWriterMessageDataType": (
                                                    "V",
                                                    "i=15925",
                                                    {},
                                                ),
                                                "JsonWriterGroupMessageDataType": (
                                                    "V",
                                                    "i=15922",
                                                    {},
                                                ),
                                                "KeyValuePair": ("V", "i=14873", {}),
                                                "LinearConversionDataType": (
                                                    "V",
                                                    "i=32566",
                                                    {},
                                                ),
                                                "LiteralOperand": ("V", "i=7941", {}),
                                                "LldpManagementAddressTxPortType": (
                                                    "V",
                                                    "i=19085",
                                                    {},
                                                ),
                                                "LldpManagementAddressType": (
                                                    "V",
                                                    "i=19088",
                                                    {},
                                                ),
                                                "LldpTlvType": ("V", "i=19097", {}),
                                                "LogRecord": ("V", "i=19380", {}),
                                                "LogRecordsDataType": (
                                                    "V",
                                                    "i=19760",
                                                    {},
                                                ),
                                                "MdnsDiscoveryConfiguration": (
                                                    "V",
                                                    "i=12905",
                                                    {},
                                                ),
                                                "ModelChangeStructureDataType": (
                                                    "V",
                                                    "i=8232",
                                                    {},
                                                ),
                                                "ModificationInfo": (
                                                    "V",
                                                    "i=15018",
                                                    {},
                                                ),
                                                "MonitoringFilter": ("V", "i=8067", {}),
                                                "NameValuePair": ("V", "i=19769", {}),
                                                "NamespaceUri": ("V", "i=7619", {}),
                                                "NetworkAddressDataType": (
                                                    "V",
                                                    "i=21159",
                                                    {},
                                                ),
                                                "NetworkAddressUrlDataType": (
                                                    "V",
                                                    "i=21162",
                                                    {},
                                                ),
                                                "NetworkGroupDataType": (
                                                    "V",
                                                    "i=11962",
                                                    {},
                                                ),
                                                "OptionSet": ("V", "i=12767", {}),
                                                "Orientation": ("V", "i=18839", {}),
                                                "PortableNodeId": ("V", "i=24114", {}),
                                                "PortableQualifiedName": (
                                                    "V",
                                                    "i=24111",
                                                    {},
                                                ),
                                                "PriorityMappingEntryType": (
                                                    "V",
                                                    "i=25240",
                                                    {},
                                                ),
                                                "ProgramDiagnostic2DataType": (
                                                    "V",
                                                    "i=24035",
                                                    {},
                                                ),
                                                "ProgramDiagnosticDataType": (
                                                    "V",
                                                    "i=8247",
                                                    {},
                                                ),
                                                "PubSubConfiguration2DataType": (
                                                    "V",
                                                    "i=23879",
                                                    {},
                                                ),
                                                "PubSubConfigurationDataType": (
                                                    "V",
                                                    "i=21168",
                                                    {},
                                                ),
                                                "PubSubConfigurationRefDataType": (
                                                    "V",
                                                    "i=25539",
                                                    {},
                                                ),
                                                "PubSubConfigurationValueDataType": (
                                                    "V",
                                                    "i=25542",
                                                    {},
                                                ),
                                                "PubSubConnectionDataType": (
                                                    "V",
                                                    "i=15857",
                                                    {},
                                                ),
                                                "PubSubGroupDataType": (
                                                    "V",
                                                    "i=15787",
                                                    {},
                                                ),
                                                "PubSubKeyPushTargetDataType": (
                                                    "V",
                                                    "i=25536",
                                                    {},
                                                ),
                                                "PublishedActionDataType": (
                                                    "V",
                                                    "i=18604",
                                                    {},
                                                ),
                                                "PublishedActionMethodDataType": (
                                                    "V",
                                                    "i=18931",
                                                    {},
                                                ),
                                                "PublishedDataItemsDataType": (
                                                    "V",
                                                    "i=15772",
                                                    {},
                                                ),
                                                "PublishedDataSetCustomSourceDataType": (
                                                    "V",
                                                    "i=25533",
                                                    {},
                                                ),
                                                "PublishedDataSetDataType": (
                                                    "V",
                                                    "i=15766",
                                                    {},
                                                ),
                                                "PublishedDataSetSourceDataType": (
                                                    "V",
                                                    "i=15769",
                                                    {},
                                                ),
                                                "PublishedEventsDataType": (
                                                    "V",
                                                    "i=15775",
                                                    {},
                                                ),
                                                "PublishedVariableDataType": (
                                                    "V",
                                                    "i=14324",
                                                    {},
                                                ),
                                                "QosDataType": ("V", "i=23882", {}),
                                                "QuantityDimension": (
                                                    "V",
                                                    "i=32569",
                                                    {},
                                                ),
                                                "Range": ("V", "i=8238", {}),
                                                "RationalNumber": ("V", "i=18824", {}),
                                                "ReaderGroupDataType": (
                                                    "V",
                                                    "i=21165",
                                                    {},
                                                ),
                                                "ReaderGroupMessageDataType": (
                                                    "V",
                                                    "i=15869",
                                                    {},
                                                ),
                                                "ReaderGroupTransportDataType": (
                                                    "V",
                                                    "i=15866",
                                                    {},
                                                ),
                                                "ReceiveQosDataType": (
                                                    "V",
                                                    "i=23897",
                                                    {},
                                                ),
                                                "ReceiveQosPriorityDataType": (
                                                    "V",
                                                    "i=23900",
                                                    {},
                                                ),
                                                "RedundantServerDataType": (
                                                    "V",
                                                    "i=8208",
                                                    {},
                                                ),
                                                "ReferenceDescriptionDataType": (
                                                    "V",
                                                    "i=32663",
                                                    {},
                                                ),
                                                "ReferenceListEntryDataType": (
                                                    "V",
                                                    "i=32666",
                                                    {},
                                                ),
                                                "RegisteredServer": ("V", "i=7782", {}),
                                                "RelativePath": ("V", "i=12721", {}),
                                                "RelativePathElement": (
                                                    "V",
                                                    "i=12718",
                                                    {},
                                                ),
                                                "RolePermissionType": (
                                                    "V",
                                                    "i=16131",
                                                    {},
                                                ),
                                                "SamplingIntervalDiagnosticsDataType": (
                                                    "V",
                                                    "i=8211",
                                                    {},
                                                ),
                                                "SecurityGroupDataType": (
                                                    "V",
                                                    "i=23876",
                                                    {},
                                                ),
                                                "SecuritySettingsDataType": (
                                                    "V",
                                                    "i=16581",
                                                    {},
                                                ),
                                                "SemanticChangeStructureDataType": (
                                                    "V",
                                                    "i=8235",
                                                    {},
                                                ),
                                                "ServerDiagnosticsSummaryDataType": (
                                                    "V",
                                                    "i=8214",
                                                    {},
                                                ),
                                                "ServerEndpointDataType": (
                                                    "V",
                                                    "i=16578",
                                                    {},
                                                ),
                                                "ServerOnNetwork": ("V", "i=12213", {}),
                                                "ServerStatusDataType": (
                                                    "V",
                                                    "i=8217",
                                                    {},
                                                ),
                                                "ServiceCertificateDataType": (
                                                    "V",
                                                    "i=23732",
                                                    {},
                                                ),
                                                "ServiceCounterDataType": (
                                                    "V",
                                                    "i=8226",
                                                    {},
                                                ),
                                                "SessionDiagnosticsDataType": (
                                                    "V",
                                                    "i=8220",
                                                    {},
                                                ),
                                                "SessionSecurityDiagnosticsDataType": (
                                                    "V",
                                                    "i=8223",
                                                    {},
                                                ),
                                                "SignedSoftwareCertificate": (
                                                    "V",
                                                    "i=7698",
                                                    {},
                                                ),
                                                "SimpleAttributeOperand": (
                                                    "V",
                                                    "i=7947",
                                                    {},
                                                ),
                                                "SimpleTypeDescription": (
                                                    "V",
                                                    "i=15501",
                                                    {},
                                                ),
                                                "SpanContextDataType": (
                                                    "V",
                                                    "i=19763",
                                                    {},
                                                ),
                                                "StandaloneSubscribedDataSetDataType": (
                                                    "V",
                                                    "i=23873",
                                                    {},
                                                ),
                                                "StandaloneSubscribedDataSetRefDataType": (
                                                    "V",
                                                    "i=23870",
                                                    {},
                                                ),
                                                "StatusResult": ("V", "i=7659", {}),
                                                "StructureDefinition": (
                                                    "V",
                                                    "i=18184",
                                                    {},
                                                ),
                                                "StructureDescription": (
                                                    "V",
                                                    "i=15599",
                                                    {},
                                                ),
                                                "StructureField": ("V", "i=18181", {}),
                                                "SubscribedDataSetDataType": (
                                                    "V",
                                                    "i=15883",
                                                    {},
                                                ),
                                                "SubscribedDataSetMirrorDataType": (
                                                    "V",
                                                    "i=15889",
                                                    {},
                                                ),
                                                "SubscriptionDiagnosticsDataType": (
                                                    "V",
                                                    "i=8229",
                                                    {},
                                                ),
                                                "TargetVariablesDataType": (
                                                    "V",
                                                    "i=15886",
                                                    {},
                                                ),
                                                "TimeZoneDataType": ("V", "i=8914", {}),
                                                "TraceContextDataType": (
                                                    "V",
                                                    "i=19766",
                                                    {},
                                                ),
                                                "TransactionErrorType": (
                                                    "V",
                                                    "i=32383",
                                                    {},
                                                ),
                                                "TransmitQosDataType": (
                                                    "V",
                                                    "i=23885",
                                                    {},
                                                ),
                                                "TransmitQosPriorityDataType": (
                                                    "V",
                                                    "i=23888",
                                                    {},
                                                ),
                                                "TrustListDataType": (
                                                    "V",
                                                    "i=12681",
                                                    {},
                                                ),
                                                "UABinaryFileDataType": (
                                                    "V",
                                                    "i=15521",
                                                    {},
                                                ),
                                                "UadpDataSetReaderMessageDataType": (
                                                    "V",
                                                    "i=15919",
                                                    {},
                                                ),
                                                "UadpDataSetWriterMessageDataType": (
                                                    "V",
                                                    "i=15898",
                                                    {},
                                                ),
                                                "UadpWriterGroupMessageDataType": (
                                                    "V",
                                                    "i=15895",
                                                    {},
                                                ),
                                                "Union": ("V", "i=12770", {}),
                                                "UnsignedRationalNumber": (
                                                    "V",
                                                    "i=24117",
                                                    {},
                                                ),
                                                "UserIdentityToken": (
                                                    "V",
                                                    "i=7671",
                                                    {},
                                                ),
                                                "UserManagementDataType": (
                                                    "V",
                                                    "i=24293",
                                                    {},
                                                ),
                                                "UserNameIdentityToken": (
                                                    "V",
                                                    "i=7677",
                                                    {},
                                                ),
                                                "UserTokenPolicy": ("V", "i=7662", {}),
                                                "UserTokenSettingsDataType": (
                                                    "V",
                                                    "i=16584",
                                                    {},
                                                ),
                                                "Vector": ("V", "i=18827", {}),
                                                "WriterGroupDataType": (
                                                    "V",
                                                    "i=21156",
                                                    {},
                                                ),
                                                "WriterGroupMessageDataType": (
                                                    "V",
                                                    "i=15854",
                                                    {},
                                                ),
                                                "WriterGroupTransportDataType": (
                                                    "V",
                                                    "i=15793",
                                                    {},
                                                ),
                                                "X509IdentityToken": (
                                                    "V",
                                                    "i=7680",
                                                    {},
                                                ),
                                                "XVType": ("V", "i=12094", {}),
                                            },
                                        )
                                    },
                                ),
                                "XML Schema": (
                                    "O",
                                    "i=92",
                                    {
                                        "Opc.Ua": (
                                            "V",
                                            "i=8252",
                                            {
                                                "3DCartesianCoordinates": (
                                                    "V",
                                                    "i=19049",
                                                    {},
                                                ),
                                                "3DFrame": ("V", "i=19061", {}),
                                                "3DOrientation": ("V", "i=19055", {}),
                                                "3DVector": ("V", "i=18866", {}),
                                                "ActionMethodDataType": (
                                                    "V",
                                                    "i=18619",
                                                    {},
                                                ),
                                                "ActionTargetDataType": (
                                                    "V",
                                                    "i=18613",
                                                    {},
                                                ),
                                                "AddNodesItem": ("V", "i=8363", {}),
                                                "AddReferencesItem": (
                                                    "V",
                                                    "i=8366",
                                                    {},
                                                ),
                                                "AdditionalParametersType": (
                                                    "V",
                                                    "i=17542",
                                                    {},
                                                ),
                                                "AggregateConfiguration": (
                                                    "V",
                                                    "i=8711",
                                                    {},
                                                ),
                                                "AliasNameDataType": (
                                                    "V",
                                                    "i=23508",
                                                    {},
                                                ),
                                                "Annotation": ("V", "i=8879", {}),
                                                "AnnotationDataType": (
                                                    "V",
                                                    "i=32575",
                                                    {},
                                                ),
                                                "AnonymousIdentityToken": (
                                                    "V",
                                                    "i=8309",
                                                    {},
                                                ),
                                                "ApplicationConfigurationDataType": (
                                                    "V",
                                                    "i=23764",
                                                    {},
                                                ),
                                                "ApplicationDescription": (
                                                    "V",
                                                    "i=8300",
                                                    {},
                                                ),
                                                "ApplicationIdentityDataType": (
                                                    "V",
                                                    "i=16617",
                                                    {},
                                                ),
                                                "Argument": ("V", "i=8285", {}),
                                                "AttributeOperand": ("V", "i=8579", {}),
                                                "AuthorizationServiceConfigurationDataType": (
                                                    "V",
                                                    "i=23773",
                                                    {},
                                                ),
                                                "AxisInformation": ("V", "i=12083", {}),
                                                "BaseConfigurationDataType": (
                                                    "V",
                                                    "i=16597",
                                                    {},
                                                ),
                                                "BaseConfigurationRecordDataType": (
                                                    "V",
                                                    "i=16604",
                                                    {},
                                                ),
                                                "BitFieldDefinition": (
                                                    "V",
                                                    "i=32427",
                                                    {},
                                                ),
                                                "BrokerConnectionTransportDataType": (
                                                    "V",
                                                    "i=15640",
                                                    {},
                                                ),
                                                "BrokerDataSetReaderTransportDataType": (
                                                    "V",
                                                    "i=16147",
                                                    {},
                                                ),
                                                "BrokerDataSetWriterTransportDataType": (
                                                    "V",
                                                    "i=16144",
                                                    {},
                                                ),
                                                "BrokerWriterGroupTransportDataType": (
                                                    "V",
                                                    "i=16125",
                                                    {},
                                                ),
                                                "BuildInfo": ("V", "i=8327", {}),
                                                "CartesianCoordinates": (
                                                    "V",
                                                    "i=18869",
                                                    {},
                                                ),
                                                "CertificateGroupDataType": (
                                                    "V",
                                                    "i=16607",
                                                    {},
                                                ),
                                                "ComplexNumberType": (
                                                    "V",
                                                    "i=12175",
                                                    {},
                                                ),
                                                "ConfigurationUpdateTargetType": (
                                                    "V",
                                                    "i=16610",
                                                    {},
                                                ),
                                                "ConfigurationVersionDataType": (
                                                    "V",
                                                    "i=14832",
                                                    {},
                                                ),
                                                "ConnectionTransportDataType": (
                                                    "V",
                                                    "i=16071",
                                                    {},
                                                ),
                                                "ContentFilter": ("V", "i=8567", {}),
                                                "ContentFilterElement": (
                                                    "V",
                                                    "i=8564",
                                                    {},
                                                ),
                                                "CurrencyUnitType": (
                                                    "V",
                                                    "i=23522",
                                                    {},
                                                ),
                                                "DataSetMetaDataType": (
                                                    "V",
                                                    "i=14805",
                                                    {},
                                                ),
                                                "DataSetReaderDataType": (
                                                    "V",
                                                    "i=16083",
                                                    {},
                                                ),
                                                "DataSetReaderMessageDataType": (
                                                    "V",
                                                    "i=16089",
                                                    {},
                                                ),
                                                "DataSetReaderTransportDataType": (
                                                    "V",
                                                    "i=16086",
                                                    {},
                                                ),
                                                "DataSetWriterDataType": (
                                                    "V",
                                                    "i=16047",
                                                    {},
                                                ),
                                                "DataSetWriterMessageDataType": (
                                                    "V",
                                                    "i=16053",
                                                    {},
                                                ),
                                                "DataSetWriterTransportDataType": (
                                                    "V",
                                                    "i=16050",
                                                    {},
                                                ),
                                                "DataTypeDefinition": (
                                                    "V",
                                                    "i=18166",
                                                    {},
                                                ),
                                                "DataTypeDescription": (
                                                    "V",
                                                    "i=14811",
                                                    {},
                                                ),
                                                "DataTypeSchemaHeader": (
                                                    "V",
                                                    "i=16027",
                                                    {},
                                                ),
                                                "DatagramConnectionTransport2DataType": (
                                                    "V",
                                                    "i=23977",
                                                    {},
                                                ),
                                                "DatagramConnectionTransportDataType": (
                                                    "V",
                                                    "i=17473",
                                                    {},
                                                ),
                                                "DatagramDataSetReaderTransportDataType": (
                                                    "V",
                                                    "i=23983",
                                                    {},
                                                ),
                                                "DatagramWriterGroupTransport2DataType": (
                                                    "V",
                                                    "i=23980",
                                                    {},
                                                ),
                                                "DatagramWriterGroupTransportDataType": (
                                                    "V",
                                                    "i=21195",
                                                    {},
                                                ),
                                                "DeleteNodesItem": ("V", "i=8369", {}),
                                                "DeleteReferencesItem": (
                                                    "V",
                                                    "i=8372",
                                                    {},
                                                ),
                                                "Deprecated": ("V", "i=15039", {}),
                                                "DiscoveryConfiguration": (
                                                    "V",
                                                    "i=12894",
                                                    {},
                                                ),
                                                "DoubleComplexNumberType": (
                                                    "V",
                                                    "i=12178",
                                                    {},
                                                ),
                                                "DtlsPubSubConnectionDataType": (
                                                    "V",
                                                    "i=18942",
                                                    {},
                                                ),
                                                "EUInformation": ("V", "i=8876", {}),
                                                "ElementOperand": ("V", "i=8573", {}),
                                                "EndpointConfiguration": (
                                                    "V",
                                                    "i=8321",
                                                    {},
                                                ),
                                                "EndpointDataType": (
                                                    "V",
                                                    "i=16620",
                                                    {},
                                                ),
                                                "EndpointDescription": (
                                                    "V",
                                                    "i=8303",
                                                    {},
                                                ),
                                                "EndpointType": ("V", "i=16024", {}),
                                                "EndpointUrlListDataType": (
                                                    "V",
                                                    "i=11951",
                                                    {},
                                                ),
                                                "EnumDefinition": ("V", "i=18175", {}),
                                                "EnumDescription": ("V", "i=15594", {}),
                                                "EnumField": ("V", "i=14826", {}),
                                                "EnumValueType": ("V", "i=8291", {}),
                                                "EphemeralKeyType": (
                                                    "V",
                                                    "i=17554",
                                                    {},
                                                ),
                                                "EventFilter": ("V", "i=8708", {}),
                                                "FieldMetaData": ("V", "i=14808", {}),
                                                "FieldTargetDataType": (
                                                    "V",
                                                    "i=14835",
                                                    {},
                                                ),
                                                "FilterOperand": ("V", "i=8570", {}),
                                                "Frame": ("V", "i=19058", {}),
                                                "HistoryEvent": ("V", "i=8639", {}),
                                                "HistoryEventFieldList": (
                                                    "V",
                                                    "i=8807",
                                                    {},
                                                ),
                                                "HistoryModifiedEvent": (
                                                    "V",
                                                    "i=32830",
                                                    {},
                                                ),
                                                "IdentityMappingRuleType": (
                                                    "V",
                                                    "i=15730",
                                                    {},
                                                ),
                                                "IssuedIdentityToken": (
                                                    "V",
                                                    "i=8318",
                                                    {},
                                                ),
                                                "JsonDataSetReaderMessageDataType": (
                                                    "V",
                                                    "i=16119",
                                                    {},
                                                ),
                                                "JsonDataSetWriterMessageDataType": (
                                                    "V",
                                                    "i=16116",
                                                    {},
                                                ),
                                                "JsonWriterGroupMessageDataType": (
                                                    "V",
                                                    "i=16113",
                                                    {},
                                                ),
                                                "KeyValuePair": ("V", "i=14829", {}),
                                                "LinearConversionDataType": (
                                                    "V",
                                                    "i=32578",
                                                    {},
                                                ),
                                                "LiteralOperand": ("V", "i=8576", {}),
                                                "LldpManagementAddressTxPortType": (
                                                    "V",
                                                    "i=19103",
                                                    {},
                                                ),
                                                "LldpManagementAddressType": (
                                                    "V",
                                                    "i=19106",
                                                    {},
                                                ),
                                                "LldpTlvType": ("V", "i=19291", {}),
                                                "LogRecord": ("V", "i=19384", {}),
                                                "LogRecordsDataType": (
                                                    "V",
                                                    "i=19790",
                                                    {},
                                                ),
                                                "MdnsDiscoveryConfiguration": (
                                                    "V",
                                                    "i=12897",
                                                    {},
                                                ),
                                                "ModelChangeStructureDataType": (
                                                    "V",
                                                    "i=8867",
                                                    {},
                                                ),
                                                "ModificationInfo": (
                                                    "V",
                                                    "i=15021",
                                                    {},
                                                ),
                                                "MonitoringFilter": ("V", "i=8702", {}),
                                                "NameValuePair": ("V", "i=19799", {}),
                                                "NamespaceUri": ("V", "i=8254", {}),
                                                "NetworkAddressDataType": (
                                                    "V",
                                                    "i=21183",
                                                    {},
                                                ),
                                                "NetworkAddressUrlDataType": (
                                                    "V",
                                                    "i=21186",
                                                    {},
                                                ),
                                                "NetworkGroupDataType": (
                                                    "V",
                                                    "i=11954",
                                                    {},
                                                ),
                                                "OptionSet": ("V", "i=12759", {}),
                                                "Orientation": ("V", "i=19052", {}),
                                                "PortableNodeId": ("V", "i=24126", {}),
                                                "PortableQualifiedName": (
                                                    "V",
                                                    "i=24123",
                                                    {},
                                                ),
                                                "PriorityMappingEntryType": (
                                                    "V",
                                                    "i=25244",
                                                    {},
                                                ),
                                                "ProgramDiagnostic2DataType": (
                                                    "V",
                                                    "i=24039",
                                                    {},
                                                ),
                                                "ProgramDiagnosticDataType": (
                                                    "V",
                                                    "i=8882",
                                                    {},
                                                ),
                                                "PubSubConfiguration2DataType": (
                                                    "V",
                                                    "i=23947",
                                                    {},
                                                ),
                                                "PubSubConfigurationDataType": (
                                                    "V",
                                                    "i=21192",
                                                    {},
                                                ),
                                                "PubSubConfigurationRefDataType": (
                                                    "V",
                                                    "i=25555",
                                                    {},
                                                ),
                                                "PubSubConfigurationValueDataType": (
                                                    "V",
                                                    "i=25558",
                                                    {},
                                                ),
                                                "PubSubConnectionDataType": (
                                                    "V",
                                                    "i=16068",
                                                    {},
                                                ),
                                                "PubSubGroupDataType": (
                                                    "V",
                                                    "i=16056",
                                                    {},
                                                ),
                                                "PubSubKeyPushTargetDataType": (
                                                    "V",
                                                    "i=25552",
                                                    {},
                                                ),
                                                "PublishedActionDataType": (
                                                    "V",
                                                    "i=18616",
                                                    {},
                                                ),
                                                "PublishedActionMethodDataType": (
                                                    "V",
                                                    "i=18939",
                                                    {},
                                                ),
                                                "PublishedDataItemsDataType": (
                                                    "V",
                                                    "i=16037",
                                                    {},
                                                ),
                                                "PublishedDataSetCustomSourceDataType": (
                                                    "V",
                                                    "i=25549",
                                                    {},
                                                ),
                                                "PublishedDataSetDataType": (
                                                    "V",
                                                    "i=16030",
                                                    {},
                                                ),
                                                "PublishedDataSetSourceDataType": (
                                                    "V",
                                                    "i=16033",
                                                    {},
                                                ),
                                                "PublishedEventsDataType": (
                                                    "V",
                                                    "i=16040",
                                                    {},
                                                ),
                                                "PublishedVariableDataType": (
                                                    "V",
                                                    "i=14320",
                                                    {},
                                                ),
                                                "QosDataType": ("V", "i=23950", {}),
                                                "QuantityDimension": (
                                                    "V",
                                                    "i=32581",
                                                    {},
                                                ),
                                                "Range": ("V", "i=8873", {}),
                                                "RationalNumber": ("V", "i=18860", {}),
                                                "ReaderGroupDataType": (
                                                    "V",
                                                    "i=21189",
                                                    {},
                                                ),
                                                "ReaderGroupMessageDataType": (
                                                    "V",
                                                    "i=16080",
                                                    {},
                                                ),
                                                "ReaderGroupTransportDataType": (
                                                    "V",
                                                    "i=16077",
                                                    {},
                                                ),
                                                "ReceiveQosDataType": (
                                                    "V",
                                                    "i=23965",
                                                    {},
                                                ),
                                                "ReceiveQosPriorityDataType": (
                                                    "V",
                                                    "i=23968",
                                                    {},
                                                ),
                                                "RedundantServerDataType": (
                                                    "V",
                                                    "i=8843",
                                                    {},
                                                ),
                                                "ReferenceDescriptionDataType": (
                                                    "V",
                                                    "i=32671",
                                                    {},
                                                ),
                                                "ReferenceListEntryDataType": (
                                                    "V",
                                                    "i=32674",
                                                    {},
                                                ),
                                                "RegisteredServer": ("V", "i=8417", {}),
                                                "RelativePath": ("V", "i=12715", {}),
                                                "RelativePathElement": (
                                                    "V",
                                                    "i=12712",
                                                    {},
                                                ),
                                                "RolePermissionType": (
                                                    "V",
                                                    "i=16127",
                                                    {},
                                                ),
                                                "SamplingIntervalDiagnosticsDataType": (
                                                    "V",
                                                    "i=8846",
                                                    {},
                                                ),
                                                "SecurityGroupDataType": (
                                                    "V",
                                                    "i=23944",
                                                    {},
                                                ),
                                                "SecuritySettingsDataType": (
                                                    "V",
                                                    "i=16626",
                                                    {},
                                                ),
                                                "SemanticChangeStructureDataType": (
                                                    "V",
                                                    "i=8870",
                                                    {},
                                                ),
                                                "ServerDiagnosticsSummaryDataType": (
                                                    "V",
                                                    "i=8849",
                                                    {},
                                                ),
                                                "ServerEndpointDataType": (
                                                    "V",
                                                    "i=16623",
                                                    {},
                                                ),
                                                "ServerOnNetwork": ("V", "i=12201", {}),
                                                "ServerStatusDataType": (
                                                    "V",
                                                    "i=8852",
                                                    {},
                                                ),
                                                "ServiceCertificateDataType": (
                                                    "V",
                                                    "i=23736",
                                                    {},
                                                ),
                                                "ServiceCounterDataType": (
                                                    "V",
                                                    "i=8861",
                                                    {},
                                                ),
                                                "SessionDiagnosticsDataType": (
                                                    "V",
                                                    "i=8855",
                                                    {},
                                                ),
                                                "SessionSecurityDiagnosticsDataType": (
                                                    "V",
                                                    "i=8858",
                                                    {},
                                                ),
                                                "SignedSoftwareCertificate": (
                                                    "V",
                                                    "i=8333",
                                                    {},
                                                ),
                                                "SimpleAttributeOperand": (
                                                    "V",
                                                    "i=8582",
                                                    {},
                                                ),
                                                "SimpleTypeDescription": (
                                                    "V",
                                                    "i=15585",
                                                    {},
                                                ),
                                                "SpanContextDataType": (
                                                    "V",
                                                    "i=19793",
                                                    {},
                                                ),
                                                "StandaloneSubscribedDataSetDataType": (
                                                    "V",
                                                    "i=23941",
                                                    {},
                                                ),
                                                "StandaloneSubscribedDataSetRefDataType": (
                                                    "V",
                                                    "i=23938",
                                                    {},
                                                ),
                                                "StatusResult": ("V", "i=8294", {}),
                                                "StructureDefinition": (
                                                    "V",
                                                    "i=18172",
                                                    {},
                                                ),
                                                "StructureDescription": (
                                                    "V",
                                                    "i=15591",
                                                    {},
                                                ),
                                                "StructureField": ("V", "i=18169", {}),
                                                "SubscribedDataSetDataType": (
                                                    "V",
                                                    "i=16092",
                                                    {},
                                                ),
                                                "SubscribedDataSetMirrorDataType": (
                                                    "V",
                                                    "i=16098",
                                                    {},
                                                ),
                                                "SubscriptionDiagnosticsDataType": (
                                                    "V",
                                                    "i=8864",
                                                    {},
                                                ),
                                                "TargetVariablesDataType": (
                                                    "V",
                                                    "i=16095",
                                                    {},
                                                ),
                                                "TimeZoneDataType": ("V", "i=8918", {}),
                                                "TraceContextDataType": (
                                                    "V",
                                                    "i=19796",
                                                    {},
                                                ),
                                                "TransactionErrorType": (
                                                    "V",
                                                    "i=32387",
                                                    {},
                                                ),
                                                "TransmitQosDataType": (
                                                    "V",
                                                    "i=23953",
                                                    {},
                                                ),
                                                "TransmitQosPriorityDataType": (
                                                    "V",
                                                    "i=23956",
                                                    {},
                                                ),
                                                "TrustListDataType": (
                                                    "V",
                                                    "i=12677",
                                                    {},
                                                ),
                                                "UABinaryFileDataType": (
                                                    "V",
                                                    "i=15588",
                                                    {},
                                                ),
                                                "UadpDataSetReaderMessageDataType": (
                                                    "V",
                                                    "i=16110",
                                                    {},
                                                ),
                                                "UadpDataSetWriterMessageDataType": (
                                                    "V",
                                                    "i=16107",
                                                    {},
                                                ),
                                                "UadpWriterGroupMessageDataType": (
                                                    "V",
                                                    "i=16104",
                                                    {},
                                                ),
                                                "Union": ("V", "i=12762", {}),
                                                "UnsignedRationalNumber": (
                                                    "V",
                                                    "i=24129",
                                                    {},
                                                ),
                                                "UserIdentityToken": (
                                                    "V",
                                                    "i=8306",
                                                    {},
                                                ),
                                                "UserManagementDataType": (
                                                    "V",
                                                    "i=24297",
                                                    {},
                                                ),
                                                "UserNameIdentityToken": (
                                                    "V",
                                                    "i=8312",
                                                    {},
                                                ),
                                                "UserTokenPolicy": ("V", "i=8297", {}),
                                                "UserTokenSettingsDataType": (
                                                    "V",
                                                    "i=16629",
                                                    {},
                                                ),
                                                "Vector": ("V", "i=18863", {}),
                                                "WriterGroupDataType": (
                                                    "V",
                                                    "i=21180",
                                                    {},
                                                ),
                                                "WriterGroupMessageDataType": (
                                                    "V",
                                                    "i=16065",
                                                    {},
                                                ),
                                                "WriterGroupTransportDataType": (
                                                    "V",
                                                    "i=16062",
                                                    {},
                                                ),
                                                "X509IdentityToken": (
                                                    "V",
                                                    "i=8315",
                                                    {},
                                                ),
                                                "XVType": ("V", "i=12086", {}),
                                            },
                                        )
                                    },
                                ),
                            },
                        ),
                        "EventTypes": ("O", "i=3048", {}),
                        "InterfaceTypes": ("O", "i=17708", {}),
                        "ObjectTypes": ("O", "i=88", {}),
                        "ReferenceTypes": ("O", "i=91", {}),
                        "VariableTypes": ("O", "i=89", {}),
                    },
                ),
                "Views": ("O", "i=87", {}),
            },
        ),
        "ServerNetworkGroups": ("V", "i=14415", {}),
        "ServerUriArray": ("V", "i=11314", {}),
        "StandardDeviationPopulation": ("O", "i=11427", {}),
        "StandardDeviationSample": ("O", "i=11426", {}),
        "Start": ("O", "i=2357", {}),
        "StartBound": ("O", "i=11505", {}),
        "TimeAverage": ("O", "i=2343", {}),
        "TimeAverage2": ("O", "i=11285", {}),
        "Total": ("O", "i=2344", {}),
        "Total2": ("O", "i=11304", {}),
        "ValueAsText": ("V", "i=11433", {}),
        "VariancePopulation": ("O", "i=11429", {}),
        "VarianceSample": ("O", "i=11428", {}),
        "ViewVersion": ("V", "i=12170", {}),
        "WorstQuality": ("O", "i=2364", {}),
        "WorstQuality2": ("O", "i=11292", {}),
    },
    "objtypes": {
        "BaseObjectType": (
            "OT",
            "i=58",
            {
                "AggregateConfigurationType": (
                    "OT",
                    "i=11187",
                    {
                        "PercentDataBad": ("V", "i=11189", {}),
                        "PercentDataGood": ("V", "i=11190", {}),
                        "TreatUncertainAsBad": ("V", "i=11188", {}),
                        "UseSlopedExtrapolation": ("V", "i=11191", {}),
                    },
                ),
                "AggregateFunctionType": ("OT", "i=2340", {}),
                "AlarmMetricsType": (
                    "OT",
                    "i=17279",
                    {
                        "AlarmCount": ("V", "i=17280", {}),
                        "AverageAlarmRate": (
                            "V",
                            "i=17288",
                            {"Rate": ("V", "i=17289", {})},
                        ),
                        "CurrentAlarmRate": (
                            "V",
                            "i=17284",
                            {"Rate": ("V", "i=17285", {})},
                        ),
                        "MaximumActiveState": ("V", "i=17281", {}),
                        "MaximumAlarmRate": (
                            "V",
                            "i=17286",
                            {"Rate": ("V", "i=17287", {})},
                        ),
                        "MaximumReAlarmCount": ("V", "i=17283", {}),
                        "MaximumUnAck": ("V", "i=17282", {}),
                        "Reset": ("M", "i=18666", {}),
                        "StartTime": ("V", "i=17991", {}),
                    },
                ),
                "AliasNameType": ("OT", "i=23455", {}),
                "AuthorizationServiceConfigurationType": (
                    "OT",
                    "i=17852",
                    {
                        "IssuerEndpointUrl": ("V", "i=18073", {}),
                        "ServiceCertificate": ("V", "i=17860", {}),
                        "ServiceUri": ("V", "i=18072", {}),
                    },
                ),
                "BaseConditionClassType": (
                    "OT",
                    "i=11163",
                    {
                        "HighlyManagedAlarmConditionClassType": ("OT", "i=17219", {}),
                        "LogEntryConditionClassType": ("OT", "i=19370", {}),
                        "MaintenanceConditionClassType": ("OT", "i=11165", {}),
                        "ProcessConditionClassType": ("OT", "i=11164", {}),
                        "SafetyConditionClassType": ("OT", "i=17218", {}),
                        "StatisticalConditionClassType": ("OT", "i=18665", {}),
                        "SystemConditionClassType": ("OT", "i=11166", {}),
                        "TestingConditionClassType": ("OT", "i=17221", {}),
                        "TrainingConditionClassType": ("OT", "i=17220", {}),
                    },
                ),
                "BaseEventType": (
                    "OT",
                    "i=2041",
                    {
                        "AuditEventType": (
                            "OT",
                            "i=2052",
                            {
                                "ActionTimeStamp": ("V", "i=2053", {}),
                                "AuditClientEventType": (
                                    "OT",
                                    "i=23606",
                                    {
                                        "AuditClientUpdateMethodResultEventType": (
                                            "OT",
                                            "i=23926",
                                            {
                                                "InputArguments": ("V", "i=23999", {}),
                                                "MethodId": ("V", "i=23995", {}),
                                                "ObjectId": ("V", "i=23994", {}),
                                                "OutputArguments": ("V", "i=25684", {}),
                                                "StatusCodeId": ("V", "i=23998", {}),
                                            },
                                        ),
                                        "ServerUri": ("V", "i=23908", {}),
                                    },
                                ),
                                "AuditHistoryBulkInsertEventType": (
                                    "OT",
                                    "i=32803",
                                    {
                                        "EndTime": ("V", "i=32823", {}),
                                        "StartTime": ("V", "i=32822", {}),
                                        "UpdatedNode": ("V", "i=32821", {}),
                                    },
                                ),
                                "AuditHistoryConfigurationChangeEventType": (
                                    "OT",
                                    "i=32758",
                                    {},
                                ),
                                "AuditNodeManagementEventType": (
                                    "OT",
                                    "i=2090",
                                    {
                                        "AuditAddNodesEventType": (
                                            "OT",
                                            "i=2091",
                                            {"NodesToAdd": ("V", "i=2092", {})},
                                        ),
                                        "AuditAddReferencesEventType": (
                                            "OT",
                                            "i=2095",
                                            {"ReferencesToAdd": ("V", "i=2096", {})},
                                        ),
                                        "AuditDeleteNodesEventType": (
                                            "OT",
                                            "i=2093",
                                            {"NodesToDelete": ("V", "i=2094", {})},
                                        ),
                                        "AuditDeleteReferencesEventType": (
                                            "OT",
                                            "i=2097",
                                            {"ReferencesToDelete": ("V", "i=2098", {})},
                                        ),
                                    },
                                ),
                                "AuditSecurityEventType": (
                                    "OT",
                                    "i=2058",
                                    {
                                        "AuditCertificateEventType": (
                                            "OT",
                                            "i=2080",
                                            {
                                                "AuditCertificateDataMismatchEventType": (
                                                    "OT",
                                                    "i=2082",
                                                    {
                                                        "InvalidHostname": (
                                                            "V",
                                                            "i=2083",
                                                            {},
                                                        ),
                                                        "InvalidUri": (
                                                            "V",
                                                            "i=2084",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "AuditCertificateExpiredEventType": (
                                                    "OT",
                                                    "i=2085",
                                                    {},
                                                ),
                                                "AuditCertificateInvalidEventType": (
                                                    "OT",
                                                    "i=2086",
                                                    {},
                                                ),
                                                "AuditCertificateMismatchEventType": (
                                                    "OT",
                                                    "i=2089",
                                                    {},
                                                ),
                                                "AuditCertificateRevokedEventType": (
                                                    "OT",
                                                    "i=2088",
                                                    {},
                                                ),
                                                "AuditCertificateUntrustedEventType": (
                                                    "OT",
                                                    "i=2087",
                                                    {},
                                                ),
                                                "Certificate": ("V", "i=2081", {}),
                                            },
                                        ),
                                        "AuditChannelEventType": (
                                            "OT",
                                            "i=2059",
                                            {
                                                "AuditOpenSecureChannelEventType": (
                                                    "OT",
                                                    "i=2060",
                                                    {
                                                        "CertificateErrorEventId": (
                                                            "V",
                                                            "i=24135",
                                                            {},
                                                        ),
                                                        "ClientCertificate": (
                                                            "V",
                                                            "i=2061",
                                                            {},
                                                        ),
                                                        "ClientCertificateThumbprint": (
                                                            "V",
                                                            "i=2746",
                                                            {},
                                                        ),
                                                        "RequestType": (
                                                            "V",
                                                            "i=2062",
                                                            {},
                                                        ),
                                                        "RequestedLifetime": (
                                                            "V",
                                                            "i=2066",
                                                            {},
                                                        ),
                                                        "SecurityMode": (
                                                            "V",
                                                            "i=2065",
                                                            {},
                                                        ),
                                                        "SecurityPolicyUri": (
                                                            "V",
                                                            "i=2063",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "SecureChannelId": ("V", "i=2745", {}),
                                            },
                                        ),
                                        "AuditSessionEventType": (
                                            "OT",
                                            "i=2069",
                                            {
                                                "AuditActivateSessionEventType": (
                                                    "OT",
                                                    "i=2075",
                                                    {
                                                        "ClientSoftwareCertificates": (
                                                            "V",
                                                            "i=2076",
                                                            {},
                                                        ),
                                                        "CurrentRoleIds": (
                                                            "V",
                                                            "i=19304",
                                                            {},
                                                        ),
                                                        "SecureChannelId": (
                                                            "V",
                                                            "i=11485",
                                                            {},
                                                        ),
                                                        "UserIdentityToken": (
                                                            "V",
                                                            "i=2077",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "AuditCancelEventType": (
                                                    "OT",
                                                    "i=2078",
                                                    {
                                                        "RequestHandle": (
                                                            "V",
                                                            "i=2079",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "AuditCreateSessionEventType": (
                                                    "OT",
                                                    "i=2071",
                                                    {
                                                        "AuditUrlMismatchEventType": (
                                                            "OT",
                                                            "i=2748",
                                                            {
                                                                "EndpointUrl": (
                                                                    "V",
                                                                    "i=2749",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "ClientCertificate": (
                                                            "V",
                                                            "i=2073",
                                                            {},
                                                        ),
                                                        "ClientCertificateThumbprint": (
                                                            "V",
                                                            "i=2747",
                                                            {},
                                                        ),
                                                        "RevisedSessionTimeout": (
                                                            "V",
                                                            "i=2074",
                                                            {},
                                                        ),
                                                        "SecureChannelId": (
                                                            "V",
                                                            "i=2072",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "SessionId": ("V", "i=2070", {}),
                                            },
                                        ),
                                        "StatusCodeId": ("V", "i=17615", {}),
                                    },
                                ),
                                "AuditUpdateEventType": (
                                    "OT",
                                    "i=2099",
                                    {
                                        "AuditHistoryUpdateEventType": (
                                            "OT",
                                            "i=2104",
                                            {
                                                "AuditHistoryAnnotationUpdateEventType": (
                                                    "OT",
                                                    "i=19095",
                                                    {
                                                        "NewValues": (
                                                            "V",
                                                            "i=19294",
                                                            {},
                                                        ),
                                                        "OldValues": (
                                                            "V",
                                                            "i=19295",
                                                            {},
                                                        ),
                                                        "PerformInsertReplace": (
                                                            "V",
                                                            "i=19293",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "AuditHistoryDeleteEventType": (
                                                    "OT",
                                                    "i=3012",
                                                    {
                                                        "AuditHistoryAtTimeDeleteEventType": (
                                                            "OT",
                                                            "i=3019",
                                                            {
                                                                "OldValues": (
                                                                    "V",
                                                                    "i=3021",
                                                                    {},
                                                                ),
                                                                "ReqTimes": (
                                                                    "V",
                                                                    "i=3020",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "AuditHistoryEventDeleteEventType": (
                                                            "OT",
                                                            "i=3022",
                                                            {
                                                                "EventIds": (
                                                                    "V",
                                                                    "i=3023",
                                                                    {},
                                                                ),
                                                                "OldValues": (
                                                                    "V",
                                                                    "i=3024",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "AuditHistoryRawModifyDeleteEventType": (
                                                            "OT",
                                                            "i=3014",
                                                            {
                                                                "EndTime": (
                                                                    "V",
                                                                    "i=3017",
                                                                    {},
                                                                ),
                                                                "IsDeleteModified": (
                                                                    "V",
                                                                    "i=3015",
                                                                    {},
                                                                ),
                                                                "OldValues": (
                                                                    "V",
                                                                    "i=3034",
                                                                    {},
                                                                ),
                                                                "StartTime": (
                                                                    "V",
                                                                    "i=3016",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "UpdatedNode": (
                                                            "V",
                                                            "i=3027",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "AuditHistoryEventUpdateEventType": (
                                                    "OT",
                                                    "i=2999",
                                                    {
                                                        "Filter": ("V", "i=3003", {}),
                                                        "NewValues": (
                                                            "V",
                                                            "i=3029",
                                                            {},
                                                        ),
                                                        "OldValues": (
                                                            "V",
                                                            "i=3030",
                                                            {},
                                                        ),
                                                        "PerformInsertReplace": (
                                                            "V",
                                                            "i=3028",
                                                            {},
                                                        ),
                                                        "UpdatedNode": (
                                                            "V",
                                                            "i=3025",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "AuditHistoryValueUpdateEventType": (
                                                    "OT",
                                                    "i=3006",
                                                    {
                                                        "NewValues": (
                                                            "V",
                                                            "i=3032",
                                                            {},
                                                        ),
                                                        "OldValues": (
                                                            "V",
                                                            "i=3033",
                                                            {},
                                                        ),
                                                        "PerformInsertReplace": (
                                                            "V",
                                                            "i=3031",
                                                            {},
                                                        ),
                                                        "UpdatedNode": (
                                                            "V",
                                                            "i=3026",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "ParameterDataTypeId": (
                                                    "V",
                                                    "i=2751",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "AuditWriteUpdateEventType": (
                                            "OT",
                                            "i=2100",
                                            {
                                                "AttributeId": ("V", "i=2750", {}),
                                                "IndexRange": ("V", "i=2101", {}),
                                                "NewValue": ("V", "i=2103", {}),
                                                "OldValue": ("V", "i=2102", {}),
                                            },
                                        ),
                                    },
                                ),
                                "AuditUpdateMethodEventType": (
                                    "OT",
                                    "i=2127",
                                    {
                                        "AuditConditionEventType": (
                                            "OT",
                                            "i=2790",
                                            {
                                                "AuditConditionAcknowledgeEventType": (
                                                    "OT",
                                                    "i=8944",
                                                    {
                                                        "Comment": ("V", "i=11853", {}),
                                                        "ConditionEventId": (
                                                            "V",
                                                            "i=17223",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "AuditConditionCommentEventType": (
                                                    "OT",
                                                    "i=2829",
                                                    {
                                                        "Comment": ("V", "i=11851", {}),
                                                        "ConditionEventId": (
                                                            "V",
                                                            "i=17222",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "AuditConditionConfirmEventType": (
                                                    "OT",
                                                    "i=8961",
                                                    {
                                                        "Comment": ("V", "i=11854", {}),
                                                        "ConditionEventId": (
                                                            "V",
                                                            "i=17224",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "AuditConditionEnableEventType": (
                                                    "OT",
                                                    "i=2803",
                                                    {},
                                                ),
                                                "AuditConditionOutOfServiceEventType": (
                                                    "OT",
                                                    "i=17259",
                                                    {},
                                                ),
                                                "AuditConditionResetEventType": (
                                                    "OT",
                                                    "i=15013",
                                                    {},
                                                ),
                                                "AuditConditionRespondEventType": (
                                                    "OT",
                                                    "i=8927",
                                                    {
                                                        "SelectedResponse": (
                                                            "V",
                                                            "i=11852",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "AuditConditionShelvingEventType": (
                                                    "OT",
                                                    "i=11093",
                                                    {
                                                        "ShelvingTime": (
                                                            "V",
                                                            "i=11855",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "AuditConditionSilenceEventType": (
                                                    "OT",
                                                    "i=17242",
                                                    {},
                                                ),
                                                "AuditConditionSuppressionEventType": (
                                                    "OT",
                                                    "i=17225",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "AuditUpdateStateEventType": (
                                            "OT",
                                            "i=2315",
                                            {
                                                "AuditProgramTransitionEventType": (
                                                    "OT",
                                                    "i=11856",
                                                    {
                                                        "TransitionNumber": (
                                                            "V",
                                                            "i=11875",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "NewStateId": ("V", "i=2778", {}),
                                                "OldStateId": ("V", "i=2777", {}),
                                                "ProgramTransitionAuditEventType": (
                                                    "OT",
                                                    "i=3806",
                                                    {
                                                        "Transition": (
                                                            "V",
                                                            "i=3825",
                                                            {"Id": ("V", "i=3826", {})},
                                                        )
                                                    },
                                                ),
                                            },
                                        ),
                                        "CertificateUpdateRequestedAuditEventType": (
                                            "OT",
                                            "i=32306",
                                            {},
                                        ),
                                        "CertificateUpdatedAuditEventType": (
                                            "OT",
                                            "i=12620",
                                            {
                                                "CertificateGroup": (
                                                    "V",
                                                    "i=13735",
                                                    {},
                                                ),
                                                "CertificateType": ("V", "i=13736", {}),
                                            },
                                        ),
                                        "InputArguments": ("V", "i=2129", {}),
                                        "KeyCredentialAuditEventType": (
                                            "OT",
                                            "i=18011",
                                            {
                                                "KeyCredentialDeletedAuditEventType": (
                                                    "OT",
                                                    "i=18047",
                                                    {
                                                        "ResourceUri": (
                                                            "V",
                                                            "i=18064",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "KeyCredentialUpdatedAuditEventType": (
                                                    "OT",
                                                    "i=18029",
                                                    {},
                                                ),
                                                "ResourceUri": ("V", "i=18028", {}),
                                            },
                                        ),
                                        "MethodId": ("V", "i=2128", {}),
                                        "OutputArguments": ("V", "i=19306", {}),
                                        "RoleMappingRuleChangedAuditEventType": (
                                            "OT",
                                            "i=17641",
                                            {},
                                        ),
                                        "StatusCodeId": ("V", "i=19305", {}),
                                        "TrustListUpdateRequestedAuditEventType": (
                                            "OT",
                                            "i=32260",
                                            {},
                                        ),
                                        "TrustListUpdatedAuditEventType": (
                                            "OT",
                                            "i=12561",
                                            {"TrustListId": ("V", "i=32281", {})},
                                        ),
                                    },
                                ),
                                "ClientApplicationUri": ("V", "i=19811", {}),
                                "ClientAuditEntryId": ("V", "i=2056", {}),
                                "ClientUserId": ("V", "i=2057", {}),
                                "ConfigurationUpdatedAuditEventType": (
                                    "OT",
                                    "i=15541",
                                    {
                                        "NewVersion": ("V", "i=15543", {}),
                                        "OldVersion": ("V", "i=15542", {}),
                                    },
                                ),
                                "ServerId": ("V", "i=2055", {}),
                                "Status": ("V", "i=2054", {}),
                            },
                        ),
                        "BaseLogEventType": (
                            "OT",
                            "i=19362",
                            {
                                "ConditionClassId": ("V", "i=19363", {}),
                                "ConditionClassName": ("V", "i=19364", {}),
                                "ErrorCode": ("V", "i=19365", {}),
                                "ErrorCodeNode": ("V", "i=19366", {}),
                            },
                        ),
                        "BaseModelChangeEventType": (
                            "OT",
                            "i=2132",
                            {
                                "GeneralModelChangeEventType": (
                                    "OT",
                                    "i=2133",
                                    {"Changes": ("V", "i=2134", {})},
                                )
                            },
                        ),
                        "ConditionClassId": ("V", "i=31771", {}),
                        "ConditionClassName": ("V", "i=31772", {}),
                        "ConditionSubClassId": ("V", "i=31773", {}),
                        "ConditionSubClassName": ("V", "i=31774", {}),
                        "ConditionType": (
                            "OT",
                            "i=2782",
                            {
                                "AcknowledgeableConditionType": (
                                    "OT",
                                    "i=2881",
                                    {
                                        "AckedState": (
                                            "V",
                                            "i=9093",
                                            {
                                                "FalseState": ("V", "i=9101", {}),
                                                "Id": ("V", "i=9094", {}),
                                                "TransitionTime": ("V", "i=9098", {}),
                                                "TrueState": ("V", "i=9100", {}),
                                            },
                                        ),
                                        "Acknowledge": (
                                            "M",
                                            "i=9111",
                                            {"InputArguments": ("V", "i=9112", {})},
                                        ),
                                        "AlarmConditionType": (
                                            "OT",
                                            "i=2915",
                                            {
                                                "ActiveState": (
                                                    "V",
                                                    "i=9160",
                                                    {
                                                        "EffectiveDisplayName": (
                                                            "V",
                                                            "i=9164",
                                                            {},
                                                        ),
                                                        "EffectiveTransitionTime": (
                                                            "V",
                                                            "i=9166",
                                                            {},
                                                        ),
                                                        "FalseState": (
                                                            "V",
                                                            "i=9168",
                                                            {},
                                                        ),
                                                        "Id": ("V", "i=9161", {}),
                                                        "TransitionTime": (
                                                            "V",
                                                            "i=9165",
                                                            {},
                                                        ),
                                                        "TrueState": (
                                                            "V",
                                                            "i=9167",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "AudibleEnabled": ("V", "i=16389", {}),
                                                "AudibleSound": ("V", "i=16390", {}),
                                                "DiscrepancyAlarmType": (
                                                    "OT",
                                                    "i=17080",
                                                    {
                                                        "ExpectedTime": (
                                                            "V",
                                                            "i=17216",
                                                            {},
                                                        ),
                                                        "TargetValueNode": (
                                                            "V",
                                                            "i=17215",
                                                            {},
                                                        ),
                                                        "Tolerance": (
                                                            "V",
                                                            "i=17217",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "DiscreteAlarmType": (
                                                    "OT",
                                                    "i=10523",
                                                    {
                                                        "OffNormalAlarmType": (
                                                            "OT",
                                                            "i=10637",
                                                            {
                                                                "InstrumentDiagnosticAlarmType": (
                                                                    "OT",
                                                                    "i=18347",
                                                                    {},
                                                                ),
                                                                "NormalState": (
                                                                    "V",
                                                                    "i=11158",
                                                                    {},
                                                                ),
                                                                "SystemDiagnosticAlarmType": (
                                                                    "OT",
                                                                    "i=18496",
                                                                    {},
                                                                ),
                                                                "SystemOffNormalAlarmType": (
                                                                    "OT",
                                                                    "i=11753",
                                                                    {
                                                                        "CertificateExpirationAlarmType": (
                                                                            "OT",
                                                                            "i=13225",
                                                                            {
                                                                                "Certificate": (
                                                                                    "V",
                                                                                    "i=13327",
                                                                                    {},
                                                                                ),
                                                                                "CertificateType": (
                                                                                    "V",
                                                                                    "i=13326",
                                                                                    {},
                                                                                ),
                                                                                "ExpirationDate": (
                                                                                    "V",
                                                                                    "i=13325",
                                                                                    {},
                                                                                ),
                                                                                "ExpirationLimit": (
                                                                                    "V",
                                                                                    "i=14900",
                                                                                    {},
                                                                                ),
                                                                            },
                                                                        ),
                                                                        "TrustListOutOfDateAlarmType": (
                                                                            "OT",
                                                                            "i=19297",
                                                                            {
                                                                                "LastUpdateTime": (
                                                                                    "V",
                                                                                    "i=19447",
                                                                                    {},
                                                                                ),
                                                                                "TrustListId": (
                                                                                    "V",
                                                                                    "i=19446",
                                                                                    {},
                                                                                ),
                                                                                "UpdateFrequency": (
                                                                                    "V",
                                                                                    "i=19448",
                                                                                    {},
                                                                                ),
                                                                            },
                                                                        ),
                                                                    },
                                                                ),
                                                                "TripAlarmType": (
                                                                    "OT",
                                                                    "i=10751",
                                                                    {},
                                                                ),
                                                            },
                                                        )
                                                    },
                                                ),
                                                "EnabledState": (
                                                    "V",
                                                    "i=9118",
                                                    {"Id": ("V", "i=9119", {})},
                                                ),
                                                "FirstInGroup": ("O", "i=16398", {}),
                                                "FirstInGroupFlag": (
                                                    "V",
                                                    "i=16397",
                                                    {},
                                                ),
                                                "GetGroupMemberships": (
                                                    "M",
                                                    "i=24744",
                                                    {
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=25154",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "InputNode": ("V", "i=11120", {}),
                                                "LatchedState": (
                                                    "V",
                                                    "i=18190",
                                                    {
                                                        "FalseState": (
                                                            "V",
                                                            "i=18198",
                                                            {},
                                                        ),
                                                        "Id": ("V", "i=18191", {}),
                                                        "TransitionTime": (
                                                            "V",
                                                            "i=18195",
                                                            {},
                                                        ),
                                                        "TrueState": (
                                                            "V",
                                                            "i=18197",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "LimitAlarmType": (
                                                    "OT",
                                                    "i=2955",
                                                    {
                                                        "BaseHighHighLimit": (
                                                            "V",
                                                            "i=16572",
                                                            {},
                                                        ),
                                                        "BaseHighLimit": (
                                                            "V",
                                                            "i=16573",
                                                            {},
                                                        ),
                                                        "BaseLowLimit": (
                                                            "V",
                                                            "i=16574",
                                                            {},
                                                        ),
                                                        "BaseLowLowLimit": (
                                                            "V",
                                                            "i=16575",
                                                            {},
                                                        ),
                                                        "ExclusiveLimitAlarmType": (
                                                            "OT",
                                                            "i=9341",
                                                            {
                                                                "ActiveState": (
                                                                    "V",
                                                                    "i=9398",
                                                                    {
                                                                        "Id": (
                                                                            "V",
                                                                            "i=9399",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "ExclusiveDeviationAlarmType": (
                                                                    "OT",
                                                                    "i=9764",
                                                                    {
                                                                        "BaseSetpointNode": (
                                                                            "V",
                                                                            "i=16817",
                                                                            {},
                                                                        ),
                                                                        "SetpointNode": (
                                                                            "V",
                                                                            "i=9905",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "ExclusiveLevelAlarmType": (
                                                                    "OT",
                                                                    "i=9482",
                                                                    {},
                                                                ),
                                                                "ExclusiveRateOfChangeAlarmType": (
                                                                    "OT",
                                                                    "i=9623",
                                                                    {
                                                                        "EngineeringUnits": (
                                                                            "V",
                                                                            "i=16899",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "LimitState": (
                                                                    "O",
                                                                    "i=9455",
                                                                    {
                                                                        "CurrentState": (
                                                                            "V",
                                                                            "i=9456",
                                                                            {
                                                                                "Id": (
                                                                                    "V",
                                                                                    "i=9457",
                                                                                    {},
                                                                                )
                                                                            },
                                                                        ),
                                                                        "LastTransition": (
                                                                            "V",
                                                                            "i=9461",
                                                                            {
                                                                                "Id": (
                                                                                    "V",
                                                                                    "i=9462",
                                                                                    {},
                                                                                ),
                                                                                "TransitionTime": (
                                                                                    "V",
                                                                                    "i=9465",
                                                                                    {},
                                                                                ),
                                                                            },
                                                                        ),
                                                                    },
                                                                ),
                                                            },
                                                        ),
                                                        "HighDeadband": (
                                                            "V",
                                                            "i=24775",
                                                            {},
                                                        ),
                                                        "HighHighDeadband": (
                                                            "V",
                                                            "i=24774",
                                                            {},
                                                        ),
                                                        "HighHighLimit": (
                                                            "V",
                                                            "i=11124",
                                                            {},
                                                        ),
                                                        "HighLimit": (
                                                            "V",
                                                            "i=11125",
                                                            {},
                                                        ),
                                                        "LowDeadband": (
                                                            "V",
                                                            "i=24776",
                                                            {},
                                                        ),
                                                        "LowLimit": (
                                                            "V",
                                                            "i=11126",
                                                            {},
                                                        ),
                                                        "LowLowDeadband": (
                                                            "V",
                                                            "i=24777",
                                                            {},
                                                        ),
                                                        "LowLowLimit": (
                                                            "V",
                                                            "i=11127",
                                                            {},
                                                        ),
                                                        "NonExclusiveLimitAlarmType": (
                                                            "OT",
                                                            "i=9906",
                                                            {
                                                                "ActiveState": (
                                                                    "V",
                                                                    "i=9963",
                                                                    {
                                                                        "Id": (
                                                                            "V",
                                                                            "i=9964",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "HighHighState": (
                                                                    "V",
                                                                    "i=10020",
                                                                    {
                                                                        "FalseState": (
                                                                            "V",
                                                                            "i=10028",
                                                                            {},
                                                                        ),
                                                                        "Id": (
                                                                            "V",
                                                                            "i=10021",
                                                                            {},
                                                                        ),
                                                                        "TransitionTime": (
                                                                            "V",
                                                                            "i=10025",
                                                                            {},
                                                                        ),
                                                                        "TrueState": (
                                                                            "V",
                                                                            "i=10027",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "HighState": (
                                                                    "V",
                                                                    "i=10029",
                                                                    {
                                                                        "FalseState": (
                                                                            "V",
                                                                            "i=10037",
                                                                            {},
                                                                        ),
                                                                        "Id": (
                                                                            "V",
                                                                            "i=10030",
                                                                            {},
                                                                        ),
                                                                        "TransitionTime": (
                                                                            "V",
                                                                            "i=10034",
                                                                            {},
                                                                        ),
                                                                        "TrueState": (
                                                                            "V",
                                                                            "i=10036",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "LowLowState": (
                                                                    "V",
                                                                    "i=10047",
                                                                    {
                                                                        "FalseState": (
                                                                            "V",
                                                                            "i=10055",
                                                                            {},
                                                                        ),
                                                                        "Id": (
                                                                            "V",
                                                                            "i=10048",
                                                                            {},
                                                                        ),
                                                                        "TransitionTime": (
                                                                            "V",
                                                                            "i=10052",
                                                                            {},
                                                                        ),
                                                                        "TrueState": (
                                                                            "V",
                                                                            "i=10054",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "LowState": (
                                                                    "V",
                                                                    "i=10038",
                                                                    {
                                                                        "FalseState": (
                                                                            "V",
                                                                            "i=10046",
                                                                            {},
                                                                        ),
                                                                        "Id": (
                                                                            "V",
                                                                            "i=10039",
                                                                            {},
                                                                        ),
                                                                        "TransitionTime": (
                                                                            "V",
                                                                            "i=10043",
                                                                            {},
                                                                        ),
                                                                        "TrueState": (
                                                                            "V",
                                                                            "i=10045",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "NonExclusiveDeviationAlarmType": (
                                                                    "OT",
                                                                    "i=10368",
                                                                    {
                                                                        "BaseSetpointNode": (
                                                                            "V",
                                                                            "i=16776",
                                                                            {},
                                                                        ),
                                                                        "SetpointNode": (
                                                                            "V",
                                                                            "i=10522",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "NonExclusiveLevelAlarmType": (
                                                                    "OT",
                                                                    "i=10060",
                                                                    {},
                                                                ),
                                                                "NonExclusiveRateOfChangeAlarmType": (
                                                                    "OT",
                                                                    "i=10214",
                                                                    {
                                                                        "EngineeringUnits": (
                                                                            "V",
                                                                            "i=16858",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                            },
                                                        ),
                                                        "SeverityHigh": (
                                                            "V",
                                                            "i=24771",
                                                            {},
                                                        ),
                                                        "SeverityHighHigh": (
                                                            "V",
                                                            "i=24770",
                                                            {},
                                                        ),
                                                        "SeverityLow": (
                                                            "V",
                                                            "i=24772",
                                                            {},
                                                        ),
                                                        "SeverityLowLow": (
                                                            "V",
                                                            "i=24773",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "MaxTimeShelved": ("V", "i=9216", {}),
                                                "OffDelay": ("V", "i=16396", {}),
                                                "OnDelay": ("V", "i=16395", {}),
                                                "OutOfServiceState": (
                                                    "V",
                                                    "i=16371",
                                                    {
                                                        "FalseState": (
                                                            "V",
                                                            "i=16379",
                                                            {},
                                                        ),
                                                        "Id": ("V", "i=16372", {}),
                                                        "TransitionTime": (
                                                            "V",
                                                            "i=16376",
                                                            {},
                                                        ),
                                                        "TrueState": (
                                                            "V",
                                                            "i=16378",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "PlaceInService": ("M", "i=17870", {}),
                                                "PlaceInService2": (
                                                    "M",
                                                    "i=24322",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=24323",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "ReAlarmRepeatCount": (
                                                    "V",
                                                    "i=16401",
                                                    {},
                                                ),
                                                "ReAlarmTime": ("V", "i=16400", {}),
                                                "RemoveFromService": (
                                                    "M",
                                                    "i=17869",
                                                    {},
                                                ),
                                                "RemoveFromService2": (
                                                    "M",
                                                    "i=24320",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=24321",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Reset": ("M", "i=18199", {}),
                                                "Reset2": (
                                                    "M",
                                                    "i=24324",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=24325",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "ShelvingState": (
                                                    "O",
                                                    "i=9178",
                                                    {
                                                        "CurrentState": (
                                                            "V",
                                                            "i=9179",
                                                            {"Id": ("V", "i=9180", {})},
                                                        ),
                                                        "LastTransition": (
                                                            "V",
                                                            "i=9184",
                                                            {
                                                                "Id": (
                                                                    "V",
                                                                    "i=9185",
                                                                    {},
                                                                ),
                                                                "TransitionTime": (
                                                                    "V",
                                                                    "i=9188",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "OneShotShelve": (
                                                            "M",
                                                            "i=9212",
                                                            {},
                                                        ),
                                                        "TimedShelve": (
                                                            "M",
                                                            "i=9213",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=9214",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "Unshelve": ("M", "i=9211", {}),
                                                        "UnshelveTime": (
                                                            "V",
                                                            "i=9189",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "Silence": ("M", "i=16402", {}),
                                                "SilenceState": (
                                                    "V",
                                                    "i=16380",
                                                    {
                                                        "FalseState": (
                                                            "V",
                                                            "i=16388",
                                                            {},
                                                        ),
                                                        "Id": ("V", "i=16381", {}),
                                                        "TransitionTime": (
                                                            "V",
                                                            "i=16385",
                                                            {},
                                                        ),
                                                        "TrueState": (
                                                            "V",
                                                            "i=16387",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "Suppress": ("M", "i=16403", {}),
                                                "Suppress2": (
                                                    "M",
                                                    "i=24316",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=24317",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "SuppressedOrShelved": (
                                                    "V",
                                                    "i=9215",
                                                    {},
                                                ),
                                                "SuppressedState": (
                                                    "V",
                                                    "i=9169",
                                                    {
                                                        "FalseState": (
                                                            "V",
                                                            "i=9177",
                                                            {},
                                                        ),
                                                        "Id": ("V", "i=9170", {}),
                                                        "TransitionTime": (
                                                            "V",
                                                            "i=9174",
                                                            {},
                                                        ),
                                                        "TrueState": (
                                                            "V",
                                                            "i=9176",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "Unsuppress": ("M", "i=17868", {}),
                                                "Unsuppress2": (
                                                    "M",
                                                    "i=24318",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=24319",
                                                            {},
                                                        )
                                                    },
                                                ),
                                            },
                                        ),
                                        "Confirm": (
                                            "M",
                                            "i=9113",
                                            {"InputArguments": ("V", "i=9114", {})},
                                        ),
                                        "ConfirmedState": (
                                            "V",
                                            "i=9102",
                                            {
                                                "FalseState": ("V", "i=9110", {}),
                                                "Id": ("V", "i=9103", {}),
                                                "TransitionTime": ("V", "i=9107", {}),
                                                "TrueState": ("V", "i=9109", {}),
                                            },
                                        ),
                                        "EnabledState": (
                                            "V",
                                            "i=9073",
                                            {"Id": ("V", "i=9074", {})},
                                        ),
                                    },
                                ),
                                "AddComment": (
                                    "M",
                                    "i=9029",
                                    {"InputArguments": ("V", "i=9030", {})},
                                ),
                                "BranchId": ("V", "i=9010", {}),
                                "ClientUserId": ("V", "i=9026", {}),
                                "Comment": (
                                    "V",
                                    "i=9024",
                                    {"SourceTimestamp": ("V", "i=9025", {})},
                                ),
                                "ConditionClassId": ("V", "i=11112", {}),
                                "ConditionClassName": ("V", "i=11113", {}),
                                "ConditionName": ("V", "i=9009", {}),
                                "ConditionRefresh": (
                                    "M",
                                    "i=3875",
                                    {"InputArguments": ("V", "i=3876", {})},
                                ),
                                "ConditionRefresh2": (
                                    "M",
                                    "i=12912",
                                    {"InputArguments": ("V", "i=12913", {})},
                                ),
                                "ConditionSubClassId": ("V", "i=16363", {}),
                                "ConditionSubClassName": ("V", "i=16364", {}),
                                "DialogConditionType": (
                                    "OT",
                                    "i=2830",
                                    {
                                        "CancelResponse": ("V", "i=9067", {}),
                                        "DefaultResponse": ("V", "i=9065", {}),
                                        "DialogState": (
                                            "V",
                                            "i=9055",
                                            {
                                                "FalseState": ("V", "i=9063", {}),
                                                "Id": ("V", "i=9056", {}),
                                                "TransitionTime": ("V", "i=9060", {}),
                                                "TrueState": ("V", "i=9062", {}),
                                            },
                                        ),
                                        "EnabledState": (
                                            "V",
                                            "i=9035",
                                            {"Id": ("V", "i=9036", {})},
                                        ),
                                        "LastResponse": ("V", "i=9068", {}),
                                        "OkResponse": ("V", "i=9066", {}),
                                        "Prompt": ("V", "i=2831", {}),
                                        "Respond": (
                                            "M",
                                            "i=9069",
                                            {"InputArguments": ("V", "i=9070", {})},
                                        ),
                                        "Respond2": (
                                            "M",
                                            "i=24312",
                                            {"InputArguments": ("V", "i=24313", {})},
                                        ),
                                        "ResponseOptionSet": ("V", "i=9064", {}),
                                    },
                                ),
                                "Disable": ("M", "i=9028", {}),
                                "Enable": ("M", "i=9027", {}),
                                "EnabledState": (
                                    "V",
                                    "i=9011",
                                    {
                                        "EffectiveDisplayName": ("V", "i=9015", {}),
                                        "EffectiveTransitionTime": ("V", "i=9017", {}),
                                        "FalseState": ("V", "i=9019", {}),
                                        "Id": ("V", "i=9012", {}),
                                        "TransitionTime": ("V", "i=9016", {}),
                                        "TrueState": ("V", "i=9018", {}),
                                    },
                                ),
                                "LastSeverity": (
                                    "V",
                                    "i=9022",
                                    {"SourceTimestamp": ("V", "i=9023", {})},
                                ),
                                "Quality": (
                                    "V",
                                    "i=9020",
                                    {"SourceTimestamp": ("V", "i=9021", {})},
                                ),
                                "Retain": ("V", "i=3874", {}),
                                "SupportsFilteredRetain": ("V", "i=32060", {}),
                            },
                        ),
                        "EventId": ("V", "i=2042", {}),
                        "EventQueueOverflowEventType": ("OT", "i=3035", {}),
                        "EventType": ("V", "i=2043", {}),
                        "LocalTime": ("V", "i=3190", {}),
                        "LogOverflowEventType": ("OT", "i=19369", {}),
                        "Message": ("V", "i=2050", {}),
                        "ProgressEventType": (
                            "OT",
                            "i=11436",
                            {
                                "Context": ("V", "i=12502", {}),
                                "Progress": ("V", "i=12503", {}),
                            },
                        ),
                        "ReceiveTime": ("V", "i=2047", {}),
                        "SemanticChangeEventType": (
                            "OT",
                            "i=2738",
                            {"Changes": ("V", "i=2739", {})},
                        ),
                        "Severity": ("V", "i=2051", {}),
                        "SourceName": ("V", "i=2045", {}),
                        "SourceNode": ("V", "i=2044", {}),
                        "SystemEventType": (
                            "OT",
                            "i=2130",
                            {
                                "DeviceFailureEventType": ("OT", "i=2131", {}),
                                "PubSubStatusEventType": (
                                    "OT",
                                    "i=15535",
                                    {
                                        "ConnectionId": ("V", "i=15545", {}),
                                        "GroupId": ("V", "i=15546", {}),
                                        "PubSubCommunicationFailureEventType": (
                                            "OT",
                                            "i=15563",
                                            {"Error": ("V", "i=15576", {})},
                                        ),
                                        "PubSubTransportLimitsExceedEventType": (
                                            "OT",
                                            "i=15548",
                                            {
                                                "Actual": ("V", "i=15561", {}),
                                                "Maximum": ("V", "i=15562", {}),
                                            },
                                        ),
                                        "State": ("V", "i=15547", {}),
                                    },
                                ),
                                "RefreshEndEventType": ("OT", "i=2788", {}),
                                "RefreshRequiredEventType": ("OT", "i=2789", {}),
                                "RefreshStartEventType": ("OT", "i=2787", {}),
                                "SystemStatusChangeEventType": (
                                    "OT",
                                    "i=11446",
                                    {"SystemState": ("V", "i=11696", {})},
                                ),
                            },
                        ),
                        "Time": ("V", "i=2046", {}),
                        "TransitionEventType": (
                            "OT",
                            "i=2311",
                            {
                                "FromState": (
                                    "V",
                                    "i=2775",
                                    {"Id": ("V", "i=3746", {})},
                                ),
                                "ProgramTransitionEventType": (
                                    "OT",
                                    "i=2378",
                                    {"IntermediateResult": ("V", "i=2379", {})},
                                ),
                                "ToState": ("V", "i=2776", {"Id": ("V", "i=3750", {})}),
                                "Transition": (
                                    "V",
                                    "i=2774",
                                    {"Id": ("V", "i=3754", {})},
                                ),
                            },
                        ),
                    },
                ),
                "BaseInterfaceType": (
                    "OT",
                    "i=17602",
                    {
                        "IBaseEthernetCapabilitiesType": (
                            "OT",
                            "i=24167",
                            {"VlanTagCapable": ("V", "i=24168", {})},
                        ),
                        "IIeeeAutoNegotiationStatusType": (
                            "OT",
                            "i=24233",
                            {"NegotiationStatus": ("V", "i=24234", {})},
                        ),
                        "IIeeeBaseEthernetPortType": (
                            "OT",
                            "i=24158",
                            {
                                "Duplex": ("V", "i=24165", {}),
                                "MaxFrameLength": ("V", "i=24166", {}),
                                "Speed": (
                                    "V",
                                    "i=24159",
                                    {"EngineeringUnits": ("V", "i=24164", {})},
                                ),
                            },
                        ),
                        "IIeeeBaseTsnStatusStreamType": (
                            "OT",
                            "i=24183",
                            {
                                "FailureCode": ("V", "i=24186", {}),
                                "FailureSystemIdentifier": ("V", "i=24187", {}),
                                "ListenerStatus": ("V", "i=24185", {}),
                                "TalkerStatus": ("V", "i=24184", {}),
                            },
                        ),
                        "IIeeeBaseTsnStreamType": (
                            "OT",
                            "i=24173",
                            {
                                "AccumulatedLatency": ("V", "i=24177", {}),
                                "SrClassId": ("V", "i=24178", {}),
                                "State": ("V", "i=24176", {}),
                                "StreamId": ("V", "i=24174", {}),
                                "StreamName": ("V", "i=24175", {}),
                            },
                        ),
                        "IIeeeBaseTsnTrafficSpecificationType": (
                            "OT",
                            "i=24179",
                            {
                                "Interval": ("V", "i=24182", {}),
                                "MaxFrameSize": ("V", "i=24181", {}),
                                "MaxIntervalFrames": ("V", "i=24180", {}),
                            },
                        ),
                        "IIeeeTsnInterfaceConfigurationType": (
                            "OT",
                            "i=24188",
                            {
                                "IIeeeTsnInterfaceConfigurationListenerType": (
                                    "OT",
                                    "i=24195",
                                    {"ReceiveOffset": ("V", "i=24198", {})},
                                ),
                                "IIeeeTsnInterfaceConfigurationTalkerType": (
                                    "OT",
                                    "i=24191",
                                    {"TimeAwareOffset": ("V", "i=24194", {})},
                                ),
                                "InterfaceName": ("V", "i=24190", {}),
                                "MacAddress": ("V", "i=24189", {}),
                            },
                        ),
                        "IIeeeTsnMacAddressType": (
                            "OT",
                            "i=24199",
                            {
                                "DestinationAddress": ("V", "i=24200", {}),
                                "SourceAddress": ("V", "i=24201", {}),
                            },
                        ),
                        "IIeeeTsnVlanTagType": (
                            "OT",
                            "i=24202",
                            {
                                "PriorityCodePoint": ("V", "i=24204", {}),
                                "VlanId": ("V", "i=24203", {}),
                            },
                        ),
                        "IIetfBaseNetworkInterfaceType": (
                            "OT",
                            "i=24148",
                            {
                                "AdminStatus": ("V", "i=24149", {}),
                                "OperStatus": ("V", "i=24150", {}),
                                "PhysAddress": ("V", "i=24151", {}),
                                "Speed": (
                                    "V",
                                    "i=24152",
                                    {"EngineeringUnits": ("V", "i=24157", {})},
                                ),
                            },
                        ),
                        "IOrderedObjectType": (
                            "OT",
                            "i=23513",
                            {"NumberInList": ("V", "i=23517", {})},
                        ),
                        "IPriorityMappingEntryType": (
                            "OT",
                            "i=24205",
                            {
                                "MappingUri": ("V", "i=24206", {}),
                                "PriorityLabel": ("V", "i=24207", {}),
                                "PriorityValue_DSCP": ("V", "i=24209", {}),
                                "PriorityValue_PCP": ("V", "i=24208", {}),
                            },
                        ),
                        "ISrClassType": (
                            "OT",
                            "i=24169",
                            {
                                "Id": ("V", "i=24170", {}),
                                "Priority": ("V", "i=24171", {}),
                                "Vid": ("V", "i=24172", {}),
                            },
                        ),
                        "IVlanIdType": (
                            "OT",
                            "i=25218",
                            {"VlanId": ("V", "i=25219", {})},
                        ),
                    },
                ),
                "CertificateGroupType": (
                    "OT",
                    "i=12555",
                    {
                        "CertificateExpired": (
                            "O",
                            "i=19450",
                            {
                                "AckedState": (
                                    "V",
                                    "i=19487",
                                    {"Id": ("V", "i=19488", {})},
                                ),
                                "Acknowledge": (
                                    "M",
                                    "i=19505",
                                    {"InputArguments": ("V", "i=19506", {})},
                                ),
                                "ActiveState": (
                                    "V",
                                    "i=19509",
                                    {"Id": ("V", "i=19510", {})},
                                ),
                                "AddComment": (
                                    "M",
                                    "i=19485",
                                    {"InputArguments": ("V", "i=19486", {})},
                                ),
                                "BranchId": ("V", "i=19465", {}),
                                "Certificate": ("V", "i=20142", {}),
                                "CertificateType": ("V", "i=20141", {}),
                                "ClientUserId": ("V", "i=19482", {}),
                                "Comment": (
                                    "V",
                                    "i=19480",
                                    {"SourceTimestamp": ("V", "i=19481", {})},
                                ),
                                "ConditionClassId": ("V", "i=19460", {}),
                                "ConditionClassName": ("V", "i=19461", {}),
                                "ConditionName": ("V", "i=19464", {}),
                                "Disable": ("M", "i=19483", {}),
                                "Enable": ("M", "i=19484", {}),
                                "EnabledState": (
                                    "V",
                                    "i=19467",
                                    {"Id": ("V", "i=19468", {})},
                                ),
                                "EventId": ("V", "i=19451", {}),
                                "EventType": ("V", "i=19452", {}),
                                "ExpirationDate": ("V", "i=20139", {}),
                                "InputNode": ("V", "i=19518", {}),
                                "LastSeverity": (
                                    "V",
                                    "i=19478",
                                    {"SourceTimestamp": ("V", "i=19479", {})},
                                ),
                                "Message": ("V", "i=19458", {}),
                                "NormalState": ("V", "i=20138", {}),
                                "Quality": (
                                    "V",
                                    "i=19476",
                                    {"SourceTimestamp": ("V", "i=19477", {})},
                                ),
                                "ReceiveTime": ("V", "i=19456", {}),
                                "Retain": ("V", "i=19466", {}),
                                "Severity": ("V", "i=19459", {}),
                                "SourceName": ("V", "i=19454", {}),
                                "SourceNode": ("V", "i=19453", {}),
                                "SuppressedOrShelved": ("V", "i=20101", {}),
                                "Time": ("V", "i=19455", {}),
                            },
                        ),
                        "CertificateTypes": ("V", "i=13631", {}),
                        "GetRejectedList": (
                            "M",
                            "i=23526",
                            {"OutputArguments": ("V", "i=23527", {})},
                        ),
                        "Purpose": ("V", "i=19398", {}),
                        "TrustList": (
                            "O",
                            "i=13599",
                            {
                                "AddCertificate": (
                                    "M",
                                    "i=13627",
                                    {"InputArguments": ("V", "i=13628", {})},
                                ),
                                "Close": (
                                    "M",
                                    "i=13608",
                                    {"InputArguments": ("V", "i=13609", {})},
                                ),
                                "CloseAndUpdate": (
                                    "M",
                                    "i=13624",
                                    {
                                        "InputArguments": ("V", "i=13625", {}),
                                        "OutputArguments": ("V", "i=13626", {}),
                                    },
                                ),
                                "GetPosition": (
                                    "M",
                                    "i=13615",
                                    {
                                        "InputArguments": ("V", "i=13616", {}),
                                        "OutputArguments": ("V", "i=13617", {}),
                                    },
                                ),
                                "LastUpdateTime": ("V", "i=13620", {}),
                                "Open": (
                                    "M",
                                    "i=13605",
                                    {
                                        "InputArguments": ("V", "i=13606", {}),
                                        "OutputArguments": ("V", "i=13607", {}),
                                    },
                                ),
                                "OpenCount": ("V", "i=13603", {}),
                                "OpenWithMasks": (
                                    "M",
                                    "i=13621",
                                    {
                                        "InputArguments": ("V", "i=13622", {}),
                                        "OutputArguments": ("V", "i=13623", {}),
                                    },
                                ),
                                "Read": (
                                    "M",
                                    "i=13610",
                                    {
                                        "InputArguments": ("V", "i=13611", {}),
                                        "OutputArguments": ("V", "i=13612", {}),
                                    },
                                ),
                                "RemoveCertificate": (
                                    "M",
                                    "i=13629",
                                    {"InputArguments": ("V", "i=13630", {})},
                                ),
                                "SetPosition": (
                                    "M",
                                    "i=13618",
                                    {"InputArguments": ("V", "i=13619", {})},
                                ),
                                "Size": ("V", "i=13600", {}),
                                "UserWritable": ("V", "i=13602", {}),
                                "Writable": ("V", "i=13601", {}),
                                "Write": (
                                    "M",
                                    "i=13613",
                                    {"InputArguments": ("V", "i=13614", {})},
                                ),
                            },
                        ),
                        "TrustListOutOfDate": (
                            "O",
                            "i=20143",
                            {
                                "AckedState": (
                                    "V",
                                    "i=20180",
                                    {"Id": ("V", "i=20181", {})},
                                ),
                                "Acknowledge": (
                                    "M",
                                    "i=20198",
                                    {"InputArguments": ("V", "i=20199", {})},
                                ),
                                "ActiveState": (
                                    "V",
                                    "i=20202",
                                    {"Id": ("V", "i=20203", {})},
                                ),
                                "AddComment": (
                                    "M",
                                    "i=20178",
                                    {"InputArguments": ("V", "i=20179", {})},
                                ),
                                "BranchId": ("V", "i=20158", {}),
                                "ClientUserId": ("V", "i=20175", {}),
                                "Comment": (
                                    "V",
                                    "i=20173",
                                    {"SourceTimestamp": ("V", "i=20174", {})},
                                ),
                                "ConditionClassId": ("V", "i=20153", {}),
                                "ConditionClassName": ("V", "i=20154", {}),
                                "ConditionName": ("V", "i=20157", {}),
                                "Disable": ("M", "i=20176", {}),
                                "Enable": ("M", "i=20177", {}),
                                "EnabledState": (
                                    "V",
                                    "i=20160",
                                    {"Id": ("V", "i=20161", {})},
                                ),
                                "EventId": ("V", "i=20144", {}),
                                "EventType": ("V", "i=20145", {}),
                                "InputNode": ("V", "i=20211", {}),
                                "LastSeverity": (
                                    "V",
                                    "i=20171",
                                    {"SourceTimestamp": ("V", "i=20172", {})},
                                ),
                                "LastUpdateTime": ("V", "i=20288", {}),
                                "Message": ("V", "i=20151", {}),
                                "NormalState": ("V", "i=20286", {}),
                                "Quality": (
                                    "V",
                                    "i=20169",
                                    {"SourceTimestamp": ("V", "i=20170", {})},
                                ),
                                "ReceiveTime": ("V", "i=20149", {}),
                                "Retain": ("V", "i=20159", {}),
                                "Severity": ("V", "i=20152", {}),
                                "SourceName": ("V", "i=20147", {}),
                                "SourceNode": ("V", "i=20146", {}),
                                "SuppressedOrShelved": ("V", "i=20249", {}),
                                "Time": ("V", "i=20148", {}),
                                "TrustListId": ("V", "i=20287", {}),
                                "UpdateFrequency": ("V", "i=20289", {}),
                            },
                        ),
                    },
                ),
                "CertificateType": (
                    "OT",
                    "i=12556",
                    {
                        "ApplicationCertificateType": (
                            "OT",
                            "i=12557",
                            {
                                "EccApplicationCertificateType": (
                                    "OT",
                                    "i=23537",
                                    {
                                        "EccBrainpoolP256r1ApplicationCertificateType": (
                                            "OT",
                                            "i=23540",
                                            {},
                                        ),
                                        "EccBrainpoolP384r1ApplicationCertificateType": (
                                            "OT",
                                            "i=23541",
                                            {},
                                        ),
                                        "EccCurve25519ApplicationCertificateType": (
                                            "OT",
                                            "i=23542",
                                            {},
                                        ),
                                        "EccCurve448ApplicationCertificateType": (
                                            "OT",
                                            "i=23543",
                                            {},
                                        ),
                                        "EccNistP256ApplicationCertificateType": (
                                            "OT",
                                            "i=23538",
                                            {},
                                        ),
                                        "EccNistP384ApplicationCertificateType": (
                                            "OT",
                                            "i=23539",
                                            {},
                                        ),
                                    },
                                ),
                                "RsaMinApplicationCertificateType": (
                                    "OT",
                                    "i=12559",
                                    {},
                                ),
                                "RsaSha256ApplicationCertificateType": (
                                    "OT",
                                    "i=12560",
                                    {},
                                ),
                            },
                        ),
                        "HttpsCertificateType": ("OT", "i=12558", {}),
                        "TlsCertificateType": (
                            "OT",
                            "i=19324",
                            {
                                "TlsClientCertificateType": ("OT", "i=19326", {}),
                                "TlsServerCertificateType": ("OT", "i=19325", {}),
                            },
                        ),
                        "UserCertificateType": ("OT", "i=19323", {}),
                    },
                ),
                "ConnectionTransportType": (
                    "OT",
                    "i=17721",
                    {
                        "BrokerConnectionTransportType": (
                            "OT",
                            "i=15155",
                            {
                                "AuthenticationProfileUri": ("V", "i=15178", {}),
                                "ResourceUri": ("V", "i=15156", {}),
                            },
                        ),
                        "DatagramConnectionTransportType": (
                            "OT",
                            "i=15064",
                            {
                                "DatagramQos": ("V", "i=25526", {}),
                                "DiscoveryAddress": (
                                    "O",
                                    "i=15072",
                                    {
                                        "NetworkInterface": (
                                            "V",
                                            "i=15154",
                                            {"Selections": ("V", "i=17579", {})},
                                        )
                                    },
                                ),
                                "DiscoveryAnnounceRate": ("V", "i=23839", {}),
                                "DiscoveryMaxMessageSize": ("V", "i=23840", {}),
                                "QosCategory": ("V", "i=25525", {}),
                            },
                        ),
                    },
                ),
                "DataSetReaderMessageType": (
                    "OT",
                    "i=21104",
                    {
                        "JsonDataSetReaderMessageType": (
                            "OT",
                            "i=21130",
                            {
                                "DataSetMessageContentMask": ("V", "i=21132", {}),
                                "NetworkMessageContentMask": ("V", "i=21131", {}),
                            },
                        ),
                        "UadpDataSetReaderMessageType": (
                            "OT",
                            "i=21116",
                            {
                                "DataSetClassId": ("V", "i=21120", {}),
                                "DataSetMessageContentMask": ("V", "i=21122", {}),
                                "DataSetOffset": ("V", "i=17477", {}),
                                "GroupVersion": ("V", "i=21117", {}),
                                "NetworkMessageContentMask": ("V", "i=21121", {}),
                                "NetworkMessageNumber": ("V", "i=21119", {}),
                                "ProcessingOffset": ("V", "i=21124", {}),
                                "PublishingInterval": ("V", "i=21123", {}),
                                "ReceiveOffset": ("V", "i=21125", {}),
                            },
                        ),
                    },
                ),
                "DataSetReaderTransportType": (
                    "OT",
                    "i=15319",
                    {
                        "BrokerDataSetReaderTransportType": (
                            "OT",
                            "i=21142",
                            {
                                "AuthenticationProfileUri": ("V", "i=15419", {}),
                                "MetaDataQueueName": ("V", "i=21144", {}),
                                "QueueName": ("V", "i=21143", {}),
                                "RequestedDeliveryGuarantee": ("V", "i=15420", {}),
                                "ResourceUri": ("V", "i=15334", {}),
                            },
                        ),
                        "DatagramDataSetReaderTransportType": (
                            "OT",
                            "i=24016",
                            {
                                "Address": (
                                    "O",
                                    "i=24017",
                                    {
                                        "NetworkInterface": (
                                            "V",
                                            "i=24018",
                                            {"Selections": ("V", "i=24019", {})},
                                        )
                                    },
                                ),
                                "DatagramQos": ("V", "i=24022", {}),
                                "QosCategory": ("V", "i=25528", {}),
                                "Topic": ("V", "i=24023", {}),
                            },
                        ),
                    },
                ),
                "DataSetReaderType": (
                    "OT",
                    "i=15306",
                    {
                        "CreateDataSetMirror": (
                            "M",
                            "i=17389",
                            {
                                "InputArguments": ("V", "i=17390", {}),
                                "OutputArguments": ("V", "i=17391", {}),
                            },
                        ),
                        "CreateTargetVariables": (
                            "M",
                            "i=17386",
                            {
                                "InputArguments": ("V", "i=17387", {}),
                                "OutputArguments": ("V", "i=17388", {}),
                            },
                        ),
                        "DataSetFieldContentMask": ("V", "i=21101", {}),
                        "DataSetMetaData": ("V", "i=21100", {}),
                        "DataSetReaderProperties": ("V", "i=17494", {}),
                        "DataSetWriterId": ("V", "i=21099", {}),
                        "Diagnostics": (
                            "O",
                            "i=19609",
                            {
                                "Counters": (
                                    "O",
                                    "i=19623",
                                    {
                                        "FailedDataSetMessages": (
                                            "V",
                                            "i=19655",
                                            {
                                                "Active": ("V", "i=19656", {}),
                                                "Classification": ("V", "i=19657", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19658",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "StateDisabledByMethod": (
                                            "V",
                                            "i=19649",
                                            {
                                                "Active": ("V", "i=19650", {}),
                                                "Classification": ("V", "i=19651", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19652",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "StateError": (
                                            "V",
                                            "i=19624",
                                            {
                                                "Active": ("V", "i=19625", {}),
                                                "Classification": ("V", "i=19626", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19627",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "StateOperationalByMethod": (
                                            "V",
                                            "i=19629",
                                            {
                                                "Active": ("V", "i=19630", {}),
                                                "Classification": ("V", "i=19631", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19632",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "StateOperationalByParent": (
                                            "V",
                                            "i=19634",
                                            {
                                                "Active": ("V", "i=19635", {}),
                                                "Classification": ("V", "i=19636", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19637",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "StateOperationalFromError": (
                                            "V",
                                            "i=19639",
                                            {
                                                "Active": ("V", "i=19640", {}),
                                                "Classification": ("V", "i=19641", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19642",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "StatePausedByParent": (
                                            "V",
                                            "i=19644",
                                            {
                                                "Active": ("V", "i=19645", {}),
                                                "Classification": ("V", "i=19646", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19647",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "DiagnosticsLevel": ("V", "i=19610", {}),
                                "LiveValues": ("O", "i=19654", {}),
                                "Reset": ("M", "i=19621", {}),
                                "SubError": ("V", "i=19622", {}),
                                "TotalError": (
                                    "V",
                                    "i=19616",
                                    {
                                        "Active": ("V", "i=19617", {}),
                                        "Classification": ("V", "i=19618", {}),
                                        "DiagnosticsLevel": ("V", "i=19619", {}),
                                    },
                                ),
                                "TotalInformation": (
                                    "V",
                                    "i=19611",
                                    {
                                        "Active": ("V", "i=19612", {}),
                                        "Classification": ("V", "i=19613", {}),
                                        "DiagnosticsLevel": ("V", "i=19614", {}),
                                    },
                                ),
                            },
                        ),
                        "HeaderLayoutUri": ("V", "i=17564", {}),
                        "KeyFrameCount": ("V", "i=17563", {}),
                        "MessageReceiveTimeout": ("V", "i=21102", {}),
                        "MessageSettings": ("O", "i=21103", {}),
                        "PublisherId": ("V", "i=21097", {}),
                        "SecurityGroupId": ("V", "i=15933", {}),
                        "SecurityKeyServices": ("V", "i=15934", {}),
                        "SecurityMode": ("V", "i=15932", {}),
                        "Status": ("O", "i=15307", {"State": ("V", "i=15308", {})}),
                        "SubscribedDataSet": ("O", "i=15316", {}),
                        "TransportSettings": ("O", "i=15311", {}),
                        "WriterGroupId": ("V", "i=21098", {}),
                    },
                ),
                "DataSetWriterMessageType": (
                    "OT",
                    "i=21096",
                    {
                        "JsonDataSetWriterMessageType": (
                            "OT",
                            "i=21128",
                            {"DataSetMessageContentMask": ("V", "i=21129", {})},
                        ),
                        "UadpDataSetWriterMessageType": (
                            "OT",
                            "i=21111",
                            {
                                "ConfiguredSize": ("V", "i=21113", {}),
                                "DataSetMessageContentMask": ("V", "i=21112", {}),
                                "DataSetOffset": ("V", "i=21115", {}),
                                "NetworkMessageNumber": ("V", "i=21114", {}),
                            },
                        ),
                    },
                ),
                "DataSetWriterTransportType": (
                    "OT",
                    "i=15305",
                    {
                        "BrokerDataSetWriterTransportType": (
                            "OT",
                            "i=21138",
                            {
                                "AuthenticationProfileUri": ("V", "i=15251", {}),
                                "MetaDataQueueName": ("V", "i=21140", {}),
                                "MetaDataUpdateTime": ("V", "i=21141", {}),
                                "QueueName": ("V", "i=21139", {}),
                                "RequestedDeliveryGuarantee": ("V", "i=15330", {}),
                                "ResourceUri": ("V", "i=15250", {}),
                            },
                        )
                    },
                ),
                "DataSetWriterType": (
                    "OT",
                    "i=15298",
                    {
                        "DataSetFieldContentMask": ("V", "i=21093", {}),
                        "DataSetWriterId": ("V", "i=21092", {}),
                        "DataSetWriterProperties": ("V", "i=17493", {}),
                        "Diagnostics": (
                            "O",
                            "i=19550",
                            {
                                "Counters": (
                                    "O",
                                    "i=19564",
                                    {
                                        "FailedDataSetMessages": (
                                            "V",
                                            "i=19596",
                                            {
                                                "Active": ("V", "i=19597", {}),
                                                "Classification": ("V", "i=19598", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19599",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "StateDisabledByMethod": (
                                            "V",
                                            "i=19590",
                                            {
                                                "Active": ("V", "i=19591", {}),
                                                "Classification": ("V", "i=19592", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19593",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "StateError": (
                                            "V",
                                            "i=19565",
                                            {
                                                "Active": ("V", "i=19566", {}),
                                                "Classification": ("V", "i=19567", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19568",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "StateOperationalByMethod": (
                                            "V",
                                            "i=19570",
                                            {
                                                "Active": ("V", "i=19571", {}),
                                                "Classification": ("V", "i=19572", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19573",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "StateOperationalByParent": (
                                            "V",
                                            "i=19575",
                                            {
                                                "Active": ("V", "i=19576", {}),
                                                "Classification": ("V", "i=19577", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19578",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "StateOperationalFromError": (
                                            "V",
                                            "i=19580",
                                            {
                                                "Active": ("V", "i=19581", {}),
                                                "Classification": ("V", "i=19582", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19583",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "StatePausedByParent": (
                                            "V",
                                            "i=19585",
                                            {
                                                "Active": ("V", "i=19586", {}),
                                                "Classification": ("V", "i=19587", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19588",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "DiagnosticsLevel": ("V", "i=19551", {}),
                                "LiveValues": ("O", "i=19595", {}),
                                "Reset": ("M", "i=19562", {}),
                                "SubError": ("V", "i=19563", {}),
                                "TotalError": (
                                    "V",
                                    "i=19557",
                                    {
                                        "Active": ("V", "i=19558", {}),
                                        "Classification": ("V", "i=19559", {}),
                                        "DiagnosticsLevel": ("V", "i=19560", {}),
                                    },
                                ),
                                "TotalInformation": (
                                    "V",
                                    "i=19552",
                                    {
                                        "Active": ("V", "i=19553", {}),
                                        "Classification": ("V", "i=19554", {}),
                                        "DiagnosticsLevel": ("V", "i=19555", {}),
                                    },
                                ),
                            },
                        ),
                        "KeyFrameCount": ("V", "i=21094", {}),
                        "MessageSettings": ("O", "i=21095", {}),
                        "Status": ("O", "i=15299", {"State": ("V", "i=15300", {})}),
                        "TransportSettings": ("O", "i=15303", {}),
                    },
                ),
                "DataTypeEncodingType": ("OT", "i=76", {}),
                "DataTypeRefinementType": ("OT", "i=19820", {}),
                "DataTypeSystemType": ("OT", "i=75", {}),
                "DictionaryEntryType": (
                    "OT",
                    "i=17589",
                    {
                        "<DictionaryEntryName>": ("O", "i=17590", {}),
                        "IrdiDictionaryEntryType": ("OT", "i=17598", {}),
                        "SyntaxReferenceEntryType": (
                            "OT",
                            "i=32439",
                            {"CommonName": ("V", "i=32441", {})},
                        ),
                        "UriDictionaryEntryType": ("OT", "i=17600", {}),
                    },
                ),
                "ExtensionFieldsType": (
                    "OT",
                    "i=15489",
                    {
                        "<ExtensionFieldName>": ("V", "i=15490", {}),
                        "AddExtensionField": (
                            "M",
                            "i=15491",
                            {
                                "InputArguments": ("V", "i=15492", {}),
                                "OutputArguments": ("V", "i=15493", {}),
                            },
                        ),
                        "RemoveExtensionField": (
                            "M",
                            "i=15494",
                            {"InputArguments": ("V", "i=15495", {})},
                        ),
                    },
                ),
                "FileType": (
                    "OT",
                    "i=11575",
                    {
                        "AddressSpaceFileType": (
                            "OT",
                            "i=11595",
                            {"ExportNamespace": ("M", "i=11615", {})},
                        ),
                        "Close": (
                            "M",
                            "i=11583",
                            {"InputArguments": ("V", "i=11584", {})},
                        ),
                        "ConfigurationFileType": (
                            "OT",
                            "i=15437",
                            {
                                "ActivityTimeout": ("V", "i=15503", {}),
                                "ApplicationConfigurationFileType": (
                                    "OT",
                                    "i=15550",
                                    {
                                        "AvailableNetworks": ("V", "i=15551", {}),
                                        "AvailablePorts": ("V", "i=15552", {}),
                                        "CertificateGroupPurposes": (
                                            "V",
                                            "i=19416",
                                            {},
                                        ),
                                        "CertificateTypes": ("V", "i=15555", {}),
                                        "MaxCertificateGroups": ("V", "i=19415", {}),
                                        "MaxEndpoints": ("V", "i=19414", {}),
                                        "SecurityPolicyUris": ("V", "i=15553", {}),
                                        "UserTokenTypes": ("V", "i=15554", {}),
                                    },
                                ),
                                "CloseAndUpdate": (
                                    "M",
                                    "i=15505",
                                    {
                                        "InputArguments": ("V", "i=15506", {}),
                                        "OutputArguments": ("V", "i=15507", {}),
                                    },
                                ),
                                "ConfirmUpdate": (
                                    "M",
                                    "i=15508",
                                    {"InputArguments": ("V", "i=15511", {})},
                                ),
                                "CurrentVersion": ("V", "i=15439", {}),
                                "LastUpdateTime": ("V", "i=15438", {}),
                                "SupportedDataType": ("V", "i=15504", {}),
                            },
                        ),
                        "GetPosition": (
                            "M",
                            "i=11590",
                            {
                                "InputArguments": ("V", "i=11591", {}),
                                "OutputArguments": ("V", "i=11592", {}),
                            },
                        ),
                        "LastModifiedTime": ("V", "i=25200", {}),
                        "MaxByteStringLength": ("V", "i=24244", {}),
                        "MimeType": ("V", "i=13341", {}),
                        "Open": (
                            "M",
                            "i=11580",
                            {
                                "InputArguments": ("V", "i=11581", {}),
                                "OutputArguments": ("V", "i=11582", {}),
                            },
                        ),
                        "OpenCount": ("V", "i=11579", {}),
                        "PubSubConfigurationType": (
                            "OT",
                            "i=25482",
                            {
                                "CloseAndUpdate": (
                                    "M",
                                    "i=25508",
                                    {
                                        "InputArguments": ("V", "i=25509", {}),
                                        "OutputArguments": ("V", "i=25510", {}),
                                    },
                                ),
                                "ReserveIds": (
                                    "M",
                                    "i=25505",
                                    {
                                        "InputArguments": ("V", "i=25506", {}),
                                        "OutputArguments": ("V", "i=25507", {}),
                                    },
                                ),
                            },
                        ),
                        "Read": (
                            "M",
                            "i=11585",
                            {
                                "InputArguments": ("V", "i=11586", {}),
                                "OutputArguments": ("V", "i=11587", {}),
                            },
                        ),
                        "SetPosition": (
                            "M",
                            "i=11593",
                            {"InputArguments": ("V", "i=11594", {})},
                        ),
                        "Size": ("V", "i=11576", {}),
                        "TrustListType": (
                            "OT",
                            "i=12522",
                            {
                                "ActivityTimeout": ("V", "i=32254", {}),
                                "AddCertificate": (
                                    "M",
                                    "i=12548",
                                    {"InputArguments": ("V", "i=12549", {})},
                                ),
                                "CloseAndUpdate": (
                                    "M",
                                    "i=12546",
                                    {
                                        "InputArguments": ("V", "i=12705", {}),
                                        "OutputArguments": ("V", "i=12547", {}),
                                    },
                                ),
                                "DefaultValidationOptions": ("V", "i=23563", {}),
                                "LastUpdateTime": ("V", "i=12542", {}),
                                "OpenWithMasks": (
                                    "M",
                                    "i=12543",
                                    {
                                        "InputArguments": ("V", "i=12544", {}),
                                        "OutputArguments": ("V", "i=12545", {}),
                                    },
                                ),
                                "RemoveCertificate": (
                                    "M",
                                    "i=12550",
                                    {"InputArguments": ("V", "i=12551", {})},
                                ),
                                "UpdateFrequency": ("V", "i=19296", {}),
                            },
                        ),
                        "UserWritable": ("V", "i=12687", {}),
                        "Writable": ("V", "i=12686", {}),
                        "Write": (
                            "M",
                            "i=11588",
                            {"InputArguments": ("V", "i=11589", {})},
                        ),
                    },
                ),
                "FolderType": (
                    "OT",
                    "i=61",
                    {
                        "AlarmGroupType": (
                            "OT",
                            "i=16405",
                            {"AlarmSuppressionGroupType": ("OT", "i=32064", {})},
                        ),
                        "AliasNameCategoryType": (
                            "OT",
                            "i=23456",
                            {
                                "<Alias>": ("O", "i=23457", {}),
                                "<SubAliasNameCategories>": (
                                    "O",
                                    "i=23458",
                                    {
                                        "FindAlias": (
                                            "M",
                                            "i=23459",
                                            {
                                                "InputArguments": ("V", "i=23460", {}),
                                                "OutputArguments": ("V", "i=23461", {}),
                                            },
                                        ),
                                        "LastChange": ("V", "i=32849", {}),
                                    },
                                ),
                                "FindAlias": (
                                    "M",
                                    "i=23462",
                                    {
                                        "InputArguments": ("V", "i=23463", {}),
                                        "OutputArguments": ("V", "i=23464", {}),
                                    },
                                ),
                                "LastChange": ("V", "i=32850", {}),
                            },
                        ),
                        "ApplicationConfigurationFolderType": (
                            "OT",
                            "i=16662",
                            {
                                "<ApplicationName>": (
                                    "O",
                                    "i=16663",
                                    {
                                        "ApplicationType": ("V", "i=18527", {}),
                                        "ApplicationUri": ("V", "i=18525", {}),
                                        "ApplyChanges": ("M", "i=18539", {}),
                                        "CertificateGroups": (
                                            "O",
                                            "i=16707",
                                            {
                                                "DefaultApplicationGroup": (
                                                    "O",
                                                    "i=16708",
                                                    {
                                                        "CertificateTypes": (
                                                            "V",
                                                            "i=16751",
                                                            {},
                                                        ),
                                                        "TrustList": (
                                                            "O",
                                                            "i=16709",
                                                            {
                                                                "AddCertificate": (
                                                                    "M",
                                                                    "i=16747",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=16748",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "Close": (
                                                                    "M",
                                                                    "i=16724",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=16725",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "CloseAndUpdate": (
                                                                    "M",
                                                                    "i=16744",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=16745",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=16746",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "GetPosition": (
                                                                    "M",
                                                                    "i=16732",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=16733",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=16734",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "LastUpdateTime": (
                                                                    "V",
                                                                    "i=16737",
                                                                    {},
                                                                ),
                                                                "Open": (
                                                                    "M",
                                                                    "i=16717",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=16722",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=16723",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "OpenCount": (
                                                                    "V",
                                                                    "i=16713",
                                                                    {},
                                                                ),
                                                                "OpenWithMasks": (
                                                                    "M",
                                                                    "i=16741",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=16742",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=16743",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "Read": (
                                                                    "M",
                                                                    "i=16726",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=16727",
                                                                            {},
                                                                        ),
                                                                        "OutputArguments": (
                                                                            "V",
                                                                            "i=16728",
                                                                            {},
                                                                        ),
                                                                    },
                                                                ),
                                                                "RemoveCertificate": (
                                                                    "M",
                                                                    "i=16749",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=16750",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "SetPosition": (
                                                                    "M",
                                                                    "i=16735",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=16736",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                                "Size": (
                                                                    "V",
                                                                    "i=16710",
                                                                    {},
                                                                ),
                                                                "UserWritable": (
                                                                    "V",
                                                                    "i=16712",
                                                                    {},
                                                                ),
                                                                "Writable": (
                                                                    "V",
                                                                    "i=16711",
                                                                    {},
                                                                ),
                                                                "Write": (
                                                                    "M",
                                                                    "i=16729",
                                                                    {
                                                                        "InputArguments": (
                                                                            "V",
                                                                            "i=16730",
                                                                            {},
                                                                        )
                                                                    },
                                                                ),
                                                            },
                                                        ),
                                                    },
                                                )
                                            },
                                        ),
                                        "CreateSigningRequest": (
                                            "M",
                                            "i=18541",
                                            {
                                                "InputArguments": ("V", "i=18542", {}),
                                                "OutputArguments": ("V", "i=18543", {}),
                                            },
                                        ),
                                        "Enabled": ("V", "i=18592", {}),
                                        "GetRejectedList": (
                                            "M",
                                            "i=18544",
                                            {"OutputArguments": ("V", "i=18545", {})},
                                        ),
                                        "MaxTrustListSize": ("V", "i=18530", {}),
                                        "MulticastDnsEnabled": ("V", "i=18531", {}),
                                        "ProductUri": ("V", "i=18526", {}),
                                        "ServerCapabilities": ("V", "i=18528", {}),
                                        "SupportedPrivateKeyFormats": (
                                            "V",
                                            "i=18529",
                                            {},
                                        ),
                                        "UpdateCertificate": (
                                            "M",
                                            "i=18533",
                                            {
                                                "InputArguments": ("V", "i=18534", {}),
                                                "OutputArguments": ("V", "i=18535", {}),
                                            },
                                        ),
                                    },
                                )
                            },
                        ),
                        "AuthorizationServicesConfigurationFolderType": (
                            "OT",
                            "i=23556",
                            {
                                "<ServiceName>": (
                                    "O",
                                    "i=23557",
                                    {
                                        "IssuerEndpointUrl": ("V", "i=23560", {}),
                                        "ServiceCertificate": ("V", "i=23559", {}),
                                        "ServiceUri": ("V", "i=23558", {}),
                                    },
                                )
                            },
                        ),
                        "CertificateGroupFolderType": (
                            "OT",
                            "i=13813",
                            {
                                "<AdditionalGroup>": (
                                    "O",
                                    "i=13916",
                                    {
                                        "CertificateTypes": ("V", "i=13949", {}),
                                        "TrustList": (
                                            "O",
                                            "i=13917",
                                            {
                                                "AddCertificate": (
                                                    "M",
                                                    "i=13945",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13946",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Close": (
                                                    "M",
                                                    "i=13926",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13927",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "CloseAndUpdate": (
                                                    "M",
                                                    "i=13942",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13943",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13944",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "GetPosition": (
                                                    "M",
                                                    "i=13933",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13934",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13935",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "LastUpdateTime": ("V", "i=13938", {}),
                                                "Open": (
                                                    "M",
                                                    "i=13923",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13924",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13925",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "OpenCount": ("V", "i=13921", {}),
                                                "OpenWithMasks": (
                                                    "M",
                                                    "i=13939",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13940",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13941",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "Read": (
                                                    "M",
                                                    "i=13928",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13929",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13930",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "RemoveCertificate": (
                                                    "M",
                                                    "i=13947",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13948",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "SetPosition": (
                                                    "M",
                                                    "i=13936",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13937",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Size": ("V", "i=13918", {}),
                                                "UserWritable": ("V", "i=13920", {}),
                                                "Writable": ("V", "i=13919", {}),
                                                "Write": (
                                                    "M",
                                                    "i=13931",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13932",
                                                            {},
                                                        )
                                                    },
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "DefaultApplicationGroup": (
                                    "O",
                                    "i=13814",
                                    {
                                        "CertificateTypes": ("V", "i=13847", {}),
                                        "TrustList": (
                                            "O",
                                            "i=13815",
                                            {
                                                "AddCertificate": (
                                                    "M",
                                                    "i=13843",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13844",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Close": (
                                                    "M",
                                                    "i=13824",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13825",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "CloseAndUpdate": (
                                                    "M",
                                                    "i=13840",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13841",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13842",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "GetPosition": (
                                                    "M",
                                                    "i=13831",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13832",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13833",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "LastUpdateTime": ("V", "i=13836", {}),
                                                "Open": (
                                                    "M",
                                                    "i=13821",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13822",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13823",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "OpenCount": ("V", "i=13819", {}),
                                                "OpenWithMasks": (
                                                    "M",
                                                    "i=13837",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13838",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13839",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "Read": (
                                                    "M",
                                                    "i=13826",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13827",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13828",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "RemoveCertificate": (
                                                    "M",
                                                    "i=13845",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13846",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "SetPosition": (
                                                    "M",
                                                    "i=13834",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13835",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Size": ("V", "i=13816", {}),
                                                "UserWritable": ("V", "i=13818", {}),
                                                "Writable": ("V", "i=13817", {}),
                                                "Write": (
                                                    "M",
                                                    "i=13829",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13830",
                                                            {},
                                                        )
                                                    },
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "DefaultHttpsGroup": (
                                    "O",
                                    "i=13848",
                                    {
                                        "CertificateTypes": ("V", "i=13881", {}),
                                        "TrustList": (
                                            "O",
                                            "i=13849",
                                            {
                                                "AddCertificate": (
                                                    "M",
                                                    "i=13877",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13878",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Close": (
                                                    "M",
                                                    "i=13858",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13859",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "CloseAndUpdate": (
                                                    "M",
                                                    "i=13874",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13875",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13876",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "GetPosition": (
                                                    "M",
                                                    "i=13865",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13866",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13867",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "LastUpdateTime": ("V", "i=13870", {}),
                                                "Open": (
                                                    "M",
                                                    "i=13855",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13856",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13857",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "OpenCount": ("V", "i=13853", {}),
                                                "OpenWithMasks": (
                                                    "M",
                                                    "i=13871",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13872",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13873",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "Read": (
                                                    "M",
                                                    "i=13860",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13861",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13862",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "RemoveCertificate": (
                                                    "M",
                                                    "i=13879",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13880",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "SetPosition": (
                                                    "M",
                                                    "i=13868",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13869",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Size": ("V", "i=13850", {}),
                                                "UserWritable": ("V", "i=13852", {}),
                                                "Writable": ("V", "i=13851", {}),
                                                "Write": (
                                                    "M",
                                                    "i=13863",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13864",
                                                            {},
                                                        )
                                                    },
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "DefaultUserTokenGroup": (
                                    "O",
                                    "i=13882",
                                    {
                                        "CertificateTypes": ("V", "i=13915", {}),
                                        "TrustList": (
                                            "O",
                                            "i=13883",
                                            {
                                                "AddCertificate": (
                                                    "M",
                                                    "i=13911",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13912",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Close": (
                                                    "M",
                                                    "i=13892",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13893",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "CloseAndUpdate": (
                                                    "M",
                                                    "i=13908",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13909",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13910",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "GetPosition": (
                                                    "M",
                                                    "i=13899",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13900",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13901",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "LastUpdateTime": ("V", "i=13904", {}),
                                                "Open": (
                                                    "M",
                                                    "i=13889",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13890",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13891",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "OpenCount": ("V", "i=13887", {}),
                                                "OpenWithMasks": (
                                                    "M",
                                                    "i=13905",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13906",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13907",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "Read": (
                                                    "M",
                                                    "i=13894",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13895",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13896",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "RemoveCertificate": (
                                                    "M",
                                                    "i=13913",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13914",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "SetPosition": (
                                                    "M",
                                                    "i=13902",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13903",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Size": ("V", "i=13884", {}),
                                                "UserWritable": ("V", "i=13886", {}),
                                                "Writable": ("V", "i=13885", {}),
                                                "Write": (
                                                    "M",
                                                    "i=13897",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13898",
                                                            {},
                                                        )
                                                    },
                                                ),
                                            },
                                        ),
                                    },
                                ),
                            },
                        ),
                        "DataSetFolderType": (
                            "OT",
                            "i=14477",
                            {
                                "<DataSetFolderName>": (
                                    "O",
                                    "i=14478",
                                    {
                                        "AddDataSetFolder": (
                                            "M",
                                            "i=16884",
                                            {
                                                "InputArguments": ("V", "i=16894", {}),
                                                "OutputArguments": ("V", "i=16922", {}),
                                            },
                                        ),
                                        "AddPublishedDataItems": (
                                            "M",
                                            "i=14479",
                                            {
                                                "InputArguments": ("V", "i=14480", {}),
                                                "OutputArguments": ("V", "i=14481", {}),
                                            },
                                        ),
                                        "AddPublishedDataItemsTemplate": (
                                            "M",
                                            "i=16842",
                                            {
                                                "InputArguments": ("V", "i=16843", {}),
                                                "OutputArguments": ("V", "i=16853", {}),
                                            },
                                        ),
                                        "AddPublishedEvents": (
                                            "M",
                                            "i=14482",
                                            {
                                                "InputArguments": ("V", "i=14483", {}),
                                                "OutputArguments": ("V", "i=14484", {}),
                                            },
                                        ),
                                        "AddPublishedEventsTemplate": (
                                            "M",
                                            "i=16881",
                                            {
                                                "InputArguments": ("V", "i=16882", {}),
                                                "OutputArguments": ("V", "i=16883", {}),
                                            },
                                        ),
                                        "RemoveDataSetFolder": (
                                            "M",
                                            "i=16923",
                                            {"InputArguments": ("V", "i=16924", {})},
                                        ),
                                        "RemovePublishedDataSet": (
                                            "M",
                                            "i=14485",
                                            {"InputArguments": ("V", "i=14486", {})},
                                        ),
                                    },
                                ),
                                "<PublishedDataSetName>": (
                                    "O",
                                    "i=14487",
                                    {
                                        "ConfigurationVersion": ("V", "i=14489", {}),
                                        "DataSetMetaData": ("V", "i=15221", {}),
                                    },
                                ),
                                "AddDataSetFolder": (
                                    "M",
                                    "i=16994",
                                    {
                                        "InputArguments": ("V", "i=16995", {}),
                                        "OutputArguments": ("V", "i=16996", {}),
                                    },
                                ),
                                "AddPublishedDataItems": (
                                    "M",
                                    "i=14493",
                                    {
                                        "InputArguments": ("V", "i=14494", {}),
                                        "OutputArguments": ("V", "i=14495", {}),
                                    },
                                ),
                                "AddPublishedDataItemsTemplate": (
                                    "M",
                                    "i=16935",
                                    {
                                        "InputArguments": ("V", "i=16958", {}),
                                        "OutputArguments": ("V", "i=16959", {}),
                                    },
                                ),
                                "AddPublishedEvents": (
                                    "M",
                                    "i=14496",
                                    {
                                        "InputArguments": ("V", "i=14497", {}),
                                        "OutputArguments": ("V", "i=14498", {}),
                                    },
                                ),
                                "AddPublishedEventsTemplate": (
                                    "M",
                                    "i=16960",
                                    {
                                        "InputArguments": ("V", "i=16961", {}),
                                        "OutputArguments": ("V", "i=16971", {}),
                                    },
                                ),
                                "RemoveDataSetFolder": (
                                    "M",
                                    "i=16997",
                                    {"InputArguments": ("V", "i=17007", {})},
                                ),
                                "RemovePublishedDataSet": (
                                    "M",
                                    "i=14499",
                                    {"InputArguments": ("V", "i=14500", {})},
                                ),
                            },
                        ),
                        "DictionaryFolderType": (
                            "OT",
                            "i=17591",
                            {
                                "<DictionaryEntryName>": ("O", "i=17593", {}),
                                "<DictionaryFolderName>": ("O", "i=17592", {}),
                            },
                        ),
                        "FileDirectoryType": (
                            "OT",
                            "i=13353",
                            {
                                "<FileDirectoryName>": (
                                    "O",
                                    "i=13354",
                                    {
                                        "CreateDirectory": (
                                            "M",
                                            "i=13355",
                                            {
                                                "InputArguments": ("V", "i=13356", {}),
                                                "OutputArguments": ("V", "i=13357", {}),
                                            },
                                        ),
                                        "CreateFile": (
                                            "M",
                                            "i=13358",
                                            {
                                                "InputArguments": ("V", "i=13359", {}),
                                                "OutputArguments": ("V", "i=13360", {}),
                                            },
                                        ),
                                        "Delete": (
                                            "M",
                                            "i=17718",
                                            {"InputArguments": ("V", "i=17719", {})},
                                        ),
                                        "MoveOrCopy": (
                                            "M",
                                            "i=13363",
                                            {
                                                "InputArguments": ("V", "i=13364", {}),
                                                "OutputArguments": ("V", "i=13365", {}),
                                            },
                                        ),
                                    },
                                ),
                                "<FileName>": (
                                    "O",
                                    "i=13366",
                                    {
                                        "Close": (
                                            "M",
                                            "i=13375",
                                            {"InputArguments": ("V", "i=13376", {})},
                                        ),
                                        "GetPosition": (
                                            "M",
                                            "i=13382",
                                            {
                                                "InputArguments": ("V", "i=13383", {}),
                                                "OutputArguments": ("V", "i=13384", {}),
                                            },
                                        ),
                                        "Open": (
                                            "M",
                                            "i=13372",
                                            {
                                                "InputArguments": ("V", "i=13373", {}),
                                                "OutputArguments": ("V", "i=13374", {}),
                                            },
                                        ),
                                        "OpenCount": ("V", "i=13370", {}),
                                        "Read": (
                                            "M",
                                            "i=13377",
                                            {
                                                "InputArguments": ("V", "i=13378", {}),
                                                "OutputArguments": ("V", "i=13379", {}),
                                            },
                                        ),
                                        "SetPosition": (
                                            "M",
                                            "i=13385",
                                            {"InputArguments": ("V", "i=13386", {})},
                                        ),
                                        "Size": ("V", "i=13367", {}),
                                        "UserWritable": ("V", "i=13369", {}),
                                        "Writable": ("V", "i=13368", {}),
                                        "Write": (
                                            "M",
                                            "i=13380",
                                            {"InputArguments": ("V", "i=13381", {})},
                                        ),
                                    },
                                ),
                                "CreateDirectory": (
                                    "M",
                                    "i=13387",
                                    {
                                        "InputArguments": ("V", "i=13388", {}),
                                        "OutputArguments": ("V", "i=13389", {}),
                                    },
                                ),
                                "CreateFile": (
                                    "M",
                                    "i=13390",
                                    {
                                        "InputArguments": ("V", "i=13391", {}),
                                        "OutputArguments": ("V", "i=13392", {}),
                                    },
                                ),
                                "Delete": (
                                    "M",
                                    "i=13393",
                                    {"InputArguments": ("V", "i=13394", {})},
                                ),
                                "MoveOrCopy": (
                                    "M",
                                    "i=13395",
                                    {
                                        "InputArguments": ("V", "i=13396", {}),
                                        "OutputArguments": ("V", "i=13397", {}),
                                    },
                                ),
                            },
                        ),
                        "KeyCredentialConfigurationFolderType": (
                            "OT",
                            "i=17496",
                            {
                                "<ServiceName>": (
                                    "O",
                                    "i=17511",
                                    {
                                        "ProfileUri": ("V", "i=17513", {}),
                                        "ResourceUri": ("V", "i=17512", {}),
                                    },
                                ),
                                "CreateCredential": (
                                    "M",
                                    "i=17522",
                                    {
                                        "InputArguments": ("V", "i=17523", {}),
                                        "OutputArguments": ("V", "i=17524", {}),
                                    },
                                ),
                            },
                        ),
                        "OperationLimitsType": (
                            "OT",
                            "i=11564",
                            {
                                "MaxMonitoredItemsPerCall": ("V", "i=11574", {}),
                                "MaxNodesPerBrowse": ("V", "i=11570", {}),
                                "MaxNodesPerHistoryReadData": ("V", "i=12161", {}),
                                "MaxNodesPerHistoryReadEvents": ("V", "i=12162", {}),
                                "MaxNodesPerHistoryUpdateData": ("V", "i=12163", {}),
                                "MaxNodesPerHistoryUpdateEvents": ("V", "i=12164", {}),
                                "MaxNodesPerMethodCall": ("V", "i=11569", {}),
                                "MaxNodesPerNodeManagement": ("V", "i=11573", {}),
                                "MaxNodesPerRead": ("V", "i=11565", {}),
                                "MaxNodesPerRegisterNodes": ("V", "i=11571", {}),
                                "MaxNodesPerTranslateBrowsePathsToNodeIds": (
                                    "V",
                                    "i=11572",
                                    {},
                                ),
                                "MaxNodesPerWrite": ("V", "i=11567", {}),
                            },
                        ),
                        "PubSubKeyPushTargetFolderType": (
                            "OT",
                            "i=25346",
                            {
                                "<PushTargetFolderName>": (
                                    "O",
                                    "i=25347",
                                    {
                                        "AddPushTarget": (
                                            "M",
                                            "i=25348",
                                            {
                                                "InputArguments": ("V", "i=25349", {}),
                                                "OutputArguments": ("V", "i=25350", {}),
                                            },
                                        ),
                                        "AddPushTargetFolder": (
                                            "M",
                                            "i=25353",
                                            {
                                                "InputArguments": ("V", "i=25354", {}),
                                                "OutputArguments": ("V", "i=25355", {}),
                                            },
                                        ),
                                        "RemovePushTarget": (
                                            "M",
                                            "i=25351",
                                            {"InputArguments": ("V", "i=25352", {})},
                                        ),
                                        "RemovePushTargetFolder": (
                                            "M",
                                            "i=25356",
                                            {"InputArguments": ("V", "i=25357", {})},
                                        ),
                                    },
                                ),
                                "<PushTargetName>": (
                                    "O",
                                    "i=25358",
                                    {
                                        "ApplicationUri": ("V", "i=25648", {}),
                                        "ConnectSecurityGroups": (
                                            "M",
                                            "i=25655",
                                            {
                                                "InputArguments": ("V", "i=25656", {}),
                                                "OutputArguments": ("V", "i=25657", {}),
                                            },
                                        ),
                                        "DisconnectSecurityGroups": (
                                            "M",
                                            "i=25658",
                                            {
                                                "InputArguments": ("V", "i=25659", {}),
                                                "OutputArguments": ("V", "i=25660", {}),
                                            },
                                        ),
                                        "EndpointUrl": ("V", "i=25649", {}),
                                        "LastPushErrorTime": ("V", "i=25654", {}),
                                        "LastPushExecutionTime": ("V", "i=25653", {}),
                                        "RequestedKeyCount": ("V", "i=25651", {}),
                                        "RetryInterval": ("V", "i=25652", {}),
                                        "SecurityPolicyUri": ("V", "i=25361", {}),
                                        "TriggerKeyUpdate": ("M", "i=25661", {}),
                                        "UserTokenType": ("V", "i=25650", {}),
                                    },
                                ),
                                "AddPushTarget": (
                                    "M",
                                    "i=25366",
                                    {
                                        "InputArguments": ("V", "i=25367", {}),
                                        "OutputArguments": ("V", "i=25368", {}),
                                    },
                                ),
                                "AddPushTargetFolder": (
                                    "M",
                                    "i=25371",
                                    {
                                        "InputArguments": ("V", "i=25372", {}),
                                        "OutputArguments": ("V", "i=25373", {}),
                                    },
                                ),
                                "RemovePushTarget": (
                                    "M",
                                    "i=25369",
                                    {"InputArguments": ("V", "i=25370", {})},
                                ),
                                "RemovePushTargetFolder": (
                                    "M",
                                    "i=25374",
                                    {"InputArguments": ("V", "i=25375", {})},
                                ),
                            },
                        ),
                        "SecurityGroupFolderType": (
                            "OT",
                            "i=15452",
                            {
                                "<SecurityGroupFolderName>": (
                                    "O",
                                    "i=15453",
                                    {
                                        "AddSecurityGroup": (
                                            "M",
                                            "i=15454",
                                            {
                                                "InputArguments": ("V", "i=15455", {}),
                                                "OutputArguments": ("V", "i=15456", {}),
                                            },
                                        ),
                                        "AddSecurityGroupFolder": (
                                            "M",
                                            "i=25293",
                                            {
                                                "InputArguments": ("V", "i=25294", {}),
                                                "OutputArguments": ("V", "i=25295", {}),
                                            },
                                        ),
                                        "RemoveSecurityGroup": (
                                            "M",
                                            "i=15457",
                                            {"InputArguments": ("V", "i=15458", {})},
                                        ),
                                        "RemoveSecurityGroupFolder": (
                                            "M",
                                            "i=25296",
                                            {"InputArguments": ("V", "i=25297", {})},
                                        ),
                                        "SupportedSecurityPolicyUris": (
                                            "V",
                                            "i=25298",
                                            {},
                                        ),
                                    },
                                ),
                                "<SecurityGroupName>": (
                                    "O",
                                    "i=15459",
                                    {
                                        "KeyLifetime": ("V", "i=15010", {}),
                                        "MaxFutureKeyCount": ("V", "i=15012", {}),
                                        "MaxPastKeyCount": ("V", "i=15043", {}),
                                        "SecurityGroupId": ("V", "i=15460", {}),
                                        "SecurityPolicyUri": ("V", "i=15011", {}),
                                    },
                                ),
                                "AddSecurityGroup": (
                                    "M",
                                    "i=15461",
                                    {
                                        "InputArguments": ("V", "i=15462", {}),
                                        "OutputArguments": ("V", "i=15463", {}),
                                    },
                                ),
                                "AddSecurityGroupFolder": (
                                    "M",
                                    "i=25312",
                                    {
                                        "InputArguments": ("V", "i=25313", {}),
                                        "OutputArguments": ("V", "i=25314", {}),
                                    },
                                ),
                                "RemoveSecurityGroup": (
                                    "M",
                                    "i=15464",
                                    {"InputArguments": ("V", "i=15465", {})},
                                ),
                                "RemoveSecurityGroupFolder": (
                                    "M",
                                    "i=25315",
                                    {"InputArguments": ("V", "i=25316", {})},
                                ),
                                "SupportedSecurityPolicyUris": ("V", "i=25317", {}),
                            },
                        ),
                        "SubscribedDataSetFolderType": (
                            "OT",
                            "i=23795",
                            {
                                "<StandaloneSubscribedDataSetName>": (
                                    "O",
                                    "i=23807",
                                    {
                                        "DataSetMetaData": ("V", "i=23809", {}),
                                        "IsConnected": ("V", "i=23810", {}),
                                        "SubscribedDataSet": ("O", "i=23808", {}),
                                    },
                                ),
                                "<SubscribedDataSetFolderName>": (
                                    "O",
                                    "i=23796",
                                    {
                                        "AddDataSetFolder": (
                                            "M",
                                            "i=23802",
                                            {
                                                "InputArguments": ("V", "i=23803", {}),
                                                "OutputArguments": ("V", "i=23804", {}),
                                            },
                                        ),
                                        "AddSubscribedDataSet": (
                                            "M",
                                            "i=23797",
                                            {
                                                "InputArguments": ("V", "i=23798", {}),
                                                "OutputArguments": ("V", "i=23799", {}),
                                            },
                                        ),
                                        "RemoveDataSetFolder": (
                                            "M",
                                            "i=23805",
                                            {"InputArguments": ("V", "i=23806", {})},
                                        ),
                                        "RemoveSubscribedDataSet": (
                                            "M",
                                            "i=23800",
                                            {"InputArguments": ("V", "i=23801", {})},
                                        ),
                                    },
                                ),
                                "AddDataSetFolder": (
                                    "M",
                                    "i=23816",
                                    {
                                        "InputArguments": ("V", "i=23817", {}),
                                        "OutputArguments": ("V", "i=23818", {}),
                                    },
                                ),
                                "AddSubscribedDataSet": (
                                    "M",
                                    "i=23811",
                                    {
                                        "InputArguments": ("V", "i=23812", {}),
                                        "OutputArguments": ("V", "i=23813", {}),
                                    },
                                ),
                                "RemoveDataSetFolder": (
                                    "M",
                                    "i=23819",
                                    {"InputArguments": ("V", "i=23820", {})},
                                ),
                                "RemoveSubscribedDataSet": (
                                    "M",
                                    "i=23814",
                                    {"InputArguments": ("V", "i=23815", {})},
                                ),
                            },
                        ),
                    },
                ),
                "HistoricalDataConfigurationType": (
                    "OT",
                    "i=2318",
                    {
                        "AggregateConfiguration": (
                            "O",
                            "i=3059",
                            {
                                "PercentDataBad": ("V", "i=11169", {}),
                                "PercentDataGood": ("V", "i=11170", {}),
                                "TreatUncertainAsBad": ("V", "i=11168", {}),
                                "UseSlopedExtrapolation": ("V", "i=11171", {}),
                            },
                        ),
                        "AggregateFunctions": ("O", "i=11876", {}),
                        "Definition": ("V", "i=2324", {}),
                        "ExceptionDeviation": ("V", "i=2327", {}),
                        "ExceptionDeviationFormat": ("V", "i=2328", {}),
                        "MaxCountStoredValues": ("V", "i=32620", {}),
                        "MaxTimeInterval": ("V", "i=2325", {}),
                        "MaxTimeStoredValues": ("V", "i=32619", {}),
                        "MinTimeInterval": ("V", "i=2326", {}),
                        "ServerTimestampSupported": ("V", "i=19092", {}),
                        "StartOfArchive": ("V", "i=11499", {}),
                        "StartOfOnlineArchive": ("V", "i=11500", {}),
                        "Stepped": ("V", "i=2323", {}),
                    },
                ),
                "HistoricalEventConfigurationType": (
                    "OT",
                    "i=32621",
                    {
                        "EventTypes": ("O", "i=32622", {}),
                        "SortByEventFields": ("V", "i=18644", {}),
                        "StartOfArchive": ("V", "i=32623", {}),
                        "StartOfOnlineArchive": ("V", "i=32624", {}),
                    },
                ),
                "HistoricalExternalEventSourceType": (
                    "OT",
                    "i=32625",
                    {
                        "EndpointUrl": ("V", "i=32627", {}),
                        "HistoricalEventFilter": ("V", "i=32632", {}),
                        "IdentityTokenPolicy": ("V", "i=32630", {}),
                        "SecurityMode": ("V", "i=32628", {}),
                        "SecurityPolicyUri": ("V", "i=32629", {}),
                        "Server": ("V", "i=32626", {}),
                        "TransportProfileUri": ("V", "i=32631", {}),
                    },
                ),
                "HistoryServerCapabilitiesType": (
                    "OT",
                    "i=2330",
                    {
                        "AccessHistoryDataCapability": ("V", "i=2331", {}),
                        "AccessHistoryEventsCapability": ("V", "i=2332", {}),
                        "AggregateFunctions": ("O", "i=11172", {}),
                        "DeleteAtTimeCapability": ("V", "i=2338", {}),
                        "DeleteEventCapability": ("V", "i=11501", {}),
                        "DeleteRawCapability": ("V", "i=2337", {}),
                        "InsertAnnotationCapability": ("V", "i=11270", {}),
                        "InsertDataCapability": ("V", "i=2334", {}),
                        "InsertEventCapability": ("V", "i=11278", {}),
                        "MaxReturnDataValues": ("V", "i=11268", {}),
                        "MaxReturnEventValues": ("V", "i=11269", {}),
                        "ReplaceDataCapability": ("V", "i=2335", {}),
                        "ReplaceEventCapability": ("V", "i=11279", {}),
                        "ServerTimestampSupported": ("V", "i=19094", {}),
                        "UpdateDataCapability": ("V", "i=2336", {}),
                        "UpdateEventCapability": ("V", "i=11280", {}),
                    },
                ),
                "IetfBaseNetworkInterfaceType": (
                    "OT",
                    "i=25221",
                    {
                        "AdminStatus": ("V", "i=25222", {}),
                        "OperStatus": ("V", "i=25223", {}),
                        "PhysAddress": ("V", "i=25224", {}),
                        "Speed": (
                            "V",
                            "i=25225",
                            {"EngineeringUnits": ("V", "i=25252", {})},
                        ),
                    },
                ),
                "KeyCredentialConfigurationType": (
                    "OT",
                    "i=18001",
                    {
                        "CredentialId": ("V", "i=18657", {}),
                        "DeleteCredential": ("M", "i=18008", {}),
                        "EndpointUrls": ("V", "i=18004", {}),
                        "GetEncryptingKey": (
                            "M",
                            "i=17534",
                            {
                                "InputArguments": ("V", "i=17535", {}),
                                "OutputArguments": ("V", "i=17536", {}),
                            },
                        ),
                        "ProfileUri": ("V", "i=18165", {}),
                        "ResourceUri": ("V", "i=18069", {}),
                        "ServiceStatus": ("V", "i=18005", {}),
                        "UpdateCredential": (
                            "M",
                            "i=18006",
                            {"InputArguments": ("V", "i=18007", {})},
                        ),
                    },
                ),
                "LldpInformationType": (
                    "OT",
                    "i=18973",
                    {
                        "LocalSystemData": (
                            "O",
                            "i=18980",
                            {
                                "ChassisId": ("V", "i=18982", {}),
                                "ChassisIdSubtype": ("V", "i=18981", {}),
                                "SystemDescription": ("V", "i=18984", {}),
                                "SystemName": ("V", "i=18983", {}),
                            },
                        ),
                        "Ports": (
                            "O",
                            "i=18987",
                            {
                                "<LldpPortInformation>": (
                                    "O",
                                    "i=18988",
                                    {
                                        "DestMacAddress": ("V", "i=18990", {}),
                                        "IetfBaseNetworkInterfaceName": (
                                            "V",
                                            "i=18989",
                                            {},
                                        ),
                                        "PortId": ("V", "i=18992", {}),
                                        "PortIdSubtype": ("V", "i=18991", {}),
                                    },
                                )
                            },
                        ),
                        "RemoteStatistics": (
                            "O",
                            "i=18974",
                            {
                                "LastChangeTime": ("V", "i=18975", {}),
                                "RemoteAgeouts": ("V", "i=18979", {}),
                                "RemoteDeletes": ("V", "i=18977", {}),
                                "RemoteDrops": ("V", "i=18978", {}),
                                "RemoteInserts": ("V", "i=18976", {}),
                            },
                        ),
                    },
                ),
                "LldpLocalSystemType": (
                    "OT",
                    "i=19002",
                    {
                        "ChassisId": ("V", "i=19004", {}),
                        "ChassisIdSubtype": ("V", "i=19003", {}),
                        "SystemCapabilitiesEnabled": ("V", "i=19008", {}),
                        "SystemCapabilitiesSupported": ("V", "i=19007", {}),
                        "SystemDescription": ("V", "i=19006", {}),
                        "SystemName": ("V", "i=19005", {}),
                    },
                ),
                "LldpPortInformationType": (
                    "OT",
                    "i=19009",
                    {
                        "DestMacAddress": ("V", "i=19011", {}),
                        "IetfBaseNetworkInterfaceName": ("V", "i=19010", {}),
                        "ManagementAddressTxPort": ("V", "i=19015", {}),
                        "PortDescription": ("V", "i=19014", {}),
                        "PortId": ("V", "i=19013", {}),
                        "PortIdSubtype": ("V", "i=19012", {}),
                        "RemoteSystemsData": (
                            "O",
                            "i=19016",
                            {
                                "<LldpRemoteSystem>": (
                                    "O",
                                    "i=19017",
                                    {
                                        "ChassisId": ("V", "i=19021", {}),
                                        "ChassisIdSubtype": ("V", "i=19020", {}),
                                        "PortId": ("V", "i=19023", {}),
                                        "PortIdSubtype": ("V", "i=19022", {}),
                                        "RemoteIndex": ("V", "i=19019", {}),
                                        "TimeMark": ("V", "i=19018", {}),
                                    },
                                )
                            },
                        ),
                    },
                ),
                "LldpRemoteStatisticsType": (
                    "OT",
                    "i=18996",
                    {
                        "LastChangeTime": ("V", "i=18997", {}),
                        "RemoteAgeouts": ("V", "i=19001", {}),
                        "RemoteDeletes": ("V", "i=18999", {}),
                        "RemoteDrops": ("V", "i=19000", {}),
                        "RemoteInserts": ("V", "i=18998", {}),
                    },
                ),
                "LldpRemoteSystemType": (
                    "OT",
                    "i=19033",
                    {
                        "ChassisId": ("V", "i=19037", {}),
                        "ChassisIdSubtype": ("V", "i=19036", {}),
                        "ManagementAddress": ("V", "i=19047", {}),
                        "PortDescription": ("V", "i=19040", {}),
                        "PortId": ("V", "i=19039", {}),
                        "PortIdSubtype": ("V", "i=19038", {}),
                        "RemoteChanges": ("V", "i=19045", {}),
                        "RemoteIndex": ("V", "i=19035", {}),
                        "RemoteTooManyNeighbors": ("V", "i=19046", {}),
                        "RemoteUnknownTlv": ("V", "i=19078", {}),
                        "SystemCapabilitiesEnabled": ("V", "i=19044", {}),
                        "SystemCapabilitiesSupported": ("V", "i=19043", {}),
                        "SystemDescription": ("V", "i=19042", {}),
                        "SystemName": ("V", "i=19041", {}),
                        "TimeMark": ("V", "i=19034", {}),
                    },
                ),
                "LogObjectType": (
                    "OT",
                    "i=19352",
                    {
                        "GetRecords": (
                            "M",
                            "i=19353",
                            {
                                "InputArguments": ("V", "i=19354", {}),
                                "OutputArguments": ("V", "i=19355", {}),
                            },
                        ),
                        "MaxRecords": ("V", "i=19356", {}),
                        "MaxStorageDuration": ("V", "i=19357", {}),
                        "MinimumSeverity": ("V", "i=19744", {}),
                    },
                ),
                "ModellingRuleType": ("OT", "i=77", {}),
                "NamespaceMetadataType": (
                    "OT",
                    "i=11616",
                    {
                        "ConfigurationVersion": ("V", "i=25267", {}),
                        "DefaultAccessRestrictions": ("V", "i=16139", {}),
                        "DefaultRolePermissions": ("V", "i=16137", {}),
                        "DefaultUserRolePermissions": ("V", "i=16138", {}),
                        "IsNamespaceSubset": ("V", "i=11620", {}),
                        "ModelVersion": ("V", "i=32419", {}),
                        "NamespaceFile": (
                            "O",
                            "i=11624",
                            {
                                "Close": (
                                    "M",
                                    "i=11632",
                                    {"InputArguments": ("V", "i=11633", {})},
                                ),
                                "GetPosition": (
                                    "M",
                                    "i=11639",
                                    {
                                        "InputArguments": ("V", "i=11640", {}),
                                        "OutputArguments": ("V", "i=11641", {}),
                                    },
                                ),
                                "Open": (
                                    "M",
                                    "i=11629",
                                    {
                                        "InputArguments": ("V", "i=11630", {}),
                                        "OutputArguments": ("V", "i=11631", {}),
                                    },
                                ),
                                "OpenCount": ("V", "i=11628", {}),
                                "Read": (
                                    "M",
                                    "i=11634",
                                    {
                                        "InputArguments": ("V", "i=11635", {}),
                                        "OutputArguments": ("V", "i=11636", {}),
                                    },
                                ),
                                "SetPosition": (
                                    "M",
                                    "i=11642",
                                    {"InputArguments": ("V", "i=11643", {})},
                                ),
                                "Size": ("V", "i=11625", {}),
                                "UserWritable": ("V", "i=12691", {}),
                                "Writable": ("V", "i=12690", {}),
                                "Write": (
                                    "M",
                                    "i=11637",
                                    {"InputArguments": ("V", "i=11638", {})},
                                ),
                            },
                        ),
                        "NamespacePublicationDate": ("V", "i=11619", {}),
                        "NamespaceUri": ("V", "i=11617", {}),
                        "NamespaceVersion": ("V", "i=11618", {}),
                        "StaticNodeIdTypes": ("V", "i=11621", {}),
                        "StaticNumericNodeIdRange": ("V", "i=11622", {}),
                        "StaticStringNodeIdPattern": ("V", "i=11623", {}),
                    },
                ),
                "NamespacesType": (
                    "OT",
                    "i=11645",
                    {
                        "<NamespaceIdentifier>": (
                            "O",
                            "i=11646",
                            {
                                "IsNamespaceSubset": ("V", "i=11650", {}),
                                "NamespacePublicationDate": ("V", "i=11649", {}),
                                "NamespaceUri": ("V", "i=11647", {}),
                                "NamespaceVersion": ("V", "i=11648", {}),
                                "StaticNodeIdTypes": ("V", "i=11651", {}),
                                "StaticNumericNodeIdRange": ("V", "i=11652", {}),
                                "StaticStringNodeIdPattern": ("V", "i=11653", {}),
                            },
                        )
                    },
                ),
                "NetworkAddressType": (
                    "OT",
                    "i=21145",
                    {
                        "NetworkAddressUrlType": (
                            "OT",
                            "i=21147",
                            {"Url": ("V", "i=21149", {})},
                        ),
                        "NetworkInterface": (
                            "V",
                            "i=21146",
                            {"Selections": ("V", "i=17582", {})},
                        ),
                    },
                ),
                "OrderedListType": (
                    "OT",
                    "i=23518",
                    {"NodeVersion": ("V", "i=23525", {})},
                ),
                "PriorityMappingTableType": (
                    "OT",
                    "i=25227",
                    {
                        "AddPriorityMappingEntry": (
                            "M",
                            "i=25229",
                            {"InputArguments": ("V", "i=25230", {})},
                        ),
                        "DeletePriorityMappingEntry": (
                            "M",
                            "i=25231",
                            {"InputArguments": ("V", "i=25232", {})},
                        ),
                        "PriorityMapppingEntries": ("V", "i=25228", {}),
                    },
                ),
                "ProvisionableDeviceType": (
                    "OT",
                    "i=26871",
                    {
                        "<ApplicationName>": (
                            "O",
                            "i=26878",
                            {
                                "ApplicationType": ("V", "i=27999", {}),
                                "ApplicationUri": ("V", "i=27997", {}),
                                "ApplyChanges": ("M", "i=28008", {}),
                                "CertificateGroups": (
                                    "O",
                                    "i=26879",
                                    {
                                        "DefaultApplicationGroup": (
                                            "O",
                                            "i=26880",
                                            {
                                                "CertificateTypes": (
                                                    "V",
                                                    "i=26917",
                                                    {},
                                                ),
                                                "TrustList": (
                                                    "O",
                                                    "i=26881",
                                                    {
                                                        "AddCertificate": (
                                                            "M",
                                                            "i=26913",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=26914",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "Close": (
                                                            "M",
                                                            "i=26892",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=26893",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "CloseAndUpdate": (
                                                            "M",
                                                            "i=26910",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=26911",
                                                                    {},
                                                                ),
                                                                "OutputArguments": (
                                                                    "V",
                                                                    "i=26912",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "GetPosition": (
                                                            "M",
                                                            "i=26899",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=26900",
                                                                    {},
                                                                ),
                                                                "OutputArguments": (
                                                                    "V",
                                                                    "i=26901",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "LastUpdateTime": (
                                                            "V",
                                                            "i=26904",
                                                            {},
                                                        ),
                                                        "Open": (
                                                            "M",
                                                            "i=26889",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=26890",
                                                                    {},
                                                                ),
                                                                "OutputArguments": (
                                                                    "V",
                                                                    "i=26891",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "OpenCount": (
                                                            "V",
                                                            "i=26885",
                                                            {},
                                                        ),
                                                        "OpenWithMasks": (
                                                            "M",
                                                            "i=26907",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=26908",
                                                                    {},
                                                                ),
                                                                "OutputArguments": (
                                                                    "V",
                                                                    "i=26909",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "Read": (
                                                            "M",
                                                            "i=26894",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=26895",
                                                                    {},
                                                                ),
                                                                "OutputArguments": (
                                                                    "V",
                                                                    "i=26896",
                                                                    {},
                                                                ),
                                                            },
                                                        ),
                                                        "RemoveCertificate": (
                                                            "M",
                                                            "i=26915",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=26916",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "SetPosition": (
                                                            "M",
                                                            "i=26902",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=26903",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "Size": ("V", "i=26882", {}),
                                                        "UserWritable": (
                                                            "V",
                                                            "i=26884",
                                                            {},
                                                        ),
                                                        "Writable": (
                                                            "V",
                                                            "i=26883",
                                                            {},
                                                        ),
                                                        "Write": (
                                                            "M",
                                                            "i=26897",
                                                            {
                                                                "InputArguments": (
                                                                    "V",
                                                                    "i=26898",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                    },
                                                ),
                                            },
                                        )
                                    },
                                ),
                                "CreateSigningRequest": (
                                    "M",
                                    "i=28010",
                                    {
                                        "InputArguments": ("V", "i=28011", {}),
                                        "OutputArguments": ("V", "i=28012", {}),
                                    },
                                ),
                                "Enabled": ("V", "i=27996", {}),
                                "GetRejectedList": (
                                    "M",
                                    "i=28013",
                                    {"OutputArguments": ("V", "i=28014", {})},
                                ),
                                "MaxTrustListSize": ("V", "i=28002", {}),
                                "MulticastDnsEnabled": ("V", "i=28003", {}),
                                "ProductUri": ("V", "i=27998", {}),
                                "ServerCapabilities": ("V", "i=28000", {}),
                                "SupportedPrivateKeyFormats": ("V", "i=28001", {}),
                                "UpdateCertificate": (
                                    "M",
                                    "i=28005",
                                    {
                                        "InputArguments": ("V", "i=28006", {}),
                                        "OutputArguments": ("V", "i=28007", {}),
                                    },
                                ),
                            },
                        ),
                        "IsSingleton": ("V", "i=26872", {}),
                        "RequestTickets": (
                            "M",
                            "i=26873",
                            {"OutputArguments": ("V", "i=26874", {})},
                        ),
                        "SetRegistrarEndpoints": (
                            "M",
                            "i=26875",
                            {"InputArguments": ("V", "i=26876", {})},
                        ),
                    },
                ),
                "PubSubCapabilitiesType": (
                    "OT",
                    "i=23832",
                    {
                        "MaxDataSetReaders": ("V", "i=23837", {}),
                        "MaxDataSetWriters": ("V", "i=23836", {}),
                        "MaxDataSetWritersPerGroup": ("V", "i=32651", {}),
                        "MaxFieldsPerDataSet": ("V", "i=23838", {}),
                        "MaxNetworkMessageSizeBroker": ("V", "i=32653", {}),
                        "MaxNetworkMessageSizeDatagram": ("V", "i=32652", {}),
                        "MaxPubSubConnections": ("V", "i=23833", {}),
                        "MaxPublishedDataSets": ("V", "i=32846", {}),
                        "MaxPushTargets": ("V", "i=32845", {}),
                        "MaxReaderGroups": ("V", "i=23835", {}),
                        "MaxSecurityGroups": ("V", "i=32844", {}),
                        "MaxStandaloneSubscribedDataSets": ("V", "i=32847", {}),
                        "MaxWriterGroups": ("V", "i=23834", {}),
                        "SupportSecurityKeyPull": ("V", "i=32654", {}),
                        "SupportSecurityKeyPush": ("V", "i=32655", {}),
                        "SupportSecurityKeyServer": ("V", "i=32848", {}),
                    },
                ),
                "PubSubConnectionType": (
                    "OT",
                    "i=14209",
                    {
                        "AddReaderGroup": (
                            "M",
                            "i=17465",
                            {
                                "InputArguments": ("V", "i=17507", {}),
                                "OutputArguments": ("V", "i=17508", {}),
                            },
                        ),
                        "AddWriterGroup": (
                            "M",
                            "i=17427",
                            {
                                "InputArguments": ("V", "i=17428", {}),
                                "OutputArguments": ("V", "i=17456", {}),
                            },
                        ),
                        "Address": (
                            "O",
                            "i=14221",
                            {
                                "NetworkInterface": (
                                    "V",
                                    "i=17202",
                                    {"Selections": ("V", "i=17576", {})},
                                )
                            },
                        ),
                        "ConnectionProperties": ("V", "i=17485", {}),
                        "Diagnostics": (
                            "O",
                            "i=19241",
                            {
                                "Counters": (
                                    "O",
                                    "i=19255",
                                    {
                                        "StateDisabledByMethod": (
                                            "V",
                                            "i=19281",
                                            {
                                                "Active": ("V", "i=19282", {}),
                                                "Classification": ("V", "i=19283", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19284",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "StateError": (
                                            "V",
                                            "i=19256",
                                            {
                                                "Active": ("V", "i=19257", {}),
                                                "Classification": ("V", "i=19258", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19259",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "StateOperationalByMethod": (
                                            "V",
                                            "i=19261",
                                            {
                                                "Active": ("V", "i=19262", {}),
                                                "Classification": ("V", "i=19263", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19264",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "StateOperationalByParent": (
                                            "V",
                                            "i=19266",
                                            {
                                                "Active": ("V", "i=19267", {}),
                                                "Classification": ("V", "i=19268", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19269",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "StateOperationalFromError": (
                                            "V",
                                            "i=19271",
                                            {
                                                "Active": ("V", "i=19272", {}),
                                                "Classification": ("V", "i=19273", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19274",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "StatePausedByParent": (
                                            "V",
                                            "i=19276",
                                            {
                                                "Active": ("V", "i=19277", {}),
                                                "Classification": ("V", "i=19278", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19279",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "DiagnosticsLevel": ("V", "i=19242", {}),
                                "LiveValues": (
                                    "O",
                                    "i=19286",
                                    {
                                        "ResolvedAddress": (
                                            "V",
                                            "i=19287",
                                            {"DiagnosticsLevel": ("V", "i=19288", {})},
                                        )
                                    },
                                ),
                                "Reset": ("M", "i=19253", {}),
                                "SubError": ("V", "i=19254", {}),
                                "TotalError": (
                                    "V",
                                    "i=19248",
                                    {
                                        "Active": ("V", "i=19249", {}),
                                        "Classification": ("V", "i=19250", {}),
                                        "DiagnosticsLevel": ("V", "i=19251", {}),
                                    },
                                ),
                                "TotalInformation": (
                                    "V",
                                    "i=19243",
                                    {
                                        "Active": ("V", "i=19244", {}),
                                        "Classification": ("V", "i=19245", {}),
                                        "DiagnosticsLevel": ("V", "i=19246", {}),
                                    },
                                ),
                            },
                        ),
                        "PublisherId": ("V", "i=14595", {}),
                        "RemoveGroup": (
                            "M",
                            "i=14225",
                            {"InputArguments": ("V", "i=14226", {})},
                        ),
                        "Status": ("O", "i=14600", {"State": ("V", "i=14601", {})}),
                        "TransportProfileUri": (
                            "V",
                            "i=17306",
                            {"Selections": ("V", "i=17710", {})},
                        ),
                        "TransportSettings": ("O", "i=17203", {}),
                    },
                ),
                "PubSubDiagnosticsType": (
                    "OT",
                    "i=19677",
                    {
                        "Counters": (
                            "O",
                            "i=19691",
                            {
                                "StateDisabledByMethod": (
                                    "V",
                                    "i=19717",
                                    {
                                        "Active": ("V", "i=19718", {}),
                                        "Classification": ("V", "i=19719", {}),
                                        "DiagnosticsLevel": ("V", "i=19720", {}),
                                    },
                                ),
                                "StateError": (
                                    "V",
                                    "i=19692",
                                    {
                                        "Active": ("V", "i=19693", {}),
                                        "Classification": ("V", "i=19694", {}),
                                        "DiagnosticsLevel": ("V", "i=19695", {}),
                                    },
                                ),
                                "StateOperationalByMethod": (
                                    "V",
                                    "i=19697",
                                    {
                                        "Active": ("V", "i=19698", {}),
                                        "Classification": ("V", "i=19699", {}),
                                        "DiagnosticsLevel": ("V", "i=19700", {}),
                                    },
                                ),
                                "StateOperationalByParent": (
                                    "V",
                                    "i=19702",
                                    {
                                        "Active": ("V", "i=19703", {}),
                                        "Classification": ("V", "i=19704", {}),
                                        "DiagnosticsLevel": ("V", "i=19705", {}),
                                    },
                                ),
                                "StateOperationalFromError": (
                                    "V",
                                    "i=19707",
                                    {
                                        "Active": ("V", "i=19708", {}),
                                        "Classification": ("V", "i=19709", {}),
                                        "DiagnosticsLevel": ("V", "i=19710", {}),
                                    },
                                ),
                                "StatePausedByParent": (
                                    "V",
                                    "i=19712",
                                    {
                                        "Active": ("V", "i=19713", {}),
                                        "Classification": ("V", "i=19714", {}),
                                        "DiagnosticsLevel": ("V", "i=19715", {}),
                                    },
                                ),
                            },
                        ),
                        "DiagnosticsLevel": ("V", "i=19678", {}),
                        "LiveValues": ("O", "i=19722", {}),
                        "PubSubDiagnosticsConnectionType": (
                            "OT",
                            "i=19786",
                            {
                                "LiveValues": (
                                    "O",
                                    "i=19831",
                                    {
                                        "ResolvedAddress": (
                                            "V",
                                            "i=19832",
                                            {"DiagnosticsLevel": ("V", "i=19833", {})},
                                        )
                                    },
                                )
                            },
                        ),
                        "PubSubDiagnosticsDataSetReaderType": (
                            "OT",
                            "i=20027",
                            {
                                "Counters": (
                                    "O",
                                    "i=20041",
                                    {
                                        "DecryptionErrors": (
                                            "V",
                                            "i=20078",
                                            {
                                                "Active": ("V", "i=20079", {}),
                                                "Classification": ("V", "i=20080", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=20081",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "FailedDataSetMessages": (
                                            "V",
                                            "i=20073",
                                            {
                                                "Active": ("V", "i=20074", {}),
                                                "Classification": ("V", "i=20075", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=20076",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "LiveValues": (
                                    "O",
                                    "i=20072",
                                    {
                                        "MajorVersion": (
                                            "V",
                                            "i=20087",
                                            {"DiagnosticsLevel": ("V", "i=20088", {})},
                                        ),
                                        "MessageSequenceNumber": (
                                            "V",
                                            "i=20083",
                                            {"DiagnosticsLevel": ("V", "i=20084", {})},
                                        ),
                                        "MinorVersion": (
                                            "V",
                                            "i=20089",
                                            {"DiagnosticsLevel": ("V", "i=20090", {})},
                                        ),
                                        "SecurityTokenID": (
                                            "V",
                                            "i=20091",
                                            {"DiagnosticsLevel": ("V", "i=20092", {})},
                                        ),
                                        "StatusCode": (
                                            "V",
                                            "i=20085",
                                            {"DiagnosticsLevel": ("V", "i=20086", {})},
                                        ),
                                        "TimeToNextTokenID": (
                                            "V",
                                            "i=20093",
                                            {"DiagnosticsLevel": ("V", "i=20094", {})},
                                        ),
                                    },
                                ),
                            },
                        ),
                        "PubSubDiagnosticsDataSetWriterType": (
                            "OT",
                            "i=19968",
                            {
                                "Counters": (
                                    "O",
                                    "i=19982",
                                    {
                                        "FailedDataSetMessages": (
                                            "V",
                                            "i=20014",
                                            {
                                                "Active": ("V", "i=20015", {}),
                                                "Classification": ("V", "i=20016", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=20017",
                                                    {},
                                                ),
                                            },
                                        )
                                    },
                                ),
                                "LiveValues": (
                                    "O",
                                    "i=20013",
                                    {
                                        "MajorVersion": (
                                            "V",
                                            "i=20023",
                                            {"DiagnosticsLevel": ("V", "i=20024", {})},
                                        ),
                                        "MessageSequenceNumber": (
                                            "V",
                                            "i=20019",
                                            {"DiagnosticsLevel": ("V", "i=20020", {})},
                                        ),
                                        "MinorVersion": (
                                            "V",
                                            "i=20025",
                                            {"DiagnosticsLevel": ("V", "i=20026", {})},
                                        ),
                                        "StatusCode": (
                                            "V",
                                            "i=20021",
                                            {"DiagnosticsLevel": ("V", "i=20022", {})},
                                        ),
                                    },
                                ),
                            },
                        ),
                        "PubSubDiagnosticsReaderGroupType": (
                            "OT",
                            "i=19903",
                            {
                                "Counters": (
                                    "O",
                                    "i=19917",
                                    {
                                        "DecryptionErrors": (
                                            "V",
                                            "i=19959",
                                            {
                                                "Active": ("V", "i=19960", {}),
                                                "Classification": ("V", "i=19961", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19962",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "ReceivedInvalidNetworkMessages": (
                                            "V",
                                            "i=19954",
                                            {
                                                "Active": ("V", "i=19955", {}),
                                                "Classification": ("V", "i=19956", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19957",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "ReceivedNetworkMessages": (
                                            "V",
                                            "i=19949",
                                            {
                                                "Active": ("V", "i=19950", {}),
                                                "Classification": ("V", "i=19951", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19952",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "LiveValues": (
                                    "O",
                                    "i=19948",
                                    {
                                        "ConfiguredDataSetReaders": (
                                            "V",
                                            "i=19964",
                                            {"DiagnosticsLevel": ("V", "i=19965", {})},
                                        ),
                                        "OperationalDataSetReaders": (
                                            "V",
                                            "i=19966",
                                            {"DiagnosticsLevel": ("V", "i=19967", {})},
                                        ),
                                    },
                                ),
                            },
                        ),
                        "PubSubDiagnosticsRootType": (
                            "OT",
                            "i=19732",
                            {
                                "LiveValues": (
                                    "O",
                                    "i=19777",
                                    {
                                        "ConfiguredDataSetReaders": (
                                            "V",
                                            "i=19780",
                                            {"DiagnosticsLevel": ("V", "i=19781", {})},
                                        ),
                                        "ConfiguredDataSetWriters": (
                                            "V",
                                            "i=19778",
                                            {"DiagnosticsLevel": ("V", "i=19779", {})},
                                        ),
                                        "OperationalDataSetReaders": (
                                            "V",
                                            "i=19784",
                                            {"DiagnosticsLevel": ("V", "i=19785", {})},
                                        ),
                                        "OperationalDataSetWriters": (
                                            "V",
                                            "i=19782",
                                            {"DiagnosticsLevel": ("V", "i=19783", {})},
                                        ),
                                    },
                                )
                            },
                        ),
                        "PubSubDiagnosticsWriterGroupType": (
                            "OT",
                            "i=19834",
                            {
                                "Counters": (
                                    "O",
                                    "i=19848",
                                    {
                                        "EncryptionErrors": (
                                            "V",
                                            "i=19890",
                                            {
                                                "Active": ("V", "i=19891", {}),
                                                "Classification": ("V", "i=19892", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19893",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "FailedTransmissions": (
                                            "V",
                                            "i=19885",
                                            {
                                                "Active": ("V", "i=19886", {}),
                                                "Classification": ("V", "i=19887", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19888",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "SentNetworkMessages": (
                                            "V",
                                            "i=19880",
                                            {
                                                "Active": ("V", "i=19881", {}),
                                                "Classification": ("V", "i=19882", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=19883",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "LiveValues": (
                                    "O",
                                    "i=19879",
                                    {
                                        "ConfiguredDataSetWriters": (
                                            "V",
                                            "i=19895",
                                            {"DiagnosticsLevel": ("V", "i=19896", {})},
                                        ),
                                        "OperationalDataSetWriters": (
                                            "V",
                                            "i=19897",
                                            {"DiagnosticsLevel": ("V", "i=19898", {})},
                                        ),
                                        "SecurityTokenID": (
                                            "V",
                                            "i=19899",
                                            {"DiagnosticsLevel": ("V", "i=19900", {})},
                                        ),
                                        "TimeToNextTokenID": (
                                            "V",
                                            "i=19901",
                                            {"DiagnosticsLevel": ("V", "i=19902", {})},
                                        ),
                                    },
                                ),
                            },
                        ),
                        "Reset": ("M", "i=19689", {}),
                        "SubError": ("V", "i=19690", {}),
                        "TotalError": (
                            "V",
                            "i=19684",
                            {
                                "Active": ("V", "i=19685", {}),
                                "Classification": ("V", "i=19686", {}),
                                "DiagnosticsLevel": ("V", "i=19687", {}),
                            },
                        ),
                        "TotalInformation": (
                            "V",
                            "i=19679",
                            {
                                "Active": ("V", "i=19680", {}),
                                "Classification": ("V", "i=19681", {}),
                                "DiagnosticsLevel": ("V", "i=19682", {}),
                            },
                        ),
                    },
                ),
                "PubSubGroupType": (
                    "OT",
                    "i=14232",
                    {
                        "GroupProperties": ("V", "i=17488", {}),
                        "MaxNetworkMessageSize": ("V", "i=17724", {}),
                        "ReaderGroupType": (
                            "OT",
                            "i=17999",
                            {
                                "AddDataSetReader": (
                                    "M",
                                    "i=21082",
                                    {
                                        "InputArguments": ("V", "i=21083", {}),
                                        "OutputArguments": ("V", "i=21084", {}),
                                    },
                                ),
                                "Diagnostics": (
                                    "O",
                                    "i=21015",
                                    {
                                        "Counters": (
                                            "O",
                                            "i=21029",
                                            {
                                                "ReceivedNetworkMessages": (
                                                    "V",
                                                    "i=21061",
                                                    {
                                                        "Active": ("V", "i=21062", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=21063",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=21064",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "StateDisabledByMethod": (
                                                    "V",
                                                    "i=21055",
                                                    {
                                                        "Active": ("V", "i=21056", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=21057",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=21058",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "StateError": (
                                                    "V",
                                                    "i=21030",
                                                    {
                                                        "Active": ("V", "i=21031", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=21032",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=21033",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "StateOperationalByMethod": (
                                                    "V",
                                                    "i=21035",
                                                    {
                                                        "Active": ("V", "i=21036", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=21037",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=21038",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "StateOperationalByParent": (
                                                    "V",
                                                    "i=21040",
                                                    {
                                                        "Active": ("V", "i=21041", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=21042",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=21043",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "StateOperationalFromError": (
                                                    "V",
                                                    "i=21045",
                                                    {
                                                        "Active": ("V", "i=21046", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=21047",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=21048",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "StatePausedByParent": (
                                                    "V",
                                                    "i=21050",
                                                    {
                                                        "Active": ("V", "i=21051", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=21052",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=21053",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                            },
                                        ),
                                        "DiagnosticsLevel": ("V", "i=21016", {}),
                                        "LiveValues": (
                                            "O",
                                            "i=21060",
                                            {
                                                "ConfiguredDataSetReaders": (
                                                    "V",
                                                    "i=21076",
                                                    {
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=21077",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "OperationalDataSetReaders": (
                                                    "V",
                                                    "i=21078",
                                                    {
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=21079",
                                                            {},
                                                        )
                                                    },
                                                ),
                                            },
                                        ),
                                        "Reset": ("M", "i=21027", {}),
                                        "SubError": ("V", "i=21028", {}),
                                        "TotalError": (
                                            "V",
                                            "i=21022",
                                            {
                                                "Active": ("V", "i=21023", {}),
                                                "Classification": ("V", "i=21024", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=21025",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "TotalInformation": (
                                            "V",
                                            "i=21017",
                                            {
                                                "Active": ("V", "i=21018", {}),
                                                "Classification": ("V", "i=21019", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=21020",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "MessageSettings": ("O", "i=21081", {}),
                                "RemoveDataSetReader": (
                                    "M",
                                    "i=21085",
                                    {"InputArguments": ("V", "i=21086", {})},
                                ),
                                "TransportSettings": ("O", "i=21080", {}),
                            },
                        ),
                        "SecurityGroupId": ("V", "i=15927", {}),
                        "SecurityKeyServices": ("V", "i=15928", {}),
                        "SecurityMode": ("V", "i=15926", {}),
                        "Status": ("O", "i=15265", {"State": ("V", "i=15266", {})}),
                        "WriterGroupType": (
                            "OT",
                            "i=17725",
                            {
                                "AddDataSetWriter": (
                                    "M",
                                    "i=17969",
                                    {
                                        "InputArguments": ("V", "i=17976", {}),
                                        "OutputArguments": ("V", "i=17987", {}),
                                    },
                                ),
                                "Diagnostics": (
                                    "O",
                                    "i=17812",
                                    {
                                        "Counters": (
                                            "O",
                                            "i=17826",
                                            {
                                                "EncryptionErrors": (
                                                    "V",
                                                    "i=17900",
                                                    {
                                                        "Active": ("V", "i=17901", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=17902",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=17903",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "FailedTransmissions": (
                                                    "V",
                                                    "i=17874",
                                                    {
                                                        "Active": ("V", "i=17878", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=17885",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=17892",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "SentNetworkMessages": (
                                                    "V",
                                                    "i=17859",
                                                    {
                                                        "Active": ("V", "i=17864", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=17871",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=17872",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "StateDisabledByMethod": (
                                                    "V",
                                                    "i=17853",
                                                    {
                                                        "Active": ("V", "i=17854", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=17855",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=17856",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "StateError": (
                                                    "V",
                                                    "i=17827",
                                                    {
                                                        "Active": ("V", "i=17828", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=17829",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=17830",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "StateOperationalByMethod": (
                                                    "V",
                                                    "i=17832",
                                                    {
                                                        "Active": ("V", "i=17833", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=17834",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=17835",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "StateOperationalByParent": (
                                                    "V",
                                                    "i=17837",
                                                    {
                                                        "Active": ("V", "i=17838", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=17839",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=17840",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "StateOperationalFromError": (
                                                    "V",
                                                    "i=17842",
                                                    {
                                                        "Active": ("V", "i=17843", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=17844",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=17845",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "StatePausedByParent": (
                                                    "V",
                                                    "i=17847",
                                                    {
                                                        "Active": ("V", "i=17848", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=17849",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=17850",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                            },
                                        ),
                                        "DiagnosticsLevel": ("V", "i=17813", {}),
                                        "LiveValues": (
                                            "O",
                                            "i=17858",
                                            {
                                                "ConfiguredDataSetWriters": (
                                                    "V",
                                                    "i=17913",
                                                    {
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=17920",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "OperationalDataSetWriters": (
                                                    "V",
                                                    "i=17927",
                                                    {
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=17934",
                                                            {},
                                                        )
                                                    },
                                                ),
                                            },
                                        ),
                                        "Reset": ("M", "i=17824", {}),
                                        "SubError": ("V", "i=17825", {}),
                                        "TotalError": (
                                            "V",
                                            "i=17819",
                                            {
                                                "Active": ("V", "i=17820", {}),
                                                "Classification": ("V", "i=17821", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=17822",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "TotalInformation": (
                                            "V",
                                            "i=17814",
                                            {
                                                "Active": ("V", "i=17815", {}),
                                                "Classification": ("V", "i=17816", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=17817",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "HeaderLayoutUri": ("V", "i=17559", {}),
                                "KeepAliveTime": ("V", "i=17738", {}),
                                "LocaleIds": ("V", "i=17740", {}),
                                "MessageSettings": ("O", "i=17742", {}),
                                "Priority": ("V", "i=17739", {}),
                                "PublishingInterval": ("V", "i=17737", {}),
                                "RemoveDataSetWriter": (
                                    "M",
                                    "i=17992",
                                    {"InputArguments": ("V", "i=17993", {})},
                                ),
                                "TransportSettings": ("O", "i=17741", {}),
                                "WriterGroupId": ("V", "i=17736", {}),
                            },
                        ),
                    },
                ),
                "PubSubKeyPushTargetType": (
                    "OT",
                    "i=25337",
                    {
                        "ApplicationUri": ("V", "i=25634", {}),
                        "ConnectSecurityGroups": (
                            "M",
                            "i=25641",
                            {
                                "InputArguments": ("V", "i=25642", {}),
                                "OutputArguments": ("V", "i=25643", {}),
                            },
                        ),
                        "DisconnectSecurityGroups": (
                            "M",
                            "i=25644",
                            {
                                "InputArguments": ("V", "i=25645", {}),
                                "OutputArguments": ("V", "i=25646", {}),
                            },
                        ),
                        "EndpointUrl": ("V", "i=25635", {}),
                        "LastPushErrorTime": ("V", "i=25640", {}),
                        "LastPushExecutionTime": ("V", "i=25639", {}),
                        "RequestedKeyCount": ("V", "i=25637", {}),
                        "RetryInterval": ("V", "i=25638", {}),
                        "SecurityPolicyUri": ("V", "i=25340", {}),
                        "TriggerKeyUpdate": ("M", "i=25647", {}),
                        "UserTokenType": ("V", "i=25636", {}),
                    },
                ),
                "PubSubKeyServiceType": (
                    "OT",
                    "i=15906",
                    {
                        "GetSecurityGroup": (
                            "M",
                            "i=15910",
                            {
                                "InputArguments": ("V", "i=15911", {}),
                                "OutputArguments": ("V", "i=15912", {}),
                            },
                        ),
                        "GetSecurityKeys": (
                            "M",
                            "i=15907",
                            {
                                "InputArguments": ("V", "i=15908", {}),
                                "OutputArguments": ("V", "i=15909", {}),
                            },
                        ),
                        "KeyPushTargets": (
                            "O",
                            "i=25277",
                            {
                                "AddPushTarget": (
                                    "M",
                                    "i=25278",
                                    {
                                        "InputArguments": ("V", "i=25279", {}),
                                        "OutputArguments": ("V", "i=25280", {}),
                                    },
                                ),
                                "RemovePushTarget": (
                                    "M",
                                    "i=25281",
                                    {"InputArguments": ("V", "i=25282", {})},
                                ),
                            },
                        ),
                        "PublishSubscribeType": (
                            "OT",
                            "i=14416",
                            {
                                "AddConnection": (
                                    "M",
                                    "i=16598",
                                    {
                                        "InputArguments": ("V", "i=16599", {}),
                                        "OutputArguments": ("V", "i=16600", {}),
                                    },
                                ),
                                "ConfigurationProperties": ("V", "i=32397", {}),
                                "ConfigurationVersion": ("V", "i=25433", {}),
                                "DataSetClasses": (
                                    "O",
                                    "i=23649",
                                    {"<DataSetName>": ("V", "i=24009", {})},
                                ),
                                "DefaultDatagramPublisherId": ("V", "i=25432", {}),
                                "DefaultSecurityKeyServices": ("V", "i=32396", {}),
                                "Diagnostics": (
                                    "O",
                                    "i=18715",
                                    {
                                        "Counters": (
                                            "O",
                                            "i=18729",
                                            {
                                                "StateDisabledByMethod": (
                                                    "V",
                                                    "i=18755",
                                                    {
                                                        "Active": ("V", "i=18756", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=18757",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=18758",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "StateError": (
                                                    "V",
                                                    "i=18730",
                                                    {
                                                        "Active": ("V", "i=18731", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=18732",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=18733",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "StateOperationalByMethod": (
                                                    "V",
                                                    "i=18735",
                                                    {
                                                        "Active": ("V", "i=18736", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=18737",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=18738",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "StateOperationalByParent": (
                                                    "V",
                                                    "i=18740",
                                                    {
                                                        "Active": ("V", "i=18741", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=18742",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=18743",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "StateOperationalFromError": (
                                                    "V",
                                                    "i=18745",
                                                    {
                                                        "Active": ("V", "i=18746", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=18747",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=18748",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "StatePausedByParent": (
                                                    "V",
                                                    "i=18750",
                                                    {
                                                        "Active": ("V", "i=18751", {}),
                                                        "Classification": (
                                                            "V",
                                                            "i=18752",
                                                            {},
                                                        ),
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=18753",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                            },
                                        ),
                                        "DiagnosticsLevel": ("V", "i=18716", {}),
                                        "LiveValues": (
                                            "O",
                                            "i=18760",
                                            {
                                                "ConfiguredDataSetReaders": (
                                                    "V",
                                                    "i=18763",
                                                    {
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=18764",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "ConfiguredDataSetWriters": (
                                                    "V",
                                                    "i=18761",
                                                    {
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=18762",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "OperationalDataSetReaders": (
                                                    "V",
                                                    "i=18767",
                                                    {
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=18768",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "OperationalDataSetWriters": (
                                                    "V",
                                                    "i=18765",
                                                    {
                                                        "DiagnosticsLevel": (
                                                            "V",
                                                            "i=18766",
                                                            {},
                                                        )
                                                    },
                                                ),
                                            },
                                        ),
                                        "Reset": ("M", "i=18727", {}),
                                        "SubError": ("V", "i=18728", {}),
                                        "TotalError": (
                                            "V",
                                            "i=18722",
                                            {
                                                "Active": ("V", "i=18723", {}),
                                                "Classification": ("V", "i=18724", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=18725",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "TotalInformation": (
                                            "V",
                                            "i=18717",
                                            {
                                                "Active": ("V", "i=18718", {}),
                                                "Classification": ("V", "i=18719", {}),
                                                "DiagnosticsLevel": (
                                                    "V",
                                                    "i=18720",
                                                    {},
                                                ),
                                            },
                                        ),
                                    },
                                ),
                                "PubSubCapablities": (
                                    "O",
                                    "i=23642",
                                    {
                                        "MaxDataSetReaders": ("V", "i=23647", {}),
                                        "MaxDataSetWriters": ("V", "i=23646", {}),
                                        "MaxFieldsPerDataSet": ("V", "i=23648", {}),
                                        "MaxPubSubConnections": ("V", "i=23643", {}),
                                        "MaxReaderGroups": ("V", "i=23645", {}),
                                        "MaxWriterGroups": ("V", "i=23644", {}),
                                    },
                                ),
                                "PubSubConfiguration": (
                                    "O",
                                    "i=25403",
                                    {
                                        "Close": (
                                            "M",
                                            "i=25414",
                                            {"InputArguments": ("V", "i=25415", {})},
                                        ),
                                        "CloseAndUpdate": (
                                            "M",
                                            "i=25429",
                                            {
                                                "InputArguments": ("V", "i=25430", {}),
                                                "OutputArguments": ("V", "i=25431", {}),
                                            },
                                        ),
                                        "GetPosition": (
                                            "M",
                                            "i=25421",
                                            {
                                                "InputArguments": ("V", "i=25422", {}),
                                                "OutputArguments": ("V", "i=25423", {}),
                                            },
                                        ),
                                        "Open": (
                                            "M",
                                            "i=25411",
                                            {
                                                "InputArguments": ("V", "i=25412", {}),
                                                "OutputArguments": ("V", "i=25413", {}),
                                            },
                                        ),
                                        "OpenCount": ("V", "i=25407", {}),
                                        "Read": (
                                            "M",
                                            "i=25416",
                                            {
                                                "InputArguments": ("V", "i=25417", {}),
                                                "OutputArguments": ("V", "i=25418", {}),
                                            },
                                        ),
                                        "ReserveIds": (
                                            "M",
                                            "i=25426",
                                            {
                                                "InputArguments": ("V", "i=25427", {}),
                                                "OutputArguments": ("V", "i=25428", {}),
                                            },
                                        ),
                                        "SetPosition": (
                                            "M",
                                            "i=25424",
                                            {"InputArguments": ("V", "i=25425", {})},
                                        ),
                                        "Size": ("V", "i=25404", {}),
                                        "UserWritable": ("V", "i=25406", {}),
                                        "Writable": ("V", "i=25405", {}),
                                        "Write": (
                                            "M",
                                            "i=25419",
                                            {"InputArguments": ("V", "i=25420", {})},
                                        ),
                                    },
                                ),
                                "PublishedDataSets": ("O", "i=14434", {}),
                                "RemoveConnection": (
                                    "M",
                                    "i=14432",
                                    {"InputArguments": ("V", "i=14433", {})},
                                ),
                                "SetSecurityKeys": (
                                    "M",
                                    "i=17296",
                                    {"InputArguments": ("V", "i=17297", {})},
                                ),
                                "Status": (
                                    "O",
                                    "i=15844",
                                    {"State": ("V", "i=15845", {})},
                                ),
                                "SubscribedDataSets": ("O", "i=23622", {}),
                                "SupportedTransportProfiles": ("V", "i=17479", {}),
                            },
                        ),
                        "SecurityGroups": (
                            "O",
                            "i=15913",
                            {
                                "AddSecurityGroup": (
                                    "M",
                                    "i=15914",
                                    {
                                        "InputArguments": ("V", "i=15915", {}),
                                        "OutputArguments": ("V", "i=15916", {}),
                                    },
                                ),
                                "RemoveSecurityGroup": (
                                    "M",
                                    "i=15917",
                                    {"InputArguments": ("V", "i=15918", {})},
                                ),
                            },
                        ),
                    },
                ),
                "PubSubStatusType": (
                    "OT",
                    "i=14643",
                    {
                        "Disable": ("M", "i=14646", {}),
                        "Enable": ("M", "i=14645", {}),
                        "State": ("V", "i=14644", {}),
                    },
                ),
                "PublishedDataSetType": (
                    "OT",
                    "i=14509",
                    {
                        "ConfigurationVersion": ("V", "i=14519", {}),
                        "CyclicDataSet": ("V", "i=25521", {}),
                        "DataSetClassId": ("V", "i=16759", {}),
                        "DataSetMetaData": ("V", "i=15229", {}),
                        "ExtensionFields": (
                            "O",
                            "i=15481",
                            {
                                "AddExtensionField": (
                                    "M",
                                    "i=15482",
                                    {
                                        "InputArguments": ("V", "i=15483", {}),
                                        "OutputArguments": ("V", "i=15484", {}),
                                    },
                                ),
                                "RemoveExtensionField": (
                                    "M",
                                    "i=15485",
                                    {"InputArguments": ("V", "i=15486", {})},
                                ),
                            },
                        ),
                        "PublishedDataItemsType": (
                            "OT",
                            "i=14534",
                            {
                                "AddVariables": (
                                    "M",
                                    "i=14555",
                                    {
                                        "InputArguments": ("V", "i=14556", {}),
                                        "OutputArguments": ("V", "i=14557", {}),
                                    },
                                ),
                                "PublishedData": ("V", "i=14548", {}),
                                "RemoveVariables": (
                                    "M",
                                    "i=14558",
                                    {
                                        "InputArguments": ("V", "i=14559", {}),
                                        "OutputArguments": ("V", "i=14560", {}),
                                    },
                                ),
                            },
                        ),
                        "PublishedEventsType": (
                            "OT",
                            "i=14572",
                            {
                                "EventNotifier": ("V", "i=14586", {}),
                                "Filter": ("V", "i=14588", {}),
                                "ModifyFieldSelection": (
                                    "M",
                                    "i=15052",
                                    {
                                        "InputArguments": ("V", "i=15053", {}),
                                        "OutputArguments": ("V", "i=15517", {}),
                                    },
                                ),
                                "SelectedFields": ("V", "i=14587", {}),
                            },
                        ),
                    },
                ),
                "QuantityType": (
                    "OT",
                    "i=32475",
                    {
                        "Annotation": ("V", "i=32478", {}),
                        "ConversionService": ("V", "i=32479", {}),
                        "Dimension": ("V", "i=32480", {}),
                        "ServerUnits": (
                            "O",
                            "i=32481",
                            {
                                "<ServerUnit>": (
                                    "O",
                                    "i=32482",
                                    {
                                        "ConversionLimit": ("V", "i=32496", {}),
                                        "Symbol": ("V", "i=32483", {}),
                                        "UnitSystem": ("V", "i=32485", {}),
                                    },
                                )
                            },
                        ),
                        "Symbol": ("V", "i=32476", {}),
                    },
                ),
                "ReaderGroupMessageType": ("OT", "i=21091", {}),
                "ReaderGroupTransportType": ("OT", "i=21090", {}),
                "RoleSetType": (
                    "OT",
                    "i=15607",
                    {
                        "<RoleName>": (
                            "O",
                            "i=15608",
                            {"Identities": ("V", "i=16162", {})},
                        ),
                        "AddRole": (
                            "M",
                            "i=15997",
                            {
                                "InputArguments": ("V", "i=15998", {}),
                                "OutputArguments": ("V", "i=15999", {}),
                            },
                        ),
                        "RemoveRole": (
                            "M",
                            "i=16000",
                            {"InputArguments": ("V", "i=16001", {})},
                        ),
                    },
                ),
                "RoleType": (
                    "OT",
                    "i=15620",
                    {
                        "AddApplication": (
                            "M",
                            "i=16176",
                            {"InputArguments": ("V", "i=16177", {})},
                        ),
                        "AddEndpoint": (
                            "M",
                            "i=16180",
                            {"InputArguments": ("V", "i=16181", {})},
                        ),
                        "AddIdentity": (
                            "M",
                            "i=15624",
                            {"InputArguments": ("V", "i=15625", {})},
                        ),
                        "Applications": ("V", "i=16174", {}),
                        "ApplicationsExclude": ("V", "i=15410", {}),
                        "CustomConfiguration": ("V", "i=24139", {}),
                        "Endpoints": ("V", "i=16175", {}),
                        "EndpointsExclude": ("V", "i=15411", {}),
                        "Identities": ("V", "i=16173", {}),
                        "RemoveApplication": (
                            "M",
                            "i=16178",
                            {"InputArguments": ("V", "i=16179", {})},
                        ),
                        "RemoveEndpoint": (
                            "M",
                            "i=16182",
                            {"InputArguments": ("V", "i=16183", {})},
                        ),
                        "RemoveIdentity": (
                            "M",
                            "i=15626",
                            {"InputArguments": ("V", "i=15627", {})},
                        ),
                    },
                ),
                "SecurityGroupType": (
                    "OT",
                    "i=15471",
                    {
                        "ForceKeyRotation": ("M", "i=25625", {}),
                        "InvalidateKeys": ("M", "i=25624", {}),
                        "KeyLifetime": ("V", "i=15046", {}),
                        "MaxFutureKeyCount": ("V", "i=15048", {}),
                        "MaxPastKeyCount": ("V", "i=15056", {}),
                        "SecurityGroupId": ("V", "i=15472", {}),
                        "SecurityPolicyUri": ("V", "i=15047", {}),
                    },
                ),
                "SerializationEntityType": (
                    "OT",
                    "i=19824",
                    {
                        "ConfigureSerialization": (
                            "M",
                            "i=19839",
                            {
                                "InputArguments": ("V", "i=19840", {}),
                                "OutputArguments": ("V", "i=19841", {}),
                            },
                        ),
                        "ConsiderSubElementSerializationProperties": (
                            "V",
                            "i=19829",
                            {},
                        ),
                        "CustomMetaDataProperties": ("V", "i=19830", {}),
                        "CustomMetaDataRef": ("V", "i=19835", {}),
                        "ExcludeReferenceTypes": ("V", "i=19827", {}),
                        "IncludeDictionaryReference": ("V", "i=19838", {}),
                        "IncludeReferenceTypes": ("V", "i=19826", {}),
                        "IncludeSourceTimestamp": ("V", "i=19837", {}),
                        "IncludeStatus": ("V", "i=19836", {}),
                        "SerializationDepth": ("V", "i=19828", {}),
                        "SerializedData": ("V", "i=19825", {}),
                    },
                ),
                "ServerCapabilitiesType": (
                    "OT",
                    "i=2013",
                    {
                        "<VendorCapability>": ("V", "i=11562", {}),
                        "AggregateFunctions": ("O", "i=2754", {}),
                        "ConformanceUnits": ("V", "i=24094", {}),
                        "LocaleIdArray": ("V", "i=2016", {}),
                        "MaxArrayLength": ("V", "i=11549", {}),
                        "MaxBrowseContinuationPoints": ("V", "i=2732", {}),
                        "MaxByteStringLength": ("V", "i=12910", {}),
                        "MaxHistoryContinuationPoints": ("V", "i=2734", {}),
                        "MaxLogObjectContinuationPoints": ("V", "i=19809", {}),
                        "MaxMonitoredItems": ("V", "i=24090", {}),
                        "MaxMonitoredItemsPerSubscription": ("V", "i=24103", {}),
                        "MaxMonitoredItemsQueueSize": ("V", "i=31770", {}),
                        "MaxQueryContinuationPoints": ("V", "i=2733", {}),
                        "MaxSelectClauseParameters": ("V", "i=24092", {}),
                        "MaxSessions": ("V", "i=24088", {}),
                        "MaxStringLength": ("V", "i=11550", {}),
                        "MaxSubscriptions": ("V", "i=24089", {}),
                        "MaxSubscriptionsPerSession": ("V", "i=24091", {}),
                        "MaxWhereClauseParameters": ("V", "i=24093", {}),
                        "MinSupportedSampleRate": ("V", "i=2017", {}),
                        "ModellingRules": ("O", "i=2019", {}),
                        "OperationLimits": ("O", "i=11551", {}),
                        "RoleSet": (
                            "O",
                            "i=16295",
                            {
                                "AddRole": (
                                    "M",
                                    "i=16296",
                                    {
                                        "InputArguments": ("V", "i=16297", {}),
                                        "OutputArguments": ("V", "i=16298", {}),
                                    },
                                ),
                                "RemoveRole": (
                                    "M",
                                    "i=16299",
                                    {"InputArguments": ("V", "i=16300", {})},
                                ),
                            },
                        ),
                        "ServerProfileArray": ("V", "i=2014", {}),
                        "SoftwareCertificates": ("V", "i=3049", {}),
                    },
                ),
                "ServerConfigurationType": (
                    "OT",
                    "i=12581",
                    {
                        "ApplicationConfigurationType": (
                            "OT",
                            "i=25731",
                            {
                                "ApplicationType": ("V", "i=26852", {}),
                                "ApplicationUri": ("V", "i=26850", {}),
                                "AuthorizationServices": ("O", "i=19427", {}),
                                "Enabled": ("V", "i=26849", {}),
                                "IsNonUaApplication": ("V", "i=23741", {}),
                                "KeyCredentials": ("O", "i=19423", {}),
                                "ProductUri": ("V", "i=26851", {}),
                            },
                        ),
                        "ApplicationNames": ("V", "i=18660", {}),
                        "ApplicationType": ("V", "i=25697", {}),
                        "ApplicationUri": ("V", "i=25696", {}),
                        "ApplyChanges": ("M", "i=12734", {}),
                        "CancelChanges": ("M", "i=25698", {}),
                        "CertificateGroups": (
                            "O",
                            "i=13950",
                            {
                                "DefaultApplicationGroup": (
                                    "O",
                                    "i=13951",
                                    {
                                        "CertificateTypes": ("V", "i=13984", {}),
                                        "TrustList": (
                                            "O",
                                            "i=13952",
                                            {
                                                "AddCertificate": (
                                                    "M",
                                                    "i=13980",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13981",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Close": (
                                                    "M",
                                                    "i=13961",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13962",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "CloseAndUpdate": (
                                                    "M",
                                                    "i=13977",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13978",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13979",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "GetPosition": (
                                                    "M",
                                                    "i=13968",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13969",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13970",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "LastUpdateTime": ("V", "i=13973", {}),
                                                "Open": (
                                                    "M",
                                                    "i=13958",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13959",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13960",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "OpenCount": ("V", "i=13956", {}),
                                                "OpenWithMasks": (
                                                    "M",
                                                    "i=13974",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13975",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13976",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "Read": (
                                                    "M",
                                                    "i=13963",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13964",
                                                            {},
                                                        ),
                                                        "OutputArguments": (
                                                            "V",
                                                            "i=13965",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "RemoveCertificate": (
                                                    "M",
                                                    "i=13982",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13983",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "SetPosition": (
                                                    "M",
                                                    "i=13971",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13972",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "Size": ("V", "i=13953", {}),
                                                "UserWritable": ("V", "i=13955", {}),
                                                "Writable": ("V", "i=13954", {}),
                                                "Write": (
                                                    "M",
                                                    "i=13966",
                                                    {
                                                        "InputArguments": (
                                                            "V",
                                                            "i=13967",
                                                            {},
                                                        )
                                                    },
                                                ),
                                            },
                                        ),
                                    },
                                )
                            },
                        ),
                        "ConfigurationFile": (
                            "O",
                            "i=15564",
                            {
                                "ActivityTimeout": ("V", "i=15814", {}),
                                "AvailableNetworks": ("V", "i=16646", {}),
                                "AvailablePorts": ("V", "i=16647", {}),
                                "CertificateGroupPurposes": ("V", "i=19422", {}),
                                "CertificateTypes": ("V", "i=16650", {}),
                                "Close": (
                                    "M",
                                    "i=15575",
                                    {"InputArguments": ("V", "i=15790", {})},
                                ),
                                "CloseAndUpdate": (
                                    "M",
                                    "i=15849",
                                    {
                                        "InputArguments": ("V", "i=15850", {}),
                                        "OutputArguments": ("V", "i=15851", {}),
                                    },
                                ),
                                "ConfirmUpdate": (
                                    "M",
                                    "i=15863",
                                    {"InputArguments": ("V", "i=15864", {})},
                                ),
                                "CurrentVersion": ("V", "i=15813", {}),
                                "GetPosition": (
                                    "M",
                                    "i=15807",
                                    {
                                        "InputArguments": ("V", "i=15808", {}),
                                        "OutputArguments": ("V", "i=15809", {}),
                                    },
                                ),
                                "LastUpdateTime": ("V", "i=15812", {}),
                                "MaxCertificateGroups": ("V", "i=19421", {}),
                                "MaxEndpoints": ("V", "i=19420", {}),
                                "Open": (
                                    "M",
                                    "i=15572",
                                    {
                                        "InputArguments": ("V", "i=15573", {}),
                                        "OutputArguments": ("V", "i=15574", {}),
                                    },
                                ),
                                "OpenCount": ("V", "i=15568", {}),
                                "Read": (
                                    "M",
                                    "i=15791",
                                    {
                                        "InputArguments": ("V", "i=15792", {}),
                                        "OutputArguments": ("V", "i=15804", {}),
                                    },
                                ),
                                "SecurityPolicyUris": ("V", "i=16648", {}),
                                "SetPosition": (
                                    "M",
                                    "i=15810",
                                    {"InputArguments": ("V", "i=15811", {})},
                                ),
                                "Size": ("V", "i=15565", {}),
                                "SupportedDataType": ("V", "i=15848", {}),
                                "UserTokenTypes": ("V", "i=16649", {}),
                                "UserWritable": ("V", "i=15567", {}),
                                "Writable": ("V", "i=15566", {}),
                                "Write": (
                                    "M",
                                    "i=15805",
                                    {"InputArguments": ("V", "i=15806", {})},
                                ),
                            },
                        ),
                        "CreateSelfSignedCertificate": (
                            "M",
                            "i=19337",
                            {
                                "InputArguments": ("V", "i=19338", {}),
                                "OutputArguments": ("V", "i=19339", {}),
                            },
                        ),
                        "CreateSigningRequest": (
                            "M",
                            "i=12731",
                            {
                                "InputArguments": ("V", "i=12732", {}),
                                "OutputArguments": ("V", "i=12733", {}),
                            },
                        ),
                        "DeleteCertificate": (
                            "M",
                            "i=19340",
                            {"InputArguments": ("V", "i=19341", {})},
                        ),
                        "GetCertificates": (
                            "M",
                            "i=32296",
                            {
                                "InputArguments": ("V", "i=32297", {}),
                                "OutputArguments": ("V", "i=32298", {}),
                            },
                        ),
                        "GetRejectedList": (
                            "M",
                            "i=12775",
                            {"OutputArguments": ("V", "i=12776", {})},
                        ),
                        "HasSecureElement": ("V", "i=23593", {}),
                        "InApplicationSetup": ("V", "i=19308", {}),
                        "MaxTrustListSize": ("V", "i=12584", {}),
                        "MulticastDnsEnabled": ("V", "i=12585", {}),
                        "ProductUri": ("V", "i=25724", {}),
                        "ResetToServerDefaults": ("M", "i=25699", {}),
                        "ServerCapabilities": ("V", "i=12708", {}),
                        "SupportedPrivateKeyFormats": ("V", "i=12583", {}),
                        "SupportsTransactions": ("V", "i=18661", {}),
                        "TransactionDiagnostics": (
                            "O",
                            "i=32299",
                            {
                                "AffectedCertificateGroups": ("V", "i=32304", {}),
                                "AffectedTrustLists": ("V", "i=32303", {}),
                                "EndTime": ("V", "i=32301", {}),
                                "Errors": ("V", "i=32305", {}),
                                "Result": ("V", "i=32302", {}),
                                "StartTime": ("V", "i=32300", {}),
                            },
                        ),
                        "UpdateCertificate": (
                            "M",
                            "i=12616",
                            {
                                "InputArguments": ("V", "i=12617", {}),
                                "OutputArguments": ("V", "i=12618", {}),
                            },
                        ),
                    },
                ),
                "ServerDiagnosticsType": (
                    "OT",
                    "i=2020",
                    {
                        "EnabledFlag": ("V", "i=2025", {}),
                        "SamplingIntervalDiagnosticsArray": ("V", "i=2022", {}),
                        "ServerDiagnosticsSummary": (
                            "V",
                            "i=2021",
                            {
                                "CumulatedSessionCount": ("V", "i=3118", {}),
                                "CumulatedSubscriptionCount": ("V", "i=3126", {}),
                                "CurrentSessionCount": ("V", "i=3117", {}),
                                "CurrentSubscriptionCount": ("V", "i=3125", {}),
                                "PublishingIntervalCount": ("V", "i=3124", {}),
                                "RejectedRequestsCount": ("V", "i=3128", {}),
                                "RejectedSessionCount": ("V", "i=3120", {}),
                                "SecurityRejectedRequestsCount": ("V", "i=3127", {}),
                                "SecurityRejectedSessionCount": ("V", "i=3119", {}),
                                "ServerViewCount": ("V", "i=3116", {}),
                                "SessionAbortCount": ("V", "i=3122", {}),
                                "SessionTimeoutCount": ("V", "i=3121", {}),
                            },
                        ),
                        "SessionsDiagnosticsSummary": (
                            "O",
                            "i=2744",
                            {
                                "SessionDiagnosticsArray": ("V", "i=3129", {}),
                                "SessionSecurityDiagnosticsArray": ("V", "i=3130", {}),
                            },
                        ),
                        "SubscriptionDiagnosticsArray": ("V", "i=2023", {}),
                    },
                ),
                "ServerRedundancyType": (
                    "OT",
                    "i=2034",
                    {
                        "NonTransparentRedundancyType": (
                            "OT",
                            "i=2039",
                            {
                                "NonTransparentBackupRedundancyType": (
                                    "OT",
                                    "i=32411",
                                    {
                                        "Failover": ("M", "i=32416", {}),
                                        "Mode": ("V", "i=32415", {}),
                                        "RedundantServerArray": ("V", "i=32413", {}),
                                    },
                                ),
                                "NonTransparentNetworkRedundancyType": (
                                    "OT",
                                    "i=11945",
                                    {"ServerNetworkGroups": ("V", "i=11948", {})},
                                ),
                                "ServerUriArray": ("V", "i=2040", {}),
                            },
                        ),
                        "RedundancySupport": ("V", "i=2035", {}),
                        "RedundantServerArray": ("V", "i=32410", {}),
                        "TransparentRedundancyType": (
                            "OT",
                            "i=2036",
                            {
                                "CurrentServerId": ("V", "i=2037", {}),
                                "RedundantServerArray": ("V", "i=2038", {}),
                            },
                        ),
                    },
                ),
                "ServerType": (
                    "OT",
                    "i=2004",
                    {
                        "Auditing": ("V", "i=2742", {}),
                        "EstimatedReturnTime": ("V", "i=12882", {}),
                        "GetMonitoredItems": (
                            "M",
                            "i=11489",
                            {
                                "InputArguments": ("V", "i=11490", {}),
                                "OutputArguments": ("V", "i=11491", {}),
                            },
                        ),
                        "LocalTime": ("V", "i=17612", {}),
                        "NamespaceArray": ("V", "i=2006", {}),
                        "Namespaces": ("O", "i=11527", {}),
                        "RequestServerStateChange": (
                            "M",
                            "i=12883",
                            {"InputArguments": ("V", "i=12884", {})},
                        ),
                        "ResendData": (
                            "M",
                            "i=12871",
                            {"InputArguments": ("V", "i=12872", {})},
                        ),
                        "ServerArray": ("V", "i=2005", {}),
                        "ServerCapabilities": (
                            "O",
                            "i=2009",
                            {
                                "AggregateFunctions": ("O", "i=3094", {}),
                                "LocaleIdArray": ("V", "i=3087", {}),
                                "MaxBrowseContinuationPoints": ("V", "i=3089", {}),
                                "MaxHistoryContinuationPoints": ("V", "i=3091", {}),
                                "MaxQueryContinuationPoints": ("V", "i=3090", {}),
                                "MinSupportedSampleRate": ("V", "i=3088", {}),
                                "ModellingRules": ("O", "i=3093", {}),
                                "ServerProfileArray": ("V", "i=3086", {}),
                                "SoftwareCertificates": ("V", "i=3092", {}),
                            },
                        ),
                        "ServerDiagnostics": (
                            "O",
                            "i=2010",
                            {
                                "EnabledFlag": ("V", "i=3114", {}),
                                "ServerDiagnosticsSummary": (
                                    "V",
                                    "i=3095",
                                    {
                                        "CumulatedSessionCount": ("V", "i=3098", {}),
                                        "CumulatedSubscriptionCount": (
                                            "V",
                                            "i=3106",
                                            {},
                                        ),
                                        "CurrentSessionCount": ("V", "i=3097", {}),
                                        "CurrentSubscriptionCount": ("V", "i=3105", {}),
                                        "PublishingIntervalCount": ("V", "i=3104", {}),
                                        "RejectedRequestsCount": ("V", "i=3108", {}),
                                        "RejectedSessionCount": ("V", "i=3100", {}),
                                        "SecurityRejectedRequestsCount": (
                                            "V",
                                            "i=3107",
                                            {},
                                        ),
                                        "SecurityRejectedSessionCount": (
                                            "V",
                                            "i=3099",
                                            {},
                                        ),
                                        "ServerViewCount": ("V", "i=3096", {}),
                                        "SessionAbortCount": ("V", "i=3102", {}),
                                        "SessionTimeoutCount": ("V", "i=3101", {}),
                                    },
                                ),
                                "SessionsDiagnosticsSummary": (
                                    "O",
                                    "i=3111",
                                    {
                                        "SessionDiagnosticsArray": ("V", "i=3112", {}),
                                        "SessionSecurityDiagnosticsArray": (
                                            "V",
                                            "i=3113",
                                            {},
                                        ),
                                    },
                                ),
                                "SubscriptionDiagnosticsArray": ("V", "i=3110", {}),
                            },
                        ),
                        "ServerRedundancy": (
                            "O",
                            "i=2012",
                            {"RedundancySupport": ("V", "i=3115", {})},
                        ),
                        "ServerStatus": (
                            "V",
                            "i=2007",
                            {
                                "BuildInfo": (
                                    "V",
                                    "i=3077",
                                    {
                                        "BuildDate": ("V", "i=3083", {}),
                                        "BuildNumber": ("V", "i=3082", {}),
                                        "ManufacturerName": ("V", "i=3079", {}),
                                        "ProductName": ("V", "i=3080", {}),
                                        "ProductUri": ("V", "i=3078", {}),
                                        "SoftwareVersion": ("V", "i=3081", {}),
                                    },
                                ),
                                "CurrentTime": ("V", "i=3075", {}),
                                "SecondsTillShutdown": ("V", "i=3084", {}),
                                "ShutdownReason": ("V", "i=3085", {}),
                                "StartTime": ("V", "i=3074", {}),
                                "State": ("V", "i=3076", {}),
                            },
                        ),
                        "ServiceLevel": ("V", "i=2008", {}),
                        "SetSubscriptionDurable": (
                            "M",
                            "i=12746",
                            {
                                "InputArguments": ("V", "i=12747", {}),
                                "OutputArguments": ("V", "i=12748", {}),
                            },
                        ),
                        "UrisVersion": ("V", "i=15003", {}),
                        "VendorServerInfo": ("O", "i=2011", {}),
                    },
                ),
                "SessionDiagnosticsObjectType": (
                    "OT",
                    "i=2029",
                    {
                        "CurrentRoleIds": ("V", "i=19303", {}),
                        "SessionDiagnostics": (
                            "V",
                            "i=2030",
                            {
                                "ActualSessionTimeout": ("V", "i=3137", {}),
                                "AddNodesCount": ("V", "i=3168", {}),
                                "AddReferencesCount": ("V", "i=3169", {}),
                                "BrowseCount": ("V", "i=3172", {}),
                                "BrowseNextCount": ("V", "i=3173", {}),
                                "CallCount": ("V", "i=3155", {}),
                                "ClientConnectionTime": ("V", "i=3139", {}),
                                "ClientDescription": ("V", "i=3133", {}),
                                "ClientLastContactTime": ("V", "i=3140", {}),
                                "CreateMonitoredItemsCount": ("V", "i=3156", {}),
                                "CreateSubscriptionCount": ("V", "i=3161", {}),
                                "CurrentMonitoredItemsCount": ("V", "i=3142", {}),
                                "CurrentPublishRequestsInQueue": ("V", "i=3143", {}),
                                "CurrentSubscriptionsCount": ("V", "i=3141", {}),
                                "DeleteMonitoredItemsCount": ("V", "i=3160", {}),
                                "DeleteNodesCount": ("V", "i=3170", {}),
                                "DeleteReferencesCount": ("V", "i=3171", {}),
                                "DeleteSubscriptionsCount": ("V", "i=3167", {}),
                                "EndpointUrl": ("V", "i=3135", {}),
                                "HistoryReadCount": ("V", "i=3152", {}),
                                "HistoryUpdateCount": ("V", "i=3154", {}),
                                "LocaleIds": ("V", "i=3136", {}),
                                "MaxResponseMessageSize": ("V", "i=3138", {}),
                                "ModifyMonitoredItemsCount": ("V", "i=3157", {}),
                                "ModifySubscriptionCount": ("V", "i=3162", {}),
                                "PublishCount": ("V", "i=3164", {}),
                                "QueryFirstCount": ("V", "i=3175", {}),
                                "QueryNextCount": ("V", "i=3176", {}),
                                "ReadCount": ("V", "i=3151", {}),
                                "RegisterNodesCount": ("V", "i=3177", {}),
                                "RepublishCount": ("V", "i=3165", {}),
                                "ServerUri": ("V", "i=3134", {}),
                                "SessionId": ("V", "i=3131", {}),
                                "SessionName": ("V", "i=3132", {}),
                                "SetMonitoringModeCount": ("V", "i=3158", {}),
                                "SetPublishingModeCount": ("V", "i=3163", {}),
                                "SetTriggeringCount": ("V", "i=3159", {}),
                                "TotalRequestCount": ("V", "i=8898", {}),
                                "TransferSubscriptionsCount": ("V", "i=3166", {}),
                                "TranslateBrowsePathsToNodeIdsCount": (
                                    "V",
                                    "i=3174",
                                    {},
                                ),
                                "UnauthorizedRequestCount": ("V", "i=11891", {}),
                                "UnregisterNodesCount": ("V", "i=3178", {}),
                                "WriteCount": ("V", "i=3153", {}),
                            },
                        ),
                        "SessionSecurityDiagnostics": (
                            "V",
                            "i=2031",
                            {
                                "AuthenticationMechanism": ("V", "i=3182", {}),
                                "ClientCertificate": ("V", "i=3187", {}),
                                "ClientUserIdHistory": ("V", "i=3181", {}),
                                "ClientUserIdOfSession": ("V", "i=3180", {}),
                                "Encoding": ("V", "i=3183", {}),
                                "SecurityMode": ("V", "i=3185", {}),
                                "SecurityPolicyUri": ("V", "i=3186", {}),
                                "SessionId": ("V", "i=3179", {}),
                                "TransportProtocol": ("V", "i=3184", {}),
                            },
                        ),
                        "SubscriptionDiagnosticsArray": ("V", "i=2032", {}),
                    },
                ),
                "SessionsDiagnosticsSummaryType": (
                    "OT",
                    "i=2026",
                    {
                        "<ClientName>": (
                            "O",
                            "i=12097",
                            {
                                "SessionDiagnostics": (
                                    "V",
                                    "i=12098",
                                    {
                                        "ActualSessionTimeout": ("V", "i=12105", {}),
                                        "AddNodesCount": ("V", "i=12131", {}),
                                        "AddReferencesCount": ("V", "i=12132", {}),
                                        "BrowseCount": ("V", "i=12135", {}),
                                        "BrowseNextCount": ("V", "i=12136", {}),
                                        "CallCount": ("V", "i=12118", {}),
                                        "ClientConnectionTime": ("V", "i=12107", {}),
                                        "ClientDescription": ("V", "i=12101", {}),
                                        "ClientLastContactTime": ("V", "i=12108", {}),
                                        "CreateMonitoredItemsCount": (
                                            "V",
                                            "i=12119",
                                            {},
                                        ),
                                        "CreateSubscriptionCount": ("V", "i=12124", {}),
                                        "CurrentMonitoredItemsCount": (
                                            "V",
                                            "i=12110",
                                            {},
                                        ),
                                        "CurrentPublishRequestsInQueue": (
                                            "V",
                                            "i=12111",
                                            {},
                                        ),
                                        "CurrentSubscriptionsCount": (
                                            "V",
                                            "i=12109",
                                            {},
                                        ),
                                        "DeleteMonitoredItemsCount": (
                                            "V",
                                            "i=12123",
                                            {},
                                        ),
                                        "DeleteNodesCount": ("V", "i=12133", {}),
                                        "DeleteReferencesCount": ("V", "i=12134", {}),
                                        "DeleteSubscriptionsCount": (
                                            "V",
                                            "i=12130",
                                            {},
                                        ),
                                        "EndpointUrl": ("V", "i=12103", {}),
                                        "HistoryReadCount": ("V", "i=12115", {}),
                                        "HistoryUpdateCount": ("V", "i=12117", {}),
                                        "LocaleIds": ("V", "i=12104", {}),
                                        "MaxResponseMessageSize": ("V", "i=12106", {}),
                                        "ModifyMonitoredItemsCount": (
                                            "V",
                                            "i=12120",
                                            {},
                                        ),
                                        "ModifySubscriptionCount": ("V", "i=12125", {}),
                                        "PublishCount": ("V", "i=12127", {}),
                                        "QueryFirstCount": ("V", "i=12138", {}),
                                        "QueryNextCount": ("V", "i=12139", {}),
                                        "ReadCount": ("V", "i=12114", {}),
                                        "RegisterNodesCount": ("V", "i=12140", {}),
                                        "RepublishCount": ("V", "i=12128", {}),
                                        "ServerUri": ("V", "i=12102", {}),
                                        "SessionId": ("V", "i=12099", {}),
                                        "SessionName": ("V", "i=12100", {}),
                                        "SetMonitoringModeCount": ("V", "i=12121", {}),
                                        "SetPublishingModeCount": ("V", "i=12126", {}),
                                        "SetTriggeringCount": ("V", "i=12122", {}),
                                        "TotalRequestCount": ("V", "i=12112", {}),
                                        "TransferSubscriptionsCount": (
                                            "V",
                                            "i=12129",
                                            {},
                                        ),
                                        "TranslateBrowsePathsToNodeIdsCount": (
                                            "V",
                                            "i=12137",
                                            {},
                                        ),
                                        "UnauthorizedRequestCount": (
                                            "V",
                                            "i=12113",
                                            {},
                                        ),
                                        "UnregisterNodesCount": ("V", "i=12141", {}),
                                        "WriteCount": ("V", "i=12116", {}),
                                    },
                                ),
                                "SessionSecurityDiagnostics": (
                                    "V",
                                    "i=12142",
                                    {
                                        "AuthenticationMechanism": ("V", "i=12146", {}),
                                        "ClientCertificate": ("V", "i=12151", {}),
                                        "ClientUserIdHistory": ("V", "i=12145", {}),
                                        "ClientUserIdOfSession": ("V", "i=12144", {}),
                                        "Encoding": ("V", "i=12147", {}),
                                        "SecurityMode": ("V", "i=12149", {}),
                                        "SecurityPolicyUri": ("V", "i=12150", {}),
                                        "SessionId": ("V", "i=12143", {}),
                                        "TransportProtocol": ("V", "i=12148", {}),
                                    },
                                ),
                                "SubscriptionDiagnosticsArray": ("V", "i=12152", {}),
                            },
                        ),
                        "SessionDiagnosticsArray": ("V", "i=2027", {}),
                        "SessionSecurityDiagnosticsArray": ("V", "i=2028", {}),
                    },
                ),
                "StandaloneSubscribedDataSetType": (
                    "OT",
                    "i=23828",
                    {
                        "DataSetMetaData": ("V", "i=23830", {}),
                        "IsConnected": ("V", "i=23831", {}),
                        "SubscribedDataSet": ("O", "i=23829", {}),
                    },
                ),
                "StateMachineType": (
                    "OT",
                    "i=2299",
                    {
                        "CurrentState": ("V", "i=2769", {"Id": ("V", "i=3720", {})}),
                        "FiniteStateMachineType": (
                            "OT",
                            "i=2771",
                            {
                                "AvailableStates": ("V", "i=17635", {}),
                                "AvailableTransitions": ("V", "i=17636", {}),
                                "CurrentState": (
                                    "V",
                                    "i=2772",
                                    {"Id": ("V", "i=3728", {})},
                                ),
                                "ExclusiveLimitStateMachineType": (
                                    "OT",
                                    "i=9318",
                                    {
                                        "High": (
                                            "O",
                                            "i=9331",
                                            {"StateNumber": ("V", "i=9332", {})},
                                        ),
                                        "HighHigh": (
                                            "O",
                                            "i=9329",
                                            {"StateNumber": ("V", "i=9330", {})},
                                        ),
                                        "HighHighToHigh": (
                                            "O",
                                            "i=9339",
                                            {"TransitionNumber": ("V", "i=11342", {})},
                                        ),
                                        "HighToHighHigh": (
                                            "O",
                                            "i=9340",
                                            {"TransitionNumber": ("V", "i=11343", {})},
                                        ),
                                        "Low": (
                                            "O",
                                            "i=9333",
                                            {"StateNumber": ("V", "i=9334", {})},
                                        ),
                                        "LowLow": (
                                            "O",
                                            "i=9335",
                                            {"StateNumber": ("V", "i=9336", {})},
                                        ),
                                        "LowLowToLow": (
                                            "O",
                                            "i=9337",
                                            {"TransitionNumber": ("V", "i=11340", {})},
                                        ),
                                        "LowToLowLow": (
                                            "O",
                                            "i=9338",
                                            {"TransitionNumber": ("V", "i=11341", {})},
                                        ),
                                    },
                                ),
                                "FileTransferStateMachineType": (
                                    "OT",
                                    "i=15803",
                                    {
                                        "ApplyWrite": (
                                            "O",
                                            "i=15821",
                                            {"StateNumber": ("V", "i=15822", {})},
                                        ),
                                        "ApplyWriteToError": (
                                            "O",
                                            "i=15839",
                                            {"TransitionNumber": ("V", "i=15840", {})},
                                        ),
                                        "ApplyWriteToIdle": (
                                            "O",
                                            "i=15833",
                                            {"TransitionNumber": ("V", "i=15834", {})},
                                        ),
                                        "Error": (
                                            "O",
                                            "i=15823",
                                            {"StateNumber": ("V", "i=15824", {})},
                                        ),
                                        "ErrorToIdle": (
                                            "O",
                                            "i=15841",
                                            {"TransitionNumber": ("V", "i=15842", {})},
                                        ),
                                        "Idle": (
                                            "O",
                                            "i=15815",
                                            {"StateNumber": ("V", "i=15816", {})},
                                        ),
                                        "IdleToApplyWrite": (
                                            "O",
                                            "i=15831",
                                            {"TransitionNumber": ("V", "i=15832", {})},
                                        ),
                                        "IdleToReadPrepare": (
                                            "O",
                                            "i=15825",
                                            {"TransitionNumber": ("V", "i=15826", {})},
                                        ),
                                        "ReadPrepare": (
                                            "O",
                                            "i=15817",
                                            {"StateNumber": ("V", "i=15818", {})},
                                        ),
                                        "ReadPrepareToError": (
                                            "O",
                                            "i=15835",
                                            {"TransitionNumber": ("V", "i=15836", {})},
                                        ),
                                        "ReadPrepareToReadTransfer": (
                                            "O",
                                            "i=15827",
                                            {"TransitionNumber": ("V", "i=15828", {})},
                                        ),
                                        "ReadTransfer": (
                                            "O",
                                            "i=15819",
                                            {"StateNumber": ("V", "i=15820", {})},
                                        ),
                                        "ReadTransferToError": (
                                            "O",
                                            "i=15837",
                                            {"TransitionNumber": ("V", "i=15838", {})},
                                        ),
                                        "ReadTransferToIdle": (
                                            "O",
                                            "i=15829",
                                            {"TransitionNumber": ("V", "i=15830", {})},
                                        ),
                                        "Reset": ("M", "i=15843", {}),
                                    },
                                ),
                                "LastTransition": (
                                    "V",
                                    "i=2773",
                                    {"Id": ("V", "i=3732", {})},
                                ),
                                "ProgramStateMachineType": (
                                    "OT",
                                    "i=2391",
                                    {
                                        "AutoDelete": ("V", "i=2394", {}),
                                        "Creatable": ("V", "i=2392", {}),
                                        "CurrentState": (
                                            "V",
                                            "i=3830",
                                            {
                                                "Id": ("V", "i=3831", {}),
                                                "Number": ("V", "i=3833", {}),
                                            },
                                        ),
                                        "Deletable": ("V", "i=2393", {}),
                                        "FinalResultData": ("O", "i=3850", {}),
                                        "Halt": ("M", "i=2429", {}),
                                        "Halted": (
                                            "O",
                                            "i=2406",
                                            {"StateNumber": ("V", "i=2407", {})},
                                        ),
                                        "HaltedToReady": (
                                            "O",
                                            "i=2408",
                                            {"TransitionNumber": ("V", "i=2409", {})},
                                        ),
                                        "InstanceCount": ("V", "i=2396", {}),
                                        "LastTransition": (
                                            "V",
                                            "i=3835",
                                            {
                                                "Id": ("V", "i=3836", {}),
                                                "Number": ("V", "i=3838", {}),
                                                "TransitionTime": ("V", "i=3839", {}),
                                            },
                                        ),
                                        "MaxInstanceCount": ("V", "i=2397", {}),
                                        "MaxRecycleCount": ("V", "i=2398", {}),
                                        "ProgramDiagnostic": (
                                            "V",
                                            "i=2399",
                                            {
                                                "CreateClientName": ("V", "i=3841", {}),
                                                "CreateSessionId": ("V", "i=3840", {}),
                                                "InvocationCreationTime": (
                                                    "V",
                                                    "i=3842",
                                                    {},
                                                ),
                                                "LastMethodCall": ("V", "i=3844", {}),
                                                "LastMethodCallTime": (
                                                    "V",
                                                    "i=3848",
                                                    {},
                                                ),
                                                "LastMethodInputArguments": (
                                                    "V",
                                                    "i=3846",
                                                    {},
                                                ),
                                                "LastMethodInputValues": (
                                                    "V",
                                                    "i=15038",
                                                    {},
                                                ),
                                                "LastMethodOutputArguments": (
                                                    "V",
                                                    "i=3847",
                                                    {},
                                                ),
                                                "LastMethodOutputValues": (
                                                    "V",
                                                    "i=15040",
                                                    {},
                                                ),
                                                "LastMethodReturnStatus": (
                                                    "V",
                                                    "i=3849",
                                                    {},
                                                ),
                                                "LastMethodSessionId": (
                                                    "V",
                                                    "i=3845",
                                                    {},
                                                ),
                                                "LastTransitionTime": (
                                                    "V",
                                                    "i=3843",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Ready": (
                                            "O",
                                            "i=2400",
                                            {"StateNumber": ("V", "i=2401", {})},
                                        ),
                                        "ReadyToHalted": (
                                            "O",
                                            "i=2424",
                                            {"TransitionNumber": ("V", "i=2425", {})},
                                        ),
                                        "ReadyToRunning": (
                                            "O",
                                            "i=2410",
                                            {"TransitionNumber": ("V", "i=2411", {})},
                                        ),
                                        "RecycleCount": ("V", "i=2395", {}),
                                        "Reset": ("M", "i=2430", {}),
                                        "Resume": ("M", "i=2428", {}),
                                        "Running": (
                                            "O",
                                            "i=2402",
                                            {"StateNumber": ("V", "i=2403", {})},
                                        ),
                                        "RunningToHalted": (
                                            "O",
                                            "i=2412",
                                            {"TransitionNumber": ("V", "i=2413", {})},
                                        ),
                                        "RunningToReady": (
                                            "O",
                                            "i=2414",
                                            {"TransitionNumber": ("V", "i=2415", {})},
                                        ),
                                        "RunningToSuspended": (
                                            "O",
                                            "i=2416",
                                            {"TransitionNumber": ("V", "i=2417", {})},
                                        ),
                                        "Start": ("M", "i=2426", {}),
                                        "Suspend": ("M", "i=2427", {}),
                                        "Suspended": (
                                            "O",
                                            "i=2404",
                                            {"StateNumber": ("V", "i=2405", {})},
                                        ),
                                        "SuspendedToHalted": (
                                            "O",
                                            "i=2420",
                                            {"TransitionNumber": ("V", "i=2421", {})},
                                        ),
                                        "SuspendedToReady": (
                                            "O",
                                            "i=2422",
                                            {"TransitionNumber": ("V", "i=2423", {})},
                                        ),
                                        "SuspendedToRunning": (
                                            "O",
                                            "i=2418",
                                            {"TransitionNumber": ("V", "i=2419", {})},
                                        ),
                                    },
                                ),
                                "ShelvedStateMachineType": (
                                    "OT",
                                    "i=2929",
                                    {
                                        "OneShotShelve": ("M", "i=2948", {}),
                                        "OneShotShelve2": (
                                            "M",
                                            "i=24760",
                                            {"InputArguments": ("V", "i=24761", {})},
                                        ),
                                        "OneShotShelved": (
                                            "O",
                                            "i=2933",
                                            {"StateNumber": ("V", "i=6101", {})},
                                        ),
                                        "OneShotShelvedToTimedShelved": (
                                            "O",
                                            "i=2945",
                                            {"TransitionNumber": ("V", "i=11327", {})},
                                        ),
                                        "OneShotShelvedToUnshelved": (
                                            "O",
                                            "i=2943",
                                            {"TransitionNumber": ("V", "i=11326", {})},
                                        ),
                                        "TimedShelve": (
                                            "M",
                                            "i=2949",
                                            {"InputArguments": ("V", "i=2991", {})},
                                        ),
                                        "TimedShelve2": (
                                            "M",
                                            "i=24756",
                                            {"InputArguments": ("V", "i=24757", {})},
                                        ),
                                        "TimedShelved": (
                                            "O",
                                            "i=2932",
                                            {"StateNumber": ("V", "i=6100", {})},
                                        ),
                                        "TimedShelvedToOneShotShelved": (
                                            "O",
                                            "i=2942",
                                            {"TransitionNumber": ("V", "i=11325", {})},
                                        ),
                                        "TimedShelvedToUnshelved": (
                                            "O",
                                            "i=2940",
                                            {"TransitionNumber": ("V", "i=11324", {})},
                                        ),
                                        "Unshelve": ("M", "i=2947", {}),
                                        "Unshelve2": (
                                            "M",
                                            "i=24758",
                                            {"InputArguments": ("V", "i=24759", {})},
                                        ),
                                        "UnshelveTime": ("V", "i=9115", {}),
                                        "Unshelved": (
                                            "O",
                                            "i=2930",
                                            {"StateNumber": ("V", "i=6098", {})},
                                        ),
                                        "UnshelvedToOneShotShelved": (
                                            "O",
                                            "i=2936",
                                            {"TransitionNumber": ("V", "i=11323", {})},
                                        ),
                                        "UnshelvedToTimedShelved": (
                                            "O",
                                            "i=2935",
                                            {"TransitionNumber": ("V", "i=11322", {})},
                                        ),
                                    },
                                ),
                            },
                        ),
                        "LastTransition": ("V", "i=2770", {"Id": ("V", "i=3724", {})}),
                    },
                ),
                "StateType": (
                    "OT",
                    "i=2307",
                    {
                        "ChoiceStateType": ("OT", "i=15109", {}),
                        "InitialStateType": ("OT", "i=2309", {}),
                        "StateNumber": ("V", "i=2308", {}),
                    },
                ),
                "SubscribedDataSetType": (
                    "OT",
                    "i=15108",
                    {
                        "SubscribedDataSetMirrorType": ("OT", "i=15127", {}),
                        "TargetVariablesType": (
                            "OT",
                            "i=15111",
                            {
                                "AddTargetVariables": (
                                    "M",
                                    "i=15115",
                                    {
                                        "InputArguments": ("V", "i=15116", {}),
                                        "OutputArguments": ("V", "i=15117", {}),
                                    },
                                ),
                                "RemoveTargetVariables": (
                                    "M",
                                    "i=15118",
                                    {
                                        "InputArguments": ("V", "i=15119", {}),
                                        "OutputArguments": ("V", "i=15120", {}),
                                    },
                                ),
                                "TargetVariables": ("V", "i=15114", {}),
                            },
                        ),
                    },
                ),
                "SubtypeRestrictionType": ("OT", "i=19822", {}),
                "TemporaryFileTransferType": (
                    "OT",
                    "i=15744",
                    {
                        "<TransferState>": (
                            "O",
                            "i=15754",
                            {
                                "CurrentState": (
                                    "V",
                                    "i=15755",
                                    {"Id": ("V", "i=15756", {})},
                                ),
                                "Reset": ("M", "i=15794", {}),
                            },
                        ),
                        "ClientProcessingTimeout": ("V", "i=15745", {}),
                        "CloseAndCommit": (
                            "M",
                            "i=15751",
                            {
                                "InputArguments": ("V", "i=15752", {}),
                                "OutputArguments": ("V", "i=15753", {}),
                            },
                        ),
                        "GenerateFileForRead": (
                            "M",
                            "i=15746",
                            {
                                "InputArguments": ("V", "i=15747", {}),
                                "OutputArguments": ("V", "i=15748", {}),
                            },
                        ),
                        "GenerateFileForWrite": (
                            "M",
                            "i=15749",
                            {
                                "InputArguments": ("V", "i=16359", {}),
                                "OutputArguments": ("V", "i=15750", {}),
                            },
                        ),
                    },
                ),
                "TransactionDiagnosticsType": (
                    "OT",
                    "i=32286",
                    {
                        "AffectedCertificateGroups": ("V", "i=32291", {}),
                        "AffectedTrustLists": ("V", "i=32290", {}),
                        "EndTime": ("V", "i=32288", {}),
                        "Errors": ("V", "i=32292", {}),
                        "Result": ("V", "i=32289", {}),
                        "StartTime": ("V", "i=32287", {}),
                    },
                ),
                "TransitionType": (
                    "OT",
                    "i=2310",
                    {"TransitionNumber": ("V", "i=2312", {})},
                ),
                "UnitType": (
                    "OT",
                    "i=32442",
                    {
                        "AlternativeUnitType": (
                            "OT",
                            "i=32467",
                            {
                                "LinearConversion": ("V", "i=32472", {}),
                                "MathMLConversion": ("V", "i=32473", {}),
                                "MathMLInverseConversion": ("V", "i=32474", {}),
                            },
                        ),
                        "Discipline": ("V", "i=32446", {}),
                        "ServerUnitType": (
                            "OT",
                            "i=32447",
                            {
                                "AlternativeUnits": (
                                    "O",
                                    "i=32452",
                                    {
                                        "<AlternativeUnit>": (
                                            "O",
                                            "i=32587",
                                            {
                                                "Symbol": ("V", "i=32588", {}),
                                                "UnitSystem": ("V", "i=32590", {}),
                                            },
                                        )
                                    },
                                ),
                                "CoherentUnit": (
                                    "O",
                                    "i=32462",
                                    {
                                        "Symbol": ("V", "i=32463", {}),
                                        "UnitSystem": ("V", "i=32465", {}),
                                    },
                                ),
                                "ConversionLimit": ("V", "i=32461", {}),
                            },
                        ),
                        "Symbol": ("V", "i=32443", {}),
                        "UnitSystem": ("V", "i=32445", {}),
                    },
                ),
                "UserManagementType": (
                    "OT",
                    "i=24264",
                    {
                        "AddUser": (
                            "M",
                            "i=24269",
                            {"InputArguments": ("V", "i=24270", {})},
                        ),
                        "ChangePassword": (
                            "M",
                            "i=24275",
                            {"InputArguments": ("V", "i=24276", {})},
                        ),
                        "ModifyUser": (
                            "M",
                            "i=24271",
                            {"InputArguments": ("V", "i=24272", {})},
                        ),
                        "PasswordLength": ("V", "i=24266", {}),
                        "PasswordOptions": ("V", "i=24267", {}),
                        "PasswordRestrictions": ("V", "i=24268", {}),
                        "RemoveUser": (
                            "M",
                            "i=24273",
                            {"InputArguments": ("V", "i=24274", {})},
                        ),
                        "Users": ("V", "i=24265", {}),
                    },
                ),
                "VendorServerInfoType": ("OT", "i=2033", {}),
                "WriterGroupMessageType": (
                    "OT",
                    "i=17998",
                    {
                        "JsonWriterGroupMessageType": (
                            "OT",
                            "i=21126",
                            {"NetworkMessageContentMask": ("V", "i=21127", {})},
                        ),
                        "UadpWriterGroupMessageType": (
                            "OT",
                            "i=21105",
                            {
                                "DataSetOrdering": ("V", "i=21107", {}),
                                "GroupVersion": ("V", "i=21106", {}),
                                "NetworkMessageContentMask": ("V", "i=21108", {}),
                                "PublishingOffset": ("V", "i=21110", {}),
                                "SamplingOffset": ("V", "i=21109", {}),
                            },
                        ),
                    },
                ),
                "WriterGroupTransportType": (
                    "OT",
                    "i=17997",
                    {
                        "BrokerWriterGroupTransportType": (
                            "OT",
                            "i=21136",
                            {
                                "AuthenticationProfileUri": ("V", "i=15247", {}),
                                "QueueName": ("V", "i=21137", {}),
                                "RequestedDeliveryGuarantee": ("V", "i=15249", {}),
                                "ResourceUri": ("V", "i=15246", {}),
                            },
                        ),
                        "DatagramWriterGroupTransportType": (
                            "OT",
                            "i=21133",
                            {
                                "Address": (
                                    "O",
                                    "i=23842",
                                    {
                                        "NetworkInterface": (
                                            "V",
                                            "i=23843",
                                            {"Selections": ("V", "i=23844", {})},
                                        )
                                    },
                                ),
                                "DatagramQos": ("V", "i=23847", {}),
                                "DiscoveryAnnounceRate": ("V", "i=23848", {}),
                                "MessageRepeatCount": ("V", "i=21134", {}),
                                "MessageRepeatDelay": ("V", "i=21135", {}),
                                "QosCategory": ("V", "i=25527", {}),
                                "Topic": ("V", "i=23849", {}),
                            },
                        ),
                    },
                ),
            },
        )
    },
    "reftypes": {
        "References": (
            "RT",
            "i=31",
            {
                "HierarchicalReferences": (
                    "RT",
                    "i=33",
                    {
                        "AllowedSubtype": ("RT", "i=19819", {}),
                        "Controls": ("RT", "i=25254", {}),
                        "DataSetToWriter": ("RT", "i=14936", {}),
                        "HasChild": (
                            "RT",
                            "i=34",
                            {
                                "Aggregates": (
                                    "RT",
                                    "i=44",
                                    {
                                        "HasComponent": (
                                            "RT",
                                            "i=47",
                                            {
                                                "HasAddIn": ("RT", "i=17604", {}),
                                                "HasAlarmSuppressionGroup": (
                                                    "RT",
                                                    "i=16361",
                                                    {},
                                                ),
                                                "HasArgumentDescription": (
                                                    "RT",
                                                    "i=129",
                                                    {
                                                        "HasOptionalInputArgumentDescription": (
                                                            "RT",
                                                            "i=131",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "HasDataSetReader": (
                                                    "RT",
                                                    "i=15297",
                                                    {},
                                                ),
                                                "HasDataSetWriter": (
                                                    "RT",
                                                    "i=15296",
                                                    {},
                                                ),
                                                "HasGuard": ("RT", "i=15112", {}),
                                                "HasOrderedComponent": (
                                                    "RT",
                                                    "i=49",
                                                    {},
                                                ),
                                                "HasPhysicalComponent": (
                                                    "RT",
                                                    "i=25262",
                                                    {
                                                        "HasAttachedComponent": (
                                                            "RT",
                                                            "i=25264",
                                                            {},
                                                        ),
                                                        "HasContainedComponent": (
                                                            "RT",
                                                            "i=25263",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "HasPubSubConnection": (
                                                    "RT",
                                                    "i=14476",
                                                    {},
                                                ),
                                                "HasReaderGroup": ("RT", "i=18805", {}),
                                                "HasStructuredComponent": (
                                                    "RT",
                                                    "i=24136",
                                                    {},
                                                ),
                                                "HasWriterGroup": ("RT", "i=18804", {}),
                                            },
                                        ),
                                        "HasHistoricalConfiguration": (
                                            "RT",
                                            "i=56",
                                            {},
                                        ),
                                        "HasProperty": ("RT", "i=46", {}),
                                    },
                                ),
                                "HasDataTypeRefinement": ("RT", "i=19846", {}),
                                "HasReferenceDescription": ("RT", "i=32679", {}),
                                "HasSubtype": ("RT", "i=45", {}),
                            },
                        ),
                        "HasEventSource": (
                            "RT",
                            "i=36",
                            {"HasNotifier": ("RT", "i=48", {})},
                        ),
                        "HasFieldDescription": (
                            "RT",
                            "i=19815",
                            {
                                "HasFieldDescriptionSetMandatory": (
                                    "RT",
                                    "i=19816",
                                    {},
                                ),
                                "IsDisabledOptionalField": ("RT", "i=19817", {}),
                            },
                        ),
                        "HasLowerLayerInterface": ("RT", "i=25238", {}),
                        "HasPushedSecurityGroup": ("RT", "i=25345", {}),
                        "HasSerializationEntity": ("RT", "i=19845", {}),
                        "Organizes": (
                            "RT",
                            "i=35",
                            {
                                "AlarmGroupMember": (
                                    "RT",
                                    "i=16362",
                                    {
                                        "AlarmSuppressionGroupMember": (
                                            "RT",
                                            "i=32059",
                                            {},
                                        )
                                    },
                                )
                            },
                        ),
                        "Requires": ("RT", "i=25256", {}),
                    },
                ),
                "NonHierarchicalReferences": (
                    "RT",
                    "i=32",
                    {
                        "AliasFor": ("RT", "i=23469", {}),
                        "AssociatedWith": ("RT", "i=24137", {}),
                        "FromState": ("RT", "i=51", {}),
                        "GeneratesEvent": (
                            "RT",
                            "i=41",
                            {"AlwaysGeneratesEvent": ("RT", "i=3065", {})},
                        ),
                        "HasCause": ("RT", "i=53", {}),
                        "HasCondition": ("RT", "i=9006", {}),
                        "HasCurrentData": ("RT", "i=32633", {}),
                        "HasCurrentEvent": ("RT", "i=32634", {}),
                        "HasDescription": ("RT", "i=39", {}),
                        "HasDictionaryEntry": ("RT", "i=17597", {}),
                        "HasEffect": (
                            "RT",
                            "i=54",
                            {
                                "HasEffectDisable": ("RT", "i=17276", {}),
                                "HasEffectEnable": ("RT", "i=17983", {}),
                                "HasEffectSuppressed": ("RT", "i=17984", {}),
                                "HasEffectUnsuppressed": ("RT", "i=17985", {}),
                            },
                        ),
                        "HasEncoding": ("RT", "i=38", {}),
                        "HasEngineeringUnitDetails": ("RT", "i=32558", {}),
                        "HasFalseSubState": ("RT", "i=9005", {}),
                        "HasInterface": ("RT", "i=17603", {}),
                        "HasKeyValueDescription": ("RT", "i=32407", {}),
                        "HasModellingRule": ("RT", "i=37", {}),
                        "HasQuantity": ("RT", "i=32559", {}),
                        "HasSubStateMachine": ("RT", "i=117", {}),
                        "HasTrueSubState": ("RT", "i=9004", {}),
                        "HasTypeDefinition": ("RT", "i=40", {}),
                        "IsDeprecated": ("RT", "i=23562", {}),
                        "IsExecutableOn": ("RT", "i=25253", {}),
                        "IsPhysicallyConnectedTo": ("RT", "i=25257", {}),
                        "RepresentsSameEntityAs": (
                            "RT",
                            "i=25258",
                            {
                                "RepresentsSameFunctionalityAs": ("RT", "i=25260", {}),
                                "RepresentsSameHardwareAs": ("RT", "i=25259", {}),
                            },
                        ),
                        "ToState": ("RT", "i=52", {}),
                        "UsesDataTypeRefinement": ("RT", "i=19814", {}),
                        "UsesPriorityMappingTable": ("RT", "i=25237", {}),
                        "UsesSubtypeRestriction": ("RT", "i=19818", {}),
                        "Utilizes": (
                            "RT",
                            "i=25255",
                            {
                                "IsExecutingOn": ("RT", "i=25265", {}),
                                "IsHostedBy": ("RT", "i=25261", {}),
                            },
                        ),
                    },
                ),
            },
        )
    },
    "vartypes": {
        "BaseVariableType": (
            "VT",
            "i=62",
            {
                "BaseDataVariableType": (
                    "VT",
                    "i=63",
                    {
                        "AlarmRateVariableType": (
                            "VT",
                            "i=17277",
                            {"Rate": ("V", "i=17278", {})},
                        ),
                        "AlarmStateVariableType": (
                            "VT",
                            "i=32244",
                            {
                                "ActiveCount": ("V", "i=32247", {}),
                                "Filter": ("V", "i=32250", {}),
                                "HighestActiveSeverity": ("V", "i=32245", {}),
                                "HighestUnackSeverity": ("V", "i=32246", {}),
                                "UnacknowledgedCount": ("V", "i=32248", {}),
                                "UnconfirmedCount": ("V", "i=32249", {}),
                            },
                        ),
                        "AudioVariableType": (
                            "VT",
                            "i=17986",
                            {
                                "AgencyId": ("V", "i=17989", {}),
                                "ListId": ("V", "i=17988", {}),
                                "VersionId": ("V", "i=17990", {}),
                            },
                        ),
                        "BitFieldType": (
                            "VT",
                            "i=32431",
                            {
                                "<FieldName>": ("V", "i=32433", {}),
                                "<OptionalFieldName>": ("V", "i=15014", {}),
                                "BitFieldsDefinitions": ("V", "i=32432", {}),
                            },
                        ),
                        "BuildInfoType": (
                            "VT",
                            "i=3051",
                            {
                                "BuildDate": ("V", "i=3057", {}),
                                "BuildNumber": ("V", "i=3056", {}),
                                "ManufacturerName": ("V", "i=3053", {}),
                                "ProductName": ("V", "i=3054", {}),
                                "ProductUri": ("V", "i=3052", {}),
                                "SoftwareVersion": ("V", "i=3055", {}),
                            },
                        ),
                        "CartesianCoordinatesType": (
                            "VT",
                            "i=18772",
                            {
                                "3DCartesianCoordinatesType": (
                                    "VT",
                                    "i=18774",
                                    {
                                        "X": ("V", "i=18776", {}),
                                        "Y": ("V", "i=18777", {}),
                                        "Z": ("V", "i=18778", {}),
                                    },
                                ),
                                "LengthUnit": ("V", "i=18773", {}),
                            },
                        ),
                        "ConditionVariableType": (
                            "VT",
                            "i=9002",
                            {"SourceTimestamp": ("V", "i=9003", {})},
                        ),
                        "DataItemType": (
                            "VT",
                            "i=2365",
                            {
                                "ArrayItemType": (
                                    "VT",
                                    "i=12021",
                                    {
                                        "AxisScaleType": ("V", "i=12028", {}),
                                        "CubeItemType": (
                                            "VT",
                                            "i=12057",
                                            {
                                                "XAxisDefinition": ("V", "i=12065", {}),
                                                "YAxisDefinition": ("V", "i=12066", {}),
                                                "ZAxisDefinition": ("V", "i=12067", {}),
                                            },
                                        ),
                                        "EURange": ("V", "i=12025", {}),
                                        "EngineeringUnits": ("V", "i=12026", {}),
                                        "ImageItemType": (
                                            "VT",
                                            "i=12047",
                                            {
                                                "XAxisDefinition": ("V", "i=12055", {}),
                                                "YAxisDefinition": ("V", "i=12056", {}),
                                            },
                                        ),
                                        "InstrumentRange": ("V", "i=12024", {}),
                                        "NDimensionArrayItemType": (
                                            "VT",
                                            "i=12068",
                                            {"AxisDefinition": ("V", "i=12076", {})},
                                        ),
                                        "Title": ("V", "i=12027", {}),
                                        "XYArrayItemType": (
                                            "VT",
                                            "i=12038",
                                            {"XAxisDefinition": ("V", "i=12046", {})},
                                        ),
                                        "YArrayItemType": (
                                            "VT",
                                            "i=12029",
                                            {"XAxisDefinition": ("V", "i=12037", {})},
                                        ),
                                    },
                                ),
                                "BaseAnalogType": (
                                    "VT",
                                    "i=15318",
                                    {
                                        "AnalogItemType": (
                                            "VT",
                                            "i=2368",
                                            {
                                                "AnalogUnitRangeType": (
                                                    "VT",
                                                    "i=17570",
                                                    {
                                                        "EngineeringUnits": (
                                                            "V",
                                                            "i=17575",
                                                            {},
                                                        )
                                                    },
                                                ),
                                                "EURange": ("V", "i=2369", {}),
                                            },
                                        ),
                                        "AnalogUnitType": (
                                            "VT",
                                            "i=17497",
                                            {"EngineeringUnits": ("V", "i=17502", {})},
                                        ),
                                        "EURange": ("V", "i=17568", {}),
                                        "EngineeringUnits": ("V", "i=17569", {}),
                                        "InstrumentRange": ("V", "i=17567", {}),
                                    },
                                ),
                                "Definition": ("V", "i=2366", {}),
                                "DiscreteItemType": (
                                    "VT",
                                    "i=2372",
                                    {
                                        "MultiStateDiscreteType": (
                                            "VT",
                                            "i=2376",
                                            {"EnumStrings": ("V", "i=2377", {})},
                                        ),
                                        "MultiStateValueDiscreteType": (
                                            "VT",
                                            "i=11238",
                                            {
                                                "EnumValues": ("V", "i=11241", {}),
                                                "MultiStateDictionaryEntryDiscreteBaseType": (
                                                    "VT",
                                                    "i=19077",
                                                    {
                                                        "EnumDictionaryEntries": (
                                                            "V",
                                                            "i=19082",
                                                            {},
                                                        ),
                                                        "MultiStateDictionaryEntryDiscreteType": (
                                                            "VT",
                                                            "i=19084",
                                                            {
                                                                "ValueAsDictionaryEntries": (
                                                                    "V",
                                                                    "i=19090",
                                                                    {},
                                                                )
                                                            },
                                                        ),
                                                        "ValueAsDictionaryEntries": (
                                                            "V",
                                                            "i=19083",
                                                            {},
                                                        ),
                                                    },
                                                ),
                                                "ValueAsText": ("V", "i=11461", {}),
                                            },
                                        ),
                                        "TwoStateDiscreteType": (
                                            "VT",
                                            "i=2373",
                                            {
                                                "FalseState": ("V", "i=2374", {}),
                                                "TrueState": ("V", "i=2375", {}),
                                            },
                                        ),
                                    },
                                ),
                                "ValuePrecision": ("V", "i=2367", {}),
                            },
                        ),
                        "DataTypeDescriptionType": (
                            "VT",
                            "i=69",
                            {
                                "DataTypeVersion": ("V", "i=104", {}),
                                "DictionaryFragment": ("V", "i=105", {}),
                            },
                        ),
                        "DataTypeDictionaryType": (
                            "VT",
                            "i=72",
                            {
                                "DataTypeVersion": ("V", "i=106", {}),
                                "Deprecated": ("V", "i=15001", {}),
                                "NamespaceUri": ("V", "i=107", {}),
                            },
                        ),
                        "FrameType": (
                            "VT",
                            "i=18786",
                            {
                                "3DFrameType": (
                                    "VT",
                                    "i=18791",
                                    {
                                        "CartesianCoordinates": (
                                            "V",
                                            "i=18796",
                                            {
                                                "X": ("V", "i=18798", {}),
                                                "Y": ("V", "i=18799", {}),
                                                "Z": ("V", "i=18800", {}),
                                            },
                                        ),
                                        "Orientation": (
                                            "V",
                                            "i=18792",
                                            {
                                                "A": ("V", "i=19074", {}),
                                                "B": ("V", "i=19075", {}),
                                                "C": ("V", "i=19076", {}),
                                            },
                                        ),
                                    },
                                ),
                                "BaseFrame": ("V", "i=18789", {}),
                                "CartesianCoordinates": ("V", "i=18801", {}),
                                "Constant": ("V", "i=18788", {}),
                                "FixedBase": ("V", "i=18790", {}),
                                "Orientation": ("V", "i=18787", {}),
                            },
                        ),
                        "GuardVariableType": (
                            "VT",
                            "i=15113",
                            {
                                "ElseGuardVariableType": ("VT", "i=15317", {}),
                                "ExpressionGuardVariableType": (
                                    "VT",
                                    "i=15128",
                                    {"Expression": ("V", "i=15129", {})},
                                ),
                            },
                        ),
                        "OptionSetType": (
                            "VT",
                            "i=11487",
                            {
                                "BitMask": ("V", "i=11701", {}),
                                "OptionSetValues": ("V", "i=11488", {}),
                            },
                        ),
                        "OrientationType": (
                            "VT",
                            "i=18779",
                            {
                                "3DOrientationType": (
                                    "VT",
                                    "i=18781",
                                    {
                                        "A": ("V", "i=18783", {}),
                                        "B": ("V", "i=18784", {}),
                                        "C": ("V", "i=18785", {}),
                                    },
                                ),
                                "AngleUnit": ("V", "i=18780", {}),
                            },
                        ),
                        "ProgramDiagnostic2Type": (
                            "VT",
                            "i=15383",
                            {
                                "CreateClientName": ("V", "i=15385", {}),
                                "CreateSessionId": ("V", "i=15384", {}),
                                "InvocationCreationTime": ("V", "i=15386", {}),
                                "LastMethodCall": ("V", "i=15388", {}),
                                "LastMethodCallTime": ("V", "i=15394", {}),
                                "LastMethodInputArguments": ("V", "i=15390", {}),
                                "LastMethodInputValues": ("V", "i=15392", {}),
                                "LastMethodOutputArguments": ("V", "i=15391", {}),
                                "LastMethodOutputValues": ("V", "i=15393", {}),
                                "LastMethodReturnStatus": ("V", "i=15395", {}),
                                "LastMethodSessionId": ("V", "i=15389", {}),
                                "LastTransitionTime": ("V", "i=15387", {}),
                            },
                        ),
                        "ProgramDiagnosticType": (
                            "VT",
                            "i=2380",
                            {
                                "CreateClientName": ("V", "i=2382", {}),
                                "CreateSessionId": ("V", "i=2381", {}),
                                "InvocationCreationTime": ("V", "i=2383", {}),
                                "LastMethodCall": ("V", "i=2385", {}),
                                "LastMethodCallTime": ("V", "i=2389", {}),
                                "LastMethodInputArguments": ("V", "i=2387", {}),
                                "LastMethodOutputArguments": ("V", "i=2388", {}),
                                "LastMethodReturnStatus": ("V", "i=2390", {}),
                                "LastMethodSessionId": ("V", "i=2386", {}),
                                "LastTransitionTime": ("V", "i=2384", {}),
                            },
                        ),
                        "PubSubDiagnosticsCounterType": (
                            "VT",
                            "i=19725",
                            {
                                "Active": ("V", "i=19726", {}),
                                "Classification": ("V", "i=19727", {}),
                                "DiagnosticsLevel": ("V", "i=19728", {}),
                                "TimeFirstChange": ("V", "i=19729", {}),
                            },
                        ),
                        "RationalNumberType": (
                            "VT",
                            "i=17709",
                            {
                                "Denominator": ("V", "i=17713", {}),
                                "Numerator": ("V", "i=17712", {}),
                            },
                        ),
                        "ReferenceDescriptionVariableType": (
                            "VT",
                            "i=32657",
                            {"ReferenceRefinement": ("V", "i=32658", {})},
                        ),
                        "SamplingIntervalDiagnosticsArrayType": (
                            "VT",
                            "i=2164",
                            {
                                "SamplingIntervalDiagnostics": (
                                    "V",
                                    "i=12779",
                                    {
                                        "DisabledMonitoredItemsSamplingCount": (
                                            "V",
                                            "i=12783",
                                            {},
                                        ),
                                        "MaxSampledMonitoredItemsCount": (
                                            "V",
                                            "i=12782",
                                            {},
                                        ),
                                        "SampledMonitoredItemsCount": (
                                            "V",
                                            "i=12781",
                                            {},
                                        ),
                                        "SamplingInterval": ("V", "i=12780", {}),
                                    },
                                )
                            },
                        ),
                        "SamplingIntervalDiagnosticsType": (
                            "VT",
                            "i=2165",
                            {
                                "DisabledMonitoredItemsSamplingCount": (
                                    "V",
                                    "i=11699",
                                    {},
                                ),
                                "MaxSampledMonitoredItemsCount": ("V", "i=11698", {}),
                                "SampledMonitoredItemsCount": ("V", "i=11697", {}),
                                "SamplingInterval": ("V", "i=2166", {}),
                            },
                        ),
                        "SelectionListType": (
                            "VT",
                            "i=16309",
                            {
                                "RestrictToList": ("V", "i=16312", {}),
                                "SelectionDescriptions": ("V", "i=17633", {}),
                                "Selections": ("V", "i=17632", {}),
                            },
                        ),
                        "ServerDiagnosticsSummaryType": (
                            "VT",
                            "i=2150",
                            {
                                "CumulatedSessionCount": ("V", "i=2153", {}),
                                "CumulatedSubscriptionCount": ("V", "i=2161", {}),
                                "CurrentSessionCount": ("V", "i=2152", {}),
                                "CurrentSubscriptionCount": ("V", "i=2160", {}),
                                "PublishingIntervalCount": ("V", "i=2159", {}),
                                "RejectedRequestsCount": ("V", "i=2163", {}),
                                "RejectedSessionCount": ("V", "i=2155", {}),
                                "SecurityRejectedRequestsCount": ("V", "i=2162", {}),
                                "SecurityRejectedSessionCount": ("V", "i=2154", {}),
                                "ServerViewCount": ("V", "i=2151", {}),
                                "SessionAbortCount": ("V", "i=2157", {}),
                                "SessionTimeoutCount": ("V", "i=2156", {}),
                            },
                        ),
                        "ServerStatusType": (
                            "VT",
                            "i=2138",
                            {
                                "BuildInfo": (
                                    "V",
                                    "i=2142",
                                    {
                                        "BuildDate": ("V", "i=3703", {}),
                                        "BuildNumber": ("V", "i=3702", {}),
                                        "ManufacturerName": ("V", "i=3699", {}),
                                        "ProductName": ("V", "i=3700", {}),
                                        "ProductUri": ("V", "i=3698", {}),
                                        "SoftwareVersion": ("V", "i=3701", {}),
                                    },
                                ),
                                "CurrentTime": ("V", "i=2140", {}),
                                "SecondsTillShutdown": ("V", "i=2752", {}),
                                "ShutdownReason": ("V", "i=2753", {}),
                                "StartTime": ("V", "i=2139", {}),
                                "State": ("V", "i=2141", {}),
                            },
                        ),
                        "ServerVendorCapabilityType": ("VT", "i=2137", {}),
                        "SessionDiagnosticsArrayType": (
                            "VT",
                            "i=2196",
                            {
                                "SessionDiagnostics": (
                                    "V",
                                    "i=12816",
                                    {
                                        "ActualSessionTimeout": ("V", "i=12823", {}),
                                        "AddNodesCount": ("V", "i=12849", {}),
                                        "AddReferencesCount": ("V", "i=12850", {}),
                                        "BrowseCount": ("V", "i=12853", {}),
                                        "BrowseNextCount": ("V", "i=12854", {}),
                                        "CallCount": ("V", "i=12836", {}),
                                        "ClientConnectionTime": ("V", "i=12825", {}),
                                        "ClientDescription": ("V", "i=12819", {}),
                                        "ClientLastContactTime": ("V", "i=12826", {}),
                                        "CreateMonitoredItemsCount": (
                                            "V",
                                            "i=12837",
                                            {},
                                        ),
                                        "CreateSubscriptionCount": ("V", "i=12842", {}),
                                        "CurrentMonitoredItemsCount": (
                                            "V",
                                            "i=12828",
                                            {},
                                        ),
                                        "CurrentPublishRequestsInQueue": (
                                            "V",
                                            "i=12829",
                                            {},
                                        ),
                                        "CurrentSubscriptionsCount": (
                                            "V",
                                            "i=12827",
                                            {},
                                        ),
                                        "DeleteMonitoredItemsCount": (
                                            "V",
                                            "i=12841",
                                            {},
                                        ),
                                        "DeleteNodesCount": ("V", "i=12851", {}),
                                        "DeleteReferencesCount": ("V", "i=12852", {}),
                                        "DeleteSubscriptionsCount": (
                                            "V",
                                            "i=12848",
                                            {},
                                        ),
                                        "EndpointUrl": ("V", "i=12821", {}),
                                        "HistoryReadCount": ("V", "i=12833", {}),
                                        "HistoryUpdateCount": ("V", "i=12835", {}),
                                        "LocaleIds": ("V", "i=12822", {}),
                                        "MaxResponseMessageSize": ("V", "i=12824", {}),
                                        "ModifyMonitoredItemsCount": (
                                            "V",
                                            "i=12838",
                                            {},
                                        ),
                                        "ModifySubscriptionCount": ("V", "i=12843", {}),
                                        "PublishCount": ("V", "i=12845", {}),
                                        "QueryFirstCount": ("V", "i=12856", {}),
                                        "QueryNextCount": ("V", "i=12857", {}),
                                        "ReadCount": ("V", "i=12832", {}),
                                        "RegisterNodesCount": ("V", "i=12858", {}),
                                        "RepublishCount": ("V", "i=12846", {}),
                                        "ServerUri": ("V", "i=12820", {}),
                                        "SessionId": ("V", "i=12817", {}),
                                        "SessionName": ("V", "i=12818", {}),
                                        "SetMonitoringModeCount": ("V", "i=12839", {}),
                                        "SetPublishingModeCount": ("V", "i=12844", {}),
                                        "SetTriggeringCount": ("V", "i=12840", {}),
                                        "TotalRequestCount": ("V", "i=12830", {}),
                                        "TransferSubscriptionsCount": (
                                            "V",
                                            "i=12847",
                                            {},
                                        ),
                                        "TranslateBrowsePathsToNodeIdsCount": (
                                            "V",
                                            "i=12855",
                                            {},
                                        ),
                                        "UnauthorizedRequestCount": (
                                            "V",
                                            "i=12831",
                                            {},
                                        ),
                                        "UnregisterNodesCount": ("V", "i=12859", {}),
                                        "WriteCount": ("V", "i=12834", {}),
                                    },
                                )
                            },
                        ),
                        "SessionDiagnosticsVariableType": (
                            "VT",
                            "i=2197",
                            {
                                "ActualSessionTimeout": ("V", "i=2204", {}),
                                "AddNodesCount": ("V", "i=2234", {}),
                                "AddReferencesCount": ("V", "i=2235", {}),
                                "BrowseCount": ("V", "i=2238", {}),
                                "BrowseNextCount": ("V", "i=2239", {}),
                                "CallCount": ("V", "i=2221", {}),
                                "ClientConnectionTime": ("V", "i=2205", {}),
                                "ClientDescription": ("V", "i=2200", {}),
                                "ClientLastContactTime": ("V", "i=2206", {}),
                                "CreateMonitoredItemsCount": ("V", "i=2222", {}),
                                "CreateSubscriptionCount": ("V", "i=2227", {}),
                                "CurrentMonitoredItemsCount": ("V", "i=2208", {}),
                                "CurrentPublishRequestsInQueue": ("V", "i=2209", {}),
                                "CurrentSubscriptionsCount": ("V", "i=2207", {}),
                                "DeleteMonitoredItemsCount": ("V", "i=2226", {}),
                                "DeleteNodesCount": ("V", "i=2236", {}),
                                "DeleteReferencesCount": ("V", "i=2237", {}),
                                "DeleteSubscriptionsCount": ("V", "i=2233", {}),
                                "EndpointUrl": ("V", "i=2202", {}),
                                "HistoryReadCount": ("V", "i=2218", {}),
                                "HistoryUpdateCount": ("V", "i=2220", {}),
                                "LocaleIds": ("V", "i=2203", {}),
                                "MaxResponseMessageSize": ("V", "i=3050", {}),
                                "ModifyMonitoredItemsCount": ("V", "i=2223", {}),
                                "ModifySubscriptionCount": ("V", "i=2228", {}),
                                "PublishCount": ("V", "i=2230", {}),
                                "QueryFirstCount": ("V", "i=2241", {}),
                                "QueryNextCount": ("V", "i=2242", {}),
                                "ReadCount": ("V", "i=2217", {}),
                                "RegisterNodesCount": ("V", "i=2730", {}),
                                "RepublishCount": ("V", "i=2231", {}),
                                "ServerUri": ("V", "i=2201", {}),
                                "SessionId": ("V", "i=2198", {}),
                                "SessionName": ("V", "i=2199", {}),
                                "SetMonitoringModeCount": ("V", "i=2224", {}),
                                "SetPublishingModeCount": ("V", "i=2229", {}),
                                "SetTriggeringCount": ("V", "i=2225", {}),
                                "TotalRequestCount": ("V", "i=8900", {}),
                                "TransferSubscriptionsCount": ("V", "i=2232", {}),
                                "TranslateBrowsePathsToNodeIdsCount": (
                                    "V",
                                    "i=2240",
                                    {},
                                ),
                                "UnauthorizedRequestCount": ("V", "i=11892", {}),
                                "UnregisterNodesCount": ("V", "i=2731", {}),
                                "WriteCount": ("V", "i=2219", {}),
                            },
                        ),
                        "SessionSecurityDiagnosticsArrayType": (
                            "VT",
                            "i=2243",
                            {
                                "SessionSecurityDiagnostics": (
                                    "V",
                                    "i=12860",
                                    {
                                        "AuthenticationMechanism": ("V", "i=12864", {}),
                                        "ClientCertificate": ("V", "i=12869", {}),
                                        "ClientUserIdHistory": ("V", "i=12863", {}),
                                        "ClientUserIdOfSession": ("V", "i=12862", {}),
                                        "Encoding": ("V", "i=12865", {}),
                                        "SecurityMode": ("V", "i=12867", {}),
                                        "SecurityPolicyUri": ("V", "i=12868", {}),
                                        "SessionId": ("V", "i=12861", {}),
                                        "TransportProtocol": ("V", "i=12866", {}),
                                    },
                                )
                            },
                        ),
                        "SessionSecurityDiagnosticsType": (
                            "VT",
                            "i=2244",
                            {
                                "AuthenticationMechanism": ("V", "i=2248", {}),
                                "ClientCertificate": ("V", "i=3058", {}),
                                "ClientUserIdHistory": ("V", "i=2247", {}),
                                "ClientUserIdOfSession": ("V", "i=2246", {}),
                                "Encoding": ("V", "i=2249", {}),
                                "SecurityMode": ("V", "i=2251", {}),
                                "SecurityPolicyUri": ("V", "i=2252", {}),
                                "SessionId": ("V", "i=2245", {}),
                                "TransportProtocol": ("V", "i=2250", {}),
                            },
                        ),
                        "StateVariableType": (
                            "VT",
                            "i=2755",
                            {
                                "EffectiveDisplayName": ("V", "i=2759", {}),
                                "FiniteStateVariableType": (
                                    "VT",
                                    "i=2760",
                                    {"Id": ("V", "i=2761", {})},
                                ),
                                "Id": ("V", "i=2756", {}),
                                "Name": ("V", "i=2757", {}),
                                "Number": ("V", "i=2758", {}),
                                "TwoStateVariableType": (
                                    "VT",
                                    "i=8995",
                                    {
                                        "EffectiveTransitionTime": ("V", "i=9001", {}),
                                        "FalseState": ("V", "i=11111", {}),
                                        "Id": ("V", "i=8996", {}),
                                        "TransitionTime": ("V", "i=9000", {}),
                                        "TrueState": ("V", "i=11110", {}),
                                    },
                                ),
                            },
                        ),
                        "SubscriptionDiagnosticsArrayType": (
                            "VT",
                            "i=2171",
                            {
                                "SubscriptionDiagnostics": (
                                    "V",
                                    "i=12784",
                                    {
                                        "CurrentKeepAliveCount": ("V", "i=12807", {}),
                                        "CurrentLifetimeCount": ("V", "i=12808", {}),
                                        "DataChangeNotificationsCount": (
                                            "V",
                                            "i=12803",
                                            {},
                                        ),
                                        "DisableCount": ("V", "i=12795", {}),
                                        "DisabledMonitoredItemCount": (
                                            "V",
                                            "i=12812",
                                            {},
                                        ),
                                        "DiscardedMessageCount": ("V", "i=12810", {}),
                                        "EnableCount": ("V", "i=12794", {}),
                                        "EventNotificationsCount": ("V", "i=12804", {}),
                                        "EventQueueOverflowCount": ("V", "i=12815", {}),
                                        "LatePublishRequestCount": ("V", "i=12806", {}),
                                        "MaxKeepAliveCount": ("V", "i=12789", {}),
                                        "MaxLifetimeCount": ("V", "i=12790", {}),
                                        "MaxNotificationsPerPublish": (
                                            "V",
                                            "i=12791",
                                            {},
                                        ),
                                        "ModifyCount": ("V", "i=12793", {}),
                                        "MonitoredItemCount": ("V", "i=12811", {}),
                                        "MonitoringQueueOverflowCount": (
                                            "V",
                                            "i=12813",
                                            {},
                                        ),
                                        "NextSequenceNumber": ("V", "i=12814", {}),
                                        "NotificationsCount": ("V", "i=12805", {}),
                                        "Priority": ("V", "i=12787", {}),
                                        "PublishRequestCount": ("V", "i=12802", {}),
                                        "PublishingEnabled": ("V", "i=12792", {}),
                                        "PublishingInterval": ("V", "i=12788", {}),
                                        "RepublishMessageCount": ("V", "i=12798", {}),
                                        "RepublishMessageRequestCount": (
                                            "V",
                                            "i=12797",
                                            {},
                                        ),
                                        "RepublishRequestCount": ("V", "i=12796", {}),
                                        "SessionId": ("V", "i=12785", {}),
                                        "SubscriptionId": ("V", "i=12786", {}),
                                        "TransferRequestCount": ("V", "i=12799", {}),
                                        "TransferredToAltClientCount": (
                                            "V",
                                            "i=12800",
                                            {},
                                        ),
                                        "TransferredToSameClientCount": (
                                            "V",
                                            "i=12801",
                                            {},
                                        ),
                                        "UnacknowledgedMessageCount": (
                                            "V",
                                            "i=12809",
                                            {},
                                        ),
                                    },
                                )
                            },
                        ),
                        "SubscriptionDiagnosticsType": (
                            "VT",
                            "i=2172",
                            {
                                "CurrentKeepAliveCount": ("V", "i=8890", {}),
                                "CurrentLifetimeCount": ("V", "i=8891", {}),
                                "DataChangeNotificationsCount": ("V", "i=2191", {}),
                                "DisableCount": ("V", "i=2183", {}),
                                "DisabledMonitoredItemCount": ("V", "i=8895", {}),
                                "DiscardedMessageCount": ("V", "i=8893", {}),
                                "EnableCount": ("V", "i=2182", {}),
                                "EventNotificationsCount": ("V", "i=2998", {}),
                                "EventQueueOverflowCount": ("V", "i=8902", {}),
                                "LatePublishRequestCount": ("V", "i=8889", {}),
                                "MaxKeepAliveCount": ("V", "i=2177", {}),
                                "MaxLifetimeCount": ("V", "i=8888", {}),
                                "MaxNotificationsPerPublish": ("V", "i=2179", {}),
                                "ModifyCount": ("V", "i=2181", {}),
                                "MonitoredItemCount": ("V", "i=8894", {}),
                                "MonitoringQueueOverflowCount": ("V", "i=8896", {}),
                                "NextSequenceNumber": ("V", "i=8897", {}),
                                "NotificationsCount": ("V", "i=2193", {}),
                                "Priority": ("V", "i=2175", {}),
                                "PublishRequestCount": ("V", "i=2190", {}),
                                "PublishingEnabled": ("V", "i=2180", {}),
                                "PublishingInterval": ("V", "i=2176", {}),
                                "RepublishMessageCount": ("V", "i=2186", {}),
                                "RepublishMessageRequestCount": ("V", "i=2185", {}),
                                "RepublishRequestCount": ("V", "i=2184", {}),
                                "SessionId": ("V", "i=2173", {}),
                                "SubscriptionId": ("V", "i=2174", {}),
                                "TransferRequestCount": ("V", "i=2187", {}),
                                "TransferredToAltClientCount": ("V", "i=2188", {}),
                                "TransferredToSameClientCount": ("V", "i=2189", {}),
                                "UnacknowledgedMessageCount": ("V", "i=8892", {}),
                            },
                        ),
                        "TransitionVariableType": (
                            "VT",
                            "i=2762",
                            {
                                "EffectiveTransitionTime": ("V", "i=11456", {}),
                                "FiniteTransitionVariableType": (
                                    "VT",
                                    "i=2767",
                                    {"Id": ("V", "i=2768", {})},
                                ),
                                "Id": ("V", "i=2763", {}),
                                "Name": ("V", "i=2764", {}),
                                "Number": ("V", "i=2765", {}),
                                "TransitionTime": ("V", "i=2766", {}),
                            },
                        ),
                        "VectorType": (
                            "VT",
                            "i=17714",
                            {
                                "3DVectorType": (
                                    "VT",
                                    "i=17716",
                                    {
                                        "X": ("V", "i=18769", {}),
                                        "Y": ("V", "i=18770", {}),
                                        "Z": ("V", "i=18771", {}),
                                    },
                                ),
                                "VectorUnit": ("V", "i=17715", {}),
                            },
                        ),
                    },
                ),
                "PropertyType": ("VT", "i=68", {}),
            },
        )
    },
}
