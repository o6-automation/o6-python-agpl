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

"""Generated OPC UA i4aas namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as i4aas_reftypes
from . import datatypes as i4aas_datypes
from . import objtypes as i4aas_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=i4aas;i=5038", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=i4aas;i=5039", browseName="Default XML")
o6.hasEncoding(i4aas_datypes.AASKeyDataType, o6.ns["ns=i4aas;i=5039"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=i4aas;i=5040", browseName="Default JSON")
o6.hasEncoding(i4aas_datypes.AASKeyDataType, o6.ns["ns=i4aas;i=5040"])
adminMinusShellDotIoSlashAasSlash2Slash0SlashAdministrativeInformationSlashRevision = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5045", browseName="ns=i4aas;Admin-shell.io/aas/2/0/AdministrativeInformation/revision", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6084"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashAdministrativeInformationSlashRevision)
adminMinusShellDotIoSlashAasSlash2Slash0SlashAdministrativeInformation = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5047", browseName="ns=i4aas;Admin-shell.io/aas/2/0/AdministrativeInformation", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASAdministrativeInformationType, "i=17597", "ns=i4aas;i=5047")
adminMinusShellDotIoSlashAasSlash2Slash0SlashAdministrativeInformationSlashVersion = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5051", browseName="ns=i4aas;Admin-shell.io/aas/2/0/AdministrativeInformation/version", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6083"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashAdministrativeInformationSlashVersion)
adminMinusShellDotIoSlashAasSlash2Slash0SlashAsset = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5052", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Asset", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASAssetType, "i=17597", "ns=i4aas;i=5052")
adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetSlashAssetIdentificationModel = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5053", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Asset/assetIdentificationModel", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetSlashAssetKind = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5054", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Asset/assetKind", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6006"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetSlashAssetKind)
adminMinusShellDotIoSlashAasSlash2Slash0SlashAnnotatedRelationshipElement = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5055", browseName="ns=i4aas;Admin-shell.io/aas/2/0/AnnotatedRelationshipElement", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASAnnotatedRelationshipElementType, "i=17597", "ns=i4aas;i=5055")
adminMinusShellDotIoSlashAasSlash2Slash0SlashAnnotatedRelationshipElementSlashAnnotations = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5056", browseName="ns=i4aas;Admin-shell.io/aas/2/0/AnnotatedRelationshipElement/annotations", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetSlashBillOfMaterial = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5057", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Asset/billOfMaterial", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetSlashDataSpecifications = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5058", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Asset/dataSpecifications", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetAdministrationShell = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5059", browseName="ns=i4aas;Admin-shell.io/aas/2/0/AssetAdministrationShell", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASAssetAdministrationShellType, "i=17597", "ns=i4aas;i=5059")
adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetAdministrationShellSlashAsset = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5060", browseName="ns=i4aas;Admin-shell.io/aas/2/0/AssetAdministrationShell/asset", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetAdministrationShellSlashConceptDictionaries = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5061", browseName="ns=i4aas;Admin-shell.io/aas/2/0/AssetAdministrationShell/conceptDictionaries", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=5005"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetAdministrationShellSlashConceptDictionaries)
adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetAdministrationShellSlashDataSpecifications = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5062", browseName="ns=i4aas;Admin-shell.io/aas/2/0/AssetAdministrationShell/dataSpecifications", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetAdministrationShellSlashDerivedFrom = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5063", browseName="ns=i4aas;Admin-shell.io/aas/2/0/AssetAdministrationShell/derivedFrom", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetAdministrationShellSlashSubmodels = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5064", browseName="ns=i4aas;Admin-shell.io/aas/2/0/AssetAdministrationShell/submodels", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetAdministrationShellSlashViews = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5065", browseName="ns=i4aas;Admin-shell.io/aas/2/0/AssetAdministrationShell/views", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=5006"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetAdministrationShellSlashViews)
adminMinusShellDotIoSlashAasSlash2Slash0SlashBasicEvent = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5066", browseName="ns=i4aas;Admin-shell.io/aas/2/0/BasicEvent", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASEventType, "i=17597", "ns=i4aas;i=5066")
adminMinusShellDotIoSlashAasSlash2Slash0SlashBlob = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5067", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Blob", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASBlobType, "i=17597", "ns=i4aas;i=5067")
adminMinusShellDotIoSlashAasSlash2Slash0SlashBlobSlashMimeType = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5068", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Blob/mimeType", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashBlobSlashValue = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5069", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Blob/value", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashConceptDescription = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5070", browseName="ns=i4aas;Admin-shell.io/aas/2/0/ConceptDescription", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASIrdiConceptDescriptionType, "i=17597", "ns=i4aas;i=5070")
o6.reference(i4aas_objtypes.AASIriConceptDescriptionType, "i=17597", "ns=i4aas;i=5070")
o6.reference(i4aas_objtypes.AASCustomConceptDescriptionType, "i=17597", "ns=i4aas;i=5070")
adminMinusShellDotIoSlashAasSlash2Slash0SlashConceptDescriptionSlashDataSpecifications = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5071", browseName="ns=i4aas;Admin-shell.io/aas/2/0/ConceptDescription/dataSpecifications", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashConceptDescriptionSlashIsCaseOf = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5072", browseName="ns=i4aas;Admin-shell.io/aas/2/0/ConceptDescription/IsCaseOf", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashDataSpecification = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5073", browseName="ns=i4aas;Admin-shell.io/aas/2/0/DataSpecification", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASDataSpecificationType, "i=17597", "ns=i4aas;i=5073")
adminMinusShellDotIoSlashAasSlash2Slash0SlashEntity = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5074", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Entity", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASEntityType, "i=17597", "ns=i4aas;i=5074")
adminMinusShellDotIoSlashAasSlash2Slash0SlashEntitySlashAsset = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5075", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Entity/asset", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashEntitySlashEntityType = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5076", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Entity/entityType", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6056"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashEntitySlashEntityType)
adminMinusShellDotIoSlashAasSlash2Slash0SlashEntitySlashStatements = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5077", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Entity/statements", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashFile = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5078", browseName="ns=i4aas;Admin-shell.io/aas/2/0/File", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASFileType, "i=17597", "ns=i4aas;i=5078")
adminMinusShellDotIoSlashAasSlash2Slash0SlashFileSlashMimeType = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5079", browseName="ns=i4aas;Admin-shell.io/aas/2/0/File/mimeType", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6037"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashFileSlashMimeType)
adminMinusShellDotIoSlashAasSlash2Slash0SlashFileSlashValue = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5080", browseName="ns=i4aas;Admin-shell.io/aas/2/0/File/value", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashHasKindSlashKind = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5081", browseName="ns=i4aas;Admin-shell.io/aas/2/0/HasKind/kind", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6009"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashHasKindSlashKind)
adminMinusShellDotIoSlashAasSlash2Slash0SlashIdentifiable = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5082", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Identifiable", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.IAASIdentifiableType, "i=17597", "ns=i4aas;i=5082")
adminMinusShellDotIoSlashAasSlash2Slash0SlashIdentifiableSlashAdministration = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5083", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Identifiable/administration", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=5035"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashIdentifiableSlashAdministration)
adminMinusShellDotIoSlashAasSlash2Slash0SlashIdentifiableSlashIdentification = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5084", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Identifiable/identification", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashIdentifier = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5085", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Identifier", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASIdentifierType, "i=17597", "ns=i4aas;i=5085")
adminMinusShellDotIoSlashAasSlash2Slash0SlashIdentifierSlashId = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5086", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Identifier/id", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6086"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashIdentifierSlashId)
adminMinusShellDotIoSlashAasSlash2Slash0SlashIdentifierSlashIdType = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5087", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Identifier/idType", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6085"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashIdentifierSlashIdType)
adminMinusShellDotIoSlashAasSlash2Slash0SlashIdentifierTypeSlashCustom = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5088", browseName="ns=i4aas;Admin-shell.io/aas/2/0/IdentifierType/Custom", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashIdentifierTypeSlashIRDI = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5089", browseName="ns=i4aas;Admin-shell.io/aas/2/0/IdentifierType/IRDI", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashIdentifierTypeSlashIRI = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5090", browseName="ns=i4aas;Admin-shell.io/aas/2/0/IdentifierType/IRI", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashMultiLanguageProperty = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5091", browseName="ns=i4aas;Admin-shell.io/aas/2/0/MultiLanguageProperty", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASMultiLanguagePropertyType, "i=17597", "ns=i4aas;i=5091")
adminMinusShellDotIoSlashAasSlash2Slash0SlashMultiLanguagePropertySlashValue = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5092", browseName="ns=i4aas;Admin-shell.io/aas/2/0/MultiLanguageProperty/value", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6019"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashMultiLanguagePropertySlashValue)
adminMinusShellDotIoSlashAasSlash2Slash0SlashMultiLanguagePropertySlashValueId = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5093", browseName="ns=i4aas;Admin-shell.io/aas/2/0/MultiLanguageProperty/valueId", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashOperation = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5094", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Operation", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASOperationType, "i=17597", "ns=i4aas;i=5094")
adminMinusShellDotIoSlashAasSlash2Slash0SlashProperty = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5095", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Property", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASPropertyType, "i=17597", "ns=i4aas;i=5095")
o6.reference(i4aas_objtypes.AASCapabilityType, "i=17597", "ns=i4aas;i=5095")
adminMinusShellDotIoSlashAasSlash2Slash0SlashPropertySlashValue = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5096", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Property/value", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6020"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashPropertySlashValue)
adminMinusShellDotIoSlashAasSlash2Slash0SlashPropertySlashValueId = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5097", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Property/valueId", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashPropertySlashValueType = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5098", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Property/valueType", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6021"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashPropertySlashValueType)
adminMinusShellDotIoSlashAasSlash2Slash0SlashQualifier = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5099", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Qualifier", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASQualifierType, "i=17597", "ns=i4aas;i=5099")
adminMinusShellDotIoSlashAasSlash2Slash0SlashQualifierSlashType = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5100", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Qualifier/type", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6010"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashQualifierSlashType)
langleIRDI_or_IRI_or_Custom_concept_description_entryRangle = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5101",
    browseName="<IRDI_or_IRI_or_Custom_concept_description_entry>",
    displayName="<IRDI or IRI or Custom concept description entry>",
    parent="i=17594",
    referenceType=ns0.reftypes.Organizes,
)
o6.reference(i4aas_objtypes.AASSubmodelElementType, "i=17597", "ns=i4aas;i=5101")
adminMinusShellDotIoSlashAasSlash2Slash0SlashQualifierSlashValue = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5102", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Qualifier/value", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6078"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashQualifierSlashValue)
adminMinusShellDotIoSlashAasSlash2Slash0SlashHasDataSpecificationSlashDataSpecification = ns0.objtypes.UriDictionaryEntryType(
    nodeId="ns=i4aas;i=5103", browseName="ns=i4aas;Admin-shell.io/aas/2/0/hasDataSpecification/dataSpecification", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASAssetType, "i=17597", "ns=i4aas;i=5103")
o6.reference(i4aas_objtypes.AASSubmodelType, "i=17597", "ns=i4aas;i=5103")
adminMinusShellDotIoSlashAasSlash2Slash0SlashQualifierSlashValueType = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5104", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Qualifier/valueType", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6015"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashQualifierSlashValueType)
adminMinusShellDotIoSlashAasSlash2Slash0SlashRange = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5105", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Range", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASRangeType, "i=17597", "ns=i4aas;i=5105")
adminMinusShellDotIoSlashAasSlash2Slash0SlashRangeSlashMax = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5106", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Range/max", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6059"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashRangeSlashMax)
adminMinusShellDotIoSlashAasSlash2Slash0SlashRangeSlashMin = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5107", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Range/min", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6058"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashRangeSlashMin)
adminMinusShellDotIoSlashAasSlash2Slash0SlashRangeSlashValueType = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5108", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Range/valueType", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6057"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashRangeSlashValueType)
adminMinusShellDotIoSlashAasSlash2Slash0SlashReferable = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5109", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Referable", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.IAASReferableType, "i=17597", "ns=i4aas;i=5109")
adminMinusShellDotIoSlashAasSlash2Slash0SlashReferableSlashCategory = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5110", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Referable/category", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6082"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferableSlashCategory)
adminMinusShellDotIoSlashAasSlash2Slash0SlashReference = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5111", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Reference", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASReferenceType, "i=17597", "ns=i4aas;i=5111")
adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5112", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Reference/keys", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6001"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceElement = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5113", browseName="ns=i4aas;Admin-shell.io/aas/2/0/ReferenceElement", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASReferenceElementType, "i=17597", "ns=i4aas;i=5113")
adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceElementSlashValue = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5114", browseName="ns=i4aas;Admin-shell.io/aas/2/0/ReferenceElement/value", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashRelationshipElement = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5115", browseName="ns=i4aas;Admin-shell.io/aas/2/0/RelationshipElement", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASRelationshipElementType, "i=17597", "ns=i4aas;i=5115")
adminMinusShellDotIoSlashAasSlash2Slash0SlashRelationshipElementSlashFirst = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5116", browseName="ns=i4aas;Admin-shell.io/aas/2/0/RelationshipElement/first", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashRelationshipElementSlashSecond = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5117", browseName="ns=i4aas;Admin-shell.io/aas/2/0/RelationshipElement/second", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodel = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5118", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Submodel", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASSubmodelType, "i=17597", "ns=i4aas;i=5118")
adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelSlashQualifiers = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5119", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Submodel/qualifiers", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelSlashSubmodelElements = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5120", browseName="ns=i4aas;Admin-shell.io/aas/2/0/Submodel/submodelElements", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElement = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5121", browseName="ns=i4aas;Admin-shell.io/aas/2/0/SubmodelElement", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASSubmodelElementType, "i=17597", "ns=i4aas;i=5121")
adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementSlashDataSpecifications = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5122", browseName="ns=i4aas;Admin-shell.io/aas/2/0/SubmodelElement/dataSpecifications", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementSlashIdShort = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5123", browseName="ns=i4aas;Admin-shell.io/aas/2/0/SubmodelElement/idShort", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementSlashKind = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5124", browseName="ns=i4aas;Admin-shell.io/aas/2/0/SubmodelElement/kind", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6013"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementSlashKind)
adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementSlashQualifiers = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5125", browseName="ns=i4aas;Admin-shell.io/aas/2/0/SubmodelElement/qualifiers", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementCollection = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5126", browseName="ns=i4aas;Admin-shell.io/aas/2/0/SubmodelElementCollection", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASSubmodelElementCollectionType, "i=17597", "ns=i4aas;i=5126")
o6.reference(i4aas_objtypes.AASOrderedSubmodelElementCollectionType, "i=17597", "ns=i4aas;i=5126")
adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementCollectionSlashAllowDuplicates = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5127", browseName="ns=i4aas;Admin-shell.io/aas/2/0/SubmodelElementCollection/allowDuplicates", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6017"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementCollectionSlashAllowDuplicates)
adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementCollectionSlashValues = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5128", browseName="ns=i4aas;Admin-shell.io/aas/2/0/SubmodelElementCollection/values", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashView = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5129", browseName="ns=i4aas;Admin-shell.io/aas/2/0/View", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASViewType, "i=17597", "ns=i4aas;i=5129")
adminMinusShellDotIoSlashAasSlash2Slash0SlashViewSlashContainedElements = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5130", browseName="ns=i4aas;Admin-shell.io/aas/2/0/View/containedElements", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashAasSlash2Slash0SlashViewSlashDataSpecifications = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5131", browseName="ns=i4aas;Admin-shell.io/aas/2/0/View/dataSpecifications", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashDataSpecificationSlashAdministration = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5132", browseName="ns=i4aas;Admin-shell.io/DataSpecification/administration", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=5027"], "i=17597", adminMinusShellDotIoSlashDataSpecificationSlashAdministration)
adminMinusShellDotIoSlashDataSpecificationSlashCategory = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5133", browseName="ns=i4aas;Admin-shell.io/DataSpecification/category", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(o6.ns["ns=i4aas;i=6065"], "i=17597", adminMinusShellDotIoSlashDataSpecificationSlashCategory)
adminMinusShellDotIoSlashDataSpecificationSlashIdentification = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5134", browseName="ns=i4aas;Admin-shell.io/DataSpecification/identification", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashDataSpecificationSlashIdShort = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5135", browseName="ns=i4aas;Admin-shell.io/DataSpecification/idShort", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0 = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5136", browseName="ns=i4aas;Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
o6.reference(i4aas_objtypes.AASDataSpecificationIEC61360Type, "i=17597", "ns=i4aas;i=5136")
adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashDataType = (
    i4aas_objtypes.AASIriConceptDescriptionType(
        nodeId="ns=i4aas;i=5137",
        browseName="ns=i4aas;Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/dataType",
        parent="i=17594",
        referenceType=ns0.reftypes.Organizes,
    )
)
o6.reference(
    o6.ns["ns=i4aas;i=6072"],
    "i=17597",
    adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashDataType,
)
adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashDefinition = (
    i4aas_objtypes.AASIriConceptDescriptionType(
        nodeId="ns=i4aas;i=5138",
        browseName="ns=i4aas;Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/definition",
        parent="i=17594",
        referenceType=ns0.reftypes.Organizes,
    )
)
o6.reference(
    o6.ns["ns=i4aas;i=6073"],
    "i=17597",
    adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashDefinition,
)
adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashLevelType = (
    i4aas_objtypes.AASIriConceptDescriptionType(
        nodeId="ns=i4aas;i=5139",
        browseName="ns=i4aas;Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/levelType",
        parent="i=17594",
        referenceType=ns0.reftypes.Organizes,
    )
)
o6.reference(
    o6.ns["ns=i4aas;i=6075"],
    "i=17597",
    adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashLevelType,
)
adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashPreferredName = (
    i4aas_objtypes.AASIriConceptDescriptionType(
        nodeId="ns=i4aas;i=5140",
        browseName="ns=i4aas;Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/preferredName",
        parent="i=17594",
        referenceType=ns0.reftypes.Organizes,
    )
)
o6.reference(
    o6.ns["ns=i4aas;i=6074"],
    "i=17597",
    adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashPreferredName,
)
adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashShortName = (
    i4aas_objtypes.AASIriConceptDescriptionType(
        nodeId="ns=i4aas;i=5141",
        browseName="ns=i4aas;Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/shortName",
        parent="i=17594",
        referenceType=ns0.reftypes.Organizes,
    )
)
o6.reference(
    o6.ns["ns=i4aas;i=6066"],
    "i=17597",
    adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashShortName,
)
adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashSourceOfDefinition = (
    i4aas_objtypes.AASIriConceptDescriptionType(
        nodeId="ns=i4aas;i=5142",
        browseName="ns=i4aas;Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/sourceOfDefinition",
        parent="i=17594",
        referenceType=ns0.reftypes.Organizes,
    )
)
o6.reference(
    o6.ns["ns=i4aas;i=6067"],
    "i=17597",
    adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashSourceOfDefinition,
)
adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashSymbol = (
    i4aas_objtypes.AASIriConceptDescriptionType(
        nodeId="ns=i4aas;i=5143",
        browseName="ns=i4aas;Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/symbol",
        parent="i=17594",
        referenceType=ns0.reftypes.Organizes,
    )
)
o6.reference(
    o6.ns["ns=i4aas;i=6068"], "i=17597", adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashSymbol
)
adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashUnit = (
    i4aas_objtypes.AASIriConceptDescriptionType(
        nodeId="ns=i4aas;i=5144",
        browseName="ns=i4aas;Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/unit",
        parent="i=17594",
        referenceType=ns0.reftypes.Organizes,
    )
)
o6.reference(
    o6.ns["ns=i4aas;i=6069"], "i=17597", adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashUnit
)
adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashUnitId = (
    i4aas_objtypes.AASIriConceptDescriptionType(
        nodeId="ns=i4aas;i=5145",
        browseName="ns=i4aas;Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/unitId",
        parent="i=17594",
        referenceType=ns0.reftypes.Organizes,
    )
)
adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashValue = (
    i4aas_objtypes.AASIriConceptDescriptionType(
        nodeId="ns=i4aas;i=5146",
        browseName="ns=i4aas;Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/value",
        parent="i=17594",
        referenceType=ns0.reftypes.Organizes,
    )
)
o6.reference(
    o6.ns["ns=i4aas;i=6071"], "i=17597", adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashValue
)
adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashValueFormat = (
    i4aas_objtypes.AASIriConceptDescriptionType(
        nodeId="ns=i4aas;i=5147",
        browseName="ns=i4aas;Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/valueFormat",
        parent="i=17594",
        referenceType=ns0.reftypes.Organizes,
    )
)
o6.reference(
    o6.ns["ns=i4aas;i=6070"],
    "i=17597",
    adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashValueFormat,
)
adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashValueId = (
    i4aas_objtypes.AASIriConceptDescriptionType(
        nodeId="ns=i4aas;i=5148",
        browseName="ns=i4aas;Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0//DataSpecificationIEC61360/valueId",
        parent="i=17594",
        referenceType=ns0.reftypes.Organizes,
    )
)
adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashValueList = i4aas_objtypes.AASIriConceptDescriptionType(
    nodeId="ns=i4aas;i=5149",
    browseName="ns=i4aas;Admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/2/0/valueList",
    parent="i=17594",
    referenceType=ns0.reftypes.Organizes,
)
o6.reference(o6.ns["ns=i4aas;i=5029"], "i=17597", adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashValueList)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6002",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6002"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(
    nodeId="ns=i4aas;i=5004", browseName="ns=i4aas;<SubmodelReference>", modellingRule="OptionalPlaceholder", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6002"])]
)
o6.reference(i4aas_objtypes.AASAssetAdministrationShellType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5004"])
o6.reference(o6.ns["ns=i4aas;i=5004"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetAdministrationShellSlashSubmodels)
o6.reference(o6.ns["ns=i4aas;i=5004"], "ns=i4aas;i=4003", o6.ns["ns=i4aas;i=6002"])
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6003",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6003"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(
    nodeId="ns=i4aas;i=5001", browseName="ns=i4aas;<DataSpecification>", modellingRule="OptionalPlaceholder", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6003"])]
)
o6.reference(i4aas_objtypes.AASAssetAdministrationShellType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5001"])
o6.reference(o6.ns["ns=i4aas;i=5001"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashHasDataSpecificationSlashDataSpecification)
o6.reference(o6.ns["ns=i4aas;i=5001"], "ns=i4aas;i=4003", o6.ns["ns=i4aas;i=6003"])
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6004",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6004"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(nodeId="ns=i4aas;i=5007", browseName="ns=i4aas;DerivedFrom", modellingRule="Optional", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6004"])])
o6.reference(i4aas_objtypes.AASAssetAdministrationShellType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5007"])
o6.reference(o6.ns["ns=i4aas;i=5007"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetAdministrationShellSlashDerivedFrom)
o6.reference(o6.ns["ns=i4aas;i=5007"], "ns=i4aas;i=4003", o6.ns["ns=i4aas;i=6004"])
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6005",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6005"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(
    nodeId="ns=i4aas;i=5008", browseName="ns=i4aas;<DataSpecification>", modellingRule="OptionalPlaceholder", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6005"])]
)
o6.reference(i4aas_objtypes.AASAssetType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5008"])
o6.reference(o6.ns["ns=i4aas;i=5008"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetSlashDataSpecifications)
o6.reference(o6.ns["ns=i4aas;i=5008"], "ns=i4aas;i=4003", o6.ns["ns=i4aas;i=6005"])
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6007",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6007"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(
    nodeId="ns=i4aas;i=5009", browseName="ns=i4aas;<DataSpecification>", modellingRule="OptionalPlaceholder", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6007"])]
)
o6.reference(i4aas_objtypes.AASSubmodelType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5009"])
o6.reference(o6.ns["ns=i4aas;i=5009"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetSlashDataSpecifications)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6008",
    browseName="ns=i4aas;AssetKind",
    dataType=i4aas_datypes.AASAssetKindDataType,
    value=i4aas_datypes.AASAssetKindDataType.TYPE,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6008"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetSlashAssetKind)
i4aas_objtypes.AASAssetType(nodeId="ns=i4aas;i=5002", browseName="ns=i4aas;Asset", modellingRule="Mandatory", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6008"])])
o6.reference(i4aas_objtypes.AASAssetAdministrationShellType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5002"])
o6.reference(o6.ns["ns=i4aas;i=5002"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashAsset)
o6.reference(o6.ns["ns=i4aas;i=5002"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetAdministrationShellSlashAsset)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6011",
    browseName="ns=i4aas;ModelingKind",
    dataType=i4aas_datypes.AASModelingKindDataType,
    value=i4aas_datypes.AASModelingKindDataType.TEMPLATE,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6011"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashHasKindSlashKind)
o6.reference(o6.ns["ns=i4aas;i=6011"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashProperty)
i4aas_objtypes.AASSubmodelType(
    nodeId="ns=i4aas;i=5003", browseName="ns=i4aas;<Submodel>", modellingRule="OptionalPlaceholder", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6011"])]
)
o6.reference(i4aas_objtypes.AASAssetAdministrationShellType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5003"])
o6.reference(o6.ns["ns=i4aas;i=5003"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetAdministrationShellSlashSubmodels)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6012",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6012"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(
    nodeId="ns=i4aas;i=5011", browseName="ns=i4aas;<DataSpecification>", modellingRule="OptionalPlaceholder", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6012"])]
)
o6.reference(i4aas_objtypes.AASSubmodelElementType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5011"])
o6.reference(o6.ns["ns=i4aas;i=5011"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashHasDataSpecificationSlashDataSpecification)
o6.reference(o6.ns["ns=i4aas;i=5011"], "ns=i4aas;i=4003", o6.ns["ns=i4aas;i=6012"])
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6014",
    browseName="ns=i4aas;ModelingKind",
    dataType=i4aas_datypes.AASModelingKindDataType,
    value=i4aas_datypes.AASModelingKindDataType.TEMPLATE,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6014"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementSlashKind)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6016",
    browseName="ns=i4aas;ModelingKind",
    dataType=i4aas_datypes.AASModelingKindDataType,
    value=i4aas_datypes.AASModelingKindDataType.TEMPLATE,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6016"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementSlashKind)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6018",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6018"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(nodeId="ns=i4aas;i=5013", browseName="ns=i4aas;ValueId", modellingRule="Optional", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6018"])])
o6.reference(i4aas_objtypes.AASMultiLanguagePropertyType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5013"])
o6.reference(o6.ns["ns=i4aas;i=5013"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashMultiLanguagePropertySlashValueId)
o6.reference(o6.ns["ns=i4aas;i=5013"], "ns=i4aas;i=4003", o6.ns["ns=i4aas;i=6018"])
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6022",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6022"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(nodeId="ns=i4aas;i=5014", browseName="ns=i4aas;ValueId", modellingRule="Optional", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6022"])])
o6.reference(i4aas_objtypes.AASPropertyType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5014"])
o6.reference(o6.ns["ns=i4aas;i=5014"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashPropertySlashValueId)
o6.reference(o6.ns["ns=i4aas;i=5014"], "ns=i4aas;i=4003", o6.ns["ns=i4aas;i=6022"])
i4aas_objtypes.AASReferenceType(
    nodeId="ns=i4aas;i=5024",
    browseName="ns=i4aas;<DataSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=i4aas;i=6036",
                browseName="ns=i4aas;Keys",
                dataType=i4aas_datypes.AASKeyDataType,
                valueRank=1,
                arrayDimensions=[1],
                value=[
                    i4aas_datypes.AASKeyDataType(
                        type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT
                    )
                ],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
)
o6.reference(i4aas_objtypes.AASIrdiConceptDescriptionType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5024"])
o6.reference(o6.ns["ns=i4aas;i=5024"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashHasDataSpecificationSlashDataSpecification)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6051",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6051"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(nodeId="ns=i4aas;i=5017", browseName="ns=i4aas;First", modellingRule="Mandatory", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6051"])])
o6.reference(i4aas_objtypes.AASRelationshipElementType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5017"])
o6.reference(o6.ns["ns=i4aas;i=5017"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashRelationshipElementSlashFirst)
o6.reference(o6.ns["ns=i4aas;i=5017"], "ns=i4aas;i=4003", o6.ns["ns=i4aas;i=6051"])
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6052",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6052"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(nodeId="ns=i4aas;i=5018", browseName="ns=i4aas;Second", modellingRule="Mandatory", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6052"])])
o6.reference(i4aas_objtypes.AASRelationshipElementType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5018"])
o6.reference(o6.ns["ns=i4aas;i=5018"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashRelationshipElementSlashSecond)
o6.reference(o6.ns["ns=i4aas;i=5018"], "ns=i4aas;i=4003", o6.ns["ns=i4aas;i=6052"])
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6053",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6053"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(nodeId="ns=i4aas;i=5020", browseName="ns=i4aas;Value", modellingRule="Mandatory", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6053"])])
o6.reference(i4aas_objtypes.AASReferenceElementType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5020"])
o6.reference(o6.ns["ns=i4aas;i=5020"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceElementSlashValue)
o6.reference(o6.ns["ns=i4aas;i=5020"], "ns=i4aas;i=4003", o6.ns["ns=i4aas;i=6053"])
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6054",
    browseName="ns=i4aas;ModelingKind",
    dataType=i4aas_datypes.AASModelingKindDataType,
    value=i4aas_datypes.AASModelingKindDataType.TEMPLATE,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6054"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementSlashKind)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6055",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6055"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(nodeId="ns=i4aas;i=5022", browseName="ns=i4aas;Asset", modellingRule="Optional", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6055"])])
o6.reference(i4aas_objtypes.AASEntityType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5022"])
o6.reference(o6.ns["ns=i4aas;i=5022"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashEntitySlashAsset)
o6.reference(o6.ns["ns=i4aas;i=5022"], "ns=i4aas;i=4003", o6.ns["ns=i4aas;i=6055"])
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6076",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6076"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(nodeId="ns=i4aas;i=5028", browseName="ns=i4aas;UnitId", modellingRule="Optional", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6076"])])
o6.reference(i4aas_objtypes.AASDataSpecificationIEC61360Type, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5028"])
o6.reference(
    o6.ns["ns=i4aas;i=5028"], "i=17597", adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashUnitId
)
o6.reference(o6.ns["ns=i4aas;i=5028"], "ns=i4aas;i=4003", o6.ns["ns=i4aas;i=6076"])
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6077",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6077"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(nodeId="ns=i4aas;i=5030", browseName="ns=i4aas;ValueId", modellingRule="Optional", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6077"])])
o6.reference(i4aas_objtypes.AASDataSpecificationIEC61360Type, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5030"])
o6.reference(
    o6.ns["ns=i4aas;i=5030"],
    "i=17597",
    adminMinusShellDotIoSlashDataSpecificationTemplatesSlashDataSpecificationIEC61360Slash2Slash0SlashSlashDataSpecificationIEC61360SlashValueId,
)
o6.reference(o6.ns["ns=i4aas;i=5030"], "ns=i4aas;i=4003", o6.ns["ns=i4aas;i=6077"])
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6079",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6079"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(nodeId="ns=i4aas;i=5033", browseName="ns=i4aas;ValueId", modellingRule="Optional", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6079"])])
o6.reference(i4aas_objtypes.AASQualifierType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5033"])
o6.reference(o6.ns["ns=i4aas;i=5033"], "ns=i4aas;i=4003", o6.ns["ns=i4aas;i=6079"])
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6080", browseName="ns=i4aas;Type", dataType=o6.String, value="\n      ", accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=i4aas;i=6080"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashQualifierSlashType)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6081", browseName="ns=i4aas;Type", dataType=o6.String, value="\n      ", accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=i4aas;i=6081"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashQualifierSlashType)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6087",
    browseName="ns=i4aas;IdType",
    dataType=i4aas_datypes.AASIdentifierTypeDataType,
    value=i4aas_datypes.AASIdentifierTypeDataType.IRDI,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6087"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashIdentifierSlashIdType)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6088", browseName="ns=i4aas;Id", dataType=o6.String, value="\n      ", accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=i4aas;i=6088"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashIdentifierSlashId)
i4aas_objtypes.AASIdentifierType(
    nodeId="ns=i4aas;i=5026",
    browseName="ns=i4aas;Identification",
    modellingRule="Mandatory",
    references=[o6.hasProperty(o6.ns["ns=i4aas;i=6087"]), o6.hasProperty(o6.ns["ns=i4aas;i=6088"])],
)
o6.reference(i4aas_objtypes.AASDataSpecificationIEC61360Type, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5026"])
o6.reference(o6.ns["ns=i4aas;i=5026"], "i=17597", adminMinusShellDotIoSlashDataSpecificationSlashIdentification)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6089",
    browseName="ns=i4aas;IdType",
    dataType=i4aas_datypes.AASIdentifierTypeDataType,
    value=i4aas_datypes.AASIdentifierTypeDataType.IRDI,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6089"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashIdentifierSlashIdType)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6090", browseName="ns=i4aas;Id", dataType=o6.String, value="\n      ", accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=i4aas;i=6090"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashIdentifierSlashId)
i4aas_objtypes.AASIdentifierType(
    nodeId="ns=i4aas;i=5034",
    browseName="ns=i4aas;Identification",
    modellingRule="Mandatory",
    references=[o6.hasProperty(o6.ns["ns=i4aas;i=6089"]), o6.hasProperty(o6.ns["ns=i4aas;i=6090"])],
)
o6.reference(i4aas_objtypes.IAASIdentifiableType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5034"])
o6.reference(o6.ns["ns=i4aas;i=5034"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashIdentifiableSlashIdentification)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6091",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6091"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(
    nodeId="ns=i4aas;i=5036", browseName="ns=i4aas;<Referable>", modellingRule="OptionalPlaceholder", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6091"])]
)
o6.reference(i4aas_objtypes.AASViewType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5036"])
o6.reference(o6.ns["ns=i4aas;i=5036"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashViewSlashContainedElements)
o6.reference(o6.ns["ns=i4aas;i=5036"], "ns=i4aas;i=4003", o6.ns["ns=i4aas;i=6091"])
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6092",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6092"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(
    nodeId="ns=i4aas;i=5037", browseName="ns=i4aas;<DataSpecification>", modellingRule="OptionalPlaceholder", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6092"])]
)
o6.reference(i4aas_objtypes.AASViewType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5037"])
o6.reference(o6.ns["ns=i4aas;i=5037"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashViewSlashDataSpecifications)
o6.reference(o6.ns["ns=i4aas;i=5037"], "ns=i4aas;i=4003", o6.ns["ns=i4aas;i=6092"])
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6093",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=3010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("IRDI"), description=o6.LocalizedText("IRDI according to ISO29002-5 as an Identifier scheme for properties and classifications")
        ),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("IRI"), description=o6.LocalizedText("Internationalized Resource Identifier according to RFC3305")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Custom"), description=o6.LocalizedText("Custom identifiers like GUIDs (globally unique Identifiers)")),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=i4aas;i=6098", browseName="ns=i4aas;AASKeyDataType", dataType=o6.String, value="AASKeyDataType")
o6.reference(o6.ns["ns=i4aas;i=5038"], "i=39", o6.ns["ns=i4aas;i=6098"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=i4aas;i=6094",
    browseName="ns=i4aas;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/I4AAS/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6095", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/I4AAS/")),
        o6.hasComponent(o6.ns["ns=i4aas;i=6098"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/I4AAS/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/I4AAS/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="AASKeyDataType">\n  <opc:Field TypeName="tns:AASKeyElementsDataType" Name="Type"/>\n  <opc:Field TypeName="opc:Boolean" Name="Local"/>\n  <opc:Field TypeName="opc:CharArray" Name="Value"/>\n  <opc:Field TypeName="tns:AASKeyTypeDataType" Name="IdType"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="AASAssetKindDataType">\n  <opc:EnumeratedValue Name="Type" Value="0"/>\n  <opc:EnumeratedValue Name="Instance" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="AASCategoryDataType">\n  <opc:EnumeratedValue Name="CONSTANT" Value="0"/>\n  <opc:EnumeratedValue Name="PARAMETER" Value="1"/>\n  <opc:EnumeratedValue Name="VARIABLE" Value="2"/>\n  <opc:EnumeratedValue Name="RELATIONSHIP" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="DataTypeIEC61360DataType">\n  <opc:EnumeratedValue Name="DATE" Value="0"/>\n  <opc:EnumeratedValue Name="STRING" Value="1"/>\n  <opc:EnumeratedValue Name="STRING_TRANSLATABLE" Value="2"/>\n  <opc:EnumeratedValue Name="REAL_MEASURE" Value="3"/>\n  <opc:EnumeratedValue Name="REAL_COUNT" Value="4"/>\n  <opc:EnumeratedValue Name="REAL_CURRENCY" Value="5"/>\n  <opc:EnumeratedValue Name="BOOLEAN" Value="6"/>\n  <opc:EnumeratedValue Name="URL" Value="7"/>\n  <opc:EnumeratedValue Name="RATIONAL" Value="8"/>\n  <opc:EnumeratedValue Name="RATIONAL_MEASURE" Value="9"/>\n  <opc:EnumeratedValue Name="TIME" Value="10"/>\n  <opc:EnumeratedValue Name="TIME_STAMP" Value="11"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="EntityTypeDataType">\n  <opc:EnumeratedValue Name="CoManagedEntity" Value="0"/>\n  <opc:EnumeratedValue Name="SelfManagedEntity" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="AASIdentifierTypeDataType">\n  <opc:EnumeratedValue Name="IRDI" Value="0"/>\n  <opc:EnumeratedValue Name="IRI" Value="1"/>\n  <opc:EnumeratedValue Name="Custom" Value="2"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="AASKeyElementsDataType">\n  <opc:EnumeratedValue Name="AccessPermissionRule" Value="0"/>\n  <opc:EnumeratedValue Name="AnnotatedRelationshipElement" Value="1"/>\n  <opc:EnumeratedValue Name="Asset" Value="2"/>\n  <opc:EnumeratedValue Name="AssetAdministrationShell" Value="3"/>\n  <opc:EnumeratedValue Name="Blob" Value="4"/>\n  <opc:EnumeratedValue Name="Capability" Value="5"/>\n  <opc:EnumeratedValue Name="ConceptDescription" Value="6"/>\n  <opc:EnumeratedValue Name="ConceptDictionary" Value="7"/>\n  <opc:EnumeratedValue Name="DataElement" Value="8"/>\n  <opc:EnumeratedValue Name="Entity" Value="9"/>\n  <opc:EnumeratedValue Name="Event" Value="10"/>\n  <opc:EnumeratedValue Name="File" Value="11"/>\n  <opc:EnumeratedValue Name="FragmentReference" Value="12"/>\n  <opc:EnumeratedValue Name="GlobalReference" Value="13"/>\n  <opc:EnumeratedValue Name="MultiLanguageProperty" Value="14"/>\n  <opc:EnumeratedValue Name="Operation" Value="15"/>\n  <opc:EnumeratedValue Name="Property" Value="16"/>\n  <opc:EnumeratedValue Name="Range" Value="17"/>\n  <opc:EnumeratedValue Name="ReferenceElement" Value="18"/>\n  <opc:EnumeratedValue Name="RelationshipElement" Value="19"/>\n  <opc:EnumeratedValue Name="Submodel" Value="20"/>\n  <opc:EnumeratedValue Name="SubmodelElement" Value="21"/>\n  <opc:EnumeratedValue Name="SubmodelElementCollection" Value="22"/>\n  <opc:EnumeratedValue Name="View" Value="23"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="AASKeyTypeDataType">\n  <opc:EnumeratedValue Name="IdShort" Value="0"/>\n  <opc:EnumeratedValue Name="FragmentId" Value="1"/>\n  <opc:EnumeratedValue Name="Custom" Value="2"/>\n  <opc:EnumeratedValue Name="IRDI" Value="3"/>\n  <opc:EnumeratedValue Name="IRI" Value="4"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="AASLevelTypeDataType">\n  <opc:EnumeratedValue Name="Min" Value="0"/>\n  <opc:EnumeratedValue Name="Max" Value="1"/>\n  <opc:EnumeratedValue Name="Num" Value="2"/>\n  <opc:EnumeratedValue Name="Type" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="AASModelingKindDataType">\n  <opc:EnumeratedValue Name="Template" Value="0"/>\n  <opc:EnumeratedValue Name="Instance" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="AASValueTypeDataType">\n  <opc:EnumeratedValue Name="Boolean" Value="0"/>\n  <opc:EnumeratedValue Name="SByte" Value="1"/>\n  <opc:EnumeratedValue Name="Byte" Value="2"/>\n  <opc:EnumeratedValue Name="Int16" Value="3"/>\n  <opc:EnumeratedValue Name="UInt16" Value="4"/>\n  <opc:EnumeratedValue Name="Int32" Value="5"/>\n  <opc:EnumeratedValue Name="UInt32" Value="6"/>\n  <opc:EnumeratedValue Name="Int64" Value="7"/>\n  <opc:EnumeratedValue Name="UInt64" Value="8"/>\n  <opc:EnumeratedValue Name="Float" Value="9"/>\n  <opc:EnumeratedValue Name="Double" Value="10"/>\n  <opc:EnumeratedValue Name="String" Value="11"/>\n  <opc:EnumeratedValue Name="DateTime" Value="12"/>\n  <opc:EnumeratedValue Name="ByteString" Value="13"/>\n  <opc:EnumeratedValue Name="LocalizedText" Value="14"/>\n  <opc:EnumeratedValue Name="UtcTime" Value="15"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6099",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=3003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("Type"),
            description=o6.LocalizedText(
                "hardware or software element which specifies the common attributes shared by all instances of the type\n[SOURCE: IEC TR 62390:2005-01, 3.1.25]\n", ""
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("Instance"),
            description=o6.LocalizedText(
                "concrete, clearly identifiable component of a certain type\n\nNote: It becomes an individual entity of a type, for example a device, by defining specific property values.\n\nNote: In an object-oriented view, an instance denotes an object of a class (of a type).\n\n[SOURCE: IEC 62890:2016, 3.1.16] 65/617/CDV\n",
                "",
            ),
        ),
    ],
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=i4aas;i=6100", browseName="ns=i4aas;AASKeyDataType", dataType=o6.String, value="//xs:element[@name='AASKeyDataType']")
o6.reference(o6.ns["ns=i4aas;i=5039"], "i=39", o6.ns["ns=i4aas;i=6100"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=i4aas;i=6096",
    browseName="ns=i4aas;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/I4AAS/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6097", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/I4AAS/Types.xsd")),
        o6.hasComponent(o6.ns["ns=i4aas;i=6100"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/I4AAS/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/I4AAS/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="AASAssetKindDataType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Type_0"/>\n   <xs:enumeration value="Instance_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:AASAssetKindDataType" name="AASAssetKindDataType"/>\n <xs:complexType name="ListOfAASAssetKindDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AASAssetKindDataType" name="AASAssetKindDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAASAssetKindDataType" name="ListOfAASAssetKindDataType" nillable="true"/>\n <xs:simpleType name="AASCategoryDataType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="CONSTANT_0"/>\n   <xs:enumeration value="PARAMETER_1"/>\n   <xs:enumeration value="VARIABLE_2"/>\n   <xs:enumeration value="RELATIONSHIP_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:AASCategoryDataType" name="AASCategoryDataType"/>\n <xs:complexType name="ListOfAASCategoryDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AASCategoryDataType" name="AASCategoryDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAASCategoryDataType" name="ListOfAASCategoryDataType" nillable="true"/>\n <xs:simpleType name="DataTypeIEC61360DataType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="DATE_0"/>\n   <xs:enumeration value="STRING_1"/>\n   <xs:enumeration value="STRING_TRANSLATABLE_2"/>\n   <xs:enumeration value="REAL_MEASURE_3"/>\n   <xs:enumeration value="REAL_COUNT_4"/>\n   <xs:enumeration value="REAL_CURRENCY_5"/>\n   <xs:enumeration value="BOOLEAN_6"/>\n   <xs:enumeration value="URL_7"/>\n   <xs:enumeration value="RATIONAL_8"/>\n   <xs:enumeration value="RATIONAL_MEASURE_9"/>\n   <xs:enumeration value="TIME_10"/>\n   <xs:enumeration value="TIME_STAMP_11"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:DataTypeIEC61360DataType" name="DataTypeIEC61360DataType"/>\n <xs:complexType name="ListOfDataTypeIEC61360DataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:DataTypeIEC61360DataType" name="DataTypeIEC61360DataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfDataTypeIEC61360DataType" name="ListOfDataTypeIEC61360DataType" nillable="true"/>\n <xs:simpleType name="EntityTypeDataType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="CoManagedEntity_0"/>\n   <xs:enumeration value="SelfManagedEntity_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:EntityTypeDataType" name="EntityTypeDataType"/>\n <xs:complexType name="ListOfEntityTypeDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:EntityTypeDataType" name="EntityTypeDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfEntityTypeDataType" name="ListOfEntityTypeDataType" nillable="true"/>\n <xs:simpleType name="AASIdentifierTypeDataType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="IRDI_0"/>\n   <xs:enumeration value="IRI_1"/>\n   <xs:enumeration value="Custom_2"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:AASIdentifierTypeDataType" name="AASIdentifierTypeDataType"/>\n <xs:complexType name="ListOfAASIdentifierTypeDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AASIdentifierTypeDataType" name="AASIdentifierTypeDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAASIdentifierTypeDataType" name="ListOfAASIdentifierTypeDataType" nillable="true"/>\n <xs:simpleType name="AASKeyElementsDataType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="AccessPermissionRule_0"/>\n   <xs:enumeration value="AnnotatedRelationshipElement_1"/>\n   <xs:enumeration value="Asset_2"/>\n   <xs:enumeration value="AssetAdministrationShell_3"/>\n   <xs:enumeration value="Blob_4"/>\n   <xs:enumeration value="Capability_5"/>\n   <xs:enumeration value="ConceptDescription_6"/>\n   <xs:enumeration value="ConceptDictionary_7"/>\n   <xs:enumeration value="DataElement_8"/>\n   <xs:enumeration value="Entity_9"/>\n   <xs:enumeration value="Event_10"/>\n   <xs:enumeration value="File_11"/>\n   <xs:enumeration value="FragmentReference_12"/>\n   <xs:enumeration value="GlobalReference_13"/>\n   <xs:enumeration value="MultiLanguageProperty_14"/>\n   <xs:enumeration value="Operation_15"/>\n   <xs:enumeration value="Property_16"/>\n   <xs:enumeration value="Range_17"/>\n   <xs:enumeration value="ReferenceElement_18"/>\n   <xs:enumeration value="RelationshipElement_19"/>\n   <xs:enumeration value="Submodel_20"/>\n   <xs:enumeration value="SubmodelElement_21"/>\n   <xs:enumeration value="SubmodelElementCollection_22"/>\n   <xs:enumeration value="View_23"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:AASKeyElementsDataType" name="AASKeyElementsDataType"/>\n <xs:complexType name="ListOfAASKeyElementsDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AASKeyElementsDataType" name="AASKeyElementsDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAASKeyElementsDataType" name="ListOfAASKeyElementsDataType" nillable="true"/>\n <xs:simpleType name="AASKeyTypeDataType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="IdShort_0"/>\n   <xs:enumeration value="FragmentId_1"/>\n   <xs:enumeration value="Custom_2"/>\n   <xs:enumeration value="IRDI_3"/>\n   <xs:enumeration value="IRI_4"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:AASKeyTypeDataType" name="AASKeyTypeDataType"/>\n <xs:complexType name="ListOfAASKeyTypeDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AASKeyTypeDataType" name="AASKeyTypeDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAASKeyTypeDataType" name="ListOfAASKeyTypeDataType" nillable="true"/>\n <xs:simpleType name="AASLevelTypeDataType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Min_0"/>\n   <xs:enumeration value="Max_1"/>\n   <xs:enumeration value="Num_2"/>\n   <xs:enumeration value="Type_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:AASLevelTypeDataType" name="AASLevelTypeDataType"/>\n <xs:complexType name="ListOfAASLevelTypeDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AASLevelTypeDataType" name="AASLevelTypeDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAASLevelTypeDataType" name="ListOfAASLevelTypeDataType" nillable="true"/>\n <xs:simpleType name="AASModelingKindDataType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Template_0"/>\n   <xs:enumeration value="Instance_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:AASModelingKindDataType" name="AASModelingKindDataType"/>\n <xs:complexType name="ListOfAASModelingKindDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AASModelingKindDataType" name="AASModelingKindDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAASModelingKindDataType" name="ListOfAASModelingKindDataType" nillable="true"/>\n <xs:simpleType name="AASValueTypeDataType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Boolean_0"/>\n   <xs:enumeration value="SByte_1"/>\n   <xs:enumeration value="Byte_2"/>\n   <xs:enumeration value="Int16_3"/>\n   <xs:enumeration value="UInt16_4"/>\n   <xs:enumeration value="Int32_5"/>\n   <xs:enumeration value="UInt32_6"/>\n   <xs:enumeration value="Int64_7"/>\n   <xs:enumeration value="UInt64_8"/>\n   <xs:enumeration value="Float_9"/>\n   <xs:enumeration value="Double_10"/>\n   <xs:enumeration value="String_11"/>\n   <xs:enumeration value="DateTime_12"/>\n   <xs:enumeration value="ByteString_13"/>\n   <xs:enumeration value="LocalizedText_14"/>\n   <xs:enumeration value="UtcTime_15"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:AASValueTypeDataType" name="AASValueTypeDataType"/>\n <xs:complexType name="ListOfAASValueTypeDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AASValueTypeDataType" name="AASValueTypeDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAASValueTypeDataType" name="ListOfAASValueTypeDataType" nillable="true"/>\n <xs:complexType name="AASKeyDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:AASKeyElementsDataType" name="Type"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:boolean" name="Local"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Value"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="tns:AASKeyTypeDataType" name="IdType"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:AASKeyDataType" name="AASKeyDataType"/>\n <xs:complexType name="ListOfAASKeyDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:AASKeyDataType" name="AASKeyDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfAASKeyDataType" name="ListOfAASKeyDataType" nillable="true"/>\n</xs:schema>\n',
)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6101",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=3012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[24],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("AccessPermissionRule"), description=o6.LocalizedText('"AccessPermissionRule"')),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("AnnotatedRelationshipElement"), description=o6.LocalizedText(";AnnotatedRelationshipElement&#8221;")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Asset"), description=o6.LocalizedText('"Asset"')),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("AssetAdministrationShell"), description=o6.LocalizedText('"AssetAdministrationShell"')),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("Blob"), description=o6.LocalizedText('"Blob"')),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("Capability"), description=o6.LocalizedText('"Capability"')),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("ConceptDescription"), description=o6.LocalizedText('"ConceptDescription"')),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("ConceptDictionary"), description=o6.LocalizedText('"ConceptDictionary"')),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("DataElement"), description=o6.LocalizedText('"DataElement"')),
        ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("Entity"), description=o6.LocalizedText('"Entity"')),
        ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("Event"), description=o6.LocalizedText('"Event"')),
        ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("File"), description=o6.LocalizedText('"File"')),
        ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("FragmentReference"), description=o6.LocalizedText('"FragmentReference"')),
        ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("GlobalReference"), description=o6.LocalizedText('"GlobalReference"')),
        ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("MultiLanguageProperty"), description=o6.LocalizedText('"MultiLanguageProperty"')),
        ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("Operation"), description=o6.LocalizedText('"Operation"')),
        ns0.datatypes.EnumValueType(value=16, displayName=o6.LocalizedText("Property"), description=o6.LocalizedText('"Property"')),
        ns0.datatypes.EnumValueType(value=17, displayName=o6.LocalizedText("Range"), description=o6.LocalizedText('"Range"')),
        ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("ReferenceElement"), description=o6.LocalizedText('"ReferenceElement"')),
        ns0.datatypes.EnumValueType(value=19, displayName=o6.LocalizedText("RelationshipElement"), description=o6.LocalizedText('"RelationshipElement"')),
        ns0.datatypes.EnumValueType(value=20, displayName=o6.LocalizedText("Submodel"), description=o6.LocalizedText('"Submodel"')),
        ns0.datatypes.EnumValueType(value=21, displayName=o6.LocalizedText("SubmodelElement"), description=o6.LocalizedText('"SubmodelElement"')),
        ns0.datatypes.EnumValueType(value=22, displayName=o6.LocalizedText("SubmodelElementCollection"), description=o6.LocalizedText('"SubmodelElementCollection"')),
        ns0.datatypes.EnumValueType(value=23, displayName=o6.LocalizedText("View"), description=o6.LocalizedText('"View"')),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6102",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=3009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Min"), description=o6.LocalizedText(";Minimum&#8221;")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Max"), description=o6.LocalizedText(";Maximum&#8221;")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Num"), description=o6.LocalizedText('"Number"')),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("Type"), description=o6.LocalizedText('"Type"')),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6103",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=3006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("CoManagedEntity"),
            description=o6.LocalizedText(
                "Self-Managed Entities have their own AAS. This is why a reference to this asset is specified as well (Entity/asset). Additionally, further property statements (compare to [15]) can be added to the asset that are not specified in the AAS of the asset itself because they are specified in relation to the complex I4.0 Component only."
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("SelfManagedEntity"),
            description=o6.LocalizedText(
                "For co-managed entities there is no separate AAS. The relationships and property statements of such entities are managed within the AAS of the composite I4.0 Component."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6104",
    browseName="ns=i4aas;ModelingKind",
    dataType=i4aas_datypes.AASModelingKindDataType,
    value=i4aas_datypes.AASModelingKindDataType.TEMPLATE,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6104"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementSlashKind)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6105",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6105"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(
    nodeId="ns=i4aas;i=5044", browseName="ns=i4aas;<ConceptDescription>", modellingRule="OptionalPlaceholder", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6105"])]
)
o6.reference(i4aas_objtypes.AASIrdiConceptDescriptionType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5044"])
o6.reference(o6.ns["ns=i4aas;i=5044"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashConceptDescriptionSlashIsCaseOf)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6106",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6106"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(
    nodeId="ns=i4aas;i=5046", browseName="ns=i4aas;<ConceptDescription>", modellingRule="OptionalPlaceholder", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6106"])]
)
o6.reference(i4aas_objtypes.AASIriConceptDescriptionType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5046"])
o6.reference(o6.ns["ns=i4aas;i=5046"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashConceptDescriptionSlashIsCaseOf)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6107",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6107"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(
    nodeId="ns=i4aas;i=5048", browseName="ns=i4aas;<ConceptDescription>", modellingRule="OptionalPlaceholder", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6107"])]
)
o6.reference(i4aas_objtypes.AASCustomConceptDescriptionType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5048"])
o6.reference(o6.ns["ns=i4aas;i=5048"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashConceptDescriptionSlashIsCaseOf)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6108",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=3002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("IdShort"), description=o6.LocalizedText("...")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("FragmentId"), description=o6.LocalizedText("...")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("Custom"), description=o6.LocalizedText("...")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("IRDI"), description=o6.LocalizedText("...")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("IRI"), description=o6.LocalizedText("...")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6109",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=3007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("CONSTANT"), description=o6.LocalizedText("Constant")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("PARAMETER"), description=o6.LocalizedText("Parameter")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("VARIABLE"), description=o6.LocalizedText("Variable")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("RELATIONSHIP"), description=o6.LocalizedText("Relationship")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6110",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=3004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[16],
    value=[
        o6.LocalizedText("Boolean"),
        o6.LocalizedText("SByte"),
        o6.LocalizedText("Byte"),
        o6.LocalizedText("Int16"),
        o6.LocalizedText("UInt16"),
        o6.LocalizedText("Int32"),
        o6.LocalizedText("UInt32"),
        o6.LocalizedText("Int64"),
        o6.LocalizedText("UInt64"),
        o6.LocalizedText("Float"),
        o6.LocalizedText("Double"),
        o6.LocalizedText("String"),
        o6.LocalizedText("DateTime"),
        o6.LocalizedText("ByteString"),
        o6.LocalizedText("LocalizedText"),
        o6.LocalizedText("UtcTime"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6111",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=3008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[12],
    value=[
        o6.LocalizedText("DATE"),
        o6.LocalizedText("STRING"),
        o6.LocalizedText("STRING_TRANSLATABLE"),
        o6.LocalizedText("REAL_MEASURE"),
        o6.LocalizedText("REAL_COUNT"),
        o6.LocalizedText("REAL_CURRENCY"),
        o6.LocalizedText("BOOLEAN"),
        o6.LocalizedText("URL"),
        o6.LocalizedText("RATIONAL"),
        o6.LocalizedText("RATIONAL_MEASURE"),
        o6.LocalizedText("TIME"),
        o6.LocalizedText("TIME_STAMP"),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6112",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6112"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(
    nodeId="ns=i4aas;i=5049", browseName="ns=i4aas;AssetIdentificationModel", modellingRule="Optional", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6112"])]
)
o6.reference(i4aas_objtypes.AASAssetType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5049"])
o6.reference(o6.ns["ns=i4aas;i=5049"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetSlashAssetIdentificationModel)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6113",
    browseName="ns=i4aas;Keys",
    dataType=i4aas_datypes.AASKeyDataType,
    valueRank=1,
    arrayDimensions=[1],
    value=[i4aas_datypes.AASKeyDataType(type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT)],
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6113"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashReferenceSlashKeys)
i4aas_objtypes.AASReferenceType(nodeId="ns=i4aas;i=5050", browseName="ns=i4aas;BillOfMaterial", modellingRule="Optional", references=[o6.hasProperty(o6.ns["ns=i4aas;i=6113"])])
o6.reference(i4aas_objtypes.AASAssetType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5050"])
o6.reference(o6.ns["ns=i4aas;i=5050"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashAssetSlashBillOfMaterial)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6114",
    browseName="ns=i4aas;ModelingKind",
    dataType=i4aas_datypes.AASModelingKindDataType,
    value=i4aas_datypes.AASModelingKindDataType.TEMPLATE,
    accessLevel=3,
    userAccessLevel=1,
)
o6.reference(o6.ns["ns=i4aas;i=6114"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementSlashKind)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashI4AASSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=i4aas;i=5023",
    browseName="ns=i4aas;http://opcfoundation.org/UA/I4AAS/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6060", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6061", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2021-06-04T00:00:00Z"))),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6062", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/I4AAS/")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6115", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=i4aas;i=6116", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[1], value=[ns0.datatypes.IdType.NUMERIC]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=i4aas;i=6117", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[1], value=["1:2147483647"]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6118", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6120", browseName="ns=i4aas;IdShort", dataType=o6.String, value="\n      ", accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=i4aas;i=6120"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementSlashIdShort)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6121", browseName="ns=i4aas;IdShort", dataType=o6.String, value="\n      ", accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=i4aas;i=6121"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementSlashIdShort)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6122", browseName="ns=i4aas;IdShort", dataType=o6.String, value="\n      ", accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=i4aas;i=6122"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementSlashIdShort)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6123", browseName="ns=i4aas;IdShort", dataType=o6.String, value="\n      ", accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=i4aas;i=6123"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementSlashIdShort)
ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6124", browseName="ns=i4aas;IdShort", dataType=o6.String, value="\n      ", accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=i4aas;i=6124"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementSlashIdShort)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6125",
    browseName="EnumValues",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=3015",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("Template"),
            description=o6.LocalizedText(
                "Hardware or software element which specifies the common attributes shared by all instances of the type\n[SOURCE: IEC TR 62390:2005-01, 3.1.25]\n", ""
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("Instance"),
            description=o6.LocalizedText(
                "Concrete, clearly identifiable component of a certain template. \n\nNote: It becomes an individual entity of a template, for example a device model, by defining specific property values. \n\nNote: In an object oriented view, an instance denotes an object of a template (class). \n\n[SOURCE: IEC 62890:2016, 3.1.16 65/617/CDV] modified\n",
                "",
            ),
        ),
    ],
)
i4aas_objtypes.AASSubmodelElementType(
    nodeId="ns=i4aas;i=5010",
    browseName="ns=i4aas;<SubmodelElement>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(o6.ns["ns=i4aas;i=6014"]),
        o6.hasProperty(o6.ns["ns=i4aas;i=6120"]),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6127", browseName="ns=i4aas;Category", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    _allow_abstract=True,
)
o6.reference(i4aas_objtypes.AASSubmodelType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5010"])
o6.reference(o6.ns["ns=i4aas;i=5010"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelSlashSubmodelElements)
i4aas_objtypes.AASSubmodelElementType(
    nodeId="ns=i4aas;i=5012",
    browseName="ns=i4aas;<SubmodelElement>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(o6.ns["ns=i4aas;i=6016"]),
        o6.hasProperty(o6.ns["ns=i4aas;i=6121"]),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6128", browseName="ns=i4aas;Category", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    _allow_abstract=True,
)
o6.reference(i4aas_objtypes.AASSubmodelElementCollectionType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5012"])
o6.reference(o6.ns["ns=i4aas;i=5012"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementCollectionSlashValues)
i4aas_objtypes.AASSubmodelElementType(
    nodeId="ns=i4aas;i=5019",
    browseName="ns=i4aas;<DataElement>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(o6.ns["ns=i4aas;i=6114"]),
        o6.hasProperty(o6.ns["ns=i4aas;i=6122"]),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6129", browseName="ns=i4aas;Category", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    _allow_abstract=True,
)
o6.reference(i4aas_objtypes.AASAnnotatedRelationshipElementType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5019"])
o6.reference(o6.ns["ns=i4aas;i=5019"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashAnnotatedRelationshipElementSlashAnnotations)
i4aas_objtypes.AASSubmodelElementType(
    nodeId="ns=i4aas;i=5021",
    browseName="ns=i4aas;<SubmodelElement>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(o6.ns["ns=i4aas;i=6054"]),
        o6.hasProperty(o6.ns["ns=i4aas;i=6123"]),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6130", browseName="ns=i4aas;Category", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    _allow_abstract=True,
)
o6.reference(i4aas_objtypes.AASEntityType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5021"])
o6.reference(o6.ns["ns=i4aas;i=5021"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashEntitySlashStatements)
i4aas_objtypes.AASSubmodelElementType(
    nodeId="ns=i4aas;i=5042",
    browseName="ns=i4aas;<SubmodelElement>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(o6.ns["ns=i4aas;i=6104"]),
        o6.hasProperty(o6.ns["ns=i4aas;i=6124"]),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6131", browseName="ns=i4aas;Category", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
    ],
    _allow_abstract=True,
)
o6.reference(i4aas_objtypes.AASOrderedSubmodelElementCollectionType, ns0.reftypes.HasOrderedComponent, o6.ns["ns=i4aas;i=5042"])
o6.reference(o6.ns["ns=i4aas;i=5042"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementCollectionSlashValues)
i4aas_objtypes.AASReferenceType(
    nodeId="ns=i4aas;i=5025",
    browseName="ns=i4aas;<DataSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=i4aas;i=6133",
                browseName="ns=i4aas;Keys",
                dataType=i4aas_datypes.AASKeyDataType,
                valueRank=1,
                arrayDimensions=[1],
                value=[
                    i4aas_datypes.AASKeyDataType(
                        type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT
                    )
                ],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
)
o6.reference(i4aas_objtypes.AASIriConceptDescriptionType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5025"])
o6.reference(o6.ns["ns=i4aas;i=5025"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashHasDataSpecificationSlashDataSpecification)
i4aas_objtypes.AASReferenceType(
    nodeId="ns=i4aas;i=5043",
    browseName="ns=i4aas;<DataSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=i4aas;i=6134",
                browseName="ns=i4aas;Keys",
                dataType=i4aas_datypes.AASKeyDataType,
                valueRank=1,
                arrayDimensions=[1],
                value=[
                    i4aas_datypes.AASKeyDataType(
                        type=i4aas_datypes.AASKeyElementsDataType.ACCESS_PERMISSION_RULE, local=False, value="", idType=i4aas_datypes.AASKeyTypeDataType.ID_SHORT
                    )
                ],
                accessLevel=3,
                userAccessLevel=1,
            )
        )
    ],
)
o6.reference(i4aas_objtypes.AASCustomConceptDescriptionType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5043"])
o6.reference(o6.ns["ns=i4aas;i=5043"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashHasDataSpecificationSlashDataSpecification)
i4aas_objtypes.AASQualifierType(
    nodeId="ns=i4aas;i=5031",
    browseName="ns=i4aas;<Qualifier>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(o6.ns["ns=i4aas;i=6080"]),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=i4aas;i=6135",
                browseName="ns=i4aas;ValueType",
                dataType=i4aas_datypes.AASValueTypeDataType,
                value=i4aas_datypes.AASValueTypeDataType.BOOLEAN,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(i4aas_objtypes.AASSubmodelElementType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5031"])
o6.reference(o6.ns["ns=i4aas;i=5031"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelElementSlashQualifiers)
i4aas_objtypes.AASQualifierType(
    nodeId="ns=i4aas;i=5032",
    browseName="ns=i4aas;<Qualifier>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(o6.ns["ns=i4aas;i=6081"]),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=i4aas;i=6136",
                browseName="ns=i4aas;ValueType",
                dataType=i4aas_datypes.AASValueTypeDataType,
                value=i4aas_datypes.AASValueTypeDataType.BOOLEAN,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
o6.reference(i4aas_objtypes.AASSubmodelType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5032"])
o6.reference(o6.ns["ns=i4aas;i=5032"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashSubmodelSlashQualifiers)


ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6023",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=i4aas;i=7002", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=i4aas;i=6023"]))

ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6024",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6025",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=7003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=i4aas;i=7003", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=i4aas;i=6024"]), outputArgs=o6.hasProperty(o6.ns["ns=i4aas;i=6025"]))

ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6026",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6027",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=i4aas;i=7004", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=i4aas;i=6026"]), outputArgs=o6.hasProperty(o6.ns["ns=i4aas;i=6027"]))

ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6029",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6030",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=7005",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=i4aas;i=7005", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=i4aas;i=6029"]), outputArgs=o6.hasProperty(o6.ns["ns=i4aas;i=6030"]))

ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6031",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=i4aas;i=7006", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=i4aas;i=6031"]))

ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6035",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=i4aas;i=7007", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=i4aas;i=6035"]))

ns0.objtypes.FileType(
    nodeId="ns=i4aas;i=5015",
    browseName="ns=i4aas;File",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6028", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6032", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6033", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6034", browseName="Writable", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=i4aas;i=7002"]),
        o6.hasComponent(o6.ns["ns=i4aas;i=7003"]),
        o6.hasComponent(o6.ns["ns=i4aas;i=7004"]),
        o6.hasComponent(o6.ns["ns=i4aas;i=7005"]),
        o6.hasComponent(o6.ns["ns=i4aas;i=7006"]),
        o6.hasComponent(o6.ns["ns=i4aas;i=7007"]),
    ],
)
o6.reference(i4aas_objtypes.AASBlobType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5015"])
o6.reference(o6.ns["ns=i4aas;i=5015"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashBlobSlashValue)


ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6038",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=i4aas;i=7008", browseName="Close", inputArgs=o6.hasProperty(o6.ns["ns=i4aas;i=6038"]))

ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6039",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6040",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=i4aas;i=7009", browseName="GetPosition", inputArgs=o6.hasProperty(o6.ns["ns=i4aas;i=6039"]), outputArgs=o6.hasProperty(o6.ns["ns=i4aas;i=6040"]))

ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6041",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Mode", dataType=o6.Byte, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6042",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1)],
)
o6.call(nodeId="ns=i4aas;i=7010", browseName="Open", inputArgs=o6.hasProperty(o6.ns["ns=i4aas;i=6041"]), outputArgs=o6.hasProperty(o6.ns["ns=i4aas;i=6042"]))

ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6044",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Length", dataType=o6.Int32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6045",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=7011",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=i4aas;i=7011", browseName="Read", inputArgs=o6.hasProperty(o6.ns["ns=i4aas;i=6044"]), outputArgs=o6.hasProperty(o6.ns["ns=i4aas;i=6045"]))

ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6046",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=7012",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Position", dataType=o6.UInt64, valueRank=-1)],
)
o6.call(nodeId="ns=i4aas;i=7012", browseName="SetPosition", inputArgs=o6.hasProperty(o6.ns["ns=i4aas;i=6046"]))

ns0.vartypes.PropertyType(
    nodeId="ns=i4aas;i=6050",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=i4aas;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="FileHandle", dataType=o6.UInt32, valueRank=-1), ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1)],
)
o6.call(nodeId="ns=i4aas;i=7013", browseName="Write", inputArgs=o6.hasProperty(o6.ns["ns=i4aas;i=6050"]))

ns0.objtypes.FileType(
    nodeId="ns=i4aas;i=5016",
    browseName="ns=i4aas;File",
    modellingRule="Optional",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6043", browseName="OpenCount", dataType=o6.UInt16)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6047", browseName="Size", dataType=o6.UInt64)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6048", browseName="UserWritable", dataType=o6.Boolean)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=i4aas;i=6049", browseName="Writable", dataType=o6.Boolean)),
        o6.hasComponent(o6.ns["ns=i4aas;i=7008"]),
        o6.hasComponent(o6.ns["ns=i4aas;i=7009"]),
        o6.hasComponent(o6.ns["ns=i4aas;i=7010"]),
        o6.hasComponent(o6.ns["ns=i4aas;i=7011"]),
        o6.hasComponent(o6.ns["ns=i4aas;i=7012"]),
        o6.hasComponent(o6.ns["ns=i4aas;i=7013"]),
    ],
)
o6.reference(i4aas_objtypes.AASFileType, ns0.reftypes.HasComponent, o6.ns["ns=i4aas;i=5016"])
o6.reference(o6.ns["ns=i4aas;i=5016"], "i=17597", adminMinusShellDotIoSlashAasSlash2Slash0SlashFileSlashValue)


del Any, TYPE_CHECKING, uuid, o6, ns0, i4aas_reftypes, i4aas_datypes, i4aas_objtypes
