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

"""Shared input validation for public client and server node deletion."""

import o6


def _delete_inputs(
    node_id: o6.NodeIdLike | list[o6.NodeIdLike], delete_target_references: bool
) -> tuple[bool, list[o6.NodeId]]:
    if not isinstance(delete_target_references, bool):
        raise TypeError("deleteTargetReferences must be a bool")
    is_scalar = not isinstance(node_id, list)
    targets = node_id if isinstance(node_id, list) else [node_id]
    return is_scalar, [o6.NodeId(target) for target in targets]
