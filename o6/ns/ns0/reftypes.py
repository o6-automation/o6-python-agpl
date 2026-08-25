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

"""Generated OPC UA ns0 namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.referencetype(nodeId="i=31", browseName="References", displayName="References", symmetric=True, isAbstract=True)
class References:
    pass


@o6.referencetype(nodeId="i=32", browseName="NonHierarchicalReferences", displayName="NonHierarchicalReferences", symmetric=True, isAbstract=True)
class NonHierarchicalReferences(References):
    pass


@o6.referencetype(nodeId="i=33", browseName="HierarchicalReferences", displayName="HierarchicalReferences", inverseName="InverseHierarchicalReferences", isAbstract=True)
class HierarchicalReferences(References):
    pass


@o6.referencetype(nodeId="i=34", browseName="HasChild", displayName="HasChild", inverseName="ChildOf", isAbstract=True)
class HasChild(HierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=35", browseName="Organizes", displayName="Organizes", inverseName="OrganizedBy")
class Organizes(HierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=36", browseName="HasEventSource", displayName="HasEventSource", inverseName="EventSourceOf")
class HasEventSource(HierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=37", browseName="HasModellingRule", displayName="HasModellingRule", inverseName="ModellingRuleOf")
class HasModellingRule(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=38", browseName="HasEncoding", displayName="HasEncoding", inverseName="EncodingOf")
class HasEncoding(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=39", browseName="HasDescription", displayName="HasDescription", inverseName="DescriptionOf")
class HasDescription(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=40", browseName="HasTypeDefinition", displayName="HasTypeDefinition", inverseName="TypeDefinitionOf")
class HasTypeDefinition(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=41", browseName="GeneratesEvent", displayName="GeneratesEvent", inverseName="GeneratedBy")
class GeneratesEvent(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=44", browseName="Aggregates", displayName="Aggregates", inverseName="AggregatedBy", isAbstract=True)
class Aggregates(HasChild):
    pass


@o6.referencetype(nodeId="i=45", browseName="HasSubtype", displayName="HasSubtype", inverseName="SubtypeOf")
class HasSubtype(HasChild):
    pass


@o6.referencetype(nodeId="i=46", browseName="HasProperty", displayName="HasProperty", inverseName="PropertyOf")
class HasProperty(Aggregates):
    pass


@o6.referencetype(nodeId="i=47", browseName="HasComponent", displayName="HasComponent", inverseName="ComponentOf")
class HasComponent(Aggregates):
    pass


@o6.referencetype(nodeId="i=48", browseName="HasNotifier", displayName="HasNotifier", inverseName="NotifierOf")
class HasNotifier(HasEventSource):
    pass


@o6.referencetype(nodeId="i=49", browseName="HasOrderedComponent", displayName="HasOrderedComponent", inverseName="OrderedComponentOf")
class HasOrderedComponent(HasComponent):
    pass


@o6.referencetype(nodeId="i=51", browseName="FromState", displayName="FromState", inverseName="ToTransition")
class FromState(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=52", browseName="ToState", displayName="ToState", inverseName="FromTransition")
class ToState(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=53", browseName="HasCause", displayName="HasCause", inverseName="MayBeCausedBy")
class HasCause(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=54", browseName="HasEffect", displayName="HasEffect", inverseName="MayBeEffectedBy")
class HasEffect(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=56", browseName="HasHistoricalConfiguration", displayName="HasHistoricalConfiguration", inverseName="HistoricalConfigurationOf")
class HasHistoricalConfiguration(Aggregates):
    pass


@o6.referencetype(nodeId="i=117", browseName="HasSubStateMachine", displayName="HasSubStateMachine", inverseName="SubStateMachineOf")
class HasSubStateMachine(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=129", browseName="HasArgumentDescription", displayName="HasArgumentDescription", inverseName="ArgumentDescriptionOf")
class HasArgumentDescription(HasComponent):
    pass


@o6.referencetype(
    nodeId="i=131", browseName="HasOptionalInputArgumentDescription", displayName="HasOptionalInputArgumentDescription", inverseName="OptionalInputArgumentDescriptionOf"
)
class HasOptionalInputArgumentDescription(HasArgumentDescription):
    pass


@o6.referencetype(nodeId="i=3065", browseName="AlwaysGeneratesEvent", displayName="AlwaysGeneratesEvent", inverseName="AlwaysGeneratedBy")
class AlwaysGeneratesEvent(GeneratesEvent):
    pass


@o6.referencetype(nodeId="i=9004", browseName="HasTrueSubState", displayName="HasTrueSubState", inverseName="IsTrueSubStateOf")
class HasTrueSubState(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=9005", browseName="HasFalseSubState", displayName="HasFalseSubState", inverseName="IsFalseSubStateOf")
class HasFalseSubState(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=9006", browseName="HasCondition", displayName="HasCondition", inverseName="IsConditionOf")
class HasCondition(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=14476", browseName="HasPubSubConnection", displayName="HasPubSubConnection", inverseName="PubSubConnectionOf")
class HasPubSubConnection(HasComponent):
    pass


@o6.referencetype(nodeId="i=14936", browseName="DataSetToWriter", displayName="DataSetToWriter", inverseName="WriterToDataSet")
class DataSetToWriter(HierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=15112", browseName="HasGuard", displayName="HasGuard", inverseName="GuardOf")
class HasGuard(HasComponent):
    pass


@o6.referencetype(nodeId="i=15296", browseName="HasDataSetWriter", displayName="HasDataSetWriter", inverseName="IsWriterInGroup")
class HasDataSetWriter(HasComponent):
    pass


@o6.referencetype(nodeId="i=15297", browseName="HasDataSetReader", displayName="HasDataSetReader", inverseName="IsReaderInGroup")
class HasDataSetReader(HasComponent):
    pass


@o6.referencetype(nodeId="i=16361", browseName="HasAlarmSuppressionGroup", displayName="HasAlarmSuppressionGroup", inverseName="IsAlarmSuppressionGroupOf")
class HasAlarmSuppressionGroup(HasComponent):
    pass


@o6.referencetype(nodeId="i=16362", browseName="AlarmGroupMember", displayName="AlarmGroupMember", inverseName="MemberOfAlarmGroup")
class AlarmGroupMember(Organizes):
    pass


@o6.referencetype(nodeId="i=17276", browseName="HasEffectDisable", displayName="HasEffectDisable", inverseName="MayBeDisabledBy")
class HasEffectDisable(HasEffect):
    pass


@o6.referencetype(nodeId="i=17597", browseName="HasDictionaryEntry", displayName="HasDictionaryEntry", inverseName="DictionaryEntryOf")
class HasDictionaryEntry(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=17603", browseName="HasInterface", displayName="HasInterface", inverseName="InterfaceOf")
class HasInterface(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=17604", browseName="HasAddIn", displayName="HasAddIn", inverseName="AddInOf")
class HasAddIn(HasComponent):
    pass


@o6.referencetype(nodeId="i=17983", browseName="HasEffectEnable", displayName="HasEffectEnable", inverseName="MayBeEnabledBy")
class HasEffectEnable(HasEffect):
    pass


@o6.referencetype(nodeId="i=17984", browseName="HasEffectSuppressed", displayName="HasEffectSuppressed", inverseName="MayBeSuppressedBy")
class HasEffectSuppressed(HasEffect):
    pass


@o6.referencetype(nodeId="i=17985", browseName="HasEffectUnsuppressed", displayName="HasEffectUnsuppressed", inverseName="MayBeUnsuppressedBy")
class HasEffectUnsuppressed(HasEffect):
    pass


@o6.referencetype(nodeId="i=18804", browseName="HasWriterGroup", displayName="HasWriterGroup", inverseName="IsWriterGroupOf")
class HasWriterGroup(HasComponent):
    pass


@o6.referencetype(nodeId="i=18805", browseName="HasReaderGroup", displayName="HasReaderGroup", inverseName="IsReaderGroupOf")
class HasReaderGroup(HasComponent):
    pass


@o6.referencetype(nodeId="i=19814", browseName="UsesDataTypeRefinement", displayName="UsesDataTypeRefinement", inverseName="DataTypeRefinementUsedBy")
class UsesDataTypeRefinement(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=19815", browseName="HasFieldDescription", displayName="HasFieldDescription", inverseName="FieldDescriptionOf")
class HasFieldDescription(HierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=19816", browseName="HasFieldDescriptionSetMandatory", displayName="HasFieldDescriptionSetMandatory", inverseName="FieldDescriptionSetMandatoryOf")
class HasFieldDescriptionSetMandatory(HasFieldDescription):
    pass


@o6.referencetype(nodeId="i=19817", browseName="IsDisabledOptionalField", displayName="IsDisabledOptionalField", inverseName="DisabledOptionalFieldOf")
class IsDisabledOptionalField(HasFieldDescription):
    pass


@o6.referencetype(nodeId="i=19818", browseName="UsesSubtypeRestriction", displayName="UsesSubtypeRestriction", inverseName="SubtypeRestrictionUsedBy")
class UsesSubtypeRestriction(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=19819", browseName="AllowedSubtype", displayName="AllowedSubtype", inverseName="AllowedSubtypeOf")
class AllowedSubtype(HierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=19845", browseName="HasSerializationEntity", displayName="HasSerializationEntity", inverseName="SerializationEntityOf")
class HasSerializationEntity(HierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=19846", browseName="HasDataTypeRefinement", displayName="HasDataTypeRefinement", inverseName="DataTypeRefinementOf")
class HasDataTypeRefinement(HasChild):
    pass


@o6.referencetype(nodeId="i=23469", browseName="AliasFor", displayName="AliasFor", inverseName="HasAlias")
class AliasFor(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=23562", browseName="IsDeprecated", displayName="IsDeprecated", inverseName="Deprecates")
class IsDeprecated(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=24136", browseName="HasStructuredComponent", displayName="HasStructuredComponent", inverseName="IsStructuredComponentOf")
class HasStructuredComponent(HasComponent):
    pass


@o6.referencetype(nodeId="i=24137", browseName="AssociatedWith", displayName="AssociatedWith", symmetric=True)
class AssociatedWith(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=25237", browseName="UsesPriorityMappingTable", displayName="UsesPriorityMappingTable", inverseName="UsedByNetworkInterface")
class UsesPriorityMappingTable(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=25238", browseName="HasLowerLayerInterface", displayName="HasLowerLayerInterface", inverseName="HasHigherLayerInterface")
class HasLowerLayerInterface(HierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=25253", browseName="IsExecutableOn", displayName="IsExecutableOn", inverseName="CanExecute")
class IsExecutableOn(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=25254", browseName="Controls", displayName="Controls", inverseName="IsControlledBy")
class Controls(HierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=25255", browseName="Utilizes", displayName="Utilizes", inverseName="IsUtilizedBy")
class Utilizes(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=25256", browseName="Requires", displayName="Requires", inverseName="IsRequiredBy")
class Requires(HierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=25257", browseName="IsPhysicallyConnectedTo", displayName="IsPhysicallyConnectedTo", symmetric=True)
class IsPhysicallyConnectedTo(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=25258", browseName="RepresentsSameEntityAs", displayName="RepresentsSameEntityAs", symmetric=True)
class RepresentsSameEntityAs(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=25259", browseName="RepresentsSameHardwareAs", displayName="RepresentsSameHardwareAs", symmetric=True)
class RepresentsSameHardwareAs(RepresentsSameEntityAs):
    pass


@o6.referencetype(nodeId="i=25260", browseName="RepresentsSameFunctionalityAs", displayName="RepresentsSameFunctionalityAs", symmetric=True)
class RepresentsSameFunctionalityAs(RepresentsSameEntityAs):
    pass


@o6.referencetype(nodeId="i=25261", browseName="IsHostedBy", displayName="IsHostedBy", inverseName="Hosts")
class IsHostedBy(Utilizes):
    pass


@o6.referencetype(nodeId="i=25262", browseName="HasPhysicalComponent", displayName="HasPhysicalComponent", inverseName="PhysicalComponentOf")
class HasPhysicalComponent(HasComponent):
    pass


@o6.referencetype(nodeId="i=25263", browseName="HasContainedComponent", displayName="HasContainedComponent", inverseName="ContainedComponentOf")
class HasContainedComponent(HasPhysicalComponent):
    pass


@o6.referencetype(nodeId="i=25264", browseName="HasAttachedComponent", displayName="HasAttachedComponent", inverseName="AttachedComponentOf")
class HasAttachedComponent(HasPhysicalComponent):
    pass


@o6.referencetype(nodeId="i=25265", browseName="IsExecutingOn", displayName="IsExecutingOn", inverseName="Executes")
class IsExecutingOn(Utilizes):
    pass


@o6.referencetype(nodeId="i=25345", browseName="HasPushedSecurityGroup", displayName="HasPushedSecurityGroup", inverseName="HasPushTarget")
class HasPushedSecurityGroup(HierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=32059", browseName="AlarmSuppressionGroupMember", displayName="AlarmSuppressionGroupMember", inverseName="MemberOfAlarmSuppressionGroup")
class AlarmSuppressionGroupMember(AlarmGroupMember):
    pass


@o6.referencetype(nodeId="i=32407", browseName="HasKeyValueDescription", displayName="HasKeyValueDescription", inverseName="KeyValueDescriptionOf")
class HasKeyValueDescription(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=32558", browseName="HasEngineeringUnitDetails", displayName="HasEngineeringUnitDetails", inverseName="EngineeringUnitDetailsOf")
class HasEngineeringUnitDetails(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=32559", browseName="HasQuantity", displayName="HasQuantity", inverseName="QuantityOf")
class HasQuantity(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=32633", browseName="HasCurrentData", displayName="HasCurrentData", inverseName="HasHistoricalData")
class HasCurrentData(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=32634", browseName="HasCurrentEvent", displayName="HasCurrentEvent", inverseName="HasHistoricalEvent")
class HasCurrentEvent(NonHierarchicalReferences):
    pass


@o6.referencetype(nodeId="i=32679", browseName="HasReferenceDescription", displayName="HasReferenceDescription", inverseName="ReferenceDescriptionOf")
class HasReferenceDescription(HasChild):
    pass


del Any, TYPE_CHECKING, uuid, o6
