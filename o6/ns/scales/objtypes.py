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

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=scales;i=23",
    browseName="ns=scales;WeighingRangeElementType",
    displayName="WeighingRangeElementType",
    description="For each weighing range a scale supports the OPC UA server provides an object of WeighingRangeElementType that contains the propertys of the weighing range like the ScaleDivision.",
)
class WeighingRangeElementType(ns0.objtypes.BaseObjectType):
    actualScaleInterval: ns0.vartypes.AnalogUnitType
    range: ns0.vartypes.BaseDataVariableType
    verificationScaleInterval: ns0.vartypes.AnalogUnitType


@o6.objecttype(
    nodeId="ns=scales;i=32",
    browseName="ns=scales;RecipeElementType",
    displayName="RecipeElementType",
    description="Represents a step, process or action in a recipe.",
    isAbstract=True,
)
class RecipeElementType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(
    nodeId="ns=scales;i=33",
    browseName="ns=scales;UserInstructionType",
    displayName="UserInstructionType",
    description="UserInstructionType represents a recipe step that requires user interaction. The recipe scale display instruction (a text and/or some application- specific symbols) on an HMI and waits until the user acknowledged the instruction.",
)
class UserInstructionType(RecipeElementType):
    displayText: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=292",
            browseName="ns=scales;DisplayText",
            description="Defines instructions for this RecipeElement that will be displayed to the user.",
            dataType=o6.LocalizedText,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    instructionId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=293",
            browseName="ns=scales;InstructionId",
            description="Defines a unique Id used to identify the instruction that is displayed via DisplayText.",
            dataType=ns0.datatypes.UInteger,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=scales;i=34",
    browseName="ns=scales;WeighingType",
    displayName="WeighingType",
    description="Represents a weighing process in a recipe. The process can be an automatic or manual filling process.",
)
class WeighingType(RecipeElementType):
    material: MaterialType | None
    targetWeight: scales_vartypes.TargetItemType
    weighingModuleNodeId: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=297",
            browseName="ns=scales;WeighingModuleNodeId",
            description="Defines the Id of the load cell which is used for weighing the product.",
            dataType=o6.NodeId,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=scales;i=36",
    browseName="ns=scales;TimerType",
    displayName="TimerType",
    description="TimerType represents a timer step in a recipe. The recipe waits until at least Duration has passed from now.",
)
class TimerType(RecipeElementType):
    duration: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=298",
            browseName="ns=scales;Duration",
            description="Defines the period of time the processing needs to wait before processing the next RecipeElement.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=scales;i=40", browseName="ns=scales;ActivationType", displayName="ActivationType", description="Represents an activation step in a recipe.")
class ActivationType(RecipeElementType):
    targetValue: ns0.vartypes.AnalogUnitType
    targetValueId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=306",
            browseName="ns=scales;TargetValueId",
            description="Defines a unique Id of the aggregate that is being activated. A list of all possible TargetValueIds is defined in RecipeScaleDeviceType.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    targetValueNodeId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=307", browseName="ns=scales;TargetValueNodeId", dataType=o6.NodeId, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=scales;i=35", browseName="ns=scales;MaterialType", displayName="MaterialType", description="Represents a material.")
class MaterialType(ns0.objtypes.BaseObjectType):
    materialId: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=309",
            browseName="ns=scales;MaterialId",
            description="Defines a unique identifier for the material.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    materialName: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=308",
            browseName="ns=scales;MaterialName",
            description="Defines a user-readable name of the material.",
            dataType=o6.LocalizedText,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=scales;i=41",
    browseName="ns=scales;MaterialAutomaticType",
    displayName="MaterialAutomaticType",
    description="Represents a material in a recipe that will be filled automatically.",
)
class MaterialAutomaticType(MaterialType):
    fillingProductInformation: AutomaticFillingProductType


@o6.objecttype(nodeId="ns=scales;i=42", browseName="ns=scales;ZoneType", displayName="ZoneType", description="Container for the weighing zones in a Checkweigher.")
class ZoneType(ns0.objtypes.BaseObjectType):
    lowerLimit: ns0.vartypes.AnalogUnitType
    name: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=311",
            browseName="ns=scales;Name",
            description="Defines the user-readable name of the zone.",
            dataType=o6.LocalizedText,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    upperLimit: ns0.vartypes.AnalogUnitType
    zoneStatistic: StatisticCounterType | None


@o6.objecttype(
    nodeId="ns=scales;i=43",
    browseName="ns=scales;StatisticCounterType",
    displayName="StatisticCounterType",
    description="Container for the different statisticvalues needed in a Checkweigher.",
)
class StatisticCounterType(ns0.objtypes.BaseObjectType):
    itemCount: ns0.vartypes.BaseDataVariableType = o6.reference(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=317",
            browseName="ns=scales;ItemCount",
            description="Totalized count of measurements within the scope of this statistic.",
            dataType=ns0.datatypes.UInteger,
            accessLevel=3,
            userAccessLevel=1,
        ),
        "ns=ia;i=4002",
    )
    maxValue: ns0.vartypes.AnalogUnitType | None
    meanValue: ns0.vartypes.AnalogUnitType | None
    minValue: ns0.vartypes.AnalogUnitType | None
    percentageOfTotal: ns0.vartypes.AnalogUnitType | None
    standardDeviation: ns0.vartypes.AnalogUnitType | None
    sumWeight: ns0.vartypes.AnalogUnitType | None
    weighed: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=162",
            browseName="ns=scales;Weighed",
            description="This flag indicates that the element is considered in the weighed statistic.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=scales;i=27", browseName="ns=scales;TotalizerType", displayName="TotalizerType", description="Contains the sum over the last measurement results.")
