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

"""Generated OPC UA dexpi namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as dexpi_reftypes
from . import datatypes as dexpi_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=dexpi;i=1060",
    browseName="ns=dexpi;BaseDEXPIObjectType",
    displayName="BaseDEXPIObjectType",
    description="Base object type, parent for all DEXPI Object types",
    isAbstract=True,
)
class BaseDEXPIObjectType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1061",
    browseName="ns=dexpi;DEXPISupplementaryDataType",
    displayName="DEXPISupplementaryDataType",
    description="Additional data including the original XML source file, the DEXPI specification as UML XMI and used version numbers for the DEXPI specification and the Proteus schema",
)
class DEXPISupplementaryDataType(BaseDEXPIObjectType):
    dEXPISpecificationVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=dexpi;i=1066",
            browseName="ns=dexpi;DEXPISpecificationVersion",
            description="Variable which holds the version of DEXPI specification",
            dataType=o6.String,
            value="1.2",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    dEXPIXMIExternalLink: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=dexpi;i=1063",
            browseName="ns=dexpi;DEXPIXMIExternalLink",
            description="Variable which holds a link to the XMI file of DEXPI specification as UML",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    dEXPIXMIFile: ns0.objtypes.FileType | None = o6.hasComponent(
        ns0.objtypes.FileType(nodeId="ns=dexpi;i=1064", browseName="ns=dexpi;DEXPIXMIFile", description="Object that holds the data of the XMI file of DEXPI specification as UML")
    )
    proteusSchemaVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=dexpi;i=1067",
            browseName="ns=dexpi;ProteusSchemaVersion",
            description="Variable which holds the version of Proteus schema",
            dataType=o6.String,
            value="4.0.1",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    proteusXMLExternalLink: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=dexpi;i=1062",
            browseName="ns=dexpi;ProteusXMLExternalLink",
            description="Variable which a link to the XML file of the input P&ID model",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    proteusXMLFile: ns0.objtypes.FileType | None = o6.hasComponent(
        ns0.objtypes.FileType(nodeId="ns=dexpi;i=1065", browseName="ns=dexpi;ProteusXMLFile", description="Object that holds the data of the Proteus XML file of DEXPI P&ID model")
    )


@o6.objecttype(nodeId="ns=dexpi;i=1079", browseName="ns=dexpi;MetaDataType", displayName="MetaDataType", description="A container for meta data about a PlantModel.")
class MetaDataType(BaseDEXPIObjectType):
    approvalDateRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1080",
            browseName="ns=dexpi;ApprovalDateRepresentationAssignmentClass",
            description="A representation of the approval date of the drawing.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    approvalDescriptionAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1081",
            browseName="ns=dexpi;ApprovalDescriptionAssignmentClass",
            description="A description of the approval of the drawing.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    approverNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1082",
            browseName="ns=dexpi;ApproverNameAssignmentClass",
            description="The name of the approver of the drawing.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    archiveNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1083",
            browseName="ns=dexpi;ArchiveNumberAssignmentClass",
            description="The archive number of the drawing.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    areaIsa95NameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1084",
            browseName="ns=dexpi;AreaIsa95NameAssignmentClass",
            description="The name of the related area according to ISA-95.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    blockNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1085",
            browseName="ns=dexpi;BlockNameAssignmentClass",
            description="The name of the related block.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    blockNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1086",
            browseName="ns=dexpi;BlockNumberAssignmentClass",
            description="The number of the related block.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    checkerNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1087",
            browseName="ns=dexpi;CheckerNameAssignmentClass",
            description="The name of the checker of the drawing.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    companyNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1088",
            browseName="ns=dexpi;CompanyNameAssignmentClass",
            description="The name of the company.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    companyNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1089",
            browseName="ns=dexpi;CompanyNumberAssignmentClass",
            description="The number of the company.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    confidentialitySpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1090",
            browseName="ns=dexpi;ConfidentialitySpecialization",
            description="The confidentiality of the drawing.",
            dataType=dexpi_datypes.ConfidentialityClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    creationDateRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1091",
            browseName="ns=dexpi;CreationDateRepresentationAssignmentClass",
            description="A representation of the creation date of the drawing.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    creatorNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1092",
            browseName="ns=dexpi;CreatorNameAssignmentClass",
            description="The name of the creator of the drawing.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    designerNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1093",
            browseName="ns=dexpi;DesignerNameAssignmentClass",
            description="The name of the designer of the drawing.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    drafterNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1094",
            browseName="ns=dexpi;DrafterNameAssignmentClass",
            description="The name of the drafter of the drawing.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    drawingNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1096",
            browseName="ns=dexpi;DrawingNameAssignmentClass",
            description="The drawing name.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    drawingNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1095",
            browseName="ns=dexpi;DrawingNumberAssignmentClass",
            description="The drawing number.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    drawingSubTitleAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1097",
            browseName="ns=dexpi;DrawingSubTitleAssignmentClass",
            description="The sub-title of the drawing.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    fileNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1098",
            browseName="ns=dexpi;FileNameAssignmentClass",
            description="The name of the drawing file.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    locationNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1099",
            browseName="ns=dexpi;LocationNameAssignmentClass",
            description="The location name.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    modificationDataRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1100",
            browseName="ns=dexpi;ModificationDataRepresentationAssignmentClass",
            description="A representation of the last modification date of the drawing.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    processCellIsa95NameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1101",
            browseName="ns=dexpi;ProcessCellIsa95NameAssignmentClass",
            description="The name of the related process cell according to ISA-95.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    processCellIsa95NumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1102",
            browseName="ns=dexpi;ProcessCellIsa95NumberAssignmentClass",
            description="The number of the related process cell according to ISA-95.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    projectNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1103",
            browseName="ns=dexpi;ProjectNameAssignmentClass",
            description="The name of the related project.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    projectNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1104",
            browseName="ns=dexpi;ProjectNumberAssignmentClass",
            description="The number of the related project.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    projectRangeNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1105",
            browseName="ns=dexpi;ProjectRangeNumberAssignmentClass",
            description="The range number of he related project.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    replacedDrawingAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1106",
            browseName="ns=dexpi;ReplacedDrawingAssignmentClass",
            description="The drawing replaced by this drawing.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    responsibleDepartmentNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1107",
            browseName="ns=dexpi;ResponsibleDepartmentNameAssignmentClass",
            description="The name of the department responsible for the drawing.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    revisionNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1108",
            browseName="ns=dexpi;RevisionNumberAssignmentClass",
            description="The revision number of the drawing.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    sheetFormatAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1109",
            browseName="ns=dexpi;SheetFormatAssignmentClass",
            description="The sheet format.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    sheetNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1110",
            browseName="ns=dexpi;SheetNumberAssignmentClass",
            description="The sheet number of the drawing.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    siteIsa95NameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1111",
            browseName="ns=dexpi;SiteIsa95NameAssignmentClass",
            description="The name of the related site according to ISA-95.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    subProjectNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1112",
            browseName="ns=dexpi;SubProjectNameAssignmentClass",
            description="The name of the related sub-project.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    subProjectNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1113",
            browseName="ns=dexpi;SubProjectNumberAssignmentClass",
            description="The number of the related sub-project.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    totalNumberOfSheets: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1114", browseName="ns=dexpi;TotalNumberOfSheets", description="The total number of sheets.", dataType=o6.Int64, accessLevel=3, userAccessLevel=1
        )
    )
    unitIsa95NameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1115",
            browseName="ns=dexpi;UnitIsa95NameAssignmentClass",
            description="The name of the related unit according to ISA-95.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    unitIsa95NumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1116",
            browseName="ns=dexpi;UnitIsa95NumberAssignmentClass",
            description="The number of the related unit according to ISA-95.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1117",
    browseName="ns=dexpi;SensingLocationType",
    displayName="SensingLocationType",
    description="An object than can act as a SensingLocation of a ProcessSignalGeneratingFunction.",
    isAbstract=True,
)
class SensingLocationType(BaseDEXPIObjectType):
    pass


@o6.objecttype(nodeId="ns=dexpi;i=1127", browseName="ns=dexpi;PositionerType", displayName="PositionerType", description="A positioner.")
class PositionerType(BaseDEXPIObjectType):
    deviceTypeNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1129",
            browseName="ns=dexpi;DeviceTypeNameAssignmentClass",
            description="The device type of the Positioner.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    subTagNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1128",
            browseName="ns=dexpi;SubTagNameAssignmentClass",
            description="The sub tag name of the Positioner.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1174",
    browseName="ns=dexpi;SignalLineFunctionType",
    displayName="SignalLineFunctionType",
    description="Information flow function for signals.\nAssociation to Source (SignalConveyingFunctionSource)\nAssociation to Target (SignalConveyingFunctionTarget)",
)
class SignalLineFunctionType(BaseDEXPIObjectType):
    portStatusSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1175",
            browseName="ns=dexpi;PortStatusSpecialization",
            description="A classification indicating the port status of the SignalConveyingFunction.",
            dataType=dexpi_datypes.PortStatusClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    signalConveyingTypeSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1176",
            browseName="ns=dexpi;SignalConveyingTypeSpecialization",
            description="A classification indicating the signal conveying type of the SignalConveyingFunction.",
            dataType=dexpi_datypes.SignalConveyingTypeClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    signalPointNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1177",
            browseName="ns=dexpi;SignalPointNumberAssignmentClass",
            description="The signal point number of the SignalConveyingFunction. Typical values are 1 to 6.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    signalProcessControlFunctionsAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1178",
            browseName="ns=dexpi;SignalProcessControlFunctionsAssignmentClass",
            description="The process control functions of the SignalConveyingFunction. Values are combinations of characters.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1181",
    browseName="ns=dexpi;MeasuringLineFunctionType",
    displayName="MeasuringLineFunctionType",
    description="Information flow function for measured values.\nAssociation to Source (SignalConveyingFunctionSource)\nAssociation to Target (SignalConveyingFunctionTarget)",
)
class MeasuringLineFunctionType(BaseDEXPIObjectType):
    portStatusSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1182",
            browseName="ns=dexpi;PortStatusSpecialization",
            description="A classification indicating the port status of the SignalConveyingFunction.",
            dataType=dexpi_datypes.PortStatusClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    signalConveyingTypeSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1183",
            browseName="ns=dexpi;SignalConveyingTypeSpecialization",
            description="A classification indicating the signal conveying type of the SignalConveyingFunction.",
            dataType=dexpi_datypes.SignalConveyingTypeClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    signalPointNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1184",
            browseName="ns=dexpi;SignalPointNumberAssignmentClass",
            description="The signal point number of the SignalConveyingFunction. Typical values are 1 to 6.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    signalProcessControlFunctionsAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1185",
            browseName="ns=dexpi;SignalProcessControlFunctionsAssignmentClass",
            description="The process control functions of the SignalConveyingFunction. Values are combinations of characters.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1188",
    browseName="ns=dexpi;InstrumentationLoopFunctionType",
    displayName="InstrumentationLoopFunctionType",
    description="An identified collection of related ProcessInstrumentationFunctions that interact for a known purpose.\nAssociation to ProcessInstrumentationFunctions (ProcessInstrumentationFunction)\nAssociation to ParentStructure (TechnicalItemParentStructure)\nAssociation to PlantTrain (PlantTrain)\nAssociation to PlantSystem (PlantSystem)\nAssociation to AreaIsa95 (AreaIsa95)",
)
class InstrumentationLoopFunctionType(BaseDEXPIObjectType):
    instrumentationLoopFunctionNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1190",
            browseName="ns=dexpi;InstrumentationLoopFunctionNumberAssignmentClass",
            description="The identification number of the InstrumentationLoopFunction.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1195",
    browseName="ns=dexpi;PrimaryElementType",
    displayName="PrimaryElementType",
    description="An artefact that converts the input variable into a signal suitable for measurement.",
)
class PrimaryElementType(BaseDEXPIObjectType):
    subTagNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1196",
            browseName="ns=dexpi;SubTagNameAssignmentClass",
            description="The sub tag name of the PrimaryElement.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1197",
    browseName="ns=dexpi;ShutOffValveReferenceType",
    displayName="ShutOffValveReferenceType",
    description="A reference to a ShutOffValve.\nAssociation to Valve (ShutOffValve)",
)
class ShutOffValveReferenceType(BaseDEXPIObjectType):
    subTagNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1198",
            browseName="ns=dexpi;SubTagNameAssignmentClass",
            description="The sub tag name of the ShutOffValveReference.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1210",
    browseName="ns=dexpi;ProcessSignalGeneratingFunctionType",
    displayName="ProcessSignalGeneratingFunctionType",
    description="A function for instrumentation and/or control structures relating to Process Engineering\nAssociation to Systems (ProcessSignalGeneratingSystem)\nAssociation to SensingLocation (SensingLocation)\nAssociation to ParentStructure (TechnicalItemParentStructure)\nAssociation to PlantTrain (PlantTrain)\nAssociation to PlantSystem (PlantSystem)\nAssociation to AreaIsa95 (AreaIsa95)",
)
class ProcessSignalGeneratingFunctionType(BaseDEXPIObjectType):
    processSignalGeneratingFunctionNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1211",
            browseName="ns=dexpi;ProcessSignalGeneratingFunctionNumberAssignmentClass",
            description="An identifier for the ProcessSignalGeneratingFunction. It usually contains the identifier of the ProcessInstrumentationFunction that includes the ProcessSignalGeneratingFunction (see ProcessInstrumentationFunctionNumberAssignmentClass).",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    sensorTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1212",
            browseName="ns=dexpi;SensorTypeAssignmentClass",
            description="The sensor type of the ProcessSignalGeneratingFunction.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1219",
    browseName="ns=dexpi;SignalConveyingFunctionTargetType",
    displayName="SignalConveyingFunctionTargetType",
    description="An object than can act as the Target of a SignalConveyingFunction.",
    isAbstract=True,
)
class SignalConveyingFunctionTargetType(BaseDEXPIObjectType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1220",
    browseName="ns=dexpi;OfflinePrimaryElementType",
    displayName="OfflinePrimaryElementType",
    description="A PrimaryElement that is not part of a PipingNetworkSegment.",
)
class OfflinePrimaryElementType(PrimaryElementType):
    connectionNominalDiameterNumericalValueRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1221",
            browseName="ns=dexpi;ConnectionNominalDiameterNumericalValueRepresentationAssignmentClass",
            description="A readable representation of the numerical value of the nominal diameter at the device connection of the OfflinePrimaryElement. The purpose of this value is to give a textual representation of the nominal diameter to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    connectionNominalDiameterRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1222",
            browseName="ns=dexpi;ConnectionNominalDiameterRepresentationAssignmentClass",
            description="A readable representation of the nominal diameter at the device connection of the OfflinePrimaryElement. The purpose of this value is to give a textual representation of the nominal diameter to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    connectionNominalDiameterStandardSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1223",
            browseName="ns=dexpi;ConnectionNominalDiameterStandardSpecialization",
            description="The nominal diameter of the device connection of the OfflinePrimaryElement, given as a reference to a nominal diameter standard and value.",
            dataType=dexpi_datypes.NominalDiameterStandardClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    connectionNominalDiameterTypeRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1224",
            browseName="ns=dexpi;ConnectionNominalDiameterTypeRepresentationAssignmentClass",
            description="A readable representation of the type of the nominal diameter at the device connection of the OfflinePrimaryElement. The purpose of this value is to give a textual representation of the nominal diameter to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    fluidCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1225",
            browseName="ns=dexpi;FluidCodeAssignmentClass",
            description="The identification code of the fluid related to the OfflinePrimaryElement. So  far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    heatTracingTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1226",
            browseName="ns=dexpi;HeatTracingTypeAssignmentClass",
            description="The heat tracing type related to the OfflinePrimaryElement, represented as a string.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    heatTracingTypeSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1227",
            browseName="ns=dexpi;HeatTracingTypeSpecialization",
            description="A specialization indicating the heat tracing type related to the OfflinePrimaryElement.",
            dataType=dexpi_datypes.HeatTracingTypeClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    insulationThickness: ns0.vartypes.AnalogUnitType | None
    insulationTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1231",
            browseName="ns=dexpi;InsulationTypeAssignmentClass",
            description="The identification code for the insulation type related to the OfflinePrimaryElement. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    locationNominalDiameterNumericalValueRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1232",
            browseName="ns=dexpi;LocationNominalDiameterNumericalValueRepresentationAssignmentClass",
            description="A readable representation of the numerical value of the nominal diameter at the location of the OfflinePrimaryElement. The purpose of this value is to give a textual representation of the nominal diameter to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    locationNominalDiameterRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1233",
            browseName="ns=dexpi;LocationNominalDiameterRepresentationAssignmentClass",
            description="A readable representation of the nominal diameter at the location of the OfflinePrimaryElement. The purpose of this value is to give a textual representation of the nominal diameter to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    locationNominalDiameterStandardSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1234",
            browseName="ns=dexpi;LocationNominalDiameterStandardSpecialization",
            description="The nominal diameter of the location of the OfflinePrimaryElement, given as a reference to a nominal diameter standard and value.",
            dataType=dexpi_datypes.NominalDiameterStandardClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    locationNominalDiameterTypeRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1235",
            browseName="ns=dexpi;LocationNominalDiameterTypeRepresentationAssignmentClass",
            description="A readable representation of the type of the nominal diameter at the location of the OfflinePrimaryElement. The purpose of this value is to give a textual representation of the nominal diameter to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    lowerLimitHeatTracingTemperature: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=dexpi;i=1239",
    browseName="ns=dexpi;ActuatingFunctionType",
    displayName="ActuatingFunctionType",
    description="A function for acting control structures relating to the process.\nAssociation to ActuatingLocation (PipingNetworkSegment)\nAssociation to Systems (ActuatingSystem)\nAssociation to ParentStructure (TechnicalItemParentStructure)\nAssociation to PlantTrain (PlantTrain)\nAssociation to PlantSystem (PlantSystem)\nAssociation to AreaIsa95 (AreaIsa95)",
)
class ActuatingFunctionType(BaseDEXPIObjectType):
    actuatingFunctionNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1240",
            browseName="ns=dexpi;ActuatingFunctionNumberAssignmentClass",
            description="An identifier for the ActuatingFunction. It usually contains the identifier of the ProcessInstrumentationFunction that includes the ActuatingFunction (see ProcessInstrumentationFunctionNumberAssignmentClass).",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1247",
    browseName="ns=dexpi;TransmitterType",
    displayName="TransmitterType",
    description="A detecting instrument that generates a process variable signal and converts it into an output signal.",
)
class TransmitterType(BaseDEXPIObjectType):
    deviceTypeNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1249",
            browseName="ns=dexpi;DeviceTypeNameAssignmentClass",
            description="The device type of the Transmitter.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    subTagNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1248",
            browseName="ns=dexpi;SubTagNameAssignmentClass",
            description="The sub tag name of the Transmitter.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1250",
    browseName="ns=dexpi;SignalConveyingFunctionSourceType",
    displayName="SignalConveyingFunctionSourceType",
    description="An object than can act as the Source of a SignalConveyingFunction.",
    isAbstract=True,
)
class SignalConveyingFunctionSourceType(BaseDEXPIObjectType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1251",
    browseName="ns=dexpi;SignalConveyingFunctionType",
    displayName="SignalConveyingFunctionType",
    description="A function for conveying a signal.\nAssociation to Source (SignalConveyingFunctionSource)\nAssociation to Target (SignalConveyingFunctionTarget)",
)
class SignalConveyingFunctionType(BaseDEXPIObjectType):
    portStatusSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1252",
            browseName="ns=dexpi;PortStatusSpecialization",
            description="A classification indicating the port status of the SignalConveyingFunction.",
            dataType=dexpi_datypes.PortStatusClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    signalConveyingTypeSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1253",
            browseName="ns=dexpi;SignalConveyingTypeSpecialization",
            description="A classification indicating the signal conveying type of the SignalConveyingFunction.",
            dataType=dexpi_datypes.SignalConveyingTypeClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    signalPointNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1254",
            browseName="ns=dexpi;SignalPointNumberAssignmentClass",
            description="The signal point number of the SignalConveyingFunction. Typical values are 1 to 6.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    signalProcessControlFunctionsAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1255",
            browseName="ns=dexpi;SignalProcessControlFunctionsAssignmentClass",
            description="The process control functions of the SignalConveyingFunction. Values are combinations of characters.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


o6.reference(SignalLineFunctionType, "ns=dexpi;i=1059", SignalConveyingFunctionType)
o6.reference(MeasuringLineFunctionType, "ns=dexpi;i=1059", SignalConveyingFunctionType)


@o6.objecttype(
    nodeId="ns=dexpi;i=1258",
    browseName="ns=dexpi;ControlledActuatorType",
    displayName="ControlledActuatorType",
    description="A transducer that is intended to convert energy (electric, mechanical, pneumatic or hydraulic) from an external source into kinetic energy (motion) in response to a signal or or power input.",
)
class ControlledActuatorType(BaseDEXPIObjectType):
    deviceTypeNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1260",
            browseName="ns=dexpi;DeviceTypeNameAssignmentClass",
            description="The device type of the ControlledActuator.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    failActionRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1261",
            browseName="ns=dexpi;FailActionRepresentationAssignmentClass",
            description="A readable representation of the fail action of the ControlledActuator. This attribute should also be referenced in the graphics if applicable.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    failActionSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1262",
            browseName="ns=dexpi;FailActionSpecialization",
            description="The fail action of the ControlledActuator.",
            dataType=dexpi_datypes.FailActionClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    subTagNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1259",
            browseName="ns=dexpi;SubTagNameAssignmentClass",
            description="The sub tag name of the ControlledActuator.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1263",
    browseName="ns=dexpi;InlinePrimaryElementReferenceType",
    displayName="InlinePrimaryElementReferenceType",
    description="A reference to an InlinePrimaryElement that is part of a PipingNetworkSegment.\nAssociation to InlinePrimaryElement (InlinePrimaryElement)",
)
class InlinePrimaryElementReferenceType(PrimaryElementType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1265",
    browseName="ns=dexpi;PlantSectionIso10209-2012Type",
    displayName="PlantSectionIso10209-2012Type",
    description="A plant section as defined by ISO 10209:2012.\nAssociation to ParentStructure (PlantSectionIso10209-2012ParentStructure)\nAssociation to AreaIsa95 (AreaIsa95)",
)
class PlantSectionIso10209_2012Type(BaseDEXPIObjectType):
    plantSectionIdentificationCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1266",
            browseName="ns=dexpi;PlantSectionIdentificationCodeAssignmentClass",
            description="The identification code of the PlantSectionIso10209-2012.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    plantSectionNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1267",
            browseName="ns=dexpi;PlantSectionNameAssignmentClass",
            description="The name of the PlantSectionIso10209-2012.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1270",
    browseName="ns=dexpi;AreaIsa95LocatedStructureType",
    displayName="AreaIsa95LocatedStructureType",
    description="A structure that can be located in an AreaIsa95.\nAssociation to AreaIsa95 (AreaIsa95)",
    isAbstract=True,
)
class AreaIsa95LocatedStructureType(BaseDEXPIObjectType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1272",
    browseName="ns=dexpi;IndustrialComplexIso10209-2012Type",
    displayName="IndustrialComplexIso10209-2012Type",
    description="An industrial complex as defined by ISO 10209:2012.\nAssociation to ParentStructure (IndustrialComplexIso10209-2012ParentStructure)\nAssociation to AreaIsa95 (AreaIsa95)",
)
class IndustrialComplexIso10209_2012Type(BaseDEXPIObjectType):
    industrialComplexIdentificationCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1273",
            browseName="ns=dexpi;IndustrialComplexIdentificationCodeAssignmentClass",
            description="The identification code of the IndustrialComplexIso10209-2012.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    industrialComplexNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1274",
            browseName="ns=dexpi;IndustrialComplexNameAssignmentClass",
            description="The name of the IndustrialComplexIso10209-2012.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1277",
    browseName="ns=dexpi;PlantTrainLocatedStructureType",
    displayName="PlantTrainLocatedStructureType",
    description="A structure can be located in a PlantTrain.\nAssociation to PlantTrain (PlantTrain)",
    isAbstract=True,
)
class PlantTrainLocatedStructureType(BaseDEXPIObjectType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1279",
    browseName="ns=dexpi;ProcessPlantParentStructureType",
    displayName="ProcessPlantParentStructureType",
    description="A PlantItemStructure that is a suitable ParentStructure of a ProcessPlant.",
    isAbstract=True,
)
class ProcessPlantParentStructureType(BaseDEXPIObjectType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1280",
    browseName="ns=dexpi;SiteIsa95Type",
    displayName="SiteIsa95Type",
    description="A site as defined by ISA 95.\nAssociation to ParentStructure (Isa95Enterprise)",
)
class SiteIsa95Type(BaseDEXPIObjectType):
    siteIdentificationCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1281",
            browseName="ns=dexpi;SiteIdentificationCodeAssignmentClass",
            description="The identification code of the SiteIsa95.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    siteNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1282",
            browseName="ns=dexpi;SiteNameAssignmentClass",
            description="The name of the SiteIsa95.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1284",
    browseName="ns=dexpi;IndustrialComplexIso10209-2012ParentStructureType",
    displayName="IndustrialComplexIso10209-2012ParentStructureType",
    description="A PlantItemStructure that is a suitable ParentStructure of am IndustrialComplexIso10209-2012.",
    isAbstract=True,
)
class IndustrialComplexIso10209_2012ParentStructureType(BaseDEXPIObjectType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1285",
    browseName="ns=dexpi;TechnicalItemType",
    displayName="TechnicalItemType",
    description="An item at the lowest level of the plant structure.\nAssociation to ParentStructure (TechnicalItemParentStructure)\nAssociation to PlantTrain (PlantTrain)\nAssociation to PlantSystem (PlantSystem)\nAssociation to AreaIsa95 (AreaIsa95)",
    isAbstract=True,
)
class TechnicalItemType(BaseDEXPIObjectType):
    pass


@o6.objecttype(nodeId="ns=dexpi;i=1290", browseName="ns=dexpi;AreaIsa95Type", displayName="AreaIsa95Type", description="An area as defined by ISA 95.")
class AreaIsa95Type(BaseDEXPIObjectType):
    areaIdentificationCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1291",
            browseName="ns=dexpi;AreaIdentificationCodeAssignmentClass",
            description="The identification code of the AreaIsa95.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    areaNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1292",
            browseName="ns=dexpi;AreaNameAssignmentClass",
            description="The name of the AreaIsa95.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1293",
    browseName="ns=dexpi;PlantSystemLocatedStructureType",
    displayName="PlantSystemLocatedStructureType",
    description="A structure can be located in a PlantSystem.\nAssociation to PlantSystem (PlantSystem)",
    isAbstract=True,
)
class PlantSystemLocatedStructureType(BaseDEXPIObjectType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1295",
    browseName="ns=dexpi;TechnicalItemParentStructureType",
    displayName="TechnicalItemParentStructureType",
    description="A PlantItemStructure that is a suitable ParentStructure of a TechnicalItem.",
    isAbstract=True,
)
class TechnicalItemParentStructureType(BaseDEXPIObjectType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1296",
    browseName="ns=dexpi;PlantSectionIso10209-2012ParentStructureType",
    displayName="PlantSectionIso10209-2012ParentStructureType",
    description="A PlantItemStructure that is a suitable ParentStructure of a PlantSectionIso10209-2012.",
    isAbstract=True,
)
class PlantSectionIso10209_2012ParentStructureType(BaseDEXPIObjectType):
    pass


@o6.objecttype(nodeId="ns=dexpi;i=1297", browseName="ns=dexpi;PlantSystemType", displayName="PlantSystemType", description="A plant system.")
class PlantSystemType(BaseDEXPIObjectType):
    plantSystemIdentificationCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1298",
            browseName="ns=dexpi;PlantSystemIdentificationCodeAssignmentClass",
            description="The identification code of the PlantSystem.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    plantSystemNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1299",
            browseName="ns=dexpi;PlantSystemNameAssignmentClass",
            description="The name of the PlantSystem.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1300",
    browseName="ns=dexpi;ProcessPlantType",
    displayName="ProcessPlantType",
    description="A plant employed in carrying out chemical processes, including the required supporting processes (from http://data.posccaesar.org/rdl/RDS7151859).\nAssociation to ParentStructure (ProcessPlantParentStructure)\nAssociation to AreaIsa95 (AreaIsa95)",
)
class ProcessPlantType(BaseDEXPIObjectType):
    processPlantIdentificationCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1301",
            browseName="ns=dexpi;ProcessPlantIdentificationCodeAssignmentClass",
            description="The identification code of the ProcessPlant.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    processPlantNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1302",
            browseName="ns=dexpi;ProcessPlantNameAssignmentClass",
            description="The name of the ProcessPlant.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=dexpi;i=1305", browseName="ns=dexpi;Isa95EnterpriseType", displayName="Isa95EnterpriseType", description="An enterprise as defined by ISA 95.")
class Isa95EnterpriseType(BaseDEXPIObjectType):
    enterpriseIdentificationCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1306",
            browseName="ns=dexpi;EnterpriseIdentificationCodeAssignmentClass",
            description="The identification code of the Isa95Enterprise.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    enterpriseNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1307",
            browseName="ns=dexpi;EnterpriseNameAssignmentClass",
            description="The name of the Isa95Enterprise.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1308",
    browseName="ns=dexpi;PlantStructureItemType",
    displayName="PlantStructureItemType",
    description="Item of the plant break down structure.",
    isAbstract=True,
)
class PlantStructureItemType(BaseDEXPIObjectType):
    pass


@o6.objecttype(nodeId="ns=dexpi;i=1309", browseName="ns=dexpi;PlantTrainType", displayName="PlantTrainType", description="A plant train.")
class PlantTrainType(BaseDEXPIObjectType):
    plantTrainIdentificationCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1310",
            browseName="ns=dexpi;PlantTrainIdentificationCodeAssignmentClass",
            description="The identification code of the PlantTrain.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    plantTrainNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1311",
            browseName="ns=dexpi;PlantTrainNameAssignmentClass",
            description="The name of the PlantTrain.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1337", browseName="ns=dexpi;TaggedPlantItemType", displayName="TaggedPlantItemType", description="A fully tagged item in a plant.", isAbstract=True
)
class TaggedPlantItemType(BaseDEXPIObjectType):
    tagNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1338",
            browseName="ns=dexpi;TagNameAssignmentClass",
            description="The tag number of the TaggedPlantItem. See also <owner.TagNamePrefixAssignmentClass>, <owner.TagNameSequenceNumberAssignmentClass>, and <owner.TagNameSuffixAssignmentClass>.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    tagNamePrefixAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1339",
            browseName="ns=dexpi;TagNamePrefixAssignmentClass",
            description='The prefix part of the tag number of the TaggedPlantItem. For example, the prefix of the tag number "P4714-A" is "P". The prefix often indicates the type of the equipment item, e.g., "P" can indicate a pump. See also <owner.TagNameAssignmentClass>.',
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    tagNameSequenceNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1340",
            browseName="ns=dexpi;TagNameSequenceNumberAssignmentClass",
            description='The sequence number part of the tag number of the TaggedPlantItem. For example, the sequence number of the tag number "P4714-A" is "4714".',
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    tagNameSuffixAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1341",
            browseName="ns=dexpi;TagNameSuffixAssignmentClass",
            description='The suffix part of the tag number of an TaggedPlantItem item. For example, the suffix of the tag number "P4714-A" is "A".',
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=dexpi;i=1370", browseName="ns=dexpi;ColumnPackingsArrangementType", displayName="ColumnPackingsArrangementType", description="The packings of a column.")
class ColumnPackingsArrangementType(BaseDEXPIObjectType):
    height: ns0.vartypes.AnalogUnitType | None
    materialOfConstructionCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1374",
            browseName="ns=dexpi;MaterialOfConstructionCodeAssignmentClass",
            description="A code that gives the material of construction of the ColumnPackingsArrangement.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    numberOfPackings: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1375",
            browseName="ns=dexpi;NumberOfPackings",
            description="The number of packings in the ColumnPackingsArrangement.",
            dataType=o6.Int64,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    packingTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1376",
            browseName="ns=dexpi;PackingTypeAssignmentClass",
            description="The type of the packings in the ColumnPackingsArrangement.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1456",
    browseName="ns=dexpi;FilterUnitType",
    displayName="FilterUnitType",
    description="The filtering unit as part of a filter.\nAssociation to Chamber (Chamber)",
)
class FilterUnitType(BaseDEXPIObjectType):
    efficiency: ns0.vartypes.AnalogUnitType | None
    filterArea: ns0.vartypes.AnalogUnitType | None
    lowerLimitAllowableSolidsConcentration: ns0.vartypes.AnalogUnitType | None
    lowerLimitPermeableParticleDiameter: ns0.vartypes.AnalogUnitType | None
    materialOfConstructionCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1470",
            browseName="ns=dexpi;MaterialOfConstructionCodeAssignmentClass",
            description="A code that gives the material of construction of the FilterUnit.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    numberOfFilterElements: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1471",
            browseName="ns=dexpi;NumberOfFilterElements",
            description="The number of filter elements in the FilterUnit.",
            dataType=o6.Int64,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    upperLimitAllowableSolidsConcentration: ns0.vartypes.AnalogUnitType | None
    upperLimitPermeableParticleDiameter: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=dexpi;i=1489",
    browseName="ns=dexpi;ColumnInternalsArrangementType",
    displayName="ColumnInternalsArrangementType",
    description="The internals of a column.",
    isAbstract=True,
)
class ColumnInternalsArrangementType(BaseDEXPIObjectType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1491",
    browseName="ns=dexpi;HeatExchangerRotorType",
    displayName="HeatExchangerRotorType",
    description="A heat exchanger rotor.\nAssociation to Chamber (Chamber)",
)
class HeatExchangerRotorType(BaseDEXPIObjectType):
    materialOfConstructionCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1492",
            browseName="ns=dexpi;MaterialOfConstructionCodeAssignmentClass",
            description="A code that gives the material of construction of the HeatExchangerRotor.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=dexpi;i=1502", browseName="ns=dexpi;PumpEquipmentType", displayName="PumpEquipmentType", description="Equipment of a Pump.", isAbstract=True)
class PumpEquipmentType(BaseDEXPIObjectType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1523",
    browseName="ns=dexpi;ChamberType",
    displayName="ChamberType",
    description="A physical object that is an enclosed space (from http://data.posccaesar.org/rdl/RDS903151421).",
)
class ChamberType(BaseDEXPIObjectType):
    chamberDescriptionAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1525",
            browseName="ns=dexpi;ChamberDescriptionAssignmentClass",
            description="The description of the Chamber.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    chamberFunctionAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1526",
            browseName="ns=dexpi;ChamberFunctionAssignmentClass",
            description="The function of the Chamber.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    chamberFunctionSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1527",
            browseName="ns=dexpi;ChamberFunctionSpecialization",
            description="A specialization indicating the function of the Chamber.",
            dataType=dexpi_datypes.ChamberFunctionClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    height: ns0.vartypes.AnalogUnitType | None
    insideDiameter: ns0.vartypes.AnalogUnitType | None
    length: ns0.vartypes.AnalogUnitType | None
    lowerLimitDesignPressure: ns0.vartypes.AnalogUnitType | None
    lowerLimitDesignTemperature: ns0.vartypes.AnalogUnitType | None
    materialOfConstructionCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1543",
            browseName="ns=dexpi;MaterialOfConstructionCodeAssignmentClass",
            description="A code that gives the material of construction of the Chamber.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    nominalDiameter: ns0.vartypes.AnalogUnitType | None
    nominalDiameterTypeRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1547",
            browseName="ns=dexpi;NominalDiameterTypeRepresentationAssignmentClass",
            description="A readable representation of the type of the nominal diameter of the Chamber. The purpose of this value is to give a textual representation of the nominal diameter to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    subTagNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1524",
            browseName="ns=dexpi;SubTagNameAssignmentClass",
            description="The sub tag name of the Chamber.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    upperLimitDesignPressure: ns0.vartypes.AnalogUnitType | None
    upperLimitDesignTemperature: ns0.vartypes.AnalogUnitType | None
    width: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=dexpi;i=1562",
    browseName="ns=dexpi;MixingElementAssemblyType",
    displayName="MixingElementAssemblyType",
    description="Assembly of mixing elements as part of a mixer.\nAssociation to Chamber (Chamber)",
)
class MixingElementAssemblyType(BaseDEXPIObjectType):
    materialOfConstructionCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1564",
            browseName="ns=dexpi;MaterialOfConstructionCodeAssignmentClass",
            description="A code that gives the material of construction of the MixingElementAssembly.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    mixingElementAssembly: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1565",
            browseName="ns=dexpi;MixingElementAssembly",
            description="The number of mixing elements in the MixingElementAssembly.",
            dataType=o6.Int64,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1592",
    browseName="ns=dexpi;TubeBundleType",
    displayName="TubeBundleType",
    description="A bundle that consists of several tubes assembled together allowing multiple flow paths from a single source (from http://data.posccaesar.org/rdl/RDS415259).\nAssociation to Chamber (Chamber)",
)
class TubeBundleType(BaseDEXPIObjectType):
    numberOfTubes: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1593", browseName="ns=dexpi;NumberOfTubes", description="The number of tubes of the TubeBundle.", dataType=o6.Int64, accessLevel=3, userAccessLevel=1
        )
    )
    tubeLength: ns0.vartypes.AnalogUnitType | None
    tubeMaterialOfConstructionCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1597",
            browseName="ns=dexpi;TubeMaterialOfConstructionCodeAssignmentClass",
            description="A code that gives the material of construction of the tubes of the TubeBundle.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    tubeNominalDiameterNumericalValueRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1598",
            browseName="ns=dexpi;TubeNominalDiameterNumericalValueRepresentationAssignmentClass",
            description="A readable representation of the numerical value of the nominal diameter of the tubes. The purpose of this value is to give a textual representation of the nominal diameter to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    tubeNominalDiameterRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1599",
            browseName="ns=dexpi;TubeNominalDiameterRepresentationAssignmentClass",
            description="A readable representation of the nominal diameter of the tubes. The purpose of this value is to give a textual representation of the nominal diameter to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    tubeNominalDiameterStandardSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1600",
            browseName="ns=dexpi;TubeNominalDiameterStandardSpecialization",
            description="The nominal diameter of the tubes, given as a reference to a nominal diameter standard and value.",
            dataType=dexpi_datypes.NominalDiameterStandardClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    tubeNominalDiameterTypeRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1601",
            browseName="ns=dexpi;TubeNominalDiameterTypeRepresentationAssignmentClass",
            description="A readable representation of the type of the nominal diameter of the tubes. The purpose of this value is to give a textual representation of the nominal diameter to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=dexpi;i=1603", browseName="ns=dexpi;ColumnTraysArrangementType", displayName="ColumnTraysArrangementType", description="The trays of a column.")
class ColumnTraysArrangementType(BaseDEXPIObjectType):
    materialOfConstructionCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1604",
            browseName="ns=dexpi;MaterialOfConstructionCodeAssignmentClass",
            description="A code that gives the material of construction of the ColumnTraysArrangement.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    numberOfTrays: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1605",
            browseName="ns=dexpi;NumberOfTrays",
            description="The number of trays in the ColumnTraysArrangement.",
            dataType=o6.Int64,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    trayTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1606",
            browseName="ns=dexpi;TrayTypeAssignmentClass",
            description="The type of the trays in the ColumnTraysArrangement.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1629",
    browseName="ns=dexpi;ImpellerType",
    displayName="ImpellerType",
    description="A physical object that is an assembly of rotating vanes within an enclosure which is used to impart energy to or derive energy from a fluid through dynamic force (from http://data.posccaesar.org/rdl/RDS414539).\nAssociation to Chamber (Chamber)",
)
class ImpellerType(BaseDEXPIObjectType):
    diameter: ns0.vartypes.AnalogUnitType | None
    materialOfConstructionCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1633",
            browseName="ns=dexpi;MaterialOfConstructionCodeAssignmentClass",
            description="A code that gives the material of construction of the Impeller.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    stageIdentifierAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1634",
            browseName="ns=dexpi;StageIdentifierAssignmentClass",
            description="The stage identfifier of of the Impeller.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1636", browseName="ns=dexpi;CompressorEquipmentType", displayName="CompressorEquipmentType", description="Equipment of a Compressor.", isAbstract=True
)
class CompressorEquipmentType(BaseDEXPIObjectType):
    pass


@o6.objecttype(nodeId="ns=dexpi;i=1656", browseName="ns=dexpi;DisplacerType", displayName="DisplacerType", description="A displacer.\nAssociation to Chamber (Chamber)")
class DisplacerType(BaseDEXPIObjectType):
    materialOfConstructionCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1657",
            browseName="ns=dexpi;MaterialOfConstructionCodeAssignmentClass",
            description="A code that gives the material of construction of the Displacer.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    stageIdentifierAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1658",
            browseName="ns=dexpi;StageIdentifierAssignmentClass",
            description="The stage identfifier of of the Displacer.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    volumePerStroke: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=dexpi;i=1672", browseName="ns=dexpi;AgitatorRotorType", displayName="AgitatorRotorType", description="An agitator rotor.\nAssociation to Chamber (Chamber)"
)
class AgitatorRotorType(BaseDEXPIObjectType):
    diameter: ns0.vartypes.AnalogUnitType | None
    lengthToMountingFlange: ns0.vartypes.AnalogUnitType | None
    materialOfConstructionCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1679",
            browseName="ns=dexpi;MaterialOfConstructionCodeAssignmentClass",
            description="A code that gives the material of construction of the AgitatorRotor.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    rotorTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1680",
            browseName="ns=dexpi;RotorTypeAssignmentClass",
            description="The rotor type of the AgitatorRotor.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1754",
    browseName="ns=dexpi;PipingNetworkSegmentItemType",
    displayName="PipingNetworkSegmentItemType",
    description="An item that can be part of a PipingNetworkSegment.",
    isAbstract=True,
)
class PipingNetworkSegmentItemType(BaseDEXPIObjectType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1757",
    browseName="ns=dexpi;StrainerType",
    displayName="StrainerType",
    description="A mechanical separator that is separating solid particles from a fluid by passing the fluid through a wire mesh, screen or metal plates containing perforations or slits (from http://data.posccaesar.org/rdl/RDS422504).",
)
class StrainerType(BaseDEXPIObjectType):
    heatTracingTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1762",
            browseName="ns=dexpi;HeatTracingTypeAssignmentClass",
            description="The heat tracing type related to the PipeFitting, represented as a string.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    heatTracingTypeSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1763",
            browseName="ns=dexpi;HeatTracingTypeSpecialization",
            description="A specialization indicating the heat tracing type related to the PipeFitting.",
            dataType=dexpi_datypes.HeatTracingTypeClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    insulationThickness: ns0.vartypes.AnalogUnitType | None
    insulationTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1767",
            browseName="ns=dexpi;InsulationTypeAssignmentClass",
            description="The identification code for the insulation type related to the PipeFitting. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    lowerLimitHeatTracingTemperature: ns0.vartypes.AnalogUnitType | None
    pipingClassCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1768",
            browseName="ns=dexpi;PipingClassCodeAssignmentClass",
            description="The identification code of the piping class of the PipeFitting. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingComponentNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1769",
            browseName="ns=dexpi;PipingComponentNameAssignmentClass",
            description="The piping component name of the PipeFitting.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingComponentNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1758",
            browseName="ns=dexpi;PipingComponentNumberAssignmentClass",
            description="The piping component number of the PipeFitting.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1807",
    browseName="ns=dexpi;PipingSourceItemType",
    displayName="PipingSourceItemType",
    description="An item that can be the source of a PipingConnection (attribute SourceItem) or a PipingNetworkSegment (attribute SourceItem).",
    isAbstract=True,
)
class PipingSourceItemType(BaseDEXPIObjectType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1812",
    browseName="ns=dexpi;SteamTrapType",
    displayName="SteamTrapType",
    description="A trap that consists of a chamber into which condensed steam from steam pipes etc. is allowed to drain, and which automatically ejects it without permitting the escape of steam (from http://data.posccaesar.org/rdl/RDS5782388).",
)
class SteamTrapType(BaseDEXPIObjectType):
    heatTracingTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1817",
            browseName="ns=dexpi;HeatTracingTypeAssignmentClass",
            description="The heat tracing type related to the PipeFitting, represented as a string.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    heatTracingTypeSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1818",
            browseName="ns=dexpi;HeatTracingTypeSpecialization",
            description="A specialization indicating the heat tracing type related to the PipeFitting.",
            dataType=dexpi_datypes.HeatTracingTypeClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    insulationThickness: ns0.vartypes.AnalogUnitType | None
    insulationTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1822",
            browseName="ns=dexpi;InsulationTypeAssignmentClass",
            description="The identification code for the insulation type related to the PipeFitting. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    lowerLimitHeatTracingTemperature: ns0.vartypes.AnalogUnitType | None
    pipingClassCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1823",
            browseName="ns=dexpi;PipingClassCodeAssignmentClass",
            description="The identification code of the piping class of the PipeFitting. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingComponentNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1824",
            browseName="ns=dexpi;PipingComponentNameAssignmentClass",
            description="The piping component name of the PipeFitting.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingComponentNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1813",
            browseName="ns=dexpi;PipingComponentNumberAssignmentClass",
            description="The piping component number of the PipeFitting.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1826",
    browseName="ns=dexpi;PipingTargetItemType",
    displayName="PipingTargetItemType",
    description="An item that can be the target of a PipingConnection (attribute TargetItem) or a PipingNetworkSegment (attribute TargetItem).",
    isAbstract=True,
)
class PipingTargetItemType(BaseDEXPIObjectType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1832",
    browseName="ns=dexpi;SilencerType",
    displayName="SilencerType",
    description="A device intended to reduce a noise level (from http://data.posccaesar.org/rdl/RDS1049368591).",
)
class SilencerType(BaseDEXPIObjectType):
    heatTracingTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1837",
            browseName="ns=dexpi;HeatTracingTypeAssignmentClass",
            description="The heat tracing type related to the PipeFitting, represented as a string.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    heatTracingTypeSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1838",
            browseName="ns=dexpi;HeatTracingTypeSpecialization",
            description="A specialization indicating the heat tracing type related to the PipeFitting.",
            dataType=dexpi_datypes.HeatTracingTypeClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    insulationThickness: ns0.vartypes.AnalogUnitType | None
    insulationTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1842",
            browseName="ns=dexpi;InsulationTypeAssignmentClass",
            description="The identification code for the insulation type related to the PipeFitting. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    lowerLimitHeatTracingTemperature: ns0.vartypes.AnalogUnitType | None
    pipingClassCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1843",
            browseName="ns=dexpi;PipingClassCodeAssignmentClass",
            description="The identification code of the piping class of the PipeFitting. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingComponentNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1844",
            browseName="ns=dexpi;PipingComponentNameAssignmentClass",
            description="The piping component name of the PipeFitting.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingComponentNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1833",
            browseName="ns=dexpi;PipingComponentNumberAssignmentClass",
            description="The piping component number of the PipeFitting.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1860",
    browseName="ns=dexpi;DirectPipingConnectionType",
    displayName="DirectPipingConnectionType",
    description="A direct connection between two piping items, i.e. a connection that is not realized by a pipe.\nAssociation to SourceItem (PipingSourceItem)\nAssociation to TargetItem (PipingTargetItem)\nAssociation to SourceNode (PipingNode)\nAssociation to TargetNode (PipingNode)",
)
class DirectPipingConnectionType(BaseDEXPIObjectType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1890",
    browseName="ns=dexpi;PipeType",
    displayName="PipeType",
    description="An elementary piece of piping, i.e., not interrupted by any item.\nAssociation to SourceItem (PipingSourceItem)\nAssociation to TargetItem (PipingTargetItem)\nAssociation to SourceNode (PipingNode)\nAssociation to TargetNode (PipingNode)",
)
class PipeType(BaseDEXPIObjectType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1958",
    browseName="ns=dexpi;VentilationDeviceType",
    displayName="VentilationDeviceType",
    description="A 'device' that allows gas or vapour to leave a container under excess pressure (from http://data.posccaesar.org/rdl/RDS1049335351).",
)
class VentilationDeviceType(BaseDEXPIObjectType):
    heatTracingTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1963",
            browseName="ns=dexpi;HeatTracingTypeAssignmentClass",
            description="The heat tracing type related to the PipeFitting, represented as a string.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    heatTracingTypeSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1964",
            browseName="ns=dexpi;HeatTracingTypeSpecialization",
            description="A specialization indicating the heat tracing type related to the PipeFitting.",
            dataType=dexpi_datypes.HeatTracingTypeClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    insulationThickness: ns0.vartypes.AnalogUnitType | None
    insulationTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1968",
            browseName="ns=dexpi;InsulationTypeAssignmentClass",
            description="The identification code for the insulation type related to the PipeFitting. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    lowerLimitHeatTracingTemperature: ns0.vartypes.AnalogUnitType | None
    pipingClassCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1969",
            browseName="ns=dexpi;PipingClassCodeAssignmentClass",
            description="The identification code of the piping class of the PipeFitting. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingComponentNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1970",
            browseName="ns=dexpi;PipingComponentNameAssignmentClass",
            description="The piping component name of the PipeFitting.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingComponentNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1959",
            browseName="ns=dexpi;PipingComponentNumberAssignmentClass",
            description="The piping component number of the PipeFitting.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1976",
    browseName="ns=dexpi;OrificePlateType",
    displayName="OrificePlateType",
    description="An 'artefact' that is a thin plate with a specified hole in the middle. It is usually placed in a pipe to measure the rate of fluid flow (from http://data.posccaesar.org/rdl/RDS418364).",
)
class OrificePlateType(BaseDEXPIObjectType):
    heatTracingTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1981",
            browseName="ns=dexpi;HeatTracingTypeAssignmentClass",
            description="The heat tracing type related to the PipeFitting, represented as a string.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    heatTracingTypeSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1982",
            browseName="ns=dexpi;HeatTracingTypeSpecialization",
            description="A specialization indicating the heat tracing type related to the PipeFitting.",
            dataType=dexpi_datypes.HeatTracingTypeClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    insulationThickness: ns0.vartypes.AnalogUnitType | None
    insulationTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1986",
            browseName="ns=dexpi;InsulationTypeAssignmentClass",
            description="The identification code for the insulation type related to the PipeFitting. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    lowerLimitHeatTracingTemperature: ns0.vartypes.AnalogUnitType | None
    pipingClassCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1987",
            browseName="ns=dexpi;PipingClassCodeAssignmentClass",
            description="The identification code of the piping class of the PipeFitting. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingComponentNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1988",
            browseName="ns=dexpi;PipingComponentNameAssignmentClass",
            description="The piping component name of the PipeFitting.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingComponentNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1977",
            browseName="ns=dexpi;PipingComponentNumberAssignmentClass",
            description="The piping component number of the PipeFitting.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1989",
    browseName="ns=dexpi;PipingConnectionType",
    displayName="PipingConnectionType",
    description="An elementary connection between two piping items.\nAssociation to SourceItem (PipingSourceItem)\nAssociation to TargetItem (PipingTargetItem)\nAssociation to SourceNode (PipingNode)\nAssociation to TargetNode (PipingNode)",
    isAbstract=True,
)
class PipingConnectionType(BaseDEXPIObjectType):
    pass


@o6.objecttype(nodeId="ns=dexpi;i=2008", browseName="ns=dexpi;PipingNodeType", displayName="PipingNodeType", description="A possible connection point for a PipingConnection.")
class PipingNodeType(BaseDEXPIObjectType):
    nodeFlowSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=2009",
            browseName="ns=dexpi;NodeFlowSpecialization",
            description="A classification of the flow direction in the PipingNode with respect to its PipingNodeOwner.",
            dataType=dexpi_datypes.NodeFlowClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    nominalDiameterNumericalValueRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=2010",
            browseName="ns=dexpi;NominalDiameterNumericalValueRepresentationAssignmentClass",
            description="A readable representation of the numerical value of the nominal diameter of the PipingNode. The purpose of this value is to give a textual representation of the nominal diameter to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    nominalDiameterRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=2011",
            browseName="ns=dexpi;NominalDiameterRepresentationAssignmentClass",
            description="A readable representation of the nominal diameter of the PipingNode. The purpose of this value is to give a textual representation of the nominal diameter to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    nominalDiameterStandardSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=2012",
            browseName="ns=dexpi;NominalDiameterStandardSpecialization",
            description="The nominal diameter of the PipingNode, given as a reference to a nominal  diameter standard and value.",
            dataType=dexpi_datypes.NominalDiameterStandardClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    nominalDiameterTypeRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=2013",
            browseName="ns=dexpi;NominalDiameterTypeRepresentationAssignmentClass",
            description="A readable representation of the type of the nominal diameter of the PipingNode. The purpose of this value is to give a textual representation of the nominal diameter to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=dexpi;i=2014", browseName="ns=dexpi;RotationalSpeedType", displayName="RotationalSpeedType")
class RotationalSpeedType(BaseDEXPIObjectType):
    unit: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2015", browseName="ns=dexpi;Unit", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
    )
    value: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2017", browseName="ns=dexpi;Value", dataType=o6.Double, value=0.0, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=dexpi;i=2018", browseName="ns=dexpi;HeatTransferCoefficientType", displayName="HeatTransferCoefficientType")
class HeatTransferCoefficientType(BaseDEXPIObjectType):
    unit: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2019", browseName="ns=dexpi;Unit", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
    )
    value: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2021", browseName="ns=dexpi;Value", dataType=o6.Double, value=0.0, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=dexpi;i=2022", browseName="ns=dexpi;TemperatureType", displayName="TemperatureType")
class TemperatureType(BaseDEXPIObjectType):
    unit: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2023", browseName="ns=dexpi;Unit", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
    )
    value: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2025", browseName="ns=dexpi;Value", dataType=o6.Double, value=0.0, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=dexpi;i=2026", browseName="ns=dexpi;PhysicalQuantityType", displayName="PhysicalQuantityType", isAbstract=True)
class PhysicalQuantityType(BaseDEXPIObjectType):
    value: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2028", browseName="ns=dexpi;Value", dataType=o6.Double, value=0.0, accessLevel=3, userAccessLevel=1)
    )


o6.reference(RotationalSpeedType, "ns=dexpi;i=1059", PhysicalQuantityType)
o6.reference(HeatTransferCoefficientType, "ns=dexpi;i=1059", PhysicalQuantityType)
o6.reference(TemperatureType, "ns=dexpi;i=1059", PhysicalQuantityType)


@o6.objecttype(nodeId="ns=dexpi;i=2029", browseName="ns=dexpi;AreaType", displayName="AreaType")
class AreaType(BaseDEXPIObjectType):
    unit: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2030", browseName="ns=dexpi;Unit", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
    )
    value: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2032", browseName="ns=dexpi;Value", dataType=o6.Double, value=0.0, accessLevel=3, userAccessLevel=1)
    )


o6.reference(AreaType, "ns=dexpi;i=1059", PhysicalQuantityType)


@o6.objecttype(nodeId="ns=dexpi;i=2033", browseName="ns=dexpi;VolumeFlowRateType", displayName="VolumeFlowRateType")
class VolumeFlowRateType(BaseDEXPIObjectType):
    unit: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2034", browseName="ns=dexpi;Unit", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
    )
    value: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2036", browseName="ns=dexpi;Value", dataType=o6.Double, value=0.0, accessLevel=3, userAccessLevel=1)
    )


o6.reference(VolumeFlowRateType, "ns=dexpi;i=1059", PhysicalQuantityType)


@o6.objecttype(nodeId="ns=dexpi;i=2037", browseName="ns=dexpi;PowerType", displayName="PowerType")
class PowerType(BaseDEXPIObjectType):
    unit: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2038", browseName="ns=dexpi;Unit", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
    )
    value: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2040", browseName="ns=dexpi;Value", dataType=o6.Double, value=0.0, accessLevel=3, userAccessLevel=1)
    )


o6.reference(PowerType, "ns=dexpi;i=1059", PhysicalQuantityType)


@o6.objecttype(nodeId="ns=dexpi;i=2041", browseName="ns=dexpi;LengthType", displayName="LengthType")
class LengthType(BaseDEXPIObjectType):
    unit: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2042", browseName="ns=dexpi;Unit", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
    )
    value: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2044", browseName="ns=dexpi;Value", dataType=o6.Double, value=0.0, accessLevel=3, userAccessLevel=1)
    )


o6.reference(LengthType, "ns=dexpi;i=1059", PhysicalQuantityType)


@o6.objecttype(nodeId="ns=dexpi;i=2045", browseName="ns=dexpi;PercentageType", displayName="PercentageType")
class PercentageType(BaseDEXPIObjectType):
    unit: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2046", browseName="ns=dexpi;Unit", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
    )
    value: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2048", browseName="ns=dexpi;Value", dataType=o6.Double, value=0.0, accessLevel=3, userAccessLevel=1)
    )


o6.reference(PercentageType, "ns=dexpi;i=1059", PhysicalQuantityType)


@o6.objecttype(nodeId="ns=dexpi;i=2049", browseName="ns=dexpi;VolumeType", displayName="VolumeType")
class VolumeType(BaseDEXPIObjectType):
    unit: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2050", browseName="ns=dexpi;Unit", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
    )
    value: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2052", browseName="ns=dexpi;Value", dataType=o6.Double, value=0.0, accessLevel=3, userAccessLevel=1)
    )


o6.reference(VolumeType, "ns=dexpi;i=1059", PhysicalQuantityType)


@o6.objecttype(nodeId="ns=dexpi;i=2053", browseName="ns=dexpi;MassType", displayName="MassType")
class MassType(BaseDEXPIObjectType):
    unit: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2054", browseName="ns=dexpi;Unit", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
    )
    value: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2056", browseName="ns=dexpi;Value", dataType=o6.Double, value=0.0, accessLevel=3, userAccessLevel=1)
    )


o6.reference(MassType, "ns=dexpi;i=1059", PhysicalQuantityType)


@o6.objecttype(nodeId="ns=dexpi;i=2057", browseName="ns=dexpi;PressureType", displayName="PressureType")
class PressureType(BaseDEXPIObjectType):
    unit: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2058", browseName="ns=dexpi;Unit", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
    )
    value: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2060", browseName="ns=dexpi;Value", dataType=o6.Double, value=0.0, accessLevel=3, userAccessLevel=1)
    )


o6.reference(PressureType, "ns=dexpi;i=1059", PhysicalQuantityType)


@o6.objecttype(nodeId="ns=dexpi;i=2061", browseName="ns=dexpi;AngleType", displayName="AngleType")
class AngleType(BaseDEXPIObjectType):
    unit: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2062", browseName="ns=dexpi;Unit", dataType=o6.String, value="", accessLevel=3, userAccessLevel=1)
    )
    value: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=dexpi;i=2064", browseName="ns=dexpi;Value", dataType=o6.Double, value=0.0, accessLevel=3, userAccessLevel=1)
    )


o6.reference(AngleType, "ns=dexpi;i=1059", PhysicalQuantityType)


@o6.objecttype(
    nodeId="ns=dexpi;i=1118",
    browseName="ns=dexpi;ProcessSignalGeneratingSystemType",
    displayName="ProcessSignalGeneratingSystemType",
    description="An assembly of artefacts that is designed to fulfill one or more ProcessSignalGeneratingFunctions.\nAssociation to ParentStructure (TechnicalItemParentStructure)\nAssociation to PlantTrain (PlantTrain)\nAssociation to PlantSystem (PlantSystem)\nAssociation to AreaIsa95 (AreaIsa95)",
)
class ProcessSignalGeneratingSystemType(BaseDEXPIObjectType):
    langlePrimaryElementRangle: PrimaryElementType | None = o6.hasComponent(
        PrimaryElementType(
            nodeId="ns=dexpi;i=2074", browseName="ns=dexpi;<PrimaryElement>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )
    langleTransmitterRangle: TransmitterType | None = o6.hasComponent(
        TransmitterType(
            nodeId="ns=dexpi;i=2075", browseName="ns=dexpi;<Transmitter>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )
    processSignalGeneratingSystemNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1119",
            browseName="ns=dexpi;ProcessSignalGeneratingSystemNumberAssignmentClass",
            description="The number of the ProcessSignalGeneratingSystem",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    typicalInformationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1120",
            browseName="ns=dexpi;TypicalInformationAssignmentClass",
            description="Typical information about the ProcessSignalGeneratingSystem.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1130",
    browseName="ns=dexpi;ProcessInstrumentationFunctionType",
    displayName="ProcessInstrumentationFunctionType",
    description="A requirement for instrumentation and/or control structures relating to Process Engineering.\nAssociation to ParentStructure (TechnicalItemParentStructure)\nAssociation to PlantTrain (PlantTrain)\nAssociation to PlantSystem (PlantSystem)\nAssociation to AreaIsa95 (AreaIsa95)",
)
class ProcessInstrumentationFunctionType(BaseDEXPIObjectType):
    deviceInformationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1132",
            browseName="ns=dexpi;DeviceInformationAssignmentClass",
            description="Device information the ProcessInstrumentationFunction, e.g., for a detector.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    gmpRelevanceSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1133",
            browseName="ns=dexpi;GmpRelevanceSpecialization",
            description="A classification indicating if the ProcessInstrumentationFunction is relevant for GMP (good manufacturing practise).",
            dataType=dexpi_datypes.GmpRelevanceClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    guaranteedSupplyFunctionSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1134",
            browseName="ns=dexpi;GuaranteedSupplyFunctionSpecialization",
            description="A classification indicating if the ProcessInstrumentationFunction is a guaranteed supply function.",
            dataType=dexpi_datypes.GuaranteedSupplyFunctionClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langleActuatingFunctionRangle: ActuatingFunctionType | None = o6.hasComponent(
        ActuatingFunctionType(
            nodeId="ns=dexpi;i=2076",
            browseName="ns=dexpi;<ActuatingFunction>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
        )
    )
    langleProcessSignalGeneratingFunctionRangle: ProcessSignalGeneratingFunctionType | None = o6.hasComponent(
        ProcessSignalGeneratingFunctionType(
            nodeId="ns=dexpi;i=2077",
            browseName="ns=dexpi;<ProcessSignalGeneratingFunction>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
        )
    )
    langleSignalConveyingFunctionRangle: SignalConveyingFunctionType | None = o6.hasComponent(
        SignalConveyingFunctionType(
            nodeId="ns=dexpi;i=2078",
            browseName="ns=dexpi;<SignalConveyingFunction>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
        )
    )
    locationSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1135",
            browseName="ns=dexpi;LocationSpecialization",
            description="A specialization indicating the location of the ProcessInstrumentationFunction.",
            dataType=dexpi_datypes.LocationClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    panelIdentificationCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1136",
            browseName="ns=dexpi;PanelIdentificationCodeAssignmentClass",
            description="The panel identification code of the ProcessInstrumentationFunction.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    processInstrumentationFunctionCategoryAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1138",
            browseName="ns=dexpi;ProcessInstrumentationFunctionCategoryAssignmentClass",
            description="The function category of the ProcessInstrumentationFunction. The value is a string, typically one or two letters. Recent standards for PIDs normally enforce a single letter from a fixed list. However, there are no formal DEXPI restrictions for valid strings.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    processInstrumentationFunctionModifierAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1139",
            browseName="ns=dexpi;ProcessInstrumentationFunctionModifierAssignmentClass",
            description="The modifier of the ProcessInstrumentationFunction. The value is a string, typically a single letter, e.g., D for difference. So far, there are no formal DEXPI restrictions for valid strings.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    processInstrumentationFunctionNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1131",
            browseName="ns=dexpi;ProcessInstrumentationFunctionNumberAssignmentClass",
            description="A unique identifier for the ProcessInstrumentationFunction. If the ProcessInstrumentationFunction is part of a InstrumentationLoopFunction, the identifier of the ProcessInstrumentationFunction usually contains the identifier of the InstrumentationLoopFunction (see InstrumentationLoopFunctionNumberAssignmentClass).",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    processInstrumentationFunctionsAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1137",
            browseName="ns=dexpi;ProcessInstrumentationFunctionsAssignmentClass",
            description="Additional functions of the ProcessInstrumentationFunction (i.e., in addition to the function category, see  ProcessInstrumentationFunctionCategoryAssignmentClass).",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    qualityRelevanceSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1140",
            browseName="ns=dexpi;QualityRelevanceSpecialization",
            description="A classification indicating if the ProcessInstrumentationFunction is quality relevant.",
            dataType=dexpi_datypes.QualityRelevanceClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    safetyRelevanceClassAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1141",
            browseName="ns=dexpi;SafetyRelevanceClassAssignmentClass",
            description="The safety relevance class the ProcessInstrumentationFunction.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    typicalInformationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1142",
            browseName="ns=dexpi;TypicalInformationAssignmentClass",
            description="Typical information about the ProcessInstrumentationFunction.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    vendorCompanyNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1143",
            browseName="ns=dexpi;VendorCompanyNameAssignmentClass",
            description="The vendor company name the ProcessInstrumentationFunction.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    votingSystemRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1144",
            browseName="ns=dexpi;VotingSystemRepresentationAssignmentClass",
            description="A representation of the voting system of the ProcessInstrumentationFunction.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1152",
    browseName="ns=dexpi;ProcessControlFunctionType",
    displayName="ProcessControlFunctionType",
    description="A requirement for control structures relating to Process Engineering.\nAssociation to ParentStructure (TechnicalItemParentStructure)\nAssociation to PlantTrain (PlantTrain)\nAssociation to PlantSystem (PlantSystem)\nAssociation to AreaIsa95 (AreaIsa95)",
)
class ProcessControlFunctionType(BaseDEXPIObjectType):
    deviceInformationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1154",
            browseName="ns=dexpi;DeviceInformationAssignmentClass",
            description="Device information the ProcessInstrumentationFunction, e.g., for a detector.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    gmpRelevanceSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1155",
            browseName="ns=dexpi;GmpRelevanceSpecialization",
            description="A classification indicating if the ProcessInstrumentationFunction is relevant for GMP (good manufacturing practise).",
            dataType=dexpi_datypes.GmpRelevanceClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    guaranteedSupplyFunctionSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1156",
            browseName="ns=dexpi;GuaranteedSupplyFunctionSpecialization",
            description="A classification indicating if the ProcessInstrumentationFunction is a guaranteed supply function.",
            dataType=dexpi_datypes.GuaranteedSupplyFunctionClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langleActuatingFunctionRangle: ActuatingFunctionType | None = o6.hasComponent(
        ActuatingFunctionType(
            nodeId="ns=dexpi;i=2079",
            browseName="ns=dexpi;<ActuatingFunction>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
        )
    )
    langleProcessSignalGeneratingFunctionRangle: ProcessSignalGeneratingFunctionType | None = o6.hasComponent(
        ProcessSignalGeneratingFunctionType(
            nodeId="ns=dexpi;i=2080",
            browseName="ns=dexpi;<ProcessSignalGeneratingFunction>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
        )
    )
    langleSignalConveyingFunctionRangle: SignalConveyingFunctionType | None = o6.hasComponent(
        SignalConveyingFunctionType(
            nodeId="ns=dexpi;i=2081",
            browseName="ns=dexpi;<SignalConveyingFunction>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
        )
    )
    locationSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1157",
            browseName="ns=dexpi;LocationSpecialization",
            description="A specialization indicating the location of the ProcessInstrumentationFunction.",
            dataType=dexpi_datypes.LocationClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    panelIdentificationCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1158",
            browseName="ns=dexpi;PanelIdentificationCodeAssignmentClass",
            description="The panel identification code of the ProcessInstrumentationFunction.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    processInstrumentationFunctionCategoryAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1160",
            browseName="ns=dexpi;ProcessInstrumentationFunctionCategoryAssignmentClass",
            description="The function category of the ProcessInstrumentationFunction. The value is a string, typically one or two letters. Recent standards for PIDs normally enforce a single letter from a fixed list. However, there are no formal DEXPI restrictions for valid strings.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    processInstrumentationFunctionModifierAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1161",
            browseName="ns=dexpi;ProcessInstrumentationFunctionModifierAssignmentClass",
            description="The modifier of the ProcessInstrumentationFunction. The value is a string, typically a single letter, e.g., D for difference. So far, there are no formal DEXPI restrictions for valid strings.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    processInstrumentationFunctionNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1153",
            browseName="ns=dexpi;ProcessInstrumentationFunctionNumberAssignmentClass",
            description="A unique identifier for the ProcessInstrumentationFunction. If the ProcessInstrumentationFunction is part of a InstrumentationLoopFunction, the identifier of the ProcessInstrumentationFunction usually contains the identifier of the InstrumentationLoopFunction (see InstrumentationLoopFunctionNumberAssignmentClass).",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    processInstrumentationFunctionsAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1159",
            browseName="ns=dexpi;ProcessInstrumentationFunctionsAssignmentClass",
            description="Additional functions of the ProcessInstrumentationFunction (i.e., in addition to the function category, see  ProcessInstrumentationFunctionCategoryAssignmentClass).",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    qualityRelevanceSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1162",
            browseName="ns=dexpi;QualityRelevanceSpecialization",
            description="A classification indicating if the ProcessInstrumentationFunction is quality relevant.",
            dataType=dexpi_datypes.QualityRelevanceClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    safetyRelevanceClassAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1163",
            browseName="ns=dexpi;SafetyRelevanceClassAssignmentClass",
            description="The safety relevance class the ProcessInstrumentationFunction.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    typicalInformationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1164",
            browseName="ns=dexpi;TypicalInformationAssignmentClass",
            description="Typical information about the ProcessInstrumentationFunction.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    vendorCompanyNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1165",
            browseName="ns=dexpi;VendorCompanyNameAssignmentClass",
            description="The vendor company name the ProcessInstrumentationFunction.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    votingSystemRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1166",
            browseName="ns=dexpi;VotingSystemRepresentationAssignmentClass",
            description="A representation of the voting system of the ProcessInstrumentationFunction.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


o6.reference(ProcessControlFunctionType, "ns=dexpi;i=1059", ProcessInstrumentationFunctionType)


@o6.objecttype(
    nodeId="ns=dexpi;i=1200",
    browseName="ns=dexpi;ActuatingSystemType",
    displayName="ActuatingSystemType",
    description="An assembly of artefacts that is designed to fulfill an  ActuatingFunction.\nAssociation to ParentStructure (TechnicalItemParentStructure)\nAssociation to PlantTrain (PlantTrain)\nAssociation to PlantSystem (PlantSystem)\nAssociation to AreaIsa95 (AreaIsa95)",
)
class ActuatingSystemType(BaseDEXPIObjectType):
    actuatingSystemNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1201",
            browseName="ns=dexpi;ActuatingSystemNumberAssignmentClass",
            description="The number of the ActuatingSystem",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langleControlledActuatorRangle: ControlledActuatorType | None = o6.hasComponent(
        ControlledActuatorType(
            nodeId="ns=dexpi;i=2082",
            browseName="ns=dexpi;<ControlledActuator>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
        )
    )
    langlePositionerRangle: PositionerType | None = o6.hasComponent(
        PositionerType(
            nodeId="ns=dexpi;i=2084", browseName="ns=dexpi;<Positioner>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )
    langleShutOffValveReferenceRangle: ShutOffValveReferenceType | None = o6.hasComponent(
        ShutOffValveReferenceType(
            nodeId="ns=dexpi;i=2083",
            browseName="ns=dexpi;<ShutOffValveReference>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
        )
    )
    typicalInformationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1202",
            browseName="ns=dexpi;TypicalInformationAssignmentClass",
            description="Typical information about the ActuatingSystem.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1361",
    browseName="ns=dexpi;NozzleType",
    displayName="NozzleType",
    description="A physical object that has a protruding part through which a stream of fluid is directed (from http://data.posccaesar.org/rdl/RDS415214).\nAssociation to Chamber (Chamber)",
)
class NozzleType(BaseDEXPIObjectType):
    langleNodeRangle: PipingNodeType | None = o6.hasComponent(
        PipingNodeType(nodeId="ns=dexpi;i=2087", browseName="ns=dexpi;<Node>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder")
    )
    nominalPressureNumericalValueRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1363",
            browseName="ns=dexpi;NominalPressureNumericalValueRepresentationAssignmentClass",
            description="A readable representation of the numerical value of the nominal pressure. The purpose of this value is to give a textual representation of the nominal pressure to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    nominalPressureRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1364",
            browseName="ns=dexpi;NominalPressureRepresentationAssignmentClass",
            description="A readable representation of the nominal pressure. The purpose of this value is to give a textual representation of the nominal pressure to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    nominalPressureStandardSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1365",
            browseName="ns=dexpi;NominalPressureStandardSpecialization",
            description="The nominal pressure of the Nozzle, given as a reference to a nominal pressure standard and value.",
            dataType=dexpi_datypes.NominalPressureStandardClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    nominalPressureTypeRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1366",
            browseName="ns=dexpi;NominalPressureTypeRepresentationAssignmentClass",
            description="A readable representation of the type of the nominal pressure. The purpose of this value is to give a textual representation of the nominal pressure to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    subTagNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1362",
            browseName="ns=dexpi;SubTagNameAssignmentClass",
            description="The sub tag name of the Nozzle.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=dexpi;i=1377", browseName="ns=dexpi;ChamberOwnerType", displayName="ChamberOwnerType", description="An object that can have chambers.", isAbstract=True)
class ChamberOwnerType(BaseDEXPIObjectType):
    langleChamberRangle: ChamberType | None = o6.hasComponent(
        ChamberType(nodeId="ns=dexpi;i=2088", browseName="ns=dexpi;<Chamber>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder")
    )


@o6.objecttype(nodeId="ns=dexpi;i=1399", browseName="ns=dexpi;SubTaggedColumnSectionType", displayName="SubTaggedColumnSectionType", description="A sub tagged column section.")
class SubTaggedColumnSectionType(BaseDEXPIObjectType):
    height: ns0.vartypes.AnalogUnitType | None
    insideDiameter: ns0.vartypes.AnalogUnitType | None
    langleInternalRangle: ColumnInternalsArrangementType | None = o6.hasComponent(
        ColumnInternalsArrangementType(
            nodeId="ns=dexpi;i=2091",
            browseName="ns=dexpi;<Internal>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
            _allow_abstract=True,
        )
    )
    subTagNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1400",
            browseName="ns=dexpi;SubTagNameAssignmentClass",
            description="The sub tag name of the SubTaggedColumnSection.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=dexpi;i=1494", browseName="ns=dexpi;ColumnSectionType", displayName="ColumnSectionType", description="A column section.", isAbstract=True)
class ColumnSectionType(BaseDEXPIObjectType):
    height: ns0.vartypes.AnalogUnitType | None
    insideDiameter: ns0.vartypes.AnalogUnitType | None
    langleInternalRangle: ColumnInternalsArrangementType | None = o6.hasComponent(
        ColumnInternalsArrangementType(
            nodeId="ns=dexpi;i=2095",
            browseName="ns=dexpi;<Internal>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
            _allow_abstract=True,
        )
    )


o6.reference(SubTaggedColumnSectionType, "ns=dexpi;i=1059", ColumnSectionType)


@o6.objecttype(nodeId="ns=dexpi;i=1574", browseName="ns=dexpi;NozzleOwnerType", displayName="NozzleOwnerType", description="An object that can have nozzles.", isAbstract=True)
class NozzleOwnerType(BaseDEXPIObjectType):
    langleNozzleRangle: NozzleType | None = o6.hasComponent(
        NozzleType(nodeId="ns=dexpi;i=2100", browseName="ns=dexpi;<Nozzle>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder")
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1682",
    browseName="ns=dexpi;EquipmentType",
    displayName="EquipmentType",
    description="A piece of equipment.\nAssociation to ParentStructure (TechnicalItemParentStructure)\nAssociation to PlantTrain (PlantTrain)\nAssociation to PlantSystem (PlantSystem)\nAssociation to AreaIsa95 (AreaIsa95)",
    isAbstract=True,
)
class EquipmentType(BaseDEXPIObjectType):
    equipmentDescriptionAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1683",
            browseName="ns=dexpi;EquipmentDescriptionAssignmentClass",
            description="A short desciption of the Equipment in natural language. So far, there is no support for descriptions in different languages.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langleChamberRangle: ChamberType | None = o6.hasComponent(
        ChamberType(nodeId="ns=dexpi;i=2108", browseName="ns=dexpi;<Chamber>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder")
    )
    langleNozzleRangle: NozzleType | None = o6.hasComponent(
        NozzleType(nodeId="ns=dexpi;i=2109", browseName="ns=dexpi;<Nozzle>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder")
    )
    tagNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1686",
            browseName="ns=dexpi;TagNameAssignmentClass",
            description="The tag number of the TaggedPlantItem. See also <owner.TagNamePrefixAssignmentClass>, <owner.TagNameSequenceNumberAssignmentClass>, and <owner.TagNameSuffixAssignmentClass>.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    tagNamePrefixAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1687",
            browseName="ns=dexpi;TagNamePrefixAssignmentClass",
            description='The prefix part of the tag number of the TaggedPlantItem. For example, the prefix of the tag number "P4714-A" is "P". The prefix often indicates the type of the equipment item, e.g., "P" can indicate a pump. See also <owner.TagNameAssignmentClass>.',
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    tagNameSequenceNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1688",
            browseName="ns=dexpi;TagNameSequenceNumberAssignmentClass",
            description='The sequence number part of the tag number of the TaggedPlantItem. For example, the sequence number of the tag number "P4714-A" is "4714".',
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    tagNameSuffixAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1689",
            browseName="ns=dexpi;TagNameSuffixAssignmentClass",
            description='The suffix part of the tag number of an TaggedPlantItem item. For example, the suffix of the tag number "P4714-A" is "A".',
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


o6.reference(EquipmentType, "ns=dexpi;i=1059", TaggedPlantItemType)
o6.reference(EquipmentType, "ns=dexpi;i=1059", ChamberOwnerType)
o6.reference(EquipmentType, "ns=dexpi;i=1059", NozzleOwnerType)


@o6.objecttype(
    nodeId="ns=dexpi;i=1326",
    browseName="ns=dexpi;HeatExchangerType",
    displayName="HeatExchangerType",
    description="An artefact that is intended to transfer heat from one object to another (from http://data.posccaesar.org/rdl/RDS304199).\nAssociation to Agitator (Agitator)",
)
class HeatExchangerType(EquipmentType):
    designHeatFlowRate: ns0.vartypes.AnalogUnitType | None
    designHeatTransferArea: ns0.vartypes.AnalogUnitType | None
    designHeatTransferCoefficient: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=dexpi;i=1350", browseName="ns=dexpi;ThinFilmEvaporatorType", displayName="ThinFilmEvaporatorType", description="A thin film evaporator.")
class ThinFilmEvaporatorType(HeatExchangerType):
    designPower: ns0.vartypes.AnalogUnitType | None
    designRotationalSpeed: ns0.vartypes.AnalogUnitType | None
    designShaftPower: ns0.vartypes.AnalogUnitType | None
    langleRotorRangle: HeatExchangerRotorType | None = o6.hasComponent(
        HeatExchangerRotorType(
            nodeId="ns=dexpi;i=2086", browseName="ns=dexpi;<Rotor>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )


@o6.objecttype(nodeId="ns=dexpi;i=1369", browseName="ns=dexpi;SpiralHeatExchangerType", displayName="SpiralHeatExchangerType", description="A spiral heat exchanger")
class SpiralHeatExchangerType(HeatExchangerType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1408",
    browseName="ns=dexpi;CompressorType",
    displayName="CompressorType",
    description="A 'gas pressure increase device' and an 'artefact' that is driven by a prime mover by which energy is either constantly or periodically added to an amount of gas in order to increase its pressure (from http://data.posccaesar.org/rdl/RDS14286497).",
)
class CompressorType(EquipmentType):
    designVolumeFlowRate: ns0.vartypes.AnalogUnitType | None
    differentialPressure: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=dexpi;i=1379",
    browseName="ns=dexpi;ReciprocatingCompressorType",
    displayName="ReciprocatingCompressorType",
    description="A positive displacement compressor in which forced reduction of gas volume takes place by the movement of a displacing element in a cylinder or enclosure (from http://data.posccaesar.org/rdl/RDS417284).",
)
class ReciprocatingCompressorType(CompressorType):
    designRotationalSpeed: ns0.vartypes.AnalogUnitType | None
    designShaftPower: ns0.vartypes.AnalogUnitType | None
    langleDisplacerRangle: DisplacerType | None = o6.hasComponent(
        DisplacerType(
            nodeId="ns=dexpi;i=2089", browseName="ns=dexpi;<Displacer>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1387",
    browseName="ns=dexpi;SpecialCompressorType",
    displayName="SpecialCompressorType",
    description="A Compressor that is not covered by any of the sibling classes of SpecialCompressor.",
)
class SpecialCompressorType(CompressorType):
    designCapacityMotiveFluid: ns0.vartypes.AnalogUnitType | None
    designRotationalSpeed: ns0.vartypes.AnalogUnitType | None
    designShaftPower: ns0.vartypes.AnalogUnitType | None
    langleCompressorEquipmentItemRangle: CompressorEquipmentType | None = o6.hasComponent(
        CompressorEquipmentType(
            nodeId="ns=dexpi;i=2090",
            browseName="ns=dexpi;<CompressorEquipmentItem>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
            _allow_abstract=True,
        )
    )
    typeNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1397",
            browseName="ns=dexpi;TypeNameAssignmentClass",
            description="The name of the type of the SpecialCompressor.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1425",
    browseName="ns=dexpi;VesselType",
    displayName="VesselType",
    description="A container intended for storage and/or processing of fluids (from http://data.posccaesar.org/rdl/RDS414674).\nAssociation to ColumnSections (TaggedColumnSection)\nAssociation to Agitator (Agitator)",
)
class VesselType(EquipmentType):
    nominalCapacityVolume: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=dexpi;i=1445",
    browseName="ns=dexpi;PressureVesselType",
    displayName="PressureVesselType",
    description="A vessel intended to withstand external and/or internal pressure (from http://data.posccaesar.org/rdl/RDS427229).",
)
class PressureVesselType(VesselType):
    cylinderLength: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=dexpi;i=1449",
    browseName="ns=dexpi;SpecialVesselType",
    displayName="SpecialVesselType",
    description="A Vessel that is not covered by any of other subclasses of Vessel.",
)
class SpecialVesselType(VesselType):
    cylinderLength: ns0.vartypes.AnalogUnitType | None
    typeNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1453",
            browseName="ns=dexpi;TypeNameAssignmentClass",
            description="The name of the type of the SpecialVessel.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=dexpi;i=1454", browseName="ns=dexpi;MixerType", displayName="MixerType", description="An object that mixes two or more different ingredients.")
class MixerType(EquipmentType):
    langleMixingElementAssemblyRangle: MixingElementAssemblyType | None = o6.hasComponent(
        MixingElementAssemblyType(
            nodeId="ns=dexpi;i=2093",
            browseName="ns=dexpi;<MixingElementAssembly>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
        )
    )


@o6.objecttype(nodeId="ns=dexpi;i=1316", browseName="ns=dexpi;KneaderType", displayName="KneaderType", description="A kneading machine that kneads different ingredients.")
class KneaderType(MixerType):
    designRotationalSpeed: ns0.vartypes.AnalogUnitType | None
    designShaftPower: ns0.vartypes.AnalogUnitType | None
    upperLimitAllowableDesignPressureDrop: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=dexpi;i=1415", browseName="ns=dexpi;RotaryMixerType", displayName="RotaryMixerType", description="Rotating mixer.")
class RotaryMixerType(MixerType):
    designRotationalSpeed: ns0.vartypes.AnalogUnitType | None
    designShaftPower: ns0.vartypes.AnalogUnitType | None
    upperLimitAllowableDesignPressureDrop: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=dexpi;i=1478",
    browseName="ns=dexpi;AirCoolingSystemType",
    displayName="AirCoolingSystemType",
    description="A cooling system which uses air as the cooling medium (from http://data.posccaesar.org/rdl/RDS277379).",
)
class AirCoolingSystemType(HeatExchangerType):
    designPower: ns0.vartypes.AnalogUnitType | None
    designRotationalSpeed: ns0.vartypes.AnalogUnitType | None
    designShaftPower: ns0.vartypes.AnalogUnitType | None
    langleRotorRangle: HeatExchangerRotorType | None = o6.hasComponent(
        HeatExchangerRotorType(
            nodeId="ns=dexpi;i=2094", browseName="ns=dexpi;<Rotor>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1490",
    browseName="ns=dexpi;SiloType",
    displayName="SiloType",
    description="A vessel that has a bottom in the shape of a cone and is intended to store solid particles (from http://data.posccaesar.org/rdl/RDS1022399).",
)
class SiloType(VesselType):
    pass


@o6.objecttype(nodeId="ns=dexpi;i=1511", browseName="ns=dexpi;TaggedColumnSectionType", displayName="TaggedColumnSectionType", description="A fully tagged column section.")
class TaggedColumnSectionType(EquipmentType):
    height: ns0.vartypes.AnalogUnitType | None
    insideDiameter: ns0.vartypes.AnalogUnitType | None
    langleInternalRangle: ColumnInternalsArrangementType | None = o6.hasComponent(
        ColumnInternalsArrangementType(
            nodeId="ns=dexpi;i=2097",
            browseName="ns=dexpi;<Internal>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
            _allow_abstract=True,
        )
    )
    tagNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1512",
            browseName="ns=dexpi;TagNameAssignmentClass",
            description="The tag number of the TaggedPlantItem. See also <owner.TagNamePrefixAssignmentClass>, <owner.TagNameSequenceNumberAssignmentClass>, and <owner.TagNameSuffixAssignmentClass>.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    tagNamePrefixAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1513",
            browseName="ns=dexpi;TagNamePrefixAssignmentClass",
            description='The prefix part of the tag number of the TaggedPlantItem. For example, the prefix of the tag number "P4714-A" is "P". The prefix often indicates the type of the equipment item, e.g., "P" can indicate a pump. See also <owner.TagNameAssignmentClass>.',
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    tagNameSequenceNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1514",
            browseName="ns=dexpi;TagNameSequenceNumberAssignmentClass",
            description='The sequence number part of the tag number of the TaggedPlantItem. For example, the sequence number of the tag number "P4714-A" is "4714".',
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    tagNameSuffixAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1515",
            browseName="ns=dexpi;TagNameSuffixAssignmentClass",
            description='The suffix part of the tag number of an TaggedPlantItem item. For example, the suffix of the tag number "P4714-A" is "A".',
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


o6.reference(TaggedColumnSectionType, "ns=dexpi;i=1059", TaggedPlantItemType)
o6.reference(TaggedColumnSectionType, "ns=dexpi;i=1059", ColumnSectionType)


@o6.objecttype(
    nodeId="ns=dexpi;i=1557",
    browseName="ns=dexpi;ElectricHeaterType",
    displayName="ElectricHeaterType",
    description="A heater in which electric energy is converted into heat for useful purposes (from http://data.posccaesar.org/rdl/RDS14070475).",
)
class ElectricHeaterType(HeatExchangerType):
    designPower: ns0.vartypes.AnalogUnitType | None
    langleTubeBundleRangle: TubeBundleType | None = o6.hasComponent(
        TubeBundleType(
            nodeId="ns=dexpi;i=2098", browseName="ns=dexpi;<TubeBundle>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1566",
    browseName="ns=dexpi;CentrifugalCompressorType",
    displayName="CentrifugalCompressorType",
    description="A dynamic compressor in which one ore more impellers accelerate the gas and where the main flow through the impeller is radial (from http://data.posccaesar.org/rdl/RDS417194).",
)
class CentrifugalCompressorType(CompressorType):
    designRotationalSpeed: ns0.vartypes.AnalogUnitType | None
    designShaftPower: ns0.vartypes.AnalogUnitType | None
    langleImpellerRangle: ImpellerType | None = o6.hasComponent(
        ImpellerType(
            nodeId="ns=dexpi;i=2099", browseName="ns=dexpi;<Impeller>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1576",
    browseName="ns=dexpi;PlateAndShellHeatExchangerType",
    displayName="PlateAndShellHeatExchangerType",
    description="A corrugated plate heat exchanger that has a corrugated plate pack inside a shell (from http://data.posccaesar.org/rdl/RDS441719).",
)
class PlateAndShellHeatExchangerType(HeatExchangerType):
    numberOfPlates: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1577",
            browseName="ns=dexpi;NumberOfPlates",
            description="The number of plates in the PlateAndShellHeatExchanger.",
            dataType=o6.Int64,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    plateHeight: ns0.vartypes.AnalogUnitType | None
    plateWidth: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=dexpi;i=1619",
    browseName="ns=dexpi;FilterType",
    displayName="FilterType",
    description="A separator intended to remove solids from vapour or liquid (from http://data.posccaesar.org/rdl/RDS300689).",
)
class FilterType(EquipmentType):
    pass


@o6.objecttype(nodeId="ns=dexpi;i=1431", browseName="ns=dexpi;GasFilterType", displayName="GasFilterType", description="A filter that is specifically designed to filter a gas.")
class GasFilterType(FilterType):
    capacity_VolumeFlowRate: ns0.vartypes.AnalogUnitType | None
    designRotationalSpeed: ns0.vartypes.AnalogUnitType | None
    designShaftPower: ns0.vartypes.AnalogUnitType | None
    langleFilterUnitRangle: FilterUnitType | None = o6.hasComponent(
        FilterUnitType(
            nodeId="ns=dexpi;i=2092", browseName="ns=dexpi;<FilterUnit>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )
    upperLimitAllowableDesignPressureDrop: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=dexpi;i=1620",
    browseName="ns=dexpi;AirEjectorType",
    displayName="AirEjectorType",
    description="An ejector intended to create vacuum using compressed air (from http://data.posccaesar.org/rdl/RDS5770157).",
)
class AirEjectorType(CompressorType):
    designCapacityMotiveFluid: ns0.vartypes.AnalogUnitType | None
    langleImpellerRangle: ImpellerType | None = o6.hasComponent(
        ImpellerType(
            nodeId="ns=dexpi;i=2103", browseName="ns=dexpi;<Impeller>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1625",
    browseName="ns=dexpi;StaticMixerType",
    displayName="StaticMixerType",
    description="A physical object that is intended to mix fluid by means of diverging the flow with static obstacles or by increasing locally the velocity.",
)
class StaticMixerType(MixerType):
    upperLimitAllowableDesignPressureDrop: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=dexpi;i=1637",
    browseName="ns=dexpi;AgitatorType",
    displayName="AgitatorType",
    description="A dynamic mixer that stir or shake fluids by reaction force from moving vanes (from http://data.posccaesar.org/rdl/RDS16045622).",
)
class AgitatorType(EquipmentType):
    designRotationalSpeed: ns0.vartypes.AnalogUnitType | None
    designShaftPower: ns0.vartypes.AnalogUnitType | None
    langleRotorRangle: AgitatorRotorType | None = o6.hasComponent(
        AgitatorRotorType(
            nodeId="ns=dexpi;i=2104", browseName="ns=dexpi;<Rotor>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1645",
    browseName="ns=dexpi;AxialCompressorType",
    displayName="AxialCompressorType",
    description="A dynamic compressor in which the gas is accelerated by the action of a bladed rotor and where the main flow is along the rotation axis of the rotor (from http://data.posccaesar.org/rdl/RDS417239).",
)
class AxialCompressorType(CompressorType):
    designRotationalSpeed: ns0.vartypes.AnalogUnitType | None
    designShaftPower: ns0.vartypes.AnalogUnitType | None
    langleImpellerRangle: ImpellerType | None = o6.hasComponent(
        ImpellerType(
            nodeId="ns=dexpi;i=2105", browseName="ns=dexpi;<Impeller>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1653",
    browseName="ns=dexpi;ShellAndTubeHeatExchangerType",
    displayName="ShellAndTubeHeatExchangerType",
    description="A tubular heat exchanger in which a tube bundle is surrounded by a shell (from http://data.posccaesar.org/rdl/RDS419084).",
)
class ShellAndTubeHeatExchangerType(HeatExchangerType):
    langleTubeBundleRangle: TubeBundleType | None = o6.hasComponent(
        TubeBundleType(
            nodeId="ns=dexpi;i=2106", browseName="ns=dexpi;<TubeBundle>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )
    temaStandardTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1654",
            browseName="ns=dexpi;TemaStandardTypeAssignmentClass",
            description="The type of the ShellAndTubeHeatExchanger according to the Tubular Exchanger Manufacturers Association, Inc. (TEMA, http://www.tema.org). This is a three-letter code.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1663",
    browseName="ns=dexpi;TankType",
    displayName="TankType",
    description="A vessel intended to contain fluid for storage. Typically a receiving or collecting function for further distribution. Typically with a vertical and cylindrical or square shape and a flat or conical bottom (from http://data.posccaesar.org/rdl/RDS445139).",
)
class TankType(VesselType):
    cylinderLength: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=dexpi;i=1667",
    browseName="ns=dexpi;ProcessColumnType",
    displayName="ProcessColumnType",
    description="A vertical vessel intended to enable chemical reactions or physical processes utilising differences in density of fluids and/or forced flow of fluid (from http://data.posccaesar.org/rdl/RDS4316825224).",
)
class ProcessColumnType(EquipmentType):
    langleColumnSectionRangle: SubTaggedColumnSectionType | None = o6.hasComponent(
        SubTaggedColumnSectionType(
            nodeId="ns=dexpi;i=2107", browseName="ns=dexpi;<ColumnSection>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )
    nominalCapacityVolume: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=dexpi;i=1716",
    browseName="ns=dexpi;PumpType",
    displayName="PumpType",
    description="A physical object that is a driven piece of equipment in which energy is either constantly or periodically added to an amount of pumped liquid in order to increase the pressure required for the process in which the pump is in operation (from http://data.posccaesar.org/rdl/RDS327239).",
)
class PumpType(EquipmentType):
    designPressureHead: ns0.vartypes.AnalogUnitType | None
    designVolumeFlowRate: ns0.vartypes.AnalogUnitType | None
    differentialPressure: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=dexpi;i=1312",
    browseName="ns=dexpi;EjectorPumpType",
    displayName="EjectorPumpType",
    description="A pump which uses pressurized gas or liquid passing through an ejector to transport liquid (from http://data.posccaesar.org/rdl/RDS860624).",
)
class EjectorPumpType(PumpType):
    designCapacityMotiveFluid: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=dexpi;i=1342",
    browseName="ns=dexpi;RotaryPumpType",
    displayName="RotaryPumpType",
    description="A positive displacement pump that consists of a chamber containing gears, cams, screws, vanes, plungers or similar elements actuated by relative rotation of the drive shaft or casing and which has no separate inlet and outlet valves (from http://data.posccaesar.org/rdl/RDS420749).",
)
class RotaryPumpType(PumpType):
    designRotationalSpeed: ns0.vartypes.AnalogUnitType | None
    designShaftPower: ns0.vartypes.AnalogUnitType | None
    langleDisplacerRangle: DisplacerType | None = o6.hasComponent(
        DisplacerType(
            nodeId="ns=dexpi;i=2085", browseName="ns=dexpi;<Displacer>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1503",
    browseName="ns=dexpi;ReciprocatingPumpType",
    displayName="ReciprocatingPumpType",
    description="a positive displacement pump which contains a displacing element intended to be moved in a reciprocating movement to exert pressure on a fluid, typically moving within a cylindrical space (from http://data.posccaesar.org/rdl/RDS416969).",
)
class ReciprocatingPumpType(PumpType):
    designRotationalSpeed: ns0.vartypes.AnalogUnitType | None
    designShaftPower: ns0.vartypes.AnalogUnitType | None
    langleDisplacerRangle: DisplacerType | None = o6.hasComponent(
        DisplacerType(
            nodeId="ns=dexpi;i=2096", browseName="ns=dexpi;<Displacer>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1584",
    browseName="ns=dexpi;CentrifugalPumpType",
    displayName="CentrifugalPumpType",
    description="A dynamic pump utilizing impellers provided with vanes generating centrifugal force to achieve the required pressure head (from http://data.posccaesar.org/rdl/RDS416834).",
)
class CentrifugalPumpType(PumpType):
    designRotationalSpeed: ns0.vartypes.AnalogUnitType | None
    designShaftPower: ns0.vartypes.AnalogUnitType | None
    langleImpellerRangle: ImpellerType | None = o6.hasComponent(
        ImpellerType(
            nodeId="ns=dexpi;i=2101", browseName="ns=dexpi;<Impeller>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1607",
    browseName="ns=dexpi;SpecialPumpType",
    displayName="SpecialPumpType",
    description="A Pump that is not covered by any of the sibling classes of SpecialPump.",
)
class SpecialPumpType(PumpType):
    designCapacityMotiveFluid: ns0.vartypes.AnalogUnitType | None
    designRotationalSpeed: ns0.vartypes.AnalogUnitType | None
    designShaftPower: ns0.vartypes.AnalogUnitType | None
    langlePumpEquipmentItemRangle: PumpEquipmentType | None = o6.hasComponent(
        PumpEquipmentType(
            nodeId="ns=dexpi;i=2102",
            browseName="ns=dexpi;<PumpEquipmentItem>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
            _allow_abstract=True,
        )
    )
    typeNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1608",
            browseName="ns=dexpi;TypeNameAssignmentClass",
            description="The name of the type of the SpecialPump.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1694", browseName="ns=dexpi;LiquidFilterType", displayName="LiquidFilterType", description="A filter that is specifically designed to filter a liquid."
)
class LiquidFilterType(FilterType):
    capacity_VolumeFlowRate: ns0.vartypes.AnalogUnitType | None
    designRotationalSpeed: ns0.vartypes.AnalogUnitType | None
    designShaftPower: ns0.vartypes.AnalogUnitType | None
    langleFilterUnitRangle: FilterUnitType | None = o6.hasComponent(
        FilterUnitType(
            nodeId="ns=dexpi;i=2110", browseName="ns=dexpi;<FilterUnit>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )
    upperLimitAllowableDesignPressureDrop: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=dexpi;i=1708",
    browseName="ns=dexpi;RotaryCompressorType",
    displayName="RotaryCompressorType",
    description="A positive displacement compressor in which compression displacement is effected by the positive action of rotating elements (from http://data.posccaesar.org/rdl/RDS435374).",
)
class RotaryCompressorType(CompressorType):
    designRotationalSpeed: ns0.vartypes.AnalogUnitType | None
    designShaftPower: ns0.vartypes.AnalogUnitType | None
    langleDisplacerRangle: DisplacerType | None = o6.hasComponent(
        DisplacerType(
            nodeId="ns=dexpi;i=2111", browseName="ns=dexpi;<Displacer>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1786",
    browseName="ns=dexpi;PipeConnectorSymbolType",
    displayName="PipeConnectorSymbolType",
    description="A pipe connector symbol. It is usually drawn as an arrow.",
    isAbstract=True,
)
class PipeConnectorSymbolType(BaseDEXPIObjectType):
    langleNodeRangle: PipingNodeType | None = o6.hasComponent(
        PipingNodeType(nodeId="ns=dexpi;i=2114", browseName="ns=dexpi;<Node>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder")
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1827",
    browseName="ns=dexpi;FlowInPipeConnectorSymbolType",
    displayName="FlowInPipeConnectorSymbolType",
    description="A pipe connector symbol that indicates that a preceding part of a PipingNetworkSegment is represented somewhere else, either on the same P&ID, or on some other P&ID.",
)
class FlowInPipeConnectorSymbolType(BaseDEXPIObjectType):
    langleNodeRangle: PipingNodeType | None = o6.hasComponent(
        PipingNodeType(nodeId="ns=dexpi;i=2115", browseName="ns=dexpi;<Node>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder")
    )


o6.reference(FlowInPipeConnectorSymbolType, "ns=dexpi;i=1059", PipeConnectorSymbolType)


@o6.objecttype(
    nodeId="ns=dexpi;i=1829",
    browseName="ns=dexpi;FlowOutPipeConnectorSymbolType",
    displayName="FlowOutPipeConnectorSymbolType",
    description="A pipe connector symbol that indicates that a subsequent part of a PipingNetworkSegment is represented somewhere else, either on the same P&ID, or on some other P&ID.",
)
class FlowOutPipeConnectorSymbolType(BaseDEXPIObjectType):
    langleNodeRangle: PipingNodeType | None = o6.hasComponent(
        PipingNodeType(nodeId="ns=dexpi;i=2116", browseName="ns=dexpi;<Node>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder")
    )


o6.reference(FlowOutPipeConnectorSymbolType, "ns=dexpi;i=1059", PipeConnectorSymbolType)


@o6.objecttype(
    nodeId="ns=dexpi;i=1898",
    browseName="ns=dexpi;PipingNetworkSegmentType",
    displayName="PipingNetworkSegmentType",
    description="The piping limited by a Node and a Break, Node and Connector,  two Nodes, two Breaks, two Connectors or a Break and a Connector. The last five providing there are no Breaks or Connectors in between. In the last three cases the Segment will coincide with a Piping Branch (from http://data.posccaesar.org/rdl/RDS267704).\nAssociation to SourceItem (PipingSourceItem)\nAssociation to SourceNode (PipingNode)\nAssociation to TargetItem (PipingTargetItem)\nAssociation to TargetNode (PipingNode)",
)
class PipingNetworkSegmentType(BaseDEXPIObjectType):
    basfLineClassAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1900",
            browseName="ns=dexpi;BasfLineClassAssignmentClass",
            description="The BASF line class of the PipingNetworkSegment, represented as a string. Note: This attribute has been included as an example for a company-specific attribute. It should actually be identified by a company-specific RDL reference. As there is currently no BASF RDL, the DEXPI RDL is used.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    colorCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1901",
            browseName="ns=dexpi;ColorCodeAssignmentClass",
            description="The color code of the PipingNetworkSegment, represented as a string.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    flowDirectionSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1902",
            browseName="ns=dexpi;FlowDirectionSpecialization",
            description="A specialization indicating if the PipingNetworkSegment enables dual flow or not.",
            dataType=dexpi_datypes.PipingNetworkSegmentFlowClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    fluidCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1903",
            browseName="ns=dexpi;FluidCodeAssignmentClass",
            description="The identification code of the fluid related to the PipingNetworkSegment. So  far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    heatTracingTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1904",
            browseName="ns=dexpi;HeatTracingTypeAssignmentClass",
            description="The heat tracing type related to the PipingNetworkSegment, represented as a string.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    heatTracingTypeSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1905",
            browseName="ns=dexpi;HeatTracingTypeSpecialization",
            description="A specialization indicating the heat tracing type related to the PipingNetworkSegment.",
            dataType=dexpi_datypes.HeatTracingTypeClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    inclination: ns0.vartypes.AnalogUnitType | None
    insulationThickness: ns0.vartypes.AnalogUnitType | None
    insulationTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1912",
            browseName="ns=dexpi;InsulationTypeAssignmentClass",
            description="The identification code for the insulation type related to the PipingNetworkSegment. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    jacketedPipeSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1913",
            browseName="ns=dexpi;JacketedPipeSpecialization",
            description="A specialization indicating whether the PipingNetworkSegment is jacketed.",
            dataType=dexpi_datypes.JacketedPipeClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langleConnectionRangle: PipingConnectionType | None = o6.hasComponent(
        PipingConnectionType(
            nodeId="ns=dexpi;i=2118",
            browseName="ns=dexpi;<Connection>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
            _allow_abstract=True,
        )
    )
    langleItemRangle: PipingNetworkSegmentItemType | None = o6.hasComponent(
        PipingNetworkSegmentItemType(
            nodeId="ns=dexpi;i=2117",
            browseName="ns=dexpi;<Item>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
            _allow_abstract=True,
        )
    )
    lowerLimitHeatTracingTemperature: ns0.vartypes.AnalogUnitType | None
    nominalDiameterNumericalValueRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1917",
            browseName="ns=dexpi;NominalDiameterNumericalValueRepresentationAssignmentClass",
            description="A readable representation of the numerical value of the nominal diameter of the PipingNetworkSegment. The purpose of this value is to give a textual representation of the nominal diameter to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    nominalDiameterRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1918",
            browseName="ns=dexpi;NominalDiameterRepresentationAssignmentClass",
            description="A readable representation of the nominal diameter of the PipingNetworkSegment. The purpose of this value is to give a textual representation of the nominal diameter to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    nominalDiameterStandardSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1919",
            browseName="ns=dexpi;NominalDiameterStandardSpecialization",
            description="The nominal diameter of the PipingNetworkSegment, given as a reference to a nominal  diameter standard and value.",
            dataType=dexpi_datypes.NominalDiameterStandardClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    nominalDiameterTypeRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1920",
            browseName="ns=dexpi;NominalDiameterTypeRepresentationAssignmentClass",
            description="A readable representation of the type of the nominal diameter of the PipingNetworkSegment. The purpose of this value is to give a textual representation of the nominal diameter to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    onHoldSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1921",
            browseName="ns=dexpi;OnHoldSpecialization",
            description="A specialization indicating if the PipingNetworkSegment is on hold or not.",
            dataType=dexpi_datypes.OnHoldClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    operatingTemperature: ns0.vartypes.AnalogUnitType | None
    pipingClassCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1925",
            browseName="ns=dexpi;PipingClassCodeAssignmentClass",
            description="The identification code of the piping class of the PipingNetworkSegment. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pressureTestCircuitNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1926",
            browseName="ns=dexpi;PressureTestCircuitNumberAssignmentClass",
            description="The number of the pressure test circuit of the PipingNetworkSegment.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    primarySecondaryPipingNetworkSegmentSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1927",
            browseName="ns=dexpi;PrimarySecondaryPipingNetworkSegmentSpecialization",
            description="A specialization indicating whether the PipingNetworkSegment is a primary or secondary PipingNetworkSegment.",
            dataType=dexpi_datypes.PrimarySecondaryPipingNetworkSegmentClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    segmentNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1899",
            browseName="ns=dexpi;SegmentNumberAssignmentClass",
            description="The segment number of a PipingNetworkSegment. Values are typically (but not  necessarily) string representations of numbers with a prefix.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    siphonSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1928",
            browseName="ns=dexpi;SiphonSpecialization",
            description="A specialization indicating if the PipingNetworkSegment is a siphon or not.",
            dataType=dexpi_datypes.SiphonClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    slopeSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1929",
            browseName="ns=dexpi;SlopeSpecialization",
            description="A specialization indicating if the PipingNetworkSegment is sloped or not.",
            dataType=dexpi_datypes.PipingNetworkSegmentSlopeClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1938", browseName="ns=dexpi;PropertyBreakType", displayName="PropertyBreakType", description="A symbol indicating a change in the piping properties."
)
class PropertyBreakType(BaseDEXPIObjectType):
    compositionBreakSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1939",
            browseName="ns=dexpi;CompositionBreakSpecialization",
            description="A specialization indicating if the PropertyBreak is a composition break or not.",
            dataType=dexpi_datypes.CompositionBreakClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    insulationBreakSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1940",
            browseName="ns=dexpi;InsulationBreakSpecialization",
            description="A specialization indicating if the PropertyBreak is an insulation break or not.",
            dataType=dexpi_datypes.InsulationBreakClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langleNodeRangle: PipingNodeType | None = o6.hasComponent(
        PipingNodeType(nodeId="ns=dexpi;i=2119", browseName="ns=dexpi;<Node>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder")
    )
    nominalDiameterBreakSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1941",
            browseName="ns=dexpi;NominalDiameterBreakSpecialization",
            description="A specialization indicating if the PropertyBreak is a nominal diameter break or not.",
            dataType=dexpi_datypes.NominalDiameterBreakClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingClassBreakSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1942",
            browseName="ns=dexpi;PipingClassBreakSpecialization",
            description="A specialization indicating if the PropertyBreak is a composition break or not.",
            dataType=dexpi_datypes.PipingClassBreakClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1726",
    browseName="ns=dexpi;PipingNetworkSystemType",
    displayName="PipingNetworkSystemType",
    description="A fluid system of interconnected piping network branches limited by Unit Operation Inlet/Outlet and  Piping Network Terminators. In this context Piping includes e.g. plumbing and tubing (from http://data.posccaesar.org/rdl/RDS270359).\nAssociation to ParentStructure (TechnicalItemParentStructure)\nAssociation to PlantTrain (PlantTrain)\nAssociation to PlantSystem (PlantSystem)\nAssociation to AreaIsa95 (AreaIsa95)",
)
class PipingNetworkSystemType(BaseDEXPIObjectType):
    fluidCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1728",
            browseName="ns=dexpi;FluidCodeAssignmentClass",
            description="The identification code of the fluid related to the PipingNetworkSystem. So  far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    heatTracingTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1736",
            browseName="ns=dexpi;HeatTracingTypeAssignmentClass",
            description="The heat tracing type related to the PipingNetworkSystem, represented as a string.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    heatTracingTypeSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1737",
            browseName="ns=dexpi;HeatTracingTypeSpecialization",
            description="A specialization indicating the heat tracing type related to the PipingNetworkSystem.",
            dataType=dexpi_datypes.HeatTracingTypeClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    insulationThickness: ns0.vartypes.AnalogUnitType | None
    insulationTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1732",
            browseName="ns=dexpi;InsulationTypeAssignmentClass",
            description="The identification code for the insulation type related to the PipingNetworkSystem. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    jacketLineNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1739",
            browseName="ns=dexpi;JacketLineNumberAssignmentClass",
            description="The line number of the PipingNetworkSystem that is the jacket of this PipingNetworkSystem.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    jacketedLineNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1738",
            browseName="ns=dexpi;JacketedLineNumberAssignmentClass",
            description="The line number of the PipingNetworkSystem for which this PipingNetworkSystem is the jacket.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    jacketedPipeSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1740",
            browseName="ns=dexpi;JacketedPipeSpecialization",
            description="A specialization indicating whether the PipingNetworkSystem is jacketed.",
            dataType=dexpi_datypes.JacketedPipeClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langlePropertyBreakRangle: PropertyBreakType | None = o6.hasComponent(
        PropertyBreakType(
            nodeId="ns=dexpi;i=2113", browseName="ns=dexpi;<PropertyBreak>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )
    langleSegmentRangle: PipingNetworkSegmentType | None = o6.hasComponent(
        PipingNetworkSegmentType(
            nodeId="ns=dexpi;i=2112", browseName="ns=dexpi;<Segment>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )
    lineNumberAssignmentClassOfPipingNetworkSystem: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1727",
            browseName="ns=dexpi;LineNumberAssignmentClassOfPipingNetworkSystem",
            description="The line number of a PipingNetworkSystem. Values are typically (but not necessarily) string representations of numbers.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    lowerLimitHeatTracingTemperature: ns0.vartypes.AnalogUnitType | None
    nominalDiameterNumericalValueRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1742",
            browseName="ns=dexpi;NominalDiameterNumericalValueRepresentationAssignmentClass",
            description="A readable representation of the numerical value of the nominal diameter of the PipingNetworkSystem. The purpose of this value is to give a textual representation of the nominal diameter to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    nominalDiameterRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1743",
            browseName="ns=dexpi;NominalDiameterRepresentationAssignmentClass",
            description="A readable representation of the nominal diameter of the PipingNetworkSystem. The purpose of this value is to give a textual representation of the nominal diameter to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    nominalDiameterStandardSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1741",
            browseName="ns=dexpi;NominalDiameterStandardSpecialization",
            description="The nominal diameter of the PipingNetworkSystem, given as a reference to a nominal  diameter standard and value.",
            dataType=dexpi_datypes.NominalDiameterStandardClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    nominalDiameterTypeRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1744",
            browseName="ns=dexpi;NominalDiameterTypeRepresentationAssignmentClass",
            description="A readable representation of the type of the nominal diameter of the PipingNetworkSystem. The purpose of this value is to give a textual representation of the nominal diameter to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    onHoldSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1745",
            browseName="ns=dexpi;OnHoldSpecialization",
            description="A specialization indicating if the PipingNetworkSystem is on hold or not.",
            dataType=dexpi_datypes.OnHoldClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingClassCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1746",
            browseName="ns=dexpi;PipingClassCodeAssignmentClass",
            description="The identification code of the piping class of the PipingNetworkSystem. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingNetworkSystemGroupNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1747",
            browseName="ns=dexpi;PipingNetworkSystemGroupNumberAssignmentClass",
            description="The number of the piping network system group of the PipingNetworkSystem, represented as a string.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=dexpi;i=1072", browseName="ns=dexpi;PlantType", displayName="PlantType", description="The engineering content of a PlantModel.")
class PlantType(BaseDEXPIObjectType):
    langleActuatingSystemRangle: ActuatingSystemType | None = o6.hasComponent(
        ActuatingSystemType(
            nodeId="ns=dexpi;i=2068", browseName="ns=dexpi;<ActuatingSystem>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )
    langleInstrumentationLoopFunctionRangle: InstrumentationLoopFunctionType | None = o6.hasComponent(
        InstrumentationLoopFunctionType(
            nodeId="ns=dexpi;i=2069",
            browseName="ns=dexpi;<InstrumentationLoopFunction>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
        )
    )
    langlePipingNetworkSystemRangle: PipingNetworkSystemType | None = o6.hasComponent(
        PipingNetworkSystemType(
            nodeId="ns=dexpi;i=2070",
            browseName="ns=dexpi;<PipingNetworkSystem>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
        )
    )
    langleProcessInstrumentationFunctionRangle: ProcessInstrumentationFunctionType | None = o6.hasComponent(
        ProcessInstrumentationFunctionType(
            nodeId="ns=dexpi;i=2071",
            browseName="ns=dexpi;<ProcessInstrumentationFunction>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
        )
    )
    langleProcessSignalGeneratingSystemRangle: ProcessSignalGeneratingSystemType | None = o6.hasComponent(
        ProcessSignalGeneratingSystemType(
            nodeId="ns=dexpi;i=2072",
            browseName="ns=dexpi;<ProcessSignalGeneratingSystem>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
        )
    )
    langleTaggedPlantItemRangle: TaggedPlantItemType | None = o6.hasComponent(
        TaggedPlantItemType(
            nodeId="ns=dexpi;i=2073",
            browseName="ns=dexpi;<TaggedPlantItem>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
            _allow_abstract=True,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1068",
    browseName="ns=dexpi;PlantModelType",
    displayName="PlantModelType",
    description="A model of a chemical plant. It includes various aspects such as the engineering content, a diagram, and metadata.",
)
class PlantModelType(BaseDEXPIObjectType):
    langleMetaDataRangle: MetaDataType | None = o6.hasComponent(
        MetaDataType(
            nodeId="ns=dexpi;i=2065", browseName="ns=dexpi;<MetaData>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder"
        )
    )
    langlePlantRangle: PlantType | None = o6.hasComponent(
        PlantType(nodeId="ns=dexpi;i=2067", browseName="ns=dexpi;<Plant>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder")
    )
    langleStructureItemRangle: PlantStructureItemType | None = o6.hasComponent(
        PlantStructureItemType(
            nodeId="ns=dexpi;i=2066",
            browseName="ns=dexpi;<StructureItem>",
            description="OPC UA Object(s) that are part of the Object Type",
            modellingRule="OptionalPlaceholder",
            _allow_abstract=True,
        )
    )


@o6.objecttype(nodeId="ns=dexpi;i=1995", browseName="ns=dexpi;PipingComponentType", displayName="PipingComponentType", description="A piping component", isAbstract=True)
class PipingComponentType(BaseDEXPIObjectType):
    basfLineClassAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1996",
            browseName="ns=dexpi;BasfLineClassAssignmentClass",
            description="The BASF line class of the PipingComponent, represented as a string. Note: This attribute has been included as an example for a company-specific attribute. It should actually be identified by a company-specific RDL reference. As there is currently no BASF RDL, the DEXPI RDL is used.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    fluidCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1997",
            browseName="ns=dexpi;FluidCodeAssignmentClass",
            description="The identification code of the fluid related to the PipingComponent. So  far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langleNodeRangle: PipingNodeType | None = o6.hasComponent(
        PipingNodeType(nodeId="ns=dexpi;i=2120", browseName="ns=dexpi;<Node>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder")
    )
    nominalDiametersRepresentationAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1998",
            browseName="ns=dexpi;NominalDiametersRepresentationAssignmentClass",
            description="A readable representation of the nominal diameters of the ports of the PipingComponent. The purpose of this value is to give a textual representation of the nominal diameters to be used in the graphics of a PID.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    onHoldSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1999",
            browseName="ns=dexpi;OnHoldSpecialization",
            description="A specialization indicating if the PipingComponent is on hold or not.",
            dataType=dexpi_datypes.OnHoldClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingClassArtefactSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=2000",
            browseName="ns=dexpi;PipingClassArtefactSpecialization",
            description="A specialization indicating if the PipingComponent is an artefact that is         described by a piping class.",
            dataType=dexpi_datypes.PipingClassArtefactClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pressureTestCircuitNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=2001",
            browseName="ns=dexpi;PressureTestCircuitNumberAssignmentClass",
            description="The number of the pressure test circuit of the PipingComponent.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1773",
    browseName="ns=dexpi;CheckValveType",
    displayName="CheckValveType",
    description="A valve that permits fluid to flow in one direction only (from http://data.posccaesar.org/rdl/RDS292229).",
)
class CheckValveType(PipingComponentType):
    heatTracingTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1775",
            browseName="ns=dexpi;HeatTracingTypeAssignmentClass",
            description="The heat tracing type related to the CheckValve, represented as a string.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    heatTracingTypeSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1776",
            browseName="ns=dexpi;HeatTracingTypeSpecialization",
            description="A specialization indicating the heat tracing type related to the CheckValve.",
            dataType=dexpi_datypes.HeatTracingTypeClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    insulationThickness: ns0.vartypes.AnalogUnitType | None
    insulationTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1780",
            browseName="ns=dexpi;InsulationTypeAssignmentClass",
            description="The identification code for the insulation type related to the CheckValve. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    lowerLimitHeatTracingTemperature: ns0.vartypes.AnalogUnitType | None
    pipingClassCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1784",
            browseName="ns=dexpi;PipingClassCodeAssignmentClass",
            description="The identification code of the piping class of the CheckValve. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingComponentNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1785",
            browseName="ns=dexpi;PipingComponentNameAssignmentClass",
            description="The piping component name of the CheckValve.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingComponentNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1774",
            browseName="ns=dexpi;PipingComponentNumberAssignmentClass",
            description="The piping component number of the CheckValve.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=dexpi;i=1793", browseName="ns=dexpi;InlinePrimaryElementType", displayName="InlinePrimaryElementType", description="An inline primary element.")
class InlinePrimaryElementType(PipingComponentType):
    heatTracingTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1798",
            browseName="ns=dexpi;HeatTracingTypeAssignmentClass",
            description="The heat tracing type related to the InlinePrimaryElement, represented as a string.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    heatTracingTypeSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1799",
            browseName="ns=dexpi;HeatTracingTypeSpecialization",
            description="A specialization indicating the heat tracing type related to the InlinePrimaryElement.",
            dataType=dexpi_datypes.HeatTracingTypeClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    insulationThickness: ns0.vartypes.AnalogUnitType | None
    insulationTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1803",
            browseName="ns=dexpi;InsulationTypeAssignmentClass",
            description="The identification code for the insulation type related to the InlinePrimaryElement. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    lowerLimitHeatTracingTemperature: ns0.vartypes.AnalogUnitType | None
    pipingComponentNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1804",
            browseName="ns=dexpi;PipingComponentNameAssignmentClass",
            description="The piping component name of the InlinePrimaryElement.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingComponentNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1794",
            browseName="ns=dexpi;PipingComponentNumberAssignmentClass",
            description="The piping component number of the InlinePrimaryElement.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1755",
    browseName="ns=dexpi;TurbineFlowMeterType",
    displayName="TurbineFlowMeterType",
    description="A velocity flow meter that uses a multi bladed rotor to measure fluid flow rate in units of volumetric flow through a closed conduit (from http://data.posccaesar.org/rdl/RDS417914).",
)
class TurbineFlowMeterType(InlinePrimaryElementType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1809",
    browseName="ns=dexpi;PositiveDisplacementFlowMeterType",
    displayName="PositiveDisplacementFlowMeterType",
    description="A flow meter that measures the volumetric flow rate of a liquid or gas by separating the flow stream into known volumes and counting them over time (from http://data.posccaesar.org/rdl/RDS418094).",
)
class PositiveDisplacementFlowMeterType(InlinePrimaryElementType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1810",
    browseName="ns=dexpi;VariableAreaFlowMeterType",
    displayName="VariableAreaFlowMeterType",
    description="A flow meter consisting of a vertical tube with a conically shaped bore which widens to the top in which a solid body (float) is supported by the force exerted by the fluid stream (from http://data.posccaesar.org/rdl/RDS418229).",
)
class VariableAreaFlowMeterType(InlinePrimaryElementType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1811",
    browseName="ns=dexpi;ElectromagneticFlowMeterType",
    displayName="ElectromagneticFlowMeterType",
    description="A velocity flow meter that is measuring flow rate of a conductive fluid running through a magnetic field by measuring the charge created when fluid interacting with the field (from http://data.posccaesar.org/rdl/RDS1009664).",
)
class ElectromagneticFlowMeterType(InlinePrimaryElementType):
    pass


@o6.objecttype(nodeId="ns=dexpi;i=1845", browseName="ns=dexpi;ShutOffValveType", displayName="ShutOffValveType", description="A shut off valve.")
class ShutOffValveType(PipingComponentType):
    heatTracingTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1847",
            browseName="ns=dexpi;HeatTracingTypeAssignmentClass",
            description="The heat tracing type related to the ShutOffValve, represented as a string.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    heatTracingTypeSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1848",
            browseName="ns=dexpi;HeatTracingTypeSpecialization",
            description="A specialization indicating the heat tracing type related to the ShutOffValve.",
            dataType=dexpi_datypes.HeatTracingTypeClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    insulationThickness: ns0.vartypes.AnalogUnitType | None
    insulationTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1852",
            browseName="ns=dexpi;InsulationTypeAssignmentClass",
            description="The identification code for the insulation type related to the ShutOffValve. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    lowerLimitHeatTracingTemperature: ns0.vartypes.AnalogUnitType | None
    numberOfPortsSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1858",
            browseName="ns=dexpi;NumberOfPortsSpecialization",
            description="A specialization indicating the number of ports of the ShutOffValve.",
            dataType=dexpi_datypes.NumberOfPortsClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    operationSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1859",
            browseName="ns=dexpi;OperationSpecialization",
            description="A specialization indicating the operation of the ShutOffValve.",
            dataType=dexpi_datypes.OperationClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingClassCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1856",
            browseName="ns=dexpi;PipingClassCodeAssignmentClass",
            description="The identification code of the piping class of the ShutOffValve. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingComponentNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1857",
            browseName="ns=dexpi;PipingComponentNameAssignmentClass",
            description="The piping component name of the ShutOffValve.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingComponentNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1846",
            browseName="ns=dexpi;PipingComponentNumberAssignmentClass",
            description="The piping component number of the ShutOffValve.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1756",
    browseName="ns=dexpi;AngleValveType",
    displayName="AngleValveType",
    description="A valve that has valve ports which are not in-line (from http://data.posccaesar.org/rdl/RDS5789384).",
)
class AngleValveType(ShutOffValveType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1771",
    browseName="ns=dexpi;NeedleValveType",
    displayName="NeedleValveType",
    description="A globe valve that has a closure member with the shape of a conical plug (needle) which closes into a small seat (from http://data.posccaesar.org/rdl/RDS421064).",
)
class NeedleValveType(ShutOffValveType):
    pass


@o6.objecttype(nodeId="ns=dexpi;i=1789", browseName="ns=dexpi;AngleBallValveType", displayName="AngleBallValveType", description="An angle ball valve.")
class AngleBallValveType(ShutOffValveType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1790",
    browseName="ns=dexpi;BallValveType",
    displayName="BallValveType",
    description="A rotary valve that has a ball closure member (from http://data.posccaesar.org/rdl/RDS416654).",
)
class BallValveType(ShutOffValveType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1791",
    browseName="ns=dexpi;PlugValveType",
    displayName="PlugValveType",
    description="A rotary valve that has a quarter turn action in which the closure member is a cylindrical or tapered plug which operates by rotating on its axis and sealing against a downstream seat (from http://data.posccaesar.org/rdl/RDS421109).",
)
class PlugValveType(ShutOffValveType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1808",
    browseName="ns=dexpi;AngleGlobeValveType",
    displayName="AngleGlobeValveType",
    description="A globe valve that deviates from the in-line design, i.e. with a body shape designed to adjust the flow direction with a specified angle relative to the straight through-flow an in-line valve would have provided for (from http://data.posccaesar.org/rdl/RDS882944).",
)
class AngleGlobeValveType(ShutOffValveType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1865",
    browseName="ns=dexpi;FlowDetectorType",
    displayName="FlowDetectorType",
    description="A detector that is intended to detect whether a fluid flow exists (from http://data.posccaesar.org/rdl/RDS1008719).",
)
class FlowDetectorType(InlinePrimaryElementType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1869",
    browseName="ns=dexpi;GlobeValveType",
    displayName="GlobeValveType",
    description="A valve that is a valve where the closure member is a disc or piston operating with linear motion normal to the flat or shaped seat (from http://data.posccaesar.org/rdl/RDS416204).",
)
class GlobeValveType(ShutOffValveType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1873",
    browseName="ns=dexpi;StraightwayValveType",
    displayName="StraightwayValveType",
    description="A valve that is straight, i.e. the centerlines perpendicular to the ends are in-line with no offset (from http://data.posccaesar.org/rdl/RDS9390905).",
)
class StraightwayValveType(ShutOffValveType):
    pass


@o6.objecttype(nodeId="ns=dexpi;i=1874", browseName="ns=dexpi;GlobeCheckValveType", displayName="GlobeCheckValveType", description="A globe chack valve.")
class GlobeCheckValveType(CheckValveType):
    pass


@o6.objecttype(nodeId="ns=dexpi;i=1877", browseName="ns=dexpi;PipeFittingType", displayName="PipeFittingType", description="A pipe fitting.")
class PipeFittingType(PipingComponentType):
    heatTracingTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1882",
            browseName="ns=dexpi;HeatTracingTypeAssignmentClass",
            description="The heat tracing type related to the PipeFitting, represented as a string.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    heatTracingTypeSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1883",
            browseName="ns=dexpi;HeatTracingTypeSpecialization",
            description="A specialization indicating the heat tracing type related to the PipeFitting.",
            dataType=dexpi_datypes.HeatTracingTypeClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    insulationThickness: ns0.vartypes.AnalogUnitType | None
    insulationTypeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1887",
            browseName="ns=dexpi;InsulationTypeAssignmentClass",
            description="The identification code for the insulation type related to the PipeFitting. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    lowerLimitHeatTracingTemperature: ns0.vartypes.AnalogUnitType | None
    pipingClassCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1888",
            browseName="ns=dexpi;PipingClassCodeAssignmentClass",
            description="The identification code of the piping class of the PipeFitting. So far, DEXPI does not define restrictions for valid values.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingComponentNameAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1889",
            browseName="ns=dexpi;PipingComponentNameAssignmentClass",
            description="The piping component name of the PipeFitting.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pipingComponentNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1878",
            browseName="ns=dexpi;PipingComponentNumberAssignmentClass",
            description="The piping component number of the PipeFitting.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


o6.reference(StrainerType, "ns=dexpi;i=1059", PipeFittingType)
o6.reference(SteamTrapType, "ns=dexpi;i=1059", PipeFittingType)
o6.reference(SilencerType, "ns=dexpi;i=1059", PipeFittingType)
o6.reference(VentilationDeviceType, "ns=dexpi;i=1059", PipeFittingType)
o6.reference(OrificePlateType, "ns=dexpi;i=1059", PipeFittingType)


@o6.objecttype(
    nodeId="ns=dexpi;i=1770",
    browseName="ns=dexpi;FunnelType",
    displayName="FunnelType",
    description="A hollow cone with a tube extending from the smaller end and that is designed to catch and direct a downward flow (from http://data.posccaesar.org/rdl/RDS6689917).",
)
class FunnelType(PipeFittingType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1772",
    browseName="ns=dexpi;InLineMixerType",
    displayName="InLineMixerType",
    description="A static mixer that is intended to be supported by connected equipment. Typically supported by piping (from http://data.posccaesar.org/rdl/RDS43167562195).",
)
class InLineMixerType(PipeFittingType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1788",
    browseName="ns=dexpi;FlangeType",
    displayName="FlangeType",
    description="A physical object that is a projecting flat rim, plate,collar, or rib (from http://data.posccaesar.org/rdl/RDS13307654).",
)
class FlangeType(PipeFittingType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1792",
    browseName="ns=dexpi;CompensatorType",
    displayName="CompensatorType",
    description="A device compensating for axial or radial movement between two elements that is connected (from http://data.posccaesar.org/rdl/RDS1280084541).",
)
class CompensatorType(PipeFittingType):
    pass


@o6.objecttype(nodeId="ns=dexpi;i=1805", browseName="ns=dexpi;FlangedConnectionType", displayName="FlangedConnectionType", description="A flanged connection.")
class FlangedConnectionType(PipeFittingType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1806",
    browseName="ns=dexpi;HoseType",
    displayName="HoseType",
    description="A tubular which is flexible and capable of conveying liquids under pressure (from http://data.posccaesar.org/rdl/RDS302174).",
)
class HoseType(PipeFittingType):
    pass


@o6.objecttype(nodeId="ns=dexpi;i=1825", browseName="ns=dexpi;IlluminatedSightGlassType", displayName="IlluminatedSightGlassType", description="An illuminated sight glass.")
class IlluminatedSightGlassType(PipeFittingType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1866",
    browseName="ns=dexpi;ConicalStrainerType",
    displayName="ConicalStrainerType",
    description="A strainer where the screen has a conical tubular shape (from http://data.posccaesar.org/rdl/RDS16044540).",
)
class ConicalStrainerType(PipeFittingType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1867",
    browseName="ns=dexpi;SightGlassType",
    displayName="SightGlassType",
    description="A physical object that is transparent and intended for viewing a vessel or piping system interior (from http://data.posccaesar.org/rdl/RDS648674).",
)
class SightGlassType(PipeFittingType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1870",
    browseName="ns=dexpi;PipeFlangeSpacerType",
    displayName="PipeFlangeSpacerType",
    description="A 'spacer' and an 'artefact' that is intended to be inserted between two pipe flanged ends to provide the distance between the flanges required to insert a 'pipe flange spade' (from http://data.posccaesar.org/rdl/RDS472724).",
)
class PipeFlangeSpacerType(PipeFittingType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1871",
    browseName="ns=dexpi;BlindFlangeType",
    displayName="BlindFlangeType",
    description="A pipe flange that is without a central opening and used to shut off a flanged pipe end (from http://data.posccaesar.org/rdl/RDS414719).",
)
class BlindFlangeType(PipeFittingType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1875",
    browseName="ns=dexpi;PipeTeeType",
    displayName="PipeTeeType",
    description="An 'artefact' that has three piping ends in T-shape, including a branch at 90 degrees (from http://data.posccaesar.org/rdl/RDS427724).",
)
class PipeTeeType(PipeFittingType):
    pass


@o6.objecttype(nodeId="ns=dexpi;i=1895", browseName="ns=dexpi;VolumetricFlowDetectorType", displayName="VolumetricFlowDetectorType", description="A volumetric flow detector.")
class VolumetricFlowDetectorType(InlinePrimaryElementType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1896",
    browseName="ns=dexpi;PipeFlangeSpadeType",
    displayName="PipeFlangeSpadeType",
    description="A 'line blind' and an 'artefact' that is a circular plate with no central opening and holes to match mating flanged ends. It is also equipped with a handle (from http://data.posccaesar.org/rdl/RDS472679).",
)
class PipeFlangeSpadeType(PipeFittingType):
    pass


@o6.objecttype(nodeId="ns=dexpi;i=1897", browseName="ns=dexpi;ClampedFlangeCouplingType", displayName="ClampedFlangeCouplingType", description="A clamped flange coupling.")
class ClampedFlangeCouplingType(PipeFittingType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1936",
    browseName="ns=dexpi;PenetrationType",
    displayName="PenetrationType",
    description="A device intended to provide a penetration (from http://data.posccaesar.org/rdl/RDS13068275).",
)
class PenetrationType(PipeFittingType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1937",
    browseName="ns=dexpi;SwingCheckValveType",
    displayName="SwingCheckValveType",
    description="A check valve that is a check valve where the closure member is a disc which swings freely on a hinge and which opens automatically when flow is established and closes automatically when flow ceases or is reversed (from http://data.posccaesar.org/rdl/RDS610424).",
)
class SwingCheckValveType(CheckValveType):
    pass


@o6.objecttype(nodeId="ns=dexpi;i=1944", browseName="ns=dexpi;SafetyValveOrFittingType", displayName="SafetyValveOrFittingType", description="A safety valve or fitting.")
class SafetyValveOrFittingType(PipingComponentType):
    flowInPipingClassCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1947",
            browseName="ns=dexpi;FlowInPipingClassCodeAssignmentClass",
            description="The code of the piping class at the flow in side of SafetyValveOrFitting.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    flowOutPipingClassCodeAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1948",
            browseName="ns=dexpi;FlowOutPipingClassCodeAssignmentClass",
            description="The code of the piping class at the flow out side of SafetyValveOrFitting.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    locationRegistrationNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1946",
            browseName="ns=dexpi;LocationRegistrationNumberAssignmentClass",
            description="The location registration number of the SafetyValveOrFitting.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    positionNumberAssignmentClass: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1945",
            browseName="ns=dexpi;PositionNumberAssignmentClass",
            description="The position number of the SafetyValveOrFitting.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    setPressureHigh: ns0.vartypes.AnalogUnitType | None
    setPressureLow: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=dexpi;i=1831",
    browseName="ns=dexpi;SpringLoadedGlobeSafetyValveType",
    displayName="SpringLoadedGlobeSafetyValveType",
    description="A spring-loaded globe safety valve.",
)
class SpringLoadedGlobeSafetyValveType(SafetyValveOrFittingType):
    pass


@o6.objecttype(nodeId="ns=dexpi;i=1868", browseName="ns=dexpi;BreatherValveType", displayName="BreatherValveType", description="A breather valve.")
class BreatherValveType(SafetyValveOrFittingType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1872",
    browseName="ns=dexpi;RuptureDiscType",
    displayName="RuptureDiscType",
    description="A physical object that is designed to burst at a certain excess pressure. It is part of a rupture disc assembly (from http://data.posccaesar.org/rdl/RDS8372601).",
)
class RuptureDiscType(SafetyValveOrFittingType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1876",
    browseName="ns=dexpi;SpringLoadedAngleGlobeSafetyValveType",
    displayName="SpringLoadedAngleGlobeSafetyValveType",
    description="A spring-loaded angle globe safety valve.",
)
class SpringLoadedAngleGlobeSafetyValveType(SafetyValveOrFittingType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1955",
    browseName="ns=dexpi;VenturiTubeType",
    displayName="VenturiTubeType",
    description="A 'measuring device' that has a constriction with a relative long passage with a smooth coned entry and exit (from http://data.posccaesar.org/rdl/RDS648044).",
)
class VenturiTubeType(InlinePrimaryElementType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1956",
    browseName="ns=dexpi;FlowNozzleType",
    displayName="FlowNozzleType",
    description="A nozzle with a smooth entry and a sharp exit (from http://data.posccaesar.org/rdl/RDS821024).",
)
class FlowNozzleType(InlinePrimaryElementType):
    pass


@o6.objecttype(nodeId="ns=dexpi;i=1957", browseName="ns=dexpi;AnglePlugValveType", displayName="AnglePlugValveType", description="An angle plug valve.")
class AnglePlugValveType(ShutOffValveType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1971",
    browseName="ns=dexpi;PipeCouplingType",
    displayName="PipeCouplingType",
    description="An 'artefact' that is a one-piece cylindrical section intended to join pipes and/or piping components (from http://data.posccaesar.org/rdl/RDS415664).",
)
class PipeCouplingType(PipeFittingType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=1972",
    browseName="ns=dexpi;FlameArrestorType",
    displayName="FlameArrestorType",
    description="An 'arrestor' which is a trap covering an opening, e.g of a ventilation system or a pipe, to prevent flames from entering the system (from http://data.posccaesar.org/rdl/RDS1325028651).",
)
class FlameArrestorType(SafetyValveOrFittingType):
    detonationProofArtefactSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1973",
            browseName="ns=dexpi;DetonationProofArtefactSpecialization",
            description="A specialization indicating if the FlameArrestor is detonation-proof.",
            dataType=dexpi_datypes.DetonationProofArtefactClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    explosionProofArtefactSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1974",
            browseName="ns=dexpi;ExplosionProofArtefactSpecialization",
            description="A specialization indicating if the FlameArrestor is explosion-proof.",
            dataType=dexpi_datypes.ExplosionProofArtefactClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    fireResistantArtefactSpecialization: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=dexpi;i=1975",
            browseName="ns=dexpi;FireResistantArtefactSpecialization",
            description="A specialization indicating if the FlameArrestor is fire-resistant.",
            dataType=dexpi_datypes.FireResistantArtefactClassification,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=dexpi;i=1994",
    browseName="ns=dexpi;ButterflyValveType",
    displayName="ButterflyValveType",
    description="A rotary valve that has a closure member of a disc type with a shaft parallel, or near parallel, to the plane of the disc, with an axis of rotation transverse to the flow direction (from http://data.posccaesar.org/rdl/RDS416609).",
)
class ButterflyValveType(ShutOffValveType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=2003",
    browseName="ns=dexpi;GateValveType",
    displayName="GateValveType",
    description="A valve that is a valve where the closure member is a gate or disc with a linear motion parallel, or nearly parallel, to the plane of flat seats, which are transverse to the direction of flow (from http://data.posccaesar.org/rdl/RDS416519).",
)
class GateValveType(ShutOffValveType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=2004",
    browseName="ns=dexpi;PipeReducerType",
    displayName="PipeReducerType",
    description="An 'artefact' that has different nominal pipe size at the two ends, intended to connect pipes or piping components (from http://data.posccaesar.org/rdl/RDS416294).",
)
class PipeReducerType(PipeFittingType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=2005",
    browseName="ns=dexpi;LineBlindType",
    displayName="LineBlindType",
    description="A functional unit used to blind off a process stream (from http://data.posccaesar.org/rdl/RDS280034).",
)
class LineBlindType(PipeFittingType):
    pass


@o6.objecttype(
    nodeId="ns=dexpi;i=2006", browseName="ns=dexpi;PipingNodeOwnerType", displayName="PipingNodeOwnerType", description="An object that can have PipingNodes.", isAbstract=True
)
class PipingNodeOwnerType(BaseDEXPIObjectType):
    langleNodeRangle: PipingNodeType | None = o6.hasComponent(
        PipingNodeType(nodeId="ns=dexpi;i=2121", browseName="ns=dexpi;<Node>", description="OPC UA Object(s) that are part of the Object Type", modellingRule="OptionalPlaceholder")
    )


o6.reference(NozzleType, "ns=dexpi;i=1059", PipingNodeOwnerType)
o6.reference(PipeConnectorSymbolType, "ns=dexpi;i=1059", PipingNodeOwnerType)
o6.reference(PropertyBreakType, "ns=dexpi;i=1059", PipingNodeOwnerType)
o6.reference(PipingComponentType, "ns=dexpi;i=1059", PipingNodeOwnerType)


del Any, TYPE_CHECKING, uuid, o6, ns0, dexpi_reftypes, dexpi_datypes
