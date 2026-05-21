# Copyright 2026 (c) o6 Automation GmbH
from __future__ import annotations
import curses
import os
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, cast
import o6

# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------


def fuzzy_match(query: str, text: str) -> tuple[bool, list[int]]:
    """Subsequence fuzzy match. Returns (matched, matched_indices_in_text)."""
    if not query:
        return True, []
    q = query.lower()
    t = text.lower()
    positions = []
    qi = 0
    for ti, ch in enumerate(t):
        if qi < len(q) and ch == q[qi]:
            positions.append(ti)
            qi += 1
    return qi == len(q), positions


@dataclass
class Vec2:
    x: int
    y: int


@dataclass
class DrawArea:
    pos: Vec2
    size: Vec2


class BorderStyle(Enum):
    NONE = 0
    HARD = 1
    LIGHT = 2


class SplitTree:

    class SplitDirection(Enum):
        VERTICAL = 1
        HORIZONTAL = 2

    @dataclass
    class Split:
        direction: SplitTree.SplitDirection
        children: list[SplitTree.Node]
        border: BorderStyle = BorderStyle.HARD

    @dataclass
    class Node:
        name: str
        size: int
        split: SplitTree.Split | None = None

    def __init__(self):

        self.root = self.Node(
            "root",
            -1,
            self.Split(
                self.SplitDirection.VERTICAL,
                [
                    self.Node("title", 2),
                    self.Node(
                        "content",
                        -1,
                        self.Split(
                            self.SplitDirection.HORIZONTAL,
                            [
                                self.Node(
                                    "refs",
                                    -1,
                                    self.Split(
                                        self.SplitDirection.VERTICAL,
                                        [
                                            self.Node("ref_list", -1),
                                            self.Node("ref_selection", 2),
                                        ],
                                        border=BorderStyle.LIGHT,
                                    ),
                                ),
                                self.Node(
                                    "details",
                                    -1,
                                    self.Split(
                                        self.SplitDirection.VERTICAL,
                                        [
                                            self.Node("details_head", 2),
                                            self.Node("details_body", -1),
                                        ],
                                        border=BorderStyle.NONE,
                                    ),
                                ),
                            ],
                        ),
                    ),
                    self.Node("status", 2),
                ],
            ),
        )

        self.drawareas: dict[str, DrawArea] = {}

    def update(self, stdscr):
        height, width = stdscr.getmaxyx()
        self.drawareas.clear()
        self._compute(self.root, DrawArea(Vec2(0, 0), Vec2(width, height)))

    def _compute(self, node: SplitTree.Node, area: DrawArea) -> None:
        # Record this node's draw area, then recurse into children
        self.drawareas[node.name] = area
        if node.split is None:
            return

        children = node.split.children
        is_vertical = node.split.direction == self.SplitDirection.VERTICAL
        total = area.size.y if is_vertical else area.size.x

        # Fixed children claim their exact size; weighted children share what's left
        has_border = node.split.border != BorderStyle.NONE
        n_borders = (len(children) - 1) if has_border else 0
        fixed_total = sum(c.size for c in children if c.size > 0)
        weight_total = sum(-c.size for c in children if c.size < 0)
        remaining = max(
            0, total - fixed_total - n_borders
        )  # space available to weighted children

        sizes: list[int] = []
        for c in children:
            if c.size > 0:
                sizes.append(c.size)
            else:
                weight = -c.size
                sizes.append(
                    int(remaining * weight / weight_total) if weight_total else 0
                )

        # Give rounding remainder to last weighted child
        diff = (total - n_borders) - sum(sizes)
        if diff != 0:
            for i in reversed(range(len(children))):
                if children[i].size < 0:
                    sizes[i] += diff
                    break

        # Walk children in order, advancing the offset and skipping one char per border
        offset = area.pos.y if is_vertical else area.pos.x
        for i, (child, sz) in enumerate(zip(children, sizes)):
            if is_vertical:
                child_area = DrawArea(Vec2(area.pos.x, offset), Vec2(area.size.x, sz))
            else:
                child_area = DrawArea(Vec2(offset, area.pos.y), Vec2(sz, area.size.y))
            self._compute(child, child_area)
            offset += sz
            if has_border and i < len(children) - 1:
                offset += 1  # reserve one char for the border line

    def draw_borders(self, stdscr) -> None:
        self._draw_node_borders(stdscr, self.root)

    def _draw_node_borders(self, stdscr, node: SplitTree.Node) -> None:
        if node.split is None:
            return
        if node.split.border != BorderStyle.NONE:
            area = self.drawareas[node.name]
            is_vertical = node.split.direction == self.SplitDirection.VERTICAL
            attr = curses.A_DIM if node.split.border == BorderStyle.LIGHT else 0
            # Draw a divider after each child except the last
            for child in node.split.children[:-1]:
                child_area = self.drawareas[child.name]
                if is_vertical:
                    # Horizontal rule on the row immediately after the child
                    y = child_area.pos.y + child_area.size.y
                    try:
                        stdscr.addnstr(
                            y, area.pos.x, "─" * area.size.x, area.size.x, attr
                        )
                    except curses.error:
                        pass
                else:
                    # Vertical bar on the column immediately after the child
                    x = child_area.pos.x + child_area.size.x
                    for row in range(area.pos.y, area.pos.y + area.size.y):
                        try:
                            stdscr.addch(row, x, curses.ACS_VLINE, attr)
                        except curses.error:
                            pass
        # Recurse so nested splits draw their own dividers
        for child in node.split.children:
            self._draw_node_borders(stdscr, child)

    def __getitem__(self, key: str) -> DrawArea:
        return self.drawareas[key]


