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
from . import vartypes as mt_connect_vartypes
from . import objtypes as mt_connect_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

mt_connect_objtypes.MTDescriptionType(
    nodeId="ns=mt_connect;i=2028",
    browseName="ns=mt_connect;Description",
    description="The base \\gls{MTComponent} Type from which all MTConnect Components are\n      derived. The component types will be created once for all\n      \\gls{MTComponent} \\glspl{Object} of that type based on the \\gls{QName} of\n      the MTConnect XML element. The Component Objects will be created and\n      inserted into the \\mtmodel{Components} folder with a \\gls{BrowseName} of\n      the Component \\gls{QName} and the \\mtmodel{name} element if specified\n      surrounded by square brackets, \\texttt{[]}. For example if the MTConnect\n      Element is: \\xml{<Linear name='X'>...</...>} The OPC\n      UA Object with \\gls{BrowseName} \\xml{Linear[X]} will be created with the\n      \\uamodel{HasTypeDefinition} referencing the \\mtmodel{Linear} OPC UA\n      \\gls{Type}. The meta data for the component and its relationships are\n      static. The dynamic data will be represented using the \\cite{UAPart8}. An\n      abstract XML element. Replaced in the XML document by types of component\n      elements representing physical parts and logical functions of a piece of\n      equipment.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2737",
                browseName="ns=mt_connect;Station",
                description="An MTConnect Component Description. See the DescriptionType in the\n      type-specifications. An XML element that can contain any descriptive\n      content.",
                dataType=o6.String,
                valueRank=-1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2738",
                browseName="ns=mt_connect;SerialNumber",
                description="An MTConnect Component Description. See the DescriptionType in the\n      type-specifications. An XML element that can contain any descriptive\n      content.",
                dataType=o6.String,
                valueRank=-1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2739",
                browseName="ns=mt_connect;Manufacturer",
                description="An MTConnect Component Description. See the DescriptionType in the\n      type-specifications. An XML element that can contain any descriptive\n      content.",
                dataType=o6.String,
                valueRank=-1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2740",
                browseName="ns=mt_connect;Data",
                description="An MTConnect Component Description. See the DescriptionType in the\n      type-specifications. An XML element that can contain any descriptive\n      content.",
                dataType=o6.String,
                valueRank=-1,
            )
        ),
    ],
)
o6.reference(mt_connect_objtypes.MTComponentType, ns0.reftypes.HasComponent, o6.ns["ns=mt_connect;i=2028"])
ns0.objtypes.DataTypeEncodingType(
    nodeId="ns=mt_connect;i=2745",
    browseName="Default Binary",
    description="A special \\gls{Variable} data type for asset change with a\n      \\mtmodel{AssetType} and \\mtmodel{AssetId}.",
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=2746",
    browseName="ns=mt_connect;AssetEventDataType",
    description="A special \\gls{Variable} data type for asset change with a\n      \\mtmodel{AssetType} and \\mtmodel{AssetId}.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2747",
                browseName="ns=mt_connect;DictionaryFragment",
                description="A special \\gls{Variable} data type for asset change with a\n      \\mtmodel{AssetType} and \\mtmodel{AssetId}.",
                dataType=o6.ByteString,
                value=b"<opc:StructuredType Name='AssetEventDataType' BaseType='ua:ExtensionObject'>\n  <opc:Documentation>The encoding for AssetEventDataType</opc:Documentation>\n  <opc:Field Name='AssetId' TypeName='opc:String'/>\n  <opc:Field Name='AssetType' TypeName='opc:String'/>\n</opc:StructuredType>",
            )
        )
    ],
    dataType=o6.String,
    value="AssetEventDataType",
)
o6.reference(o6.ns["ns=mt_connect;i=2745"], "i=39", o6.ns["ns=mt_connect;i=2746"])
ns0.objtypes.DataTypeEncodingType(
    nodeId="ns=mt_connect;i=2748",
    browseName="Default XML",
    description="A special \\gls{Variable} data type for asset change with a\n      \\mtmodel{AssetType} and \\mtmodel{AssetId}.",
)
o6.hasEncoding(mt_connect_datypes.AssetEventDataType, o6.ns["ns=mt_connect;i=2748"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=2749",
    browseName="ns=mt_connect;AssetEventDataType",
    description="A special \\gls{Variable} data type for asset change with a\n      \\mtmodel{AssetType} and \\mtmodel{AssetId}.",
    dataType=o6.String,
    value="//xs:element[@name='AssetEventDataType']",
)
o6.reference(o6.ns["ns=mt_connect;i=2748"], "i=39", o6.ns["ns=mt_connect;i=2749"])
ns0.objtypes.DataTypeEncodingType(
    nodeId="ns=mt_connect;i=2750",
    browseName="Default JSON",
    description="A special \\gls{Variable} data type for asset change with a\n      \\mtmodel{AssetType} and \\mtmodel{AssetId}.",
)
o6.hasEncoding(mt_connect_datypes.AssetEventDataType, o6.ns["ns=mt_connect;i=2750"])
mt_connect_objtypes.MTConstraintType(
    nodeId="ns=mt_connect;i=2760",
    browseName="ns=mt_connect;Constraints",
    description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2761",
                browseName="ns=mt_connect;Values",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.String,
                valueRank=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2762",
                browseName="ns=mt_connect;Minimum",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2763",
                browseName="ns=mt_connect;Maximum",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2764",
                browseName="ns=mt_connect;Nominal",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
    ],
)
o6.reference(mt_connect_vartypes.MTAssetEventType, ns0.reftypes.HasComponent, o6.ns["ns=mt_connect;i=2760"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=2765",
    browseName="ns=mt_connect;EnumStrings",
    description="Represents the \\gls{category} attribute of the MTConnect \\gls{MTDataItem}.",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2634",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("EVENT", "en"), o6.LocalizedText("CONDITION", "en"), o6.LocalizedText("SAMPLE", "en")],
)
ns0.objtypes.DataTypeEncodingType(
    nodeId="ns=mt_connect;i=2769", browseName="Default XML", description="Represents the \\gls{category} attribute of the MTConnect \\gls{MTDataItem}."
)
o6.hasEncoding(mt_connect_datypes.MTCategoryType, o6.ns["ns=mt_connect;i=2769"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=2770",
    browseName="ns=mt_connect;MTCategoryType",
    description="Represents the \\gls{category} attribute of the MTConnect \\gls{MTDataItem}.",
    dataType=o6.String,
    value="//xs:element[@name='MTCategoryType']",
)
o6.reference(o6.ns["ns=mt_connect;i=2769"], "i=39", o6.ns["ns=mt_connect;i=2770"])
mt_connect_objtypes.MTConstraintType(
    nodeId="ns=mt_connect;i=2780",
    browseName="ns=mt_connect;Constraints",
    description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2781",
                browseName="ns=mt_connect;Values",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.String,
                valueRank=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2782",
                browseName="ns=mt_connect;Minimum",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2783",
                browseName="ns=mt_connect;Maximum",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2784",
                browseName="ns=mt_connect;Nominal",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
    ],
)
o6.reference(mt_connect_vartypes.MTControlledVocabEventType, ns0.reftypes.HasComponent, o6.ns["ns=mt_connect;i=2780"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=2785",
    browseName="ns=mt_connect;EnumStrings",
    description="Represents the \\mtmodel{coordinateSystem} attribute of the MTConnect\n      \\gls{MTDataItem}. It is a reference system that associates a unique set of\n      n parameters with each point in an n-dimensional space. Ref: ISO\n      10303-218:2004",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2635",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("MACHINE", "en"), o6.LocalizedText("WORK", "en")],
)
ns0.objtypes.DataTypeEncodingType(
    nodeId="ns=mt_connect;i=2789",
    browseName="Default XML",
    description="Represents the \\mtmodel{coordinateSystem} attribute of the MTConnect\n      \\gls{MTDataItem}. It is a reference system that associates a unique set of\n      n parameters with each point in an n-dimensional space. Ref: ISO\n      10303-218:2004",
)
o6.hasEncoding(mt_connect_datypes.MTCoordinateSystemType, o6.ns["ns=mt_connect;i=2789"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=2790",
    browseName="ns=mt_connect;MTCoordinateSystemType",
    description="Represents the \\mtmodel{coordinateSystem} attribute of the MTConnect\n      \\gls{MTDataItem}. It is a reference system that associates a unique set of\n      n parameters with each point in an n-dimensional space. Ref: ISO\n      10303-218:2004",
    dataType=o6.String,
    value="//xs:element[@name='MTCoordinateSystemType']",
)
o6.reference(o6.ns["ns=mt_connect;i=2789"], "i=39", o6.ns["ns=mt_connect;i=2790"])
mt_connect_objtypes.MTConstraintType(
    nodeId="ns=mt_connect;i=2800",
    browseName="ns=mt_connect;Constraints",
    description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2801",
                browseName="ns=mt_connect;Values",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.String,
                valueRank=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2802",
                browseName="ns=mt_connect;Minimum",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2803",
                browseName="ns=mt_connect;Maximum",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2804",
                browseName="ns=mt_connect;Nominal",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
    ],
)
o6.reference(mt_connect_vartypes.MTMessageType, ns0.reftypes.HasComponent, o6.ns["ns=mt_connect;i=2800"])
mt_connect_objtypes.MTConstraintType(
    nodeId="ns=mt_connect;i=2814",
    browseName="ns=mt_connect;Constraints",
    description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2815",
                browseName="ns=mt_connect;Values",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.String,
                valueRank=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2816",
                browseName="ns=mt_connect;Minimum",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2817",
                browseName="ns=mt_connect;Maximum",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2818",
                browseName="ns=mt_connect;Nominal",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
    ],
)
o6.reference(mt_connect_vartypes.MTNumericEventType, ns0.reftypes.HasComponent, o6.ns["ns=mt_connect;i=2814"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=2827",
    browseName="ns=mt_connect;EnumStrings",
    description="Represents the \\mtmodel{representation} attribute of the MTConnect\n      \\gls{MTDataItem}.",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2633",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("DISCRETE", "en"), o6.LocalizedText("TIME_SERIES", "en"), o6.LocalizedText("VALUE", "en")],
)
ns0.objtypes.DataTypeEncodingType(
    nodeId="ns=mt_connect;i=2831", browseName="Default XML", description="Represents the \\mtmodel{representation} attribute of the MTConnect\n      \\gls{MTDataItem}."
)
o6.hasEncoding(mt_connect_datypes.MTRepresentationType, o6.ns["ns=mt_connect;i=2831"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=2832",
    browseName="ns=mt_connect;MTRepresentationType",
    description="Represents the \\mtmodel{representation} attribute of the MTConnect\n      \\gls{MTDataItem}.",
    dataType=o6.String,
    value="//xs:element[@name='MTRepresentationType']",
)
o6.reference(o6.ns["ns=mt_connect;i=2831"], "i=39", o6.ns["ns=mt_connect;i=2832"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=2833",
    browseName="ns=mt_connect;EnumStrings",
    description="These need to become \\uamodel{Good_} status code in OPC UA. resettrigger\n      is an optional XML element that identifies the type of event that may\n      cause a reset to occur. It is additional information regarding the meaning\n      of the data that establishes an understanding of the time frame that the\n      data represents so that the data may be correctly understood by a client\n      software application.",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2636",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[9],
    value=[
        o6.LocalizedText("ACTION_COMPLETE", "en"),
        o6.LocalizedText("ANNUAL", "en"),
        o6.LocalizedText("DAY", "en"),
        o6.LocalizedText("MAINTENANCE", "en"),
        o6.LocalizedText("MANUAL", "en"),
        o6.LocalizedText("MONTH", "en"),
        o6.LocalizedText("POWER_ON", "en"),
        o6.LocalizedText("SHIFT", "en"),
        o6.LocalizedText("WEEK", "en"),
    ],
)
ns0.objtypes.DataTypeEncodingType(
    nodeId="ns=mt_connect;i=2837",
    browseName="Default XML",
    description="These need to become \\uamodel{Good_} status code in OPC UA. resettrigger\n      is an optional XML element that identifies the type of event that may\n      cause a reset to occur. It is additional information regarding the meaning\n      of the data that establishes an understanding of the time frame that the\n      data represents so that the data may be correctly understood by a client\n      software application.",
)
o6.hasEncoding(mt_connect_datypes.MTResetTriggerType, o6.ns["ns=mt_connect;i=2837"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=2838",
    browseName="ns=mt_connect;MTResetTriggerType",
    description="These need to become \\uamodel{Good_} status code in OPC UA. resettrigger\n      is an optional XML element that identifies the type of event that may\n      cause a reset to occur. It is additional information regarding the meaning\n      of the data that establishes an understanding of the time frame that the\n      data represents so that the data may be correctly understood by a client\n      software application.",
    dataType=o6.String,
    value="//xs:element[@name='MTResetTriggerType']",
)
o6.reference(o6.ns["ns=mt_connect;i=2837"], "i=39", o6.ns["ns=mt_connect;i=2838"])
mt_connect_objtypes.MTConstraintType(
    nodeId="ns=mt_connect;i=2848",
    browseName="ns=mt_connect;Constraints",
    description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2849",
                browseName="ns=mt_connect;Values",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.String,
                valueRank=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2850",
                browseName="ns=mt_connect;Minimum",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2851",
                browseName="ns=mt_connect;Maximum",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2852",
                browseName="ns=mt_connect;Nominal",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
    ],
)
o6.reference(mt_connect_vartypes.MTSampleType, ns0.reftypes.HasComponent, o6.ns["ns=mt_connect;i=2848"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=2861",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2659",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        o6.LocalizedText("AVERAGE", "en"),
        o6.LocalizedText("MAXIMUM", "en"),
        o6.LocalizedText("MEDIAN", "en"),
        o6.LocalizedText("MINIMUM", "en"),
        o6.LocalizedText("MODE", "en"),
        o6.LocalizedText("RANGE", "en"),
        o6.LocalizedText("ROOT_MEAN_SQUARE", "en"),
        o6.LocalizedText("STANDARD_DEVIATION", "en"),
    ],
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=2865", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.MTStatisticType, o6.ns["ns=mt_connect;i=2865"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=mt_connect;i=2866", browseName="ns=mt_connect;MTStatisticType", dataType=o6.String, value="//xs:element[@name='MTStatisticType']")
o6.reference(o6.ns["ns=mt_connect;i=2865"], "i=39", o6.ns["ns=mt_connect;i=2866"])
mt_connect_objtypes.MTConstraintType(
    nodeId="ns=mt_connect;i=2876",
    browseName="ns=mt_connect;Constraints",
    description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2877",
                browseName="ns=mt_connect;Values",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.String,
                valueRank=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2878",
                browseName="ns=mt_connect;Minimum",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2879",
                browseName="ns=mt_connect;Maximum",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2880",
                browseName="ns=mt_connect;Nominal",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
    ],
)
o6.reference(mt_connect_vartypes.MTStringEventType, ns0.reftypes.HasComponent, o6.ns["ns=mt_connect;i=2876"])
mt_connect_objtypes.MTConstraintType(
    nodeId="ns=mt_connect;i=2890",
    browseName="ns=mt_connect;Constraints",
    description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2891",
                browseName="ns=mt_connect;Values",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.String,
                valueRank=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2892",
                browseName="ns=mt_connect;Minimum",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2893",
                browseName="ns=mt_connect;Maximum",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2894",
                browseName="ns=mt_connect;Nominal",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
    ],
)
o6.reference(mt_connect_vartypes.MTThreeSpaceSampleType, ns0.reftypes.HasComponent, o6.ns["ns=mt_connect;i=2890"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=2903", browseName="Default Binary")
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=2904",
    browseName="ns=mt_connect;MessageDataType",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2905",
                browseName="ns=mt_connect;DictionaryFragment",
                dataType=o6.ByteString,
                value=b"<opc:StructuredType Name='MessageDataType' BaseType='ua:ExtensionObject'>\n  <opc:Documentation>The encoding for MessageDataType</opc:Documentation>\n  <opc:Field Name='NativeCode' TypeName='opc:String'/>\n  <opc:Field Name='Text' TypeName='opc:String'/>\n</opc:StructuredType>",
            )
        )
    ],
    dataType=o6.String,
    value="MessageDataType",
)
o6.reference(o6.ns["ns=mt_connect;i=2903"], "i=39", o6.ns["ns=mt_connect;i=2904"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=2906", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.MessageDataType, o6.ns["ns=mt_connect;i=2906"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=mt_connect;i=2907", browseName="ns=mt_connect;MessageDataType", dataType=o6.String, value="//xs:element[@name='MessageDataType']")
o6.reference(o6.ns["ns=mt_connect;i=2906"], "i=39", o6.ns["ns=mt_connect;i=2907"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=2908", browseName="Default JSON")
o6.hasEncoding(mt_connect_datypes.MessageDataType, o6.ns["ns=mt_connect;i=2908"])
ns0.objtypes.DataTypeEncodingType(
    nodeId="ns=mt_connect;i=2909",
    browseName="Default Binary",
    description="Represents a position in a three space coordinate system. The positions\n      must be given in millimeters.",
)
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=2910",
    browseName="ns=mt_connect;ThreeSpaceSampleDataType",
    description="Represents a position in a three space coordinate system. The positions\n      must be given in millimeters.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2911",
                browseName="ns=mt_connect;DictionaryFragment",
                description="Represents a position in a three space coordinate system. The positions\n      must be given in millimeters.",
                dataType=o6.ByteString,
                value=b"<opc:StructuredType Name='ThreeSpaceSampleDataType' BaseType='ua:ExtensionObject'>\n  <opc:Documentation>The encoding for ThreeSpaceSampleDataType</opc:Documentation>\n  <opc:Field Name='X' TypeName='opc:Double'/>\n  <opc:Field Name='Y' TypeName='opc:Double'/>\n  <opc:Field Name='Z' TypeName='opc:Double'/>\n</opc:StructuredType>",
            )
        )
    ],
    dataType=o6.String,
    value="ThreeSpaceSampleDataType",
)
o6.reference(o6.ns["ns=mt_connect;i=2909"], "i=39", o6.ns["ns=mt_connect;i=2910"])
opcDotUaDotMTConnect = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=mt_connect;i=2729",
    browseName="ns=mt_connect;Opc.Ua.MTConnect",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=mt_connect;i=2731", browseName="NamespaceUri", dataType=o6.String, valueRank=-1, value="http://opcfoundation.org/UA/MTConnect/v2/")
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=mt_connect;i=2732", browseName="Deprecated", dataType=o6.Boolean, valueRank=-1)
        ),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2746"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2904"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2910"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b"<?xml version='1.0' encoding='UTF-8'?>\n<opc:TypeDictionary DefaultByteOrder='LittleEndian' TargetNamespace='http://opcfoundation.org/UA/MTConnect/v2/' xmlns:opc='http://opcfoundation.org/BinarySchema/' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:ua='http://opcfoundation.org/UA/' xmlns:tns='http://opcfoundation.org/UA/'>\n  <opc:Import Namespace='http://opcfoundation.org/UA/' Location='Opc.Ua.BinarySchema.bsd'/>\n  <opc:StructuredType Name='AssetEventDataType' BaseType='ua:ExtensionObject'>\n    <opc:Documentation>The encoding for AssetEventDataType</opc:Documentation>\n    <opc:Field Name='AssetId' TypeName='opc:String'/>\n    <opc:Field Name='AssetType' TypeName='opc:String'/>\n  </opc:StructuredType>\n  <opc:EnumeratedType Name='MTCategoryType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='EVENT' Value='0'/>\n    <opc:EnumeratedValue Name='CONDITION' Value='1'/>\n    <opc:EnumeratedValue Name='SAMPLE' Value='2'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='MTCoordinateSystemType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='MACHINE' Value='0'/>\n    <opc:EnumeratedValue Name='WORK' Value='1'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='MTRepresentationType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='DISCRETE' Value='0'/>\n    <opc:EnumeratedValue Name='TIME_SERIES' Value='1'/>\n    <opc:EnumeratedValue Name='VALUE' Value='2'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='MTResetTriggerType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='ACTION_COMPLETE' Value='0'/>\n    <opc:EnumeratedValue Name='ANNUAL' Value='1'/>\n    <opc:EnumeratedValue Name='DAY' Value='2'/>\n    <opc:EnumeratedValue Name='MAINTENANCE' Value='3'/>\n    <opc:EnumeratedValue Name='MANUAL' Value='4'/>\n    <opc:EnumeratedValue Name='MONTH' Value='5'/>\n    <opc:EnumeratedValue Name='POWER_ON' Value='6'/>\n    <opc:EnumeratedValue Name='SHIFT' Value='7'/>\n    <opc:EnumeratedValue Name='WEEK' Value='8'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='MTStatisticType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='AVERAGE' Value='0'/>\n    <opc:EnumeratedValue Name='MAXIMUM' Value='1'/>\n    <opc:EnumeratedValue Name='MEDIAN' Value='2'/>\n    <opc:EnumeratedValue Name='MINIMUM' Value='3'/>\n    <opc:EnumeratedValue Name='MODE' Value='4'/>\n    <opc:EnumeratedValue Name='RANGE' Value='5'/>\n    <opc:EnumeratedValue Name='ROOT_MEAN_SQUARE' Value='6'/>\n    <opc:EnumeratedValue Name='STANDARD_DEVIATION' Value='7'/>\n  </opc:EnumeratedType>\n  <opc:StructuredType Name='MessageDataType' BaseType='ua:ExtensionObject'>\n    <opc:Documentation>The encoding for MessageDataType</opc:Documentation>\n    <opc:Field Name='NativeCode' TypeName='opc:String'/>\n    <opc:Field Name='Text' TypeName='opc:String'/>\n  </opc:StructuredType>\n  <opc:StructuredType Name='ThreeSpaceSampleDataType' BaseType='ua:ExtensionObject'>\n    <opc:Documentation>The encoding for ThreeSpaceSampleDataType</opc:Documentation>\n    <opc:Field Name='X' TypeName='opc:Double'/>\n    <opc:Field Name='Y' TypeName='opc:Double'/>\n    <opc:Field Name='Z' TypeName='opc:Double'/>\n  </opc:StructuredType>\n  <opc:EnumeratedType Name='MTSeverityDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='FAULT' Value='0'/>\n    <opc:EnumeratedValue Name='NORMAL' Value='1'/>\n    <opc:EnumeratedValue Name='WARNING' Value='2'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='QualifierDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='HIGH' Value='0'/>\n    <opc:EnumeratedValue Name='LOW' Value='1'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='ActiveStateDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='ACTIVE' Value='0'/>\n    <opc:EnumeratedValue Name='INACTIVE' Value='1'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='AvailabilityDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='AVAILABLE' Value='0'/>\n    <opc:EnumeratedValue Name='UNAVAILABLE' Value='1'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='AxisCouplingDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='MASTER' Value='0'/>\n    <opc:EnumeratedValue Name='SLAVE' Value='1'/>\n    <opc:EnumeratedValue Name='SYNCHRONOUS' Value='2'/>\n    <opc:EnumeratedValue Name='TANDEM' Value='3'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='AxisStateDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='HOME' Value='0'/>\n    <opc:EnumeratedValue Name='PARKED' Value='1'/>\n    <opc:EnumeratedValue Name='STOPPED' Value='2'/>\n    <opc:EnumeratedValue Name='TRAVEL' Value='3'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='CompositionStateDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='ACTIVE' Value='0'/>\n    <opc:EnumeratedValue Name='CLOSED' Value='1'/>\n    <opc:EnumeratedValue Name='DOWN' Value='2'/>\n    <opc:EnumeratedValue Name='INACTIVE' Value='3'/>\n    <opc:EnumeratedValue Name='LEFT' Value='4'/>\n    <opc:EnumeratedValue Name='OFF' Value='5'/>\n    <opc:EnumeratedValue Name='ON' Value='6'/>\n    <opc:EnumeratedValue Name='OPEN' Value='7'/>\n    <opc:EnumeratedValue Name='RIGHT' Value='8'/>\n    <opc:EnumeratedValue Name='TRANSITIONING' Value='9'/>\n    <opc:EnumeratedValue Name='UNLATCHED' Value='10'/>\n    <opc:EnumeratedValue Name='UP' Value='11'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='ControllerModeDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='AUTOMATIC' Value='0'/>\n    <opc:EnumeratedValue Name='EDIT' Value='1'/>\n    <opc:EnumeratedValue Name='MANUAL' Value='2'/>\n    <opc:EnumeratedValue Name='MANUAL_DATA_INPUT' Value='3'/>\n    <opc:EnumeratedValue Name='SEMI_AUTOMATIC' Value='4'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='DirectionDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='CLOCKWISE' Value='0'/>\n    <opc:EnumeratedValue Name='COUNTER_CLOCKWISE' Value='1'/>\n    <opc:EnumeratedValue Name='NEGATIVE' Value='2'/>\n    <opc:EnumeratedValue Name='POSITIVE' Value='3'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='EmergencyStopDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='ARMED' Value='0'/>\n    <opc:EnumeratedValue Name='TRIGGERED' Value='1'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='ExecutionDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='ACTIVE' Value='0'/>\n    <opc:EnumeratedValue Name='FEED_HOLD' Value='1'/>\n    <opc:EnumeratedValue Name='INTERRUPTED' Value='2'/>\n    <opc:EnumeratedValue Name='OPTIONAL_STOP' Value='3'/>\n    <opc:EnumeratedValue Name='READY' Value='4'/>\n    <opc:EnumeratedValue Name='PROGRAM_COMPLETED' Value='5'/>\n    <opc:EnumeratedValue Name='PROGRAM_STOPPED' Value='6'/>\n    <opc:EnumeratedValue Name='STOPPED' Value='7'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='FunctionalModeDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='MAINTENANCE' Value='0'/>\n    <opc:EnumeratedValue Name='PRODUCTION' Value='1'/>\n    <opc:EnumeratedValue Name='PROCESS_DEVELOPMENT' Value='2'/>\n    <opc:EnumeratedValue Name='SETUP' Value='3'/>\n    <opc:EnumeratedValue Name='TEARDOWN' Value='4'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='InterfaceStateDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='ACTIVE' Value='0'/>\n    <opc:EnumeratedValue Name='COMPLETE' Value='1'/>\n    <opc:EnumeratedValue Name='FAIL' Value='2'/>\n    <opc:EnumeratedValue Name='NOT_READY' Value='4'/>\n    <opc:EnumeratedValue Name='READY' Value='5'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='InterfaceStatusDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='DISABLED' Value='0'/>\n    <opc:EnumeratedValue Name='ENABLED' Value='1'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='OnOffDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='OFF' Value='0'/>\n    <opc:EnumeratedValue Name='ON' Value='1'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='OpenStateDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='CLOSED' Value='0'/>\n    <opc:EnumeratedValue Name='OPEN' Value='1'/>\n    <opc:EnumeratedValue Name='UNLATCHED' Value='2'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='PathModeDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='INDEPENDENT' Value='0'/>\n    <opc:EnumeratedValue Name='MASTER' Value='1'/>\n    <opc:EnumeratedValue Name='MIRROR' Value='2'/>\n    <opc:EnumeratedValue Name='SYNCHRONOUS' Value='3'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='ProgramEditDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='ACTIVE' Value='0'/>\n    <opc:EnumeratedValue Name='NOT_READY' Value='1'/>\n    <opc:EnumeratedValue Name='READY' Value='2'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='RotaryModeDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='CONTOUR' Value='0'/>\n    <opc:EnumeratedValue Name='INDEX' Value='1'/>\n    <opc:EnumeratedValue Name='SPINDLE' Value='2'/>\n  </opc:EnumeratedType>\n  <opc:EnumeratedType Name='YesNoDataType' LengthInBits='32' BaseType='ua:ExtensionObject'>\n    <opc:EnumeratedValue Name='NO' Value='0'/>\n    <opc:EnumeratedValue Name='YES' Value='1'/>\n  </opc:EnumeratedType>\n</opc:TypeDictionary>",
)
ns0.objtypes.DataTypeEncodingType(
    nodeId="ns=mt_connect;i=2912",
    browseName="Default XML",
    description="Represents a position in a three space coordinate system. The positions\n      must be given in millimeters.",
)
o6.hasEncoding(mt_connect_datypes.ThreeSpaceSampleDataType, o6.ns["ns=mt_connect;i=2912"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=2913",
    browseName="ns=mt_connect;ThreeSpaceSampleDataType",
    description="Represents a position in a three space coordinate system. The positions\n      must be given in millimeters.",
    dataType=o6.String,
    value="//xs:element[@name='ThreeSpaceSampleDataType']",
)
o6.reference(o6.ns["ns=mt_connect;i=2912"], "i=39", o6.ns["ns=mt_connect;i=2913"])
ns0.objtypes.DataTypeEncodingType(
    nodeId="ns=mt_connect;i=2914",
    browseName="Default JSON",
    description="Represents a position in a three space coordinate system. The positions\n      must be given in millimeters.",
)
o6.hasEncoding(mt_connect_datypes.ThreeSpaceSampleDataType, o6.ns["ns=mt_connect;i=2914"])
mt_connect_objtypes.MTConstraintType(
    nodeId="ns=mt_connect;i=2924",
    browseName="ns=mt_connect;Constraints",
    description="The data item mixin will inject the properties and the methods into the\n      related classes. This facility is similar to the Ruby module mixin or the\n      Scala traits. data entity describing a piece of information reported about\n      a piece of equipment.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2925",
                browseName="ns=mt_connect;Values",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.String,
                valueRank=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2926",
                browseName="ns=mt_connect;Minimum",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2927",
                browseName="ns=mt_connect;Maximum",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2928",
                browseName="ns=mt_connect;Nominal",
                description="The MTConnect constraints. The Values or the Minimum, Maximum, and Nominal\n      values should be provided. Multiple Values can be provided as an array as\n      a set of allowable values for this \\gls{MTDataItem}. A constraint is used\n      by a software application to evaluate the validity of the reported data.",
                dataType=o6.Float,
                valueRank=-1,
            )
        ),
    ],
)
o6.reference(mt_connect_objtypes.MTConditionType, ns0.reftypes.HasComponent, o6.ns["ns=mt_connect;i=2924"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=2937",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2669",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("FAULT", "en"), o6.LocalizedText("NORMAL", "en"), o6.LocalizedText("WARNING", "en")],
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=2941", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.MTSeverityDataType, o6.ns["ns=mt_connect;i=2941"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=2942", browseName="ns=mt_connect;MTSeverityDataType", dataType=o6.String, value="//xs:element[@name='MTSeverityDataType']"
)
o6.reference(o6.ns["ns=mt_connect;i=2941"], "i=39", o6.ns["ns=mt_connect;i=2942"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=2943",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2668",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("HIGH", "en"), o6.LocalizedText("LOW", "en")],
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=2947", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.QualifierDataType, o6.ns["ns=mt_connect;i=2947"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=2948", browseName="ns=mt_connect;QualifierDataType", dataType=o6.String, value="//xs:element[@name='QualifierDataType']"
)
o6.reference(o6.ns["ns=mt_connect;i=2947"], "i=39", o6.ns["ns=mt_connect;i=2948"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=2949",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2197",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("ACTIVE", "en"), o6.LocalizedText("INACTIVE", "en")],
)
o6.reference(mt_connect_objtypes.ActuatorStateClassType, "i=46", "ns=mt_connect;i=2949")
o6.reference(mt_connect_objtypes.AxisInterlockClassType, "i=46", "ns=mt_connect;i=2949")
o6.reference(mt_connect_objtypes.ChuckInterlockClassType, "i=46", "ns=mt_connect;i=2949")
o6.reference(mt_connect_objtypes.SpindleInterlockClassType, "i=46", "ns=mt_connect;i=2949")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=2953", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.ActiveStateDataType, o6.ns["ns=mt_connect;i=2953"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=2954", browseName="ns=mt_connect;ActiveStateDataType", dataType=o6.String, value="//xs:element[@name='ActiveStateDataType']"
)
o6.reference(o6.ns["ns=mt_connect;i=2953"], "i=39", o6.ns["ns=mt_connect;i=2954"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=2955",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2198",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("AVAILABLE", "en"), o6.LocalizedText("UNAVAILABLE", "en")],
)
o6.reference(mt_connect_objtypes.AvailabilityClassType, "i=46", "ns=mt_connect;i=2955")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=2959", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.AvailabilityDataType, o6.ns["ns=mt_connect;i=2959"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=2960", browseName="ns=mt_connect;AvailabilityDataType", dataType=o6.String, value="//xs:element[@name='AvailabilityDataType']"
)
o6.reference(o6.ns["ns=mt_connect;i=2959"], "i=39", o6.ns["ns=mt_connect;i=2960"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=2961",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2199",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("MASTER", "en"), o6.LocalizedText("SLAVE", "en"), o6.LocalizedText("SYNCHRONOUS", "en"), o6.LocalizedText("TANDEM", "en")],
)
o6.reference(mt_connect_objtypes.AxisCouplingClassType, "i=46", "ns=mt_connect;i=2961")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=2965", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.AxisCouplingDataType, o6.ns["ns=mt_connect;i=2965"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=2966", browseName="ns=mt_connect;AxisCouplingDataType", dataType=o6.String, value="//xs:element[@name='AxisCouplingDataType']"
)
o6.reference(o6.ns["ns=mt_connect;i=2965"], "i=39", o6.ns["ns=mt_connect;i=2966"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=2967",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2200",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("HOME", "en"), o6.LocalizedText("PARKED", "en"), o6.LocalizedText("STOPPED", "en"), o6.LocalizedText("TRAVEL", "en")],
)
o6.reference(mt_connect_objtypes.AxisStateClassType, "i=46", "ns=mt_connect;i=2967")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=2971", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.AxisStateDataType, o6.ns["ns=mt_connect;i=2971"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=2972", browseName="ns=mt_connect;AxisStateDataType", dataType=o6.String, value="//xs:element[@name='AxisStateDataType']"
)
o6.reference(o6.ns["ns=mt_connect;i=2971"], "i=39", o6.ns["ns=mt_connect;i=2972"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=2973",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2202",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[12],
    value=[
        o6.LocalizedText("ACTIVE", "en"),
        o6.LocalizedText("CLOSED", "en"),
        o6.LocalizedText("DOWN", "en"),
        o6.LocalizedText("INACTIVE", "en"),
        o6.LocalizedText("LEFT", "en"),
        o6.LocalizedText("OFF", "en"),
        o6.LocalizedText("ON", "en"),
        o6.LocalizedText("OPEN", "en"),
        o6.LocalizedText("RIGHT", "en"),
        o6.LocalizedText("TRANSITIONING", "en"),
        o6.LocalizedText("UNLATCHED", "en"),
        o6.LocalizedText("UP", "en"),
    ],
)
o6.reference(mt_connect_objtypes.CompositionStateClassType, "i=46", "ns=mt_connect;i=2973")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=2977", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.CompositionStateDataType, o6.ns["ns=mt_connect;i=2977"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=2978", browseName="ns=mt_connect;CompositionStateDataType", dataType=o6.String, value="//xs:element[@name='CompositionStateDataType']"
)
o6.reference(o6.ns["ns=mt_connect;i=2977"], "i=39", o6.ns["ns=mt_connect;i=2978"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=2979",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2203",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        o6.LocalizedText("AUTOMATIC", "en"),
        o6.LocalizedText("EDIT", "en"),
        o6.LocalizedText("MANUAL", "en"),
        o6.LocalizedText("MANUAL_DATA_INPUT", "en"),
        o6.LocalizedText("SEMI_AUTOMATIC", "en"),
    ],
)
o6.reference(mt_connect_objtypes.ControllerModeClassType, "i=46", "ns=mt_connect;i=2979")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=2983", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.ControllerModeDataType, o6.ns["ns=mt_connect;i=2983"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=2984", browseName="ns=mt_connect;ControllerModeDataType", dataType=o6.String, value="//xs:element[@name='ControllerModeDataType']"
)
o6.reference(o6.ns["ns=mt_connect;i=2983"], "i=39", o6.ns["ns=mt_connect;i=2984"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=2985",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2205",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("CLOCKWISE", "en"), o6.LocalizedText("COUNTER_CLOCKWISE", "en"), o6.LocalizedText("NEGATIVE", "en"), o6.LocalizedText("POSITIVE", "en")],
)
o6.reference(mt_connect_objtypes.DirectionClassType, "i=46", "ns=mt_connect;i=2985")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=2989", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.DirectionDataType, o6.ns["ns=mt_connect;i=2989"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=2990", browseName="ns=mt_connect;DirectionDataType", dataType=o6.String, value="//xs:element[@name='DirectionDataType']"
)
o6.reference(o6.ns["ns=mt_connect;i=2989"], "i=39", o6.ns["ns=mt_connect;i=2990"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=2991",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2207",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("ARMED", "en"), o6.LocalizedText("TRIGGERED", "en")],
)
o6.reference(mt_connect_objtypes.EmergencyStopClassType, "i=46", "ns=mt_connect;i=2991")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=2995", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.EmergencyStopDataType, o6.ns["ns=mt_connect;i=2995"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=2996", browseName="ns=mt_connect;EmergencyStopDataType", dataType=o6.String, value="//xs:element[@name='EmergencyStopDataType']"
)
o6.reference(o6.ns["ns=mt_connect;i=2995"], "i=39", o6.ns["ns=mt_connect;i=2996"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=2997",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2262",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        o6.LocalizedText("ACTIVE", "en"),
        o6.LocalizedText("FEED_HOLD", "en"),
        o6.LocalizedText("INTERRUPTED", "en"),
        o6.LocalizedText("OPTIONAL_STOP", "en"),
        o6.LocalizedText("READY", "en"),
        o6.LocalizedText("PROGRAM_COMPLETED", "en"),
        o6.LocalizedText("PROGRAM_STOPPED", "en"),
        o6.LocalizedText("STOPPED", "en"),
    ],
)
o6.reference(mt_connect_objtypes.ExecutionClassType, "i=46", "ns=mt_connect;i=2997")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=3001", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.ExecutionDataType, o6.ns["ns=mt_connect;i=3001"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=3002", browseName="ns=mt_connect;ExecutionDataType", dataType=o6.String, value="//xs:element[@name='ExecutionDataType']"
)
o6.reference(o6.ns["ns=mt_connect;i=3001"], "i=39", o6.ns["ns=mt_connect;i=3002"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=3003",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2208",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        o6.LocalizedText("MAINTENANCE", "en"),
        o6.LocalizedText("PRODUCTION", "en"),
        o6.LocalizedText("PROCESS_DEVELOPMENT", "en"),
        o6.LocalizedText("SETUP", "en"),
        o6.LocalizedText("TEARDOWN", "en"),
    ],
)
o6.reference(mt_connect_objtypes.FunctionalModeClassType, "i=46", "ns=mt_connect;i=3003")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=3007", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.FunctionalModeDataType, o6.ns["ns=mt_connect;i=3007"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=3008", browseName="ns=mt_connect;FunctionalModeDataType", dataType=o6.String, value="//xs:element[@name='FunctionalModeDataType']"
)
o6.reference(o6.ns["ns=mt_connect;i=3007"], "i=39", o6.ns["ns=mt_connect;i=3008"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=3009",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2234",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        o6.LocalizedText("ACTIVE", "en"),
        o6.LocalizedText("COMPLETE", "en"),
        o6.LocalizedText("FAIL", "en"),
        o6.LocalizedText("NOT_READY", "en"),
        o6.LocalizedText("READY", "en"),
    ],
)
o6.reference(mt_connect_objtypes.MaterialFeedClassType, "i=46", "ns=mt_connect;i=3009")
o6.reference(mt_connect_objtypes.MaterialChangeClassType, "i=46", "ns=mt_connect;i=3009")
o6.reference(mt_connect_objtypes.MaterialRetractClassType, "i=46", "ns=mt_connect;i=3009")
o6.reference(mt_connect_objtypes.MaterialLoadClassType, "i=46", "ns=mt_connect;i=3009")
o6.reference(mt_connect_objtypes.MaterialUnloadClassType, "i=46", "ns=mt_connect;i=3009")
o6.reference(mt_connect_objtypes.OpenDoorClassType, "i=46", "ns=mt_connect;i=3009")
o6.reference(mt_connect_objtypes.CloseDoorClassType, "i=46", "ns=mt_connect;i=3009")
o6.reference(mt_connect_objtypes.OpenChuckClassType, "i=46", "ns=mt_connect;i=3009")
o6.reference(mt_connect_objtypes.CloseChuckClassType, "i=46", "ns=mt_connect;i=3009")
o6.reference(mt_connect_objtypes.PartChangeClassType, "i=46", "ns=mt_connect;i=3009")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=3013", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.InterfaceStateDataType, o6.ns["ns=mt_connect;i=3013"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=3014", browseName="ns=mt_connect;InterfaceStateDataType", dataType=o6.String, value="//xs:element[@name='InterfaceStateDataType']"
)
o6.reference(o6.ns["ns=mt_connect;i=3013"], "i=39", o6.ns["ns=mt_connect;i=3014"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=3015",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2230",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("DISABLED", "en"), o6.LocalizedText("ENABLED", "en")],
)
o6.reference(mt_connect_objtypes.InterfaceStateClassType, "i=46", "ns=mt_connect;i=3015")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=3019", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.InterfaceStatusDataType, o6.ns["ns=mt_connect;i=3019"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=3020", browseName="ns=mt_connect;InterfaceStatusDataType", dataType=o6.String, value="//xs:element[@name='InterfaceStatusDataType']"
)
o6.reference(o6.ns["ns=mt_connect;i=3019"], "i=39", o6.ns["ns=mt_connect;i=3020"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=3021",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2204",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("OFF", "en"), o6.LocalizedText("ON", "en")],
)
o6.reference(mt_connect_objtypes.ControllerModeOverrideClassType, "i=46", "ns=mt_connect;i=3021")
o6.reference(mt_connect_objtypes.EquipmentModeClassType, "i=46", "ns=mt_connect;i=3021")
o6.reference(mt_connect_objtypes.PowerStateClassType, "i=46", "ns=mt_connect;i=3021")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=3025", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.OnOffDataType, o6.ns["ns=mt_connect;i=3025"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=mt_connect;i=3026", browseName="ns=mt_connect;OnOffDataType", dataType=o6.String, value="//xs:element[@name='OnOffDataType']")
o6.reference(o6.ns["ns=mt_connect;i=3025"], "i=39", o6.ns["ns=mt_connect;i=3026"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=3027",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2201",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("CLOSED", "en"), o6.LocalizedText("OPEN", "en"), o6.LocalizedText("UNLATCHED", "en")],
)
o6.reference(mt_connect_objtypes.ChuckStateClassType, "i=46", "ns=mt_connect;i=3027")
o6.reference(mt_connect_objtypes.DoorStateClassType, "i=46", "ns=mt_connect;i=3027")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=3031", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.OpenStateDataType, o6.ns["ns=mt_connect;i=3031"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=3032", browseName="ns=mt_connect;OpenStateDataType", dataType=o6.String, value="//xs:element[@name='OpenStateDataType']"
)
o6.reference(o6.ns["ns=mt_connect;i=3031"], "i=39", o6.ns["ns=mt_connect;i=3032"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=3033",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2209",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("INDEPENDENT", "en"), o6.LocalizedText("MASTER", "en"), o6.LocalizedText("MIRROR", "en"), o6.LocalizedText("SYNCHRONOUS", "en")],
)
o6.reference(mt_connect_objtypes.PathModeClassType, "i=46", "ns=mt_connect;i=3033")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=3037", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.PathModeDataType, o6.ns["ns=mt_connect;i=3037"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=mt_connect;i=3038", browseName="ns=mt_connect;PathModeDataType", dataType=o6.String, value="//xs:element[@name='PathModeDataType']")
o6.reference(o6.ns["ns=mt_connect;i=3037"], "i=39", o6.ns["ns=mt_connect;i=3038"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=3039",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2210",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("ACTIVE", "en"), o6.LocalizedText("NOT_READY", "en"), o6.LocalizedText("READY", "en")],
)
o6.reference(mt_connect_objtypes.ProgramEditClassType, "i=46", "ns=mt_connect;i=3039")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=3043", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.ProgramEditDataType, o6.ns["ns=mt_connect;i=3043"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=3044", browseName="ns=mt_connect;ProgramEditDataType", dataType=o6.String, value="//xs:element[@name='ProgramEditDataType']"
)
o6.reference(o6.ns["ns=mt_connect;i=3043"], "i=39", o6.ns["ns=mt_connect;i=3044"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=3045",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2211",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[3],
    value=[o6.LocalizedText("CONTOUR", "en"), o6.LocalizedText("INDEX", "en"), o6.LocalizedText("SPINDLE", "en")],
)
o6.reference(mt_connect_objtypes.RotaryModeClassType, "i=46", "ns=mt_connect;i=3045")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=3049", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.RotaryModeDataType, o6.ns["ns=mt_connect;i=3049"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=mt_connect;i=3050", browseName="ns=mt_connect;RotaryModeDataType", dataType=o6.String, value="//xs:element[@name='RotaryModeDataType']"
)
o6.reference(o6.ns["ns=mt_connect;i=3049"], "i=39", o6.ns["ns=mt_connect;i=3050"])
ns0.vartypes.PropertyType(
    nodeId="ns=mt_connect;i=3051",
    browseName="ns=mt_connect;EnumStrings",
    modellingRule="Mandatory",
    parent="ns=mt_connect;i=2206",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("NO", "en"), o6.LocalizedText("YES", "en")],
)
o6.reference(mt_connect_objtypes.EndOfBarClassType, "i=46", "ns=mt_connect;i=3051")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=mt_connect;i=3055", browseName="Default XML")
o6.hasEncoding(mt_connect_datypes.YesNoDataType, o6.ns["ns=mt_connect;i=3055"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=mt_connect;i=3056", browseName="ns=mt_connect;YesNoDataType", dataType=o6.String, value="//xs:element[@name='YesNoDataType']")
o6.reference(o6.ns["ns=mt_connect;i=3055"], "i=39", o6.ns["ns=mt_connect;i=3056"])
opcDotUaDotMTConnect_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=mt_connect;i=2733",
    browseName="ns=mt_connect;Opc.Ua.MTConnect",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=2735", browseName="NamespaceUri", dataType=o6.String, valueRank=-1, value="http://opcfoundation.org/UA/MTConnect/v2/Types.xsd"
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=mt_connect;i=2736", browseName="Deprecated", dataType=o6.Boolean, valueRank=-1)
        ),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2749"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2770"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2790"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2832"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2838"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2866"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2907"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2913"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2942"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2948"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2954"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2960"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2966"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2972"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2978"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2984"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2990"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=2996"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=3002"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=3008"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=3014"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=3020"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=3026"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=3032"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=3038"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=3044"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=3050"]),
        o6.hasComponent(o6.ns["ns=mt_connect;i=3056"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b"<?xml version='1.0' encoding='UTF-8'?>\n<xs:schema xmlns:xs='http://www.w3.org/2001/XMLSchema' xmlns:ua='http://opcfoundation.org/UA/2008/02/Types.xsd' xmlns:mtc='http://opcfoundation.org/UA/MTConnect/v2//Types.xsd' targetNamespace='http://opcfoundation.org/UA/MTConnect/v2//Types.xsd' elementFormDefault='qualified'>\n  <xs:import namespace='http://opcfoundation.org/UA/2008/02/Types.xsd'/>\n  <xs:complexType name='AssetEventDataTypeDataType'>\n    <xs:sequence>\n      <xs:element name='AssetId' type='xs:string' minOccurs='1' maxOccurs='1'/>\n      <xs:element name='AssetType' type='xs:string' minOccurs='1' maxOccurs='1'/>\n    </xs:sequence>\n  </xs:complexType>\n  <xs:element name='AssetEventDataType' type='mtc:AssetEventDataTypeDataType'/>\n  <xs:simpleType name='MTCategoryTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='EVENT'/>\n      <xs:enumeration value='CONDITION'/>\n      <xs:enumeration value='SAMPLE'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='MTCategoryType' type='mtc:MTCategoryTypeEnum'/>\n  <xs:simpleType name='MTCoordinateSystemTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='MACHINE'/>\n      <xs:enumeration value='WORK'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='MTCoordinateSystemType' type='mtc:MTCoordinateSystemTypeEnum'/>\n  <xs:simpleType name='MTRepresentationTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='DISCRETE'/>\n      <xs:enumeration value='TIME_SERIES'/>\n      <xs:enumeration value='VALUE'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='MTRepresentationType' type='mtc:MTRepresentationTypeEnum'/>\n  <xs:simpleType name='MTResetTriggerTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='ACTION_COMPLETE'/>\n      <xs:enumeration value='ANNUAL'/>\n      <xs:enumeration value='DAY'/>\n      <xs:enumeration value='MAINTENANCE'/>\n      <xs:enumeration value='MANUAL'/>\n      <xs:enumeration value='MONTH'/>\n      <xs:enumeration value='POWER_ON'/>\n      <xs:enumeration value='SHIFT'/>\n      <xs:enumeration value='WEEK'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='MTResetTriggerType' type='mtc:MTResetTriggerTypeEnum'/>\n  <xs:simpleType name='MTStatisticTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='AVERAGE'/>\n      <xs:enumeration value='MAXIMUM'/>\n      <xs:enumeration value='MEDIAN'/>\n      <xs:enumeration value='MINIMUM'/>\n      <xs:enumeration value='MODE'/>\n      <xs:enumeration value='RANGE'/>\n      <xs:enumeration value='ROOT_MEAN_SQUARE'/>\n      <xs:enumeration value='STANDARD_DEVIATION'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='MTStatisticType' type='mtc:MTStatisticTypeEnum'/>\n  <xs:complexType name='MessageDataTypeDataType'>\n    <xs:sequence>\n      <xs:element name='NativeCode' type='xs:string' minOccurs='1' maxOccurs='1'/>\n      <xs:element name='Text' type='xs:string' minOccurs='1' maxOccurs='1'/>\n    </xs:sequence>\n  </xs:complexType>\n  <xs:element name='MessageDataType' type='mtc:MessageDataTypeDataType'/>\n  <xs:complexType name='ThreeSpaceSampleDataTypeDataType'>\n    <xs:sequence>\n      <xs:element name='X' type='xs:float' minOccurs='1' maxOccurs='1'/>\n      <xs:element name='Y' type='xs:float' minOccurs='1' maxOccurs='1'/>\n      <xs:element name='Z' type='xs:float' minOccurs='1' maxOccurs='1'/>\n    </xs:sequence>\n  </xs:complexType>\n  <xs:element name='ThreeSpaceSampleDataType' type='mtc:ThreeSpaceSampleDataTypeDataType'/>\n  <xs:simpleType name='MTSeverityDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='FAULT'/>\n      <xs:enumeration value='NORMAL'/>\n      <xs:enumeration value='WARNING'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='MTSeverityDataType' type='mtc:MTSeverityDataTypeEnum'/>\n  <xs:simpleType name='QualifierDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='HIGH'/>\n      <xs:enumeration value='LOW'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='QualifierDataType' type='mtc:QualifierDataTypeEnum'/>\n  <xs:simpleType name='ActiveStateDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='ACTIVE'/>\n      <xs:enumeration value='INACTIVE'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='ActiveStateDataType' type='mtc:ActiveStateDataTypeEnum'/>\n  <xs:simpleType name='AvailabilityDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='AVAILABLE'/>\n      <xs:enumeration value='UNAVAILABLE'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='AvailabilityDataType' type='mtc:AvailabilityDataTypeEnum'/>\n  <xs:simpleType name='AxisCouplingDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='MASTER'/>\n      <xs:enumeration value='SLAVE'/>\n      <xs:enumeration value='SYNCHRONOUS'/>\n      <xs:enumeration value='TANDEM'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='AxisCouplingDataType' type='mtc:AxisCouplingDataTypeEnum'/>\n  <xs:simpleType name='AxisStateDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='HOME'/>\n      <xs:enumeration value='PARKED'/>\n      <xs:enumeration value='STOPPED'/>\n      <xs:enumeration value='TRAVEL'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='AxisStateDataType' type='mtc:AxisStateDataTypeEnum'/>\n  <xs:simpleType name='CompositionStateDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='ACTIVE'/>\n      <xs:enumeration value='CLOSED'/>\n      <xs:enumeration value='DOWN'/>\n      <xs:enumeration value='INACTIVE'/>\n      <xs:enumeration value='LEFT'/>\n      <xs:enumeration value='OFF'/>\n      <xs:enumeration value='ON'/>\n      <xs:enumeration value='OPEN'/>\n      <xs:enumeration value='RIGHT'/>\n      <xs:enumeration value='TRANSITIONING'/>\n      <xs:enumeration value='UNLATCHED'/>\n      <xs:enumeration value='UP'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='CompositionStateDataType' type='mtc:CompositionStateDataTypeEnum'/>\n  <xs:simpleType name='ControllerModeDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='AUTOMATIC'/>\n      <xs:enumeration value='EDIT'/>\n      <xs:enumeration value='MANUAL'/>\n      <xs:enumeration value='MANUAL_DATA_INPUT'/>\n      <xs:enumeration value='SEMI_AUTOMATIC'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='ControllerModeDataType' type='mtc:ControllerModeDataTypeEnum'/>\n  <xs:simpleType name='DirectionDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='CLOCKWISE'/>\n      <xs:enumeration value='COUNTER_CLOCKWISE'/>\n      <xs:enumeration value='NEGATIVE'/>\n      <xs:enumeration value='POSITIVE'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='DirectionDataType' type='mtc:DirectionDataTypeEnum'/>\n  <xs:simpleType name='EmergencyStopDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='ARMED'/>\n      <xs:enumeration value='TRIGGERED'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='EmergencyStopDataType' type='mtc:EmergencyStopDataTypeEnum'/>\n  <xs:simpleType name='ExecutionDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='ACTIVE'/>\n      <xs:enumeration value='FEED_HOLD'/>\n      <xs:enumeration value='INTERRUPTED'/>\n      <xs:enumeration value='OPTIONAL_STOP'/>\n      <xs:enumeration value='READY'/>\n      <xs:enumeration value='PROGRAM_COMPLETED'/>\n      <xs:enumeration value='PROGRAM_STOPPED'/>\n      <xs:enumeration value='STOPPED'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='ExecutionDataType' type='mtc:ExecutionDataTypeEnum'/>\n  <xs:simpleType name='FunctionalModeDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='MAINTENANCE'/>\n      <xs:enumeration value='PRODUCTION'/>\n      <xs:enumeration value='PROCESS_DEVELOPMENT'/>\n      <xs:enumeration value='SETUP'/>\n      <xs:enumeration value='TEARDOWN'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='FunctionalModeDataType' type='mtc:FunctionalModeDataTypeEnum'/>\n  <xs:simpleType name='InterfaceStateDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='ACTIVE'/>\n      <xs:enumeration value='COMPLETE'/>\n      <xs:enumeration value='FAIL'/>\n      <xs:enumeration value='NOT_READY'/>\n      <xs:enumeration value='READY'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='InterfaceStateDataType' type='mtc:InterfaceStateDataTypeEnum'/>\n  <xs:simpleType name='InterfaceStatusDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='DISABLED'/>\n      <xs:enumeration value='ENABLED'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='InterfaceStatusDataType' type='mtc:InterfaceStatusDataTypeEnum'/>\n  <xs:simpleType name='OnOffDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='OFF'/>\n      <xs:enumeration value='ON'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='OnOffDataType' type='mtc:OnOffDataTypeEnum'/>\n  <xs:simpleType name='OpenStateDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='CLOSED'/>\n      <xs:enumeration value='OPEN'/>\n      <xs:enumeration value='UNLATCHED'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='OpenStateDataType' type='mtc:OpenStateDataTypeEnum'/>\n  <xs:simpleType name='PathModeDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='INDEPENDENT'/>\n      <xs:enumeration value='MASTER'/>\n      <xs:enumeration value='MIRROR'/>\n      <xs:enumeration value='SYNCHRONOUS'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='PathModeDataType' type='mtc:PathModeDataTypeEnum'/>\n  <xs:simpleType name='ProgramEditDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='ACTIVE'/>\n      <xs:enumeration value='NOT_READY'/>\n      <xs:enumeration value='READY'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='ProgramEditDataType' type='mtc:ProgramEditDataTypeEnum'/>\n  <xs:simpleType name='RotaryModeDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='CONTOUR'/>\n      <xs:enumeration value='INDEX'/>\n      <xs:enumeration value='SPINDLE'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='RotaryModeDataType' type='mtc:RotaryModeDataTypeEnum'/>\n  <xs:simpleType name='YesNoDataTypeEnum'>\n    <xs:restriction base='xs:string'>\n      <xs:enumeration value='NO'/>\n      <xs:enumeration value='YES'/>\n    </xs:restriction>\n  </xs:simpleType>\n  <xs:element name='YesNoDataType' type='mtc:YesNoDataTypeEnum'/>\n</xs:schema>",
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMTConnectSlash2Dot0Slash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=mt_connect;i=3630",
    browseName="ns=mt_connect;http://opcfoundation.org/UA/MTConnect/2.0/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=3632", browseName="NamespaceUri", dataType=o6.String, valueRank=-1, value="http://opcfoundation.org/UA/MTConnect/2.0/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mt_connect;i=3633", browseName="NamespaceVersion", dataType=o6.String, valueRank=-1, value="2.00.01")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=3634", browseName="NamespacePublicationDate", dataType=o6.DateTime, valueRank=-1, value=o6.DateTime("2020-06-05T00:00:00Z")
            )
        ),
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=mt_connect;i=3635", browseName="IsNamespaceSubset", dataType=o6.Boolean, valueRank=-1)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=3636", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=mt_connect;i=3637", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["1:1073741824"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=mt_connect;i=3638", browseName="StaticStringNodeIdPattern", dataType=o6.String, valueRank=-1)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)


del Any, TYPE_CHECKING, uuid, o6, ns0, mt_connect_reftypes, mt_connect_datypes, mt_connect_vartypes, mt_connect_objtypes
