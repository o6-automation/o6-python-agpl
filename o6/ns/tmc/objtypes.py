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

"""Generated OPC UA tmc namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.pack_ml as pack_ml
from . import reftypes as tmc_reftypes
from . import datatypes as tmc_datypes
from . import vartypes as tmc_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=tmc;i=1001",
    browseName="ns=tmc;MachineModuleProductionStateMachineType",
    displayName="MachineModuleProductionStateMachineType",
    description="The MachineModuleProductionStateMachineType provides state information about the \nexecution of a production order at a Machine Module.",
)
class MachineModuleProductionStateMachineType(ns0.objtypes.FiniteStateMachineType):
    aborted: ns0.objtypes.StateType
    abortedToComplete: ns0.objtypes.TransitionType
    abortedToCompleteGuard: tmc_vartypes.BooleanGuardVariableType
    aborting: ns0.objtypes.StateType
    abortingToAborted: ns0.objtypes.TransitionType
    abortingToAbortedGuard: tmc_vartypes.BooleanGuardVariableType
    assigned: ns0.objtypes.StateType
    assignedToComplete: ns0.objtypes.TransitionType
    assignedToCompleteGuard: tmc_vartypes.BooleanGuardVariableType
    assignedToStarting: ns0.objtypes.TransitionType
    assignedToStartingGuard: tmc_vartypes.BooleanGuardVariableType
    complete: ns0.objtypes.InitialStateType
    completeToAssigned: ns0.objtypes.TransitionType
    completeToAssignedGuard: tmc_vartypes.BooleanGuardVariableType
    completing: ns0.objtypes.StateType
    completingToAborting: ns0.objtypes.TransitionType
    completingToAbortingGuard: tmc_vartypes.BooleanGuardVariableType
    completingToComplete: ns0.objtypes.TransitionType
    completingToCompleteGuard: tmc_vartypes.BooleanGuardVariableType
    execute: ns0.objtypes.StateType
    executeToAborting: ns0.objtypes.TransitionType
    executeToAbortingGuard: tmc_vartypes.BooleanGuardVariableType
    executeToCompleting: ns0.objtypes.TransitionType
    executeToCompletingGuard: tmc_vartypes.BooleanGuardVariableType
    lastTransition: ns0.vartypes.FiniteTransitionVariableType
    starting: ns0.objtypes.StateType
    startingToAborting: ns0.objtypes.TransitionType
    startingToAbortingGuard: tmc_vartypes.BooleanGuardVariableType
    startingToExecute: ns0.objtypes.TransitionType
    startingToExecuteGuard: tmc_vartypes.BooleanGuardVariableType


@o6.objecttype(
    nodeId="ns=tmc;i=1006",
    browseName="ns=tmc;LogbookEventType",
    displayName="LogbookEventType",
    description="Subtypes of LogbookEvent Type provide detailed information on the event they are triggered \nby.",
    isAbstract=True,
)
class LogbookEventType(ns0.objtypes.BaseEventType):
    pass


@o6.objecttype(
    nodeId="ns=tmc;i=1090",
    browseName="ns=tmc;TMCDeviceType",
    displayName="TMCDeviceType",
    description="The TMCDeviceType ObjectType is used to include UIInfo and specify which DeviceType \ncomponents are mandatory when used in compliance with TMC.",
    isAbstract=True,
)
class TMCDeviceType(di.objtypes.DeviceType):
    uIInfo: UIInformationType | None


@o6.objecttype(
    nodeId="ns=tmc;i=1043",
    browseName="ns=tmc;UserInterfaceType",
    displayName="UserInterfaceType",
    description="The UserInterfaceType provides a generic User Interface description.",
)
class UserInterfaceType(ns0.objtypes.BaseObjectType):
    controlPanelVURO: ns0.objtypes.BaseObjectType = o6.hasComponent(
        ns0.objtypes.BaseObjectType(
            nodeId="ns=tmc;i=5088",
            browseName="ns=tmc;ControlPanelVURO",
            description="The control panel area where read-only objects are shown. Objects connected to a ControlPanelVURO by \nmeans of a non-hierarchical reference of type IsDisplayedBy are shown in the control panel.",
        )
    )
    controlPanelVURW: ns0.objtypes.BaseObjectType = o6.hasComponent(
        ns0.objtypes.BaseObjectType(
            nodeId="ns=tmc;i=5089",
            browseName="ns=tmc;ControlPanelVURW",
            description="The control panel area where read-write objects are shown. Objects connected to a ControlPanelVURW by \nmeans of a non-hierarchical reference of type IsDisplayedBy are shown in the control panel.",
        )
    )
    kPIVU: ns0.objtypes.BaseObjectType = o6.hasComponent(
        ns0.objtypes.BaseObjectType(
            nodeId="ns=tmc;i=5286",
            browseName="ns=tmc;KPIVU",
            description="The object collecting variables to be displayed in the KPI section. Objects connected to a KPIVU by means \nof a non-hierarchical reference of type IsDisplayedBy are shown in the KPI display area.",
        )
    )
    loopVUReferences: ns0.objtypes.BaseObjectType = o6.hasComponent(
        ns0.objtypes.BaseObjectType(
            nodeId="ns=tmc;i=5290",
            browseName="ns=tmc;LoopVUReferences",
            description="The collection of references to control loops to be displayed. Non-hierarchical references connected to \nLoopVuReferences by means of a non-hierarchical reference of type IsDisplayedBy are shown in the control \npanel.",
        )
    )
    overVU: ns0.objtypes.BaseObjectType = o6.hasComponent(
        ns0.objtypes.BaseObjectType(
            nodeId="ns=tmc;i=5291",
            browseName="ns=tmc;OverVU",
            description="The overview of the UI interface. Objects connected to an OverVU by means of a non-hierarchical \nreference of type IsDisplayedBy are shown in the overview display.",
        )
    )
    zoomedVU: ns0.objtypes.BaseObjectType = o6.hasComponent(
        ns0.objtypes.BaseObjectType(
            nodeId="ns=tmc;i=5292",
            browseName="ns=tmc;ZoomedVU",
            description="The zooned view of the UI interface. Objects connected to a ZoomedVU by means of a non-hierarchical \nreference of type IsDisplayedBy are shown in the zoomed in area.",
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1047",
    browseName="ns=tmc;ControlModuleConfigurationType",
    displayName="ControlModuleConfigurationType",
    description="The ControlModuleConfigurationType ObjectType contains all digital settings, stop reasons and \nroot causes of a control module.",
)
class ControlModuleConfigurationType(ns0.objtypes.BaseObjectType):
    deviceLifeSpan: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=tmc;i=6100", browseName="ns=tmc;DeviceLifeSpan", description="The control module expected life span duration.", dataType=o6.UInt32)
    )
    langleConfigurationItemRangle: ns0.vartypes.DataItemType | None = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=tmc;i=6099",
            browseName="ns=tmc;<ConfigurationItem>",
            description="A digital setting for the control module e.g. parameter, stop reason or root cause.",
            modellingRule="OptionalPlaceholder",
        )
    )
    validSince: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6101", browseName="ns=tmc;ValidSince", description="The UTC date and time when the configuration was last changed.", dataType=ns0.datatypes.UtcTime
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1012",
    browseName="ns=tmc;MachineModuleHistoricalRecordType",
    displayName="MachineModuleHistoricalRecordType",
    description="The MachineModuleHistoricalRecordType ObjectType contains the specifications of the \nmachine module that have been valid in the past.",
)
class MachineModuleHistoricalRecordType(ns0.objtypes.BaseObjectType):
    machineModuleSpecification: MachineModuleSpecificationType
    validUntil: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6155",
            browseName="ns=tmc;ValidUntil",
            description="The ValidUntil Propertyontains the date and time the MachineModuleSpecification was last \nvalid.",
            dataType=ns0.datatypes.UtcTime,
            value=o6.DateTime("2000-01-01T00:00:00Z"),
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6275",
    browseName="ns=tmc;RejectionMode",
    description="When RejectionMode is True, the rejection trap discharges material when triggered, \notherwise no material is rejected.",
    dataType=o6.Boolean,
    value=False,
    accessLevel=3,
    userAccessLevel=1,
)


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6041",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Enable", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("The flag enables (True) or disables (False) the remote control mode.")
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6042",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=7001",
    browseName="ns=tmc;SetRemoteControl",
    description="The SetRemoteControl Method enables or disables the remote control mode.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6041"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6042"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=13434",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=7007",
    browseName="ns=tmc;EndSubCarrierLoading",
    description="The EndSubCarrierLoading Method informs the underlying system that the loading of (sub) carriers into \nthe carrier is complete.",
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=13434"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6180",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(
            name="NewMaterialLoadingPoints",
            dataType=o6.NodeId("ns=tmc;i=3013"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("The information about the material loading points that will be valid after the machine specification is changed.\n"),
        ),
        ns0.datatypes.Argument(
            name="NewMaterialStorageBuffers",
            dataType=o6.NodeId("ns=tmc;i=3014"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("The information about the storage buffers that will be valid after the machine specification is changed.\n"),
        ),
        ns0.datatypes.Argument(
            name="NewMaterialOutputPoints",
            dataType=o6.NodeId("ns=tmc;i=3013"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("The information about the material output points that will be valid after the machine specification is changed."),
        ),
        ns0.datatypes.Argument(
            name="NewMaterialRejectionPoints",
            dataType=o6.NodeId("ns=tmc;i=3013"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("The information about the material rejection points that will be valid after the machine specification is changed."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6367",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure.\n"),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=7029",
    browseName="ns=tmc;SetNewSpecification",
    description="The Method SetNewSpecification saves its arguments as the new specification for the machine module. \nPrior to that it saves the previous specification into the PastSpecification Records Object of the same \nmachine module.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6180"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6367"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6305",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7033",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="MaterialList", dataType=o6.NodeId("ns=tmc;i=3037"), valueRank=-1, description=o6.LocalizedText("The material list to be transferred to the underlying system.")
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6329",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7033",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=7033",
    browseName="ns=tmc;LoadMaterialList",
    description="The LoadMaterialList Method loads the material list to the underlying system after having validated that \n(a) the material list is complete and (b) the material list is valid.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6305"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6329"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6185",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7034",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="DataSet", dataType=o6.NodeId("ns=tmc;i=3018"), valueRank=-1, description=o6.LocalizedText("The dataset to be validated by the underlying system.")
        ),
        ns0.datatypes.Argument(
            name="IsCompleteDataSet",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("When true, the DataSet argument is a complete dataset, meaning all DataSet entries are included."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6186",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7034",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="FailedValidationEntries",
            dataType=o6.NodeId("ns=tmc;i=3004"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("The dataset items that failed the validation."),
        ),
        ns0.datatypes.Argument(
            name="FailedValidationMessages",
            dataType=o6.NodeId("ns=tmc;i=3002"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("The detailed reasons the validation failed."),
        ),
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        ),
    ],
)
o6.call(
    nodeId="ns=tmc;i=7034",
    browseName="ns=tmc;ValidateDataSet",
    description="The ValidateDataSet Method transfers a dataset, complete when IsCompleteDataSet is True, to the underlying system and returns the result of the validation, i.e. verifying that the dataset is complete and can run in production.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6185"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6186"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6437",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7042",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="DataSet", dataType=o6.NodeId("ns=tmc;i=3018"), valueRank=-1, description=o6.LocalizedText("The dataset to be transferred to the underlying system.")
        ),
        ns0.datatypes.Argument(
            name="IsCompleteDataSet",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("When true, the DataSet argument is a complete dataset, meaning all DataSet entries are included."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6438",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7042",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure.\n"),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=7042",
    browseName="ns=tmc;LoadDataSet",
    description="The LoadDataSet Method loads the dataset to the underlying system after having validated that (a) the dataset is complete when IsCompleteDataset is True and (b) the dataset is valid.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6437"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6438"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6331",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7043",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="MaterialList", dataType=o6.NodeId("ns=tmc;i=3037"), valueRank=-1, description=o6.LocalizedText("The material list to be validated by the underlying system.")
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6332",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7043",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="FailedValidationEntries", dataType=o6.NodeId("ns=tmc;i=3036"), valueRank=1, description=o6.LocalizedText("The material list items that failed the validation.")
        ),
        ns0.datatypes.Argument(
            name="FailedValidationMessages", dataType=o6.NodeId("ns=tmc;i=3002"), valueRank=1, description=o6.LocalizedText("The detailed reasons the validation failed.")
        ),
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        ),
    ],
)
o6.call(
    nodeId="ns=tmc;i=7043",
    browseName="ns=tmc;ValidateMaterialList",
    description="The ValidateMaterialList Method transfers a material list to the underlying system and returns the result \nof the validation.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6331"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6332"]),
)


@o6.objecttype(
    nodeId="ns=tmc;i=1016",
    browseName="ns=tmc;MachineModuleSetupType",
    displayName="MachineModuleSetupType",
    description="The MachineModuleSetupType ObjectType contains the value of all the settings (including \nmechanical adjustments) required to run production as well as affordances to validate and load \nsettings for the machine module.",
)
class MachineModuleSetupType(ns0.objtypes.BaseObjectType):
    dataSet: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6177",
            browseName="ns=tmc;DataSet",
            description="DataSet contains all the digital settings (other than the mechanical settings stored in the folder \nMechanicalAdjustments) required by the machine module.",
            dataType=tmc_datypes.DataSetType,
            value=tmc_datypes.DataSetType(iD="", values=[]),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    dataSetFolder: ns0.objtypes.FolderType
    loadDataSet: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7042"])
    loadMaterialList: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7033"])
    materialList: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6330",
            browseName="ns=tmc;MaterialList",
            description="MaterialList contains the list of materials that are going to be used for the production of the current \nproduction order.",
            dataType=tmc_datypes.MaterialListType,
        )
    )
    mechanicalAdjustments: ns0.objtypes.FolderType
    validateDataSet: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7034"])
    validateMaterialList: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7043"])


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6232",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7044",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ControlMode", dataType=o6.NodeId("ns=tmc;i=3023"), valueRank=-1, description=o6.LocalizedText("The control mode to be set to the machine module.")
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6389",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7044",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure.\n"),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=7044",
    browseName="ns=tmc;SetControlMode",
    description="The SetControlMode Method sets the control mode of the machine module.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6232"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6389"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6098",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7045",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=7045",
    browseName="ns=tmc;ResetAggregates",
    description="The ResetAggregates Method resets the aggregates of the control module.",
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6098"]),
)


@o6.objecttype(
    nodeId="ns=tmc;i=1051",
    browseName="ns=tmc;ControlModuleAggregatesType",
    displayName="ControlModuleAggregatesType",
    description="The ControlModuleAggregatesType ObjectType provides aggregates computed by the \nunderlying system for the control module.",
)
class ControlModuleAggregatesType(ns0.objtypes.BaseObjectType):
    langleAggregateItemRangle: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=6003",
            browseName="ns=tmc;<AggregateItem>",
            description="A single aggregate data point exposed by the control module.",
            modellingRule="OptionalPlaceholder",
        )
    )
    resetAggregates: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=7045"])
    validSince: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6245", browseName="ns=tmc;ValidSince", description="The time of the last reset for the aggregates.", dataType=ns0.datatypes.UtcTime
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6241",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7052",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(name="Command", dataType=o6.NodeId("ns=tmc;i=3007"), valueRank=-1, description=o6.LocalizedText("The command to be sent to the machine module."))
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6385",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7052",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure.\n"),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=7052",
    browseName="ns=tmc;SendCommand",
    description="The Method SendCommand sends a command to change the state of the machine module state machine.\nThe Method SendCommand sends a command to change the state of the machine module state machine.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6241"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6385"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6405",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7053",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=7053",
    browseName="ns=tmc;AcknowledgeAlarms",
    description="The AcknowledgeAlarms Method acknowledges the alarms of the control module.",
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6405"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6246",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7056",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="IdleEnergySavingMode", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("The energy saving mode to set."))],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6393",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7056",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure.\n"),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=7056",
    browseName="ns=tmc;SetIdleEnergySavingMode",
    description="The Method SetIdleEnergySavingMode activates the energy saving mode when the machine \nmodule is idle.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6246"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6393"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6868",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7063",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="RejectionMode",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("When true, the rejection trap rejects. When false, the rejection trap does not reject.\n"),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6917",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7063",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure.\n"),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=7063",
    browseName="ns=tmc;SetRejectionMode",
    description="The Method SetRejectionMode turns the rejection on or off.\nThe Method SetRejectionMode turns the rejection on or off.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6868"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6917"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6326",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7072",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="RootCauseList",
            dataType=o6.NodeId("ns=tmc;i=3029"),
            valueRank=1,
            description=o6.LocalizedText("The list of root causes to be transferred to and used by the server."),
        ),
        ns0.datatypes.Argument(
            name="RootCauseGroupList",
            dataType=o6.NodeId("ns=tmc;i=3030"),
            valueRank=1,
            description=o6.LocalizedText("The list of root cause groups to be transferred to and used by the server."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6327",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7072",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=7072",
    browseName="ns=tmc;SetRootCauseLists",
    description="The SetRootCauseLists Method sets both the RootCauseList and RootCauseGroupList \naccording to the input arguments.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6326"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6327"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6425",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7104",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(
            name="Dependency",
            dataType=o6.NodeId("ns=tmc;i=3005"),
            valueRank=-1,
            description=o6.LocalizedText("Dependency specifies how to select (filter) a subset of the dataset based on dependency."),
        ),
        ns0.datatypes.Argument(
            name="UserSubset",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("UserSubset specifies how to select (filter) a subset of the dataset based on the user-defined UserSubset."),
        ),
        ns0.datatypes.Argument(
            name="CompleteSet",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText(
                "If CompleteSet is True, then the method returns the complete dataset without considering the input \nparameters Dependency and UserSubset."
            ),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6429",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7104",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="DataSetList",
            dataType=o6.NodeId("ns=tmc;i=3021"),
            valueRank=-1,
            description=o6.LocalizedText("The list of parameters filtered as per the input arguments Dependency and UserSubset."),
        ),
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure.\n"),
        ),
    ],
)
o6.call(
    nodeId="ns=tmc;i=7104",
    browseName="ns=tmc;GetDataSetList",
    description="The GetDatasetList Method returns the list of descriptions for parameters of the dataset filtered \nby the dependency and subset created by the user.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6425"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6429"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6210",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7105",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="RootCauseList", dataType=o6.NodeId("ns=tmc;i=3029"), valueRank=1, description=o6.LocalizedText("The complete list of root cause messages.")),
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure.\n"),
        ),
    ],
)
o6.call(
    nodeId="ns=tmc;i=7105",
    browseName="ns=tmc;GetRootCauseList",
    description="The GetRootCauseList Method returns the complete list of root causes as persisted by the \nserver.",
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6210"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6306",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7106",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="StopReasonList", dataType=o6.NodeId("ns=tmc;i=3002"), valueRank=1, description=o6.LocalizedText("The complete list of stop reason messages.")),
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure.\n"),
        ),
    ],
)
o6.call(
    nodeId="ns=tmc;i=7106",
    browseName="ns=tmc;GetStopReasonList",
    description="The GetStopReasonList Method returns the complete list of stop reasons as persisted by the \nserver.",
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6306"]),
)

o6.call(nodeId="ns=tmc;i=7109", browseName="ns=pack_ml;Abort")

o6.call(nodeId="ns=tmc;i=7121", browseName="ns=pack_ml;Clear")


@o6.objecttype(nodeId="ns=tmc;i=1018", browseName="ns=tmc;TMCStateMachineType", displayName="TMCStateMachineType")
class TMCStateMachineType(pack_ml.objtypes.PackMLBaseStateMachineType):
    abort: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7109"])
    aborted: ns0.objtypes.StateType
    abortedSubstate: ns0.objtypes.StateMachineType | None
    abortedToCleared: ns0.objtypes.TransitionType
    abortedToClearedGuard: tmc_vartypes.BooleanGuardVariableType
    aborting: ns0.objtypes.StateType
    abortingToAborted: ns0.objtypes.TransitionType
    abortingToAbortedGuard: tmc_vartypes.BooleanGuardVariableType
    clear: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7121"])
    cleared: ns0.objtypes.StateType
    clearedToAborting: ns0.objtypes.TransitionType
    clearedToAbortingGuard: tmc_vartypes.BooleanGuardVariableType
    lastTransition: ns0.vartypes.FiniteTransitionVariableType
    machineState: TMCMachineStateMachineType


o6.reference(TMCStateMachineType, "i=41", "i=2311")


o6.call(nodeId="ns=tmc;i=7122", browseName="ns=pack_ml;Reset")

o6.call(nodeId="ns=tmc;i=7149", browseName="ns=pack_ml;Stop")


@o6.objecttype(nodeId="ns=tmc;i=1019", browseName="ns=tmc;TMCMachineStateMachineType", displayName="TMCMachineStateMachineType")
class TMCMachineStateMachineType(pack_ml.objtypes.PackMLMachineStateMachineType):
    clearing: ns0.objtypes.StateType
    clearingToStopped: ns0.objtypes.TransitionType
    clearingToStoppedGuard: tmc_vartypes.BooleanGuardVariableType
    executeState: TMCExecuteStateMachineType
    lastTransition: ns0.vartypes.FiniteTransitionVariableType
    reset: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7122"])
    running: ns0.objtypes.StateType
    runningToStopping: ns0.objtypes.TransitionType
    runningToStoppingGuard: tmc_vartypes.BooleanGuardVariableType
    stop: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7149"])
    stopped: ns0.objtypes.StateType
    stoppedSubstate: ns0.objtypes.StateMachineType | None
    stoppedToRunning: ns0.objtypes.TransitionType
    stoppedToRunningGuard: tmc_vartypes.BooleanGuardVariableType
    stopping: ns0.objtypes.StateType
    stoppingToStopped: ns0.objtypes.TransitionType
    stoppingToStoppedGuard: tmc_vartypes.BooleanGuardVariableType


o6.reference(TMCMachineStateMachineType, "i=41", "i=2311")


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6089",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7201",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=7201",
    browseName="ns=tmc;ResetProductionTotals",
    description="The Method ResetProductionTotals simultaneously resets the totals of the machine components \nbelonging to the following machine folders: DefectDetectionSensors, MaterialLoadingPoints, MaterialOutputPoints, MaterialRejectionPoints.",
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6089"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=7258",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7257",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(name="Command", dataType=o6.NodeId("ns=tmc;i=3007"), valueRank=-1, description=o6.LocalizedText("The command to be sent to the machine module."))
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=7259",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7257",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=7257",
    browseName="ns=tmc;SendCommand",
    description="The Method SendCommand sends a command to change the state of the control module state \nmachine remotely.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=7258"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=7259"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=7279",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7276",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ControlMode", dataType=o6.NodeId("ns=tmc;i=3023"), valueRank=-1, description=o6.LocalizedText("The control mode to be set to the machine module.")
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=7280",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7276",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=7276",
    browseName="ns=tmc;SetControlMode",
    description="The SetControlMode Method sets the control mode of the control module.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=7279"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=7280"]),
)


@o6.objecttype(
    nodeId="ns=tmc;i=1050",
    browseName="ns=tmc;ControlModuleLiveStatusType",
    displayName="ControlModuleLiveStatusType",
    description="The ControlModuleLiveStatusType ObjectType contains information about the real time status \nof the control module and provides affordances to control the control module remotely in real\ntime.",
)
class ControlModuleLiveStatusType(ns0.objtypes.BaseObjectType):
    acknowledgeAlarms: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7053"])
    alarms: ns0.objtypes.FolderType
    controlMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6448",
            browseName="ns=tmc;ControlMode",
            description="The ControlMode describes the current control mode of the equipment module.",
            dataType=tmc_datypes.ControlModeEnumeration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    data: ns0.objtypes.FolderType | None
    interlocks: ns0.objtypes.FolderType | None
    measurements: ns0.objtypes.FolderType | None
    processControlLoops: ns0.objtypes.FolderType | None
    sendCommand: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7257"])
    setControlMode: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7276"])
    state: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=7282",
            browseName="ns=tmc;State",
            description="The State Property describes the status of the state machine controlling the control module. State provides \na subset of the information of the state machine, when the latter is implemented.",
            dataType=tmc_datypes.StateEnumeration,
        )
    )
    stateMachine: TMCStateMachineType | None


o6.reference(ControlModuleLiveStatusType, "i=41", "i=10523")


@o6.objecttype(
    nodeId="ns=tmc;i=1052",
    browseName="ns=tmc;ControlModuleSetupType",
    displayName="ControlModuleSetupType",
    description="The ControlModuleSetupType ObjectType contains the value of all the settings required to run \nas well as affordances to validate and load settings for the control module.",
)
class ControlModuleSetupType(ns0.objtypes.BaseObjectType):
    langleSetupItemRangle: ns0.vartypes.DataItemType | None = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=tmc;i=7288",
            browseName="ns=tmc;<SetupItem>",
            description="This property describes a setting which belongs to the ControlModule instance.",
            modellingRule="OptionalPlaceholder",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1056",
    browseName="ns=tmc;AnalogInputSetupType",
    displayName="AnalogInputSetupType",
    description="The AnalogInputSetupType ObjectType provides settings and other affordance to set up an \nanalog input.",
)
class AnalogInputSetupType(ControlModuleSetupType):
    forcedValue: ns0.vartypes.AnalogItemType


@o6.objecttype(
    nodeId="ns=tmc;i=1059",
    browseName="ns=tmc;ValveSetupType",
    displayName="ValveSetupType",
    description="The ValveSetupType ObjectType provides aggregates computed by the underlying system for \na valve.",
)
class ValveSetupType(ControlModuleSetupType):
    positionSetPoint: ns0.vartypes.AnalogItemType | None


@o6.objecttype(
    nodeId="ns=tmc;i=1062",
    browseName="ns=tmc;ControlModuleType",
    displayName="ControlModuleType",
    description="The ControlModuleType ObjectType represents a control module according to the ISA 95 \nPhysical Structure.",
)
class ControlModuleType(TMCDeviceType):
    aggregates: ControlModuleAggregatesType | None
    configuration: ControlModuleConfigurationType
    liveStatus: ControlModuleLiveStatusType
    setup: ControlModuleSetupType | None = o6.hasComponent(
        ControlModuleSetupType(
            nodeId="ns=tmc;i=5143", browseName="ns=tmc;Setup", description="Setup provides the value of all the digital settings required to run the control module."
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1063", browseName="ns=tmc;AnalogInputType", displayName="AnalogInputType", description="The AnalogInputType ObjectType describes an analog input signal."
)
class AnalogInputType(ControlModuleType):
    rawValue: ns0.vartypes.AnalogItemType
    setup: AnalogInputSetupType
    value: ns0.vartypes.AnalogItemType


@o6.objecttype(
    nodeId="ns=tmc;i=1064", browseName="ns=tmc;DigitalInputType", displayName="DigitalInputType", description="The DigitalInputType ObjectType describes a digital input signal."
)
class DigitalInputType(ControlModuleType):
    setup: DigitalInputSetupType
    value: ns0.vartypes.TwoStateDiscreteType


@o6.objecttype(nodeId="ns=tmc;i=1066", browseName="ns=tmc;SensorType", displayName="SensorType", description="The MotorType ObjectType describes a sensor.")
class SensorType(ControlModuleType):
    setup: ControlModuleSetupType = o6.hasComponent(ControlModuleSetupType(nodeId="ns=tmc;i=5263", browseName="ns=tmc;Setup", description="The settings to set up the motor."))


@o6.objecttype(nodeId="ns=tmc;i=1067", browseName="ns=tmc;ValveType", displayName="ValveType", description="The MotorType ObjectType describes a valve.")
class ValveType(ControlModuleType):
    aggregates: ValveAggregatesType
    configuration: ControlModuleConfigurationType
    setup: ValveSetupType = o6.hasComponent(ValveSetupType(nodeId="ns=tmc;i=5293", browseName="ns=tmc;Setup", description="The settings to set up the valve."))


@o6.objecttype(
    nodeId="ns=tmc;i=1053",
    browseName="ns=tmc;ValveAggregatesType",
    displayName="ValveAggregatesType",
    description="The ValveAggregatesType ObjectType provides aggregates computed by the underlying \nsystem for an analog input.",
)
class ValveAggregatesType(ControlModuleAggregatesType):
    cycleCounter: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=7303", browseName="ns=tmc;CycleCounter", description="The total number of times the solenoid valve was energized and de-energised.", dataType=o6.UInt32
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1054",
    browseName="ns=tmc;MotorAggregatesType",
    displayName="MotorAggregatesType",
    description="The MotorAggregatesType ObjectType provides aggregates computed by the underlying \nsystem for an analog input.",
)
class MotorAggregatesType(ControlModuleAggregatesType):
    totalRunningHours: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=7310", browseName="ns=tmc;TotalRunningHours", description="The total number of running hours for the motor.", dataType=o6.UInt32
        )
    )
    totalStartStopCounter: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=7311", browseName="ns=tmc;TotalStartStopCounter", description="The total number of times the motor was started and stopped.", dataType=o6.UInt32
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1057",
    browseName="ns=tmc;DigitalInputSetupType",
    displayName="DigitalInputSetupType",
    description="The DigitalInputSetupType ObjectType provides settings and other affordance to set up an \nanalog input.",
)
class DigitalInputSetupType(ControlModuleSetupType):
    forcedValue: ns0.vartypes.DataItemType = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=tmc;i=7313",
            browseName="ns=tmc;ForcedValue",
            description="The value to set as the input Value when ControlMode is MANUAL.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=7322",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7314",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="RootCauseGroupList", dataType=o6.NodeId("ns=tmc;i=3030"), valueRank=1, description=o6.LocalizedText("The complete list of root cause groups.")
        ),
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure.\n"),
        ),
    ],
)
o6.call(
    nodeId="ns=tmc;i=7314",
    browseName="ns=tmc;GetRootCauseGroupList",
    description="The GetRootCauseGroupList Method returns the complete list of root cause groups as persisted \nby the server.",
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=7322"]),
)


@o6.objecttype(
    nodeId="ns=tmc;i=1058",
    browseName="ns=tmc;MotorSetupType",
    displayName="MotorSetupType",
    description="The MotorSetupType ObjectType provides settings and other affordances to set up a motor.",
)
class MotorSetupType(ControlModuleSetupType):
    direction: ns0.vartypes.DataItemType | None = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=tmc;i=7317",
            browseName="ns=tmc;Direction",
            description="The rotation direction of the motor.",
            dataType=tmc_datypes.MotorDirectionEnumeration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=tmc;i=1065", browseName="ns=tmc;MotorType", displayName="MotorType", description="The MotorType ObjectType describes a motor.")
class MotorType(ControlModuleType):
    aggregates: MotorAggregatesType
    setup: MotorSetupType = o6.hasComponent(MotorSetupType(nodeId="ns=tmc;i=5258", browseName="ns=tmc;Setup", description="The settings to set up the motor"))


o6.call(nodeId="ns=tmc;i=7350", browseName="ns=pack_ml;Hold")

o6.call(nodeId="ns=tmc;i=7351", browseName="ns=pack_ml;Reset")

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6935",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7352",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Parameter",
            dataType=o6.NodeId("ns=pack_ml;i=16"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("The array of parameter that can be used by the method"),
        )
    ],
)
o6.call(nodeId="ns=tmc;i=7352", browseName="ns=pack_ml;Start", inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6935"]))

o6.call(nodeId="ns=tmc;i=7353", browseName="ns=pack_ml;Suspend")

o6.call(nodeId="ns=tmc;i=7357", browseName="ns=pack_ml;Unhold")

o6.call(nodeId="ns=tmc;i=7358", browseName="ns=pack_ml;Unsuspend")

o6.call(nodeId="ns=tmc;i=7361", browseName="ns=pack_ml;ToComplete")


@o6.objecttype(nodeId="ns=tmc;i=1028", browseName="ns=tmc;TMCExecuteStateMachineType", displayName="TMCExecuteStateMachineType")
class TMCExecuteStateMachineType(pack_ml.objtypes.PackMLExecuteStateMachineType):
    complete: ns0.objtypes.StateType
    completeSubstate: ns0.objtypes.StateMachineType | None
    completeToResetting: ns0.objtypes.TransitionType
    completeToResettingGuard: tmc_vartypes.BooleanGuardVariableType | None
    completing: ns0.objtypes.StateType
    completingToComplete: ns0.objtypes.TransitionType
    completingToCompleteGuard: tmc_vartypes.BooleanGuardVariableType | None
    execute: ns0.objtypes.StateType
    executeSubstate: ns0.objtypes.StateMachineType | None
    executeToCompleting: ns0.objtypes.TransitionType
    executeToCompletingGuard: tmc_vartypes.BooleanGuardVariableType | None
    executeToHolding: ns0.objtypes.TransitionType
    executeToHoldingGuard: tmc_vartypes.BooleanGuardVariableType | None
    executeToSuspending: ns0.objtypes.TransitionType
    executeToSuspendingGuard: tmc_vartypes.BooleanGuardVariableType | None
    held: ns0.objtypes.StateType
    heldToUnholding: ns0.objtypes.TransitionType
    heldToUnholdingGuard: tmc_vartypes.BooleanGuardVariableType | None
    hold: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7350"])
    holding: ns0.objtypes.StateType
    holdingToHeld: ns0.objtypes.TransitionType
    holdingToHeldGuard: tmc_vartypes.BooleanGuardVariableType | None
    idle: ns0.objtypes.StateType
    idleSubstate: ns0.objtypes.StateMachineType | None
    idleToStarting: ns0.objtypes.TransitionType
    idleToStartingGuard: tmc_vartypes.BooleanGuardVariableType
    lastTransition: ns0.vartypes.FiniteTransitionVariableType
    reset: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7351"])
    resetting: ns0.objtypes.StateType
    resettingToIdle: ns0.objtypes.TransitionType
    resettingToIdleGuard: tmc_vartypes.BooleanGuardVariableType
    start: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7352"])
    starting: ns0.objtypes.StateType
    startingToExecute: ns0.objtypes.TransitionType
    startingToExecuteGuard: tmc_vartypes.BooleanGuardVariableType
    startingToHolding: ns0.objtypes.TransitionType
    startingToHoldingGuard: tmc_vartypes.BooleanGuardVariableType | None
    suspend: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7353"])
    suspended: ns0.objtypes.StateType
    suspendedToHolding: ns0.objtypes.TransitionType
    suspendedToHoldingGuard: tmc_vartypes.BooleanGuardVariableType | None
    suspendedToUnsuspending: ns0.objtypes.TransitionType
    suspendedToUnsuspendingGuard: tmc_vartypes.BooleanGuardVariableType | None
    suspending: ns0.objtypes.StateType
    suspendingToHolding: ns0.objtypes.TransitionType
    suspendingToHoldingGuard: tmc_vartypes.BooleanGuardVariableType | None
    suspendingToSuspended: ns0.objtypes.TransitionType
    suspendingToSuspendedGuard: tmc_vartypes.BooleanGuardVariableType | None
    toComplete: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7361"])
    unhold: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7357"])
    unholding: ns0.objtypes.StateType
    unholdingToExecute: ns0.objtypes.TransitionType
    unholdingToExecuteGuard: tmc_vartypes.BooleanGuardVariableType | None
    unholdingToHolding: ns0.objtypes.TransitionType
    unholdingToHoldingGuard: tmc_vartypes.BooleanGuardVariableType | None
    unsuspend: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7358"])
    unsuspending: ns0.objtypes.StateType
    unsuspendingToExecute: ns0.objtypes.TransitionType
    unsuspendingToExecuteGuard: tmc_vartypes.BooleanGuardVariableType | None
    unsuspendingToHolding: ns0.objtypes.TransitionType
    unsuspendingToHoldingGuard: tmc_vartypes.BooleanGuardVariableType | None


o6.reference(TMCExecuteStateMachineType, "i=41", "i=2311")


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6184",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7428",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Enable", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("Specifies if the method enables or disables the defect reason"))],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6189",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7428",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=7428",
    browseName="ns=tmc;SetDetectionMode",
    description="The Method SetDetectionMode enables or disables the defect reason.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6184"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6189"]),
)


@o6.objecttype(
    nodeId="ns=tmc;i=1041",
    browseName="ns=tmc;DefectReasonType",
    displayName="DefectReasonType",
    description="The DefectReasonType describes a defect reason that is monitored by a SensorFunction.",
)
class DefectReasonType(ns0.objtypes.BaseObjectType):
    detectionCountMasterTotal: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=7291",
            browseName="ns=tmc;DetectionCountMasterTotal",
            description="The total number of times the defect reason occurred. The total is never reset to zero.",
            dataType=o6.UInt64,
        )
    )
    detectionCountTotal: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=7349",
            browseName="ns=tmc;DetectionCountTotal",
            description="The total number of times a defect reason occurred. The total is reset to zero only when the \nResetProductionTotals method in the MachineModuleProductionType is executed successfully.",
            dataType=o6.UInt64,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    detectionMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=7359",
            browseName="ns=tmc;DetectionMode",
            description="When DetectionMode is True, the defect reason is triggered. When DetectionMode is False, the \ndefect reason is not active, i.e. never triggered.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    setDetectionMode: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7428"])
    uIInfo: UIInformationType | None


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6233",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7437",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=7443",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7437",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Features", dataType=o6.ByteString, valueRank=1, description=o6.LocalizedText("The list of binary profiles to be used as references for a detection system.")
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=7437",
    browseName="ns=tmc;LoadReferenceFeatures",
    description="The Method LoadReferenceFeatures loads binary profiles to be used as references for defect detection.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=7443"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6233"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=7441",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7440",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Enable", dataType=o6.Boolean, valueRank=-1, description=o6.LocalizedText("Specifies if the method enables or disables the defect detection sensor")
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=7442",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7440",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=7440",
    browseName="ns=tmc;SetDetectionMode",
    description="The method SetDetectionMode enables or disables the detection function and the underneath defect reasons.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=7441"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=7442"]),
)


@o6.objecttype(
    nodeId="ns=tmc;i=1044",
    browseName="ns=tmc;SensorFunctionType",
    displayName="SensorFunctionType",
    description="The SensorFunctionType describes a single measuring function or quality sampling function.",
)
class SensorFunctionType(ns0.objtypes.BaseObjectType):
    detectionMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6193",
            browseName="ns=tmc;DetectionMode",
            description="When DetectionMode is True, the sensor function measures the sensor value and the inner \ndefect reasons are enabled, meaning they can be active or not.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langleDefectReasonRangle: DefectReasonType | None
    loadReferenceFeatures: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7437"])
    sensorValue: ns0.vartypes.AnalogUnitType | None
    setDetectionMode: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7440"])
    uIInfo: UIInformationType | None


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=7467",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7465",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Enable",
            dataType=o6.Boolean,
            valueRank=-1,
            description=o6.LocalizedText("Specifies if the method enables, when True, or disables, when False, the defect detection \nsensor."),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=7468",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=7465",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=7465",
    browseName="ns=tmc;SetDetectionMode",
    description="The Method SetDetectionMode enables or disables the defect detection sensor.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=7467"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=7468"]),
)


@o6.objecttype(
    nodeId="ns=tmc;i=1025",
    browseName="ns=tmc;DefectDetectionSensorType",
    displayName="DefectDetectionSensorType",
    description="The DefectDetectionSensorType represents a sensor or sensing system fitted to the machine \nmodule that detects product defects or a quality sampling point that can be triggered by an \noperator.",
)
class DefectDetectionSensorType(TMCDeviceType):
    data: ns0.objtypes.FolderType | None
    detectionCountMasterTotal: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=7460",
            browseName="ns=tmc;DetectionCountMasterTotal",
            description="The total number of times a detection occurred. The total is never reset to zero.",
            dataType=o6.UInt64,
        )
    )
    detectionCountTotal: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=7461",
            browseName="ns=tmc;DetectionCountTotal",
            description="The total number of times a detection occurred. The total is reset to zero only when the \nResetProductionTotals method in the MachineModuleProductionType is executed successfully.",
            dataType=o6.UInt64,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    detectionMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=7462",
            browseName="ns=tmc;DetectionMode",
            description="When DetectionMode is True, the defect detection sensor or system detects defects and the \ninner sensor functions are enabled, meaning they can be active or not.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langleSensorFunctionRangle: SensorFunctionType
    setDetectionMode: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7465"])


@o6.objecttype(
    nodeId="ns=tmc;i=1023",
    browseName="ns=tmc;MaterialRejectionPointType",
    displayName="MaterialRejectionPointType",
    description="The MaterialRejectionPointType describes a device that is capable of rejecting product from the \nproduct flow.",
)
class MaterialRejectionPointType(TMCDeviceType):
    mES_ID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=7356",
            browseName="ns=tmc;MES_ID",
            description="Unique identifier for the material point in an external system, e.g. MES.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
            historizing=True,
        )
    )
    materialDefinition: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6673",
            browseName="ns=tmc;MaterialDefinition",
            description="The material definition for the material to be rejected at the rejection trap",
            dataType=tmc_datypes.MaterialDefinitionType,
        )
    )
    materialPointDefinition: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=7698",
            browseName="ns=tmc;MaterialPointDefinition",
            description="The Property MaterialPointDefinition contains the identification of the material point and the material that is processed.",
            dataType=tmc_datypes.MaterialPointType,
            value=tmc_datypes.MaterialPointType(iD="", materialCapability=[], connectedMaterialPoint=o6.ExpandedNodeId("i=0"), propagatesProductionOrder=False),
            historizing=True,
        )
    )
    rejectedMaterialMasterTotal: tmc_vartypes.MaterialQuantityVariableType
    rejectedMaterialRatio: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=6282",
            browseName="ns=tmc;RejectedMaterialRatio",
            description="The Variable MaterialRejectedRatio is the ratio of the total material rejected \n(MaterialRejectedTotal) over the total good product and is computed by the underlying \nsystem.",
            dataType=o6.Double,
            value=0.0,
        )
    )
    rejectedMaterialTotal: tmc_vartypes.MaterialQuantityVariableType
    rejectionCountMasterTotal: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=6271",
            browseName="ns=tmc;RejectionCountMasterTotal",
            description="The total number of times the rejection trap was triggered. The total is never reset to zero.",
            dataType=o6.UInt64,
            value=0,
        )
    )
    rejectionCountTotal: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=6264",
            browseName="ns=tmc;RejectionCountTotal",
            description="The total number of times the rejection trap was triggered. The total is reset to zero only\nwhen the ResetRejectionTotals is invoked.",
            dataType=o6.UInt64,
            value=0,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    rejectionMode: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=tmc;i=6275"])
    rejectionsRatio: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=6281",
            browseName="ns=tmc;RejectionsRatio",
            description="The Variable RejectionsRatio is the ratio between the good product output total and the \nrejected quantity total.",
            dataType=o6.Double,
            value=0.0,
            accessLevel=5,
            userAccessLevel=1,
            historizing=True,
        )
    )
    setRejectionMode: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7063"])


@o6.objecttype(
    nodeId="ns=tmc;i=1081",
    browseName="ns=tmc;SubCarrierUnloadedLogType",
    displayName="SubCarrierUnloadedLogType",
    description="The SubCarrierUnloadedLogType event is generated when a (sub)carrier or a material sublot \nis unloaded from a carrier.",
)
class SubCarrierUnloadedLogType(LogbookEventType):
    carrierID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6088",
            browseName="ns=tmc;CarrierID",
            description="The unique identifier for the carrier that has been unloaded with the subcarrier.",
            dataType=o6.String,
        )
    )
    subCarrierID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=8871", browseName="ns=tmc;SubCarrierID", description="The unique identifier for the subcarrier that has been unloaded.", dataType=o6.String
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1055",
    browseName="ns=tmc;CarrierSublotsChangeLogType",
    displayName="CarrierSublotsChangeLogType",
    description="The CarrierSublotsChangeLogType event is generated when the sublots in a carrier changes.",
)
class CarrierSublotsChangeLogType(LogbookEventType):
    carrierID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=8873", browseName="ns=tmc;CarrierID", description="The unique identifier for the carrier whose payload is modified", dataType=o6.String
        )
    )
    sublots: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=8874",
            browseName="ns=tmc;Sublots",
            description="The sublots after the modification.",
            dataType=tmc_datypes.MaterialSublotType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1078",
    browseName="ns=tmc;SubCarrierLoadedLogType",
    displayName="SubCarrierLoadedLogType",
    description="The SubCarrierLoadedLogType event is generated when a (sub)carrier or a material lot is \nloaded onto a carrier.",
)
class SubCarrierLoadedLogType(LogbookEventType):
    carrierID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6087", browseName="ns=tmc;CarrierID", description="The unique identifier of the carrier where the subcarrier is loaded.", dataType=o6.String
        )
    )
    subCarrierID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=8875", browseName="ns=tmc;SubCarrierID", description="The unique identifier for the subcarrier that is loaded on the carrier.", dataType=o6.String
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1079",
    browseName="ns=tmc;SubCarrierLoadingEndedLogType",
    displayName="SubCarrierLoadingEndedLogType",
    description="The SubCarrierLoadingEndedLogType event is generated when the loading of a carrier is \ncomplete.",
)
class SubCarrierLoadingEndedLogType(LogbookEventType):
    carrierID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=8876", browseName="ns=tmc;CarrierID", description="The unique identifier for the carrier that ended loading.", dataType=o6.String
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1080",
    browseName="ns=tmc;SubCarrierLoadingStartedLogType",
    displayName="SubCarrierLoadingStartedLogType",
    description="The SubCarrierLoadingStartedLogType event is generated when the loading onto a carrier is \nstarted.",
)
class SubCarrierLoadingStartedLogType(LogbookEventType):
    carrierID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=8877", browseName="ns=tmc;CarrierID", description="The unique identifier for the carrier that staretd loading.", dataType=o6.String
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1082",
    browseName="ns=tmc;SubCarrierUnloadingEndedLogType",
    displayName="SubCarrierUnloadingEndedLogType",
    description="The SubCarrierUnloadingEndedLogType event is generated when the unloading from a carrier \nis complete.",
)
class SubCarrierUnloadingEndedLogType(LogbookEventType):
    carrierID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=8878", browseName="ns=tmc;CarrierID", description="The unique identifier for the carrier that ended unloading.", dataType=o6.String
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1083",
    browseName="ns=tmc;SubCarrierUnloadingStartedLogType",
    displayName="SubCarrierUnloadingStartedLogType",
    description="The SubCarrierUnloadingStartedLogType event is generated when the unloading from a carrier \nis started.",
)
class SubCarrierUnloadingStartedLogType(LogbookEventType):
    carrierID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=8879", browseName="ns=tmc;CarrierID", description="The unique identifier for the carrier that started unloading.", dataType=o6.String
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=9125",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=9030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="IDs",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("The IDs of the elements of the Definitions array whose MES_ID shall be changed if the method executes successfully."),
        ),
        ns0.datatypes.Argument(name="MESIDs", dataType=o6.String, valueRank=1, arrayDimensions=[0], description=o6.LocalizedText("The values of the MES_IDs to be set.")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=19982",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=9030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=9030",
    browseName="ns=tmc;SetDataSetListMESID",
    description="The SetDataSetListMESID Method sets the MES_ID of one or more items of the array Definitions contained in the DataSetList.\nEach item of Definitions is identified by its ID.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=9125"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=19982"]),
)


@o6.objecttype(
    nodeId="ns=tmc;i=1013",
    browseName="ns=tmc;MachineModuleConfigurationType",
    displayName="MachineModuleConfigurationType",
    description="The MachineModuleConfigurationType provides descriptions for settings, stop reasons and root \ncauses as well as affordances to make modifications.",
)
class MachineModuleConfigurationType(ns0.objtypes.BaseObjectType):
    dataSetList: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6175",
            browseName="ns=tmc;DataSetList",
            description="The Property DataSetList of type DataSetDefinition contains the descriptors for all the \nparameters used to set up the machine.",
            dataType=tmc_datypes.DataSetDefinitionType,
            value=tmc_datypes.DataSetDefinitionType(iD="", definitions=[]),
        )
    )
    getDataSetList: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=7104"])
    getRootCauseGroupList: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=7314"])
    getRootCauseList: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=7105"])
    getStopReasonList: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=7106"])
    lastChangeDate: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6215",
            browseName="ns=tmc;LastChangeDate",
            description="The Property LastChangeDate is the date and time of the last change applied to the machine \nmodule configuration and the effective date of the modification.",
            dataType=ns0.datatypes.UtcTime,
            value=o6.DateTime("2000-01-01T00:00:00Z"),
        )
    )
    longestMicroStopDuration: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6167",
            browseName="ns=tmc;LongestMicroStopDuration",
            description="The Property LongestMicroStopDuration is the maximum duration of a micro-stop in seconds, \nlonger stops are not micro-stops. Operators are not required to enter a root cause for micro-stops.",
            dataType=o6.Double,
            value=0.0,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    rootCauseGroupList: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=7269",
            browseName="ns=tmc;RootCauseGroupList",
            description="The Property RootCauseGroupList is the list of groups that root causes can be grouped in. \nThey are defined by the end user.",
            dataType=tmc_datypes.RootCauseGroupType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    rootCauseList: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6156",
            browseName="ns=tmc;RootCauseList",
            description="The Property RootCauseList is the complete list of the root causes that the end user has defined \nto classify and organize the downtime due to the machine module stops. The RootCauseList is \nuser defined.",
            dataType=tmc_datypes.RootCauseMessageType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    rootCauseListInputIsMandatory: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6165",
            browseName="ns=tmc;RootCauseListInputIsMandatory",
            description="The Property RootCauseListInputIsMandatory is true when the operator is mandatorily required \nto select the root cause that best describes the current stop situation. For micro- stops such \nrequirement does not apply.",
            dataType=o6.Boolean,
            value=False,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    setDataSetListMESID: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=9030"])
    setRootCauseLists: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=7072"])
    stopReasonList: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6158",
            browseName="ns=tmc;StopReasonList",
            description="The Property StopReasonList is a list containing the descriptors for all the possible machine \nmodule messages, including alarms and warnings. Messages include their localization. The list is \ndefined, created and maintained by the OEM.",
            dataType=tmc_datypes.MessageType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=6401",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=9178",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Sublots", dataType=o6.NodeId("ns=tmc;i=3025"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText("The material sublots to be loaded to the carrier.")
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=9213",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=9178",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=9178",
    browseName="ns=tmc;LoadSublots",
    description="The LoadSublot Method requests the underlying system to load one or more material sublots into the \ncarrier that is currently being loaded.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=6401"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=9213"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=9268",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=9267",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="DocumentToBeLoaded",
            dataType=o6.ByteString,
            valueRank=-1,
            description=o6.LocalizedText("The document, as a byte string, to be transferred to the Documentation folder.\n"),
        ),
        ns0.datatypes.Argument(
            name="DocumentName", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The document name to be associated to the document in the underlying system.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=9269",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=9267",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure.\n"),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=9267",
    browseName="ns=tmc;LoadMachineModuleDocumentation",
    description="The LoadMachineModuleDocumentation Method allows to securely load any machine module \ndocumentation to the documentation repository DocumentationRep folder where it can be reached by \napplications.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=9268"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=9269"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=9271",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=9270",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="DocumentName", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The document name to be associated to the document in the underlying system.")
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=9272",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=9270",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure.\n"),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=9270",
    browseName="ns=tmc;RemoveMachineModuleDocumentation",
    description="The RemoveMachineModuleDocumentation Method allows to securely remove, i.e. permanently delete,\nany machine module documentation from the documentation repository Documentation.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=9271"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=9272"]),
)


@o6.objecttype(
    nodeId="ns=tmc;i=1004", browseName="ns=tmc;MachineModuleType", displayName="MachineModuleType", description="The MachineModuleType represents a machine module or workcentre."
)
class MachineModuleType(TMCDeviceType):
    configuration: MachineModuleConfigurationType
    controlModules: ns0.objtypes.FolderType | None
    defectDetectionSensors: ns0.objtypes.FolderType | None
    equipmentModules: ns0.objtypes.FolderType | None
    liveStatus: MachineModuleLiveStatusType
    materialBuffers: ns0.objtypes.FolderType | None
    materialLoadingPoints: ns0.objtypes.FolderType | None
    materialLocations: ns0.objtypes.FolderType | None
    materialOutputPoints: ns0.objtypes.FolderType | None
    materialRejectionPoints: ns0.objtypes.FolderType | None
    pastSpecificationRecords: ns0.objtypes.FolderType | None
    processControlLoops: ns0.objtypes.FolderType | None
    processItems: ns0.objtypes.FolderType | None
    production: MachineModuleProductionType | None
    remote: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=9311",
            browseName="ns=tmc;Remote",
            description="When Remote is True, all methods exposed by the machine module and contained objects are \nexecuted and all variables marked as RW can be written to.",
            dataType=o6.Boolean,
        )
    )
    setup: MachineModuleSetupType | None
    specification: MachineModuleSpecificationType | None


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=9654",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=9653",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="POHeaderToStart", dataType=o6.NodeId("ns=tmc;i=3016"), valueRank=-1, description=o6.LocalizedText("The production order to be started.")),
        ns0.datatypes.Argument(
            name="SourceMaterialLoadingPointIDs",
            dataType=o6.String,
            valueRank=1,
            description=o6.LocalizedText("The list of material loading points that are going to be used by the production order to be started."),
        ),
        ns0.datatypes.Argument(
            name="DestinationMaterialOutputPointIDs",
            dataType=o6.String,
            valueRank=1,
            description=o6.LocalizedText("The list of material outputs that are going to be used by the production order to be started."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=9655",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=9653",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure.\n"),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=9653", browseName="ns=tmc;StartAssignedProductionOrder", inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=9654"]), outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=9655"])
)


@o6.objecttype(
    nodeId="ns=tmc;i=1070",
    browseName="ns=tmc;EquipmentModuleSetupType",
    displayName="EquipmentModuleSetupType",
    description="The EquipmentModuleSetupType ObjectType contains the value of all the settings required to \nrun as well as affordances to validate and load settings for the equipment module.",
)
class EquipmentModuleSetupType(ns0.objtypes.BaseObjectType):
    langleSetupItemRangle: ns0.vartypes.DataItemType | None = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=tmc;i=9682",
            browseName="ns=tmc;<SetupItem>",
            description="This property describes a setting which belongs to the EquipmentModule instance.",
            modellingRule="OptionalPlaceholder",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1071",
    browseName="ns=tmc;EquipmentModuleType",
    displayName="EquipmentModuleType",
    description="The EquipmentModuleType ObjectType represents an equipment module according to the ISA \n95 Physical Structure.",
)
class EquipmentModuleType(TMCDeviceType):
    configuration: EquipmentModuleConfigurationType
    controlModules: ns0.objtypes.FolderType | None
    liveStatus: EquipmentModuleLiveStatusType
    processControlLoops: ns0.objtypes.FolderType | None
    processItems: ns0.objtypes.FolderType | None
    setup: EquipmentModuleSetupType = o6.hasComponent(
        EquipmentModuleSetupType(
            nodeId="ns=tmc;i=5303",
            browseName="ns=tmc;Setup",
            description="The Setup Object contains the value of all the settings (including mechanical adjustments) required to run \nproduction as well as affordances to validate and load settings for the equipment module.",
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=10316",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=10315",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(name="Message", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("The message that will be displayed for the external alarm."))
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=10317",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=10315",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=10315",
    browseName="ns=tmc;SetMessage",
    description="The Method SetMessage sets the Message that the underlying system will display for the alarm.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=10316"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=10317"]),
)


@o6.objecttype(
    nodeId="ns=tmc;i=1048",
    browseName="ns=tmc;ExternalAlarmType",
    displayName="ExternalAlarmType",
    description="The ExternalAlarmType EventType is an alarm that is managed by the underlying system \n(display, acknowledge, retain, reset, etc) while the alarm condition is generated and set by an \nexternal system connected as a client.",
)
class ExternalAlarmType(ns0.objtypes.DiscreteAlarmType):
    externalAlarmCondition: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6692",
            browseName="ns=tmc;ExternalAlarmCondition",
            description="The condition that causes the alarm.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    setMessage: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=10315"])


@o6.objecttype(
    nodeId="ns=tmc;i=1049",
    browseName="ns=tmc;ProcessControlLoopType",
    displayName="ProcessControlLoopType",
    description="The ProcessControlLoopType is the general description of a control loop consisting of the \ndesired value (SetPoint) for a measured value (ProcessValue) which is obtained by acting on \nan actuator (ControlValue).",
)
class ProcessControlLoopType(TMCDeviceType):
    controlValue: ProcessControlItemType
    externalAlarms: ns0.objtypes.FolderType
    processValue: ProcessControlItemType
    setPoint: ProcessControlItemType | None
    watchdogEnabled: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=10483",
            browseName="ns=tmc;WatchdogEnabled",
            description="When WatchdogEnable is True, if a ProcessControlLoop component’s RemoteControl is True and the time \nbetween two consecutive writes of the RemoteAnalogMeasurement is longer than WatchdogTimeout, \nthen the underlying system will generate an alarm, set RemoteControl to False and take control of the \nloop. When WatchdogEnable is False, no watchdog alarm is generated.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    watchdogTimeout: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=10490",
            browseName="ns=tmc;WatchdogTimeout",
            description="The longest time between two write actions before a watchdog alarm is generated by the underlying \nsystem. The value is expressed in milliseconds.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


o6.reference(ProcessControlLoopType, "i=41", ExternalAlarmType)


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=10821",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=10820",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="SublotIDs", dataType=o6.String, valueRank=1, arrayDimensions=[0], description=o6.LocalizedText("The unique identifiers of the material sublots to be unloaded.")
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=10822",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=10820",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=10820",
    browseName="ns=tmc;UnloadSublots",
    description="The UnloadSublots Method requests the underlying system to unload one or more sublots from the \ncarrier that is currently being unloaded.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=10821"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=10822"]),
)


@o6.objecttype(
    nodeId="ns=tmc;i=1068",
    browseName="ns=tmc;EquipmentModuleConfigurationType",
    displayName="EquipmentModuleConfigurationType",
    description="The EquipmentModuleConfigurationType ObjectType contains all digital settings, stop reasons \nand root causes of an equipment module.",
)
class EquipmentModuleConfigurationType(ns0.objtypes.BaseObjectType):
    langleConfigurationItemRangle: ns0.vartypes.DataItemType | None = o6.hasComponent(
        ns0.vartypes.DataItemType(
            nodeId="ns=tmc;i=9681",
            browseName="ns=tmc;<ConfigurationItem>",
            description="A data item used for configuration of the equipment module such as for example a setting, stop reason, \nroot cause or other editable field. The data item type is any BaseDataType, e.g. string, float, integer and so \non, for maximum flexibility.",
            modellingRule="OptionalPlaceholder",
        )
    )
    lastChangeDate: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=11661",
            browseName="ns=tmc;LastChangeDate",
            description="The UTC date and time when the configuration was last changed.",
            dataType=ns0.datatypes.UtcTime,
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=11663",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=11662",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=11662",
    browseName="ns=tmc;AcknowledgeAlarms",
    description="The AcknowledgeAlarms method acknowledges the alarms of the equipment module and control \nmodules belonging to it.",
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=11663"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=11702",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=11701",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(name="Command", dataType=o6.NodeId("ns=tmc;i=3007"), valueRank=-1, description=o6.LocalizedText("The command to be sent to the machine module."))
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=11703",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=11701",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=11701",
    browseName="ns=tmc;SendCommand",
    description="The Method SendCommand sends a command to change the state of the equipment module \nstate machine remotely.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=11702"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=11703"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=11705",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=11704",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ControlMode", dataType=o6.NodeId("ns=tmc;i=3023"), valueRank=-1, description=o6.LocalizedText("The control mode to be set to the machine module.")
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=11706",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=11704",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=11704",
    browseName="ns=tmc;SetControlMode",
    description="The SetControlMode Method sets the control mode of the equipment module.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=11705"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=11706"]),
)


@o6.objecttype(
    nodeId="ns=tmc;i=1069",
    browseName="ns=tmc;EquipmentModuleLiveStatusType",
    displayName="EquipmentModuleLiveStatusType",
    description="The EquipmentModuleLiveStatusType ObjectType contains information about the real time \nstatus of the equipment module and provides affordances to control the control module remotely \nin real time.",
)
class EquipmentModuleLiveStatusType(ns0.objtypes.BaseObjectType):
    acknowledgeAlarms: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=11662"])
    alarms: ns0.objtypes.FolderType
    controlMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=11699",
            browseName="ns=tmc;ControlMode",
            description="The ControlMode describes the current control mode of the equipment module.",
            dataType=tmc_datypes.ControlModeEnumeration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    data: ns0.objtypes.FolderType | None
    sendCommand: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=11701"])
    setControlMode: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=11704"])
    state: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=11707",
            browseName="ns=tmc;State",
            description="The State Property describes the status of the state machine controlling the equipment module. State \nprovides a subset of the information of the state machine, when the latter is implemented.",
            dataType=tmc_datypes.StateEnumeration,
        )
    )
    stateMachine: TMCStateMachineType | None


o6.reference(EquipmentModuleLiveStatusType, "i=41", "i=10523")


@o6.objecttype(
    nodeId="ns=tmc;i=1072",
    browseName="ns=tmc;ProductionOrderExecutionStateMachineType",
    displayName="ProductionOrderExecutionStateMachineType",
    description="The ProductionOrderExecutionStateMachineType provides state information about the \nexecution of a production order at a production line.",
)
class ProductionOrderExecutionStateMachineType(ns0.objtypes.FiniteStateMachineType):
    aborted: ns0.objtypes.StateType
    aborting: ns0.objtypes.StateType
    abortingToAborted: ns0.objtypes.TransitionType
    abortingToAbortedGuard: tmc_vartypes.BooleanGuardVariableType
    assigned: ns0.objtypes.StateType
    assignedToStarting: ns0.objtypes.TransitionType
    assignedToStartingGuard: tmc_vartypes.BooleanGuardVariableType
    assignedToUnassigning: ns0.objtypes.TransitionType
    assignedToUnassigningGuard: tmc_vartypes.BooleanGuardVariableType
    assignedToUnreleasing: ns0.objtypes.TransitionType
    assignedToUnreleasingGuard: tmc_vartypes.BooleanGuardVariableType
    assigning: ns0.objtypes.StateType
    assigningToAssigned: ns0.objtypes.TransitionType
    assigningToAssignedGuard: tmc_vartypes.BooleanGuardVariableType
    complete: ns0.objtypes.StateType
    completing: ns0.objtypes.StateType
    completingToAborting: ns0.objtypes.TransitionType
    completingToAbortingGuard: tmc_vartypes.BooleanGuardVariableType
    completingToComplete: ns0.objtypes.TransitionType
    completingToCompleteGuard: tmc_vartypes.BooleanGuardVariableType
    execute: ns0.objtypes.StateType
    executeToAborting: ns0.objtypes.TransitionType
    executeToAbortingGuard: tmc_vartypes.BooleanGuardVariableType
    executeToCompleting: ns0.objtypes.TransitionType
    executeToCompletingGuard: tmc_vartypes.BooleanGuardVariableType
    lastTransition: ns0.vartypes.FiniteTransitionVariableType
    machineModuleProductionOrders: ns0.objtypes.FolderType
    productionOrderHeader: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=11933",
            browseName="ns=tmc;ProductionOrderHeader",
            description="The ProductionOrderHeader of the production order in execution. When no production order is in execution, the ProductionOrderNumber in the ProductionOrderHeader is an empty string.",
            dataType=tmc_datypes.ProductionOrderHeaderType,
            value=tmc_datypes.ProductionOrderHeaderType(
                number="",
                producedMaterial=tmc_datypes.MaterialDefinitionType(
                    iD="",
                    mES_ID="",
                    baseUnitOfMeasure=ns0.datatypes.EUInformation(namespaceUri="", unitId=0, displayName=o6.LocalizedText()),
                    batchManaged=False,
                    groupID=None,
                    parentGroupID=None,
                    shelfLife=None,
                    properties=[],
                ),
                targetQuantity=0.0,
                continueAtJobEnd=False,
                targetStartTime=o6.DateTime("1900-01-01T00:00:00Z"),
                targetEndTime=o6.DateTime("1900-01-01T00:00:00Z"),
                dataSetID="",
                dataSetDescription=o6.LocalizedText(),
                materialListID="",
                materialListDescription=o6.LocalizedText(),
            ),
        )
    )
    released: ns0.objtypes.StateType
    releasedToAssigning: ns0.objtypes.TransitionType
    releasedToAssigningGuard: tmc_vartypes.BooleanGuardVariableType
    releasedToUnreleasing: ns0.objtypes.TransitionType
    releasedToUnreleasingGuard: tmc_vartypes.BooleanGuardVariableType
    releasing: ns0.objtypes.InitialStateType
    releasingToReleased: ns0.objtypes.TransitionType
    releasingToReleasedGuard: tmc_vartypes.BooleanGuardVariableType
    releasingToUnreleasing: ns0.objtypes.TransitionType
    releasingToUnreleasingGuard: tmc_vartypes.BooleanGuardVariableType
    starting: ns0.objtypes.StateType
    startingToAborting: ns0.objtypes.TransitionType
    startingToAbortingGuard: tmc_vartypes.BooleanGuardVariableType
    startingToExecute: ns0.objtypes.TransitionType
    startingToExecuteGuard: tmc_vartypes.BooleanGuardVariableType
    unassigning: ns0.objtypes.StateType
    unassigningToReleased: ns0.objtypes.TransitionType
    unassigningToReleasedGuard: tmc_vartypes.BooleanGuardVariableType
    unreleased: ns0.objtypes.StateType
    unreleasedToReleased: ns0.objtypes.TransitionType
    unreleasedToReleasedGuard: tmc_vartypes.BooleanGuardVariableType
    unreleasing: ns0.objtypes.StateType
    unreleasingToUnreleased: ns0.objtypes.TransitionType
    unreleasingToUnreleasedGuard: tmc_vartypes.BooleanGuardVariableType


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=11950",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=11949",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="POToAbort", dataType=o6.NodeId("ns=tmc;i=3016"), valueRank=-1, description=o6.LocalizedText("The Production Order to be aborted."))],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=11951",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=11949",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback", dataType=o6.NodeId("ns=tmc;i=3009"), valueRank=-1, description=o6.LocalizedText("The result of the execution of the method.")
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=11949",
    browseName="ns=tmc;AbortProductionOrder",
    description="The AbortProductionOrder Method is used to abort a production order that is in execution or starting or \ncompleting in the production line.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=11950"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=11951"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=11953",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=11952",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="POToAssign", dataType=o6.NodeId("ns=tmc;i=3016"), valueRank=-1, description=o6.LocalizedText("The Production Order Header to be assigned.")),
        ns0.datatypes.Argument(
            name="MachineModuleUserName",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("The user name of the machine modules to which the PO is assigned."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=11954",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=11952",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback", dataType=o6.NodeId("ns=tmc;i=3009"), valueRank=-1, description=o6.LocalizedText("The result of the execution of the method.")
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=11952",
    browseName="ns=tmc;AssignProductionOrder",
    description="The AssignProductionOrder Method is used to assign a production order to one infeed machine module \nwhere it shall be executed.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=11953"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=11954"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=11956",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=11955",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="POToComplete", dataType=o6.NodeId("ns=tmc;i=3016"), valueRank=-1, description=o6.LocalizedText("The Production Order Header to be completed.")
        ),
        ns0.datatypes.Argument(
            name="MachineModuleUserName", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The user name of the machine module where the PO is completed.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=11957",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=11955",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback", dataType=o6.NodeId("ns=tmc;i=3009"), valueRank=-1, description=o6.LocalizedText("The result of the execution of the method.")
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=11955",
    browseName="ns=tmc;CompleteProductionOrder",
    description="The CompleteProductionOrder Method is used to complete a production order in execution.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=11956"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=11957"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=11959",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=11958",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="POHeader", dataType=o6.NodeId("ns=tmc;i=3016"), valueRank=-1, description=o6.LocalizedText("The Production Order Header of the dataset to be retrieved.")
        ),
        ns0.datatypes.Argument(
            name="MachineModuleUserName",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText("The user name of the machine module for which the information is requested."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=11960",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=11958",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="DataSet", dataType=o6.NodeId("ns=tmc;i=3018"), valueRank=-1, description=o6.LocalizedText("The DataSet for the production order with Production Order Header.")
        ),
        ns0.datatypes.Argument(
            name="ExecutionFeedback", dataType=o6.NodeId("ns=tmc;i=3009"), valueRank=-1, description=o6.LocalizedText("The result of the execution of the method.")
        ),
    ],
)
o6.call(
    nodeId="ns=tmc;i=11958",
    browseName="ns=tmc;GetDataSet",
    description="The GetDataset Method is used to retrieve the data set from a production order header.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=11959"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=11960"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=11962",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=11961",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="POHeader", dataType=o6.NodeId("ns=tmc;i=3016"), valueRank=-1, description=o6.LocalizedText("The Production Order Header of the Material List to be retrieved.")
        ),
        ns0.datatypes.Argument(
            name="MachineModuleUserName",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText("The user name of the machine module for which the information is requested."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=11963",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=11961",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="MaterialList",
            dataType=o6.NodeId("ns=tmc;i=3037"),
            valueRank=-1,
            description=o6.LocalizedText("The Material List for the production order with Production Order Header."),
        ),
        ns0.datatypes.Argument(
            name="ExecutionFeedback", dataType=o6.NodeId("ns=tmc;i=3009"), valueRank=-1, description=o6.LocalizedText("The result of the execution of the method.")
        ),
    ],
)
o6.call(
    nodeId="ns=tmc;i=11961",
    browseName="ns=tmc;GetMaterialList",
    description="The GetMaterialList Method is used to retrieve the material list information from a production order \nheader.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=11962"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=11963"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=11965",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=11964",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="POHeader", dataType=o6.NodeId("ns=tmc;i=3016"), valueRank=-1, description=o6.LocalizedText("The Production Order Header of the Material List to be retrieved.")
        ),
        ns0.datatypes.Argument(
            name="MachineModuleUserName",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText("The user name of the machine module for which the information is requested."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=11966",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=11964",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ProductionOrder",
            dataType=o6.NodeId("ns=tmc;i=3038"),
            valueRank=-1,
            description=o6.LocalizedText("The complete Production Order with header Production Order Header."),
        ),
        ns0.datatypes.Argument(
            name="ExecutionFeedback", dataType=o6.NodeId("ns=tmc;i=3009"), valueRank=-1, description=o6.LocalizedText("The result of the execution of the method.")
        ),
    ],
)
o6.call(
    nodeId="ns=tmc;i=11964",
    browseName="ns=tmc;GetProductionOrder",
    description="The GetProductionOrder Method is used to retrieve the complete production order information starting \nwith a production order header as an input argument.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=11965"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=11966"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=12008",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=12007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="POToRelease",
            dataType=o6.NodeId("ns=tmc;i=3006"),
            valueRank=-1,
            description=o6.LocalizedText("The Production Order Header for the Production Order to be released."),
        ),
        ns0.datatypes.Argument(
            name="MachineModuleUserName", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The user name of the machine module where the PO is released.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=12009",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=12007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback", dataType=o6.NodeId("ns=tmc;i=3009"), valueRank=-1, description=o6.LocalizedText("The result of the execution of the method.")
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=12007",
    browseName="ns=tmc;ReleaseProductionOrder",
    description="The ReleaseProductionOrder Method is used to make a production order available to a machine module \nfor orchestrated execution in a production line (Process Cell according to ANSI/ISA-88.00.01-2010 \nPhysical Model).",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=12008"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=12009"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=12011",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=12010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(
            name="POToStart", dataType=o6.NodeId("ns=tmc;i=3016"), valueRank=-1, description=o6.LocalizedText("The Production Order Header for the Production Order to be started.")
        ),
        ns0.datatypes.Argument(
            name="MachineModuleUserName", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The user name of the machine module where the PO is started.")
        ),
        ns0.datatypes.Argument(
            name="SourceMaterialLoadingPointIDs",
            dataType=o6.String,
            valueRank=1,
            description=o6.LocalizedText("The MaterialLoadingPoints where input materials will be fed for the Production Order to be \nstarted."),
        ),
        ns0.datatypes.Argument(
            name="DestinationMaterialOutputPointIDs",
            dataType=o6.String,
            valueRank=1,
            description=o6.LocalizedText("The MaterialOutputPointss where output materials will be directed to for the Production Order to be started."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=12012",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=12010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback", dataType=o6.NodeId("ns=tmc;i=3009"), valueRank=-1, description=o6.LocalizedText("The result of the execution of the method.")
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=12010",
    browseName="ns=tmc;StartProductionOrder",
    description="The StartProductionOrder Method is used to start the execution of a production order at a machine \nmodule specifying the loading points that input materials will be fed to and the output points where output \nwill be directed.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=12011"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=12012"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=12014",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=12013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="POToUnassign",
            dataType=o6.NodeId("ns=tmc;i=3016"),
            valueRank=-1,
            description=o6.LocalizedText("The Production Order Header for the Production Order to be unassigned."),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=12015",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=12013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback", dataType=o6.NodeId("ns=tmc;i=3009"), valueRank=-1, description=o6.LocalizedText("The result of the execution of the method.")
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=12013",
    browseName="ns=tmc;UnassignProductionOrder",
    description="The UnAssignProductionOrder Method is used to unassign a production order previously assigned to \nan infeed machine module.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=12014"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=12015"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=12017",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=12016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="POToUnrelease",
            dataType=o6.NodeId("ns=tmc;i=3016"),
            valueRank=-1,
            description=o6.LocalizedText("The Production Order Header for the Production Order to be unreleased."),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=12018",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=12016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback", dataType=o6.NodeId("ns=tmc;i=3009"), valueRank=-1, description=o6.LocalizedText("The result of the execution of the method.")
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=12016",
    browseName="ns=tmc;UnreleaseProductionOrder",
    description="The UnreleaseProductionOrder Method is used to reverse the effect of the ReleaseProductionOrder\nmethod and make a previously released production order unavailable for assignment and production.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=12017"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=12018"]),
)


@o6.objecttype(
    nodeId="ns=tmc;i=1073",
    browseName="ns=tmc;ProductionOrderOrchestrationLayerType",
    displayName="ProductionOrderOrchestrationLayerType",
    description="The ProductionOrderOrchestrationLayerType (POOL) ObjectType consists of a set of variables, \ngenerated events and methods that are used to orchestrate production orders for a set of \nMachine Modules that implement the MachineModuleProductionType and are variously \nconnected in a production line.",
)
class ProductionOrderOrchestrationLayerType(TMCDeviceType):
    abortProductionOrder: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=11949"])
    assignProductionOrder: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=11952"])
    completeProductionOrder: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=11955"])
    getDataSet: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=11958"])
    getMaterialList: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=11961"])
    getProductionOrder: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=11964"])
    productionOrders: ns0.objtypes.FolderType
    productionOrdersRetentionTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=12006",
            browseName="ns=tmc;ProductionOrdersRetentionTime",
            description="The time in hours a ProductionOrderStateMachine is retained in memory after the production \norder is complete.",
            dataType=o6.UInt32,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    releaseProductionOrder: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=12007"])
    startProductionOrder: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=12010"])
    unassignProductionOrder: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=12013"])
    unreleaseProductionOrder: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=12016"])


@o6.objecttype(
    nodeId="ns=tmc;i=1089",
    browseName="ns=tmc;MachineContextLogType",
    displayName="MachineContextLogType",
    description="The MachineContextLogType payload contains machine status context to the derived \nevent types.",
    isAbstract=True,
)
class MachineContextLogType(LogbookEventType):
    executeStateMachineStateNumber: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=12092",
            browseName="ns=tmc;ExecuteStateMachineStateNumber",
            description="The value of the state number attribute for the ExecuteStateMachine of the object containing the \nevent notifier.",
            dataType=o6.UInt32,
        )
    )
    stateMachineStateNumber: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=12091",
            browseName="ns=tmc;StateMachineStateNumber",
            description="The value of the state number attribute for the TMCStateMachine of the object containing the \nevent notifier.",
            dataType=o6.UInt32,
        )
    )
    userMachineName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=tmc;i=12094", browseName="ns=tmc;UserMachineName", description="The name of the machine for the user.", dataType=o6.String)
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1010",
    browseName="ns=tmc;ControlModeChangeLogType",
    displayName="ControlModeChangeLogType",
    description="The ControlModeChangeLogType event is generated when the control mode changes.",
)
class ControlModeChangeLogType(MachineContextLogType):
    newControlMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6104", browseName="ns=tmc;NewControlMode", description="The control mode after the change.", dataType=tmc_datypes.ControlModeEnumeration
        )
    )
    oldControlMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6103", browseName="ns=tmc;OldControlMode", description="The control mode prior to the change.", dataType=tmc_datypes.ControlModeEnumeration
        )
    )


o6.reference(ControlModuleLiveStatusType, "i=41", ControlModeChangeLogType)
o6.reference(EquipmentModuleLiveStatusType, "i=41", ControlModeChangeLogType)


@o6.objecttype(
    nodeId="ns=tmc;i=1011",
    browseName="ns=tmc;ProductionContextLogType",
    displayName="ProductionContextLogType",
    description="The ProductionContextLogType payload contains production status context to the\nderived event types.",
    isAbstract=True,
)
class ProductionContextLogType(MachineContextLogType):
    pONumber: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6140",
            browseName="ns=tmc;PONumber",
            description="The PO number for the production order running in the machine module containing the node \nthat generates the event.",
            dataType=o6.String,
        )
    )
    productionStateMachineStateNumber: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=12093",
            browseName="ns=tmc;ProductionStateMachineStateNumber",
            description="The value of the state number attribute for the ProductionStateMachine of the machine \nmodule containing the event notifier.",
            dataType=o6.UInt32,
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1014",
    browseName="ns=tmc;RootCauseListChangeLogType",
    displayName="RootCauseListChangeLogType",
    description="The RootCauseListChangeLogType event is generated when the root cause list is changed.",
)
class RootCauseListChangeLogType(MachineContextLogType):
    newRootCauseMessages: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6170",
            browseName="ns=tmc;NewRootCauseMessages",
            description="The list of modified root cause messages.",
            dataType=tmc_datypes.RootCauseMessageType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    oldRootCauseMessages: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6169",
            browseName="ns=tmc;OldRootCauseMessages",
            description="The list of root cause messages prior to the change.",
            dataType=tmc_datypes.RootCauseMessageType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


o6.reference(MachineModuleConfigurationType, "i=41", RootCauseListChangeLogType)


@o6.objecttype(
    nodeId="ns=tmc;i=1015",
    browseName="ns=tmc;StopReasonListChangeLogType",
    displayName="StopReasonListChangeLogType",
    description="The StopReasonListChangeLogType event is generated when the stop reason list changes.",
)
class StopReasonListChangeLogType(MachineContextLogType):
    newStopReasonMessages: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6172",
            browseName="ns=tmc;NewStopReasonMessages",
            description="The list of modified stop reasons.",
            dataType=tmc_datypes.MessageType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    oldStopReasonMessages: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6171",
            browseName="ns=tmc;OldStopReasonMessages",
            description="The list of stop reasons prior to the change.",
            dataType=tmc_datypes.MessageType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


o6.reference(MachineModuleConfigurationType, "i=41", StopReasonListChangeLogType)


@o6.objecttype(
    nodeId="ns=tmc;i=1017",
    browseName="ns=tmc;DataSetChangeLogType",
    displayName="DataSetChangeLogType",
    description="The DataSetChangeLogType event is generated when the dataset changes.",
)
class DataSetChangeLogType(ProductionContextLogType):
    newDataSetEntries: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6179",
            browseName="ns=tmc;NewDataSetEntries",
            description="The list of modified dataset entries.",
            dataType=tmc_datypes.DataSetEntryType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    newDataSetID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6286", browseName="ns=tmc;NewDataSetID", description="The unique identifier for the dataset after the modification.", dataType=o6.String
        )
    )
    oldDataSetEntries: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6178",
            browseName="ns=tmc;OldDataSetEntries",
            description="The list of dataset entries prior to the change.",
            dataType=tmc_datypes.DataSetEntryType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    oldDataSetID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6287", browseName="ns=tmc;OldDataSetID", description="The unique identifier for the dataset after the modification.", dataType=o6.String
        )
    )


o6.reference(MachineModuleSetupType, "i=41", DataSetChangeLogType)


@o6.objecttype(
    nodeId="ns=tmc;i=1021",
    browseName="ns=tmc;StateChangeLogType",
    displayName="StateChangeLogType",
    description="The StateChangeLogType event is generated when the state in a LiveStatus object changes.",
)
class StateChangeLogType(ProductionContextLogType):
    newState: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=tmc;i=6221", browseName="ns=tmc;NewState", description="The state after the change.", dataType=tmc_datypes.StateEnumeration)
    )
    oldState: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=tmc;i=6220", browseName="ns=tmc;OldState", description="The state prior to the change.", dataType=tmc_datypes.StateEnumeration)
    )


o6.reference(ControlModuleLiveStatusType, "i=41", StateChangeLogType)
o6.reference(EquipmentModuleLiveStatusType, "i=41", StateChangeLogType)


@o6.objecttype(
    nodeId="ns=tmc;i=1024",
    browseName="ns=tmc;DowntimeLogType",
    displayName="DowntimeLogType",
    description="The DowntimeLogType event is generated when a downtime event finishes and the machine \nrestarts.",
)
class DowntimeLogType(ProductionContextLogType):
    duration: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6252",
            browseName="ns=tmc;Duration",
            description="The duration of the downtime in seconds until the machine restarts.",
            dataType=ns0.datatypes.Duration,
            value=0.0,
        )
    )
    rootCauses: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6251",
            browseName="ns=tmc;RootCauses",
            description="The root causes reported by the machine during the downtime.",
            dataType=tmc_datypes.RootCauseMessageType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    stopReasons: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6250",
            browseName="ns=tmc;StopReasons",
            description="The stop reasons reported by the machine during the downtime.",
            dataType=tmc_datypes.MessageType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1026",
    browseName="ns=tmc;DefectDetectedLogType",
    displayName="DefectDetectedLogType",
    description="The DefectDetectedLogType event is generated when a defect is detected. Multiple defect \ndetections can be grouped to generate a lower number of messages that is supported by the \nunderlying system.",
)
class DefectDetectedLogType(ProductionContextLogType):
    defectEU: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6277",
            browseName="ns=tmc;DefectEU",
            description="The engineering units of the measurement of the defect.",
            dataType=ns0.datatypes.EUInformation,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    defectPicture: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6278", browseName="ns=tmc;DefectPicture", description="The picture relevant to the defect detected.", dataType=ns0.datatypes.Image
        )
    )
    defectValue: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6276", browseName="ns=tmc;DefectValue", description="The measurement of the defects.", dataType=o6.Double, valueRank=1, arrayDimensions=[0]
        )
    )


o6.reference(DefectReasonType, "i=41", DefectDetectedLogType)


@o6.objecttype(
    nodeId="ns=tmc;i=1029",
    browseName="ns=tmc;RejectionModeChangeLogType",
    displayName="RejectionModeChangeLogType",
    description="The RejectionModeChangeLogType event is generated when the rejection mode of a material \nrejection trap changes.",
)
class RejectionModeChangeLogType(ProductionContextLogType):
    rejectionMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=tmc;i=7695", browseName="ns=tmc;RejectionMode", description="The rejection mode after the change.", dataType=o6.Boolean)
    )


o6.reference(MaterialRejectionPointType, "i=41", RejectionModeChangeLogType)
o6.reference(o6.ns["ns=tmc;i=6275"], "i=41", RejectionModeChangeLogType)


@o6.objecttype(
    nodeId="ns=tmc;i=1031",
    browseName="ns=tmc;ProcessItemResetLogType",
    displayName="ProcessItemResetLogType",
    description="The ProcessItemResetLogType event is generated when the aggregates of a process item are \nreset.",
)
class ProcessItemResetLogType(ProductionContextLogType):
    aggregationWindow: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6288", browseName="ns=tmc;AggregationWindow", description="Tthe number of samples over which the aggregates are computed.", dataType=o6.UInt32
        )
    )
    avg: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=6370",
            browseName="ns=tmc;Avg",
            description="The average of valid values over the last AggregationWindow samples and after the last reset.",
            dataType=o6.Double,
        )
    )
    lastResetTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=7066",
            browseName="ns=tmc;LastResetTime",
            description="The time (in UTC) when ResetAggregates was last successfully executed.",
            dataType=ns0.datatypes.UtcTime,
        )
    )
    max: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=8986",
            browseName="ns=tmc;Max",
            description="The maximum valid value for the last AggregationWindow samples and after the last reset.",
            dataType=o6.Double,
        )
    )
    min: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=8988",
            browseName="ns=tmc;Min",
            description="The minimum valid value for the last AggregationWindow samples and after the last reset.",
            dataType=o6.Double,
        )
    )
    samplingRate: ns0.vartypes.AnalogUnitRangeType
    std: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=8992",
            browseName="ns=tmc;Std",
            description="The standard deviation of the valid value for the last AggregationWindow samples and after the last reset.",
            dataType=o6.Double,
        )
    )
    total: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=8993",
            browseName="ns=tmc;Total",
            description="The accumulated total of the valid value for the last AggregationWindow samples and after the last reset.",
            dataType=o6.Double,
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1036",
    browseName="ns=tmc;RootCauseGroupListChangeLogType",
    displayName="RootCauseGroupListChangeLogType",
    description="The RootCauseGroupListChangeLogType event is generated when the root cause group list is \nchanged.",
)
class RootCauseGroupListChangeLogType(MachineContextLogType):
    newRootCauseGroups: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=7355",
            browseName="ns=tmc;NewRootCauseGroups",
            description="The root cause groups after the change.",
            dataType=tmc_datypes.RootCauseGroupType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    oldRootCauseGroups: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=7354",
            browseName="ns=tmc;OldRootCauseGroups",
            description="The root cause groups prior to the change.",
            dataType=tmc_datypes.RootCauseGroupType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


o6.reference(MachineModuleConfigurationType, "i=41", RootCauseGroupListChangeLogType)


@o6.objecttype(
    nodeId="ns=tmc;i=1045",
    browseName="ns=tmc;DetectionModeChangeLogType",
    displayName="DetectionModeChangeLogType",
    description="The DetectionModeChangeLogType event is generated when the detection mode of a defect \ndetection sensor changes.",
)
class DetectionModeChangeLogType(ProductionContextLogType):
    detectionMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=tmc;i=6243", browseName="ns=tmc;DetectionMode", description="The detection mode after the change.", dataType=o6.Boolean)
    )


o6.reference(DefectDetectionSensorType, "i=41", DetectionModeChangeLogType)
o6.reference(DefectReasonType, "i=41", DetectionModeChangeLogType)
o6.reference(SensorFunctionType, "i=41", DetectionModeChangeLogType)


@o6.objecttype(
    nodeId="ns=tmc;i=1086",
    browseName="ns=tmc;MaterialContextLogType",
    displayName="MaterialContextLogType",
    description="The MaterialContextLogType payload contains the location of material production and \nconsumption context to the derived event types.",
    isAbstract=True,
)
class MaterialContextLogType(ProductionContextLogType):
    materialPointID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=9265",
            browseName="ns=tmc;MaterialPointID",
            description="The unique identifier of the material point (loading point, rejection point or output point).",
            dataType=o6.String,
        )
    )
    materialPointMES_ID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=9266",
            browseName="ns=tmc;MaterialPointMES_ID",
            description="The higher-level system unique identifier of the material point (loading point, rejection point or output point).",
            dataType=o6.String,
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1027",
    browseName="ns=tmc;MaterialRejectedLogType",
    displayName="MaterialRejectedLogType",
    description="The MaterialRejectedLogType event is generated when some material is rejected at a rejection \ntrap.",
)
class MaterialRejectedLogType(MaterialContextLogType):
    rejectedMaterial: tmc_vartypes.MaterialQuantityVariableType
    rejectedMaterialTotal: tmc_vartypes.MaterialQuantityVariableType


o6.reference(MaterialRejectionPointType, "i=41", MaterialRejectedLogType)


@o6.objecttype(
    nodeId="ns=tmc;i=1030",
    browseName="ns=tmc;MaterialOutputProducedLogType",
    displayName="MaterialOutputProducedLogType",
    description="The MaterialOutputProducedLogType event is generated when (a) a sublot of good product is \nproduced or (b) some time elapsed.",
)
class MaterialOutputProducedLogType(MaterialContextLogType):
    producedMaterial: tmc_vartypes.MaterialSublotVariableType
    producedMaterialTotal: tmc_vartypes.MaterialQuantityVariableType


@o6.objecttype(
    nodeId="ns=tmc;i=1032",
    browseName="ns=tmc;LoadingPointUnloadedLogType",
    displayName="LoadingPointUnloadedLogType",
    description="The LoadingPointUnloadedLogType event is generated when a presented material is removed \nfrom a loading point.",
)
class LoadingPointUnloadedLogType(MaterialContextLogType):
    materialSublot: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6130",
            browseName="ns=tmc;MaterialSublot",
            description="The material sublot unloaded from the loading point.",
            dataType=tmc_datypes.MaterialSublotType,
            value=tmc_datypes.MaterialSublotType(
                iD="",
                mES_ID="",
                materialLot=tmc_datypes.MaterialLotType(
                    iD="",
                    mES_ID="",
                    materialDefinition=tmc_datypes.MaterialDefinitionType(
                        iD="",
                        mES_ID="",
                        baseUnitOfMeasure=ns0.datatypes.EUInformation(namespaceUri="", unitId=0, displayName=o6.LocalizedText()),
                        batchManaged=False,
                        groupID=None,
                        parentGroupID=None,
                        shelfLife=None,
                        properties=[],
                    ),
                    status=tmc_datypes.MaterialStockStatusEnumeration.UNRESTRICTED,
                    productionDate=o6.DateTime("1900-01-01T00:00:00Z"),
                    bestUsedBeforeDate=None,
                    properties=[],
                ),
                materialStorageLocationID="",
                quantity=0.0,
                carrierID=None,
                relativePositionID=None,
                parentSublotID=None,
                sublots=[],
            ),
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1033",
    browseName="ns=tmc;MaterialConsumedLogType",
    displayName="MaterialConsumedLogType",
    description="The MaterialConsumedLogType event is generated when a material sublot is consumed at a \nloading point.",
)
class MaterialConsumedLogType(MaterialContextLogType):
    consumedMaterial: tmc_vartypes.MaterialSublotVariableType
    consumedMaterialTotal: tmc_vartypes.MaterialQuantityVariableType


@o6.objecttype(
    nodeId="ns=tmc;i=1034",
    browseName="ns=tmc;MaterialUnloadingRequiredLogType",
    displayName="MaterialUnloadingRequiredLogType",
    description="The MaterialUnloadingRequiredLogType event is generated when some material is required to \nbe removed from the machine module loading point.",
)
class MaterialUnloadingRequiredLogType(MaterialContextLogType):
    materialSublot: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6356",
            browseName="ns=tmc;MaterialSublot",
            description="The material sublot that is requested to be unloaded.",
            dataType=tmc_datypes.MaterialSublotType,
            value=tmc_datypes.MaterialSublotType(
                iD="",
                mES_ID="",
                materialLot=tmc_datypes.MaterialLotType(
                    iD="",
                    mES_ID="",
                    materialDefinition=tmc_datypes.MaterialDefinitionType(
                        iD="",
                        mES_ID="",
                        baseUnitOfMeasure=ns0.datatypes.EUInformation(namespaceUri="", unitId=0, displayName=o6.LocalizedText()),
                        batchManaged=False,
                        groupID=None,
                        parentGroupID=None,
                        shelfLife=None,
                        properties=[],
                    ),
                    status=tmc_datypes.MaterialStockStatusEnumeration.UNRESTRICTED,
                    productionDate=o6.DateTime("1900-01-01T00:00:00Z"),
                    bestUsedBeforeDate=None,
                    properties=[],
                ),
                materialStorageLocationID="",
                quantity=0.0,
                carrierID=None,
                relativePositionID=None,
                parentSublotID=None,
                sublots=[],
            ),
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1038",
    browseName="ns=tmc;NewPresentedMaterialLogType",
    displayName="NewPresentedMaterialLogType",
    description="The NewPresentedMaterialLogType event is generated when a new material sublot is \npresented and identified at a machine module loading point.",
)
class NewPresentedMaterialLogType(MaterialContextLogType):
    materialSublot: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6357",
            browseName="ns=tmc;MaterialSublot",
            description="The material sublot that is presented.",
            dataType=tmc_datypes.MaterialSublotType,
            value=tmc_datypes.MaterialSublotType(
                iD="",
                mES_ID="",
                materialLot=tmc_datypes.MaterialLotType(
                    iD="",
                    mES_ID="",
                    materialDefinition=tmc_datypes.MaterialDefinitionType(
                        iD="",
                        mES_ID="",
                        baseUnitOfMeasure=ns0.datatypes.EUInformation(namespaceUri="", unitId=0, displayName=o6.LocalizedText()),
                        batchManaged=False,
                        groupID=None,
                        parentGroupID=None,
                        shelfLife=None,
                        properties=[],
                    ),
                    status=tmc_datypes.MaterialStockStatusEnumeration.UNRESTRICTED,
                    productionDate=o6.DateTime("1900-01-01T00:00:00Z"),
                    bestUsedBeforeDate=None,
                    properties=[],
                ),
                materialStorageLocationID="",
                quantity=0.0,
                carrierID=None,
                relativePositionID=None,
                parentSublotID=None,
                sublots=[],
            ),
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1039",
    browseName="ns=tmc;IntegrityRejectedMaterialLogType",
    displayName="IntegrityRejectedMaterialLogType",
    description="The IntegrityRejectedMaterialLogType event is generated when the validation of a presented \nmaterial is negative.",
)
class IntegrityRejectedMaterialLogType(MaterialContextLogType):
    rejectedSublot: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=7479",
            browseName="ns=tmc;RejectedSublot",
            description="The sublot of the rejected material.",
            dataType=tmc_datypes.MaterialSublotType,
            value=tmc_datypes.MaterialSublotType(
                iD="",
                mES_ID="",
                materialLot=tmc_datypes.MaterialLotType(
                    iD="",
                    mES_ID="",
                    materialDefinition=tmc_datypes.MaterialDefinitionType(
                        iD="",
                        mES_ID="",
                        baseUnitOfMeasure=ns0.datatypes.EUInformation(namespaceUri="", unitId=0, displayName=o6.LocalizedText()),
                        batchManaged=False,
                        groupID=None,
                        parentGroupID=None,
                        shelfLife=None,
                        properties=[],
                    ),
                    status=tmc_datypes.MaterialStockStatusEnumeration.UNRESTRICTED,
                    productionDate=o6.DateTime("1900-01-01T00:00:00Z"),
                    bestUsedBeforeDate=None,
                    properties=[],
                ),
                materialStorageLocationID="",
                quantity=0.0,
                carrierID=None,
                relativePositionID=None,
                parentSublotID=None,
                sublots=[],
            ),
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1084",
    browseName="ns=tmc;MaterialDispensedLogType",
    displayName="MaterialDispensedLogType",
    description="The MaterialDispensedLogType event is generated when some material is dispensed at a \nloading point.",
)
class MaterialDispensedLogType(MaterialContextLogType):
    dispensedMaterial: tmc_vartypes.MaterialSublotVariableType
    dispensedMaterialTotal: tmc_vartypes.MaterialQuantityVariableType


@o6.objecttype(
    nodeId="ns=tmc;i=1091", browseName="ns=tmc;POStartedLogType", displayName="POStartedLogType", description="The POStartedLogType event is generated when a PO is started."
)
class POStartedLogType(ProductionContextLogType):
    pass


@o6.objecttype(
    nodeId="ns=tmc;i=1092",
    browseName="ns=tmc;POStoppedLogType",
    displayName="POStoppedLogType",
    description="The POStoppedLogType event is generated when the running production order changes in a \nmachine module.",
)
class POStoppedLogType(ProductionContextLogType):
    pass


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=12166",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=12165",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=12165",
    browseName="ns=tmc;AcknowledgeAlarms",
    description="The AcknowledgeAlarms Method acknowledges all alarms of the machine module.",
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=12166"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=12169",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=12168",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="SpecificationRecord",
            dataType=o6.NodeId,
            valueRank=-1,
            description=o6.LocalizedText("The OPC UA unique node identifier for the specification to be deleted from the underlying system \nrepository."),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=12170",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=12168",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure.\n"),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=12168",
    browseName="ns=tmc;DeleteSpecificationRecord",
    description="The DeleteSpecificationRecord Method deletes a specification record.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=12169"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=12170"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=13436",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=13435",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=13435",
    browseName="ns=tmc;EndSubCarrierUnloading",
    description="The EndSubCarrierUnloading Method informs the underlying system that the unloading of (sub) carriers \ninto the carrier is complete.",
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=13436"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=13439",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=13438",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="ID", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The unique identifier of the carrier to be loaded.")),
        ns0.datatypes.Argument(name="MESID", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The higher-level system identifier for the carrier to be loaded.")),
        ns0.datatypes.Argument(
            name="ParentCarrierID",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText("The unique identifier of the parent carrier i.e., the carrier containing the carrier."),
        ),
        ns0.datatypes.Argument(
            name="Sublots", dataType=o6.NodeId("ns=tmc;i=3025"), valueRank=1, arrayDimensions=[0], description=o6.LocalizedText("The material sublots to be loaded to the carrier.")
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=13440",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=13438",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=13438",
    browseName="ns=tmc;LoadSubCarrier",
    description="The LoadSubCarrier Method requests the underlying system to load a subcarrier into the carrier that is \ncurrently being loaded.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=13439"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=13440"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=13443",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=13442",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=13442",
    browseName="ns=tmc;StartSubCarrierLoading",
    description="The StartSubCarrierLoading Method informs the underlying system that the loading of (sub) carriers into \nthe carrier has started.",
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=13443"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=13445",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=13444",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=13444",
    browseName="ns=tmc;StartSubCarrierUnloading",
    description="The StartSubCarrierUnLoading Method informs the underlying system that the unloading of (sub) \ncarriers from the carrier has started.",
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=13445"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=13448",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=13447",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ID", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The unique identifier of the carrier to be loaded."))],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=13449",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=13447",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=13447",
    browseName="ns=tmc;UnloadSubCarrier",
    description="The UnloadSubCarrier Method requests the underlying system to unload a subcarrier from the carrier \nthat is currently being unloaded.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=13448"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=13449"]),
)


@o6.objecttype(
    nodeId="ns=tmc;i=1074",
    browseName="ns=tmc;CarrierType",
    displayName="CarrierType",
    description="The CarrierType ObjectType provides a description for a uniquely identified reusable carrier. \nExamples of CarrierType implementations are AGVs, trays with RFIDs, IBCs with RFIDs, bins \nwith permanent bar codes.",
)
class CarrierType(ns0.objtypes.BaseObjectType):
    data: ns0.objtypes.FolderType | None
    endSubCarrierLoading: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=7007"])
    endSubCarrierUnloading: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=13435"])
    formFactor: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6056", browseName="ns=tmc;FormFactor", description="The form factor of the carrier e.g., trolley, AGV, core, IBC, etc.", dataType=o6.String
        )
    )
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=tmc;i=13437", browseName="ns=tmc;ID", description="The underlying system identification of the carrier.", dataType=o6.String)
    )
    loadSubCarrier: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=13438"])
    loadSublots: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=9178"])
    mES_ID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=13441",
            browseName="ns=tmc;MES_ID",
            description="A higher-level system e.g., MES, identification of the carrier.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    parentCarrierID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6063",
            browseName="ns=tmc;ParentCarrierID",
            description="The unique identifier of the carrier that contains the carrier in question.",
            dataType=o6.String,
        )
    )
    startSubCarrierLoading: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=13442"])
    startSubCarrierUnloading: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=13444"])
    subCarriers: ns0.objtypes.FolderType | None
    sublots: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=13446",
            browseName="ns=tmc;Sublots",
            description="The subLots contained in the carrier.",
            dataType=tmc_datypes.MaterialSublotType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    unloadSubCarrier: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=13447"])
    unloadSublots: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=10820"])


o6.reference(CarrierType, "i=41", CarrierSublotsChangeLogType)
o6.reference(CarrierType, "i=41", SubCarrierLoadedLogType)
o6.reference(CarrierType, "i=41", SubCarrierLoadingEndedLogType)
o6.reference(CarrierType, "i=41", SubCarrierLoadingStartedLogType)
o6.reference(CarrierType, "i=41", SubCarrierUnloadedLogType)
o6.reference(CarrierType, "i=41", SubCarrierUnloadingEndedLogType)
o6.reference(CarrierType, "i=41", SubCarrierUnloadingStartedLogType)


@o6.objecttype(
    nodeId="ns=tmc;i=1077",
    browseName="ns=tmc;MaterialLocationType",
    displayName="MaterialLocationType",
    description="The MaterialLocationType ObjectType describes locations where material is stored around a machine module. Examples of such locations are the designated areas on the floor where materials are delivered for consumption or where material produced by the machine is waiting to be collected. When the location where the material is stored is integral part of the mechanics or control of the machine, the location shall be modelled as a MaterialStorageBuffer.",
)
class MaterialLocationType(ns0.objtypes.BaseObjectType):
    canReceive: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=13468",
            browseName="ns=tmc;CanReceive",
            description="When True, material sublots or carriers can be stored in the material location. It is set by the underlying \nsystem to make the material location available for receiving.",
            dataType=o6.Boolean,
        )
    )
    canSend: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=13469",
            browseName="ns=tmc;CanSend",
            description="When True, material sublots or carriers can be removed in the material location. It is set by the underlying \nsystem to make the material location available for sending.",
            dataType=o6.Boolean,
        )
    )
    carriers: ns0.objtypes.FolderType
    iD: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=tmc;i=13508", browseName="ns=tmc;ID", description="The unique identifier for the material location.", dataType=o6.String)
    )
    mES_ID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=13509",
            browseName="ns=tmc;MES_ID",
            description="The unique identifier of the material location according to a higher-level system, e.g. MES or ERP.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    state: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=tmc;i=13510", browseName="ns=tmc;State", description="The state the material location is in.", dataType=tmc_datypes.StateEnumeration)
    )
    stateMachine: TMCStateMachineType | None
    sublots: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=tmc;i=11638", browseName="ns=tmc;Sublots", dataType=tmc_datypes.MaterialSublotType, valueRank=1, arrayDimensions=[0])
    )
    uIInfo: UIInformationType | None


o6.reference(MaterialLocationType, "i=41", StateChangeLogType)


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=13570",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=13569",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ValidationResult", dataType=o6.NodeId("ns=tmc;i=3040"), valueRank=-1, description=o6.LocalizedText("The result of the validation of the PresentedMaterial.")
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=13571",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=13569",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=13569",
    browseName="ns=tmc;SetPresentedMaterialValidationStatus",
    description="The SetPresentedMaterialValidationStatus Method provides a client with an affordance to perform the \nvalidation of the PresentedMaterial against the ExpectedMaterials and set the result of the validation in \nthe PresentedMaterialValidationStatus variable.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=13570"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=13571"]),
)


@o6.objecttype(
    nodeId="ns=tmc;i=1085",
    browseName="ns=tmc;CarrierEnteredLogType",
    displayName="CarrierEnteredLogType",
    description="The CarrierEnteredLogType event is generated when a carrier is identified by the underlying \nsystem.",
)
class CarrierEnteredLogType(LogbookEventType):
    carrierID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=13587", browseName="ns=tmc;CarrierID", description="The unique identifier for the carrier that has just entered.", dataType=o6.String
        )
    )


o6.reference(MaterialLocationType, "i=41", CarrierEnteredLogType)


@o6.objecttype(
    nodeId="ns=tmc;i=1087",
    browseName="ns=tmc;CarrierReleasedLogType",
    displayName="CarrierReleasedLogType",
    description="The CarrierReleasedLogType event is generated when a carrier is released by the underlying \nsystem.",
)
class CarrierReleasedLogType(LogbookEventType):
    carrierID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=tmc;i=13588", browseName="ns=tmc;CarrierID", description="The unique identifier for the carrier that is released.", dataType=o6.String)
    )


o6.reference(MaterialLocationType, "i=41", CarrierReleasedLogType)


@o6.objecttype(
    nodeId="ns=tmc;i=1088",
    browseName="ns=tmc;ProductionOrderTransitionLogType",
    displayName="ProductionOrderTransitionLogType",
    description="The ProductionOrderTransitionLogType event is generated when there is a state transition in \nthe machine module production order state machine.",
)
class ProductionOrderTransitionLogType(ns0.objtypes.TransitionEventType):
    pONumber: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=13589",
            browseName="ns=tmc;PONumber",
            description="The PO active when the production order state machine performed a transition.",
            dataType=o6.String,
            value="",
        )
    )
    userMachineName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=12095", browseName="ns=tmc;UserMachineName", description="The user name for the machine producing the production order.", dataType=o6.String
        )
    )


o6.reference(MachineModuleProductionStateMachineType, "i=41", ProductionOrderTransitionLogType)
o6.reference(ProductionOrderExecutionStateMachineType, "i=41", ProductionOrderTransitionLogType)


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=16539",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=16538",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="ResourceName", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The name of the UI resource to be created in the underlying system.")
        ),
        ns0.datatypes.Argument(
            name="ResourceValue",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText("The value that the UI resource will obtain in the underlying system, i.e. the SVG file."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=16540",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=16538",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=16538",
    browseName="ns=tmc;LoadUIResource",
    description="The Method LoadUIResource loads a UI resource in the underlying system for visualization. It will \noverride the existing UI resource by the same name.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=16539"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=16540"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=16748",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=16541",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ResourceName", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The name of the UI resource to be deleted from the underlying system.")
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=16749",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=16541",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=16541",
    browseName="ns=tmc;DeleteUIResource",
    description="The Method DeleteUIResource permanently removes a UI resource from the underlying system \nmemory.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=16748"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=16749"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=19799",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=19798",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=19798",
    browseName="ns=tmc;ResetAggregates",
    description="The method resets all aggregated values calculated by each ProcessItem",
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=19799"]),
)


@o6.objecttype(
    nodeId="ns=tmc;i=1005",
    browseName="ns=tmc;MachineModuleLiveStatusType",
    displayName="MachineModuleLiveStatusType",
    description="The MachineModuleLiveStatusType ObjectType contains information about the real time status \nof the machine module and provides affordances to control the machine module remotely in \nreal time.",
)
class MachineModuleLiveStatusType(ns0.objtypes.BaseObjectType):
    acknowledgeAlarms: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=12165"])
    alarms: ns0.objtypes.FolderType
    controlMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6108",
            browseName="ns=tmc;ControlMode",
            description="The ControlMode property describes the current control mode of the machine.",
            dataType=tmc_datypes.ControlModeEnumeration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    data: ns0.objtypes.FolderType | None
    idleEnergySavingMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6349",
            browseName="ns=tmc;IdleEnergySavingMode",
            description="The IdleEnergySavingMode Property is set to True when the energy saving mode during the idle phase is \nset.",
            dataType=o6.Boolean,
            value=False,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    resetAggregates: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=19798"])
    sendCommand: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=7052"])
    setControlMode: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=7044"])
    setIdleEnergySavingMode: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=7056"])
    state: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6109",
            browseName="ns=tmc;State",
            description="The Property State describes the status of the state machine controlling the machine module. State \nprovides a subset of the information of the state machine, when the latter is implemented.",
            dataType=tmc_datypes.StateEnumeration,
        )
    )
    stateMachine: TMCStateMachineType | None


o6.reference(MachineModuleLiveStatusType, "i=41", "i=10523")
o6.reference(MachineModuleLiveStatusType, "i=41", ControlModeChangeLogType)
o6.reference(MachineModuleLiveStatusType, "i=41", StateChangeLogType)
o6.reference(MachineModuleLiveStatusType, "i=41", DowntimeLogType)
o6.reference(MachineModuleLiveStatusType, "i=41", ExternalAlarmType)


@o6.objecttype(
    nodeId="ns=tmc;i=1035",
    browseName="ns=tmc;MaterialStorageBufferType",
    displayName="MaterialStorageBufferType",
    description="The MaterialStorageBufferType ObjectType describes locations where the product is stored in \na machine module and the stored product.",
)
class MaterialStorageBufferType(TMCDeviceType):
    actualLoadingRate: tmc_vartypes.MaterialRateType
    actualUnloadingRate: tmc_vartypes.MaterialRateType
    loadingRateState: ns0.vartypes.StateVariableType
    mES_ID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6947",
            browseName="ns=tmc;MES_ID",
            description="Unique identifier for the material point in an external system, e.g. MES.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    materialPointDefinition: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=19992",
            browseName="ns=tmc;MaterialPointDefinition",
            description="The Property MaterialPointDefinition contains the identification of the material point and the material that is processed or stored in the buffer.",
            dataType=tmc_datypes.MaterialStorageBufferDataType,
            value=tmc_datypes.MaterialStorageBufferDataType(
                iD="",
                storedMaterial=tmc_datypes.MaterialDefinitionType(
                    iD="",
                    mES_ID="",
                    baseUnitOfMeasure=ns0.datatypes.EUInformation(namespaceUri="", unitId=0, displayName=o6.LocalizedText()),
                    batchManaged=False,
                    groupID=None,
                    parentGroupID=None,
                    shelfLife=None,
                    properties=[],
                ),
                engineeringUnits=ns0.datatypes.EUInformation(namespaceUri="", unitId=0, displayName=o6.LocalizedText()),
                totalStorageCapacity=0.0,
                storageLogic=tmc_datypes.StorageLogicEnumeration.OTHER,
                mixingLogic=tmc_datypes.StorageMixingLogicEnumeration.MIXING,
            ),
        )
    )
    mixingLogic: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=9312",
            browseName="ns=tmc;MixingLogic",
            description="MixingLogic identifies if and how materials can be mixed in the MaterialStorageBuffer.",
            dataType=tmc_datypes.StorageMixingLogicEnumeration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    nominalLoadingRate: tmc_vartypes.MaterialRateType
    nominalUnloadingRate: tmc_vartypes.MaterialRateType
    storageLogic: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6951",
            browseName="ns=tmc;StorageLogic",
            description="The logic used at the buffer storage to store and retrieve material.",
            dataType=tmc_datypes.StorageLogicEnumeration,
        )
    )
    storedLot: tmc_vartypes.MaterialLotVariableType
    totalStorageCapacity: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6950",
            browseName="ns=tmc;TotalStorageCapacity",
            description="The total capacity of the material storage buffer.",
            dataType=o6.Double,
            value=0.0,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    unloadingRateState: ns0.vartypes.StateVariableType


@o6.objecttype(
    nodeId="ns=tmc;i=1037",
    browseName="ns=tmc;MaterialOutputPointType",
    displayName="MaterialOutputPointType",
    description="This OPC UA MaterialOutputPointType ObjectType describes the capability and real time information about \nthe hand-over point of material from one machine module to another.",
)
class MaterialOutputPointType(TMCDeviceType):
    actualProductionRate: tmc_vartypes.MaterialRateType
    downstreamHeld: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6001",
            browseName="ns=tmc;DownstreamHeld",
            description="When the downstream machine module cannot receive the product flow, the upstream \nmachine is required to hold the transfer of product to the downstream machine module.",
            dataType=o6.Boolean,
            value=False,
        )
    )
    mES_ID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=19995",
            browseName="ns=tmc;MES_ID",
            description="Unique identifier for the material point in an external system, e.g. MES.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    materialDefinition: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6667",
            browseName="ns=tmc;MaterialDefinition",
            description="The Property MaterialPointDefinition contains the identification of the material point and the material that is processed.",
            dataType=tmc_datypes.MaterialDefinitionType,
        )
    )
    materialPointDefinition: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=7530",
            browseName="ns=tmc;MaterialPointDefinition",
            description="The identification of the material output physical location and the material capabilities.",
            dataType=tmc_datypes.MaterialPointType,
            value=tmc_datypes.MaterialPointType(iD="", materialCapability=[], connectedMaterialPoint=o6.ExpandedNodeId("i=0"), propagatesProductionOrder=False),
        )
    )
    nominalProductionRate: tmc_vartypes.MaterialRateType
    producedMaterial: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=6123",
            browseName="ns=tmc;ProducedMaterial",
            description="The sublot currently being produced by the material output. The sublot quantity is updated by \nthe underlying system as output is generated.",
            dataType=tmc_datypes.MaterialSublotType,
            value=tmc_datypes.MaterialSublotType(
                iD="",
                mES_ID="",
                materialLot=tmc_datypes.MaterialLotType(
                    iD="",
                    mES_ID="",
                    materialDefinition=tmc_datypes.MaterialDefinitionType(
                        iD="",
                        mES_ID="",
                        baseUnitOfMeasure=ns0.datatypes.EUInformation(namespaceUri="", unitId=0, displayName=o6.LocalizedText()),
                        batchManaged=False,
                        groupID=None,
                        parentGroupID=None,
                        shelfLife=None,
                        properties=[],
                    ),
                    status=tmc_datypes.MaterialStockStatusEnumeration.UNRESTRICTED,
                    productionDate=o6.DateTime("1900-01-01T00:00:00Z"),
                    bestUsedBeforeDate=None,
                    properties=[],
                ),
                materialStorageLocationID="",
                quantity=0.0,
                carrierID=None,
                relativePositionID=None,
                parentSublotID=None,
                sublots=[],
            ),
        )
    )
    producedMaterialMasterTotal: tmc_vartypes.MaterialQuantityVariableType
    producedMaterialTotal: tmc_vartypes.MaterialQuantityVariableType
    productionRateState: ns0.vartypes.StateVariableType


o6.reference(MaterialOutputPointType, "i=41", MaterialOutputProducedLogType)


@o6.objecttype(
    nodeId="ns=tmc;i=1003",
    browseName="ns=tmc;MaterialLoadingPointType",
    displayName="MaterialLoadingPointType",
    description="The MaterialLoadingPointType ObjectType describes the machine module part where materials are \nloaded (either manually or by means of an automated system or both) and the materials being loaded, \nas well as the brand integrity checks required.",
)
class MaterialLoadingPointType(TMCDeviceType):
    actualDispensingRate: tmc_vartypes.MaterialRateType
    allowMixedLots: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=7699",
            browseName="ns=tmc;AllowMixedLots",
            description="When AllowMixedLots is False and BatchManaged in the material definition of the \nExpectedMaterials is True, then one material lot will be processed i.e. the first material lot \nreceived.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    consumedMaterialMasterTotal: tmc_vartypes.MaterialQuantityVariableType
    consumedMaterialTotal: tmc_vartypes.MaterialQuantityVariableType
    dispensedMaterialMasterTotal: tmc_vartypes.MaterialQuantityVariableType
    dispensedMaterialTotal: tmc_vartypes.MaterialQuantityVariableType
    dispensingRateState: ns0.vartypes.StateVariableType
    expectedMaterials: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=7362",
            browseName="ns=tmc;ExpectedMaterials",
            description="The array of sublots of the material that are expected at the machine loading point for the \ncurrent production.",
            dataType=tmc_datypes.MaterialSublotType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    loadedMaterial: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=6097",
            browseName="ns=tmc;LoadedMaterial",
            description="An array of the sublots that entered the machine loading point. When a sublot is unloaded, it is \nalso removed from the array.",
            dataType=tmc_datypes.MaterialSublotType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    mES_ID: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=20257",
            browseName="ns=tmc;MES_ID",
            description="Unique identifier for the material point in an external system, e.g. MES.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    materialIntegrityAgent: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6141",
            browseName="ns=tmc;MaterialIntegrityAgent",
            description="MaterialIntegrityAgent defines how material validation is performed.",
            dataType=tmc_datypes.MaterialIntegrityAgentEnumeration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    materialPointDefinition: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6066",
            browseName="ns=tmc;MaterialPointDefinition",
            description="The Property MaterialPointDefinition contains the identification of the material point and the material that is processed.",
            dataType=tmc_datypes.MaterialPointType,
            value=tmc_datypes.MaterialPointType(iD="", materialCapability=[], connectedMaterialPoint=o6.ExpandedNodeId("i=0"), propagatesProductionOrder=False),
        )
    )
    nominalDispensingRate: tmc_vartypes.MaterialRateType
    presentedMaterial: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=6061",
            browseName="ns=tmc;PresentedMaterial",
            description="The material presented to the material loading point, but not yet loaded.",
            dataType=tmc_datypes.MaterialSublotType,
            value=tmc_datypes.MaterialSublotType(
                iD="",
                mES_ID="",
                materialLot=tmc_datypes.MaterialLotType(
                    iD="",
                    mES_ID="",
                    materialDefinition=tmc_datypes.MaterialDefinitionType(
                        iD="",
                        mES_ID="",
                        baseUnitOfMeasure=ns0.datatypes.EUInformation(namespaceUri="", unitId=0, displayName=o6.LocalizedText()),
                        batchManaged=False,
                        groupID=None,
                        parentGroupID=None,
                        shelfLife=None,
                        properties=[],
                    ),
                    status=tmc_datypes.MaterialStockStatusEnumeration.UNRESTRICTED,
                    productionDate=o6.DateTime("1900-01-01T00:00:00Z"),
                    bestUsedBeforeDate=None,
                    properties=[],
                ),
                materialStorageLocationID="",
                quantity=0.0,
                carrierID=None,
                relativePositionID=None,
                parentSublotID=None,
                sublots=[],
            ),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    presentedMaterialValidationStatus: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=6065",
            browseName="ns=tmc;PresentedMaterialValidationStatus",
            description="The status of the validation of the presented material.",
            dataType=tmc_datypes.MaterialValidationStatusEnumeration,
        )
    )
    setPresentedMaterialValidationStatus: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=13569"])
    upstreamHold: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6002",
            browseName="ns=tmc;UpstreamHold",
            description="UpstreamHold is true when the loading point cannot receive more product and the upstream \nmachine is required to stop loading, False when the loading point can receive product.",
            dataType=o6.Boolean,
        )
    )


o6.reference(MaterialLoadingPointType, "i=41", LoadingPointUnloadedLogType)
o6.reference(MaterialLoadingPointType, "i=41", MaterialConsumedLogType)
o6.reference(MaterialLoadingPointType, "i=41", MaterialUnloadingRequiredLogType)
o6.reference(MaterialLoadingPointType, "i=41", NewPresentedMaterialLogType)
o6.reference(MaterialLoadingPointType, "i=41", IntegrityRejectedMaterialLogType)
o6.reference(MaterialLoadingPointType, "i=41", MaterialDispensedLogType)


@o6.objecttype(
    nodeId="ns=tmc;i=1002",
    browseName="ns=tmc;MachineModuleSpecificationType",
    displayName="MachineModuleSpecificationType",
    description="The MachineModuleSpecificationType provides the specification of the machine module as \ncurrently operating including capabilities, internal buffers and loading points.",
)
class MachineModuleSpecificationType(ns0.objtypes.BaseObjectType):
    deleteSpecificationRecord: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=12168"])
    documentation: ns0.objtypes.FolderType
    loadMachineModuleDocumentation: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=9267"])
    locationName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=7284",
            browseName="ns=tmc;LocationName",
            description="The Property LocationName of type String contains the location of the machine module within \nthe user production site.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    materialLoadingPoints: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6080",
            browseName="ns=tmc;MaterialLoadingPoints",
            description="The Property MaterialLoadingPoints identifies the loading points of the machine module and their capability in terms of what materials can be loaded at a loading point. The Property MaterialLoadingPoints is defined as a list of objects of type MaterialPointType.",
            dataType=tmc_datypes.MaterialPointType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    materialOutputPoints: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=12098",
            browseName="ns=tmc;MaterialOutputPoints",
            description="The Property MaterialOutputPoints identifies the output points of the machine module and their capability in terms of what materials can be output The Property MaterialOutputPoints is defined as a list of objects of type MaterialPointType.",
            dataType=tmc_datypes.MaterialPointType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    materialRejectionPoints: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=20259",
            browseName="ns=tmc;MaterialRejectionPoints",
            description="The Property MaterialRejectionPoints identifies the rejection points of the machine module and their capability in terms of what materials are rejected The Property MaterialRejectionPoints is defined as a list of objects of type MaterialPointType.",
            dataType=tmc_datypes.MaterialPointType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    materialStorageBuffers: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6084",
            browseName="ns=tmc;MaterialStorageBuffers",
            description="The Property MaterialStorageBuffers describes the buffers inside the machine module and their current status. The Property MaterialStorageBuffers is a list of objects of type MaterialStorageBufferDataType.",
            dataType=tmc_datypes.MaterialStorageBufferDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    removeMachineModuleDocumentation: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=9270"])
    setNewSpecification: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=7029"])
    timeZone: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=7300",
            browseName="ns=tmc;TimeZone",
            description="The local time zone where the machine operates. It is required to convert UTC times into local \ntime.",
            dataType=ns0.datatypes.TimeZoneDataType,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    totalRunningHours: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6198",
            browseName="ns=tmc;TotalRunningHours",
            description="The Property TotalRunningHours counts the number of hours the machine module has been in operation \nsince the last time its configuration was changed.",
            dataType=o6.UInt64,
            value=0,
        )
    )
    userMachineName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=7285",
            browseName="ns=tmc;UserMachineName",
            description="The Property UserMachineName of type String contains the name used by the user to identify \nthe machine module. LocationName and UserMachineName uniquely identify the machine \nmodule in the user organization.",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    validSince: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6145",
            browseName="ns=tmc;ValidSince",
            description="The Property ValidSince is the date since the configuration was last modified.",
            dataType=ns0.datatypes.UtcTime,
            value=o6.DateTime("2000-01-01T00:00:00Z"),
        )
    )


@o6.objecttype(
    nodeId="ns=tmc;i=1022",
    browseName="ns=tmc;MachineModuleSpecificationChangeLogType",
    displayName="MachineModuleSpecificationChangeLogType",
    description="The MachineModuleSpecificationChangeLogType event is generated when the specification of \na machine module is changed.",
)
class MachineModuleSpecificationChangeLogType(MachineContextLogType):
    newMaterialLoadingPoints: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=8880",
            browseName="ns=tmc;NewMaterialLoadingPoints",
            description="The specification of the material loading points after the change.",
            dataType=tmc_datypes.MaterialPointType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    newMaterialOutputPoints: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=8881",
            browseName="ns=tmc;NewMaterialOutputPoints",
            description="The specification of the material output points after the change.",
            dataType=tmc_datypes.MaterialPointType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    newMaterialRejectionPoints: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=20263",
            browseName="ns=tmc;NewMaterialRejectionPoints",
            description="The specification of the material rejection points after the change.",
            dataType=tmc_datypes.MaterialPointType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    newMaterialStorageBuffers: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=8882",
            browseName="ns=tmc;NewMaterialStorageBuffers",
            description="The specification of the material storage buffers after the change.",
            dataType=tmc_datypes.MaterialStorageBufferDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    newValidSince: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=8883", browseName="ns=tmc;NewValidSince", description="When the change to the specifications occurred.", dataType=ns0.datatypes.UtcTime
        )
    )
    oldMaterialLoadingPoints: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6190",
            browseName="ns=tmc;OldMaterialLoadingPoints",
            description="The specification of the material loading points prior to the change.",
            dataType=tmc_datypes.MaterialPointType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    oldMaterialOutputPoints: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6223",
            browseName="ns=tmc;OldMaterialOutputPoints",
            description="The specification of the material output points prior to the change.",
            dataType=tmc_datypes.MaterialPointType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    oldMaterialRejectionPoints: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=20264",
            browseName="ns=tmc;OldMaterialRejectionPoints",
            description="The specification of the material rejection points prior to the change.",
            dataType=tmc_datypes.MaterialPointType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    oldMaterialStorageBuffers: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6285",
            browseName="ns=tmc;OldMaterialStorageBuffers",
            description="The specification of the material storage buffers prior to the change.",
            dataType=tmc_datypes.MaterialStorageBufferDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


o6.reference(MachineModuleSpecificationType, "i=41", MachineModuleSpecificationChangeLogType)


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=22389",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=22388",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExecutionFeedback", dataType=o6.NodeId("ns=tmc;i=3009"), valueRank=-1)],
)
o6.call(
    nodeId="ns=tmc;i=22388",
    browseName="ns=tmc;ResetAggregates",
    description="The Method ResetAggregates restarts from new the computation of aggregates performed by the \nunderlying system.",
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=22389"]),
)


@o6.objecttype(
    nodeId="ns=tmc;i=1046",
    browseName="ns=tmc;ProcessItemType",
    displayName="ProcessItemType",
    description="The ProcessItemType is used to measure and monitor over time a measurement point. The \nProcessItemType also provides aggregates (Avg, Max, Min, Std, Total) that are computed by \nthe underlying system.",
)
class ProcessItemType(ns0.objtypes.BaseObjectType):
    aggregationWindow: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6230",
            browseName="ns=tmc;AggregationWindow",
            description="Tthe number of samples over which the aggregates are computed. When the number of aggregated \nsamples since the last reset exceeds the AggregationWindow, the aggregates are rolled over, i.e. computed \nover the last AggregationWindow number of samples.",
            dataType=o6.UInt32,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    avg: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=6231",
            browseName="ns=tmc;Avg",
            description="The average of valid values over the last AggregationWindow samples and after the last reset. \nIt is only reset by the successful execution of the ResetAggregates method.",
            dataType=o6.Double,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    lastResetTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6234",
            browseName="ns=tmc;LastResetTime",
            description="The time (in UTC) when ResetAggregates was last successfully executed.",
            dataType=ns0.datatypes.UtcTime,
        )
    )
    limitAlarms: ns0.objtypes.NonExclusiveLevelAlarmType
    max: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=6235",
            browseName="ns=tmc;Max",
            description="The maximum valid value for the last AggregationWindow samples and after the last reset.\nIt is only reset by the successful execution of the ResetAggregates method.",
            dataType=o6.Double,
        )
    )
    min: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=6236",
            browseName="ns=tmc;Min",
            description="The minimum valid value for the last AggregationWindow samples and after the last reset.\nIt is only reset by the successful execution of the ResetAggregates method.",
            dataType=o6.Double,
        )
    )
    resetAggregates: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=22388"])
    samplingRate: ns0.vartypes.AnalogUnitRangeType
    std: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=7290",
            browseName="ns=tmc;Std",
            description="The standard deviation of the valid value for the last AggregationWindow samples and after the last reset.",
            dataType=o6.Double,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    total: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=7292",
            browseName="ns=tmc;Total",
            description="The accumulated total of the valid value for the last AggregationWindow samples and after the last reset.\nIt is only reset by the successful execution of the ResetAggregates method.",
            dataType=o6.Double,
        )
    )
    uIInfo: UIInformationType | None
    value: tmc_vartypes.DisplayAnalogUnitType


o6.reference(ProcessItemType, "i=41", "i=10060")
o6.reference(ProcessItemType, "i=41", ProcessItemResetLogType)


@o6.objecttype(
    nodeId="ns=tmc;i=1040",
    browseName="ns=tmc;ProcessControlItemType",
    displayName="ProcessControlItemType",
    description="The ProcessControlItem Object Type describes a generic control loop including the measured variable to be controlled (PV), the desired value for the variable (SP) and the signal to the actuator (CV) to bring the PV to match the SP.",
)
class ProcessControlItemType(ProcessItemType):
    operatorControl: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=20298",
            browseName="ns=tmc;OperatorControl",
            description="The OperatorControl variable qualifies the source of the ProcessControlItem Value when RemoteControl is False, otherwise OperatorControl is undefined. When OperatorControl is True, the underlying system exposes the information that the ProcessControlItem Value is modified by the operator with respect to the nominal value, e.g. NominalRate, a.k.a. design speed for a speed control loop. When OperatorControl is False, the underlying system exposes the information that the ProcessControlItem Value is not modified by the operator.",
            dataType=o6.Boolean,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    remoteControl: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6040",
            browseName="ns=tmc;RemoteControl",
            description="The RemoteControl variable lets the underlying system expose which system is currently in control of the ProcessControlItem. More specifically, if RemoteControl is True, the underlying system copies the RemoteValue to the ProcesControlItem Value to drive it, i.e. the ProcessControlItem is remotely controlled. If RemoteControl is False, the underlying system is not using RemoteValue to drive the ProcessControlItem, but another value that is exposed as the ProcessControlItem Value, i.e. the ProcessControlItem is locally controlled.\nA client requests (resp. releases) control of the ProcessControlItem by setting RemoteControl to True (resp. False) preferably by invoking the SetRemoteControl Method. If the client does not support methods, then the client sets RemoteControl to True. The underlying system will reset RemoteControl to False if remote control is not activated.",
            dataType=o6.Boolean,
            accessLevel=7,
            userAccessLevel=1,
        )
    )
    remoteControlEnable: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=20265",
            browseName="ns=tmc;RemoteControlEnable",
            description="The RemoteControlEnable variable exposes when the underlying system is ready to activate the RemoteControl upon a request by a client. When RemoteControlEnable is False, the underlying system is not ready and will not activate a request to remotely control the ProcessControlItem.",
            dataType=o6.Boolean,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    remoteValue: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=tmc;i=6039",
            browseName="ns=tmc;RemoteValue",
            description="The value set by the client to override the object value.",
            dataType=o6.Double,
            accessLevel=7,
            userAccessLevel=1,
        )
    )
    setRemoteControl: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=7001"])


ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=22399",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=22398",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="POToAbort", dataType=o6.NodeId("ns=tmc;i=3016"), valueRank=-1, description=o6.LocalizedText("The production order to be aborted."))],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=22400",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=22398",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=22398",
    browseName="ns=tmc;AbortProductionOrder",
    description="The AbortProductionOrder method is used to abnormally terminate, or abort, a production order \nthat is in execution or starting or completing. Aborting cannot be reversed or undone.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=22399"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=22400"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=22403",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=22402",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=22402",
    browseName="ns=tmc;ClearProductionOrder",
    description="The ClearProductionOrder method is used to positively confirm that the machine module where \na production order is aborted has been cleared of the product or parts left by the aborted \nproduction order.",
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=22403"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=22405",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=22404",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=22404",
    browseName="ns=tmc;CompleteProductionOrder",
    description="The CompleteProductionOrder method is used to complete a production order in execution.",
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=22405"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=22409",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=22408",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="POToStart", dataType=o6.NodeId("ns=tmc;i=3038"), valueRank=-1, description=o6.LocalizedText("The production order to be started.")),
        ns0.datatypes.Argument(
            name="SourceMaterialLoadingPointIDs",
            dataType=o6.String,
            valueRank=1,
            description=o6.LocalizedText("The list of material loading points that are going to be used by the production order to be started."),
        ),
        ns0.datatypes.Argument(
            name="DestinationMaterialOutputPointIDs",
            dataType=o6.String,
            valueRank=1,
            description=o6.LocalizedText("The list of material outputs that are going to be used by the production order to be started."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=22410",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=22408",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure.\n"),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=22408",
    browseName="ns=tmc;StartProductionOrder",
    description="The StartProductionOrder Method starts a production order at the machine module.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=22409"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=22410"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=22412",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=22411",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="POToUnassign", dataType=o6.NodeId("ns=tmc;i=3016"), valueRank=-1, description=o6.LocalizedText("The production order to be unassigned at the machine module.")
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=22413",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=22411",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=22411",
    browseName="ns=tmc;UnassignProductionOrder",
    description="The UnAssignProductionOrder method is used to remove the specified production order from \nAssignedProductionOrders[] of an infeed machine module.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=22412"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=22413"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=22538",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=22537",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="POToAssign",
            dataType=o6.NodeId("ns=tmc;i=3038"),
            valueRank=-1,
            description=o6.LocalizedText("The production order to assign to the machine module for later execution."),
        )
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=tmc;i=22539",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=tmc;i=22537",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="ExecutionFeedback",
            dataType=o6.NodeId("ns=tmc;i=3009"),
            valueRank=-1,
            description=o6.LocalizedText("The extended feedback returning a detailed message in case of execution failure."),
        )
    ],
)
o6.call(
    nodeId="ns=tmc;i=22537",
    browseName="ns=tmc;AssignProductionOrder",
    description="The AssignProductionOrder Method is used to transfer the information of an upcoming \nproduction order to the machine module.",
    inputArgs=o6.hasProperty(o6.ns["ns=tmc;i=22538"]),
    outputArgs=o6.hasProperty(o6.ns["ns=tmc;i=22539"]),
)


@o6.objecttype(
    nodeId="ns=tmc;i=1009",
    browseName="ns=tmc;MachineModuleProductionType",
    displayName="MachineModuleProductionType",
    description="The MachineModuleProductionType Object provides information about the current production \norder and quantity produced as well as affordances to start/stop a production order and reset \ntotals for the machine module.",
)
class MachineModuleProductionType(ns0.objtypes.BaseObjectType):
    abortProductionOrder: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=22398"])
    assignProductionOrder: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=22537"])
    assignedProductionOrders: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=22401",
            browseName="ns=tmc;AssignedProductionOrders",
            description="The AssignedProductionOrders array contains the production orders that have been assigned to the \nmachine module and have not yet been started or unassigned.",
            dataType=tmc_datypes.ProductionOrderType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    autoComplete: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6124",
            browseName="ns=tmc;AutoComplete",
            description="The AutoComplete boolean defines how to trigger the machine module to complete the execution of a \nproduction order.",
            dataType=o6.Boolean,
            value=False,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    autoStart: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6129",
            browseName="ns=tmc;AutoStart",
            description="The Autostart Boolean defines how to trigger the machine module to start a production order.",
            dataType=o6.Boolean,
            value=False,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    clearProductionOrder: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=22402"])
    completeProductionOrder: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=22404"])
    data: ns0.objtypes.FolderType | None
    productionOrder: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6091",
            browseName="ns=tmc;ProductionOrder",
            description="The production order header in execution at the machine module.",
            dataType=tmc_datypes.ProductionOrderHeaderType,
            value=tmc_datypes.ProductionOrderHeaderType(
                number="",
                producedMaterial=tmc_datypes.MaterialDefinitionType(
                    iD="",
                    mES_ID="",
                    baseUnitOfMeasure=ns0.datatypes.EUInformation(namespaceUri="", unitId=0, displayName=o6.LocalizedText()),
                    batchManaged=False,
                    groupID=None,
                    parentGroupID=None,
                    shelfLife=None,
                    properties=[],
                ),
                targetQuantity=0.0,
                continueAtJobEnd=False,
                targetStartTime=o6.DateTime("1900-01-01T00:00:00Z"),
                targetEndTime=o6.DateTime("1900-01-01T00:00:00Z"),
                dataSetID="",
                dataSetDescription=o6.LocalizedText(),
                materialListID="",
                materialListDescription=o6.LocalizedText(),
            ),
        )
    )
    productionStatus: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6093",
            browseName="ns=tmc;ProductionStatus",
            description="The execution status of the production order.",
            dataType=tmc_datypes.ProductionStatusEnumeration,
        )
    )
    resetProductionTotals: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=7201"])
    startAssignedProductionOrder: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=9653"])
    startProductionOrder: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=22408"])
    stateMachine: MachineModuleProductionStateMachineType | None
    unassignProductionOrder: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=tmc;i=22411"])


o6.reference(MachineModuleProductionType, "i=41", POStartedLogType)
o6.reference(MachineModuleProductionType, "i=41", POStoppedLogType)


@o6.objecttype(
    nodeId="ns=tmc;i=1020",
    browseName="ns=tmc;UIInformationType",
    displayName="UIInformationType",
    description="The UIInformationType provides graphical specifications required for creating faceplates to \ndisplay the information made available by the OPC UA Server.",
)
class UIInformationType(ns0.objtypes.BaseObjectType):
    deleteUIResource: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=16541"])
    loadUIResource: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=tmc;i=16538"])
    positionX: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6183",
            browseName="ns=tmc;PositionX",
            description="PositionX is the relative horizontal position of the top-left corner of the object rendering in the target \nvisualization scope.",
            dataType=o6.Double,
            value=0.0,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    positionY: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6217",
            browseName="ns=tmc;PositionY",
            description="PositionX is the relative vertical position of the top-left corner of the object rendering in the target \nvisualization scope.",
            dataType=o6.Double,
            value=0.0,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    positionZ: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=22540",
            browseName="ns=tmc;PositionZ",
            description="PositionZ is the depth of the object rendering in the target visualization scope.",
            dataType=o6.Double,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    resizable: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=7346",
            browseName="ns=tmc;Resizable",
            description="When Resizable is True, the UI resource Width is rescaled based on the actual display size.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    uIResources: ns0.objtypes.FolderType
    width: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=tmc;i=6218",
            browseName="ns=tmc;Width",
            description="Width is the width of the object visualization in the target visualization scope.",
            dataType=o6.Double,
            value=0.0,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pack_ml, tmc_reftypes, tmc_datypes, tmc_vartypes
