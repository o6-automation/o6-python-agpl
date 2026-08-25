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

"""Generated OPC UA plastics_rubber namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import datatypes as plastics_rubber_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1027",
    browseName="ns=plastics_rubber;RequestJobListEventType",
    displayName="RequestJobListEventType",
    description="This EventType is used to initiate a call of SendJobList by the client",
    isAbstract=True,
)
class RequestJobListEventType(ns0.objtypes.BaseEventType):
    pass


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1028",
    browseName="ns=plastics_rubber;RequestCyclicJobListEventType",
    displayName="RequestCyclicJobListEventType",
    description="This EventType is used to initiate a call of SendCyclicJobList by the client",
    isAbstract=True,
)
class RequestCyclicJobListEventType(ns0.objtypes.BaseEventType):
    pass


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1004",
    browseName="ns=plastics_rubber;MessageConditionType",
    displayName="MessageConditionType",
    description="Text messages (incl. error messages) of the control system currently shown on the screen of the machine",
)
class MessageConditionType(ns0.objtypes.AlarmConditionType):
    classification: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6001", browseName="ns=plastics_rubber;Classification", description="Classification of the message", dataType=ns0.datatypes.Enumeration
        )
    )
    id: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6009", browseName="ns=plastics_rubber;Id", description="Id of the message", dataType=o6.String, value="")
    )
    isStandstillMessage: ns0.vartypes.PropertyType = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6015",
            browseName="ns=plastics_rubber;IsStandstillMessage",
            description="Indication if the message has led to a standstill",
            dataType=o6.Boolean,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1005",
    browseName="ns=plastics_rubber;MouldCycleParametersType",
    displayName="MouldCycleParametersType",
    description="Information on the production cycle related to a mould",
    isAbstract=True,
)
class MouldCycleParametersType(ns0.objtypes.BaseObjectType):
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6016",
            browseName="ns=plastics_rubber;Index",
            description="Number of the mould",
            dataType=o6.UInt32,
            value=0,
            accessLevel=5,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1007",
    browseName="ns=plastics_rubber;RequestProductionDatasetWriteEventType",
    displayName="RequestProductionDatasetWriteEventType",
    description="This EventType is used to trigger a production dataset transfer from the client to the server by the server (e.g. initiated by the operator)",
    isAbstract=True,
)
class RequestProductionDatasetWriteEventType(ns0.objtypes.BaseEventType):
    components: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6025",
            browseName="ns=plastics_rubber;Components",
            description="Array which indicates which parts of the production dataset shall be activated in the machine control after writing",
            dataType=o6.UInt16,
            valueRank=1,
        )
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6023",
            browseName="ns=plastics_rubber;Name",
            description="Name of the production dataset that should be transferred from the client to the server",
            dataType=o6.String,
            value="",
        )
    )
    storage: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6024",
            browseName="ns=plastics_rubber;Storage",
            description="Indication where the dataset is written to",
            dataType=plastics_rubber_datypes.StorageEnumeration,
            value=plastics_rubber_datypes.StorageEnumeration.PRODUCTION,
        )
    )


@o6.objecttype(nodeId="ns=plastics_rubber;i=1048", browseName="ns=plastics_rubber;UsersType", displayName="UsersType", description="Container for objects of UserType")
class UsersType(ns0.objtypes.BaseObjectType):
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6063", browseName="NodeVersion", dataType=o6.String, value=""))
    user_LangleNrRangle: UserType | None


o6.reference(UsersType, "i=41", "i=2133")


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1025",
    browseName="ns=plastics_rubber;RequestCyclicJobWriteEventType",
    displayName="RequestCyclicJobWriteEventType",
    description="This EventType is used to initiate a call of the SetCyclicJobData Method by the client",
    isAbstract=True,
)
class RequestCyclicJobWriteEventType(ns0.objtypes.BaseEventType):
    jobName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6070", browseName="ns=plastics_rubber;JobName", dataType=o6.String, value="")
    )


@o6.objecttype(nodeId="ns=plastics_rubber;i=1002", browseName="ns=plastics_rubber;MaterialType", displayName="MaterialType")
class MaterialType(ns0.objtypes.BaseObjectType):
    density: ns0.vartypes.AnalogUnitType
    id: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6098", browseName="ns=plastics_rubber;Id", dataType=o6.String, value=""))
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6097", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1055",
    browseName="ns=plastics_rubber;TemperatureZonesType",
    displayName="TemperatureZonesType",
    description="Container for objects of TemperatureZoneType",
)
class TemperatureZonesType(ns0.objtypes.BaseObjectType):
    langleTemperatureZone_NrRangle: TemperatureZoneType | None
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6123", browseName="NodeVersion", dataType=o6.String, value=""))


o6.reference(TemperatureZonesType, "i=41", "i=2133")


@o6.objecttype(nodeId="ns=plastics_rubber;i=1050", browseName="ns=plastics_rubber;MouldsType", displayName="MouldsType", description="Container for objects of MouldType")
class MouldsType(ns0.objtypes.BaseObjectType):
    mould_LangleNrRangle: MouldType | None
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6134", browseName="NodeVersion", dataType=o6.String, value=""))


o6.reference(MouldsType, "i=41", "i=2133")


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1033", browseName="ns=plastics_rubber;PowerUnitType", displayName="PowerUnitType", description="Information on an hydraulic unit or electric drive"
)
class PowerUnitType(ns0.objtypes.BaseObjectType):
    actualTemperature: ns0.vartypes.AnalogItemType | None
    id: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6140", browseName="ns=plastics_rubber;Id", description="Id of the PowerUnit", dataType=o6.String, value="")
    )
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6137", browseName="ns=plastics_rubber;Index", description="Number of the power unit", dataType=o6.UInt32, value=0)
    )
    isPresent: ns0.vartypes.PropertyType = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6138",
            browseName="ns=plastics_rubber;IsPresent",
            description="Indication if the power unit is physically present and connected",
            dataType=o6.Boolean,
        )
    )
    powerOn: ns0.vartypes.PropertyType = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6139", browseName="ns=plastics_rubber;PowerOn", description="Indication if the PowerUnit is switched on", dataType=o6.Boolean
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1035", browseName="ns=plastics_rubber;HydraulicUnitType", displayName="HydraulicUnitType", description="Information on an  hydraulic unit"
)
class HydraulicUnitType(PowerUnitType):
    actualPressure: ns0.vartypes.AnalogItemType | None


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1036", browseName="ns=plastics_rubber;ElectricDriveType", displayName="ElectricDriveType", description="Information on an electric drive"
)
class ElectricDriveType(PowerUnitType):
    pass


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1049", browseName="ns=plastics_rubber;PowerUnitsType", displayName="PowerUnitsType", description="Container for objects of PowerUnitType"
)
class PowerUnitsType(ns0.objtypes.BaseObjectType):
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6141", browseName="NodeVersion", dataType=o6.String, value=""))
    powerUnit_LangleNrRangle: PowerUnitType | None


o6.reference(PowerUnitsType, "i=41", "i=2133")


@o6.objecttype(nodeId="ns=plastics_rubber;i=1029", browseName="ns=plastics_rubber;MouldType", displayName="MouldType", description="Description and status of a mould")
class MouldType(ns0.objtypes.BaseObjectType):
    description: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6126", browseName="ns=plastics_rubber;Description", description="Description of the installed mould", dataType=o6.String, value=""
        )
    )
    id: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6127", browseName="ns=plastics_rubber;Id", description="Id of the installed mould", dataType=o6.String, value="")
    )
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6124", browseName="ns=plastics_rubber;Index", description="Number of the mould", dataType=o6.UInt32, value=0)
    )
    isPresent: ns0.vartypes.PropertyType = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6142",
            browseName="ns=plastics_rubber;IsPresent",
            description="Indication if the mould is physically present and connected",
            dataType=o6.Boolean,
        )
    )
    mouldStatus: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6125",
            browseName="ns=plastics_rubber;MouldStatus",
            description="Current (physical) status of the mould",
            dataType=plastics_rubber_datypes.MouldStatusEnumeration,
            value=plastics_rubber_datypes.MouldStatusEnumeration.OTHER,
        )
    )
    temperatureZones: TemperatureZonesType


@o6.objecttype(nodeId="ns=plastics_rubber;i=1045", browseName="ns=plastics_rubber;UserType", displayName="UserType", description="Information on a operator of the machine")
class UserType(ns0.objtypes.BaseObjectType):
    cardUid: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6057",
            browseName="ns=plastics_rubber;CardUid",
            description="Uid of the identification card used by the operator for logging in to the machine",
            dataType=o6.String,
            value="",
        )
    )
    id: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6058", browseName="ns=plastics_rubber;Id", description="Id of the user", dataType=o6.String, value="")
    )
    isPresent: ns0.vartypes.PropertyType = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6156",
            browseName="ns=plastics_rubber;IsPresent",
            description="The machine can have instances for the maximum number of users that can be simultaneously logged in. TRUE if the instance of UserType represents a user that is currently logged in.",
            dataType=o6.Boolean,
        )
    )
    language: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6059",
            browseName="ns=plastics_rubber;Language",
            description="Currently selected language on the machine control unit",
            dataType=ns0.datatypes.LocaleId,
            value="",
        )
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6060", browseName="ns=plastics_rubber;Name", description="Name of the user", dataType=o6.String, value="")
    )
    userLevel: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6061", browseName="ns=plastics_rubber;UserLevel", description="Level of the user", dataType=o6.String, value="")
    )
    userRole: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6062", browseName="ns=plastics_rubber;UserRole", description="Role of the user", dataType=o6.String, value="")
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1011",
    browseName="ns=plastics_rubber;LogbookEventType",
    displayName="LogbookEventType",
    description="Logbook events are fired by the machine for the documentation of relevant changes in the machine configuration/status",
    isAbstract=True,
)
class LogbookEventType(ns0.objtypes.BaseEventType):
    eventOriginator: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6165",
            browseName="ns=plastics_rubber;EventOriginator",
            description="Originator of a logbook event",
            dataType=plastics_rubber_datypes.EventOriginatorEnumeration,
            value=plastics_rubber_datypes.EventOriginatorEnumeration.OTHER,
        )
    )
    jobCycleCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6039",
            browseName="ns=plastics_rubber;JobCycleCounter",
            description="Current value of JobCycleCounter in the ActiveJobValues Object when the event is fired. Only to be used for cyclic production",
            dataType=o6.UInt64,
            value=0,
        )
    )
    user: UserType


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1022",
    browseName="ns=plastics_rubber;RemoteAccessLogType",
    displayName="RemoteAccessLogType",
    description="The RemoteAccessLogType is used for logging access from outside to the machine (e.g. remote service)",
    isAbstract=True,
)
class RemoteAccessLogType(LogbookEventType):
    origin: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6014",
            browseName="ns=plastics_rubber;Origin",
            description="Information about the origin of the remote access",
            dataType=o6.String,
            value="",
        )
    )
    remoteUserName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6012",
            browseName="ns=plastics_rubber;RemoteUserName",
            description="Name of the remote user (e.g. name of the service employee doing remote service)",
            dataType=o6.String,
            value="",
        )
    )
    userChange: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6013",
            browseName="ns=plastics_rubber;UserChange",
            description="Information if the user logs in or off",
            dataType=plastics_rubber_datypes.UserChangeEnumeration,
            value=plastics_rubber_datypes.UserChangeEnumeration.LOG_ON,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1041",
    browseName="ns=plastics_rubber;ProductionDatasetFrozenLogType",
    displayName="ProductionDatasetFrozenLogType",
    description="The ProductionDatasetFrozenLogType is used when a production dataset is locked or unlocked",
    isAbstract=True,
)
class ProductionDatasetFrozenLogType(LogbookEventType):
    newValue: ns0.vartypes.PropertyType = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6056", browseName="ns=plastics_rubber;NewValue", description="Information if the production dataset is now locked", dataType=o6.Boolean
        )
    )
    oldValue: ns0.vartypes.PropertyType = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6055", browseName="ns=plastics_rubber;OldValue", description="Information if the production dataset was locked", dataType=o6.Boolean
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1012",
    browseName="ns=plastics_rubber;ProductionDatasetChangeLogType",
    displayName="ProductionDatasetChangeLogType",
    description="The ProductionDatasetChangeLogType is used when a new production dataset is loaded and activated in the control system of the machine",
    isAbstract=True,
)
class ProductionDatasetChangeLogType(LogbookEventType):
    newProductionDatasetName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6169", browseName="ns=plastics_rubber;NewProductionDatasetName", description="Name of new production dataset", dataType=o6.String, value=""
        )
    )
    oldProductionDatasetName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6170", browseName="ns=plastics_rubber;OldProductionDatasetName", description="Name of old production dataset", dataType=o6.String, value=""
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1044",
    browseName="ns=plastics_rubber;ProductionStatusChangeLogType",
    displayName="ProductionStatusChangeLogType",
    description="The ProductionStatusChangeLogType is used for logging changes of the production status",
    isAbstract=True,
)
class ProductionStatusChangeLogType(LogbookEventType):
    newProductionStatus: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6171",
            browseName="ns=plastics_rubber;NewProductionStatus",
            description="New production status",
            dataType=plastics_rubber_datypes.ProductionStatusEnumeration,
            value=plastics_rubber_datypes.ProductionStatusEnumeration.OTHER,
        )
    )
    oldProductionStatus: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6172",
            browseName="ns=plastics_rubber;OldProductionStatus",
            description="Old production status",
            dataType=plastics_rubber_datypes.ProductionStatusEnumeration,
            value=plastics_rubber_datypes.ProductionStatusEnumeration.OTHER,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1013",
    browseName="ns=plastics_rubber;StandstillReasonLogType",
    displayName="StandstillReasonLogType",
    description="The StandstillReasonLogType is used for logging StandstillReasons",
    isAbstract=True,
)
class StandstillReasonLogType(LogbookEventType):
    standstillReasonId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6173", browseName="ns=plastics_rubber;StandstillReasonId", description="Id of the standstill reason", dataType=o6.String, value=""
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1014",
    browseName="ns=plastics_rubber;MachineModeChangeLogType",
    displayName="MachineModeChangeLogType",
    description="The MachineModeChangeLogType is used for logging changes of the machine mode",
    isAbstract=True,
)
class MachineModeChangeLogType(LogbookEventType):
    newMachineMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6175",
            browseName="ns=plastics_rubber;NewMachineMode",
            description="New machine mode",
            dataType=plastics_rubber_datypes.MachineModeEnumeration,
            value=plastics_rubber_datypes.MachineModeEnumeration.OTHER,
        )
    )
    oldMachineMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6176",
            browseName="ns=plastics_rubber;OldMachineMode",
            description="Old machine mode",
            dataType=plastics_rubber_datypes.MachineModeEnumeration,
            value=plastics_rubber_datypes.MachineModeEnumeration.OTHER,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1010",
    browseName="ns=plastics_rubber;ParameterChangeLogType",
    displayName="ParameterChangeLogType",
    description="The ParameterChangeLogType is used for the logging of relevant changes in production parameters. The decision which parameter is relevant for the production is done by the machine.",
    isAbstract=True,
)
class ParameterChangeLogType(LogbookEventType):
    newValue: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6166", browseName="ns=plastics_rubber;NewValue", description="New value of the changed parameter")
    )
    newValueUnit: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6177",
            browseName="ns=plastics_rubber;NewValueUnit",
            description="New unit of the changed parameter",
            dataType=ns0.datatypes.EUInformation,
            value=ns0.datatypes.EUInformation(namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=-1, displayName=o6.LocalizedText()),
        )
    )
    oldValue: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6167", browseName="ns=plastics_rubber;OldValue", description="Old value of the changed parameter")
    )
    oldValueUnit: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6178",
            browseName="ns=plastics_rubber;OldValueUnit",
            description="Old unit of the changed parameter",
            dataType=ns0.datatypes.EUInformation,
            value=ns0.datatypes.EUInformation(namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=-1, displayName=o6.LocalizedText()),
        )
    )
    parameterId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6168", browseName="ns=plastics_rubber;ParameterId", description="Id of the changed parameter", dataType=o6.String, value=""
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1015",
    browseName="ns=plastics_rubber;UserLogType",
    displayName="UserLogType",
    description="The UserLogType is used for logging which users are logged in to the machine",
    isAbstract=True,
)
class UserLogType(LogbookEventType):
    userChange: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6180",
            browseName="ns=plastics_rubber;UserChange",
            description="Information if the user logs in or off",
            dataType=plastics_rubber_datypes.UserChangeEnumeration,
            value=plastics_rubber_datypes.UserChangeEnumeration.LOG_ON,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1043",
    browseName="ns=plastics_rubber;SequenceChangeLogType",
    displayName="SequenceChangeLogType",
    description="The SequenceChangeLogType is used for the logging changes in the production sequence",
    isAbstract=True,
)
class SequenceChangeLogType(LogbookEventType):
    sequenceChange: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6182",
            browseName="ns=plastics_rubber;SequenceChange",
            description="Classification of production sequence change",
            dataType=plastics_rubber_datypes.SequenceChangeEnumeration,
            value=plastics_rubber_datypes.SequenceChangeEnumeration.UPDATE,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1042",
    browseName="ns=plastics_rubber;MessageLogType",
    displayName="MessageLogType",
    description="The MessageLogType is used for logging MessageConditions",
    isAbstract=True,
)
class MessageLogType(LogbookEventType):
    classification: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6183", browseName="ns=plastics_rubber;Classification", description="Classification of the message", dataType=ns0.datatypes.Enumeration
        )
    )
    id: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6184", browseName="ns=plastics_rubber;Id", description="Id of the message", dataType=o6.String, value="")
    )
    isStandstillMessage: ns0.vartypes.PropertyType = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6185",
            browseName="ns=plastics_rubber;IsStandstillMessage",
            description="Indication if the message has led to a standstill",
            dataType=o6.Boolean,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1046",
    browseName="ns=plastics_rubber;UserFeedbackLogType",
    displayName="UserFeedbackLogType",
    description="The UserFeedbackLogType is used for logging text messages entered by the user into the machine control system",
    isAbstract=True,
)
class UserFeedbackLogType(LogbookEventType):
    classification: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6186", browseName="ns=plastics_rubber;Classification", description="Classification of the message", dataType=ns0.datatypes.Enumeration
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1018",
    browseName="ns=plastics_rubber;MachineMESConfigurationType",
    displayName="MachineMESConfigurationType",
    description="Current configuration of a machine related to a Manufacturing Execution System (MES)",
)
class MachineMESConfigurationType(ns0.objtypes.BaseObjectType):
    mESUrl: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6200",
            browseName="ns=plastics_rubber;MESUrl",
            description="URL to display a webpage generated by the MES in a web browser integrated in the machine",
            dataType=o6.String,
            value="0",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    standstillReasons: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6196",
            browseName="ns=plastics_rubber;StandstillReasons",
            description="List of the standstill reasons from which one is selected by the operator in the case of a standstill",
            dataType=plastics_rubber_datypes.StandstillReasonType,
            valueRank=1,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    standstillReasonsLockedByMES: ns0.vartypes.PropertyType = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6199",
            browseName="ns=plastics_rubber;StandstillReasonsLockedByMES",
            description="Indication if the list StandstillReasons has been modified by the MES and may not be changed by the machine",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1026",
    browseName="ns=plastics_rubber;StandstillMessageType",
    displayName="StandstillMessageType",
    description="Information on the fault which causes standstill. This is set by machine control",
)
class StandstillMessageType(ns0.objtypes.BaseObjectType):
    classification: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6206", browseName="ns=plastics_rubber;Classification", description="Classification of the message", dataType=ns0.datatypes.Enumeration
        )
    )
    id: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6207", browseName="ns=plastics_rubber;Id", description="Id of the message", dataType=o6.String, value="")
    )
    message: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6209", browseName="Message", description="Text of the message", dataType=o6.LocalizedText, value=o6.LocalizedText())
    )
    severity: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6208", browseName="Severity", description="Severity of the message", dataType=o6.UInt16, value=0)
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1051",
    browseName="ns=plastics_rubber;MESMessageType",
    displayName="MESMessageType",
    description="Text message sent from the MES to be shown on the machine",
)
class MESMessageType(ns0.objtypes.BaseObjectType):
    id: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6210", browseName="ns=plastics_rubber;Id", description="Id of the message", dataType=o6.String, value="")
    )
    message: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6211", browseName="ns=plastics_rubber;Message", description="Text of the message", dataType=o6.String, value="")
    )
    severity: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6212", browseName="Severity", description="Severity of the message", dataType=o6.UInt16, value=0)
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1038",
    browseName="ns=plastics_rubber;CycleParametersEventType",
    displayName="CycleParametersEventType",
    description="Information on a production cycle",
    isAbstract=True,
)
class CycleParametersEventType(ns0.objtypes.BaseEventType):
    averageCycleTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6249",
            browseName="ns=plastics_rubber;AverageCycleTime",
            dataType=ns0.datatypes.Duration,
            value=0.0,
            accessLevel=5,
            userAccessLevel=1,
            historizing=True,
        )
    )
    boxBadPartsCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6051",
            browseName="ns=plastics_rubber;BoxBadPartsCounter",
            description="Number of bad parts produced in the current box",
            dataType=o6.UInt64,
            value=0,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    boxCycleCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6049", browseName="ns=plastics_rubber;BoxCycleCounter", dataType=o6.UInt64, accessLevel=5, userAccessLevel=1)
    )
    boxGoodPartsCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6050",
            browseName="ns=plastics_rubber;BoxGoodPartsCounter",
            description="Number of good parts produced in the current box",
            dataType=o6.UInt64,
            value=0,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    boxId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6256",
            browseName="ns=plastics_rubber;BoxId",
            description="Id of the box in which the current production is put in",
            dataType=o6.String,
            value="",
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    boxPartsCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6271",
            browseName="ns=plastics_rubber;BoxPartsCounter",
            description="Total number of  parts produced in the current box",
            dataType=o6.UInt64,
            value=0,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    boxTestSamplesCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6102",
            browseName="ns=plastics_rubber;BoxTestSamplesCounter",
            description="Number of test sample parts produced in the current box",
            dataType=o6.UInt64,
            value=0,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    cavityCycleQuality: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6252",
            browseName="ns=plastics_rubber;CavityCycleQuality",
            description="Quality of the cycle for each cavity",
            dataType=plastics_rubber_datypes.CavityCycleQualityEnumeration,
            valueRank=1,
            accessLevel=5,
            userAccessLevel=1,
            historizing=True,
        )
    )
    currentLotName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6253",
            browseName="ns=plastics_rubber;CurrentLotName",
            description="Name of the current production lot",
            dataType=o6.String,
            value="",
            accessLevel=5,
            userAccessLevel=1,
            historizing=True,
        )
    )
    cycleQuality: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6255",
            browseName="ns=plastics_rubber;CycleQuality",
            description="Quality of the whole cycle",
            dataType=plastics_rubber_datypes.CycleQualityEnumeration,
            value=plastics_rubber_datypes.CycleQualityEnumeration.GOOD_CYCLE,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    cycleTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6250",
            browseName="ns=plastics_rubber;CycleTime",
            description="Cycle time",
            dataType=ns0.datatypes.Duration,
            value=0.0,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    jobBadPartsCounter: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6269",
            browseName="ns=plastics_rubber;JobBadPartsCounter",
            description="Number of bad parts produced in the current job",
            dataType=o6.UInt64,
            value=0,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    jobCycleCounter: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6254",
            browseName="ns=plastics_rubber;JobCycleCounter",
            description="Number of the cycle in the job",
            dataType=o6.UInt64,
            value=0,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    jobGoodPartsCounter: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6258",
            browseName="ns=plastics_rubber;JobGoodPartsCounter",
            description="Number of good parts produced in the current job",
            dataType=o6.UInt64,
            value=0,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    jobName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6259",
            browseName="ns=plastics_rubber;JobName",
            description="Name of the job",
            dataType=o6.String,
            value="",
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    jobPartsCounter: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6257",
            browseName="ns=plastics_rubber;JobPartsCounter",
            description="Total number of parts produced in the current job",
            dataType=o6.UInt64,
            value=0,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    jobStatus: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6251",
            browseName="ns=plastics_rubber;JobStatus",
            description="Current status of the job",
            dataType=plastics_rubber_datypes.JobStatusEnumeration,
            value=plastics_rubber_datypes.JobStatusEnumeration.OTHER,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    jobTestSamplesCounter: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6270",
            browseName="ns=plastics_rubber;JobTestSamplesCounter",
            description="Number of test sample parts produced in the current job",
            dataType=o6.UInt64,
            value=0,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    machineCycleCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6260",
            browseName="ns=plastics_rubber;MachineCycleCounter",
            description="Number of finished cycles in the machine life time",
            dataType=o6.UInt64,
            value=0,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    partId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6272",
            browseName="ns=plastics_rubber;PartId",
            description="Id(s) of the parts produced in the cycle",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[1],
            value=[""],
            accessLevel=5,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1040",
    browseName="ns=plastics_rubber;RequestProductionDatasetListEventType",
    displayName="RequestProductionDatasetListEventType",
    description="This EventType is used initiate a call of SendProductionDatasetList by the client",
    isAbstract=True,
)
class RequestProductionDatasetListEventType(ns0.objtypes.BaseEventType):
    mouldId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6040",
            browseName="ns=plastics_rubber;MouldId",
            description="Id of the mould for which the available production datasets are requested",
            dataType=o6.String,
            value="",
        )
    )
    nameFilter: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6286",
            browseName="ns=plastics_rubber;NameFilter",
            description="Filtering the list of production datasets by name",
            dataType=o6.String,
            value="",
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1037",
    browseName="ns=plastics_rubber;JobInformationType",
    displayName="JobInformationType",
    description="Information about a production job",
    isAbstract=True,
)
class JobInformationType(ns0.objtypes.BaseObjectType):
    continueAtJobEnd: ns0.vartypes.PropertyType = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6261",
            browseName="ns=plastics_rubber;ContinueAtJobEnd",
            description="Indication if the machine continues the production even if the nominal output has been reached",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    customerName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6054",
            browseName="ns=plastics_rubber;CustomerName",
            description="Name of the customer for that the job is produced",
            dataType=o6.String,
            value="",
        )
    )
    jobDescription: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6289", browseName="ns=plastics_rubber;JobDescription", description="Description of the job", dataType=o6.String, value=""
        )
    )
    jobName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6290", browseName="ns=plastics_rubber;JobName", description="Name of the job", dataType=o6.String, value="")
    )
    material: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6291",
            browseName="ns=plastics_rubber;Material",
            description="Array of material names used for the job",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[1],
            value=[""],
        )
    )
    productDescription: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6295",
            browseName="ns=plastics_rubber;ProductDescription",
            description="Array of descriptions of the products produced by the job",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[1],
            value=[""],
        )
    )
    productName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6296",
            browseName="ns=plastics_rubber;ProductName",
            description="Array of product names produced by the job",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[1],
            value=[""],
        )
    )
    productionDatasetDescription: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6262",
            browseName="ns=plastics_rubber;ProductionDatasetDescription",
            description="Additional description of the production dataset which is needed for the job",
            dataType=o6.String,
            value="",
        )
    )
    productionDatasetName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6263",
            browseName="ns=plastics_rubber;ProductionDatasetName",
            description="Name of the production dataset which is needed for the job",
            dataType=o6.String,
            value="",
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1052",
    browseName="ns=plastics_rubber;HelpOffNormalAlarmType",
    displayName="HelpOffNormalAlarmType",
    description="OffNormalAlarmType with additional help text",
)
class HelpOffNormalAlarmType(ns0.objtypes.OffNormalAlarmType):
    helpText: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6309",
            browseName="ns=plastics_rubber;HelpText",
            description="Text with additional information for the operator",
            dataType=o6.LocalizedText,
            value=o6.LocalizedText(),
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1070",
    browseName="ns=plastics_rubber;MonitoredParameterAlarmType",
    displayName="MonitoredParameterAlarmType",
    description="HelpOffNormalAlarmType with additional infomration, if the cause of the alarm is a process variable expressed as MonitoredParameterType.",
)
class MonitoredParameterAlarmType(HelpOffNormalAlarmType):
    status: ns0.vartypes.MultiStateValueDiscreteType


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1006",
    browseName="ns=plastics_rubber;RequestProductionDatasetReadEventType",
    displayName="RequestProductionDatasetReadEventType",
    description="This EventType is used to trigger a production dataset transfer from the server to the client by the server (e.g. initiated by the operator)",
    isAbstract=True,
)
class RequestProductionDatasetReadEventType(ns0.objtypes.BaseEventType):
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6022",
            browseName="ns=plastics_rubber;Name",
            description="Name of the production dataset that should be transferred from the server to the client",
            dataType=o6.String,
            value="",
        )
    )
    storage: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6317",
            browseName="ns=plastics_rubber;Storage",
            description="Indication from where the dataset is read",
            dataType=plastics_rubber_datypes.StorageEnumeration,
            value=plastics_rubber_datypes.StorageEnumeration.PRODUCTION,
        )
    )


@o6.objecttype(nodeId="ns=plastics_rubber;i=1063", browseName="ns=plastics_rubber;EnergyType", displayName="EnergyType")
class EnergyType(ns0.objtypes.BaseObjectType):
    actualPower: ns0.vartypes.AnalogUnitType | None
    actualSpecificEnergy: ns0.vartypes.AnalogUnitType | None
    powerConsumption: ns0.vartypes.AnalogUnitType | None
    powerFactor: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_rubber;i=6423", browseName="ns=plastics_rubber;PowerFactor", dataType=o6.Double, value=0.0)
    )


@o6.objecttype(nodeId="ns=plastics_rubber;i=1065", browseName="ns=plastics_rubber;MeasuringDevicesType", displayName="MeasuringDevicesType")
class MeasuringDevicesType(ns0.objtypes.BaseObjectType):
    langleNameRangle_LangleNrRangle: MeasuringDeviceType | None
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6460", browseName="NodeVersion", dataType=o6.String, value=""))


o6.reference(MeasuringDevicesType, "i=41", "i=2133")


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1058",
    browseName="ns=plastics_rubber;IdentificationType",
    displayName="IdentificationType",
    description="General information about a machine (less detailed than MachineInformationType)",
)
class IdentificationType(di.objtypes.ComponentType):
    deviceClass: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6375",
            browseName="ns=di;DeviceClass",
            description="Indicates in which domain or for what purpose a certain device is used",
            dataType=o6.String,
        )
    )
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6376", browseName="ns=di;Manufacturer", description="Provides the name of the manufacturer of the machine", dataType=o6.LocalizedText
        )
    )
    model: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6377", browseName="ns=di;Model", description="Represents the name of the machine type", dataType=o6.LocalizedText)
    )
    serialNumber: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6379",
            browseName="ns=di;SerialNumber",
            description="Represents the serial number of the machine (unique ID given by the manufacturer)",
            dataType=o6.String,
        )
    )
    yearOfConstruction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6495",
            browseName="ns=plastics_rubber;YearOfConstruction",
            description="Represents the year of construction of the machine",
            dataType=o6.UInt16,
        )
    )


@o6.objecttype(nodeId="ns=plastics_rubber;i=1060", browseName="ns=plastics_rubber;DiagnosisEndEventType", displayName="DiagnosisEndEventType", isAbstract=True)
class DiagnosisEndEventType(ns0.objtypes.BaseEventType):
    status: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6499",
            browseName="ns=plastics_rubber;Status",
            dataType=plastics_rubber_datypes.DiagnosticsStatusEnumeration,
            value=plastics_rubber_datypes.DiagnosticsStatusEnumeration.OFF,
        )
    )


@o6.objecttype(nodeId="ns=plastics_rubber;i=1062", browseName="ns=plastics_rubber;DiagnosisStepEndEventType", displayName="DiagnosisStepEndEventType", isAbstract=True)
class DiagnosisStepEndEventType(ns0.objtypes.BaseEventType):
    inputNode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6502", browseName="ns=plastics_rubber;InputNode", dataType=o6.NodeId, value=o6.NodeId("i=0"))
    )
    result: ns0.vartypes.PropertyType = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6501", browseName="ns=plastics_rubber;Result", dataType=o6.Boolean)
    )


@o6.objecttype(nodeId="ns=plastics_rubber;i=1061", browseName="ns=plastics_rubber;RequestAddMaterialEventType", displayName="RequestAddMaterialEventType", isAbstract=True)
class RequestAddMaterialEventType(ns0.objtypes.BaseEventType):
    id: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6513", browseName="ns=plastics_rubber;Id", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1030",
    browseName="ns=plastics_rubber;TemperatureZoneType",
    displayName="TemperatureZoneType",
    description="Information about a temperature zone e.g. on moulds and barrels",
)
class TemperatureZoneType(ns0.objtypes.BaseObjectType):
    actualTemperature: ns0.vartypes.AnalogItemType
    classification: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6522",
            browseName="ns=plastics_rubber;Classification",
            description="Type of the temperature zone",
            dataType=plastics_rubber_datypes.TemperatureZoneClassificationEnumeration,
        )
    )
    controlMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6094",
            browseName="ns=plastics_rubber;ControlMode",
            description="Indication how the temperature is currently controlled",
            dataType=plastics_rubber_datypes.ControlModeEnumeration,
            value=plastics_rubber_datypes.ControlModeEnumeration.OTHER,
        )
    )
    highDeviationTemperature1: ns0.vartypes.AnalogItemType | None
    highDeviationTemperature2: ns0.vartypes.AnalogItemType | None
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6080", browseName="ns=plastics_rubber;Index", description="Number of the zone", dataType=o6.UInt32, value=0)
    )
    isPresent: ns0.vartypes.PropertyType = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6099",
            browseName="ns=plastics_rubber;IsPresent",
            description="Indication if the temperature zone is physically present and connected",
            dataType=o6.Boolean,
        )
    )
    lowDeviationTemperature1: ns0.vartypes.AnalogItemType | None
    lowDeviationTemperature2: ns0.vartypes.AnalogItemType | None
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6087", browseName="ns=plastics_rubber;Name", description="Name of the zone", dataType=o6.String, value="")
    )
    nominalTemperature: ns0.vartypes.AnalogItemType
    standbyTemperature: ns0.vartypes.AnalogItemType | None


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1001",
    browseName="ns=plastics_rubber;BarrelTemperatureZoneType",
    displayName="BarrelTemperatureZoneType",
    description="Information about a temperature zone on a barrel",
)
class BarrelTemperatureZoneType(TemperatureZoneType):
    position: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6095",
            browseName="ns=plastics_rubber;Position",
            description="Location of the temperature zone on a barrel. Counting starts with 1 beginning from the feeding. The highest position is at the nozzle.",
            dataType=o6.UInt32,
            value=0,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1034",
    browseName="ns=plastics_rubber;MouldTemperatureZoneType",
    displayName="MouldTemperatureZoneType",
    description="Information about a temperature zone in a mould",
)
class MouldTemperatureZoneType(TemperatureZoneType):
    pass


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1047",
    browseName="ns=plastics_rubber;TemperatureZoneCycleParametersType",
    displayName="TemperatureZoneCycleParametersType",
    description="Information on the production cycle related to a temperature zone",
)
class TemperatureZoneCycleParametersType(ns0.objtypes.BaseObjectType):
    actualTemperature: ns0.vartypes.AnalogItemType
    classification: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6536",
            browseName="ns=plastics_rubber;Classification",
            description="Type of the temperature zone",
            dataType=plastics_rubber_datypes.TemperatureZoneClassificationEnumeration,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    index: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6044",
            browseName="ns=plastics_rubber;Index",
            description="Number of the zone",
            dataType=o6.UInt32,
            value=0,
            accessLevel=5,
            userAccessLevel=1,
        )
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6045", browseName="ns=plastics_rubber;Name", description="Name of the zone", dataType=o6.String, value="", accessLevel=5, userAccessLevel=1
        )
    )


@o6.objecttype(nodeId="ns=plastics_rubber;i=1069", browseName="ns=plastics_rubber;DrivesType", displayName="DrivesType")
class DrivesType(ns0.objtypes.BaseObjectType):
    langleNameRangle_LangleNrRangle: DriveType | None
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6563", browseName="NodeVersion", dataType=o6.String))


o6.reference(DrivesType, "i=41", "i=2133")


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1009",
    browseName="ns=plastics_rubber;MachineInformationType",
    displayName="MachineInformationType",
    description="General description of the machine",
)
class MachineInformationType(di.objtypes.ComponentType):
    controllerName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6052", browseName="ns=plastics_rubber;ControllerName", description="Name of the machine controller", dataType=o6.String, value=""
        )
    )
    deviceClass: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6310", browseName="ns=di;DeviceClass", description="Indicates in which domain or for what purpose a device is used.", dataType=o6.String
        )
    )
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6217", browseName="ns=di;Manufacturer", description="Name of the company that manufactured the device", dataType=o6.LocalizedText
        )
    )
    model: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6500", browseName="ns=di;Model", description="Model name of the device", dataType=o6.LocalizedText)
    )
    serialNumber: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6713",
            browseName="ns=di;SerialNumber",
            description="Identifier that uniquely identifies, within a manufacturer, a device instance",
            dataType=o6.String,
        )
    )
    supportedLogbookEvents: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6152",
            browseName="ns=plastics_rubber;SupportedLogbookEvents",
            description="Information which LogbookEvents are supported by the machine",
            dataType=plastics_rubber_datypes.LogbookEventsEnumeration,
            valueRank=1,
        )
    )


@o6.objecttype(nodeId="ns=plastics_rubber;i=1068", browseName="ns=plastics_rubber;DriveType", displayName="DriveType")
class DriveType(ns0.objtypes.BaseObjectType):
    additionalMeasuringDevices: MeasuringDevicesType | None
    energy: EnergyType | None
    maintenance: MaintenanceType | None
    position: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6721", browseName="ns=plastics_rubber;Position", dataType=o6.String)
    )
    speed: MonitoredParameterType | None
    startDrive: StartDeviceType | None
    torque: MonitoredParameterType | None


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6018",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="NameFilter", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="MouldId", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6019",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductionDatasetList", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=1)],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7001",
    browseName="ns=plastics_rubber;GetProductionDatasetList",
    description="This Method is used to read a list from the server, which production datasets that are available on the machine's file system",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6018"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6019"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6020",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ProductionDatasetList", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=1)],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7004",
    browseName="ns=plastics_rubber;SendProductionDatasetList",
    description="This Method is used to send a list of production datasets available on the client to the server",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6020"]),
)


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1003",
    browseName="ns=plastics_rubber;ProductionDatasetListsType",
    displayName="ProductionDatasetListsType",
    description="Functions for exchanging information on the available production datasets on client and server",
)
class ProductionDatasetListsType(ns0.objtypes.BaseObjectType):
    getProductionDatasetList: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=plastics_rubber;i=7001"])
    sendProductionDatasetList: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=plastics_rubber;i=7004"])


o6.reference(ProductionDatasetListsType, "i=41", RequestProductionDatasetListEventType)


@o6.objecttype(nodeId="ns=plastics_rubber;i=1021", browseName="ns=plastics_rubber;ActiveJobValuesType", displayName="ActiveJobValuesType", description="Values of the active job")
class ActiveJobValuesType(ns0.objtypes.BaseObjectType):
    boxId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6219",
            browseName="ns=plastics_rubber;BoxId",
            description="Id of the box in which the current production is put in",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    currentLotName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6239",
            browseName="ns=plastics_rubber;CurrentLotName",
            description="Name of the current production lot",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    finishJob: o6.node.MethodNode = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_rubber;i=7009",
            browseName="ns=plastics_rubber;FinishJob",
            description="With this Method the client (e.g. MES) requests the machine to change the JobStatus to JOB_FINISHED_8",
        )
    )
    interruptJob: o6.node.MethodNode = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_rubber;i=7003",
            browseName="ns=plastics_rubber;InterruptJob",
            description="With this Method the client (e.g. MES) requests the machine to change the JobStatus to JOB_INTERRUPTED_7",
        )
    )
    jobStatus: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6243",
            browseName="ns=plastics_rubber;JobStatus",
            description="Current status of the job",
            dataType=plastics_rubber_datypes.JobStatusEnumeration,
            value=plastics_rubber_datypes.JobStatusEnumeration.OTHER,
        )
    )
    startJob: o6.node.MethodNode = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_rubber;i=7002",
            browseName="ns=plastics_rubber;StartJob",
            description="With this Method the client (e.g. MES) requests the machine to change the JobStatus to JOB_IN_PRODUCTION_6",
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6187",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7016",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7016",
    browseName="ns=plastics_rubber;Save",
    description="Stores a production dataset from the control of the machine to the file system of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6187"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6191",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="VisualisationUnit", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6192",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7017",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Page", dataType=ns0.datatypes.Image, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7017",
    browseName="ns=plastics_rubber;GetCurrentPage",
    description="Method for retrieving a screenshot of the control system with the currently shown contents",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6191"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6192"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6193",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6194",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7018",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Page", dataType=ns0.datatypes.Image, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7018",
    browseName="ns=plastics_rubber;GetPage",
    description="Method for retrieving the image of a page of the control system",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6193"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6194"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6198",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="DateTime", dataType=o6.DateTime, valueRank=-1),
        ns0.datatypes.Argument(name="TimeZoneOffset", dataType=ns0.datatypes.TimeZoneDataType, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7019",
    browseName="ns=plastics_rubber;SetMachineTime",
    description="Method for setting the server time together with TimeZoneOffset",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6198"]),
)


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1016",
    browseName="ns=plastics_rubber;MachineConfigurationType",
    displayName="MachineConfigurationType",
    description="Current configuration of the machine",
)
class MachineConfigurationType(ns0.objtypes.BaseObjectType):
    getCurrentPage: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_rubber;i=7017"])
    getPage: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_rubber;i=7018"])
    locationName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6195",
            browseName="ns=plastics_rubber;LocationName",
            description="Description of the location of the machine given by the machine operator or OPC client",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pageDirectory: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6197",
            browseName="ns=plastics_rubber;PageDirectory",
            description="List of the pages that are implemented in the machine control system and are shown on the screen of the machine",
            dataType=plastics_rubber_datypes.PageEntryDataType,
            valueRank=1,
            arrayDimensions=[1],
            value=[plastics_rubber_datypes.PageEntryDataType(id="", title=o6.LocalizedText())],
        )
    )
    setMachineTime: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=plastics_rubber;i=7019"])
    timeZoneOffset: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6201",
            browseName="ns=plastics_rubber;TimeZoneOffset",
            description="Difference of the local time to Coordinated Universal Time (UTC) given by the machine operator or OPC client",
            dataType=ns0.datatypes.TimeZoneDataType,
            value=ns0.datatypes.TimeZoneDataType(offset=0, daylightSavingInOffset=False),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    userMachineName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6202",
            browseName="ns=plastics_rubber;UserMachineName",
            description="Description of the machine given by the machine operator or OPC client",
            dataType=o6.String,
            value="",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1019",
    browseName="ns=plastics_rubber;MachineStatusType",
    displayName="MachineStatusType",
    description="Information on the current status of the machine",
)
class MachineStatusType(ns0.objtypes.BaseObjectType):
    activateSleepMode: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=plastics_rubber;i=7020", browseName="ns=plastics_rubber;ActivateSleepMode", description="Method for activation of sleep mode")
    )
    deactivateSleepMode: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=plastics_rubber;i=7021", browseName="ns=plastics_rubber;DeactivateSleepMode", description="Method for deactivation of sleep mode")
    )
    isPresent: ns0.vartypes.PropertyType = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6203",
            browseName="ns=plastics_rubber;IsPresent",
            description="Indication if the machine is physically present and connected",
            dataType=o6.Boolean,
        )
    )
    machineMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6205",
            browseName="ns=plastics_rubber;MachineMode",
            description="Current machine mode (as defined by mode selector on the machine)",
            dataType=plastics_rubber_datypes.MachineModeEnumeration,
            value=plastics_rubber_datypes.MachineModeEnumeration.OTHER,
        )
    )
    users: UsersType


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6268",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7025",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[14],
    value=[
        ns0.datatypes.Argument(name="JobName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="JobDescription", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="CustomerName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ProductionDatasetName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ProductionDatasetDescription", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Material", dataType=o6.String, valueRank=1),
        ns0.datatypes.Argument(name="ProductName", dataType=o6.String, valueRank=1),
        ns0.datatypes.Argument(name="ProductDescription", dataType=o6.String, valueRank=1),
        ns0.datatypes.Argument(name="ContinueAtJobEnd", dataType=o6.Boolean, valueRank=-1),
        ns0.datatypes.Argument(name="NominalParts", dataType=o6.UInt64, valueRank=-1),
        ns0.datatypes.Argument(name="NominalBoxParts", dataType=o6.UInt64, valueRank=-1),
        ns0.datatypes.Argument(name="ExpectedCycleTime", dataType=ns0.datatypes.Duration, valueRank=-1),
        ns0.datatypes.Argument(name="MouldId", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="NumCavities", dataType=o6.UInt32, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7025",
    browseName="ns=plastics_rubber;SetCyclicJobData",
    description="Method for setting the data for cyclic jobs",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6268"]),
)


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1024",
    browseName="ns=plastics_rubber;CyclicJobInformationType",
    displayName="CyclicJobInformationType",
    description="Information about a cyclic production job",
)
class CyclicJobInformationType(JobInformationType):
    expectedCycleTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6267",
            browseName="ns=plastics_rubber;ExpectedCycleTime",
            description="Calculated cycle time for the job",
            dataType=ns0.datatypes.Duration,
            value=0.0,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    mouldId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6190", browseName="ns=plastics_rubber;MouldId", description="Id of the Mould used for the job", dataType=o6.String, value=""
        )
    )
    nominalBoxParts: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6266",
            browseName="ns=plastics_rubber;NominalBoxParts",
            description="Number of parts that shall be put into one box",
            dataType=o6.UInt64,
            value=0,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    nominalParts: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6265",
            browseName="ns=plastics_rubber;NominalParts",
            description="Total number (sum of all cavities) of parts that shall be produced by the job",
            dataType=o6.UInt64,
            value=0,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    numCavities: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6279",
            browseName="ns=plastics_rubber;NumCavities",
            description="Number of cavities in the Mould used for production",
            dataType=o6.UInt32,
            value=0,
        )
    )
    setCyclicJobData: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=plastics_rubber;i=7025"])


o6.reference(CyclicJobInformationType, "i=41", RequestCyclicJobWriteEventType)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6222",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="WatchDogTime", dataType=o6.Int32, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7029",
    browseName="ns=plastics_rubber;SetWatchDogTime",
    description="Release of production for a given time",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6222"]),
)


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1017",
    browseName="ns=plastics_rubber;ProductionControlType",
    displayName="ProductionControlType",
    description="Control of the production of the machine by MES",
)
class ProductionControlType(ns0.objtypes.BaseObjectType):
    automaticRunEnabled: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6218", browseName="ns=plastics_rubber;AutomaticRunEnabled", dataType=o6.Boolean)
    )
    disableAutomaticRun: o6.node.MethodNode = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_rubber;i=7024",
            browseName="ns=plastics_rubber;DisableAutomaticRun",
            description="Method for disabling the semi-automatic and automatic run of the machine",
        )
    )
    enableAutomaticRun: o6.node.MethodNode = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_rubber;i=7026",
            browseName="ns=plastics_rubber;EnableAutomaticRun",
            description="Method for enabling the semi-automatic and automatic run of the machine",
        )
    )
    productionOnlyWithMES: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6220", browseName="ns=plastics_rubber;ProductionOnlyWithMES", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    productionReleasedByMES: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6021", browseName="ns=plastics_rubber;ProductionReleasedByMES", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
        )
    )
    productionStatus: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6221",
            browseName="ns=plastics_rubber;ProductionStatus",
            description="Production status when the machine is in automatic or semi-automatic mode",
            dataType=plastics_rubber_datypes.ProductionStatusEnumeration,
            value=plastics_rubber_datypes.ProductionStatusEnumeration.OTHER,
        )
    )
    requestTestSample: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_rubber;i=7022",
            browseName="ns=plastics_rubber;RequestTestSample",
            description="The machine shall separate a test sample (e.g. for quality check). The size of the test sample depends on the product/machine configuration.",
        )
    )
    resetWatchDog: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_rubber;i=7028",
            browseName="ns=plastics_rubber;ResetWatchDog",
            description="Setting the watch dog timer to the value set by the last calling of SetWatchDogTime",
        )
    )
    setWatchDogTime: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_rubber;i=7029"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6283",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7032",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="fileHandle", dataType=o6.UInt32, valueRank=-1)],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6284",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7032",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Information", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7032",
    browseName="ns=plastics_rubber;GetProductionDatasetInformation",
    description="This Method allows reading the description of a production dataset during the file transfer from the server to the client with ProductionDatasetTransfer",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6283"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6284"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6384",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7036",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="JobList", dataType=o6.NodeId("ns=plastics_rubber;i=3021"), valueRank=1)],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7036",
    browseName="ns=plastics_rubber;SendJobList",
    description="Sends a list of jobs available on the client to the server",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6384"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6232",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7039",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Message", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Severity", dataType=o6.UInt16, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7039",
    browseName="ns=plastics_rubber;SetMESMessage",
    description="Method for setting the MESMessage",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6232"]),
)


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1020",
    browseName="ns=plastics_rubber;MachineMESStatusType",
    displayName="MachineMESStatusType",
    description="Current status of a machine related to the MES",
)
class MachineMESStatusType(ns0.objtypes.BaseObjectType):
    clearMESMessage: o6.node.MethodNode = o6.hasComponent(
        o6.call(nodeId="ns=plastics_rubber;i=7030", browseName="ns=plastics_rubber;ClearMESMessage", description="Method for clearing the MESMessage")
    )
    mESMessage: MESMessageType
    productionControl: ProductionControlType
    setMESMessage: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=plastics_rubber;i=7039"])
    standstillMessage: StandstillMessageType
    standstillReasonId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6237",
            browseName="ns=plastics_rubber;StandstillReasonId",
            description="Id of the StandstillReason set by the operator after a standstill occurs",
            dataType=o6.String,
            value="",
        )
    )


o6.reference(MachineMESStatusType, "i=41", MessageConditionType)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6389",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7040",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="JobList", dataType=o6.NodeId("ns=plastics_rubber;i=3022"), valueRank=1)],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7040",
    browseName="ns=plastics_rubber;SendCyclicJobList",
    description="Sends a list of jobs for cyclic processes available on the client to the server",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6389"]),
)


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1032",
    browseName="ns=plastics_rubber;JobsType",
    displayName="JobsType",
    description="Management of production jobs on the machine and information on their status including process parameters",
)
class JobsType(ns0.objtypes.BaseObjectType):
    activeJob: JobInformationType
    activeJobValues: ActiveJobValuesType
    jobInPreparation: JobInformationType | None
    sendCyclicJobList: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_rubber;i=7040"])
    sendJobList: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_rubber;i=7036"])


o6.reference(JobsType, "i=41", RequestJobListEventType)
o6.reference(JobsType, "i=41", RequestCyclicJobListEventType)


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1031",
    browseName="ns=plastics_rubber;ActiveCyclicJobValuesType",
    displayName="ActiveCyclicJobValuesType",
    description="Values of the active job for cyclic production",
)
class ActiveCyclicJobValuesType(ActiveJobValuesType):
    averageCycleTime: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_rubber;i=6241", browseName="ns=plastics_rubber;AverageCycleTime", description="Average cycle time", dataType=ns0.datatypes.Duration, value=0.0
        )
    )
    boxBadPartsCounter: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_rubber;i=6047",
            browseName="ns=plastics_rubber;BoxBadPartsCounter",
            description="Number of bad parts produced in the current box",
            dataType=o6.UInt64,
            value=0,
        )
    )
    boxCycleCounter: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_rubber;i=6046",
            browseName="ns=plastics_rubber;BoxCycleCounter",
            description="Number of finished cycles for the current box",
            dataType=o6.UInt64,
            value=0,
        )
    )
    boxGoodPartsCounter: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_rubber;i=6041",
            browseName="ns=plastics_rubber;BoxGoodPartsCounter",
            description="Number of good parts produced in the current box",
            dataType=o6.UInt64,
            value=0,
        )
    )
    boxPartsCounter: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_rubber;i=6247",
            browseName="ns=plastics_rubber;BoxPartsCounter",
            description="Total number of parts produced in the current box",
            dataType=o6.UInt64,
            value=0,
        )
    )
    boxTestSamplesCounter: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_rubber;i=6048",
            browseName="ns=plastics_rubber;BoxTestSamplesCounter",
            description="Number of test sample parts produced in the current box",
            dataType=o6.UInt64,
            value=0,
        )
    )
    jobBadPartsCounter: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_rubber;i=6245",
            browseName="ns=plastics_rubber;JobBadPartsCounter",
            description="Number of bad parts produced in the current job",
            dataType=o6.UInt64,
            value=0,
        )
    )
    jobCycleCounter: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_rubber;i=6228", browseName="ns=plastics_rubber;JobCycleCounter", description="Number of finished cycles in the job", dataType=o6.UInt64, value=0
        )
    )
    jobGoodPartsCounter: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_rubber;i=6244",
            browseName="ns=plastics_rubber;JobGoodPartsCounter",
            description="Number of good parts produced in the current job",
            dataType=o6.UInt64,
            value=0,
        )
    )
    jobPartsCounter: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_rubber;i=6242",
            browseName="ns=plastics_rubber;JobPartsCounter",
            description="Total number of parts produced in the current job",
            dataType=o6.UInt64,
            value=0,
        )
    )
    jobTestSamplesCounter: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_rubber;i=6246",
            browseName="ns=plastics_rubber;JobTestSamplesCounter",
            description="Number of test sample parts produced in the current job",
            dataType=o6.UInt64,
            value=0,
        )
    )
    lastCycleTime: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_rubber;i=6240",
            browseName="ns=plastics_rubber;LastCycleTime",
            description="Time of the recently finished cycle",
            dataType=ns0.datatypes.Duration,
            value=0.0,
        )
    )
    lastPartId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_rubber;i=6248",
            browseName="ns=plastics_rubber;LastPartId",
            description="Id(s) of the parts produced in the recently finished cycle",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[1],
            value=[""],
        )
    )
    machineCycleCounter: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_rubber;i=6238",
            browseName="ns=plastics_rubber;MachineCycleCounter",
            description="Number of finished cycles in the machine life time",
            dataType=o6.UInt64,
            value=0,
        )
    )
    resetAverageCycleTime: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_rubber;i=7042",
            browseName="ns=plastics_rubber;ResetAverageCycleTime",
            description="Initiates a new calculation of the average cycle time for the job",
        )
    )
    resetBoxCounters: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=plastics_rubber;i=7041", browseName="ns=plastics_rubber;ResetBoxCounters", description="Setting the cycle and parts counters for the current box to 0")
    )
    resetJobCounters: o6.node.MethodNode = o6.hasComponent(
        o6.call(nodeId="ns=plastics_rubber;i=7034", browseName="ns=plastics_rubber;ResetJobCounters", description="Setting the cycle and parts counters for the job to 0")
    )
    stopAtCycleEnd: o6.node.MethodNode = o6.hasComponent(
        o6.call(nodeId="ns=plastics_rubber;i=7031", browseName="ns=plastics_rubber;StopAtCycleEnd", description="Directs the machine to stop at the end of the current cycle")
    )


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6275",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7043",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=-1), ns0.datatypes.Argument(name="Components", dataType=o6.UInt16, valueRank=1)],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7043",
    browseName="ns=plastics_rubber;Load",
    description="Loads a production dataset from the file system of the machine to the control of the machine",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6275"]),
)


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1039",
    browseName="ns=plastics_rubber;ProductionDatasetStatusType",
    displayName="ProductionDatasetStatusType",
    description="Status of a production dataset",
)
class ProductionDatasetStatusType(ns0.objtypes.BaseObjectType):
    frozen: ns0.vartypes.PropertyType | None = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6135",
            browseName="ns=plastics_rubber;Frozen",
            description="Indication if changes on the machine in the production dataset are allowed",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    information: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6104",
            browseName="ns=plastics_rubber;Information",
            description="Set of information on the production dataset",
            dataType=plastics_rubber_datypes.ProductionDatasetInformationType,
            value=plastics_rubber_datypes.ProductionDatasetInformationType(
                name="",
                description="",
                mESId="",
                creationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                lastModificationTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                lastSaveTimestamp=o6.DateTime("1900-01-01T00:00:00Z"),
                userName="",
                components=[],
                manufacturer="",
                serialNumber="",
                model="",
                controllerName="",
                userMachineName="",
                locationName="",
                productName=[""],
                mouldId="",
                numCavities=0,
            ),
        )
    )
    load: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_rubber;i=7043"])
    modified: ns0.vartypes.PropertyType | None = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6105",
            browseName="ns=plastics_rubber;Modified",
            description="Indication if the production dataset has been changed after the last storage",
            dataType=o6.Boolean,
        )
    )
    save: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_rubber;i=7016"])


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6285",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7045",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(name="fileHandle", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="Information", dataType=o6.NodeId("ns=plastics_rubber;i=3006"), valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=plastics_rubber;i=7045",
    browseName="ns=plastics_rubber;SendProductionDatasetInformation",
    description="This Method allows sending of the description of a production dataset during the file transfer from the client to the server with ProductionDatasetTransfer",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6285"]),
)


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1008",
    browseName="ns=plastics_rubber;ProductionDatasetManagementType",
    displayName="ProductionDatasetManagementType",
    description="Management of production datasets",
)
class ProductionDatasetManagementType(ns0.objtypes.BaseObjectType):
    activeProductionDatasetStatus: ProductionDatasetStatusType
    getProductionDatasetInformation: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_rubber;i=7032"])
    productionDatasetInPreparationStatus: ProductionDatasetStatusType | None
    productionDatasetLists: ProductionDatasetListsType | None
    productionDatasetTransfer: ns0.objtypes.TemporaryFileTransferType
    sendProductionDatasetInformation: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_rubber;i=7045"])


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1053",
    browseName="ns=plastics_rubber;MaintenanceType",
    displayName="MaintenanceType",
    description="Provides information on the maintenance status of a machine, device or component",
)
class MaintenanceType(ns0.objtypes.BaseObjectType):
    additionalInformation: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6514",
            browseName="ns=plastics_rubber;AdditionalInformation",
            description="Additional information on the necessary maintenance. Can be also a link to another document.",
            dataType=o6.String,
        )
    )
    interval: ns0.vartypes.AnalogItemType | None
    remainingInterval: ns0.vartypes.AnalogItemType | None
    reset: o6.node.MethodNode = o6.hasComponent(
        o6.call(nodeId="ns=plastics_rubber;i=7046", browseName="ns=plastics_rubber;Reset", description="This Method sets the RemainingInterval to Interval and Status to NOT_DUE_0")
    )
    status: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6311",
            browseName="ns=plastics_rubber;Status",
            description="Maintenance status of the machine/device/component (represented by the parent element)",
            dataType=plastics_rubber_datypes.MaintenanceStatusEnumeration,
            value=plastics_rubber_datypes.MaintenanceStatusEnumeration.NOT_DUE,
        )
    )
    totalOperation: ns0.vartypes.AnalogItemType | None


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1054",
    browseName="ns=plastics_rubber;ClosedLoopControlType",
    displayName="ClosedLoopControlType",
    description="Settings for the closed loop control on the device for a parameter",
)
class ClosedLoopControlType(ns0.objtypes.BaseObjectType):
    autoTuningActive: ns0.vartypes.PropertyType | None = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6320",
            browseName="ns=plastics_rubber;AutoTuningActive",
            description="Informs if the automatic tuning is currently active",
            dataType=o6.Boolean,
        )
    )
    autoTuningOff: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_rubber;i=7048",
            browseName="ns=plastics_rubber;AutoTuningOff",
            description="Stops an already active self-optimisation process (no control parameters are changed)",
        )
    )
    autoTuningOn: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=plastics_rubber;i=7047", browseName="ns=plastics_rubber;AutoTuningOn", description="Starts the self-optimisation of the controller")
    )
    automaticControllerMode: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6319",
            browseName="ns=plastics_rubber;AutomaticControllerMode",
            description="Determination if PID Parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    pIDParameters: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6318",
            browseName="ns=plastics_rubber;PIDParameters",
            description="PID Parameters as array if several input signals (sensors) are used for the control",
            dataType=plastics_rubber_datypes.PIDParametersDataType,
            valueRank=1,
            arrayDimensions=[1],
            value=[plastics_rubber_datypes.PIDParametersDataType(p=0.0, i=0.0, d=0.0)],
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1056",
    browseName="ns=plastics_rubber;MonitoredParameterType",
    displayName="MonitoredParameterType",
    description="Used for process parameters that are monitored by the client",
)
class MonitoredParameterType(ns0.objtypes.BaseObjectType):
    actualValue: ns0.vartypes.AnalogItemType
    alarmSuppression: ns0.vartypes.MultiStateValueDiscreteType | None
    automaticMonitoring: ns0.vartypes.PropertyType | None = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6350",
            browseName="ns=plastics_rubber;AutomaticMonitoring",
            description="Determination if monitoring tolerance parameters are determined by auto-tuning itself (TRUE) or can be manually adjusted (FALSE)",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    lowerTolerance: ns0.vartypes.AnalogItemType | None
    lowerTolerance2: ns0.vartypes.AnalogItemType | None
    maxValue: ns0.vartypes.AnalogItemType | None
    minValue: ns0.vartypes.AnalogItemType | None
    monitoringSensitivity: ns0.vartypes.MultiStateValueDiscreteType | None
    resetMonitoring: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_rubber;i=7053",
            browseName="ns=plastics_rubber;ResetMonitoring",
            description="With this method the tolerance values are set according to the actual value and the set monitoring sensitivity",
        )
    )
    setRampDown: ns0.vartypes.AnalogItemType | None
    setRampUp: ns0.vartypes.AnalogItemType | None
    setValue: ns0.vartypes.AnalogItemType | None
    status: ns0.vartypes.MultiStateValueDiscreteType | None
    upperTolerance: ns0.vartypes.AnalogItemType | None
    upperTolerance2: ns0.vartypes.AnalogItemType | None


@o6.objecttype(
    nodeId="ns=plastics_rubber;i=1057",
    browseName="ns=plastics_rubber;ControlledParameterType",
    displayName="ControlledParameterType",
    description="Used for process parameters that are controlled by the client by writing a set value and optional ramps and parameters for closed loop control",
)
class ControlledParameterType(MonitoredParameterType):
    closedLoopControl: ClosedLoopControlType | None
    setRampDown: ns0.vartypes.AnalogItemType | None
    setRampUp: ns0.vartypes.AnalogItemType | None


@o6.objecttype(nodeId="ns=plastics_rubber;i=1064", browseName="ns=plastics_rubber;MeasuringDeviceType", displayName="MeasuringDeviceType")
class MeasuringDeviceType(ControlledParameterType):
    controlMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6428",
            browseName="ns=plastics_rubber;ControlMode",
            dataType=plastics_rubber_datypes.ControlModeEnumeration,
            value=plastics_rubber_datypes.ControlModeEnumeration.OTHER,
        )
    )
    id: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6424", browseName="ns=plastics_rubber;Id", dataType=o6.String, value=""))
    isPresent: ns0.vartypes.PropertyType = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6427", browseName="ns=plastics_rubber;IsPresent", dataType=o6.Boolean)
    )
    maintenance: MaintenanceType | None
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6425", browseName="ns=plastics_rubber;Name", dataType=o6.LocalizedText, value=o6.LocalizedText())
    )
    position: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6426", browseName="ns=plastics_rubber;Position", dataType=o6.String)
    )
    startDevice: StartDeviceType | None


@o6.objecttype(nodeId="ns=plastics_rubber;i=1023", browseName="ns=plastics_rubber;StartDeviceType", displayName="StartDeviceType")
class StartDeviceType(ns0.objtypes.BaseObjectType):
    startBlockedByClient: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6101", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    startRequest: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=plastics_rubber;i=7051", browseName="ns=plastics_rubber;StartRequest"))
    status: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_rubber;i=6010",
            browseName="ns=plastics_rubber;Status",
            dataType=plastics_rubber_datypes.StartEnumeration,
            value=plastics_rubber_datypes.StartEnumeration.NOT_READY_TO_START,
        )
    )
    stopRequest: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=plastics_rubber;i=7056", browseName="ns=plastics_rubber;StopRequest"))


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6100",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7057",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Name", dataType=o6.LocalizedText, valueRank=-1),
        ns0.datatypes.Argument(name="Density", dataType=o6.Double, valueRank=-1),
    ],
)
o6.call(nodeId="ns=plastics_rubber;i=7057", browseName="ns=plastics_rubber;AddMaterial", inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6100"]))

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_rubber;i=6307",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_rubber;i=7058",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(nodeId="ns=plastics_rubber;i=7058", browseName="ns=plastics_rubber;RemoveMaterialById", inputArgs=o6.hasProperty(o6.ns["ns=plastics_rubber;i=6307"]))


@o6.objecttype(nodeId="ns=plastics_rubber;i=1059", browseName="ns=plastics_rubber;MaterialListType", displayName="MaterialListType")
class MaterialListType(ns0.objtypes.BaseObjectType):
    addMaterial: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_rubber;i=7057"])
    densityUnit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6512", browseName="ns=plastics_rubber;DensityUnit", dataType=ns0.datatypes.EUInformation)
    )
    material_LangleNrRangle: MaterialType | None
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6306", browseName="NodeVersion", dataType=o6.String, value=""))
    removeMaterialById: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_rubber;i=7058"])


o6.reference(MaterialListType, "i=41", "i=2133")
o6.reference(MaterialListType, "i=41", RequestAddMaterialEventType)


@o6.objecttype(nodeId="ns=plastics_rubber;i=1066", browseName="ns=plastics_rubber;DiagnosticsType", displayName="DiagnosticsType")
class DiagnosticsType(ns0.objtypes.BaseObjectType):
    runDiagnostics: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="ns=plastics_rubber;i=7059", browseName="ns=plastics_rubber;RunDiagnostics"))
    status: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_rubber;i=6503", browseName="ns=plastics_rubber;Status", dataType=plastics_rubber_datypes.DiagnosticsStatusEnumeration)
    )
    stopDiagnostics: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="ns=plastics_rubber;i=7060", browseName="ns=plastics_rubber;StopDiagnostics"))


o6.reference(DiagnosticsType, "i=41", DiagnosisEndEventType)
o6.reference(DiagnosticsType, "i=41", DiagnosisStepEndEventType)


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_rubber_datypes
