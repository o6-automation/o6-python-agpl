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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=6011",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="AggregationElement", dataType=o6.NodeId("ns=open_scs;i=3002"), valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ParentSNFormat", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="PackedElementSNFormat", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="AggregationContext", dataType=o6.NodeId("ns=open_scs;i=15010"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=6013",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1)],
)
o6.call(
    nodeId="ns=open_scs;i=7004",
    browseName="ns=open_scs;AggregationUnpackingEvent",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=6011"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=6013"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15039",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15038",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="SNCollection", dataType=o6.NodeId("ns=open_scs;i=15008"), valueRank=-1),
        ns0.datatypes.Argument(name="PoolSelectionCriteria", dataType=o6.NodeId("ns=open_scs;i=15010"), valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="SNFormat", dataType=o6.String, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15040",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15038",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1)],
)
o6.call(
    nodeId="ns=open_scs;i=15038",
    browseName="ns=open_scs;SNtoEncoded",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15039"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15040"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15045",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15044",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="SNCollection", dataType=o6.NodeId("ns=open_scs;i=15008"), valueRank=-1),
        ns0.datatypes.Argument(name="PoolSelectionCriteria", dataType=o6.NodeId("ns=open_scs;i=15010"), valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="SNFormat", dataType=o6.String, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15046",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15044",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1)],
)
o6.call(
    nodeId="ns=open_scs;i=15044",
    browseName="ns=open_scs;SNtoUnallocated",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15045"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15046"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15048",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15047",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="SNCollection",
            dataType=o6.NodeId("ns=open_scs;i=15008"),
            valueRank=-1,
            description=o6.LocalizedText("Contains a Serial Number Collection from which Serial Numbers were originally provided."),
        ),
        ns0.datatypes.Argument(
            name="PoolSelectionCriteria",
            dataType=o6.NodeId("ns=open_scs;i=15010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("Identified value to be used by the method provider to determine which pool to return the Serial Numbers to"),
        ),
        ns0.datatypes.Argument(name="SNFormat", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The serial number format of the serial numbers being returned. ")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15049",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15047",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")
        )
    ],
)
o6.call(
    nodeId="ns=open_scs;i=15047",
    browseName="ns=open_scs;SNReturnAllocated",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15048"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15049"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15051",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15050",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="SNCollection",
            dataType=o6.NodeId("ns=open_scs;i=15008"),
            valueRank=-1,
            description=o6.LocalizedText("Contains a Serial Number Collection from which Serial Numbers were originally provided."),
        ),
        ns0.datatypes.Argument(
            name="PoolSelectionCriteria",
            dataType=o6.NodeId("ns=open_scs;i=15010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("Identified value to be used by the method provider to determine which pool to return the Serial Numbers to"),
        ),
        ns0.datatypes.Argument(name="SNFormat", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The serial number format of the serial numbers being returned. ")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15052",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15050",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")
        )
    ],
)
o6.call(
    nodeId="ns=open_scs;i=15050",
    browseName="ns=open_scs;SNReturnUnallocated",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15051"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15052"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15054",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15053",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(
            name="SNCollectionID",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText("Identifies the Serial Number Collection from which unassigned Serial Numbers are to be provided."),
        ),
        ns0.datatypes.Argument(name="Count", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("Identifies the number of Serial Numbers requested.")),
        ns0.datatypes.Argument(
            name="SNFormat", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Defines the desired serial number format for the requested serial numbers. ")
        ),
        ns0.datatypes.Argument(
            name="PoolSelectionCriteria",
            dataType=o6.NodeId("ns=open_scs;i=15010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("Identified value to be used by the method provider to determine which Serial Numbers to return. "),
        ),
        ns0.datatypes.Argument(
            name="RequestToken",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText("If it has a value of null or an empty string, then this is the initial request for Serial Numbers. "),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15055",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15053",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution. ")
        ),
        ns0.datatypes.Argument(
            name="SNCollection",
            dataType=o6.NodeId("ns=open_scs;i=15008"),
            valueRank=-1,
            description=o6.LocalizedText("Contains requested Serial Number collection with Serial Numbers of the specified state. "),
        ),
        ns0.datatypes.Argument(
            name="ReturnedRequestToken",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "If non null or an empty string, then there are more serial numbers to be returned and the returned Request Token is to be passed as an input parameter on a subsequent call."
            ),
        ),
    ],
)
o6.call(
    nodeId="ns=open_scs;i=15053",
    browseName="ns=open_scs;SNRequestAllocated",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15054"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15055"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15057",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15056",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(
            name="SNCollectionID",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText("Identifies the Serial Number Collection from which unassigned Serial Numbers are to be provided."),
        ),
        ns0.datatypes.Argument(name="Count", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("Identifies the number of Serial Numbers requested.")),
        ns0.datatypes.Argument(
            name="SNFormat", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Defines the desired serial number format for the requested serial numbers. ")
        ),
        ns0.datatypes.Argument(
            name="PoolSelectionCriteria",
            dataType=o6.NodeId("ns=open_scs;i=15010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("Identified value to be used by the method provider to determine which Serial Numbers to return. "),
        ),
        ns0.datatypes.Argument(
            name="RequestToken",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText("If it has a value of null or an empty string, then this is the initial request for Serial Numbers. "),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15058",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15056",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution. ")
        ),
        ns0.datatypes.Argument(
            name="SNCollection",
            dataType=o6.NodeId("ns=open_scs;i=15008"),
            valueRank=-1,
            description=o6.LocalizedText("Contains requested Serial Number collection with Serial Numbers of the specified state. "),
        ),
        ns0.datatypes.Argument(
            name="ReturnedRequestToken",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "If non null or an empty string, then there are more serial numbers to be returned and the returned Request Token is to be passed as an input parameter on a subsequent call."
            ),
        ),
    ],
)
o6.call(
    nodeId="ns=open_scs;i=15056",
    browseName="ns=open_scs;SNRequestUnallocated",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15057"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15058"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15060",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15059",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(
            name="SNCollectionID",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText("Identifies the Serial Number Collection from which unassigned Serial Numbers are to be provided."),
        ),
        ns0.datatypes.Argument(name="Count", dataType=o6.UInt32, valueRank=-1, description=o6.LocalizedText("Identifies the number of Serial Numbers requested.")),
        ns0.datatypes.Argument(
            name="SNFormat", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Defines the desired serial number format for the requested serial numbers. ")
        ),
        ns0.datatypes.Argument(
            name="PoolSelectionCriteria",
            dataType=o6.NodeId("ns=open_scs;i=15010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("Identified value to be used by the method provider to determine which Serial Numbers to return. "),
        ),
        ns0.datatypes.Argument(
            name="RequestToken",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText("If it has a value of null or an empty string, then this is the initial request for Serial Numbers. "),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15061",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15059",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution. ")
        ),
        ns0.datatypes.Argument(
            name="SNCollection",
            dataType=o6.NodeId("ns=open_scs;i=15008"),
            valueRank=-1,
            description=o6.LocalizedText("Contains requested Serial Number collection with Serial Numbers of the specified state. "),
        ),
        ns0.datatypes.Argument(
            name="ReturnedRequestToken",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "If non null or an empty string, then there are more serial numbers to be returned and the returned Request Token is to be passed as an input parameter on a subsequent call."
            ),
        ),
    ],
)
o6.call(
    nodeId="ns=open_scs;i=15059",
    browseName="ns=open_scs;SNRequestUnassigned",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15060"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15061"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15065",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15064",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="LabelCollection",
            dataType=o6.NodeId("ns=open_scs;i=15006"),
            valueRank=-1,
            description=o6.LocalizedText("Identifies the Label Collection with Serial Numbers and optional label properties."),
        ),
        ns0.datatypes.Argument(
            name="SNFormat", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Defines the format of the serial numbers associated to the event.")
        ),
        ns0.datatypes.Argument(
            name="OPENSCSEventContext",
            dataType=o6.NodeId("ns=open_scs;i=15010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("Zero or mode key value pairs that define additional context information for the event, such as order number or lot number."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15066",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15064",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")
        )
    ],
)
o6.call(
    nodeId="ns=open_scs;i=15064",
    browseName="ns=open_scs;SIDDecommissioningEvent",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15065"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15066"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15068",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15067",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="LabelCollection",
            dataType=o6.NodeId("ns=open_scs;i=15006"),
            valueRank=-1,
            description=o6.LocalizedText("Identifies the Label Collection with Serial Numbers and optional label properties."),
        ),
        ns0.datatypes.Argument(
            name="SNFormat", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Defines the format of the serial numbers associated to the event.")
        ),
        ns0.datatypes.Argument(
            name="OPENSCSEventContext",
            dataType=o6.NodeId("ns=open_scs;i=15010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("Zero or mode key value pairs that define additional context information for the event, such as order number or lot number."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15069",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15067",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")
        )
    ],
)
o6.call(
    nodeId="ns=open_scs;i=15067",
    browseName="ns=open_scs;SIDInspectingEvent",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15068"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15069"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15071",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15070",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="LabelCollection",
            dataType=o6.NodeId("ns=open_scs;i=15006"),
            valueRank=-1,
            description=o6.LocalizedText("Identifies the Label Collection with Serial Numbers and optional label properties."),
        ),
        ns0.datatypes.Argument(
            name="SNFormat", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Defines the format of the serial numbers associated to the event.")
        ),
        ns0.datatypes.Argument(
            name="OPENSCSEventContext",
            dataType=o6.NodeId("ns=open_scs;i=15010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("Zero or mode key value pairs that define additional context information for the event, such as order number or lot number."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15072",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15070",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")
        )
    ],
)
o6.call(
    nodeId="ns=open_scs;i=15070",
    browseName="ns=open_scs;SIDShippingEvent",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15071"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15072"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15074",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15073",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="LabelCollection",
            dataType=o6.NodeId("ns=open_scs;i=15006"),
            valueRank=-1,
            description=o6.LocalizedText("Identifies the Label Collection with Serial Numbers and optional label properties."),
        ),
        ns0.datatypes.Argument(
            name="SNFormat", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Defines the format of the serial numbers associated to the event.")
        ),
        ns0.datatypes.Argument(
            name="OPENSCSEventContext",
            dataType=o6.NodeId("ns=open_scs;i=15010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("Zero or mode key value pairs that define additional context information for the event, such as order number or lot number."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15075",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15073",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")
        )
    ],
)
o6.call(
    nodeId="ns=open_scs;i=15073",
    browseName="ns=open_scs;SIDDestroyingEvent",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15074"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15075"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15077",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15076",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="LabelCollection",
            dataType=o6.NodeId("ns=open_scs;i=15006"),
            valueRank=-1,
            description=o6.LocalizedText("Identifies the Label Collection with Serial Numbers and optional label properties."),
        ),
        ns0.datatypes.Argument(
            name="SNFormat", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Defines the format of the serial numbers associated to the event.")
        ),
        ns0.datatypes.Argument(
            name="OPENSCSEventContext",
            dataType=o6.NodeId("ns=open_scs;i=15010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("Zero or mode key value pairs that define additional context information for the event, such as order number or lot number."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15078",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15076",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")
        )
    ],
)
o6.call(
    nodeId="ns=open_scs;i=15076",
    browseName="ns=open_scs;SIDCommissioningEvent",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15077"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15078"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15080",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15079",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="LabelCollection",
            dataType=o6.NodeId("ns=open_scs;i=15006"),
            valueRank=-1,
            description=o6.LocalizedText("Identifies the Label Collection with Serial Numbers and optional label properties."),
        ),
        ns0.datatypes.Argument(
            name="SNFormat", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Defines the format of the serial numbers associated to the event.")
        ),
        ns0.datatypes.Argument(
            name="OPENSCSEventContext",
            dataType=o6.NodeId("ns=open_scs;i=15010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("Zero or mode key value pairs that define additional context information for the event, such as order number or lot number."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15081",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15079",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")
        )
    ],
)
o6.call(
    nodeId="ns=open_scs;i=15079",
    browseName="ns=open_scs;LabelsSamplingEvent",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15080"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15081"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15083",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15082",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="LabelCollection",
            dataType=o6.NodeId("ns=open_scs;i=15006"),
            valueRank=-1,
            description=o6.LocalizedText("Identifies the Label Collection with Serial Numbers and optional label properties."),
        ),
        ns0.datatypes.Argument(
            name="SNFormat", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Defines the format of the serial numbers associated to the event.")
        ),
        ns0.datatypes.Argument(
            name="OPENSCSEventContext",
            dataType=o6.NodeId("ns=open_scs;i=15010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("Zero or mode key value pairs that define additional context information for the event, such as order number or lot number."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15084",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15082",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")
        )
    ],
)
o6.call(
    nodeId="ns=open_scs;i=15082",
    browseName="ns=open_scs;LabelsInspectingEvent",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15083"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15084"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15086",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15085",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="LabelCollection",
            dataType=o6.NodeId("ns=open_scs;i=15006"),
            valueRank=-1,
            description=o6.LocalizedText("Identifies the Label Collection with Serial Numbers and optional label properties."),
        ),
        ns0.datatypes.Argument(
            name="SNFormat", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Defines the format of the serial numbers associated to the event.")
        ),
        ns0.datatypes.Argument(
            name="OPENSCSEventContext",
            dataType=o6.NodeId("ns=open_scs;i=15010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("Zero or mode key value pairs that define additional context information for the event, such as order number or lot number."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15087",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15085",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")
        )
    ],
)
o6.call(
    nodeId="ns=open_scs;i=15085",
    browseName="ns=open_scs;LabelsScrappingEvent",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15086"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15087"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15089",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15088",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="LabelCollection",
            dataType=o6.NodeId("ns=open_scs;i=15006"),
            valueRank=-1,
            description=o6.LocalizedText("Identifies the Label Collection with Serial Numbers and optional label properties."),
        ),
        ns0.datatypes.Argument(
            name="SNFormat", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Defines the format of the serial numbers associated to the event.")
        ),
        ns0.datatypes.Argument(
            name="OPENSCSEventContext",
            dataType=o6.NodeId("ns=open_scs;i=15010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("Zero or mode key value pairs that define additional context information for the event, such as order number or lot number."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15090",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15088",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")
        )
    ],
)
o6.call(
    nodeId="ns=open_scs;i=15088",
    browseName="ns=open_scs;LabelsEncodingEvent",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15089"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15090"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15092",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15091",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="SNCollection", dataType=o6.NodeId("ns=open_scs;i=15008"), valueRank=-1, description=o6.LocalizedText("Identifies the Serial Number Collection.")
        ),
        ns0.datatypes.Argument(
            name="SNFormat", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Defines the format of the serial numbers associated to the event.")
        ),
        ns0.datatypes.Argument(
            name="OPENSCSEventContext",
            dataType=o6.NodeId("ns=open_scs;i=15010"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("Zero or mode key value pairs that define additional context information for the event, such as order number or lot number."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15093",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15091",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")
        )
    ],
)
o6.call(
    nodeId="ns=open_scs;i=15091",
    browseName="ns=open_scs;SNInvalidatingEvent",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15092"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15093"]),
)


