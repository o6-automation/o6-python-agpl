# Copyright (c) 2026 o6 Automation GmbH
#
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

"""Socket setup for the native asyncio event loop."""

import asyncio
import errno
from collections.abc import Callable, Sequence


class _ListenerServer(asyncio.Server):
    # CPython gh-109564: an accepted socket can reach _attach after close().
    # The native protocol closes late connections in connection_made; keep
    # asyncio's transport accounting valid until connection_lost runs.
    def _attach(self, transport: asyncio.BaseTransport | None = None) -> None:
        if transport is None:  # Python 3.11 and 3.12 count active transports.
            self._active_count = getattr(self, "_active_count") + 1
        else:
            getattr(self, "_clients").add(transport)

    def _wakeup(self) -> None:
        if getattr(self, "_waiters") is not None:
            getattr(super(), "_wakeup")()


async def create_listener(
    loop: asyncio.AbstractEventLoop,
    protocol_factory: Callable[[], asyncio.Protocol],
    host: str | Sequence[str] | None,
    port: int,
    *,
    reuse_address: bool,
) -> asyncio.Server:
    """Prepare the listener before accepts can race with its shutdown."""
    if port == 0:
        return await create_ephemeral_listener(
            loop, protocol_factory, host, reuse_address=reuse_address
        )
    server = await loop.create_server(
        protocol_factory, host, port, reuse_address=reuse_address, start_serving=False
    )
    if type(server) is asyncio.Server:
        server.__class__ = _ListenerServer
    try:
        await server.start_serving()
    except BaseException:
        server.close()
        raise
    return server


async def create_ephemeral_listener(
    loop: asyncio.AbstractEventLoop,
    protocol_factory: Callable[[], asyncio.Protocol],
    host: str | Sequence[str] | None,
    *,
    reuse_address: bool,
) -> asyncio.Server:
    """Bind all resolved addresses to one OS-selected port."""
    attempts_left = 5
    while True:
        probe = await loop.create_server(
            protocol_factory, host, 0, reuse_address=reuse_address, start_serving=False
        )
        try:
            port = probe.sockets[0].getsockname()[1]
        finally:
            probe.close()
            await probe.wait_closed()

        try:
            return await create_listener(
                loop, protocol_factory, host, port, reuse_address=reuse_address
            )
        except OSError as error:
            # Another listener can claim the port between the two binds, or
            # the selected port can already be occupied in another family.
            attempts_left -= 1
            if error.errno != errno.EADDRINUSE or not attempts_left:
                raise
