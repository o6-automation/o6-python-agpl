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

"""Generated OPC UA gms namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machine_tool as machine_tool
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.machinery_result as machinery_result
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=gms;i=3002", browseName="ToolIsQualifiedStatus")
class ToolIsQualifiedStatus(ns0.datatypes.Enumeration):
    QUALIFIED = o6.enumfield(0, name="Qualified")
    IMPRECISE = o6.enumfield(1, name="Imprecise")
    NOT_QUALIFIED = o6.enumfield(2, name="NotQualified")


@o6.enumtype(nodeId="ns=gms;i=3004", browseName="ToolAlignmentState")
class ToolAlignmentState(ns0.datatypes.Enumeration):
    FIXED = o6.enumfield(0, name="Fixed")
    INDEXED = o6.enumfield(1, name="Indexed")
    CONTINUOUS = o6.enumfield(2, name="Continuous")


@o6.datatype(nodeId="ns=gms;i=3006", browseName="WorkspaceType", isAbstract=True)
class WorkspaceType(ns0.datatypes.Structure):
    pass


@o6.datatype(nodeId="ns=gms;i=3007", browseName="CartesianWorkspaceType", defaultEncodingId="ns=gms;i=5007")
class CartesianWorkspaceType(WorkspaceType):
    length: o6.Double
    width: o6.Double
    height: o6.Double


@o6.datatype(nodeId="ns=gms;i=3008", browseName="CylindricalWorkspaceType", defaultEncodingId="ns=gms;i=5013")
class CylindricalWorkspaceType(WorkspaceType):
    length: o6.Double
    radius: o6.Double


@o6.enumtype(nodeId="ns=gms;i=3009", browseName="MeasurementReasonEnum")
class MeasurementReasonEnum(ns0.datatypes.Enumeration):
    CONTINUOUS_MEASUREMENTS = o6.enumfield(0, name="ContinuousMeasurements")
    SPECIAL_MEASUREMENT = o6.enumfield(1, name="SpecialMeasurement")
    AUDIT_MEASUREMENT = o6.enumfield(2, name="AuditMeasurement")
    MIN_MASTERING = o6.enumfield(3, name="MinMastering")
    MED_MASTERING = o6.enumfield(4, name="MedMastering")
    MAX_MASTERING = o6.enumfield(5, name="MaxMastering")


@o6.enumtype(nodeId="ns=gms;i=3010", browseName="ToleranceLimitEnum")
class ToleranceLimitEnum(ns0.datatypes.Enumeration):
    NO_LIMIT = o6.enumfield(0, name="NoLimit")
    LIMIT_VALUE = o6.enumfield(1, name="LimitValue")
    NATURAL_LIMIT = o6.enumfield(2, name="NaturalLimit")


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machine_tool, machinery, machinery_jobs, machinery_result, ns0
