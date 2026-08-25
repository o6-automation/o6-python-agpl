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

"""Generated OPC UA wire_harness namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.machinery_result as machinery_result
import o6.ns.ns0 as ns0
import o6.ns.wire_harness_vec as wire_harness_vec
from . import datatypes as wire_harness_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=wire_harness;i=1000", browseName="ns=wire_harness;WireHarnessMachineType", displayName="WireHarnessMachineType")
class WireHarnessMachineType(ns0.objtypes.BaseObjectType):
    articleSpecManagement: ArticleSpecManagementType | None
    components: machinery.objtypes.MachineComponentsType | None = o6.hasAddIn(
        machinery.objtypes.MachineComponentsType(nodeId="ns=wire_harness;i=5036", browseName="ns=machinery;Components")
    )
    identification: WireHarnessMachineIdentificationType
    machineryBuildingBlocks: ns0.objtypes.FolderType
    partManagement: PartManagementType | None


@o6.objecttype(nodeId="ns=wire_harness;i=1003", browseName="ns=wire_harness;WireHarnessMachineIdentificationType", displayName="WireHarnessMachineIdentificationType")
class WireHarnessMachineIdentificationType(machinery.objtypes.MachineIdentificationType):
    assetId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=wire_harness;i=6008",
            browseName="ns=di;AssetId",
            description="To be used by end users to store a unique identification in the context of their overall application. Servers shall support at least 40 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 40 Unicode characters into that field.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=wire_harness;i=1008", browseName="ns=wire_harness;RunCompleteEventType", displayName="RunCompleteEventType", isAbstract=True)
class RunCompleteEventType(ns0.objtypes.BaseEventType):
    endTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=wire_harness;i=6056", browseName="ns=wire_harness;EndTime", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)
    )
    goodQuantity: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=wire_harness;i=6061", browseName="ns=wire_harness;GoodQuantity", dataType=o6.Double, accessLevel=3, userAccessLevel=1)
    )
    jobOrderID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=wire_harness;i=6036", browseName="ns=wire_harness;JobOrderID", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    producedQuantity: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=wire_harness;i=6059", browseName="ns=wire_harness;ProducedQuantity", dataType=o6.Double, accessLevel=3, userAccessLevel=1)
    )
    productIDs: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=wire_harness;i=6062", browseName="ns=wire_harness;ProductIDs", dataType=o6.String, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
        )
    )
    run: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=wire_harness;i=6052", browseName="ns=wire_harness;Run", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )
    startTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=wire_harness;i=6053", browseName="ns=wire_harness;StartTime", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=wire_harness;i=1005", browseName="ns=wire_harness;ProductFinishedEventType", displayName="ProductFinishedEventType", isAbstract=True)
class ProductFinishedEventType(ns0.objtypes.BaseEventType):
    endTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=wire_harness;i=6078", browseName="ns=wire_harness;EndTime", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)
    )
    jobOrderID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=wire_harness;i=6066", browseName="ns=wire_harness;JobOrderID", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    materialDefinitionID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=wire_harness;i=6067", browseName="ns=wire_harness;MaterialDefinitionID", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    productID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=wire_harness;i=6076", browseName="ns=wire_harness;ProductID", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    resultIDs: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=wire_harness;i=6079",
            browseName="ns=wire_harness;ResultIDs",
            dataType=ns0.datatypes.TrimmedString,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    run: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=wire_harness;i=6075", browseName="ns=wire_harness;Run", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )
    startTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=wire_harness;i=6077", browseName="ns=wire_harness;StartTime", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)
    )
    state: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=wire_harness;i=6080", browseName="ns=wire_harness;State", dataType=machinery_jobs.datatypes.JobResult, accessLevel=3, userAccessLevel=1
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6018",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderID",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "Contains information defining the job order with all parameters and any material, equipment, or physical asset requirements associated with the order."
            ),
        ),
        ns0.datatypes.Argument(
            name="Comment",
            dataType=o6.LocalizedText,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "The comment provides a description of why the method was called. In order to provide the comment in several languages, it is an array of LocalizedText. The array may be empty, when no comment is provided."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6020",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution."))],
)
o6.call(
    nodeId="ns=wire_harness;i=7002",
    browseName="ns=isa95_jobcontrol_v2;Cancel",
    inputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6018"]),
    outputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6020"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6021",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderID",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "Contains information defining the job order with all parameters and any material, equipment, or physical asset requirements associated with the order."
            ),
        ),
        ns0.datatypes.Argument(
            name="Comment",
            dataType=o6.LocalizedText,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "The comment provides a description of why the method was called. In order to provide the comment in several languages, it is an array of LocalizedText. The array may be empty, when no comment is provided."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6024",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution."))],
)
o6.call(
    nodeId="ns=wire_harness;i=7003",
    browseName="ns=isa95_jobcontrol_v2;Abort",
    inputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6021"]),
    outputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6024"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6025",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderID",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "Contains information defining the job order with all parameters and any material, equipment, or physical asset requirements associated with the order."
            ),
        ),
        ns0.datatypes.Argument(
            name="Comment",
            dataType=o6.LocalizedText,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "The comment provides a description of why the method was called. In order to provide the comment in several languages, it is an array of LocalizedText. The array may be empty, when no comment is provided."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6100",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution."))],
)
o6.call(
    nodeId="ns=wire_harness;i=7004",
    browseName="ns=isa95_jobcontrol_v2;Start",
    inputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6025"]),
    outputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6100"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6101",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderID",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "Contains information defining the job order with all parameters and any material, equipment, or physical asset requirements associated with the order."
            ),
        ),
        ns0.datatypes.Argument(
            name="Comment",
            dataType=o6.LocalizedText,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "The comment provides a description of why the method was called. In order to provide the comment in several languages, it is an array of LocalizedText. The array may be empty, when no comment is provided."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6102",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution."))],
)
o6.call(
    nodeId="ns=wire_harness;i=7005",
    browseName="ns=isa95_jobcontrol_v2;Clear",
    inputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6101"]),
    outputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6102"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6103",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderID",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "Contains information defining the job order with all parameters and any material, equipment, or physical asset requirements associated with the order."
            ),
        ),
        ns0.datatypes.Argument(
            name="Comment",
            dataType=o6.LocalizedText,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "The comment provides a description of why the method was called. In order to provide the comment in several languages, it is an array of LocalizedText. The array may be empty, when no comment is provided."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6104",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution."))],
)
o6.call(
    nodeId="ns=wire_harness;i=7006",
    browseName="ns=isa95_jobcontrol_v2;Pause",
    inputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6103"]),
    outputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6104"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6105",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderID",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "Contains information defining the job order with all parameters and any material, equipment, or physical asset requirements associated with the order."
            ),
        ),
        ns0.datatypes.Argument(
            name="Comment",
            dataType=o6.LocalizedText,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "The comment provides a description of why the method was called. In order to provide the comment in several languages, it is an array of LocalizedText. The array may be empty, when no comment is provided."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6106",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution."))],
)
o6.call(
    nodeId="ns=wire_harness;i=7007",
    browseName="ns=isa95_jobcontrol_v2;Stop",
    inputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6105"]),
    outputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6106"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6107",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobOrder",
            dataType=o6.NodeId("ns=amb;i=3008"),
            valueRank=-1,
            description=o6.LocalizedText(
                "Contains information defining the job order with all parameters and any material, equipment, or physical asset requirements associated with the order."
            ),
        ),
        ns0.datatypes.Argument(
            name="Comment",
            dataType=o6.LocalizedText,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "The comment provides a description of why the method was called. In order to provide the comment in several languages, it is an array of LocalizedText. The array may be empty, when no comment is provided."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6108",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution."))],
)
o6.call(
    nodeId="ns=wire_harness;i=7008",
    browseName="ns=isa95_jobcontrol_v2;Store",
    inputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6107"]),
    outputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6108"]),
)


@o6.objecttype(nodeId="ns=wire_harness;i=1006", browseName="ns=wire_harness;WireHarnessJobOrderReceiverSubStatesType", displayName="WireHarnessJobOrderReceiverSubStatesType")
class WireHarnessJobOrderReceiverSubStatesType(isa95_jobcontrol_v2.objtypes.ISA95JobOrderReceiverSubStatesType):
    abort: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wire_harness;i=7003"])
    cancel: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wire_harness;i=7002"])
    clear: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wire_harness;i=7005"])
    pause: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wire_harness;i=7006"])
    start: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wire_harness;i=7004"])
    stop: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wire_harness;i=7007"])
    store: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wire_harness;i=7008"])


ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6028",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TypeNodeId", dataType=o6.NodeId, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6034",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Parts", dataType=o6.NodeId("ns=amb;i=3010"), valueRank=1, arrayDimensions=[0])],
)
o6.call(
    nodeId="ns=wire_harness;i=7009",
    browseName="ns=wire_harness;FindPartsByType",
    inputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6028"]),
    outputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6034"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6054",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Part", dataType=o6.NodeId("ns=amb;i=3010"), valueRank=-1)],
)
o6.call(nodeId="ns=wire_harness;i=7015", browseName="ns=wire_harness;StorePart", inputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6054"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6055",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Part", dataType=o6.NodeId("ns=amb;i=3010"), valueRank=-1)],
)
o6.call(nodeId="ns=wire_harness;i=7016", browseName="ns=wire_harness;ClearPart", inputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6055"]))


@o6.objecttype(nodeId="ns=wire_harness;i=1004", browseName="ns=wire_harness;PartManagementType", displayName="PartManagementType")
class PartManagementType(ns0.objtypes.BaseObjectType):
    clearPart: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wire_harness;i=7016"])
    findPartsByType: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=wire_harness;i=7009"])
    seals: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=wire_harness;i=6022",
            browseName="ns=wire_harness;Seals",
            dataType=isa95_jobcontrol_v2.datatypes.ISA95MaterialDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    sleeves: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=wire_harness;i=6026",
            browseName="ns=wire_harness;Sleeves",
            dataType=isa95_jobcontrol_v2.datatypes.ISA95MaterialDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    storePart: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wire_harness;i=7015"])
    terminals: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=wire_harness;i=6017",
            browseName="ns=wire_harness;Terminals",
            dataType=isa95_jobcontrol_v2.datatypes.ISA95MaterialDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    wires: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=wire_harness;i=6027",
            browseName="ns=wire_harness;Wires",
            dataType=isa95_jobcontrol_v2.datatypes.ISA95MaterialDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6057",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ArticleSpec", dataType=o6.NodeId("ns=amb;i=3010"), valueRank=-1)],
)
o6.call(nodeId="ns=wire_harness;i=7017", browseName="ns=wire_harness;StoreArticleSpec", inputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6057"]))

ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness;i=6058",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=wire_harness;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ArticleSpec", dataType=o6.NodeId("ns=amb;i=3010"), valueRank=-1)],
)
o6.call(nodeId="ns=wire_harness;i=7018", browseName="ns=wire_harness;ClearArticleSpec", inputArgs=o6.hasProperty(o6.ns["ns=wire_harness;i=6058"]))


@o6.objecttype(nodeId="ns=wire_harness;i=1007", browseName="ns=wire_harness;ArticleSpecManagementType", displayName="ArticleSpecManagementType")
class ArticleSpecManagementType(ns0.objtypes.BaseObjectType):
    articleSpecList: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=wire_harness;i=6023",
            browseName="ns=wire_harness;ArticleSpecList",
            dataType=isa95_jobcontrol_v2.datatypes.ISA95MaterialDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    clearArticleSpec: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wire_harness;i=7018"])
    storeArticleSpec: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=wire_harness;i=7017"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, machinery_result, ns0, wire_harness_vec, wire_harness_datypes
