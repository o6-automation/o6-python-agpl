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

"""Generated OPC UA adi namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as adi_reftypes
from . import datatypes as adi_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(
    nodeId="ns=adi;i=9380",
    browseName="ns=adi;EngineeringValueType",
    displayName="EngineeringValueType",
    description="Expose key results of an analyser and the associated values that qualified it",
    valueRank=o6.ValueRank.ANY,
)
class EngineeringValueType(ns0.vartypes.DataItemType):
    langleIdentifierRangle: ns0.vartypes.DataItemType | None = o6.hasComponent(
        ns0.vartypes.DataItemType(nodeId="ns=adi;i=13030", browseName="ns=adi;<Identifier>", description="Point to the data source", modellingRule="OptionalPlaceholder")
    )


@o6.variabletype(
    nodeId="ns=adi;i=2007",
    browseName="ns=adi;ChemometricModelType",
    displayName="ChemometricModelType",
    description="Hold the descriptions of a mathematical process and associated information to convert scaled data into one or more process values.",
    dataType=o6.ByteString,
    valueRank=o6.ValueRank.ANY,
)
class ChemometricModelType(ns0.vartypes.BaseDataVariableType):
    creationDate: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=13034", browseName="ns=adi;CreationDate", dataType=o6.DateTime))
    langleUserSpaceDefinedSpaceInputHashRangle: ns0.vartypes.BaseVariableType = o6.reference(
        ns0.vartypes.BaseVariableType(
            nodeId="ns=adi;i=13036",
            browseName="ns=adi;<User defined Input#>",
            description="Point to model input parameters",
            modellingRule="MandatoryPlaceholder",
            _allow_abstract=True,
        ),
        "ns=adi;i=4002",
    )
    langleUserSpaceDefinedSpaceOutputHashRangle: ns0.vartypes.BaseVariableType = o6.reference(
        ns0.vartypes.BaseVariableType(
            nodeId="ns=adi;i=13037",
            browseName="ns=adi;<User defined Output#>",
            description="Point to model output parameters",
            modellingRule="MandatoryPlaceholder",
            _allow_abstract=True,
        ),
        "ns=adi;i=4003",
    )
    modelDescription: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=adi;i=13035", browseName="ns=adi;ModelDescription", dataType=o6.LocalizedText)
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=13033", browseName="ns=adi;Name", dataType=o6.LocalizedText))


@o6.variabletype(
    nodeId="ns=adi;i=2008",
    browseName="ns=adi;ProcessVariableType",
    displayName="ProcessVariableType",
    description="Provides a stable address space view from the user point of view even if the ADI server address space changes, after the new configuration is loaded.",
    valueRank=o6.ValueRank.ANY,
)
class ProcessVariableType(ns0.vartypes.DataItemType):
    langleSourceRangle: ns0.vartypes.BaseVariableType = o6.reference(
        ns0.vartypes.BaseVariableType(
            nodeId="ns=adi;i=13040", browseName="ns=adi;<Source>", description="Point to source parameter", modellingRule="MandatoryPlaceholder", _allow_abstract=True
        ),
        "ns=adi;i=4001",
    )


@o6.variabletype(
    nodeId="ns=adi;i=2009",
    browseName="ns=adi;MVAModelType",
    displayName="MVAModelType",
    description="Hold the descriptions of a mathematical process and associated information to convert scaled data into one or more process values.",
    dataType=o6.ByteString,
    valueRank=o6.ValueRank.ANY,
)
class MVAModelType(ChemometricModelType):
    langleUserSpaceDefinedSpaceOutputHashRangle: MVAOutputParameterType | None
    mainDataIndex: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=adi;i=13046", browseName="ns=adi;MainDataIndex", dataType=o6.Int32))


@o6.variabletype(
    nodeId="ns=adi;i=2010",
    browseName="ns=adi;MVAOutputParameterType",
    displayName="MVAOutputParameterType",
    description="Hold the descriptions of a mathematical process and associated information to convert scaled data into one or more process values.",
    valueRank=o6.ValueRank.ANY,
)
class MVAOutputParameterType(ns0.vartypes.BaseDataVariableType):
    alarmLimits: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=adi;i=13055", browseName="ns=adi;AlarmLimits", dataType=ns0.datatypes.Range)
    )
    alarmState: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=adi;i=13056", browseName="ns=adi;AlarmState", dataType=adi_datypes.AlarmStateEnumeration)
    )
    statistics: MVAOutputParameterType | None
    vendorSpecificError: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=adi;i=13057", browseName="ns=adi;VendorSpecificError", dataType=o6.String)
    )
    warningLimits: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=adi;i=13054", browseName="ns=adi;WarningLimits", dataType=ns0.datatypes.Range)
    )


del Any, TYPE_CHECKING, uuid, o6, di, ns0, adi_reftypes, adi_datypes