class TotalizerType(ns0.objtypes.BaseObjectType):
    resetTotalizer: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=scales;i=451",
            browseName="ns=scales;ResetTotalizer",
            description="Resets the TotalizedValue of this totalizer object. Only useful if reset is not related to a period of time.",
        )
    )
    totalizedValue: scales_vartypes.MeasuredItemType


ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=337",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=453",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="FeederSpeed", dataType=o6.Float, valueRank=-1),
        ns0.datatypes.Argument(name="EngineeringUnits", dataType=ns0.datatypes.EUInformation, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=scales;i=453",
    browseName="ns=scales;SetFeederSpeed",
    description="Allows to set a new value for the speed of the feeder system. The OPC UA server must check if the value is between the minimal and maximum allowed speed and if the unit is allowed.",
    inputArgs=o6.hasProperty(o6.ns["ns=scales;i=337"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=181",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=456",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="RecipeId", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="RecipeName", dataType=o6.LocalizedText, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=182",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=456",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RecipeNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=scales;i=456",
    browseName="ns=scales;AddRecipe",
    description="Method to add an additional recipe of RecipeType.",
    inputArgs=o6.hasProperty(o6.ns["ns=scales;i=181"]),
    outputArgs=o6.hasProperty(o6.ns["ns=scales;i=182"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=373",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=458",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RecipeNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=458", browseName="ns=scales;StartRecipe", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=373"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=180",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=459",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RecipeId", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=459", browseName="ns=scales;RemoveRecipe", description="Method to remove a recipe of RecipeType.", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=180"]))


@o6.objecttype(
    nodeId="ns=scales;i=30",
    browseName="ns=scales;RecipeManagementType",
    displayName="RecipeManagementType",
    description="Contains methods and properties required for managing recipes.",
)
class RecipeManagementType(ns0.objtypes.BaseObjectType):
    addRecipe: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=456"])
    langleRecipe_NoRangle: RecipeType | None
    removeRecipe: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=459"])


ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=398",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=460",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TargetItemCount", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=460", browseName="ns=scales;SetTargetItemCount", description="Set the number of TargetItemCount.", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=398"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=175",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=464",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductId", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=464", browseName="ns=scales;SelectProduct", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=175"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=437",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=465",
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
    nodeId="ns=scales;i=438",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=465",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ElementNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=465", browseName="ns=scales;AddRecipeElement", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=437"]), outputArgs=o6.hasProperty(o6.ns["ns=scales;i=438"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=439",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=466",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RecipeElementNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=466", browseName="ns=scales;RemoveRecipeElement", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=439"]))


@o6.objecttype(
    nodeId="ns=scales;i=31",
    browseName="ns=scales;RecipeType",
    displayName="RecipeType",
    description="Represents a recipe. It defines additional methods and properties required for managing a recipe.",
)
class RecipeType(ns0.objtypes.BaseObjectType):
    addRecipeElement: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=465"])
    recipeElements: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(
            nodeId="ns=scales;i=82", browseName="ns=scales;RecipeElements", description="Defines a Placeholder for all RecipeElements that are part of the Recipe."
        )
    )
    recipeFile: ns0.objtypes.FileType | None
    recipeId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=288",
            browseName="ns=scales;RecipeId",
            description="RecipeId defines a unique identifier of a recipe.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    recipeName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=287",
            browseName="ns=scales;RecipeName",
            description="Defines a user-readable name of the recipe.",
            dataType=o6.LocalizedText,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    removeRecipeElement: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=466"])


ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=145",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=525",
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
    nodeId="ns=scales;i=146",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=525",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ZoneNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=scales;i=525",
    browseName="ns=scales;AddZone",
    description="Adds a zone to the zone array.",
    inputArgs=o6.hasProperty(o6.ns["ns=scales;i=145"]),
    outputArgs=o6.hasProperty(o6.ns["ns=scales;i=146"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=147",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=526",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ZoneNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=526", browseName="ns=scales;RemoveZone", description="Removes a zone from the zone array.", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=147"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=176",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=576",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductId", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=576", browseName="ns=scales;DeselectProduct", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=176"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=184",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=577",
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
    nodeId="ns=scales;i=577",
    browseName="ns=scales;SetTargetPieceCount",
    description="Sets the value of TargetPieceCount. See TargetPieceCount.",
    inputArgs=o6.hasProperty(o6.ns["ns=scales;i=184"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1013",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=602",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NumberOfReferencePieces", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(
    nodeId="ns=scales;i=602", browseName="ns=scales;StartReference", description="Triggers the reference weighing process.", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=1013"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=604",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=603",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="ReferencePieceWeight", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="EngineeringUnits", dataType=ns0.datatypes.EUInformation, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=scales;i=603",
    browseName="ns=scales;SetReferencePieceWeight",
    description="Sets the value for the ReferencePieceWeight (product-specific data).",
    inputArgs=o6.hasProperty(o6.ns["ns=scales;i=604"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=177",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=638",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductNodeId", dataType=o6.NodeId, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=246",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=638",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ProductName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ProductId", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ProductType", dataType=o6.NodeId, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=scales;i=638",
    browseName="ns=scales;AddProduct",
    description="Creates an object with the JobType from the address space.",
    inputArgs=o6.hasProperty(o6.ns["ns=scales;i=246"]),
    outputArgs=o6.hasProperty(o6.ns["ns=scales;i=177"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=647",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=646",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductId", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=scales;i=646",
    browseName="ns=scales;RemoveProduct",
    description="Removes an object with the JobType from the address space.",
    inputArgs=o6.hasProperty(o6.ns["ns=scales;i=647"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=759",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=758",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Shield", dataType=o6.NodeId("ns=scales;i=65"), valueRank=-1)],
)
o6.call(
    nodeId="ns=scales;i=758",
    browseName="ns=scales;OpenDraftShields",
    description="Method to open a certain or all draft shields.",
    inputArgs=o6.hasProperty(o6.ns["ns=scales;i=759"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=762",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=761",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Shield", dataType=o6.NodeId("ns=scales;i=65"), valueRank=-1)],
)
o6.call(
    nodeId="ns=scales;i=761",
    browseName="ns=scales;CloseDraftShields",
    description="Method to close a certain or all draft shields.",
    inputArgs=o6.hasProperty(o6.ns["ns=scales;i=762"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1014",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=783",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RecipeNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=783", browseName="ns=scales;StopRecipe", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=1014"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1015",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=784",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RecipeNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=784", browseName="ns=scales;ContinueRecipe", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=1015"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1016",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=785",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RecipeNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=785", browseName="ns=scales;SkipCurrentRecipeElement", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=1016"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1017",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=786",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RecipeNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=786", browseName="ns=scales;AbortRecipe", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=1017"]))


@o6.objecttype(nodeId="ns=scales;i=13", browseName="ns=scales;ScaleEventType", displayName="ScaleEventType")
class ScaleEventType(ns0.objtypes.BaseEventType):
    auxParameters: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=312", browseName="ns=scales;AuxParameters", dataType=o6.String, valueRank=1, arrayDimensions=[1], accessLevel=3, userAccessLevel=1
        )
    )
    helpSource: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=319", browseName="ns=scales;HelpSource", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    notificationCategory: ns0.vartypes.MultiStateValueDiscreteType
    notificationId: ns0.vartypes.MultiStateValueDiscreteType
    vendorNotificationId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=scales;i=948", browseName="ns=scales;VendorNotificationId", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=scales;i=11", browseName="ns=scales;ProductType", displayName="ProductType", description="Represents a product related to the scale.", isAbstract=True)
class ProductType(ns0.objtypes.BaseObjectType):
    batchId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=648", browseName="ns=scales;BatchId", description="Defines a unique Id of this Batch.", dataType=o6.String, accessLevel=3, userAccessLevel=1
        )
    )
    batchName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=649", browseName="ns=scales;BatchName", description="Defines the name of this Batch.", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1
        )
    )
    jobId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=185", browseName="ns=scales;JobId", description="Defines a unique Id of this job.", dataType=o6.String, accessLevel=3, userAccessLevel=1
        )
    )
    jobName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=310", browseName="ns=scales;JobName", description="Defines the name of this job.", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1
        )
    )
    lock: di.objtypes.LockingServicesType | None
    presetTare: ns0.vartypes.AnalogUnitType | None
    productId: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=963", browseName="ns=scales;ProductId", description="Defines a unique Id of this product.", dataType=o6.String, accessLevel=3, userAccessLevel=1
        )
    )
    productMode: ns0.vartypes.TwoStateDiscreteType | None
    productName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=166",
            browseName="ns=scales;ProductName",
            description="Defines the name of this product.",
            dataType=o6.LocalizedText,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    statistic: StatisticType | None


@o6.objecttype(
    nodeId="ns=scales;i=12", browseName="ns=scales;PieceCountingProductType", displayName="PieceCountingProductType", description="Represents a product of a piece counting scale."
)
class PieceCountingProductType(ProductType):
    currentItemCount: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=261",
            browseName="ns=scales;CurrentItemCount",
            description="Defines the current number of items that are captured by the scale.",
            dataType=ns0.datatypes.UInteger,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    feedRateMeasuringInterval: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=597",
            browseName="ns=scales;FeedRateMeasuringInterval",
            description="Defines the measurement interval for evaluating the current flowrate.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    fillingTime: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=274",
            browseName="ns=scales;FillingTime",
            description="Defines the interval during which the filling has to be completed.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    fineFeedCount: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=scales;i=376", browseName="ns=scales;FineFeedCount", dataType=ns0.datatypes.UInteger, accessLevel=3, userAccessLevel=1)
    )
    inFlightCount: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=578",
            browseName="ns=scales;InFlightCount",
            description="Defines the number of items that is behind valve / in flight after feeding is stopped.",
            dataType=ns0.datatypes.UInteger,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    jogFeed: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=589",
            browseName="ns=scales;JogFeed",
            description="Defines if an additional dosage is necessary.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    minimumDeltaPerFeedRateMeasuringInterval: ns0.vartypes.AnalogItemType | None
    numberOfReferencePieces: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=167",
            browseName="ns=scales;NumberOfReferencePieces",
            description="Defines the number of pieces that need to be used for reference process.",
            dataType=ns0.datatypes.UInteger,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    referencePieceWeight: ns0.vartypes.AnalogItemType
    registeredPieceCount: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=579",
            browseName="ns=scales;RegisteredPieceCount",
            description="Defines the number of pieces that were actually counted related to the ReferencePieceWeight.",
            dataType=ns0.datatypes.UInteger,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    setTargetItemCount: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=460"])
    setTargetPieceCount: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=577"])
    settlingTime: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=580",
            browseName="ns=scales;SettlingTime",
            description="Defines the time that needs to be passed before measurement process can be triggered.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    tareId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=592",
            browseName="ns=scales;TareId",
            description="Defines the Id of tare value for the current product or item.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    targetItemCount: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=587",
            browseName="ns=scales;TargetItemCount",
            description="Defines the number of items that are supposed to be counted during the measurement process.",
            dataType=ns0.datatypes.UInteger,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    targetPieceCount: scales_vartypes.TargetItemType | None
    totalizedItemCount: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=581",
            browseName="ns=scales;TotalizedItemCount",
            description="Defines the summed up number of items. Will be reset either triggered by the user or a different product selection.",
            dataType=ns0.datatypes.UInteger,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    totalizedWeight: scales_vartypes.WeightItemType | None


