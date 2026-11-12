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

"""Registry of every example: the single source of truth for both
``examples/check_examples.py`` and ``docs/gen_examples.py``.

Manifest id scheme
------------------

An example's id is its path under ``examples/`` without the ``.py`` suffix
of the entry script, always starting with one of the four role roots:

* ``client/C02_firststeps``                        — single-file example
* ``type_authoring/T03_nodeset_authoring/example`` — entry inside a
  multi-file example folder

Multi-file example folders (an entry script plus supporting modules, e.g. a
namespace module imported by the entry) set ``doc_files`` to control how
``docs/gen_examples.py`` renders the folder into one doc page: the tuple
lists every file to render, in the order they appear on the page, and must
include ``entry``. Order the file a reader needs *first* before the ones
that build on it — e.g. the namespace module that defines the types before
the script that exercises them — since that is the order someone opening
the folder cold would need to read them in.

``requires_server`` is a manifest id — resolved through ``ALL_EXAMPLES``,
never a hand-copied path string that can drift from the real location — for
a client example that needs another example's server running to work. It is
a top-level ``ExampleSpec`` field rather than part of ``test`` because it
describes the example itself, independent of whether it has an automated
check: ``examples/check_examples.py`` starts that server before the entry
script and stops it after, and ``docs/gen_examples.py`` renders it as a
standard "start this server first" admonition on the example's doc page —
one generated block instead of every script hand-writing its own reminder.

``test`` describes the automated check ``examples/check_examples.py`` runs:

* ``expected``       — stdout substring that must appear (finite examples)
* ``ready_marker``   — stdout substring proving an infinite-loop example got
                       going cleanly; reaching it counts as success
* ``timeout``        — seconds before the runner sends SIGINT
* ``allow_server_exit`` — permit a clean dependency-server exit after a successful client

``test=None`` means "no automated check"; it must be paired with a
non-empty ``skip_reason`` explaining why. ``requires_server`` is independent
of this — an interactive example with no automated check can still declare it.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

EXAMPLES_ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class ExampleSpec:
    """Description of one runnable example."""

    entry: str
    title: str
    doc: bool
    test: dict[str, Any] | None = None
    skip_reason: str = field(default="")
    doc_files: tuple[str, ...] | None = None
    requires_server: str | None = None

    def __post_init__(self) -> None:
        if self.test is None and not self.skip_reason:
            raise ValueError(f"example {self.entry!r}: test=None requires a non-empty skip_reason")
        if self.test is not None and self.skip_reason:
            raise ValueError(f"example {self.entry!r}: skip_reason is only valid when test is None")
        if self.test is not None and "timeout" not in self.test:
            raise ValueError(f"example {self.entry!r}: test requires a timeout")
        if self.test is not None and "requires_server" in self.test:
            raise ValueError(
                f"example {self.entry!r}: requires_server belongs on the ExampleSpec, not in test"
            )
        if self.doc_files is not None and self.entry not in self.doc_files:
            raise ValueError(f"example {self.entry!r}: doc_files must include the entry file")


def script_path(example_id: str, spec: ExampleSpec) -> Path:
    """Absolute path of an example's entry script.

    Single-file examples have ids like ``client/C02_firststeps`` and the
    script is ``<id>.py``.  Multi-file examples have ids like
    ``type_authoring/T03_nodeset_authoring/example`` and ``entry`` is
    relative to the folder holding the entry script.
    """
    parts = example_id.split("/")
    if len(parts) > 2:
        return EXAMPLES_ROOT / "/".join(parts[:-1]) / spec.entry
    return EXAMPLES_ROOT / f"{example_id}.py"


ALL_EXAMPLES: dict[str, ExampleSpec] = {
    # ------------------------------------------------------------------ client
    "client/C01_lowlevel": ExampleSpec(
        entry="C01_lowlevel.py",
        title="Client (Low-level)",
        doc=True,
        test=dict(expected="=== Example completed ===", timeout=30.0, allow_server_exit=True),
        requires_server="advanced_applications/tutorial_server/server",
    ),
    "client/C02_firststeps": ExampleSpec(
        entry="C02_firststeps.py",
        title="Client First Steps",
        doc=True,
        test=dict(expected="=== Example completed ===", timeout=30.0),
        requires_server="server/S03_firststeps",
    ),
    "client/C03_browsing": ExampleSpec(
        entry="C03_browsing.py",
        title="Client Browsing",
        doc=True,
        test=dict(expected="=== Example completed ===", timeout=30.0),
        requires_server="server/S03_firststeps",
    ),
    "client/C04_configuration": ExampleSpec(
        entry="C04_configuration.py",
        title="Client Configuration",
        doc=True,
        test=dict(expected="=== Example completed ===", timeout=30.0),
        requires_server="server/S03_firststeps",
    ),
    "client/C05_usernamepw": ExampleSpec(
        entry="C05_usernamepw.py",
        title="Client Username / Password Authentication",
        doc=True,
        test=dict(expected="=== Example completed ===", timeout=30.0),
        requires_server="server/S03_firststeps",
    ),
    "client/C06_async_modes": ExampleSpec(
        entry="C06_async_modes.py",
        title="Client Sync/Async Calling Patterns",
        doc=True,
        test=dict(expected="=== Example completed ===", timeout=30.0),
        requires_server="server/S03_firststeps",
    ),
    "client/C07_nodemanagement": ExampleSpec(
        entry="C07_nodemanagement.py",
        title="Client Node Management",
        doc=True,
        test=dict(expected="=== Example completed ===", timeout=30.0),
        requires_server="server/S03_firststeps",
    ),
    "client/C08_subscriptions_firststeps": ExampleSpec(
        entry="C08_subscriptions_firststeps.py",
        title="Client Subscriptions",
        doc=True,
        test=dict(expected="=== Example completed ===", timeout=30.0),
        requires_server="server/S03_firststeps",
    ),
    "client/C09_subscriptions_modify": ExampleSpec(
        entry="C09_subscriptions_modify.py",
        title="Client Subscription Modification",
        doc=True,
        test=dict(expected="=== Example completed ===", timeout=45.0),
    ),
    "client/C10_subscriptions_events": ExampleSpec(
        entry="C10_subscriptions_events.py",
        title="Client Subscription Events",
        doc=True,
        test=dict(expected="=== Example completed ===", timeout=30.0),
    ),
    "client/C11_subscriptions_triggering": ExampleSpec(
        entry="C11_subscriptions_triggering.py",
        title="Client Subscription Triggering",
        doc=True,
        test=dict(expected="=== Example completed ===", timeout=30.0),
    ),
    "client/C12_browser": ExampleSpec(
        entry="C12_browser.py",
        title="Client Interactive Browser",
        doc=True,
        test=None,
        skip_reason="interactive curses TUI",
        requires_server="server/S03_firststeps",
    ),
    # ------------------------------------------------------------------ server
    "server/S01_lowlevel": ExampleSpec(
        entry="S01_lowlevel.py",
        title="Server (Low-level)",
        doc=True,
        test=dict(ready_marker="Server running at opc.tcp://localhost:4840", timeout=15.0),
    ),
    "server/S02_minimal": ExampleSpec(
        entry="S02_minimal.py",
        title="Server Minimal",
        doc=True,
        test=dict(ready_marker="Server running", timeout=15.0),
    ),
    "server/S03_firststeps": ExampleSpec(
        entry="S03_firststeps.py",
        title="Server First Steps",
        doc=True,
        test=dict(ready_marker="Server running at opc.tcp://localhost:4840", timeout=15.0),
    ),
    "server/S04_variables": ExampleSpec(
        entry="S04_variables.py",
        title="Server Variables",
        doc=True,
        test=dict(ready_marker="Server running at", timeout=15.0),
    ),
    "server/S05_objects": ExampleSpec(
        entry="S05_objects.py",
        title="Server Objects",
        doc=True,
        test=dict(ready_marker="Server running at opc.tcp://localhost:4840", timeout=15.0),
    ),
    "server/S06_methods": ExampleSpec(
        entry="S06_methods.py",
        title="Server Methods",
        doc=True,
        test=dict(ready_marker="Server running at opc.tcp://localhost:4840", timeout=15.0),
    ),
    "server/S07_data_source": ExampleSpec(
        entry="S07_data_source.py",
        title="Server Data Source Updates",
        doc=True,
        test=dict(expected="=== Example completed ===", timeout=30.0),
    ),
    "server/S08_asynchronous": ExampleSpec(
        entry="S08_asynchronous.py",
        title="Server Async",
        doc=True,
        test=dict(ready_marker="Server running", timeout=15.0),
    ),
    "server/S09_implement_readwrite": ExampleSpec(
        entry="S09_implement_readwrite.py",
        title="Server Variable Read/Write Override",
        doc=True,
        test=dict(expected="=== Example completed ===", timeout=30.0),
    ),
    "server/S10_implement_objtype": ExampleSpec(
        entry="S10_implement_objtype.py",
        title="Server ObjectType Implementation",
        doc=True,
        test=dict(expected="=== Example completed ===", timeout=30.0),
    ),
    "server/S11_history": ExampleSpec(
        entry="S11_history.py",
        title="Server History",
        doc=True,
        test=dict(ready_marker="Server running at", timeout=15.0),
    ),
    # ---------------------------------------------------------- type_authoring
    "type_authoring/T01_lowlevel": ExampleSpec(
        entry="T01_lowlevel.py",
        title="Types (Low-level)",
        doc=True,
        test=dict(expected="=== Example completed ===", timeout=30.0),
    ),
    "type_authoring/T02_types": ExampleSpec(
        entry="T02_types.py",
        title="Built-in Types",
        doc=True,
        test=dict(expected="=== Example completed ===", timeout=30.0),
    ),
    "type_authoring/T03_nodeset_authoring/example": ExampleSpec(
        entry="example.py",
        title="Nodeset Authoring",
        doc=True,
        test=dict(expected="=== Example completed ===", timeout=30.0),
        doc_files=("myns.py", "example.py"),
    ),
    # --------------------------------------------------- advanced_applications
    "advanced_applications/sim_examples/basic_sim/client": ExampleSpec(
        entry="client.py",
        title="Pump Simulation Example: Client",
        doc=False,
        skip_reason="no automated check, requires manual interaction with the server",
    ),
    "advanced_applications/sim_examples/basic_sim/server": ExampleSpec(
        entry="server.py",
        title="Pump Simulation Example: Server",
        doc=False,
        skip_reason="no automated check, requires manual interaction with the server",
    ),
    "advanced_applications/sim_examples/basic_hierarchic": ExampleSpec(
        entry="basic_hierarchic.py",
        title="Hierarchic Simulation",
        doc=False,
        test=None,
        skip_reason="no automated check",
    ),
    "advanced_applications/sim_examples/basic_sim/gui_pump": ExampleSpec(
        entry="gui_pump.py",
        title="Pump Simulation GUI",
        doc=False,
        test=None,
        skip_reason="tkinter GUI",
    ),
    "advanced_applications/tutorial_server/client": ExampleSpec(
        entry="client.py",
        title="Distilling Simulation Example: Client",
        doc=False,
        test=dict(expected="=== Example completed ===", timeout=30.0),
        requires_server="advanced_applications/tutorial_server/server",
    ),
    "advanced_applications/tutorial_server/server": ExampleSpec(
        entry="server.py",
        title="Distilling Simulation Example: Server",
        doc=False,
        test=dict(ready_marker="Server running at", timeout=15.0),
    ),
    "advanced_applications/tutorial_server/ui": ExampleSpec(
        entry="ui.py",
        title="Distilling Simulation Dashboard",
        doc=False,
        test=None,
        skip_reason="interactive curses UI",
    ),
    "advanced_applications/aggregation_server/server": ExampleSpec(
        entry="server.py",
        title="Aggregation Server",
        doc=False,
        test=None,
        skip_reason="nondeterministic background threads",
    ),
    "advanced_applications/gds_push/server": ExampleSpec(
        entry="server.py",
        title="GDS PushManagement Receiver",
        doc=True,
        test=None,
        skip_reason="manual PKI and external certificate manager required; externally unverified",
    ),
    "advanced_applications/lds/server": ExampleSpec(
        entry="server.py",
        title="Local Discovery Server with mDNS",
        doc=True,
        doc_files=(
            "README.md",
            "server.py",
            "registered_server.py",
            "client.py",
        ),
        test=None,
        skip_reason="three-process lifecycle tested by tests/examples/test_lds.py and its LDS-specific runner",
    ),
    "advanced_applications/lds/registered_server": ExampleSpec(
        entry="registered_server.py",
        title="LDS Registered Application",
        doc=False,
        test=None,
        skip_reason="three-process lifecycle tested by tests/examples/test_lds.py and its LDS-specific runner",
    ),
    "advanced_applications/lds/client": ExampleSpec(
        entry="client.py",
        title="LDS Discovery Client",
        doc=False,
        test=None,
        skip_reason="three-process lifecycle tested by tests/examples/test_lds.py and its LDS-specific runner",
    ),
    "advanced_applications/opcua_fx/client": ExampleSpec(
        entry="client.py",
        title="OPC UA FX Demo: Client",
        doc=False,
        test=dict(expected="=== OPC UA FX smoke scenario completed ===", timeout=30.0),
        requires_server="advanced_applications/opcua_fx/server",
    ),
    "advanced_applications/opcua_fx/server": ExampleSpec(
        entry="server.py",
        title="OPC UA FX Demo: Server",
        doc=False,
        test=dict(
            ready_marker="OPC UA FX demo server running at opc.tcp://localhost:4840", timeout=20.0
        ),
    ),
    "advanced_applications/mcp_server/server": ExampleSpec(
        entry="server.py",
        title="MCP Server",
        doc=False,
        test=None,
        skip_reason="subprocess + MCP client integration",
    ),
    "advanced_applications/mcp_server/demo": ExampleSpec(
        entry="demo.py",
        title="MCP Server Demo",
        doc=False,
        test=None,
        skip_reason="subprocess + MCP client integration",
    ),
    "advanced_applications/mcp_server/demo_server": ExampleSpec(
        entry="demo_server.py",
        title="MCP Demo Server",
        doc=False,
        test=None,
        skip_reason="subprocess + MCP client integration",
    ),
    "advanced_applications/sortingline/server": ExampleSpec(
        entry="server.py",
        title="Sorting Line Example: Server",
        doc=False,
        test=dict(ready_marker="OPC UA Server online", timeout=15.0),
    ),
    "advanced_applications/sortingline/controller": ExampleSpec(
        entry="controller.py",
        title="Sorting Line Example: Controller",
        doc=False,
        test=dict(ready_marker="Connected to the OPC UA server.", timeout=15.0),
        requires_server="advanced_applications/sortingline/server",
    ),
    "advanced_applications/sortingline/client": ExampleSpec(
        entry="client.py",
        title="Sorting Line Example: Client",
        doc=False,
        test=dict(ready_marker="Connected to the Digital Twin.", timeout=15.0),
        requires_server="advanced_applications/sortingline/server",
    ),
    "advanced_applications/sortingline/all_in_one": ExampleSpec(
        entry="all_in_one.py",
        title="Sorting Line Example: All-in-One",
        doc=False,
        test=None,
        skip_reason="no automated check",
    ),
}
