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

"""Generated OPC UA weihenstephan namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
import o6.ns.pack_ml as pack_ml
from . import datatypes as weihenstephan_datypes
from . import vartypes as weihenstephan_vartypes
from . import objtypes as weihenstephan_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

httpColonSlashSlashOpcfoundationDotOrgSlashUASlashWeihenstephanSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=weihenstephan;i=5000",
    browseName="ns=weihenstephan;http://opcfoundation.org/UA/Weihenstephan/",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=weihenstephan;i=6000", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=weihenstephan;i=6001", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2021-07-12T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=weihenstephan;i=6002", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Weihenstephan/")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=weihenstephan;i=6003", browseName="NamespaceVersion", dataType=o6.String, value="1.00.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=weihenstephan;i=6004",
                browseName="StaticNodeIdTypes",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[1],
                value=[ns0.datatypes.IdType.NUMERIC],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=weihenstephan;i=6005",
                browseName="StaticNumericNodeIdRange",
                dataType=ns0.datatypes.NumericRange,
                valueRank=1,
                arrayDimensions=[1],
                value=["1:2147483647"],
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=weihenstephan;i=6006", browseName="StaticStringNodeIdPattern", dataType=o6.String, value="")),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
machinery.objtypes.MachineIdentificationType(
    nodeId="ns=weihenstephan;i=5001",
    browseName="ns=di;Identification",
    modellingRule="Mandatory",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=weihenstephan;i=6012", browseName="ns=di;SerialNumber", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=weihenstephan;i=6013", browseName="ns=di;ProductInstanceUri", dataType=o6.String)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=weihenstephan;i=6014", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)),
    ],
)
o6.reference(weihenstephan_objtypes.WSMachineType, ns0.reftypes.HasAddIn, o6.ns["ns=weihenstephan;i=5001"])
o6.reference(o6.ns["ns=weihenstephan;i=5001"], "i=17603", "ns=machinery;i=1010")
o6.reference(o6.ns["ns=weihenstephan;i=5001"], "i=17603", "ns=machinery;i=1011")
ns0.vartypes.PropertyType(
    nodeId="ns=weihenstephan;i=6021",
    browseName="EnumValues",
    parent="ns=weihenstephan;i=3000",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("Off", "en"),
            description=o6.LocalizedText(
                "The machine state (in the Weihenstephan Standards the machine state is understood to be the operating mode) provides information about whether the machine is off (Off: relevant bit = 1 or identification by the documented integer number). If this bit is not set, then the machine is in operation and is in one of the following operating modes.",
                "en",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("Manual", "en"),
            description=o6.LocalizedText(
                "An operating mode in which the control units only operate with intervention by the operator and involve possible locking mechanisms (DIN 19237). As opposed to the DIN standard, in the context of the Weihenstephan Standards this term also includes the setup mode, the step setting mode and tipping mode.",
                "en",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("Semi-automatic", "en"),
            description=o6.LocalizedText(
                "An operating mode in which only some of the controls or part of the program function without intervention by the operator (DIN 19 237). In the context of the Weihenstephan Standards, this term means that the machines of a bottling plant are not integrated into a control concept for the entire system and the set output is manually controlled on site.",
                "en",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=8,
            displayName=o6.LocalizedText("Automatic", "en"),
            description=o6.LocalizedText(
                "An operating mode in which the control unit operates without intervention by the operator following a set of control procedures (DIN 19 237). In the context of the Weihenstephan Standards this term means that the machines of a production plant are integrated into a control concept for the entire system and the set output is automatically controlled.",
                "en",
            ),
        ),
    ],
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=weihenstephan;i=6026",
    browseName="EnumValues",
    parent="ns=weihenstephan;i=3001",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[8],
    value=[
        ns0.datatypes.EnumValueType(
            value=0,
            displayName=o6.LocalizedText("Undefined (No Program)", "en"),
            description=o6.LocalizedText(
                "A machine was turned on, but no program for a special application function has been selected. &#8222;Undefined&#8220; may also be used to provide the information that a machine is ready for action, but not required (&#8222;No Order, No Activity&#8220;)",
                "en",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=1, displayName=o6.LocalizedText("Production", "en"), description=o6.LocalizedText("The machine is functioning as designed by the manufacturer.", "en")
        ),
        ns0.datatypes.EnumValueType(
            value=2,
            displayName=o6.LocalizedText("Start Up", "en"),
            description=o6.LocalizedText(
                "Although the machine is functioning as designed by the manufacturer, it is running a start-up pro-gram which ensures full production after a warm-up period as stipulated by regulations or for safe-ty considerations, or in conjunction with container buffering machines.",
                "en",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=4,
            displayName=o6.LocalizedText("Run Down", "en"),
            description=o6.LocalizedText(
                "Although the machine is functioning as designed by the manufacturer, it is running a stop program which ensures production stop after a run-down period as stipulated by regulations or for safety considerations, or in conjunction with container buffering machines.",
                "en",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=8,
            displayName=o6.LocalizedText("Clean", "en"),
            description=o6.LocalizedText(
                "The machine is running the cleaning program. This program can consist of program steps which can be controlled independently of each another, for example the program step &#8220;flush&#8221; for the filling or closing machine, or the program step &#8220;headspace disinfection&#8221; for the cleaning machine.",
                "en",
            ),
        ),
        ns0.datatypes.EnumValueType(
            value=16,
            displayName=o6.LocalizedText("Changeover", "en"),
            description=o6.LocalizedText("The machine is running the changeover program in which automatic machine adjustments are made depending on specific parameters.", "en"),
        ),
        ns0.datatypes.EnumValueType(
            value=32,
            displayName=o6.LocalizedText("Maintenance", "en"),
            description=o6.LocalizedText("The machine is running the maintenance program in which the maintenance and service work are carried out.", "en"),
        ),
        ns0.datatypes.EnumValueType(
            value=64,
            displayName=o6.LocalizedText("Break", "en"),
            description=o6.LocalizedText(
                "The machine is running the break program. This ensures there is start up of the machine in accordance with regulations after a break.", "en"
            ),
        ),
    ],
    accessLevel=3,
)


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, pack_ml, weihenstephan_datypes, weihenstephan_vartypes, weihenstephan_objtypes