@o6.objecttype(
    nodeId="ns=scales;i=16",
    browseName="ns=scales;AutomaticFillingProductType",
    displayName="AutomaticFillingProductType",
    description="Represents a product of an automatic filling scale.",
)
class AutomaticFillingProductType(ProductType):
    feedRateMeasuringInterval: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=552",
            browseName="ns=scales;FeedRateMeasuringInterval",
            description="Defines the measuring interval for evaluating the current flowrate.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    fillingTime: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=551",
            browseName="ns=scales;FillingTime",
            description="Defines the maximal duration for the filling process to take place. Needs to be completed during this period.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    fineFeedWeight: ns0.vartypes.AnalogItemType | None
    inFlightWeight: ns0.vartypes.AnalogItemType
    jogFeed: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=549",
            browseName="ns=scales;JogFeed",
            description="Defines if an additional dosage is necessary.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    minimumDeltaPerFeedRateMeasuringInterval: ns0.vartypes.AnalogItemType | None
    settlingTime: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=547",
            browseName="ns=scales;SettlingTime",
            description="Defines the time that needs to be passed before measurement process can be triggered.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    tareId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=555",
            browseName="ns=scales;TareId",
            description="Defines an Id of tare value for the current product or item.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    targetWeight: scales_vartypes.TargetItemType


