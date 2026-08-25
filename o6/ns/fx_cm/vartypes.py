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

"""Generated OPC UA fx_cm namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.fx_data as fx_data
import o6.ns.ns0 as ns0
from . import reftypes as fx_cm_reftypes
from . import datatypes as fx_cm_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(
    nodeId="ns=fx_cm;i=2003",
    browseName="ns=fx_cm;ServerAddressType",
    displayName="ServerAddressType",
    dataType=fx_cm_datypes.ServerAddressDataType,
    value=fx_cm_datypes.ServerAddressDataType(address="", securityMode=ns0.datatypes.MessageSecurityMode.INVALID, securityPolicyUri="", serverUri=""),
)
class ServerAddressType(ns0.vartypes.BaseDataVariableType):
    address: ns0.vartypes.SelectionListType
    securityMode: ns0.vartypes.SelectionListType
    securityPolicyUri: ns0.vartypes.SelectionListType
    serverUri: ns0.vartypes.SelectionListType


@o6.variabletype(
    nodeId="ns=fx_cm;i=2002",
    browseName="ns=fx_cm;SecurityKeyServerAddressType",
    displayName="SecurityKeyServerAddressType",
    dataType=fx_cm_datypes.SecurityKeyServerAddressDataType,
    value=fx_cm_datypes.SecurityKeyServerAddressDataType(address="", securityPolicyUri="", serverUri="", usePushModel=False),
)
class SecurityKeyServerAddressType(ns0.vartypes.BaseDataVariableType):
    address: ns0.vartypes.SelectionListType
    securityPolicyUri: ns0.vartypes.SelectionListType
    serverUri: ns0.vartypes.SelectionListType
    usePushModel: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=fx_cm;i=6065", browseName="ns=fx_cm;UsePushModel", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )


del Any, TYPE_CHECKING, uuid, o6, di, fx_data, ns0, fx_cm_reftypes, fx_cm_datypes
