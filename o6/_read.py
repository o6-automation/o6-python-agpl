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

"""Shared request normalization and result handling for public reads."""

from typing import Any

import o6
from o6._node_backend import _attribute_id, _targets_and_ranges
from o6.ns import ns0


def _read_request(
    target: o6.NodeIdLike | list[o6.NodeIdLike],
    attr: o6.AttributeId | str,
    timestamps: ns0.datatypes.TimestampsToReturn | None,
    value_only: bool,
    index_range: o6.IndexRange | list[o6.IndexRange],
) -> tuple[bool, ns0.datatypes.ReadRequest]:
    attribute = _attribute_id(attr)
    if not isinstance(attribute, int):
        raise TypeError("attr must be an AttributeId or attribute name")
    if not isinstance(value_only, bool):
        raise TypeError("valueOnly must be a bool")
    if timestamps is None:
        timestamps = ns0.datatypes.TimestampsToReturn.SOURCE
    if not isinstance(timestamps, int):
        raise TypeError("timestampsToReturn must be a TimestampsToReturn value")
    if not 0 <= timestamps <= ns0.datatypes.TimestampsToReturn.NEITHER:
        raise o6.StatusCodeError(o6.StatusCode.BAD_TIMESTAMPS_TO_RETURN_INVALID)
    is_scalar, targets, ranges = _targets_and_ranges(target, index_range)
    request = ns0.datatypes.ReadRequest()
    request.timestampsToReturn = timestamps
    items = []
    for node, item_range in zip(targets, ranges):
        item = ns0.datatypes.ReadValueId()
        item.nodeId = o6.NodeId(node)
        item.attributeId = attribute
        if item_range is not None:
            item.indexRange = item_range
        items.append(item)
    request.nodesToRead = items
    return is_scalar, request


def _check_read_status(status: o6.StatusCode | None, index: int | None = None) -> None:
    if status and status & (o6.StatusCode.BAD | o6.StatusCode.UNCERTAIN):
        error = o6.StatusCodeError(status)
        if index is not None:
            error.add_note(f"Read result at index {index} failed")
        raise error


def _read_results(results: list[o6.DataValue], is_scalar: bool, value_only: bool) -> Any:
    if value_only:
        for index, result in enumerate(results):
            _check_read_status(result.status, None if is_scalar else index)
        values = [result.value for result in results]
        return values[0] if is_scalar else values
    return results[0] if is_scalar else results