@o6.objecttype(
    nodeId="ns=scales;i=17", browseName="ns=scales;CatchweigherProductType", displayName="CatchweigherProductType", description="Represents a product of a Catchweigher."
)
class CatchweigherProductType(ProductType):
    addZone: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=525"])
    langleZonesRangle: ZoneType | None
    lastItem: WeighingItemType | None
    presetHeight: ns0.vartypes.AnalogUnitType | None
    presetLength: ns0.vartypes.AnalogUnitType | None
    presetWidth: ns0.vartypes.AnalogUnitType | None
    removeZone: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=526"])
    targetThroughput: scales_vartypes.TargetItemType | None


@o6.objecttype(
    nodeId="ns=scales;i=18", browseName="ns=scales;ContinuousProductType", displayName="ContinuousProductType", description="Represents a product of a continuous scale."
)
class ContinuousProductType(ProductType):
    materialDensity: ns0.vartypes.AnalogUnitType | None
    targetFlowRate: scales_vartypes.TargetItemType | None
    targetWeight: scales_vartypes.TargetItemType | None


@o6.objecttype(nodeId="ns=scales;i=19", browseName="ns=scales;RecipeProductType", displayName="RecipeProductType", description="Represents a product of a recipe scale.")
class RecipeProductType(ProductType):
    recipeNodeId: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=633",
            browseName="ns=scales;RecipeNodeId",
            description="Defines the NodeId of the recipe that is being produced.",
            dataType=o6.NodeId,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    report: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=632",
            browseName="ns=scales;Report",
            description="Defines an array with the various messages from the recipe. Each RecipeElement generates its own report message.",
            dataType=scales_datypes.RecipeReportElementType,
            valueRank=1,
            arrayDimensions=[1],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    reportFile: ns0.objtypes.FileType | None


@o6.objecttype(
    nodeId="ns=scales;i=22",
    browseName="ns=scales;TotalizingHopperProductType",
    displayName="TotalizingHopperProductType",
    description="Represents a product of a totalizing hopper scale.",
)
class TotalizingHopperProductType(ProductType):
    tipCounter: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=637",
            browseName="ns=scales;TipCounter",
            description="Defines the number of fillings (downpour, bulk produce)",
            dataType=ns0.datatypes.UInteger,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    volumeTargetValue: scales_vartypes.TargetItemType | None


@o6.objecttype(
    nodeId="ns=scales;i=46", browseName="ns=scales;CheckweigherProductType", displayName="CheckweigherProductType", description="Represents a product of a Checkweigher."
)
class CheckweigherProductType(CatchweigherProductType):
    lowerToleranceLimit1: ns0.vartypes.AnalogUnitType | None
    lowerToleranceLimit2: ns0.vartypes.AnalogUnitType | None
    nominalWeight: scales_vartypes.TargetItemType
    statistic: CheckweigherStatisticType | None


@o6.objecttype(
    nodeId="ns=scales;i=47",
    browseName="ns=scales;AutomaticWeightPriceLabelerProductType",
    displayName="AutomaticWeightPriceLabelerProductType",
    description="Represents a product of a automatic weight-price-labeler.",
)
class AutomaticWeightPriceLabelerProductType(CatchweigherProductType):
    lastItem: PriceItemType | None
    unitPrice: ns0.vartypes.BaseDataVariableType | None


@o6.objecttype(
    nodeId="ns=scales;i=25",
    browseName="ns=scales;StatisticType",
    displayName="StatisticType",
    description="Container for the different statisticvalues. All variables are optional, so that the statistics can be instantiated application-specific.",
    interfaces=[ia.objtypes.IAggregateStatisticsType],
)
class StatisticType(ns0.objtypes.BaseObjectType):
    lastItem: WeighingItemType | None
    resetCondition: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=986",
            browseName="ns=ia;ResetCondition",
            description="The reason and context for the reset of the statistics, which is done without a trigger from an OPC UA Client, like calling the ResetStatistics Method. ResetCondition is a vendor-specific, human readable string. ResetCondition is non-localized and might contain an expression that can be parsed by certain clients. Examples are: “AFTER 4 HOURS”, “AFTER 1000 ITEMS”, “OPERATOR”. “OPERATOR” means, that an operator resets the statistics on a local HMI.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    startTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=283",
            browseName="ns=ia;StartTime",
            description="Indicates the point in time at which the collection of the statistical data has been started.",
            dataType=o6.DateTime,
        )
    )
    tare: ns0.vartypes.AnalogUnitType | None
    throughput: ns0.vartypes.AnalogUnitType | None
    totalPackages: StatisticCounterType | None
    totalPackagesWeighed: StatisticCounterType | None


@o6.objecttype(nodeId="ns=scales;i=48", browseName="ns=scales;CheckweigherStatisticType", displayName="CheckweigherStatisticType")
class CheckweigherStatisticType(StatisticType):
    giveAway: ns0.vartypes.AnalogUnitType | None
    langlePackagesAcceptedWithPropertyRangle: AcceptedStatisticCounterType | None
    langlePackagesRejectedBySystemRangle: RejectedStatisticCounterType | None
    packagesAcceptedWithLowerToleranceLimit1: AcceptedStatisticCounterType | None
    packagesRejectedByDistanceFault: RejectedStatisticCounterType | None
    packagesRejectedByLength: RejectedStatisticCounterType | None
    packagesRejectedByLowerToleranceLimit1: RejectedStatisticCounterType | None
    packagesRejectedByLowerToleranceLimit2: RejectedStatisticCounterType | None
    packagesRejectedByMeanValueRequirement: RejectedStatisticCounterType | None
    packagesRejectedByMetal: RejectedStatisticCounterType | None
    packagesRejectedByVision: RejectedStatisticCounterType | None
    packagesRejectedByXRay: RejectedStatisticCounterType | None
    percentageLowerToleranceLimit: ns0.vartypes.AnalogItemType | None
    totalPackagesAccepted: AcceptedStatisticCounterType | None
    totalPackagesRejected: RejectedStatisticCounterType | None


@o6.objecttype(nodeId="ns=scales;i=20", browseName="ns=scales;SimpleProductType", displayName="SimpleProductType", description="Represents a product of a simple scale.")
class SimpleProductType(ProductType):
    containerId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=1012", browseName="ns=scales;ContainerId", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    unitPrice: ns0.vartypes.BaseDataVariableType | None


