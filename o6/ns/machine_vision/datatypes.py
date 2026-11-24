# Copyright (c) 2026 o6 Automation GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
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


@o6.datatype(nodeId="ns=machine_vision;i=3003", browseName="ns=machine_vision;ProductIdDataType", defaultEncodingId="ns=machine_vision;i=5224")
class ProductIdDataType(ns0.datatypes.Structure):
    id: o6.String = o6.field(name="Id")
    description: o6.LocalizedText | None = o6.field(name="Description")


@o6.datatype(nodeId="ns=machine_vision;i=3004", browseName="ns=machine_vision;PartIdDataType", defaultEncodingId="ns=machine_vision;i=5013")
class PartIdDataType(ns0.datatypes.Structure):
    id: o6.String = o6.field(name="Id")
    description: o6.LocalizedText | None = o6.field(name="Description")


@o6.datatype(nodeId="ns=machine_vision;i=3005", browseName="ns=machine_vision;ProcessingTimesDataType", defaultEncodingId="ns=machine_vision;i=5016")
class ProcessingTimesDataType(ns0.datatypes.Structure):
    startTime: o6.DateTime = o6.field(name="StartTime")
    endTime: o6.DateTime = o6.field(name="EndTime")
    acquisitionDuration: o6.Double | None = o6.field(name="AcquisitionDuration")
    processingDuration: o6.Double | None = o6.field(name="ProcessingDuration")


@o6.datatype(nodeId="ns=machine_vision;i=3009", browseName="ns=machine_vision;ResultStateDataType", parent="i=6")
class ResultStateDataType:
    pass


@o6.enumtype(nodeId="ns=machine_vision;i=3014", browseName="ns=machine_vision;TriStateBooleanDataType")
class TriStateBooleanDataType(ns0.datatypes.Enumeration):
    FALSE_0 = o6.enumfield(0, name="FALSE_0")
    TRUE_1 = o6.enumfield(1, name="TRUE_1")
    DONTCARE_2 = o6.enumfield(2, name="DONTCARE_2")


@o6.datatype(nodeId="ns=machine_vision;i=3015", browseName="ns=machine_vision;MeasIdDataType", defaultEncodingId="ns=machine_vision;i=5006")
class MeasIdDataType(ns0.datatypes.Structure):
    id: o6.String = o6.field(name="Id")
    description: o6.LocalizedText | None = o6.field(name="Description")


@o6.datatype(nodeId="ns=machine_vision;i=3016", browseName="ns=machine_vision;JobIdDataType", defaultEncodingId="ns=machine_vision;i=5008")
class JobIdDataType(ns0.datatypes.Structure):
    id: o6.String = o6.field(name="Id")


@o6.datatype(nodeId="ns=machine_vision;i=3017", browseName="ns=machine_vision;TrimmedString", parent="i=12")
class TrimmedString:
    pass


@o6.datatype(nodeId="ns=machine_vision;i=3018", browseName="ns=machine_vision;Handle", parent="i=7")
class Handle:
    pass


@o6.datatype(nodeId="ns=machine_vision;i=3019", browseName="ns=machine_vision;BinaryIdBaseDataType", defaultEncodingId="ns=machine_vision;i=5027", isAbstract=True)
class BinaryIdBaseDataType(ns0.datatypes.Structure):
    id: o6.String = o6.field(name="Id")
    version: o6.String | None = o6.field(name="Version")
    hash: o6.ByteString | None = o6.field(name="Hash")
    hashAlgorithm: o6.String | None = o6.field(name="HashAlgorithm")
    description: o6.LocalizedText | None = o6.field(name="Description")


@o6.datatype(nodeId="ns=machine_vision;i=3002", browseName="ns=machine_vision;RecipeIdExternalDataType", defaultEncodingId="ns=machine_vision;i=5002")
class RecipeIdExternalDataType(BinaryIdBaseDataType):
    id: o6.String = o6.field(name="Id")
    version: o6.String | None = o6.field(name="Version")
    hash: o6.ByteString | None = o6.field(name="Hash")
    hashAlgorithm: o6.String | None = o6.field(name="HashAlgorithm")
    description: o6.LocalizedText | None = o6.field(name="Description")


@o6.datatype(nodeId="ns=machine_vision;i=3008", browseName="ns=machine_vision;ConfigurationIdDataType", defaultEncodingId="ns=machine_vision;i=5090")
class ConfigurationIdDataType(BinaryIdBaseDataType):
    id: o6.String = o6.field(name="Id")
    version: o6.String | None = o6.field(name="Version")
    hash: o6.ByteString | None = o6.field(name="Hash")
    hashAlgorithm: o6.String | None = o6.field(name="HashAlgorithm")
    description: o6.LocalizedText | None = o6.field(name="Description")


@o6.datatype(nodeId="ns=machine_vision;i=3007", browseName="ns=machine_vision;ConfigurationDataType", defaultEncodingId="ns=machine_vision;i=5088")
class ConfigurationDataType(ns0.datatypes.Structure):
    hasTransferableDataOnFile: o6.Boolean | None = o6.field(name="HasTransferableDataOnFile")
    externalId: ConfigurationIdDataType | None = o6.field(name="ExternalId")
    internalId: ConfigurationIdDataType = o6.field(name="InternalId")
    lastModified: o6.DateTime = o6.field(name="LastModified")


