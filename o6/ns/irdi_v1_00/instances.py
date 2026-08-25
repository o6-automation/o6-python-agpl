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

httpColonSlashSlashOpcfoundationDotOrgSlashUASlashDictionarySlashIRDI = ns0.objtypes.NamespaceMetadataType(
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
zero112Slash2SlashSlashSlash61987HashABA038Hash003 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA038#003",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA038#003",
    displayName="Asset ID",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA300Hash006 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA300#006",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA300#006",
    displayName="Product code",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA418Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA418#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA418#001",
    displayName="Pulse value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA565Hash007 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA565#007",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA565#007",
    displayName="Manufacturer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA567Hash007 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA567#007",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA567#007",
    displayName="Model",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA601Hash006 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA601#006",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA601#006",
    displayName="Software revision",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA635Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA635#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA635#002",
    displayName="Pulse width",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA926Hash006 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA926#006",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA926#006",
    displayName="Hardware revision",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA927Hash005 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA927#005",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA927#005",
    displayName="Temperature",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA946Hash004 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA946#004",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA946#004",
    displayName="Density",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA951Hash007 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA951#007",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA951#007",
    displayName="Serial number",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABA968Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABA968#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABA968#002",
    displayName="UnitOfMeasure",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABB088Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB088#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB088#002",
    displayName="Sensor type",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABB091Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB091#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB091#002",
    displayName="RTD-Sensor connection",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABB092Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB092#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB092#002",
    displayName="Sensor type",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABB093Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB093#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB093#002",
    displayName="TC-Sensor reference",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABB271Hash007 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB271#007",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB271#007",
    displayName="Tag",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABB290Hash005 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB290#005",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB290#005",
    displayName="Mass flow rate",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABB291Hash005 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB291#005",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB291#005",
    displayName="Volume flow rate",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABB292Hash005 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABB292#005",
    browseName="ns=irdi_v1_00;0112/2///61987#ABB292#005",
    displayName="Normalized volume flow rate",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABD740Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABD740#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABD740#002",
    displayName="Operating direction",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABD742Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABD742#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABD742#002",
    displayName="Actuator type",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABE882Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABE882#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABE882#001",
    displayName="Pulse value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABH327Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABH327#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABH327#001",
    displayName="Mass",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABH328Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABH328#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABH328#001",
    displayName="Volume",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABH329Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABH329#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABH329#002",
    displayName="Level",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABH526Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABH526#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABH526#002",
    displayName="Damping",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABJ683Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABJ683#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABJ683#001",
    displayName="ControlReadback",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABJ724Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABJ724#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABJ724#002",
    displayName="Low flow cut off",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN590Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN590#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN590#001",
    displayName="URI of Product instance",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN591Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN591#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN591#001",
    displayName="URI of Manufacturer",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN594Hash002 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN594#002",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN594#002",
    displayName="Flow direction",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN597Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN597#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN597#001",
    displayName="Display language",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN603Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN603#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN603#001",
    displayName="Revision counter",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN604Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN604#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN604#001",
    displayName="Date of last change",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN607Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN607#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN607#001",
    displayName="Setpoint",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN609Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN609#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN609#001",
    displayName="Factory reset",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN611Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN611#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN611#001",
    displayName="Simulation state",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN613Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN613#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN613#001",
    displayName="Simulation value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN614Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN614#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN614#001",
    displayName="Zero point adjustment",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN616Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN616#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN616#001",
    displayName="Pressure",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN632Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN632#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN632#001",
    displayName="TwoStateSimulationValue",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN634Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN634#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN634#001",
    displayName="Value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN635Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN635#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN635#001",
    displayName="TwoStateValue",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN636Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN636#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN636#001",
    displayName="MultiStateValue",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN637Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN637#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN637#001",
    displayName="MultiStateSimulationValue",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN644Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN644#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN644#001",
    displayName="Actual value",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN645Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN645#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN645#001",
    displayName="TwoStateActualValue",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN646Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN646#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN646#001",
    displayName="MultiStateActualValue",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN726Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN726#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN726#001",
    displayName="Autoadjust",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)
zero112Slash2SlashSlashSlash61987HashABN972Hash001 = ns0.objtypes.IrdiDictionaryEntryType(
    nodeId="ns=irdi_v1_00;s=0112/2///61987#ABN972#001",
    browseName="ns=irdi_v1_00;0112/2///61987#ABN972#001",
    displayName="Device diagnostic status",
    parent="i=17594",
    referenceType=ns0.reftypes.HasComponent,
)


del Any, TYPE_CHECKING, uuid, o6, ns0
