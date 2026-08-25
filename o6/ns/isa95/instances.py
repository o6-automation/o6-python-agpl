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

"""Generated OPC UA isa95 namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as isa95_reftypes
from . import datatypes as isa95_datypes
from . import vartypes as isa95_vartypes
from . import objtypes as isa95_objtypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4778",
    browseName="ns=isa95;SchemeId",
    modellingRule="Optional",
    parent="ns=isa95;i=4777",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4779",
    browseName="ns=isa95;SchemeVersionId",
    modellingRule="Optional",
    parent="ns=isa95;i=4777",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4780",
    browseName="ns=isa95;SchemeAgencyId",
    modellingRule="Optional",
    parent="ns=isa95;i=4777",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95;i=4784", browseName="Default XML")
o6.hasEncoding(isa95_datypes.CurrencyCode, o6.ns["ns=isa95;i=4784"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=isa95;i=4785", browseName="ns=isa95;CurrencyCode", dataType=o6.String, value="//xs:element[@name='CurrencyCode']")
o6.reference(o6.ns["ns=isa95;i=4784"], "i=39", o6.ns["ns=isa95;i=4785"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95;i=4788", browseName="Default Binary")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=isa95;i=4789", browseName="ns=isa95;CurrencyCode", dataType=o6.String, value="CurrencyCode")
o6.reference(o6.ns["ns=isa95;i=4788"], "i=39", o6.ns["ns=isa95;i=4789"])
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4793",
    browseName="ns=isa95;ListId",
    modellingRule="Optional",
    parent="ns=isa95;i=4792",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4794",
    browseName="ns=isa95;ListAgencyId",
    modellingRule="Optional",
    parent="ns=isa95;i=4792",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4795",
    browseName="ns=isa95;ListVersionId",
    modellingRule="Optional",
    parent="ns=isa95;i=4792",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4797",
    browseName="ns=isa95;Currency",
    modellingRule="Optional",
    parent="ns=isa95;i=4796",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=isa95_datypes.CurrencyCode,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4800",
    browseName="ns=isa95;CharacterSet",
    modellingRule="Optional",
    parent="ns=isa95;i=4798",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4801",
    browseName="ns=isa95;Encoding",
    modellingRule="Optional",
    parent="ns=isa95;i=4798",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4802",
    browseName="ns=isa95;FileName",
    modellingRule="Optional",
    parent="ns=isa95;i=4798",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4804",
    browseName="ns=isa95;Timezone",
    modellingRule="Optional",
    parent="ns=isa95;i=4803",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4805",
    browseName="ns=isa95;DaylightSavings",
    modellingRule="Optional",
    parent="ns=isa95;i=4803",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.Boolean,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4808",
    browseName="ns=isa95;FileName",
    modellingRule="Optional",
    parent="ns=isa95;i=4806",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4810",
    browseName="ns=isa95;Unit",
    modellingRule="Optional",
    parent="ns=isa95;i=4809",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=ns0.datatypes.EUInformation,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4812",
    browseName="ns=isa95;Unit",
    modellingRule="Optional",
    parent="ns=isa95;i=4811",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=ns0.datatypes.EUInformation,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4814",
    browseName="ns=isa95;Unit",
    modellingRule="Optional",
    parent="ns=isa95;i=4813",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=ns0.datatypes.EUInformation,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4816",
    browseName="ns=isa95;Unit",
    modellingRule="Optional",
    parent="ns=isa95;i=4815",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=ns0.datatypes.EUInformation,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4818",
    browseName="ns=isa95;Unit",
    modellingRule="Optional",
    parent="ns=isa95;i=4817",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=ns0.datatypes.EUInformation,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4820",
    browseName="ns=isa95;Unit",
    modellingRule="Optional",
    parent="ns=isa95;i=4819",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=ns0.datatypes.EUInformation,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4824",
    browseName="ns=isa95;FileName",
    modellingRule="Optional",
    parent="ns=isa95;i=4822",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4826",
    browseName="ns=isa95;Multiplier",
    modellingRule="Optional",
    parent="ns=isa95;i=4825",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.Double,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4827",
    browseName="ns=isa95;Unit",
    modellingRule="Optional",
    parent="ns=isa95;i=4825",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=ns0.datatypes.EUInformation,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4828",
    browseName="ns=isa95;Currency",
    modellingRule="Optional",
    parent="ns=isa95;i=4825",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=isa95_datypes.CurrencyCode,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4829",
    browseName="ns=isa95;BaseMultiplier",
    modellingRule="Optional",
    parent="ns=isa95;i=4825",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.Double,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4830",
    browseName="ns=isa95;BaseUnit",
    modellingRule="Optional",
    parent="ns=isa95;i=4825",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=ns0.datatypes.EUInformation,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4831",
    browseName="ns=isa95;BaseCurrency",
    modellingRule="Optional",
    parent="ns=isa95;i=4825",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=isa95_datypes.CurrencyCode,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4833",
    browseName="ns=isa95;Multiplier",
    modellingRule="Optional",
    parent="ns=isa95;i=4832",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.Double,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4834",
    browseName="ns=isa95;Unit",
    modellingRule="Optional",
    parent="ns=isa95;i=4832",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=ns0.datatypes.EUInformation,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4835",
    browseName="ns=isa95;Currency",
    modellingRule="Optional",
    parent="ns=isa95;i=4832",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=isa95_datypes.CurrencyCode,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4836",
    browseName="ns=isa95;BaseMultiplier",
    modellingRule="Optional",
    parent="ns=isa95;i=4832",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.Double,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4837",
    browseName="ns=isa95;BaseUnit",
    modellingRule="Optional",
    parent="ns=isa95;i=4832",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=ns0.datatypes.EUInformation,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4838",
    browseName="ns=isa95;BaseCurrency",
    modellingRule="Optional",
    parent="ns=isa95;i=4832",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=isa95_datypes.CurrencyCode,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4840",
    browseName="ns=isa95;Multiplier",
    modellingRule="Optional",
    parent="ns=isa95;i=4839",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.Double,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4841",
    browseName="ns=isa95;Unit",
    modellingRule="Optional",
    parent="ns=isa95;i=4839",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=ns0.datatypes.EUInformation,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4842",
    browseName="ns=isa95;Currency",
    modellingRule="Optional",
    parent="ns=isa95;i=4839",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=isa95_datypes.CurrencyCode,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4843",
    browseName="ns=isa95;BaseMultiplier",
    modellingRule="Optional",
    parent="ns=isa95;i=4839",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.Double,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4844",
    browseName="ns=isa95;BaseUnit",
    modellingRule="Optional",
    parent="ns=isa95;i=4839",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=ns0.datatypes.EUInformation,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4845",
    browseName="ns=isa95;BaseCurrency",
    modellingRule="Optional",
    parent="ns=isa95;i=4839",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=isa95_datypes.CurrencyCode,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4847",
    browseName="ns=isa95;Multiplier",
    modellingRule="Optional",
    parent="ns=isa95;i=4846",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.Double,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4848",
    browseName="ns=isa95;Unit",
    modellingRule="Optional",
    parent="ns=isa95;i=4846",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=ns0.datatypes.EUInformation,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4849",
    browseName="ns=isa95;Currency",
    modellingRule="Optional",
    parent="ns=isa95;i=4846",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=isa95_datypes.CurrencyCode,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4850",
    browseName="ns=isa95;BaseMultiplier",
    modellingRule="Optional",
    parent="ns=isa95;i=4846",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.Double,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4851",
    browseName="ns=isa95;BaseUnit",
    modellingRule="Optional",
    parent="ns=isa95;i=4846",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=ns0.datatypes.EUInformation,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4852",
    browseName="ns=isa95;BaseCurrency",
    modellingRule="Optional",
    parent="ns=isa95;i=4846",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=isa95_datypes.CurrencyCode,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4855",
    browseName="ns=isa95;FileName",
    modellingRule="Optional",
    parent="ns=isa95;i=4853",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4858",
    browseName="ns=isa95;FileName",
    modellingRule="Optional",
    parent="ns=isa95;i=4856",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95;i=4863", browseName="Default XML")
o6.hasEncoding(isa95_datypes.ISA95TestResultMeasurementDataType, o6.ns["ns=isa95;i=4863"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95;i=4864", browseName="ns=isa95;ISA95TestResultMeasurementDataType", dataType=o6.String, value="//xs:element[@name='ISA95TestResultMeasurementDataType']"
)
o6.reference(o6.ns["ns=isa95;i=4863"], "i=39", o6.ns["ns=isa95;i=4864"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95;i=4867", browseName="Default Binary")
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95;i=4868", browseName="ns=isa95;ISA95TestResultMeasurementDataType", dataType=o6.String, value="ISA95TestResultMeasurementDataType"
)
o6.reference(o6.ns["ns=isa95;i=4867"], "i=39", o6.ns["ns=isa95;i=4868"])
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4872",
    browseName="EnumStrings",
    modellingRule="Mandatory",
    parent="ns=isa95;i=4871",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[15],
    value=[
        o6.LocalizedText("Enterprise", "\n          "),
        o6.LocalizedText("Site", "\n          "),
        o6.LocalizedText("Area", "\n          "),
        o6.LocalizedText("ProcessCell", "\n          "),
        o6.LocalizedText("Unit", "\n          "),
        o6.LocalizedText("ProductionLine", "\n          "),
        o6.LocalizedText("WorkCell", "\n          "),
        o6.LocalizedText("ProductionUnit", "\n          "),
        o6.LocalizedText("StorageZone", "\n          "),
        o6.LocalizedText("StorageUnit", "\n          "),
        o6.LocalizedText("WorkCenter", "\n          "),
        o6.LocalizedText("WorkUnit", "\n          "),
        o6.LocalizedText("EquipmentModule", "\n          "),
        o6.LocalizedText("ControlModule", "\n          "),
        o6.LocalizedText("Other", "\n          "),
    ],
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95;i=4894", browseName="Default XML")
o6.hasEncoding(isa95_datypes.ISA95TestResultDataType, o6.ns["ns=isa95;i=4894"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95;i=4896", browseName="ns=isa95;ISA95TestResultDataType", dataType=o6.String, value="//xs:element[@name='ISA95TestResultDataType']"
)
o6.reference(o6.ns["ns=isa95;i=4894"], "i=39", o6.ns["ns=isa95;i=4896"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95;i=4902", browseName="Default Binary")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=isa95;i=4904", browseName="ns=isa95;ISA95TestResultDataType", dataType=o6.String, value="ISA95TestResultDataType")
o6.reference(o6.ns["ns=isa95;i=4902"], "i=39", o6.ns["ns=isa95;i=4904"])
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4930",
    browseName="ns=isa95;MimeContentType",
    modellingRule="Optional",
    parent="ns=isa95;i=4798",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4931",
    browseName="ns=isa95;MIMEListId",
    modellingRule="Optional",
    parent="ns=isa95;i=4798",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4932",
    browseName="ns=isa95;MIMEListAgencyId",
    modellingRule="Optional",
    parent="ns=isa95;i=4798",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4933",
    browseName="ns=isa95;MIMEListVersionId",
    modellingRule="Optional",
    parent="ns=isa95;i=4798",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4934",
    browseName="ns=isa95;CharacterSetListId",
    modellingRule="Optional",
    parent="ns=isa95;i=4798",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4935",
    browseName="ns=isa95;CharacterSetListAgencyId",
    modellingRule="Optional",
    parent="ns=isa95;i=4798",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4936",
    browseName="ns=isa95;CharacterSetListVersionId",
    modellingRule="Optional",
    parent="ns=isa95;i=4798",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4937",
    browseName="ns=isa95;EncodingListId",
    modellingRule="Optional",
    parent="ns=isa95;i=4798",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4938",
    browseName="ns=isa95;EncodingListAgencyId",
    modellingRule="Optional",
    parent="ns=isa95;i=4798",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4939",
    browseName="ns=isa95;EncodingListVersionId",
    modellingRule="Optional",
    parent="ns=isa95;i=4798",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4940",
    browseName="ns=isa95;MimeContentType",
    modellingRule="Optional",
    parent="ns=isa95;i=4806",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4941",
    browseName="ns=isa95;MIMEListId",
    modellingRule="Optional",
    parent="ns=isa95;i=4806",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4942",
    browseName="ns=isa95;MIMEListAgencyId",
    modellingRule="Optional",
    parent="ns=isa95;i=4806",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4943",
    browseName="ns=isa95;MIMEListVersionId",
    modellingRule="Optional",
    parent="ns=isa95;i=4806",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4944",
    browseName="ns=isa95;MimeContentType",
    modellingRule="Optional",
    parent="ns=isa95;i=4822",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4945",
    browseName="ns=isa95;MIMEListId",
    modellingRule="Optional",
    parent="ns=isa95;i=4822",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4946",
    browseName="ns=isa95;MIMEListAgencyId",
    modellingRule="Optional",
    parent="ns=isa95;i=4822",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4947",
    browseName="ns=isa95;MIMEListVersionId",
    modellingRule="Optional",
    parent="ns=isa95;i=4822",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4948",
    browseName="ns=isa95;MimeContentType",
    modellingRule="Optional",
    parent="ns=isa95;i=4853",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4949",
    browseName="ns=isa95;MIMEListId",
    modellingRule="Optional",
    parent="ns=isa95;i=4853",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4950",
    browseName="ns=isa95;MIMEListAgencyId",
    modellingRule="Optional",
    parent="ns=isa95;i=4853",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4951",
    browseName="ns=isa95;MIMEListVersionId",
    modellingRule="Optional",
    parent="ns=isa95;i=4853",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4952",
    browseName="ns=isa95;MimeContentType",
    modellingRule="Optional",
    parent="ns=isa95;i=4856",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4953",
    browseName="ns=isa95;MIMEListId",
    modellingRule="Optional",
    parent="ns=isa95;i=4856",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4954",
    browseName="ns=isa95;MIMEListAgencyId",
    modellingRule="Optional",
    parent="ns=isa95;i=4856",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.vartypes.PropertyType(
    nodeId="ns=isa95;i=4955",
    browseName="ns=isa95;MIMEListVersionId",
    modellingRule="Optional",
    parent="ns=isa95;i=4856",
    referenceType=isa95_reftypes.HasCDTSupplemental,
    dataType=o6.String,
    accessLevel=3,
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95;i=4969", browseName="Default XML")
o6.hasEncoding(isa95_datypes.ISA95AssetAssignmentDataType, o6.ns["ns=isa95;i=4969"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=isa95;i=4970", browseName="ns=isa95;ISA95AssetAssignmentDataType", dataType=o6.String, value="//xs:element[@name='ISA95AssetAssignmentDataType']"
)
o6.reference(o6.ns["ns=isa95;i=4969"], "i=39", o6.ns["ns=isa95;i=4970"])
opcDotISA95 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=isa95;i=4759",
    browseName="ns=isa95;Opc.ISA95",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=isa95;i=4761",
                browseName="NamespaceUri",
                description="A URI that uniquely identifies the dictionary.",
                dataType=o6.String,
                value="http://www.OPCFoundation.org/UA/2013/01/ISA95",
            )
        ),
        o6.hasComponent(o6.ns["ns=isa95;i=4785"]),
        o6.hasComponent(o6.ns["ns=isa95;i=4864"]),
        o6.hasComponent(o6.ns["ns=isa95;i=4896"]),
        o6.hasComponent(o6.ns["ns=isa95;i=4970"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema \r\n  xmlns:xs="http://www.w3.org/2001/XMLSchema"\r\n  xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" \r\n  xmlns:tns="http://www.OPCFoundation.org/UA/2013/01/ISA95" \r\n  targetNamespace="http://www.OPCFoundation.org/UA/2013/01/ISA95" \r\n  elementFormDefault="qualified"\r\n>\r\n  <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd" />\r\n  \r\n  <xs:element name="DecimalString" type="xs:string" />\r\n\r\n  <xs:element name="DateString" type="xs:string" />\r\n\r\n  <xs:element name="TimeString" type="xs:string" />\r\n\r\n  <xs:element name="DurationString" type="xs:string" />\r\n\r\n  <xs:element name="NormalizedString" type="xs:string" />\r\n\r\n  <xs:element name="Decimal" type="xs:base64Binary" />\r\n\r\n  <xs:complexType name="CurrencyCode">\r\n  \t<xs:sequence>\r\n      <xs:element name="namespaceUri" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="unitId" type="xs:int" minOccurs="0" />\r\n      <xs:element name="charId" type="ua:ListOfByte" minOccurs="0" nillable="true" />\r\n      <xs:element name="displayName" type="ua:LocalizedText" minOccurs="0" nillable="true" />\r\n      <xs:element name="Description" type="ua:LocalizedText" minOccurs="0" nillable="true" />\r\n  \t</xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="CurrencyCode" type="tns:CurrencyCode" />\r\n\r\n  <xs:complexType name="ListOfCurrencyCode">\r\n    <xs:sequence>\r\n      <xs:element name="CurrencyCode" type="tns:CurrencyCode" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfCurrencyCode" type="tns:ListOfCurrencyCode" nillable="true"></xs:element>\r\n\r\n  <xs:element name="CDTAmountDecimal" type="xs:base64Binary" />\r\n\r\n  <xs:element name="CDTBinaryObject" type="xs:base64Binary" />\r\n\r\n  <xs:element name="CDTCode" type="xs:string" />\r\n\r\n  <xs:element name="CDTDateTime" type="xs:dateTime" />\r\n\r\n  <xs:element name="CDTGraphic" type="xs:base64Binary" />\r\n\r\n  <xs:element name="CDTIdentifier" type="xs:string" />\r\n\r\n  <xs:element name="CDTMeasureDecimal" type="xs:base64Binary" />\r\n\r\n  <xs:element name="CDTMeasureDouble" type="xs:double" />\r\n\r\n  <xs:element name="CDTMeasureFloat" type="xs:float" />\r\n\r\n  <xs:element name="CDTMeasureInt16" type="xs:short" />\r\n\r\n  <xs:element name="CDTMeasureInt32" type="xs:int" />\r\n\r\n  <xs:element name="CDTMeasureInt64" type="xs:long" />\r\n\r\n  <xs:element name="CDTOrdinal" type="xs:int" />\r\n\r\n  <xs:element name="CDTPicture" type="xs:base64Binary" />\r\n\r\n  <xs:element name="CDTRateDecimal" type="xs:base64Binary" />\r\n\r\n  <xs:element name="CDTRateDouble" type="xs:double" />\r\n\r\n  <xs:element name="CDTRateFloat" type="xs:float" />\r\n\r\n  <xs:element name="CDTRateInt32" type="xs:int" />\r\n\r\n  <xs:element name="CDTSound" type="xs:base64Binary" />\r\n\r\n  <xs:element name="CDTVideo" type="xs:base64Binary" />\r\n\r\n  <xs:simpleType  name="ISA95EquipmentElementLevelEnum">\r\n    <xs:restriction base="xs:string">\r\n      <xs:enumeration value="Enterprise_0" />\r\n      <xs:enumeration value="Site_1" />\r\n      <xs:enumeration value="Area_2" />\r\n      <xs:enumeration value="ProcessCell_3" />\r\n      <xs:enumeration value="Unit_4" />\r\n      <xs:enumeration value="ProductionLine_5" />\r\n      <xs:enumeration value="WorkCell_6" />\r\n      <xs:enumeration value="ProductionUnit_7" />\r\n      <xs:enumeration value="StorageZone_8" />\r\n      <xs:enumeration value="StorageUnit_9" />\r\n      <xs:enumeration value="WorkCenter_10" />\r\n      <xs:enumeration value="WorkUnit_11" />\r\n      <xs:enumeration value="EquipmentModule_12" />\r\n      <xs:enumeration value="ControlModule_13" />\r\n      <xs:enumeration value="Other_14" />\r\n    </xs:restriction>\r\n  </xs:simpleType>\r\n  <xs:element name="ISA95EquipmentElementLevelEnum" type="tns:ISA95EquipmentElementLevelEnum" />\r\n\r\n  <xs:complexType name="ListOfISA95EquipmentElementLevelEnum">\r\n    <xs:sequence>\r\n      <xs:element name="ISA95EquipmentElementLevelEnum" type="tns:ISA95EquipmentElementLevelEnum" minOccurs="0" maxOccurs="unbounded" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfISA95EquipmentElementLevelEnum" type="tns:ListOfISA95EquipmentElementLevelEnum" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="ISA95TestResultMeasurementDataType">\r\n  \t<xs:sequence>\r\n      <xs:element name="Id" type="ua:NodeId" minOccurs="0" nillable="true" />\r\n      <xs:element name="TestResultDescription" type="ua:LocalizedText" minOccurs="0" nillable="true" />\r\n      <xs:element name="Date" type="xs:dateTime" minOccurs="0" />\r\n      <xs:element name="Result" type="ua:Variant" minOccurs="0" />\r\n      <xs:element name="ResultUnitOfMeasure" type="ua:EUInformation" minOccurs="0" nillable="true" />\r\n      <xs:element name="Expiration" type="xs:dateTime" minOccurs="0" />\r\n  \t</xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ISA95TestResultMeasurementDataType" type="tns:ISA95TestResultMeasurementDataType" />\r\n\r\n  <xs:complexType name="ListOfISA95TestResultMeasurementDataType">\r\n    <xs:sequence>\r\n      <xs:element name="ISA95TestResultMeasurementDataType" type="tns:ISA95TestResultMeasurementDataType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfISA95TestResultMeasurementDataType" type="tns:ListOfISA95TestResultMeasurementDataType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="ISA95TestResultDataType">\r\n  \t<xs:sequence>\r\n      <xs:element name="Id" type="ua:NodeId" minOccurs="0" nillable="true" />\r\n      <xs:element name="TestResultDescription" type="ua:LocalizedText" minOccurs="0" nillable="true" />\r\n      <xs:element name="Date" type="xs:dateTime" minOccurs="0" />\r\n      <xs:element name="Result" type="ua:Variant" minOccurs="0" />\r\n      <xs:element name="ResultUnitOfMeasure" type="xs:string" minOccurs="0" nillable="true" />\r\n      <xs:element name="Expiration" type="xs:dateTime" minOccurs="0" />\r\n  \t</xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ISA95TestResultDataType" type="tns:ISA95TestResultDataType" />\r\n\r\n  <xs:complexType name="ListOfISA95TestResultDataType">\r\n    <xs:sequence>\r\n      <xs:element name="ISA95TestResultDataType" type="tns:ISA95TestResultDataType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfISA95TestResultDataType" type="tns:ListOfISA95TestResultDataType" nillable="true"></xs:element>\r\n\r\n  <xs:complexType name="ISA95AssetAssignmentDataType">\r\n  \t<xs:sequence>\r\n      <xs:element name="Id" type="ua:NodeId" minOccurs="0" nillable="true" />\r\n      <xs:element name="AssinmentDescription" type="ua:LocalizedText" minOccurs="0" nillable="true" />\r\n      <xs:element name="StartTime" type="xs:dateTime" minOccurs="0" />\r\n      <xs:element name="EndTime" type="xs:dateTime" minOccurs="0" />\r\n  \t</xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ISA95AssetAssignmentDataType" type="tns:ISA95AssetAssignmentDataType" />\r\n\r\n  <xs:complexType name="ListOfISA95AssetAssignmentDataType">\r\n    <xs:sequence>\r\n      <xs:element name="ISA95AssetAssignmentDataType" type="tns:ISA95AssetAssignmentDataType" minOccurs="0" maxOccurs="unbounded" nillable="true" />\r\n    </xs:sequence>\r\n  </xs:complexType>\r\n  <xs:element name="ListOfISA95AssetAssignmentDataType" type="tns:ListOfISA95AssetAssignmentDataType" nillable="true"></xs:element>\r\n  \r\n</xs:schema>',
)
ns0.objtypes.DataTypeEncodingType(nodeId="ns=isa95;i=4973", browseName="Default Binary")
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=isa95;i=4974", browseName="ns=isa95;ISA95AssetAssignmentDataType", dataType=o6.String, value="ISA95AssetAssignmentDataType")
o6.reference(o6.ns["ns=isa95;i=4973"], "i=39", o6.ns["ns=isa95;i=4974"])
opcDotISA95_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=isa95;i=4765",
    browseName="ns=isa95;Opc.ISA95",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=isa95;i=4767",
                browseName="NamespaceUri",
                description="A URI that uniquely identifies the dictionary.",
                dataType=o6.String,
                value="http://www.OPCFoundation.org/UA/2013/01/ISA95",
            )
        ),
        o6.hasComponent(o6.ns["ns=isa95;i=4789"]),
        o6.hasComponent(o6.ns["ns=isa95;i=4868"]),
        o6.hasComponent(o6.ns["ns=isa95;i=4904"]),
        o6.hasComponent(o6.ns["ns=isa95;i=4974"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary\r\n  xmlns:opc="http://opcfoundation.org/BinarySchema/"\r\n  xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.bsd"\r\n  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\r\n  xmlns:tns="http://www.OPCFoundation.org/UA/2013/01/ISA95"\r\n  DefaultByteOrder="LittleEndian"\r\n  TargetNamespace="http://www.OPCFoundation.org/UA/2013/01/ISA95"  \r\n>\r\n  <opc:Import Namespace="http://opcfoundation.org/UA/" Location="Opc.Ua.BinarySchema.bsd"/>\r\n  \r\n  <opc:OpaqueType Name="DecimalString">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="DateString">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="TimeString">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="DurationString">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="NormalizedString">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="Decimal">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:StructuredType Name="CurrencyCode" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="namespaceUri" TypeName="opc:String" />\r\n    <opc:Field Name="unitId" TypeName="opc:Int32" />\r\n    <opc:Field Name="NoOfcharId" TypeName="opc:Int32" />\r\n    <opc:Field Name="charId" TypeName="opc:Byte" LengthField="NoOfcharId" />\r\n    <opc:Field Name="displayName" TypeName="ua:LocalizedText" />\r\n    <opc:Field Name="Description" TypeName="ua:LocalizedText" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:OpaqueType Name="CDTAmountDecimal">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="CDTBinaryObject">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="CDTCode">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="CDTDateTime">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="CDTGraphic">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="CDTIdentifier">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="CDTMeasureDecimal">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="CDTMeasureDouble">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="CDTMeasureFloat">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="CDTMeasureInt16">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="CDTMeasureInt32">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="CDTMeasureInt64">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="CDTOrdinal">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="CDTPicture">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="CDTRateDecimal">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="CDTRateDouble">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="CDTRateFloat">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="CDTRateInt32">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="CDTSound">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:OpaqueType Name="CDTVideo">\r\n  </opc:OpaqueType>\r\n\r\n  <opc:EnumeratedType Name="ISA95EquipmentElementLevelEnum" LengthInBits="32">\r\n    <opc:EnumeratedValue Name="Enterprise" Value="0" />\r\n    <opc:EnumeratedValue Name="Site" Value="1" />\r\n    <opc:EnumeratedValue Name="Area" Value="2" />\r\n    <opc:EnumeratedValue Name="ProcessCell" Value="3" />\r\n    <opc:EnumeratedValue Name="Unit" Value="4" />\r\n    <opc:EnumeratedValue Name="ProductionLine" Value="5" />\r\n    <opc:EnumeratedValue Name="WorkCell" Value="6" />\r\n    <opc:EnumeratedValue Name="ProductionUnit" Value="7" />\r\n    <opc:EnumeratedValue Name="StorageZone" Value="8" />\r\n    <opc:EnumeratedValue Name="StorageUnit" Value="9" />\r\n    <opc:EnumeratedValue Name="WorkCenter" Value="10" />\r\n    <opc:EnumeratedValue Name="WorkUnit" Value="11" />\r\n    <opc:EnumeratedValue Name="EquipmentModule" Value="12" />\r\n    <opc:EnumeratedValue Name="ControlModule" Value="13" />\r\n    <opc:EnumeratedValue Name="Other" Value="14" />\r\n  </opc:EnumeratedType>\r\n\r\n  <opc:StructuredType Name="ISA95TestResultMeasurementDataType" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="Id" TypeName="ua:NodeId" />\r\n    <opc:Field Name="TestResultDescription" TypeName="ua:LocalizedText" />\r\n    <opc:Field Name="Date" TypeName="opc:DateTime" />\r\n    <opc:Field Name="Result" TypeName="ua:Variant" />\r\n    <opc:Field Name="ResultUnitOfMeasure" TypeName="ua:EUInformation" />\r\n    <opc:Field Name="Expiration" TypeName="opc:DateTime" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="ISA95TestResultDataType" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="Id" TypeName="ua:NodeId" />\r\n    <opc:Field Name="TestResultDescription" TypeName="ua:LocalizedText" />\r\n    <opc:Field Name="Date" TypeName="opc:DateTime" />\r\n    <opc:Field Name="Result" TypeName="ua:Variant" />\r\n    <opc:Field Name="ResultUnitOfMeasure" TypeName="opc:String" />\r\n    <opc:Field Name="Expiration" TypeName="opc:DateTime" />\r\n  </opc:StructuredType>\r\n\r\n  <opc:StructuredType Name="ISA95AssetAssignmentDataType" BaseType="ua:ExtensionObject">\r\n    <opc:Field Name="Id" TypeName="ua:NodeId" />\r\n    <opc:Field Name="AssinmentDescription" TypeName="ua:LocalizedText" />\r\n    <opc:Field Name="StartTime" TypeName="opc:DateTime" />\r\n    <opc:Field Name="EndTime" TypeName="opc:DateTime" />\r\n  </opc:StructuredType>\r\n  \r\n</opc:TypeDictionary>',
)
isa95_vartypes.PersonnelClassPropertyType(nodeId="ns=isa95;i=4979", browseName="ns=isa95;<PropertyName>", modellingRule="OptionalPlaceholder")
o6.reference(isa95_vartypes.PersonnelClassPropertyType, isa95_reftypes.HasISA95ClassProperty, o6.ns["ns=isa95;i=4979"])
langleTestSpecificationRangle = isa95_objtypes.QualificationTestSpecificationType(
    nodeId="ns=isa95;i=4981",
    browseName="ns=isa95;<TestSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=4982", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713")],
)
o6.reference(isa95_vartypes.PersonnelClassPropertyType, "ns=isa95;i=4918", "ns=isa95;i=4981")
langleTestSpecificationRangle_2 = isa95_objtypes.QualificationTestSpecificationType(
    nodeId="ns=isa95;i=4999",
    browseName="ns=isa95;<TestSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5000", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713")],
)
o6.reference(isa95_objtypes.PersonnelClassType, "ns=isa95;i=4918", "ns=isa95;i=4999")
isa95_vartypes.EquipmentClassPropertyType(nodeId="ns=isa95;i=5019", browseName="ns=isa95;<PropertyName>", modellingRule="OptionalPlaceholder")
o6.reference(isa95_vartypes.EquipmentClassPropertyType, isa95_reftypes.HasISA95ClassProperty, o6.ns["ns=isa95;i=5019"])
langleTestSpecificationRangle_3 = isa95_objtypes.EquipmentCapabilityTestSpecificationType(
    nodeId="ns=isa95;i=5021",
    browseName="ns=isa95;<TestSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5022", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713")],
)
o6.reference(isa95_vartypes.EquipmentClassPropertyType, "ns=isa95;i=4920", "ns=isa95;i=5021")
isa95_vartypes.EquipmentPropertyType(nodeId="ns=isa95;i=5023", browseName="ns=isa95;<PropertyName>", modellingRule="OptionalPlaceholder")
o6.reference(isa95_vartypes.EquipmentPropertyType, isa95_reftypes.HasISA95Property, o6.ns["ns=isa95;i=5023"])
langleTestSpecificationRangle_4 = isa95_objtypes.EquipmentCapabilityTestSpecificationType(
    nodeId="ns=isa95;i=5025",
    browseName="ns=isa95;<TestSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5026", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713")],
)
o6.reference(isa95_vartypes.EquipmentPropertyType, "ns=isa95;i=4920", "ns=isa95;i=5025")
isa95_vartypes.EquipmentCapabilityTestResultType(
    nodeId="ns=isa95;i=5027",
    browseName="ns=isa95;<TestResult>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5028", browseName="ns=isa95;Id", dataType=o6.NodeId, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5029", browseName="ns=isa95;ResultDescription", dataType=o6.LocalizedText, accessLevel=3), "ns=isa95;i=4713"
        ),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5030", browseName="ns=isa95;TestDate", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5031", browseName="ns=isa95;Result", accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5032", browseName="ns=isa95;ResultUnitOfMeasure", accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5033", browseName="ns=isa95;Expiration", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
    ],
    dataType=ns0.datatypes.Structure,
)
o6.reference(isa95_vartypes.EquipmentPropertyType, isa95_reftypes.HasTestResult, o6.ns["ns=isa95;i=5027"])
langleTestSpecificationRangle_5 = isa95_objtypes.EquipmentCapabilityTestSpecificationType(
    nodeId="ns=isa95;i=5037",
    browseName="ns=isa95;<TestSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5038", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713")],
)
o6.reference(isa95_objtypes.EquipmentClassType, "ns=isa95;i=4920", "ns=isa95;i=5037")
langleEquipmentClassRangle = isa95_objtypes.EquipmentClassType(nodeId="ns=isa95;i=5043", browseName="ns=isa95;<EquipmentClass>", modellingRule="OptionalPlaceholder")
o6.reference(isa95_objtypes.EquipmentType, "ns=isa95;i=4919", "ns=isa95;i=5043")
langleTestSpecificationRangle_6 = isa95_objtypes.EquipmentCapabilityTestSpecificationType(
    nodeId="ns=isa95;i=5045",
    browseName="ns=isa95;<TestSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5046", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713")],
)
o6.reference(isa95_objtypes.EquipmentType, "ns=isa95;i=4920", "ns=isa95;i=5045")
isa95_vartypes.PhysicalAssetClassPropertyType(nodeId="ns=isa95;i=5061", browseName="ns=isa95;<PropertyName>", modellingRule="OptionalPlaceholder")
o6.reference(isa95_vartypes.PhysicalAssetClassPropertyType, isa95_reftypes.HasISA95ClassProperty, o6.ns["ns=isa95;i=5061"])
langleTestSpecificationRangle_7 = isa95_objtypes.PhysicalAssetCapabilityTestSpecificationType(
    nodeId="ns=isa95;i=5063",
    browseName="ns=isa95;<TestSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5064", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713")],
)
o6.reference(isa95_vartypes.PhysicalAssetClassPropertyType, "ns=isa95;i=4922", "ns=isa95;i=5063")
isa95_vartypes.PhysicalAssetPropertyType(nodeId="ns=isa95;i=5067", browseName="ns=isa95;<PropertyName>", modellingRule="OptionalPlaceholder")
o6.reference(isa95_vartypes.PhysicalAssetPropertyType, isa95_reftypes.HasISA95Property, o6.ns["ns=isa95;i=5067"])
langleTestSpecificationRangle_8 = isa95_objtypes.PhysicalAssetCapabilityTestSpecificationType(
    nodeId="ns=isa95;i=5069",
    browseName="ns=isa95;<TestSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5070", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713")],
)
o6.reference(isa95_vartypes.PhysicalAssetPropertyType, "ns=isa95;i=4922", "ns=isa95;i=5069")
isa95_vartypes.PhysicalAssetCapabilityTestResultType(
    nodeId="ns=isa95;i=5071",
    browseName="ns=isa95;<TestResult>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5072", browseName="ns=isa95;Id", dataType=o6.NodeId, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5073", browseName="ns=isa95;ResultDescription", dataType=o6.LocalizedText, accessLevel=3), "ns=isa95;i=4713"
        ),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5074", browseName="ns=isa95;TestDate", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5075", browseName="ns=isa95;Result", accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5076", browseName="ns=isa95;ResultUnitOfMeasure", accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5077", browseName="ns=isa95;Expiration", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
    ],
    dataType=ns0.datatypes.Structure,
)
o6.reference(isa95_vartypes.PhysicalAssetPropertyType, isa95_reftypes.HasTestResult, o6.ns["ns=isa95;i=5071"])
langleTestSpecificationRangle_9 = isa95_objtypes.PhysicalAssetCapabilityTestSpecificationType(
    nodeId="ns=isa95;i=5081",
    browseName="ns=isa95;<TestSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5082", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713")],
)
o6.reference(isa95_objtypes.PhysicalAssetClassType, "ns=isa95;i=4922", "ns=isa95;i=5081")
physicalAssetClass = isa95_objtypes.PhysicalAssetClassType(nodeId="ns=isa95;i=5088", browseName="ns=isa95;PhysicalAssetClass", modellingRule="Optional")
o6.reference(isa95_objtypes.PhysicalAssetType, "ns=isa95;i=4921", "ns=isa95;i=5088")
langleTestSpecificationRangle_10 = isa95_objtypes.PhysicalAssetCapabilityTestSpecificationType(
    nodeId="ns=isa95;i=5091",
    browseName="ns=isa95;<TestSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5092", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713")],
)
o6.reference(isa95_objtypes.PhysicalAssetType, "ns=isa95;i=4922", "ns=isa95;i=5091")
langlePhysicalAssetRangle = isa95_objtypes.PhysicalAssetType(nodeId="ns=isa95;i=5093", browseName="ns=isa95;<PhysicalAsset>", modellingRule="Optional")
o6.reference(isa95_objtypes.EquipmentType, "ns=isa95;i=4914", "ns=isa95;i=5093")
isa95_vartypes.PersonPropertyType(nodeId="ns=isa95;i=5120", browseName="ns=isa95;<PropertyName>", modellingRule="OptionalPlaceholder")
o6.reference(isa95_vartypes.PersonPropertyType, isa95_reftypes.HasISA95Property, o6.ns["ns=isa95;i=5120"])
langleTestSpecificationRangle_11 = isa95_objtypes.QualificationTestSpecificationType(
    nodeId="ns=isa95;i=5122",
    browseName="ns=isa95;<TestSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5123", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713")],
)
o6.reference(isa95_vartypes.PersonPropertyType, "ns=isa95;i=4918", "ns=isa95;i=5122")
isa95_vartypes.QualificationTestResultType(
    nodeId="ns=isa95;i=5124",
    browseName="ns=isa95;<TestResult>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5125", browseName="ns=isa95;Id", dataType=o6.NodeId, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5126", browseName="ns=isa95;ResultDescription", dataType=o6.LocalizedText, accessLevel=3), "ns=isa95;i=4713"
        ),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5127", browseName="ns=isa95;TestDate", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5128", browseName="ns=isa95;Result", accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5129", browseName="ns=isa95;ResultUnitOfMeasure", accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5130", browseName="ns=isa95;Expiration", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
    ],
    dataType=ns0.datatypes.Structure,
)
o6.reference(isa95_vartypes.PersonPropertyType, isa95_reftypes.HasTestResult, o6.ns["ns=isa95;i=5124"])
langleTestSpecificationRangle_12 = isa95_objtypes.QualificationTestSpecificationType(
    nodeId="ns=isa95;i=5134",
    browseName="ns=isa95;<TestSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5135", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713")],
)
o6.reference(isa95_objtypes.PersonType, "ns=isa95;i=4918", "ns=isa95;i=5134")
langlePhysicalAssetRangle_2 = isa95_objtypes.PhysicalAssetType(nodeId="ns=isa95;i=5146", browseName="ns=isa95;<PhysicalAsset>", modellingRule="Optional")
physicalAssetClass_2 = isa95_objtypes.PhysicalAssetClassType(nodeId="ns=isa95;i=5148", browseName="ns=isa95;PhysicalAssetClass", modellingRule="Optional")
isa95_vartypes.MaterialDefinitionPropertyType(nodeId="ns=isa95;i=5176", browseName="ns=isa95;<PropertyName>", modellingRule="OptionalPlaceholder")
o6.reference(isa95_vartypes.MaterialDefinitionPropertyType, isa95_reftypes.HasISA95ClassProperty, o6.ns["ns=isa95;i=5176"])
langleTestSpecificationRangle_13 = isa95_objtypes.MaterialTestSpecificationType(
    nodeId="ns=isa95;i=5178",
    browseName="ns=isa95;<TestSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5179", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713")],
)
o6.reference(isa95_vartypes.MaterialDefinitionPropertyType, "ns=isa95;i=4924", "ns=isa95;i=5178")
isa95_vartypes.MaterialClassPropertyType(nodeId="ns=isa95;i=5182", browseName="ns=isa95;<PropertyName>", modellingRule="OptionalPlaceholder")
o6.reference(isa95_vartypes.MaterialClassPropertyType, isa95_reftypes.HasISA95ClassProperty, o6.ns["ns=isa95;i=5182"])
langleTestSpecificationRangle_14 = isa95_objtypes.MaterialTestSpecificationType(
    nodeId="ns=isa95;i=5184",
    browseName="ns=isa95;<TestSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5185", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713")],
)
o6.reference(isa95_vartypes.MaterialClassPropertyType, "ns=isa95;i=4924", "ns=isa95;i=5184")
isa95_vartypes.MaterialLotPropertyType(
    nodeId="ns=isa95;i=5193",
    browseName="ns=isa95;<TestResult>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5194", browseName="ns=isa95;Id", dataType=o6.NodeId, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5195", browseName="ns=isa95;ResultDescription", dataType=o6.LocalizedText, accessLevel=3), "ns=isa95;i=4713"
        ),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5196", browseName="ns=isa95;TestDate", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5197", browseName="ns=isa95;Result", accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5198", browseName="ns=isa95;ResultUnitOfMeasure", accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5199", browseName="ns=isa95;Expiration", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
    ],
    dataType=ns0.datatypes.Structure,
)
o6.reference(isa95_vartypes.MaterialLotPropertyType, isa95_reftypes.HasTestResult, o6.ns["ns=isa95;i=5193"])
isa95_vartypes.MaterialLotPropertyType(
    nodeId="ns=isa95;i=5200",
    browseName="ns=isa95;<PropertyName>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5201", browseName="ns=isa95;Id", dataType=o6.NodeId, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5202", browseName="ns=isa95;ResultDescription", dataType=o6.LocalizedText, accessLevel=3), "ns=isa95;i=4713"
        ),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5203", browseName="ns=isa95;TestDate", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5204", browseName="ns=isa95;Result", accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5205", browseName="ns=isa95;ResultUnitOfMeasure", accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5206", browseName="ns=isa95;Expiration", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
    ],
    dataType=ns0.datatypes.Structure,
)
o6.reference(isa95_vartypes.MaterialLotPropertyType, isa95_reftypes.HasISA95Property, o6.ns["ns=isa95;i=5200"])
langleTestSpecificationRangle_15 = isa95_objtypes.MaterialTestSpecificationType(
    nodeId="ns=isa95;i=5207",
    browseName="ns=isa95;<TestSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5208", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713")],
)
o6.reference(isa95_vartypes.MaterialLotPropertyType, "ns=isa95;i=4924", "ns=isa95;i=5207")
langleTestSpecificationRangle_16 = isa95_objtypes.MaterialTestSpecificationType(
    nodeId="ns=isa95;i=5212",
    browseName="ns=isa95;<TestSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5213", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713")],
)
o6.reference(isa95_objtypes.MaterialClassType, "ns=isa95;i=4924", "ns=isa95;i=5212")
isa95_objtypes.MaterialClassType(
    nodeId="ns=isa95;i=5214",
    browseName="ns=isa95;<AssemblyClass>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5215", browseName="ns=isa95;AssemblyType"), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5216", browseName="ns=isa95;AssemblyRelationship"), "ns=isa95;i=4713"),
    ],
)
o6.reference(isa95_objtypes.MaterialClassType, isa95_reftypes.AssembledFromClass, o6.ns["ns=isa95;i=5214"])
langleTestSpecificationRangle_17 = isa95_objtypes.MaterialTestSpecificationType(
    nodeId="ns=isa95;i=5222",
    browseName="ns=isa95;<TestSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5223", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713")],
)
o6.reference(isa95_objtypes.MaterialDefinitionType, "ns=isa95;i=4924", "ns=isa95;i=5222")
langleMaterialClassRangle = isa95_objtypes.MaterialClassType(nodeId="ns=isa95;i=5224", browseName="ns=isa95;<MaterialClass>", modellingRule="OptionalPlaceholder")
isa95_objtypes.MaterialDefinitionType(
    nodeId="ns=isa95;i=5227",
    browseName="ns=isa95;<AssemblyClass>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5228", browseName="ns=isa95;AssemblyType"), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5229", browseName="ns=isa95;AssemblyRelationship"), "ns=isa95;i=4713"),
    ],
)
o6.reference(isa95_objtypes.MaterialDefinitionType, isa95_reftypes.AssembledFromDefinition, o6.ns["ns=isa95;i=5227"])
isa95_vartypes.MaterialLotPropertyType(
    nodeId="ns=isa95;i=5233",
    browseName="ns=isa95;<PropertyName>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5234", browseName="ns=isa95;Id", dataType=o6.NodeId, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5235", browseName="ns=isa95;ResultDescription", dataType=o6.LocalizedText, accessLevel=3), "ns=isa95;i=4713"
        ),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5236", browseName="ns=isa95;TestDate", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5237", browseName="ns=isa95;Result", accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5238", browseName="ns=isa95;ResultUnitOfMeasure", accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5239", browseName="ns=isa95;Expiration", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
    ],
    dataType=ns0.datatypes.Structure,
)
o6.reference(isa95_objtypes.MaterialLotType, isa95_reftypes.HasISA95Property, o6.ns["ns=isa95;i=5233"])
langleTestSpecificationRangle_18 = isa95_objtypes.MaterialTestSpecificationType(
    nodeId="ns=isa95;i=5240",
    browseName="ns=isa95;<TestSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5241", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713")],
)
o6.reference(isa95_objtypes.MaterialLotType, "ns=isa95;i=4924", "ns=isa95;i=5240")
langleMaterialDefinitionRangle = isa95_objtypes.MaterialDefinitionType(nodeId="ns=isa95;i=5242", browseName="ns=isa95;<MaterialDefinition>", modellingRule="Optional")
o6.reference(isa95_objtypes.MaterialLotType, "ns=isa95;i=5301", "ns=isa95;i=5242")
langleMaterialDefinitionRangle_2 = isa95_objtypes.MaterialDefinitionType(nodeId="ns=isa95;i=5246", browseName="ns=isa95;<MaterialDefinition>", modellingRule="Optional")
isa95_objtypes.MaterialLotType(
    nodeId="ns=isa95;i=5245",
    browseName="ns=isa95;<AssemblyLot>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5249", browseName="ns=isa95;AssemblyType"), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5250", browseName="ns=isa95;AssemblyRelationship"), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5251", browseName="ns=isa95;Status", dataType=isa95_datypes.CDTIdentifier), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5252", browseName="ns=isa95;StorageLocation", dataType=isa95_datypes.CDTIdentifier), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5253", browseName="ns=isa95;Quantity"), "ns=isa95;i=4713"),
    ],
)
o6.reference(isa95_objtypes.MaterialLotType, isa95_reftypes.AssembledFromLot, o6.ns["ns=isa95;i=5245"])
o6.reference(o6.ns["ns=isa95;i=5245"], "ns=isa95;i=5301", langleMaterialDefinitionRangle_2)
isa95_vartypes.MaterialLotPropertyType(
    nodeId="ns=isa95;i=5260",
    browseName="ns=isa95;<PropertyName>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5261", browseName="ns=isa95;Id", dataType=o6.NodeId, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5262", browseName="ns=isa95;ResultDescription", dataType=o6.LocalizedText, accessLevel=3), "ns=isa95;i=4713"
        ),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5263", browseName="ns=isa95;TestDate", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5264", browseName="ns=isa95;Result", accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5265", browseName="ns=isa95;ResultUnitOfMeasure", accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5266", browseName="ns=isa95;Expiration", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
    ],
    dataType=ns0.datatypes.Structure,
)
o6.reference(isa95_objtypes.MaterialSublotType, isa95_reftypes.HasISA95Property, o6.ns["ns=isa95;i=5260"])
langleTestSpecificationRangle_19 = isa95_objtypes.MaterialTestSpecificationType(
    nodeId="ns=isa95;i=5267",
    browseName="ns=isa95;<TestSpecification>",
    modellingRule="OptionalPlaceholder",
    references=[o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5268", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713")],
)
o6.reference(isa95_objtypes.MaterialSublotType, "ns=isa95;i=4924", "ns=isa95;i=5267")
langleAssemblySublotRangle = isa95_objtypes.MaterialSublotType(
    nodeId="ns=isa95;i=5278",
    browseName="ns=isa95;<AssemblySublot>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5279", browseName="ns=isa95;AssemblyType"), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5280", browseName="ns=isa95;AssemblyRelationship"), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5281", browseName="ns=isa95;Status", dataType=isa95_datypes.CDTIdentifier), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5282", browseName="ns=isa95;StorageLocation", dataType=isa95_datypes.CDTIdentifier), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5283", browseName="ns=isa95;Quantity"), "ns=isa95;i=4713"),
    ],
)
isa95_objtypes.MaterialSublotType(
    nodeId="ns=isa95;i=5286",
    browseName="ns=isa95;<Sublot>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5287", browseName="ns=isa95;AssemblyType"), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5288", browseName="ns=isa95;AssemblyRelationship"), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5289", browseName="ns=isa95;Status", dataType=isa95_datypes.CDTIdentifier), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5290", browseName="ns=isa95;StorageLocation", dataType=isa95_datypes.CDTIdentifier), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5291", browseName="ns=isa95;Quantity"), "ns=isa95;i=4713"),
    ],
)
o6.reference(isa95_objtypes.MaterialSublotType, isa95_reftypes.MadeUpOfMaterialSublot, o6.ns["ns=isa95;i=5286"])
langleAssemblySublotRangle_2 = isa95_objtypes.MaterialSublotType(nodeId="ns=isa95;i=5295", browseName="ns=isa95;<AssemblySublot>", modellingRule="OptionalPlaceholder")
langlePersonnelClassRangle = isa95_objtypes.PersonnelClassType(nodeId="ns=isa95;i=5302", browseName="ns=isa95;<PersonnelClass>", modellingRule="OptionalPlaceholder")
o6.reference(isa95_objtypes.PersonType, "ns=isa95;i=4917", "ns=isa95;i=5302")
isa95_vartypes.ISA95AssetAssignmentType(
    nodeId="ns=isa95;i=5303",
    browseName="ns=isa95;AssetAssignment",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5304", browseName="ns=isa95;Id", dataType=o6.NodeId, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5305", browseName="ns=isa95;AssignmentDescription", dataType=o6.LocalizedText, accessLevel=3), "ns=isa95;i=4713"
        ),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5306", browseName="ns=isa95;StartTime", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5307", browseName="ns=isa95;StopTime", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
    ],
)
isa95_objtypes.PhysicalAssetType(
    nodeId="ns=isa95;i=5136",
    browseName="ns=isa95;<PhysicalAsset>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=isa95;i=5303"]),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5151", browseName="ns=isa95;FixedAssetId", dataType=isa95_datypes.CDTIdentifier), "ns=isa95;i=4713"),
        o6.reference(isa95_vartypes.CompanyType(nodeId="ns=isa95;i=5152", browseName="ns=isa95;VendorId"), "ns=isa95;i=4713"),
        o6.reference(isa95_vartypes.GeoSpatialLocationType(nodeId="ns=isa95;i=5137", browseName="ns=isa95;PhysicalLocation", dataType=o6.String), "ns=isa95;i=5114"),
    ],
)
o6.reference(isa95_objtypes.PhysicalAssetType, isa95_reftypes.HasISA95Property, o6.ns["ns=isa95;i=5136"])
o6.reference(o6.ns["ns=isa95;i=5136"], "ns=isa95;i=4921", physicalAssetClass_2)
isa95_vartypes.ISA95AssetAssignmentType(
    nodeId="ns=isa95;i=5308",
    browseName="ns=isa95;AssetAssignment",
    modellingRule="Optional",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5309", browseName="ns=isa95;Id", dataType=o6.NodeId, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5310", browseName="ns=isa95;AssignmentDescription", dataType=o6.LocalizedText, accessLevel=3), "ns=isa95;i=4713"
        ),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5311", browseName="ns=isa95;StartTime", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5312", browseName="ns=isa95;StopTime", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
    ],
)
o6.reference(isa95_objtypes.PhysicalAssetType, ns0.reftypes.HasComponent, o6.ns["ns=isa95;i=5308"])
isa95_vartypes.ISA95AssetAssignmentType(
    nodeId="ns=isa95;i=5318",
    browseName="ns=isa95;AssetAssignment",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5319", browseName="ns=isa95;Id", dataType=o6.NodeId, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5320", browseName="ns=isa95;AssignmentDescription", dataType=o6.LocalizedText, accessLevel=3), "ns=isa95;i=4713"
        ),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5321", browseName="ns=isa95;StartTime", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5322", browseName="ns=isa95;StopTime", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
    ],
)
isa95_objtypes.EquipmentType(
    nodeId="ns=isa95;i=5144",
    browseName="ns=isa95;<Equipment>",
    modellingRule="OptionalPlaceholder",
    references=[
        o6.hasComponent(o6.ns["ns=isa95;i=5318"]),
        o6.reference(
            ns0.vartypes.PropertyType(nodeId="ns=isa95;i=5145", browseName="ns=isa95;EquipmentLevel", dataType=isa95_datypes.ISA95EquipmentElementLevelEnum), "ns=isa95;i=4713"
        ),
    ],
)
o6.reference(isa95_objtypes.EquipmentType, isa95_reftypes.MadeUpOfEquipment, o6.ns["ns=isa95;i=5144"])
o6.reference(o6.ns["ns=isa95;i=5144"], "ns=isa95;i=4914", langlePhysicalAssetRangle_2)
isa95_vartypes.ISA95AssetAssignmentType(
    nodeId="ns=isa95;i=5328",
    browseName="ns=isa95;AssetAssignment",
    modellingRule="Optional",
    references=[
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5329", browseName="ns=isa95;Id", dataType=o6.NodeId, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(
            ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5330", browseName="ns=isa95;AssignmentDescription", dataType=o6.LocalizedText, accessLevel=3), "ns=isa95;i=4713"
        ),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5331", browseName="ns=isa95;StartTime", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
        o6.reference(ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5332", browseName="ns=isa95;StopTime", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"),
    ],
)
o6.reference(isa95_objtypes.EquipmentType, ns0.reftypes.HasComponent, o6.ns["ns=isa95;i=5328"])


del Any, TYPE_CHECKING, uuid, o6, ns0, isa95_reftypes, isa95_datypes, isa95_vartypes, isa95_objtypes