@o6.objecttype(nodeId="ns=scales;i=21", browseName="ns=scales;ScaleAlarmType", displayName="ScaleAlarmType")
class ScaleAlarmType(ns0.objtypes.AlarmConditionType):
    auxParameters: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=763", browseName="ns=scales;AuxParameters", dataType=o6.String, valueRank=1, arrayDimensions=[1], accessLevel=3, userAccessLevel=1
        )
    )
    helpSource: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=764", browseName="ns=scales;HelpSource", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    notificationCategory: ns0.vartypes.MultiStateValueDiscreteType
    notificationId: ns0.vartypes.MultiStateValueDiscreteType
    vendorNotificationId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=scales;i=1020", browseName="ns=scales;VendorNotificationId", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=988",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1021",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductId", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=1021", browseName="ns=scales;SwitchProduct", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=988"]))


@o6.objecttype(
    nodeId="ns=scales;i=14", browseName="ns=scales;ProductionPresetType", displayName="ProductionPresetType", description="Provides methods to manage the Production preset."
)
class ProductionPresetType(ns0.objtypes.BaseObjectType):
    addProduct: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=638"])
    currentProducts: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=436", browseName="ns=scales;CurrentProducts", dataType=o6.String, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
        )
    )
    deselectProduct: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=576"])
    products: ns0.objtypes.FolderType | None
    removeProduct: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=646"])
    selectProduct: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=464"])
    switchProduct: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=1021"])


ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=946",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="VehicleId", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=1022", browseName="ns=scales;InboundWeighing", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=946"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=947",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1023",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="VehicleId", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=1023", browseName="ns=scales;OutboundWeighing", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=947"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=949",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1024",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="VehicleId", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=1024", browseName="ns=scales;OnePassWeighing", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=949"]))

ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=990",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1026",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NumberOfReferencePieces", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=1026", browseName="ns=scales;SetNumberOfReferencePieces", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=990"]))


@o6.objecttype(nodeId="ns=scales;i=1027", browseName="ns=scales;AcceptedStatisticCounterType", displayName="AcceptedStatisticCounterType")
class AcceptedStatisticCounterType(StatisticCounterType):
    pass


@o6.objecttype(nodeId="ns=scales;i=1028", browseName="ns=scales;RejectedStatisticCounterType", displayName="RejectedStatisticCounterType")
class RejectedStatisticCounterType(StatisticCounterType):
    pass


@o6.objecttype(nodeId="ns=scales;i=24", browseName="ns=scales;WeighingItemType", displayName="WeighingItemType")
class WeighingItemType(ns0.objtypes.BaseObjectType):
    itemId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=248",
            browseName="ns=scales;ItemId",
            description="Defines a unique number that is assigned to an item.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    measuredHeight: ns0.vartypes.AnalogUnitType | None
    measuredLength: ns0.vartypes.AnalogUnitType | None
    measuredVolume: ns0.vartypes.AnalogUnitType | None
    measuredWeight: scales_vartypes.WeightItemType
    measuredWidth: ns0.vartypes.AnalogUnitType | None
    zoneName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=1029", browseName="ns=scales;ZoneName", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=scales;i=833", browseName="ns=scales;PriceItemType", displayName="PriceItemType")
class PriceItemType(WeighingItemType):
    itemPrice: ns0.vartypes.BaseDataVariableType | None


ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1208",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1396",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="VehicleId", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=scales;i=1396", browseName="ns=scales;GetVehicleInformation", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=1208"]))


@o6.objecttype(nodeId="ns=scales;i=832", browseName="ns=scales;VehicleProductType", displayName="VehicleProductType")
class VehicleProductType(ProductType):
    carrierDisplayName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=858", browseName="ns=scales;CarrierDisplayName", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
    )
    carrierId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=859", browseName="ns=scales;CarrierId", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    customer: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=860", browseName="ns=scales;Customer", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
    )
    deltaWeight: scales_vartypes.WeightItemType
    destination: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=870", browseName="ns=scales;Destination", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
    )
    driverDisplayName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=871", browseName="ns=scales;DriverDisplayName", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
    )
    driverId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=872", browseName="ns=scales;DriverId", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    getVehicleInformation: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=1396"])
    inboundScale: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=874", browseName="ns=scales;InboundScale", dataType=o6.NodeId, accessLevel=3, userAccessLevel=1)
    )
    inboundWeight: scales_vartypes.WeightItemType | None
    material: MaterialType | None
    outboundScale: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=877", browseName="ns=scales;OutboundScale", dataType=o6.NodeId, accessLevel=3, userAccessLevel=1)
    )
    outboundWeight: scales_vartypes.WeightItemType
    scaleOperatorId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=896", browseName="ns=scales;ScaleOperatorId", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    supplier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=897", browseName="ns=scales;Supplier", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
    )
    tare: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=1117", browseName="ns=scales;Tare", dataType=ns0.datatypes.Number, accessLevel=3, userAccessLevel=1)
    )
    tareExpirationDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=898", browseName="ns=scales;TareExpirationDate", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)
    )
    totalWeight: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=1210", browseName="ns=scales;TotalWeight", dataType=scales_datypes.WeightType, accessLevel=3, userAccessLevel=1)
    )
    totalWeightResetDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=873", browseName="ns=scales;TotalWeightResetDate", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)
    )
    vehicleId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=900", browseName="ns=scales;VehicleId", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=scales;i=1353",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=scales;i=1407",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="PresetTare", dataType=o6.Double, valueRank=-1),
        ns0.datatypes.Argument(name="EngineeringUnits", dataType=ns0.datatypes.EUInformation, valueRank=-1),
    ],
)
o6.call(nodeId="ns=scales;i=1407", browseName="ns=scales;SetPresetTare", inputArgs=o6.hasProperty(o6.ns["ns=scales;i=1353"]))

ns0.objtypes.FolderType(nodeId="ns=scales;i=50019", browseName="ns=machinery;MachineryBuildingBlocks")


