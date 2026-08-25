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

"""Generated OPC UA machine_vision namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as machine_vision_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=machine_vision;i=3003", browseName="ProductIdDataType", defaultEncodingId="ns=machine_vision;i=5224")
class ProductIdDataType(ns0.datatypes.Structure):
    id: o6.String
    description: o6.LocalizedText | None


@o6.datatype(nodeId="ns=machine_vision;i=3004", browseName="PartIdDataType", defaultEncodingId="ns=machine_vision;i=5013")
class PartIdDataType(ns0.datatypes.Structure):
    id: o6.String
    description: o6.LocalizedText | None


@o6.datatype(nodeId="ns=machine_vision;i=3005", browseName="ProcessingTimesDataType", defaultEncodingId="ns=machine_vision;i=5016")
class ProcessingTimesDataType(ns0.datatypes.Structure):
    startTime: o6.DateTime
    endTime: o6.DateTime
    acquisitionDuration: o6.Double | None
    processingDuration: o6.Double | None


@o6.datatype(nodeId="ns=machine_vision;i=3009", browseName="ResultStateDataType", parent="i=6")
class ResultStateDataType:
    pass


@o6.enumtype(nodeId="ns=machine_vision;i=3014", browseName="TriStateBooleanDataType")
class TriStateBooleanDataType(ns0.datatypes.Enumeration):
    FALSE_0 = o6.enumfield(0, name="FALSE_0")
    TRUE_1 = o6.enumfield(1, name="TRUE_1")
    DONTCARE_2 = o6.enumfield(2, name="DONTCARE_2")


@o6.datatype(nodeId="ns=machine_vision;i=3015", browseName="MeasIdDataType", defaultEncodingId="ns=machine_vision;i=5006")
class MeasIdDataType(ns0.datatypes.Structure):
    id: o6.String
    description: o6.LocalizedText | None


@o6.datatype(nodeId="ns=machine_vision;i=3016", browseName="JobIdDataType", defaultEncodingId="ns=machine_vision;i=5008")
class JobIdDataType(ns0.datatypes.Structure):
    id: o6.String


@o6.datatype(nodeId="ns=machine_vision;i=3017", browseName="TrimmedString", parent="i=12")
class TrimmedString:
    pass


@o6.datatype(nodeId="ns=machine_vision;i=3018", browseName="Handle", parent="i=7")
class Handle:
    pass


@o6.datatype(nodeId="ns=machine_vision;i=3019", browseName="BinaryIdBaseDataType", defaultEncodingId="ns=machine_vision;i=5027", isAbstract=True)
class BinaryIdBaseDataType(ns0.datatypes.Structure):
    id: o6.String
    version: o6.String | None
    hash: o6.ByteString | None
    hashAlgorithm: o6.String | None
    description: o6.LocalizedText | None


@o6.datatype(nodeId="ns=machine_vision;i=3002", browseName="RecipeIdExternalDataType", defaultEncodingId="ns=machine_vision;i=5002")
class RecipeIdExternalDataType(BinaryIdBaseDataType):
    id: o6.String
    version: o6.String | None
    hash: o6.ByteString | None
    hashAlgorithm: o6.String | None
    description: o6.LocalizedText | None


@o6.datatype(nodeId="ns=machine_vision;i=3008", browseName="ConfigurationIdDataType", defaultEncodingId="ns=machine_vision;i=5090")
class ConfigurationIdDataType(BinaryIdBaseDataType):
    id: o6.String
    version: o6.String | None
    hash: o6.ByteString | None
    hashAlgorithm: o6.String | None
    description: o6.LocalizedText | None


@o6.datatype(nodeId="ns=machine_vision;i=3007", browseName="ConfigurationDataType", defaultEncodingId="ns=machine_vision;i=5088")
class ConfigurationDataType(ns0.datatypes.Structure):
    hasTransferableDataOnFile: o6.Boolean | None
    externalId: ConfigurationIdDataType | None
    internalId: ConfigurationIdDataType
    lastModified: o6.DateTime


@o6.datatype(nodeId="ns=machine_vision;i=3011", browseName="ConfigurationTransferOptions", defaultEncodingId="ns=machine_vision;i=5246")
class ConfigurationTransferOptions(ns0.datatypes.Structure):
    internalId: ConfigurationIdDataType


@o6.datatype(nodeId="ns=machine_vision;i=3013", browseName="RecipeIdInternalDataType", defaultEncodingId="ns=machine_vision;i=5268")
class RecipeIdInternalDataType(BinaryIdBaseDataType):
    id: o6.String
    version: o6.String | None
    hash: o6.ByteString | None
    hashAlgorithm: o6.String | None
    description: o6.LocalizedText | None


@o6.datatype(nodeId="ns=machine_vision;i=3012", browseName="RecipeTransferOptions", defaultEncodingId="ns=machine_vision;i=5248")
class RecipeTransferOptions(ns0.datatypes.Structure):
    internalId: RecipeIdInternalDataType


@o6.datatype(nodeId="ns=machine_vision;i=3020", browseName="ProductDataType", defaultEncodingId="ns=machine_vision;i=5272")
class ProductDataType(ns0.datatypes.Structure):
    externalId: ProductIdDataType


@o6.datatype(nodeId="ns=machine_vision;i=3021", browseName="ResultIdDataType", defaultEncodingId="ns=machine_vision;i=5274")
class ResultIdDataType(ns0.datatypes.Structure):
    id: o6.String


@o6.datatype(nodeId="ns=machine_vision;i=3006", browseName="ResultDataType", defaultEncodingId="ns=machine_vision;i=5018")
class ResultDataType(ns0.datatypes.Structure):
    resultId: ResultIdDataType
    hasTransferableDataOnFile: o6.Boolean | None
    isPartial: o6.Boolean
    isSimulated: o6.Boolean | None
    resultState: o6.Int32
    measId: MeasIdDataType | None
    partId: PartIdDataType | None
    externalRecipeId: RecipeIdExternalDataType | None
    internalRecipeId: RecipeIdInternalDataType
    productId: ProductIdDataType | None
    externalConfigurationId: ConfigurationIdDataType | None
    internalConfigurationId: ConfigurationIdDataType
    jobId: JobIdDataType
    creationTime: o6.DateTime
    processingTimes: ProcessingTimesDataType | None
    resultContent: list[Any] | None = o6.field(arrayDimensions=[1])


@o6.datatype(nodeId="ns=machine_vision;i=3022", browseName="ResultTransferOptions", defaultEncodingId="ns=machine_vision;i=5276")
class ResultTransferOptions(ns0.datatypes.Structure):
    id: ResultIdDataType


@o6.enumtype(nodeId="ns=machine_vision;i=3023", browseName="SystemStateDataType")
class SystemStateDataType(ns0.datatypes.Enumeration):
    PRD_1 = o6.enumfield(1, name="PRD_1")
    SBY_2 = o6.enumfield(2, name="SBY_2")
    ENG_3 = o6.enumfield(3, name="ENG_3")
    SDT_4 = o6.enumfield(4, name="SDT_4")
    UDT_5 = o6.enumfield(5, name="UDT_5")
    NST_6 = o6.enumfield(6, name="NST_6")


@o6.datatype(nodeId="ns=machine_vision;i=3024", browseName="SystemStateDescriptionDataType", defaultEncodingId="ns=machine_vision;i=5278")
class SystemStateDescriptionDataType(ns0.datatypes.Structure):
    state: SystemStateDataType
    stateDescription: o6.String | None


del Any, TYPE_CHECKING, uuid, o6, ns0, machine_vision_reftypes
