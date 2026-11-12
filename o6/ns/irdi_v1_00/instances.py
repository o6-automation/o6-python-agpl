# Copyright (c) 2026 o6 Automation GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
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

"""Generated OPC UA irdi_v1_00 namespace declarations."""

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

http_opcfoundation_org_UA_Dictionary_IRDI = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=irdi_v1_00;i=1000",
    browseName="ns=irdi_v1_00;http://opcfoundation.org/UA/Dictionary/IRDI",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=irdi_v1_00;i=1001", browseName="IsNamespaceSubset", description="If TRUE then the server only supports a subset of the namespace.", dataType=o6.Boolean
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=irdi_v1_00;i=1002",
                browseName="NamespacePublicationDate",
                description="The publication date for the namespace.",
                dataType=o6.DateTime,
                value=o6.DateTime("2020-02-04T00:00:00Z"),
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=irdi_v1_00;i=1003",
                browseName="NamespaceUri",
                description="The URI of the namespace.",
                dataType=o6.String,
                value="http://opcfoundation.org/UA/Dictionary/IRDI",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=irdi_v1_00;i=1004",
                browseName="NamespaceVersion",
                description="The human readable string representing version of the namespace.",
                dataType=o6.String,
                value="1.00",
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=irdi_v1_00;i=1005",
                browseName="StaticNodeIdTypes",
                description="A list of IdTypes for nodes which are the same in every server that exposes them.",
                dataType=ns0.datatypes.IdType,
                valueRank=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=irdi_v1_00;i=1006",
                browseName="StaticNumericNodeIdRange",
                description="A list of ranges for numeric node ids which are the same in every server that exposes them.",
                dataType=ns0.datatypes.NumericRange,
                valueRank=1,
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=irdi_v1_00;i=1007",
                browseName="StaticStringNodeIdPattern",
                description="A regular expression which matches string node ids are the same in every server that exposes them.",
                dataType=o6.String,
            )
        ),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