@o6.objecttype(nodeId="ns=open_scs;i=15062", browseName="ns=open_scs;OPENSCSEventManagerObjectType", displayName="OPENSCSEventManagerObjectType")
class OPENSCSEventManagerObjectType(ns0.objtypes.BaseObjectType):
    ePCISStream: ns0.objtypes.TemporaryFileTransferType | None
    labelsEncodingEvent: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=open_scs;i=15088"])
    labelsInspectingEvent: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=open_scs;i=15082"])
    labelsSamplingEvent: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=open_scs;i=15079"])
    labelsScrappingEvent: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=open_scs;i=15085"])
    maxEPCISObjectEventSIDs: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=6009", browseName="ns=open_scs;MaxEPCISObjectEventSIDs", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )
    maxEPCISaggregationEvents: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=6010", browseName="ns=open_scs;MaxEPCISaggregationEvents", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )
    maxEvents: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15063", browseName="ns=open_scs;MaxEvents", dataType=o6.UInt32))
    sIDCommissioningEvent: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=open_scs;i=15076"])
    sIDDecommissioningEvent: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=open_scs;i=15064"])
    sIDDestroyingEvent: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=open_scs;i=15073"])
    sIDInspectingEvent: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=open_scs;i=15067"])
    sIDShippingEvent: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=open_scs;i=15070"])
    sNInvalidatingEvent: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=open_scs;i=15091"])


ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15100",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15099",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="AggregationElement", dataType=o6.NodeId("ns=open_scs;i=3002"), valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="ParentSNFormat", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="PackedElementSNFormat", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="AggregationContext", dataType=o6.NodeId("ns=open_scs;i=15010"), valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15101",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15099",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1, description=o6.LocalizedText("Returns the status of the method execution.")
        )
    ],
)
o6.call(
    nodeId="ns=open_scs;i=15099",
    browseName="ns=open_scs;AggregationPackingEvent",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15100"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15101"]),
)


