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

import o6.ns.di as di

import o6.ns.ns0 as ns0

class BYTE:
    """It describes that the type is used as bit string of length 8."""

class WORD:
    """It describes that the type is used as bit string of length 16."""

class DWORD:
    """It describes that the type is used as bit string of length 32."""

class LWORD:
    """It describes that the type is used as bit string of length 64."""

class TIME:
    """It describes that the type is used as interval of time in milliseconds. The representation contains information for days (d), hours (h), minutes (m), seconds (s) and milliseconds (ms). The range of valid values is vendor specific. The server has to check if the value has a valid range. Sample: T#+24d20h31m23s647ms."""

class LTIME:
    """It describes that the type is used as interval of time in nanoseconds. The valid range is LT#-106751d23h47m16s854ms775us808ns to LT#+106751d23h47m16s854ms775us807ns. The representation contains information for days (d), hours (h), minutes (m), seconds (s) milliseconds (ms), microseconds (us) and nanoseconds (ns)."""

class DATE:
    """It describes that the type is used as a date only."""

class TOD:
    """TIME_OF_DAY stores number of milliseconds since the beginning of the day: TOD#00:00:00.000 to TOD#23:59:59.999."""

class LTOD:
    """LTIME_OF_DAY stores the number of nanoseconds since the beginning of the day: LTOD#00:00:00.000000000 to LTOD#23:59:59.999999999."""

class DT:
    """Vendor specific type."""

class CHAR:
    """. It describes that the type is used as single-byte character."""

class WCHAR:
    """It describes that the type is used as double-byte character."""

class STRING:
    """It describes that the type is used as a variable-length single-byte character string."""

class LDATE:
    """It describes that the type is used as date only. The interval is nanoseconds since 1970-01-01."""

class LDT:
    """It describes the number of nanoseconds elapsed since 1970-01-01-00:00:00."""
