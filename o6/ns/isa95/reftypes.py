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

"""Generated OPC UA isa95 namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.referencetype(
    nodeId="ns=isa95;i=2009",
    browseName="ns=isa95;HasISA95Property",
    displayName="HasISA95Property",
    description="This ReferenceType is used to describe the ownership of ISA-95 Property",
    inverseName="ISA95PropertyOf",
)
class HasISA95Property(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4713",
    browseName="ns=isa95;HasISA95Attribute",
    displayName="HasISA95Attribute",
    description="This ReferenceType indicates an ownership of ISA95Attribute",
    inverseName="ISA95AttributeOf",
)
class HasISA95Attribute(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4714",
    browseName="ns=isa95;MadeUpOf",
    displayName="MadeUpOf",
    description="This ReferenceType is used to describe a shared aggregation",
    inverseName="ContainedBy",
    isAbstract=True,
)
class MadeUpOf(ns0.reftypes.Aggregates):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4910",
    browseName="ns=isa95;HasISA95ClassProperty",
    displayName="HasISA95ClassProperty",
    description="This ReferenceType is used to describe the ownership of an ISA95ClassProperty",
    inverseName="ISA95ClassPropertyOf",
)
class HasISA95ClassProperty(ns0.reftypes.HasComponent):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4911",
    browseName="ns=isa95;HasCDTSupplemental",
    displayName="HasCDTSupplemental",
    description="This ReferenceType indicates an ownership of supplemental elements regarding CDT",
    inverseName="CDTSupplementalOf",
)
class HasCDTSupplemental(ns0.reftypes.HasProperty):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4912",
    browseName="ns=isa95;DefinedBy",
    displayName="DefinedBy",
    description="This ReferenceType is used to describe a categorization of the SourceNode",
    inverseName="DefinitionOf",
    isAbstract=True,
)
class DefinedBy(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4913",
    browseName="ns=isa95;TestedBy",
    displayName="TestedBy",
    description="A reference that is used to describe an ISA-95 Test Specification that is associated with the SourceNode",
    inverseName="TestSpecificationOf",
    isAbstract=True,
)
class TestedBy(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4914",
    browseName="ns=isa95;ImplementedBy",
    displayName="ImplementedBy",
    description="A reference that is used to describe a relationship between ISA95Equipment and ISA95PhysicalAsset.",
    inverseName="ImplementationOf",
)
class ImplementedBy(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4915",
    browseName="ns=isa95;HasTestResult",
    displayName="HasTestResult",
    description="A reference that is used to describe the test results that are associated with an ISA95Property.",
    inverseName="TestResultOf",
)
class HasTestResult(ns0.reftypes.HasProperty):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4916",
    browseName="ns=isa95;ResultsForSpecification",
    displayName="ResultsForSpecification",
    description="A reference that is used to describe the test results that are associated with an ISA95Property.",
    inverseName="TestResultOf",
)
class ResultsForSpecification(ns0.reftypes.NonHierarchicalReferences):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4917",
    browseName="ns=isa95;DefinedByPersonnelClass",
    displayName="DefinedByPersonnelClass",
    description="This ReferenceType is used to describe a categorization of the SourceNode.",
    inverseName="PersonnelClassOf",
)
class DefinedByPersonnelClass(DefinedBy):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4918",
    browseName="ns=isa95;TestedByQualificationTest",
    displayName="TestedByQualificationTest",
    description="This ReferenceType is used to describe a qualification test that is associated with the SourceNode.",
    inverseName="QualificationTestOf",
)
class TestedByQualificationTest(TestedBy):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4919",
    browseName="ns=isa95;DefinedByEquipmentClass",
    displayName="DefinedByEquipmentClass",
    description="This ReferenceType is used to describe a categorization of the SourceNode.",
    inverseName="EquipmentClassOf",
)
class DefinedByEquipmentClass(DefinedBy):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4920",
    browseName="ns=isa95;TestedByEquipmentTest",
    displayName="TestedByEquipmentTest",
    description="This ReferenceType is used to describe a qualification test that is associated with the SourceNode.",
    inverseName="EquipmentTestOf",
)
class TestedByEquipmentTest(TestedBy):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4921",
    browseName="ns=isa95;DefinedByPhysicalAssetClass",
    displayName="DefinedByPhysicalAssetClass",
    description="This ReferenceType is used to describe a categorization of the SourceNode.",
    inverseName="PhysicalAssetClassOf",
)
class DefinedByPhysicalAssetClass(DefinedBy):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4922",
    browseName="ns=isa95;TestedByPhysicalAssetTest",
    displayName="TestedByPhysicalAssetTest",
    description="This ReferenceType is used to describe a qualification test that is associated with the SourceNode",
    inverseName="PhysicalAssetTestOf",
)
class TestedByPhysicalAssetTest(TestedBy):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4924",
    browseName="ns=isa95;TestedByMaterialTest",
    displayName="TestedByMaterialTest",
    description="This ReferenceType is used to describe a MaterialTestSpecification that is associated with the SourceNode",
    inverseName="MaterialTestOf",
)
class TestedByMaterialTest(TestedBy):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4925",
    browseName="ns=isa95;AssembledFrom",
    displayName="AssembledFrom",
    description="This ReferenceType is used to describe the assemblies that compose a material, where the assemblies are other material.",
    inverseName="AssemblyTo",
    isAbstract=True,
)
class AssembledFrom(ns0.reftypes.Aggregates):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4926",
    browseName="ns=isa95;AssembledFromDefinition",
    displayName="AssembledFromDefinition",
    description="This ReferenceType is used to describe the assemblies that compose a material, where the assemblies are other material.",
    inverseName="AssemblyToDefinition",
)
class AssembledFromDefinition(AssembledFrom):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4927",
    browseName="ns=isa95;AssembledFromClass",
    displayName="AssembledFromClass",
    description="This ReferenceType is used to describe the assemblies that compose a material, where the assemblies are other material.",
    inverseName="AssemblyToClass",
)
class AssembledFromClass(AssembledFrom):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=4928",
    browseName="ns=isa95;AssembledFromLot",
    displayName="AssembledFromLot",
    description="This ReferenceType is used to describe the assemblies that compose a material, where the assemblies are other material.",
    inverseName="AssemblyToLot",
)
class AssembledFromLot(AssembledFrom):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=5114",
    browseName="ns=isa95;LocatedIn",
    displayName="LocatedIn",
    description="A reference that is used to describe the test results that are associated with an ISA95Property.",
    inverseName="LocationOf",
)
class LocatedIn(ns0.reftypes.HasProperty):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=5115",
    browseName="ns=isa95;MadeUpOfEquipment",
    displayName="MadeUpOfEquipment",
    description="This ReferenceType is used to describe a shared aggregation",
    inverseName="ContainedByEquipment",
)
class MadeUpOfEquipment(MadeUpOf):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=5116",
    browseName="ns=isa95;MadeUpOfPhysicalAsset",
    displayName="MadeUpOfPhysicalAsset",
    description="This ReferenceType is used to describe a shared aggregation",
    inverseName="ContainedByPhysicalAsset",
)
class MadeUpOfPhysicalAsset(MadeUpOf):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=5117",
    browseName="ns=isa95;MadeUpOfMaterialSublot",
    displayName="MadeUpOfMaterialSublot",
    description="This ReferenceType is used to describe a shared aggregation",
    inverseName="ContainedByMaterialSublot",
)
class MadeUpOfMaterialSublot(MadeUpOf):
    pass


@o6.referencetype(
    nodeId="ns=isa95;i=5301",
    browseName="ns=isa95;DefinedByMaterialDefinition",
    displayName="DefinedByMaterialDefinition",
    description="This ReferenceType is used to describe a categorization of the SourceNode.",
    inverseName="MaterialClassOf",
)
class DefinedByMaterialDefinition(DefinedBy):
    pass


del Any, TYPE_CHECKING, uuid, o6, ns0
