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

"""Generated OPC UA surface_technology namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.ns0 as ns0
from . import objtypes as surface_technology_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.FolderType(
    nodeId="ns=surface_technology;i=5008",
    browseName="ns=machinery;Status",
    description="Entry point for status information of the MachineryItem. If this Object is provided, and the MachineryItemState is provided, it shall be referenced. If this Object is provided and the MachineryOperationMode is provided, it shall be referenced.",
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology;i=5004", browseName="ns=machinery;Monitoring", modellingRule="Optional", references=[o6.hasComponent(o6.ns["ns=surface_technology;i=5008"])]
)
o6.reference(surface_technology_objtypes.STSysType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology;i=5004"])
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology;i=5020",
    browseName="ns=machinery;Status",
    description="Entry point for status information of the MachineryItem. If this Object is provided, and the MachineryItemState is provided, it shall be referenced. If this Object is provided and the MachineryOperationMode is provided, it shall be referenced.",
)
machinery.objtypes.MonitoringType(
    nodeId="ns=surface_technology;i=5014",
    browseName="ns=machinery;Monitoring",
    modellingRule="Optional",
    references=[
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=surface_technology;i=5017", browseName="ns=machinery;Consumption", description="Entry point for consumption information of the MachineryItem."
            )
        ),
        o6.hasComponent(
            ns0.objtypes.FolderType(nodeId="ns=surface_technology;i=5018", browseName="ns=machinery;Health", description="Entry point of health information of the MachineryItem.")
        ),
        o6.hasComponent(
            ns0.objtypes.FolderType(
                nodeId="ns=surface_technology;i=5019", browseName="ns=machinery;Process", description="Entry point for process information of the MachineryItem."
            )
        ),
        o6.hasComponent(o6.ns["ns=surface_technology;i=5020"]),
    ],
)
o6.reference(surface_technology_objtypes.STCompType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology;i=5014"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashSurfaceTechnologySlashGeneralTypesSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=surface_technology;i=5001",
    browseName="ns=surface_technology;http://opcfoundation.org/UA/SurfaceTechnology/GeneralTypes/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6001", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6002", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2026-04-01T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology;i=6003", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/SurfaceTechnology/GeneralTypes/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6004", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology;i=6005",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology;i=6006", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0], value=[]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6007", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=surface_technology;i=5002",
    browseName="ns=di;Identification",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology;i=6008",
                browseName="ns=di;ProductInstanceUri",
                description="A globally unique resource identifier provided by the manufacturer of the machine",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology;i=6009",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology;i=6010",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(surface_technology_objtypes.STSysType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology;i=5002"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=surface_technology;i=6011",
    browseName="CurrentState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6012", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6023", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6024", browseName="Name", dataType=o6.QualifiedName)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6025", browseName="Number", dataType=o6.UInt32)),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=surface_technology;i=6017",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6018", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6026", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6027", browseName="Name", dataType=o6.QualifiedName)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6028", browseName="Number", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6029", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=surface_technology;i=5009",
    browseName="ns=machinery;MachineryItemState",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology;i=6011"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=surface_technology;i=6015", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=surface_technology;i=6016", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasComponent(o6.ns["ns=surface_technology;i=6017"]),
    ],
)
o6.reference(o6.ns["ns=surface_technology;i=5008"], "i=47", o6.ns["ns=surface_technology;i=5009"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=surface_technology;i=6013",
    browseName="CurrentState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6014", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6030", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6031", browseName="Name", dataType=o6.QualifiedName)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6032", browseName="Number", dataType=o6.UInt32)),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=surface_technology;i=6021",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6022", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6033", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6034", browseName="Name", dataType=o6.QualifiedName)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6035", browseName="Number", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6036", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryOperationModeStateMachineType(
    nodeId="ns=surface_technology;i=5010",
    browseName="ns=machinery;MachineryOperationMode",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology;i=6013"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=surface_technology;i=6019", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=surface_technology;i=6020", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasComponent(o6.ns["ns=surface_technology;i=6021"]),
    ],
)
o6.reference(o6.ns["ns=surface_technology;i=5008"], "i=47", o6.ns["ns=surface_technology;i=5010"])
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology;i=5005",
    browseName="ns=machinery;MachineryBuildingBlocks",
    modellingRule="Mandatory",
    references=[
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=surface_technology;i=5007", browseName="ns=di;OperationCounters")),
        o6.hasAddIn(o6.ns["ns=surface_technology;i=5009"]),
        o6.hasAddIn(o6.ns["ns=surface_technology;i=5010"]),
    ],
)
o6.reference(surface_technology_objtypes.STSysType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology;i=5005"])
o6.reference(o6.ns["ns=surface_technology;i=5005"], "i=17604", o6.ns["ns=surface_technology;i=5002"])
o6.reference(o6.ns["ns=surface_technology;i=5005"], "i=17604", o6.ns["ns=surface_technology;i=5003"])
o6.reference(o6.ns["ns=surface_technology;i=5005"], "i=17604", o6.ns["ns=surface_technology;i=5004"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=surface_technology;i=5013",
    browseName="ns=di;Identification",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology;i=6037",
                browseName="ns=di;Manufacturer",
                description="A human-readable, localized name of the manufacturer of the MachineryItem.",
                dataType=o6.LocalizedText,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=surface_technology;i=6038",
                browseName="ns=di;SerialNumber",
                description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
                dataType=o6.String,
            )
        ),
    ],
)
o6.reference(surface_technology_objtypes.STCompType, ns0.reftypes.HasAddIn, o6.ns["ns=surface_technology;i=5013"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=surface_technology;i=6039",
    browseName="CurrentState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6040", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6051", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6052", browseName="Name", dataType=o6.QualifiedName)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6053", browseName="Number", dataType=o6.UInt32)),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=surface_technology;i=6045",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6046", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6054", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6055", browseName="Name", dataType=o6.QualifiedName)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6056", browseName="Number", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6057", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=surface_technology;i=5021",
    browseName="ns=machinery;MachineryItemState",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology;i=6039"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=surface_technology;i=6043", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=surface_technology;i=6044", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasComponent(o6.ns["ns=surface_technology;i=6045"]),
    ],
)
o6.reference(o6.ns["ns=surface_technology;i=5020"], "i=47", o6.ns["ns=surface_technology;i=5021"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=surface_technology;i=6041",
    browseName="CurrentState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6042", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6058", browseName="EffectiveDisplayName", dataType=o6.LocalizedText)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6059", browseName="Name", dataType=o6.QualifiedName)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6060", browseName="Number", dataType=o6.UInt32)),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=surface_technology;i=6049",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6050", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6061", browseName="EffectiveTransitionTime", dataType=ns0.datatypes.UtcTime)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6062", browseName="Name", dataType=o6.QualifiedName)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6063", browseName="Number", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6064", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryOperationModeStateMachineType(
    nodeId="ns=surface_technology;i=5011",
    browseName="ns=machinery;MachineryOperationMode",
    references=[
        o6.hasComponent(o6.ns["ns=surface_technology;i=6041"]),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=surface_technology;i=6047", browseName="AvailableStates", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasComponent(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=surface_technology;i=6048", browseName="AvailableTransitions", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasComponent(o6.ns["ns=surface_technology;i=6049"]),
    ],
)
o6.reference(o6.ns["ns=surface_technology;i=5020"], "i=47", o6.ns["ns=surface_technology;i=5011"])
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology;i=5015",
    browseName="ns=machinery;MachineryBuildingBlocks",
    modellingRule="Mandatory",
    references=[
        o6.hasAddIn(o6.ns["ns=surface_technology;i=5011"]),
        o6.hasAddIn(o6.ns["ns=surface_technology;i=5021"]),
        o6.hasAddIn(machinery.objtypes.MachineryOperationCounterType(nodeId="ns=surface_technology;i=5024", browseName="ns=di;OperationCounters")),
    ],
)
o6.reference(surface_technology_objtypes.STCompType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology;i=5015"])
o6.reference(o6.ns["ns=surface_technology;i=5015"], "i=17604", o6.ns["ns=surface_technology;i=5013"])
o6.reference(o6.ns["ns=surface_technology;i=5015"], "i=17604", o6.ns["ns=surface_technology;i=5014"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=surface_technology;i=6065",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6066", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=surface_technology;i=5027", browseName="ns=machinery;MachineryItemState", references=[o6.hasComponent(o6.ns["ns=surface_technology;i=6065"])]
)
o6.reference(o6.ns["ns=surface_technology;i=5026"], "i=17604", o6.ns["ns=surface_technology;i=5027"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=surface_technology;i=6067",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6068", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryOperationModeStateMachineType(
    nodeId="ns=surface_technology;i=5012", browseName="ns=machinery;MachineryOperationMode", references=[o6.hasComponent(o6.ns["ns=surface_technology;i=6067"])]
)
o6.reference(o6.ns["ns=surface_technology;i=5026"], "i=17604", o6.ns["ns=surface_technology;i=5012"])
ns0.objtypes.FolderType(
    nodeId="ns=surface_technology;i=5025",
    browseName="ns=surface_technology;State",
    modellingRule="Mandatory",
    references=[o6.hasComponent(o6.ns["ns=surface_technology;i=5012"]), o6.hasComponent(o6.ns["ns=surface_technology;i=5027"])],
)
o6.reference(surface_technology_objtypes.STSystemControllerType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology;i=5025"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=surface_technology;i=6070",
    browseName="CurrentState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6071", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6072", browseName="Number", dataType=o6.UInt32)),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=surface_technology;i=6074",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6075", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6076", browseName="Number", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6077", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)
ns0.objtypes.ProgramStateMachineType(
    nodeId="ns=surface_technology;i=5029",
    browseName="ns=surface_technology;StartUp",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6069", browseName="AutoDelete", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6073", browseName="Deletable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6078", browseName="RecycleCount", dataType=o6.Int32)),
        o6.hasComponent(o6.ns["ns=surface_technology;i=6070"]),
        o6.hasComponent(o6.ns["ns=surface_technology;i=6074"]),
    ],
)
o6.reference(surface_technology_objtypes.STBaseControllerType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology;i=5029"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=surface_technology;i=6080",
    browseName="CurrentState",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6081", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6082", browseName="Number", dataType=o6.UInt32)),
    ],
    dataType=o6.LocalizedText,
)
ns0.vartypes.FiniteTransitionVariableType(
    nodeId="ns=surface_technology;i=6084",
    browseName="LastTransition",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6085", browseName="Id", dataType=o6.NodeId)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6086", browseName="Number", dataType=o6.UInt32)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6087", browseName="TransitionTime", dataType=ns0.datatypes.UtcTime)),
    ],
    dataType=o6.LocalizedText,
)
ns0.objtypes.ProgramStateMachineType(
    nodeId="ns=surface_technology;i=5030",
    browseName="ns=surface_technology;ShutDown",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6079", browseName="AutoDelete", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6083", browseName="Deletable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=surface_technology;i=6088", browseName="RecycleCount", dataType=o6.Int32)),
        o6.hasComponent(o6.ns["ns=surface_technology;i=6080"]),
        o6.hasComponent(o6.ns["ns=surface_technology;i=6084"]),
    ],
)
o6.reference(surface_technology_objtypes.STBaseControllerType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology;i=5030"])


ns0.vartypes.PropertyType(
    nodeId="ns=surface_technology;i=6089",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=surface_technology;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="AliasNameSearchPattern", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ReferenceTypeFilter", dataType=o6.NodeId, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=surface_technology;i=6090",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=surface_technology;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="AliasNodeList", dataType=ns0.datatypes.AliasNameDataType, valueRank=1, arrayDimensions=[0])],
)
o6.call(
    nodeId="ns=surface_technology;i=7001",
    browseName="FindAlias",
    inputArgs=o6.hasProperty(o6.ns["ns=surface_technology;i=6089"]),
    outputArgs=o6.hasProperty(o6.ns["ns=surface_technology;i=6090"]),
)

ns0.objtypes.AliasNameCategoryType(
    nodeId="ns=surface_technology;i=5031",
    browseName="ns=surface_technology;STJobManagementAliases",
    modellingRule="Optional",
    references=[o6.hasComponent(o6.ns["ns=surface_technology;i=7001"])],
)
o6.reference(surface_technology_objtypes.STJobManagementType, ns0.reftypes.HasComponent, o6.ns["ns=surface_technology;i=5031"])


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, ns0, surface_technology_objtypes
