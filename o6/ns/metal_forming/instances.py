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

"""Generated OPC UA metal_forming namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.irdi_v1_00 as irdi_v1_00
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machine_tool as machine_tool
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.machinery_processvalues as machinery_processvalues
import o6.ns.ns0 as ns0
import o6.ns.padim as padim
from . import datatypes as metal_forming_datypes
from . import vartypes as metal_forming_vartypes
from . import objtypes as metal_forming_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=metal_forming;i=5001", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=metal_forming;i=5002", browseName="Default XML")
o6.hasEncoding(metal_forming_datypes.CyclicProcessValueDataType, o6.ns["ns=metal_forming;i=5002"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=metal_forming;i=5006", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=metal_forming;i=5017", browseName="Default XML")
o6.hasEncoding(metal_forming_datypes.CyclicPartInformationDataType, o6.ns["ns=metal_forming;i=5017"])
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashMetalFormingSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=metal_forming;i=5011",
    browseName="ns=metal_forming;http://opcfoundation.org/UA/MetalForming/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6001", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6002", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2024-02-01T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6003", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/MetalForming/")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6004", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=metal_forming;i=6005",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=metal_forming;i=6006", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6007", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=metal_forming;i=6009",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6010", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6011", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6012", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=metal_forming;i=6012"], "i=17597", "ns=irdi_v1_00;s=0112/2///61987#ABB271#007")
metal_forming_objtypes.CyclicProcessValueType(
    nodeId="ns=metal_forming;i=5012",
    browseName="ns=metal_forming;Retract",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=metal_forming;i=6012"]),
        o6.hasComponent(
            metal_forming_vartypes.CyclicProcessValueVariableType(
                nodeId="ns=metal_forming;i=6008",
                browseName="ns=metal_forming;CyclicProcessValue",
                dataType=metal_forming_datypes.CyclicProcessValueDataType,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6009"]),
    ],
)
o6.reference(metal_forming_objtypes.FormingPositionsType, ns0.reftypes.HasComponent, o6.ns["ns=metal_forming;i=5012"])
ns0.vartypes.FiniteStateVariableType(
    nodeId="ns=metal_forming;i=6014",
    browseName="CurrentState",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6015", browseName="Id", dataType=o6.NodeId))],
    dataType=o6.LocalizedText,
)
machinery.objtypes.MachineryItemState_StateMachineType(
    nodeId="ns=metal_forming;i=5007", browseName="ns=metal_forming;MachineryItemState", modellingRule="Mandatory", references=[o6.hasComponent(o6.ns["ns=metal_forming;i=6014"])]
)
o6.reference(metal_forming_objtypes.ProcessWorkingUnitType, ns0.reftypes.HasComponent, o6.ns["ns=metal_forming;i=5007"])
ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6019", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=metal_forming;i=6019"], "i=17597", "ns=irdi_v1_00;s=0112/2///61987#ABB271#007")
ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6025", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=metal_forming;i=6025"], "i=17597", "ns=irdi_v1_00;s=0112/2///61987#ABB271#007")
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=metal_forming;i=6027",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6028", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6029", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6030", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=metal_forming;i=6030"], "i=17597", "ns=irdi_v1_00;s=0112/2///61987#ABB271#007")
metal_forming_objtypes.CyclicProcessValueType(
    nodeId="ns=metal_forming;i=5013",
    browseName="ns=metal_forming;Start",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=metal_forming;i=6030"]),
        o6.hasComponent(
            metal_forming_vartypes.CyclicProcessValueVariableType(
                nodeId="ns=metal_forming;i=6013",
                browseName="ns=metal_forming;CyclicProcessValue",
                dataType=metal_forming_datypes.CyclicProcessValueDataType,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6027"]),
    ],
)
o6.reference(metal_forming_objtypes.FormingPositionsType, ns0.reftypes.HasComponent, o6.ns["ns=metal_forming;i=5013"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=metal_forming;i=6032",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6033", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6034", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6035", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=metal_forming;i=6035"], "i=17597", "ns=irdi_v1_00;s=0112/2///61987#ABB271#007")
metal_forming_objtypes.CyclicProcessValueType(
    nodeId="ns=metal_forming;i=5014",
    browseName="ns=metal_forming;TDC",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=metal_forming;i=6035"]),
        o6.hasComponent(
            metal_forming_vartypes.CyclicProcessValueVariableType(
                nodeId="ns=metal_forming;i=6031",
                browseName="ns=metal_forming;CyclicProcessValue",
                dataType=metal_forming_datypes.CyclicProcessValueDataType,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6032"]),
    ],
)
o6.reference(metal_forming_objtypes.FormingPositionsType, ns0.reftypes.HasComponent, o6.ns["ns=metal_forming;i=5014"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=metal_forming;i=6037",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6038", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6039", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6040", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=metal_forming;i=6040"], "i=17597", "ns=irdi_v1_00;s=0112/2///61987#ABB271#007")
metal_forming_objtypes.CyclicProcessValueType(
    nodeId="ns=metal_forming;i=5015",
    browseName="ns=metal_forming;Touch",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=metal_forming;i=6040"]),
        o6.hasComponent(
            metal_forming_vartypes.CyclicProcessValueVariableType(
                nodeId="ns=metal_forming;i=6036",
                browseName="ns=metal_forming;CyclicProcessValue",
                dataType=metal_forming_datypes.CyclicProcessValueDataType,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6037"]),
    ],
)
o6.reference(metal_forming_objtypes.FormingPositionsType, ns0.reftypes.HasComponent, o6.ns["ns=metal_forming;i=5015"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=metal_forming;i=6042",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6043", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6044", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6045", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=metal_forming;i=6045"], "i=17597", "ns=irdi_v1_00;s=0112/2///61987#ABB271#007")
metal_forming_objtypes.CyclicProcessValueType(
    nodeId="ns=metal_forming;i=5016",
    browseName="ns=metal_forming;BDC",
    modellingRule="Optional",
    references=[
        o6.hasProperty(o6.ns["ns=metal_forming;i=6045"]),
        o6.hasComponent(
            metal_forming_vartypes.CyclicProcessValueVariableType(
                nodeId="ns=metal_forming;i=6041",
                browseName="ns=metal_forming;CyclicProcessValue",
                dataType=metal_forming_datypes.CyclicProcessValueDataType,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6042"]),
    ],
)
o6.reference(metal_forming_objtypes.FormingPositionsType, ns0.reftypes.HasComponent, o6.ns["ns=metal_forming;i=5016"])
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=metal_forming;i=6048",
    browseName="ns=metal_forming;Position",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6049", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6050", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=metal_forming;i=6051",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6052", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6053", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6054", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=metal_forming;i=6054"], "i=17597", "ns=irdi_v1_00;s=0112/2///61987#ABB271#007")
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=metal_forming;i=5019",
    browseName="ns=metal_forming;CurrentProcessValue",
    modellingRule="Mandatory",
    references=[o6.hasProperty(o6.ns["ns=metal_forming;i=6054"]), o6.hasComponent(o6.ns["ns=metal_forming;i=6051"])],
)
o6.reference(metal_forming_objtypes.CyclicEventType, ns0.reftypes.HasComponent, o6.ns["ns=metal_forming;i=5019"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=metal_forming;i=6057",
    browseName="ns=machinery_processvalues;HighHighLimit",
    description="Defines the absolute high high limit",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6058", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=metal_forming;i=6059",
    browseName="ns=machinery_processvalues;HighLimit",
    description="Defines the absolute high limit",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6060", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=metal_forming;i=6061",
    browseName="ns=machinery_processvalues;LowLimit",
    description="Defines the absolute low limit",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6062", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=metal_forming;i=6063",
    browseName="ns=machinery_processvalues;LowLowLimit",
    description="Defines the absolute low low limit",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6064", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=metal_forming;i=6065",
    browseName="ns=machinery_processvalues;PercentageValue",
    description="Provides the process value in percentage.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=metal_forming;i=6066",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6067", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=100.0))
        ),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.vartypes.ProcessValueVariableType(
    nodeId="ns=metal_forming;i=6016",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6017", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6018", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6057"]),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6059"]),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6061"]),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6063"]),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6065"]),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.vartypes.ProcessValueSetpointVariableType(
    nodeId="ns=metal_forming;i=6068",
    browseName="ns=machinery_processvalues;ProcessValueSetpoint",
    description="The desired value, may or may not be controlled by the server.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6069", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6070", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.objtypes.ProcessValueType(
    nodeId="ns=metal_forming;i=5009",
    browseName="ns=metal_forming;<ProcessValue>",
    modellingRule="OptionalPlaceholder",
    references=[o6.hasProperty(o6.ns["ns=metal_forming;i=6019"]), o6.hasComponent(o6.ns["ns=metal_forming;i=6016"]), o6.hasComponent(o6.ns["ns=metal_forming;i=6068"])],
)
o6.reference(metal_forming_objtypes.ProcessWorkingUnitType, ns0.reftypes.HasComponent, o6.ns["ns=metal_forming;i=5009"])
ns0.vartypes.AnalogUnitType(
    nodeId="ns=metal_forming;i=6071",
    browseName="ns=machinery_processvalues;HighHighLimit",
    description="Defines the absolute high high limit",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6072", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=metal_forming;i=6073",
    browseName="ns=machinery_processvalues;HighLimit",
    description="Defines the absolute high limit",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6074", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=metal_forming;i=6075",
    browseName="ns=machinery_processvalues;LowLimit",
    description="Defines the absolute low limit",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6076", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitType(
    nodeId="ns=metal_forming;i=6077",
    browseName="ns=machinery_processvalues;LowLowLimit",
    description="Defines the absolute low low limit",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6078", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation))],
    dataType=ns0.datatypes.Number,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.AnalogUnitRangeType(
    nodeId="ns=metal_forming;i=6079",
    browseName="ns=machinery_processvalues;PercentageValue",
    description="Provides the process value in percentage.",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=metal_forming;i=6080",
                browseName="EngineeringUnits",
                dataType=ns0.datatypes.EUInformation,
                value=ns0.datatypes.EUInformation(
                    namespaceUri="http://www.opcfoundation.org/UA/units/un/cefact", unitId=20529, displayName=o6.LocalizedText("%"), description=o6.LocalizedText("percent")
                ),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6081", browseName="EURange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=100.0))
        ),
    ],
    dataType=o6.Double,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.vartypes.ProcessValueVariableType(
    nodeId="ns=metal_forming;i=6022",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6023", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6024", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6071"]),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6073"]),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6075"]),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6077"]),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6079"]),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
machinery_processvalues.vartypes.ProcessValueSetpointVariableType(
    nodeId="ns=metal_forming;i=6082",
    browseName="ns=machinery_processvalues;ProcessValueSetpoint",
    description="The desired value, may or may not be controlled by the server.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6083", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6084", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
metal_forming_objtypes.CyclicProcessValueType(
    nodeId="ns=metal_forming;i=5010",
    browseName="ns=metal_forming;<CyclicProcessValue>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(o6.ns["ns=metal_forming;i=6025"]),
        o6.hasComponent(
            metal_forming_vartypes.CyclicProcessValueVariableType(
                nodeId="ns=metal_forming;i=6021",
                browseName="ns=metal_forming;CyclicProcessValue",
                dataType=metal_forming_datypes.CyclicProcessValueDataType,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6022"]),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6082"]),
    ],
)
o6.reference(metal_forming_objtypes.ProcessWorkingUnitType, ns0.reftypes.HasComponent, o6.ns["ns=metal_forming;i=5010"])
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=metal_forming;i=6026",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6087", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6088", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6090", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=metal_forming;i=6090"], "i=17597", "ns=irdi_v1_00;s=0112/2///61987#ABB271#007")
metal_forming_objtypes.CyclicProcessValueType(
    nodeId="ns=metal_forming;i=5021",
    browseName="ns=metal_forming;BDC",
    references=[
        o6.hasProperty(o6.ns["ns=metal_forming;i=6090"]),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6026"]),
        o6.hasComponent(
            metal_forming_vartypes.CyclicProcessValueVariableType(
                nodeId="ns=metal_forming;i=6089",
                browseName="ns=metal_forming;CyclicProcessValue",
                dataType=metal_forming_datypes.CyclicProcessValueDataType,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=metal_forming;i=6091",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6092", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6093", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6095", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=metal_forming;i=6095"], "i=17597", "ns=irdi_v1_00;s=0112/2///61987#ABB271#007")
metal_forming_objtypes.CyclicProcessValueType(
    nodeId="ns=metal_forming;i=5022",
    browseName="ns=metal_forming;Retract",
    references=[
        o6.hasProperty(o6.ns["ns=metal_forming;i=6095"]),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6091"]),
        o6.hasComponent(
            metal_forming_vartypes.CyclicProcessValueVariableType(
                nodeId="ns=metal_forming;i=6094",
                browseName="ns=metal_forming;CyclicProcessValue",
                dataType=metal_forming_datypes.CyclicProcessValueDataType,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=metal_forming;i=6096",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6097", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6098", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6100", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=metal_forming;i=6100"], "i=17597", "ns=irdi_v1_00;s=0112/2///61987#ABB271#007")
metal_forming_objtypes.CyclicProcessValueType(
    nodeId="ns=metal_forming;i=5023",
    browseName="ns=metal_forming;Start",
    references=[
        o6.hasProperty(o6.ns["ns=metal_forming;i=6100"]),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6096"]),
        o6.hasComponent(
            metal_forming_vartypes.CyclicProcessValueVariableType(
                nodeId="ns=metal_forming;i=6099",
                browseName="ns=metal_forming;CyclicProcessValue",
                dataType=metal_forming_datypes.CyclicProcessValueDataType,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=metal_forming;i=6101",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6102", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6103", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6105", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=metal_forming;i=6105"], "i=17597", "ns=irdi_v1_00;s=0112/2///61987#ABB271#007")
metal_forming_objtypes.CyclicProcessValueType(
    nodeId="ns=metal_forming;i=5024",
    browseName="ns=metal_forming;TDC",
    references=[
        o6.hasProperty(o6.ns["ns=metal_forming;i=6105"]),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6101"]),
        o6.hasComponent(
            metal_forming_vartypes.CyclicProcessValueVariableType(
                nodeId="ns=metal_forming;i=6104",
                browseName="ns=metal_forming;CyclicProcessValue",
                dataType=metal_forming_datypes.CyclicProcessValueDataType,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
padim.vartypes.AnalogSignalVariableType(
    nodeId="ns=metal_forming;i=6106",
    browseName="ns=padim;AnalogSignal",
    description="The process value.",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6107", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6108", browseName="EURange", dataType=ns0.datatypes.Range)),
    ],
    dataType=ns0.datatypes.Number,
    valueRank=-2,
    accessLevel=3,
    userAccessLevel=1,
)
ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6110", browseName="ns=padim;SignalTag", displayName="Tag", dataType=o6.String, accessLevel=3, userAccessLevel=1)
o6.reference(o6.ns["ns=metal_forming;i=6110"], "i=17597", "ns=irdi_v1_00;s=0112/2///61987#ABB271#007")
metal_forming_objtypes.CyclicProcessValueType(
    nodeId="ns=metal_forming;i=5025",
    browseName="ns=metal_forming;Touch",
    references=[
        o6.hasProperty(o6.ns["ns=metal_forming;i=6110"]),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6106"]),
        o6.hasComponent(
            metal_forming_vartypes.CyclicProcessValueVariableType(
                nodeId="ns=metal_forming;i=6109",
                browseName="ns=metal_forming;CyclicProcessValue",
                dataType=metal_forming_datypes.CyclicProcessValueDataType,
                accessLevel=3,
                userAccessLevel=1,
            )
        ),
    ],
)
metal_forming_objtypes.FormingPositionsType(
    nodeId="ns=metal_forming;i=5008",
    browseName="ns=metal_forming;FormingPositions",
    modellingRule="Mandatory",
    references=[
        o6.hasComponent(o6.ns["ns=metal_forming;i=5021"]),
        o6.hasComponent(o6.ns["ns=metal_forming;i=5022"]),
        o6.hasComponent(o6.ns["ns=metal_forming;i=5023"]),
        o6.hasComponent(o6.ns["ns=metal_forming;i=5024"]),
        o6.hasComponent(o6.ns["ns=metal_forming;i=5025"]),
    ],
)
o6.reference(metal_forming_objtypes.FormingProcessWorkingUnitType, ns0.reftypes.HasComponent, o6.ns["ns=metal_forming;i=5008"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=metal_forming;i=5004",
    browseName="ns=machine_tool;Location",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6046", browseName="ns=metal_forming;Orientation", dataType=o6.String, accessLevel=3, userAccessLevel=1)
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6047", browseName="ns=metal_forming;Stage", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6111", browseName="ns=machine_tool;Name", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6112", browseName="ns=machine_tool;PlaceNumber", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)),
        o6.hasComponent(o6.ns["ns=metal_forming;i=6048"]),
    ],
)
o6.reference(metal_forming_objtypes.FormingToolType, ns0.reftypes.HasComponent, o6.ns["ns=metal_forming;i=5004"])
ns0.objtypes.BaseObjectType(
    nodeId="ns=metal_forming;i=5020",
    browseName="ns=machine_tool;Location",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6113", browseName="ns=machine_tool;Name", dataType=o6.String, accessLevel=3, userAccessLevel=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6114", browseName="ns=machine_tool;PlaceNumber", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)),
    ],
)
metal_forming_objtypes.FormingToolType(
    nodeId="ns=metal_forming;i=5005",
    browseName="ns=metal_forming;<FormingTool>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6085", browseName="ns=machine_tool;Identifier", dataType=o6.String, value="")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=metal_forming;i=6086", browseName="ns=machine_tool;Name", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=metal_forming;i=5020"]),
    ],
)
o6.reference(metal_forming_objtypes.FormingMultiToolType, ns0.reftypes.HasComponent, o6.ns["ns=metal_forming;i=5005"])


del (
    Any,
    TYPE_CHECKING,
    uuid,
    o6,
    di,
    ia,
    irdi_v1_00,
    isa95_jobcontrol_v2,
    machine_tool,
    machinery,
    machinery_jobs,
    machinery_processvalues,
    ns0,
    padim,
    metal_forming_datypes,
    metal_forming_vartypes,
    metal_forming_objtypes,
)