@o6.objecttype(
    nodeId="ns=open_scs;i=15094",
    browseName="ns=open_scs;OPENSCSAggregationManagerObjectType",
    displayName="OPENSCSAggregationManagerObjectType",
    description="The aggregation manager receives unsolicited events through the aggregation methods.  The aggregation methods have the same method signature.",
)
class OPENSCSAggregationManagerObjectType(ns0.objtypes.BaseObjectType):
    aggregationPackingEvent: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=open_scs;i=15099"])
    aggregationUnpackingEvent: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=open_scs;i=7004"])
    maxAggregationEvents: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15095", browseName="ns=open_scs;MaxAggregationEvents", dataType=o6.UInt32)
    )


@o6.objecttype(nodeId="ns=open_scs;i=15102", browseName="ns=open_scs;OPENSCSSIDClassObjectType", displayName="OPENSCSSIDClassObjectType")
class OPENSCSSIDClassObjectType(ns0.objtypes.BaseObjectType):
    allowedCharacterSet: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15105", browseName="ns=open_scs;AllowedCharacterSet", dataType=o6.String)
    )
    intendedUse: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15104", browseName="ns=open_scs;IntendedUse", dataType=o6.String)
    )
    sIDClassDescription: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15107", browseName="ns=open_scs;SIDClassDescription", dataType=o6.String)
    )
    sIDClassID: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15109", browseName="ns=open_scs;SIDClassID", dataType=o6.String))
    sIDClassOwner: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15108", browseName="ns=open_scs;SIDClassOwner", dataType=o6.String))
    sIDClassProperty: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=open_scs;i=6012",
            browseName="ns=open_scs;SIDClassProperty",
            dataType=open_scs_datypes.OPENSCSSIDClassPropertyDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    syntaxSpecification: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15106", browseName="ns=open_scs;SyntaxSpecification", dataType=o6.String)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15111",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15110",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="SNCollection", dataType=o6.NodeId("ns=open_scs;i=15008"), valueRank=-1),
        ns0.datatypes.Argument(name="PoolSelectionCriteria", dataType=o6.NodeId("ns=open_scs;i=15010"), valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="SNFormat", dataType=o6.String, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=open_scs;i=15112",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=open_scs;i=15110",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReturnStatus", dataType=o6.NodeId("ns=open_scs;i=15001"), valueRank=-1)],
)
o6.call(
    nodeId="ns=open_scs;i=15110",
    browseName="ns=open_scs;SNtoAllocated",
    inputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15111"]),
    outputArgs=o6.hasProperty(o6.ns["ns=open_scs;i=15112"]),
)


