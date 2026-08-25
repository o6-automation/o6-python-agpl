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

"""Generated OPC UA wire_harness_vec namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import datatypes as wire_harness_vec_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5002", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5003", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.ARGB32ColorType, o6.ns["ns=wire_harness_vec;i=5003"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5004", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.ARGB32ColorType, o6.ns["ns=wire_harness_vec;i=5004"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5005", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5006", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.BoundingBox, o6.ns["ns=wire_harness_vec;i=5006"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5007", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.BoundingBox, o6.ns["ns=wire_harness_vec;i=5007"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5008", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5009", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.ContactPoint, o6.ns["ns=wire_harness_vec;i=5009"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5010", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.ContactPoint, o6.ns["ns=wire_harness_vec;i=5010"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5011", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5012", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.PartOccurrence, o6.ns["ns=wire_harness_vec;i=5012"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5013", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.PartOccurrence, o6.ns["ns=wire_harness_vec;i=5013"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5014", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5015", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireElementReference, o6.ns["ns=wire_harness_vec;i=5015"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5016", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireElementReference, o6.ns["ns=wire_harness_vec;i=5016"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5017", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5018", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.CoreCrimpDetail, o6.ns["ns=wire_harness_vec;i=5018"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5019", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.CoreCrimpDetail, o6.ns["ns=wire_harness_vec;i=5019"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5020", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5021", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.InsulationCrimpDetail, o6.ns["ns=wire_harness_vec;i=5021"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5022", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.InsulationCrimpDetail, o6.ns["ns=wire_harness_vec;i=5022"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5023", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5024", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.DocumentVersion, o6.ns["ns=wire_harness_vec;i=5024"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5025", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.DocumentVersion, o6.ns["ns=wire_harness_vec;i=5025"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5026", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5027", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.PartVersion, o6.ns["ns=wire_harness_vec;i=5027"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5028", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.PartVersion, o6.ns["ns=wire_harness_vec;i=5028"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5029", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5030", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.ResourceVersion, o6.ns["ns=wire_harness_vec;i=5030"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5031", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.ResourceVersion, o6.ns["ns=wire_harness_vec;i=5031"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5032", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5033", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.CavitySealRole, o6.ns["ns=wire_harness_vec;i=5033"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5034", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.CavitySealRole, o6.ns["ns=wire_harness_vec;i=5034"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5035", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5036", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.TerminalRole, o6.ns["ns=wire_harness_vec;i=5036"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5037", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.TerminalRole, o6.ns["ns=wire_harness_vec;i=5037"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5038", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5039", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.PluggableTerminalRole, o6.ns["ns=wire_harness_vec;i=5039"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5040", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.PluggableTerminalRole, o6.ns["ns=wire_harness_vec;i=5040"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5041", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5042", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireRole, o6.ns["ns=wire_harness_vec;i=5042"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5043", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireRole, o6.ns["ns=wire_harness_vec;i=5043"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5044", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5045", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.CompositionSpecification, o6.ns["ns=wire_harness_vec;i=5045"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5046", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.CompositionSpecification, o6.ns["ns=wire_harness_vec;i=5046"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5047", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5048", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.CoreSpecification, o6.ns["ns=wire_harness_vec;i=5048"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5049", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.CoreSpecification, o6.ns["ns=wire_harness_vec;i=5049"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5050", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5051", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.ContactingSpecification, o6.ns["ns=wire_harness_vec;i=5051"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5052", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.ContactingSpecification, o6.ns["ns=wire_harness_vec;i=5052"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5053", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5054", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.InsulationSpecification, o6.ns["ns=wire_harness_vec;i=5054"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5055", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.InsulationSpecification, o6.ns["ns=wire_harness_vec;i=5055"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5056", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5057", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.PartOrUsageRelatedSpecification, o6.ns["ns=wire_harness_vec;i=5057"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5058", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.PartOrUsageRelatedSpecification, o6.ns["ns=wire_harness_vec;i=5058"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5059", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5060", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.CavitySealSpecification, o6.ns["ns=wire_harness_vec;i=5060"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5061", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.CavitySealSpecification, o6.ns["ns=wire_harness_vec;i=5061"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5062", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5063", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.GeneralTechnicalPartSpecification, o6.ns["ns=wire_harness_vec;i=5063"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5064", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.GeneralTechnicalPartSpecification, o6.ns["ns=wire_harness_vec;i=5064"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5065", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5066", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.TerminalSpecification, o6.ns["ns=wire_harness_vec;i=5066"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5067", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.TerminalSpecification, o6.ns["ns=wire_harness_vec;i=5067"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5068", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5069", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.PluggableTerminalSpecification, o6.ns["ns=wire_harness_vec;i=5069"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5070", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.PluggableTerminalSpecification, o6.ns["ns=wire_harness_vec;i=5070"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5071", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5072", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireSpecification, o6.ns["ns=wire_harness_vec;i=5072"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5073", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireSpecification, o6.ns["ns=wire_harness_vec;i=5073"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5074", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5075", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireElementSpecification, o6.ns["ns=wire_harness_vec;i=5075"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5076", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireElementSpecification, o6.ns["ns=wire_harness_vec;i=5076"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5077", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5078", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireReceptionSpecification, o6.ns["ns=wire_harness_vec;i=5078"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5079", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireReceptionSpecification, o6.ns["ns=wire_harness_vec;i=5079"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5080", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5081", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.Tolerance, o6.ns["ns=wire_harness_vec;i=5081"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5082", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.Tolerance, o6.ns["ns=wire_harness_vec;i=5082"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5083", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5084", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireElement, o6.ns["ns=wire_harness_vec;i=5084"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5085", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireElement, o6.ns["ns=wire_harness_vec;i=5085"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5086", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5087", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireEnd, o6.ns["ns=wire_harness_vec;i=5087"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5088", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireEnd, o6.ns["ns=wire_harness_vec;i=5088"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5089", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5090", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireMounting, o6.ns["ns=wire_harness_vec;i=5090"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5091", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireMounting, o6.ns["ns=wire_harness_vec;i=5091"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5092", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5093", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireMountingDetail, o6.ns["ns=wire_harness_vec;i=5093"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5094", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireMountingDetail, o6.ns["ns=wire_harness_vec;i=5094"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5095", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5096", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireReception, o6.ns["ns=wire_harness_vec;i=5096"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5097", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireReception, o6.ns["ns=wire_harness_vec;i=5097"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5098", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5099", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireReceptionReference, o6.ns["ns=wire_harness_vec;i=5099"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5100", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireReceptionReference, o6.ns["ns=wire_harness_vec;i=5100"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5101", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5102", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.CavityPartRoleIdDataType, o6.ns["ns=wire_harness_vec;i=5102"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5103", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.CavityPartRoleIdDataType, o6.ns["ns=wire_harness_vec;i=5103"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5104", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5105", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.CavityPartSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5105"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5106", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.CavityPartSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5106"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5107", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5108", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.CavitySealRoleIdDataType, o6.ns["ns=wire_harness_vec;i=5108"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5109", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.CavitySealRoleIdDataType, o6.ns["ns=wire_harness_vec;i=5109"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5110", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5111", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.CavitySealSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5111"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5112", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.CavitySealSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5112"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5113", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5114", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.CompositionSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5114"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5115", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.CompositionSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5115"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5116", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5117", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.ConductorSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5117"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5118", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.ConductorSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5118"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5119", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5120", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.ConfigurableElementIdDataType, o6.ns["ns=wire_harness_vec;i=5120"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5121", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.ConfigurableElementIdDataType, o6.ns["ns=wire_harness_vec;i=5121"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5122", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5123", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.ContactingSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5123"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5124", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.ContactingSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5124"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5125", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5126", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.ContactPointIdDataType, o6.ns["ns=wire_harness_vec;i=5126"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5127", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.ContactPointIdDataType, o6.ns["ns=wire_harness_vec;i=5127"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5128", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5129", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.CoreCrimpDetailIdDataType, o6.ns["ns=wire_harness_vec;i=5129"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5130", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.CoreCrimpDetailIdDataType, o6.ns["ns=wire_harness_vec;i=5130"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5131", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5132", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.CoreSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5132"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5133", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.CoreSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5133"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5134", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5135", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.CrimpDetailIdDataType, o6.ns["ns=wire_harness_vec;i=5135"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5136", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.CrimpDetailIdDataType, o6.ns["ns=wire_harness_vec;i=5136"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5137", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5138", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.DocumentVersionIdDataType, o6.ns["ns=wire_harness_vec;i=5138"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5139", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.DocumentVersionIdDataType, o6.ns["ns=wire_harness_vec;i=5139"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5140", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5141", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.ExtendableElementIdDataType, o6.ns["ns=wire_harness_vec;i=5141"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5142", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.ExtendableElementIdDataType, o6.ns["ns=wire_harness_vec;i=5142"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5143", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5144", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.GeneralTechnicalPartSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5144"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5145", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.GeneralTechnicalPartSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5145"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5146", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5147", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.InsulationCrimpDetailIdDataType, o6.ns["ns=wire_harness_vec;i=5147"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5148", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.InsulationCrimpDetailIdDataType, o6.ns["ns=wire_harness_vec;i=5148"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5149", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5150", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.InsulationSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5150"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5151", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.InsulationSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5151"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5152", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5153", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.ItemVersionIdDataType, o6.ns["ns=wire_harness_vec;i=5153"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5154", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.ItemVersionIdDataType, o6.ns["ns=wire_harness_vec;i=5154"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5155", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5156", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.OccurrenceOrUsageIdDataType, o6.ns["ns=wire_harness_vec;i=5156"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5157", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.OccurrenceOrUsageIdDataType, o6.ns["ns=wire_harness_vec;i=5157"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5158", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5159", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.PartOccurrenceIdDataType, o6.ns["ns=wire_harness_vec;i=5159"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5160", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.PartOccurrenceIdDataType, o6.ns["ns=wire_harness_vec;i=5160"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5161", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5162", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.PartOrUsageRelatedSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5162"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5163", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.PartOrUsageRelatedSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5163"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5164", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5165", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.PartVersionIdDataType, o6.ns["ns=wire_harness_vec;i=5165"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5166", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.PartVersionIdDataType, o6.ns["ns=wire_harness_vec;i=5166"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5167", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5168", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.PluggableTerminalRoleIdDataType, o6.ns["ns=wire_harness_vec;i=5168"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5169", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.PluggableTerminalRoleIdDataType, o6.ns["ns=wire_harness_vec;i=5169"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5170", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5171", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.PluggableTerminalSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5171"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5172", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.PluggableTerminalSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5172"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5173", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5174", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.ResourceVersionIdDataType, o6.ns["ns=wire_harness_vec;i=5174"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5175", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.ResourceVersionIdDataType, o6.ns["ns=wire_harness_vec;i=5175"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5176", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5177", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.RoleIdDataType, o6.ns["ns=wire_harness_vec;i=5177"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5178", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.RoleIdDataType, o6.ns["ns=wire_harness_vec;i=5178"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5179", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5180", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.RoutableElementIdDataType, o6.ns["ns=wire_harness_vec;i=5180"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5181", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.RoutableElementIdDataType, o6.ns["ns=wire_harness_vec;i=5181"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5182", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5183", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.SpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5183"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5184", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.SpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5184"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5185", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5186", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.TerminalRoleIdDataType, o6.ns["ns=wire_harness_vec;i=5186"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5187", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.TerminalRoleIdDataType, o6.ns["ns=wire_harness_vec;i=5187"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5188", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5189", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.TerminalSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5189"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5190", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.TerminalSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5190"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5191", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5192", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireElementIdDataType, o6.ns["ns=wire_harness_vec;i=5192"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5193", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireElementIdDataType, o6.ns["ns=wire_harness_vec;i=5193"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5194", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5195", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireElementReferenceIdDataType, o6.ns["ns=wire_harness_vec;i=5195"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5196", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireElementReferenceIdDataType, o6.ns["ns=wire_harness_vec;i=5196"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5197", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5198", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireElementSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5198"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5199", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireElementSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5199"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5200", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5201", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireEndIdDataType, o6.ns["ns=wire_harness_vec;i=5201"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5202", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireEndIdDataType, o6.ns["ns=wire_harness_vec;i=5202"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5203", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5204", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireMountingDetailIdDataType, o6.ns["ns=wire_harness_vec;i=5204"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5205", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireMountingDetailIdDataType, o6.ns["ns=wire_harness_vec;i=5205"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5206", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5207", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireMountingIdDataType, o6.ns["ns=wire_harness_vec;i=5207"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5208", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireMountingIdDataType, o6.ns["ns=wire_harness_vec;i=5208"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5209", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5210", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireReceptionIdDataType, o6.ns["ns=wire_harness_vec;i=5210"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5211", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireReceptionIdDataType, o6.ns["ns=wire_harness_vec;i=5211"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5212", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5213", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireReceptionReferenceIdDataType, o6.ns["ns=wire_harness_vec;i=5213"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5214", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireReceptionReferenceIdDataType, o6.ns["ns=wire_harness_vec;i=5214"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5215", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5216", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireReceptionSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5216"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5217", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireReceptionSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5217"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5218", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5219", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireRoleIdDataType, o6.ns["ns=wire_harness_vec;i=5219"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5220", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireRoleIdDataType, o6.ns["ns=wire_harness_vec;i=5220"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5221", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5222", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.WireSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5222"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5223", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.WireSpecificationIdDataType, o6.ns["ns=wire_harness_vec;i=5223"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5224", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5225", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.Material, o6.ns["ns=wire_harness_vec;i=5225"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5226", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.Material, o6.ns["ns=wire_harness_vec;i=5226"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5227", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5228", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.Size, o6.ns["ns=wire_harness_vec;i=5228"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5229", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.Size, o6.ns["ns=wire_harness_vec;i=5229"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5230", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5231", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.NumericalValue, o6.ns["ns=wire_harness_vec;i=5231"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5232", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.NumericalValue, o6.ns["ns=wire_harness_vec;i=5232"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5233", browseName="Default Binary")
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5234", browseName="Default XML")
o6.hasEncoding(wire_harness_vec_datypes.ValueRange, o6.ns["ns=wire_harness_vec;i=5234"])
ns0.objtypes.DataTypeEncodingType(nodeId="ns=wire_harness_vec;i=5235", browseName="Default JSON")
o6.hasEncoding(wire_harness_vec_datypes.ValueRange, o6.ns["ns=wire_harness_vec;i=5235"])
ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness_vec;i=6001",
    browseName="EnumStrings",
    parent="ns=wire_harness_vec;i=1003",
    referenceType=ns0.reftypes.HasProperty,
    dataType=o6.LocalizedText,
    valueRank=1,
    arrayDimensions=[2],
    value=[o6.LocalizedText("Open"), o6.LocalizedText("Closed")],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness_vec;i=6002",
    browseName="EnumValues",
    parent="ns=wire_harness_vec;i=3160",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[44],
    value=[
        ns0.datatypes.EnumValueType(value=0, displayName=o6.LocalizedText("Antenna")),
        ns0.datatypes.EnumValueType(value=1, displayName=o6.LocalizedText("Battery")),
        ns0.datatypes.EnumValueType(value=2, displayName=o6.LocalizedText("BoltMountedFixing")),
        ns0.datatypes.EnumValueType(value=3, displayName=o6.LocalizedText("BoltTerminal")),
        ns0.datatypes.EnumValueType(value=4, displayName=o6.LocalizedText("BridgeTerminal")),
        ns0.datatypes.EnumValueType(value=5, displayName=o6.LocalizedText("CableDuct")),
        ns0.datatypes.EnumValueType(value=6, displayName=o6.LocalizedText("CableTie")),
        ns0.datatypes.EnumValueType(value=7, displayName=o6.LocalizedText("Capacitor")),
        ns0.datatypes.EnumValueType(value=8, displayName=o6.LocalizedText("CavityAccessory")),
        ns0.datatypes.EnumValueType(value=9, displayName=o6.LocalizedText("CavityPlug")),
        ns0.datatypes.EnumValueType(value=10, displayName=o6.LocalizedText("CavitySeal")),
        ns0.datatypes.EnumValueType(value=11, displayName=o6.LocalizedText("ConnectorHousing")),
        ns0.datatypes.EnumValueType(value=12, displayName=o6.LocalizedText("ConnectorHousingCap")),
        ns0.datatypes.EnumValueType(value=13, displayName=o6.LocalizedText("ConnectorHousingCover")),
        ns0.datatypes.EnumValueType(value=14, displayName=o6.LocalizedText("CorrugatedPipe")),
        ns0.datatypes.EnumValueType(value=15, displayName=o6.LocalizedText("Diode")),
        ns0.datatypes.EnumValueType(value=16, displayName=o6.LocalizedText("EdgeMountedFixing")),
        ns0.datatypes.EnumValueType(value=17, displayName=o6.LocalizedText("EEComponent")),
        ns0.datatypes.EnumValueType(value=18, displayName=o6.LocalizedText("Ferrite")),
        ns0.datatypes.EnumValueType(value=19, displayName=o6.LocalizedText("Fitting")),
        ns0.datatypes.EnumValueType(value=20, displayName=o6.LocalizedText("Fixing")),
        ns0.datatypes.EnumValueType(value=21, displayName=o6.LocalizedText("Fuse")),
        ns0.datatypes.EnumValueType(value=22, displayName=o6.LocalizedText("Grommet")),
        ns0.datatypes.EnumValueType(value=23, displayName=o6.LocalizedText("HoleMountedFixing")),
        ns0.datatypes.EnumValueType(value=24, displayName=o6.LocalizedText("MultiCavityPlug")),
        ns0.datatypes.EnumValueType(value=25, displayName=o6.LocalizedText("MultiCavitySeal")),
        ns0.datatypes.EnumValueType(value=26, displayName=o6.LocalizedText("MultiFuse")),
        ns0.datatypes.EnumValueType(
            value=27,
            displayName=o6.LocalizedText("Other"),
            description=o6.LocalizedText(
                ';p&gt;The&lt;i&gt;PrimaryPartType&lt;/i&gt;"&lt;i&gt;Other&lt;/i&gt;" is used for parts that are described by a direct instance of&lt;i&gt;PartOrUsageRelatedSpecification&lt;/i&gt;. These are parts that do not have a specific classification in the VEC and can be described with a&lt;i&gt;PartOrUsageRelatedSpecification&lt;/i&gt;and&lt;i&gt;CustomProperties.&lt;/i&gt;The corresponding&lt;i&gt;Role&lt;/i&gt;is the&lt;i&gt;SpecificRole.&lt;/i&gt;&lt;/p&gt;'
            ),
        ),
        ns0.datatypes.EnumValueType(value=28, displayName=o6.LocalizedText("OpenWireEndTerminal")),
        ns0.datatypes.EnumValueType(value=29, displayName=o6.LocalizedText("OpenWireEnd")),
        ns0.datatypes.EnumValueType(
            value=30,
            displayName=o6.LocalizedText("PartStructure"),
            description=o6.LocalizedText(
                ';p&gt;The&lt;i&gt;PrimaryPartType&lt;/i&gt;"&lt;i&gt;PartStructure&lt;/i&gt;" has an inconsistency with VEC&#160;conventions for historical reasons, which is kept for backwards compatibility. The corresponding&lt;i&gt;PartOrUsageRelatedSpecification&lt;/i&gt;is the&lt;i&gt;PartStructureSpecification.&lt;/i&gt;However, the corresponding&lt;i&gt;Role&lt;/i&gt;is the&lt;i&gt;PartWithSubComponentsRole&lt;/i&gt;.&lt;/p&gt;'
            ),
        ),
        ns0.datatypes.EnumValueType(value=31, displayName=o6.LocalizedText("PluggableTerminal")),
        ns0.datatypes.EnumValueType(value=32, displayName=o6.LocalizedText("PotentialDistributor")),
        ns0.datatypes.EnumValueType(value=33, displayName=o6.LocalizedText("Relay")),
        ns0.datatypes.EnumValueType(value=34, displayName=o6.LocalizedText("RingTerminal")),
        ns0.datatypes.EnumValueType(value=35, displayName=o6.LocalizedText("ShrinkableTube")),
        ns0.datatypes.EnumValueType(value=36, displayName=o6.LocalizedText("SpliceTerminal")),
        ns0.datatypes.EnumValueType(value=37, displayName=o6.LocalizedText("Stripe")),
        ns0.datatypes.EnumValueType(value=38, displayName=o6.LocalizedText("Tape")),
        ns0.datatypes.EnumValueType(value=39, displayName=o6.LocalizedText("Terminal")),
        ns0.datatypes.EnumValueType(value=40, displayName=o6.LocalizedText("Tube")),
        ns0.datatypes.EnumValueType(value=41, displayName=o6.LocalizedText("Wire")),
        ns0.datatypes.EnumValueType(value=42, displayName=o6.LocalizedText("WireEndAccessory")),
        ns0.datatypes.EnumValueType(value=43, displayName=o6.LocalizedText("WireProtection")),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=wire_harness_vec;i=6003",
    browseName="EnumValues",
    parent="ns=wire_harness_vec;i=3500",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.EnumValueType,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.EnumValueType(
            value=0, displayName=o6.LocalizedText("Rigid"), description=o6.LocalizedText(";p&gt;Used for conductors that are made of solid material.&lt;/p&gt;")
        ),
        ns0.datatypes.EnumValueType(
            value=1,
            displayName=o6.LocalizedText("Stranded"),
            description=o6.LocalizedText(";p&gt;Used for conductors that are made of multiple individual strands (used for most automotive cores).&lt;/p&gt;"),
        ),
        ns0.datatypes.EnumValueType(
            value=2, displayName=o6.LocalizedText("Foil"), description=o6.LocalizedText(";p&gt;Used for conductors that are a foil (e.g. some shields).&lt;/p&gt;")
        ),
        ns0.datatypes.EnumValueType(
            value=3,
            displayName=o6.LocalizedText("Braided"),
            description=o6.LocalizedText(
                ";p&gt;Used for conductors that are made of multiple individual strands that are braided together&#160;(often used for shields).&lt;/p&gt;"
            ),
        ),
    ],
)
httpColonSlashSlashOpcfoundationDotOrgSlashUASlashWireHarnessSlashVECSlash = ns0.objtypes.NamespaceMetadataType(
    nodeId="ns=wire_harness_vec;i=5001",
    browseName="ns=wire_harness_vec;http://opcfoundation.org/UA/WireHarness/VEC/",
    references=[
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wire_harness_vec;i=6004", browseName="IsNamespaceSubset", dataType=o6.Boolean, value=False)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=wire_harness_vec;i=6009", browseName="NamespacePublicationDate", dataType=o6.DateTime, value=o6.DateTime("2025-04-01T00:00:00Z"))
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=wire_harness_vec;i=6014", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/WireHarness/VEC/")
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wire_harness_vec;i=6015", browseName="NamespaceVersion", dataType=o6.String, value="1.0.0")),
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=wire_harness_vec;i=6016", browseName="StaticNodeIdTypes", dataType=ns0.datatypes.IdType, valueRank=1, arrayDimensions=[0])
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wire_harness_vec;i=6017", browseName="StaticNumericNodeIdRange", dataType=ns0.datatypes.NumericRange, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wire_harness_vec;i=6018", browseName="StaticStringNodeIdPattern", dataType=o6.String)),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wire_harness_vec;i=6019", browseName="DefaultRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wire_harness_vec;i=6020", browseName="DefaultUserRolePermissions", dataType=ns0.datatypes.RolePermissionType, valueRank=1, arrayDimensions=[0]
            )
        ),
        o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=wire_harness_vec;i=6021", browseName="DefaultAccessRestrictions", dataType=ns0.datatypes.AccessRestrictionType)),
    ],
    parent="i=11715",
    referenceType=ns0.reftypes.HasComponent,
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6026", browseName="ns=wire_harness_vec;ARGB32ColorType", dataType=o6.String, value="ARGB32ColorType")
o6.reference(o6.ns["ns=wire_harness_vec;i=5002"], "i=39", o6.ns["ns=wire_harness_vec;i=6026"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6027", browseName="ns=wire_harness_vec;ARGB32ColorType", dataType=o6.String, value="//xs:element[@name='ARGB32ColorType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5003"], "i=39", o6.ns["ns=wire_harness_vec;i=6027"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6028", browseName="ns=wire_harness_vec;BoundingBox", dataType=o6.String, value="BoundingBox")
o6.reference(o6.ns["ns=wire_harness_vec;i=5005"], "i=39", o6.ns["ns=wire_harness_vec;i=6028"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6029", browseName="ns=wire_harness_vec;BoundingBox", dataType=o6.String, value="//xs:element[@name='BoundingBox']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5006"], "i=39", o6.ns["ns=wire_harness_vec;i=6029"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6030", browseName="ns=wire_harness_vec;ContactPoint", dataType=o6.String, value="ContactPoint")
o6.reference(o6.ns["ns=wire_harness_vec;i=5008"], "i=39", o6.ns["ns=wire_harness_vec;i=6030"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6031", browseName="ns=wire_harness_vec;ContactPoint", dataType=o6.String, value="//xs:element[@name='ContactPoint']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5009"], "i=39", o6.ns["ns=wire_harness_vec;i=6031"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6032", browseName="ns=wire_harness_vec;PartOccurrence", dataType=o6.String, value="PartOccurrence")
o6.reference(o6.ns["ns=wire_harness_vec;i=5011"], "i=39", o6.ns["ns=wire_harness_vec;i=6032"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6033", browseName="ns=wire_harness_vec;PartOccurrence", dataType=o6.String, value="//xs:element[@name='PartOccurrence']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5012"], "i=39", o6.ns["ns=wire_harness_vec;i=6033"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6034", browseName="ns=wire_harness_vec;WireElementReference", dataType=o6.String, value="WireElementReference")
o6.reference(o6.ns["ns=wire_harness_vec;i=5014"], "i=39", o6.ns["ns=wire_harness_vec;i=6034"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6035", browseName="ns=wire_harness_vec;WireElementReference", dataType=o6.String, value="//xs:element[@name='WireElementReference']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5015"], "i=39", o6.ns["ns=wire_harness_vec;i=6035"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6036", browseName="ns=wire_harness_vec;CoreCrimpDetail", dataType=o6.String, value="CoreCrimpDetail")
o6.reference(o6.ns["ns=wire_harness_vec;i=5017"], "i=39", o6.ns["ns=wire_harness_vec;i=6036"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6037", browseName="ns=wire_harness_vec;CoreCrimpDetail", dataType=o6.String, value="//xs:element[@name='CoreCrimpDetail']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5018"], "i=39", o6.ns["ns=wire_harness_vec;i=6037"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6038", browseName="ns=wire_harness_vec;InsulationCrimpDetail", dataType=o6.String, value="InsulationCrimpDetail")
o6.reference(o6.ns["ns=wire_harness_vec;i=5020"], "i=39", o6.ns["ns=wire_harness_vec;i=6038"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6039", browseName="ns=wire_harness_vec;InsulationCrimpDetail", dataType=o6.String, value="//xs:element[@name='InsulationCrimpDetail']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5021"], "i=39", o6.ns["ns=wire_harness_vec;i=6039"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6040", browseName="ns=wire_harness_vec;DocumentVersion", dataType=o6.String, value="DocumentVersion")
o6.reference(o6.ns["ns=wire_harness_vec;i=5023"], "i=39", o6.ns["ns=wire_harness_vec;i=6040"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6041", browseName="ns=wire_harness_vec;DocumentVersion", dataType=o6.String, value="//xs:element[@name='DocumentVersion']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5024"], "i=39", o6.ns["ns=wire_harness_vec;i=6041"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6042", browseName="ns=wire_harness_vec;PartVersion", dataType=o6.String, value="PartVersion")
o6.reference(o6.ns["ns=wire_harness_vec;i=5026"], "i=39", o6.ns["ns=wire_harness_vec;i=6042"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6043", browseName="ns=wire_harness_vec;PartVersion", dataType=o6.String, value="//xs:element[@name='PartVersion']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5027"], "i=39", o6.ns["ns=wire_harness_vec;i=6043"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6044", browseName="ns=wire_harness_vec;ResourceVersion", dataType=o6.String, value="ResourceVersion")
o6.reference(o6.ns["ns=wire_harness_vec;i=5029"], "i=39", o6.ns["ns=wire_harness_vec;i=6044"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6045", browseName="ns=wire_harness_vec;ResourceVersion", dataType=o6.String, value="//xs:element[@name='ResourceVersion']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5030"], "i=39", o6.ns["ns=wire_harness_vec;i=6045"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6046", browseName="ns=wire_harness_vec;CavitySealRole", dataType=o6.String, value="CavitySealRole")
o6.reference(o6.ns["ns=wire_harness_vec;i=5032"], "i=39", o6.ns["ns=wire_harness_vec;i=6046"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6047", browseName="ns=wire_harness_vec;CavitySealRole", dataType=o6.String, value="//xs:element[@name='CavitySealRole']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5033"], "i=39", o6.ns["ns=wire_harness_vec;i=6047"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6048", browseName="ns=wire_harness_vec;TerminalRole", dataType=o6.String, value="TerminalRole")
o6.reference(o6.ns["ns=wire_harness_vec;i=5035"], "i=39", o6.ns["ns=wire_harness_vec;i=6048"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6049", browseName="ns=wire_harness_vec;TerminalRole", dataType=o6.String, value="//xs:element[@name='TerminalRole']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5036"], "i=39", o6.ns["ns=wire_harness_vec;i=6049"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6050", browseName="ns=wire_harness_vec;PluggableTerminalRole", dataType=o6.String, value="PluggableTerminalRole")
o6.reference(o6.ns["ns=wire_harness_vec;i=5038"], "i=39", o6.ns["ns=wire_harness_vec;i=6050"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6051", browseName="ns=wire_harness_vec;PluggableTerminalRole", dataType=o6.String, value="//xs:element[@name='PluggableTerminalRole']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5039"], "i=39", o6.ns["ns=wire_harness_vec;i=6051"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6052", browseName="ns=wire_harness_vec;WireRole", dataType=o6.String, value="WireRole")
o6.reference(o6.ns["ns=wire_harness_vec;i=5041"], "i=39", o6.ns["ns=wire_harness_vec;i=6052"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6053", browseName="ns=wire_harness_vec;WireRole", dataType=o6.String, value="//xs:element[@name='WireRole']")
o6.reference(o6.ns["ns=wire_harness_vec;i=5042"], "i=39", o6.ns["ns=wire_harness_vec;i=6053"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6054", browseName="ns=wire_harness_vec;CompositionSpecification", dataType=o6.String, value="CompositionSpecification"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5044"], "i=39", o6.ns["ns=wire_harness_vec;i=6054"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6055", browseName="ns=wire_harness_vec;CompositionSpecification", dataType=o6.String, value="//xs:element[@name='CompositionSpecification']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5045"], "i=39", o6.ns["ns=wire_harness_vec;i=6055"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6056", browseName="ns=wire_harness_vec;CoreSpecification", dataType=o6.String, value="CoreSpecification")
o6.reference(o6.ns["ns=wire_harness_vec;i=5047"], "i=39", o6.ns["ns=wire_harness_vec;i=6056"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6057", browseName="ns=wire_harness_vec;CoreSpecification", dataType=o6.String, value="//xs:element[@name='CoreSpecification']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5048"], "i=39", o6.ns["ns=wire_harness_vec;i=6057"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6058", browseName="ns=wire_harness_vec;ContactingSpecification", dataType=o6.String, value="ContactingSpecification"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5050"], "i=39", o6.ns["ns=wire_harness_vec;i=6058"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6059", browseName="ns=wire_harness_vec;ContactingSpecification", dataType=o6.String, value="//xs:element[@name='ContactingSpecification']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5051"], "i=39", o6.ns["ns=wire_harness_vec;i=6059"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6060", browseName="ns=wire_harness_vec;InsulationSpecification", dataType=o6.String, value="InsulationSpecification"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5053"], "i=39", o6.ns["ns=wire_harness_vec;i=6060"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6061", browseName="ns=wire_harness_vec;InsulationSpecification", dataType=o6.String, value="//xs:element[@name='InsulationSpecification']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5054"], "i=39", o6.ns["ns=wire_harness_vec;i=6061"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6062", browseName="ns=wire_harness_vec;PartOrUsageRelatedSpecification", dataType=o6.String, value="PartOrUsageRelatedSpecification"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5056"], "i=39", o6.ns["ns=wire_harness_vec;i=6062"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6063",
    browseName="ns=wire_harness_vec;PartOrUsageRelatedSpecification",
    dataType=o6.String,
    value="//xs:element[@name='PartOrUsageRelatedSpecification']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5057"], "i=39", o6.ns["ns=wire_harness_vec;i=6063"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6064", browseName="ns=wire_harness_vec;CavitySealSpecification", dataType=o6.String, value="CavitySealSpecification"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5059"], "i=39", o6.ns["ns=wire_harness_vec;i=6064"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6065", browseName="ns=wire_harness_vec;CavitySealSpecification", dataType=o6.String, value="//xs:element[@name='CavitySealSpecification']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5060"], "i=39", o6.ns["ns=wire_harness_vec;i=6065"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6066", browseName="ns=wire_harness_vec;GeneralTechnicalPartSpecification", dataType=o6.String, value="GeneralTechnicalPartSpecification"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5062"], "i=39", o6.ns["ns=wire_harness_vec;i=6066"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6067",
    browseName="ns=wire_harness_vec;GeneralTechnicalPartSpecification",
    dataType=o6.String,
    value="//xs:element[@name='GeneralTechnicalPartSpecification']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5063"], "i=39", o6.ns["ns=wire_harness_vec;i=6067"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6068", browseName="ns=wire_harness_vec;TerminalSpecification", dataType=o6.String, value="TerminalSpecification")
o6.reference(o6.ns["ns=wire_harness_vec;i=5065"], "i=39", o6.ns["ns=wire_harness_vec;i=6068"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6069", browseName="ns=wire_harness_vec;TerminalSpecification", dataType=o6.String, value="//xs:element[@name='TerminalSpecification']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5066"], "i=39", o6.ns["ns=wire_harness_vec;i=6069"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6070", browseName="ns=wire_harness_vec;PluggableTerminalSpecification", dataType=o6.String, value="PluggableTerminalSpecification"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5068"], "i=39", o6.ns["ns=wire_harness_vec;i=6070"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6071",
    browseName="ns=wire_harness_vec;PluggableTerminalSpecification",
    dataType=o6.String,
    value="//xs:element[@name='PluggableTerminalSpecification']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5069"], "i=39", o6.ns["ns=wire_harness_vec;i=6071"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6072", browseName="ns=wire_harness_vec;WireSpecification", dataType=o6.String, value="WireSpecification")
o6.reference(o6.ns["ns=wire_harness_vec;i=5071"], "i=39", o6.ns["ns=wire_harness_vec;i=6072"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6073", browseName="ns=wire_harness_vec;WireSpecification", dataType=o6.String, value="//xs:element[@name='WireSpecification']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5072"], "i=39", o6.ns["ns=wire_harness_vec;i=6073"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6074", browseName="ns=wire_harness_vec;WireElementSpecification", dataType=o6.String, value="WireElementSpecification"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5074"], "i=39", o6.ns["ns=wire_harness_vec;i=6074"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6075", browseName="ns=wire_harness_vec;WireElementSpecification", dataType=o6.String, value="//xs:element[@name='WireElementSpecification']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5075"], "i=39", o6.ns["ns=wire_harness_vec;i=6075"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6076", browseName="ns=wire_harness_vec;WireReceptionSpecification", dataType=o6.String, value="WireReceptionSpecification"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5077"], "i=39", o6.ns["ns=wire_harness_vec;i=6076"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6077", browseName="ns=wire_harness_vec;WireReceptionSpecification", dataType=o6.String, value="//xs:element[@name='WireReceptionSpecification']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5078"], "i=39", o6.ns["ns=wire_harness_vec;i=6077"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6078", browseName="ns=wire_harness_vec;Tolerance", dataType=o6.String, value="Tolerance")
o6.reference(o6.ns["ns=wire_harness_vec;i=5080"], "i=39", o6.ns["ns=wire_harness_vec;i=6078"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6079", browseName="ns=wire_harness_vec;Tolerance", dataType=o6.String, value="//xs:element[@name='Tolerance']")
o6.reference(o6.ns["ns=wire_harness_vec;i=5081"], "i=39", o6.ns["ns=wire_harness_vec;i=6079"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6080", browseName="ns=wire_harness_vec;WireElement", dataType=o6.String, value="WireElement")
o6.reference(o6.ns["ns=wire_harness_vec;i=5083"], "i=39", o6.ns["ns=wire_harness_vec;i=6080"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6081", browseName="ns=wire_harness_vec;WireElement", dataType=o6.String, value="//xs:element[@name='WireElement']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5084"], "i=39", o6.ns["ns=wire_harness_vec;i=6081"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6082", browseName="ns=wire_harness_vec;WireEnd", dataType=o6.String, value="WireEnd")
o6.reference(o6.ns["ns=wire_harness_vec;i=5086"], "i=39", o6.ns["ns=wire_harness_vec;i=6082"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6083", browseName="ns=wire_harness_vec;WireEnd", dataType=o6.String, value="//xs:element[@name='WireEnd']")
o6.reference(o6.ns["ns=wire_harness_vec;i=5087"], "i=39", o6.ns["ns=wire_harness_vec;i=6083"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6084", browseName="ns=wire_harness_vec;WireMounting", dataType=o6.String, value="WireMounting")
o6.reference(o6.ns["ns=wire_harness_vec;i=5089"], "i=39", o6.ns["ns=wire_harness_vec;i=6084"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6085", browseName="ns=wire_harness_vec;WireMounting", dataType=o6.String, value="//xs:element[@name='WireMounting']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5090"], "i=39", o6.ns["ns=wire_harness_vec;i=6085"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6086", browseName="ns=wire_harness_vec;WireMountingDetail", dataType=o6.String, value="WireMountingDetail")
o6.reference(o6.ns["ns=wire_harness_vec;i=5092"], "i=39", o6.ns["ns=wire_harness_vec;i=6086"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6087", browseName="ns=wire_harness_vec;WireMountingDetail", dataType=o6.String, value="//xs:element[@name='WireMountingDetail']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5093"], "i=39", o6.ns["ns=wire_harness_vec;i=6087"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6088", browseName="ns=wire_harness_vec;WireReception", dataType=o6.String, value="WireReception")
o6.reference(o6.ns["ns=wire_harness_vec;i=5095"], "i=39", o6.ns["ns=wire_harness_vec;i=6088"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6089", browseName="ns=wire_harness_vec;WireReception", dataType=o6.String, value="//xs:element[@name='WireReception']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5096"], "i=39", o6.ns["ns=wire_harness_vec;i=6089"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6090", browseName="ns=wire_harness_vec;WireReceptionReference", dataType=o6.String, value="WireReceptionReference"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5098"], "i=39", o6.ns["ns=wire_harness_vec;i=6090"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6091", browseName="ns=wire_harness_vec;WireReceptionReference", dataType=o6.String, value="//xs:element[@name='WireReceptionReference']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5099"], "i=39", o6.ns["ns=wire_harness_vec;i=6091"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6092", browseName="ns=wire_harness_vec;CavityPartRoleIdDataType", dataType=o6.String, value="CavityPartRoleIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5101"], "i=39", o6.ns["ns=wire_harness_vec;i=6092"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6093", browseName="ns=wire_harness_vec;CavityPartRoleIdDataType", dataType=o6.String, value="//xs:element[@name='CavityPartRoleIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5102"], "i=39", o6.ns["ns=wire_harness_vec;i=6093"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6094", browseName="ns=wire_harness_vec;CavityPartSpecificationIdDataType", dataType=o6.String, value="CavityPartSpecificationIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5104"], "i=39", o6.ns["ns=wire_harness_vec;i=6094"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6095",
    browseName="ns=wire_harness_vec;CavityPartSpecificationIdDataType",
    dataType=o6.String,
    value="//xs:element[@name='CavityPartSpecificationIdDataType']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5105"], "i=39", o6.ns["ns=wire_harness_vec;i=6095"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6096", browseName="ns=wire_harness_vec;CavitySealRoleIdDataType", dataType=o6.String, value="CavitySealRoleIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5107"], "i=39", o6.ns["ns=wire_harness_vec;i=6096"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6097", browseName="ns=wire_harness_vec;CavitySealRoleIdDataType", dataType=o6.String, value="//xs:element[@name='CavitySealRoleIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5108"], "i=39", o6.ns["ns=wire_harness_vec;i=6097"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6098", browseName="ns=wire_harness_vec;CavitySealSpecificationIdDataType", dataType=o6.String, value="CavitySealSpecificationIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5110"], "i=39", o6.ns["ns=wire_harness_vec;i=6098"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6099",
    browseName="ns=wire_harness_vec;CavitySealSpecificationIdDataType",
    dataType=o6.String,
    value="//xs:element[@name='CavitySealSpecificationIdDataType']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5111"], "i=39", o6.ns["ns=wire_harness_vec;i=6099"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6100", browseName="ns=wire_harness_vec;CompositionSpecificationIdDataType", dataType=o6.String, value="CompositionSpecificationIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5113"], "i=39", o6.ns["ns=wire_harness_vec;i=6100"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6101",
    browseName="ns=wire_harness_vec;CompositionSpecificationIdDataType",
    dataType=o6.String,
    value="//xs:element[@name='CompositionSpecificationIdDataType']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5114"], "i=39", o6.ns["ns=wire_harness_vec;i=6101"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6102", browseName="ns=wire_harness_vec;ConductorSpecificationIdDataType", dataType=o6.String, value="ConductorSpecificationIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5116"], "i=39", o6.ns["ns=wire_harness_vec;i=6102"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6103",
    browseName="ns=wire_harness_vec;ConductorSpecificationIdDataType",
    dataType=o6.String,
    value="//xs:element[@name='ConductorSpecificationIdDataType']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5117"], "i=39", o6.ns["ns=wire_harness_vec;i=6103"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6104", browseName="ns=wire_harness_vec;ConfigurableElementIdDataType", dataType=o6.String, value="ConfigurableElementIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5119"], "i=39", o6.ns["ns=wire_harness_vec;i=6104"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6105",
    browseName="ns=wire_harness_vec;ConfigurableElementIdDataType",
    dataType=o6.String,
    value="//xs:element[@name='ConfigurableElementIdDataType']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5120"], "i=39", o6.ns["ns=wire_harness_vec;i=6105"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6106", browseName="ns=wire_harness_vec;ContactingSpecificationIdDataType", dataType=o6.String, value="ContactingSpecificationIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5122"], "i=39", o6.ns["ns=wire_harness_vec;i=6106"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6107",
    browseName="ns=wire_harness_vec;ContactingSpecificationIdDataType",
    dataType=o6.String,
    value="//xs:element[@name='ContactingSpecificationIdDataType']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5123"], "i=39", o6.ns["ns=wire_harness_vec;i=6107"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6108", browseName="ns=wire_harness_vec;ContactPointIdDataType", dataType=o6.String, value="ContactPointIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5125"], "i=39", o6.ns["ns=wire_harness_vec;i=6108"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6109", browseName="ns=wire_harness_vec;ContactPointIdDataType", dataType=o6.String, value="//xs:element[@name='ContactPointIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5126"], "i=39", o6.ns["ns=wire_harness_vec;i=6109"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6110", browseName="ns=wire_harness_vec;CoreCrimpDetailIdDataType", dataType=o6.String, value="CoreCrimpDetailIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5128"], "i=39", o6.ns["ns=wire_harness_vec;i=6110"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6111", browseName="ns=wire_harness_vec;CoreCrimpDetailIdDataType", dataType=o6.String, value="//xs:element[@name='CoreCrimpDetailIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5129"], "i=39", o6.ns["ns=wire_harness_vec;i=6111"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6112", browseName="ns=wire_harness_vec;CoreSpecificationIdDataType", dataType=o6.String, value="CoreSpecificationIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5131"], "i=39", o6.ns["ns=wire_harness_vec;i=6112"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6113", browseName="ns=wire_harness_vec;CoreSpecificationIdDataType", dataType=o6.String, value="//xs:element[@name='CoreSpecificationIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5132"], "i=39", o6.ns["ns=wire_harness_vec;i=6113"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6114", browseName="ns=wire_harness_vec;CrimpDetailIdDataType", dataType=o6.String, value="CrimpDetailIdDataType")
o6.reference(o6.ns["ns=wire_harness_vec;i=5134"], "i=39", o6.ns["ns=wire_harness_vec;i=6114"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6115", browseName="ns=wire_harness_vec;CrimpDetailIdDataType", dataType=o6.String, value="//xs:element[@name='CrimpDetailIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5135"], "i=39", o6.ns["ns=wire_harness_vec;i=6115"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6116", browseName="ns=wire_harness_vec;DocumentVersionIdDataType", dataType=o6.String, value="DocumentVersionIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5137"], "i=39", o6.ns["ns=wire_harness_vec;i=6116"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6117", browseName="ns=wire_harness_vec;DocumentVersionIdDataType", dataType=o6.String, value="//xs:element[@name='DocumentVersionIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5138"], "i=39", o6.ns["ns=wire_harness_vec;i=6117"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6118", browseName="ns=wire_harness_vec;ExtendableElementIdDataType", dataType=o6.String, value="ExtendableElementIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5140"], "i=39", o6.ns["ns=wire_harness_vec;i=6118"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6119", browseName="ns=wire_harness_vec;ExtendableElementIdDataType", dataType=o6.String, value="//xs:element[@name='ExtendableElementIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5141"], "i=39", o6.ns["ns=wire_harness_vec;i=6119"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6120",
    browseName="ns=wire_harness_vec;GeneralTechnicalPartSpecificationIdDataType",
    dataType=o6.String,
    value="GeneralTechnicalPartSpecificationIdDataType",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5143"], "i=39", o6.ns["ns=wire_harness_vec;i=6120"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6121",
    browseName="ns=wire_harness_vec;GeneralTechnicalPartSpecificationIdDataType",
    dataType=o6.String,
    value="//xs:element[@name='GeneralTechnicalPartSpecificationIdDataType']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5144"], "i=39", o6.ns["ns=wire_harness_vec;i=6121"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6122", browseName="ns=wire_harness_vec;InsulationCrimpDetailIdDataType", dataType=o6.String, value="InsulationCrimpDetailIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5146"], "i=39", o6.ns["ns=wire_harness_vec;i=6122"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6123",
    browseName="ns=wire_harness_vec;InsulationCrimpDetailIdDataType",
    dataType=o6.String,
    value="//xs:element[@name='InsulationCrimpDetailIdDataType']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5147"], "i=39", o6.ns["ns=wire_harness_vec;i=6123"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6124", browseName="ns=wire_harness_vec;InsulationSpecificationIdDataType", dataType=o6.String, value="InsulationSpecificationIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5149"], "i=39", o6.ns["ns=wire_harness_vec;i=6124"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6125",
    browseName="ns=wire_harness_vec;InsulationSpecificationIdDataType",
    dataType=o6.String,
    value="//xs:element[@name='InsulationSpecificationIdDataType']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5150"], "i=39", o6.ns["ns=wire_harness_vec;i=6125"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6126", browseName="ns=wire_harness_vec;ItemVersionIdDataType", dataType=o6.String, value="ItemVersionIdDataType")
o6.reference(o6.ns["ns=wire_harness_vec;i=5152"], "i=39", o6.ns["ns=wire_harness_vec;i=6126"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6127", browseName="ns=wire_harness_vec;ItemVersionIdDataType", dataType=o6.String, value="//xs:element[@name='ItemVersionIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5153"], "i=39", o6.ns["ns=wire_harness_vec;i=6127"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6128", browseName="ns=wire_harness_vec;OccurrenceOrUsageIdDataType", dataType=o6.String, value="OccurrenceOrUsageIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5155"], "i=39", o6.ns["ns=wire_harness_vec;i=6128"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6129", browseName="ns=wire_harness_vec;OccurrenceOrUsageIdDataType", dataType=o6.String, value="//xs:element[@name='OccurrenceOrUsageIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5156"], "i=39", o6.ns["ns=wire_harness_vec;i=6129"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6130", browseName="ns=wire_harness_vec;PartOccurrenceIdDataType", dataType=o6.String, value="PartOccurrenceIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5158"], "i=39", o6.ns["ns=wire_harness_vec;i=6130"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6131", browseName="ns=wire_harness_vec;PartOccurrenceIdDataType", dataType=o6.String, value="//xs:element[@name='PartOccurrenceIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5159"], "i=39", o6.ns["ns=wire_harness_vec;i=6131"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6132",
    browseName="ns=wire_harness_vec;PartOrUsageRelatedSpecificationIdDataType",
    dataType=o6.String,
    value="PartOrUsageRelatedSpecificationIdDataType",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5161"], "i=39", o6.ns["ns=wire_harness_vec;i=6132"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6133",
    browseName="ns=wire_harness_vec;PartOrUsageRelatedSpecificationIdDataType",
    dataType=o6.String,
    value="//xs:element[@name='PartOrUsageRelatedSpecificationIdDataType']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5162"], "i=39", o6.ns["ns=wire_harness_vec;i=6133"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6134", browseName="ns=wire_harness_vec;PartVersionIdDataType", dataType=o6.String, value="PartVersionIdDataType")
o6.reference(o6.ns["ns=wire_harness_vec;i=5164"], "i=39", o6.ns["ns=wire_harness_vec;i=6134"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6135", browseName="ns=wire_harness_vec;PartVersionIdDataType", dataType=o6.String, value="//xs:element[@name='PartVersionIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5165"], "i=39", o6.ns["ns=wire_harness_vec;i=6135"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6136", browseName="ns=wire_harness_vec;PluggableTerminalRoleIdDataType", dataType=o6.String, value="PluggableTerminalRoleIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5167"], "i=39", o6.ns["ns=wire_harness_vec;i=6136"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6137",
    browseName="ns=wire_harness_vec;PluggableTerminalRoleIdDataType",
    dataType=o6.String,
    value="//xs:element[@name='PluggableTerminalRoleIdDataType']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5168"], "i=39", o6.ns["ns=wire_harness_vec;i=6137"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6138",
    browseName="ns=wire_harness_vec;PluggableTerminalSpecificationIdDataType",
    dataType=o6.String,
    value="PluggableTerminalSpecificationIdDataType",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5170"], "i=39", o6.ns["ns=wire_harness_vec;i=6138"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6139",
    browseName="ns=wire_harness_vec;PluggableTerminalSpecificationIdDataType",
    dataType=o6.String,
    value="//xs:element[@name='PluggableTerminalSpecificationIdDataType']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5171"], "i=39", o6.ns["ns=wire_harness_vec;i=6139"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6140", browseName="ns=wire_harness_vec;ResourceVersionIdDataType", dataType=o6.String, value="ResourceVersionIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5173"], "i=39", o6.ns["ns=wire_harness_vec;i=6140"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6141", browseName="ns=wire_harness_vec;ResourceVersionIdDataType", dataType=o6.String, value="//xs:element[@name='ResourceVersionIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5174"], "i=39", o6.ns["ns=wire_harness_vec;i=6141"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6142", browseName="ns=wire_harness_vec;RoleIdDataType", dataType=o6.String, value="RoleIdDataType")
o6.reference(o6.ns["ns=wire_harness_vec;i=5176"], "i=39", o6.ns["ns=wire_harness_vec;i=6142"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6143", browseName="ns=wire_harness_vec;RoleIdDataType", dataType=o6.String, value="//xs:element[@name='RoleIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5177"], "i=39", o6.ns["ns=wire_harness_vec;i=6143"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6144", browseName="ns=wire_harness_vec;RoutableElementIdDataType", dataType=o6.String, value="RoutableElementIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5179"], "i=39", o6.ns["ns=wire_harness_vec;i=6144"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6145", browseName="ns=wire_harness_vec;RoutableElementIdDataType", dataType=o6.String, value="//xs:element[@name='RoutableElementIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5180"], "i=39", o6.ns["ns=wire_harness_vec;i=6145"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6146", browseName="ns=wire_harness_vec;SpecificationIdDataType", dataType=o6.String, value="SpecificationIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5182"], "i=39", o6.ns["ns=wire_harness_vec;i=6146"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6147", browseName="ns=wire_harness_vec;SpecificationIdDataType", dataType=o6.String, value="//xs:element[@name='SpecificationIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5183"], "i=39", o6.ns["ns=wire_harness_vec;i=6147"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6148", browseName="ns=wire_harness_vec;TerminalRoleIdDataType", dataType=o6.String, value="TerminalRoleIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5185"], "i=39", o6.ns["ns=wire_harness_vec;i=6148"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6149", browseName="ns=wire_harness_vec;TerminalRoleIdDataType", dataType=o6.String, value="//xs:element[@name='TerminalRoleIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5186"], "i=39", o6.ns["ns=wire_harness_vec;i=6149"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6150", browseName="ns=wire_harness_vec;TerminalSpecificationIdDataType", dataType=o6.String, value="TerminalSpecificationIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5188"], "i=39", o6.ns["ns=wire_harness_vec;i=6150"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6151",
    browseName="ns=wire_harness_vec;TerminalSpecificationIdDataType",
    dataType=o6.String,
    value="//xs:element[@name='TerminalSpecificationIdDataType']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5189"], "i=39", o6.ns["ns=wire_harness_vec;i=6151"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6152", browseName="ns=wire_harness_vec;WireElementIdDataType", dataType=o6.String, value="WireElementIdDataType")
o6.reference(o6.ns["ns=wire_harness_vec;i=5191"], "i=39", o6.ns["ns=wire_harness_vec;i=6152"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6153", browseName="ns=wire_harness_vec;WireElementIdDataType", dataType=o6.String, value="//xs:element[@name='WireElementIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5192"], "i=39", o6.ns["ns=wire_harness_vec;i=6153"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6154", browseName="ns=wire_harness_vec;WireElementReferenceIdDataType", dataType=o6.String, value="WireElementReferenceIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5194"], "i=39", o6.ns["ns=wire_harness_vec;i=6154"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6155",
    browseName="ns=wire_harness_vec;WireElementReferenceIdDataType",
    dataType=o6.String,
    value="//xs:element[@name='WireElementReferenceIdDataType']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5195"], "i=39", o6.ns["ns=wire_harness_vec;i=6155"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6156", browseName="ns=wire_harness_vec;WireElementSpecificationIdDataType", dataType=o6.String, value="WireElementSpecificationIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5197"], "i=39", o6.ns["ns=wire_harness_vec;i=6156"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6157",
    browseName="ns=wire_harness_vec;WireElementSpecificationIdDataType",
    dataType=o6.String,
    value="//xs:element[@name='WireElementSpecificationIdDataType']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5198"], "i=39", o6.ns["ns=wire_harness_vec;i=6157"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6160", browseName="ns=wire_harness_vec;WireEndIdDataType", dataType=o6.String, value="WireEndIdDataType")
o6.reference(o6.ns["ns=wire_harness_vec;i=5200"], "i=39", o6.ns["ns=wire_harness_vec;i=6160"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6161", browseName="ns=wire_harness_vec;WireEndIdDataType", dataType=o6.String, value="//xs:element[@name='WireEndIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5201"], "i=39", o6.ns["ns=wire_harness_vec;i=6161"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6162", browseName="ns=wire_harness_vec;WireMountingDetailIdDataType", dataType=o6.String, value="WireMountingDetailIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5203"], "i=39", o6.ns["ns=wire_harness_vec;i=6162"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6163",
    browseName="ns=wire_harness_vec;WireMountingDetailIdDataType",
    dataType=o6.String,
    value="//xs:element[@name='WireMountingDetailIdDataType']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5204"], "i=39", o6.ns["ns=wire_harness_vec;i=6163"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6164", browseName="ns=wire_harness_vec;WireMountingIdDataType", dataType=o6.String, value="WireMountingIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5206"], "i=39", o6.ns["ns=wire_harness_vec;i=6164"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6165", browseName="ns=wire_harness_vec;WireMountingIdDataType", dataType=o6.String, value="//xs:element[@name='WireMountingIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5207"], "i=39", o6.ns["ns=wire_harness_vec;i=6165"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6166", browseName="ns=wire_harness_vec;WireReceptionIdDataType", dataType=o6.String, value="WireReceptionIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5209"], "i=39", o6.ns["ns=wire_harness_vec;i=6166"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6167", browseName="ns=wire_harness_vec;WireReceptionIdDataType", dataType=o6.String, value="//xs:element[@name='WireReceptionIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5210"], "i=39", o6.ns["ns=wire_harness_vec;i=6167"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6168", browseName="ns=wire_harness_vec;WireReceptionReferenceIdDataType", dataType=o6.String, value="WireReceptionReferenceIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5212"], "i=39", o6.ns["ns=wire_harness_vec;i=6168"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6169",
    browseName="ns=wire_harness_vec;WireReceptionReferenceIdDataType",
    dataType=o6.String,
    value="//xs:element[@name='WireReceptionReferenceIdDataType']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5213"], "i=39", o6.ns["ns=wire_harness_vec;i=6169"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6170", browseName="ns=wire_harness_vec;WireReceptionSpecificationIdDataType", dataType=o6.String, value="WireReceptionSpecificationIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5215"], "i=39", o6.ns["ns=wire_harness_vec;i=6170"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6171",
    browseName="ns=wire_harness_vec;WireReceptionSpecificationIdDataType",
    dataType=o6.String,
    value="//xs:element[@name='WireReceptionSpecificationIdDataType']",
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5216"], "i=39", o6.ns["ns=wire_harness_vec;i=6171"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6172", browseName="ns=wire_harness_vec;WireRoleIdDataType", dataType=o6.String, value="WireRoleIdDataType")
o6.reference(o6.ns["ns=wire_harness_vec;i=5218"], "i=39", o6.ns["ns=wire_harness_vec;i=6172"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6173", browseName="ns=wire_harness_vec;WireRoleIdDataType", dataType=o6.String, value="//xs:element[@name='WireRoleIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5219"], "i=39", o6.ns["ns=wire_harness_vec;i=6173"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6174", browseName="ns=wire_harness_vec;WireSpecificationIdDataType", dataType=o6.String, value="WireSpecificationIdDataType"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5221"], "i=39", o6.ns["ns=wire_harness_vec;i=6174"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6175", browseName="ns=wire_harness_vec;WireSpecificationIdDataType", dataType=o6.String, value="//xs:element[@name='WireSpecificationIdDataType']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5222"], "i=39", o6.ns["ns=wire_harness_vec;i=6175"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6176", browseName="ns=wire_harness_vec;Material", dataType=o6.String, value="Material")
o6.reference(o6.ns["ns=wire_harness_vec;i=5224"], "i=39", o6.ns["ns=wire_harness_vec;i=6176"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6177", browseName="ns=wire_harness_vec;Material", dataType=o6.String, value="//xs:element[@name='Material']")
o6.reference(o6.ns["ns=wire_harness_vec;i=5225"], "i=39", o6.ns["ns=wire_harness_vec;i=6177"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6178", browseName="ns=wire_harness_vec;Size", dataType=o6.String, value="Size")
o6.reference(o6.ns["ns=wire_harness_vec;i=5227"], "i=39", o6.ns["ns=wire_harness_vec;i=6178"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6179", browseName="ns=wire_harness_vec;Size", dataType=o6.String, value="//xs:element[@name='Size']")
o6.reference(o6.ns["ns=wire_harness_vec;i=5228"], "i=39", o6.ns["ns=wire_harness_vec;i=6179"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6180", browseName="ns=wire_harness_vec;NumericalValue", dataType=o6.String, value="NumericalValue")
o6.reference(o6.ns["ns=wire_harness_vec;i=5230"], "i=39", o6.ns["ns=wire_harness_vec;i=6180"])
ns0.vartypes.DataTypeDescriptionType(
    nodeId="ns=wire_harness_vec;i=6181", browseName="ns=wire_harness_vec;NumericalValue", dataType=o6.String, value="//xs:element[@name='NumericalValue']"
)
o6.reference(o6.ns["ns=wire_harness_vec;i=5231"], "i=39", o6.ns["ns=wire_harness_vec;i=6181"])
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6182", browseName="ns=wire_harness_vec;ValueRange", dataType=o6.String, value="ValueRange")
o6.reference(o6.ns["ns=wire_harness_vec;i=5233"], "i=39", o6.ns["ns=wire_harness_vec;i=6182"])
typeDictionary = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=wire_harness_vec;i=6022",
    browseName="ns=wire_harness_vec;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/WireHarness/VEC/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(nodeId="ns=wire_harness_vec;i=6023", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/WireHarness/VEC/")
        ),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6026"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6028"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6030"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6032"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6034"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6036"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6038"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6040"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6042"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6044"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6046"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6048"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6050"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6052"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6054"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6056"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6058"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6060"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6062"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6064"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6066"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6068"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6070"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6072"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6074"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6076"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6078"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6080"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6082"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6084"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6086"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6088"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6090"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6092"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6094"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6096"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6098"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6100"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6102"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6104"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6106"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6108"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6110"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6112"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6114"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6116"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6118"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6120"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6122"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6124"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6126"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6128"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6130"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6132"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6134"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6136"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6138"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6140"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6142"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6144"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6146"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6148"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6150"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6152"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6154"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6156"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6160"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6162"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6164"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6166"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6168"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6170"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6172"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6174"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6176"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6178"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6180"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6182"]),
    ],
    parent="i=93",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<opc:TypeDictionary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://opcfoundation.org/UA/WireHarness/VEC/" DefaultByteOrder="LittleEndian" xmlns:opc="http://opcfoundation.org/BinarySchema/" xmlns:ua="http://opcfoundation.org/UA/" TargetNamespace="http://opcfoundation.org/UA/WireHarness/VEC/">\n <opc:Import Namespace="http://opcfoundation.org/UA/"/>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ARGB32ColorType">\n  <opc:Field TypeName="opc:UInt32" Name="Value"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfName"/>\n  <opc:Field LengthField="NoOfName" TypeName="opc:CharArray" Name="Name"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ExtendableElement">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ExtendableElement" Name="BoundingBox">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="X"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="Y"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="Z"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ExtendableElement" Name="ConfigurableElement">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ConfigurableElement" Name="ContactPoint">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfMountedTerminal"/>\n  <opc:Field LengthField="NoOfMountedTerminal" TypeName="ua:ExtensionObject" Name="MountedTerminal"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfWireMounting"/>\n  <opc:Field LengthField="NoOfWireMounting" TypeName="ua:ExtensionObject" Name="WireMounting"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ConfigurableElement" Name="OccurrenceOrUsage">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfRole"/>\n  <opc:Field LengthField="NoOfRole" TypeName="ua:ExtensionObject" Name="Role"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:OccurrenceOrUsage" Name="PartOccurrence">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:OccurrenceOrUsage" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field SourceType="tns:OccurrenceOrUsage" TypeName="opc:Int32" Name="NoOfRole"/>\n  <opc:Field LengthField="NoOfRole" SourceType="tns:OccurrenceOrUsage" TypeName="ua:ExtensionObject" Name="Role"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfPart"/>\n  <opc:Field LengthField="NoOfPart" TypeName="ua:ExtensionObject" Name="Part"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ConfigurableElement" Name="RoutableElement">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:RoutableElement" Name="WireElementReference">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="ReferencedWireElement"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfWireEnd"/>\n  <opc:Field LengthField="NoOfWireEnd" TypeName="ua:ExtensionObject" Name="WireEnd"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfWireLength"/>\n  <opc:Field LengthField="NoOfWireLength" TypeName="ua:ExtensionObject" Name="WireLength"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ExtendableElement" Name="CrimpDetail">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfSize"/>\n  <opc:Field LengthField="NoOfSize" TypeName="ua:ExtensionObject" Name="Size"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:CrimpDetail" Name="CoreCrimpDetail">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:CrimpDetail" TypeName="opc:Int32" Name="NoOfSize"/>\n  <opc:Field LengthField="NoOfSize" SourceType="tns:CrimpDetail" TypeName="ua:ExtensionObject" Name="Size"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="AppliesTo"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfInsulationCrimpDetails"/>\n  <opc:Field LengthField="NoOfInsulationCrimpDetails" TypeName="ua:ExtensionObject" Name="InsulationCrimpDetails"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfPullOffForce"/>\n  <opc:Field LengthField="NoOfPullOffForce" TypeName="ua:ExtensionObject" Name="PullOffForce"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:CrimpDetail" Name="InsulationCrimpDetail">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:CrimpDetail" TypeName="opc:Int32" Name="NoOfSize"/>\n  <opc:Field LengthField="NoOfSize" SourceType="tns:CrimpDetail" TypeName="ua:ExtensionObject" Name="Size"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfPullOffForce"/>\n  <opc:Field LengthField="NoOfPullOffForce" TypeName="ua:ExtensionObject" Name="PullOffForce"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="AppliesTo"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ExtendableElement" Name="ItemVersion">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfCompanyName"/>\n  <opc:Field LengthField="NoOfCompanyName" TypeName="opc:CharArray" Name="CompanyName"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ItemVersion" Name="DocumentVersion">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:ItemVersion" TypeName="opc:Int32" Name="NoOfCompanyName"/>\n  <opc:Field LengthField="NoOfCompanyName" SourceType="tns:ItemVersion" TypeName="opc:CharArray" Name="CompanyName"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfDocumentNumber"/>\n  <opc:Field LengthField="NoOfDocumentNumber" TypeName="opc:CharArray" Name="DocumentNumber"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfDocumentVersion"/>\n  <opc:Field LengthField="NoOfDocumentVersion" TypeName="opc:CharArray" Name="DocumentVersion"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfDigitalRepresentationIndex"/>\n  <opc:Field LengthField="NoOfDigitalRepresentationIndex" TypeName="opc:CharArray" Name="DigitalRepresentationIndex"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfSpecification"/>\n  <opc:Field LengthField="NoOfSpecification" TypeName="ua:ExtensionObject" Name="Specification"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ItemVersion" Name="PartVersion">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:ItemVersion" TypeName="opc:Int32" Name="NoOfCompanyName"/>\n  <opc:Field LengthField="NoOfCompanyName" SourceType="tns:ItemVersion" TypeName="opc:CharArray" Name="CompanyName"/>\n  <opc:Field TypeName="opc:CharArray" Name="PartNumber"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ItemVersion" Name="ResourceVersion">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:ItemVersion" TypeName="opc:Int32" Name="NoOfCompanyName"/>\n  <opc:Field LengthField="NoOfCompanyName" SourceType="tns:ItemVersion" TypeName="opc:CharArray" Name="CompanyName"/>\n  <opc:Field TypeName="opc:CharArray" Name="ResourceNumber"/>\n  <opc:Field TypeName="opc:CharArray" Name="ResourceVersion"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ExtendableElement" Name="Role">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" TypeName="opc:CharArray" Name="Identification"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:Role" Name="CavityPartRole">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:Role" TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" SourceType="tns:Role" TypeName="opc:CharArray" Name="Identification"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:CavityPartRole" Name="CavitySealRole">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:Role" TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" SourceType="tns:Role" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="CavitySealSpecification"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:Role" Name="TerminalRole">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:Role" TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" SourceType="tns:Role" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="TerminalSpecification"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfWireReceptionReference"/>\n  <opc:Field LengthField="NoOfWireReceptionReference" TypeName="ua:ExtensionObject" Name="WireReceptionReference"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:TerminalRole" Name="PluggableTerminalRole">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:Role" TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" SourceType="tns:Role" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field SourceType="tns:TerminalRole" TypeName="ua:ExtensionObject" Name="TerminalSpecification"/>\n  <opc:Field SourceType="tns:TerminalRole" TypeName="opc:Int32" Name="NoOfWireReceptionReference"/>\n  <opc:Field LengthField="NoOfWireReceptionReference" SourceType="tns:TerminalRole" TypeName="ua:ExtensionObject" Name="WireReceptionReference"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:Role" Name="WireRole">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:Role" TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" SourceType="tns:Role" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="WireSpecification"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfWireElementReference"/>\n  <opc:Field LengthField="NoOfWireElementReference" TypeName="ua:ExtensionObject" Name="WireElementReference"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ExtendableElement" Name="Specification">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" TypeName="opc:CharArray" Name="Identification"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:Specification" Name="CompositionSpecification">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:Specification" TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" SourceType="tns:Specification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfComponent"/>\n  <opc:Field LengthField="NoOfComponent" TypeName="ua:ExtensionObject" Name="Component"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:Specification" Name="ConductorSpecification">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:Specification" TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" SourceType="tns:Specification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfCrossSectionArea"/>\n  <opc:Field LengthField="NoOfCrossSectionArea" TypeName="ua:ExtensionObject" Name="CrossSectionArea"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfType"/>\n  <opc:Field LengthField="NoOfType" TypeName="tns:ConductorType" Name="Type"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ConductorSpecification" Name="CoreSpecification">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:Specification" TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" SourceType="tns:Specification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field SourceType="tns:ConductorSpecification" TypeName="opc:Int32" Name="NoOfCrossSectionArea"/>\n  <opc:Field LengthField="NoOfCrossSectionArea" SourceType="tns:ConductorSpecification" TypeName="ua:ExtensionObject" Name="CrossSectionArea"/>\n  <opc:Field SourceType="tns:ConductorSpecification" TypeName="opc:Int32" Name="NoOfType"/>\n  <opc:Field LengthField="NoOfType" SourceType="tns:ConductorSpecification" TypeName="tns:ConductorType" Name="Type"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfOutsideDiameter"/>\n  <opc:Field LengthField="NoOfOutsideDiameter" TypeName="ua:ExtensionObject" Name="OutsideDiameter"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:Specification" Name="ContactingSpecification">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:Specification" TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" SourceType="tns:Specification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfContactPoint"/>\n  <opc:Field LengthField="NoOfContactPoint" TypeName="ua:ExtensionObject" Name="ContactPoint"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:Specification" Name="InsulationSpecification">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:Specification" TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" SourceType="tns:Specification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="BaseColor"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfFirstIdentificationColor"/>\n  <opc:Field LengthField="NoOfFirstIdentificationColor" TypeName="ua:ExtensionObject" Name="FirstIdentificationColor"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfSecondIdentificationColor"/>\n  <opc:Field LengthField="NoOfSecondIdentificationColor" TypeName="ua:ExtensionObject" Name="SecondIdentificationColor"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfThickness"/>\n  <opc:Field LengthField="NoOfThickness" TypeName="ua:ExtensionObject" Name="Thickness"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:Specification" Name="PartOrUsageRelatedSpecification">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:Specification" TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" SourceType="tns:Specification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfSpecialPartType"/>\n  <opc:Field LengthField="NoOfSpecialPartType" TypeName="opc:CharArray" Name="SpecialPartType"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfDescribedPart"/>\n  <opc:Field LengthField="NoOfDescribedPart" TypeName="ua:ExtensionObject" Name="DescribedPart"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:PartOrUsageRelatedSpecification" Name="CavityPartSpecification">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:Specification" TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" SourceType="tns:Specification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field SourceType="tns:PartOrUsageRelatedSpecification" TypeName="opc:Int32" Name="NoOfSpecialPartType"/>\n  <opc:Field LengthField="NoOfSpecialPartType" SourceType="tns:PartOrUsageRelatedSpecification" TypeName="opc:CharArray" Name="SpecialPartType"/>\n  <opc:Field SourceType="tns:PartOrUsageRelatedSpecification" TypeName="opc:Int32" Name="NoOfDescribedPart"/>\n  <opc:Field LengthField="NoOfDescribedPart" SourceType="tns:PartOrUsageRelatedSpecification" TypeName="ua:ExtensionObject" Name="DescribedPart"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:CavityPartSpecification" Name="CavitySealSpecification">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:Specification" TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" SourceType="tns:Specification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field SourceType="tns:PartOrUsageRelatedSpecification" TypeName="opc:Int32" Name="NoOfSpecialPartType"/>\n  <opc:Field LengthField="NoOfSpecialPartType" SourceType="tns:PartOrUsageRelatedSpecification" TypeName="opc:CharArray" Name="SpecialPartType"/>\n  <opc:Field SourceType="tns:PartOrUsageRelatedSpecification" TypeName="opc:Int32" Name="NoOfDescribedPart"/>\n  <opc:Field LengthField="NoOfDescribedPart" SourceType="tns:PartOrUsageRelatedSpecification" TypeName="ua:ExtensionObject" Name="DescribedPart"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:PartOrUsageRelatedSpecification" Name="GeneralTechnicalPartSpecification">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:Specification" TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" SourceType="tns:Specification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field SourceType="tns:PartOrUsageRelatedSpecification" TypeName="opc:Int32" Name="NoOfSpecialPartType"/>\n  <opc:Field LengthField="NoOfSpecialPartType" SourceType="tns:PartOrUsageRelatedSpecification" TypeName="opc:CharArray" Name="SpecialPartType"/>\n  <opc:Field SourceType="tns:PartOrUsageRelatedSpecification" TypeName="opc:Int32" Name="NoOfDescribedPart"/>\n  <opc:Field LengthField="NoOfDescribedPart" SourceType="tns:PartOrUsageRelatedSpecification" TypeName="ua:ExtensionObject" Name="DescribedPart"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfColorInformation"/>\n  <opc:Field LengthField="NoOfColorInformation" TypeName="ua:ExtensionObject" Name="ColorInformation"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfBoundingBox"/>\n  <opc:Field LengthField="NoOfBoundingBox" TypeName="ua:ExtensionObject" Name="BoundingBox"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:PartOrUsageRelatedSpecification" Name="TerminalSpecification">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:Specification" TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" SourceType="tns:Specification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field SourceType="tns:PartOrUsageRelatedSpecification" TypeName="opc:Int32" Name="NoOfSpecialPartType"/>\n  <opc:Field LengthField="NoOfSpecialPartType" SourceType="tns:PartOrUsageRelatedSpecification" TypeName="opc:CharArray" Name="SpecialPartType"/>\n  <opc:Field SourceType="tns:PartOrUsageRelatedSpecification" TypeName="opc:Int32" Name="NoOfDescribedPart"/>\n  <opc:Field LengthField="NoOfDescribedPart" SourceType="tns:PartOrUsageRelatedSpecification" TypeName="ua:ExtensionObject" Name="DescribedPart"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfConnectionALength"/>\n  <opc:Field LengthField="NoOfConnectionALength" TypeName="ua:ExtensionObject" Name="ConnectionALength"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="OverallLength"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfWireReception"/>\n  <opc:Field LengthField="NoOfWireReception" TypeName="ua:ExtensionObject" Name="WireReception"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:TerminalSpecification" Name="PluggableTerminalSpecification">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:Specification" TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" SourceType="tns:Specification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field SourceType="tns:PartOrUsageRelatedSpecification" TypeName="opc:Int32" Name="NoOfSpecialPartType"/>\n  <opc:Field LengthField="NoOfSpecialPartType" SourceType="tns:PartOrUsageRelatedSpecification" TypeName="opc:CharArray" Name="SpecialPartType"/>\n  <opc:Field SourceType="tns:PartOrUsageRelatedSpecification" TypeName="opc:Int32" Name="NoOfDescribedPart"/>\n  <opc:Field LengthField="NoOfDescribedPart" SourceType="tns:PartOrUsageRelatedSpecification" TypeName="ua:ExtensionObject" Name="DescribedPart"/>\n  <opc:Field SourceType="tns:TerminalSpecification" TypeName="opc:Int32" Name="NoOfConnectionALength"/>\n  <opc:Field LengthField="NoOfConnectionALength" SourceType="tns:TerminalSpecification" TypeName="ua:ExtensionObject" Name="ConnectionALength"/>\n  <opc:Field SourceType="tns:TerminalSpecification" TypeName="ua:ExtensionObject" Name="OverallLength"/>\n  <opc:Field SourceType="tns:TerminalSpecification" TypeName="opc:Int32" Name="NoOfWireReception"/>\n  <opc:Field LengthField="NoOfWireReception" SourceType="tns:TerminalSpecification" TypeName="ua:ExtensionObject" Name="WireReception"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:PartOrUsageRelatedSpecification" Name="WireSpecification">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:Specification" TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" SourceType="tns:Specification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field SourceType="tns:PartOrUsageRelatedSpecification" TypeName="opc:Int32" Name="NoOfSpecialPartType"/>\n  <opc:Field LengthField="NoOfSpecialPartType" SourceType="tns:PartOrUsageRelatedSpecification" TypeName="opc:CharArray" Name="SpecialPartType"/>\n  <opc:Field SourceType="tns:PartOrUsageRelatedSpecification" TypeName="opc:Int32" Name="NoOfDescribedPart"/>\n  <opc:Field LengthField="NoOfDescribedPart" SourceType="tns:PartOrUsageRelatedSpecification" TypeName="ua:ExtensionObject" Name="DescribedPart"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="WireElement"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:Specification" Name="WireElementSpecification">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:Specification" TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" SourceType="tns:Specification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfOutsideDiameter"/>\n  <opc:Field LengthField="NoOfOutsideDiameter" TypeName="ua:ExtensionObject" Name="OutsideDiameter"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfConductorSpecification"/>\n  <opc:Field LengthField="NoOfConductorSpecification" TypeName="ua:ExtensionObject" Name="ConductorSpecification"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfInsulationSpecification"/>\n  <opc:Field LengthField="NoOfInsulationSpecification" TypeName="ua:ExtensionObject" Name="InsulationSpecification"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:Specification" Name="WireReceptionSpecification">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field SourceType="tns:Specification" TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" SourceType="tns:Specification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="InsulationDisplacementLength"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfConductorCrimpLength"/>\n  <opc:Field LengthField="NoOfConductorCrimpLength" TypeName="ua:ExtensionObject" Name="ConductorCrimpLength"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="CrimpConnectionLength"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfInsulationCrimpLength"/>\n  <opc:Field LengthField="NoOfInsulationCrimpLength" TypeName="ua:ExtensionObject" Name="InsulationCrimpLength"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfWireTipProtrusion"/>\n  <opc:Field LengthField="NoOfWireTipProtrusion" TypeName="ua:ExtensionObject" Name="WireTipProtrusion"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfCoreCrimpDetails"/>\n  <opc:Field LengthField="NoOfCoreCrimpDetails" TypeName="ua:ExtensionObject" Name="CoreCrimpDetails"/>\n  <opc:Field TypeName="tns:CrimpBarrelType" Name="CrimpBarrelType"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ExtendableElement" Name="Tolerance">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field TypeName="opc:Double" Name="LowerBoundary"/>\n  <opc:Field TypeName="opc:Double" Name="UpperBoundary"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ExtendableElement" Name="WireElement">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="WireElementSpecification"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfSubWireElement"/>\n  <opc:Field LengthField="NoOfSubWireElement" TypeName="ua:ExtensionObject" Name="SubWireElement"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ExtendableElement" Name="WireEnd">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field TypeName="opc:Double" Name="PositionOnWire"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfStrippingLength"/>\n  <opc:Field LengthField="NoOfStrippingLength" TypeName="ua:ExtensionObject" Name="StrippingLength"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfInsulationPullbackLength"/>\n  <opc:Field LengthField="NoOfInsulationPullbackLength" TypeName="ua:ExtensionObject" Name="InsulationPullbackLength"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ExtendableElement" Name="WireMounting">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfMountedCavitySeal"/>\n  <opc:Field LengthField="NoOfMountedCavitySeal" TypeName="ua:ExtensionObject" Name="MountedCavitySeal"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfReferencedWireEnd"/>\n  <opc:Field LengthField="NoOfReferencedWireEnd" TypeName="ua:ExtensionObject" Name="ReferencedWireEnd"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfWireMountingDetail"/>\n  <opc:Field LengthField="NoOfWireMountingDetail" TypeName="ua:ExtensionObject" Name="WireMountingDetail"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ExtendableElement" Name="WireMountingDetail">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfCoreCrimpSize"/>\n  <opc:Field LengthField="NoOfCoreCrimpSize" TypeName="ua:ExtensionObject" Name="CoreCrimpSize"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfInsulationCrimpSize"/>\n  <opc:Field LengthField="NoOfInsulationCrimpSize" TypeName="ua:ExtensionObject" Name="InsulationCrimpSize"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfWireTipProtrusion"/>\n  <opc:Field LengthField="NoOfWireTipProtrusion" TypeName="ua:ExtensionObject" Name="WireTipProtrusion"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="ContactedWireReception"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfReferencedWireEnd"/>\n  <opc:Field LengthField="NoOfReferencedWireEnd" TypeName="ua:ExtensionObject" Name="ReferencedWireEnd"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="AbsoluteSealPosition"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfCorePullOffForce"/>\n  <opc:Field LengthField="NoOfCorePullOffForce" TypeName="ua:ExtensionObject" Name="CorePullOffForce"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ExtendableElement" Name="WireReception">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfRotation"/>\n  <opc:Field LengthField="NoOfRotation" TypeName="ua:ExtensionObject" Name="Rotation"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="WireReceptionSpecification"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ExtendableElement" Name="WireReceptionReference">\n  <opc:Field SourceType="tns:ExtendableElement" TypeName="opc:CharArray" Name="id"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfIdentification"/>\n  <opc:Field LengthField="NoOfIdentification" TypeName="opc:CharArray" Name="Identification"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="WireReception"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="IdBaseDataType"/>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="CavityPartRoleIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="CavityPartSpecificationIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="CavitySealRoleIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="CavitySealSpecificationIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="CompositionSpecificationIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="ConductorSpecificationIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="ConfigurableElementIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="ContactingSpecificationIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="ContactPointIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="CoreCrimpDetailIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="CoreSpecificationIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="CrimpDetailIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="DocumentVersionIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="ExtendableElementIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="GeneralTechnicalPartSpecificationIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="InsulationCrimpDetailIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="InsulationSpecificationIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="ItemVersionIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="OccurrenceOrUsageIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="PartOccurrenceIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="PartOrUsageRelatedSpecificationIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="PartVersionIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="PluggableTerminalRoleIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="PluggableTerminalSpecificationIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="ResourceVersionIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="RoleIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="RoutableElementIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="SpecificationIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="TerminalRoleIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="TerminalSpecificationIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="WireElementIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="WireElementReferenceIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="WireElementSpecificationIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="WireEndIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="WireMountingDetailIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="WireMountingIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="WireReceptionIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="WireReceptionReferenceIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="WireReceptionSpecificationIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="WireRoleIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:IdBaseDataType" Name="WireSpecificationIdDataType">\n  <opc:Field TypeName="opc:CharArray" Name="id"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="Material">\n  <opc:Field TypeName="opc:CharArray" Name="Key"/>\n  <opc:Field TypeName="opc:CharArray" Name="ReferenceSystem"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="Size">\n  <opc:Field TypeName="ua:ExtensionObject" Name="Width"/>\n  <opc:Field TypeName="ua:ExtensionObject" Name="Height"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="ua:ExtensionObject" Name="ValueWithUnit">\n  <opc:Field TypeName="ua:ExtensionObject" Name="UnitComponent"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ValueWithUnit" Name="NumericalValue">\n  <opc:Field SourceType="tns:ValueWithUnit" TypeName="ua:ExtensionObject" Name="UnitComponent"/>\n  <opc:Field TypeName="opc:Double" Name="ValueComponent"/>\n  <opc:Field TypeName="opc:Int32" Name="NoOfTolerance"/>\n  <opc:Field LengthField="NoOfTolerance" TypeName="ua:ExtensionObject" Name="Tolerance"/>\n </opc:StructuredType>\n <opc:StructuredType BaseType="tns:ValueWithUnit" Name="ValueRange">\n  <opc:Field SourceType="tns:ValueWithUnit" TypeName="ua:ExtensionObject" Name="UnitComponent"/>\n  <opc:Field TypeName="opc:Double" Name="Minimum"/>\n  <opc:Field TypeName="opc:Double" Name="Maximum"/>\n </opc:StructuredType>\n <opc:EnumeratedType LengthInBits="32" Name="ConductorType">\n  <opc:EnumeratedValue Name="Rigid" Value="0"/>\n  <opc:EnumeratedValue Name="Stranded" Value="1"/>\n  <opc:EnumeratedValue Name="Foil" Value="2"/>\n  <opc:EnumeratedValue Name="Braided" Value="3"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="CrimpBarrelType">\n  <opc:EnumeratedValue Name="Open" Value="0"/>\n  <opc:EnumeratedValue Name="Closed" Value="1"/>\n </opc:EnumeratedType>\n <opc:EnumeratedType LengthInBits="32" Name="PrimaryPartType">\n  <opc:EnumeratedValue Name="Antenna" Value="0"/>\n  <opc:EnumeratedValue Name="Battery" Value="1"/>\n  <opc:EnumeratedValue Name="BoltMountedFixing" Value="2"/>\n  <opc:EnumeratedValue Name="BoltTerminal" Value="3"/>\n  <opc:EnumeratedValue Name="BridgeTerminal" Value="4"/>\n  <opc:EnumeratedValue Name="CableDuct" Value="5"/>\n  <opc:EnumeratedValue Name="CableTie" Value="6"/>\n  <opc:EnumeratedValue Name="Capacitor" Value="7"/>\n  <opc:EnumeratedValue Name="CavityAccessory" Value="8"/>\n  <opc:EnumeratedValue Name="CavityPlug" Value="9"/>\n  <opc:EnumeratedValue Name="CavitySeal" Value="10"/>\n  <opc:EnumeratedValue Name="ConnectorHousing" Value="11"/>\n  <opc:EnumeratedValue Name="ConnectorHousingCap" Value="12"/>\n  <opc:EnumeratedValue Name="ConnectorHousingCover" Value="13"/>\n  <opc:EnumeratedValue Name="CorrugatedPipe" Value="14"/>\n  <opc:EnumeratedValue Name="Diode" Value="15"/>\n  <opc:EnumeratedValue Name="EdgeMountedFixing" Value="16"/>\n  <opc:EnumeratedValue Name="EEComponent" Value="17"/>\n  <opc:EnumeratedValue Name="Ferrite" Value="18"/>\n  <opc:EnumeratedValue Name="Fitting" Value="19"/>\n  <opc:EnumeratedValue Name="Fixing" Value="20"/>\n  <opc:EnumeratedValue Name="Fuse" Value="21"/>\n  <opc:EnumeratedValue Name="Grommet" Value="22"/>\n  <opc:EnumeratedValue Name="HoleMountedFixing" Value="23"/>\n  <opc:EnumeratedValue Name="MultiCavityPlug" Value="24"/>\n  <opc:EnumeratedValue Name="MultiCavitySeal" Value="25"/>\n  <opc:EnumeratedValue Name="MultiFuse" Value="26"/>\n  <opc:EnumeratedValue Name="Other" Value="27"/>\n  <opc:EnumeratedValue Name="OpenWireEndTerminal" Value="28"/>\n  <opc:EnumeratedValue Name="OpenWireEnd" Value="29"/>\n  <opc:EnumeratedValue Name="PartStructure" Value="30"/>\n  <opc:EnumeratedValue Name="PluggableTerminal" Value="31"/>\n  <opc:EnumeratedValue Name="PotentialDistributor" Value="32"/>\n  <opc:EnumeratedValue Name="Relay" Value="33"/>\n  <opc:EnumeratedValue Name="RingTerminal" Value="34"/>\n  <opc:EnumeratedValue Name="ShrinkableTube" Value="35"/>\n  <opc:EnumeratedValue Name="SpliceTerminal" Value="36"/>\n  <opc:EnumeratedValue Name="Stripe" Value="37"/>\n  <opc:EnumeratedValue Name="Tape" Value="38"/>\n  <opc:EnumeratedValue Name="Terminal" Value="39"/>\n  <opc:EnumeratedValue Name="Tube" Value="40"/>\n  <opc:EnumeratedValue Name="Wire" Value="41"/>\n  <opc:EnumeratedValue Name="WireEndAccessory" Value="42"/>\n  <opc:EnumeratedValue Name="WireProtection" Value="43"/>\n </opc:EnumeratedType>\n</opc:TypeDictionary>\n',
)
ns0.vartypes.DataTypeDescriptionType(nodeId="ns=wire_harness_vec;i=6183", browseName="ns=wire_harness_vec;ValueRange", dataType=o6.String, value="//xs:element[@name='ValueRange']")
o6.reference(o6.ns["ns=wire_harness_vec;i=5234"], "i=39", o6.ns["ns=wire_harness_vec;i=6183"])
typeDictionary_2 = ns0.vartypes.DataTypeDictionaryType(
    nodeId="ns=wire_harness_vec;i=6024",
    browseName="ns=wire_harness_vec;TypeDictionary",
    description="Collects the data type descriptions of http://opcfoundation.org/UA/WireHarness/VEC/",
    references=[
        o6.hasProperty(
            ns0.vartypes.PropertyType(
                nodeId="ns=wire_harness_vec;i=6025", browseName="NamespaceUri", dataType=o6.String, value="http://opcfoundation.org/UA/WireHarness/VEC/Types.xsd"
            )
        ),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6027"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6029"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6031"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6033"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6035"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6037"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6039"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6041"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6043"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6045"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6047"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6049"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6051"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6053"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6055"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6057"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6059"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6061"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6063"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6065"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6067"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6069"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6071"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6073"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6075"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6077"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6079"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6081"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6083"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6085"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6087"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6089"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6091"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6093"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6095"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6097"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6099"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6101"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6103"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6105"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6107"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6109"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6111"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6113"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6115"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6117"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6119"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6121"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6123"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6125"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6127"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6129"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6131"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6133"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6135"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6137"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6139"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6141"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6143"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6145"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6147"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6149"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6151"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6153"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6155"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6157"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6161"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6163"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6165"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6167"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6169"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6171"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6173"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6175"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6177"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6179"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6181"]),
        o6.hasComponent(o6.ns["ns=wire_harness_vec;i=6183"]),
    ],
    parent="i=92",
    referenceType=ns0.reftypes.HasComponent,
    dataType=o6.ByteString,
    value=b'<xs:schema elementFormDefault="qualified" targetNamespace="http://opcfoundation.org/UA/WireHarness/VEC/Types.xsd" xmlns:tns="http://opcfoundation.org/UA/WireHarness/VEC/Types.xsd" xmlns:ua="http://opcfoundation.org/UA/2008/02/Types.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema">\n <xs:import namespace="http://opcfoundation.org/UA/2008/02/Types.xsd"/>\n <xs:simpleType name="ConductorType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Rigid_0"/>\n   <xs:enumeration value="Stranded_1"/>\n   <xs:enumeration value="Foil_2"/>\n   <xs:enumeration value="Braided_3"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:ConductorType" name="ConductorType"/>\n <xs:complexType name="ListOfConductorType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ConductorType" name="ConductorType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfConductorType" name="ListOfConductorType" nillable="true"/>\n <xs:simpleType name="CrimpBarrelType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Open_0"/>\n   <xs:enumeration value="Closed_1"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:CrimpBarrelType" name="CrimpBarrelType"/>\n <xs:complexType name="ListOfCrimpBarrelType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CrimpBarrelType" name="CrimpBarrelType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCrimpBarrelType" name="ListOfCrimpBarrelType" nillable="true"/>\n <xs:simpleType name="PrimaryPartType">\n  <xs:restriction base="xs:string">\n   <xs:enumeration value="Antenna_0"/>\n   <xs:enumeration value="Battery_1"/>\n   <xs:enumeration value="BoltMountedFixing_2"/>\n   <xs:enumeration value="BoltTerminal_3"/>\n   <xs:enumeration value="BridgeTerminal_4"/>\n   <xs:enumeration value="CableDuct_5"/>\n   <xs:enumeration value="CableTie_6"/>\n   <xs:enumeration value="Capacitor_7"/>\n   <xs:enumeration value="CavityAccessory_8"/>\n   <xs:enumeration value="CavityPlug_9"/>\n   <xs:enumeration value="CavitySeal_10"/>\n   <xs:enumeration value="ConnectorHousing_11"/>\n   <xs:enumeration value="ConnectorHousingCap_12"/>\n   <xs:enumeration value="ConnectorHousingCover_13"/>\n   <xs:enumeration value="CorrugatedPipe_14"/>\n   <xs:enumeration value="Diode_15"/>\n   <xs:enumeration value="EdgeMountedFixing_16"/>\n   <xs:enumeration value="EEComponent_17"/>\n   <xs:enumeration value="Ferrite_18"/>\n   <xs:enumeration value="Fitting_19"/>\n   <xs:enumeration value="Fixing_20"/>\n   <xs:enumeration value="Fuse_21"/>\n   <xs:enumeration value="Grommet_22"/>\n   <xs:enumeration value="HoleMountedFixing_23"/>\n   <xs:enumeration value="MultiCavityPlug_24"/>\n   <xs:enumeration value="MultiCavitySeal_25"/>\n   <xs:enumeration value="MultiFuse_26"/>\n   <xs:enumeration value="Other_27"/>\n   <xs:enumeration value="OpenWireEndTerminal_28"/>\n   <xs:enumeration value="OpenWireEnd_29"/>\n   <xs:enumeration value="PartStructure_30"/>\n   <xs:enumeration value="PluggableTerminal_31"/>\n   <xs:enumeration value="PotentialDistributor_32"/>\n   <xs:enumeration value="Relay_33"/>\n   <xs:enumeration value="RingTerminal_34"/>\n   <xs:enumeration value="ShrinkableTube_35"/>\n   <xs:enumeration value="SpliceTerminal_36"/>\n   <xs:enumeration value="Stripe_37"/>\n   <xs:enumeration value="Tape_38"/>\n   <xs:enumeration value="Terminal_39"/>\n   <xs:enumeration value="Tube_40"/>\n   <xs:enumeration value="Wire_41"/>\n   <xs:enumeration value="WireEndAccessory_42"/>\n   <xs:enumeration value="WireProtection_43"/>\n  </xs:restriction>\n </xs:simpleType>\n <xs:element type="tns:PrimaryPartType" name="PrimaryPartType"/>\n <xs:complexType name="ListOfPrimaryPartType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PrimaryPartType" name="PrimaryPartType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPrimaryPartType" name="ListOfPrimaryPartType" nillable="true"/>\n <xs:complexType name="ARGB32ColorType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:unsignedInt" name="Value"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="Name"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ARGB32ColorType" name="ARGB32ColorType"/>\n <xs:complexType name="ListOfARGB32ColorType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ARGB32ColorType" name="ARGB32ColorType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfARGB32ColorType" name="ListOfARGB32ColorType" nillable="true"/>\n <xs:complexType name="ExtendableElement">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ExtendableElement" name="ExtendableElement"/>\n <xs:complexType name="ListOfExtendableElement">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ExtendableElement" name="ExtendableElement" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfExtendableElement" name="ListOfExtendableElement" nillable="true"/>\n <xs:complexType name="BoundingBox">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="X"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="Y"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="Z"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:BoundingBox" name="BoundingBox"/>\n <xs:complexType name="ListOfBoundingBox">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:BoundingBox" name="BoundingBox" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfBoundingBox" name="ListOfBoundingBox" nillable="true"/>\n <xs:complexType name="ConfigurableElement">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence/>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:ConfigurableElement" name="ConfigurableElement"/>\n <xs:complexType name="ListOfConfigurableElement">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ConfigurableElement" name="ConfigurableElement" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfConfigurableElement" name="ListOfConfigurableElement" nillable="true"/>\n <xs:complexType name="ContactPoint">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="Identification"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="MountedTerminal"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="WireMounting"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:ContactPoint" name="ContactPoint"/>\n <xs:complexType name="ListOfContactPoint">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ContactPoint" name="ContactPoint" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfContactPoint" name="ListOfContactPoint" nillable="true"/>\n <xs:complexType name="OccurrenceOrUsage">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Identification"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="Role"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:OccurrenceOrUsage" name="OccurrenceOrUsage"/>\n <xs:complexType name="ListOfOccurrenceOrUsage">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OccurrenceOrUsage" name="OccurrenceOrUsage" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOccurrenceOrUsage" name="ListOfOccurrenceOrUsage" nillable="true"/>\n <xs:complexType name="PartOccurrence">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="Part"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:PartOccurrence" name="PartOccurrence"/>\n <xs:complexType name="ListOfPartOccurrence">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PartOccurrence" name="PartOccurrence" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPartOccurrence" name="ListOfPartOccurrence" nillable="true"/>\n <xs:complexType name="RoutableElement">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence/>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:RoutableElement" name="RoutableElement"/>\n <xs:complexType name="ListOfRoutableElement">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RoutableElement" name="RoutableElement" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRoutableElement" name="ListOfRoutableElement" nillable="true"/>\n <xs:complexType name="WireElementReference">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="Identification"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="ReferencedWireElement"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="WireEnd"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="WireLength"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireElementReference" name="WireElementReference"/>\n <xs:complexType name="ListOfWireElementReference">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireElementReference" name="WireElementReference" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireElementReference" name="ListOfWireElementReference" nillable="true"/>\n <xs:complexType name="CrimpDetail">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="Size"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CrimpDetail" name="CrimpDetail"/>\n <xs:complexType name="ListOfCrimpDetail">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CrimpDetail" name="CrimpDetail" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCrimpDetail" name="ListOfCrimpDetail" nillable="true"/>\n <xs:complexType name="CoreCrimpDetail">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="AppliesTo"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="InsulationCrimpDetails"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="PullOffForce"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CoreCrimpDetail" name="CoreCrimpDetail"/>\n <xs:complexType name="ListOfCoreCrimpDetail">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CoreCrimpDetail" name="CoreCrimpDetail" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCoreCrimpDetail" name="ListOfCoreCrimpDetail" nillable="true"/>\n <xs:complexType name="InsulationCrimpDetail">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="PullOffForce"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="AppliesTo"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:InsulationCrimpDetail" name="InsulationCrimpDetail"/>\n <xs:complexType name="ListOfInsulationCrimpDetail">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:InsulationCrimpDetail" name="InsulationCrimpDetail" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfInsulationCrimpDetail" name="ListOfInsulationCrimpDetail" nillable="true"/>\n <xs:complexType name="ItemVersion">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="CompanyName"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:ItemVersion" name="ItemVersion"/>\n <xs:complexType name="ListOfItemVersion">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ItemVersion" name="ItemVersion" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfItemVersion" name="ListOfItemVersion" nillable="true"/>\n <xs:complexType name="DocumentVersion">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="DocumentNumber"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="DocumentVersion"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="DigitalRepresentationIndex"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="Specification"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:DocumentVersion" name="DocumentVersion"/>\n <xs:complexType name="ListOfDocumentVersion">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:DocumentVersion" name="DocumentVersion" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfDocumentVersion" name="ListOfDocumentVersion" nillable="true"/>\n <xs:complexType name="PartVersion">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="PartNumber"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:PartVersion" name="PartVersion"/>\n <xs:complexType name="ListOfPartVersion">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PartVersion" name="PartVersion" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPartVersion" name="ListOfPartVersion" nillable="true"/>\n <xs:complexType name="ResourceVersion">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ResourceNumber"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ResourceVersion"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:ResourceVersion" name="ResourceVersion"/>\n <xs:complexType name="ListOfResourceVersion">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ResourceVersion" name="ResourceVersion" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfResourceVersion" name="ListOfResourceVersion" nillable="true"/>\n <xs:complexType name="Role">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="Identification"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:Role" name="Role"/>\n <xs:complexType name="ListOfRole">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:Role" name="Role" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRole" name="ListOfRole" nillable="true"/>\n <xs:complexType name="CavityPartRole">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence/>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CavityPartRole" name="CavityPartRole"/>\n <xs:complexType name="ListOfCavityPartRole">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CavityPartRole" name="CavityPartRole" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCavityPartRole" name="ListOfCavityPartRole" nillable="true"/>\n <xs:complexType name="CavitySealRole">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="CavitySealSpecification"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CavitySealRole" name="CavitySealRole"/>\n <xs:complexType name="ListOfCavitySealRole">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CavitySealRole" name="CavitySealRole" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCavitySealRole" name="ListOfCavitySealRole" nillable="true"/>\n <xs:complexType name="TerminalRole">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="TerminalSpecification"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="WireReceptionReference"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:TerminalRole" name="TerminalRole"/>\n <xs:complexType name="ListOfTerminalRole">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:TerminalRole" name="TerminalRole" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfTerminalRole" name="ListOfTerminalRole" nillable="true"/>\n <xs:complexType name="PluggableTerminalRole">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:TerminalRole">\n    <xs:sequence/>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:PluggableTerminalRole" name="PluggableTerminalRole"/>\n <xs:complexType name="ListOfPluggableTerminalRole">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PluggableTerminalRole" name="PluggableTerminalRole" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPluggableTerminalRole" name="ListOfPluggableTerminalRole" nillable="true"/>\n <xs:complexType name="WireRole">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="WireSpecification"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="WireElementReference"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireRole" name="WireRole"/>\n <xs:complexType name="ListOfWireRole">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireRole" name="WireRole" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireRole" name="ListOfWireRole" nillable="true"/>\n <xs:complexType name="Specification">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="Identification"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:Specification" name="Specification"/>\n <xs:complexType name="ListOfSpecification">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:Specification" name="Specification" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSpecification" name="ListOfSpecification" nillable="true"/>\n <xs:complexType name="CompositionSpecification">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="Component"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CompositionSpecification" name="CompositionSpecification"/>\n <xs:complexType name="ListOfCompositionSpecification">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CompositionSpecification" name="CompositionSpecification" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCompositionSpecification" name="ListOfCompositionSpecification" nillable="true"/>\n <xs:complexType name="ConductorSpecification">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="CrossSectionArea"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="tns:ListOfConductorType" name="Type"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:ConductorSpecification" name="ConductorSpecification"/>\n <xs:complexType name="ListOfConductorSpecification">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ConductorSpecification" name="ConductorSpecification" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfConductorSpecification" name="ListOfConductorSpecification" nillable="true"/>\n <xs:complexType name="CoreSpecification">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="OutsideDiameter"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CoreSpecification" name="CoreSpecification"/>\n <xs:complexType name="ListOfCoreSpecification">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CoreSpecification" name="CoreSpecification" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCoreSpecification" name="ListOfCoreSpecification" nillable="true"/>\n <xs:complexType name="ContactingSpecification">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="ContactPoint"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:ContactingSpecification" name="ContactingSpecification"/>\n <xs:complexType name="ListOfContactingSpecification">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ContactingSpecification" name="ContactingSpecification" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfContactingSpecification" name="ListOfContactingSpecification" nillable="true"/>\n <xs:complexType name="InsulationSpecification">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="BaseColor"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="FirstIdentificationColor"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="SecondIdentificationColor"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="Thickness"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:InsulationSpecification" name="InsulationSpecification"/>\n <xs:complexType name="ListOfInsulationSpecification">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:InsulationSpecification" name="InsulationSpecification" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfInsulationSpecification" name="ListOfInsulationSpecification" nillable="true"/>\n <xs:complexType name="PartOrUsageRelatedSpecification">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="SpecialPartType"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="DescribedPart"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:PartOrUsageRelatedSpecification" name="PartOrUsageRelatedSpecification"/>\n <xs:complexType name="ListOfPartOrUsageRelatedSpecification">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PartOrUsageRelatedSpecification" name="PartOrUsageRelatedSpecification" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPartOrUsageRelatedSpecification" name="ListOfPartOrUsageRelatedSpecification" nillable="true"/>\n <xs:complexType name="CavityPartSpecification">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:PartOrUsageRelatedSpecification">\n    <xs:sequence/>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CavityPartSpecification" name="CavityPartSpecification"/>\n <xs:complexType name="ListOfCavityPartSpecification">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CavityPartSpecification" name="CavityPartSpecification" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCavityPartSpecification" name="ListOfCavityPartSpecification" nillable="true"/>\n <xs:complexType name="CavitySealSpecification">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence/>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CavitySealSpecification" name="CavitySealSpecification"/>\n <xs:complexType name="ListOfCavitySealSpecification">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CavitySealSpecification" name="CavitySealSpecification" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCavitySealSpecification" name="ListOfCavitySealSpecification" nillable="true"/>\n <xs:complexType name="GeneralTechnicalPartSpecification">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:PartOrUsageRelatedSpecification">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="ColorInformation"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="BoundingBox"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:GeneralTechnicalPartSpecification" name="GeneralTechnicalPartSpecification"/>\n <xs:complexType name="ListOfGeneralTechnicalPartSpecification">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:GeneralTechnicalPartSpecification" name="GeneralTechnicalPartSpecification" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfGeneralTechnicalPartSpecification" name="ListOfGeneralTechnicalPartSpecification" nillable="true"/>\n <xs:complexType name="TerminalSpecification">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:PartOrUsageRelatedSpecification">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="ConnectionALength"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="OverallLength"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="WireReception"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:TerminalSpecification" name="TerminalSpecification"/>\n <xs:complexType name="ListOfTerminalSpecification">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:TerminalSpecification" name="TerminalSpecification" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfTerminalSpecification" name="ListOfTerminalSpecification" nillable="true"/>\n <xs:complexType name="PluggableTerminalSpecification">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:TerminalSpecification">\n    <xs:sequence/>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:PluggableTerminalSpecification" name="PluggableTerminalSpecification"/>\n <xs:complexType name="ListOfPluggableTerminalSpecification">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PluggableTerminalSpecification" name="PluggableTerminalSpecification" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPluggableTerminalSpecification" name="ListOfPluggableTerminalSpecification" nillable="true"/>\n <xs:complexType name="WireSpecification">\n  <xs:complexContent mixed="false">\n   <xs:extension base="tns:PartOrUsageRelatedSpecification">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="WireElement"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireSpecification" name="WireSpecification"/>\n <xs:complexType name="ListOfWireSpecification">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireSpecification" name="WireSpecification" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireSpecification" name="ListOfWireSpecification" nillable="true"/>\n <xs:complexType name="WireElementSpecification">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="OutsideDiameter"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="ConductorSpecification"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="InsulationSpecification"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireElementSpecification" name="WireElementSpecification"/>\n <xs:complexType name="ListOfWireElementSpecification">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireElementSpecification" name="WireElementSpecification" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireElementSpecification" name="ListOfWireElementSpecification" nillable="true"/>\n <xs:complexType name="WireReceptionSpecification">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="InsulationDisplacementLength"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="ConductorCrimpLength"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="CrimpConnectionLength"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="InsulationCrimpLength"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="WireTipProtrusion"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="CoreCrimpDetails"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="tns:CrimpBarrelType" name="CrimpBarrelType"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireReceptionSpecification" name="WireReceptionSpecification"/>\n <xs:complexType name="ListOfWireReceptionSpecification">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireReceptionSpecification" name="WireReceptionSpecification" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireReceptionSpecification" name="ListOfWireReceptionSpecification" nillable="true"/>\n <xs:complexType name="Tolerance">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="LowerBoundary"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="UpperBoundary"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:Tolerance" name="Tolerance"/>\n <xs:complexType name="ListOfTolerance">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:Tolerance" name="Tolerance" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfTolerance" name="ListOfTolerance" nillable="true"/>\n <xs:complexType name="WireElement">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="Identification"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="WireElementSpecification"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="SubWireElement"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireElement" name="WireElement"/>\n <xs:complexType name="ListOfWireElement">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireElement" name="WireElement" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireElement" name="ListOfWireElement" nillable="true"/>\n <xs:complexType name="WireEnd">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="Identification"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="PositionOnWire"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="StrippingLength"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="InsulationPullbackLength"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireEnd" name="WireEnd"/>\n <xs:complexType name="ListOfWireEnd">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireEnd" name="WireEnd" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireEnd" name="ListOfWireEnd" nillable="true"/>\n <xs:complexType name="WireMounting">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="MountedCavitySeal"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="ReferencedWireEnd"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="WireMountingDetail"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireMounting" name="WireMounting"/>\n <xs:complexType name="ListOfWireMounting">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireMounting" name="WireMounting" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireMounting" name="ListOfWireMounting" nillable="true"/>\n <xs:complexType name="WireMountingDetail">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="CoreCrimpSize"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="InsulationCrimpSize"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="WireTipProtrusion"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="ContactedWireReception"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="ReferencedWireEnd"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="AbsoluteSealPosition"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="CorePullOffForce"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireMountingDetail" name="WireMountingDetail"/>\n <xs:complexType name="ListOfWireMountingDetail">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireMountingDetail" name="WireMountingDetail" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireMountingDetail" name="ListOfWireMountingDetail" nillable="true"/>\n <xs:complexType name="WireReception">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="Identification"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="Rotation"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="WireReceptionSpecification"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireReception" name="WireReception"/>\n <xs:complexType name="ListOfWireReception">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireReception" name="WireReception" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireReception" name="ListOfWireReception" nillable="true"/>\n <xs:complexType name="WireReceptionReference">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfString" name="Identification"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="WireReception"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireReceptionReference" name="WireReceptionReference"/>\n <xs:complexType name="ListOfWireReceptionReference">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireReceptionReference" name="WireReceptionReference" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireReceptionReference" name="ListOfWireReceptionReference" nillable="true"/>\n <xs:complexType name="CavityPartRoleIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CavityPartRoleIdDataType" name="CavityPartRoleIdDataType"/>\n <xs:complexType name="ListOfCavityPartRoleIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CavityPartRoleIdDataType" name="CavityPartRoleIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCavityPartRoleIdDataType" name="ListOfCavityPartRoleIdDataType" nillable="true"/>\n <xs:complexType name="CavityPartSpecificationIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CavityPartSpecificationIdDataType" name="CavityPartSpecificationIdDataType"/>\n <xs:complexType name="ListOfCavityPartSpecificationIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CavityPartSpecificationIdDataType" name="CavityPartSpecificationIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCavityPartSpecificationIdDataType" name="ListOfCavityPartSpecificationIdDataType" nillable="true"/>\n <xs:complexType name="CavitySealRoleIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CavitySealRoleIdDataType" name="CavitySealRoleIdDataType"/>\n <xs:complexType name="ListOfCavitySealRoleIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CavitySealRoleIdDataType" name="CavitySealRoleIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCavitySealRoleIdDataType" name="ListOfCavitySealRoleIdDataType" nillable="true"/>\n <xs:complexType name="CavitySealSpecificationIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CavitySealSpecificationIdDataType" name="CavitySealSpecificationIdDataType"/>\n <xs:complexType name="ListOfCavitySealSpecificationIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CavitySealSpecificationIdDataType" name="CavitySealSpecificationIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCavitySealSpecificationIdDataType" name="ListOfCavitySealSpecificationIdDataType" nillable="true"/>\n <xs:complexType name="CompositionSpecificationIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CompositionSpecificationIdDataType" name="CompositionSpecificationIdDataType"/>\n <xs:complexType name="ListOfCompositionSpecificationIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CompositionSpecificationIdDataType" name="CompositionSpecificationIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCompositionSpecificationIdDataType" name="ListOfCompositionSpecificationIdDataType" nillable="true"/>\n <xs:complexType name="ConductorSpecificationIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:ConductorSpecificationIdDataType" name="ConductorSpecificationIdDataType"/>\n <xs:complexType name="ListOfConductorSpecificationIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ConductorSpecificationIdDataType" name="ConductorSpecificationIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfConductorSpecificationIdDataType" name="ListOfConductorSpecificationIdDataType" nillable="true"/>\n <xs:complexType name="ConfigurableElementIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:ConfigurableElementIdDataType" name="ConfigurableElementIdDataType"/>\n <xs:complexType name="ListOfConfigurableElementIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ConfigurableElementIdDataType" name="ConfigurableElementIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfConfigurableElementIdDataType" name="ListOfConfigurableElementIdDataType" nillable="true"/>\n <xs:complexType name="ContactingSpecificationIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:ContactingSpecificationIdDataType" name="ContactingSpecificationIdDataType"/>\n <xs:complexType name="ListOfContactingSpecificationIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ContactingSpecificationIdDataType" name="ContactingSpecificationIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfContactingSpecificationIdDataType" name="ListOfContactingSpecificationIdDataType" nillable="true"/>\n <xs:complexType name="ContactPointIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:ContactPointIdDataType" name="ContactPointIdDataType"/>\n <xs:complexType name="ListOfContactPointIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ContactPointIdDataType" name="ContactPointIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfContactPointIdDataType" name="ListOfContactPointIdDataType" nillable="true"/>\n <xs:complexType name="CoreCrimpDetailIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CoreCrimpDetailIdDataType" name="CoreCrimpDetailIdDataType"/>\n <xs:complexType name="ListOfCoreCrimpDetailIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CoreCrimpDetailIdDataType" name="CoreCrimpDetailIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCoreCrimpDetailIdDataType" name="ListOfCoreCrimpDetailIdDataType" nillable="true"/>\n <xs:complexType name="CoreSpecificationIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CoreSpecificationIdDataType" name="CoreSpecificationIdDataType"/>\n <xs:complexType name="ListOfCoreSpecificationIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CoreSpecificationIdDataType" name="CoreSpecificationIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCoreSpecificationIdDataType" name="ListOfCoreSpecificationIdDataType" nillable="true"/>\n <xs:complexType name="CrimpDetailIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:CrimpDetailIdDataType" name="CrimpDetailIdDataType"/>\n <xs:complexType name="ListOfCrimpDetailIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:CrimpDetailIdDataType" name="CrimpDetailIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfCrimpDetailIdDataType" name="ListOfCrimpDetailIdDataType" nillable="true"/>\n <xs:complexType name="DocumentVersionIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:DocumentVersionIdDataType" name="DocumentVersionIdDataType"/>\n <xs:complexType name="ListOfDocumentVersionIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:DocumentVersionIdDataType" name="DocumentVersionIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfDocumentVersionIdDataType" name="ListOfDocumentVersionIdDataType" nillable="true"/>\n <xs:complexType name="ExtendableElementIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:ExtendableElementIdDataType" name="ExtendableElementIdDataType"/>\n <xs:complexType name="ListOfExtendableElementIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ExtendableElementIdDataType" name="ExtendableElementIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfExtendableElementIdDataType" name="ListOfExtendableElementIdDataType" nillable="true"/>\n <xs:complexType name="GeneralTechnicalPartSpecificationIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:GeneralTechnicalPartSpecificationIdDataType" name="GeneralTechnicalPartSpecificationIdDataType"/>\n <xs:complexType name="ListOfGeneralTechnicalPartSpecificationIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:GeneralTechnicalPartSpecificationIdDataType" name="GeneralTechnicalPartSpecificationIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfGeneralTechnicalPartSpecificationIdDataType" name="ListOfGeneralTechnicalPartSpecificationIdDataType" nillable="true"/>\n <xs:complexType name="InsulationCrimpDetailIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:InsulationCrimpDetailIdDataType" name="InsulationCrimpDetailIdDataType"/>\n <xs:complexType name="ListOfInsulationCrimpDetailIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:InsulationCrimpDetailIdDataType" name="InsulationCrimpDetailIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfInsulationCrimpDetailIdDataType" name="ListOfInsulationCrimpDetailIdDataType" nillable="true"/>\n <xs:complexType name="InsulationSpecificationIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:InsulationSpecificationIdDataType" name="InsulationSpecificationIdDataType"/>\n <xs:complexType name="ListOfInsulationSpecificationIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:InsulationSpecificationIdDataType" name="InsulationSpecificationIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfInsulationSpecificationIdDataType" name="ListOfInsulationSpecificationIdDataType" nillable="true"/>\n <xs:complexType name="ItemVersionIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:ItemVersionIdDataType" name="ItemVersionIdDataType"/>\n <xs:complexType name="ListOfItemVersionIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ItemVersionIdDataType" name="ItemVersionIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfItemVersionIdDataType" name="ListOfItemVersionIdDataType" nillable="true"/>\n <xs:complexType name="OccurrenceOrUsageIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:OccurrenceOrUsageIdDataType" name="OccurrenceOrUsageIdDataType"/>\n <xs:complexType name="ListOfOccurrenceOrUsageIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:OccurrenceOrUsageIdDataType" name="OccurrenceOrUsageIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfOccurrenceOrUsageIdDataType" name="ListOfOccurrenceOrUsageIdDataType" nillable="true"/>\n <xs:complexType name="PartOccurrenceIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:PartOccurrenceIdDataType" name="PartOccurrenceIdDataType"/>\n <xs:complexType name="ListOfPartOccurrenceIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PartOccurrenceIdDataType" name="PartOccurrenceIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPartOccurrenceIdDataType" name="ListOfPartOccurrenceIdDataType" nillable="true"/>\n <xs:complexType name="PartOrUsageRelatedSpecificationIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:PartOrUsageRelatedSpecificationIdDataType" name="PartOrUsageRelatedSpecificationIdDataType"/>\n <xs:complexType name="ListOfPartOrUsageRelatedSpecificationIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PartOrUsageRelatedSpecificationIdDataType" name="PartOrUsageRelatedSpecificationIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPartOrUsageRelatedSpecificationIdDataType" name="ListOfPartOrUsageRelatedSpecificationIdDataType" nillable="true"/>\n <xs:complexType name="PartVersionIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:PartVersionIdDataType" name="PartVersionIdDataType"/>\n <xs:complexType name="ListOfPartVersionIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PartVersionIdDataType" name="PartVersionIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPartVersionIdDataType" name="ListOfPartVersionIdDataType" nillable="true"/>\n <xs:complexType name="PluggableTerminalRoleIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:PluggableTerminalRoleIdDataType" name="PluggableTerminalRoleIdDataType"/>\n <xs:complexType name="ListOfPluggableTerminalRoleIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PluggableTerminalRoleIdDataType" name="PluggableTerminalRoleIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPluggableTerminalRoleIdDataType" name="ListOfPluggableTerminalRoleIdDataType" nillable="true"/>\n <xs:complexType name="PluggableTerminalSpecificationIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:PluggableTerminalSpecificationIdDataType" name="PluggableTerminalSpecificationIdDataType"/>\n <xs:complexType name="ListOfPluggableTerminalSpecificationIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:PluggableTerminalSpecificationIdDataType" name="PluggableTerminalSpecificationIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfPluggableTerminalSpecificationIdDataType" name="ListOfPluggableTerminalSpecificationIdDataType" nillable="true"/>\n <xs:complexType name="ResourceVersionIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:ResourceVersionIdDataType" name="ResourceVersionIdDataType"/>\n <xs:complexType name="ListOfResourceVersionIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ResourceVersionIdDataType" name="ResourceVersionIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfResourceVersionIdDataType" name="ListOfResourceVersionIdDataType" nillable="true"/>\n <xs:complexType name="RoleIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:RoleIdDataType" name="RoleIdDataType"/>\n <xs:complexType name="ListOfRoleIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RoleIdDataType" name="RoleIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRoleIdDataType" name="ListOfRoleIdDataType" nillable="true"/>\n <xs:complexType name="RoutableElementIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:RoutableElementIdDataType" name="RoutableElementIdDataType"/>\n <xs:complexType name="ListOfRoutableElementIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:RoutableElementIdDataType" name="RoutableElementIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfRoutableElementIdDataType" name="ListOfRoutableElementIdDataType" nillable="true"/>\n <xs:complexType name="SpecificationIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:SpecificationIdDataType" name="SpecificationIdDataType"/>\n <xs:complexType name="ListOfSpecificationIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:SpecificationIdDataType" name="SpecificationIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSpecificationIdDataType" name="ListOfSpecificationIdDataType" nillable="true"/>\n <xs:complexType name="TerminalRoleIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:TerminalRoleIdDataType" name="TerminalRoleIdDataType"/>\n <xs:complexType name="ListOfTerminalRoleIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:TerminalRoleIdDataType" name="TerminalRoleIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfTerminalRoleIdDataType" name="ListOfTerminalRoleIdDataType" nillable="true"/>\n <xs:complexType name="TerminalSpecificationIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:TerminalSpecificationIdDataType" name="TerminalSpecificationIdDataType"/>\n <xs:complexType name="ListOfTerminalSpecificationIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:TerminalSpecificationIdDataType" name="TerminalSpecificationIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfTerminalSpecificationIdDataType" name="ListOfTerminalSpecificationIdDataType" nillable="true"/>\n <xs:complexType name="WireElementIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireElementIdDataType" name="WireElementIdDataType"/>\n <xs:complexType name="ListOfWireElementIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireElementIdDataType" name="WireElementIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireElementIdDataType" name="ListOfWireElementIdDataType" nillable="true"/>\n <xs:complexType name="WireElementReferenceIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireElementReferenceIdDataType" name="WireElementReferenceIdDataType"/>\n <xs:complexType name="ListOfWireElementReferenceIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireElementReferenceIdDataType" name="WireElementReferenceIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireElementReferenceIdDataType" name="ListOfWireElementReferenceIdDataType" nillable="true"/>\n <xs:complexType name="WireElementSpecificationIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireElementSpecificationIdDataType" name="WireElementSpecificationIdDataType"/>\n <xs:complexType name="ListOfWireElementSpecificationIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireElementSpecificationIdDataType" name="WireElementSpecificationIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireElementSpecificationIdDataType" name="ListOfWireElementSpecificationIdDataType" nillable="true"/>\n <xs:complexType name="WireEndIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireEndIdDataType" name="WireEndIdDataType"/>\n <xs:complexType name="ListOfWireEndIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireEndIdDataType" name="WireEndIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireEndIdDataType" name="ListOfWireEndIdDataType" nillable="true"/>\n <xs:complexType name="WireMountingDetailIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireMountingDetailIdDataType" name="WireMountingDetailIdDataType"/>\n <xs:complexType name="ListOfWireMountingDetailIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireMountingDetailIdDataType" name="WireMountingDetailIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireMountingDetailIdDataType" name="ListOfWireMountingDetailIdDataType" nillable="true"/>\n <xs:complexType name="WireMountingIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireMountingIdDataType" name="WireMountingIdDataType"/>\n <xs:complexType name="ListOfWireMountingIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireMountingIdDataType" name="WireMountingIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireMountingIdDataType" name="ListOfWireMountingIdDataType" nillable="true"/>\n <xs:complexType name="WireReceptionIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireReceptionIdDataType" name="WireReceptionIdDataType"/>\n <xs:complexType name="ListOfWireReceptionIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireReceptionIdDataType" name="WireReceptionIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireReceptionIdDataType" name="ListOfWireReceptionIdDataType" nillable="true"/>\n <xs:complexType name="WireReceptionReferenceIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireReceptionReferenceIdDataType" name="WireReceptionReferenceIdDataType"/>\n <xs:complexType name="ListOfWireReceptionReferenceIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireReceptionReferenceIdDataType" name="WireReceptionReferenceIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireReceptionReferenceIdDataType" name="ListOfWireReceptionReferenceIdDataType" nillable="true"/>\n <xs:complexType name="WireReceptionSpecificationIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireReceptionSpecificationIdDataType" name="WireReceptionSpecificationIdDataType"/>\n <xs:complexType name="ListOfWireReceptionSpecificationIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireReceptionSpecificationIdDataType" name="WireReceptionSpecificationIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireReceptionSpecificationIdDataType" name="ListOfWireReceptionSpecificationIdDataType" nillable="true"/>\n <xs:complexType name="WireRoleIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireRoleIdDataType" name="WireRoleIdDataType"/>\n <xs:complexType name="ListOfWireRoleIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireRoleIdDataType" name="WireRoleIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireRoleIdDataType" name="ListOfWireRoleIdDataType" nillable="true"/>\n <xs:complexType name="WireSpecificationIdDataType">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="id"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:WireSpecificationIdDataType" name="WireSpecificationIdDataType"/>\n <xs:complexType name="ListOfWireSpecificationIdDataType">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:WireSpecificationIdDataType" name="WireSpecificationIdDataType" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfWireSpecificationIdDataType" name="ListOfWireSpecificationIdDataType" nillable="true"/>\n <xs:complexType name="Material">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="Key"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="xs:string" name="ReferenceSystem"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:Material" name="Material"/>\n <xs:complexType name="ListOfMaterial">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:Material" name="Material" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfMaterial" name="ListOfMaterial" nillable="true"/>\n <xs:complexType name="Size">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="Width"/>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="Height"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:Size" name="Size"/>\n <xs:complexType name="ListOfSize">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:Size" name="Size" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfSize" name="ListOfSize" nillable="true"/>\n <xs:complexType name="ValueWithUnit">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="1" type="ua:ExtensionObject" name="UnitComponent"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ValueWithUnit" name="ValueWithUnit"/>\n <xs:complexType name="ListOfValueWithUnit">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ValueWithUnit" name="ValueWithUnit" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfValueWithUnit" name="ListOfValueWithUnit" nillable="true"/>\n <xs:complexType name="NumericalValue">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="ValueComponent"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="ua:ListOfExtensionObject" name="Tolerance"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:NumericalValue" name="NumericalValue"/>\n <xs:complexType name="ListOfNumericalValue">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:NumericalValue" name="NumericalValue" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfNumericalValue" name="ListOfNumericalValue" nillable="true"/>\n <xs:complexType name="ValueRange">\n  <xs:complexContent mixed="false">\n   <xs:extension base="ua:ExtensionObject">\n    <xs:sequence>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Minimum"/>\n     <xs:element minOccurs="0" maxOccurs="1" type="xs:double" name="Maximum"/>\n    </xs:sequence>\n   </xs:extension>\n  </xs:complexContent>\n </xs:complexType>\n <xs:element type="tns:ValueRange" name="ValueRange"/>\n <xs:complexType name="ListOfValueRange">\n  <xs:sequence>\n   <xs:element minOccurs="0" maxOccurs="unbounded" type="tns:ValueRange" name="ValueRange" nillable="true"/>\n  </xs:sequence>\n </xs:complexType>\n <xs:element type="tns:ListOfValueRange" name="ListOfValueRange" nillable="true"/>\n</xs:schema>\n',
)


del Any, TYPE_CHECKING, uuid, o6, ns0, wire_harness_vec_datypes
