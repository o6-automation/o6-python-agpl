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

"""Generated OPC UA irdi namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

httpColonSlashSlashOpcfoundationDotOrgSlashUASlashDictionarySlashIRDI = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=irdi;i=1000",
    browseName="ns=irdi;http://opcfoundation.org/UA/Dictionary/IRDI",
    modellingRule="Optional",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=irdi;i=1001", browseName="IsNamespaceSubset", description="If TRUE then the server only supports a subset of the namespace.", dataType=o6.Boolean
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=irdi;i=1002",
                browseName="NamespacePublicationDate",
                description="The publication date for the namespace.",
                dataType=o6.DateTime,
                value=o6.DateTime("2025-11-10T00:00:00Z"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=irdi;i=1003", browseName="NamespaceUri", description="The URI of the namespace.", dataType=o6.String, value="http://opcfoundation.org/UA/Dictionary/IRDI"
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=irdi;i=1004",
                browseName="NamespaceVersion",
                description="The human readable string representing version of the namespace.",
                dataType=o6.String,
                value="1.02.0",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=irdi;i=1005",
                browseName="StaticNodeIdTypes",
                description="A list of IdTypes for nodes which are the same in every server that exposes them.",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=irdi;i=1006",
                browseName="StaticNumericNodeIdRange",
                description="A list of ranges for numeric node ids which are the same in every server that exposes them.",
                dataType=ns0.datatypes.NumericRange,
                valueRank=1,
                arrayDimensions=[0],
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=irdi;i=1007",
                browseName="StaticStringNodeIdPattern",
                description="A regular expression which matches string node ids are the same in every server that exposes them.",
                dataType=o6.String,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=irdi;i=1008", browseName="DefaultRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0])
        ),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61360_7HashCBA031Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61360_7#CBA031#001",
    browseName="ns=irdi;0112/2///61360_7#CBA031#001",
    displayName="name of manufacturer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61360_7HashCBA032Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61360_7#CBA032#001",
    browseName="ns=irdi;0112/2///61360_7#CBA032#001",
    displayName="URI of manufacturer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61360_7HashCBA039Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61360_7#CBA039#001",
    browseName="ns=irdi;0112/2///61360_7#CBA039#001",
    displayName="model name of product",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61360_7HashCBA040Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61360_7#CBA040#001",
    browseName="ns=irdi;0112/2///61360_7#CBA040#001",
    displayName="code of product",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61360_7HashCBA046Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61360_7#CBA046#001",
    browseName="ns=irdi;0112/2///61360_7#CBA046#001",
    displayName="software version",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61360_7HashCBA047Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61360_7#CBA047#001",
    browseName="ns=irdi;0112/2///61360_7#CBA047#001",
    displayName="hardware version",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61360_7HashCBA050Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61360_7#CBA050#001",
    browseName="ns=irdi;0112/2///61360_7#CBA050#001",
    displayName="serial number",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61360_7HashCBA055Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61360_7#CBA055#001",
    browseName="ns=irdi;0112/2///61360_7#CBA055#001",
    displayName="URI of product instance",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA038Hash004 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA038#004",
    browseName="ns=irdi;0112/2///61987#ABA038#004",
    displayName="identification code of device",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA418Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA418#002",
    browseName="ns=irdi;0112/2///61987#ABA418#002",
    displayName="pulse value of mass",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA635Hash003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA635#003",
    browseName="ns=irdi;0112/2///61987#ABA635#003",
    displayName="set pulse width",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA752Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA752#002",
    browseName="ns=irdi;0112/2///61987#ABA752#002",
    displayName="Accelerometer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA753Hash003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA753#003",
    browseName="ns=irdi;0112/2///61987#ABA753#003",
    displayName="Current transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA754Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA754#001",
    browseName="ns=irdi;0112/2///61987#ABA754#001",
    displayName="Density transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA763Hash003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA763#003",
    browseName="ns=irdi;0112/2///61987#ABA763#003",
    displayName="Coriolis mass flow transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA764Hash003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA764#003",
    browseName="ns=irdi;0112/2///61987#ABA764#003",
    displayName="Thermal mass flow transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA782Hash003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA782#003",
    browseName="ns=irdi;0112/2///61987#ABA782#003",
    displayName="Volume flow transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA803Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA803#002",
    browseName="ns=irdi;0112/2///61987#ABA803#002",
    displayName="Level transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA804Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA804#002",
    browseName="ns=irdi;0112/2///61987#ABA804#002",
    displayName="Displacer level transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA806Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA806#002",
    browseName="ns=irdi;0112/2///61987#ABA806#002",
    displayName="Capacitance level transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA824Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA824#002",
    browseName="ns=irdi;0112/2///61987#ABA824#002",
    displayName="Free-space radar level transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA827Hash003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA827#003",
    browseName="ns=irdi;0112/2///61987#ABA827#003",
    displayName="Guided-wave radar level transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA829Hash003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA829#003",
    browseName="ns=irdi;0112/2///61987#ABA829#003",
    displayName="Ultrasonic level transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA830Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA830#002",
    browseName="ns=irdi;0112/2///61987#ABA830#002",
    displayName="Power transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA831Hash003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA831#003",
    browseName="ns=irdi;0112/2///61987#ABA831#003",
    displayName="Pressure transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA835Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA835#002",
    browseName="ns=irdi;0112/2///61987#ABA835#002",
    displayName="Temperature transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA839Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA839#002",
    browseName="ns=irdi;0112/2///61987#ABA839#002",
    displayName="Velocity transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA841Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA841#002",
    browseName="ns=irdi;0112/2///61987#ABA841#002",
    displayName="Voltage transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA842Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA842#002",
    browseName="ns=irdi;0112/2///61987#ABA842#002",
    displayName="Weight transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA927Hash005 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA927#005",
    browseName="ns=irdi;0112/2///61987#ABA927#005",
    displayName="temperature",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA946Hash004 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA946#004",
    browseName="ns=irdi;0112/2///61987#ABA946#004",
    displayName="actual density",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA968Hash004 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABA968#004",
    browseName="ns=irdi;0112/2///61987#ABA968#004",
    displayName="unit of measure",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABB088Hash003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABB088#003",
    browseName="ns=irdi;0112/2///61987#ABB088#003",
    displayName="type of RTD sensor",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABB091Hash003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABB091#003",
    browseName="ns=irdi;0112/2///61987#ABB091#003",
    displayName="style of wiring",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABB092Hash003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABB092#003",
    browseName="ns=irdi;0112/2///61987#ABB092#003",
    displayName="type of thermocouple sensor",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABB093Hash003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABB093#003",
    browseName="ns=irdi;0112/2///61987#ABB093#003",
    displayName="type of thermocouple reference junction",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABB271Hash009 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABB271#009", browseName="ns=irdi;0112/2///61987#ABB271#009", displayName="tag name", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABB290Hash005 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABB290#005",
    browseName="ns=irdi;0112/2///61987#ABB290#005",
    displayName="mass flow rate",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABB291Hash005 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABB291#005",
    browseName="ns=irdi;0112/2///61987#ABB291#005",
    displayName="actual volume flow rate",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABB292Hash005 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABB292#005",
    browseName="ns=irdi;0112/2///61987#ABB292#005",
    displayName="normalized volume flow rate",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABD740Hash003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABD740#003",
    browseName="ns=irdi;0112/2///61987#ABD740#003",
    displayName="type of action",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABD742Hash003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABD742#003",
    browseName="ns=irdi;0112/2///61987#ABD742#003",
    displayName="type of actuator compatibility",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABE882Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABE882#002",
    browseName="ns=irdi;0112/2///61987#ABE882#002",
    displayName="pulse value of volume",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABF161Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABF161#001",
    browseName="ns=irdi;0112/2///61987#ABF161#001",
    displayName="nominal cell constant",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABF288Hash004 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABF288#004",
    browseName="ns=irdi;0112/2///61987#ABF288#004",
    displayName="set type of connected probe",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABH327Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABH327#001", browseName="ns=irdi;0112/2///61987#ABH327#001", displayName="mass", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABH328Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABH328#001",
    browseName="ns=irdi;0112/2///61987#ABH328#001",
    displayName="actual volume",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABH329Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABH329#002", browseName="ns=irdi;0112/2///61987#ABH329#002", displayName="level", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABH526Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABH526#002", browseName="ns=irdi;0112/2///61987#ABH526#002", displayName="damping", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABH609Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABH609#002",
    browseName="ns=irdi;0112/2///61987#ABH609#002",
    displayName="type of calibration",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABI407Hash004 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABI407#004", browseName="ns=irdi;0112/2///61987#ABI407#004", displayName="others", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABJ683Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABJ683#001",
    browseName="ns=irdi;0112/2///61987#ABJ683#001",
    displayName="READBACK_VALUE",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABJ724Hash003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABJ724#003",
    browseName="ns=irdi;0112/2///61987#ABJ724#003",
    displayName="value of low flow cut-off in units of span",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABK976Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK976#001", browseName="ns=irdi;0112/2///61987#ABK976#001", displayName="Cu1000", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABK977Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK977#001", browseName="ns=irdi;0112/2///61987#ABK977#001", displayName="Cu25", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABK978Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK978#001", browseName="ns=irdi;0112/2///61987#ABK978#001", displayName="Ni100", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABK979Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK979#001", browseName="ns=irdi;0112/2///61987#ABK979#001", displayName="Ni1000", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABK980Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK980#001", browseName="ns=irdi;0112/2///61987#ABK980#001", displayName="Ni120", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABK981Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK981#001", browseName="ns=irdi;0112/2///61987#ABK981#001", displayName="Ni25", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABK982Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK982#001", browseName="ns=irdi;0112/2///61987#ABK982#001", displayName="Ni50", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABK983Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK983#001", browseName="ns=irdi;0112/2///61987#ABK983#001", displayName="Pt10", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABK984Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK984#001", browseName="ns=irdi;0112/2///61987#ABK984#001", displayName="Pt100", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABK985Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK985#001", browseName="ns=irdi;0112/2///61987#ABK985#001", displayName="Pt1000", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABK986Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK986#001", browseName="ns=irdi;0112/2///61987#ABK986#001", displayName="Pt200", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABK987Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK987#001", browseName="ns=irdi;0112/2///61987#ABK987#001", displayName="Pt25", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABK988Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK988#001", browseName="ns=irdi;0112/2///61987#ABK988#001", displayName="Pt50", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABK989Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK989#001", browseName="ns=irdi;0112/2///61987#ABK989#001", displayName="Pt500", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABK993Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK993#001",
    browseName="ns=irdi;0112/2///61987#ABK993#001",
    displayName="Type B: Pt30Rh-Pt6Rh",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABK994Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK994#001",
    browseName="ns=irdi;0112/2///61987#ABK994#001",
    displayName="Type\xa0E: NiCr-CuNi",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABK995Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK995#001",
    browseName="ns=irdi;0112/2///61987#ABK995#001",
    displayName="Type J: Fe-CuNi",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABK996Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK996#001",
    browseName="ns=irdi;0112/2///61987#ABK996#001",
    displayName="Type\xa0K: NiCr-Ni",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABK997Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK997#001",
    browseName="ns=irdi;0112/2///61987#ABK997#001",
    displayName="Type\xa0N: NiCrSi-NiSi",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABK998Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK998#001",
    browseName="ns=irdi;0112/2///61987#ABK998#001",
    displayName="Type R: Pt13Rh-Pt",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABK999Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABK999#001",
    browseName="ns=irdi;0112/2///61987#ABK999#001",
    displayName="Type S: Pt10Rh-Pt",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABL000Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABL000#001",
    browseName="ns=irdi;0112/2///61987#ABL000#001",
    displayName="Type T: Cu-CuNi",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABL001Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABL001#001",
    browseName="ns=irdi;0112/2///61987#ABL001#001",
    displayName="Type L: Fe-CuNi",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABL002Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABL002#001",
    browseName="ns=irdi;0112/2///61987#ABL002#001",
    displayName="Type U: Cu-CuNi",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABL003Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABL003#001",
    browseName="ns=irdi;0112/2///61987#ABL003#001",
    displayName="Type C: W5%-Re",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABL004Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABL004#001",
    browseName="ns=irdi;0112/2///61987#ABL004#001",
    displayName="Type D: W3%-Re",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABL113Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABL113#001", browseName="ns=irdi;0112/2///61987#ABL113#001", displayName="4-wire", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABL114Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABL114#001", browseName="ns=irdi;0112/2///61987#ABL114#001", displayName="3-wire", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABL115Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABL115#001", browseName="ns=irdi;0112/2///61987#ABL115#001", displayName="2-wire", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABL147Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABL147#001", browseName="ns=irdi;0112/2///61987#ABL147#001", displayName="direct", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABL148Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABL148#001", browseName="ns=irdi;0112/2///61987#ABL148#001", displayName="reverse", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABL213Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABL213#001", browseName="ns=irdi;0112/2///61987#ABL213#001", displayName="on", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABL214Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABL214#001", browseName="ns=irdi;0112/2///61987#ABL214#001", displayName="off", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABL215Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABL215#001", browseName="ns=irdi;0112/2///61987#ABL215#001", displayName="open", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABL216Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABL216#001", browseName="ns=irdi;0112/2///61987#ABL216#001", displayName="closed", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABL238Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABL238#001", browseName="ns=irdi;0112/2///61987#ABL238#001", displayName="RTD", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABL239Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABL239#001", browseName="ns=irdi;0112/2///61987#ABL239#001", displayName="TC", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABM625Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABM625#001", browseName="ns=irdi;0112/2///61987#ABM625#001", displayName="low", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABM627Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABM627#001", browseName="ns=irdi;0112/2///61987#ABM627#001", displayName="high", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABM885Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABM885#001", browseName="ns=irdi;0112/2///61987#ABM885#001", displayName="positive", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABM886Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABM886#001", browseName="ns=irdi;0112/2///61987#ABM886#001", displayName="negative", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABN145Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN145#001",
    browseName="ns=irdi;0112/2///61987#ABN145#001",
    displayName="sliding‐stem linear",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN146Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN146#001",
    browseName="ns=irdi;0112/2///61987#ABN146#001",
    displayName="quarter‐turn rotary",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN416Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN416#001",
    browseName="ns=irdi;0112/2///61987#ABN416#001",
    displayName="external cold junction",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN417Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN417#001",
    browseName="ns=irdi;0112/2///61987#ABN417#001",
    displayName="internal cold junction",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN594Hash003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN594#003",
    browseName="ns=irdi;0112/2///61987#ABN594#003",
    displayName="indication of forward flow direction",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN597Hash004 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN597#004",
    browseName="ns=irdi;0112/2///61987#ABN597#004",
    displayName="set display language",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN603Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN603#002",
    browseName="ns=irdi;0112/2///61987#ABN603#002",
    displayName="revision counter value of the parameter setting",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN604Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN604#001",
    browseName="ns=irdi;0112/2///61987#ABN604#001",
    displayName="time stamp of last parameter setting change",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN607Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN607#002",
    browseName="ns=irdi;0112/2///61987#ABN607#002",
    displayName="setpoint of positioner",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN609Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN609#002",
    browseName="ns=irdi;0112/2///61987#ABN609#002",
    displayName="reset command",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN611Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN611#002",
    browseName="ns=irdi;0112/2///61987#ABN611#002",
    displayName="state of simulation",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN613Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN613#001",
    browseName="ns=irdi;0112/2///61987#ABN613#001",
    displayName="value of simulation",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN614Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN614#002",
    browseName="ns=irdi;0112/2///61987#ABN614#002",
    displayName="zero point setting command",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN616Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN616#001", browseName="ns=irdi;0112/2///61987#ABN616#001", displayName="pressure", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABN632Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN632#002",
    browseName="ns=irdi;0112/2///61987#ABN632#002",
    displayName="discrete two-state value of simulation",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN634Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN634#001",
    browseName="ns=irdi;0112/2///61987#ABN634#001",
    displayName="input/output value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN635Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN635#002",
    browseName="ns=irdi;0112/2///61987#ABN635#002",
    displayName="discrete two-state input/output value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN636Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN636#002",
    browseName="ns=irdi;0112/2///61987#ABN636#002",
    displayName="discrete multistate input/output value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN637Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN637#002",
    browseName="ns=irdi;0112/2///61987#ABN637#002",
    displayName="discrete multistate value of simulation",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN639Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN639#001",
    browseName="ns=irdi;0112/2///61987#ABN639#001",
    displayName="operating time",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN644Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN644#001",
    browseName="ns=irdi;0112/2///61987#ABN644#001",
    displayName="actual value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN645Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN645#002",
    browseName="ns=irdi;0112/2///61987#ABN645#002",
    displayName="discrete two-state actual value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN646Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN646#002",
    browseName="ns=irdi;0112/2///61987#ABN646#002",
    displayName="discrete multistate actual value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN726Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN726#002",
    browseName="ns=irdi;0112/2///61987#ABN726#002",
    displayName="autoadjust command",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN824Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN824#001", browseName="ns=irdi;0112/2///61987#ABN824#001", displayName="no action", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABN825Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN825#002",
    browseName="ns=irdi;0112/2///61987#ABN825#002",
    displayName="factory reset",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN826Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN826#002",
    browseName="ns=irdi;0112/2///61987#ABN826#002",
    displayName="application reset",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN827Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN827#002",
    browseName="ns=irdi;0112/2///61987#ABN827#002",
    displayName="communication reset",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN828Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN828#001",
    browseName="ns=irdi;0112/2///61987#ABN828#001",
    displayName="simulation on",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN829Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN829#001",
    browseName="ns=irdi;0112/2///61987#ABN829#001",
    displayName="simulation off",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN836Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN836#001",
    browseName="ns=irdi;0112/2///61987#ABN836#001",
    displayName="in-between",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN839Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN839#001", browseName="ns=irdi;0112/2///61987#ABN839#001", displayName="moving", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABN840Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN840#001", browseName="ns=irdi;0112/2///61987#ABN840#001", displayName="true", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABN841Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN841#001", browseName="ns=irdi;0112/2///61987#ABN841#001", displayName="false", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABN906Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN906#001",
    browseName="ns=irdi;0112/2///61987#ABN906#001",
    displayName="zero point adjustment",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN972Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABN972#002",
    browseName="ns=irdi;0112/2///61987#ABN972#002",
    displayName="Device diagnostic status",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP397Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP397#002",
    browseName="ns=irdi;0112/2///61987#ABP397#002",
    displayName="Process analyser",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP400Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP400#002",
    browseName="ns=irdi;0112/2///61987#ABP400#002",
    displayName="Gas chromatograph",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP405Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP405#002",
    browseName="ns=irdi;0112/2///61987#ABP405#002",
    displayName="Conductivity meter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP407Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP407#002",
    browseName="ns=irdi;0112/2///61987#ABP407#002",
    displayName="Amperometric analyser",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP409Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP409#002",
    browseName="ns=irdi;0112/2///61987#ABP409#002",
    displayName="Zirconium dioxide analyser",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP410Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP410#002",
    browseName="ns=irdi;0112/2///61987#ABP410#002",
    displayName="Flame ionisation detector",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP412Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP412#002",
    browseName="ns=irdi;0112/2///61987#ABP412#002",
    displayName="Catalytic bead sensor",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP413Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP413#002",
    browseName="ns=irdi;0112/2///61987#ABP413#002",
    displayName="Infrared sensor",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP415Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP415#002",
    browseName="ns=irdi;0112/2///61987#ABP415#002",
    displayName="Amperometric sensor",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP423Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP423#002",
    browseName="ns=irdi;0112/2///61987#ABP423#002",
    displayName="Optical fluorescence quenching sensor",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP425Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP425#002",
    browseName="ns=irdi;0112/2///61987#ABP425#002",
    displayName="Non-dispersive infrared gas analyser",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP432Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP432#002",
    browseName="ns=irdi;0112/2///61987#ABP432#002",
    displayName="FTNIR or FTIR spectrometer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP433Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP433#002",
    browseName="ns=irdi;0112/2///61987#ABP433#002",
    displayName="Diode array spectrometer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP434Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP434#002",
    browseName="ns=irdi;0112/2///61987#ABP434#002",
    displayName="Raman spectrometer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP435Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP435#002",
    browseName="ns=irdi;0112/2///61987#ABP435#002",
    displayName="Tunable diode laser spectrometer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP436Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP436#002",
    browseName="ns=irdi;0112/2///61987#ABP436#002",
    displayName="Paramagnetic gas analyser",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP440Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP440#002", browseName="ns=irdi;0112/2///61987#ABP440#002", displayName="pH meter", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABP444Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP444#002",
    browseName="ns=irdi;0112/2///61987#ABP444#002",
    displayName="TOC analyser",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP453Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP453#002",
    browseName="ns=irdi;0112/2///61987#ABP453#002",
    displayName="Thermal conductivity gas analyser",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP495Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP495#001",
    browseName="ns=irdi;0112/2///61987#ABP495#001",
    displayName="Matrix of components/measurands",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP496Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP496#001",
    browseName="ns=irdi;0112/2///61987#ABP496#001",
    displayName="Chemical component/measurand",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP541Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP541#002",
    browseName="ns=irdi;0112/2///61987#ABP541#002",
    displayName="discrete two-state control value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP542Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP542#002",
    browseName="ns=irdi;0112/2///61987#ABP542#002",
    displayName="discrete two-state setpoint value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP543Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP543#002",
    browseName="ns=irdi;0112/2///61987#ABP543#002",
    displayName="discrete two-state fault value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP544Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP544#001",
    browseName="ns=irdi;0112/2///61987#ABP544#001",
    displayName="date and time of calibration",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP545Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP545#001",
    browseName="ns=irdi;0112/2///61987#ABP545#001",
    displayName="operating cycle counter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP546Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP546#001",
    browseName="ns=irdi;0112/2///61987#ABP546#001",
    displayName="total number of passed CIP events",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP547Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP547#001",
    browseName="ns=irdi;0112/2///61987#ABP547#001",
    displayName="total number of passed SIP events",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP550Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP550#001",
    browseName="ns=irdi;0112/2///61987#ABP550#001",
    displayName="power on time",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP551Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP551#001",
    browseName="ns=irdi;0112/2///61987#ABP551#001",
    displayName="zero signal of detector",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP552Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP552#001",
    browseName="ns=irdi;0112/2///61987#ABP552#001",
    displayName="relative residual operational life of radiation source",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP553Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP553#001",
    browseName="ns=irdi;0112/2///61987#ABP553#001",
    displayName="relative deviation of chopper frequency",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP554Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP554#001",
    browseName="ns=irdi;0112/2///61987#ABP554#001",
    displayName="temperature of thermal combustion reactor",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP555Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP555#001",
    browseName="ns=irdi;0112/2///61987#ABP555#001",
    displayName="temperature of gas cooler",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP556Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP556#001",
    browseName="ns=irdi;0112/2///61987#ABP556#001",
    displayName="temperature of sample cell",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP557Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP557#001",
    browseName="ns=irdi;0112/2///61987#ABP557#001",
    displayName="relative level of reagent",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP558Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP558#001",
    browseName="ns=irdi;0112/2///61987#ABP558#001",
    displayName="volume flow of carrier gas",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP559Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP559#001",
    browseName="ns=irdi;0112/2///61987#ABP559#001",
    displayName="gauge pressure of carrier gas",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP560Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP560#001",
    browseName="ns=irdi;0112/2///61987#ABP560#001",
    displayName="absolute pressure of sample gas",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP561Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP561#001",
    browseName="ns=irdi;0112/2///61987#ABP561#001",
    displayName="volume flow of sample water",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP562Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP562#001",
    browseName="ns=irdi;0112/2///61987#ABP562#001",
    displayName="volume flow of sample gas",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP563Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP563#001",
    browseName="ns=irdi;0112/2///61987#ABP563#001",
    displayName="reference injection volume",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP564Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP564#001",
    browseName="ns=irdi;0112/2///61987#ABP564#001",
    displayName="actual injected volume",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP565Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP565#001",
    browseName="ns=irdi;0112/2///61987#ABP565#001",
    displayName="temperature of sensing element",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP566Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP566#001",
    browseName="ns=irdi;0112/2///61987#ABP566#001",
    displayName="time remaining until next calibration",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP567Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP567#001",
    browseName="ns=irdi;0112/2///61987#ABP567#001",
    displayName="slope of a pH sensing element characteristic",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP568Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP568#001",
    browseName="ns=irdi;0112/2///61987#ABP568#001",
    displayName="zero point of a pH sensing element characteristic",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP569Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP569#001",
    browseName="ns=irdi;0112/2///61987#ABP569#001",
    displayName="t90 settling time at calibration",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP570Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP570#001",
    browseName="ns=irdi;0112/2///61987#ABP570#001",
    displayName="impedance of pH sensing element",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP571Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP571#001",
    browseName="ns=irdi;0112/2///61987#ABP571#001",
    displayName="impedance of pH reference system",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP572Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP572#001",
    browseName="ns=irdi;0112/2///61987#ABP572#001",
    displayName="slope of an amperometric sensing element characteristic",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP573Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP573#001",
    browseName="ns=irdi;0112/2///61987#ABP573#001",
    displayName="zero point of an amperometric sensing element characteristic",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP574Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP574#001",
    browseName="ns=irdi;0112/2///61987#ABP574#001",
    displayName="absolute pressure of air at calibration",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP575Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP575#001",
    browseName="ns=irdi;0112/2///61987#ABP575#001",
    displayName="temperature of sample",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP576Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP576#001",
    browseName="ns=irdi;0112/2///61987#ABP576#001",
    displayName="temperature of catalyst",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP577Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP577#001",
    browseName="ns=irdi;0112/2///61987#ABP577#001",
    displayName="temperature of FID block",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP578Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP578#001",
    browseName="ns=irdi;0112/2///61987#ABP578#001",
    displayName="absolute pressure of fuel gas",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP579Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP579#001",
    browseName="ns=irdi;0112/2///61987#ABP579#001",
    displayName="absolute pressure of the combustion air",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP580Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP580#001",
    browseName="ns=irdi;0112/2///61987#ABP580#001",
    displayName="relative quality of signal fit",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP581Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP581#001",
    browseName="ns=irdi;0112/2///61987#ABP581#001",
    displayName="signal to noise ratio (absolute)",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP582Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP582#001",
    browseName="ns=irdi;0112/2///61987#ABP582#001",
    displayName="transmission ratio",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP583Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP583#001",
    browseName="ns=irdi;0112/2///61987#ABP583#001",
    displayName="temperature of laser",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP584Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP584#001",
    browseName="ns=irdi;0112/2///61987#ABP584#001",
    displayName="relative residual operational life of sensing element",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP585Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP585#001",
    browseName="ns=irdi;0112/2///61987#ABP585#001",
    displayName="relative heat output",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP586Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP586#001",
    browseName="ns=irdi;0112/2///61987#ABP586#001",
    displayName="slope of an optical fluorescence quenching sensing element characteristic",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP587Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP587#001",
    browseName="ns=irdi;0112/2///61987#ABP587#001",
    displayName="zero point of an optical fluorescence quenching sensing element characteristic",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP588Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP588#001",
    browseName="ns=irdi;0112/2///61987#ABP588#001",
    displayName="analog control value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP591Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP591#001",
    browseName="ns=irdi;0112/2///61987#ABP591#001",
    displayName="internal temperature of device/transmitter housing",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP595Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP595#001",
    browseName="ns=irdi;0112/2///61987#ABP595#001",
    displayName="relative residual operational life",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP596Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP596#001",
    browseName="ns=irdi;0112/2///61987#ABP596#001",
    displayName="resistance of cell",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP640Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP640#002",
    browseName="ns=irdi;0112/2///61987#ABP640#002",
    displayName="style of pH sensing element",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP641Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP641#002",
    browseName="ns=irdi;0112/2///61987#ABP641#002",
    displayName="style of conductivity sensing element",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP642Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP642#002",
    browseName="ns=irdi;0112/2///61987#ABP642#002",
    displayName="style of temperature compensation",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP643Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP643#002",
    browseName="ns=irdi;0112/2///61987#ABP643#002",
    displayName="device version",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP644Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP644#002",
    browseName="ns=irdi;0112/2///61987#ABP644#002",
    displayName="discrete multi-state control value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP645Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP645#002",
    browseName="ns=irdi;0112/2///61987#ABP645#002",
    displayName="discrete multi-state setpoint value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP651Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP651#002",
    browseName="ns=irdi;0112/2///61987#ABP651#002",
    displayName="discrete multi-state fault value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP718Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP718#001",
    browseName="ns=irdi;0112/2///61987#ABP718#001",
    displayName="glass electrode",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP719Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP719#001", browseName="ns=irdi;0112/2///61987#ABP719#001", displayName="ISFET", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABP720Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP720#001",
    browseName="ns=irdi;0112/2///61987#ABP720#001",
    displayName="ceramic electrode",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP721Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP721#001", browseName="ns=irdi;0112/2///61987#ABP721#001", displayName="inductive", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABP722Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP722#001",
    browseName="ns=irdi;0112/2///61987#ABP722#001",
    displayName="conductive 2-electrodes",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP723Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP723#001",
    browseName="ns=irdi;0112/2///61987#ABP723#001",
    displayName="conductive 4-electrodes",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP724Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP724#001",
    browseName="ns=irdi;0112/2///61987#ABP724#001",
    displayName="no temperature compensation",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP725Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP725#001",
    browseName="ns=irdi;0112/2///61987#ABP725#001",
    displayName="linear compensation",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP726Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP726#001",
    browseName="ns=irdi;0112/2///61987#ABP726#001",
    displayName="NaCl (IEC 60746-3)",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP727Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP727#001",
    browseName="ns=irdi;0112/2///61987#ABP727#001",
    displayName="water ISO 7888 (20°C)",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP728Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP728#001",
    browseName="ns=irdi;0112/2///61987#ABP728#001",
    displayName="water ISO 7888 (25°C)",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP729Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP729#001", browseName="ns=irdi;0112/2///61987#ABP729#001", displayName="UPW NaCl", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABP730Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP730#001", browseName="ns=irdi;0112/2///61987#ABP730#001", displayName="UPW HCl", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABP731Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP731#001",
    browseName="ns=irdi;0112/2///61987#ABP731#001",
    displayName="compensation table",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP732Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP732#001",
    browseName="ns=irdi;0112/2///61987#ABP732#001",
    displayName="adjustment",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP733Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP733#001",
    browseName="ns=irdi;0112/2///61987#ABP733#001",
    displayName="calibration",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP734Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP734#001",
    browseName="ns=irdi;0112/2///61987#ABP734#001",
    displayName="custody transfer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABP996Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABP996#002", browseName="ns=irdi;0112/2///61987#ABP996#002", displayName="watchdog", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)
zero112Slash2SlashSlashSlash61987HashABQ006Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ006#001",
    browseName="ns=irdi;0112/2///61987#ABQ006#001",
    displayName="time of injection",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ007Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ007#001",
    browseName="ns=irdi;0112/2///61987#ABQ007#001",
    displayName="quantity of valve switching cycles",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ010Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ010#001",
    browseName="ns=irdi;0112/2///61987#ABQ010#001",
    displayName="operating duration of sensing element",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ011Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ011#001",
    browseName="ns=irdi;0112/2///61987#ABQ011#001",
    displayName="relative gas flow rate",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ016Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ016#001",
    browseName="ns=irdi;0112/2///61987#ABQ016#001",
    displayName="days remaining until next calibration (based on the fixed maintenance interval)",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ017Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ017#001",
    browseName="ns=irdi;0112/2///61987#ABQ017#001",
    displayName="days remaining until next calibration (based on the dynamic maintenance interval)",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ018Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ018#001",
    browseName="ns=irdi;0112/2///61987#ABQ018#001",
    displayName="consumed sensor capacity",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ019Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ019#001",
    browseName="ns=irdi;0112/2///61987#ABQ019#001",
    displayName="peak value over upper range-limit of measurement",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ020Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ020#001",
    browseName="ns=irdi;0112/2///61987#ABQ020#001",
    displayName="duration of exceeding the upper range-limit of measurement",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ021Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ021#001",
    browseName="ns=irdi;0112/2///61987#ABQ021#001",
    displayName="sensor signal of a catalytic bead sensor",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ022Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ022#001",
    browseName="ns=irdi;0112/2///61987#ABQ022#001",
    displayName="peak width of a substance",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ023Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ023#001",
    browseName="ns=irdi;0112/2///61987#ABQ023#001",
    displayName="peak height of a substance",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ024Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ024#001",
    browseName="ns=irdi;0112/2///61987#ABQ024#001",
    displayName="response factor for calibration range 1",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ025Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ025#001",
    browseName="ns=irdi;0112/2///61987#ABQ025#001",
    displayName="lower range-value of volume concentration for calibration range 1",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ026Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ026#001",
    browseName="ns=irdi;0112/2///61987#ABQ026#001",
    displayName="upper range-value of volume concentration for calibration range 1",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ027Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ027#001",
    browseName="ns=irdi;0112/2///61987#ABQ027#001",
    displayName="response factor for calibration range 2",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ028Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ028#001",
    browseName="ns=irdi;0112/2///61987#ABQ028#001",
    displayName="lower range-value of volume concentration for calibration range 2",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ029Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ029#001",
    browseName="ns=irdi;0112/2///61987#ABQ029#001",
    displayName="upper range-value of volume concentration for calibration range 2",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ030Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ030#001",
    browseName="ns=irdi;0112/2///61987#ABQ030#001",
    displayName="response factor for calibration range 3",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ031Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ031#001",
    browseName="ns=irdi;0112/2///61987#ABQ031#001",
    displayName="lower range-value of volume concentration for calibration range 3",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ032Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ032#001",
    browseName="ns=irdi;0112/2///61987#ABQ032#001",
    displayName="upper range-value of volume concentration for calibration range 3",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ033Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ033#001",
    browseName="ns=irdi;0112/2///61987#ABQ033#001",
    displayName="tailing factor",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ034Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ034#001",
    browseName="ns=irdi;0112/2///61987#ABQ034#001",
    displayName="expected retention time of a substance",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ035Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ035#001",
    browseName="ns=irdi;0112/2///61987#ABQ035#001",
    displayName="actual retention time of a substance",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ036Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ036#001",
    browseName="ns=irdi;0112/2///61987#ABQ036#001",
    displayName="noise of baseline",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ037Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ037#001",
    browseName="ns=irdi;0112/2///61987#ABQ037#001",
    displayName="mahalanobis distance",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ038Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ038#001",
    browseName="ns=irdi;0112/2///61987#ABQ038#001",
    displayName="spectral residual",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ039Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ039#001",
    browseName="ns=irdi;0112/2///61987#ABQ039#001",
    displayName="remaining capacity of the internal data storage",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ040Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ040#001",
    browseName="ns=irdi;0112/2///61987#ABQ040#001",
    displayName="relative residual sensitivity of sensing element",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ041Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ041#001",
    browseName="ns=irdi;0112/2///61987#ABQ041#001",
    displayName="relative residual operational life of infrared radiation source",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ042Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ042#001",
    browseName="ns=irdi;0112/2///61987#ABQ042#001",
    displayName="peak area of a substance",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ043Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ043#001",
    browseName="ns=irdi;0112/2///61987#ABQ043#001",
    displayName="total area of measured peaks",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ044Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ044#001",
    browseName="ns=irdi;0112/2///61987#ABQ044#001",
    displayName="relative residual operational life of the interferometric laser",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ045Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ045#001",
    browseName="ns=irdi;0112/2///61987#ABQ045#001",
    displayName="designation of substance",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ046Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ046#001",
    browseName="ns=irdi;0112/2///61987#ABQ046#001",
    displayName="designation of valve",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABQ057Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=0112/2///61987#ABQ057#001",
    browseName="ns=irdi;0112/2///61987#ABQ057#001",
    displayName="electronics read noise",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
langleDictionaryEntryNameRangle = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi;s=<DictionaryEntryName>", browseName="ns=irdi;<DictionaryEntryName>", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)


del Any, TYPE_CHECKING, uuid, o6, ns0
