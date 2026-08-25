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

"""Generated OPC UA tmc namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.pack_ml as pack_ml
from . import reftypes as tmc_reftypes
from . import datatypes as tmc_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(
    nodeId="ns=tmc;i=2001",
    browseName="ns=tmc;DisplayAnalogUnitType",
    displayName="DisplayAnalogUnitType",
    description="The DisplayAnalogUnitType is a subtype of the AnalogUnitType. It is used to provide an analog \nsignal as well as its display format.",
    dataType=ns0.datatypes.Number,
)
class DisplayAnalogUnitType(ns0.vartypes.AnalogUnitType):
    displayFormat: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6046", browseName="ns=tmc;DisplayFormat", description="Display format for visualization of the AnalogUnitType.", dataType=o6.String
        )
    )


@o6.variabletype(
    nodeId="ns=tmc;i=2007",
    browseName="ns=tmc;BooleanGuardVariableType",
    displayName="BooleanGuardVariableType",
    dataType=o6.LocalizedText,
    value=o6.LocalizedText("AllConditionsTrue"),
)
class BooleanGuardVariableType(ns0.vartypes.GuardVariableType):
    langleConditionRangle: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6051",
            browseName="ns=tmc;<Condition>",
            description="A condition that is necessary to trigger a transition in a state machine. The description is the human-readable identification of the value of the Condition. The browse name is the human-readable identification subject to naming conventions and browse name limitations.",
            modellingRule="MandatoryPlaceholder",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.variabletype(
    nodeId="ns=tmc;i=2003",
    browseName="ns=tmc;MaterialQuantityVariableType",
    displayName="MaterialQuantityVariableType",
    description="The MaterialQuantityVariableType is a subtype of the DisplayAnalogUnitType. It is used to \nprovide a material quantity.",
    dataType=o6.Double,
    value=0.0,
)
class MaterialQuantityVariableType(DisplayAnalogUnitType):
    eURange: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=tmc;i=13390", browseName="EURange", description="The range for the material quantity value.", dataType=ns0.datatypes.Range)
    )
    valueInBUoM: DisplayAnalogUnitType


@o6.variabletype(
    nodeId="ns=tmc;i=2004",
    browseName="ns=tmc;MaterialLotVariableType",
    displayName="MaterialLotVariableType",
    description="The MaterialLotVariableType is a subtype of the MaterialQuantityVariableType. It is used to \nprovide the quantity for a material lot.",
    dataType=o6.Double,
    value=0.0,
)
class MaterialLotVariableType(MaterialQuantityVariableType):
    materialLot: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=tmc;i=6668", browseName="ns=tmc;MaterialLot", description="The material definition for the lot.", dataType=tmc_datypes.MaterialLotType)
    )


@o6.variabletype(
    nodeId="ns=tmc;i=2006",
    browseName="ns=tmc;MaterialRateType",
    displayName="MaterialRateType",
    description="The MaterialRateType is a subtype of the MaterialQuantityVariableType. It is used to provide \nthe rate for a material flow rate.",
    dataType=o6.Double,
    value=0.0,
)
class MaterialRateType(MaterialQuantityVariableType):
    pass


@o6.variabletype(
    nodeId="ns=tmc;i=2008",
    browseName="ns=tmc;MaterialSublotVariableType",
    displayName="MaterialSublotVariableType",
    description="The MaterialSublotVariableType is a subtype of the MaterialQuantityVariableType. It is used to \nprovide the quantity for a material sublot.",
    dataType=o6.Double,
    value=0.0,
)
class MaterialSublotVariableType(MaterialQuantityVariableType):
    carrierID: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6057", browseName="ns=tmc;CarrierID", description="The unique identifier of the carrier containing the material sublot.", dataType=o6.String
        )
    )
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=tmc;i=6308", browseName="ns=tmc;ID", description="The unique identifier for the material sublot.", dataType=o6.String)
    )
    mES_ID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6054", browseName="ns=tmc;MES_ID", description="The unique identifier for the material sublot for a higher-level system e.g. MES.", dataType=o6.String
        )
    )
    materialLot: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6060", browseName="ns=tmc;MaterialLot", description="The material lot of the material sublot.", dataType=tmc_datypes.MaterialLotType
        )
    )
    materialStorageLocationID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6119",
            browseName="ns=tmc;MaterialStorageLocationID",
            description="The material storage location where the material sublot is located.",
            dataType=o6.String,
        )
    )
    parentSublotID: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6059", browseName="ns=tmc;ParentSublotID", description="The unique identified for the parent sublot, if any.", dataType=o6.String
        )
    )
    relativePositionID: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6309",
            browseName="ns=tmc;RelativePositionID",
            description="The relative position of the sublot within the carrier identified by CarrierID.",
            dataType=o6.String,
        )
    )
    sublots: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6055",
            browseName="ns=tmc;Sublots",
            description="The sublots contained in the sublot.",
            dataType=tmc_datypes.MaterialSublotType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


@o6.variabletype(nodeId="ns=tmc;i=2002", browseName="ns=tmc;MaterialPointVariableType", displayName="MaterialPointVariableType", dataType=o6.LocalizedText)
class MaterialPointVariableType(ns0.vartypes.BaseDataVariableType):
    connectedMaterialPoint: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=tmc;i=19988", browseName="ns=tmc;ConnectedMaterialPoint", dataType=o6.ExpandedNodeId)
    )
    iD: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=tmc;i=19986", browseName="ns=tmc;ID", dataType=o6.String))
    mES_ID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=tmc;i=19987", browseName="ns=tmc;MES_ID", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    materialCapability: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=19989",
            browseName="ns=tmc;MaterialCapability",
            dataType=tmc_datypes.MaterialDefinitionType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pack_ml, tmc_reftypes, tmc_datypes
