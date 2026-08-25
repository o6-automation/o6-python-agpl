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

"""Generated OPC UA mt_connect namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as mt_connect_reftypes
from . import datatypes as mt_connect_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(
    nodeId="ns=mt_connect;i=2621",
    browseName="ns=mt_connect;MTAssetEventType",
    displayName="MTAssetEventType",
    description="The asset events have an additional attribute regarding the asset change\n      or removal identifier and the type of asset that is being reported.",
    dataType=mt_connect_datypes.AssetEventDataType,
    valueRank=o6.ValueRank.SCALAR,
)
class MTAssetEventType(ns0.vartypes.BaseDataVariableType):
    category: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2753",
            browseName="ns=mt_connect;Category",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=mt_connect_datypes.MTCategoryType,
            valueRank=-1,
        )
    )
    constraints: MTConstraintType | None
    mTSubTypeName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2755",
            browseName="ns=mt_connect;MTSubTypeName",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    mTTypeName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2754",
            browseName="ns=mt_connect;MTTypeName",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2752",
            browseName="ns=mt_connect;Name",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    periodFilter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2759",
            browseName="ns=mt_connect;PeriodFilter",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.Float,
            valueRank=-1,
        )
    )
    representation: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2758",
            browseName="ns=mt_connect;Representation",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=mt_connect_datypes.MTRepresentationType,
            valueRank=-1,
        )
    )
    sampleRate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2757",
            browseName="ns=mt_connect;SampleRate",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.Double,
            valueRank=-1,
        )
    )
    sourceData: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2756",
            browseName="ns=mt_connect;SourceData",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    xmlId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2751",
            browseName="ns=mt_connect;XmlId",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )


@o6.variabletype(
    nodeId="ns=mt_connect;i=2471",
    browseName="ns=mt_connect;MTMessageType",
    displayName="MTMessageType",
    description="The message is a sub-type of the \\uaterm{DataVariableType} using the\n      \\mtuatype{MessageDataType} to represent the values for \\mtterm{NativeCode}\n      and \\mtterm{Text} of the message from the \\gls{CDATA} of the MTConnect\n      Streams message. Any text string of information to be transferred from a\n      piece of equipment to a client software application.",
    dataType=mt_connect_datypes.MessageDataType,
    valueRank=o6.ValueRank.SCALAR,
)
class MTMessageType(ns0.vartypes.BaseDataVariableType):
    category: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2793",
            browseName="ns=mt_connect;Category",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=mt_connect_datypes.MTCategoryType,
            valueRank=-1,
        )
    )
    constraints: MTConstraintType | None
    mTSubTypeName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2795",
            browseName="ns=mt_connect;MTSubTypeName",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    mTTypeName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2794",
            browseName="ns=mt_connect;MTTypeName",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2792",
            browseName="ns=mt_connect;Name",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    periodFilter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2799",
            browseName="ns=mt_connect;PeriodFilter",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.Float,
            valueRank=-1,
        )
    )
    representation: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2798",
            browseName="ns=mt_connect;Representation",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=mt_connect_datypes.MTRepresentationType,
            valueRank=-1,
        )
    )
    sampleRate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2797",
            browseName="ns=mt_connect;SampleRate",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.Double,
            valueRank=-1,
        )
    )
    sourceData: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2796",
            browseName="ns=mt_connect;SourceData",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    xmlId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2791",
            browseName="ns=mt_connect;XmlId",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )


@o6.variabletype(
    nodeId="ns=mt_connect;i=2433",
    browseName="ns=mt_connect;MTStringEventType",
    displayName="MTStringEventType",
    description="All data items with \\gls{category} \\uamodel{EVENT} where the data is\n      freeform text. The data type will be set to String for all the sub-types.\n      All extended type, regardless of controlled vocabularies, will use this\n      base type unless proprietary enumerations are added to the nodeset as\n      required by the builtin state event types inherited from\n      \\mtmodel{MTControlledVocabEventType} (see\n      \\ref{type:MTControlledVocabEventType}).",
    dataType=o6.String,
    valueRank=o6.ValueRank.SCALAR,
)
class MTStringEventType(ns0.vartypes.BaseDataVariableType):
    category: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2869",
            browseName="ns=mt_connect;Category",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=mt_connect_datypes.MTCategoryType,
            valueRank=-1,
        )
    )
    constraints: MTConstraintType | None
    mTSubTypeName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2871",
            browseName="ns=mt_connect;MTSubTypeName",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    mTTypeName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2870",
            browseName="ns=mt_connect;MTTypeName",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2868",
            browseName="ns=mt_connect;Name",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    periodFilter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2875",
            browseName="ns=mt_connect;PeriodFilter",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.Float,
            valueRank=-1,
        )
    )
    representation: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2874",
            browseName="ns=mt_connect;Representation",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=mt_connect_datypes.MTRepresentationType,
            valueRank=-1,
        )
    )
    sampleRate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2873",
            browseName="ns=mt_connect;SampleRate",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.Double,
            valueRank=-1,
        )
    )
    sourceData: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2872",
            browseName="ns=mt_connect;SourceData",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    xmlId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2867",
            browseName="ns=mt_connect;XmlId",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )


@o6.variabletype(
    nodeId="ns=mt_connect;i=2626",
    browseName="ns=mt_connect;MTControlledVocabEventType",
    displayName="MTControlledVocabEventType",
    description="All \\glspl{MTDataItem} with \\gls{category} \\mtmodel{EVENT} having\n      Controlled Vocabularies (Enumerations) will be added as sub-types of this\n      type which is mapped to the OPC/UA MultiStateValueDiscreteType. Otherwise,\n      either \\mtmodel{MTString} or \\mtmodel{MTNumeric} will be used. All\n      subtypes are direct representations of the MTConnect equivalent elements\n      that can be found in the MTConnect Part 3 \\cite{MTCPart3} documents.",
    dataType=ns0.datatypes.UInteger,
    valueRank=o6.ValueRank.SCALAR,
)
class MTControlledVocabEventType(ns0.vartypes.MultiStateDiscreteType):
    category: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2773",
            browseName="ns=mt_connect;Category",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=mt_connect_datypes.MTCategoryType,
            valueRank=-1,
        )
    )
    constraints: MTConstraintType | None
    mTSubTypeName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2775",
            browseName="ns=mt_connect;MTSubTypeName",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    mTTypeName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2774",
            browseName="ns=mt_connect;MTTypeName",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2772",
            browseName="ns=mt_connect;Name",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    periodFilter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2779",
            browseName="ns=mt_connect;PeriodFilter",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.Float,
            valueRank=-1,
        )
    )
    representation: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2778",
            browseName="ns=mt_connect;Representation",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=mt_connect_datypes.MTRepresentationType,
            valueRank=-1,
        )
    )
    sampleRate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2777",
            browseName="ns=mt_connect;SampleRate",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.Double,
            valueRank=-1,
        )
    )
    sourceData: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2776",
            browseName="ns=mt_connect;SourceData",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    valueAsText: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=3090",
            browseName="ns=mt_connect;ValueAsText",
            description="All \\glspl{MTDataItem} with \\gls{category} \\mtmodel{EVENT} having\n      Controlled Vocabularies (Enumerations) will be added as sub-types of this\n      type which is mapped to the OPC/UA MultiStateValueDiscreteType. Otherwise,\n      either \\mtmodel{MTString} or \\mtmodel{MTNumeric} will be used. All\n      subtypes are direct representations of the MTConnect equivalent elements\n      that can be found in the MTConnect Part 3 \\cite{MTCPart3} documents.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    xmlId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2771",
            browseName="ns=mt_connect;XmlId",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )


@o6.variabletype(
    nodeId="ns=mt_connect;i=2438",
    browseName="ns=mt_connect;MTNumericEventType",
    displayName="MTNumericEventType",
    description="All data items with category \\gls{MTEvent} and a numeric value. These are\n      usually counters for parts and lines. Currently only builtin types that\n      are known to be integers will be sub-typed from this type. Extended types\n      will be subtyped from the \\mtuatype{MTStringEventType}.",
    dataType=ns0.datatypes.Number,
    valueRank=o6.ValueRank.SCALAR,
)
class MTNumericEventType(ns0.vartypes.DataItemType):
    category: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2807",
            browseName="ns=mt_connect;Category",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=mt_connect_datypes.MTCategoryType,
            valueRank=-1,
        )
    )
    constraints: MTConstraintType | None
    coordinateSystem: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2822",
            browseName="ns=mt_connect;CoordinateSystem",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=mt_connect_datypes.MTCoordinateSystemType,
            valueRank=-1,
        )
    )
    duration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=3671",
            browseName="ns=mt_connect;Duration",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
        )
    )
    initialValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2823",
            browseName="ns=mt_connect;InitialValue",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=o6.Double,
            valueRank=-1,
        )
    )
    mTSubTypeName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2809",
            browseName="ns=mt_connect;MTSubTypeName",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    mTTypeName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2808",
            browseName="ns=mt_connect;MTTypeName",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    minimumDeltaFilter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2826",
            browseName="ns=mt_connect;MinimumDeltaFilter",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=o6.Float,
            valueRank=-1,
        )
    )
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2806",
            browseName="ns=mt_connect;Name",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    nativeUnits: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2821",
            browseName="ns=mt_connect;NativeUnits",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    periodFilter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2813",
            browseName="ns=mt_connect;PeriodFilter",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.Float,
            valueRank=-1,
        )
    )
    representation: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2812",
            browseName="ns=mt_connect;Representation",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=mt_connect_datypes.MTRepresentationType,
            valueRank=-1,
        )
    )
    resetTrigger: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2824",
            browseName="ns=mt_connect;ResetTrigger",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=mt_connect_datypes.MTResetTriggerType,
            valueRank=-1,
        )
    )
    resetTriggeredReason: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=3675",
            browseName="ns=mt_connect;ResetTriggeredReason",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=mt_connect_datypes.MTResetTriggerType,
            valueRank=-1,
        )
    )
    sampleRate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2811",
            browseName="ns=mt_connect;SampleRate",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.Double,
            valueRank=-1,
        )
    )
    significantDigits: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2819",
            browseName="ns=mt_connect;SignificantDigits",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=o6.Int16,
            valueRank=-1,
        )
    )
    sourceData: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2810",
            browseName="ns=mt_connect;SourceData",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    statistic: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2820",
            browseName="ns=mt_connect;Statistic",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=mt_connect_datypes.MTStatisticType,
            valueRank=-1,
        )
    )
    units: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2825",
            browseName="ns=mt_connect;Units",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    xmlId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2805",
            browseName="ns=mt_connect;XmlId",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )


@o6.variabletype(
    nodeId="ns=mt_connect;i=2429",
    browseName="ns=mt_connect;MTSampleType",
    displayName="MTSampleType",
    description="Data Items with category \\mtmodel{SAMPLE}. The simplest mapping since all\n      these types are floating point numeric data and comply with the\n      \\uamodel{AnalogUnitType} from \\cite{UAPart8} Amendment 1. In ammendment 1,\n      the \\uamodel{EURange} is optional. \\uamodel{EngineeringUnits} for all\n      \\mtuatype{MTSampleType} Data Items. The \\uamodel{EURange} will becreated\n      if the \\mtmodel{Constraints} element exists and both \\mtmodel{Maximum} and\n      \\mtmodel{Minimum} values are given. An XML element that provides the\n      information and data reported from a piece of equipment for those dataitem\n      elements defined with a category attribute of sample category in the\n      mtconnectdevices document.",
    dataType=ns0.datatypes.Number,
    valueRank=o6.ValueRank.SCALAR,
)
class MTSampleType(ns0.vartypes.AnalogUnitType):
    category: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2841",
            browseName="ns=mt_connect;Category",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=mt_connect_datypes.MTCategoryType,
            valueRank=-1,
        )
    )
    constraints: MTConstraintType | None
    coordinateSystem: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2856",
            browseName="ns=mt_connect;CoordinateSystem",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=mt_connect_datypes.MTCoordinateSystemType,
            valueRank=-1,
        )
    )
    duration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=3672",
            browseName="ns=mt_connect;Duration",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
        )
    )
    initialValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2857",
            browseName="ns=mt_connect;InitialValue",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=o6.Double,
            valueRank=-1,
        )
    )
    mTSubTypeName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2843",
            browseName="ns=mt_connect;MTSubTypeName",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    mTTypeName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2842",
            browseName="ns=mt_connect;MTTypeName",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    minimumDeltaFilter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2860",
            browseName="ns=mt_connect;MinimumDeltaFilter",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=o6.Float,
            valueRank=-1,
        )
    )
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2840",
            browseName="ns=mt_connect;Name",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    nativeUnits: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2855",
            browseName="ns=mt_connect;NativeUnits",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    periodFilter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2847",
            browseName="ns=mt_connect;PeriodFilter",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.Float,
            valueRank=-1,
        )
    )
    representation: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2846",
            browseName="ns=mt_connect;Representation",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=mt_connect_datypes.MTRepresentationType,
            valueRank=-1,
        )
    )
    resetTrigger: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2858",
            browseName="ns=mt_connect;ResetTrigger",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=mt_connect_datypes.MTResetTriggerType,
            valueRank=-1,
        )
    )
    resetTriggeredReason: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=3676",
            browseName="ns=mt_connect;ResetTriggeredReason",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=mt_connect_datypes.MTResetTriggerType,
            valueRank=-1,
        )
    )
    sampleRate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2845",
            browseName="ns=mt_connect;SampleRate",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.Double,
            valueRank=-1,
        )
    )
    significantDigits: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2853",
            browseName="ns=mt_connect;SignificantDigits",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=o6.Int16,
            valueRank=-1,
        )
    )
    sourceData: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2844",
            browseName="ns=mt_connect;SourceData",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    statistic: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2854",
            browseName="ns=mt_connect;Statistic",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=mt_connect_datypes.MTStatisticType,
            valueRank=-1,
        )
    )
    units: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2859",
            browseName="ns=mt_connect;Units",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    xmlId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2839",
            browseName="ns=mt_connect;XmlId",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )


@o6.variabletype(
    nodeId="ns=mt_connect;i=2641",
    browseName="ns=mt_connect;MTThreeSpaceSampleType",
    displayName="MTThreeSpaceSampleType",
    description="A special data item type that represents a three space coordinate. It uses\n      a data type with three fields, X, Y, and Z, where the coordinates are\n      given in millimeters. The EngineeringUnits will always be set to MMT in\n      the UNECE convetion.",
    dataType=mt_connect_datypes.ThreeSpaceSampleDataType,
    valueRank=o6.ValueRank.SCALAR,
)
class MTThreeSpaceSampleType(ns0.vartypes.DataItemType):
    category: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2883",
            browseName="ns=mt_connect;Category",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=mt_connect_datypes.MTCategoryType,
            valueRank=-1,
        )
    )
    constraints: MTConstraintType | None
    coordinateSystem: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2898",
            browseName="ns=mt_connect;CoordinateSystem",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=mt_connect_datypes.MTCoordinateSystemType,
            valueRank=-1,
        )
    )
    duration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=3673",
            browseName="ns=mt_connect;Duration",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=ns0.datatypes.Duration,
            valueRank=-1,
        )
    )
    engineeringUnits: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2642",
            browseName="ns=mt_connect;EngineeringUnits",
            description="A special data item type that represents a three space coordinate. It uses\n      a data type with three fields, X, Y, and Z, where the coordinates are\n      given in millimeters. The EngineeringUnits will always be set to MMT in\n      the UNECE convetion.",
            dataType=ns0.datatypes.EUInformation,
            valueRank=-1,
        )
    )
    initialValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2899",
            browseName="ns=mt_connect;InitialValue",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=o6.Double,
            valueRank=-1,
        )
    )
    mTSubTypeName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2885",
            browseName="ns=mt_connect;MTSubTypeName",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    mTTypeName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2884",
            browseName="ns=mt_connect;MTTypeName",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    minimumDeltaFilter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2902",
            browseName="ns=mt_connect;MinimumDeltaFilter",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=o6.Float,
            valueRank=-1,
        )
    )
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2882",
            browseName="ns=mt_connect;Name",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    nativeUnits: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2897",
            browseName="ns=mt_connect;NativeUnits",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    periodFilter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2889",
            browseName="ns=mt_connect;PeriodFilter",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.Float,
            valueRank=-1,
        )
    )
    representation: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2888",
            browseName="ns=mt_connect;Representation",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=mt_connect_datypes.MTRepresentationType,
            valueRank=-1,
        )
    )
    resetTrigger: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2900",
            browseName="ns=mt_connect;ResetTrigger",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=mt_connect_datypes.MTResetTriggerType,
            valueRank=-1,
        )
    )
    resetTriggeredReason: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=3677",
            browseName="ns=mt_connect;ResetTriggeredReason",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=mt_connect_datypes.MTResetTriggerType,
            valueRank=-1,
        )
    )
    sampleRate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2887",
            browseName="ns=mt_connect;SampleRate",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.Double,
            valueRank=-1,
        )
    )
    significantDigits: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2895",
            browseName="ns=mt_connect;SignificantDigits",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=o6.Int16,
            valueRank=-1,
        )
    )
    sourceData: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2886",
            browseName="ns=mt_connect;SourceData",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    statistic: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2896",
            browseName="ns=mt_connect;Statistic",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=mt_connect_datypes.MTStatisticType,
            valueRank=-1,
        )
    )
    units: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2901",
            browseName="ns=mt_connect;Units",
            description="These are the additional attributes that are relevent to numeric data\n      items. The factory will evaluate these values and will set the engineering\n      units and the range associated with the parent entity.",
            dataType=o6.String,
            valueRank=-1,
        )
    )
    xmlId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=mt_connect;i=2881",
            browseName="ns=mt_connect;XmlId",
            description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
            dataType=o6.String,
            valueRank=-1,
        )
    )


del Any, TYPE_CHECKING, uuid, o6, ns0, mt_connect_reftypes, mt_connect_datypes