@o6.objecttype(nodeId="ns=open_scs;i=15032", browseName="ns=open_scs;OPENSCSPoolManagerObjectType", displayName="OPENSCSPoolManagerObjectType")
class OPENSCSPoolManagerObjectType(ns0.objtypes.BaseObjectType):
    maxSNPushable: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15034", browseName="ns=open_scs;MaxSNPushable", dataType=o6.UInt32))
    maxSNRequestable: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15036", browseName="ns=open_scs;MaxSNRequestable", dataType=o6.UInt32)
    )
    maxSNReturnable: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15035", browseName="ns=open_scs;MaxSNReturnable", dataType=o6.UInt32)
    )
    poolSelectionCriteria: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=open_scs;i=15033", browseName="ns=open_scs;PoolSelectionCriteria", dataType=open_scs_datypes.OPENSCSKeyValueDataType, valueRank=1, arrayDimensions=[0]
        )
    )
    sNFormat: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=open_scs;i=15037", browseName="ns=open_scs;SNFormat", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    sNRequestAllocated: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=open_scs;i=15053"])
    sNRequestUnallocated: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=open_scs;i=15056"])
    sNRequestUnassigned: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=open_scs;i=15059"])
    sNReturnAllocated: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=open_scs;i=15047"])
    sNReturnUnallocated: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=open_scs;i=15050"])
    sNtoAllocated: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=open_scs;i=15110"])
    sNtoEncoded: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=open_scs;i=15038"])
    sNtoUnallocated: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=open_scs;i=15044"])


del Any, TYPE_CHECKING, uuid, o6, ns0, open_scs_datypes
