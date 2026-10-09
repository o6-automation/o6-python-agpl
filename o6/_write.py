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

"""Shared input validation for public client and server writes."""

from typing import Any, Mapping

import o6
from o6._node_backend import _attribute_id, _targets_and_ranges

_WRITE_UNSET = object()


def _write_inputs(
    target: o6.NodeIdLike | list[o6.NodeIdLike] | Mapping[o6.NodeIdLike, Any],
    value: Any,
    attr: o6.AttributeId | str,
    index_range: o6.IndexRange | list[o6.IndexRange],
) -> tuple[bool, o6.AttributeId, list[o6.NodeId], list[Any], list[str | None]]:
    attribute = _attribute_id(attr)
    if not isinstance(attribute, int):
        raise TypeError("attr must be an AttributeId or attribute name")
    is_scalar = not isinstance(target, (list, Mapping))
    if isinstance(target, Mapping):
        if value is not _WRITE_UNSET:
            raise ValueError("value must not be provided when target is a mapping")
        if index_range is not None:
            raise ValueError("range is not supported when target is a mapping; use the list form")
        targets, values = list(target.keys()), list(target.values())
    elif isinstance(target, list):
        if not isinstance(value, list):
            raise ValueError("value must be a list when target is a list")
        if len(target) != len(value):
            raise ValueError(
                f"value list length {len(value)} does not match target list length {len(target)}"
            )
        targets, values = list(target), list(value)
    else:
        if value is _WRITE_UNSET:
            raise ValueError("value must be provided when target is a single node")
        targets, values = [target], [value]
    _, _, ranges = _targets_and_ranges(targets, index_range)
    if attribute != o6.AttributeId.VALUE and any(ranges):
        raise ValueError("range is only supported for the Value attribute")
    return is_scalar, attribute, [o6.NodeId(node) for node in targets], values, ranges


def _write_payload(value: Any) -> o6.DataValue:
    """Preserve envelopes and infer bare payload types without attribute coercion."""
    return value if isinstance(value, o6.DataValue) else o6.DataValue(value=value)


def _write_payload_status(value: o6.DataValue, attribute: o6.AttributeId) -> o6.StatusCode:
    if attribute != o6.AttributeId.VALUE and value._has_metadata:
        return o6.StatusCode.BAD_WRITE_NOT_SUPPORTED
    return o6.StatusCode.GOOD
