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

"""Generated OPC UA pack_ml namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as pack_ml_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=pack_ml;i=11", browseName="ProductionMaintenanceModeEnum")
class ProductionMaintenanceModeEnum(ns0.datatypes.Enumeration):
    INVALID = o6.enumfield(0, name="Invalid")
    PRODUCE = o6.enumfield(1, name="Produce")
    MAINTENANCE = o6.enumfield(2, name="Maintenance")
    MANUAL = o6.enumfield(3, name="Manual")


@o6.datatype(nodeId="ns=pack_ml;i=14", browseName="PackMLCountDataType", defaultEncodingId="ns=pack_ml;i=69")
class PackMLCountDataType(ns0.datatypes.Structure):
    iD: o6.Int32
    name: o6.String
    unit: ns0.datatypes.EUInformation
    count: o6.Int32
    accCount: o6.Int32


@o6.datatype(nodeId="ns=pack_ml;i=15", browseName="PackMLAlarmDataType", defaultEncodingId="ns=pack_ml;i=74")
class PackMLAlarmDataType(ns0.datatypes.Structure):
    iD: o6.Int32
    value: o6.Int32
    message: o6.String
    category: o6.Int32
    dateTime: o6.DateTime
    ackDateTime: o6.DateTime
    trigger: o6.Boolean


@o6.datatype(nodeId="ns=pack_ml;i=16", browseName="PackMLDescriptorDataType", defaultEncodingId="ns=pack_ml;i=77")
class PackMLDescriptorDataType(ns0.datatypes.Structure):
    iD: o6.Int32
    name: o6.String
    unit: ns0.datatypes.EUInformation
    value: o6.Float


@o6.datatype(nodeId="ns=pack_ml;i=17", browseName="PackMLIngredientsDataType", defaultEncodingId="ns=pack_ml;i=79")
class PackMLIngredientsDataType(ns0.datatypes.Structure):
    ingredientID: o6.Int32
    parameter: list[PackMLDescriptorDataType] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=pack_ml;i=18", browseName="PackMLProductDataType", defaultEncodingId="ns=pack_ml;i=81")
class PackMLProductDataType(ns0.datatypes.Structure):
    productID: o6.Int32
    processVariables: list[PackMLDescriptorDataType] = o6.field(arrayDimensions=[0])
    ingredients: list[PackMLIngredientsDataType] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=pack_ml;i=19", browseName="PackMLRemoteInterfaceDataType", defaultEncodingId="ns=pack_ml;i=83")
class PackMLRemoteInterfaceDataType(ns0.datatypes.Structure):
    number: o6.Int32
    controlCmdNumber: o6.Int32
    cmdValue: o6.Int32
    parameter: list[PackMLDescriptorDataType] = o6.field(arrayDimensions=[0])


del Any, TYPE_CHECKING, uuid, o6, ns0, pack_ml_reftypes