class InputMode(Enum):
    NAV = 1
    SET_FILTER = 2
    SELECT = 3


class Cmd:
    def __init__(
        self,
        name: str,
        keys: list,
        func,
        *,
        label: str | None = None,
        group: str | None = None,
    ):
        self.name = name
        self.keys = keys
        self.func = func
        self.label = label if label is not None else name
        self.group = group if group is not None else name


def _key_label(key) -> str:
    """Return a short human-readable string for a key (str char or int keycode)."""
    if isinstance(key, str):
        return key
    _NAMES = {
        curses.KEY_UP: "↑",
        curses.KEY_DOWN: "↓",
        curses.KEY_LEFT: "←",
        curses.KEY_RIGHT: "→",
        curses.KEY_BACKSPACE: "Bksp",
        127: "Bksp",
        263: "Bksp",
        curses.KEY_PPAGE: "Pg↑",
        curses.KEY_NPAGE: "Pg↓",
        10: "↵",
        13: "↵",
        27: "ESC",
    }
    return _NAMES.get(key, f"<{key}>")


_PARENT_REF = object()  # sentinel for the ".." back-navigation entry


# ---------------------------------------------------------------------------
# Modal dialog
# ---------------------------------------------------------------------------


class ModalDialog:
    """A small modal dialog with a title, a list of selectable options and a
    fixed key-hint footer.  Drawn centred over the existing UI with a thick
    border.  Holds its own selection state and key dispatch.

    Each option is a :class:`Cmd`; ``cmd.name`` is the label shown in the
    list, ``cmd.keys`` are direct shortcut keys, and ``cmd.func`` is invoked
    when the option is activated (either via Enter on the highlighted row or
    one of its shortcut keys).

    Built-in keys:
      * ``j`` / ``Down``  – move selection down
      * ``k`` / ``Up``    – move selection up
      * ``Enter``         – activate the highlighted option
      * ``Esc``           – cancel (close without activating)

    Any key that activates an option or cancels the dialog sets ``done`` to
    True; the owning controller is expected to discard the dialog afterwards.
    """

    _FOOTER = " Enter=Accept   Esc=Cancel "

    def __init__(self, title: str, options: list[Cmd]):
        self.title = title
        self.options = options
        self.selected_idx = 0
        self.done = False
        self.input_mode = InputMode.SELECT
        # Built-in dialog controls: navigation, accept, cancel.  Stored as a
        # Cmd table keyed by *input_mode* to mirror the controller's dispatch
        # pattern.
        self.cmds: dict[InputMode, list[Cmd]] = {
            InputMode.SELECT: [
                Cmd(
                    "dialog_up",
                    ["k", curses.KEY_UP],
                    self._move_up,
                    label="move cursor",
                    group="move",
                ),
                Cmd(
                    "dialog_down",
                    ["j", curses.KEY_DOWN],
                    self._move_down,
                    label="move cursor",
                    group="move",
                ),
                Cmd("dialog_accept", [10, 13], self._accept, label="accept"),
                Cmd("dialog_cancel", [27], self._cancel, label="cancel"),
            ],
        }

    def _move_up(self) -> None:
        n = len(self.options)
        if n:
            self.selected_idx = (self.selected_idx - 1) % n

    def _move_down(self) -> None:
        n = len(self.options)
        if n:
            self.selected_idx = (self.selected_idx + 1) % n

    def _accept(self) -> None:
        if self.options:
            self.options[self.selected_idx].func()
        self.done = True

    def _cancel(self) -> None:
        self.done = True

    def handle_key(self, key: int) -> None:
        # Built-in dialog controls (navigation / accept / cancel)
        for cmd in self.cmds.get(self.input_mode, []):
            if any(key == (ord(k) if isinstance(k, str) else k) for k in cmd.keys):
                cmd.func()
                return
        # Per-option shortcut keys
        for cmd in self.options:
            if any(key == (ord(k) if isinstance(k, str) else k) for k in cmd.keys):
                cmd.func()
                self.done = True
                return

    def draw(self, stdscr) -> None:
        scr_h, scr_w = stdscr.getmaxyx()
        labels = [opt.name for opt in self.options]
        inner_w = max(
            len(self.title),
            max((len(l) for l in labels), default=0) + 4,  # " > " prefix + 1
            len(self._FOOTER),
        )
        inner_w = min(inner_w, max(scr_w - 4, 1))
        w = inner_w + 2  # add side borders
        # Rows inside borders: title, sep, options..., sep, footer
        inner_h = 1 + 1 + len(labels) + 1 + 1
        h = inner_h + 2
        h = min(h, max(scr_h, 3))

        y0 = max((scr_h - h) // 2, 0)
        x0 = max((scr_w - w) // 2, 0)

        # Border characters (thick / double-style box)
        top = "┏" + "━" * (w - 2) + "┓"
        bot = "┗" + "━" * (w - 2) + "┛"
        sep = "┣" + "━" * (w - 2) + "┫"
        side = "┃"

        attr = curses.A_BOLD
        try:
            stdscr.addnstr(y0, x0, top, w, attr)
        except curses.error:
            pass

        def _draw_row(y: int, content: str, row_attr: int = 0) -> None:
            # Pad/truncate content to fit inside the borders
            text = content[:inner_w].ljust(inner_w)
            try:
                stdscr.addnstr(y, x0, side, 1, attr)
                stdscr.addnstr(y, x0 + 1, text, inner_w, row_attr)
                stdscr.addnstr(y, x0 + 1 + inner_w, side, 1, attr)
            except curses.error:
                pass

        # Title
        _draw_row(
            y0 + 1, self.title.center(inner_w), curses.A_BOLD | curses.color_pair(2)
        )
        # Separator under title
        try:
            stdscr.addnstr(y0 + 2, x0, sep, w, attr)
        except curses.error:
            pass
        # Options
        for i, label in enumerate(labels):
            marker = " > " if i == self.selected_idx else "   "
            row_attr = curses.color_pair(1) if i == self.selected_idx else 0
            _draw_row(y0 + 3 + i, marker + label, row_attr)
        # Separator above footer
        sep_y = y0 + 3 + len(labels)
        try:
            stdscr.addnstr(sep_y, x0, sep, w, attr)
        except curses.error:
            pass
        # Footer
        _draw_row(sep_y + 1, self._FOOTER, curses.A_DIM)
        # Bottom border
        try:
            stdscr.addnstr(sep_y + 2, x0, bot, w, attr)
        except curses.error:
            pass


# ---------------------------------------------------------------------------
# Navigation history
# ---------------------------------------------------------------------------


@dataclass
class NavEntry:
    node: o6.NodeId
    selected_nodeid: str | None = None  # str(ref.nodeid) of selected item, or None


class PathNavigator:
    """Manages backward/forward navigation history with per-node selection state.

    push(nodeid, current_selected_nodeid)
        Navigate to *nodeid*.  The str-nodeid of the currently selected
        reference is saved on the current entry before moving.  If *nodeid*
        matches the top of the forward stack that entry's saved nodeid is
        returned; otherwise the forward stack is cleared and *None* is
        returned.

    pop() -> (nodeid, selected_nodeid) | None
        Go back one step.  The current entry is pushed onto the forward stack
        so a subsequent push can restore it.  Returns the previous node with
        its saved selected_nodeid, or *None* when already at the bottom.
    """

    def __init__(self, client: o6.Client, initial: o6.NodeId) -> None:
        self._client = client
        self._stack: list[NavEntry] = [NavEntry(initial)]
        self._forward: list[NavEntry] = []
        self.path: list[o6.NodeId] = []
        self.browse_path: str = ""
        self.pending_restore: str | None = None
        self._update_path(initial)

    @property
    def current(self) -> o6.NodeId:
        return self._stack[-1].node

    def push(
        self,
        nodeid: o6.NodeId,
        current_selected_nodeid: str | None = None,
    ) -> None:
        """Navigate to *nodeid*.  Sets *pending_restore* to the saved selection for that node."""
        self._stack[-1].selected_nodeid = current_selected_nodeid

        if self._forward and str(self._forward[-1].node) == str(nodeid):
            entry = self._forward.pop()
            self._stack.append(entry)
            self.pending_restore = entry.selected_nodeid
        else:
            self._forward.clear()
            self._stack.append(NavEntry(nodeid))
            self.pending_restore = None
        self._update_path(self.current)

    def pop(self, current_selected_nodeid: str | None = None) -> bool:
        """Go back.  Saves *current_selected_nodeid* on the current entry before
        moving it to the forward stack.  Sets *pending_restore* to the previous
        node's saved selection.  Returns *False* when already at the bottom."""
        if len(self._stack) <= 1:
            return False
        self._stack[-1].selected_nodeid = current_selected_nodeid
        current = self._stack.pop()
        self._forward.append(current)
        prev = self._stack[-1]
        self.pending_restore = prev.selected_nodeid
        self._update_path(prev.node)
        return True

    def _update_path(self, node: o6.NodeId) -> None:
        root_str = str(o6.NodeId(self._client.root))
        chain: list[tuple[o6.NodeId, str]] = []
        current = node
        visited: set[str] = set()
        while True:
            cur_str = str(current)
            if cur_str in visited:
                break
            visited.add(cur_str)
            name = str(self._client.read(current, attr=o6.AttributeId.BROWSENAME))
            chain.append((current, name))
            if cur_str == root_str:
                break
            parents = cast(
                list[o6.ReferenceDescription],
                self._client.browse(
                    current,
                    direction=o6.BrowseDirection.INVERSE,
                    result_mask=o6.BrowseResultMask.BROWSENAME,
                ),
            )
            if not parents:
                break
            current = o6.NodeId(str(parents[0].nodeid))
        chain.reverse()
        self.path = [nid for nid, _ in chain]
        # skip chain[0] (root itself) so that root_node[browse_path] resolves to the current node.
        self.browse_path = (
            "/" + "/".join(name for _, name in chain[1:]) if len(chain) > 1 else "/"
        )

    def can_go_back(self) -> bool:
        return len(self._stack) > 1

    def can_go_forward(self) -> bool:
        return bool(self._forward)

    def restore(self, filtered_refs: list, viewport_h: int) -> tuple[int, int] | None:
        """Apply pending selection restore against *filtered_refs*.

        Returns *(selected_idx, scroll)* when a restore was pending, else *None*.
        """
        if self.pending_restore is None:
            return None
        nodeid_str = self.pending_restore
        self.pending_restore = None
        for i, ref in enumerate(filtered_refs):
            if ref is not _PARENT_REF and str(ref.nodeid) == nodeid_str:
                return i, max(0, i - viewport_h // 2)
        return 0, 0


# ---------------------------------------------------------------------------
# Model
# ---------------------------------------------------------------------------


class BrowserModel:
    """All state and OPC UA interactions. Holds no curses/draw logic."""

    def __init__(self, client: o6.Client, start_node: o6.NodeId | None = None):
        self.client = client

        # Navigation state
        _start = (
            o6.NodeId(start_node) if start_node is not None else o6.NodeId(client.root)
        )
        self.navigator: PathNavigator = PathNavigator(client, _start)

        # Browse + filter state
        self.refs: list[o6.ReferenceDescription] = []
        self.filtered_refs: list = []
        self.filter_query: str = ""
        self.match_positions_map: dict[int, list[int]] = {}
        self.selected_idx: int = 0
        self.scroll: int = 0

        # Detail view state
        self.node_details: list[tuple[str, str]] = []

        # Status message (one-shot, cleared by controller each frame)
        self.message: str = ""

        self._viewport_h: int = 20

        self.update()

    @property
    def node(self) -> o6.NodeId:
        return self.navigator.current

    @property
    def path(self) -> list[o6.NodeId]:
        return self.navigator.path

    @property
    def browse_path(self) -> str:
        return self.navigator.browse_path

    # -- OPC UA queries ----------------------------------------------------

    def _update_refs(self) -> None:
        self.refs = cast(
            list[o6.ReferenceDescription],
            self.client.browse(
                self.node,
                result_mask=o6.BrowseResultMask(
                    o6.BrowseResultMask.BROWSENAME
                    | o6.BrowseResultMask.NODECLASS
                    | o6.BrowseResultMask.REFERENCETYPEID
                ),
            ),
        )
        self.filtered_refs = [_PARENT_REF] if len(self.path) > 1 else []
        self.match_positions_map = {}
        for ref in self.refs:
            matched, positions = fuzzy_match(self.filter_query, str(ref.browse_name))
            if matched:
                self.filtered_refs.append(ref)
                if self.filter_query:
                    self.match_positions_map[id(ref)] = positions
        if self.selected_idx >= len(self.filtered_refs):
            self.selected_idx = max(len(self.filtered_refs) - 1, 0)

    def _current_selected_nodeid(self) -> str | None:
        """Return str(nodeid) of the currently selected reference, or None."""
        if not self.filtered_refs or self.selected_idx >= len(self.filtered_refs):
            return None
        ref = self.filtered_refs[self.selected_idx]
        if ref is _PARENT_REF:
            return None
        return str(ref.nodeid)

    def _update_node_details(self) -> None:
        if not self.filtered_refs:
            self.node_details = []
            return

        ref = self.filtered_refs[self.selected_idx]
        if ref is _PARENT_REF:
            self.node_details = []
            return
        nodeid = o6.NodeId(str(ref.nodeid))
        node_class = ref.node_class

        def tryread(label, attr):
            try:
                return (label, str(self.client.read(nodeid, attr=attr)))
            except Exception:
                return None

        pairs: list[tuple[str, str]] = [
            ("NodeId", str(nodeid)),
            ("Class", node_class.name),
        ]
        for pair in [
            tryread("DisplayName", o6.AttributeId.DISPLAYNAME),
            tryread("BrowseName", o6.AttributeId.BROWSENAME),
            tryread("Description", o6.AttributeId.DESCRIPTION),
            tryread("WriteMask", o6.AttributeId.WRITEMASK),
            tryread("UserWriteMask", o6.AttributeId.USERWRITEMASK),
        ]:
            if pair:
                pairs.append(pair)

        if node_class == o6.NodeClass.VARIABLE:
            extras = [
                tryread("Value", o6.AttributeId.VALUE),
                tryread("DataType", o6.AttributeId.DATATYPE),
                tryread("ValueRank", o6.AttributeId.VALUERANK),
                tryread("ArrayDimensions", o6.AttributeId.ARRAYDIMENSIONS),
                tryread("AccessLevel", o6.AttributeId.ACCESSLEVEL),
                tryread("UserAccessLevel", o6.AttributeId.USERACCESSLEVEL),
                tryread("MinSamplingInterval", o6.AttributeId.MINIMUMSAMPLINGINTERVAL),
                tryread("Historizing", o6.AttributeId.HISTORIZING),
            ]
        elif node_class == o6.NodeClass.OBJECT:
            extras = [tryread("EventNotifier", o6.AttributeId.EVENTNOTIFIER)]
        elif node_class == o6.NodeClass.METHOD:
            extras = [
                tryread("Executable", o6.AttributeId.EXECUTABLE),
                tryread("UserExecutable", o6.AttributeId.USEREXECUTABLE),
            ]
        elif node_class in (o6.NodeClass.OBJECTTYPE, o6.NodeClass.DATATYPE):
            extras = [tryread("IsAbstract", o6.AttributeId.ISABSTRACT)]
            if node_class == o6.NodeClass.DATATYPE:
                extras.append(
                    tryread("DataTypeDefinition", o6.AttributeId.DATATYPEDEFINITION)
                )
        elif node_class == o6.NodeClass.VARIABLETYPE:
            extras = [
                tryread("IsAbstract", o6.AttributeId.ISABSTRACT),
                tryread("Value", o6.AttributeId.VALUE),
                tryread("DataType", o6.AttributeId.DATATYPE),
                tryread("ValueRank", o6.AttributeId.VALUERANK),
                tryread("ArrayDimensions", o6.AttributeId.ARRAYDIMENSIONS),
            ]
        elif node_class == o6.NodeClass.REFERENCETYPE:
            extras = [
                tryread("IsAbstract", o6.AttributeId.ISABSTRACT),
                tryread("Symmetric", o6.AttributeId.SYMMETRIC),
                tryread("InverseName", o6.AttributeId.INVERSENAME),
            ]
        elif node_class == o6.NodeClass.VIEW:
            extras = [
                tryread("ContainsNoLoops", o6.AttributeId.CONTAINSNOLOOPS),
                tryread("EventNotifier", o6.AttributeId.EVENTNOTIFIER),
            ]
        else:
            extras = []

        for pair in extras:
            if pair:
                pairs.append(pair)

        self.node_details = pairs

    def update(self) -> None:
        """Refresh all model state for the current node."""
        self._update_refs()
        result = self.navigator.restore(self.filtered_refs, self._viewport_h)
        if result is not None:
            self.selected_idx, self.scroll = result
        self._update_node_details()

    # -- Mutations ---------------------------------------------------------

    def move_selection(
        self, delta: int, viewport_h: int, *, clamp: bool = False
    ) -> None:
        if not self.filtered_refs:
            self.selected_idx = 0
            self.scroll = 0
            return
        n = len(self.filtered_refs)
        if clamp:
            self.selected_idx = max(0, min(n - 1, self.selected_idx + delta))
        else:
            self.selected_idx = (self.selected_idx + delta) % n
        if self.selected_idx >= self.scroll + viewport_h:
            self.scroll = self.selected_idx - viewport_h + 1
        elif self.selected_idx < self.scroll:
            self.scroll = self.selected_idx

    def navigate_into(self) -> None:
        if not self.filtered_refs:
            return
        ref = self.filtered_refs[self.selected_idx]
        if ref is _PARENT_REF:
            return
        target = o6.NodeId(str(ref.nodeid))
        try:
            children = self.client.browse(
                target, result_mask=o6.BrowseResultMask.BROWSENAME
            )
        except Exception as e:
            self.message = f"Error: {e}"
            return
        if not children:
            return
        self.navigator.push(target, self._current_selected_nodeid())
        self.selected_idx = 0
        self.scroll = 0
        self.filter_query = ""

    def navigate_parent(self) -> None:
        if len(self.path) <= 1:
            self.message = "Already at root"
            return
        parent = self.path[-2]
        self.navigator.push(parent, self._current_selected_nodeid())
        self.selected_idx = 0
        self.scroll = 0
        self.filter_query = ""

    def navigate_back(self) -> None:
        if not self.navigator.pop(self._current_selected_nodeid()):
            self.message = "No backward history"
            return
        self.selected_idx = 0
        self.scroll = 0
        self.filter_query = ""

    # -- Filter mutations --------------------------------------------------

    def begin_filter(self) -> None:
        self.filter_query = ""
        self.selected_idx = 0
        self.scroll = 0

    def clear_filter(self) -> None:
        self.filter_query = ""
        self.selected_idx = 0
        self.scroll = 0

    def filter_append(self, ch: str) -> None:
        self.filter_query += ch
        self.selected_idx = 0
        self.scroll = 0

    def filter_backspace(self) -> None:
        self.filter_query = self.filter_query[:-1]
        self.selected_idx = 0
        self.scroll = 0


# ---------------------------------------------------------------------------
# View
# ---------------------------------------------------------------------------


class BrowserView:
    """Renders the model into a curses screen. Holds no state of its own
    beyond the layout cache."""

    def __init__(self):
        self.layout = SplitTree()

    def init_colors(self) -> None:
        curses.curs_set(0)
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)  # selected row
        curses.init_pair(2, curses.COLOR_CYAN, -1)  # header/title
        curses.init_pair(3, curses.COLOR_YELLOW, -1)  # node info
        curses.init_pair(4, curses.COLOR_GREEN, -1)  # status bar
        curses.init_pair(5, curses.COLOR_RED, -1)  # status bar message

    def refs_viewport_height(self) -> int:
        return self.layout["ref_list"].size.y

    def render(
        self,
        stdscr,
        model: BrowserModel,
        input_mode: InputMode,
        dialog: ModalDialog | None = None,
        legend: list[tuple[str, str]] | None = None,
    ) -> None:
        stdscr.clear()
        self.layout.update(stdscr)
        self.layout.draw_borders(stdscr)
        self._draw_title_bar(stdscr)
        self._draw_browse_path(stdscr, model)
        self._draw_refs(stdscr, model)
        self._draw_node_details(stdscr, model)
        self._draw_status_bar(stdscr, model, input_mode, legend)
        if dialog is not None:
            dialog.draw(stdscr)
        stdscr.refresh()

    # -- sections ---------------------------------------------------------

    def _draw_title_bar(self, stdscr):
        d = self.layout["title"]
        stdscr.attron(curses.color_pair(2) | curses.A_BOLD)
        stdscr.addnstr(
            d.pos.y, d.pos.x, " o6 - OPC UA Browser ".center(d.size.x), d.size.x
        )
        stdscr.attroff(curses.color_pair(2) | curses.A_BOLD)

    def _draw_browse_path(self, stdscr, model: BrowserModel):
        d = self.layout["title"]
        browse_path = model.browse_path
        stdscr.attron(curses.A_BOLD)
        stdscr.addstr(d.pos.y + 1, d.pos.x, " Browse Path: ")
        stdscr.attroff(curses.A_BOLD)
        stdscr.addnstr(
            d.pos.y + 1,
            d.pos.x + len(" Browse Path: "),
            browse_path.ljust(d.size.x),
            d.size.x - len(" Browse Path: ") - 1,
        )

    def _draw_refs(self, stdscr, model: BrowserModel):
        d = self.layout["ref_list"]
        for list_idx in range(
            model.scroll, min(model.scroll + d.size.y, len(model.filtered_refs))
        ):
            ref = model.filtered_refs[list_idx]
            row_y = d.pos.y + (list_idx - model.scroll)
            if row_y >= d.pos.y + d.size.y:
                break
            is_selected = list_idx == model.selected_idx
            base_attr = curses.color_pair(1) if is_selected else 0
            if ref is _PARENT_REF:
                line = " .."
                stdscr.addnstr(
                    row_y,
                    d.pos.x,
                    line.ljust(d.size.x),
                    d.size.x,
                    base_attr | curses.A_DIM,
                )
                continue
            bn = str(ref.browse_name)
            prefix = " "
            line = (prefix + bn)[: d.size.x].ljust(d.size.x)
            stdscr.addnstr(row_y, d.pos.x, line, d.size.x, base_attr)
            if model.filter_query:
                positions = set(model.match_positions_map.get(id(ref), []))
                for i, ch in enumerate(bn):
                    col = len(prefix) + i
                    if col >= d.size.x:
                        break
                    if i in positions:
                        try:
                            stdscr.addch(row_y, col, ch, base_attr | curses.A_BOLD)
                        except curses.error:
                            pass

        # Bottom of left pane: selected ref details
        d = self.layout["ref_selection"]
        if model.filtered_refs:
            sel_ref = model.filtered_refs[model.selected_idx]
            if sel_ref is not _PARENT_REF:
                ref_detail = (
                    f" {sel_ref.browse_name}  "
                    f"id={sel_ref.nodeid}  "
                    f"type={sel_ref.reference_type_id}"
                )
                stdscr.addnstr(
                    d.pos.y, 0, ref_detail[: d.size.x].ljust(d.size.x), d.size.x
                )

    def _draw_node_details(self, stdscr, model: BrowserModel):
        dh = self.layout["details_head"]
        d = self.layout["details_body"]

        stdscr.attron(curses.A_BOLD)
        stdscr.addnstr(
            dh.pos.y,
            dh.pos.x,
            " Node Details"[: dh.size.x].ljust(dh.size.x),
            dh.size.x,
        )
        stdscr.attroff(curses.A_BOLD)

        if not model.node_details:
            return

        col = max(len(label) for label, _ in model.node_details)
        for i, (label, val) in enumerate(model.node_details):
            row_y = d.pos.y + i
            if row_y >= d.pos.y + d.size.y:
                break
            prefix = f" {label.ljust(col)} : "
            val = (
                val.replace("\r\n", " ")
                .replace("\n", " ")
                .replace("\r", " ")
                .replace("\t", " ")
            )
            avail = d.size.x - len(prefix) - 1
            if avail > 0 and len(val) > avail:
                val = val[: max(0, avail - 3)] + "..."
            line = (prefix + val)[: d.size.x - 1]
            stdscr.attron(curses.color_pair(3))
            stdscr.addnstr(row_y, d.pos.x, line, d.size.x - 1)
            stdscr.attroff(curses.color_pair(3))

    def _draw_status_bar(
        self,
        stdscr,
        model: BrowserModel,
        input_mode: InputMode,
        legend: list[tuple[str, str]] | None = None,
    ):
        d = self.layout["status"]
        if input_mode == InputMode.SET_FILTER:
            filter_display = f" Filter: {model.filter_query}▌"
            stdscr.attron(curses.color_pair(4) | curses.A_BOLD)
            stdscr.addnstr(
                d.pos.y, d.pos.x, filter_display.ljust(d.size.x), d.size.x - 1
            )
            stdscr.attroff(curses.color_pair(4) | curses.A_BOLD)
        else:
            base = curses.color_pair(4)
            key_attr = base | curses.A_BOLD
            sep_attr = base | curses.A_DIM
            label_attr = base
            x = d.pos.x
            max_x = d.pos.x + d.size.x - 1

            def _write(text: str, attr: int) -> None:
                nonlocal x
                if x >= max_x or not text:
                    return
                n = min(len(text), max_x - x)
                if n <= 0:
                    return
                stdscr.addnstr(d.pos.y, x, text, n, attr)
                x += n

            if model.message:
                msg = f" {model.message} "
                _write(msg, base | curses.A_BOLD | curses.color_pair(5))

            if legend:
                _write(" ", base)
                for i, (keys_str, label_str) in enumerate(legend):
                    if i > 0:
                        _write("  ", base)
                    for j, key in enumerate(keys_str.split("/")):
                        if j > 0:
                            _write("/", sep_attr)
                        _write(key, key_attr)
                    _write(":", sep_attr)
                    _write(label_str, label_attr)

            if x < max_x:
                stdscr.addnstr(d.pos.y, x, " " * (max_x - x), max_x - x, base)


# ---------------------------------------------------------------------------
# Controller
# ---------------------------------------------------------------------------


class InteractiveBrowser:
    """Controller: wires model + view together and dispatches input."""

    def __init__(self, client: o6.Client, start_node: o6.NodeId | None = None):
        self.model = BrowserModel(client, start_node)
        self.view = BrowserView()
        self.input_mode = InputMode.NAV
        self.running = False
        self.dialog: ModalDialog | None = None
        self.result: Any | None = None

        self.cmds: dict[InputMode, list[Cmd]] = {
            InputMode.NAV: [
                Cmd("quit", ["q", "Q"], self._quit, label="quit"),
                Cmd(
                    "nav_down",
                    ["j", curses.KEY_DOWN],
                    self._navigate_down,
                    label="move",
                    group="move",
                ),
                Cmd(
                    "nav_up",
                    ["k", curses.KEY_UP],
                    self._navigate_up,
                    label="move",
                    group="move",
                ),
                Cmd(
                    "nav_page_down",
                    ["J", curses.KEY_NPAGE],
                    self._navigate_page_down,
                    label="move page",
                    group="page",
                ),
                Cmd(
                    "nav_page_up",
                    ["K", curses.KEY_PPAGE],
                    self._navigate_page_up,
                    label="move page",
                    group="page",
                ),
                Cmd(
                    "nav_back",
                    ["h", curses.KEY_LEFT, curses.KEY_BACKSPACE],
                    self.model.navigate_back,
                    label="back",
                ),
                Cmd(
                    "nav_into",
                    ["l", curses.KEY_RIGHT],
                    self.model.navigate_into,
                    label="open",
                    group="open",
                ),
                Cmd("enter", [10, 13], self._enter, label="open", group="open"),
                Cmd("filter", ["/"], self._enter_filter_mode, label="set filter"),
                Cmd(
                    "clear_filter", [27], self.model.clear_filter, label="clear filter"
                ),
                Cmd("select", ["s", "S"], self._select, label="select"),
            ],
            InputMode.SET_FILTER: [
                Cmd("filter_cancel", [27], self._filter_cancel, label="cancel"),
                Cmd(
                    "filter_confirm", [10, 13], self._exit_filter_mode, label="confirm"
                ),
                Cmd(
                    "filter_backspace",
                    [curses.KEY_BACKSPACE, 127, 263],
                    self.model.filter_backspace,
                    label="del",
                ),
            ],
        }
        self.default_handlers = {
            InputMode.SET_FILTER: self._filter_type,
        }

    # -- mode transitions --------------------------------------------------

    def _quit(self):
        self.running = False

    def _enter(self):
        if not self.model.filtered_refs:
            return
        ref = self.model.filtered_refs[self.model.selected_idx]
        if ref is _PARENT_REF:
            self.model.navigate_parent()
        else:
            self.model.navigate_into()

    def _enter_filter_mode(self):
        self.input_mode = InputMode.SET_FILTER
        self.model.begin_filter()

    def _exit_filter_mode(self):
        self.input_mode = InputMode.NAV

    def _filter_cancel(self):
        self.model.clear_filter()
        self.input_mode = InputMode.NAV

    def _filter_type(self, key: int):
        if 32 <= key < 256:
            self.model.filter_append(chr(key))

    def _navigate_up(self):
        self.model.move_selection(-1, self.view.refs_viewport_height())

    def _navigate_down(self):
        self.model.move_selection(1, self.view.refs_viewport_height())

    def _navigate_page_up(self):
        self.model.move_selection(
            -self.view.refs_viewport_height(),
            self.view.refs_viewport_height(),
            clamp=True,
        )

    def _navigate_page_down(self):
        self.model.move_selection(
            self.view.refs_viewport_height(),
            self.view.refs_viewport_height(),
            clamp=True,
        )

    # -- select dialog -----------------------------------------------------

    def _select(self):
        """Open the ModalDialog for the currently highlighted reference."""
        if not self.model.filtered_refs:
            return
        ref = self.model.filtered_refs[self.model.selected_idx]
        if ref is _PARENT_REF:
            return
        name = str(ref.browse_name)
        nodeid_str = str(ref.nodeid)
        browse_path = f"{self.model.browse_path}/{name}"

        def _quit_with_nodeid() -> None:
            self.result = nodeid_str
            self.running = False

        def _quit_with_path() -> None:
            self.result = browse_path
            self.running = False

        def _cancel() -> None:
            pass  # dialog closes itself; nothing else to do

        self.dialog = ModalDialog(
            title=name,
            options=[
                Cmd(f"Quit with NodeId  ({nodeid_str})", ["n", "N"], _quit_with_nodeid),
                Cmd(
                    f"Quit with BrowsePath  ({browse_path})",
                    ["p", "P"],
                    _quit_with_path,
                ),
                Cmd("Cancel", ["q", "Q"], _cancel),
            ],
        )

    # -- main loop ---------------------------------------------------------

    def run(self) -> Any:
        os.environ.setdefault("ESCDELAY", "25")
        curses.wrapper(self._main)
        return self.result

    def _main(self, stdscr):
        self.running = True
        self.view.init_colors()

        while self.running:
            self.view.layout.update(stdscr)
            self.model._viewport_h = self.view.refs_viewport_height()
            self.model.update()
            self.view.render(
                stdscr, self.model, self.input_mode, self.dialog, self._legend()
            )
            self.model.message = ""

            key = stdscr.getch()
            self._dispatch(key)

    def _legend(self) -> list[tuple[str, str]]:
        """Build structured (keys, label) pairs from the current input mode's cmds.

        Cmds sharing the same ``group`` are merged so that e.g. nav_up and
        nav_down appear as a single ("j/k/↓/↑", "move") token.
        When a dialog is active its cmds take precedence.
        """
        if self.dialog is not None:
            src = self.dialog.cmds.get(self.dialog.input_mode, [])
        else:
            src = self.cmds.get(self.input_mode, [])
        groups: dict[str, tuple[str, list]] = {}
        for cmd in src:
            if cmd.group not in groups:
                groups[cmd.group] = (cmd.label, [])
            groups[cmd.group][1].extend(cmd.keys)
        result: list[tuple[str, str]] = []
        for label, keys in groups.values():
            unique: list[str] = []
            seen: set[str] = set()
            for k in keys:
                lbl = _key_label(k)
                if lbl not in seen:
                    seen.add(lbl)
                    unique.append(lbl)
            result.append(("/".join(unique), label))
        return result

    def _dispatch(self, key: int) -> None:
        if self.dialog is not None:
            self.dialog.handle_key(key)
            if self.dialog.done:
                self.dialog = None
            return
        for cmd in self.cmds.get(self.input_mode, []):
            if any(key == (ord(k) if isinstance(k, str) else k) for k in cmd.keys):
                cmd.func()
                return
        handler = self.default_handlers.get(self.input_mode)
        if handler:
            handler(key)
