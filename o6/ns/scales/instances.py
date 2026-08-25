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

"""Generated OPC UA scales namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
import o6.ns.pack_ml as pack_ml
from . import reftypes as scales_reftypes
from . import datatypes as scales_datypes
from . import vartypes as scales_vartypes
from . import objtypes as scales_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=scales;i=88", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scales;i=89", browseName="Default XML")
o6.hasEncoding(scales_datypes.WeightType, o6.ns["ns=scales;i=89"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scales;i=90", browseName="Default JSON")
o6.hasEncoding(scales_datypes.WeightType, o6.ns["ns=scales;i=90"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scales;i=97", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scales;i=98", browseName="Default XML")
o6.hasEncoding(scales_datypes.PrintableWeightType, o6.ns["ns=scales;i=98"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scales;i=99", browseName="Default JSON")
o6.hasEncoding(scales_datypes.PrintableWeightType, o6.ns["ns=scales;i=99"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scales;i=100", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scales;i=101", browseName="Default XML")
o6.hasEncoding(scales_datypes.RecipeThresholdType, o6.ns["ns=scales;i=101"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scales;i=102", browseName="Default JSON")
o6.hasEncoding(scales_datypes.RecipeThresholdType, o6.ns["ns=scales;i=102"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scales;i=103", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scales;i=104", browseName="Default XML")
o6.hasEncoding(scales_datypes.RecipeTargetValueType, o6.ns["ns=scales;i=104"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scales;i=105", browseName="Default JSON")
o6.hasEncoding(scales_datypes.RecipeTargetValueType, o6.ns["ns=scales;i=105"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scales;i=106", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scales;i=107", browseName="Default XML")
o6.hasEncoding(scales_datypes.RecipeReportElementType, o6.ns["ns=scales;i=107"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scales;i=108", browseName="Default JSON")
o6.hasEncoding(scales_datypes.RecipeReportElementType, o6.ns["ns=scales;i=108"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scales;i=109", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scales;i=110", browseName="Default XML")
o6.hasEncoding(scales_datypes.AbstractWeightType, o6.ns["ns=scales;i=110"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=scales;i=111", browseName="Default JSON")
o6.hasEncoding(scales_datypes.AbstractWeightType, o6.ns["ns=scales;i=111"])
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=195",
    browseName="EnumStrings",
    parent="ns=scales;i=54",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("None_0"), o6.LocalizedText("MeasuredTare_1"), o6.LocalizedText("PresetTare_2"), o6.LocalizedText("ProportionalTare_3")],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=scales;i=134",
    browseName="ns=scales;NotificationId",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=233", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=244", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=ns0.datatypes.UInteger,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ScaleEventType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=134"])
scales_objtypes.MaterialType(
    nodeId="ns=scales;i=86",
    browseName="ns=scales;Material",
    description="Defines the material which needs to be measured. Each material has different characteristics that are defined in MaterialType.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=259",
                browseName="ns=scales;MaterialId",
                description="Defines a unique identifier for the material.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=260",
                browseName="ns=scales;MaterialName",
                description="Defines a user-readable name of the material.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(scales_objtypes.WeighingType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=86"])
scales_objtypes.StatisticCounterType(
    nodeId="ns=scales;i=115",
    browseName="ns=scales;ZoneStatistic",
    description="Contains statistics regarding this zone.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=232",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=320",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
o6.reference(scales_objtypes.ZoneType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=115"])
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=321",
    browseName="EnumStrings",
    parent="ns=scales;i=60",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("In_0"), o6.LocalizedText("Under_1"), o6.LocalizedText("Over_2"), o6.LocalizedText("UnderOrOver_3")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=322",
    browseName="EnumStrings",
    parent="ns=scales;i=61",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[6],
    value=[
        o6.LocalizedText("Equal_0"),
        o6.LocalizedText("NotEqual_1"),
        o6.LocalizedText("LessOrEqualThan_2"),
        o6.LocalizedText("GreaterOrEqualThan_3"),
        o6.LocalizedText("LessThan_4"),
        o6.LocalizedText("GreaterThan_5"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=323",
    browseName="EnumStrings",
    parent="ns=scales;i=62",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("Rising_0"), o6.LocalizedText("Falling_1")],
)
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=scales;i=325",
    browseName="ns=scales;NotificationCategory",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=326",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[8],
                value=[
                    ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("OTHERS")),
                    ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("PROCESS")),
                    ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("SYSTEM")),
                    ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("MEMORY")),
                    ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("COMPONENT")),
                    ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("COMMUNICATION")),
                    ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("WEIGHING_MODULE")),
                    ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("ENVIRONMENT")),
                ],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=327", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=ns0.datatypes.UInteger,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ScaleEventType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=325"])
scales_vartypes.MeasuredItemType(
    nodeId="ns=scales;i=329",
    browseName="ns=scales;TotalizedValue",
    description="Defines a summed up/totalized volume within a period of time.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=331", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=332", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=333",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
    ],
    dataType=scales_datypes.AbstractWeightType,
)
o6.reference(scales_objtypes.TotalizerType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=329"])
scales_vartypes.TargetItemType(
    nodeId="ns=scales;i=334",
    browseName="ns=scales;FeederSpeed",
    description="Defines the current speed of a feeder system. The unit of the FeederSpeed depends on the construction system.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=335", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=336", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
)
o6.reference(scales_objtypes.FeederModuleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=334"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=scales;i=328",
    browseName="ns=scales;NotificationCategory",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=330",
                browseName="EnumValues",
                dataType=ns0.datatypes.EnumValueType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText())],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=339", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=ns0.datatypes.UInteger,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ScaleAlarmType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=328"])
scales_vartypes.MeasuredItemType(
    nodeId="ns=scales;i=338",
    browseName="ns=scales;FeederLoad",
    description="Defines the current loaded weight on the feeder system.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=340", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=341", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=342",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
)
o6.reference(scales_objtypes.FeederModuleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=338"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=scales;i=343",
    browseName="ns=scales;LabelStock",
    description="Indicates the level of labels in stock in percent.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=344", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=ns0.datatypes.Number,
)
o6.reference(scales_objtypes.PrinterModuleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=343"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=scales;i=349",
    browseName="ns=scales;PrintMediaStock",
    description="Defines the level of the print media in percent (e.g. ink, wear of thermal element, etc)",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=350", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=ns0.datatypes.Number,
)
o6.reference(scales_objtypes.PrinterModuleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=349"])
ns0.vartypes.MultiStateValueDiscreteType(
    nodeId="ns=scales;i=353",
    browseName="ns=scales;NotificationId",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=358", browseName="EnumValues", dataType=ns0.datatypes.EnumValueType, valueRank=1, arrayDimensions=[0])),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=359", browseName="ValueAsText", dataType=o6.LocalizedText)),
    ],
    dataType=ns0.datatypes.UInteger,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ScaleAlarmType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=353"])
# WARNING: The source NodeSet value does not match the declared DataType.
# It is intentionally omitted; the server supplies a typed default.
ns0.vartypes.TwoStateDiscreteType(
    nodeId="ns=scales;i=360",
    browseName="ns=scales;ProductMode",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=361", browseName="FalseState", dataType=o6.LocalizedText, value=o6.LocalizedText("NotProcessing"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=362", browseName="TrueState", dataType=o6.LocalizedText, value=o6.LocalizedText("Processing"))),
    ],
    dataType=o6.Boolean,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=360"])
scales_vartypes.TargetItemType(
    nodeId="ns=scales;i=378",
    browseName="ns=scales;NominalWeight",
    description="Defines the nominal (printed) weight of the product.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=379", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=380", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.CheckweigherProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=378"])
scales_vartypes.MeasuredItemType(
    nodeId="ns=scales;i=390",
    browseName="ns=scales;TotalizedValue",
    description="Defines a summed up/totalized volume within a period of time.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=391", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=392", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=393",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
    ],
    dataType=scales_datypes.AbstractWeightType,
)
scales_objtypes.TotalizerType(
    nodeId="ns=scales;i=72",
    browseName="ns=scales;<Totalizer>",
    description="Defines the overall volume that was conveyed over a defined duration. Multiple object may be instantiated depending on the use case.",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=scales;i=390"])],
)
o6.reference(scales_objtypes.ContinuousScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=72"])
scales_vartypes.MeasuredItemType(
    nodeId="ns=scales;i=394",
    browseName="ns=scales;TotalizedValue",
    description="Defines a summed up/totalized volume within a period of time.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=395", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=396", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=397",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
    ],
    dataType=scales_datypes.AbstractWeightType,
)
scales_objtypes.TotalizerType(
    nodeId="ns=scales;i=73",
    browseName="ns=scales;MasterTotalizer",
    description="Defines the overall volume that was conveyed over the lifetime of the scale.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=scales;i=394"])],
)
o6.reference(scales_objtypes.ContinuousScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=73"])
scales_vartypes.TargetItemType(
    nodeId="ns=scales;i=294",
    browseName="ns=scales;TargetWeight",
    description="Defines the preset of the volume to be processed.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=295", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=296", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=411", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.WeighingType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=294"])
scales_objtypes.StatisticType(
    nodeId="ns=scales;i=95",
    browseName="ns=scales;Statistic",
    description="Contains the different statistic values of the product.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=444",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        )
    ],
)
o6.reference(scales_objtypes.ProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=95"])


ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=254",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=450",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="RecipeId", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="RecipeName", dataType=o6.LocalizedText, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=255",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=450",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RecipeNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=scales;i=450",
    browseName="ns=scales;AddRecipe",
    description="Method to add an additional recipe of RecipeType.",
    inputArgs=o6.hasProperty(o6.ns["ns=scales;i=254"]),
    outputArgs=o6.hasProperty(o6.ns["ns=scales;i=255"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=256",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=452",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RecipeId", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=452", browseName="ns=scales;RemoveRecipe", description="Method to remove a recipe of RecipeType.", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=256"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=440",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=467",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ElementType", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="ElementName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="PreviousElements", dataType=o6.NodeId, valueRank=1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=441",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=467",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ElementNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=467", browseName="ns=scales;AddRecipeElement", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=440"]), outputArgs=o6.hasProperty(o6.ns["ns=scales;i=441"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=442",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=468",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RecipeElementNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=468", browseName="ns=scales;RemoveRecipeElement", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=442"]))

scales_objtypes.RecipeType(
    nodeId="ns=scales;i=74",
    browseName="ns=scales;<Recipe_No>",
    displayName="Recipe",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=257",
                browseName="ns=scales;RecipeId",
                description="RecipeId defines a unique identifier of a recipe.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=258",
                browseName="ns=scales;RecipeName",
                description="Defines a user-readable name of the recipe.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=scales;i=83", browseName="ns=scales;RecipeElements", description="Defines a Placeholder for all RecipeElements that are part of the Recipe."
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=467"]),
        o6.hasComponent(o6.ns["ns=scales;i=468"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=443",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=469",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ElementType", dataType=o6.NodeId, valueRank=-1),
        ns0.datatypes.Argument(name="ElementName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="PreviousElements", dataType=o6.NodeId, valueRank=1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=445",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=469",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ElementNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=469", browseName="ns=scales;AddRecipeElement", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=443"]), outputArgs=o6.hasProperty(o6.ns["ns=scales;i=445"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=446",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=470",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RecipeElementNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=470", browseName="ns=scales;RemoveRecipeElement", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=446"]))

scales_objtypes.RecipeType(
    nodeId="ns=scales;i=112",
    browseName="ns=scales;<Recipe_No>",
    description="Defines an instance of a recipe with the number No.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=289",
                browseName="ns=scales;RecipeName",
                description="Defines a user-readable name of the recipe.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=290",
                browseName="ns=scales;RecipeId",
                description="RecipeId defines a unique identifier of a recipe.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=scales;i=84", browseName="ns=scales;RecipeElements", description="Defines a Placeholder for all RecipeElements that are part of the Recipe."
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=469"]),
        o6.hasComponent(o6.ns["ns=scales;i=470"]),
    ],
)
o6.reference(scales_objtypes.RecipeManagementType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=112"])
scales_vartypes.TargetItemType(
    nodeId="ns=scales;i=472",
    browseName="ns=scales;TargetThroughput",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=473", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=474", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.CatchweigherProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=472"])
scales_objtypes.StatisticType(
    nodeId="ns=scales;i=114",
    browseName="ns=scales;Statistic",
    description="Contains the different statistic values of the product.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=475",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        )
    ],
)
scales_vartypes.WeightItemType(
    nodeId="ns=scales;i=495",
    browseName="ns=scales;MeasuredWeight",
    description="Defines the registered weight that may be unmistakeable referenced to one item.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=496", browseName="ns=scales;CenterOfZero", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=497", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=498", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=499", browseName="ns=scales;GrossNegative", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=500", browseName="ns=scales;HighResolutionValue", dataType=scales_datypes.WeightType)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=501",
                browseName="ns=scales;InsideZero",
                description="Defines if the current measured value is within the valid range for the setting zero procedure. This is a necessary condition to success the setZero() method if available.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=503", browseName="ns=scales;Overload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=504", browseName="ns=scales;PrintableValue", dataType=scales_datypes.PrintableWeightType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=505", browseName="ns=scales;TareMode", dataType=scales_datypes.TareMode)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=506", browseName="ns=scales;Underload", dataType=o6.Boolean)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=508",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=509", browseName="ns=scales;WeightId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=510", browseName="ns=scales;WeightStable", dataType=o6.Boolean)),
    ],
    dataType=scales_datypes.WeightType,
    value=scales_datypes.WeightType(gross=0.0, net=0.0, tare=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
scales_objtypes.WeighingItemType(nodeId="ns=scales;i=87", browseName="ns=scales;LastItem", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=scales;i=495"])])
o6.reference(scales_objtypes.CatchweigherProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=87"])
scales_vartypes.MeasuredItemType(
    nodeId="ns=scales;i=517",
    browseName="ns=scales;FlowRate",
    description="Defines the conveying capacity in volume per time.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=518", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=519", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=520",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
    ],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ContinuousScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=517"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=scales;i=605",
    browseName="ns=scales;ReferenceOptimisationRange",
    description="Defines the tolerance range within the scale may optimize the ReferencePieceWeight.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=606", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.PieceCountingScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=605"])
scales_vartypes.MeasuredItemType(
    nodeId="ns=scales;i=607",
    browseName="ns=scales;CurrentPieceCount",
    description="Defines the number of pieces that are currently measured related to the ReferencePieceWeight.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=449", browseName="ns=scales;InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=608", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=609", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=610",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.PieceCountingScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=607"])


ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=614",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=613",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=613", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=614"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=616",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=615",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=617",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=615",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=615", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=616"]), outputArgs=o6.hasProperty(o6.ns["ns=scales;i=617"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=619",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=618",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=620",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=618",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=618", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=619"]), outputArgs=o6.hasProperty(o6.ns["ns=scales;i=620"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=623",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=622",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=624",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=622",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=622", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=623"]), outputArgs=o6.hasProperty(o6.ns["ns=scales;i=624"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=626",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=625",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=625", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=626"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=631",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=630",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=630", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=631"]))

ns0.objtypes.FileType(
    nodeId="ns=scales;i=131",
    browseName="ns=scales;ReportFile",
    description="Defines the file (binary, xml or other) that contains the report of the current process.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=621", browseName="OpenCount", description="The current number of open file handles.", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=627", browseName="Size", description="The size of the file in bytes.", dataType=o6.UInt64)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=scales;i=628", browseName="UserWritable", description="Whether the file is writable by the current user.", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=629", browseName="Writable", description="Whether the file is writable.", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=scales;i=613"]),
        o6.hasComponent(o6.ns["ns=scales;i=615"]),
        o6.hasComponent(o6.ns["ns=scales;i=618"]),
        o6.hasComponent(o6.ns["ns=scales;i=622"]),
        o6.hasComponent(o6.ns["ns=scales;i=625"]),
        o6.hasComponent(o6.ns["ns=scales;i=630"]),
    ],
)
o6.reference(scales_objtypes.RecipeProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=131"])
scales_vartypes.TargetItemType(
    nodeId="ns=scales;i=634",
    browseName="ns=scales;VolumeTargetValue",
    description="Defines the preset of the volume to be processed.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=635", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=636", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.TotalizingHopperProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=634"])
scales_vartypes.TargetItemType(
    nodeId="ns=scales;i=178",
    browseName="ns=scales;TargetPieceCount",
    description="Defines the number of pieces that need to be counted.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=179", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=183", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=641", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.UInteger,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.PieceCountingProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=178"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=scales;i=173",
    browseName="ns=scales;ReferencePieceWeight",
    description="Defines the reference weight of a piece.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=174", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=650", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=651", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=652",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.PieceCountingProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=173"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=scales;i=599",
    browseName="ns=scales;ReferencePieceWeight",
    description="Defines the reference weight of a piece.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=600", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=653", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=654", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=655",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=scales;i=590",
    browseName="ns=scales;MinimumDeltaPerFeedRateMeasuringInterval",
    description="Defines the minimum amount of weight that needs to change within the FeedRateMeasuringInterval. Otherwise the filling procedure is not valid.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=591", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=656", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=657", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=658",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.PieceCountingProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=590"])
scales_vartypes.TargetItemType(
    nodeId="ns=scales;i=531",
    browseName="ns=scales;TargetWeight",
    description="Defines a preset of the volume to be processed.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=532", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=533", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=663", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ContinuousProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=531"])
scales_vartypes.TargetItemType(
    nodeId="ns=scales;i=534",
    browseName="ns=scales;TargetWeight",
    description="Defines a preset of the volume to be processed.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=535", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=536", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=668", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
scales_vartypes.TargetItemType(
    nodeId="ns=scales;i=235",
    browseName="ns=scales;TargetFlowRate",
    description="Defines a preset of flowrate that needs to be conveyed. This value defines the setpoint for the FlowRate control loop.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=236", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=237", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=673", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ContinuousProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=235"])
scales_vartypes.TargetItemType(
    nodeId="ns=scales;i=544",
    browseName="ns=scales;TargetWeight",
    description="Defines the preset of the volume to be processed.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=548", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=550", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=691", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.AutomaticFillingProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=544"])
scales_vartypes.TargetItemType(
    nodeId="ns=scales;i=562",
    browseName="ns=scales;TargetWeight",
    description="Defines the preset of the volume to be processed.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=568", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=569", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=696", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
scales_vartypes.TargetItemType(
    nodeId="ns=scales;i=572",
    browseName="ns=scales;TargetWeight",
    description="Defines the preset of the volume to be processed.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=573", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=574", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=701", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=scales;i=553",
    browseName="ns=scales;MinimumDeltaPerFeedRateMeasuringInterval",
    description="Defines the minimum amount of weight data which needs to change within the FeedRateMeasuringInterval.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=554", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=706",
                browseName="Definition",
                description="A vendor-specific, human readable string that specifies how the value of this DataItem is calculated.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=707", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=708", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=709",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.AutomaticFillingProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=553"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=scales;i=565",
    browseName="ns=scales;MinimumDeltaPerFeedRateMeasuringInterval",
    description="Defines the minimum amount of weight data which needs to change within the FeedRateMeasuringInterval.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=566", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=710",
                browseName="Definition",
                description="A vendor-specific, human readable string that specifies how the value of this DataItem is calculated.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=711", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=712", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=713",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=scales;i=545",
    browseName="ns=scales;InFlightWeight",
    description="Defines the volume that is behind the valve / in flight after feeding is stopped.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=557", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=714",
                browseName="Definition",
                description="A vendor-specific, human readable string that specifies how the value of this DataItem is calculated.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=715", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=716", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=717",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.AutomaticFillingProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=545"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=scales;i=556",
    browseName="ns=scales;InFlightWeight",
    description="Defines the volume that is behind the valve / in flight after feeding is stopped.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=559", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=718",
                browseName="Definition",
                description="A vendor-specific, human readable string that specifies how the value of this DataItem is calculated.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=719", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=720", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=721",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=scales;i=570",
    browseName="ns=scales;InFlightWeight",
    description="Defines the volume that is behind the valve / in flight after feeding is stopped.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=571", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=722",
                browseName="Definition",
                description="A vendor-specific, human readable string that specifies how the value of this DataItem is calculated.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=723", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=724", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=725",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=scales;i=546",
    browseName="ns=scales;FineFeedWeight",
    description="Defines the volume to be dosed in fine flow.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=558", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=726",
                browseName="Definition",
                description="A vendor-specific, human readable string that specifies how the value of this DataItem is calculated.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=727", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=728", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=729",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.AutomaticFillingProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=546"])
scales_objtypes.StatisticCounterType(
    nodeId="ns=scales;i=78",
    browseName="ns=scales;TotalPackages",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=736",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=461",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
o6.reference(scales_objtypes.StatisticType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=78"])
scales_objtypes.StatisticCounterType(
    nodeId="ns=scales;i=81",
    browseName="ns=scales;TotalPackagesWeighed",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=753",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=744",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
o6.reference(scales_objtypes.StatisticType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=81"])
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=760",
    browseName="EnumStrings",
    parent="ns=scales;i=65",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[4],
    value=[o6.LocalizedText("Right_0"), o6.LocalizedText("Left_1"), o6.LocalizedText("Top_2"), o6.LocalizedText("All_3")],
)
scales_objtypes.StatisticCounterType(
    nodeId="ns=scales;i=96",
    browseName="ns=scales;ZoneStatistic",
    description="Contains statistics regarding this zone.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=768",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=765",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_vartypes.WeightItemType(
    nodeId="ns=scales;i=247",
    browseName="ns=scales;MeasuredWeight",
    description="Defines the registered weight that may be unmistakeable referenced to one item.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=227", browseName="ns=scales;Overload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=228", browseName="ns=scales;Underload", dataType=o6.Boolean)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=230",
                browseName="ns=scales;InsideZero",
                description="Defines if the current measured value is within the valid range for the setting zero procedure. This is a necessary condition to success the setZero() method if available.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=363", browseName="ns=scales;CenterOfZero", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=370", browseName="ns=scales;GrossNegative", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=371", browseName="ns=scales;TareMode", dataType=scales_datypes.TareMode)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=372", browseName="ns=scales;WeightStable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=400", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=401", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=402",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=688", browseName="ns=scales;WeightId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=776", browseName="ns=scales;PrintableValue", dataType=scales_datypes.PrintableWeightType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=777", browseName="ns=scales;HighResolutionValue", dataType=scales_datypes.WeightType)),
    ],
    dataType=scales_datypes.WeightType,
    value=scales_datypes.WeightType(gross=0.0, net=0.0, tare=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.WeighingItemType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=247"])
scales_vartypes.WeightItemType(
    nodeId="ns=scales;i=582",
    browseName="ns=scales;TotalizedWeight",
    description="Defines the summed up number of weight. Will be reset either triggered by the user or a different product selection.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=223", browseName="ns=scales;Overload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=224", browseName="ns=scales;Underload", dataType=o6.Boolean)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=225",
                browseName="ns=scales;InsideZero",
                description="Defines if the current measured value is within the valid range for the setting zero procedure. This is a necessary condition to success the setZero() method if available.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=583", browseName="ns=scales;CenterOfZero", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=584", browseName="ns=scales;GrossNegative", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=585", browseName="ns=scales;TareMode", dataType=scales_datypes.TareMode)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=586", browseName="ns=scales;WeightStable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=588", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=593", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=594",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=640", browseName="ns=scales;WeightId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=779", browseName="ns=scales;PrintableValue", dataType=scales_datypes.PrintableWeightType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=780", browseName="ns=scales;HighResolutionValue", dataType=scales_datypes.WeightType)),
    ],
    dataType=scales_datypes.WeightType,
    value=scales_datypes.WeightType(gross=0.0, net=0.0, tare=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.PieceCountingProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=582"])
scales_objtypes.MaterialType(
    nodeId="ns=scales;i=69",
    browseName="ns=scales;SupportedMaterial",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=scales;i=374", browseName="ns=scales;MaterialId", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=scales;i=787", browseName="ns=scales;MaterialName", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
        ),
    ],
)
o6.reference(scales_objtypes.RecipeScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=69"])
scales_vartypes.TargetItemType(
    nodeId="ns=scales;i=300",
    browseName="ns=scales;TargetThresholdValue",
    description="The target value with which the threshold value is compared.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=434", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=435", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=800", browseName="ns=scales;AllowedEngineeringUnits", dataType=ns0.datatypes.EUInformation, valueRank=1, arrayDimensions=[0]
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.AnalogConditionSleepType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=300"])
scales_vartypes.TargetItemType(
    nodeId="ns=scales;i=822",
    browseName="ns=scales;TargetThroughput",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=823", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=824", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
scales_vartypes.WeightItemType(
    nodeId="ns=scales;i=807",
    browseName="ns=scales;MeasuredWeight",
    description="Defines the registered weight that may be unmistakeable referenced to one item.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=808", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=809", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=810",
                browseName="ns=scales;InsideZero",
                description="Defines if the current measured value is within the valid range for the setting zero procedure. This is a necessary condition to success the setZero() method if available.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=812", browseName="ns=scales;Overload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=813", browseName="ns=scales;TareMode", dataType=scales_datypes.TareMode)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=814", browseName="ns=scales;Underload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=815", browseName="ns=scales;WeightStable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=825", browseName="ns=scales;CenterOfZero", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=826", browseName="ns=scales;GrossNegative", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=827", browseName="ns=scales;HighResolutionValue", dataType=scales_datypes.WeightType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=828", browseName="ns=scales;PrintableValue", dataType=scales_datypes.PrintableWeightType)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=829",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=830", browseName="ns=scales;WeightId", dataType=o6.String)),
    ],
    dataType=scales_datypes.WeightType,
    value=scales_datypes.WeightType(gross=0.0, net=0.0, tare=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
scales_objtypes.WeighingItemType(nodeId="ns=scales;i=801", browseName="ns=scales;LastItem", references=[o6.hasComponent(o6.ns["ns=scales;i=807"])])


ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=805",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=831",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="ZoneName", dataType=o6.LocalizedText, valueRank=-1),
        ns0.datatypes.Argument(name="LowerLimit", dataType=o6.Double, valueRank=-1),
        ns0.datatypes.Argument(name="UpperLimit", dataType=o6.Double, valueRank=-1),
        ns0.datatypes.Argument(name="EngineeringUnits", dataType=ns0.datatypes.EUInformation, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=806",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=831",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ZoneNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=scales;i=831",
    browseName="ns=scales;AddZone",
    description="Adds a zone to the zone array.",
    inputArgs=o6.hasProperty(o6.ns["ns=scales;i=805"]),
    outputArgs=o6.hasProperty(o6.ns["ns=scales;i=806"]),
)

scales_objtypes.MaterialType(
    nodeId="ns=scales;i=835",
    browseName="ns=scales;Material",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=875",
                browseName="ns=scales;MaterialId",
                description="Defines a unique identifier for the material.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=876",
                browseName="ns=scales;MaterialName",
                description="Defines a user-readable name of the material.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(scales_objtypes.VehicleProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=835"])
scales_vartypes.WeightItemType(
    nodeId="ns=scales;i=878",
    browseName="ns=scales;OutboundWeight",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=879",
                browseName="ns=scales;InsideZero",
                description="Defines if the current measured value is within the valid range for the setting zero procedure. This is a necessary condition to success the setZero() method if available.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=881", browseName="ns=scales;Overload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=882", browseName="ns=scales;TareMode", dataType=scales_datypes.TareMode)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=883", browseName="ns=scales;Underload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=884", browseName="ns=scales;WeightStable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=885", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=886", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=scales_datypes.WeightType,
    value=scales_datypes.WeightType(gross=0.0, net=0.0, tare=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.VehicleProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=878"])
scales_vartypes.WeightItemType(
    nodeId="ns=scales;i=887",
    browseName="ns=scales;InboundWeight",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=888",
                browseName="ns=scales;InsideZero",
                description="Defines if the current measured value is within the valid range for the setting zero procedure. This is a necessary condition to success the setZero() method if available.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=890", browseName="ns=scales;Overload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=891", browseName="ns=scales;TareMode", dataType=scales_datypes.TareMode)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=892", browseName="ns=scales;Underload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=893", browseName="ns=scales;WeightStable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=894", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=895", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=scales_datypes.WeightType,
    value=scales_datypes.WeightType(gross=0.0, net=0.0, tare=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.VehicleProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=887"])
scales_vartypes.WeightItemType(
    nodeId="ns=scales;i=861",
    browseName="ns=scales;DeltaWeight",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=862",
                browseName="ns=scales;InsideZero",
                description="Defines if the current measured value is within the valid range for the setting zero procedure. This is a necessary condition to success the setZero() method if available.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=864", browseName="ns=scales;Overload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=865", browseName="ns=scales;TareMode", dataType=scales_datypes.TareMode)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=866", browseName="ns=scales;Underload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=867", browseName="ns=scales;WeightStable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=868", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=869", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=899", browseName="ns=scales;IsFilling", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=scales_datypes.WeightType,
    value=scales_datypes.WeightType(gross=0.0, net=0.0, tare=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.VehicleProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=861"])
scales_vartypes.WeightItemType(
    nodeId="ns=scales;i=902",
    browseName="ns=scales;MeasuredWeight",
    description="Defines the registered weight that may be unmistakeable referenced to one item.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=901", browseName="ns=scales;CenterOfZero", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=903", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=904", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=905",
                browseName="ns=scales;InsideZero",
                description="Defines if the current measured value is within the valid range for the setting zero procedure. This is a necessary condition to success the setZero() method if available.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=907", browseName="ns=scales;Overload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=908", browseName="ns=scales;TareMode", dataType=scales_datypes.TareMode)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=909", browseName="ns=scales;Underload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=910", browseName="ns=scales;WeightStable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=911", browseName="ns=scales;GrossNegative", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=912", browseName="ns=scales;HighResolutionValue", dataType=scales_datypes.WeightType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=913", browseName="ns=scales;PrintableValue", dataType=scales_datypes.PrintableWeightType)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=914",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=915", browseName="ns=scales;WeightId", dataType=o6.String)),
    ],
    dataType=scales_datypes.WeightType,
    value=scales_datypes.WeightType(gross=0.0, net=0.0, tare=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
scales_objtypes.PriceItemType(nodeId="ns=scales;i=836", browseName="ns=scales;LastItem", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=scales;i=902"])])
o6.reference(scales_objtypes.AutomaticWeightPriceLabelerProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=836"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashScalesSlashV2Slash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=scales;i=839",
    browseName="ns=scales;http://opcfoundation.org/UA/Scales/V2/",
    description="Provides the metadata for a namespace used by the server.",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=scales;i=918", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=919", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-03-01T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=920", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Scales/V2/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=921", browseName="NamespaceVersion", dataType=o6.String, value="2.00")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=922", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=scales;i=923", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=924", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
scales_vartypes.TargetItemType(
    nodeId="ns=scales;i=940",
    browseName="ns=scales;NominalWeight",
    description="Defines the nominal (printed) weight of the product.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=941", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=942", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
scales_vartypes.WeightItemType(
    nodeId="ns=scales;i=976",
    browseName="ns=scales;OutboundWeight",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=977", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=978", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=979",
                browseName="ns=scales;InsideZero",
                description="Defines if the current measured value is within the valid range for the setting zero procedure. This is a necessary condition to success the setZero() method if available.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=981", browseName="ns=scales;Overload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=982", browseName="ns=scales;TareMode", dataType=scales_datypes.TareMode)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=983", browseName="ns=scales;Underload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=984", browseName="ns=scales;WeightStable", dataType=o6.Boolean)),
    ],
    dataType=scales_datypes.WeightType,
    value=scales_datypes.WeightType(gross=0.0, net=0.0, tare=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
scales_objtypes.AcceptedStatisticCounterType(
    nodeId="ns=scales;i=1030",
    browseName="ns=scales;PackagesAcceptedWithLowerToleranceLimit1",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1057",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1056",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1031",
    browseName="ns=scales;PackagesRejectedByDistanceFault",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1059",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1058",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1032",
    browseName="ns=scales;PackagesRejectedByLength",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1061",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1060",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1033",
    browseName="ns=scales;PackagesRejectedByLowerToleranceLimit1",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1063",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1062",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1034",
    browseName="ns=scales;PackagesRejectedByLowerToleranceLimit2",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1065",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1064",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1035",
    browseName="ns=scales;PackagesRejectedByMeanValueRequirement",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1067",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1066",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1036",
    browseName="ns=scales;PackagesRejectedByMetal",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1069",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1068",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1037",
    browseName="ns=scales;PackagesRejectedByVision",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1071",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1070",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1038",
    browseName="ns=scales;PackagesRejectedByXRay",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1073",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1072",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.AcceptedStatisticCounterType(
    nodeId="ns=scales;i=1042",
    browseName="ns=scales;PackagesAcceptedWithLowerToleranceLimit1",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1087",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1086",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1043",
    browseName="ns=scales;PackagesRejectedByDistanceFault",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1089",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1088",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1044",
    browseName="ns=scales;PackagesRejectedByLength",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1091",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1090",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1045",
    browseName="ns=scales;PackagesRejectedByLowerToleranceLimit1",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1093",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1092",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1046",
    browseName="ns=scales;PackagesRejectedByLowerToleranceLimit2",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1095",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1094",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1047",
    browseName="ns=scales;PackagesRejectedByMeanValueRequirement",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1097",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1096",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1048",
    browseName="ns=scales;PackagesRejectedByMetal",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1099",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1098",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1049",
    browseName="ns=scales;PackagesRejectedByVision",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1101",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1100",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1050",
    browseName="ns=scales;PackagesRejectedByXRay",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1103",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1102",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.StatisticCounterType(
    nodeId="ns=scales;i=1051",
    browseName="ns=scales;TotalPackages",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1110",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1109",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.StatisticCounterType(
    nodeId="ns=scales;i=1054",
    browseName="ns=scales;TotalPackagesWeighed",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1116",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1115",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_objtypes.AcceptedStatisticCounterType(
    nodeId="ns=scales;i=1158",
    browseName="ns=scales;PackagesAcceptedWithLowerToleranceLimit1",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1184",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1183",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
o6.reference(scales_objtypes.CheckweigherStatisticType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=1158"])
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1159",
    browseName="ns=scales;PackagesRejectedByDistanceFault",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1186",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1185",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
o6.reference(scales_objtypes.CheckweigherStatisticType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=1159"])
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1160",
    browseName="ns=scales;PackagesRejectedByLength",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1188",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1187",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
o6.reference(scales_objtypes.CheckweigherStatisticType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=1160"])
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1161",
    browseName="ns=scales;PackagesRejectedByLowerToleranceLimit1",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1190",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1189",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
o6.reference(scales_objtypes.CheckweigherStatisticType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=1161"])
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1162",
    browseName="ns=scales;PackagesRejectedByLowerToleranceLimit2",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1192",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1191",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
o6.reference(scales_objtypes.CheckweigherStatisticType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=1162"])
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1163",
    browseName="ns=scales;PackagesRejectedByMeanValueRequirement",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1194",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1193",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
o6.reference(scales_objtypes.CheckweigherStatisticType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=1163"])
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1164",
    browseName="ns=scales;PackagesRejectedByMetal",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1196",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1195",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
o6.reference(scales_objtypes.CheckweigherStatisticType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=1164"])
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1165",
    browseName="ns=scales;PackagesRejectedByVision",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1198",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1197",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
o6.reference(scales_objtypes.CheckweigherStatisticType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=1165"])
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=1168",
    browseName="ns=scales;PackagesRejectedByXRay",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1204",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1203",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
o6.reference(scales_objtypes.CheckweigherStatisticType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=1168"])
scales_objtypes.AcceptedStatisticCounterType(
    nodeId="ns=scales;i=1169",
    browseName="ns=scales;<PackagesAcceptedWithProperty>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1206",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1205",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
o6.reference(scales_objtypes.CheckweigherStatisticType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=1169"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=scales;i=1214",
    browseName="ns=scales;FineFeedWeight",
    description="Defines the volume to be dosed in fine flow.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1215",
                browseName="Definition",
                description="A vendor-specific, human readable string that specifies how the value of this DataItem is calculated.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1216", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1217", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1218", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1219",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=scales;i=1221",
    browseName="ns=scales;MinimumDeltaPerFeedRateMeasuringInterval",
    description="Defines the minimum amount of weight data which needs to change within the FeedRateMeasuringInterval.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1222",
                browseName="Definition",
                description="A vendor-specific, human readable string that specifies how the value of this DataItem is calculated.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1223", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1224", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1225", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1226",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=1229",
    browseName="ns=scales;ActualScaleInterval",
    description='Value expressed in units of mass of the difference between two consecutive indicated values, for digital indication ("d" as described in Welmec /OIML).',
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1230", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=1231",
    browseName="ns=scales;VerificationScaleInterval",
    description='Value, expressed in units of mass, used for the classification and verification of an instrument. ("e" as described in Welmec /OIML)',
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1232", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
scales_objtypes.AcceptedStatisticCounterType(
    nodeId="ns=scales;i=1170",
    browseName="ns=scales;<PackagesAcceptedWithProperty>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1243",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1242",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
scales_vartypes.TargetItemType(
    nodeId="ns=scales;i=1258",
    browseName="ns=scales;TargetFlowRate",
    description="Defines a preset of flowrate that needs to be conveyed. This value defines the setpoint for the FlowRate control loop.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1259", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1260", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1265", browseName="ValuePrecision", dataType=o6.Double)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=scales;i=1270",
    browseName="ns=scales;MinimumDeltaPerFeedRateMeasuringInterval",
    description="Defines the minimum amount of weight that needs to change within the FeedRateMeasuringInterval. Otherwise the filling procedure is not valid.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1271", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1272", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1273", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1274",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
scales_vartypes.TargetItemType(
    nodeId="ns=scales;i=1280",
    browseName="ns=scales;TargetPieceCount",
    description="Defines the number of pieces that need to be counted.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1281", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1282", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1283", browseName="InstrumentRange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.UInteger,
    accessLevel=3,
    userAccessLevel=1,
)
scales_vartypes.WeightItemType(
    nodeId="ns=scales;i=1289",
    browseName="ns=scales;TotalizedWeight",
    description="Defines the summed up number of weight. Will be reset either triggered by the user or a different product selection.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1290", browseName="ns=scales;CenterOfZero", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1291", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1292", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1293", browseName="ns=scales;GrossNegative", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1294", browseName="ns=scales;HighResolutionValue", dataType=scales_datypes.WeightType)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1295",
                browseName="ns=scales;InsideZero",
                description="Defines if the current measured value is within the valid range for the setting zero procedure. This is a necessary condition to success the setZero() method if available.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1297", browseName="ns=scales;Overload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1298", browseName="ns=scales;PrintableValue", dataType=scales_datypes.PrintableWeightType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1299", browseName="ns=scales;TareMode", dataType=scales_datypes.TareMode)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1300", browseName="ns=scales;Underload", dataType=o6.Boolean)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1301",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1302", browseName="ns=scales;WeightId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1303", browseName="ns=scales;WeightStable", dataType=o6.Boolean)),
    ],
    dataType=scales_datypes.WeightType,
    value=scales_datypes.WeightType(gross=0.0, net=0.0, tare=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
scales_vartypes.TargetItemType(
    nodeId="ns=scales;i=1319",
    browseName="ns=scales;VolumeTargetValue",
    description="Defines the preset of the volume to be processed.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1320", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1321", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
scales_vartypes.WeightItemType(
    nodeId="ns=scales;i=1333",
    browseName="ns=scales;InboundWeight",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1334", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1335", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1336",
                browseName="ns=scales;InsideZero",
                description="Defines if the current measured value is within the valid range for the setting zero procedure. This is a necessary condition to success the setZero() method if available.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1338", browseName="ns=scales;Overload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1339", browseName="ns=scales;TareMode", dataType=scales_datypes.TareMode)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1340", browseName="ns=scales;Underload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1341", browseName="ns=scales;WeightStable", dataType=o6.Boolean)),
    ],
    dataType=scales_datypes.WeightType,
    value=scales_datypes.WeightType(gross=0.0, net=0.0, tare=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
scales_objtypes.MaterialType(
    nodeId="ns=scales;i=1176",
    browseName="ns=scales;Material",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1342",
                browseName="ns=scales;MaterialId",
                description="Defines a unique identifier for the material.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1343",
                browseName="ns=scales;MaterialName",
                description="Defines a user-readable name of the material.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=262",
    browseName="ns=scales;ActualScaleInterval",
    description='Value expressed in units of mass of the difference between two consecutive indicated values, for digital indication ("d" as described in Welmec /OIML).',
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1351", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.WeighingRangeElementType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=262"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=417",
    browseName="ns=scales;VerificationScaleInterval",
    description='Value, expressed in units of mass, used for the classification and verification of an instrument. ("e" as described in Welmec /OIML)',
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1352", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.WeighingRangeElementType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=417"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=scales;i=1354",
    browseName="ns=scales;ItemPrice",
    description="ItemPrice defines the price related to measured weight and UnitPrice.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=scales;i=1355", browseName="ns=scales;CurrencyUnit", dataType=ns0.datatypes.CurrencyUnitType, accessLevel=3, userAccessLevel=1)
        )
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.PriceItemType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=1354"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=scales;i=1318",
    browseName="ns=scales;UnitPrice",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=scales;i=1356", browseName="ns=scales;CurrencyUnit", dataType=ns0.datatypes.CurrencyUnitType, accessLevel=3, userAccessLevel=1)
        )
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.SimpleProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=1318"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=scales;i=1357",
    browseName="ns=scales;UnitPrice",
    description="Defines the price per weight unit.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=scales;i=1211", browseName="ns=scales;CurrencyUnit", dataType=ns0.datatypes.CurrencyUnitType, accessLevel=3, userAccessLevel=1)
        )
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.AutomaticWeightPriceLabelerProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=1357"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=scales;i=291",
    browseName="ns=scales;Range",
    description="Defines the range within the scale may be operated depending on the additional parameters within this type.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1358", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3, userAccessLevel=1))
    ],
    dataType=ns0.datatypes.Range,
    value=ns0.datatypes.Range(low=0.0, high=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.WeighingRangeElementType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=291"])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=scales;i=926",
    browseName="ns=scales;Range",
    description="Defines the range within the scale may be operated depending on the additional parameters within this type.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1369", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3, userAccessLevel=1))
    ],
    dataType=ns0.datatypes.Range,
    value=ns0.datatypes.Range(low=0.0, high=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
scales_objtypes.WeighingRangeElementType(
    nodeId="ns=scales;i=94",
    browseName="ns=scales;<ListOfWeighingRanges>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=scales;i=926"]), o6.hasComponent(o6.ns["ns=scales;i=1229"]), o6.hasComponent(o6.ns["ns=scales;i=1231"])],
)
o6.reference(scales_objtypes.ScaleDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=94"])
scales_objtypes.AutomaticFillingProductType(
    nodeId="ns=scales;i=113",
    browseName="ns=scales;FillingProductInformation",
    description="Defines the parameters necessary for filling of the material.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=448",
                browseName="ns=scales;ProductName",
                description="Defines the name of this product.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=567",
                browseName="ns=scales;TareId",
                description="Defines an Id of tare value for the current product or item.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=114"]),
        o6.hasComponent(o6.ns["ns=scales;i=556"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=560",
                browseName="ns=scales;JogFeed",
                description="Defines if an additional dosage is necessary.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=561",
                browseName="ns=scales;SettlingTime",
                description="Defines the time that needs to be passed before measurement process can be triggered.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=562"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=563",
                browseName="ns=scales;FillingTime",
                description="Defines the maximal duration for the filling process to take place. Needs to be completed during this period.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=564",
                browseName="ns=scales;FeedRateMeasuringInterval",
                description="Defines the measuring interval for evaluating the current flowrate.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=565"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1385",
                browseName="ns=scales;ProductId",
                description="Defines a unique Id of this product.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(scales_objtypes.MaterialAutomaticType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=113"])
scales_vartypes.WeightItemType(
    nodeId="ns=scales;i=1389",
    browseName="ns=scales;MeasuredWeight",
    description="Defines the registered weight that may be unmistakeable referenced to one item.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1390", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1391", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1393", browseName="ns=scales;Overload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1394", browseName="ns=scales;TareMode", dataType=scales_datypes.TareMode)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1395", browseName="ns=scales;Underload", dataType=o6.Boolean)),
    ],
    dataType=scales_datypes.WeightType,
    value=scales_datypes.WeightType(gross=0.0, net=0.0, tare=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
scales_objtypes.WeighingItemType(nodeId="ns=scales;i=1182", browseName="ns=scales;LastItem", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=scales;i=1389"])])
o6.reference(scales_objtypes.StatisticType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=1182"])


ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1209",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1397",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="VehicleId", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=1397", browseName="ns=scales;GetVehicleInformation", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=1209"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1275",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1398",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TargetItemCount", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=1398", browseName="ns=scales;SetTargetItemCount", description="Set the number of TargetItemCount.", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=1275"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1276",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1399",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="TargetPieceCount", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="PlusTolerance", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="MinusTolerance", dataType=o6.UInt32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=scales;i=1399",
    browseName="ns=scales;SetTargetPieceCount",
    description="Sets the value of TargetPieceCount. See TargetPieceCount.",
    inputArgs=o6.hasProperty(o6.ns["ns=scales;i=1276"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1304",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1400",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=1400", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=1304"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1305",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1401",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1306",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1401",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=1401", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=1305"]), outputArgs=o6.hasProperty(o6.ns["ns=scales;i=1306"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1307",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1402",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1308",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1402",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=1402", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=1307"]), outputArgs=o6.hasProperty(o6.ns["ns=scales;i=1308"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1310",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1403",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1311",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1403",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=1403", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=1310"]), outputArgs=o6.hasProperty(o6.ns["ns=scales;i=1311"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1312",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1404",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=1404", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=1312"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1316",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1405",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=1405", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=1316"]))

ns0.objtypes.FileType(
    nodeId="ns=scales;i=1172",
    browseName="ns=scales;ReportFile",
    description="Defines the file (binary, xml or other) that contains the report of the current process.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1309", browseName="OpenCount", description="The current number of open file handles.", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1313", browseName="Size", description="The size of the file in bytes.", dataType=o6.UInt64)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=scales;i=1314", browseName="UserWritable", description="Whether the file is writable by the current user.", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1315", browseName="Writable", description="Whether the file is writable.", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=scales;i=1400"]),
        o6.hasComponent(o6.ns["ns=scales;i=1401"]),
        o6.hasComponent(o6.ns["ns=scales;i=1402"]),
        o6.hasComponent(o6.ns["ns=scales;i=1403"]),
        o6.hasComponent(o6.ns["ns=scales;i=1404"]),
        o6.hasComponent(o6.ns["ns=scales;i=1405"]),
    ],
)


ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1375",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1410",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=1410", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=scales;i=1375"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1376",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1411",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=1411", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=scales;i=1376"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1377",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1412",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1378",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1412",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=1412", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=1377"]), outputArgs=o6.hasProperty(o6.ns["ns=scales;i=1378"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1383",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1413",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=1413", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=scales;i=1383"]))

di.objtypes.LockingServicesType(
    nodeId="ns=scales;i=1181",
    browseName="ns=scales;Lock",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1379", browseName="ns=di;Locked", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1380", browseName="ns=di;LockingClient", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1381", browseName="ns=di;LockingUser", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1382", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=scales;i=1410"]),
        o6.hasComponent(o6.ns["ns=scales;i=1411"]),
        o6.hasComponent(o6.ns["ns=scales;i=1412"]),
        o6.hasComponent(o6.ns["ns=scales;i=1413"]),
    ],
)
o6.reference(scales_objtypes.ProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=1181"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=1427",
    browseName="ns=scales;ActualScaleInterval",
    description='Value expressed in units of mass of the difference between two consecutive indicated values, for digital indication ("d" as described in Welmec /OIML).',
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1428", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=scales;i=1429",
    browseName="ns=scales;Range",
    description="Defines the range within the scale may be operated depending on the additional parameters within this type.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1430", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3, userAccessLevel=1))
    ],
    dataType=ns0.datatypes.Range,
    value=ns0.datatypes.Range(low=0.0, high=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=1431",
    browseName="ns=scales;VerificationScaleInterval",
    description='Value, expressed in units of mass, used for the classification and verification of an instrument. ("e" as described in Welmec /OIML)',
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1432", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
scales_objtypes.WeighingRangeElementType(
    nodeId="ns=scales;i=1415",
    browseName="ns=scales;<ListOfWeighingRanges>",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=scales;i=1427"]), o6.hasComponent(o6.ns["ns=scales;i=1429"]), o6.hasComponent(o6.ns["ns=scales;i=1431"])],
)
scales_vartypes.WeightItemType(
    nodeId="ns=scales;i=1418",
    browseName="ns=scales;CurrentWeight",
    description="Defines the current value that is measured at the sensor at the current timestamp. Might be a highly fluctuating value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1419", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1420", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1422", browseName="ns=scales;Overload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1423", browseName="ns=scales;TareMode", dataType=scales_datypes.TareMode)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1424", browseName="ns=scales;Underload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1437", browseName="ns=scales;CenterOfZero", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1438", browseName="ns=scales;CurrentRangeId", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1439", browseName="ns=scales;GrossNegative", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1440", browseName="ns=scales;HighResolutionValue", dataType=scales_datypes.WeightType)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1441",
                browseName="ns=scales;InsideZero",
                description="Defines if the current measured value is within the valid range for the setting zero procedure. This is a necessary condition to success the setZero() method if available.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1442", browseName="ns=scales;PrintableValue", dataType=scales_datypes.PrintableWeightType)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1443",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1444", browseName="ns=scales;WeightId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1445", browseName="ns=scales;WeightStable", dataType=o6.Boolean)),
    ],
    dataType=scales_datypes.WeightType,
    value=scales_datypes.WeightType(gross=0.0, net=0.0, tare=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
scales_vartypes.WeightItemType(
    nodeId="ns=scales;i=1449",
    browseName="ns=scales;MeasuredWeight",
    description="Defines the registered weight that may be unmistakeable referenced to one item.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1450", browseName="ns=scales;CenterOfZero", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1451", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1452", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1453", browseName="ns=scales;GrossNegative", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1454", browseName="ns=scales;HighResolutionValue", dataType=scales_datypes.WeightType)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1455",
                browseName="ns=scales;InsideZero",
                description="Defines if the current measured value is within the valid range for the setting zero procedure. This is a necessary condition to success the setZero() method if available.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1457", browseName="ns=scales;Overload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1458", browseName="ns=scales;PrintableValue", dataType=scales_datypes.PrintableWeightType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1459", browseName="ns=scales;TareMode", dataType=scales_datypes.TareMode)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1460", browseName="ns=scales;Underload", dataType=o6.Boolean)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1461",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1462", browseName="ns=scales;WeightId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1463", browseName="ns=scales;WeightStable", dataType=o6.Boolean)),
    ],
    dataType=scales_datypes.WeightType,
    value=scales_datypes.WeightType(gross=0.0, net=0.0, tare=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
scales_objtypes.PriceItemType(nodeId="ns=scales;i=1417", browseName="ns=scales;LastItem", references=[o6.hasComponent(o6.ns["ns=scales;i=1449"])])
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=scales;i=1464",
    browseName="ns=scales;UnitPrice",
    description="Defines the price per weight unit.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=scales;i=1465", browseName="ns=scales;CurrencyUnit", dataType=ns0.datatypes.CurrencyUnitType, accessLevel=3, userAccessLevel=1)
        )
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=scales;i=1466",
    browseName="ns=scales;UnitPrice",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=scales;i=1467", browseName="ns=scales;CurrencyUnit", dataType=ns0.datatypes.CurrencyUnitType, accessLevel=3, userAccessLevel=1)
        )
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
scales_objtypes.CatchweigherProductType(
    nodeId="ns=scales;i=77",
    browseName="ns=scales;<Product>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1469",
                browseName="ns=scales;ProductName",
                description="Defines the name of this product.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1468",
                browseName="ns=scales;ProductId",
                description="Defines a unique Id of this product.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=scales;i=76",
    browseName="ns=scales;Products",
    description="The products used in the scale aggregated in the Products Object.",
    references=[o6.hasComponent(o6.ns["ns=scales;i=77"])],
)
scales_objtypes.ProductionPresetType(
    nodeId="ns=scales;i=849",
    browseName="ns=scales;ProductionPreset",
    description="Contains the productions presets.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=scales;i=76"])],
)
o6.reference(scales_objtypes.CatchweigherType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=849"])
scales_vartypes.WeightItemType(
    nodeId="ns=scales;i=60001",
    browseName="ns=scales;CurrentWeight",
    description="Defines the current value that is measured at the sensor at the current timestamp. Might be a highly fluctuating value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=6010", browseName="ns=scales;CenterOfZero", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=6011", browseName="ns=scales;CurrentRangeId", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=6012", browseName="ns=scales;GrossNegative", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=6013", browseName="ns=scales;HighResolutionValue", dataType=scales_datypes.WeightType)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=6014",
                browseName="ns=scales;InsideZero",
                description="Defines if the current measured value is within the valid range for the setting zero procedure. This is a necessary condition to success the setZero() method if available.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=6015", browseName="ns=scales;PrintableValue", dataType=scales_datypes.PrintableWeightType)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=6016",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=6017", browseName="ns=scales;WeightId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=6018", browseName="ns=scales;WeightStable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60002", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60003", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60005", browseName="ns=scales;Overload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60006", browseName="ns=scales;TareMode", dataType=scales_datypes.TareMode)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60007", browseName="ns=scales;Underload", dataType=o6.Boolean)),
    ],
    dataType=scales_datypes.WeightType,
    value=scales_datypes.WeightType(gross=0.0, net=0.0, tare=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60010",
    browseName="ns=scales;ActualScaleInterval",
    description='Value expressed in units of mass of the difference between two consecutive indicated values, for digital indication ("d" as described in Welmec /OIML).',
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60011", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=scales;i=60012",
    browseName="ns=scales;Range",
    description="Defines the range within the scale may be operated depending on the additional parameters within this type.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60013", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation, accessLevel=3, userAccessLevel=1))
    ],
    dataType=ns0.datatypes.Range,
    value=ns0.datatypes.Range(low=0.0, high=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60014",
    browseName="ns=scales;VerificationScaleInterval",
    description='Value, expressed in units of mass, used for the classification and verification of an instrument. ("e" as described in Welmec /OIML)',
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60015", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
    accessLevel=3,
    userAccessLevel=1,
)
scales_objtypes.WeighingRangeElementType(
    nodeId="ns=scales;i=50002",
    browseName="ns=scales;<ListOfWeighingRanges>",
    displayName="WeighingRange",
    modellingRule="MandatoryPlaceholder",
    references=[o6.hasComponent(o6.ns["ns=scales;i=60010"]), o6.hasComponent(o6.ns["ns=scales;i=60012"]), o6.hasComponent(o6.ns["ns=scales;i=60014"])],
)
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=scales;i=50003",
    browseName="ns=di;Identification",
    description="Used to organize parameters for identification of this TopologyElement",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60020",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60021",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60022",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(scales_objtypes.ScaleDeviceType, ns0.reftypes.HasAddIn, o6.ns["ns=scales;i=50003"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60053",
    browseName="ns=scales;MinimalWeight",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60054", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ScaleDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60053"])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=scales;i=50007",
    browseName="ns=di;Identification",
    description="Used to organize parameters for identification of this TopologyElement",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60057",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60058",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
o6.reference(scales_objtypes.PrinterModuleType, ns0.reftypes.HasAddIn, o6.ns["ns=scales;i=50007"])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=scales;i=50009",
    browseName="ns=di;Identification",
    description="Used to organize parameters for identification of this TopologyElement",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60059",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60060",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
o6.reference(scales_objtypes.FeederModuleType, ns0.reftypes.HasAddIn, o6.ns["ns=scales;i=50009"])
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=scales;i=50011",
    browseName="ns=di;Identification",
    description="Used to organize parameters for identification of this TopologyElement",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60064",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60065",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
scales_objtypes.FeederModuleType(
    nodeId="ns=scales;i=1177", browseName="ns=scales;<FeederModule>", modellingRule="OptionalPlaceholder", references=[o6.hasAddIn(o6.ns["ns=scales;i=50011"])]
)
machinery.objtypes.MachineryItemIdentificationType(
    nodeId="ns=scales;i=50012",
    browseName="ns=di;Identification",
    description="Used to organize parameters for identification of this TopologyElement",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60066",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60067",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
scales_objtypes.PrinterModuleType(
    nodeId="ns=scales;i=1178", browseName="ns=scales;<PrinterModule>", modellingRule="OptionalPlaceholder", references=[o6.hasAddIn(o6.ns["ns=scales;i=50012"])]
)
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=scales;i=50010",
    browseName="ns=di;Identification",
    description="Used to organize parameters for identification of this TopologyElement",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60061",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60062",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60069",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(scales_objtypes.ScaleSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=scales;i=50010"])
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=scales;i=50013",
    browseName="ns=di;Identification",
    description="Used to organize parameters for identification of this TopologyElement",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60068",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60070",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60071",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
scales_objtypes.WeighingModuleType(
    nodeId="ns=scales;i=1414",
    browseName="ns=scales;<WeighingModule>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1425", browseName="ns=di;DeviceClass", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1426", browseName="ns=di;HardwareRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1433", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1434", browseName="ns=di;Model", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1435", browseName="ns=di;SerialNumber", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1436", browseName="ns=di;SoftwareRevision", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=scales;i=1415"]),
        o6.hasComponent(o6.ns["ns=scales;i=1418"]),
        o6.hasAddIn(o6.ns["ns=scales;i=50013"]),
    ],
)
di.objtypes.ConfigurableObjectType(
    nodeId="ns=scales;i=67",
    browseName="ns=scales;SubDevices",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=scales;i=80",
                browseName="ns=di;SupportedTypes",
                description="Folder maintaining the set of (sub-types of) BaseObjectTypes that can be instantiated in the ConfigurableComponent.",
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=1177"]),
        o6.hasComponent(o6.ns["ns=scales;i=1178"]),
        o6.hasComponent(o6.ns["ns=scales;i=1414"]),
    ],
)
o6.reference(scales_objtypes.ScaleDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=67"])
scales_objtypes.StatisticType(
    nodeId="ns=scales;i=93",
    browseName="ns=scales;Statistic",
    description="Contains the different statistic values of the product.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60074",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        )
    ],
)
scales_objtypes.ProductType(
    nodeId="ns=scales;i=92",
    browseName="ns=scales;<Product>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=414",
                browseName="ns=scales;ProductName",
                description="Defines the name of this product.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=93"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1384",
                browseName="ns=scales;ProductId",
                description="Defines a unique Id of this product.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
    _allow_abstract=True,
)
ns0.objtypes.FolderType(
    nodeId="ns=scales;i=75",
    browseName="ns=scales;Products",
    description="The products used in the scale aggregated in the Products Object.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=scales;i=92"])],
)
o6.reference(scales_objtypes.ProductionPresetType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=75"])
scales_objtypes.StatisticType(
    nodeId="ns=scales;i=1416",
    browseName="ns=scales;Statistic",
    description="Contains the different statistic values of the product.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60075",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        )
    ],
)
scales_objtypes.AutomaticWeightPriceLabelerProductType(
    nodeId="ns=scales;i=117",
    browseName="ns=scales;<Product>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1447",
                browseName="ns=scales;ProductName",
                description="Defines the name of this product.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=1416"]),
        o6.hasComponent(o6.ns["ns=scales;i=1417"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1446",
                browseName="ns=scales;ProductId",
                description="Defines a unique Id of this product.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=1464"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=scales;i=116",
    browseName="ns=scales;Products",
    description="The products used in the scale aggregated in the Products Object.",
    references=[o6.hasComponent(o6.ns["ns=scales;i=117"])],
)
scales_objtypes.ProductionPresetType(
    nodeId="ns=scales;i=851",
    browseName="ns=scales;ProductionPreset",
    description="Contains the productions presets.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=scales;i=116"])],
)
o6.reference(scales_objtypes.AutomaticWeightPriceLabelerType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=851"])
scales_objtypes.StatisticType(
    nodeId="ns=scales;i=120",
    browseName="ns=scales;Statistic",
    description="Contains the different statistic values of the product.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60076",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        )
    ],
)
scales_objtypes.ContinuousProductType(
    nodeId="ns=scales;i=119",
    browseName="ns=scales;<Product>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=489",
                browseName="ns=scales;ProductName",
                description="Defines the name of this product.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=120"]),
        o6.hasComponent(o6.ns["ns=scales;i=534"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1009",
                browseName="ns=scales;ProductId",
                description="Defines a unique Id of this product.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=1258"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=scales;i=118",
    browseName="ns=scales;Products",
    description="The products used in the scale aggregated in the Products Object.",
    references=[o6.hasComponent(o6.ns["ns=scales;i=119"])],
)
scales_objtypes.ProductionPresetType(
    nodeId="ns=scales;i=852",
    browseName="ns=scales;ProductionPreset",
    description="Contains the productions presets.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=scales;i=118"])],
)
o6.reference(scales_objtypes.ContinuousScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=852"])
scales_objtypes.StatisticType(
    nodeId="ns=scales;i=123",
    browseName="ns=scales;Statistic",
    description="Contains the different statistic values of the product.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60077",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        )
    ],
)
scales_objtypes.AutomaticFillingProductType(
    nodeId="ns=scales;i=122",
    browseName="ns=scales;<Product>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=507",
                browseName="ns=scales;ProductName",
                description="Defines the name of this product.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1228",
                browseName="ns=scales;TareId",
                description="Defines an Id of tare value for the current product or item.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=123"]),
        o6.hasComponent(o6.ns["ns=scales;i=570"]),
        o6.hasComponent(o6.ns["ns=scales;i=572"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1212",
                browseName="ns=scales;FeedRateMeasuringInterval",
                description="Defines the measuring interval for evaluating the current flowrate.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1213",
                browseName="ns=scales;FillingTime",
                description="Defines the maximal duration for the filling process to take place. Needs to be completed during this period.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=1214"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1220",
                browseName="ns=scales;JogFeed",
                description="Defines if an additional dosage is necessary.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=1221"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1227",
                browseName="ns=scales;SettlingTime",
                description="Defines the time that needs to be passed before measurement process can be triggered.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1386",
                browseName="ns=scales;ProductId",
                description="Defines a unique Id of this product.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=scales;i=121",
    browseName="ns=scales;Products",
    description="The products used in the scale aggregated in the Products Object.",
    references=[o6.hasComponent(o6.ns["ns=scales;i=122"])],
)
scales_objtypes.ProductionPresetType(
    nodeId="ns=scales;i=848",
    browseName="ns=scales;ProductionPreset",
    description="Contains the productions presets.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=scales;i=121"])],
)
o6.reference(scales_objtypes.AutomaticFillingScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=848"])
scales_objtypes.StatisticType(
    nodeId="ns=scales;i=126",
    browseName="ns=scales;Statistic",
    description="Contains the different statistic values of the product.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60078",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        )
    ],
)
scales_objtypes.PieceCountingProductType(
    nodeId="ns=scales;i=125",
    browseName="ns=scales;<Product>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=516",
                browseName="ns=scales;ProductName",
                description="Defines the name of this product.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=126"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=595",
                browseName="ns=scales;CurrentItemCount",
                description="Defines the current number of items that are captured by the scale.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=596",
                browseName="ns=scales;InFlightCount",
                description="Defines the number of items that is behind valve / in flight after feeding is stopped.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=598",
                browseName="ns=scales;NumberOfReferencePieces",
                description="Defines the number of pieces that need to be used for reference process.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=599"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=601",
                browseName="ns=scales;RegisteredPieceCount",
                description="Defines the number of pieces that were actually counted related to the ReferencePieceWeight.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=965", browseName="ns=scales;ProductId", description="Defines a unique Id of this product.", dataType=o6.String, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1266",
                browseName="ns=scales;FeedRateMeasuringInterval",
                description="Defines the measurement interval for evaluating the current flowrate.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1267",
                browseName="ns=scales;FillingTime",
                description="Defines the interval during which the filling has to be completed.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=scales;i=1268", browseName="ns=scales;FineFeedCount", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1269",
                browseName="ns=scales;JogFeed",
                description="Defines if an additional dosage is necessary.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=1270"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1277",
                browseName="ns=scales;SettlingTime",
                description="Defines the time that needs to be passed before measurement process can be triggered.",
                dataType=ns0.datatypes.Duration,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1278",
                browseName="ns=scales;TareId",
                description="Defines the Id of tare value for the current product or item.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1279",
                browseName="ns=scales;TargetItemCount",
                description="Defines the number of items that are supposed to be counted during the measurement process.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=1280"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1288",
                browseName="ns=scales;TotalizedItemCount",
                description="Defines the summed up number of items. Will be reset either triggered by the user or a different product selection.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=1289"]),
        o6.hasComponent(o6.ns["ns=scales;i=1398"]),
        o6.hasComponent(o6.ns["ns=scales;i=1399"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=scales;i=124",
    browseName="ns=scales;Products",
    description="The products used in the scale aggregated in the Products Object.",
    references=[o6.hasComponent(o6.ns["ns=scales;i=125"])],
)
scales_objtypes.ProductionPresetType(
    nodeId="ns=scales;i=853",
    browseName="ns=scales;ProductionPreset",
    description="Contains the productions presets.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=scales;i=124"])],
)
o6.reference(scales_objtypes.PieceCountingScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=853"])
scales_objtypes.StatisticType(
    nodeId="ns=scales;i=130",
    browseName="ns=scales;Statistic",
    description="Contains the different statistic values of the product.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60079",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        )
    ],
)
scales_objtypes.RecipeProductType(
    nodeId="ns=scales;i=129",
    browseName="ns=scales;<Product>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=575",
                browseName="ns=scales;ProductName",
                description="Defines the name of this product.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=130"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=253",
                browseName="ns=scales;Report",
                description="Defines an array with the various messages from the recipe. Each RecipeElement generates its own report message.",
                dataType=scales_datypes.RecipeReportElementType,
                valueRank=1,
                arrayDimensions=[1],
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1010",
                browseName="ns=scales;RecipeNodeId",
                description="Defines the NodeId of the recipe that is being produced.",
                dataType=o6.NodeId,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1011",
                browseName="ns=scales;ProductId",
                description="Defines a unique Id of this product.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=1172"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=scales;i=128",
    browseName="ns=scales;Products",
    description="The products used in the scale aggregated in the Products Object.",
    references=[o6.hasComponent(o6.ns["ns=scales;i=129"])],
)
scales_objtypes.ProductionPresetType(
    nodeId="ns=scales;i=854",
    browseName="ns=scales;ProductionPreset",
    description="Contains the productions presets.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=scales;i=128"])],
)
o6.reference(scales_objtypes.RecipeScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=854"])
scales_objtypes.StatisticType(
    nodeId="ns=scales;i=1174",
    browseName="ns=scales;Statistic",
    description="Contains the different statistic values of the product.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60080",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        )
    ],
)
scales_objtypes.TotalizingHopperProductType(
    nodeId="ns=scales;i=841",
    browseName="ns=scales;<Product>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=964",
                browseName="ns=scales;ProductName",
                description="Defines the name of this product.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=962",
                browseName="ns=scales;TipCounter",
                description="Defines the number of fillings (downpour, bulk produce)",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=1174"]),
        o6.hasComponent(o6.ns["ns=scales;i=1319"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1387",
                browseName="ns=scales;ProductId",
                description="Defines a unique Id of this product.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=scales;i=840",
    browseName="ns=scales;Products",
    description="The products used in the scale aggregated in the Products Object.",
    references=[o6.hasComponent(o6.ns["ns=scales;i=841"])],
)
scales_objtypes.ProductionPresetType(
    nodeId="ns=scales;i=856",
    browseName="ns=scales;ProductionPreset",
    description="Contains the productions presets.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=scales;i=840"])],
)
o6.reference(scales_objtypes.TotalizingHopperScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=856"])
scales_objtypes.StatisticType(
    nodeId="ns=scales;i=1173",
    browseName="ns=scales;Statistic",
    description="Contains the different statistic values of the product.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60081",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        )
    ],
)
scales_objtypes.SimpleProductType(
    nodeId="ns=scales;i=843",
    browseName="ns=scales;<Product>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=966",
                browseName="ns=scales;ProductName",
                description="Defines the name of this product.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1317", browseName="ns=scales;ContainerId", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=991", browseName="ns=scales;ProductId", description="Defines a unique Id of this product.", dataType=o6.String, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=1173"]),
        o6.hasComponent(o6.ns["ns=scales;i=1466"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=scales;i=842",
    browseName="ns=scales;Products",
    description="The products used in the scale aggregated in the Products Object.",
    references=[o6.hasComponent(o6.ns["ns=scales;i=843"])],
)
scales_objtypes.ProductionPresetType(
    nodeId="ns=scales;i=855",
    browseName="ns=scales;ProductionPreset",
    description="Contains the productions presets.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=scales;i=842"])],
)
o6.reference(scales_objtypes.SimpleScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=855"])
scales_vartypes.WeightItemType(
    nodeId="ns=scales;i=967",
    browseName="ns=scales;DeltaWeight",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=968", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=969", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=970",
                browseName="ns=scales;InsideZero",
                description="Defines if the current measured value is within the valid range for the setting zero procedure. This is a necessary condition to success the setZero() method if available.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=972", browseName="ns=scales;Overload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=973", browseName="ns=scales;TareMode", dataType=scales_datypes.TareMode)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=974", browseName="ns=scales;Underload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=975", browseName="ns=scales;WeightStable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60082", browseName="ns=scales;IsFilling", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=scales_datypes.WeightType,
    value=scales_datypes.WeightType(gross=0.0, net=0.0, tare=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
scales_objtypes.StatisticType(
    nodeId="ns=scales;i=1175",
    browseName="ns=scales;Statistic",
    description="Contains the different statistic values of the product.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60083",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        )
    ],
)
scales_objtypes.VehicleProductType(
    nodeId="ns=scales;i=845",
    browseName="ns=scales;<Product>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=985", browseName="ns=scales;VehicleId", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=987",
                browseName="ns=scales;ProductName",
                description="Defines the name of this product.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=scales;i=1326", browseName="ns=scales;CarrierDisplayName", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1327", browseName="ns=scales;CarrierId", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1328", browseName="ns=scales;Customer", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1329", browseName="ns=scales;Destination", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1330", browseName="ns=scales;DriverDisplayName", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1331", browseName="ns=scales;DriverId", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1332", browseName="ns=scales;InboundScale", dataType=o6.NodeId, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1344", browseName="ns=scales;OutboundScale", dataType=o6.NodeId, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1345", browseName="ns=scales;ScaleOperatorId", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1346", browseName="ns=scales;Supplier", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1347", browseName="ns=scales;Tare", dataType=ns0.datatypes.Number, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1348", browseName="ns=scales;TareExpirationDate", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=scales;i=1349", browseName="ns=scales;TotalWeight", dataType=scales_datypes.WeightType, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=1350", browseName="ns=scales;TotalWeightResetDate", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=scales;i=967"]),
        o6.hasComponent(o6.ns["ns=scales;i=976"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1019",
                browseName="ns=scales;ProductId",
                description="Defines a unique Id of this product.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=1175"]),
        o6.hasComponent(o6.ns["ns=scales;i=1176"]),
        o6.hasComponent(o6.ns["ns=scales;i=1333"]),
        o6.hasComponent(o6.ns["ns=scales;i=1397"]),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=scales;i=844",
    browseName="ns=scales;Products",
    description="The products used in the scale aggregated in the Products Object.",
    references=[o6.hasComponent(o6.ns["ns=scales;i=845"])],
)
scales_objtypes.ProductionPresetType(
    nodeId="ns=scales;i=857",
    browseName="ns=scales;ProductionPreset",
    description="Contains the productions presets.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=scales;i=844"])],
)
o6.reference(scales_objtypes.VehicleScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=857"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=scales;i=60084",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60085", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=scales;i=60086",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60087", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=scales;i=60088",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60089", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=scales;i=60090",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60091", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=scales;i=512",
    browseName="ns=scales;PercentageLowerToleranceLimit",
    description="Defines the lower tolerance limit defined in welmec 6.4.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60092", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=ns0.datatypes.Number,
)
o6.reference(scales_objtypes.CheckweigherStatisticType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=512"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=scales;i=1074",
    browseName="ns=scales;PercentageLowerToleranceLimit",
    description="Defines the lower tolerance limit defined in welmec 6.4.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60093", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=ns0.datatypes.Number,
)
scales_objtypes.CheckweigherStatisticType(
    nodeId="ns=scales;i=71",
    browseName="ns=scales;Statistic",
    description="Contains the different statistic values of the product.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1075",
                browseName="ns=ia;ResetCondition",
                description="The reason and context for the reset of the statistics, which is done without a trigger from an OPC UA Client, like calling the ResetStatistics Method. ResetCondition is a vendor-specific, human readable string. ResetCondition is non-localized and might contain an expression that can be parsed by certain clients. Examples are: “AFTER 4 HOURS”, “AFTER 1000 ITEMS”, “OPERATOR”. “OPERATOR” means, that an operator resets the statistics on a local HMI.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1076",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.reference(o6.ns["ns=scales;i=1030"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1031"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1032"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1033"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1034"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1035"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1036"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1037"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1038"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1074"], "ns=ia;i=4002"),
    ],
)
o6.reference(scales_objtypes.CheckweigherProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=71"])
ns0.vartypes.AnalogItemType(
    nodeId="ns=scales;i=1104",
    browseName="ns=scales;PercentageLowerToleranceLimit",
    description="Defines the lower tolerance limit defined in welmec 6.4.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60094", browseName="EURange", dataType=ns0.datatypes.Range))],
    dataType=ns0.datatypes.Number,
)
scales_objtypes.CheckweigherStatisticType(
    nodeId="ns=scales;i=802",
    browseName="ns=scales;Statistic",
    description="Contains the different statistic values of the product.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1105",
                browseName="ns=ia;ResetCondition",
                description="The reason and context for the reset of the statistics, which is done without a trigger from an OPC UA Client, like calling the ResetStatistics Method. ResetCondition is a vendor-specific, human readable string. ResetCondition is non-localized and might contain an expression that can be parsed by certain clients. Examples are: “AFTER 4 HOURS”, “AFTER 1000 ITEMS”, “OPERATOR”. “OPERATOR” means, that an operator resets the statistics on a local HMI.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=6021",
                browseName="ns=ia;StartTime",
                description="Indicates the point in time at which the collection of the statistical data has been started.",
                dataType=o6.DateTime,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=1170"]),
        o6.reference(o6.ns["ns=scales;i=1042"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1043"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1044"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1045"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1046"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1047"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1048"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1049"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1050"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1051"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1054"], "ns=ia;i=4002"),
        o6.reference(o6.ns["ns=scales;i=1104"], "ns=ia;i=4002"),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scales;i=60095", browseName="ns=scales;PrintableWeightType", dataType=o6.String, value="PrintableWeightType")
o6.reference(o6.ns["ns=scales;i=97"], "i=39", o6.ns["ns=scales;i=60095"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scales;i=60096", browseName="ns=scales;PrintableWeightType", dataType=o6.String, value="//xs:element[@name='PrintableWeightType']")
o6.reference(o6.ns["ns=scales;i=98"], "i=39", o6.ns["ns=scales;i=60096"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scales;i=60097", browseName="ns=scales;WeightType", dataType=o6.String, value="WeightType")
o6.reference(o6.ns["ns=scales;i=88"], "i=39", o6.ns["ns=scales;i=60097"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scales;i=60098", browseName="ns=scales;WeightType", dataType=o6.String, value="//xs:element[@name='WeightType']")
o6.reference(o6.ns["ns=scales;i=89"], "i=39", o6.ns["ns=scales;i=60098"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scales;i=60099", browseName="ns=scales;RecipeReportElementType", dataType=o6.String, value="RecipeReportElementType")
o6.reference(o6.ns["ns=scales;i=106"], "i=39", o6.ns["ns=scales;i=60099"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=scales;i=60100", browseName="ns=scales;RecipeReportElementType", dataType=o6.String, value="//xs:element[@name='RecipeReportElementType']"
)
o6.reference(o6.ns["ns=scales;i=107"], "i=39", o6.ns["ns=scales;i=60100"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scales;i=60101", browseName="ns=scales;RecipeTargetValueType", dataType=o6.String, value="RecipeTargetValueType")
o6.reference(o6.ns["ns=scales;i=103"], "i=39", o6.ns["ns=scales;i=60101"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=scales;i=60102", browseName="ns=scales;RecipeTargetValueType", dataType=o6.String, value="//xs:element[@name='RecipeTargetValueType']"
)
o6.reference(o6.ns["ns=scales;i=104"], "i=39", o6.ns["ns=scales;i=60102"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scales;i=60103", browseName="ns=scales;RecipeThresholdType", dataType=o6.String, value="RecipeThresholdType")
o6.reference(o6.ns["ns=scales;i=100"], "i=39", o6.ns["ns=scales;i=60103"])
opcDotUaDotScale = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=scales;i=186",
    browseName="ns=scales;Opc.Ua.Scale",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Scales/V2/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=187", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Scales/V2/")),
        o6.hasComponent(o6.ns["ns=scales;i=60095"]),
        o6.hasComponent(o6.ns["ns=scales;i=60097"]),
        o6.hasComponent(o6.ns["ns=scales;i=60099"]),
        o6.hasComponent(o6.ns["ns=scales;i=60101"]),
        o6.hasComponent(o6.ns["ns=scales;i=60103"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/Scales/V2/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/Scales/V2/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="AbstractWeightType"/>\n <opc:StructuredType BaseType="tns:AbstractWeightType" Name="PrintableWeightType">\n  <opc:Field TypeName="opc:CharArray" Name="Gross"/>\n  <opc:Field TypeName="opc:CharArray" Name="Net"/>\n  <opc:Field TypeName="opc:CharArray" Name="Tare"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:AbstractWeightType" Name="WeightType">\n  <opc:Field TypeName="opc:Double" Name="Gross"/>\n  <opc:Field TypeName="opc:Double" Name="Net"/>\n  <opc:Field TypeName="opc:Double" Name="Tare"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RecipeReportElementType">\n  <opc:Field TypeName="ua:LocalizedText" Name="ReportMessage"/>\n  <opc:Field TypeName="opc:DateTime" Name="Timestamp"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RecipeTargetValueType">\n  <opc:Field TypeName="opc:Bit" Name="TargetValueNodeIdSpecified"/>\n  <opc:Field Length="31" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:UInt32" Name="TargetValueId"/>\n  <opc:Field SwitchField="TargetValueNodeIdSpecified" TypeName="ua:NodeId" Name="TargetValueNodeId"/>\n  <opc:Field TypeName="ua:LocalizedText" Name="TargetValueName"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="RecipeThresholdType">\n  <opc:Field TypeName="opc:Bit" Name="ThresholdNodeIdSpecified"/>\n  <opc:Field Length="31" TypeName="opc:Bit" Name="Reserved1"/>\n  <opc:Field TypeName="opc:UInt32" Name="ThresholdId"/>\n  <opc:Field SwitchField="ThresholdNodeIdSpecified" TypeName="ua:NodeId" Name="ThresholdNodeId"/>\n  <opc:Field TypeName="ua:LocalizedText" Name="ThresholdName"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="DraftShieldType">\n  <opc:EnumeratedValue Name="Right_0" Value="0"/>\n  <opc:EnumeratedValue Name="Left_1" Value="1"/>\n  <opc:EnumeratedValue Name="Top_2" Value="2"/>\n  <opc:EnumeratedValue Name="All_3" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="EdgeOperator">\n  <opc:EnumeratedValue Name="Rising_0" Value="0"/>\n  <opc:EnumeratedValue Name="Falling_1" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="EqualityAndRelationalOperator">\n  <opc:Documentation>This enumeration describes the different condition modes for an analog condition.</opc:Documentation>\n  <opc:EnumeratedValue Name="Equal_0" Value="0"/>\n  <opc:EnumeratedValue Name="NotEqual_1" Value="1"/>\n  <opc:EnumeratedValue Name="LessOrEqualThan_2" Value="2"/>\n  <opc:EnumeratedValue Name="GreaterOrEqualThan_3" Value="3"/>\n  <opc:EnumeratedValue Name="LessThan_4" Value="4"/>\n  <opc:EnumeratedValue Name="GreaterThan_5" Value="5"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="RateControlMode">\n  <opc:EnumeratedValue Name="Gravimetric_0" Value="0"/>\n  <opc:EnumeratedValue Name="Volumetric_1" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="TareMode">\n  <opc:EnumeratedValue Name="None_0" Value="0"/>\n  <opc:EnumeratedValue Name="MeasuredTare_1" Value="1"/>\n  <opc:EnumeratedValue Name="PresetTare_2" Value="2"/>\n  <opc:EnumeratedValue Name="ProportionalTare_3" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="ToleranceState">\n  <opc:EnumeratedValue Name="In_0" Value="0"/>\n  <opc:EnumeratedValue Name="Under_1" Value="1"/>\n  <opc:EnumeratedValue Name="Over_2" Value="2"/>\n  <opc:EnumeratedValue Name="UnderOrOver_3" Value="3"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=scales;i=60104", browseName="ns=scales;RecipeThresholdType", dataType=o6.String, value="//xs:element[@name='RecipeThresholdType']")
o6.reference(o6.ns["ns=scales;i=101"], "i=39", o6.ns["ns=scales;i=60104"])
opcDotUaDotScale_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=scales;i=188",
    browseName="ns=scales;Opc.Ua.Scale",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/Scales/V2/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=189", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Scales/V2/Types.xsd")),
        o6.hasComponent(o6.ns["ns=scales;i=60096"]),
        o6.hasComponent(o6.ns["ns=scales;i=60098"]),
        o6.hasComponent(o6.ns["ns=scales;i=60100"]),
        o6.hasComponent(o6.ns["ns=scales;i=60102"]),
        o6.hasComponent(o6.ns["ns=scales;i=60104"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/Scales/V2/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/Scales/V2/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="DraftShieldType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Right_0_0"/>\n   <xs:enumeration value="Left_1_1"/>\n   <xs:enumeration value="Top_2_2"/>\n   <xs:enumeration value="All_3_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:DraftShieldType" name="DraftShieldType"/>\n <xs:complexType name="ListOfDraftShieldType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:DraftShieldType" name="DraftShieldType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfDraftShieldType" name="ListOfDraftShieldType" nillable="true"/>\n <xs:simpleType name="EdgeOperator">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Rising_0_0"/>\n   <xs:enumeration value="Falling_1_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:EdgeOperator" name="EdgeOperator"/>\n <xs:complexType name="ListOfEdgeOperator">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:EdgeOperator" name="EdgeOperator" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEdgeOperator" name="ListOfEdgeOperator" nillable="true"/>\n <xs:simpleType name="EqualityAndRelationalOperator">\n  <xs:annotation>\n   <xs:documentation>This enumeration describes the different condition modes for an analog condition.</xs:documentation>\n  </xs:annotation>\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Equal_0_0"/>\n   <xs:enumeration value="NotEqual_1_1"/>\n   <xs:enumeration value="LessOrEqualThan_2_2"/>\n   <xs:enumeration value="GreaterOrEqualThan_3_3"/>\n   <xs:enumeration value="LessThan_4_4"/>\n   <xs:enumeration value="GreaterThan_5_5"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:EqualityAndRelationalOperator" name="EqualityAndRelationalOperator"/>\n <xs:complexType name="ListOfEqualityAndRelationalOperator">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:EqualityAndRelationalOperator" name="EqualityAndRelationalOperator" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEqualityAndRelationalOperator" name="ListOfEqualityAndRelationalOperator" nillable="true"/>\n <xs:simpleType name="RateControlMode">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Gravimetric_0_0"/>\n   <xs:enumeration value="Volumetric_1_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:RateControlMode" name="RateControlMode"/>\n <xs:complexType name="ListOfRateControlMode">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RateControlMode" name="RateControlMode" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRateControlMode" name="ListOfRateControlMode" nillable="true"/>\n <xs:simpleType name="TareMode">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="None_0_0"/>\n   <xs:enumeration value="MeasuredTare_1_1"/>\n   <xs:enumeration value="PresetTare_2_2"/>\n   <xs:enumeration value="ProportionalTare_3_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:TareMode" name="TareMode"/>\n <xs:complexType name="ListOfTareMode">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:TareMode" name="TareMode" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfTareMode" name="ListOfTareMode" nillable="true"/>\n <xs:simpleType name="ToleranceState">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="In_0_0"/>\n   <xs:enumeration value="Under_1_1"/>\n   <xs:enumeration value="Over_2_2"/>\n   <xs:enumeration value="UnderOrOver_3_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ToleranceState" name="ToleranceState"/>\n <xs:complexType name="ListOfToleranceState">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ToleranceState" name="ToleranceState" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfToleranceState" name="ListOfToleranceState" nillable="true"/>\n <xs:complexType name="AbstractWeightType">\n  <xs:sequence/>\n </xs:complexType>\n <xs:element type="tns:AbstractWeightType" name="AbstractWeightType"/>\n <xs:complexType name="ListOfAbstractWeightType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AbstractWeightType" name="AbstractWeightType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAbstractWeightType" name="ListOfAbstractWeightType" nillable="true"/>\n <xs:complexType name="PrintableWeightType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Gross"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Net"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Tare"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:PrintableWeightType" name="PrintableWeightType"/>\n <xs:complexType name="ListOfPrintableWeightType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PrintableWeightType" name="PrintableWeightType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPrintableWeightType" name="ListOfPrintableWeightType" nillable="true"/>\n <xs:complexType name="WeightType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Gross"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Net"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Tare"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WeightType" name="WeightType"/>\n <xs:complexType name="ListOfWeightType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WeightType" name="WeightType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWeightType" name="ListOfWeightType" nillable="true"/>\n <xs:complexType name="RecipeReportElementType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="ReportMessage"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:dateTime" name="Timestamp"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RecipeReportElementType" name="RecipeReportElementType"/>\n <xs:complexType name="ListOfRecipeReportElementType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RecipeReportElementType" name="RecipeReportElementType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRecipeReportElementType" name="ListOfRecipeReportElementType" nillable="true"/>\n <xs:complexType name="RecipeTargetValueType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="TargetValueId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:NodeId" name="TargetValueNodeId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="TargetValueName"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RecipeTargetValueType" name="RecipeTargetValueType"/>\n <xs:complexType name="ListOfRecipeTargetValueType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RecipeTargetValueType" name="RecipeTargetValueType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRecipeTargetValueType" name="ListOfRecipeTargetValueType" nillable="true"/>\n <xs:complexType name="RecipeThresholdType">\n  <xs:sequence>\n   <xs:element minOccurs="0" type="xs:unsignedInt" name="EncodingMask"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="ThresholdId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:NodeId" name="ThresholdNodeId"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:LocalizedText" name="ThresholdName"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:RecipeThresholdType" name="RecipeThresholdType"/>\n <xs:complexType name="ListOfRecipeThresholdType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RecipeThresholdType" name="RecipeThresholdType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRecipeThresholdType" name="ListOfRecipeThresholdType" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=scales;i=60107",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60108", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
pack_ml.objtypes.PackMLExecuteStateMachineType(
    nodeId="ns=scales;i=50017",
    browseName="ns=pack_ml;ExecuteState",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=scales;i=60105", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=scales;i=60106", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(o6.ns["ns=scales;i=60107"]),
    ],
)
pack_ml.objtypes.PackMLMachineStateMachineType(
    nodeId="ns=scales;i=50015",
    browseName="ns=pack_ml;MachineState",
    references=[
        o6.hasComponent(o6.ns["ns=scales;i=50017"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=scales;i=60031", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=scales;i=60032", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(o6.ns["ns=scales;i=60084"]),
    ],
)
pack_ml.objtypes.PackMLBaseStateMachineType(
    nodeId="ns=scales;i=50005",
    browseName="ns=scales;State",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=scales;i=50015"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=scales;i=60029", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=scales;i=60030", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(o6.ns["ns=scales;i=60086"]),
    ],
)
o6.reference(scales_objtypes.ScaleDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=50005"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=scales;i=60111",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60112", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
pack_ml.objtypes.PackMLExecuteStateMachineType(
    nodeId="ns=scales;i=50018",
    browseName="ns=pack_ml;ExecuteState",
    references=[
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=scales;i=60109", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=scales;i=60110", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(o6.ns["ns=scales;i=60111"]),
    ],
)
pack_ml.objtypes.PackMLMachineStateMachineType(
    nodeId="ns=scales;i=50016",
    browseName="ns=pack_ml;MachineState",
    references=[
        o6.hasComponent(o6.ns["ns=scales;i=50018"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=scales;i=60051", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=scales;i=60052", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(o6.ns["ns=scales;i=60088"]),
    ],
)
pack_ml.objtypes.PackMLBaseStateMachineType(
    nodeId="ns=scales;i=50008",
    browseName="ns=scales;SystemState",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=scales;i=50016"]),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=scales;i=60049", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=scales;i=60050", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])),
        o6.hasComponent(o6.ns["ns=scales;i=60090"]),
    ],
)
o6.reference(scales_objtypes.ScaleSystemType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=50008"])
scales_vartypes.WeightItemType(
    nodeId="ns=scales;i=203",
    browseName="ns=scales;CurrentWeight",
    description="Defines the current value that is measured at the sensor at the current timestamp. Might be a highly fluctuating value.",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=159", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=160",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=163", browseName="ns=scales;Overload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=164", browseName="ns=scales;Underload", dataType=o6.Boolean)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=165",
                browseName="ns=scales;InsideZero",
                description="Defines if the current measured value is within the valid range for the setting zero procedure. This is a necessary condition to success the setZero() method if available.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=200", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=204", browseName="ns=scales;WeightId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=205", browseName="ns=scales;GrossNegative", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=206", browseName="ns=scales;CenterOfZero", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=209", browseName="ns=scales;TareMode", dataType=scales_datypes.TareMode)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=210", browseName="ns=scales;WeightStable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=399", browseName="ns=scales;CurrentRangeId", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=772", browseName="ns=scales;PrintableValue", dataType=scales_datypes.PrintableWeightType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=773", browseName="ns=scales;HighResolutionValue", dataType=scales_datypes.WeightType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60113", browseName="ns=scales;Gross", dataType=o6.Double, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60114", browseName="ns=scales;LegalForTrade", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60115", browseName="ns=scales;Net", dataType=o6.Double, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60116", browseName="ns=scales;Tare", dataType=o6.Double, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=scales_datypes.WeightType,
    value=scales_datypes.WeightType(gross=0.0, net=0.0, tare=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ScaleDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=203"])
scales_vartypes.WeightItemType(
    nodeId="ns=scales;i=211",
    browseName="ns=scales;RegisteredWeight",
    description="Defines the last valid measurement that was recorded and will be used for further processing. This is the legal registered value of the scale.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=201", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=202",
                browseName="ValuePrecision",
                description="The maximum precision that the server can maintain for the item based on restrictions in the target environment.",
                dataType=o6.Double,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=207", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=212", browseName="ns=scales;WeightId", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=213", browseName="ns=scales;GrossNegative", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=214", browseName="ns=scales;CenterOfZero", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=215", browseName="ns=scales;Overload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=216", browseName="ns=scales;Underload", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=217", browseName="ns=scales;TareMode", dataType=scales_datypes.TareMode)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=218", browseName="ns=scales;WeightStable", dataType=o6.Boolean)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=221",
                browseName="ns=scales;InsideZero",
                description="Defines if the current measured value is within the valid range for the setting zero procedure. This is a necessary condition to success the setZero() method if available.",
                dataType=o6.Boolean,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=774", browseName="ns=scales;PrintableValue", dataType=scales_datypes.PrintableWeightType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=775", browseName="ns=scales;HighResolutionValue", dataType=scales_datypes.WeightType)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60117", browseName="ns=scales;CurrentRangeId", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60118", browseName="ns=scales;Gross", dataType=o6.Double, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60119", browseName="ns=scales;LegalForTrade", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60120", browseName="ns=scales;Net", dataType=o6.Double, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60121", browseName="ns=scales;Tare", dataType=o6.Double, accessLevel=3, userAccessLevel=1)),
    ],
    dataType=scales_datypes.WeightType,
    value=scales_datypes.WeightType(gross=0.0, net=0.0, tare=0.0),
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ScaleDeviceType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=211"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=scales;i=60122",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60123", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=scales;i=50023", browseName="ns=machinery;MachineryItemState", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=scales;i=60122"])]
)
o6.reference(scales_objtypes.FeederModuleType, ns0.reftypes.HasAddIn, o6.ns["ns=scales;i=50023"])
o6.reference(o6.ns["ns=scales;i=50019"], "i=17604", o6.ns["ns=scales;i=50023"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=scales;i=60124",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60125", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryOperationModeStateMachineType(
    nodeId="ns=scales;i=50024", browseName="ns=machinery;MachineryOperationMode", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=scales;i=60124"])]
)
o6.reference(scales_objtypes.FeederModuleType, ns0.reftypes.HasAddIn, o6.ns["ns=scales;i=50024"])
o6.reference(o6.ns["ns=scales;i=50019"], "i=17604", o6.ns["ns=scales;i=50024"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=scales;i=60126",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60127", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=scales;i=50025", browseName="ns=machinery;MachineryItemState", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=scales;i=60126"])]
)
o6.reference(scales_objtypes.PrinterModuleType, ns0.reftypes.HasAddIn, o6.ns["ns=scales;i=50025"])
o6.reference(o6.ns["ns=scales;i=50020"], "i=17604", o6.ns["ns=scales;i=50025"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=scales;i=60128",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60129", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryOperationModeStateMachineType(
    nodeId="ns=scales;i=50026", browseName="ns=machinery;MachineryOperationMode", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=scales;i=60128"])]
)
o6.reference(scales_objtypes.PrinterModuleType, ns0.reftypes.HasAddIn, o6.ns["ns=scales;i=50026"])
o6.reference(o6.ns["ns=scales;i=50020"], "i=17604", o6.ns["ns=scales;i=50026"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=scales;i=60130",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60131", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=scales;i=50027", browseName="ns=machinery;MachineryItemState", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=scales;i=60130"])]
)
o6.reference(scales_objtypes.ScaleDeviceType, ns0.reftypes.HasAddIn, o6.ns["ns=scales;i=50027"])
o6.reference(o6.ns["ns=scales;i=50021"], "i=17604", o6.ns["ns=scales;i=50027"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=scales;i=60132",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60133", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryOperationModeStateMachineType(
    nodeId="ns=scales;i=50028", browseName="ns=machinery;MachineryOperationMode", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=scales;i=60132"])]
)
o6.reference(scales_objtypes.ScaleDeviceType, ns0.reftypes.HasAddIn, o6.ns["ns=scales;i=50028"])
o6.reference(o6.ns["ns=scales;i=50021"], "i=17604", o6.ns["ns=scales;i=50028"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=scales;i=60134",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60135", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=scales;i=50029", browseName="ns=machinery;MachineryItemState", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=scales;i=60134"])]
)
o6.reference(scales_objtypes.ScaleSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=scales;i=50029"])
o6.reference(o6.ns["ns=scales;i=50022"], "i=17604", o6.ns["ns=scales;i=50029"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=scales;i=60136",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60137", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryOperationModeStateMachineType(
    nodeId="ns=scales;i=50030", browseName="ns=machinery;MachineryOperationMode", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=scales;i=60136"])]
)
o6.reference(scales_objtypes.ScaleSystemType, ns0.reftypes.HasAddIn, o6.ns["ns=scales;i=50030"])
o6.reference(o6.ns["ns=scales;i=50022"], "i=17604", o6.ns["ns=scales;i=50030"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60138",
    browseName="ns=scales;LowerToleranceLimit1",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60139", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.CheckweigherProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60138"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60140",
    browseName="ns=scales;LowerToleranceLimit2",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60141", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.CheckweigherProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60140"])
scales_vartypes.MeasuredItemType(
    nodeId="ns=scales;i=60144",
    browseName="ns=scales;HopperWeight",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60145", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60146", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60147", browseName="ValuePrecision", dataType=o6.Double, accessLevel=3, userAccessLevel=1)),
    ],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.LossInWeightScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60144"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60148",
    browseName="ns=scales;TargetFlowRate",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60149", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ContinuousScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60148"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60153",
    browseName="ns=scales;ControlMagnitude",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60142", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ContinuousScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60153"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60154",
    browseName="ns=scales;Speed",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60155", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ContinuousScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60154"])
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=60156",
    browseName="EnumStrings",
    parent="ns=scales;i=30003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("Gravimetric_0"), o6.LocalizedText("Volumetric_1")],
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60157",
    browseName="ns=scales;HopperFillLevel",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60158", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.LossInWeightScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60157"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60143",
    browseName="ns=scales;MaximumFeederSpeed",
    description="Defines the maximal possible speed of the feeder.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60159", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
)
o6.reference(scales_objtypes.FeederModuleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60143"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60160",
    browseName="ns=scales;MinimalFeederSpeed",
    description="Defines the minimal possible speed of the feeder.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60161", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
)
o6.reference(scales_objtypes.FeederModuleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60160"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60056",
    browseName="ns=scales;LabelLength",
    description="Defines the length of the labels in stock.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60162", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
)
o6.reference(scales_objtypes.PrinterModuleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60056"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60163",
    browseName="ns=scales;LabelWidth",
    description="Defines the width of the labels in stock.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60164", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
)
o6.reference(scales_objtypes.PrinterModuleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60163"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60165",
    browseName="ns=scales;Tare",
    description="Defines the last occurring tare value at time of statistic.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60166", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=o6.Double,
    value=0.0,
)
o6.reference(scales_objtypes.StatisticType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=60165"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60167",
    browseName="ns=scales;Throughput",
    description="Defines the number of items registered over period of the statistic.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60168", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.UInteger,
)
o6.reference(scales_objtypes.StatisticType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=60167"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60169",
    browseName="ns=scales;PresetTare",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60170", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60169"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60171",
    browseName="ns=scales;PresetHeight",
    description="Defines the predefined height (in direction of global gravity) of the measured item. The value must be write before the item is measured.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60172", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.CatchweigherProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60171"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60173",
    browseName="ns=scales;PresetLength",
    description="Defines the predefined length (in direction of travel) of the measured item. The value must be written before the item is measured.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60174", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.CatchweigherProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60173"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60175",
    browseName="ns=scales;PresetWidth",
    description="Defines the predefined width (in third possible orthogonal direction to height and length) of the measured item. The value must be write before the item is measured.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60176", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.CatchweigherProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60175"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60177",
    browseName="ns=scales;MeasuredHeight",
    description="Defines the maximum height (in direction of travel) of the measured item.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60178", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.WeighingItemType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60177"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60179",
    browseName="ns=scales;MeasuredLength",
    description="Defines the maximum measured length (in direction of travel) of the measured item.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60180", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.WeighingItemType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60179"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60181",
    browseName="ns=scales;MeasuredVolume",
    description="Defines the volume of the item.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60182", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.WeighingItemType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60181"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60183",
    browseName="ns=scales;MeasuredWidth",
    description="Defines the maximum width (in third possible orthogonal direction to height and length) of the measured item.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60184", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.WeighingItemType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60183"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60185",
    browseName="ns=scales;GiveAway",
    description="Defines the totalized value of volume above TargetWeight.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60186", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
)
o6.reference(scales_objtypes.CheckweigherStatisticType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=60185"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60187",
    browseName="ns=scales;SumWeight",
    description="Totalized weight of all items in ItemCount.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60188", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.StatisticCounterType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=60187"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60189",
    browseName="ns=scales;Deviation",
    description="Defines the relative amount of over (positive value) or under (negative value) dosed value in relation of the TargetWeight.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60190", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.AutomaticFillingScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60189"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60191",
    browseName="ns=scales;MaxValue",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60192", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.StatisticCounterType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=60191"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60193",
    browseName="ns=scales;MeanValue",
    description="Mean value of zone measured within this statistic.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60194", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.StatisticCounterType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=60193"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60195",
    browseName="ns=scales;MinValue",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60196", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.StatisticCounterType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=60195"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60197",
    browseName="ns=scales;PercentageOfTotal",
    description="Percentage of this statistic in relation to the total. The total is defined as the duration the product is activated within the scale.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60198", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.StatisticCounterType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=60197"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60199",
    browseName="ns=scales;StandardDeviation",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60200", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.StatisticCounterType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=60199"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60201",
    browseName="ns=scales;LowerLimit",
    description="Defines the lower weight limit of this zone. The lower limit is prior to the upper limit if two zones are beside each other.",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60202", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ZoneType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60201"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60203",
    browseName="ns=scales;UpperLimit",
    description="Defines the upper weight limit of this zone.",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60204", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ZoneType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60203"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60205",
    browseName="ns=scales;LowerLimit",
    description="Defines the lower weight limit of this zone. The lower limit is prior to the upper limit if two zones are beside each other.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60206", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60207",
    browseName="ns=scales;UpperLimit",
    description="Defines the upper weight limit of this zone.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60208", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
scales_objtypes.ZoneType(
    nodeId="ns=scales;i=68",
    browseName="ns=scales;<Zones>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=scales;i=96"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=137",
                browseName="ns=scales;Name",
                description="Defines the user-readable name of the zone.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=60205"]),
        o6.hasComponent(o6.ns["ns=scales;i=60207"]),
    ],
)
o6.reference(scales_objtypes.CatchweigherProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=68"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60209",
    browseName="ns=scales;LowerLimit",
    description="Defines the lower weight limit of this zone. The lower limit is prior to the upper limit if two zones are beside each other.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60210", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60211",
    browseName="ns=scales;UpperLimit",
    description="Defines the upper weight limit of this zone.",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60212", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
scales_objtypes.ZoneType(
    nodeId="ns=scales;i=847",
    browseName="ns=scales;<Zones>",
    displayName="Zones",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=937",
                browseName="ns=scales;Name",
                description="Defines the user-readable name of the zone.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=60209"]),
        o6.hasComponent(o6.ns["ns=scales;i=60211"]),
    ],
)
scales_objtypes.CheckweigherProductType(
    nodeId="ns=scales;i=846",
    browseName="ns=scales;<Product>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=1008",
                browseName="ns=scales;ProductName",
                description="Defines the name of this product.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=801"]),
        o6.hasComponent(o6.ns["ns=scales;i=802"]),
        o6.hasComponent(o6.ns["ns=scales;i=822"]),
        o6.hasComponent(o6.ns["ns=scales;i=831"]),
        o6.hasComponent(o6.ns["ns=scales;i=847"]),
        o6.hasComponent(o6.ns["ns=scales;i=940"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=1007",
                browseName="ns=scales;ProductId",
                description="Defines a unique Id of this product.",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=scales;i=91",
    browseName="ns=scales;Products",
    description="The products used in the scale aggregated in the Products Object.",
    references=[o6.hasComponent(o6.ns["ns=scales;i=846"])],
)
scales_objtypes.ProductionPresetType(
    nodeId="ns=scales;i=850",
    browseName="ns=scales;ProductionPreset",
    description="Contains the productions presets.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=scales;i=91"])],
)
o6.reference(scales_objtypes.CheckweigherType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=850"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60213",
    browseName="ns=scales;MaxFlowRate",
    description="Defines the maximum volume that may be conveyed. Largest volume per time.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60214", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ContinuousScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60213"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60215",
    browseName="ns=scales;MinFlowRate",
    description="Defines the minimum volume that can be conveyed. Smallest volume per time.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60216", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ContinuousScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60215"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60217",
    browseName="ns=scales;MaterialDensity",
    description="Defines the density of the used material.",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60218", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ContinuousProductType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60217"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60219",
    browseName="ns=scales;TargetValue",
    description="Defines the value to be reached of the TargetValue of an aggregate that is referenced by TargetValueId.",
    modellingRule="Mandatory",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60220", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ActivationType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60219"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60225",
    browseName="ns=scales;MinusTolerance",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60226", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_vartypes.TargetItemType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60225"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60227",
    browseName="ns=scales;PlusTolerance",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60228", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_vartypes.TargetItemType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60227"])
scales_vartypes.MeasuredItemType(
    nodeId="ns=scales;i=60150",
    browseName="ns=scales;BinWeight",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60151", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60229", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.LossInWeightScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60150"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60221",
    browseName="ns=scales;LevelMax",
    description="Defines a the maximum fill level where a action is necessary.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60222", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60230", browseName="ns=scales;LevelMode", dataType=scales_datypes.EqualityAndRelationalOperator, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.HopperScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60221"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60223",
    browseName="ns=scales;LevelMin",
    description="Defines a the minimum fill level where a action is necessary.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60224", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60231", browseName="ns=scales;LevelMode", dataType=scales_datypes.EqualityAndRelationalOperator, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.HopperScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60223"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=scales;i=60232",
    browseName="ns=scales;Load",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60233", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(scales_objtypes.ContinuousScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=60232"])
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=50032",
    browseName="ns=scales;<PackagesRejectedBySystem>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60235",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=60234",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
o6.reference(scales_objtypes.CheckweigherStatisticType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=50032"])
scales_objtypes.AcceptedStatisticCounterType(
    nodeId="ns=scales;i=50033",
    browseName="ns=scales;TotalPackagesAccepted",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60237",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=60236",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
o6.reference(scales_objtypes.CheckweigherStatisticType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=50033"])
scales_objtypes.RejectedStatisticCounterType(
    nodeId="ns=scales;i=50034",
    browseName="ns=scales;TotalPackagesRejected",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60239",
                browseName="ns=scales;Weighed",
                description="This flag indicates that the element is considered in the weighed statistic.",
                dataType=o6.Boolean,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=scales;i=60238",
                browseName="ns=scales;ItemCount",
                description="Totalized count of measurements within the scope of this statistic.",
                dataType=ns0.datatypes.UInteger,
                accessLevel=3,
                userAccessLevel=1,
            ),
            "ns=ia;i=4002",
        ),
    ],
)
o6.reference(scales_objtypes.CheckweigherStatisticType, ia.reftypes.HasStatisticComponent, o6.ns["ns=scales;i=50034"])
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=scales;i=50014",
    browseName="ns=di;Identification",
    description="Used to organize parameters for identification of this TopologyElement",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60072",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60073",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=scales;i=60241",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
scales_objtypes.ScaleDeviceType(
    nodeId="ns=scales;i=50001",
    browseName="ns=scales;<ScaleDevice>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60008", browseName="ns=di;DeviceClass", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60009", browseName="ns=di;HardwareRevision", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60016", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60017", browseName="ns=di;Model", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60018", browseName="ns=di;SerialNumber", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60019", browseName="ns=di;SoftwareRevision", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=scales;i=50002"]),
        o6.hasComponent(o6.ns["ns=scales;i=60001"]),
        o6.hasAddIn(o6.ns["ns=scales;i=50014"]),
    ],
    _allow_abstract=True,
)
di.objtypes.ConfigurableObjectType(
    nodeId="ns=scales;i=837",
    browseName="ns=scales;SubDevices",
    description="The Scales must be a subtype of the ScaleDeviceType but must not be from the same type.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=scales;i=838",
                browseName="ns=di;SupportedTypes",
                description="Folder maintaining the set of (sub-types of) BaseObjectTypes that can be instantiated in the ConfigurableComponent.",
            )
        ),
        o6.hasComponent(o6.ns["ns=scales;i=50001"]),
    ],
)
o6.reference(scales_objtypes.ScaleSystemType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=837"])


ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=60023",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=70001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=60024",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=70001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="CompletionStateMachine", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=70001", browseName="CloseAndCommit", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=60023"]), outputArgs=o6.hasProperty(o6.ns["ns=scales;i=60024"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=60025",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=70002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=ns0.datatypes.BaseDataType, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=60026",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=70002",
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
o6.call(nodeId="ns=scales;i=70002", browseName="GenerateFileForRead", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=60025"]), outputArgs=o6.hasProperty(o6.ns["ns=scales;i=60026"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=60027",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=70003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="GenerateOptions", dataType=ns0.datatypes.BaseDataType, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=60028",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=70003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileNodeId", dataType=o6.NodeId, valueRank=-1), ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=70003", browseName="GenerateFileForWrite", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=60027"]), outputArgs=o6.hasProperty(o6.ns["ns=scales;i=60028"]))

ns0.objtypes.TemporaryFileTransferType(
    nodeId="ns=scales;i=50004",
    browseName="ns=scales;RecipeUpload",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60004", browseName="ClientProcessingTimeout", dataType=ns0.datatypes.Duration)),
        o6.hasComponent(o6.ns["ns=scales;i=70001"]),
        o6.hasComponent(o6.ns["ns=scales;i=70002"]),
        o6.hasComponent(o6.ns["ns=scales;i=70003"]),
    ],
)
scales_objtypes.RecipeManagementType(
    nodeId="ns=scales;i=127",
    browseName="ns=scales;Recipes",
    description="Defines a folder that contains all recipes. Elements in this folder must have the RecipeType.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(o6.ns["ns=scales;i=74"]),
        o6.hasComponent(o6.ns["ns=scales;i=450"]),
        o6.hasComponent(o6.ns["ns=scales;i=452"]),
        o6.hasComponent(o6.ns["ns=scales;i=50004"]),
    ],
)
o6.reference(scales_objtypes.RecipeScaleType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=127"])


ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=60035",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=70004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=70004", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=60035"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=60036",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=70005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=60037",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=70005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=70005", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=60036"]), outputArgs=o6.hasProperty(o6.ns["ns=scales;i=60037"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=60038",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=70006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=60039",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=70006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=70006", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=60038"]), outputArgs=o6.hasProperty(o6.ns["ns=scales;i=60039"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=60041",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=70007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=60042",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=70007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=70007", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=60041"]), outputArgs=o6.hasProperty(o6.ns["ns=scales;i=60042"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=60043",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=70008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=70008", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=60043"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=60047",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=70009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=70009", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=60047"]))

ns0.objtypes.FileType(
    nodeId="ns=scales;i=50006",
    browseName="ns=scales;RecipeFile",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60040", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60044", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60045", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=scales;i=60046", browseName="Writable", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=scales;i=70004"]),
        o6.hasComponent(o6.ns["ns=scales;i=70005"]),
        o6.hasComponent(o6.ns["ns=scales;i=70006"]),
        o6.hasComponent(o6.ns["ns=scales;i=70007"]),
        o6.hasComponent(o6.ns["ns=scales;i=70008"]),
        o6.hasComponent(o6.ns["ns=scales;i=70009"]),
    ],
)
o6.reference(scales_objtypes.RecipeType, ns0.reftypes.HasComponent, o6.ns["ns=scales;i=50006"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, pack_ml, scales_reftypes, scales_datypes, scales_vartypes, scales_objtypes