@o6.datatype(nodeId="ns=machine_vision;i=3011", browseName="ns=machine_vision;ConfigurationTransferOptions", defaultEncodingId="ns=machine_vision;i=5246")
class ConfigurationTransferOptions(ns0.datatypes.Structure):
    internalId: ConfigurationIdDataType = o6.field(name="InternalId")


@o6.datatype(nodeId="ns=machine_vision;i=3013", browseName="ns=machine_vision;RecipeIdInternalDataType", defaultEncodingId="ns=machine_vision;i=5268")
class RecipeIdInternalDataType(BinaryIdBaseDataType):
    id: o6.String = o6.field(name="Id")
    version: o6.String | None = o6.field(name="Version")
    hash: o6.ByteString | None = o6.field(name="Hash")
    hashAlgorithm: o6.String | None = o6.field(name="HashAlgorithm")
    description: o6.LocalizedText | None = o6.field(name="Description")


@o6.datatype(nodeId="ns=machine_vision;i=3012", browseName="ns=machine_vision;RecipeTransferOptions", defaultEncodingId="ns=machine_vision;i=5248")
class RecipeTransferOptions(ns0.datatypes.Structure):
    internalId: RecipeIdInternalDataType = o6.field(name="InternalId")


@o6.datatype(nodeId="ns=machine_vision;i=3020", browseName="ns=machine_vision;ProductDataType", defaultEncodingId="ns=machine_vision;i=5272")
class ProductDataType(ns0.datatypes.Structure):
    externalId: ProductIdDataType = o6.field(name="ExternalId")


@o6.datatype(nodeId="ns=machine_vision;i=3021", browseName="ns=machine_vision;ResultIdDataType", defaultEncodingId="ns=machine_vision;i=5274")
class ResultIdDataType(ns0.datatypes.Structure):
    id: o6.String = o6.field(name="Id")


@o6.datatype(nodeId="ns=machine_vision;i=3006", browseName="ns=machine_vision;ResultDataType", defaultEncodingId="ns=machine_vision;i=5018")
class ResultDataType(ns0.datatypes.Structure):
    resultId: ResultIdDataType = o6.field(name="ResultId")
    hasTransferableDataOnFile: o6.Boolean | None = o6.field(name="HasTransferableDataOnFile")
    isPartial: o6.Boolean = o6.field(name="IsPartial")
    isSimulated: o6.Boolean | None = o6.field(name="IsSimulated")
    resultState: o6.Int32 = o6.field(name="ResultState")
    measId: MeasIdDataType | None = o6.field(name="MeasId")
    partId: PartIdDataType | None = o6.field(name="PartId")
    externalRecipeId: RecipeIdExternalDataType | None = o6.field(name="ExternalRecipeId")
    internalRecipeId: RecipeIdInternalDataType = o6.field(name="InternalRecipeId")
    productId: ProductIdDataType | None = o6.field(name="ProductId")
    externalConfigurationId: ConfigurationIdDataType | None = o6.field(name="ExternalConfigurationId")
    internalConfigurationId: ConfigurationIdDataType = o6.field(name="InternalConfigurationId")
    jobId: JobIdDataType = o6.field(name="JobId")
    creationTime: o6.DateTime = o6.field(name="CreationTime")
    processingTimes: ProcessingTimesDataType | None = o6.field(name="ProcessingTimes")
    resultContent: list[Any] | None = o6.field(name="ResultContent", arrayDimensions=[1])


@o6.datatype(nodeId="ns=machine_vision;i=3022", browseName="ns=machine_vision;ResultTransferOptions", defaultEncodingId="ns=machine_vision;i=5276")
class ResultTransferOptions(ns0.datatypes.Structure):
    id: ResultIdDataType = o6.field(name="Id")


@o6.enumtype(nodeId="ns=machine_vision;i=3023", browseName="ns=machine_vision;SystemStateDataType")
class SystemStateDataType(ns0.datatypes.Enumeration):
    PRD_1 = o6.enumfield(1, name="PRD_1")
    SBY_2 = o6.enumfield(2, name="SBY_2")
    ENG_3 = o6.enumfield(3, name="ENG_3")
    SDT_4 = o6.enumfield(4, name="SDT_4")
    UDT_5 = o6.enumfield(5, name="UDT_5")
    NST_6 = o6.enumfield(6, name="NST_6")


@o6.datatype(nodeId="ns=machine_vision;i=3024", browseName="ns=machine_vision;SystemStateDescriptionDataType", defaultEncodingId="ns=machine_vision;i=5278")
class SystemStateDescriptionDataType(ns0.datatypes.Structure):
    state: SystemStateDataType = o6.field(name="State")
    stateDescription: o6.String | None = o6.field(name="StateDescription")


del Any, TYPE_CHECKING, uuid, o6, ns0, machine_vision_reftypes
