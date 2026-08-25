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

"""Generated OPC UA machinery_jobs namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.ns0 as ns0
from . import datatypes as machinery_jobs_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=machinery_jobs;i=1003", browseName="ns=machinery_jobs;JobManagementType", displayName="JobManagementType")
class JobManagementType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machinery_jobs;i=6013",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type.",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("machinery_jobs:JobManagement"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    jobOrderControl: isa95_jobcontrol_v2.objtypes.ISA95JobOrderReceiverObjectType
    jobOrderResults: isa95_jobcontrol_v2.objtypes.ISA95JobResponseProviderObjectType


del Any, TYPE_CHECKING, uuid, o6, isa95_jobcontrol_v2, ns0, machinery_jobs_datypes