@o6.objecttype(
    nodeId="ns=scales;i=28",
    browseName="ns=scales;FeederModuleType",
    displayName="FeederModuleType",
    description="Represents a feeder system. A feeder system is a subdevice of an automatic scale for conveying the product to or from the WeighingBridge.",
)
class FeederModuleType(di.objtypes.ComponentType):
    feederLoad: scales_vartypes.MeasuredItemType | None
    feederRunning: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=925", browseName="ns=scales;FeederRunning", description="Indicates that the feeder system is running.", dataType=o6.Boolean)
    )
    feederSpeed: scales_vartypes.TargetItemType | None
    identification: machinery.objtypes.MachineryItemIdentificationType
    machineryBuildingBlocks: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=scales;i=50019"])
    machineryItemState: machinery.objtypes.MachineryItemState_StateMachineType | None
    machineryOperationMode: machinery.objtypes.MachineryOperationModeStateMachineType | None
    maximumFeederSpeed: ns0.vartypes.AnalogUnitType | None
    minimalFeederSpeed: ns0.vartypes.AnalogUnitType | None
    setFeederSpeed: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=453"])


ns0.objtypes.FolderType(nodeId="ns=scales;i=50020", browseName="ns=machinery;MachineryBuildingBlocks")


@o6.objecttype(
    nodeId="ns=scales;i=29",
    browseName="ns=scales;PrinterModuleType",
    displayName="PrinterModuleType",
    description="Represents a printing device. A printing device is a subdevice of a scale, that prints labels or other documents releated to the scale or the measurement results.",
)
class PrinterModuleType(di.objtypes.ComponentType):
    identification: machinery.objtypes.MachineryItemIdentificationType
    labelLength: ns0.vartypes.AnalogUnitType | None
    labelStock: ns0.vartypes.AnalogItemType | None
    labelTypeId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=351", browseName="ns=scales;LabelTypeId", description="Defines the Id of the label to be printed.", dataType=o6.String
        )
    )
    labelWidth: ns0.vartypes.AnalogUnitType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=scales;i=50020"])
    machineryItemState: machinery.objtypes.MachineryItemState_StateMachineType | None
    machineryOperationMode: machinery.objtypes.MachineryOperationModeStateMachineType | None
    printMediaStock: ns0.vartypes.AnalogItemType | None


ns0.objtypes.FolderType(nodeId="ns=scales;i=50021", browseName="ns=machinery;MachineryBuildingBlocks")
ns0.objtypes.FolderType(nodeId="ns=scales;i=50022", browseName="ns=machinery;MachineryBuildingBlocks")


@o6.objecttype(
    nodeId="ns=scales;i=44", browseName="ns=scales;ScaleSystemType", displayName="ScaleSystemType", description="Represents a scale system and contains one or more scales."
)
class ScaleSystemType(di.objtypes.ComponentType):
    identification: machinery.objtypes.MachineIdentificationType
    machineryBuildingBlocks: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=scales;i=50022"])
    machineryItemState: machinery.objtypes.MachineryItemState_StateMachineType | None
    machineryOperationMode: machinery.objtypes.MachineryOperationModeStateMachineType | None
    policy: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=140",
            browseName="ns=scales;Policy",
            description="Defines the legal guidelines that apply for the scale or need to be complied by the scale.",
            dataType=o6.LocalizedText,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    processStateId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=356",
            browseName="ns=scales;ProcessStateId",
            description="Contains an relating identification for the occurring ProcessStateMessage.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    processStateMessage: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=357",
            browseName="ns=scales;ProcessStateMessage",
            description="Contains the message of the current overall state of the scale.",
            dataType=o6.LocalizedText,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    productionOutput: StatisticType | None = o6.hasComponent(StatisticType(nodeId="ns=scales;i=79", browseName="ns=scales;ProductionOutput"))
    productionPreset: ProductionPresetType | None = o6.hasComponent(
        ProductionPresetType(nodeId="ns=scales;i=70", browseName="ns=scales;ProductionPreset", description="Contains the productions presets.")
    )
    resetGlobalStatistics: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=scales;i=1025", browseName="ns=scales;ResetGlobalStatistics"))
    subDevices: di.objtypes.ConfigurableObjectType | None
    systemState: pack_ml.objtypes.PackMLBaseStateMachineType | None


@o6.objecttype(nodeId="ns=scales;i=2", browseName="ns=scales;ScaleDeviceType", displayName="ScaleDeviceType", description="Represents a scale.", isAbstract=True)
class ScaleDeviceType(di.objtypes.ComponentType):
    allowedEngineeringUnits: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=989",
            browseName="ns=scales;AllowedEngineeringUnits",
            dataType=ns0.datatypes.EUInformation,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    clearTare: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=scales;i=1406", browseName="ns=scales;ClearTare"))
    currentWeight: scales_vartypes.WeightItemType
    identification: machinery.objtypes.MachineIdentificationType
    langleListOfWeighingRangesRangle: WeighingRangeElementType
    machineryBuildingBlocks: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=scales;i=50021"])
    machineryItemState: machinery.objtypes.MachineryItemState_StateMachineType | None
    machineryOperationMode: machinery.objtypes.MachineryOperationModeStateMachineType | None
    materialClass: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=234",
            browseName="ns=scales;MaterialClass",
            description="Defines the allowed material the scale may measure. Only relevant for certain scales (e.g. totalizing hopper scale or continuous scale)",
            dataType=o6.LocalizedText,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    minimalWeight: ns0.vartypes.AnalogUnitType | None
    policy: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=60048", browseName="ns=scales;Policy", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
        )
    )
    processStateId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=229",
            browseName="ns=scales;ProcessStateId",
            description="Contains an relating identification for the occurring ProcessStateMessage.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    processStateMessage: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=161",
            browseName="ns=scales;ProcessStateMessage",
            description="Contains the message of the current overall state of the scale.",
            dataType=o6.LocalizedText,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    productionOutput: StatisticType | None = o6.hasComponent(StatisticType(nodeId="ns=scales;i=50031", browseName="ns=scales;ProductionOutput"))
    productionPreset: ProductionPresetType | None = o6.hasComponent(
        ProductionPresetType(nodeId="ns=scales;i=85", browseName="ns=scales;ProductionPreset", description="Contains the productions presets.")
    )
    registerWeight: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=scales;i=471", browseName="ns=scales;RegisterWeight"))
    registeredWeight: scales_vartypes.WeightItemType | None
    setPresetTare: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=1407"])
    setTare: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=scales;i=1409", browseName="ns=scales;SetTare"))
    setZero: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=scales;i=1408", browseName="ns=scales;SetZero"))
    state: pack_ml.objtypes.PackMLBaseStateMachineType | None
    subDevices: di.objtypes.ConfigurableObjectType | None


