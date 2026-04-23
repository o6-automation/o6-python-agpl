# Terminal OPC UA Browser Example

Source example: `examples/highlevel/opcua_browser.py`

This example builds a small terminal browser with `curses`. It browses references on the left and reads attributes for the selected node on the right.

## Explanation

The browser uses the newer attribute-based API when it needs node metadata. Instead of convenience properties, it reads values explicitly with `AttributeId`.

```python
node(attr=o6.AttributeId.DISPLAYNAME)
client.read(node._nodeid, attribute_id=o6.AttributeId.BROWSENAME)
```

The main loop combines `client.browse(...)`, fuzzy filtering, and keyboard navigation to keep both panes updated.

## Full source

```python
import o6
from o6 import Client, StatusCodeError, types
import socket
import curses
import os

os.environ.setdefault("ESCDELAY", "25")  # reduce ESC key delay from ~1000ms to 25ms

localhost = socket.gethostname()
endpoint_url = f"opc.tcp://{localhost}:4840"


def node_detail_lines(node, max_w):
    """Return display lines for all available attributes of a node."""
    from o6.client_nodes import (
        ObjectNode,
        VariableNode,
        MethodNode,
        ObjectTypeNode,
        VariableTypeNode,
        ReferenceTypeNode,
        DataTypeNode,
        ViewNode,
    )

    def tryread(label, fn):
        try:
            return (label, str(fn()))
        except Exception:
            return None

    pairs = [
        ("NodeId", str(node._nodeid)),
        ("Class", node._node_class.name),
    ]
    for pair in [
        tryread("DisplayName", lambda: node(attr=o6.AttributeId.DISPLAYNAME)),
        tryread("BrowseName", lambda: node(attr=o6.AttributeId.BROWSENAME)),
        tryread("Description", lambda: node(attr=o6.AttributeId.DESCRIPTION)),
        tryread("WriteMask", lambda: node(attr=o6.AttributeId.WRITEMASK)),
        tryread("UserWriteMask", lambda: node(attr=o6.AttributeId.USERWRITEMASK)),
    ]:
        if pair:
            pairs.append(pair)

    if isinstance(node, VariableNode):
        for pair in [
            tryread("Value", lambda: node(attr=o6.AttributeId.VALUE)),
            tryread("DataType", lambda: node(attr=o6.AttributeId.DATATYPE)),
            tryread("ValueRank", lambda: node(attr=o6.AttributeId.VALUERANK)),
            tryread("ArrayDimensions", lambda: node(attr=o6.AttributeId.ARRAYDIMENSIONS)),
            tryread("AccessLevel", lambda: node(attr=o6.AttributeId.ACCESSLEVEL)),
            tryread("UserAccessLevel", lambda: node(attr=o6.AttributeId.USERACCESSLEVEL)),
            tryread("MinSamplingInterval", lambda: node(attr=o6.AttributeId.MINIMUMSAMPLINGINTERVAL)),
            tryread("Historizing", lambda: node(attr=o6.AttributeId.HISTORIZING)),
        ]:
            if pair:
                pairs.append(pair)

    elif isinstance(node, ObjectNode):
        pair = tryread("EventNotifier", lambda: node(attr=o6.AttributeId.EVENTNOTIFIER))
        if pair:
            pairs.append(pair)

    elif isinstance(node, MethodNode):
        for pair in [
            tryread("Executable", lambda: node(attr=o6.AttributeId.EXECUTABLE)),
            tryread("UserExecutable", lambda: node(attr=o6.AttributeId.USEREXECUTABLE)),
        ]:
            if pair:
                pairs.append(pair)

    elif isinstance(node, ObjectTypeNode):
        pair = tryread("IsAbstract", lambda: node(attr=o6.AttributeId.ISABSTRACT))
        if pair:
            pairs.append(pair)

    elif isinstance(node, VariableTypeNode):
        for pair in [
            tryread("IsAbstract", lambda: node(attr=o6.AttributeId.ISABSTRACT)),
            tryread("Value", lambda: node(attr=o6.AttributeId.VALUE)),
            tryread("DataType", lambda: node(attr=o6.AttributeId.DATATYPE)),
            tryread("ValueRank", lambda: node(attr=o6.AttributeId.VALUERANK)),
            tryread("ArrayDimensions", lambda: node(attr=o6.AttributeId.ARRAYDIMENSIONS)),
        ]:
            if pair:
                pairs.append(pair)

    elif isinstance(node, ReferenceTypeNode):
        for pair in [
            tryread("IsAbstract", lambda: node(attr=o6.AttributeId.ISABSTRACT)),
            tryread("Symmetric", lambda: node(attr=o6.AttributeId.SYMMETRIC)),
            tryread("InverseName", lambda: node(attr=o6.AttributeId.INVERSENAME)),
        ]:
            if pair:
                pairs.append(pair)

    elif isinstance(node, DataTypeNode):
        for pair in [
            tryread("IsAbstract", lambda: node(attr=o6.AttributeId.ISABSTRACT)),
            tryread("DataTypeDefinition", lambda: node(attr=o6.AttributeId.DATATYPEDEFINITION)),
        ]:
            if pair:
                pairs.append(pair)

    elif isinstance(node, ViewNode):
        for pair in [
            tryread("ContainsNoLoops", lambda: node(attr=o6.AttributeId.CONTAINSNOLOOPS)),
            tryread("EventNotifier", lambda: node(attr=o6.AttributeId.EVENTNOTIFIER)),
        ]:
            if pair:
                pairs.append(pair)

    # Align values after the colon using the longest label width
    col = max((len(label) for label, _ in pairs), default=0)
    lines = []
    for label, val in pairs:
        prefix = f" {label.ljust(col)} : "
        avail = max_w - len(prefix) - 1
        if len(val) > avail:
            val = val[: avail - 3] + "..."
        lines.append(prefix + val)
    return lines


def fuzzy_match(query, text):
    """Subsequence fuzzy match. Returns (matched, [matched_indices_in_text])."""
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


def main(stdscr):
    curses.curs_set(0)
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)  # selected row
    curses.init_pair(2, curses.COLOR_CYAN, -1)  # header/title
    curses.init_pair(3, curses.COLOR_YELLOW, -1)  # node info
    curses.init_pair(4, curses.COLOR_GREEN, -1)  # status bar

    with Client(endpoint_url) as client:
        node = client.root
        history = []
        path_segments = [str(client.read(node._nodeid, attribute_id=o6.AttributeId.BROWSENAME))]
        selected = 0
        message = ""
        filter_query = ""
        filter_mode = False

        while True:
            stdscr.clear()
            height, width = stdscr.getmaxyx()

            # Layout rows:
            #  0        title bar
            #  1        browse path (full width, with label)
            #  2        horizontal separator
            #  3        col headers (left) | "Node Details" (right)
            #  4..      ref list (left)    | node attrs (right)
            #  H-4      left sep row for ref detail panel
            #  H-3      ref detail (left, 1 line)
            #  H-2      horizontal separator (full width)
            #  H-1      key legend

            left_w = width // 2
            div_x = left_w
            right_x = div_x + 1
            right_w = width - right_x

            REF_DETAIL_ROWS = 1
            list_start = 4
            # rows used below list: left-sep(1) + refdetail(1) + full-sep(1) + legend(1) = 4
            list_height = height - list_start - REF_DETAIL_ROWS - 4

            # --- Title bar ---
            stdscr.attron(curses.color_pair(2) | curses.A_BOLD)
            stdscr.addnstr(0, 0, " OPC UA Browser ".center(width), width)
            stdscr.attroff(curses.color_pair(2) | curses.A_BOLD)

            # --- Browse path row (row 1) ---
            browse_path = "/" + "/".join(path_segments)
            avail = width - len(" Browse Path: ") - 1
            if len(browse_path) > avail:
                browse_path = "..." + browse_path[-avail + 3 :]
            stdscr.attron(curses.A_BOLD)
            stdscr.addstr(1, 0, " Browse Path: ")
            stdscr.attroff(curses.A_BOLD)
            stdscr.addnstr(
                1,
                len(" Browse Path: "),
                browse_path.ljust(width),
                width - len(" Browse Path: ") - 1,
            )

            # --- Horizontal separator after browse path (row 2) ---
            try:
                stdscr.addnstr(2, 0, "─" * width, width - 1)
            except curses.error:
                pass

            # --- Vertical divider (rows 3..H-3) ---
            for row in range(3, height - 2):
                try:
                    stdscr.addch(row, div_x, curses.ACS_VLINE)
                except curses.error:
                    pass

            # --- Left pane: reference list ---
            refs = client.browse(
                node._nodeid,
                result_mask=(
                    o6.BrowseResultMask.BrowseName
                    | o6.BrowseResultMask.NodeClass
                    | o6.BrowseResultMask.ReferenceTypeId
                ),
            )

            # Fuzzy filter
            filtered_refs = []
            match_positions_map = {}
            for ref in refs:
                bn = str(ref.browse_name)
                matched, positions = fuzzy_match(filter_query, bn)
                if matched:
                    filtered_refs.append(ref)
                    match_positions_map[id(ref)] = positions

            if selected < 0:
                selected = 0
            if selected >= len(filtered_refs):
                selected = max(len(filtered_refs) - 1, 0)
            scroll = max(0, selected - list_height + 1)

            # Column header (row 3): show active filter query if set
            if filter_query:
                hdr = f" /{filter_query} ({len(filtered_refs)}/{len(refs)})"
                stdscr.attron(curses.color_pair(4))
                stdscr.addnstr(3, 0, hdr[:left_w].ljust(left_w), left_w)
                stdscr.attroff(curses.color_pair(4))
            else:
                stdscr.attron(curses.A_BOLD)
                stdscr.addnstr(
                    3, 0, f" {'#':>3}  browse_name"[:left_w].ljust(left_w), left_w
                )
                stdscr.attroff(curses.A_BOLD)

            for list_idx in range(
                scroll, min(scroll + list_height, len(filtered_refs))
            ):
                ref = filtered_refs[list_idx]
                row_y = list_start + (list_idx - scroll)
                if row_y >= list_start + list_height:
                    break
                bn = str(ref.browse_name)
                prefix = f" {list_idx:>3}  "
                is_selected = list_idx == selected
                base_attr = curses.color_pair(1) if is_selected else 0
                line = (prefix + bn)[:left_w].ljust(left_w)
                stdscr.addnstr(row_y, 0, line, left_w, base_attr)
                # Overdraw matched chars with bold highlight
                if filter_query:
                    positions = set(match_positions_map.get(id(ref), []))
                    for i, ch in enumerate(bn):
                        col = len(prefix) + i
                        if col >= left_w:
                            break
                        if i in positions:
                            try:
                                stdscr.addch(row_y, col, ch, base_attr | curses.A_BOLD)
                            except curses.error:
                                pass

            # --- Left pane bottom: selected ref details ---
            sep_y = height - REF_DETAIL_ROWS - 3
            stdscr.attron(curses.A_DIM)
            stdscr.addnstr(sep_y, 0, ("─" * left_w)[:left_w], left_w)
            stdscr.attroff(curses.A_DIM)

            if filtered_refs:
                sel_ref = filtered_refs[selected]
                ref_detail = (
                    f" {sel_ref.browse_name}  "
                    f"id={sel_ref.nodeid}  "
                    f"type={sel_ref.reference_type_id}"
                )
                stdscr.addnstr(sep_y + 1, 0, ref_detail[:left_w].ljust(left_w), left_w)

            # --- Right pane: current node details ---
            stdscr.attron(curses.A_BOLD)
            stdscr.addnstr(
                3, right_x, " Node Details"[:right_w].ljust(right_w), right_w
            )
            stdscr.attroff(curses.A_BOLD)

            detail_lines = node_detail_lines(node, right_w)
            for i, line in enumerate(detail_lines):
                row_y = 4 + i
                if row_y >= height - 2:
                    break
                stdscr.attron(curses.color_pair(3))
                stdscr.addnstr(row_y, right_x, line[:right_w].ljust(right_w), right_w)
                stdscr.attroff(curses.color_pair(3))

            # --- Horizontal separator before legend (row H-2) ---
            try:
                stdscr.addnstr(height - 2, 0, "─" * width, width - 1)
            except curses.error:
                pass

            # --- Key legend / filter input (row H-1) ---
            if filter_mode:
                filter_display = f" Filter: {filter_query}▌"
                stdscr.attron(curses.color_pair(4) | curses.A_BOLD)
                stdscr.addnstr(height - 1, 0, filter_display.ljust(width), width - 1)
                stdscr.attroff(curses.color_pair(4) | curses.A_BOLD)
            else:
                legend = " jk/↑↓:select  l/→/Enter:open  h/←/Bksp:back  /:filter  g:goto  q:quit"
                if message:
                    legend = f" {message}  |{legend}"
                stdscr.attron(curses.color_pair(4))
                stdscr.addnstr(height - 1, 0, legend.ljust(width), width - 1)
                stdscr.attroff(curses.color_pair(4))

            stdscr.refresh()
            message = ""

            # --- Input handling ---
            key = stdscr.getch()

            if filter_mode:
                if key == 27:  # ESC — clear and exit
                    filter_query = ""
                    filter_mode = False
                    selected = 0
                elif key in (10, 13):  # Enter — keep filter, exit mode
                    filter_mode = False
                elif key in (curses.KEY_BACKSPACE, 127, 263):
                    filter_query = filter_query[:-1]
                    selected = 0
                elif 32 <= key < 256:
                    filter_query += chr(key)
                    selected = 0
            else:
                if key == ord("q") or key == ord("Q"):
                    break
                elif key == 27:  # ESC — clear filter
                    filter_query = ""
                    selected = 0
                elif key == ord("/"):
                    filter_mode = True
                    filter_query = ""
                    selected = 0
                elif key == curses.KEY_UP or key == ord("k"):
                    selected = max(0, selected - 1)
                elif key == curses.KEY_DOWN or key == ord("j"):
                    selected = min(len(filtered_refs) - 1, selected + 1)
                elif key == curses.KEY_PPAGE:
                    selected = max(0, selected - list_height)
                elif key == curses.KEY_NPAGE:
                    selected = min(len(filtered_refs) - 1, selected + list_height)
                elif key == curses.KEY_HOME:
                    selected = 0
                elif key == curses.KEY_END:
                    selected = len(filtered_refs) - 1
                elif key in (curses.KEY_ENTER, 10, 13, curses.KEY_RIGHT, ord("l")):
                    if filtered_refs:
                        ref = filtered_refs[selected]
                        try:
                            new_node = client[types.NodeId(str(ref.nodeid))]
                            history.append((node, selected, list(path_segments)))
                            path_segments.append(str(ref.browse_name))
                            node = new_node
                            selected = 0
                            filter_query = ""
                            filter_mode = False
                        except Exception as e:
                            message = f"Error: {e}"
                elif key in (curses.KEY_BACKSPACE, 127, 263, curses.KEY_LEFT, ord("h")):
                    if history:
                        node, selected, saved_path = history.pop()
                        path_segments.clear()
                        path_segments.extend(saved_path)
                        filter_query = ""
                        filter_mode = False
                    else:
                        message = "Already at root"
                elif key == ord("g"):
                    # --- Goto: manual input loop with ESC to cancel ---
                    curses.curs_set(1)
                    prompt = " Goto: "
                    input_buf = []

                    while True:
                        display = prompt + "".join(input_buf)
                        stdscr.attron(curses.color_pair(4))
                        stdscr.addnstr(height - 1, 0, display.ljust(width), width - 1)
                        stdscr.attroff(curses.color_pair(4))
                        stdscr.move(height - 1, min(len(display), width - 1))
                        stdscr.refresh()
                        ch = stdscr.getch()
                        if ch == 27:  # ESC — cancel
                            input_buf = None
                            break
                        elif ch in (10, 13):  # Enter — confirm
                            break
                        elif ch in (curses.KEY_BACKSPACE, 127, 263):
                            if input_buf:
                                input_buf.pop()
                        elif 32 <= ch < 256:
                            input_buf.append(chr(ch))

                    curses.curs_set(0)

                    if input_buf is not None:
                        path_input = "".join(input_buf).strip()
                        if path_input:
                            segments = [
                                s for s in path_input.strip("/").split("/") if s
                            ]
                            try:
                                cur = client.root
                                new_segments = [str(client.read(cur._nodeid, attribute_id=o6.AttributeId.BROWSENAME))]
                                for seg in segments:
                                    cur = getattr(cur, seg)
                                    new_segments.append(seg)
                                # Push current state so back returns here
                                history.append((node, selected, list(path_segments)))
                                path_segments.clear()
                                path_segments.extend(new_segments)
                                node = cur
                                selected = 0
                            except KeyError as e:
                                message = f"Not found: {e}"
                            except Exception as e:
                                message = f"Error: {e}"


curses.wrapper(main)

```