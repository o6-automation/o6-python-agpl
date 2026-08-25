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

"""Generated OPC UA plastics_extrusion_die namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
import o6.ns.plastics_extrusion as plastics_extrusion
import o6.ns.plastics_rubber as plastics_rubber
from . import objtypes as plastics_extrusion_die_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_die;i=5002",
    browseName="ns=plastics_extrusion_die;MeltPressures",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_die;i=6002", browseName="NodeVersion", dataType=o6.String, value=""))],
)
o6.reference(plastics_extrusion_die_objtypes.Die_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_die;i=5002"])
o6.reference(o6.ns["ns=plastics_extrusion_die;i=5002"], "i=41", "i=2133")
plastics_rubber.objtypes.MeasuringDevicesType(
    nodeId="ns=plastics_extrusion_die;i=5003",
    browseName="ns=plastics_extrusion_die;DimensionAdjustment",
    modellingRule="Optional",
    references=[o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_die;i=6003", browseName="NodeVersion", dataType=o6.String, value=""))],
)
o6.reference(plastics_extrusion_die_objtypes.Die_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_die;i=5003"])
o6.reference(o6.ns["ns=plastics_extrusion_die;i=5003"], "i=41", "i=2133")
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_die;i=6007",
    browseName="ns=plastics_rubber;Interval",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_die;i=6008", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_die;i=6014", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashPlasticsRubberSlashExtrusion_v2SlashDieSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=plastics_extrusion_die;i=5005",
    browseName="ns=plastics_extrusion_die;http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/Die/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_die;i=6015", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_die;i=6016", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2022-05-01T00:00:00Z")
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_die;i=6017", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/PlasticsRubber/Extrusion_v2/Die/"
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_die;i=6018", browseName="NamespaceVersion", dataType=o6.String, value="2.00")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_die;i=6019",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_die;i=6020", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_die;i=6021", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_die;i=6009",
    browseName="ns=plastics_rubber;RemainingInterval",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_die;i=6010", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_die;i=6022", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
    value=0.0,
)
ns0.vartypes.AnalogItemType(
    nodeId="ns=plastics_extrusion_die;i=6011",
    browseName="ns=plastics_rubber;TotalOperation",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_die;i=6012", browseName="EURange", dataType=ns0.datatypes.Range)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_die;i=6023", browseName="EngineeringUnits", dataType=ns0.datatypes.EUInformation)),
    ],
    dataType=o6.Double,
)
plastics_rubber.objtypes.MaintenanceType(
    nodeId="ns=plastics_extrusion_die;i=5004",
    browseName="ns=plastics_extrusion;Maintenance",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_die;i=6004", browseName="ns=plastics_rubber;Status", dataType=plastics_rubber.datatypes.MaintenanceStatusEnumeration
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_die;i=6006", browseName="ns=plastics_rubber;AdditionalInformation", dataType=o6.String)),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_die;i=6007"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_die;i=6009"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_die;i=6011"]),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_die;i=7001", browseName="ns=plastics_rubber;Reset")),
    ],
)
plastics_rubber.objtypes.StartDeviceType(
    nodeId="ns=plastics_extrusion_die;i=5006",
    browseName="ns=plastics_extrusion;StartTempering",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_die;i=6005", browseName="ns=plastics_rubber;Status", dataType=plastics_rubber.datatypes.StartEnumeration)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=plastics_extrusion_die;i=6013", browseName="ns=plastics_rubber;StartBlockedByClient", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
            )
        ),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_die;i=7002", browseName="ns=plastics_rubber;StartRequest")),
        o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_die;i=7003", browseName="ns=plastics_rubber;StopRequest")),
    ],
)
plastics_extrusion.objtypes.ExtrusionTemperatureZonesType(
    nodeId="ns=plastics_extrusion_die;i=5001",
    browseName="ns=plastics_extrusion_die;TemperatureZones",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_die;i=6001", browseName="NodeVersion", dataType=o6.String, value="0")),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_die;i=5004"]),
        o6.hasComponent(o6.ns["ns=plastics_extrusion_die;i=5006"]),
    ],
)
o6.reference(plastics_extrusion_die_objtypes.Die_InterfaceType, ns0.reftypes.HasComponent, o6.ns["ns=plastics_extrusion_die;i=5001"])
o6.reference(o6.ns["ns=plastics_extrusion_die;i=5001"], "i=41", "i=2133")


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, plastics_extrusion, plastics_rubber, plastics_extrusion_die_objtypes
