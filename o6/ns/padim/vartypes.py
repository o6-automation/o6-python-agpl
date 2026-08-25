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

"""Generated OPC UA padim namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.irdi as irdi
import o6.ns.ns0 as ns0
from . import datatypes as padim_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.BaseDataVariableType(nodeId="ns=padim;i=1113", browseName="ns=padim;SimulationState", displayName="Simulation state", dataType=o6.Boolean, value=False, accessLevel=3)
o6.reference(o6.ns["ns=padim;i=1113"], "i=17597", "ns=irdi;s=0112/2///61987#ABN611#002")
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=padim;i=1115", browseName="ns=padim;ActualValue", displayName="Actual value", dataType=ns0.datatypes.Number, valueRank=-2, accessLevel=3
)
o6.reference(o6.ns["ns=padim;i=1115"], "i=17597", "ns=irdi;s=0112/2///61987#ABN644#001")
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=padim;i=1117", browseName="ns=padim;SimulationValue", displayName="Simulation value", dataType=ns0.datatypes.Number, valueRank=-2, accessLevel=3
)
o6.reference(o6.ns["ns=padim;i=1117"], "i=17597", "ns=irdi;s=0112/2///61987#ABN613#001")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1118", browseName="ns=padim;Damping", dataType=o6.Float, value=1.0, accessLevel=3)
o6.reference(o6.ns["ns=padim;i=1118"], "i=17597", "ns=irdi;s=0112/2///61987#ABH526#002")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1131", browseName="ns=padim;LowFlowCutOff", displayName="Low flow cut off", dataType=o6.Float, valueRank=-2, accessLevel=3)
o6.reference(o6.ns["ns=padim;i=1131"], "i=17597", "ns=irdi;s=0112/2///61987#ABJ724#003")
ns0.vartypes.PropertyType(nodeId="ns=padim;i=1140", browseName="ns=padim;PulseWidth", displayName="Pulse width", dataType=o6.Float, value=0.5, accessLevel=3)
o6.reference(o6.ns["ns=padim;i=1140"], "i=17597", "ns=irdi;s=0112/2///61987#ABA635#003")
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=padim;i=1144", browseName="ns=padim;ActualValue", displayName="Two-state actual value", dataType=o6.Boolean, valueRank=-2, value=False, accessLevel=3
)
o6.reference(o6.ns["ns=padim;i=1144"], "i=17597", "ns=irdi;s=0112/2///61987#ABN645#002")
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=padim;i=1145", browseName="ns=padim;SimulationValue", displayName="Two-state value of simulation", dataType=o6.Boolean, valueRank=-2, value=False, accessLevel=3
)
o6.reference(o6.ns["ns=padim;i=1145"], "i=17597", "ns=irdi;s=0112/2///61987#ABN632#002")
ns0.vartypes.BaseDataVariableType(nodeId="ns=padim;i=1147", browseName="ns=padim;SimulationState", displayName="Simulation state", dataType=o6.Boolean, value=False, accessLevel=3)
o6.reference(o6.ns["ns=padim;i=1147"], "i=17597", "ns=irdi;s=0112/2///61987#ABN611#002")


@o6.variabletype(
    nodeId="ns=padim;i=1141", browseName="ns=padim;TwoStateDiscreteSignalVariableType", displayName="Two-state I/O value", dataType=o6.Boolean, valueRank=o6.ValueRank.ANY
)
class TwoStateDiscreteSignalVariableType(ns0.vartypes.TwoStateDiscreteType):
    actualValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=padim;i=1144"])
    simulationState: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=padim;i=1147"])
    simulationValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=padim;i=1145"])


o6.reference(TwoStateDiscreteSignalVariableType, "i=17597", "ns=irdi;s=0112/2///61987#ABN635#002")


ns0.vartypes.BaseDataVariableType(nodeId="ns=padim;i=1148", browseName="ns=padim;ActualValue", displayName="Multistate actual value", dataType=o6.UInt32, value=0, accessLevel=3)
o6.reference(o6.ns["ns=padim;i=1148"], "i=17597", "ns=irdi;s=0112/2///61987#ABN646#002")
ns0.vartypes.BaseDataVariableType(
    nodeId="ns=padim;i=1149", browseName="ns=padim;SimulationValue", displayName="Multistate value of simulation", dataType=o6.UInt32, value=0, accessLevel=3
)
o6.reference(o6.ns["ns=padim;i=1149"], "i=17597", "ns=irdi;s=0112/2///61987#ABN637#002")
ns0.vartypes.BaseDataVariableType(nodeId="ns=padim;i=1151", browseName="ns=padim;SimulationState", displayName="Simulation state", dataType=o6.Boolean, value=False, accessLevel=3)
o6.reference(o6.ns["ns=padim;i=1151"], "i=17597", "ns=irdi;s=0112/2///61987#ABN611#002")


@o6.variabletype(nodeId="ns=padim;i=1142", browseName="ns=padim;MultiStateDiscreteSignalVariableType", displayName="Multistate I/O value", dataType=o6.UInt32)
class MultiStateDiscreteSignalVariableType(ns0.vartypes.MultiStateDictionaryEntryDiscreteBaseType):
    actualValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=padim;i=1148"])
    simulationState: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=padim;i=1151"])
    simulationValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=padim;i=1149"])


o6.reference(MultiStateDiscreteSignalVariableType, "i=17597", "ns=irdi;s=0112/2///61987#ABN636#002")


ns0.vartypes.BaseDataVariableType(nodeId="ns=padim;i=1152", browseName="ns=padim;ActualValue", displayName="Actual value", valueRank=-2, accessLevel=3)
o6.reference(o6.ns["ns=padim;i=1152"], "i=17597", "ns=irdi;s=0112/2///61987#ABN644#001")
ns0.vartypes.BaseDataVariableType(nodeId="ns=padim;i=1153", browseName="ns=padim;SimulationValue", displayName="Simulation value", valueRank=-2, accessLevel=3)
o6.reference(o6.ns["ns=padim;i=1153"], "i=17597", "ns=irdi;s=0112/2///61987#ABN613#001")
ns0.vartypes.BaseDataVariableType(nodeId="ns=padim;i=1155", browseName="ns=padim;SimulationState", displayName="Simulation state", dataType=o6.Boolean, value=False, accessLevel=3)
o6.reference(o6.ns["ns=padim;i=1155"], "i=17597", "ns=irdi;s=0112/2///61987#ABN611#002")


@o6.variabletype(nodeId="ns=padim;i=1143", browseName="ns=padim;DiscreteSignalVariableType", displayName="DiscreteSignalVariableType", valueRank=o6.ValueRank.ANY)
class DiscreteSignalVariableType(ns0.vartypes.DiscreteItemType):
    actualValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=padim;i=1152"])
    simulationState: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=padim;i=1155"])
    simulationValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=padim;i=1153"])


ns0.vartypes.PropertyType(nodeId="ns=padim;i=1206", browseName="EngineeringUnits", displayName="Unit", dataType=ns0.datatypes.EUInformation)
o6.reference(o6.ns["ns=padim;i=1206"], "i=17597", "ns=irdi;s=0112/2///61987#ABA968#004")


@o6.variabletype(nodeId="ns=padim;i=1111", browseName="ns=padim;AnalogSignalVariableType", displayName="Value", dataType=ns0.datatypes.Number, valueRank=o6.ValueRank.ANY)
class AnalogSignalVariableType(ns0.vartypes.AnalogUnitRangeType):
    actualValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=padim;i=1115"])
    damping: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1118"])
    engineeringUnits: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=padim;i=1206"])
    simulationState: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=padim;i=1113"])
    simulationValue: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=padim;i=1117"])


o6.reference(AnalogSignalVariableType, "i=17597", "ns=irdi;s=0112/2///61987#ABN634#001")


@o6.variabletype(nodeId="ns=padim;i=1120", browseName="ns=padim;TemperatureMeasurementVariableType", displayName="Temperature", dataType=o6.Float, valueRank=o6.ValueRank.ANY)
class TemperatureMeasurementVariableType(AnalogSignalVariableType):
    sensorClass: ns0.vartypes.MultiStateDictionaryEntryDiscreteType | None
    sensorConnection: ns0.vartypes.MultiStateDictionaryEntryDiscreteType | None
    sensorReference: ns0.vartypes.MultiStateDictionaryEntryDiscreteType | None
    sensorType: ns0.vartypes.MultiStateDictionaryEntryDiscreteType


o6.reference(TemperatureMeasurementVariableType, "i=17597", "ns=irdi;s=0112/2///61987#ABA927#005")


@o6.variabletype(nodeId="ns=padim;i=1121", browseName="ns=padim;PressureMeasurementVariableType", displayName="Pressure", dataType=o6.Float, valueRank=o6.ValueRank.ANY)
class PressureMeasurementVariableType(AnalogSignalVariableType):
    pass


o6.reference(PressureMeasurementVariableType, "i=17597", "ns=irdi;s=0112/2///61987#ABN616#001")


@o6.variabletype(
    nodeId="ns=padim;i=1122", browseName="ns=padim;FlowMeasurementVariableType", displayName="FlowMeasurementVariableType", dataType=o6.Float, valueRank=o6.ValueRank.ANY
)
class FlowMeasurementVariableType(AnalogSignalVariableType):
    flowDirection: ns0.vartypes.MultiStateDictionaryEntryDiscreteType | None
    lowFlowCutOff: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=padim;i=1131"])


@o6.variabletype(nodeId="ns=padim;i=1123", browseName="ns=padim;LevelMeasurementVariableType", displayName="Level", dataType=o6.Float, valueRank=o6.ValueRank.ANY)
class LevelMeasurementVariableType(AnalogSignalVariableType):
    pass


o6.reference(LevelMeasurementVariableType, "i=17597", "ns=irdi;s=0112/2///61987#ABH329#002")


@o6.variabletype(nodeId="ns=padim;i=1124", browseName="ns=padim;ActualDensityVariableType", displayName="Density", dataType=o6.Float, valueRank=o6.ValueRank.ANY)
class ActualDensityVariableType(AnalogSignalVariableType):
    pass


o6.reference(ActualDensityVariableType, "i=17597", "ns=irdi;s=0112/2///61987#ABA946#004")


@o6.variabletype(nodeId="ns=padim;i=1125", browseName="ns=padim;ControlVariableType", displayName="Readback", dataType=o6.Float, valueRank=o6.ValueRank.ANY)
class ControlVariableType(AnalogSignalVariableType):
    actuatorType: ns0.vartypes.MultiStateDictionaryEntryDiscreteType
    operatingDirection: ns0.vartypes.MultiStateDictionaryEntryDiscreteType
    setpoint: ns0.vartypes.BaseAnalogType


o6.reference(ControlVariableType, "i=17597", "ns=irdi;s=0112/2///61987#ABP588#001")


@o6.variabletype(
    nodeId="ns=padim;i=1126", browseName="ns=padim;TotalizerVariableType", displayName="TotalizerVariableType", dataType=ns0.datatypes.Number, valueRank=o6.ValueRank.ANY
)
class TotalizerVariableType(AnalogSignalVariableType):
    pulseValue: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=padim;i=1139", browseName="ns=padim;PulseValue", displayName="Pulse value", dataType=ns0.datatypes.Number, accessLevel=3)
    )
    pulseWidth: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=padim;i=1140"])


@o6.variabletype(
    nodeId="ns=padim;i=1127",
    browseName="ns=padim;AnalyticalMeasurementVariableType",
    displayName="AnalyticalMeasurementVariableType",
    dataType=o6.Float,
    valueRank=o6.ValueRank.ANY,
)
class AnalyticalMeasurementVariableType(AnalogSignalVariableType):
    pass


@o6.variabletype(nodeId="ns=padim;i=1133", browseName="ns=padim;MassFlowRateVariableType", displayName="Mass flow rate", dataType=o6.Float, valueRank=o6.ValueRank.ANY)
class MassFlowRateVariableType(FlowMeasurementVariableType):
    pass


o6.reference(MassFlowRateVariableType, "i=17597", "ns=irdi;s=0112/2///61987#ABB290#005")


@o6.variabletype(nodeId="ns=padim;i=1134", browseName="ns=padim;ActualVolumeFlowRateVariableType", displayName="Volume flow rate", dataType=o6.Float, valueRank=o6.ValueRank.ANY)
class ActualVolumeFlowRateVariableType(FlowMeasurementVariableType):
    pass


o6.reference(ActualVolumeFlowRateVariableType, "i=17597", "ns=irdi;s=0112/2///61987#ABB291#005")


@o6.variabletype(
    nodeId="ns=padim;i=1135", browseName="ns=padim;NormalizedVolumeFlowRateVariableType", displayName="Norm. volume flow", dataType=o6.Float, valueRank=o6.ValueRank.ANY
)
class NormalizedVolumeFlowRateVariableType(FlowMeasurementVariableType):
    pass


o6.reference(NormalizedVolumeFlowRateVariableType, "i=17597", "ns=irdi;s=0112/2///61987#ABB292#005")


@o6.variabletype(
    nodeId="ns=padim;i=1215", browseName="ns=padim;TwoStateDiscreteControlVariableType", displayName="Two-state control value", dataType=o6.Boolean, valueRank=o6.ValueRank.ANY
)
class TwoStateDiscreteControlVariableType(TwoStateDiscreteSignalVariableType):
    faultState: ns0.vartypes.TwoStateDiscreteType | None
    operatingDirection: ns0.vartypes.MultiStateDictionaryEntryDiscreteType
    setpoint: ns0.vartypes.TwoStateDiscreteType


o6.reference(TwoStateDiscreteControlVariableType, "i=17597", "ns=irdi;s=0112/2///61987#ABP541#002")


@o6.variabletype(nodeId="ns=padim;i=1219", browseName="ns=padim;MultiStateDiscreteControlVariableType", displayName="Discrete multi-state control value", dataType=o6.UInt32)
class MultiStateDiscreteControlVariableType(MultiStateDiscreteSignalVariableType):
    faultState: ns0.vartypes.MultiStateDictionaryEntryDiscreteType | None
    operatingDirection: ns0.vartypes.MultiStateDictionaryEntryDiscreteType | None
    setpoint: ns0.vartypes.MultiStateDictionaryEntryDiscreteType


o6.reference(MultiStateDiscreteControlVariableType, "i=17597", "ns=irdi;s=0112/2///61987#ABP644#002")


ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1562",
    browseName="ns=padim;PatMatrixDescription",
    displayName="Matrix of components/measurands",
    dataType=padim_datypes.ChemicalSubstanceDataType,
    valueRank=1,
    arrayDimensions=[1],
    accessLevel=3,
)
o6.reference(o6.ns["ns=padim;i=1562"], "i=17597", "ns=irdi;s=0112/2///61987#ABP495#001")
ns0.vartypes.PropertyType(
    nodeId="ns=padim;i=1563",
    browseName="ns=padim;PatMeasurandDescription",
    displayName="Chemical component/measurand",
    dataType=padim_datypes.ChemicalSubstanceDataType,
    accessLevel=3,
)
o6.reference(o6.ns["ns=padim;i=1563"], "i=17597", "ns=irdi;s=0112/2///61987#ABP496#001")


@o6.variabletype(nodeId="ns=padim;i=1274", browseName="ns=padim;PatMeasurementVariableType", displayName="PatMeasurementVariableType", dataType=o6.Float)
class PatMeasurementVariableType(AnalyticalMeasurementVariableType):
    patMatrixDescription: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1562"])
    patMeasurandDescription: ns0.vartypes.PropertyType | None = o6.hasProperty(o6.ns["ns=padim;i=1563"])


o6.reference(PatMeasurementVariableType, "i=17597", "ns=irdi;s=<DictionaryEntryName>")


del Any, TYPE_CHECKING, uuid, o6, di, irdi, ns0, padim_datypes
