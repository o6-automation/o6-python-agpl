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

"""Generated OPC UA isa95_jobcontrol_v2 namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import datatypes as isa95_jobcontrol_v2_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=isa95_jobcontrol_v2;i=1001", browseName="ns=isa95_jobcontrol_v2;ISA95PrepareStateMachineType", displayName="ISA95PrepareStateMachineType")
class ISA95PrepareStateMachineType(ns0.objtypes.FiniteStateMachineType):
    fromLoadedToReady: ns0.objtypes.TransitionType
    fromLoadedToWaiting: ns0.objtypes.TransitionType
    fromReadyToLoaded: ns0.objtypes.TransitionType
    fromReadyToWaiting: ns0.objtypes.TransitionType
    fromWaitingToReady: ns0.objtypes.TransitionType
    loaded: ns0.objtypes.StateType
    ready: ns0.objtypes.StateType
    waiting: ns0.objtypes.StateType


@o6.objecttype(nodeId="ns=isa95_jobcontrol_v2;i=1005", browseName="ns=isa95_jobcontrol_v2;ISA95EndedStateMachineType", displayName="ISA95EndedStateMachineType")
class ISA95EndedStateMachineType(ns0.objtypes.FiniteStateMachineType):
    closed: ns0.objtypes.StateType
    completed: ns0.objtypes.StateType
    fromCompletedToClosed: ns0.objtypes.TransitionType


@o6.objecttype(nodeId="ns=isa95_jobcontrol_v2;i=1007", browseName="ns=isa95_jobcontrol_v2;ISA95InterruptedStateMachineType", displayName="ISA95InterruptedStateMachineType")
class ISA95InterruptedStateMachineType(ns0.objtypes.FiniteStateMachineType):
    fromHeldToSuspended: ns0.objtypes.TransitionType
    fromSuspendedToHeld: ns0.objtypes.TransitionType
    held: ns0.objtypes.StateType
    suspended: ns0.objtypes.StateType


@o6.objecttype(
    nodeId="ns=isa95_jobcontrol_v2;i=1006", browseName="ns=isa95_jobcontrol_v2;ISA95JobOrderStatusEventType", displayName="ISA95JobOrderStatusEventType", isAbstract=True
)
class ISA95JobOrderStatusEventType(ns0.objtypes.BaseEventType):
    jobOrder: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=isa95_jobcontrol_v2;i=6047",
            browseName="ns=isa95_jobcontrol_v2;JobOrder",
            dataType=isa95_jobcontrol_v2_datypes.ISA95JobOrderDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    jobResponse: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=isa95_jobcontrol_v2;i=6049",
            browseName="ns=isa95_jobcontrol_v2;JobResponse",
            dataType=isa95_jobcontrol_v2_datypes.ISA95JobResponseDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    jobState: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=isa95_jobcontrol_v2;i=6048",
            browseName="ns=isa95_jobcontrol_v2;JobState",
            dataType=isa95_jobcontrol_v2_datypes.ISA95StateDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=isa95_jobcontrol_v2;i=6040",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobOrder",
            dataType=o6.NodeId("ns=isa95_jobcontrol_v2;i=3008"),
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
    nodeId="ns=isa95_jobcontrol_v2;i=6041",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution."))],
)
o6.call(
    nodeId="ns=isa95_jobcontrol_v2;i=7001",
    browseName="ns=isa95_jobcontrol_v2;Store",
    inputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6040"]),
    outputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6041"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=isa95_jobcontrol_v2;i=6042",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderID", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Contains an ID of the job order, as specified by the method caller.")
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95_jobcontrol_v2;i=6043",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponse",
            dataType=o6.NodeId("ns=isa95_jobcontrol_v2;i=3013"),
            valueRank=-1,
            description=o6.LocalizedText(
                "Contains information about the execution of a job order, such as the current status of the job, actual material consumed, actual material produced, actual equipment used, and job specific data."
            ),
        ),
        ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")),
    ],
)
o6.call(
    nodeId="ns=isa95_jobcontrol_v2;i=7002",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderID",
    inputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6042"]),
    outputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6043"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=isa95_jobcontrol_v2;i=6044",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="JobResponse",
            dataType=o6.NodeId("ns=isa95_jobcontrol_v2;i=3013"),
            valueRank=-1,
            description=o6.LocalizedText(
                "Contains information about the execution of a job order, such as actual material consumed, actual material produced, actual equipment used, and job specific data."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95_jobcontrol_v2;i=6045",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution."))],
)
o6.call(
    nodeId="ns=isa95_jobcontrol_v2;i=7003",
    browseName="ns=isa95_jobcontrol_v2;ReceiveJobResponse",
    inputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6044"]),
    outputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6045"]),
)


@o6.objecttype(
    nodeId="ns=isa95_jobcontrol_v2;i=1004",
    browseName="ns=isa95_jobcontrol_v2;ISA95JobResponseReceiverObjectType",
    displayName="ISA95JobResponseReceiverObjectType",
    description="A Job Response Receiver receives unsolicited Job Responses, usually as the result of completion of a job, or at intermediate points within the job.",
)
class ISA95JobResponseReceiverObjectType(ns0.objtypes.BaseObjectType):
    receiveJobResponse: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=7003"])


ns0.vartypes.PropertyType(
    nodeId="ns=isa95_jobcontrol_v2;i=6051",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobOrder",
            dataType=o6.NodeId("ns=isa95_jobcontrol_v2;i=3008"),
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
    nodeId="ns=isa95_jobcontrol_v2;i=6052",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution."))],
)
o6.call(
    nodeId="ns=isa95_jobcontrol_v2;i=7004",
    browseName="ns=isa95_jobcontrol_v2;StoreAndStart",
    inputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6051"]),
    outputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6052"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=isa95_jobcontrol_v2;i=6053",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7005",
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
    nodeId="ns=isa95_jobcontrol_v2;i=6054",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution."))],
)
o6.call(
    nodeId="ns=isa95_jobcontrol_v2;i=7005",
    browseName="ns=isa95_jobcontrol_v2;Start",
    inputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6053"]),
    outputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6054"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=isa95_jobcontrol_v2;i=6055",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7006",
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
    nodeId="ns=isa95_jobcontrol_v2;i=6056",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution."))],
)
o6.call(
    nodeId="ns=isa95_jobcontrol_v2;i=7006",
    browseName="ns=isa95_jobcontrol_v2;Stop",
    inputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6055"]),
    outputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6056"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=isa95_jobcontrol_v2;i=6057",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7007",
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
    nodeId="ns=isa95_jobcontrol_v2;i=6058",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution."))],
)
o6.call(
    nodeId="ns=isa95_jobcontrol_v2;i=7007",
    browseName="ns=isa95_jobcontrol_v2;Pause",
    inputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6057"]),
    outputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6058"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=isa95_jobcontrol_v2;i=6059",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7008",
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
    nodeId="ns=isa95_jobcontrol_v2;i=6060",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution."))],
)
o6.call(
    nodeId="ns=isa95_jobcontrol_v2;i=7008",
    browseName="ns=isa95_jobcontrol_v2;Resume",
    inputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6059"]),
    outputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6060"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=isa95_jobcontrol_v2;i=6061",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobOrder",
            dataType=o6.NodeId("ns=isa95_jobcontrol_v2;i=3008"),
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
    nodeId="ns=isa95_jobcontrol_v2;i=6062",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution."))],
)
o6.call(
    nodeId="ns=isa95_jobcontrol_v2;i=7009",
    browseName="ns=isa95_jobcontrol_v2;Update",
    inputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6061"]),
    outputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6062"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=isa95_jobcontrol_v2;i=6063",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7010",
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
    nodeId="ns=isa95_jobcontrol_v2;i=6064",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution."))],
)
o6.call(
    nodeId="ns=isa95_jobcontrol_v2;i=7010",
    browseName="ns=isa95_jobcontrol_v2;Abort",
    inputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6063"]),
    outputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6064"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=isa95_jobcontrol_v2;i=6065",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7011",
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
    nodeId="ns=isa95_jobcontrol_v2;i=6066",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution."))],
)
o6.call(
    nodeId="ns=isa95_jobcontrol_v2;i=7011",
    browseName="ns=isa95_jobcontrol_v2;Cancel",
    inputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6065"]),
    outputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6066"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=isa95_jobcontrol_v2;i=6067",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7012",
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
    nodeId="ns=isa95_jobcontrol_v2;i=6068",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution."))],
)
o6.call(
    nodeId="ns=isa95_jobcontrol_v2;i=7012",
    browseName="ns=isa95_jobcontrol_v2;Clear",
    inputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6067"]),
    outputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6068"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=isa95_jobcontrol_v2;i=6069",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7013",
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
    nodeId="ns=isa95_jobcontrol_v2;i=6070",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution."))],
)
o6.call(
    nodeId="ns=isa95_jobcontrol_v2;i=7013",
    browseName="ns=isa95_jobcontrol_v2;RevokeStart",
    inputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6069"]),
    outputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6070"]),
)


@o6.objecttype(
    nodeId="ns=isa95_jobcontrol_v2;i=1002",
    browseName="ns=isa95_jobcontrol_v2;ISA95JobOrderReceiverObjectType",
    displayName="ISA95JobOrderReceiverObjectType",
    description="The OPENSCSJobOrderReciverObjectType contains a method to receive job order commands and optional definitions of allowable job order information",
)
class ISA95JobOrderReceiverObjectType(ns0.objtypes.FiniteStateMachineType):
    abort: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=7010"])
    aborted: ns0.objtypes.StateType
    allowedToStart: ns0.objtypes.StateType
    cancel: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=7011"])
    clear: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=7012"])
    ended: ns0.objtypes.StateType
    equipmentID: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=isa95_jobcontrol_v2;i=6037",
            browseName="ns=isa95_jobcontrol_v2;EquipmentID",
            description="Defines a read-only set of Equipment Class IDs and Equipment IDs that may be specified in a job order.",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    fromAllowedToStartToAborted: ns0.objtypes.TransitionType
    fromAllowedToStartToAllowedToStart: ns0.objtypes.TransitionType
    fromAllowedToStartToNotAllowedToStart: ns0.objtypes.TransitionType
    fromAllowedToStartToRunning: ns0.objtypes.TransitionType
    fromInterruptedToAborted: ns0.objtypes.TransitionType
    fromInterruptedToEnded: ns0.objtypes.TransitionType
    fromInterruptedToRunning: ns0.objtypes.TransitionType
    fromNotAllowedToStartToAborted: ns0.objtypes.TransitionType
    fromNotAllowedToStartToAllowedToStart: ns0.objtypes.TransitionType
    fromNotAllowedToStartToNotAllowedToStart: ns0.objtypes.TransitionType
    fromRunningToAborted: ns0.objtypes.TransitionType
    fromRunningToEnded: ns0.objtypes.TransitionType
    fromRunningToInterrupted: ns0.objtypes.TransitionType
    interrupted: ns0.objtypes.StateType
    jobOrderList: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=isa95_jobcontrol_v2;i=6033",
            browseName="ns=isa95_jobcontrol_v2;JobOrderList",
            description="Defines a read-only list of job order information available from the server.",
            dataType=isa95_jobcontrol_v2_datypes.ISA95JobOrderAndStateDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    materialClassID: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=isa95_jobcontrol_v2;i=6035",
            browseName="ns=isa95_jobcontrol_v2;MaterialClassID",
            description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    materialDefinitionID: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=isa95_jobcontrol_v2;i=6036",
            browseName="ns=isa95_jobcontrol_v2;MaterialDefinitionID",
            description="Defines a read-only set of Material Classes IDs that may be specified in a job order.",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    maxDownloadableJobOrders: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=isa95_jobcontrol_v2;i=6088", browseName="ns=isa95_jobcontrol_v2;MaxDownloadableJobOrders", dataType=o6.UInt16)
    )
    notAllowedToStart: ns0.objtypes.StateType
    pause: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=7007"])
    personnelID: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=isa95_jobcontrol_v2;i=6039",
            browseName="ns=isa95_jobcontrol_v2;PersonnelID",
            description="Defines a read-only set of Personnel IDs and Person IDs that may be specified in a job order.",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    physicalAssetID: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=isa95_jobcontrol_v2;i=6038",
            browseName="ns=isa95_jobcontrol_v2;PhysicalAssetID",
            description="Defines a read-only set of Physical Asset Class IDs and Physical Asset IDs that may be specified in a job order.",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    resume: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=7008"])
    revokeStart: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=7013"])
    running: ns0.objtypes.StateType
    start: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=7005"])
    stop: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=7006"])
    store: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=7001"])
    storeAndStart: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=7004"])
    update: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=7009"])
    workMaster: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=isa95_jobcontrol_v2;i=6034",
            browseName="ns=isa95_jobcontrol_v2;WorkMaster",
            description="Defines a read-only set of work master IDs that may be specified in a job order, and the read-only set of parameters that may be specified for a specific work master.",
            dataType=isa95_jobcontrol_v2_datypes.ISA95WorkMasterDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


@o6.objecttype(nodeId="ns=isa95_jobcontrol_v2;i=1008", browseName="ns=isa95_jobcontrol_v2;ISA95JobOrderReceiverSubStatesType", displayName="ISA95JobOrderReceiverSubStatesType")
class ISA95JobOrderReceiverSubStatesType(ISA95JobOrderReceiverObjectType):
    aborted: ns0.objtypes.StateType
    allowedToStart: ns0.objtypes.StateType
    allowedToStartSubstates: ISA95PrepareStateMachineType | None
    ended: ns0.objtypes.StateType
    endedSubstates: ISA95EndedStateMachineType | None
    fromAllowedToStartToAborted: ns0.objtypes.TransitionType
    fromAllowedToStartToAllowedToStart: ns0.objtypes.TransitionType
    fromAllowedToStartToNotAllowedToStart: ns0.objtypes.TransitionType
    fromAllowedToStartToRunning: ns0.objtypes.TransitionType
    fromInterruptedToAborted: ns0.objtypes.TransitionType
    fromInterruptedToEnded: ns0.objtypes.TransitionType
    fromInterruptedToRunning: ns0.objtypes.TransitionType
    fromNotAllowedToStartToAborted: ns0.objtypes.TransitionType
    fromNotAllowedToStartToAllowedToStart: ns0.objtypes.TransitionType
    fromNotAllowedToStartToNotAllowedToStart: ns0.objtypes.TransitionType
    fromRunningToAborted: ns0.objtypes.TransitionType
    fromRunningToEnded: ns0.objtypes.TransitionType
    fromRunningToInterrupted: ns0.objtypes.TransitionType
    interrupted: ns0.objtypes.StateType
    interruptedSubstates: ISA95InterruptedStateMachineType | None
    notAllowedToStart: ns0.objtypes.StateType
    notAllowedToStartSubstates: ISA95PrepareStateMachineType | None
    running: ns0.objtypes.StateType


ns0.vartypes.PropertyType(
    nodeId="ns=isa95_jobcontrol_v2;i=6016",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="JobOrderState",
            dataType=o6.NodeId("ns=isa95_jobcontrol_v2;i=3006"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "Contains a job status of the JobResponse to be returned. The array shall provide at least one entry representing the top level state and potentially additional entries representing substates. The first entry shall be the top level entry, having the BrowsePath set to null. The order of the substates is not defined."
            ),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95_jobcontrol_v2;i=6017",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=isa95_jobcontrol_v2;i=7014",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="JobResponses",
            dataType=o6.NodeId("ns=isa95_jobcontrol_v2;i=3013"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText(
                "Contains a list of information about the execution of a job order, such as the current status of the job, actual material consumed, actual material produced, actual equipment used, and job specific data. "
            ),
        ),
        ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.UInt64, valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")),
    ],
)
o6.call(
    nodeId="ns=isa95_jobcontrol_v2;i=7014",
    browseName="ns=isa95_jobcontrol_v2;RequestJobResponseByJobOrderState",
    inputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6016"]),
    outputArgs=o6.hasProperty(o6.ns["ns=isa95_jobcontrol_v2;i=6017"]),
)


@o6.objecttype(
    nodeId="ns=isa95_jobcontrol_v2;i=1003",
    browseName="ns=isa95_jobcontrol_v2;ISA95JobResponseProviderObjectType",
    displayName="ISA95JobResponseProviderObjectType",
    description="The OPENSCSJobResponseProviderObjectType contains a method to receive unsolicited job response requests.",
)
class ISA95JobResponseProviderObjectType(ns0.objtypes.BaseObjectType):
    jobOrderResponseList: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=isa95_jobcontrol_v2;i=6050",
            browseName="ns=isa95_jobcontrol_v2;JobOrderResponseList",
            dataType=isa95_jobcontrol_v2_datypes.ISA95JobResponseDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    requestJobResponseByJobOrderID: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=7002"])
    requestJobResponseByJobOrderState: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=isa95_jobcontrol_v2;i=7014"])


o6.reference(ISA95JobResponseProviderObjectType, "i=41", ISA95JobOrderStatusEventType)


del Any, TYPE_CHECKING, uuid, o6, ns0, isa95_jobcontrol_v2_datypes
