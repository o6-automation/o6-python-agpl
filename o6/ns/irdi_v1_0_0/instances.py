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

"""Generated OPC UA irdi_v1_0_0 namespace declarations."""

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
    nodeId="ns=irdi_v1_0_0;i=5001",
    browseName="ns=irdi_v1_0_0;http://opcfoundation.org/UA/Dictionary/IRDI",
    references=[
        o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
            # It is intentionally omitted; the server supplies a typed default.
            ns0.vartypes.PropertyType(nodeId="ns=irdi_v1_0_0;i=6001", browseName="IsNamespaceSubset", dataType=o6.Boolean)
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=irdi_v1_0_0;i=6002", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2024-07-11T15:02:44Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=irdi_v1_0_0;i=6003", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/Dictionary/IRDI")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=irdi_v1_0_0;i=6004", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=irdi_v1_0_0;i=6005", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=irdi_v1_0_0;i=6006", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1)),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=irdi_v1_0_0;i=6007", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash62683HashACE205 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE205", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE205", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE211 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE211", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE211", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE212 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE212", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE212", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE213 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE213", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE213", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE220 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE220", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE220", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE221 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE221", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE221", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE222 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE222", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE222", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE223 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE223", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE223", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE224 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE224", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE224", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE225 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE225", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE225", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE227 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE227", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE227", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE301 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE301", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE301", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE302 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE302", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE302", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE303 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE303", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE303", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE331 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE331", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE331", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE332 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE332", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE332", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE333 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE333", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE333", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE334 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE334", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE334", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE362 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE362", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE362", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE404 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE404", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE404", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE430 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE430", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE430", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE434 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE434", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE434", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE455 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE455", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE455", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE457 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE457", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE457", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE508 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE508", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE508", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE511 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE511", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE511", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE602 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE602", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE602", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE741 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE741", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE741", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACE749 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACE749", browseName="ns=irdi_v1_0_0;0112/2///62683#ACE749", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH005 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH005", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH005", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH006 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH006", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH006", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH020 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH020", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH020", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH021 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH021", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH021", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH022 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH022", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH022", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH023 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH023", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH023", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH024 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH024", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH024", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH025 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH025", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH025", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH026 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH026", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH026", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH027 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH027", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH027", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH028 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH028", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH028", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH029 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH029", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH029", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH030 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH030", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH030", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH031 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH031", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH031", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH318 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH318", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH318", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH319 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH319", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH319", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH471Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH471#001", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH471#001", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH472Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH472#001", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH472#001", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH473Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH473#001", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH473#001", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH474Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH474#001", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH474#001", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH505Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH505#001", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH505#001", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH506Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH506#001", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH506#001", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH507Hash001 = ns0.objtypes.BaseObjectType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH507#001", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH507#001", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH508Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH508#001", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH508#001", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH569Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH569#001", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH569#001", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH649Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH649#001", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH649#001", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH652Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH652#001", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH652#001", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH653Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH653#001", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH653#001", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH654Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH654#001", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH654#001", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH657Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH657#001", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH657#001", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH661Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH661#001", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH661#001", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH662Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH662#001", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH662#001", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH663Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH663#001", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH663#001", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH666Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH666#001", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH666#001", parent="i=17594", referenceType=ns0.reftypes.Organizes
)
zero112Slash2SlashSlashSlash62683HashACH669Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_0_0;s=0112/2///62683#ACH669#001", browseName="ns=irdi_v1_0_0;0112/2///62683#ACH669#001", parent="i=17594", referenceType=ns0.reftypes.Organizes
)


del Any, TYPE_CHECKING, uuid, o6, ns0
