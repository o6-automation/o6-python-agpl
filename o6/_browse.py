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

"""Shared state for complete browsing across synchronous and async backends."""

import asyncio
from typing import Any, Awaitable, Callable

from o6.ns import ns0


async def _finish_request(operation: Awaitable[Any]) -> Any:
    """Finish adopting a response before allowing cancellation to release its resources."""
    pending = asyncio.ensure_future(operation)
    try:
        return await asyncio.shield(pending)
    except asyncio.CancelledError:
        while not pending.done():
            try:
                await asyncio.shield(pending)
            except asyncio.CancelledError:
                pass
            except Exception:
                break
        if not pending.cancelled():
            pending.exception()
        raise


class _BrowseCollection:
    def __init__(self) -> None:
        self.references: list[ns0.datatypes.ReferenceDescription] = []
        self.continuation_point: bytes = b""

    def append(self, page: ns0.datatypes.BrowseResult) -> None:
        # A failed page may omit the token even though the previous one is live.
        if page.continuationPoint or page.statusCode == 0:
            self.continuation_point = page.continuationPoint
        page.statusCode.check()
        self.references.extend(page.references)


def _browse_description(target, direction, reftype, refsubtypes, node_class_mask, result_mask):
    import o6

    return ns0.datatypes.BrowseDescription(
        nodeId=o6.NodeId(target),
        browseDirection=direction,
        referenceTypeId=o6.NodeId(reftype),
        includeSubtypes=refsubtypes,
        nodeClassMask=node_class_mask,
        resultMask=result_mask,
    )


def _simplified_browse_path(origin, path):
    import o6

    names = path if isinstance(path, (list, tuple)) else [path]
    elements = [
        ns0.datatypes.RelativePathElement(
            referenceTypeId=o6.NodeId(ns0.reftypes.HierarchicalReferences),
            includeSubtypes=True,
            targetName=o6.QualifiedName(name),
        )
        for name in names
    ]
    relative = ns0.datatypes.RelativePath()
    relative.elements = elements
    return ns0.datatypes.BrowsePath(startingNode=o6.NodeId(origin), relativePath=relative)


async def _translate_paths(service: Callable[[Any], Awaitable[Any]], browse_path: Any) -> Any:
    scalar = not isinstance(browse_path, list)
    paths = [browse_path] if scalar else browse_path
    if not paths:
        return []
    request = ns0.datatypes.TranslateBrowsePathsToNodeIdsRequest(browsePaths=paths)
    response = await service(request)
    response.responseHeader.serviceResult.check()
    if len(response.results) != len(paths):
        raise RuntimeError("Browse path result count does not match the request")
    return response.results[0] if scalar else list(response.results)
