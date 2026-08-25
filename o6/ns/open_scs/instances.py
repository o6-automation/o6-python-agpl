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

"""Generated OPC UA open_scs namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import datatypes as open_scs_datypes
from . import objtypes as open_scs_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=5002", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=5003", browseName="Default XML")
o6.hasEncoding(open_scs_datypes.OPENSCSAggregationDataType, o6.ns["ns=open_scs;i=5003"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=5004", browseName="Default JSON")
o6.hasEncoding(open_scs_datypes.OPENSCSAggregationDataType, o6.ns["ns=open_scs;i=5004"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=5005", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=5006", browseName="Default XML")
o6.hasEncoding(open_scs_datypes.OPENSCSLabelDataType, o6.ns["ns=open_scs;i=5006"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=5007", browseName="Default JSON")
o6.hasEncoding(open_scs_datypes.OPENSCSLabelDataType, o6.ns["ns=open_scs;i=5007"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=5008", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=5009", browseName="Default XML")
o6.hasEncoding(open_scs_datypes.OPENSCSEventStreamArgumentDataType, o6.ns["ns=open_scs;i=5009"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=5010", browseName="Default JSON")
o6.hasEncoding(open_scs_datypes.OPENSCSEventStreamArgumentDataType, o6.ns["ns=open_scs;i=5010"])
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=6008",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[12],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Undefined0"), description=o6.LocalizedText("Undefined value, should never be seen.")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("NoError1"), description=o6.LocalizedText("There were no errors in processing the method.  ")),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("InvalidSerialNumberCollection2"),
            description=o6.LocalizedText("The Serial Number Collection ID does not match a Serial Number Collection managed by the server."),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("InsufficientSerialNumbers3"),
            description=o6.LocalizedText("Fewer Serial Numbers are available from the pool, then are requested."),
        ),
        ns0.datatypes.EnumValueType(
            value=4, displayName=o6.LocalizedText("InvalidSerialNumbersFormat4"), description=o6.LocalizedText("The serial number format is not known or defined in the server")
        ),
        ns0.datatypes.EnumValueType(
            value=5, displayName=o6.LocalizedText("InvalidRequestToken5"), description=o6.LocalizedText("The Request Token has a value not understood by the server.")
        ),
        ns0.datatypes.EnumValueType(
            value=6, displayName=o6.LocalizedText("InvalidSelectionCriteria6"), description=o6.LocalizedText("The Selection Criteria is not known or defined in the server.")
        ),
        ns0.datatypes.EnumValueType(
            value=7, displayName=o6.LocalizedText("UnableToAcceptSerialNumberEvents7"), description=o6.LocalizedText("The server cannot accept Serial Number events.")
        ),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("UnableToAcceptLabelEvents8"), description=o6.LocalizedText("The server cannot accept Label events.")),
        ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("UnableToAcceptSIDEvents9"), description=o6.LocalizedText("The server cannot accept SID events.")),
        ns0.datatypes.EnumValueType(
            value=10, displayName=o6.LocalizedText("UnknownAggregationSID10"), description=o6.LocalizedText("The SID of the aggregation for packing or unpacking is unknown.")
        ),
        ns0.datatypes.EnumValueType(
            value=11,
            displayName=o6.LocalizedText("InsufficientPrivilegeToExecute11"),
            description=o6.LocalizedText(" The server has determined that the client does not have sufficient privilege for the method to execute."),
        ),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=open_scs;i=6014", browseName="ns=open_scs;OPENSCSAggregationDataType", dataType=o6.String, value="OPENSCSAggregationDataType")
o6.reference(o6.ns["ns=open_scs;i=5002"], "i=39", o6.ns["ns=open_scs;i=6014"])
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=6015",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=3006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Undefined_0"), description=o6.LocalizedText("Undefined value, should never be seen.")),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("Store_1"), description=o6.LocalizedText("Command to store the job order in local storage, but not to start the order.")
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("StoreAndStart_2"),
            description=o6.LocalizedText("Command to store the job order and start it as soon as the Job Order receiver is ready to start."),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("Start_3"),
            description=o6.LocalizedText(
                "Command to start a stored job order as soon as the receiver is ready to start. Only the Job Orders ID is used to identify the stored job order, all other information is not used.  No changes are made to the stored order. If multiple Job Orders have been commanded to Start, then the priority and timing values in the Job Orders shall be used to determine the order of execution of the orders."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("Update_4"),
            description=o6.LocalizedText(
                "Command to update a stored Job Order that has not yet been started, with the new order information.  All previously stored information is replaced."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=5,
            displayName=o6.LocalizedText("Stop_5"),
            description=o6.LocalizedText(
                "Command to stop a started job order, report on any work done on the order, and remove the stored information. Only the Job Orders ID is used to identify the job order, all other information is not used."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=6,
            displayName=o6.LocalizedText("Cancel_6"),
            description=o6.LocalizedText(
                "Cancel an un-started job order and remove the stored information. Only the Job Orders ID is used to identify the job order, all other information is not used."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=7,
            displayName=o6.LocalizedText("Clear_7"),
            description=o6.LocalizedText(
                "Command to allow the Information Receiver to clear any maintained information on the Job Order (usually sent after a receipt of a Job Response with a status of Finished.) Only the Job Orders ID is used to identify the job order, all other information is not used."
            ),
        ),
    ],
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=open_scs;i=6016", browseName="ns=open_scs;OPENSCSAggregationDataType", dataType=o6.String, value="//xs:element[@name='OPENSCSAggregationDataType']"
)
o6.reference(o6.ns["ns=open_scs;i=5003"], "i=39", o6.ns["ns=open_scs;i=6016"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=open_scs;i=6017", browseName="ns=open_scs;OPENSCSLabelDataType", dataType=o6.String, value="OPENSCSLabelDataType")
o6.reference(o6.ns["ns=open_scs;i=5005"], "i=39", o6.ns["ns=open_scs;i=6017"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=open_scs;i=6018", browseName="ns=open_scs;OPENSCSLabelDataType", dataType=o6.String, value="//xs:element[@name='OPENSCSLabelDataType']"
)
o6.reference(o6.ns["ns=open_scs;i=5006"], "i=39", o6.ns["ns=open_scs;i=6018"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=open_scs;i=6019", browseName="ns=open_scs;OPENSCSEventStreamArgumentDataType", dataType=o6.String, value="OPENSCSEventStreamArgumentDataType"
)
o6.reference(o6.ns["ns=open_scs;i=5008"], "i=39", o6.ns["ns=open_scs;i=6019"])
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=6020",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=3009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[10],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Undefined_0"), description=o6.LocalizedText("defined value, should never be seen.")),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("Waiting_1"), description=o6.LocalizedText("The necessary pre-conditions have not been met and the order is not ready to run.")
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("Ready_2"),
            description=o6.LocalizedText("The necessary pre-conditions have been met and the order is ready to run, awaiting a Start command."),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("Loaded_3"),
            description=o6.LocalizedText(
                "In situations where only one job may be in active memory and is able to be run, then the job is loaded in active memory, the  necessary pre-conditions have been met, and the order is ready to run, awaiting a Start command."
            ),
        ),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Running_4"), description=o6.LocalizedText("The order is executing.")),
        ns0.datatypes.EnumValueType(
            value=5, displayName=o6.LocalizedText("Completed_5"), description=o6.LocalizedText("The order has been completed and are no longer in execution.")
        ),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("Aborted_6"), description=o6.LocalizedText("The order was aborted.")),
        ns0.datatypes.EnumValueType(
            value=7, displayName=o6.LocalizedText("Held_7"), description=o6.LocalizedText("The order has been temporarily stopped due to a constraint of some form.")
        ),
        ns0.datatypes.EnumValueType(
            value=8,
            displayName=o6.LocalizedText("Suspended_8"),
            description=o6.LocalizedText("The order has been temporarily stopped due to a deliberate decision within the execution system."),
        ),
        ns0.datatypes.EnumValueType(
            value=9,
            displayName=o6.LocalizedText("Closed_9"),
            description=o6.LocalizedText("The order has been completed and fully reconciled. No further changes, or restatement of actuals is expected."),
        ),
    ],
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=open_scs;i=6021", browseName="ns=open_scs;OPENSCSEventStreamArgumentDataType", dataType=o6.String, value="//xs:element[@name='OPENSCSEventStreamArgumentDataType']"
)
o6.reference(o6.ns["ns=open_scs;i=5009"], "i=39", o6.ns["ns=open_scs;i=6021"])
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=6022",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15143",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[12],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("Unassigned0"), description=o6.LocalizedText("The Serial Number has not been assigned to production or a packaging run.")
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("Unallocated1"),
            description=o6.LocalizedText(
                "As Serial Number has been assigned to production or a packaging run, but it has not yet been allocated for use a specific production run of a product or aggregation."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("Allocated2"),
            description=o6.LocalizedText("The Serial Number has been assigned to a specific product or aggregation production run. "),
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("SNInvalid3"),
            description=o6.LocalizedText("The Serial Number is no longer viable, and the related serial number is no longer defined. "),
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("Encoded4"),
            description=o6.LocalizedText("The Serial Number has been written to a barcode or RFID tag, but not yet commissioned."),
        ),
        ns0.datatypes.EnumValueType(
            value=5,
            displayName=o6.LocalizedText("LabelSampled5"),
            description=o6.LocalizedText("The printed label has been retained and is not associated with a physical product or aggregation."),
        ),
        ns0.datatypes.EnumValueType(
            value=6,
            displayName=o6.LocalizedText("LabelScrapped6"),
            description=o6.LocalizedText("A label was encoded with a Serial Number, but was made unusable before being applied to a product or aggregation."),
        ),
        ns0.datatypes.EnumValueType(
            value=7,
            displayName=o6.LocalizedText("Commissioned7"),
            description=o6.LocalizedText("The Serial Number has been associated with a physical product or aggregation, but has not yet left the responsibility of production"),
        ),
        ns0.datatypes.EnumValueType(
            value=8,
            displayName=o6.LocalizedText("Sampled8"),
            description=o6.LocalizedText("The product or aggregation is to be used as a sample for testing or other use, not to be made active."),
        ),
        ns0.datatypes.EnumValueType(
            value=9, displayName=o6.LocalizedText("Inactive9"), description=o6.LocalizedText("The product or aggregation is no longer active, but may not have been destroyed.")
        ),
        ns0.datatypes.EnumValueType(
            value=10, displayName=o6.LocalizedText("Destroyed10"), description=o6.LocalizedText("The product or aggregation was has been fully rendered non-usable.")
        ),
        ns0.datatypes.EnumValueType(
            value=11,
            displayName=o6.LocalizedText("Released11"),
            description=o6.LocalizedText("The Serial Number has been associated with a physical product or aggregation, and has left the responsibility of production."),
        ),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=6002",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=6003",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=open_scs;i=7001", browseName="CloseAndCommit", inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=6002"]), outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=6003"]))

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=6004",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=ns0.datatypes.BaseDataType, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=6005",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=open_scs;i=7002", browseName="GenerateFileForRead", inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=6004"]), outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=6005"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=6006",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=ns0.datatypes.BaseDataType, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=6007",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=open_scs;i=7003", browseName="GenerateFileForWrite", inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=6006"]), outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=6007"])
)

ns0.objtypes.TemporaryFileTransferType(
    nodeId="ns=open_scs;i=5001",
    browseName="ns=open_scs;EPCISStream",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=6001", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=open_scs;i=7001"]),
        o6.hasComponent(o6.ns["ns=open_scs;i=7002"]),
        o6.hasComponent(o6.ns["ns=open_scs;i=7003"]),
    ],
)
o6.reference(open_scs_objtypes.OPENSCSEventManagerObjectType, ns0.reftypes.HasComponent, o6.ns["ns=open_scs;i=5001"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashOPENSCSMinusSERSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=open_scs;i=15011",
    browseName="ns=open_scs;http://opcfoundation.org/UA/OPENSCS-SER/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15012", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/OPENSCS-SER/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15013", browseName="NamespaceVersion", dataType=o6.String, value="1.00")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15014", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2019-02-04T00:00:00Z"))
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15015", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=open_scs;i=15016", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=open_scs;i=15017", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["1:65535"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15018", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=open_scs;i=15119", browseName="DefaultRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=open_scs;i=15120", browseName="DefaultUserRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15121", browseName="DefaultAccessRestrictions", dataType=ns0.datatypes.AccessRestrictionType)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=15188", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=15189", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=15190", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=15191", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=15192", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=15193", browseName="Default Binary")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=open_scs;i=15198", browseName="ns=open_scs;OPENSCSCollectionDataType", dataType=o6.String, value="OPENSCSCollectionDataType")
o6.reference(o6.ns["ns=open_scs;i=15188"], "i=39", o6.ns["ns=open_scs;i=15198"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=open_scs;i=15201", browseName="ns=open_scs;OPENSCSLabelCollectionDataType", dataType=o6.String, value="OPENSCSLabelCollectionDataType"
)
o6.reference(o6.ns["ns=open_scs;i=15189"], "i=39", o6.ns["ns=open_scs;i=15201"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=open_scs;i=15204", browseName="ns=open_scs;OPENSCSLabelPropertyDataType", dataType=o6.String, value="OPENSCSLabelPropertyDataType")
o6.reference(o6.ns["ns=open_scs;i=15190"], "i=39", o6.ns["ns=open_scs;i=15204"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=open_scs;i=15207", browseName="ns=open_scs;OPENSCSSNCollectionDataType", dataType=o6.String, value="OPENSCSSNCollectionDataType")
o6.reference(o6.ns["ns=open_scs;i=15191"], "i=39", o6.ns["ns=open_scs;i=15207"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=open_scs;i=15210", browseName="ns=open_scs;OPENSCSSIDClassPropertyDataType", dataType=o6.String, value="OPENSCSSIDClassPropertyDataType"
)
o6.reference(o6.ns["ns=open_scs;i=15192"], "i=39", o6.ns["ns=open_scs;i=15210"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=open_scs;i=15213", browseName="ns=open_scs;OPENSCSKeyValueDataType", dataType=o6.String, value="OPENSCSKeyValueDataType")
o6.reference(o6.ns["ns=open_scs;i=15193"], "i=39", o6.ns["ns=open_scs;i=15213"])
openSCS = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=open_scs;i=15194",
    browseName="ns=open_scs;OpenSCS",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/OPENSCS-SER/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15196", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/OPENSCS-SER/")),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15197", browseName="Deprecated", dataType=o6.Boolean)
        ),
        o6.hasComponent(o6.ns["ns=open_scs;i=6014"]),
        o6.hasComponent(o6.ns["ns=open_scs;i=6017"]),
        o6.hasComponent(o6.ns["ns=open_scs;i=6019"]),
        o6.hasComponent(o6.ns["ns=open_scs;i=15198"]),
        o6.hasComponent(o6.ns["ns=open_scs;i=15201"]),
        o6.hasComponent(o6.ns["ns=open_scs;i=15204"]),
        o6.hasComponent(o6.ns["ns=open_scs;i=15207"]),
        o6.hasComponent(o6.ns["ns=open_scs;i=15210"]),
        o6.hasComponent(o6.ns["ns=open_scs;i=15213"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/OPENSCS-SER/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/OPENSCS-SER/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="OPENSCSAggregationDataType">\n  <opc:Documentation>Iidentifies a parent element and a collection of packed elements. This is used in the aggregation packing and unpacking methods.</opc:Documentation>\n  <opc:Field TypeName="tns:OPENSCSLabelDataType" Name="ParentElement"/>\n  <opc:Field TypeName="tns:OPENSCSLabelCollectionDataType" Name="ParentElementCollection"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="OPENSCSCollectionDataType">\n  <opc:Field TypeName="opc:CharArray" Name="ID"/>\n  <opc:Field TypeName="opc:CharArray" Name="Description"/>\n  <opc:Field TypeName="tns:OPENSCSSerialNumberStateEnum" Name="State"/>\n  <opc:Field TypeName="opc:CharArray" Name="AssociatedPoolID"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfSerialNumbers"/>\n  <opc:Field LengthField="NoOfSerialNumbers" TypeName="opc:CharArray" Name="SerialNumbers"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:OPENSCSCollectionDataType" Name="OPENSCSLabelCollectionDataType">\n  <opc:Field TypeName="opc:Bit" Name="LabelCollectionPropertiesSpecified"/>\n  <opc:Field Length="31" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field SourceType="tns:OPENSCSCollectionDataType" TypeName="opc:CharArray" Name="ID"/>\n  <opc:Field SourceType="tns:OPENSCSCollectionDataType" TypeName="opc:CharArray" Name="Description"/>\n  <opc:Field SourceType="tns:OPENSCSCollectionDataType" TypeName="tns:OPENSCSSerialNumberStateEnum" Name="State"/>\n  <opc:Field SourceType="tns:OPENSCSCollectionDataType" TypeName="opc:CharArray" Name="AssociatedPoolID"/>\n  <opc:Field SourceType="tns:OPENSCSCollectionDataType" TypeName="opc:Int32" Name="NoOfSerialNumbers"/>\n  <opc:Field LengthField="NoOfSerialNumbers" SourceType="tns:OPENSCSCollectionDataType" TypeName="opc:CharArray" Name="SerialNumbers"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfLabelCollection"/>\n  <opc:Field LengthField="NoOfLabelCollection" TypeName="tns:OPENSCSLabelDataType" Name="LabelCollection"/>\n  <opc:Field SwitchField="LabelCollectionPropertiesSpecified" TypeName="opc:Int32" Name="NoOfLabelCollectionProperties"/>\n  <opc:Field LengthField="NoOfLabelCollectionProperties" SwitchField="LabelCollectionPropertiesSpecified" TypeName="tns:OPENSCSKeyValueDataType" Name="LabelCollectionProperties"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="OPENSCSEventStreamArgumentDataType">\n  <opc:Documentation>Defines the generateOptions argument for an EPCISStream GenerateFileForWrite method. It defines the serial number format information for object events and for aggregation events, and event context information. </opc:Documentation>\n  <opc:Field TypeName="opc:CharArray" Name="SNFormat"/>\n  <opc:Field TypeName="opc:CharArray" Name="ParentSNFormat"/>\n  <opc:Field TypeName="opc:CharArray" Name="PackedElementSNFormat"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfEventContext"/>\n  <opc:Field LengthField="NoOfEventContext" TypeName="tns:OPENSCSKeyValueDataType" Name="EventContext"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="OPENSCSKeyValueDataType">\n  <opc:Field TypeName="opc:CharArray" Name="Key"/>\n  <opc:Field TypeName="opc:CharArray" Name="Value"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="OPENSCSLabelDataType">\n  <opc:Documentation>Defines a single serial number and label, which may be associated with an SID, and collection of properties in the form of OPENSCSKeyValueDataType. </opc:Documentation>\n  <opc:Field TypeName="opc:CharArray" Name="ID"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfLabelProperties"/>\n  <opc:Field LengthField="NoOfLabelProperties" TypeName="tns:OPENSCSKeyValueDataType" Name="LabelProperties"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="OPENSCSLabelPropertyDataType">\n  <opc:Field TypeName="opc:CharArray" Name="PropertyID"/>\n  <opc:Field TypeName="opc:CharArray" Name="PropertyDescription"/>\n  <opc:Field TypeName="opc:CharArray" Name="PropertyValue"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="OPENSCSSIDClassPropertyDataType">\n  <opc:Field TypeName="opc:CharArray" Name="PropertyID"/>\n  <opc:Field TypeName="opc:CharArray" Name="PropertyDescription"/>\n  <opc:Field TypeName="opc:CharArray" Name="PropertyValue"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfLabelProperty"/>\n  <opc:Field LengthField="NoOfLabelProperty" TypeName="tns:OPENSCSLabelPropertyDataType" Name="LabelProperty"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="JobOrderCommandEnum">\n  <opc:Documentation>Describes the possible job order commands.  </opc:Documentation>\n  <opc:EnumeratedValue Name="Undefined_0" Value="0"/>\n  <opc:EnumeratedValue Name="Store_1" Value="1"/>\n  <opc:EnumeratedValue Name="StoreAndStart_2" Value="2"/>\n  <opc:EnumeratedValue Name="Start_3" Value="3"/>\n  <opc:EnumeratedValue Name="Update_4" Value="4"/>\n  <opc:EnumeratedValue Name="Stop_5" Value="5"/>\n  <opc:EnumeratedValue Name="Cancel_6" Value="6"/>\n  <opc:EnumeratedValue Name="Clear_7" Value="7"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="JobOrderStateEnum">\n  <opc:Documentation>Describes the possible serial number statesjob order states.  </opc:Documentation>\n  <opc:EnumeratedValue Name="Undefined_0" Value="0"/>\n  <opc:EnumeratedValue Name="Waiting_1" Value="1"/>\n  <opc:EnumeratedValue Name="Ready_2" Value="2"/>\n  <opc:EnumeratedValue Name="Loaded_3" Value="3"/>\n  <opc:EnumeratedValue Name="Running_4" Value="4"/>\n  <opc:EnumeratedValue Name="Completed_5" Value="5"/>\n  <opc:EnumeratedValue Name="Aborted_6" Value="6"/>\n  <opc:EnumeratedValue Name="Held_7" Value="7"/>\n  <opc:EnumeratedValue Name="Suspended_8" Value="8"/>\n  <opc:EnumeratedValue Name="Closed_9" Value="9"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="OPENSCSReturnEnum">\n  <opc:EnumeratedValue Name="Undefined0" Value="0"/>\n  <opc:EnumeratedValue Name="NoError1" Value="1"/>\n  <opc:EnumeratedValue Name="InvalidSerialNumberCollection2" Value="2"/>\n  <opc:EnumeratedValue Name="InsufficientSerialNumbers3" Value="3"/>\n  <opc:EnumeratedValue Name="InvalidSerialNumbersFormat4" Value="4"/>\n  <opc:EnumeratedValue Name="InvalidRequestToken5" Value="5"/>\n  <opc:EnumeratedValue Name="InvalidSelectionCriteria6" Value="6"/>\n  <opc:EnumeratedValue Name="UnableToAcceptSerialNumberEvents7" Value="7"/>\n  <opc:EnumeratedValue Name="UnableToAcceptLabelEvents8" Value="8"/>\n  <opc:EnumeratedValue Name="UnableToAcceptSIDEvents9" Value="9"/>\n  <opc:EnumeratedValue Name="UnknownAggregationSID10" Value="10"/>\n  <opc:EnumeratedValue Name="InsufficientPrivilegeToExecute11" Value="11"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="OPENSCSSerialNumberStateEnum">\n  <opc:EnumeratedValue Name="Unassigned0" Value="0"/>\n  <opc:EnumeratedValue Name="Unallocated1" Value="1"/>\n  <opc:EnumeratedValue Name="Allocated2" Value="2"/>\n  <opc:EnumeratedValue Name="SNInvalid3" Value="3"/>\n  <opc:EnumeratedValue Name="Encoded4" Value="4"/>\n  <opc:EnumeratedValue Name="LabelSampled5" Value="5"/>\n  <opc:EnumeratedValue Name="LabelScrapped6" Value="6"/>\n  <opc:EnumeratedValue Name="Commissioned7" Value="7"/>\n  <opc:EnumeratedValue Name="Sampled8" Value="8"/>\n  <opc:EnumeratedValue Name="Inactive9" Value="9"/>\n  <opc:EnumeratedValue Name="Destroyed10" Value="10"/>\n  <opc:EnumeratedValue Name="Released11" Value="11"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=15216", browseName="Default XML")
o6.hasEncoding(open_scs_datypes.OPENSCSCollectionDataType, o6.ns["ns=open_scs;i=15216"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=15217", browseName="Default XML")
o6.hasEncoding(open_scs_datypes.OPENSCSLabelCollectionDataType, o6.ns["ns=open_scs;i=15217"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=15218", browseName="Default XML")
o6.hasEncoding(open_scs_datypes.OPENSCSLabelPropertyDataType, o6.ns["ns=open_scs;i=15218"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=15219", browseName="Default XML")
o6.hasEncoding(open_scs_datypes.OPENSCSSNCollectionDataType, o6.ns["ns=open_scs;i=15219"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=15220", browseName="Default XML")
o6.hasEncoding(open_scs_datypes.OPENSCSSIDClassPropertyDataType, o6.ns["ns=open_scs;i=15220"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=15221", browseName="Default XML")
o6.hasEncoding(open_scs_datypes.OPENSCSKeyValueDataType, o6.ns["ns=open_scs;i=15221"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=open_scs;i=15226", browseName="ns=open_scs;OPENSCSCollectionDataType", dataType=o6.String, value="//xs:element[@name='OPENSCSCollectionDataType']"
)
o6.reference(o6.ns["ns=open_scs;i=15216"], "i=39", o6.ns["ns=open_scs;i=15226"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=open_scs;i=15229", browseName="ns=open_scs;OPENSCSLabelCollectionDataType", dataType=o6.String, value="//xs:element[@name='OPENSCSLabelCollectionDataType']"
)
o6.reference(o6.ns["ns=open_scs;i=15217"], "i=39", o6.ns["ns=open_scs;i=15229"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=open_scs;i=15232", browseName="ns=open_scs;OPENSCSLabelPropertyDataType", dataType=o6.String, value="//xs:element[@name='OPENSCSLabelPropertyDataType']"
)
o6.reference(o6.ns["ns=open_scs;i=15218"], "i=39", o6.ns["ns=open_scs;i=15232"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=open_scs;i=15235", browseName="ns=open_scs;OPENSCSSNCollectionDataType", dataType=o6.String, value="//xs:element[@name='OPENSCSSNCollectionDataType']"
)
o6.reference(o6.ns["ns=open_scs;i=15219"], "i=39", o6.ns["ns=open_scs;i=15235"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=open_scs;i=15238", browseName="ns=open_scs;OPENSCSSIDClassPropertyDataType", dataType=o6.String, value="//xs:element[@name='OPENSCSSIDClassPropertyDataType']"
)
o6.reference(o6.ns["ns=open_scs;i=15220"], "i=39", o6.ns["ns=open_scs;i=15238"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=open_scs;i=15241", browseName="ns=open_scs;OPENSCSKeyValueDataType", dataType=o6.String, value="//xs:element[@name='OPENSCSKeyValueDataType']"
)
o6.reference(o6.ns["ns=open_scs;i=15221"], "i=39", o6.ns["ns=open_scs;i=15241"])
openSCS_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=open_scs;i=15222",
    browseName="ns=open_scs;OpenSCS",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/OPENSCS-SER/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15224", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/OPENSCS-SER/Types.xsd")
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15225", browseName="Deprecated", dataType=o6.Boolean)
        ),
        o6.hasComponent(o6.ns["ns=open_scs;i=6016"]),
        o6.hasComponent(o6.ns["ns=open_scs;i=6018"]),
        o6.hasComponent(o6.ns["ns=open_scs;i=6021"]),
        o6.hasComponent(o6.ns["ns=open_scs;i=15226"]),
        o6.hasComponent(o6.ns["ns=open_scs;i=15229"]),
        o6.hasComponent(o6.ns["ns=open_scs;i=15232"]),
        o6.hasComponent(o6.ns["ns=open_scs;i=15235"]),
        o6.hasComponent(o6.ns["ns=open_scs;i=15238"]),
        o6.hasComponent(o6.ns["ns=open_scs;i=15241"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/OPENSCS-SER/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/OPENSCS-SER/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="JobOrderCommandEnum">\n  <xs:annotation>\n   <xs:documentation>Describes the possible job order commands.  </xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Undefined_0_0"/>\n   <xs:enumeration value="Store_1_1"/>\n   <xs:enumeration value="StoreAndStart_2_2"/>\n   <xs:enumeration value="Start_3_3"/>\n   <xs:enumeration value="Update_4_4"/>\n   <xs:enumeration value="Stop_5_5"/>\n   <xs:enumeration value="Cancel_6_6"/>\n   <xs:enumeration value="Clear_7_7"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:JobOrderCommandEnum" name="JobOrderCommandEnum"/>\n <xs:complexType name="ListOfJobOrderCommandEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:JobOrderCommandEnum" name="JobOrderCommandEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfJobOrderCommandEnum" name="ListOfJobOrderCommandEnum" nillable="true"/>\n <xs:simpleType name="JobOrderStateEnum">\n  <xs:annotation>\n   <xs:documentation>Describes the possible serial number statesjob order states.  </xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Undefined_0_0"/>\n   <xs:enumeration value="Waiting_1_1"/>\n   <xs:enumeration value="Ready_2_2"/>\n   <xs:enumeration value="Loaded_3_3"/>\n   <xs:enumeration value="Running_4_4"/>\n   <xs:enumeration value="Completed_5_5"/>\n   <xs:enumeration value="Aborted_6_6"/>\n   <xs:enumeration value="Held_7_7"/>\n   <xs:enumeration value="Suspended_8_8"/>\n   <xs:enumeration value="Closed_9_9"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:JobOrderStateEnum" name="JobOrderStateEnum"/>\n <xs:complexType name="ListOfJobOrderStateEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:JobOrderStateEnum" name="JobOrderStateEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfJobOrderStateEnum" name="ListOfJobOrderStateEnum" nillable="true"/>\n <xs:simpleType name="OPENSCSReturnEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Undefined0_0"/>\n   <xs:enumeration value="NoError1_1"/>\n   <xs:enumeration value="InvalidSerialNumberCollection2_2"/>\n   <xs:enumeration value="InsufficientSerialNumbers3_3"/>\n   <xs:enumeration value="InvalidSerialNumbersFormat4_4"/>\n   <xs:enumeration value="InvalidRequestToken5_5"/>\n   <xs:enumeration value="InvalidSelectionCriteria6_6"/>\n   <xs:enumeration value="UnableToAcceptSerialNumberEvents7_7"/>\n   <xs:enumeration value="UnableToAcceptLabelEvents8_8"/>\n   <xs:enumeration value="UnableToAcceptSIDEvents9_9"/>\n   <xs:enumeration value="UnknownAggregationSID10_10"/>\n   <xs:enumeration value="InsufficientPrivilegeToExecute11_11"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:OPENSCSReturnEnum" name="OPENSCSReturnEnum"/>\n <xs:complexType name="ListOfOPENSCSReturnEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OPENSCSReturnEnum" name="OPENSCSReturnEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOPENSCSReturnEnum" name="ListOfOPENSCSReturnEnum" nillable="true"/>\n <xs:simpleType name="OPENSCSSerialNumberStateEnum">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Unassigned0_0"/>\n   <xs:enumeration value="Unallocated1_1"/>\n   <xs:enumeration value="Allocated2_2"/>\n   <xs:enumeration value="SNInvalid3_3"/>\n   <xs:enumeration value="Encoded4_4"/>\n   <xs:enumeration value="LabelSampled5_5"/>\n   <xs:enumeration value="LabelScrapped6_6"/>\n   <xs:enumeration value="Commissioned7_7"/>\n   <xs:enumeration value="Sampled8_8"/>\n   <xs:enumeration value="Inactive9_9"/>\n   <xs:enumeration value="Destroyed10_10"/>\n   <xs:enumeration value="Released11_11"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:OPENSCSSerialNumberStateEnum" name="OPENSCSSerialNumberStateEnum"/>\n <xs:complexType name="ListOfOPENSCSSerialNumberStateEnum">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OPENSCSSerialNumberStateEnum" name="OPENSCSSerialNumberStateEnum" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOPENSCSSerialNumberStateEnum" name="ListOfOPENSCSSerialNumberStateEnum" nillable="true"/>\n <xs:complexType name="OPENSCSAggregationDataType">\n  <xs:annotation>\n   <xs:documentation>Iidentifies a parent element and a collection of packed elements. This is used in the aggregation packing and unpacking methods.</xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:OPENSCSLabelDataType" name="ParentElement"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:OPENSCSLabelCollectionDataType" name="ParentElementCollection"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:OPENSCSAggregationDataType" name="OPENSCSAggregationDataType"/>\n <xs:complexType name="ListOfOPENSCSAggregationDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OPENSCSAggregationDataType" name="OPENSCSAggregationDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOPENSCSAggregationDataType" name="ListOfOPENSCSAggregationDataType" nillable="true"/>\n <xs:complexType name="OPENSCSCollectionDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:OPENSCSSerialNumberStateEnum" name="State"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="AssociatedPoolID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="SerialNumbers"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:OPENSCSCollectionDataType" name="OPENSCSCollectionDataType"/>\n <xs:complexType name="ListOfOPENSCSCollectionDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OPENSCSCollectionDataType" name="OPENSCSCollectionDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOPENSCSCollectionDataType" name="ListOfOPENSCSCollectionDataType" nillable="true"/>\n <xs:complexType name="OPENSCSLabelCollectionDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Description"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:OPENSCSSerialNumberStateEnum" name="State"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="AssociatedPoolID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="SerialNumbers"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfOPENSCSLabelDataType" name="LabelCollection"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfOPENSCSKeyValueDataType" name="LabelCollectionProperties"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:OPENSCSLabelCollectionDataType" name="OPENSCSLabelCollectionDataType"/>\n <xs:complexType name="ListOfOPENSCSLabelCollectionDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OPENSCSLabelCollectionDataType" name="OPENSCSLabelCollectionDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOPENSCSLabelCollectionDataType" name="ListOfOPENSCSLabelCollectionDataType" nillable="true"/>\n <xs:complexType name="OPENSCSEventStreamArgumentDataType">\n  <xs:annotation>\n   <xs:documentation>Defines the generateOptions argument for an EPCISStream GenerateFileForWrite method. It defines the serial number format information for object events and for aggregation events, and event context information. </xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="SNFormat"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ParentSNFormat"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="PackedElementSNFormat"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfOPENSCSKeyValueDataType" name="EventContext"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:OPENSCSEventStreamArgumentDataType" name="OPENSCSEventStreamArgumentDataType"/>\n <xs:complexType name="ListOfOPENSCSEventStreamArgumentDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OPENSCSEventStreamArgumentDataType" name="OPENSCSEventStreamArgumentDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOPENSCSEventStreamArgumentDataType" name="ListOfOPENSCSEventStreamArgumentDataType" nillable="true"/>\n <xs:complexType name="OPENSCSKeyValueDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Key"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Value"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:OPENSCSKeyValueDataType" name="OPENSCSKeyValueDataType"/>\n <xs:complexType name="ListOfOPENSCSKeyValueDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OPENSCSKeyValueDataType" name="OPENSCSKeyValueDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOPENSCSKeyValueDataType" name="ListOfOPENSCSKeyValueDataType" nillable="true"/>\n <xs:complexType name="OPENSCSLabelDataType">\n  <xs:annotation>\n   <xs:documentation>Defines a single serial number and label, which may be associated with an SID, and collection of properties in the form of OPENSCSKeyValueDataType. </xs:documentation>\n  </xs:annotation>\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfOPENSCSKeyValueDataType" name="LabelProperties"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:OPENSCSLabelDataType" name="OPENSCSLabelDataType"/>\n <xs:complexType name="ListOfOPENSCSLabelDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OPENSCSLabelDataType" name="OPENSCSLabelDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOPENSCSLabelDataType" name="ListOfOPENSCSLabelDataType" nillable="true"/>\n <xs:complexType name="OPENSCSLabelPropertyDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="PropertyID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="PropertyDescription"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="PropertyValue"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:OPENSCSLabelPropertyDataType" name="OPENSCSLabelPropertyDataType"/>\n <xs:complexType name="ListOfOPENSCSLabelPropertyDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OPENSCSLabelPropertyDataType" name="OPENSCSLabelPropertyDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOPENSCSLabelPropertyDataType" name="ListOfOPENSCSLabelPropertyDataType" nillable="true"/>\n <xs:complexType name="OPENSCSSIDClassPropertyDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="PropertyID"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="PropertyDescription"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="PropertyValue"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfOPENSCSLabelPropertyDataType" name="LabelProperty"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:OPENSCSSIDClassPropertyDataType" name="OPENSCSSIDClassPropertyDataType"/>\n <xs:complexType name="ListOfOPENSCSSIDClassPropertyDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OPENSCSSIDClassPropertyDataType" name="OPENSCSSIDClassPropertyDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOPENSCSSIDClassPropertyDataType" name="ListOfOPENSCSSIDClassPropertyDataType" nillable="true"/>\n</xs:schema>\n',
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=15244", browseName="Default JSON")
o6.hasEncoding(open_scs_datypes.OPENSCSCollectionDataType, o6.ns["ns=open_scs;i=15244"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=15245", browseName="Default JSON")
o6.hasEncoding(open_scs_datypes.OPENSCSLabelCollectionDataType, o6.ns["ns=open_scs;i=15245"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=15246", browseName="Default JSON")
o6.hasEncoding(open_scs_datypes.OPENSCSLabelPropertyDataType, o6.ns["ns=open_scs;i=15246"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=15247", browseName="Default JSON")
o6.hasEncoding(open_scs_datypes.OPENSCSSNCollectionDataType, o6.ns["ns=open_scs;i=15247"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=15248", browseName="Default JSON")
o6.hasEncoding(open_scs_datypes.OPENSCSSIDClassPropertyDataType, o6.ns["ns=open_scs;i=15248"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=open_scs;i=15249", browseName="Default JSON")
o6.hasEncoding(open_scs_datypes.OPENSCSKeyValueDataType, o6.ns["ns=open_scs;i=15249"])


del Any, TYPE_CHECKING, uuid, o6, ns0, open_scs_datypes, open_scs_objtypes
