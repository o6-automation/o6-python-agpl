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

"""Generated OPC UA csp_plus namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import vartypes as csp_plus_vartypes
from . import objtypes as csp_plus_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.BaseObjectType(
    nodeId="ns=csp_plus;i=5001",
    browseName="ns=di;ParameterSet",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(ns0.vartypes.DataItemType(nodeId="ns=csp_plus;i=6001", browseName="ns=csp_plus;<VariableName>", modellingRule="OptionalPlaceholder")),
        o6.hasComponent(ns0.vartypes.DataItemType(nodeId="ns=csp_plus;i=6002", browseName="ns=csp_plus;<ConfigurationName>", modellingRule="OptionalPlaceholder")),
    ],
)
o6.reference(csp_plus_objtypes.CsppMachineType, ns0.reftypes.HasComponent, o6.ns["ns=csp_plus;i=5001"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=csp_plus;i=5003",
    browseName="ns=csp_plus;<CommIfVariablePart>",
    modellingRule="OptionalPlaceholder",
    references=[o6.organizes(ns0.vartypes.DataItemType(nodeId="ns=csp_plus;i=6004", browseName="ns=csp_plus;<VariableName>", modellingRule="MandatoryPlaceholder"))],
)
di.objtypes.FunctionalGroupType(
    nodeId="ns=csp_plus;i=5004",
    browseName="ns=csp_plus;<CommIfConfigurationPart>",
    modellingRule="OptionalPlaceholder",
    references=[o6.organizes(ns0.vartypes.DataItemType(nodeId="ns=csp_plus;i=6005", browseName="ns=csp_plus;<ConfigurationName>", modellingRule="MandatoryPlaceholder"))],
)
di.objtypes.FunctionalGroupType(
    nodeId="ns=csp_plus;i=5002",
    browseName="ns=csp_plus;<CommIfSection>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.organizes(ns0.vartypes.DataItemType(nodeId="ns=csp_plus;i=6003", browseName="ns=csp_plus;<VariableOrConfigurationName>", modellingRule="MandatoryPlaceholder")),
        o6.hasComponent(o6.ns["ns=csp_plus;i=5003"]),
        o6.hasComponent(o6.ns["ns=csp_plus;i=5004"]),
    ],
)
o6.reference(csp_plus_objtypes.CsppMachineType, ns0.reftypes.HasComponent, o6.ns["ns=csp_plus;i=5002"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashCSPPlusForMachineSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=csp_plus;i=5005",
    browseName="ns=csp_plus;http://opcfoundation.org/UA/CSPPlusForMachine/",
    description="Provides the metadata for a namespace used by the server.",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(
                nodeId="ns=csp_plus;i=6007", browseName="IsNamespaceSubset", description="If TRUE then the server only supports a subset of the namespace.", dataType=o6.Boolean
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=csp_plus;i=6008",
                browseName="NamespacePublicationDate",
                description="The publication date for the namespace.",
                dataType=o6.DateTime,
                value=o6.DateTime("2017-11-28T00:00:00Z"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=csp_plus;i=6009",
                browseName="NamespaceUri",
                description="The URI of the namespace.",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/CSPPlusForMachine/",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=csp_plus;i=6010",
                browseName="NamespaceVersion",
                description="The human readable string representing version of the namespace.",
                dataType=o6.String,
                value="1.00",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=csp_plus;i=6011",
                browseName="StaticNodeIdTypes",
                description="A list of IdTypes for nodes which are the same in every server that exposes them.",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=csp_plus;i=6012",
                browseName="StaticNumericNodeIdRange",
                description="A list of ranges for numeric node ids which are the same in every server that exposes them.",
                dataType=ns0.datatypes.NumericRange,
                valueRank=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=csp_plus;i=6013",
                browseName="StaticStringNodeIdPattern",
                description="A regular expression which matches string node ids are the same in every server that exposes them.",
                dataType=o6.String,
            )
        ),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)


del Any, TYPE_CHECKING, uuid, o6, di, ns0, csp_plus_vartypes, csp_plus_objtypes
