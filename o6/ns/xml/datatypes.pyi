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

from typing import Any, Sequence, SupportsFloat

import numpy as np

_Integer = int | np.integer[Any]

_Boolean = bool | np.bool_

import enum

from o6.node import ObjectNode as _ObjectNode, VariableNode as _VariableNode

import uuid

import o6

import o6.ns.ns0 as ns0

class XmlQName:
    pass

class XmlToken:
    pass

class XmlNmToken:
    pass

class XmlName:
    pass

class XmlNcName:
    pass

class XmlId:
    pass

class XmlIdRef:
    pass

class XmlEntity:
    pass

class XmlInteger:
    pass

class XmlNonPositiveInteger:
    pass

class XmlNegativeInteger:
    pass

class XmlNonNegativeInteger:
    pass

class XmlPositiveInteger:
    pass

class XmlHexBinary:
    pass

class XmlYearMonthDuration:
    pass

class XmlGYearMonth:
    pass

class XmlDayTimeDuration:
    pass

class XmlGYear:
    pass

class XmlGMonth:
    pass

class XmlGDay:
    pass

class XmlGMonthDay:
    pass

class XmlTime:
    pass

class XmlDate:
    pass