defaultRolePermissions = ns0.vartypes.PropertyType(
    nodeId="ns=irdi_v1_00;i=1008", browseName="DefaultRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0]
)
zero112_2_61360_7_CBA031_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61360_7#CBA031#001",
    browseName="ns=irdi_v1_00;0112/2///61360_7#CBA031#001",
    displayName="name of manufacturer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61360_7_CBA032_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61360_7#CBA032#001",
    browseName="ns=irdi_v1_00;0112/2///61360_7#CBA032#001",
    displayName="URI of manufacturer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61360_7_CBA039_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61360_7#CBA039#001",
    browseName="ns=irdi_v1_00;0112/2///61360_7#CBA039#001",
    displayName="model name of product",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61360_7_CBA040_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61360_7#CBA040#001",
    browseName="ns=irdi_v1_00;0112/2///61360_7#CBA040#001",
    displayName="code of product",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61360_7_CBA046_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61360_7#CBA046#001",
    browseName="ns=irdi_v1_00;0112/2///61360_7#CBA046#001",
    displayName="software version",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61360_7_CBA047_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61360_7#CBA047#001",
    browseName="ns=irdi_v1_00;0112/2///61360_7#CBA047#001",
    displayName="hardware version",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61360_7_CBA050_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61360_7#CBA050#001",
    browseName="ns=irdi_v1_00;0112/2///61360_7#CBA050#001",
    displayName="serial number",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61360_7_CBA055_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61360_7#CBA055#001",
    browseName="ns=irdi_v1_00;0112/2///61360_7#CBA055#001",
    displayName="URI of product instance",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA038_003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA038#003",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA038#003",
    displayName="Asset ID",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA038_004 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA038#004",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA038#004",
    displayName="identification code of device",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA300_006 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA300#006",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA300#006",
    displayName="Product code",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA418_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA418#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA418#001",
    displayName="Pulse value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA418_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA418#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA418#002",
    displayName="pulse value of mass",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA565_007 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA565#007",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA565#007",
    displayName="Manufacturer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA567_007 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA567#007",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA567#007",
    displayName="Model",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA601_006 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA601#006",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA601#006",
    displayName="Software revision",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA635_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA635#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA635#002",
    displayName="Pulse width",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA635_003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA635#003",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA635#003",
    displayName="set pulse width",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA752_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA752#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA752#002",
    displayName="Accelerometer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA753_003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA753#003",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA753#003",
    displayName="Current transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA754_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA754#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA754#001",
    displayName="Density transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA763_003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA763#003",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA763#003",
    displayName="Coriolis mass flow transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA764_003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA764#003",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA764#003",
    displayName="Thermal mass flow transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA782_003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA782#003",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA782#003",
    displayName="Volume flow transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA803_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA803#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA803#002",
    displayName="Level transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA804_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA804#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA804#002",
    displayName="Displacer level transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA806_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA806#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA806#002",
    displayName="Capacitance level transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA824_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA824#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA824#002",
    displayName="Free-space radar level transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA827_003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA827#003",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA827#003",
    displayName="Guided-wave radar level transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA829_003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA829#003",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA829#003",
    displayName="Ultrasonic level transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA830_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA830#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA830#002",
    displayName="Power transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA831_003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA831#003",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA831#003",
    displayName="Pressure transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA835_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA835#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA835#002",
    displayName="Temperature transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA839_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA839#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA839#002",
    displayName="Velocity transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA841_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA841#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA841#002",
    displayName="Voltage transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA842_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA842#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA842#002",
    displayName="Weight transmitter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA926_006 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA926#006",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA926#006",
    displayName="Hardware revision",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA927_005 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA927#005",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA927#005",
    displayName="Temperature",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA946_004 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA946#004",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA946#004",
    displayName="Density",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA951_007 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA951#007",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA951#007",
    displayName="Serial number",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA968_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA968#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA968#002",
    displayName="UnitOfMeasure",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABA968_004 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA968#004",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA968#004",
    displayName="unit of measure",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABB088_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB088#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB088#002",
    displayName="Sensor type",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABB088_003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB088#003",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB088#003",
    displayName="type of RTD sensor",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABB091_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB091#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB091#002",
    displayName="RTD-Sensor connection",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABB091_003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB091#003",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB091#003",
    displayName="style of wiring",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABB092_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB092#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB092#002",
    displayName="Sensor type",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABB092_003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB092#003",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB092#003",
    displayName="type of thermocouple sensor",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABB093_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB093#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB093#002",
    displayName="TC-Sensor reference",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABB093_003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB093#003",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB093#003",
    displayName="type of thermocouple reference junction",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABB271_007 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB271#007",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB271#007",
    displayName="Tag",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABB271_009 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB271#009",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB271#009",
    displayName="tag name",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABB290_005 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB290#005",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB290#005",
    displayName="Mass flow rate",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABB291_005 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB291#005",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB291#005",
    displayName="Volume flow rate",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABB292_005 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB292#005",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB292#005",
    displayName="Normalized volume flow rate",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABD740_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABD740#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABD740#002",
    displayName="Operating direction",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABD740_003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABD740#003",
    browseName="ns=irdi_v1_00;0112/2///61987#ABD740#003",
    displayName="type of action",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABD742_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABD742#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABD742#002",
    displayName="Actuator type",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABD742_003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABD742#003",
    browseName="ns=irdi_v1_00;0112/2///61987#ABD742#003",
    displayName="type of actuator compatibility",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABE882_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABE882#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABE882#001",
    displayName="Pulse value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABE882_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABE882#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABE882#002",
    displayName="pulse value of volume",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABF161_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABF161#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABF161#001",
    displayName="nominal cell constant",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABF288_004 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABF288#004",
    browseName="ns=irdi_v1_00;0112/2///61987#ABF288#004",
    displayName="set type of connected probe",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABH327_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABH327#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABH327#001",
    displayName="Mass",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABH328_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABH328#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABH328#001",
    displayName="Volume",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABH329_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABH329#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABH329#002",
    displayName="Level",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABH526_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABH526#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABH526#002",
    displayName="Damping",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABH609_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABH609#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABH609#002",
    displayName="type of calibration",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABI407_004 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABI407#004",
    browseName="ns=irdi_v1_00;0112/2///61987#ABI407#004",
    displayName="others",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABJ683_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABJ683#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABJ683#001",
    displayName="ControlReadback",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABJ724_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABJ724#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABJ724#002",
    displayName="Low flow cut off",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABJ724_003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABJ724#003",
    browseName="ns=irdi_v1_00;0112/2///61987#ABJ724#003",
    displayName="value of low flow cut-off in units of span",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK976_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK976#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK976#001",
    displayName="Cu1000",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK977_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK977#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK977#001",
    displayName="Cu25",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK978_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK978#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK978#001",
    displayName="Ni100",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK979_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK979#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK979#001",
    displayName="Ni1000",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK980_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK980#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK980#001",
    displayName="Ni120",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK981_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK981#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK981#001",
    displayName="Ni25",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK982_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK982#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK982#001",
    displayName="Ni50",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK983_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK983#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK983#001",
    displayName="Pt10",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK984_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK984#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK984#001",
    displayName="Pt100",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK985_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK985#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK985#001",
    displayName="Pt1000",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK986_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK986#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK986#001",
    displayName="Pt200",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK987_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK987#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK987#001",
    displayName="Pt25",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK988_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK988#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK988#001",
    displayName="Pt50",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK989_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK989#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK989#001",
    displayName="Pt500",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK993_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK993#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK993#001",
    displayName="Type B: Pt30Rh-Pt6Rh",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK994_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK994#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK994#001",
    displayName="Type\xa0E: NiCr-CuNi",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK995_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK995#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK995#001",
    displayName="Type J: Fe-CuNi",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK996_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK996#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK996#001",
    displayName="Type\xa0K: NiCr-Ni",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK997_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK997#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK997#001",
    displayName="Type\xa0N: NiCrSi-NiSi",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK998_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK998#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK998#001",
    displayName="Type R: Pt13Rh-Pt",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABK999_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABK999#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABK999#001",
    displayName="Type S: Pt10Rh-Pt",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABL000_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABL000#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABL000#001",
    displayName="Type T: Cu-CuNi",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABL001_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABL001#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABL001#001",
    displayName="Type L: Fe-CuNi",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABL002_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABL002#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABL002#001",
    displayName="Type U: Cu-CuNi",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABL003_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABL003#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABL003#001",
    displayName="Type C: W5%-Re",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABL004_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABL004#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABL004#001",
    displayName="Type D: W3%-Re",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABL113_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABL113#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABL113#001",
    displayName="4-wire",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABL114_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABL114#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABL114#001",
    displayName="3-wire",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABL115_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABL115#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABL115#001",
    displayName="2-wire",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABL147_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABL147#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABL147#001",
    displayName="direct",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABL148_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABL148#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABL148#001",
    displayName="reverse",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABL213_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABL213#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABL213#001",
    displayName="on",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABL214_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABL214#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABL214#001",
    displayName="off",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABL215_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABL215#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABL215#001",
    displayName="open",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABL216_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABL216#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABL216#001",
    displayName="closed",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABL238_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABL238#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABL238#001",
    displayName="RTD",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABL239_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABL239#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABL239#001",
    displayName="TC",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABM625_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABM625#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABM625#001",
    displayName="low",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABM627_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABM627#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABM627#001",
    displayName="high",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABM885_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABM885#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABM885#001",
    displayName="positive",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABM886_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABM886#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABM886#001",
    displayName="negative",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN145_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN145#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN145#001",
    displayName="sliding‐stem linear",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN146_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN146#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN146#001",
    displayName="quarter‐turn rotary",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN416_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN416#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN416#001",
    displayName="external cold junction",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN417_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN417#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN417#001",
    displayName="internal cold junction",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN590_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN590#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN590#001",
    displayName="URI of Product instance",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN591_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN591#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN591#001",
    displayName="URI of Manufacturer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN594_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN594#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN594#002",
    displayName="Flow direction",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN594_003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN594#003",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN594#003",
    displayName="indication of forward flow direction",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN597_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN597#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN597#001",
    displayName="Display language",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN597_004 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN597#004",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN597#004",
    displayName="set display language",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN603_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN603#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN603#001",
    displayName="Revision counter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN603_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN603#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN603#002",
    displayName="revision counter value of the parameter setting",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN604_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN604#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN604#001",
    displayName="Date of last change",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN607_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN607#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN607#001",
    displayName="Setpoint",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN607_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN607#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN607#002",
    displayName="setpoint of positioner",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN609_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN609#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN609#001",
    displayName="Factory reset",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN609_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN609#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN609#002",
    displayName="reset command",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN611_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN611#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN611#001",
    displayName="Simulation state",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN611_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN611#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN611#002",
    displayName="state of simulation",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN613_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN613#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN613#001",
    displayName="Simulation value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN614_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN614#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN614#001",
    displayName="Zero point adjustment",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN614_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN614#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN614#002",
    displayName="zero point setting command",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN616_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN616#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN616#001",
    displayName="Pressure",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN632_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN632#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN632#001",
    displayName="TwoStateSimulationValue",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN632_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN632#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN632#002",
    displayName="discrete two-state value of simulation",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN634_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN634#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN634#001",
    displayName="Value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN635_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN635#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN635#001",
    displayName="TwoStateValue",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN635_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN635#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN635#002",
    displayName="discrete two-state input/output value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN636_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN636#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN636#001",
    displayName="MultiStateValue",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN636_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN636#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN636#002",
    displayName="discrete multistate input/output value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN637_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN637#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN637#001",
    displayName="MultiStateSimulationValue",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN637_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN637#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN637#002",
    displayName="discrete multistate value of simulation",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN639_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN639#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN639#001",
    displayName="operating time",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN644_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN644#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN644#001",
    displayName="Actual value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN645_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN645#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN645#001",
    displayName="TwoStateActualValue",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN645_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN645#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN645#002",
    displayName="discrete two-state actual value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN646_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN646#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN646#001",
    displayName="MultiStateActualValue",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN646_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN646#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN646#002",
    displayName="discrete multistate actual value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN726_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN726#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN726#001",
    displayName="Autoadjust",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN726_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN726#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN726#002",
    displayName="autoadjust command",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN824_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN824#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN824#001",
    displayName="no action",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN825_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN825#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN825#002",
    displayName="factory reset",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN826_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN826#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN826#002",
    displayName="application reset",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN827_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN827#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN827#002",
    displayName="communication reset",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN828_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN828#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN828#001",
    displayName="simulation on",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN829_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN829#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN829#001",
    displayName="simulation off",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN836_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN836#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN836#001",
    displayName="in-between",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN839_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN839#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN839#001",
    displayName="moving",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN840_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN840#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN840#001",
    displayName="true",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN841_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN841#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN841#001",
    displayName="false",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN906_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN906#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN906#001",
    displayName="zero point adjustment",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN972_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN972#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN972#001",
    displayName="Device diagnostic status",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABN972_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN972#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN972#002",
    displayName="Device diagnostic status",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP397_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP397#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP397#002",
    displayName="Process analyser",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP400_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP400#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP400#002",
    displayName="Gas chromatograph",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP405_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP405#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP405#002",
    displayName="Conductivity meter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP407_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP407#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP407#002",
    displayName="Amperometric analyser",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP409_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP409#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP409#002",
    displayName="Zirconium dioxide analyser",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP410_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP410#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP410#002",
    displayName="Flame ionisation detector",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP412_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP412#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP412#002",
    displayName="Catalytic bead sensor",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP413_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP413#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP413#002",
    displayName="Infrared sensor",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP415_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP415#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP415#002",
    displayName="Amperometric sensor",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP423_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP423#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP423#002",
    displayName="Optical fluorescence quenching sensor",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP425_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP425#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP425#002",
    displayName="Non-dispersive infrared gas analyser",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP432_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP432#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP432#002",
    displayName="FTNIR or FTIR spectrometer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP433_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP433#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP433#002",
    displayName="Diode array spectrometer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP434_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP434#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP434#002",
    displayName="Raman spectrometer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP435_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP435#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP435#002",
    displayName="Tunable diode laser spectrometer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP436_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP436#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP436#002",
    displayName="Paramagnetic gas analyser",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP440_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP440#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP440#002",
    displayName="pH meter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP444_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP444#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP444#002",
    displayName="TOC analyser",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP453_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP453#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP453#002",
    displayName="Thermal conductivity gas analyser",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP495_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP495#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP495#001",
    displayName="Matrix of components/measurands",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP496_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP496#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP496#001",
    displayName="Chemical component/measurand",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP541_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP541#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP541#002",
    displayName="discrete two-state control value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP542_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP542#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP542#002",
    displayName="discrete two-state setpoint value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP543_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP543#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP543#002",
    displayName="discrete two-state fault value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP544_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP544#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP544#001",
    displayName="date and time of calibration",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP545_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP545#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP545#001",
    displayName="operating cycle counter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP546_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP546#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP546#001",
    displayName="total number of passed CIP events",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP547_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP547#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP547#001",
    displayName="total number of passed SIP events",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP550_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP550#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP550#001",
    displayName="power on time",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP551_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP551#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP551#001",
    displayName="zero signal of detector",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP552_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP552#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP552#001",
    displayName="relative residual operational life of radiation source",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP553_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP553#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP553#001",
    displayName="relative deviation of chopper frequency",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP554_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP554#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP554#001",
    displayName="temperature of thermal combustion reactor",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP555_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP555#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP555#001",
    displayName="temperature of gas cooler",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP556_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP556#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP556#001",
    displayName="temperature of sample cell",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP557_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP557#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP557#001",
    displayName="relative level of reagent",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP558_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP558#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP558#001",
    displayName="volume flow of carrier gas",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP559_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP559#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP559#001",
    displayName="gauge pressure of carrier gas",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP560_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP560#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP560#001",
    displayName="absolute pressure of sample gas",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP561_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP561#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP561#001",
    displayName="volume flow of sample water",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP562_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP562#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP562#001",
    displayName="volume flow of sample gas",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP563_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP563#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP563#001",
    displayName="reference injection volume",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP564_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP564#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP564#001",
    displayName="actual injected volume",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP565_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP565#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP565#001",
    displayName="temperature of sensing element",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP566_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP566#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP566#001",
    displayName="time remaining until next calibration",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP567_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP567#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP567#001",
    displayName="slope of a pH sensing element characteristic",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP568_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP568#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP568#001",
    displayName="zero point of a pH sensing element characteristic",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP569_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP569#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP569#001",
    displayName="t90 settling time at calibration",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP570_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP570#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP570#001",
    displayName="impedance of pH sensing element",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP571_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP571#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP571#001",
    displayName="impedance of pH reference system",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP572_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP572#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP572#001",
    displayName="slope of an amperometric sensing element characteristic",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP573_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP573#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP573#001",
    displayName="zero point of an amperometric sensing element characteristic",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP574_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP574#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP574#001",
    displayName="absolute pressure of air at calibration",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP575_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP575#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP575#001",
    displayName="temperature of sample",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP576_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP576#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP576#001",
    displayName="temperature of catalyst",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP577_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP577#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP577#001",
    displayName="temperature of FID block",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP578_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP578#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP578#001",
    displayName="absolute pressure of fuel gas",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP579_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP579#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP579#001",
    displayName="absolute pressure of the combustion air",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP580_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP580#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP580#001",
    displayName="relative quality of signal fit",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP581_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP581#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP581#001",
    displayName="signal to noise ratio (absolute)",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP582_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP582#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP582#001",
    displayName="transmission ratio",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP583_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP583#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP583#001",
    displayName="temperature of laser",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP584_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP584#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP584#001",
    displayName="relative residual operational life of sensing element",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP585_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP585#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP585#001",
    displayName="relative heat output",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP586_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP586#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP586#001",
    displayName="slope of an optical fluorescence quenching sensing element characteristic",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP587_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP587#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP587#001",
    displayName="zero point of an optical fluorescence quenching sensing element characteristic",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP588_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP588#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP588#001",
    displayName="analog control value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP591_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP591#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP591#001",
    displayName="internal temperature of device/transmitter housing",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP595_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP595#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP595#001",
    displayName="relative residual operational life",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP596_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP596#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP596#001",
    displayName="resistance of cell",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP640_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP640#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP640#002",
    displayName="style of pH sensing element",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP641_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP641#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP641#002",
    displayName="style of conductivity sensing element",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP642_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP642#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP642#002",
    displayName="style of temperature compensation",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP643_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP643#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP643#002",
    displayName="device version",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP644_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP644#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP644#002",
    displayName="discrete multi-state control value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP645_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP645#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP645#002",
    displayName="discrete multi-state setpoint value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP651_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP651#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP651#002",
    displayName="discrete multi-state fault value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP718_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP718#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP718#001",
    displayName="glass electrode",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP719_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP719#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP719#001",
    displayName="ISFET",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP720_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP720#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP720#001",
    displayName="ceramic electrode",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP721_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP721#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP721#001",
    displayName="inductive",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP722_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP722#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP722#001",
    displayName="conductive 2-electrodes",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP723_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP723#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP723#001",
    displayName="conductive 4-electrodes",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP724_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP724#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP724#001",
    displayName="no temperature compensation",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP725_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP725#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP725#001",
    displayName="linear compensation",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP726_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP726#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP726#001",
    displayName="NaCl (IEC 60746-3)",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP727_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP727#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP727#001",
    displayName="water ISO 7888 (20°C)",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP728_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP728#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP728#001",
    displayName="water ISO 7888 (25°C)",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP729_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP729#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP729#001",
    displayName="UPW NaCl",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP730_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP730#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP730#001",
    displayName="UPW HCl",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP731_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP731#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP731#001",
    displayName="compensation table",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP732_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP732#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP732#001",
    displayName="adjustment",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP733_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP733#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP733#001",
    displayName="calibration",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP734_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP734#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP734#001",
    displayName="custody transfer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABP996_002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABP996#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABP996#002",
    displayName="watchdog",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ006_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ006#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ006#001",
    displayName="time of injection",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ007_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ007#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ007#001",
    displayName="quantity of valve switching cycles",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ010_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ010#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ010#001",
    displayName="operating duration of sensing element",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ011_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ011#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ011#001",
    displayName="relative gas flow rate",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ016_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ016#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ016#001",
    displayName="days remaining until next calibration (based on the fixed maintenance interval)",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ017_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ017#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ017#001",
    displayName="days remaining until next calibration (based on the dynamic maintenance interval)",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ018_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ018#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ018#001",
    displayName="consumed sensor capacity",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ019_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ019#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ019#001",
    displayName="peak value over upper range-limit of measurement",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ020_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ020#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ020#001",
    displayName="duration of exceeding the upper range-limit of measurement",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ021_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ021#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ021#001",
    displayName="sensor signal of a catalytic bead sensor",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ022_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ022#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ022#001",
    displayName="peak width of a substance",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ023_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ023#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ023#001",
    displayName="peak height of a substance",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ024_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ024#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ024#001",
    displayName="response factor for calibration range 1",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ025_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ025#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ025#001",
    displayName="lower range-value of volume concentration for calibration range 1",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ026_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ026#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ026#001",
    displayName="upper range-value of volume concentration for calibration range 1",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ027_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ027#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ027#001",
    displayName="response factor for calibration range 2",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ028_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ028#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ028#001",
    displayName="lower range-value of volume concentration for calibration range 2",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ029_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ029#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ029#001",
    displayName="upper range-value of volume concentration for calibration range 2",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ030_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ030#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ030#001",
    displayName="response factor for calibration range 3",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ031_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ031#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ031#001",
    displayName="lower range-value of volume concentration for calibration range 3",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ032_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ032#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ032#001",
    displayName="upper range-value of volume concentration for calibration range 3",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ033_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ033#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ033#001",
    displayName="tailing factor",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ034_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ034#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ034#001",
    displayName="expected retention time of a substance",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ035_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ035#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ035#001",
    displayName="actual retention time of a substance",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ036_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ036#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ036#001",
    displayName="noise of baseline",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ037_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ037#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ037#001",
    displayName="mahalanobis distance",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ038_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ038#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ038#001",
    displayName="spectral residual",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ039_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ039#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ039#001",
    displayName="remaining capacity of the internal data storage",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ040_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ040#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ040#001",
    displayName="relative residual sensitivity of sensing element",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ041_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ041#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ041#001",
    displayName="relative residual operational life of infrared radiation source",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ042_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ042#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ042#001",
    displayName="peak area of a substance",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ043_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ043#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ043#001",
    displayName="total area of measured peaks",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ044_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ044#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ044#001",
    displayName="relative residual operational life of the interferometric laser",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ045_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ045#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ045#001",
    displayName="designation of substance",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ046_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ046#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ046#001",
    displayName="designation of valve",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112_2_61987_ABQ057_001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABQ057#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABQ057#001",
    displayName="electronics read noise",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
dictionaryEntryName_ = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=<DictionaryEntryName>", browseName="ns=irdi_v1_00;<DictionaryEntryName>", parent="i=17594", referenceType=ns0.reftypes.HasComponent
)


del Any, TYPE_CHECKING, uuid, o6, ns0
