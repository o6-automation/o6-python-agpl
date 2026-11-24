# Copyright (c) 2026 o6 Automation GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
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

"""Generated OPC UA wire_harness_vec namespace declarations."""

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


@o6.datatype(nodeId="ns=wire_harness_vec;i=1001", browseName="ns=wire_harness_vec;ARGB32ColorType", defaultEncodingId="ns=wire_harness_vec;i=5002")
class ARGB32ColorType(ns0.datatypes.Structure):
    value: o6.UInt32 = o6.field(name="Value")
    name: list[o6.String] = o6.field(name="Name", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=1002", browseName="ns=wire_harness_vec;IdBaseDataType", isAbstract=True, parent="i=22")
class IdBaseDataType:
    pass


@o6.enumtype(nodeId="ns=wire_harness_vec;i=1003", browseName="ns=wire_harness_vec;CrimpBarrelType")
class CrimpBarrelType(ns0.datatypes.Enumeration):
    OPEN = o6.enumfield(0, name="Open")
    CLOSED = o6.enumfield(1, name="Closed")


@o6.datatype(nodeId="ns=wire_harness_vec;i=3012", browseName="ns=wire_harness_vec;ExtendableElement", isAbstract=True)
class ExtendableElement(ns0.datatypes.Structure):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=3010", browseName="ns=wire_harness_vec;ConfigurableElement", isAbstract=True)
class ConfigurableElement(ExtendableElement):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=3013", browseName="ns=wire_harness_vec;ItemVersion", isAbstract=True)
class ItemVersion(ExtendableElement):
    id: o6.String
    companyName: list[o6.String] = o6.field(name="CompanyName", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3159", browseName="ns=wire_harness_vec;PartVersion", defaultEncodingId="ns=wire_harness_vec;i=5026")
class PartVersion(ItemVersion):
    id: o6.String
    companyName: list[o6.String] = o6.field(name="CompanyName", arrayDimensions=[1])
    partNumber: o6.String = o6.field(name="PartNumber")


@o6.enumtype(nodeId="ns=wire_harness_vec;i=3160", browseName="ns=wire_harness_vec;PrimaryPartType")
class PrimaryPartType(ns0.datatypes.Enumeration):
    ANTENNA = o6.enumfield(0, name="Antenna")
    BATTERY = o6.enumfield(1, name="Battery")
    BOLT_MOUNTED_FIXING = o6.enumfield(2, name="BoltMountedFixing")
    BOLT_TERMINAL = o6.enumfield(3, name="BoltTerminal")
    BRIDGE_TERMINAL = o6.enumfield(4, name="BridgeTerminal")
    CABLE_DUCT = o6.enumfield(5, name="CableDuct")
    CABLE_TIE = o6.enumfield(6, name="CableTie")
    CAPACITOR = o6.enumfield(7, name="Capacitor")
    CAVITY_ACCESSORY = o6.enumfield(8, name="CavityAccessory")
    CAVITY_PLUG = o6.enumfield(9, name="CavityPlug")
    CAVITY_SEAL = o6.enumfield(10, name="CavitySeal")
    CONNECTOR_HOUSING = o6.enumfield(11, name="ConnectorHousing")
    CONNECTOR_HOUSING_CAP = o6.enumfield(12, name="ConnectorHousingCap")
    CONNECTOR_HOUSING_COVER = o6.enumfield(13, name="ConnectorHousingCover")
    CORRUGATED_PIPE = o6.enumfield(14, name="CorrugatedPipe")
    DIODE = o6.enumfield(15, name="Diode")
    EDGE_MOUNTED_FIXING = o6.enumfield(16, name="EdgeMountedFixing")
    EE_COMPONENT = o6.enumfield(17, name="EEComponent")
    FERRITE = o6.enumfield(18, name="Ferrite")
    FITTING = o6.enumfield(19, name="Fitting")
    FIXING = o6.enumfield(20, name="Fixing")
    FUSE = o6.enumfield(21, name="Fuse")
    GROMMET = o6.enumfield(22, name="Grommet")
    HOLE_MOUNTED_FIXING = o6.enumfield(23, name="HoleMountedFixing")
    MULTI_CAVITY_PLUG = o6.enumfield(24, name="MultiCavityPlug")
    MULTI_CAVITY_SEAL = o6.enumfield(25, name="MultiCavitySeal")
    MULTI_FUSE = o6.enumfield(26, name="MultiFuse")
    OTHER = o6.enumfield(27, name="Other")
    OPEN_WIRE_END_TERMINAL = o6.enumfield(28, name="OpenWireEndTerminal")
    OPEN_WIRE_END = o6.enumfield(29, name="OpenWireEnd")
    PART_STRUCTURE = o6.enumfield(30, name="PartStructure")
    PLUGGABLE_TERMINAL = o6.enumfield(31, name="PluggableTerminal")
    POTENTIAL_DISTRIBUTOR = o6.enumfield(32, name="PotentialDistributor")
    RELAY = o6.enumfield(33, name="Relay")
    RING_TERMINAL = o6.enumfield(34, name="RingTerminal")
    SHRINKABLE_TUBE = o6.enumfield(35, name="ShrinkableTube")
    SPLICE_TERMINAL = o6.enumfield(36, name="SpliceTerminal")
    STRIPE = o6.enumfield(37, name="Stripe")
    TAPE = o6.enumfield(38, name="Tape")
    TERMINAL = o6.enumfield(39, name="Terminal")
    TUBE = o6.enumfield(40, name="Tube")
    WIRE = o6.enumfield(41, name="Wire")
    WIRE_END_ACCESSORY = o6.enumfield(42, name="WireEndAccessory")
    WIRE_PROTECTION = o6.enumfield(43, name="WireProtection")


@o6.datatype(nodeId="ns=wire_harness_vec;i=3205", browseName="ns=wire_harness_vec;RoutableElement", isAbstract=True)
class RoutableElement(ConfigurableElement):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=3207", browseName="ns=wire_harness_vec;Specification", isAbstract=True)
class Specification(ExtendableElement):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3011", browseName="ns=wire_harness_vec;DocumentVersion", defaultEncodingId="ns=wire_harness_vec;i=5023")
class DocumentVersion(ItemVersion):
    id: o6.String
    companyName: list[o6.String] = o6.field(name="CompanyName", arrayDimensions=[1])
    documentNumber: list[o6.String] = o6.field(name="DocumentNumber", arrayDimensions=[1])
    documentVersion: list[o6.String] = o6.field(name="DocumentVersion", arrayDimensions=[1])
    digitalRepresentationIndex: list[o6.String] = o6.field(name="DigitalRepresentationIndex", arrayDimensions=[1])
    specification: list[Specification] = o6.field(name="Specification", arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3158", browseName="ns=wire_harness_vec;PartOrUsageRelatedSpecification", defaultEncodingId="ns=wire_harness_vec;i=5056")
class PartOrUsageRelatedSpecification(Specification):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    specialPartType: list[o6.String] = o6.field(name="SpecialPartType", arrayDimensions=[1])
    describedPart: list[PartVersion] = o6.field(name="DescribedPart", arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3277", browseName="ns=wire_harness_vec;ResourceVersion", defaultEncodingId="ns=wire_harness_vec;i=5029")
class ResourceVersion(ItemVersion):
    id: o6.String
    companyName: list[o6.String] = o6.field(name="CompanyName", arrayDimensions=[1])
    resourceNumber: o6.String = o6.field(name="ResourceNumber")
    resourceVersion: o6.String = o6.field(name="ResourceVersion")


@o6.datatype(nodeId="ns=wire_harness_vec;i=3433", browseName="ns=wire_harness_vec;CavityPartSpecification", isAbstract=True)
class CavityPartSpecification(PartOrUsageRelatedSpecification):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    specialPartType: list[o6.String] = o6.field(name="SpecialPartType", arrayDimensions=[1])
    describedPart: list[PartVersion] = o6.field(name="DescribedPart", arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3296", browseName="ns=wire_harness_vec;CavitySealSpecification", defaultEncodingId="ns=wire_harness_vec;i=5059")
class CavitySealSpecification(CavityPartSpecification):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    specialPartType: list[o6.String] = o6.field(name="SpecialPartType", arrayDimensions=[1])
    describedPart: list[PartVersion] = o6.field(name="DescribedPart", arrayDimensions=[0])


@o6.enumtype(nodeId="ns=wire_harness_vec;i=3500", browseName="ns=wire_harness_vec;ConductorType")
class ConductorType(ns0.datatypes.Enumeration):
    RIGID = o6.enumfield(0, name="Rigid")
    STRANDED = o6.enumfield(1, name="Stranded")
    FOIL = o6.enumfield(2, name="Foil")
    BRAIDED = o6.enumfield(3, name="Braided")


@o6.datatype(nodeId="ns=wire_harness_vec;i=3705", browseName="ns=wire_harness_vec;Role", isAbstract=True)
class Role(ExtendableElement):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3703", browseName="ns=wire_harness_vec;OccurrenceOrUsage", isAbstract=True)
class OccurrenceOrUsage(ConfigurableElement):
    id: o6.String
    identification: o6.String = o6.field(name="Identification")
    role: list[Role] = o6.field(name="Role", arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3757", browseName="ns=wire_harness_vec;CavityPartRole", isAbstract=True)
class CavityPartRole(Role):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3942", browseName="ns=wire_harness_vec;PartOccurrence", defaultEncodingId="ns=wire_harness_vec;i=5011")
class PartOccurrence(OccurrenceOrUsage):
    id: o6.String
    identification: o6.String = o6.field(name="Identification")
    role: list[Role] = o6.field(name="Role", arrayDimensions=[0])
    part: list[PartVersion] = o6.field(name="Part", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3941", browseName="ns=wire_harness_vec;CompositionSpecification", defaultEncodingId="ns=wire_harness_vec;i=5044")
class CompositionSpecification(Specification):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    component: list[PartOccurrence] = o6.field(name="Component", arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=4026", browseName="ns=wire_harness_vec;Material", defaultEncodingId="ns=wire_harness_vec;i=5224")
class Material(ns0.datatypes.Structure):
    key: o6.String = o6.field(name="Key")
    referenceSystem: o6.String = o6.field(name="ReferenceSystem")


@o6.datatype(nodeId="ns=wire_harness_vec;i=4091", browseName="ns=wire_harness_vec;Tolerance", defaultEncodingId="ns=wire_harness_vec;i=5080")
class Tolerance(ExtendableElement):
    id: o6.String
    lowerBoundary: o6.Double = o6.field(name="LowerBoundary")
    upperBoundary: o6.Double = o6.field(name="UpperBoundary")


@o6.datatype(nodeId="ns=wire_harness_vec;i=4098", browseName="ns=wire_harness_vec;ValueWithUnit", isAbstract=True)
class ValueWithUnit(ns0.datatypes.Structure):
    unitComponent: ns0.datatypes.EUInformation = o6.field(name="UnitComponent")


@o6.datatype(nodeId="ns=wire_harness_vec;i=4027", browseName="ns=wire_harness_vec;NumericalValue", defaultEncodingId="ns=wire_harness_vec;i=5230")
class NumericalValue(ValueWithUnit):
    unitComponent: ns0.datatypes.EUInformation = o6.field(name="UnitComponent")
    valueComponent: o6.Double = o6.field(name="ValueComponent")
    tolerance: list[Tolerance] = o6.field(name="Tolerance", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3300", browseName="ns=wire_harness_vec;ConductorSpecification", isAbstract=True)
class ConductorSpecification(Specification):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    crossSectionArea: list[NumericalValue] = o6.field(name="CrossSectionArea", arrayDimensions=[1])
    type: list[ConductorType] = o6.field(name="Type", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3302", browseName="ns=wire_harness_vec;CoreSpecification", defaultEncodingId="ns=wire_harness_vec;i=5047")
class CoreSpecification(ConductorSpecification):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    crossSectionArea: list[NumericalValue] = o6.field(name="CrossSectionArea", arrayDimensions=[1])
    type: list[ConductorType] = o6.field(name="Type", arrayDimensions=[1])
    outsideDiameter: list[NumericalValue] = o6.field(name="OutsideDiameter", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3308", browseName="ns=wire_harness_vec;InsulationSpecification", defaultEncodingId="ns=wire_harness_vec;i=5053")
class InsulationSpecification(Specification):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    baseColor: ARGB32ColorType = o6.field(name="BaseColor")
    firstIdentificationColor: list[ARGB32ColorType] = o6.field(name="FirstIdentificationColor", arrayDimensions=[1])
    secondIdentificationColor: list[ARGB32ColorType] = o6.field(name="SecondIdentificationColor", arrayDimensions=[1])
    thickness: list[NumericalValue] = o6.field(name="Thickness", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3377", browseName="ns=wire_harness_vec;WireElementSpecification", defaultEncodingId="ns=wire_harness_vec;i=5074")
class WireElementSpecification(Specification):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    outsideDiameter: list[NumericalValue] = o6.field(name="OutsideDiameter", arrayDimensions=[1])
    conductorSpecification: list[ConductorSpecification] = o6.field(name="ConductorSpecification", arrayDimensions=[1])
    insulationSpecification: list[InsulationSpecification] = o6.field(name="InsulationSpecification", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3376", browseName="ns=wire_harness_vec;WireElement", defaultEncodingId="ns=wire_harness_vec;i=5083")
class WireElement(ExtendableElement):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    wireElementSpecification: WireElementSpecification = o6.field(name="WireElementSpecification")
    subWireElement: list[WireElement] = o6.field(name="SubWireElement", arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3381", browseName="ns=wire_harness_vec;WireSpecification", defaultEncodingId="ns=wire_harness_vec;i=5071")
class WireSpecification(PartOrUsageRelatedSpecification):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    specialPartType: list[o6.String] = o6.field(name="SpecialPartType", arrayDimensions=[1])
    describedPart: list[PartVersion] = o6.field(name="DescribedPart", arrayDimensions=[0])
    wireElement: WireElement = o6.field(name="WireElement")


@o6.datatype(nodeId="ns=wire_harness_vec;i=3731", browseName="ns=wire_harness_vec;WireEnd", defaultEncodingId="ns=wire_harness_vec;i=5086")
class WireEnd(ExtendableElement):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    positionOnWire: o6.Double = o6.field(name="PositionOnWire")
    strippingLength: list[NumericalValue] = o6.field(name="StrippingLength", arrayDimensions=[1])
    insulationPullbackLength: list[NumericalValue] = o6.field(name="InsulationPullbackLength", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=4088", browseName="ns=wire_harness_vec;Size", defaultEncodingId="ns=wire_harness_vec;i=5227")
class Size(ns0.datatypes.Structure):
    width: NumericalValue = o6.field(name="Width")
    height: NumericalValue = o6.field(name="Height")


@o6.datatype(nodeId="ns=wire_harness_vec;i=3655", browseName="ns=wire_harness_vec;CrimpDetail", isAbstract=True)
class CrimpDetail(ExtendableElement):
    id: o6.String
    size: list[Size] = o6.field(name="Size", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3653", browseName="ns=wire_harness_vec;InsulationCrimpDetail", defaultEncodingId="ns=wire_harness_vec;i=5020")
class InsulationCrimpDetail(CrimpDetail):
    id: o6.String
    size: list[Size] = o6.field(name="Size", arrayDimensions=[1])
    pullOffForce: list[NumericalValue] = o6.field(name="PullOffForce", arrayDimensions=[1])
    appliesTo: InsulationSpecification = o6.field(name="AppliesTo")


@o6.datatype(nodeId="ns=wire_harness_vec;i=3654", browseName="ns=wire_harness_vec;CoreCrimpDetail", defaultEncodingId="ns=wire_harness_vec;i=5017")
class CoreCrimpDetail(CrimpDetail):
    id: o6.String
    size: list[Size] = o6.field(name="Size", arrayDimensions=[1])
    appliesTo: ConductorSpecification = o6.field(name="AppliesTo")
    insulationCrimpDetails: list[InsulationCrimpDetail] = o6.field(name="InsulationCrimpDetails", arrayDimensions=[0])
    pullOffForce: list[NumericalValue] = o6.field(name="PullOffForce", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=4097", browseName="ns=wire_harness_vec;ValueRange", defaultEncodingId="ns=wire_harness_vec;i=5233")
class ValueRange(ValueWithUnit):
    unitComponent: ns0.datatypes.EUInformation = o6.field(name="UnitComponent")
    minimum: o6.Double = o6.field(name="Minimum")
    maximum: o6.Double = o6.field(name="Maximum")


@o6.datatype(nodeId="ns=wire_harness_vec;i=3380", browseName="ns=wire_harness_vec;WireReceptionSpecification", defaultEncodingId="ns=wire_harness_vec;i=5077")
class WireReceptionSpecification(Specification):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    insulationDisplacementLength: NumericalValue = o6.field(name="InsulationDisplacementLength")
    conductorCrimpLength: list[NumericalValue] = o6.field(name="ConductorCrimpLength", arrayDimensions=[1])
    crimpConnectionLength: NumericalValue = o6.field(name="CrimpConnectionLength")
    insulationCrimpLength: list[NumericalValue] = o6.field(name="InsulationCrimpLength", arrayDimensions=[1])
    wireTipProtrusion: list[ValueRange] = o6.field(name="WireTipProtrusion", arrayDimensions=[1])
    coreCrimpDetails: list[CoreCrimpDetail] = o6.field(name="CoreCrimpDetails", arrayDimensions=[0])
    crimpBarrelType: CrimpBarrelType = o6.field(name="CrimpBarrelType")


@o6.datatype(nodeId="ns=wire_harness_vec;i=3379", browseName="ns=wire_harness_vec;WireReception", defaultEncodingId="ns=wire_harness_vec;i=5095")
class WireReception(ExtendableElement):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    rotation: list[NumericalValue] = o6.field(name="Rotation", arrayDimensions=[1])
    wireReceptionSpecification: WireReceptionSpecification = o6.field(name="WireReceptionSpecification")


@o6.datatype(nodeId="ns=wire_harness_vec;i=3374", browseName="ns=wire_harness_vec;TerminalSpecification", defaultEncodingId="ns=wire_harness_vec;i=5065")
class TerminalSpecification(PartOrUsageRelatedSpecification):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    specialPartType: list[o6.String] = o6.field(name="SpecialPartType", arrayDimensions=[1])
    describedPart: list[PartVersion] = o6.field(name="DescribedPart", arrayDimensions=[0])
    connectionALength: list[NumericalValue] = o6.field(name="ConnectionALength", arrayDimensions=[1])
    overallLength: NumericalValue = o6.field(name="OverallLength")
    wireReception: list[WireReception] = o6.field(name="WireReception", arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3361", browseName="ns=wire_harness_vec;PluggableTerminalSpecification", defaultEncodingId="ns=wire_harness_vec;i=5068")
class PluggableTerminalSpecification(TerminalSpecification):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    specialPartType: list[o6.String] = o6.field(name="SpecialPartType", arrayDimensions=[1])
    describedPart: list[PartVersion] = o6.field(name="DescribedPart", arrayDimensions=[0])
    connectionALength: list[NumericalValue] = o6.field(name="ConnectionALength", arrayDimensions=[1])
    overallLength: NumericalValue = o6.field(name="OverallLength")
    wireReception: list[WireReception] = o6.field(name="WireReception", arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=4126", browseName="ns=wire_harness_vec;BoundingBox", defaultEncodingId="ns=wire_harness_vec;i=5005")
class BoundingBox(ExtendableElement):
    id: o6.String
    x: NumericalValue = o6.field(name="X")
    y: NumericalValue = o6.field(name="Y")
    z: NumericalValue = o6.field(name="Z")


@o6.datatype(nodeId="ns=wire_harness_vec;i=3306", browseName="ns=wire_harness_vec;GeneralTechnicalPartSpecification", defaultEncodingId="ns=wire_harness_vec;i=5062")
class GeneralTechnicalPartSpecification(PartOrUsageRelatedSpecification):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    specialPartType: list[o6.String] = o6.field(name="SpecialPartType", arrayDimensions=[1])
    describedPart: list[PartVersion] = o6.field(name="DescribedPart", arrayDimensions=[0])
    colorInformation: list[ARGB32ColorType] = o6.field(name="ColorInformation", arrayDimensions=[1])
    boundingBox: list[BoundingBox] = o6.field(name="BoundingBox", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=6005", browseName="ns=wire_harness_vec;ContactPointIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5125")
class ContactPointIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6006", browseName="ns=wire_harness_vec;ContactingSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5122")
class ContactingSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6007", browseName="ns=wire_harness_vec;WireMountingIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5206")
class WireMountingIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6008", browseName="ns=wire_harness_vec;WireMountingDetailIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5203")
class WireMountingDetailIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6010", browseName="ns=wire_harness_vec;ConfigurableElementIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5119")
class ConfigurableElementIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6011", browseName="ns=wire_harness_vec;DocumentVersionIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5137")
class DocumentVersionIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6012", browseName="ns=wire_harness_vec;ExtendableElementIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5140")
class ExtendableElementIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6013", browseName="ns=wire_harness_vec;ItemVersionIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5152")
class ItemVersionIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6158", browseName="ns=wire_harness_vec;PartOrUsageRelatedSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5161")
class PartOrUsageRelatedSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6159", browseName="ns=wire_harness_vec;PartVersionIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5164")
class PartVersionIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6205", browseName="ns=wire_harness_vec;RoutableElementIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5179")
class RoutableElementIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6207", browseName="ns=wire_harness_vec;SpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5182")
class SpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6277", browseName="ns=wire_harness_vec;ResourceVersionIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5173")
class ResourceVersionIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6296", browseName="ns=wire_harness_vec;CavitySealSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5110")
class CavitySealSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=3710", browseName="ns=wire_harness_vec;CavitySealRole", defaultEncodingId="ns=wire_harness_vec;i=5032")
class CavitySealRole(CavityPartRole):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    cavitySealSpecification: CavitySealSpecificationIdDataType = o6.field(name="CavitySealSpecification")


@o6.datatype(nodeId="ns=wire_harness_vec;i=6300", browseName="ns=wire_harness_vec;ConductorSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5116")
class ConductorSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6302", browseName="ns=wire_harness_vec;CoreSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5131")
class CoreSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6306", browseName="ns=wire_harness_vec;GeneralTechnicalPartSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5143")
class GeneralTechnicalPartSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6308", browseName="ns=wire_harness_vec;InsulationSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5149")
class InsulationSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6361", browseName="ns=wire_harness_vec;PluggableTerminalSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5170")
class PluggableTerminalSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6374", browseName="ns=wire_harness_vec;TerminalSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5188")
class TerminalSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6376", browseName="ns=wire_harness_vec;WireElementIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5191")
class WireElementIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=3730", browseName="ns=wire_harness_vec;WireElementReference", defaultEncodingId="ns=wire_harness_vec;i=5014")
class WireElementReference(RoutableElement):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    referencedWireElement: WireElementIdDataType = o6.field(name="ReferencedWireElement")
    wireEnd: list[WireEnd] = o6.field(name="WireEnd", arrayDimensions=[0])
    wireLength: list[NumericalValue] = o6.field(name="WireLength", arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=6377", browseName="ns=wire_harness_vec;WireElementSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5197")
class WireElementSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6379", browseName="ns=wire_harness_vec;WireReceptionIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5209")
class WireReceptionIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=3736", browseName="ns=wire_harness_vec;WireReceptionReference", defaultEncodingId="ns=wire_harness_vec;i=5098")
class WireReceptionReference(ExtendableElement):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    wireReception: WireReceptionIdDataType = o6.field(name="WireReception")


@o6.datatype(nodeId="ns=wire_harness_vec;i=3729", browseName="ns=wire_harness_vec;TerminalRole", defaultEncodingId="ns=wire_harness_vec;i=5035")
class TerminalRole(Role):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    terminalSpecification: TerminalSpecificationIdDataType = o6.field(name="TerminalSpecification")
    wireReceptionReference: list[WireReceptionReference] = o6.field(name="WireReceptionReference", arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3719", browseName="ns=wire_harness_vec;PluggableTerminalRole", defaultEncodingId="ns=wire_harness_vec;i=5038")
class PluggableTerminalRole(TerminalRole):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    terminalSpecification: TerminalSpecificationIdDataType = o6.field(name="TerminalSpecification")
    wireReceptionReference: list[WireReceptionReference] = o6.field(name="WireReceptionReference", arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=6380", browseName="ns=wire_harness_vec;WireReceptionSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5215")
class WireReceptionSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6381", browseName="ns=wire_harness_vec;WireSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5221")
class WireSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=3735", browseName="ns=wire_harness_vec;WireRole", defaultEncodingId="ns=wire_harness_vec;i=5041")
class WireRole(Role):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    wireSpecification: WireSpecificationIdDataType = o6.field(name="WireSpecification")
    wireElementReference: list[WireElementReference] = o6.field(name="WireElementReference", arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=6433", browseName="ns=wire_harness_vec;CavityPartSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5104")
class CavityPartSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6653", browseName="ns=wire_harness_vec;InsulationCrimpDetailIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5146")
class InsulationCrimpDetailIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6654", browseName="ns=wire_harness_vec;CoreCrimpDetailIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5128")
class CoreCrimpDetailIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6655", browseName="ns=wire_harness_vec;CrimpDetailIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5134")
class CrimpDetailIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6703", browseName="ns=wire_harness_vec;OccurrenceOrUsageIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5155")
class OccurrenceOrUsageIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6705", browseName="ns=wire_harness_vec;RoleIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5176")
class RoleIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6710", browseName="ns=wire_harness_vec;CavitySealRoleIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5107")
class CavitySealRoleIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6719", browseName="ns=wire_harness_vec;PluggableTerminalRoleIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5167")
class PluggableTerminalRoleIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6729", browseName="ns=wire_harness_vec;TerminalRoleIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5185")
class TerminalRoleIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6730", browseName="ns=wire_harness_vec;WireElementReferenceIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5194")
class WireElementReferenceIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6731", browseName="ns=wire_harness_vec;WireEndIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5200")
class WireEndIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6735", browseName="ns=wire_harness_vec;WireRoleIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5218")
class WireRoleIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6736", browseName="ns=wire_harness_vec;WireReceptionReferenceIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5212")
class WireReceptionReferenceIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=3008", browseName="ns=wire_harness_vec;WireMountingDetail", defaultEncodingId="ns=wire_harness_vec;i=5092")
class WireMountingDetail(ExtendableElement):
    id: o6.String
    coreCrimpSize: list[Size] = o6.field(name="CoreCrimpSize", arrayDimensions=[1])
    insulationCrimpSize: list[Size] = o6.field(name="InsulationCrimpSize", arrayDimensions=[1])
    wireTipProtrusion: list[ValueRange] = o6.field(name="WireTipProtrusion", arrayDimensions=[1])
    contactedWireReception: WireReceptionReferenceIdDataType = o6.field(name="ContactedWireReception")
    referencedWireEnd: list[WireEndIdDataType] = o6.field(name="ReferencedWireEnd", arrayDimensions=[0])
    absoluteSealPosition: NumericalValue = o6.field(name="AbsoluteSealPosition")
    corePullOffForce: list[NumericalValue] = o6.field(name="CorePullOffForce", arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3007", browseName="ns=wire_harness_vec;WireMounting", defaultEncodingId="ns=wire_harness_vec;i=5089")
class WireMounting(ExtendableElement):
    id: o6.String
    mountedCavitySeal: list[CavitySealRoleIdDataType] = o6.field(name="MountedCavitySeal", arrayDimensions=[1])
    referencedWireEnd: list[WireEndIdDataType] = o6.field(name="ReferencedWireEnd", arrayDimensions=[0])
    wireMountingDetail: list[WireMountingDetail] = o6.field(name="WireMountingDetail", arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3005", browseName="ns=wire_harness_vec;ContactPoint", defaultEncodingId="ns=wire_harness_vec;i=5008")
class ContactPoint(ConfigurableElement):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    mountedTerminal: list[TerminalRoleIdDataType] = o6.field(name="MountedTerminal", arrayDimensions=[1])
    wireMounting: list[WireMounting] = o6.field(name="WireMounting", arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3006", browseName="ns=wire_harness_vec;ContactingSpecification", defaultEncodingId="ns=wire_harness_vec;i=5050")
class ContactingSpecification(Specification):
    id: o6.String
    identification: list[o6.String] = o6.field(name="Identification", arrayDimensions=[1])
    contactPoint: list[ContactPoint] = o6.field(name="ContactPoint", arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=6757", browseName="ns=wire_harness_vec;CavityPartRoleIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5101")
class CavityPartRoleIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6941", browseName="ns=wire_harness_vec;CompositionSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5113")
class CompositionSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6942", browseName="ns=wire_harness_vec;PartOccurrenceIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5158")
class PartOccurrenceIdDataType(IdBaseDataType):
    id: o6.String


del Any, TYPE_CHECKING, uuid, o6, ns0
