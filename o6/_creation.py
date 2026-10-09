# Copyright 2026 (c) o6 Automation GmbH
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

"""Shared attributes for client/server node-creation conveniences."""

from typing import Any

import numpy as np

import o6
from o6.ns import ns0
from o6.util import _empty_sequence_shape, _infer_data_type, _value_rank


def variable_attributes(
    name: o6.LocalizedTextLike, value: Any, data_type: o6.NodeIdLike | None, writable: bool
) -> tuple[ns0.datatypes.VariableAttributes, Any, tuple[int, ...] | None]:
    empty_shape = _empty_sequence_shape(value)
    if isinstance(value, np.ndarray) and value.size == 0:
        empty_shape = value.shape
    if data_type is not None:
        type_id = o6.NodeId(data_type)
        rank = len(empty_shape) if empty_shape is not None else _value_rank(value)
    elif value is not None:
        type_id, rank = _infer_data_type(value)
    else:
        type_id, rank = o6.NodeId(o6.Int32), -1

    access = int(ns0.datatypes.AccessLevelType.CURRENT_READ)
    if writable:
        access |= int(ns0.datatypes.AccessLevelType.CURRENT_WRITE)
    attributes = ns0.datatypes.VariableAttributes(
        displayName=o6.LocalizedText(name),
        dataType=type_id,
        valueRank=rank,
        accessLevel=access,
        userAccessLevel=access,
    )
    if rank >= 1:
        attributes.arrayDimensions = [o6.UInt32(0)] * rank
    initial = o6.Double(value) if isinstance(value, float) else value
    # An empty Variant has no dimensions on the wire. Let the target type and
    # rank initialize its typed empty value instead of encoding zero dimensions.
    if initial is not None and empty_shape is None:
        attributes.value = initial
    return attributes, initial, empty_shape
