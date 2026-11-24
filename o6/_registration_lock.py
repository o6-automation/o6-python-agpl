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

"""The registration lock, which serialises namespace and DataType registration.

One process-wide re-entrant lock covers:

- namespace registration (`o6.ns.register`, `o6.ns.namespace` and the
  generated packages' `_initialize_namespace`), including the native call;
- each native DataType registration (`_register` in `_datatype_registration`);
- a client's runtime loading of server DataTypes (`_DataTypeLoader.load`),
  including applying them to the client's decoder.

Loading a packaged namespace module is not covered: it runs through the import
system, whose per-module locks make other threads wait for a load in progress.

Rules for code that holds the lock:

- Never import a module or run code that may. The import system holds a
  module's lock while the module's body registers types, so a holder waiting
  for an import can deadlock with it.
- Never marshal to an event loop or block on one. Loop threads take the lock
  when they load DataTypes at runtime, so a holder waiting for a loop can
  deadlock with it. `_run_on_loop` raises instead of marshalling, or waiting
  for an idle loop that another thread holds, while the caller holds the lock;
  `_call_native` goes through it.
- Never take the lock in the notification path (`decodeNotification`), which
  runs under the native client lock. Read paths stay lock-free.
- A per-client asyncio lock around namespace-snapshot application is taken
  before this lock, never after it.
"""

import threading

REGISTRATION_LOCK = threading.RLock()


def registration_lock_held() -> bool:
    """Whether the calling thread holds the registration lock."""
    return REGISTRATION_LOCK._is_owned()  # type: ignore[attr-defined]
