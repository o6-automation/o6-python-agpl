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


@o6.datatype(nodeId="ns=wire_harness_vec;i=1001", browseName="ARGB32ColorType", defaultEncodingId="ns=wire_harness_vec;i=5002")
class ARGB32ColorType(ns0.datatypes.Structure):
    value: o6.UInt32
    name: list[o6.String] = o6.field(arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=1002", browseName="IdBaseDataType", isAbstract=True, parent="i=22")
class IdBaseDataType:
    pass


@o6.enumtype(nodeId="ns=wire_harness_vec;i=1003", browseName="CrimpBarrelType")
class CrimpBarrelType(ns0.datatypes.Enumeration):
    OPEN = o6.enumfield(0, name="Open")
    CLOSED = o6.enumfield(1, name="Closed")


@o6.datatype(nodeId="ns=wire_harness_vec;i=3012", browseName="ExtendableElement", isAbstract=True)
class ExtendableElement(ns0.datatypes.Structure):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=3010", browseName="ConfigurableElement", isAbstract=True)
class ConfigurableElement(ExtendableElement):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=3013", browseName="ItemVersion", isAbstract=True)
class ItemVersion(ExtendableElement):
    id: o6.String
    companyName: list[o6.String] = o6.field(arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3159", browseName="PartVersion", defaultEncodingId="ns=wire_harness_vec;i=5026")
class PartVersion(ItemVersion):
    id: o6.String
    companyName: list[o6.String]
    partNumber: o6.String


@o6.enumtype(nodeId="ns=wire_harness_vec;i=3160", browseName="PrimaryPartType")
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


@o6.datatype(nodeId="ns=wire_harness_vec;i=3205", browseName="RoutableElement", isAbstract=True)
class RoutableElement(ConfigurableElement):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=3207", browseName="Specification", isAbstract=True)
class Specification(ExtendableElement):
    id: o6.String
    identification: list[o6.String] = o6.field(arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3011", browseName="DocumentVersion", defaultEncodingId="ns=wire_harness_vec;i=5023")
class DocumentVersion(ItemVersion):
    id: o6.String
    companyName: list[o6.String]
    documentNumber: list[o6.String] = o6.field(arrayDimensions=[1])
    documentVersion: list[o6.String] = o6.field(arrayDimensions=[1])
    digitalRepresentationIndex: list[o6.String] = o6.field(arrayDimensions=[1])
    specification: list[Specification] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3158", browseName="PartOrUsageRelatedSpecification", defaultEncodingId="ns=wire_harness_vec;i=5056")
class PartOrUsageRelatedSpecification(Specification):
    id: o6.String
    identification: list[o6.String]
    specialPartType: list[o6.String] = o6.field(arrayDimensions=[1])
    describedPart: list[PartVersion] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3277", browseName="ResourceVersion", defaultEncodingId="ns=wire_harness_vec;i=5029")
class ResourceVersion(ItemVersion):
    id: o6.String
    companyName: list[o6.String]
    resourceNumber: o6.String
    resourceVersion: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=3433", browseName="CavityPartSpecification", isAbstract=True)
class CavityPartSpecification(PartOrUsageRelatedSpecification):
    id: o6.String
    identification: list[o6.String]
    specialPartType: list[o6.String]
    describedPart: list[PartVersion]


@o6.datatype(nodeId="ns=wire_harness_vec;i=3296", browseName="CavitySealSpecification", defaultEncodingId="ns=wire_harness_vec;i=5059")
class CavitySealSpecification(CavityPartSpecification):
    id: o6.String
    identification: list[o6.String]
    specialPartType: list[o6.String]
    describedPart: list[PartVersion]


@o6.enumtype(nodeId="ns=wire_harness_vec;i=3500", browseName="ConductorType")
class ConductorType(ns0.datatypes.Enumeration):
    RIGID = o6.enumfield(0, name="Rigid")
    STRANDED = o6.enumfield(1, name="Stranded")
    FOIL = o6.enumfield(2, name="Foil")
    BRAIDED = o6.enumfield(3, name="Braided")


@o6.datatype(nodeId="ns=wire_harness_vec;i=3705", browseName="Role", isAbstract=True)
class Role(ExtendableElement):
    id: o6.String
    identification: list[o6.String] = o6.field(arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3703", browseName="OccurrenceOrUsage", isAbstract=True)
class OccurrenceOrUsage(ConfigurableElement):
    id: o6.String
    identification: o6.String
    role: list[Role] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3757", browseName="CavityPartRole", isAbstract=True)
class CavityPartRole(Role):
    id: o6.String
    identification: list[o6.String]


@o6.datatype(nodeId="ns=wire_harness_vec;i=3942", browseName="PartOccurrence", defaultEncodingId="ns=wire_harness_vec;i=5011")
class PartOccurrence(OccurrenceOrUsage):
    id: o6.String
    identification: o6.String
    role: list[Role]
    part: list[PartVersion] = o6.field(arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3941", browseName="CompositionSpecification", defaultEncodingId="ns=wire_harness_vec;i=5044")
class CompositionSpecification(Specification):
    id: o6.String
    identification: list[o6.String]
    component: list[PartOccurrence] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=4026", browseName="Material", defaultEncodingId="ns=wire_harness_vec;i=5224")
class Material(ns0.datatypes.Structure):
    key: o6.String
    referenceSystem: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=4091", browseName="Tolerance", defaultEncodingId="ns=wire_harness_vec;i=5080")
class Tolerance(ExtendableElement):
    id: o6.String
    lowerBoundary: o6.Double
    upperBoundary: o6.Double


@o6.datatype(nodeId="ns=wire_harness_vec;i=4098", browseName="ValueWithUnit", isAbstract=True)
class ValueWithUnit(ns0.datatypes.Structure):
    unitComponent: ns0.datatypes.EUInformation


@o6.datatype(nodeId="ns=wire_harness_vec;i=4027", browseName="NumericalValue", defaultEncodingId="ns=wire_harness_vec;i=5230")
class NumericalValue(ValueWithUnit):
    unitComponent: ns0.datatypes.EUInformation
    valueComponent: o6.Double
    tolerance: list[Tolerance] = o6.field(arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3300", browseName="ConductorSpecification", isAbstract=True)
class ConductorSpecification(Specification):
    id: o6.String
    identification: list[o6.String]
    crossSectionArea: list[NumericalValue] = o6.field(arrayDimensions=[1])
    type: list[ConductorType] = o6.field(arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3302", browseName="CoreSpecification", defaultEncodingId="ns=wire_harness_vec;i=5047")
class CoreSpecification(ConductorSpecification):
    id: o6.String
    identification: list[o6.String]
    crossSectionArea: list[NumericalValue]
    type: list[ConductorType]
    outsideDiameter: list[NumericalValue] = o6.field(arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3308", browseName="InsulationSpecification", defaultEncodingId="ns=wire_harness_vec;i=5053")
class InsulationSpecification(Specification):
    id: o6.String
    identification: list[o6.String]
    baseColor: ARGB32ColorType
    firstIdentificationColor: list[ARGB32ColorType] = o6.field(arrayDimensions=[1])
    secondIdentificationColor: list[ARGB32ColorType] = o6.field(arrayDimensions=[1])
    thickness: list[NumericalValue] = o6.field(arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3377", browseName="WireElementSpecification", defaultEncodingId="ns=wire_harness_vec;i=5074")
class WireElementSpecification(Specification):
    id: o6.String
    identification: list[o6.String]
    outsideDiameter: list[NumericalValue] = o6.field(arrayDimensions=[1])
    conductorSpecification: list[ConductorSpecification] = o6.field(arrayDimensions=[1])
    insulationSpecification: list[InsulationSpecification] = o6.field(arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3376", browseName="WireElement", defaultEncodingId="ns=wire_harness_vec;i=5083")
class WireElement(ExtendableElement):
    id: o6.String
    identification: list[o6.String] = o6.field(arrayDimensions=[1])
    wireElementSpecification: WireElementSpecification
    subWireElement: list[WireElement] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3381", browseName="WireSpecification", defaultEncodingId="ns=wire_harness_vec;i=5071")
class WireSpecification(PartOrUsageRelatedSpecification):
    id: o6.String
    identification: list[o6.String]
    specialPartType: list[o6.String]
    describedPart: list[PartVersion]
    wireElement: WireElement


@o6.datatype(nodeId="ns=wire_harness_vec;i=3731", browseName="WireEnd", defaultEncodingId="ns=wire_harness_vec;i=5086")
class WireEnd(ExtendableElement):
    id: o6.String
    identification: list[o6.String] = o6.field(arrayDimensions=[1])
    positionOnWire: o6.Double
    strippingLength: list[NumericalValue] = o6.field(arrayDimensions=[1])
    insulationPullbackLength: list[NumericalValue] = o6.field(arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=4088", browseName="Size", defaultEncodingId="ns=wire_harness_vec;i=5227")
class Size(ns0.datatypes.Structure):
    width: NumericalValue
    height: NumericalValue


@o6.datatype(nodeId="ns=wire_harness_vec;i=3655", browseName="CrimpDetail", isAbstract=True)
class CrimpDetail(ExtendableElement):
    id: o6.String
    size: list[Size] = o6.field(arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3653", browseName="InsulationCrimpDetail", defaultEncodingId="ns=wire_harness_vec;i=5020")
class InsulationCrimpDetail(CrimpDetail):
    id: o6.String
    size: list[Size]
    pullOffForce: list[NumericalValue] = o6.field(arrayDimensions=[1])
    appliesTo: InsulationSpecification


@o6.datatype(nodeId="ns=wire_harness_vec;i=3654", browseName="CoreCrimpDetail", defaultEncodingId="ns=wire_harness_vec;i=5017")
class CoreCrimpDetail(CrimpDetail):
    id: o6.String
    size: list[Size]
    appliesTo: ConductorSpecification
    insulationCrimpDetails: list[InsulationCrimpDetail] = o6.field(arrayDimensions=[0])
    pullOffForce: list[NumericalValue] = o6.field(arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=4097", browseName="ValueRange", defaultEncodingId="ns=wire_harness_vec;i=5233")
class ValueRange(ValueWithUnit):
    unitComponent: ns0.datatypes.EUInformation
    minimum: o6.Double
    maximum: o6.Double


@o6.datatype(nodeId="ns=wire_harness_vec;i=3380", browseName="WireReceptionSpecification", defaultEncodingId="ns=wire_harness_vec;i=5077")
class WireReceptionSpecification(Specification):
    id: o6.String
    identification: list[o6.String]
    insulationDisplacementLength: NumericalValue
    conductorCrimpLength: list[NumericalValue] = o6.field(arrayDimensions=[1])
    crimpConnectionLength: NumericalValue
    insulationCrimpLength: list[NumericalValue] = o6.field(arrayDimensions=[1])
    wireTipProtrusion: list[ValueRange] = o6.field(arrayDimensions=[1])
    coreCrimpDetails: list[CoreCrimpDetail] = o6.field(arrayDimensions=[0])
    crimpBarrelType: CrimpBarrelType


@o6.datatype(nodeId="ns=wire_harness_vec;i=3379", browseName="WireReception", defaultEncodingId="ns=wire_harness_vec;i=5095")
class WireReception(ExtendableElement):
    id: o6.String
    identification: list[o6.String] = o6.field(arrayDimensions=[1])
    rotation: list[NumericalValue] = o6.field(arrayDimensions=[1])
    wireReceptionSpecification: WireReceptionSpecification


@o6.datatype(nodeId="ns=wire_harness_vec;i=3374", browseName="TerminalSpecification", defaultEncodingId="ns=wire_harness_vec;i=5065")
class TerminalSpecification(PartOrUsageRelatedSpecification):
    id: o6.String
    identification: list[o6.String]
    specialPartType: list[o6.String]
    describedPart: list[PartVersion]
    connectionALength: list[NumericalValue] = o6.field(arrayDimensions=[1])
    overallLength: NumericalValue
    wireReception: list[WireReception] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3361", browseName="PluggableTerminalSpecification", defaultEncodingId="ns=wire_harness_vec;i=5068")
class PluggableTerminalSpecification(TerminalSpecification):
    id: o6.String
    identification: list[o6.String]
    specialPartType: list[o6.String]
    describedPart: list[PartVersion]
    connectionALength: list[NumericalValue]
    overallLength: NumericalValue
    wireReception: list[WireReception]


@o6.datatype(nodeId="ns=wire_harness_vec;i=4126", browseName="BoundingBox", defaultEncodingId="ns=wire_harness_vec;i=5005")
class BoundingBox(ExtendableElement):
    id: o6.String
    x: NumericalValue
    y: NumericalValue
    z: NumericalValue


@o6.datatype(nodeId="ns=wire_harness_vec;i=3306", browseName="GeneralTechnicalPartSpecification", defaultEncodingId="ns=wire_harness_vec;i=5062")
class GeneralTechnicalPartSpecification(PartOrUsageRelatedSpecification):
    id: o6.String
    identification: list[o6.String]
    specialPartType: list[o6.String]
    describedPart: list[PartVersion]
    colorInformation: list[ARGB32ColorType] = o6.field(arrayDimensions=[1])
    boundingBox: list[BoundingBox] = o6.field(arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=6005", browseName="ContactPointIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5125")
class ContactPointIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6006", browseName="ContactingSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5122")
class ContactingSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6007", browseName="WireMountingIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5206")
class WireMountingIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6008", browseName="WireMountingDetailIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5203")
class WireMountingDetailIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6010", browseName="ConfigurableElementIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5119")
class ConfigurableElementIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6011", browseName="DocumentVersionIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5137")
class DocumentVersionIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6012", browseName="ExtendableElementIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5140")
class ExtendableElementIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6013", browseName="ItemVersionIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5152")
class ItemVersionIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6158", browseName="PartOrUsageRelatedSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5161")
class PartOrUsageRelatedSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6159", browseName="PartVersionIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5164")
class PartVersionIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6205", browseName="RoutableElementIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5179")
class RoutableElementIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6207", browseName="SpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5182")
class SpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6277", browseName="ResourceVersionIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5173")
class ResourceVersionIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6296", browseName="CavitySealSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5110")
class CavitySealSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=3710", browseName="CavitySealRole", defaultEncodingId="ns=wire_harness_vec;i=5032")
class CavitySealRole(CavityPartRole):
    id: o6.String
    identification: list[o6.String]
    cavitySealSpecification: CavitySealSpecificationIdDataType


@o6.datatype(nodeId="ns=wire_harness_vec;i=6300", browseName="ConductorSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5116")
class ConductorSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6302", browseName="CoreSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5131")
class CoreSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6306", browseName="GeneralTechnicalPartSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5143")
class GeneralTechnicalPartSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6308", browseName="InsulationSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5149")
class InsulationSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6361", browseName="PluggableTerminalSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5170")
class PluggableTerminalSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6374", browseName="TerminalSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5188")
class TerminalSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6376", browseName="WireElementIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5191")
class WireElementIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=3730", browseName="WireElementReference", defaultEncodingId="ns=wire_harness_vec;i=5014")
class WireElementReference(RoutableElement):
    id: o6.String
    identification: list[o6.String] = o6.field(arrayDimensions=[1])
    referencedWireElement: WireElementIdDataType
    wireEnd: list[WireEnd] = o6.field(arrayDimensions=[0])
    wireLength: list[NumericalValue] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=6377", browseName="WireElementSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5197")
class WireElementSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6379", browseName="WireReceptionIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5209")
class WireReceptionIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=3736", browseName="WireReceptionReference", defaultEncodingId="ns=wire_harness_vec;i=5098")
class WireReceptionReference(ExtendableElement):
    id: o6.String
    identification: list[o6.String] = o6.field(arrayDimensions=[1])
    wireReception: WireReceptionIdDataType


@o6.datatype(nodeId="ns=wire_harness_vec;i=3729", browseName="TerminalRole", defaultEncodingId="ns=wire_harness_vec;i=5035")
class TerminalRole(Role):
    id: o6.String
    identification: list[o6.String]
    terminalSpecification: TerminalSpecificationIdDataType
    wireReceptionReference: list[WireReceptionReference] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3719", browseName="PluggableTerminalRole", defaultEncodingId="ns=wire_harness_vec;i=5038")
class PluggableTerminalRole(TerminalRole):
    id: o6.String
    identification: list[o6.String]
    terminalSpecification: TerminalSpecificationIdDataType
    wireReceptionReference: list[WireReceptionReference]


@o6.datatype(nodeId="ns=wire_harness_vec;i=6380", browseName="WireReceptionSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5215")
class WireReceptionSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6381", browseName="WireSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5221")
class WireSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=3735", browseName="WireRole", defaultEncodingId="ns=wire_harness_vec;i=5041")
class WireRole(Role):
    id: o6.String
    identification: list[o6.String]
    wireSpecification: WireSpecificationIdDataType
    wireElementReference: list[WireElementReference] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=6433", browseName="CavityPartSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5104")
class CavityPartSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6653", browseName="InsulationCrimpDetailIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5146")
class InsulationCrimpDetailIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6654", browseName="CoreCrimpDetailIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5128")
class CoreCrimpDetailIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6655", browseName="CrimpDetailIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5134")
class CrimpDetailIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6703", browseName="OccurrenceOrUsageIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5155")
class OccurrenceOrUsageIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6705", browseName="RoleIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5176")
class RoleIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6710", browseName="CavitySealRoleIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5107")
class CavitySealRoleIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6719", browseName="PluggableTerminalRoleIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5167")
class PluggableTerminalRoleIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6729", browseName="TerminalRoleIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5185")
class TerminalRoleIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6730", browseName="WireElementReferenceIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5194")
class WireElementReferenceIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6731", browseName="WireEndIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5200")
class WireEndIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6735", browseName="WireRoleIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5218")
class WireRoleIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6736", browseName="WireReceptionReferenceIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5212")
class WireReceptionReferenceIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=3008", browseName="WireMountingDetail", defaultEncodingId="ns=wire_harness_vec;i=5092")
class WireMountingDetail(ExtendableElement):
    id: o6.String
    coreCrimpSize: list[Size] = o6.field(arrayDimensions=[1])
    insulationCrimpSize: list[Size] = o6.field(arrayDimensions=[1])
    wireTipProtrusion: list[ValueRange] = o6.field(arrayDimensions=[1])
    contactedWireReception: WireReceptionReferenceIdDataType
    referencedWireEnd: list[WireEndIdDataType] = o6.field(arrayDimensions=[0])
    absoluteSealPosition: NumericalValue
    corePullOffForce: list[NumericalValue] = o6.field(arrayDimensions=[1])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3007", browseName="WireMounting", defaultEncodingId="ns=wire_harness_vec;i=5089")
class WireMounting(ExtendableElement):
    id: o6.String
    mountedCavitySeal: list[CavitySealRoleIdDataType] = o6.field(arrayDimensions=[1])
    referencedWireEnd: list[WireEndIdDataType] = o6.field(arrayDimensions=[0])
    wireMountingDetail: list[WireMountingDetail] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3005", browseName="ContactPoint", defaultEncodingId="ns=wire_harness_vec;i=5008")
class ContactPoint(ConfigurableElement):
    id: o6.String
    identification: list[o6.String] = o6.field(arrayDimensions=[1])
    mountedTerminal: list[TerminalRoleIdDataType] = o6.field(arrayDimensions=[1])
    wireMounting: list[WireMounting] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=3006", browseName="ContactingSpecification", defaultEncodingId="ns=wire_harness_vec;i=5050")
class ContactingSpecification(Specification):
    id: o6.String
    identification: list[o6.String]
    contactPoint: list[ContactPoint] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=wire_harness_vec;i=6757", browseName="CavityPartRoleIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5101")
class CavityPartRoleIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6941", browseName="CompositionSpecificationIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5113")
class CompositionSpecificationIdDataType(IdBaseDataType):
    id: o6.String


@o6.datatype(nodeId="ns=wire_harness_vec;i=6942", browseName="PartOccurrenceIdDataType", defaultEncodingId="ns=wire_harness_vec;i=5158")
class PartOccurrenceIdDataType(IdBaseDataType):
    id: o6.String


del Any, TYPE_CHECKING, uuid, o6, ns0