@o6.objecttype(nodeId="ns=scales;i=3", browseName="ns=scales;SimpleScaleType", displayName="SimpleScaleType", description="Represents a simple scale.")
class SimpleScaleType(ScaleDeviceType):
    productionPreset: ProductionPresetType | None


@o6.objecttype(nodeId="ns=scales;i=1", browseName="ns=scales;WeighingModuleType", displayName="WeighingModuleType", description="Represents a weighing bridge.")
class WeighingModuleType(SimpleScaleType):
    pass


@o6.objecttype(
    nodeId="ns=scales;i=4",
    browseName="ns=scales;CatchweigherType",
    displayName="CatchweigherType",
    description="Represents a Catchweigher. It has no method or properties defined.",
)
class CatchweigherType(ScaleDeviceType):
    productionPreset: ProductionPresetType | None


@o6.objecttype(
    nodeId="ns=scales;i=5", browseName="ns=scales;AutomaticFillingScaleType", displayName="AutomaticFillingScaleType", description="Represents an automatic filling scale."
)
class AutomaticFillingScaleType(ScaleDeviceType):
    deviation: ns0.vartypes.AnalogUnitType | None
    productionPreset: ProductionPresetType | None
    toleranceState: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=543",
            browseName="ns=scales;ToleranceState",
            description="Describes the state of the tolerance deviation. The option under and over needs to be determined via TargetItemType information of TargetWeight.",
            dataType=scales_datypes.ToleranceState,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=scales;i=6", browseName="ns=scales;PieceCountingScaleType", displayName="PieceCountingScaleType", description="Represents a piece counting scale.")
class PieceCountingScaleType(ScaleDeviceType):
    currentPieceCount: scales_vartypes.MeasuredItemType
    productionPreset: ProductionPresetType | None
    referenceOptimisationRange: ns0.vartypes.AnalogItemType | None
    setNumberOfReferencePieces: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=scales;i=1026"])
    setReferencePieceWeight: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=scales;i=603"])
    startReference: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=602"])


@o6.objecttype(nodeId="ns=scales;i=7", browseName="ns=scales;RecipeScaleType", displayName="RecipeScaleType", description="RecipeScaleType represents a recipe scale.")
class RecipeScaleType(ScaleDeviceType):
    abortRecipe: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=786"])
    continueRecipe: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=784"])
    productionPreset: ProductionPresetType | None
    recipes: RecipeManagementType | None
    skipCurrentRecipeElement: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=785"])
    startRecipe: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=458"])
    stopRecipe: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=783"])
    supportedMaterial: MaterialType | None
    supportedTargetValues: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=612",
            browseName="ns=scales;SupportedTargetValues",
            description="Defines a list of values that may be set via the recipe.",
            dataType=scales_datypes.RecipeTargetValueType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    supportedThresholdValues: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=611",
            browseName="ns=scales;SupportedThresholdValues",
            description="Defines a list of threshold values that may be used within one recipe.",
            dataType=scales_datypes.RecipeThresholdType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=scales;i=8", browseName="ns=scales;TotalizingHopperScaleType", displayName="TotalizingHopperScaleType", description="Represents a totalizing hopper scale."
)
class TotalizingHopperScaleType(ScaleDeviceType):
    productionPreset: ProductionPresetType | None


@o6.objecttype(nodeId="ns=scales;i=9", browseName="ns=scales;HopperScaleType", displayName="HopperScaleType", description="Represents a hopper scale.")
class HopperScaleType(SimpleScaleType):
    langleLimitsRangle: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=381",
            browseName="ns=scales;<Limits>",
            description="Defines a placeholder for individual additional limits that may be reached.",
            modellingRule="OptionalPlaceholder",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    levelMax: ns0.vartypes.AnalogUnitType | None
    levelMin: ns0.vartypes.AnalogUnitType | None
    limitMax: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=388",
            browseName="ns=scales;LimitMax",
            description="The current fill level exceeds the allowed maximum level.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    limitMin: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=389",
            browseName="ns=scales;LimitMin",
            description="The current fill level falls below the allowed minimum level.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=scales;i=15", browseName="ns=scales;LaboratoryScaleType", displayName="LaboratoryScaleType", description="Represents a laboratory scale.")
class LaboratoryScaleType(SimpleScaleType):
    calibrationNeeded: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=265",
            browseName="ns=scales;CalibrationNeeded",
            description="Defines if a calibration procedure is needed and the current process should be paused.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    calibrationRunning: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=264",
            browseName="ns=scales;CalibrationRunning",
            description="Defines if a calibration procedure is running.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    closeDraftShields: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=761"])
    draftShieldLeftClosed: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=238",
            browseName="ns=scales;DraftShieldLeftClosed",
            description="Defines if the left draft shield is closed.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    draftShieldRightClosed: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=239",
            browseName="ns=scales;DraftShieldRightClosed",
            description="Defines if the right draft shield is closed.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    draftShieldTopClosed: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=240",
            browseName="ns=scales;DraftShieldTopClosed",
            description="Defines if the top draft shield is closed.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ionisatorRunning: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=1207", browseName="ns=scales;IonisatorRunning", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    levelingRunning: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=263",
            browseName="ns=scales;LevelingRunning",
            description="Defines if a levelling process is running.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    openDraftShields: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=758"])
    startCalibration: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=scales;i=455", browseName="ns=scales;StartCalibration", description="Method to start the automatic calibration procedure.")
    )
    startIonisator: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=scales;i=457", browseName="ns=scales;StartIonisator", description="Method to start the ionization process.")
    )
    startLeveling: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=scales;i=454", browseName="ns=scales;StartLeveling", description="Method to start the automatic leveling procedure of the scale.")
    )
    stopIonisator: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=scales;i=463", browseName="ns=scales;StopIonisator", description="Method to stop the ionization process.")
    )


