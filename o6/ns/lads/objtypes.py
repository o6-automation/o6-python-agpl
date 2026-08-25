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

"""Generated OPC UA lads namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.amb as amb
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
from . import datatypes as lads_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=lads;i=1008",
    browseName="ns=lads;ControllerTuningParameterType",
    displayName="ControllerTuningParameterType",
    description="The ControllerTuningParameterType is an abstract class. It is formally defined in Table 85. Subtypes of the ControllerTuningParameterType contain the parameters and information about a Controller (configuration).",
)
class ControllerTuningParameterType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(
    nodeId="ns=lads;i=1035",
    browseName="ns=lads;SupportedPropertyType",
    displayName="SupportedPropertyType",
    description="The SupportedPropertyType provides alias names and links to variables within the information model, typically target values or parameters of Functions. This makes it possible to specify a list of KeyValuePairs as an input object. The SupportedPropertyType is used in the SupportedPropertiesSet of the FunctionalUnit or ActiveProgram. The name of each Property object is used as a key in the KeyValuePair list input Argument of the Start()/StartFunctions() Method. Each Property object should contain an Organizes Reference to the target variable to which it belongs. Thus, the metadata of the target variable can be introspected online. The name of the Property object is typically an alias for a variable in the Device.",
)
class SupportedPropertyType(ns0.objtypes.BaseObjectType):
    pass


di.objtypes.FunctionalGroupType(nodeId="ns=lads;i=5003", browseName="ns=di;Identification", description="Used to organize parameters for identification of this functional unit.")
di.objtypes.FunctionalGroupType(
    nodeId="ns=lads;i=5009",
    browseName="ns=lads;Operational",
    description="Operational is a FunctionalGroup that shall organize the CurrentState property of the StateMachine and all its remote invocable Methods. Furthermore, it shall organize at least the CurrentValue and TargetValue variables.",
)
di.objtypes.FunctionalGroupType(nodeId="ns=lads;i=5011", browseName="ns=lads;Operational", description="Used to organize parameters for operation of this function.")
di.objtypes.FunctionalGroupType(nodeId="ns=lads;i=5024", browseName="ns=lads;Operational", description="Used to organize parameters for operation of this function.")
di.objtypes.FunctionalGroupType(
    nodeId="ns=lads;i=5058",
    browseName="ns=lads;Operational",
    description="Operational is a FunctionalGroup that shall organize the CurrentState property of the StateMachine and all its remote invocable Methods. Furthermore, it shall organize at least the CurrentValue and TargetValue variables.",
)
di.objtypes.FunctionalGroupType(
    nodeId="ns=lads;i=5059",
    browseName="ns=lads;Operational",
    description="Operational is a FunctionalGroup that shall organize the CurrentState property of the StateMachine and all its remote invocable Methods. Furthermore, it shall organize at least the CurrentValue and TargetValue variables.",
)
di.objtypes.FunctionalGroupType(nodeId="ns=lads;i=5061", browseName="ns=lads;Operational", description="Used to organize parameters for operation of this function.")
di.objtypes.FunctionalGroupType(nodeId="ns=lads;i=5064", browseName="ns=lads;Operational", description="Operational organizes the methods and current state of the cover function.")
di.objtypes.FunctionalGroupType(
    nodeId="ns=lads;i=5084",
    browseName="ns=lads;Operational",
    description="Operational is a FunctionalGroup that shall organize the CurrentState property of the StateMachine and all its remote invocable Methods. Furthermore, it shall organize at least the CurrentValue and TargetValue variables.",
)
ns0.objtypes.FolderType(
    nodeId="ns=lads;i=5088",
    browseName="ns=machinery;MachineryBuildingBlocks",
    description="The MachineryBuildingBlocks folder contains all machinery building blocks, especially the MachineryItemState, MachineryOperationMode, OperationCounter and Lifetime Counters.",
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=lads;i=5089",
    browseName="ns=machinery;MachineryItemState",
    description="MachineryItemState indicates the current state of the device in conformance with the Machinery Basics specification.",
)
machinery.objtypes.MachineryOperationCounterType(
    nodeId="ns=lads;i=5093",
    browseName="ns=di;OperationCounters",
    description="OperationCounters for monitoring the condition of the device or component in conformance with the Devices specification.",
)
machinery.objtypes.MachineryLifetimeCounterType(
    nodeId="ns=lads;i=5094", browseName="ns=machinery;LifetimeCounters", description="Lifetime Counter provides information about the past and estimated remaining lifetime."
)
o6.reference(o6.ns["ns=lads;i=5088"], "i=17604", o6.ns["ns=lads;i=5094"])
machinery.objtypes.MachineryComponentIdentificationType(
    nodeId="ns=lads;i=5095", browseName="ns=di;Identification", description="Identification provides properties to identify a device or component."
)
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=lads;i=5096", browseName="ns=di;Identification", description="Identification provides properties to identify a device or component."
)
machinery.objtypes.MachineryOperationCounterType(nodeId="ns=lads;i=5097", browseName="ns=di;OperationCounters")
o6.reference(o6.ns["ns=lads;i=5088"], "i=17604", o6.ns["ns=lads;i=5097"])
di.objtypes.FunctionalGroupType(
    nodeId="ns=lads;i=5113",
    browseName="ns=lads;Operational",
    description="Operational is a FunctionalGroup that shall organize the CurrentState property of the StateMachine and all its remote invocable Methods. Furthermore, it shall organize at least the CurrentValue and TargetValue variables.",
)
ns0.vartypes.AnalogUnitRangeType(nodeId="ns=lads;i=6001", browseName="ns=lads;CurrentValue", description="CurrentValue is the current process value.", dataType=o6.Double)
o6.reference(o6.ns["ns=lads;i=5009"], "i=35", o6.ns["ns=lads;i=6001"])


@o6.objecttype(nodeId="ns=lads;i=1004", browseName="ns=lads;FunctionType", displayName="FunctionType", description="Abstract function type", isAbstract=True)
class FunctionType(di.objtypes.TopologyElementType):
    configuration: di.objtypes.FunctionalGroupType | None = o6.hasComponent(
        di.objtypes.FunctionalGroupType(
            nodeId="ns=lads;i=5012", browseName="ns=lads;Configuration", description="Configuration is used to organize parameters for configuration of the Function."
        )
    )
    functionSet: FunctionSetType | None
    isEnabled: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6002",
            browseName="ns=lads;IsEnabled",
            description="IsEnabled indicates whether the Function can currently be executed on the Device. A Function may be disabled for several reasons including not licensed, missing hardware modules, or missing supplies",
            dataType=o6.Boolean,
            accessLevel=3,
        )
    )


@o6.objecttype(
    nodeId="ns=lads;i=1005",
    browseName="ns=lads;BaseSensorFunctionType",
    displayName="BaseSensorFunctionType",
    description="The BaseSensorFunctionType is an abstract ObjectType used as a base for derivation of Sensor Functions. A Sensor Function is a Function that measures data.",
    isAbstract=True,
)
class BaseSensorFunctionType(FunctionType):
    configuration: di.objtypes.FunctionalGroupType | None


@o6.objecttype(
    nodeId="ns=lads;i=1007",
    browseName="ns=lads;BaseControlFunctionType",
    displayName="BaseControlFunctionType",
    description="The BaseControlFunctionType provides an abstract superclass for all control functions.",
    isAbstract=True,
)
class BaseControlFunctionType(FunctionType):
    alarmMonitor: ns0.objtypes.ExclusiveDeviationAlarmType | None
    controlFunctionState: ControlFunctionStateMachineType
    controllerTuningParameter: ControllerTuningParameterType | None = o6.hasComponent(
        ControllerTuningParameterType(
            nodeId="ns=lads;i=5001",
            browseName="ns=lads;ControllerTuningParameter",
            description="The ControllerTuningParameterType is an abstract class. It is formally defined in Table 85. Subtypes of the ControllerTuningParameterType contain the parameters and information about a Controller (configuration).",
        )
    )
    operational: di.objtypes.FunctionalGroupType


@o6.objecttype(
    nodeId="ns=lads;i=1011",
    browseName="ns=lads;CoverFunctionType",
    displayName="CoverFunctionType",
    description="The CoverFunctionType is used to control the cover, door, or lid of a Laboratory Device.",
)
class CoverFunctionType(FunctionType):
    coverState: CoverStateMachineType
    operational: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=lads;i=5064"])


@o6.objecttype(
    nodeId="ns=lads;i=1013",
    browseName="ns=lads;TimerControlFunctionType",
    displayName="TimerControlFunctionType",
    description="The TimerControlFunctionType defines a simple “one shot” Timer which stops once it has elapsed. It follows the design of other LADS ControlFunctions, utilizing the same state machine and similar variable definitions. As soon as the CurrentValue reaches the TargetValue, the CurrentState of the TimerFunction automatically transitions to Off. This is typically accompanied by some (internal) action/effect, such as stopping the execution of a Function or similar. In the SuspendedState the CurrentValue holds its current value and does not count further until the state switches back to On, either due to a Client command or an internal state change.",
)
class TimerControlFunctionType(BaseControlFunctionType):
    currentValue: ns0.vartypes.AnalogUnitRangeType | None
    differenceValue: ns0.vartypes.AnalogUnitRangeType | None
    operational: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=lads;i=5113"])
    targetValue: ns0.vartypes.AnalogUnitRangeType | None


@o6.objecttype(
    nodeId="ns=lads;i=1051",
    browseName="ns=lads;MultiSensorFunctionType",
    displayName="MultiSensorFunctionType",
    description="The MultiSensorFunction represents complex detectors with multiple sensors targeting a specific measurement task, e.g. diode array detector of a HPLC system. The specific sensor elements are represented by sensor-functions in the FunctionSet.",
)
class MultiSensorFunctionType(BaseSensorFunctionType):
    functionSet: FunctionSetType


@o6.objecttype(
    nodeId="ns=lads;i=1030",
    browseName="ns=lads;PidControllerParameterType",
    displayName="PidControllerParameterType",
    description="The PidControllerParameterType contains the parameters of an PID controller.",
)
class PidControllerParameterType(ControllerTuningParameterType):
    ctrlP: ns0.vartypes.AnalogUnitRangeType | None = o6.hasComponent(
        ns0.vartypes.AnalogUnitRangeType(
            nodeId="ns=lads;i=6003", browseName="ns=lads;CtrlP", description="CtrlP is the proportional controller parameter", dataType=o6.Double, accessLevel=3
        )
    )
    ctrlTd: ns0.vartypes.AnalogUnitRangeType | None = o6.hasComponent(
        ns0.vartypes.AnalogUnitRangeType(
            nodeId="ns=lads;i=6004", browseName="ns=lads;CtrlTd", description="CtrlTd is the derivate controller parameter", dataType=o6.Double, accessLevel=3
        )
    )
    ctrlTi: ns0.vartypes.AnalogUnitRangeType | None = o6.hasComponent(
        ns0.vartypes.AnalogUnitRangeType(
            nodeId="ns=lads;i=6005", browseName="ns=lads;CtrlTi", description="CtrlTi is the integrator controller parameter.", dataType=o6.Double, accessLevel=3
        )
    )


ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=lads;i=6006", browseName="ns=lads;TargetValue", description="TargetValue is the targeted set-point value.", dataType=o6.Double, accessLevel=3
)
o6.reference(o6.ns["ns=lads;i=5009"], "i=35", o6.ns["ns=lads;i=6006"])


@o6.objecttype(
    nodeId="ns=lads;i=1009",
    browseName="ns=lads;AnalogControlFunctionType",
    displayName="AnalogControlFunctionType",
    description="The AnalogControlFunctionType describes an analogue control function (using analogue values). More specialized analogue control functions can be derived from this ObjectType.",
)
class AnalogControlFunctionType(BaseControlFunctionType):
    controlFunctionState: ControlFunctionStateMachineType
    currentValue: ns0.vartypes.AnalogUnitRangeType = o6.hasComponent(o6.ns["ns=lads;i=6001"])
    operational: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=lads;i=5009"])
    targetValue: ns0.vartypes.AnalogUnitRangeType = o6.hasComponent(o6.ns["ns=lads;i=6006"])


ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6008",
    browseName="ns=di;RevisionCounter",
    description="An incremental counter indicating the number of times the static data within the Device has been modified",
    dataType=o6.Int32,
)
o6.reference(o6.ns["ns=lads;i=5096"], "i=46", o6.ns["ns=lads;i=6008"])
ns0.vartypes.PropertyType(nodeId="ns=lads;i=6009", browseName="ns=di;Manufacturer", description="Name of the company that manufactured the device", dataType=o6.LocalizedText)
o6.reference(o6.ns["ns=lads;i=5096"], "i=46", o6.ns["ns=lads;i=6009"])
ns0.vartypes.PropertyType(nodeId="ns=lads;i=6010", browseName="ns=di;Model", description="Model name of the device", dataType=o6.LocalizedText)
o6.reference(o6.ns["ns=lads;i=5096"], "i=46", o6.ns["ns=lads;i=6010"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=lads;i=6011",
    browseName="ns=lads;TotalizedValue",
    description="TotalizedValue is the totalized process value. It can be reset at any time using the ResetTotalizer() command.",
    dataType=o6.Double,
)
o6.reference(o6.ns["ns=lads;i=5059"], "i=35", o6.ns["ns=lads;i=6011"])


@o6.objecttype(nodeId="ns=lads;i=1034", browseName="ns=lads;LADSOperationCountersType", displayName="LADSOperationCountersType", interfaces=[di.objtypes.IOperationCounterType])
class LADSOperationCountersType(machinery.objtypes.MachineryOperationCounterType):
    lifeTime: di.vartypes.LifetimeVariableType | None = o6.hasComponent(
        di.vartypes.LifetimeVariableType(nodeId="ns=lads;i=6027", browseName="ns=lads;LifeTime", dataType=ns0.datatypes.Number, accessLevel=3)
    )


ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6028",
    browseName="ns=amb;OperationalLocation",
    description="OperationalLocation provides the operational location of the Device or Component. The structure within the string may expose several levels. How this is exposed, which delimiters are used, etc. is vendor-specific. Examples of such strings are “Warehouse1/Sheet3” or “StainlessSteelTote3” (see OPC UA OPC 10000-110 for more details).",
    dataType=o6.String,
    accessLevel=3,
)
o6.reference(o6.ns["ns=lads;i=5096"], "i=35", o6.ns["ns=lads;i=6028"])
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6029",
    browseName="ns=amb;HierarchicalLocation",
    description="HierarchicalLocation provides the hierarchical location of the LADSDevice.The structure within the string may expose several levels. How this is exposed, which delimiters are used, etc. is vendor-specific. Examples of such strings are “FactoryA/BuildingC/Floor1” or “Area1-ProcessCell17-Unit4” (see OPC UA OPC 10000-110 for more details).",
    dataType=o6.String,
    accessLevel=3,
)
o6.reference(o6.ns["ns=lads;i=5096"], "i=35", o6.ns["ns=lads;i=6029"])
ns0.vartypes.DiscreteItemType(nodeId="ns=lads;i=6031", browseName="ns=lads;SensorValue", description="SensorValue is a discrete measurement value.", _allow_abstract=True)
o6.reference(o6.ns["ns=lads;i=5061"], "i=35", o6.ns["ns=lads;i=6031"])


@o6.objecttype(
    nodeId="ns=lads;i=1012",
    browseName="ns=lads;DiscreteSensorFunctionType",
    displayName="DiscreteSensorFunctionType",
    description="The DiscreteSensorFunctionType is an abstract ObjectType used as a base for derivation of sensors with discrete signals.",
    isAbstract=True,
)
class DiscreteSensorFunctionType(BaseSensorFunctionType):
    operational: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=lads;i=5061"])
    sensorValue: ns0.vartypes.DiscreteItemType = o6.hasComponent(o6.ns["ns=lads;i=6031"])


@o6.objecttype(
    nodeId="ns=lads;i=1031",
    browseName="ns=lads;TwoStateDiscreteSensorFunctionType",
    displayName="TwoStateDiscreteSensorFunctionType",
    description="The TwoStateDiscreteSensorFunctionType represents a Boolean value that is measured by a Sensor.",
)
class TwoStateDiscreteSensorFunctionType(DiscreteSensorFunctionType):
    sensorValue: ns0.vartypes.TwoStateDiscreteType


@o6.objecttype(
    nodeId="ns=lads;i=1037",
    browseName="ns=lads;MultiStateDiscreteSensorFunctionType",
    displayName="MultiStateDiscreteSensorFunctionType",
    description="The MultiStateDiscreteSensorFunctionType represents a value that is measured by a Sensor and can only be set to a discrete set of values.",
)
class MultiStateDiscreteSensorFunctionType(DiscreteSensorFunctionType):
    sensorValue: ns0.vartypes.MultiStateDiscreteType


ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=lads;i=6033", browseName="ns=lads;SensorValue", description="SensorValue is the calibrated and optionally compensated/filtered process value.", dataType=o6.Double
)
o6.reference(o6.ns["ns=lads;i=5024"], "i=35", o6.ns["ns=lads;i=6033"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=lads;i=6039",
    browseName="ns=lads;RawValue",
    description="RawValue is the raw value measured at the Sensor element, such as the Nernst voltage of a pH Sensor element.",
    dataType=o6.Double,
)
o6.reference(o6.ns["ns=lads;i=5024"], "i=35", o6.ns["ns=lads;i=6039"])
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6051",
    browseName="ns=di;DeviceManual",
    description="DeviceManual allows specifying an address of the user manual. It may be a pathname in the file system or a URL (Web address).",
    dataType=o6.String,
)
o6.reference(o6.ns["ns=lads;i=5096"], "i=46", o6.ns["ns=lads;i=6051"])
ns0.vartypes.PropertyType(nodeId="ns=lads;i=6062", browseName="ns=di;DeviceRevision", description="Overall revision level of the device", dataType=o6.String)
o6.reference(o6.ns["ns=lads;i=5096"], "i=46", o6.ns["ns=lads;i=6062"])
ns0.vartypes.PropertyType(nodeId="ns=lads;i=6063", browseName="ns=di;SoftwareRevision", description="Revision level of the software/firmware of the device", dataType=o6.String)
o6.reference(o6.ns["ns=lads;i=5096"], "i=46", o6.ns["ns=lads;i=6063"])
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6064", browseName="ns=di;SerialNumber", description="Identifier that uniquely identifies, within a manufacturer, a device instance", dataType=o6.String
)
o6.reference(o6.ns["ns=lads;i=5096"], "i=46", o6.ns["ns=lads;i=6064"])
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6068",
    browseName="ns=di;AssetId",
    description="AssetId is a user writable alphanumeric character sequence uniquely identifying a component. The ID is provided by the integrator or user of the device.",
    dataType=o6.String,
    accessLevel=3,
)
o6.reference(o6.ns["ns=lads;i=5096"], "i=46", o6.ns["ns=lads;i=6068"])
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6069",
    browseName="ns=di;ComponentName",
    description="ComponentName is a user writable name provided by the integrator or user of the component.",
    dataType=o6.LocalizedText,
    accessLevel=3,
)
o6.reference(o6.ns["ns=lads;i=5096"], "i=46", o6.ns["ns=lads;i=6069"])
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6074",
    browseName="ns=amb;OperationalLocation",
    description="OperationalLocation provides the operational location of the Device or Component. The structure within the string may expose several levels. How this is exposed, which delimiters are used, etc. is vendor-specific. Examples of such strings are “Warehouse1/Sheet3” or “StainlessSteelTote3” (see OPC UA OPC 10000-110 for more details).",
    dataType=o6.String,
    accessLevel=3,
)
o6.reference(o6.ns["ns=lads;i=5095"], "i=35", o6.ns["ns=lads;i=6074"])


@o6.objecttype(nodeId="ns=lads;i=61", browseName="ns=lads;SetType", displayName="SetType", description="The SetType provides an unordered set of objects.", isAbstract=True)
class SetType(ns0.objtypes.FolderType):
    langleSetElementRangle: ns0.objtypes.BaseObjectType | None = o6.hasComponent(
        ns0.objtypes.BaseObjectType(
            nodeId="ns=lads;i=5014",
            browseName="ns=lads;<SetElement>",
            description="SetElement is the element of the set. Subtypes of the SetType will override this node.",
            modellingRule="OptionalPlaceholder",
        )
    )
    nodeVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6075",
            browseName="NodeVersion",
            description="NodeVersion and the GeneralModelChangeEventType are mechanisms to notify clients that the content of the set has changed and shall be used as defined in OPC 10000-3.",
            dataType=o6.String,
            value="NaN",
            accessLevel=3,
        )
    )


o6.reference(SetType, "i=41", "i=2133")


@o6.objecttype(
    nodeId="ns=lads;i=1026",
    browseName="ns=lads;FunctionSetType",
    displayName="FunctionSetType",
    description="The FunctionSetType is used for organising FunctionType objects in an unordered list structure.",
)
class FunctionSetType(SetType):
    langleSetElementRangle: FunctionType | None = o6.hasComponent(
        FunctionType(
            nodeId="ns=lads;i=5027",
            browseName="ns=lads;<SetElement>",
            description="SetElement is the element of the set and is overridden with FunctionType.",
            modellingRule="OptionalPlaceholder",
            _allow_abstract=True,
        )
    )


@o6.objecttype(
    nodeId="ns=lads;i=1027",
    browseName="ns=lads;MaintenanceSetType",
    displayName="MaintenanceSetType",
    description="The MaintenanceSetType is a set containing all maintenance tasks for a Device or Component according to the recommendations in OPC UA 10000-110.",
)
class MaintenanceSetType(SetType):
    langleSetElementRangle: MaintenanceTaskType | None


o6.reference(MaintenanceSetType, "i=41", "i=2133")


@o6.objecttype(
    nodeId="ns=lads;i=1033",
    browseName="ns=lads;SupportedPropertiesSetType",
    displayName="SupportedPropertiesSetType",
    description="The SupportedPropertiesSetType provides a set of properties which are supported as members of a properties list Argument for Method calls such as, FunctionalUnit.StartFunctions() or ActiveProgram.Start().",
)
class SupportedPropertiesSetType(SetType):
    langleSetElementRangle: SupportedPropertyType | None = o6.hasComponent(
        SupportedPropertyType(
            nodeId="ns=lads;i=5048",
            browseName="ns=lads;<SetElement>",
            description="SetElement is the element of the set and is overridden with SupportedPropertiesType.",
            modellingRule="OptionalPlaceholder",
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6080",
    browseName="ns=amb;HierarchicalLocation",
    description="HierarchicalLocation provides the hierarchical location of the LADS Device.The structure inside the string may expose several levels. How this is exposed, which delimiters are used, etc. is vendor-specific. Examples of such strings are “FactoryA/BuildingC/Floor1” or “Area1-ProcessCell17-Unit4” (see OPC UA OPC 10000-110 for more Details).",
    dataType=o6.String,
    accessLevel=3,
)
o6.reference(o6.ns["ns=lads;i=5095"], "i=35", o6.ns["ns=lads;i=6080"])


@o6.objecttype(
    nodeId="ns=lads;i=1041",
    browseName="ns=lads;VariableSetType",
    displayName="VariableSetType",
    description="The VariableSetType is used for storing additional sample data that was created during a run.",
)
class VariableSetType(SetType):
    langleSetElementRangle: ns0.objtypes.BaseObjectType | None = o6.hasComponent(
        ns0.objtypes.BaseObjectType(
            nodeId="ns=lads;i=5086",
            browseName="ns=lads;<SetElement>",
            description="Placeholder for one or more objects that hold vendor-specific data that was created during a run. Objects follow these rules: The type of each object shall be BaseObjectType. Each object may have arbitrary child nodes; The structure and data contained in each object are vendor specific; It is up to the vendor whether the list contains objects with the same kind of data or objects of different kinds of data; The structure may be nested.",
            modellingRule="OptionalPlaceholder",
        )
    )
    langleVariableSetElementRangle: ns0.vartypes.BaseVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseVariableType(
            nodeId="ns=lads;i=6082",
            browseName="ns=lads;<VariableSetElement>",
            description="Placeholder for vendor-specific properties.",
            modellingRule="OptionalPlaceholder",
            _allow_abstract=True,
            accessLevel=3,
        )
    )


o6.reference(VariableSetType, "i=41", "i=2133")


@o6.objecttype(
    nodeId="ns=lads;i=1052",
    browseName="ns=lads;AnalogControlFunctionWithComposedTargetValueType",
    displayName="AnalogControlFunctionWithComposedTargetValueType",
    description="The AnalogControlFunctionWithComposedTargetValueType describes an analogue control function (using analogue values), but the TargetValue is composed of several partial values. An example of a composed target value used in mechanical stress analysers involves combining a static/constant base value with periodically changing values for defined amplitude, frequency, and waveform. As the TargetValue is calculated from variables in the TargetValueSet, it should be read-only.",
)
class AnalogControlFunctionWithComposedTargetValueType(AnalogControlFunctionType):
    targetValueSet: VariableSetType = o6.hasComponent(
        VariableSetType(nodeId="ns=lads;i=5087", browseName="ns=lads;TargetValueSet", description="TargetValueSet contains the partial values for the target value.")
    )


ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=lads;i=6089",
    browseName="ns=lads;IncreaseRate",
    description="Rate by which the internal target-value is increased on change (e.g., acceleration ramp, aspirating action, ..).",
    dataType=o6.Double,
    accessLevel=3,
)
o6.reference(o6.ns["ns=lads;i=5084"], "i=35", o6.ns["ns=lads;i=6089"])
ns0.vartypes.PropertyType(nodeId="ns=lads;i=6093", browseName="ns=di;HardwareRevision", description="Revision level of the hardware of the device", dataType=o6.String)
o6.reference(o6.ns["ns=lads;i=5096"], "i=46", o6.ns["ns=lads;i=6093"])
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6094",
    browseName="ns=di;ManufacturerUri",
    description="ManufacturerUri provides a unique identifier for this company. This identifier should be a fully qualified domain name; however, it may be a GUID or similar construct that ensures global uniqueness.",
    dataType=o6.String,
)
o6.reference(o6.ns["ns=lads;i=5096"], "i=46", o6.ns["ns=lads;i=6094"])
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6095",
    browseName="ns=di;ProductCode",
    description="ProductCode provides a unique combination of numbers and letters used to identify the product. It may be the order information displayed on type shields or in ERP systems.",
    dataType=o6.String,
)
o6.reference(o6.ns["ns=lads;i=5096"], "i=46", o6.ns["ns=lads;i=6095"])
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6096",
    browseName="ns=di;ProductInstanceUri",
    description="ProductInstanceUri is a globally unique resource identifier provided by the manufacturer. This is often stamped on the outside of a physical component and may be used for traceability and warranty purposes.",
    dataType=o6.String,
)
o6.reference(o6.ns["ns=lads;i=5096"], "i=46", o6.ns["ns=lads;i=6096"])


@o6.objecttype(nodeId="ns=lads;i=1048", browseName="ns=lads;ControllerParameterType", displayName="ControllerParameterType")
class ControllerParameterType(ns0.objtypes.BaseObjectType):
    alarmMonitor: ns0.objtypes.ExclusiveDeviationAlarmType | None = o6.hasComponent(
        ns0.objtypes.ExclusiveDeviationAlarmType(
            nodeId="ns=lads;i=5146",
            browseName="ns=lads;AlarmMonitor",
            description="AlarmMonitor indicates whether the deviation from a set point exceeds the limit. See: 10000-9: Alarms & Conditions | ExclusiveDeviationAlarmType.",
        )
    )
    currentValue: ns0.vartypes.AnalogUnitRangeType = o6.hasComponent(
        ns0.vartypes.AnalogUnitRangeType(nodeId="ns=lads;i=6109", browseName="ns=lads;CurrentValue", description="CurrentValue is the current process value.", dataType=o6.Double)
    )
    targetValue: ns0.vartypes.AnalogUnitRangeType = o6.hasComponent(
        ns0.vartypes.AnalogUnitRangeType(
            nodeId="ns=lads;i=6110", browseName="ns=lads;TargetValue", description="TargetValue is the targeted set-point value.", dataType=o6.Double, accessLevel=3
        )
    )


@o6.objecttype(
    nodeId="ns=lads;i=1049",
    browseName="ns=lads;ControllerParameterSetType",
    displayName="ControllerParameterSetType",
    description="The ControllerParameterSetType is used for organising ControllerParameterType objects in an unordered list structure.",
)
class ControllerParameterSetType(SetType):
    langleSetElementRangle: ControllerParameterType | None = o6.hasComponent(
        ControllerParameterType(
            nodeId="ns=lads;i=5023",
            browseName="ns=lads;<SetElement>",
            description="SetElement is the element of the set. Subtypes of the SetType will override this node.",
            modellingRule="OptionalPlaceholder",
        )
    )


@o6.objecttype(
    nodeId="ns=lads;i=1047",
    browseName="ns=lads;MultiModeAnalogControlFunctionType",
    displayName="MultiModeAnalogControlFunctionType",
    description="The MultiModeAnalogControlFunctionType is used when a controller or actuator can be operated in different modes, depending on how the target value and current value are represented. A common example in the laboratory and analytical domain is a peristaltic pump. In this case, the user can choose from various operation modes, such as relative pump speed (0 to 100%), absolute pump rotor speed in RPM, volumetric rate in mL/min (requiring pump calibration), or mass flow rate in g/min (requiring knowledge of the fluid density). Another example in the laboratory and analytical domain is centrifuges. Operators can select between RPM or RCF (Rotational Centrifugal Force, defined as a multiple of G-force) modes. The RCF mode considers the radius of the centrifuge rotor when converting RCF to RPM.",
)
class MultiModeAnalogControlFunctionType(BaseControlFunctionType):
    controllerModeSet: ControllerParameterSetType = o6.hasComponent(
        ControllerParameterSetType(nodeId="ns=lads;i=5076", browseName="ns=lads;ControllerModeSet", description="ControllerModeSet is the set of target/current value pairs.")
    )
    currentMode: ns0.vartypes.MultiStateDiscreteType
    operational: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=lads;i=5058"])


ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=lads;i=6112",
    browseName="ns=lads;SensorValue",
    description="SensorValue is the calibrated and optionally compensated/filtered process value.",
    dataType=o6.Double,
    valueRank=-2,
    accessLevel=3,
)
o6.reference(o6.ns["ns=lads;i=5011"], "i=35", o6.ns["ns=lads;i=6112"])


@o6.objecttype(
    nodeId="ns=lads;i=1046",
    browseName="ns=lads;AnalogSensorFunctionType",
    displayName="AnalogSensorFunctionType",
    description="The AnalogSensorFunctionType is a abstract subtype of the BaseSensorFunctionType which represents an analogue measured value. This is an extension point for all analogue measured values without built-in compensation on the Sensor.",
    isAbstract=True,
)
class AnalogSensorFunctionType(BaseSensorFunctionType):
    alarmMonitor: ns0.objtypes.ExclusiveLevelAlarmType | None
    calibration: di.objtypes.FunctionalGroupType | None
    operational: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=lads;i=5011"])
    rawValue: ns0.vartypes.AnalogUnitRangeType = o6.hasComponent(
        ns0.vartypes.AnalogUnitRangeType(
            nodeId="ns=lads;i=6040",
            browseName="ns=lads;RawValue",
            description="RawValue is the raw value measured at the Sensor element, such as the Nernst voltage of a pH Sensor element.",
            dataType=o6.Double,
            valueRank=-2,
            accessLevel=3,
        )
    )
    sensorValue: ns0.vartypes.AnalogUnitRangeType = o6.hasComponent(o6.ns["ns=lads;i=6112"])
    tuning: di.objtypes.FunctionalGroupType | None


@o6.objecttype(
    nodeId="ns=lads;i=1016",
    browseName="ns=lads;AnalogScalarSensorFunctionType",
    displayName="AnalogScalarSensorFunctionType",
    description="The AnalogScalarSensorFunctionType is a concrete subtype of the AnalogSensorFunctionType which represents an analogue measured value.",
)
class AnalogScalarSensorFunctionType(AnalogSensorFunctionType):
    operational: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=lads;i=5024"])
    rawValue: ns0.vartypes.AnalogUnitRangeType = o6.hasComponent(o6.ns["ns=lads;i=6039"])
    sensorValue: ns0.vartypes.AnalogUnitRangeType = o6.hasComponent(o6.ns["ns=lads;i=6033"])


@o6.objecttype(
    nodeId="ns=lads;i=1000",
    browseName="ns=lads;AnalogScalarSensorFunctionWithCompensationType",
    displayName="AnalogScalarSensorFunctionWithCompensationType",
    description="The AnalogScalarSensorFunctionWithCompensationType represents a compensated  analogue measured value (e.g. pH sensor, dissolved oxygen sensor, ..)",
)
class AnalogScalarSensorFunctionWithCompensationType(AnalogScalarSensorFunctionType):
    compensationValue: ns0.vartypes.AnalogUnitRangeType = o6.hasComponent(
        ns0.vartypes.AnalogUnitRangeType(
            nodeId="ns=lads;i=6037",
            browseName="ns=lads;CompensationValue",
            description="CompensationValue is the compensation value used while calculating the process value, such as the temperature at the Sensor element for pH or DO Sensors.",
            dataType=o6.Double,
            accessLevel=3,
        )
    )


@o6.objecttype(
    nodeId="ns=lads;i=1017",
    browseName="ns=lads;DiscreteControlFunctionType",
    displayName="DiscreteControlFunctionType",
    description="The DiscreteControlFunctionType describes an abstract discrete control function (using discrete values). More specialized discrete control functions can be derived from this ObjectType.",
    isAbstract=True,
)
class DiscreteControlFunctionType(BaseControlFunctionType):
    currentValue: ns0.vartypes.DiscreteItemType = o6.hasComponent(
        ns0.vartypes.DiscreteItemType(
            nodeId="ns=lads;i=6065", browseName="ns=lads;CurrentValue", description="CurrentValue is a current discrete process value.", _allow_abstract=True
        )
    )
    targetValue: ns0.vartypes.DiscreteItemType = o6.hasComponent(
        ns0.vartypes.DiscreteItemType(
            nodeId="ns=lads;i=6123", browseName="ns=lads;TargetValue", description="TargetValue is the targeted discrete set-point value.", _allow_abstract=True, accessLevel=3
        )
    )


@o6.objecttype(
    nodeId="ns=lads;i=1042",
    browseName="ns=lads;TwoStateDiscreteControlFunctionType",
    displayName="TwoStateDiscreteControlFunctionType",
    description="The TwoStateDiscreteControlFunctionType describes a discrete control function with two possible values (e.g., on/off).",
)
class TwoStateDiscreteControlFunctionType(DiscreteControlFunctionType):
    controlFunctionState: ControlFunctionStateMachineType
    currentValue: ns0.vartypes.TwoStateDiscreteType
    targetValue: ns0.vartypes.TwoStateDiscreteType


@o6.objecttype(
    nodeId="ns=lads;i=1045",
    browseName="ns=lads;MultiStateDiscreteControlFunctionType",
    displayName="MultiStateDiscreteControlFunctionType",
    description="The MultiStateDiscreteControlFunctionType describes a discrete control function (using more than two discrete values).",
)
class MultiStateDiscreteControlFunctionType(DiscreteControlFunctionType):
    controlFunctionState: ControlFunctionStateMachineType
    currentValue: ns0.vartypes.MultiStateDiscreteType
    targetValue: ns0.vartypes.MultiStateDiscreteType


ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=lads;i=6125",
    browseName="ns=lads;DecreaseRate",
    description="Rate by which the internal target-value is decreased on change (e.g., deceleration/brake ramp, dispensing action, ..).",
    dataType=o6.Double,
    accessLevel=3,
)
o6.reference(o6.ns["ns=lads;i=5084"], "i=35", o6.ns["ns=lads;i=6125"])


@o6.objecttype(
    nodeId="ns=lads;i=1015",
    browseName="ns=lads;AnalogArraySensorFunctionType",
    displayName="AnalogArraySensorFunctionType",
    description="The AnalogArraySensorFunctionType is a concrete subtype of the AnalogSensorFunctionType which represents an array of analogue measured values.",
)
class AnalogArraySensorFunctionType(AnalogSensorFunctionType):
    rawValue: ns0.vartypes.AnalogUnitRangeType = o6.hasComponent(
        ns0.vartypes.AnalogUnitRangeType(
            nodeId="ns=lads;i=6134",
            browseName="ns=lads;RawValue",
            description="RawValue is the raw value measured at the sensor array, such as the electrical current of plate-reader photo-detectors.",
            dataType=o6.Double,
            valueRank=0,
        )
    )
    sensorValue: ns0.vartypes.AnalogUnitRangeType = o6.hasComponent(
        ns0.vartypes.AnalogUnitRangeType(
            nodeId="ns=lads;i=6130",
            browseName="ns=lads;SensorValue",
            description="SensorValue is the calibrated and optionally compensated/filtered array of measurement values.",
            dataType=o6.Double,
            valueRank=0,
        )
    )


ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6149",
    browseName="ns=di;AssetId",
    description="AssetId is a user writable alphanumeric character sequence uniquely identifying a component. The ID is provided by the integrator or user of the device.",
    dataType=o6.String,
    accessLevel=3,
)
o6.reference(o6.ns["ns=lads;i=5095"], "i=46", o6.ns["ns=lads;i=6149"])
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6150",
    browseName="ns=di;ComponentName",
    description="ComponentName is a user writable name provided by the integrator or user of the component.",
    dataType=o6.LocalizedText,
    accessLevel=3,
)
o6.reference(o6.ns["ns=lads;i=5095"], "i=46", o6.ns["ns=lads;i=6150"])
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6151",
    browseName="ns=di;DeviceClass",
    description="DeviceClass indicates in which domain or for what purpose a certain item for which the Interface is applied is used. Examples are “ProgrammableController”, “RemoteIO”, and “TemperatureSensor”.",
    dataType=o6.String,
)
o6.reference(o6.ns["ns=lads;i=5095"], "i=46", o6.ns["ns=lads;i=6151"])
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6152",
    browseName="ns=di;DeviceManual",
    description="DeviceManual allows specifying an address of the user manual. It may be a pathname in the file system or a URL (Web address).",
    dataType=o6.String,
)
o6.reference(o6.ns["ns=lads;i=5095"], "i=46", o6.ns["ns=lads;i=6152"])
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6153",
    browseName="ns=di;DeviceRevision",
    description="DeviceRevision provides the overall revision level of a hardware component or the Device. As an example, this Property can be used in ERP systems together with the ProductCode Property.",
    dataType=o6.String,
)
o6.reference(o6.ns["ns=lads;i=5095"], "i=46", o6.ns["ns=lads;i=6153"])
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6154", browseName="ns=di;HardwareRevision", description="HardwareRevision provides the revision level of the hardware.", dataType=o6.String
)
o6.reference(o6.ns["ns=lads;i=5095"], "i=46", o6.ns["ns=lads;i=6154"])
ns0.vartypes.PropertyType(nodeId="ns=lads;i=6169", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)
o6.reference(o6.ns["ns=lads;i=5095"], "i=46", o6.ns["ns=lads;i=6169"])
ns0.vartypes.PropertyType(nodeId="ns=lads;i=6170", browseName="ns=di;ManufacturerUri", dataType=o6.String)
o6.reference(o6.ns["ns=lads;i=5095"], "i=46", o6.ns["ns=lads;i=6170"])
ns0.vartypes.PropertyType(nodeId="ns=lads;i=6171", browseName="ns=di;Model", dataType=o6.LocalizedText)
o6.reference(o6.ns["ns=lads;i=5095"], "i=46", o6.ns["ns=lads;i=6171"])
ns0.vartypes.PropertyType(nodeId="ns=lads;i=6172", browseName="ns=di;ProductCode", dataType=o6.String)
o6.reference(o6.ns["ns=lads;i=5095"], "i=46", o6.ns["ns=lads;i=6172"])
ns0.vartypes.PropertyType(nodeId="ns=lads;i=6173", browseName="ns=di;ProductInstanceUri", dataType=o6.String)
o6.reference(o6.ns["ns=lads;i=5095"], "i=46", o6.ns["ns=lads;i=6173"])
ns0.vartypes.PropertyType(nodeId="ns=lads;i=6174", browseName="ns=di;RevisionCounter", dataType=o6.Int32)
o6.reference(o6.ns["ns=lads;i=5095"], "i=46", o6.ns["ns=lads;i=6174"])
ns0.vartypes.PropertyType(nodeId="ns=lads;i=6175", browseName="ns=di;SerialNumber", dataType=o6.String)
o6.reference(o6.ns["ns=lads;i=5095"], "i=46", o6.ns["ns=lads;i=6175"])
ns0.vartypes.PropertyType(nodeId="ns=lads;i=6176", browseName="ns=di;SoftwareRevision", dataType=o6.String)
o6.reference(o6.ns["ns=lads;i=5095"], "i=46", o6.ns["ns=lads;i=6176"])
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6284",
    browseName="ns=di;AssetId",
    description="AssetId is a user-writable alphanumeric character sequence the uniquely identifies a FunctionalUnit (see OPC UA 10000-100).",
    dataType=o6.String,
)
o6.reference(o6.ns["ns=lads;i=5003"], "i=35", o6.ns["ns=lads;i=6284"])
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6285",
    browseName="ns=di;ComponentName",
    description="ComponentName is a user-writable name provided by the integrator or user of the FunctionalUnit.",
    dataType=o6.LocalizedText,
)
o6.reference(o6.ns["ns=lads;i=5003"], "i=35", o6.ns["ns=lads;i=6285"])


@o6.objecttype(
    nodeId="ns=lads;i=1001",
    browseName="ns=lads;ResultFileType",
    displayName="ResultFileType",
    description="ResultFile provides a description of a file that is part of a result of a program managers run.",
)
class ResultFileType(ns0.objtypes.BaseObjectType):
    file: ns0.objtypes.FileType | None = o6.hasComponent(
        ns0.objtypes.FileType(nodeId="ns=lads;i=5072", browseName="ns=lads;File", description="File is the OPC UA node of the file with the method for downloading the file.")
    )
    mimeType: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=lads;i=6297", browseName="ns=lads;MimeType", description="MimeType is the MIME type of the file.", dataType=o6.String)
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6298",
            browseName="ns=lads;Name",
            description="Name is the name that describes the file. The name may be different from the filename on the filesystem.",
            dataType=o6.String,
        )
    )
    uRL: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=lads;i=6299", browseName="ns=lads;URL", description="URL is an URL from which the file can be downloaded.", dataType=o6.String)
    )


@o6.objecttype(
    nodeId="ns=lads;i=1022",
    browseName="ns=lads;ResultFileSetType",
    displayName="ResultFileSetType",
    description="The ResultFileSetType is used for organising ResultFileType objects in an unordered list structure.",
)
class ResultFileSetType(SetType):
    langleSetElementRangle: ResultFileType | None = o6.hasComponent(
        ResultFileType(
            nodeId="ns=lads;i=5060",
            browseName="ns=lads;<SetElement>",
            description="ResultFile provides a description of a file that is part of a result of a program managers run.",
            modellingRule="OptionalPlaceholder",
        )
    )


@o6.objecttype(
    nodeId="ns=lads;i=1040",
    browseName="ns=lads;ActiveProgramType",
    displayName="ActiveProgramType",
    description="The ActiveProgramType specifies the current state of operation of a FunctionalUnit. It provides context and information about the currently active program on the device. This allows users to follow the progress of a program run in a standardized fashion by organising steps into a flat, linear sequence.",
)
class ActiveProgramType(ns0.objtypes.BaseObjectType):
    currentPauseTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6180",
            browseName="ns=lads;CurrentPauseTime",
            description="CurrentPauseTime is the current pause-time of the program- run. The CurrentPauseTime is set to 0 at the start of the program and is counted upwards when the program run is in a Paused state. The Paused state is an aggregation of the Suspended state and the Held State.",
            dataType=ns0.datatypes.Duration,
        )
    )
    currentProgramTemplate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6315",
            browseName="ns=lads;CurrentProgramTemplate",
            description="CurrentProgramTemplate provides the template-id as well as the node-id of the currently executed program.",
            dataType=amb.datatypes.NameNodeIdDataType,
            accessLevel=3,
        )
    )
    currentRuntime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6163",
            browseName="ns=lads;CurrentRuntime",
            description="CurrentRuntime is the current run-time of the program -run. The CurrentRunTime is set to 0 at the start of the program and is counted upwards as long as the program run is not in a Paused state. The Paused state is an aggregation of the Suspended state and the Held state.",
            dataType=ns0.datatypes.Duration,
        )
    )
    currentStepName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6184", browseName="ns=lads;CurrentStepName", description="CurrentStepName is the name of the current step.", dataType=o6.LocalizedText
        )
    )
    currentStepNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6185",
            browseName="ns=lads;CurrentStepNumber",
            description="CurrentStepNumber is the number/index of the current step (incremented whenever the next step is entered). The CurrentStepNumber starts with 1.",
            dataType=o6.UInt32,
        )
    )
    currentStepRuntime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6186",
            browseName="ns=lads;CurrentStepRuntime",
            description="CurrentStepRuntime is the runtime of the current step. The CurrentStepRunTime is set to 0 at the start of the current step and is counted upwards as long as the program run is not in Paused state. The Paused state is an aggregation of the Suspended state and the Held State.",
            dataType=ns0.datatypes.Duration,
        )
    )
    deviceProgramRunId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6126",
            browseName="ns=lads;DeviceProgramRunId",
            description="DeviceProgramRunId represents a device-specific unique internal identifier for this program run. Its value shall be identical to the return value of the last call to the FunctionalUnit’s StartProgram() Method. It is used to identify the result object corresponding to this program run within the FunctionalUnit’s result set.",
            dataType=o6.String,
        )
    )
    estimatedRuntime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6159",
            browseName="ns=lads;EstimatedRuntime",
            description="EstimatedRuntime is the estimated run-time of the current program run. If the runtime cannot be estimated, the StatusCode BadNoData should be sent.",
            dataType=ns0.datatypes.Duration,
        )
    )
    estimatedStepNumbers: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6162",
            browseName="ns=lads;EstimatedStepNumbers",
            description="EstimatedStepNumbers are the estimated total number of steps of the current program run. If the total number cannot be estimated, the StatusCode BadNoData should be sent.",
            dataType=o6.UInt32,
        )
    )
    estimatedStepRuntime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6183",
            browseName="ns=lads;EstimatedStepRuntime",
            description="EstimatedStepRuntime is the estimated run-time of the current program-step. If the run-time cannot estimate, the StatusCode BadNoData should sent.",
            dataType=ns0.datatypes.Duration,
        )
    )


@o6.objecttype(
    nodeId="ns=lads;i=1018", browseName="ns=lads;ProgramTemplateType", displayName="ProgramTemplateType", description="The ProgramTemplateType provides a program template."
)
class ProgramTemplateType(ns0.objtypes.BaseObjectType):
    author: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=lads;i=6348", browseName="ns=lads;Author", description="Author is the user who created the template.", dataType=o6.String)
    )
    created: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=lads;i=6341", browseName="ns=lads;Created", description="Created is the time of the template’s creation.", dataType=o6.DateTime)
    )
    description: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6340", browseName="ns=lads;Description", description="Description is a human-readable description of the template.", dataType=o6.LocalizedText
        )
    )
    deviceTemplateId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6259",
            browseName="ns=lads;DeviceTemplateId",
            description="DeviceTemplateId is the program template's identifier unique within the scope of the device.",
            dataType=o6.String,
        )
    )
    modified: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=lads;i=6344", browseName="ns=lads;Modified", description="Modified is the time of last modification.", dataType=o6.DateTime)
    )
    supervisoryTemplateId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6090",
            browseName="ns=lads;SupervisoryTemplateId",
            description="SupervisoryTemplateId is an optional enterprise-wide unique ID for the template. This can be utilized to refer the template to supervisory systems.",
            dataType=o6.String,
        )
    )
    version: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6346",
            browseName="ns=lads;Version",
            description="Version is the version of the template (the format is at the user’s discretion).",
            dataType=o6.String,
        )
    )


@o6.objecttype(
    nodeId="ns=lads;i=1019",
    browseName="ns=lads;ProgramTemplateSetType",
    displayName="ProgramTemplateSetType",
    description="The ProgramTemplateSetType is used for organising ProgramTemplateType objects in an unordered list structure.",
)
class ProgramTemplateSetType(SetType):
    langleSetElementRangle: ProgramTemplateType | None = o6.hasComponent(
        ProgramTemplateType(
            nodeId="ns=lads;i=5029",
            browseName="ns=lads;<SetElement>",
            description="SetElement is the element of the set and is overridden with ProgramTemplateType.",
            modellingRule="OptionalPlaceholder",
        )
    )
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6133",
            browseName="NodeVersion",
            description="NodeVersion and the GeneralModelChangeEventType are mechanisms to notify clients that the content of the set has changed and shall be used as defined in OPC 10000-3.",
            dataType=o6.String,
            value="NaN",
            accessLevel=3,
        )
    )


@o6.objecttype(
    nodeId="ns=lads;i=1024",
    browseName="ns=lads;LADSComponentType",
    displayName="LADSComponentType",
    description="Devices may be composed of tangible sub-components. A component is represented by the LADSComponentType. A component itself may also have sub-components.",
    interfaces=[di.objtypes.IDeviceHealthType],
)
class LADSComponentType(di.objtypes.ComponentType):
    assetId: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6149"])
    componentName: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6150"])
    components: LADSComponentsType | None
    deviceClass: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6151"])
    deviceHealth: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=lads;i=6480",
            browseName="ns=di;DeviceHealth",
            description="DeviceHealth indicates the health status of a device as defined by NAMUR Recommendation NE 107.",
            dataType=di.datatypes.DeviceHealthEnumeration,
            accessLevel=3,
        )
    )
    deviceHealthAlarms: ns0.objtypes.FolderType | None = o6.hasComponent(
        ns0.objtypes.FolderType(
            nodeId="ns=lads;i=5258", browseName="ns=di;DeviceHealthAlarms", description="DeviceHealthAlarms groups all instances of device health related alarms."
        )
    )
    deviceManual: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6152"])
    deviceRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6153"])
    hardwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6154"])
    hierarchicalLocation: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6080"])
    identification: machinery.objtypes.MachineryComponentIdentificationType = o6.hasAddIn(o6.ns["ns=lads;i=5095"])
    lifetimeCounters: machinery.objtypes.MachineryLifetimeCounterType | None = o6.hasAddIn(o6.ns["ns=lads;i=5094"])
    machineryBuildingBlocks: ns0.objtypes.FolderType | None = o6.organizes(o6.ns["ns=lads;i=5088"])
    maintenance: MaintenanceSetType | None
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=lads;i=6169"])
    manufacturerUri: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6170"])
    model: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6171"])
    operationCounters: machinery.objtypes.MachineryOperationCounterType | None = o6.hasAddIn(o6.ns["ns=lads;i=5097"])
    operationalLocation: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6074"])
    productCode: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6172"])
    productInstanceUri: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6173"])
    revisionCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6174"])
    serialNumber: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=lads;i=6175"])
    softwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6176"])


@o6.objecttype(
    nodeId="ns=lads;i=1025",
    browseName="ns=lads;LADSComponentsType",
    displayName="LADSComponentsType",
    description="The LADSComponentsType is a type used for structuring objects of type LADSComponentsType in an unordered list structure.",
)
class LADSComponentsType(machinery.objtypes.MachineComponentsType):
    langleComponentRangle: LADSComponentType | None = o6.hasComponent(
        LADSComponentType(
            nodeId="ns=lads;i=5065",
            browseName="ns=machinery;<Component>",
            description="<Components> is a placeholder for the Components.",
            displayName="<Components>",
            modellingRule="OptionalPlaceholder",
        )
    )
    nodeVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=lads;i=6085", browseName="NodeVersion", dataType=o6.String, value="NaN", accessLevel=3)
    )


o6.reference(LADSComponentsType, "i=41", "i=2133")


LADSComponentsType(
    nodeId="ns=lads;i=5111",
    browseName="ns=machinery;Components",
    description="Components is used for structuring objects of type LADSComponentsType in an unordered list structure.",
)


@o6.objecttype(nodeId="ns=lads;i=1021", browseName="ns=lads;ResultType", displayName="ResultType", description="The ResultType  provides the results of a specific program run.")
class ResultType(ns0.objtypes.BaseObjectType):
    applicationUri: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6281",
            browseName="ns=lads;ApplicationUri",
            description="ApplicationUri provides information about the remote client that initiated the program run generating the result. It must align with the ApplicationUri in the ApplicationDescription (refer to OPC 10000-4 section 7.1) of a Session (refer to OPC 10000-4 section 5.6.2). In instances where the program was initiated locally and cannot be attributed to an OPC UA Client, the ApplicationUri of the Server should be utilized.",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    description: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6396",
            browseName="ns=lads;Description",
            description="Description is the human-readable description of the specific program run that created this result and the result itself.",
            dataType=o6.LocalizedText,
            accessLevel=3,
        )
    )
    deviceProgramRunId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6495",
            browseName="ns=lads;DeviceProgramRunId",
            description="DeviceProgramRunId is the internal program identifier assigned by the Device to the program run generating this result. It is used to identify a Result object and is returned to the Client when the StartProgram Method is called.",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    estimatedRuntime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6504",
            browseName="ns=lads;EstimatedRuntime",
            description="EstimatedRuntime is the time that was estimated for the program execution. This information is retrieved from the ActiveProgramType.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
        )
    )
    fileSet: ResultFileSetType = o6.hasComponent(
        ResultFileSetType(
            nodeId="ns=lads;i=5081", browseName="ns=lads;FileSet", description="The ResultFileSetType is used for organising ResultFileType objects in an unordered list structure."
        )
    )
    programTemplate: ProgramTemplateType = o6.hasComponent(
        ProgramTemplateType(
            nodeId="ns=lads;i=5112",
            browseName="ns=lads;ProgramTemplate",
            description="ProgramTemplate is an immutable copy of the Program Template attributes with which the result was generated and is provided for documentation and traceability purposes. This copy will not change even if the original is changed.",
        )
    )
    properties: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6485",
            browseName="ns=lads;Properties",
            description="Properties is a list of key-value pairs with KeyValueType, provided when calling the StartProgram() Method, which can be utilized when performing the program run and provided in the ResultType object for documentation and traceability purposes.",
            dataType=lads_datypes.KeyValueType,
            valueRank=1,
            arrayDimensions=[1],
            accessLevel=3,
        )
    )
    samples: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6308",
            browseName="ns=lads;Samples",
            description="Samples is a list of sample-specific information with SampleInfoType provided when calling the StartProgram() Method, which can be utilized when performing the program run and provided in the ResultType object for documentation and traceability purposes.",
            dataType=lads_datypes.SampleInfoType,
            valueRank=1,
            arrayDimensions=[1],
            accessLevel=3,
        )
    )
    started: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6307", browseName="ns=lads;Started", description="Started is the timestamp of when the program was started.", dataType=o6.DateTime, accessLevel=3
        )
    )
    stopped: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6394", browseName="ns=lads;Stopped", description="Stopped is the timestamp of when the program was stopped.", dataType=o6.DateTime, accessLevel=3
        )
    )
    supervisoryJobId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6393",
            browseName="ns=lads;SupervisoryJobId",
            description="SupervisoryJobId is the identifier for the execution of a specific workflow consisting of one or multiple tasks. It is provided as an Argument of the StartProgram() Method which initiates the program run.",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    supervisoryTaskId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6487",
            browseName="ns=lads;SupervisoryTaskId",
            description="SupervisoryTaskId is the unique identifier of the specific Task in the supervisory system to which the result belongs. It is provided as an Argument of the StartProgram() Method which initiates the program run.",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    totalPauseTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6501",
            browseName="ns=lads;TotalPauseTime",
            description="TotalPauseTime is the time the program execution for the result was in a paused state. Paused states are the Held State and the Suspended State. This information is retrieved from the ActiveProgramType.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
        )
    )
    totalRuntime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6500",
            browseName="ns=lads;TotalRuntime",
            description="TotalRuntime is the total time of program execution including paused states. Paused states are the held State and the suspended State. This information is retrieved from the ActiveProgramType.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
        )
    )
    user: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6282",
            browseName="ns=lads;User",
            description="User provides information about the remote client user that initiated the program run generating the result. User must be a human-readable value, based on the UserIdentityToken (refer to OPC 10000-4 section 7.36). In instances where the program was initiated locally and cannot be attributed to an OPC UA Client, the local user of the Server should be utilized.",
            dataType=o6.String,
            accessLevel=3,
        )
    )
    variableSet: VariableSetType = o6.hasComponent(
        VariableSetType(
            nodeId="ns=lads;i=5067", browseName="ns=lads;VariableSet", description="The VariableSetType is used for storing additional sample data that was created during a run."
        )
    )


@o6.objecttype(
    nodeId="ns=lads;i=1020",
    browseName="ns=lads;ResultSetType",
    displayName="ResultSetType",
    description="The ResultSetType is used for organising ResultType objects in an unordered list structure.",
)
class ResultSetType(SetType):
    langleSetElementRangle: ResultType | None = o6.hasComponent(
        ResultType(
            nodeId="ns=lads;i=5062",
            browseName="ns=lads;<SetElement>",
            description="SetElement is the element of the set and is overridden with ResultSetType.",
            modellingRule="OptionalPlaceholder",
        )
    )
    nodeVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6104",
            browseName="NodeVersion",
            description="NodeVersion and the GeneralModelChangeEventType are mechanisms to notify clients that the content of the set has changed and shall be used as defined in OPC 10000-3.",
            dataType=o6.String,
            value="NaN",
            accessLevel=3,
        )
    )


o6.call(nodeId="ns=lads;i=7000", browseName="ns=lads;Reset")

ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6092",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=lads;i=7001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="MaintenanceTaskStopResult", dataType=o6.NodeId("ns=lads;i=3000"), valueRank=-1, description=o6.LocalizedText("Provide the result of the.Task execution.")
        ),
        ns0.datatypes.Argument(name="Comment", dataType=o6.LocalizedText, valueRank=-1, description=o6.LocalizedText("Additional comment.")),
    ],
)
o6.call(nodeId="ns=lads;i=7001", browseName="ns=lads;StopTask", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6092"]))

ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6132",
    browseName="InputArguments",
    modellingRule="Optional",
    parent="ns=lads;i=7002",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Value", dataType=o6.Double, valueRank=-1)],
    accessLevel=3,
)
o6.call(nodeId="ns=lads;i=7002", browseName="ns=lads;ResetTotalizer", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6132"]))
o6.reference(o6.ns["ns=lads;i=5059"], "i=35", o6.ns["ns=lads;i=7002"])


@o6.objecttype(
    nodeId="ns=lads;i=1014",
    browseName="ns=lads;AnalogControlFunctionWithTotalizerType",
    displayName="AnalogControlFunctionWithTotalizerType",
    description="The AnalogControlFunctionWithTotalizerType describes an analogue control (using analogue values) function with totalizer.  Typical usage examples include but are not limited to fluid controllers where the quantity of fluid needs to be accurately measured and totalled for metering purposes.",
)
class AnalogControlFunctionWithTotalizerType(AnalogControlFunctionType):
    operational: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=lads;i=5059"])
    resetTotalizer: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7002"])
    totalizedValue: ns0.vartypes.AnalogUnitRangeType = o6.hasComponent(o6.ns["ns=lads;i=6011"])


ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6127",
    browseName="InputArguments",
    description="the definition of the input argument of method 4:FunctionalUnitStatemachineType.4:Start",
    modellingRule="Mandatory",
    parent="ns=lads;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Properties",
            dataType=ns0.datatypes.KeyValuePair,
            valueRank=1,
            description=o6.LocalizedText("A set of Properties that parameterize the execution of the Functional Unit"),
        )
    ],
)
o6.call(nodeId="ns=lads;i=7004", browseName="ns=lads;Start", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6127"]))

ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6129",
    browseName="InputArguments",
    description="the definition of the input argument of method 4:FunctionStateMachineTypeType.4:Start",
    modellingRule="Mandatory",
    parent="ns=lads;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="TargetValue",
            dataType=ns0.datatypes.Number,
            valueRank=-1,
            description=o6.LocalizedText("(Optional) The value can use to set the target value parallel with the start method."),
        )
    ],
)
o6.call(nodeId="ns=lads;i=7009", browseName="ns=lads;StartWithTargetValue", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6129"]))

ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6098",
    browseName="InputArguments",
    description="the definition of the input argument of method 4:FunctionalUnitStateMachineType.4:StartProgram",
    modellingRule="Mandatory",
    parent="ns=lads;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[5],
    value=[
        ns0.datatypes.Argument(
            name="ProgramTemplateId",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText("The unique id of the program template used for the program-run. The template must be a member of the ProgramTemplateSet."),
        ),
        ns0.datatypes.Argument(
            name="Properties",
            dataType=o6.NodeId("ns=lads;i=3003"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("A Key/Value list for parameterization of the program-run."),
        ),
        ns0.datatypes.Argument(name="SupervisoryJobId", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The ID of the supervisory job.")),
        ns0.datatypes.Argument(name="SupervisoryTaskId", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The ID of the supervisory task.")),
        ns0.datatypes.Argument(
            name="Samples",
            dataType=o6.NodeId("ns=lads;i=3002"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("An array of the SampleInfoType that describes the samples processed in this program-run."),
        ),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6121",
    browseName="OutputArguments",
    description="the definition of the output arguments of method 4:FunctionalUnitStateMachineType.4:StartProgram",
    modellingRule="Mandatory",
    parent="ns=lads;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="DeviceProgramRunId", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("The device specific ID of the current program-run."))],
)
o6.call(nodeId="ns=lads;i=7010", browseName="ns=lads;StartProgram", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6098"]), outputArgs=o6.hasProperty(o6.ns["ns=lads;i=6121"]))

o6.call(nodeId="ns=lads;i=7011", browseName="ns=lads;Open")

o6.call(nodeId="ns=lads;i=7012", browseName="ns=lads;Close")

o6.call(nodeId="ns=lads;i=7013", browseName="ns=lads;Lock")

o6.call(nodeId="ns=lads;i=7014", browseName="ns=lads;Unlock")


@o6.objecttype(
    nodeId="ns=lads;i=1010",
    browseName="ns=lads;CoverStateMachineType",
    displayName="CoverStateMachineType",
    description="he CoverStateMachineType is used to control the lid, door, or cover of a laboratory device. One Device may have any arbitrary number of lids, doors, covers and their corresponding CoverFunction.",
)
class CoverStateMachineType(ns0.objtypes.FiniteStateMachineType):
    close: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7012"])
    closed: ns0.objtypes.StateType
    closedToError: ns0.objtypes.TransitionType
    closedToLocked: ns0.objtypes.TransitionType
    closedToLocking: ns0.objtypes.TransitionType
    closedToOpened: ns0.objtypes.TransitionType
    closedToOpening: ns0.objtypes.TransitionType
    closing: ns0.objtypes.StateType
    closingToClosed: ns0.objtypes.TransitionType
    error: ns0.objtypes.StateType
    errorToOpened: ns0.objtypes.TransitionType
    lock: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7013"])
    locked: ns0.objtypes.StateType
    lockedToClosed: ns0.objtypes.TransitionType
    lockedToError: ns0.objtypes.TransitionType
    lockedToUnlocking: ns0.objtypes.TransitionType
    locking: ns0.objtypes.StateType
    lockingToLocked: ns0.objtypes.TransitionType
    open: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7011"])
    opened: ns0.objtypes.StateType
    openedToClosed: ns0.objtypes.TransitionType
    openedToClosing: ns0.objtypes.TransitionType
    opening: ns0.objtypes.StateType
    openingToOpened: ns0.objtypes.TransitionType
    reset: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7000"])
    unlock: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7014"])
    unlocking: ns0.objtypes.StateType
    unlockingToClosed: ns0.objtypes.TransitionType


o6.call(nodeId="ns=lads;i=7021", browseName="ns=lads;GotoOperate")

ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6128",
    browseName="InputArguments",
    description="the definition of the input argument of method 4:AnalogControlFunctionWithIncreaseDecreaseRatesType.4:ModifyTargetValueByDelta",
    modellingRule="Mandatory",
    parent="ns=lads;i=7022",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Value",
            dataType=o6.Double,
            valueRank=-1,
            description=o6.LocalizedText(
                "Relative value by which the target value will be changed. The resulting value will typically be limited to the target-value's allowed range. Provided values can be positive or negative."
            ),
        )
    ],
)
o6.call(nodeId="ns=lads;i=7022", browseName="ns=lads;ModifyTargetValueBy", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6128"]))
o6.reference(o6.ns["ns=lads;i=5084"], "i=35", o6.ns["ns=lads;i=7022"])


@o6.objecttype(
    nodeId="ns=lads;i=1029",
    browseName="ns=lads;AnalogControlFunctionWithRelativeTargetValueType",
    displayName="AnalogControlFunctionWithRelativeTargetValueType",
    description="The AnalogControlFunctionWithRelativeTargetValueType supports applications where the target value is typically modified by relative increments or decrements. Examples of its usage include position controllers where the actuator needs to modify its position relative to the last defined position by a specific amount, or dispenser controllers that are responsible for aspirating or dispensing a certain volume of fluid.  The optional DecreaseRate and IncreaseRate variables can be utilized to customize the dynamics of the resulting action based on application-specific requirements. These variables allow for adapting to factors such as viscosity when aspirating or dispensing fluids.",
)
class AnalogControlFunctionWithRelativeTargetValueType(AnalogControlFunctionType):
    decreaseRate: ns0.vartypes.AnalogUnitRangeType | None = o6.hasComponent(o6.ns["ns=lads;i=6125"])
    increaseRate: ns0.vartypes.AnalogUnitRangeType | None = o6.hasComponent(o6.ns["ns=lads;i=6089"])
    modifyTargetValueBy: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7022"])
    operational: di.objtypes.FunctionalGroupType = o6.hasComponent(o6.ns["ns=lads;i=5084"])


o6.call(nodeId="ns=lads;i=7031", browseName="ns=lads;GotoShutdown")

o6.call(nodeId="ns=lads;i=7032", browseName="ns=lads;GotoSleep")


@o6.objecttype(
    nodeId="ns=lads;i=1039",
    browseName="ns=lads;LADSDeviceStateMachineType",
    displayName="LADSDeviceStateMachineType",
    description="The LADSDeviceStateMachineType state machine represents the Device’s operation mode. It is inspired by the AnalyserDeviceStateMachineType from the Analyzer Devices Specification.",
)
class LADSDeviceStateMachineType(ns0.objtypes.FiniteStateMachineType):
    gotoOperate: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7021"])
    gotoShutdown: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7031"])
    gotoSleep: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7032"])
    initialization: ns0.objtypes.InitialStateType
    initializationToOperate: ns0.objtypes.TransitionType
    operate: ns0.objtypes.StateType
    operateToShutdown: ns0.objtypes.TransitionType
    operateToSleep: ns0.objtypes.TransitionType
    shutdown: ns0.objtypes.StateType
    sleep: ns0.objtypes.StateType
    sleepToOperate: ns0.objtypes.TransitionType


ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6289",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=lads;i=7051",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TemplateId", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Unique identifier of the template to be downloaded."))],
)
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6290",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=lads;i=7051",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="AdditionalParameters",
            dataType=o6.NodeId("ns=lads;i=3003"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("Additional properties of the program template."),
        ),
        ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("Opaque program template data.")),
    ],
)
o6.call(nodeId="ns=lads;i=7051", browseName="ns=lads;Download", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6289"]), outputArgs=o6.hasProperty(o6.ns["ns=lads;i=6290"]))

ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6291",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=lads;i=7052",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="TemplateId", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Unique identifier of the template to be removed."))],
)
o6.call(nodeId="ns=lads;i=7052", browseName="ns=lads;Remove", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6291"]))

ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6032",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=lads;i=7053",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="TemplateId",
            dataType=o6.String,
            valueRank=-1,
            description=o6.LocalizedText(
                "The unique identifier of the template which might be generated by the device/functional-unit itself or might be provided as element of the opaque input data."
            ),
        )
    ],
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=lads;i=6292",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=lads;i=7053",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[2],
    value=[
        ns0.datatypes.Argument(
            name="AdditionalParameters",
            dataType=o6.NodeId("ns=lads;i=3003"),
            valueRank=1,
            arrayDimensions=[0],
            description=o6.LocalizedText("Additional properties of the program template."),
        ),
        ns0.datatypes.Argument(name="Data", dataType=o6.ByteString, valueRank=-1, description=o6.LocalizedText("Opaque program template data.")),
    ],
)
o6.call(nodeId="ns=lads;i=7053", browseName="ns=lads;Upload", inputArgs=o6.hasProperty(o6.ns["ns=lads;i=6292"]), outputArgs=o6.hasProperty(o6.ns["ns=lads;i=6032"]))


@o6.objecttype(
    nodeId="ns=lads;i=1006",
    browseName="ns=lads;ProgramManagerType",
    displayName="ProgramManagerType",
    description="The ProgramManager provides the functional unit's program manager.",
)
class ProgramManagerType(di.objtypes.TopologyElementType):
    activeProgram: ActiveProgramType = o6.hasComponent(
        ActiveProgramType(
            nodeId="ns=lads;i=5190",
            browseName="ns=lads;ActiveProgram",
            description="The ActiveProgram specifies the current state of operation of a FunctionalUnit. It provides context and information about the currently active program on the device. This allows users to follow the progress of a program run in a standardized fashion by organising steps into a flat, linear sequence.",
        )
    )
    download: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7051"])
    programTemplateSet: ProgramTemplateSetType
    remove: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7052"])
    resultSet: ResultSetType
    upload: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7053"])


@o6.objecttype(
    nodeId="ns=lads;i=1050",
    browseName="ns=lads;LADSOperationModeStateMachineType",
    displayName="LADSOperationModeStateMachineType",
    description="State machine representing the operation mode of a laboratory device. Optional methods allow for initiating changes of the operation mode from remote.",
)
class LADSOperationModeStateMachineType(machinery.objtypes.MachineryOperationModeStateMachineType):
    gotoMaintenance: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=lads;i=7055", browseName="ns=lads;GotoMaintenance"))
    gotoProcessing: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=lads;i=7020", browseName="ns=lads;GotoProcessing"))
    gotoSetup: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=lads;i=7056", browseName="ns=lads;GotoSetup"))


LADSOperationModeStateMachineType(
    nodeId="ns=lads;i=5090",
    browseName="ns=machinery;MachineryOperationMode",
    description="State machine representing the operation mode of a laboratory device. Optional methods allow for initiating changes of the operation mode from remote.",
)


@o6.objecttype(
    nodeId="ns=lads;i=1002",
    browseName="ns=lads;LADSDeviceType",
    displayName="LADSDeviceType",
    description="The LADSDeviceType provides a base class for laboratory- and analytical devices.",
)
class LADSDeviceType(di.objtypes.DeviceType):
    assetId: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=lads;i=6068"])
    componentName: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=lads;i=6069"])
    components: LADSComponentsType | None = o6.hasAddIn(o6.ns["ns=lads;i=5111"])
    deviceClass: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6083",
            browseName="ns=di;DeviceClass",
            description="DeviceClass indicates in which domain or for what purpose a certain item for which the Interface is applied is used. Examples are “ProgrammableController”, “RemoteIO”, and “TemperatureSensor”.",
            dataType=o6.String,
        )
    )
    deviceHealth: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=lads;i=6086",
            browseName="ns=di;DeviceHealth",
            description="DeviceHealth indicates the status as defined by NAMUR Recommendation NE107. Clients can read or monitor this Variable to determine the device condition.",
            dataType=di.datatypes.DeviceHealthEnumeration,
        )
    )
    deviceManual: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=lads;i=6051"])
    deviceRevision: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=lads;i=6062"])
    deviceState: LADSDeviceStateMachineType
    functionalUnitSet: FunctionalUnitSetType
    hardwareRevision: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=lads;i=6093"])
    hierarchicalLocation: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6029"])
    identification: machinery.objtypes.MachineIdentificationType = o6.hasAddIn(o6.ns["ns=lads;i=5096"])
    machineryBuildingBlocks: ns0.objtypes.FolderType | None
    machineryItemState: machinery.objtypes.MachineryItemState_StateMachineType | None = o6.hasAddIn(o6.ns["ns=lads;i=5089"])
    machineryOperationMode: LADSOperationModeStateMachineType | None = o6.hasAddIn(o6.ns["ns=lads;i=5090"])
    maintenance: MaintenanceSetType | None
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=lads;i=6009"])
    manufacturerUri: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6094"])
    model: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=lads;i=6010"])
    operationCounters: machinery.objtypes.MachineryOperationCounterType | None = o6.hasAddIn(o6.ns["ns=lads;i=5093"])
    operationalLocation: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6028"])
    productCode: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6095"])
    productInstanceUri: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=lads;i=6096"])
    revisionCounter: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=lads;i=6008"])
    serialNumber: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=lads;i=6064"])
    softwareRevision: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=lads;i=6063"])


@o6.objecttype(
    nodeId="ns=lads;i=1028",
    browseName="ns=lads;MaintenanceTaskType",
    displayName="MaintenanceTaskType",
    description="The MaintenanceTaskType shall be used to implement instances of maintenance tasks applicable at both the Device and Component levels. Maintenance tasks include activities such as periodic maintenance, cleaning, calibration, and validation.",
    interfaces=[amb.objtypes.IMaintenanceEventType],
)
class MaintenanceTaskType(di.objtypes.MaintenanceRequiredAlarmType):
    configurationChanged: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6097",
            browseName="ns=amb;ConfigurationChanged",
            description="The ConfigurationChanged provides information if the configuration of the asset is planned to be changed or has changed during the maintenance activity.",
            dataType=o6.Boolean,
            accessLevel=3,
        )
    )
    estimatedDowntime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6102",
            browseName="ns=amb;EstimatedDowntime",
            description="The EstimatedDowntime provides the estimated time the execution of the maintenance activity will take. In case of replanning, it is allowed to change the EstimatedDowntime. If during the execution of the maintenance activity the EstimatedDowntime can be adjusted (e.g., the asset needs to be repaired because an inspection found some issues) this should be done. Clients can access the history of Events to receive the information on the original estimates when the maintenance activity started.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
        )
    )
    lastExecutionDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6360",
            browseName="ns=lads;LastExecutionDate",
            description="LastExecutionDate is the date when the Task was last performed. Optional, as the Task may have never run before.",
            dataType=ns0.datatypes.UtcTime,
            accessLevel=3,
        )
    )
    lastOperatingCycles: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6088",
            browseName="ns=lads;LastOperatingCycles",
            description="LastOperatingCycles is the number of cycles during the operating time (as defined in Section 9.3 of EN 13306-2017) recorded at the time of the last execution of the Task.",
            dataType=o6.UInt32,
            accessLevel=3,
        )
    )
    lastOperatingTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6081",
            browseName="ns=lads;LastOperatingTime",
            description="LastOperatingTime is the total amount of operating time (as defined in Section 9.3 of EN 13306-2017) in milliseconds (ms) by the Device at the time of the last execution of the Task.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
        )
    )
    maintenanceMethod: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6106",
            browseName="ns=amb;MaintenanceMethod",
            description="The MaintenanceMethod provides information about the planned or used maintenance method. The content may change during the different MaintenanceStates. By accessing the history of Events a Client can distinguish between the planned and actual used maintenance method during the maintenance activity.",
            dataType=amb.datatypes.MaintenanceMethodEnum,
            accessLevel=3,
        )
    )
    maintenanceState: amb.objtypes.MaintenanceEventStateMachineType = o6.hasComponent(
        amb.objtypes.MaintenanceEventStateMachineType(
            nodeId="ns=lads;i=5066",
            browseName="ns=amb;MaintenanceState",
            description="The MaintenanceState state-machine provides information, whether a maintenance activity is planned, currently in execution, of has been executed.",
        )
    )
    maintenanceSupplier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6107",
            browseName="ns=amb;MaintenanceSupplier",
            description="The MaintenanceSupplier provides information on the supplier that is planned to execute, currently executing or has executed the maintenance activity. The content may change during the different MaintenanceStates. By accessing the history of Events a Client can distinguish between the planned and actual supplier that executed the maintenance activity. The value contains always a human-readable name of the supplier and optionally references a Node representing the supplier in the AddressSpace.",
            dataType=amb.datatypes.NameNodeIdDataType,
            accessLevel=3,
        )
    )
    nextOperatingCycles: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6091",
            browseName="ns=lads;NextOperatingCycles",
            description="NextOperatingCycles is the number of cycles during operating time (as defined in Section 9.3 of EN 13306-2017) to be completed before the next execution of the Task.",
            dataType=o6.UInt32,
            accessLevel=3,
        )
    )
    nextOperatingTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6087",
            browseName="ns=lads;NextOperatingTime",
            description="NextOperatingTime is the total amount of operating time (as defined in Section 9.3 of EN 13306-2017) in milliseconds (ms) by the Device before the next execution of the Task.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
        )
    )
    partsOfAssetReplaced: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6108",
            browseName="ns=amb;PartsOfAssetReplaced",
            description="The PartsOfAssetReplaced provides information on the parts of the assets that are planned to be replaced during the maintenance activity, currently in replacement or have been replaced, depending on the different MaintenanceStates. The content may change during the different MaintenanceStates. By accessing the history of Events a Client can distinguish between the planned and actual parts of the assets replaced during the maintenance activity. The value contains always an array of a human-readable name of the qualification of the parts of the asset to be replaced and optionally references a Node representing each part of the asset in the AddressSpace.",
            dataType=amb.datatypes.NameNodeIdDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
        )
    )
    partsOfAssetServiced: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6111",
            browseName="ns=amb;PartsOfAssetServiced",
            description="The PartsOfAssetServiced provides information on the parts of the assets that are planned to be serviced during the maintenance activity, currently serviced or have been serviced, depending on the different MaintenanceStates. The content may change during the different MaintenanceStates. By accessing the history of Events a Client can distinguish between the planned and actual parts of the assets serviced during the maintenance activity. The value contains always an array of a human-readable name of the qualification of the parts of the asset to be serviced and optionally references a Node representing the part of the asset in the AddressSpace.",
            dataType=amb.datatypes.NameNodeIdDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
        )
    )
    plannedDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6119",
            browseName="ns=amb;PlannedDate",
            description="The PlannedDate provides the date for which the maintenance activity has been scheduled.. In case of replanning, it is allowed to change the PlannedDate. However, it is not the intention that the PlannedDate is modified because the maintenance activity starts to get executed. If the PlannedDate depends for example on the operation hours of the asset, it might get adapted depending on the passed operation hours.",
            dataType=ns0.datatypes.UtcTime,
            accessLevel=3,
        )
    )
    qualificationOfPersonnel: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6120",
            browseName="ns=amb;QualificationOfPersonnel",
            description="The QualificationOfPersonnel provides information on the qualification of the personnel that is planned to execute, currently executing or has executed the maintenance activity. The content may change during the different MaintenanceStates. By accessing the history of Events a Client can distinguish between the planned and actual qualification of the personnel that executed the maintenance activity. The value contains always a human-readable name of the qualification of the personnel and optionally references a Node representing the qualification of the personnel in the AddressSpace.",
            dataType=amb.datatypes.NameNodeIdDataType,
            accessLevel=3,
        )
    )
    recurrencePeriod: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=lads;i=6362",
            browseName="ns=lads;RecurrencePeriod",
            description="RecurrencePeriod is the period of repetition of the Task, specified in milliseconds. Optional, as not all Tasks have a recurrence period.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
        )
    )
    resetTask: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=lads;i=7003", browseName="ns=lads;ResetTask"))
    startTask: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=lads;i=7061", browseName="ns=lads;StartTask"))
    stopTask: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7001"])


o6.call(nodeId="ns=lads;i=7069", browseName="ns=lads;Reset")

o6.call(nodeId="ns=lads;i=7070", browseName="ns=lads;ToComplete")

o6.call(nodeId="ns=lads;i=7072", browseName="ns=lads;Unhold")

o6.call(nodeId="ns=lads;i=7073", browseName="ns=lads;Suspend")

o6.call(nodeId="ns=lads;i=7074", browseName="ns=lads;Hold")

o6.call(nodeId="ns=lads;i=7075", browseName="ns=lads;Unsuspend")


@o6.objecttype(
    nodeId="ns=lads;i=1036",
    browseName="ns=lads;RunningStateMachineType",
    displayName="RunningStateMachineType",
    description="The RunningStateMachineType is a sub-state machine of the FunctionalStateMachine and includes detailed substates.",
)
class RunningStateMachineType(ns0.objtypes.FiniteStateMachineType):
    complete: ns0.objtypes.StateType
    completeToResetting: ns0.objtypes.TransitionType
    completing: ns0.objtypes.StateType
    completingToComplete: ns0.objtypes.TransitionType
    currentState: ns0.vartypes.FiniteStateVariableType = o6.hasComponent(
        ns0.vartypes.FiniteStateVariableType(nodeId="ns=lads;i=6146", browseName="CurrentState", dataType=o6.LocalizedText)
    )
    execute: ns0.objtypes.StateType
    executeToCompleting: ns0.objtypes.TransitionType
    executeToHolding: ns0.objtypes.TransitionType
    executeToSuspending: ns0.objtypes.TransitionType
    held: ns0.objtypes.StateType
    heldToUnholding: ns0.objtypes.TransitionType
    hold: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7074"])
    holding: ns0.objtypes.StateType
    holdingToHeld: ns0.objtypes.TransitionType
    idle: ns0.objtypes.StateType
    idleToStarting: ns0.objtypes.TransitionType
    reset: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7069"])
    resetting: ns0.objtypes.StateType
    resettingToIdle: ns0.objtypes.TransitionType
    starting: ns0.objtypes.StateType
    startingToExecute: ns0.objtypes.TransitionType
    startingToHolding: ns0.objtypes.TransitionType
    suspend: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7073"])
    suspended: ns0.objtypes.StateType
    suspendedToHolding: ns0.objtypes.TransitionType
    suspendedToUnsuspending: ns0.objtypes.TransitionType
    suspending: ns0.objtypes.StateType
    suspendingToHolding: ns0.objtypes.TransitionType
    suspendingToSuspended: ns0.objtypes.TransitionType
    toComplete: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7070"])
    unhold: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7072"])
    unholding: ns0.objtypes.StateType
    unholdingToExecute: ns0.objtypes.TransitionType
    unholdingToHolding: ns0.objtypes.TransitionType
    unsuspend: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7075"])
    unsuspending: ns0.objtypes.StateType
    unsuspendingToExecute: ns0.objtypes.TransitionType
    unsuspendingToHolding: ns0.objtypes.TransitionType


RunningStateMachineType(
    nodeId="ns=lads;i=5130",
    browseName="ns=lads;RunningStateMachine",
    description="The RunningStateMachineType is a sub-state machine of the FunctionalStateMachine and includes detailed substates.",
)


o6.call(nodeId="ns=lads;i=7078", browseName="ns=lads;Abort")

o6.call(nodeId="ns=lads;i=7079", browseName="ns=lads;Clear")

o6.call(nodeId="ns=lads;i=7112", browseName="ns=lads;Stop")


@o6.objecttype(nodeId="ns=lads;i=1038", browseName="ns=lads;FunctionalStateMachineType", displayName="FunctionalStateMachineType", isAbstract=True)
class FunctionalStateMachineType(ns0.objtypes.FiniteStateMachineType):
    abort: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7078"])
    aborted: ns0.objtypes.StateType
    abortedToClearing: ns0.objtypes.TransitionType
    aborting: ns0.objtypes.StateType
    abortingToAborted: ns0.objtypes.TransitionType
    availableStates: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=lads;i=6473",
            browseName="AvailableStates",
            description="Set of states supported by the implementation.",
            dataType=o6.NodeId,
            valueRank=1,
            arrayDimensions=[1],
        )
    )
    availableTransitions: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=lads;i=6472",
            browseName="AvailableTransitions",
            description="Set of transitions supported by the implementation.",
            dataType=o6.NodeId,
            valueRank=1,
            arrayDimensions=[1],
        )
    )
    clear: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7079"])
    clearing: ns0.objtypes.StateType
    clearingToStopped: ns0.objtypes.TransitionType
    currentState: ns0.vartypes.FiniteStateVariableType
    running: ns0.objtypes.StateType
    runningStateMachine: RunningStateMachineType | None = o6.hasComponent(o6.ns["ns=lads;i=5130"])
    runningToAborting: ns0.objtypes.TransitionType
    runningToStopping: ns0.objtypes.TransitionType
    stop: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7112"])
    stopped: ns0.objtypes.InitialStateType
    stoppedToRunning: ns0.objtypes.TransitionType
    stopping: ns0.objtypes.StateType
    stoppingToStopped: ns0.objtypes.TransitionType


@o6.objecttype(
    nodeId="ns=lads;i=1043",
    browseName="ns=lads;FunctionalUnitStateMachineType",
    displayName="FunctionalUnitStateMachineType",
    description="Represents the state of a FunctionalUnit in a LADS Device",
)
class FunctionalUnitStateMachineType(FunctionalStateMachineType):
    currentState: ns0.vartypes.FiniteStateVariableType
    start: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7004"])
    startProgram: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7010"])


@o6.objecttype(
    nodeId="ns=lads;i=1044",
    browseName="ns=lads;ControlFunctionStateMachineType",
    displayName="ControlFunctionStateMachineType",
    description="Represents the state of a Function in a LADS Device",
)
class ControlFunctionStateMachineType(FunctionalStateMachineType):
    start: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=lads;i=7035", browseName="ns=lads;Start"))
    startWithTargetValue: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=lads;i=7009"])


@o6.objecttype(
    nodeId="ns=lads;i=1003",
    browseName="ns=lads;FunctionalUnitType",
    displayName="FunctionalUnitType",
    description="The FunctionalUnitType represents a functional unit of a laboratory or analytical device.",
    interfaces=[di.objtypes.ITagNameplateType],
)
class FunctionalUnitType(di.objtypes.TopologyElementType):
    assetId: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6284"])
    componentName: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=lads;i=6285"])
    functionSet: FunctionSetType | None = o6.hasComponent(
        FunctionSetType(
            nodeId="ns=lads;i=5008", browseName="ns=lads;FunctionSet", description="The FunctionSetType is used for organising FunctionType objects in an unordered list structure."
        )
    )
    functionalUnitState: FunctionalUnitStateMachineType = o6.hasComponent(
        FunctionalUnitStateMachineType(
            nodeId="ns=lads;i=5005", browseName="ns=lads;FunctionalUnitState", description="FunctionalUnitState provides the state-machine of the FunctionalUnit."
        )
    )
    identification: di.objtypes.FunctionalGroupType | None = o6.hasComponent(o6.ns["ns=lads;i=5003"])
    lock: di.objtypes.LockingServicesType
    operational: di.objtypes.FunctionalGroupType | None
    programManager: ProgramManagerType | None
    supportedPropertiesSet: SupportedPropertiesSetType | None = o6.hasComponent(
        SupportedPropertiesSetType(
            nodeId="ns=lads;i=5116",
            browseName="ns=lads;SupportedPropertiesSet",
            description="SupportedPropertiesSet provides a set of properties which are supported as members of a properties list Argument for Method calls such as, FunctionalUnit.StartFunctions() or ActiveProgram.Start().",
        )
    )


@o6.objecttype(
    nodeId="ns=lads;i=1023",
    browseName="ns=lads;FunctionalUnitSetType",
    displayName="FunctionalUnitSetType",
    description="The FunctionalUnitSetType provides a set of a FunctionalUnit objects.",
)
class FunctionalUnitSetType(SetType):
    langleSetElementRangle: FunctionalUnitType | None = o6.hasComponent(
        FunctionalUnitType(
            nodeId="ns=lads;i=5016",
            browseName="ns=lads;<SetElement>",
            description="SetElement is the element of the set and is overridden with FunctionalUnitType.",
            modellingRule="OptionalPlaceholder",
        )
    )


del Any, TYPE_CHECKING, uuid, o6, amb, di, ia, machinery, ns0, lads_datypes
