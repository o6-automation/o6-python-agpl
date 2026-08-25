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

"""Generated OPC UA machinery namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.ns0 as ns0
from . import objtypes as machinery_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

machines = ns0.objtypes.FolderType(
    nodeId="ns=machinery;i=1001",
    browseName="ns=machinery;Machines",
    description="This object is the entry point to machines managed in the server. All machines are directly referenced by this object.",
    parent="i=85",
    referenceType=ns0.reftypes.Organizes,
    eventNotifier=1,
)
machinery_objtypes.MachineryItemIdentificationType(
    nodeId="ns=machinery;i=5003",
    browseName="ns=di;Identification",
    description="Contains information about the identification and nameplate of a MachineryItem",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery;i=6019",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery;i=6020",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
    _allow_abstract=True,
)
ns0.objtypes.BaseObjectType(
    nodeId="ns=machinery;i=5002",
    browseName="ns=machinery;<Component>",
    description="Represents the identifiable components of a machine.",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasAddIn(o6.ns["ns=machinery;i=5003"])],
)
o6.reference(machinery_objtypes.MachineComponentsType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5002"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMachinerySlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=machinery;i=5001",
    browseName="ns=machinery;http://opcfoundation.org/UA/Machinery/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6031", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6032", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2026-01-01T00:00:00Z"))
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6033", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Machinery/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6034", browseName="NamespaceVersion", dataType=o6.String, value="1.04.1")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery;i=6035", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery;i=6036", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0], value=[]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6037", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.objtypes.StateType(
    nodeId="ns=machinery;i=5004",
    browseName="ns=machinery;OutOfService",
    description="The machine is not functional and does not perform any activity (e.g., error, blocked)",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6038", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5004"])
ns0.objtypes.StateType(
    nodeId="ns=machinery;i=5005",
    browseName="ns=machinery;NotAvailable",
    description="The machine is not available and does not perform any activity (e.g., switched off, in energy saving mode)",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6039", browseName="StateNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5005"])
ns0.objtypes.StateType(
    nodeId="ns=machinery;i=5006",
    browseName="ns=machinery;Executing",
    description="The machine is available & functional and is actively performing an activity (pursues a purpose)",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6040", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5006"])
ns0.objtypes.StateType(
    nodeId="ns=machinery;i=5007",
    browseName="ns=machinery;NotExecuting",
    description="The machine is available & functional and does not perform any activity. It waits for an action from outside to start or restart an activity",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6041", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5007"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5008",
    browseName="ns=machinery;FromNotAvailableToOutOfService",
    description="Transition from state NotAvailable to state OutOfService",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6042", browseName="TransitionNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5008"])
o6.reference(o6.ns["ns=machinery;i=5008"], "i=51", o6.ns["ns=machinery;i=5005"])
o6.reference(o6.ns["ns=machinery;i=5008"], "i=52", o6.ns["ns=machinery;i=5004"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5009",
    browseName="ns=machinery;FromNotAvailableToNotExecuting",
    description="Transition from state NotAvailable to state NotExecuting",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6043", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5009"])
o6.reference(o6.ns["ns=machinery;i=5009"], "i=51", o6.ns["ns=machinery;i=5005"])
o6.reference(o6.ns["ns=machinery;i=5009"], "i=52", o6.ns["ns=machinery;i=5007"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5010",
    browseName="ns=machinery;FromNotAvailableToExecuting",
    description="Transition from state NotAvailable to state Executing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6044", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5010"])
o6.reference(o6.ns["ns=machinery;i=5010"], "i=51", o6.ns["ns=machinery;i=5005"])
o6.reference(o6.ns["ns=machinery;i=5010"], "i=52", o6.ns["ns=machinery;i=5006"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5011",
    browseName="ns=machinery;FromNotAvailableToNotAvailable",
    description="Transition from state NotAvailable to state NotAvailable",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6045", browseName="TransitionNumber", dataType=o6.UInt32, value=12))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5011"])
o6.reference(o6.ns["ns=machinery;i=5011"], "i=51", o6.ns["ns=machinery;i=5005"])
o6.reference(o6.ns["ns=machinery;i=5011"], "i=52", o6.ns["ns=machinery;i=5005"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5012",
    browseName="ns=machinery;FromOutOfServiceToNotAvailable",
    description="Transition from state OutOfService to state NotAvailable",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6046", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5012"])
o6.reference(o6.ns["ns=machinery;i=5012"], "i=51", o6.ns["ns=machinery;i=5004"])
o6.reference(o6.ns["ns=machinery;i=5012"], "i=52", o6.ns["ns=machinery;i=5005"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5013",
    browseName="ns=machinery;FromOutOfServiceToNotExecuting",
    description="Transition from state OutOfService to state NotExecuting",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6047", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5013"])
o6.reference(o6.ns["ns=machinery;i=5013"], "i=51", o6.ns["ns=machinery;i=5004"])
o6.reference(o6.ns["ns=machinery;i=5013"], "i=52", o6.ns["ns=machinery;i=5007"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5014",
    browseName="ns=machinery;FromOutOfServiceToExecuting",
    description="Transition from state OutOfService to state Executing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6048", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5014"])
o6.reference(o6.ns["ns=machinery;i=5014"], "i=51", o6.ns["ns=machinery;i=5004"])
o6.reference(o6.ns["ns=machinery;i=5014"], "i=52", o6.ns["ns=machinery;i=5006"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5015",
    browseName="ns=machinery;FromOutOfServiceToOutOfService",
    description="Transition from state OutOfService to state OutOfService",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6049", browseName="TransitionNumber", dataType=o6.UInt32, value=13))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5015"])
o6.reference(o6.ns["ns=machinery;i=5015"], "i=51", o6.ns["ns=machinery;i=5004"])
o6.reference(o6.ns["ns=machinery;i=5015"], "i=52", o6.ns["ns=machinery;i=5004"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5016",
    browseName="ns=machinery;FromNotExecutingToNotAvailable",
    description="Transition from state NotExecuting to state NotAvailable",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6050", browseName="TransitionNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5016"])
o6.reference(o6.ns["ns=machinery;i=5016"], "i=51", o6.ns["ns=machinery;i=5007"])
o6.reference(o6.ns["ns=machinery;i=5016"], "i=52", o6.ns["ns=machinery;i=5005"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5017",
    browseName="ns=machinery;FromNotExecutingToOutOfService",
    description="Transition from state NotExecuting to state OutOfService",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6051", browseName="TransitionNumber", dataType=o6.UInt32, value=10))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5017"])
o6.reference(o6.ns["ns=machinery;i=5017"], "i=51", o6.ns["ns=machinery;i=5007"])
o6.reference(o6.ns["ns=machinery;i=5017"], "i=52", o6.ns["ns=machinery;i=5004"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5018",
    browseName="ns=machinery;FromNotExecutingToExecuting",
    description="Transition from state NotExecuting to state Executing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6052", browseName="TransitionNumber", dataType=o6.UInt32, value=11))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5018"])
o6.reference(o6.ns["ns=machinery;i=5018"], "i=51", o6.ns["ns=machinery;i=5007"])
o6.reference(o6.ns["ns=machinery;i=5018"], "i=52", o6.ns["ns=machinery;i=5006"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5019",
    browseName="ns=machinery;FromNotExecutingToNotExecuting",
    description="Transition from state NotExecuting to state NotExecuting",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6053", browseName="TransitionNumber", dataType=o6.UInt32, value=15))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5019"])
o6.reference(o6.ns["ns=machinery;i=5019"], "i=51", o6.ns["ns=machinery;i=5007"])
o6.reference(o6.ns["ns=machinery;i=5019"], "i=52", o6.ns["ns=machinery;i=5007"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5020",
    browseName="ns=machinery;FromExecutingToNotAvailable",
    description="Transition from state Executing to state NotAvailable",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6054", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5020"])
o6.reference(o6.ns["ns=machinery;i=5020"], "i=51", o6.ns["ns=machinery;i=5006"])
o6.reference(o6.ns["ns=machinery;i=5020"], "i=52", o6.ns["ns=machinery;i=5005"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5021",
    browseName="ns=machinery;FromExecutingToOutOfService",
    description="Transition from state Executing to state OutOfService",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6055", browseName="TransitionNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5021"])
o6.reference(o6.ns["ns=machinery;i=5021"], "i=51", o6.ns["ns=machinery;i=5006"])
o6.reference(o6.ns["ns=machinery;i=5021"], "i=52", o6.ns["ns=machinery;i=5004"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5022",
    browseName="ns=machinery;FromExecutingToNotExecuting",
    description="Transition from state Executing to state NotExecuting",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6056", browseName="TransitionNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5022"])
o6.reference(o6.ns["ns=machinery;i=5022"], "i=51", o6.ns["ns=machinery;i=5006"])
o6.reference(o6.ns["ns=machinery;i=5022"], "i=52", o6.ns["ns=machinery;i=5007"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5023",
    browseName="ns=machinery;FromExecutingToExecuting",
    description="Transition from state Executing to state Executing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6057", browseName="TransitionNumber", dataType=o6.UInt32, value=14))],
)
o6.reference(machinery_objtypes.MachineryItemState_StateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5023"])
o6.reference(o6.ns["ns=machinery;i=5023"], "i=51", o6.ns["ns=machinery;i=5006"])
o6.reference(o6.ns["ns=machinery;i=5023"], "i=52", o6.ns["ns=machinery;i=5006"])
ns0.objtypes.StateType(
    nodeId="ns=machinery;i=5024",
    browseName="ns=machinery;None",
    description="There is currently no operation mode available",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6059", browseName="StateNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5024"])
ns0.objtypes.StateType(
    nodeId="ns=machinery;i=5025",
    browseName="ns=machinery;Maintenance",
    description="MachineryItem is set into maintenance mode with the intention to carry out maintenance or servicing activities",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6060", browseName="StateNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5025"])
ns0.objtypes.StateType(
    nodeId="ns=machinery;i=5026",
    browseName="ns=machinery;Processing",
    description="MachineryItem is set into processing mode with the intention to carry out the value adding activities",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6061", browseName="StateNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5026"])
ns0.objtypes.StateType(
    nodeId="ns=machinery;i=5027",
    browseName="ns=machinery;Setup",
    description="MachineryItem is set into setup mode with the intention to carry out setup, preparation or postprocessing activities of a production process",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6062", browseName="StateNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5027"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5028",
    browseName="ns=machinery;FromNoneToMaintenance",
    description="Transition from state None to state Maintenance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6063", browseName="TransitionNumber", dataType=o6.UInt32, value=0))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5028"])
o6.reference(o6.ns["ns=machinery;i=5028"], "i=51", o6.ns["ns=machinery;i=5024"])
o6.reference(o6.ns["ns=machinery;i=5028"], "i=52", o6.ns["ns=machinery;i=5025"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5029",
    browseName="ns=machinery;FromNoneToSetup",
    description="Transition from state None to state Setup",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6064", browseName="TransitionNumber", dataType=o6.UInt32, value=2))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5029"])
o6.reference(o6.ns["ns=machinery;i=5029"], "i=51", o6.ns["ns=machinery;i=5024"])
o6.reference(o6.ns["ns=machinery;i=5029"], "i=52", o6.ns["ns=machinery;i=5027"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5030",
    browseName="ns=machinery;FromNoneToProcessing",
    description="Transition from state None to state Processing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6065", browseName="TransitionNumber", dataType=o6.UInt32, value=1))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5030"])
o6.reference(o6.ns["ns=machinery;i=5030"], "i=51", o6.ns["ns=machinery;i=5024"])
o6.reference(o6.ns["ns=machinery;i=5030"], "i=52", o6.ns["ns=machinery;i=5026"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5031",
    browseName="ns=machinery;FromNoneToNone",
    description="Transition from state None to state None",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6066", browseName="TransitionNumber", dataType=o6.UInt32, value=12))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5031"])
o6.reference(o6.ns["ns=machinery;i=5031"], "i=51", o6.ns["ns=machinery;i=5024"])
o6.reference(o6.ns["ns=machinery;i=5031"], "i=52", o6.ns["ns=machinery;i=5024"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5032",
    browseName="ns=machinery;FromMaintenanceToNone",
    description="Transition from state Maintenance to state None",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6067", browseName="TransitionNumber", dataType=o6.UInt32, value=3))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5032"])
o6.reference(o6.ns["ns=machinery;i=5032"], "i=51", o6.ns["ns=machinery;i=5025"])
o6.reference(o6.ns["ns=machinery;i=5032"], "i=52", o6.ns["ns=machinery;i=5024"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5033",
    browseName="ns=machinery;FromMaintenanceToSetup",
    description="Transition from state Maintenance to state Setup",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6068", browseName="TransitionNumber", dataType=o6.UInt32, value=5))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5033"])
o6.reference(o6.ns["ns=machinery;i=5033"], "i=51", o6.ns["ns=machinery;i=5025"])
o6.reference(o6.ns["ns=machinery;i=5033"], "i=52", o6.ns["ns=machinery;i=5027"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5034",
    browseName="ns=machinery;FromMaintenanceToProcessing",
    description="Transition from state Maintenance to state Processing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6069", browseName="TransitionNumber", dataType=o6.UInt32, value=4))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5034"])
o6.reference(o6.ns["ns=machinery;i=5034"], "i=51", o6.ns["ns=machinery;i=5025"])
o6.reference(o6.ns["ns=machinery;i=5034"], "i=52", o6.ns["ns=machinery;i=5026"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5035",
    browseName="ns=machinery;FromMaintenanceToMaintenance",
    description="Transition from state Maintenance to state Maintenance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6070", browseName="TransitionNumber", dataType=o6.UInt32, value=13))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5035"])
o6.reference(o6.ns["ns=machinery;i=5035"], "i=51", o6.ns["ns=machinery;i=5025"])
o6.reference(o6.ns["ns=machinery;i=5035"], "i=52", o6.ns["ns=machinery;i=5025"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5036",
    browseName="ns=machinery;FromSetupToNone",
    description="Transition from state Setup to state None",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6071", browseName="TransitionNumber", dataType=o6.UInt32, value=9))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5036"])
o6.reference(o6.ns["ns=machinery;i=5036"], "i=51", o6.ns["ns=machinery;i=5027"])
o6.reference(o6.ns["ns=machinery;i=5036"], "i=52", o6.ns["ns=machinery;i=5024"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5037",
    browseName="ns=machinery;FromSetupToMaintenance",
    description="Transition from state Setup to state Maintenance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6072", browseName="TransitionNumber", dataType=o6.UInt32, value=10))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5037"])
o6.reference(o6.ns["ns=machinery;i=5037"], "i=51", o6.ns["ns=machinery;i=5027"])
o6.reference(o6.ns["ns=machinery;i=5037"], "i=52", o6.ns["ns=machinery;i=5025"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5038",
    browseName="ns=machinery;FromSetupToProcessing",
    description="Transition from state Setup to state Processing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6073", browseName="TransitionNumber", dataType=o6.UInt32, value=11))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5038"])
o6.reference(o6.ns["ns=machinery;i=5038"], "i=51", o6.ns["ns=machinery;i=5027"])
o6.reference(o6.ns["ns=machinery;i=5038"], "i=52", o6.ns["ns=machinery;i=5026"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5039",
    browseName="ns=machinery;FromSetupToSetup",
    description="Transition from state Setup to state Setup",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6074", browseName="TransitionNumber", dataType=o6.UInt32, value=15))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5039"])
o6.reference(o6.ns["ns=machinery;i=5039"], "i=51", o6.ns["ns=machinery;i=5027"])
o6.reference(o6.ns["ns=machinery;i=5039"], "i=52", o6.ns["ns=machinery;i=5027"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5040",
    browseName="ns=machinery;FromProcessingToNone",
    description="Transition from state Processing to state None",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6075", browseName="TransitionNumber", dataType=o6.UInt32, value=6))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5040"])
o6.reference(o6.ns["ns=machinery;i=5040"], "i=51", o6.ns["ns=machinery;i=5026"])
o6.reference(o6.ns["ns=machinery;i=5040"], "i=52", o6.ns["ns=machinery;i=5024"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5041",
    browseName="ns=machinery;FromProcessingToMaintenance",
    description="Transition from state Processing to state Maintenance",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6076", browseName="TransitionNumber", dataType=o6.UInt32, value=7))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5041"])
o6.reference(o6.ns["ns=machinery;i=5041"], "i=51", o6.ns["ns=machinery;i=5026"])
o6.reference(o6.ns["ns=machinery;i=5041"], "i=52", o6.ns["ns=machinery;i=5025"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5042",
    browseName="ns=machinery;FromProcessingToSetup",
    description="Transition from state Processing to state Setup",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6077", browseName="TransitionNumber", dataType=o6.UInt32, value=8))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5042"])
o6.reference(o6.ns["ns=machinery;i=5042"], "i=51", o6.ns["ns=machinery;i=5026"])
o6.reference(o6.ns["ns=machinery;i=5042"], "i=52", o6.ns["ns=machinery;i=5027"])
ns0.objtypes.TransitionType(
    nodeId="ns=machinery;i=5043",
    browseName="ns=machinery;FromProcessingToProcessing",
    description="Transition from state Processing to state Processing",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6078", browseName="TransitionNumber", dataType=o6.UInt32, value=14))],
)
o6.reference(machinery_objtypes.MachineryOperationModeStateMachineType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5043"])
o6.reference(o6.ns["ns=machinery;i=5043"], "i=51", o6.ns["ns=machinery;i=5026"])
o6.reference(o6.ns["ns=machinery;i=5043"], "i=52", o6.ns["ns=machinery;i=5026"])
di.vartypes.LifetimeVariableType(
    nodeId="ns=machinery;i=6083",
    browseName="ns=machinery;<LifetimeVariable>",
    modellingRule="MandatoryPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery;i=6084",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery;i=6085",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6086", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(machinery_objtypes.MachineryLifetimeCounterType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=6083"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machinery;i=6090",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6091", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery_objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=machinery;i=5048", browseName="ns=machinery;MachineryItemState", references=[o6.hasComponent(o6.ns["ns=machinery;i=6090"])]
)
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=machinery;i=6092",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6093", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery_objtypes.MachineryOperationModeStateMachineType(
    nodeId="ns=machinery;i=5049", browseName="ns=machinery;MachineryOperationMode", references=[o6.hasComponent(o6.ns["ns=machinery;i=6092"])]
)
ia.objtypes.BasicStacklightType(
    nodeId="ns=machinery;i=5050",
    browseName="ns=machinery;Stacklight",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery;i=6094",
                browseName="ns=ia;StacklightMode",
                description="Shows in what way (stack of individual lights, level meter, running light) the stacklight unit is used.",
                dataType=ia.datatypes.StacklightOperationMode,
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
)
ns0.objtypes.FolderType(
    nodeId="ns=machinery;i=5044",
    browseName="ns=machinery;Status",
    description="Entry point for status information of the MachineryItem. If this Object is provided, and the MachineryItemState is provided, it shall be referenced. If this Object is provided and the MachineryOperationMode is provided, it shall be referenced.",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=machinery;i=5048"]), o6.hasComponent(o6.ns["ns=machinery;i=5049"]), o6.hasComponent(o6.ns["ns=machinery;i=5050"])],
)
o6.reference(machinery_objtypes.MonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5044"])
ns0.objtypes.FolderType(
    nodeId="ns=machinery;i=5045",
    browseName="ns=machinery;Health",
    description="Entry point of health information of the MachineryItem.",
    modellingRule="Optional",
    references=[
        o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=machinery;i=5051", browseName="ns=di;DeviceHealthAlarms")),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(
                nodeId="ns=machinery;i=6095", browseName="ns=di;DeviceHealth", dataType=di.datatypes.DeviceHealthEnumeration, accessLevel=3, userAccessLevel=1
            )
        ),
    ],
)
o6.reference(machinery_objtypes.MonitoringType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5045"])
o6.reference(o6.ns["ns=machinery;i=5045"], "i=17603", "ns=di;i=15051")
ns0.objtypes.BaseObjectType(
    nodeId="ns=machinery;i=5052",
    browseName="ns=machinery;<MachineryEquipment>",
    description="Placeholder for MachineryEquipment that implements the IMachineryEquipmentType.",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery;i=6096",
                browseName="ns=di;AssetId",
                description="Companywide unique ID for a specific asset (Each 8 mm drill of a company has the same MachineryEquipmentTypeId and a unique AssetId).",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery;i=6097",
                browseName="ns=di;ComponentName",
                description="Used name for the MachineryEquipment.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery;i=6098",
                browseName="ns=machinery;Description",
                description="Additional information and description about the MachineryEquipment. Should be used if Description Attribute cannot be written via OPC UA and should be ideally identical to Description Attribute.",
                dataType=o6.LocalizedText,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery;i=6099",
                browseName="ns=di;DeviceClass",
                description='Class of the MachineryEquipment (e.g.: Each drill of a company has the DeviceClass "drill").',
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery;i=6100",
                browseName="ns=machinery;Location",
                description="Location of the MachineryEquipment (e.g.: Storage Location; Position in the Tool Changer; Position on the machine).",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery;i=6101",
                browseName="ns=machinery;MachineryEquipmentTypeId",
                description="Identification of a generic MachineryEquipment. Defined by each company (e.g., company has an MachineryEquipmentTypeId for all 8 mm drills).",
                dataType=o6.String,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6102", browseName="ns=di;ManufacturerUri", description="Manufacturer of the MachineryEquipment.", dataType=o6.String)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6103", browseName="ns=di;Model", description="Model of the MachineryEquipment.", dataType=o6.LocalizedText)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6104", browseName="ns=di;SerialNumber", description="Serial Number of the MachineryEquipment.", dataType=o6.String)
        ),
    ],
)
o6.reference(machinery_objtypes.MachineryEquipmentFolderType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=5052"])
o6.reference(o6.ns["ns=machinery;i=5052"], "i=17603", "ns=di;i=15035")
o6.reference(o6.ns["ns=machinery;i=5052"], "i=17603", machinery_objtypes.IMachineryEquipmentType)
di.vartypes.LifetimeVariableType(
    nodeId="ns=machinery;i=6109",
    browseName="ns=machinery;EquipmentLife",
    description="Lifetime indication of the MachineryEquipment.",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery;i=6110",
                browseName="ns=di;LimitValue",
                description="LimitValue indicates when the end of lifetime has been reached.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=machinery;i=6111",
                browseName="ns=di;StartValue",
                description="StartValue indicates the initial value, when there is still the full lifetime left.",
                dataType=ns0.datatypes.Number,
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machinery;i=6112", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=ns0.datatypes.Number,
)
o6.reference(machinery_objtypes.IMachineryEquipmentType, ns0.reftypes.HasComponent, o6.ns["ns=machinery;i=6109"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, ns0, machinery_objtypes