@o6.objecttype(nodeId="ns=scales;i=45", browseName="ns=scales;CheckweigherType", displayName="CheckweigherType", description="Represents a Checkweigher.")
class CheckweigherType(CatchweigherType):
    productionPreset: ProductionPresetType | None
    tU1Percent: ns0.vartypes.DataItemType | None = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=scales;i=447",
            browseName="ns=scales;TU1Percent",
            description="Permitted percentage of items with weight less than TU1",
            dataType=ns0.datatypes.Number,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=scales;i=49",
    browseName="ns=scales;AutomaticWeightPriceLabelerType",
    displayName="AutomaticWeightPriceLabelerType",
    description="Represents an automatic weight-price-labeler.",
)
class AutomaticWeightPriceLabelerType(CatchweigherType):
    productionPreset: ProductionPresetType | None


@o6.objecttype(nodeId="ns=scales;i=834", browseName="ns=scales;VehicleScaleType", displayName="VehicleScaleType")
class VehicleScaleType(ScaleDeviceType):
    inboundWeighing: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=1022"])
    onePassWeighing: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=1024"])
    outboundWeighing: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=scales;i=1023"])
    productionPreset: ProductionPresetType | None


@o6.objecttype(
    nodeId="ns=scales;i=26",
    browseName="ns=scales;FloatingStatisticType",
    displayName="FloatingStatisticType",
    description="Container for the different statisticvalues. All variables are optional, so that the statistics can be instantiated application-specific. Should be used for application-specific statistics.",
    interfaces=[ia.objtypes.IRollingStatisticsType],
)
class FloatingStatisticType(StatisticType):
    windowNumberOfValues: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=60063", browseName="ns=ia;WindowNumberOfValues", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=scales;i=10", browseName="ns=scales;ContinuousScaleType", displayName="ContinuousScaleType", description="Represents a continuous scale.")
class ContinuousScaleType(ScaleDeviceType):
    controlMagnitude: ns0.vartypes.AnalogUnitType | None
    flowRate: scales_vartypes.MeasuredItemType
    langleTotalizerRangle: TotalizerType | None
    load: ns0.vartypes.AnalogUnitType | None
    masterTotalizer: TotalizerType | None
    maxFlowRate: ns0.vartypes.AnalogUnitType | None
    minFlowRate: ns0.vartypes.AnalogUnitType | None
    productionPreset: ProductionPresetType | None
    rateControlMode: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=60152", browseName="ns=scales;RateControlMode", dataType=scales_datypes.RateControlMode, accessLevel=3, userAccessLevel=1
        )
    )
    speed: ns0.vartypes.AnalogUnitType | None
    targetFlowRate: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=scales;i=50", browseName="ns=scales;LossInWeightScaleType", displayName="LossInWeightScaleType", description="Represents a loss in weight scale.")
class LossInWeightScaleType(ContinuousScaleType):
    binWeight: scales_vartypes.MeasuredItemType | None
    dischargeStart: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="ns=scales;i=539", browseName="ns=scales;DischargeStart", description="Starts a discharging process."))
    dischargeStop: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="ns=scales;i=540", browseName="ns=scales;DischargeStop", description="Stops a discharging process."))
    discharging: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=916",
            browseName="ns=scales;Discharging",
            description="Indicates that a discharging process is taking place.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    hopperFillLevel: ns0.vartypes.AnalogUnitType
    hopperWeight: scales_vartypes.MeasuredItemType
    refillStart: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="ns=scales;i=537", browseName="ns=scales;RefillStart", description="Starts a refilling process."))
    refillStop: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="ns=scales;i=538", browseName="ns=scales;RefillStop", description="Stops a refilling process."))
    refilling: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=scales;i=917", browseName="ns=scales;Refilling", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(
    nodeId="ns=scales;i=37",
    browseName="ns=scales;ConditionSleepType",
    displayName="ConditionSleepType",
    description="Represents a condition sleep step in a recipe.",
    isAbstract=True,
)
class ConditionSleepType(RecipeElementType):
    targetThresholdValue: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=scales;i=299",
            browseName="ns=scales;TargetThresholdValue",
            description="The target value with which the threshold value is compared.",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    thresholdValueId: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=scales;i=943",
            browseName="ns=scales;ThresholdValueId",
            description="Defines an Id of process value that needs to be monitored and is element of the SupportedThresholdValues in the RecipeScale.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    thresholdValueNodeId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=scales;i=60240",
            browseName="ns=scales;ThresholdValueNodeId",
            description="The NodeId of process value that needs to be monitored and is element of the SupportedThresholdValues in the RecipeScale. This variable should be used if the value is part of the address space.",
            dataType=o6.NodeId,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    timeout: ns0.vartypes.DataItemType | None = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=scales;i=945",
            browseName="ns=scales;Timeout",
            description="Timeout specifies the duration within the TargetThresholdValue needs to be reached. If Timeout is exceeded and operator intervention is necessary.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=scales;i=38", browseName="ns=scales;AnalogConditionSleepType", displayName="AnalogConditionSleepType", description="Represents a condition sleep step in a recipe."
)
class AnalogConditionSleepType(ConditionSleepType):
    conditionMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=302",
            browseName="ns=scales;ConditionMode",
            description="Defines the type of condition operator that is used.",
            dataType=scales_datypes.EqualityAndRelationalOperator,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    targetThresholdValue: scales_vartypes.TargetItemType


@o6.objecttype(
    nodeId="ns=scales;i=39", browseName="ns=scales;EdgeTriggeredSleepType", displayName="EdgeTriggeredSleepType", description="Represents a condition sleep step in a recipe."
)
class EdgeTriggeredSleepType(ConditionSleepType):
    conditionMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=scales;i=303",
            browseName="ns=scales;ConditionMode",
            description="Defines the type of condition operator that is used.",
            dataType=scales_datypes.EdgeOperator,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    targetThresholdValue: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=scales;i=301",
            browseName="ns=scales;TargetThresholdValue",
            description="The target value with which the threshold value is compared.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, pack_ml, scales_reftypes, scales_datypes, scales_vartypes
