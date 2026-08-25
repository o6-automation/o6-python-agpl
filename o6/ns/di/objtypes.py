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

"""Generated OPC UA di namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as di_reftypes
from . import datatypes as di_datypes
from . import vartypes as di_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=413",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=119",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="IndicationDuration", dataType=ns0.datatypes.Duration, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=119", browseName="ns=di;StartLocationIndication", inputArgs=o6.hasProperty(o6.ns["ns=di;i=413"]))


@o6.objecttype(nodeId="ns=di;i=135", browseName="ns=di;SoftwareLoadingType", displayName="SoftwareLoadingType", isAbstract=True)
class SoftwareLoadingType(ns0.objtypes.BaseObjectType):
    updateKey: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=136", browseName="ns=di;UpdateKey", dataType=o6.String))


@o6.objecttype(nodeId="ns=di;i=137", browseName="ns=di;PackageLoadingType", displayName="PackageLoadingType", isAbstract=True)
class PackageLoadingType(SoftwareLoadingType):
    currentVersion: SoftwareVersionType
    errorMessage: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=151", browseName="ns=di;ErrorMessage", dataType=o6.LocalizedText)
    )
    fileTransfer: ns0.objtypes.TemporaryFileTransferType
    writeBlockSize: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=152", browseName="ns=di;WriteBlockSize", dataType=o6.UInt32))


@o6.objecttype(nodeId="ns=di;i=118", browseName="ns=di;IAssetLocationIndicationType", displayName="IAssetLocationIndicationType", isAbstract=True)
class IAssetLocationIndicationType(ns0.objtypes.BaseInterfaceType):
    isIndicating: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=154", browseName="ns=di;IsIndicating", dataType=o6.Boolean))
    startLocationIndication: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=di;i=119"])
    stopLocationIndication: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="ns=di;i=121", browseName="ns=di;StopLocationIndication"))
    supportedIndicationTypes: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=di;i=156", browseName="ns=di;SupportedIndicationTypes", dataType=di_datypes.LocationIndicationType)
    )
    usedIndicationType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=di;i=155", browseName="ns=di;UsedIndicationType", dataType=di_datypes.LocationIndicationType)
    )


@o6.objecttype(nodeId="ns=di;i=153", browseName="ns=di;DirectLoadingType", displayName="DirectLoadingType")
class DirectLoadingType(PackageLoadingType):
    updateBehavior: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=169", browseName="ns=di;UpdateBehavior", dataType=di_datypes.UpdateBehavior)
    )
    writeTimeout: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=di;i=170", browseName="ns=di;WriteTimeout", dataType=ns0.datatypes.Duration)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=di;i=190",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=189",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="ManufacturerUri", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="SoftwareRevision", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="PatchIdentifiers", dataType=o6.String, valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=191",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=189",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="UpdateBehavior", dataType=o6.NodeId("ns=di;i=333"), valueRank=-1)],
)
o6.call(nodeId="ns=di;i=189", browseName="ns=di;GetUpdateBehavior", inputArgs=o6.hasProperty(o6.ns["ns=di;i=190"]), outputArgs=o6.hasProperty(o6.ns["ns=di;i=191"]))


@o6.objecttype(nodeId="ns=di;i=171", browseName="ns=di;CachedLoadingType", displayName="CachedLoadingType")
class CachedLoadingType(PackageLoadingType):
    fallbackVersion: SoftwareVersionType | None
    getUpdateBehavior: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=di;i=189"])
    pendingVersion: SoftwareVersionType


ns0.vartypes.PropertyType(
    nodeId="ns=di;i=207",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=206",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NodeIds", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=208",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=206",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="UpdateBehavior", dataType=o6.NodeId("ns=di;i=333"), valueRank=-1)],
)
o6.call(nodeId="ns=di;i=206", browseName="ns=di;GetUpdateBehavior", inputArgs=o6.hasProperty(o6.ns["ns=di;i=207"]), outputArgs=o6.hasProperty(o6.ns["ns=di;i=208"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=210",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=209",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NodeIds", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=211",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=209",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="ErrorCode", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="ErrorMessage", dataType=o6.LocalizedText, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=209", browseName="ns=di;ValidateFiles", inputArgs=o6.hasProperty(o6.ns["ns=di;i=210"]), outputArgs=o6.hasProperty(o6.ns["ns=di;i=211"]))


@o6.objecttype(nodeId="ns=di;i=192", browseName="ns=di;FileSystemLoadingType", displayName="FileSystemLoadingType")
class FileSystemLoadingType(SoftwareLoadingType):
    fileSystem: ns0.objtypes.FileDirectoryType
    getUpdateBehavior: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=di;i=206"])
    validateFiles: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=di;i=209"])


o6.call(nodeId="ns=di;i=228", browseName="ns=di;Prepare")

o6.call(nodeId="ns=di;i=229", browseName="ns=di;Abort")

o6.call(nodeId="ns=di;i=230", browseName="ns=di;Resume")


@o6.objecttype(nodeId="ns=di;i=213", browseName="ns=di;PrepareForUpdateStateMachineType", displayName="PrepareForUpdateStateMachineType")
class PrepareForUpdateStateMachineType(ns0.objtypes.FiniteStateMachineType):
    abort: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=di;i=229"])
    idle: ns0.objtypes.InitialStateType
    idleToPreparing: ns0.objtypes.TransitionType
    percentComplete: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=227", browseName="ns=di;PercentComplete", dataType=o6.Byte)
    )
    prepare: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=di;i=228"])
    preparedForUpdate: ns0.objtypes.StateType
    preparedForUpdateToResuming: ns0.objtypes.TransitionType
    preparing: ns0.objtypes.StateType
    preparingToIdle: ns0.objtypes.TransitionType
    preparingToPreparedForUpdate: ns0.objtypes.TransitionType
    resume: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=di;i=230"])
    resuming: ns0.objtypes.StateType
    resumingToIdle: ns0.objtypes.TransitionType


ns0.vartypes.PropertyType(
    nodeId="ns=di;i=266",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=265",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="ManufacturerUri", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="SoftwareRevision", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="PatchIdentifiers", dataType=o6.String, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="Hash", dataType=o6.ByteString, valueRank=-1),
    ],
)
o6.call(nodeId="ns=di;i=265", browseName="ns=di;InstallSoftwarePackage", inputArgs=o6.hasProperty(o6.ns["ns=di;i=266"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=269",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=268",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="NodeIds", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0])],
)
o6.call(nodeId="ns=di;i=268", browseName="ns=di;InstallFiles", inputArgs=o6.hasProperty(o6.ns["ns=di;i=269"]))

o6.call(nodeId="ns=di;i=270", browseName="ns=di;Resume")


@o6.objecttype(nodeId="ns=di;i=285", browseName="ns=di;PowerCycleStateMachineType", displayName="PowerCycleStateMachineType")
class PowerCycleStateMachineType(ns0.objtypes.FiniteStateMachineType):
    notWaitingForPowerCycle: ns0.objtypes.InitialStateType
    notWaitingForPowerCycleToWaitingForPowerCycle: ns0.objtypes.TransitionType
    waitingForPowerCycle: ns0.objtypes.StateType
    waitingForPowerCycleToNotWaitingForPowerCycle: ns0.objtypes.TransitionType


o6.call(nodeId="ns=di;i=321", browseName="ns=di;Confirm")


@o6.objecttype(nodeId="ns=di;i=307", browseName="ns=di;ConfirmationStateMachineType", displayName="ConfirmationStateMachineType")
class ConfirmationStateMachineType(ns0.objtypes.FiniteStateMachineType):
    confirm: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=di;i=321"])
    confirmationTimeout: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=322", browseName="ns=di;ConfirmationTimeout", dataType=ns0.datatypes.Duration)
    )
    notWaitingForConfirm: ns0.objtypes.InitialStateType
    notWaitingForConfirmToWaitingForConfirm: ns0.objtypes.TransitionType
    waitingForConfirm: ns0.objtypes.StateType
    waitingForConfirmToNotWaitingForConfirm: ns0.objtypes.TransitionType


@o6.objecttype(nodeId="ns=di;i=212", browseName="ns=di;SoftwareVersionType", displayName="SoftwareVersionType")
class SoftwareVersionType(ns0.objtypes.BaseObjectType):
    changeLogReference: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=di;i=385", browseName="ns=di;ChangeLogReference", dataType=o6.String)
    )
    clear: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=di;i=359", browseName="ns=di;Clear"))
    hash: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=386", browseName="ns=di;Hash", dataType=o6.ByteString))
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=380", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText))
    manufacturerUri: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=381", browseName="ns=di;ManufacturerUri", dataType=o6.String))
    patchIdentifiers: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=di;i=383", browseName="ns=di;PatchIdentifiers", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    releaseDate: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=384", browseName="ns=di;ReleaseDate", dataType=o6.DateTime))
    softwareRevision: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=382", browseName="ns=di;SoftwareRevision", dataType=o6.String))


@o6.objecttype(nodeId="ns=di;i=1", browseName="ns=di;SoftwareUpdateType", displayName="SoftwareUpdateType")
class SoftwareUpdateType(ns0.objtypes.BaseObjectType):
    confirmation: ConfirmationStateMachineType | None
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=di;i=134", browseName="DefaultInstanceBrowseName", dataType=o6.QualifiedName, value=o6.QualifiedName("di:SoftwareUpdate"))
    )
    installation: InstallationStateMachineType | None
    loading: SoftwareLoadingType | None = o6.hasComponent(SoftwareLoadingType(nodeId="ns=di;i=2", browseName="ns=di;Loading", _allow_abstract=True))
    parameters: ns0.objtypes.TemporaryFileTransferType | None
    powerCycle: PowerCycleStateMachineType | None
    prepareForUpdate: PrepareForUpdateStateMachineType | None
    softwareClass: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=di;i=352", browseName="ns=di;SoftwareClass", dataType=di_datypes.SoftwareClass)
    )
    softwareName: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=354", browseName="ns=di;SoftwareName", dataType=o6.String))
    softwareSubclass: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=353", browseName="ns=di;SoftwareSubclass", dataType=o6.String))
    unsignedPackageAllowed: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=di;i=355", browseName="ns=di;UnsignedPackageAllowed", dataType=o6.Boolean)
    )
    updateStatus: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=133", browseName="ns=di;UpdateStatus", dataType=o6.LocalizedText)
    )
    vendorErrorCode: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=402", browseName="ns=di;VendorErrorCode", dataType=o6.Int32)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=di;i=404",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=403",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Subclass", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=403", browseName="ns=di;Add", inputArgs=o6.hasProperty(o6.ns["ns=di;i=404"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=406",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=405",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ObjectToDelete", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=405", browseName="ns=di;Delete", inputArgs=o6.hasProperty(o6.ns["ns=di;i=406"]))


@o6.objecttype(nodeId="ns=di;i=364", browseName="ns=di;SoftwareFolderType", displayName="SoftwareFolderType")
class SoftwareFolderType(ns0.objtypes.FolderType):
    add: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=di;i=403"])
    delete: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=di;i=405"])
    softwareClass: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=365", browseName="ns=di;SoftwareClass", dataType=di_datypes.SoftwareClass))


o6.call(nodeId="ns=di;i=407", browseName="ns=di;Uninstall")


@o6.objecttype(nodeId="ns=di;i=249", browseName="ns=di;InstallationStateMachineType", displayName="InstallationStateMachineType")
class InstallationStateMachineType(ns0.objtypes.FiniteStateMachineType):
    error: ns0.objtypes.StateType
    errorToIdle: ns0.objtypes.TransitionType
    idle: ns0.objtypes.InitialStateType
    idleToInstalling: ns0.objtypes.TransitionType
    installFiles: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=di;i=268"])
    installSoftwarePackage: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=di;i=265"])
    installationDelay: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=264", browseName="ns=di;InstallationDelay", dataType=ns0.datatypes.Duration)
    )
    installing: ns0.objtypes.StateType
    installingToError: ns0.objtypes.TransitionType
    installingToIdle: ns0.objtypes.TransitionType
    percentComplete: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=263", browseName="ns=di;PercentComplete", dataType=o6.Byte)
    )
    resume: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=di;i=270"])
    uninstall: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=di;i=407"])


@o6.objecttype(
    nodeId="ns=di;i=473",
    browseName="ns=di;BaseLifetimeIndicationType",
    displayName="BaseLifetimeIndicationType",
    description="Base indication type not further defining a semantic",
    isAbstract=True,
)
class BaseLifetimeIndicationType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(
    nodeId="ns=di;i=474",
    browseName="ns=di;TimeIndicationType",
    displayName="TimeIndicationType",
    description="Indicates the time the entity has been in use or can still be used",
    isAbstract=True,
)
class TimeIndicationType(BaseLifetimeIndicationType):
    pass


@o6.objecttype(
    nodeId="ns=di;i=475",
    browseName="ns=di;NumberOfPartsIndicationType",
    displayName="NumberOfPartsIndicationType",
    description="Indicates the total number of parts that have been produced or can still be produced.",
    isAbstract=True,
)
class NumberOfPartsIndicationType(BaseLifetimeIndicationType):
    pass


@o6.objecttype(
    nodeId="ns=di;i=476",
    browseName="ns=di;NumberOfUsagesIndicationType",
    displayName="NumberOfUsagesIndicationType",
    description="Indicates counting the process steps the entity has been used or can still be used for (for example usages of a punching tool).",
    isAbstract=True,
)
class NumberOfUsagesIndicationType(BaseLifetimeIndicationType):
    pass


@o6.objecttype(
    nodeId="ns=di;i=477",
    browseName="ns=di;LengthIndicationType",
    displayName="LengthIndicationType",
    description="Indicates the abraded length, for example of a drill.",
    isAbstract=True,
)
class LengthIndicationType(BaseLifetimeIndicationType):
    pass


@o6.objecttype(
    nodeId="ns=di;i=478",
    browseName="ns=di;DiameterIndicationType",
    displayName="DiameterIndicationType",
    description="Indicates the abraded diameter, for example of a drill.",
    isAbstract=True,
)
class DiameterIndicationType(BaseLifetimeIndicationType):
    pass


@o6.objecttype(
    nodeId="ns=di;i=479",
    browseName="ns=di;SubstanceVolumeIndicationType",
    displayName="SubstanceVolumeIndicationType",
    description="Indicates the volume of a substance, for example of a liquid.",
    isAbstract=True,
)
class SubstanceVolumeIndicationType(BaseLifetimeIndicationType):
    pass


@o6.objecttype(
    nodeId="ns=di;i=480",
    browseName="ns=di;IOperationCounterType",
    displayName="IOperationCounterType",
    description="Interface defining counters for the duration of operation",
    isAbstract=True,
)
class IOperationCounterType(ns0.objtypes.BaseInterfaceType):
    operationCycleCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=di;i=483",
            browseName="ns=di;OperationCycleCounter",
            description="OperationCycleCounter is counting the times the Device switches from not performing an activity to performing an activity. For example, each time a valve starts moving, is counted. This value shall only increase during the lifetime of the Device and shall not be reset when the Device is restarted.",
            dataType=ns0.datatypes.UInteger,
        )
    )
    operationDuration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=di;i=482",
            browseName="ns=di;OperationDuration",
            description="OperationDuration is the duration the Device has been powered and performing an activity. This counter is intended for Devices where a distinction is made between switched on and in operation. For example, a drive can be powered on but not operating. It is not intended for Devices always performing an activity like sensors always measuring data. This value shall only increase during the lifetime of the Device and shall not be reset when the Device is restarted. The OperationDuration is provided as Duration, i.e., in milliseconds or even fractions of a millisecond. However, the Server is not expected to update the value in such a high frequency, but possibly once a minute or once an hour, depending on the application.",
            dataType=ns0.datatypes.Duration,
        )
    )
    powerOnDuration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=di;i=481",
            browseName="ns=di;PowerOnDuration",
            description="PowerOnDuration is the duration the Device has been powered. The main purpose is to determine the time in which degradation of the Device occurred. The details, when the time is counted, is implementation-specific. Companion specifications can define specific rules. Typically, when the Device has supply voltage and the main CPU is running, the time is counted. This can include any kind of sleep mode, but cannot include pure Wake on LAN. This value shall only increase during the lifetime of the Device and shall not be reset when the Device is restarted. The PowerOnDuration is provided as Duration, i.e., in milliseconds or even fractions of a millisecond. However, the Server is not expected to update the value in such a high frequency, but possibly once a minute or once an hour, depending on the application.",
            dataType=ns0.datatypes.Duration,
        )
    )


@o6.objecttype(nodeId="ns=di;i=1006", browseName="ns=di;ProtocolType", displayName="ProtocolType")
class ProtocolType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(nodeId="ns=di;i=1004", browseName="ns=di;ConfigurableObjectType", displayName="ConfigurableObjectType")
class ConfigurableObjectType(ns0.objtypes.BaseObjectType):
    langleObjectIdentifierRangle: ns0.objtypes.BaseObjectType | None = o6.hasComponent(
        ns0.objtypes.BaseObjectType(nodeId="ns=di;i=6026", browseName="ns=di;<ObjectIdentifier>", modellingRule="OptionalPlaceholder")
    )
    supportedTypes: ns0.objtypes.FolderType = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=di;i=5004", browseName="ns=di;SupportedTypes"))


@o6.objecttype(nodeId="ns=di;i=1005", browseName="ns=di;FunctionalGroupType", displayName="FunctionalGroupType")
class FunctionalGroupType(ns0.objtypes.FolderType):
    langleGroupIdentifierRangle: FunctionalGroupType | None
    uIElement: di_vartypes.UIElementType | None = o6.hasComponent(di_vartypes.UIElementType(nodeId="ns=di;i=6243", browseName="ns=di;UIElement", _allow_abstract=True))


ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6394",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=6393",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Context", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6395",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=6393",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="InitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=6393", browseName="ns=di;InitLock", inputArgs=o6.hasProperty(o6.ns["ns=di;i=6394"]), outputArgs=o6.hasProperty(o6.ns["ns=di;i=6395"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6397",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=6396",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="RenewLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=6396", browseName="ns=di;RenewLock", outputArgs=o6.hasProperty(o6.ns["ns=di;i=6397"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6399",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=6398",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ExitLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=6398", browseName="ns=di;ExitLock", outputArgs=o6.hasProperty(o6.ns["ns=di;i=6399"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6401",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=6400",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="BreakLockStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=6400", browseName="ns=di;BreakLock", outputArgs=o6.hasProperty(o6.ns["ns=di;i=6401"]))

ProtocolType(nodeId="ns=di;i=6499", browseName="ns=di;<ProfileIdentifier>", modellingRule="MandatoryPlaceholder")


ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6528",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=6527",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="TransferID", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="InitTransferStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=6527", browseName="ns=di;TransferToDevice", outputArgs=o6.hasProperty(o6.ns["ns=di;i=6528"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6530",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=6529",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="TransferID", dataType=o6.Int32, valueRank=-1), ns0.datatypes.Argument(name="InitTransferStatus", dataType=o6.Int32, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=6529", browseName="ns=di;TransferFromDevice", outputArgs=o6.hasProperty(o6.ns["ns=di;i=6530"]))

ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6532",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=6531",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="TransferID", dataType=o6.Int32, valueRank=-1),
        ns0.datatypes.Argument(name="SequenceNumber", dataType=o6.Int32, valueRank=-1),
        ns0.datatypes.Argument(name="MaxParameterResultsToReturn", dataType=o6.Int32, valueRank=-1),
        ns0.datatypes.Argument(name="OmitGoodResults", dataType=o6.Boolean, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=di;i=6533",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=di;i=6531",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="FetchResultData", dataType=ns0.datatypes.Structure, valueRank=-1)],
)
o6.call(nodeId="ns=di;i=6531", browseName="ns=di;FetchTransferResultData", inputArgs=o6.hasProperty(o6.ns["ns=di;i=6532"]), outputArgs=o6.hasProperty(o6.ns["ns=di;i=6533"]))


@o6.objecttype(nodeId="ns=di;i=6526", browseName="ns=di;TransferServicesType", displayName="TransferServicesType")
class TransferServicesType(ns0.objtypes.BaseObjectType):
    fetchTransferResultData: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=di;i=6531"])
    transferFromDevice: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=di;i=6529"])
    transferToDevice: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=di;i=6527"])


@o6.objecttype(nodeId="ns=di;i=1001", browseName="ns=di;TopologyElementType", displayName="TopologyElementType", isAbstract=True)
class TopologyElementType(ns0.objtypes.BaseObjectType):
    identification: FunctionalGroupType | None = o6.hasComponent(FunctionalGroupType(nodeId="ns=di;i=6014", browseName="ns=di;Identification"))
    langleGroupIdentifierRangle: FunctionalGroupType | None = o6.hasComponent(
        FunctionalGroupType(nodeId="ns=di;i=6567", browseName="ns=di;<GroupIdentifier>", modellingRule="OptionalPlaceholder")
    )
    lock: LockingServicesType | None
    methodSet: ns0.objtypes.BaseObjectType | None = o6.hasComponent(ns0.objtypes.BaseObjectType(nodeId="ns=di;i=5003", browseName="ns=di;MethodSet"))
    parameterSet: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=di;i=1003", browseName="ns=di;BlockType", displayName="BlockType", isAbstract=True)
class BlockType(TopologyElementType):
    actualMode: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6010", browseName="ns=di;ActualMode", dataType=o6.LocalizedText))
    normalMode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=di;i=6012", browseName="ns=di;NormalMode", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])
    )
    permittedMode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=di;i=6011", browseName="ns=di;PermittedMode", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])
    )
    revisionCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6009", browseName="ns=di;RevisionCounter", dataType=o6.Int32))
    targetMode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=di;i=6013", browseName="ns=di;TargetMode", dataType=o6.LocalizedText, valueRank=1, arrayDimensions=[0])
    )


@o6.objecttype(nodeId="ns=di;i=6308", browseName="ns=di;ConnectionPointType", displayName="ConnectionPointType", isAbstract=True)
class ConnectionPointType(TopologyElementType):
    langleProfileIdentifierRangle: ProtocolType = o6.hasComponent(o6.ns["ns=di;i=6499"])
    networkAddress: FunctionalGroupType = o6.hasComponent(FunctionalGroupType(nodeId="ns=di;i=6354", browseName="ns=di;NetworkAddress"))


ProtocolType(nodeId="ns=di;i=6596", browseName="ns=di;<ProfileIdentifier>", modellingRule="MandatoryPlaceholder")


@o6.objecttype(nodeId="ns=di;i=6247", browseName="ns=di;NetworkType", displayName="NetworkType")
class NetworkType(ns0.objtypes.BaseObjectType):
    langleProfileIdentifierRangle: ProtocolType = o6.hasComponent(o6.ns["ns=di;i=6596"])
    lock: LockingServicesType | None


@o6.objecttype(nodeId="ns=di;i=15035", browseName="ns=di;IVendorNameplateType", displayName="IVendorNameplateType", isAbstract=True)
class IVendorNameplateType(ns0.objtypes.BaseInterfaceType):
    deviceClass: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15044", browseName="ns=di;DeviceClass", dataType=o6.String))
    deviceManual: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15043", browseName="ns=di;DeviceManual", dataType=o6.String))
    deviceRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15041", browseName="ns=di;DeviceRevision", dataType=o6.String))
    hardwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15039", browseName="ns=di;HardwareRevision", dataType=o6.String))
    manufacturer: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15036", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText))
    manufacturerUri: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15037", browseName="ns=di;ManufacturerUri", dataType=o6.String))
    model: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15038", browseName="ns=di;Model", dataType=o6.LocalizedText))
    patchIdentifiers: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=di;i=24", browseName="ns=di;PatchIdentifiers", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    productCode: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15042", browseName="ns=di;ProductCode", dataType=o6.String))
    productInstanceUri: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=di;i=15046", browseName="ns=di;ProductInstanceUri", dataType=o6.String)
    )
    revisionCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15047", browseName="ns=di;RevisionCounter", dataType=o6.Int32))
    serialNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15045", browseName="ns=di;SerialNumber", dataType=o6.String))
    softwareReleaseDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=di;i=23", browseName="ns=di;SoftwareReleaseDate", dataType=o6.DateTime)
    )
    softwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15040", browseName="ns=di;SoftwareRevision", dataType=o6.String))


@o6.objecttype(nodeId="ns=di;i=15048", browseName="ns=di;ITagNameplateType", displayName="ITagNameplateType", isAbstract=True)
class ITagNameplateType(ns0.objtypes.BaseInterfaceType):
    assetId: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15049", browseName="ns=di;AssetId", dataType=o6.String))
    componentName: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15050", browseName="ns=di;ComponentName", dataType=o6.LocalizedText))


@o6.objecttype(nodeId="ns=di;i=15051", browseName="ns=di;IDeviceHealthType", displayName="IDeviceHealthType", isAbstract=True)
class IDeviceHealthType(ns0.objtypes.BaseInterfaceType):
    deviceHealth: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=15052", browseName="ns=di;DeviceHealth", dataType=di_datypes.DeviceHealthEnumeration)
    )
    deviceHealthAlarms: ns0.objtypes.FolderType | None = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=di;i=15053", browseName="ns=di;DeviceHealthAlarms"))


@o6.objecttype(nodeId="ns=di;i=15054", browseName="ns=di;ISupportInfoType", displayName="ISupportInfoType", isAbstract=True)
class ISupportInfoType(ns0.objtypes.BaseInterfaceType):
    deviceTypeImage: ns0.objtypes.FolderType | None
    documentation: ns0.objtypes.FolderType | None
    documentationFiles: ns0.objtypes.FolderType | None
    imageSet: ns0.objtypes.FolderType | None
    protocolSupport: ns0.objtypes.FolderType | None


@o6.objecttype(nodeId="ns=di;i=15063", browseName="ns=di;ComponentType", displayName="ComponentType", isAbstract=True, interfaces=[IVendorNameplateType, ITagNameplateType])
class ComponentType(TopologyElementType):
    assetId: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15098", browseName="ns=di;AssetId", dataType=o6.String))
    componentName: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15099", browseName="ns=di;ComponentName", dataType=o6.LocalizedText))
    deviceClass: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15094", browseName="ns=di;DeviceClass", dataType=o6.String))
    deviceManual: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15093", browseName="ns=di;DeviceManual", dataType=o6.String))
    deviceRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15091", browseName="ns=di;DeviceRevision", dataType=o6.String))
    hardwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15089", browseName="ns=di;HardwareRevision", dataType=o6.String))
    manufacturer: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15086", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText))
    manufacturerUri: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15087", browseName="ns=di;ManufacturerUri", dataType=o6.String))
    model: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15088", browseName="ns=di;Model", dataType=o6.LocalizedText))
    productCode: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15092", browseName="ns=di;ProductCode", dataType=o6.String))
    productInstanceUri: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=di;i=15096", browseName="ns=di;ProductInstanceUri", dataType=o6.String)
    )
    revisionCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15097", browseName="ns=di;RevisionCounter", dataType=o6.Int32))
    serialNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15095", browseName="ns=di;SerialNumber", dataType=o6.String))
    softwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15090", browseName="ns=di;SoftwareRevision", dataType=o6.String))


@o6.objecttype(nodeId="ns=di;i=1002", browseName="ns=di;DeviceType", displayName="DeviceType", isAbstract=True, interfaces=[IDeviceHealthType, ISupportInfoType])
class DeviceType(ComponentType):
    deviceClass: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6470", browseName="ns=di;DeviceClass", dataType=o6.String))
    deviceHealth: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=di;i=6208", browseName="ns=di;DeviceHealth", dataType=di_datypes.DeviceHealthEnumeration)
    )
    deviceHealthAlarms: ns0.objtypes.FolderType | None = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=di;i=15105", browseName="ns=di;DeviceHealthAlarms"))
    deviceManual: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6005", browseName="ns=di;DeviceManual", dataType=o6.String))
    deviceRevision: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6006", browseName="ns=di;DeviceRevision", dataType=o6.String))
    deviceTypeImage: ns0.objtypes.FolderType | None
    documentation: ns0.objtypes.FolderType | None
    hardwareRevision: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6008", browseName="ns=di;HardwareRevision", dataType=o6.String))
    imageSet: ns0.objtypes.FolderType | None
    langleCPIdentifierRangle: ConnectionPointType | None
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6003", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText))
    manufacturerUri: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15100", browseName="ns=di;ManufacturerUri", dataType=o6.String))
    model: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6004", browseName="ns=di;Model", dataType=o6.LocalizedText))
    productCode: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15101", browseName="ns=di;ProductCode", dataType=o6.String))
    productInstanceUri: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=di;i=15102", browseName="ns=di;ProductInstanceUri", dataType=o6.String)
    )
    protocolSupport: ns0.objtypes.FolderType | None
    revisionCounter: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6002", browseName="ns=di;RevisionCounter", dataType=o6.Int32))
    serialNumber: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6001", browseName="ns=di;SerialNumber", dataType=o6.String))
    softwareRevision: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6007", browseName="ns=di;SoftwareRevision", dataType=o6.String))


@o6.objecttype(nodeId="ns=di;i=15106", browseName="ns=di;SoftwareType", displayName="SoftwareType")
class SoftwareType(ComponentType):
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15129", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText))
    model: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15131", browseName="ns=di;Model", dataType=o6.LocalizedText))
    softwareRevision: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=15133", browseName="ns=di;SoftwareRevision", dataType=o6.String))


@o6.objecttype(nodeId="ns=di;i=15143", browseName="ns=di;DeviceHealthDiagnosticAlarmType", displayName="DeviceHealthDiagnosticAlarmType", isAbstract=True)
class DeviceHealthDiagnosticAlarmType(ns0.objtypes.InstrumentDiagnosticAlarmType):
    pass


@o6.objecttype(nodeId="ns=di;i=15292", browseName="ns=di;FailureAlarmType", displayName="FailureAlarmType")
class FailureAlarmType(DeviceHealthDiagnosticAlarmType):
    pass


@o6.objecttype(nodeId="ns=di;i=15441", browseName="ns=di;CheckFunctionAlarmType", displayName="CheckFunctionAlarmType")
class CheckFunctionAlarmType(DeviceHealthDiagnosticAlarmType):
    pass


@o6.objecttype(nodeId="ns=di;i=15590", browseName="ns=di;OffSpecAlarmType", displayName="OffSpecAlarmType")
class OffSpecAlarmType(DeviceHealthDiagnosticAlarmType):
    pass


@o6.objecttype(nodeId="ns=di;i=15739", browseName="ns=di;MaintenanceRequiredAlarmType", displayName="MaintenanceRequiredAlarmType")
class MaintenanceRequiredAlarmType(DeviceHealthDiagnosticAlarmType):
    pass


@o6.objecttype(nodeId="ns=di;i=6388", browseName="ns=di;LockingServicesType", displayName="LockingServicesType")
class LockingServicesType(ns0.objtypes.BaseObjectType):
    breakLock: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=di;i=6400"])
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=di;i=15890", browseName="DefaultInstanceBrowseName", dataType=o6.QualifiedName, value=o6.QualifiedName("di:Lock"))
    )
    exitLock: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=di;i=6398"])
    initLock: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=di;i=6393"])
    locked: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6534", browseName="ns=di;Locked", dataType=o6.Boolean))
    lockingClient: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6390", browseName="ns=di;LockingClient", dataType=o6.String))
    lockingUser: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=di;i=6391", browseName="ns=di;LockingUser", dataType=o6.String))
    remainingLockTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=di;i=6392", browseName="ns=di;RemainingLockTime", dataType=ns0.datatypes.Duration)
    )
    renewLock: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=di;i=6396"])


del Any, TYPE_CHECKING, uuid, o6, ns0, di_reftypes, di_datypes, di_vartypes
