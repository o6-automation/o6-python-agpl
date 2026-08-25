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

"""Generated OPC UA machinery namespace."""

from o6.ns import _initialize_namespace

_initialize_namespace(__name__, shortname="machinery", uri="http://opcfoundation.org/UA/Machinery/", version="1.04.1", publication_date="2026-01-01T00:00:00Z")

from . import objtypes as objtypes
from . import instances as instances

del _initialize_namespace
