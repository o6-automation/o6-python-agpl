#!/usr/bin/env python3
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

"""Record real ptpython sessions and render their terminal output as GIFs.

Run with an environment containing o6, ptpython, pexpect, pyte, and Pillow:
    python tools/record_ptpython_demos.py

The server in the first recording stays alive while the second is recorded.
No completion results or Python output are synthesized by the renderer.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
COLUMNS, ROWS = 94, 20


def repl() -> None:
    import logging

    sys.path.insert(0, str(ROOT))
    # Finish the SDK startup banner before capturing the first prompt.
    import o6  # noqa: F401
    from prompt_toolkit.output import ColorDepth
    from ptpython.layout import CompletionVisualisation
    from ptpython.repl import embed

    logging.getLogger("o6").setLevel(logging.ERROR)

    def configure(shell):
        shell.show_signature = True
        shell.show_status_bar = False
        shell.show_meta_enter_message = False
        shell.completion_visualisation = CompletionVisualisation.POP_UP
        shell.complete_while_typing = True
        shell.enable_dictionary_completion = False
        shell.insert_blank_line_after_output = False
        shell.confirm_exit = False
        shell.color_depth = ColorDepth.TRUE_COLOR
        shell.use_code_colorscheme("monokai")

    print("\033[2J\033[H", end="", flush=True)
    namespace = {"__name__": "__main__"}
    try:
        embed(globals=namespace, configure=configure)
    finally:
        if "client" in namespace:
            namespace["client"].disconnect()
        if "server" in namespace:
            namespace["server"].stop()


class Recording:
    def __init__(self, title: str, output: Path, font_path: str):
        import pexpect
        import pyte
        from PIL import ImageFont

        self.title = title
        self.output = output
        self.screen = pyte.Screen(COLUMNS, ROWS)
        self.stream = pyte.Stream(self.screen)
        self.font = ImageFont.truetype(font_path, 20)
        self.small_font = ImageFont.truetype(font_path, 16)
        self.cell_width = round(self.font.getlength("M"))
        self.cell_height = 27
        self.width = COLUMNS * self.cell_width + 48
        self.height = ROWS * self.cell_height + 158
        self.frames = []
        self.durations = []
        self.events = []
        self.caption = ""
        self.started = time.monotonic()
        self.last_frame = self.started
        self.child = pexpect.spawn(
            sys.executable,
            [str(Path(__file__).resolve()), "--repl"],
            cwd=str(ROOT),
            env={**os.environ, "TERM": "xterm-256color", "PROMPT_TOOLKIT_NO_CPR": "1"},
            dimensions=(ROWS, COLUMNS),
            encoding="utf-8",
            timeout=15,
        )
        self.child.delaybeforesend = None
        try:
            self.child.expect_exact(">>>")
        except Exception:
            self.child.close(force=True)
            raise
        self.stream.feed(">>>")

    def pump(self, seconds: float) -> None:
        import pexpect

        deadline = time.monotonic() + seconds
        while time.monotonic() < deadline:
            try:
                data = self.child.read_nonblocking(65536, timeout=0.025)
                self.events.append([round(time.monotonic() - self.started, 3), "o", data])
                self.stream.feed(data)
            except pexpect.TIMEOUT:
                pass
            if time.monotonic() - self.last_frame >= 0.1:
                self.capture()

    def capture(self) -> None:
        from PIL import Image, ImageDraw

        now = time.monotonic()
        if self.frames:
            self.durations[-1] += max(10, round((now - self.last_frame) * 100) * 10)
        self.last_frame = now
        bg = "#171c28"
        fg = "#e6edf3"
        frame = Image.new("RGB", (self.width, self.height), bg)
        draw = ImageDraw.Draw(frame)
        draw.rectangle((0, 0, self.width, 74), fill="#232b3b")
        for index, color in enumerate(("#fb7185", "#fbbf24", "#34d399")):
            draw.ellipse((24 + index * 23, 28, 36 + index * 23, 40), fill=color)
        draw.text((112, 20), self.title, font=self.font, fill=fg)
        draw.text((24, 88), "ptpython  /  o6 OPC UA", font=self.small_font, fill="#8ba0b9")

        ansi = {
            "black": "#202633", "red": "#fb7185", "green": "#a6e22e",
            "brown": "#e6db74", "blue": "#75a7ff", "magenta": "#ae81ff",
            "cyan": "#66d9ef", "white": "#e6edf3",
            "brightblack": "#7e8da6", "brightred": "#fb7185",
            "brightgreen": "#a6e22e", "brightbrown": "#e6db74",
            "brightblue": "#75a7ff", "brightmagenta": "#ae81ff",
            "brightcyan": "#66d9ef", "brightwhite": "#ffffff",
        }

        def color(value, default):
            if value == "default":
                return default
            return ansi.get(value, "#" + value)

        for y, row in self.screen.buffer.items():
            for x, char in row.items():
                front, back = color(char.fg, fg), color(char.bg, bg)
                if char.reverse:
                    front, back = back, front
                left, top = 24 + x * self.cell_width, 120 + y * self.cell_height
                if back != bg:
                    draw.rectangle(
                        (left, top, left + self.cell_width - 1, top + self.cell_height - 1),
                        fill=back,
                    )
                if char.data.strip():
                    draw.text((left, top), char.data, font=self.font, fill=front)
        cursor = self.screen.cursor
        if not cursor.hidden and cursor.x < COLUMNS:
            left = 24 + cursor.x * self.cell_width
            top = 120 + cursor.y * self.cell_height
            draw.rectangle((left, top + 23, left + self.cell_width - 1, top + 25), fill="#66d9ef")
        draw.rectangle((0, self.height - 40, self.width, self.height), fill="#232b3b")
        draw.text((24, self.height - 31), self.caption, font=self.small_font, fill="#b9d9ee")
        # Reuse identical frames so pauses cost very little space.
        if self.frames and frame.tobytes() == self.frames[-1].tobytes():
            return
        self.frames.append(frame)
        self.durations.append(0)

    def type(self, text: str) -> None:
        for char in text:
            self.child.send(char)
            self.pump(0.035)

    def key(self, value: str, pause: float = 0.3) -> None:
        self.child.send(value)
        self.pump(pause)

    def require(self, text: str) -> None:
        screen = "\n".join(self.screen.display)
        if text not in screen:
            raise RuntimeError(f"Expected {text!r} in terminal:\n{screen}")
        if "Traceback (most recent call last)" in screen:
            raise RuntimeError(screen)

    def line(self, text: str, pause: float = 0.6) -> None:
        self.type(text)
        self.key("\r", pause)

    def completion(self, prefix: str, choice: str, suffix: str) -> None:
        self.type(prefix)
        self.pump(1.8)
        self.require(choice)
        self.key("\t", 0.5)
        self.key("\033[C", 0.2)  # Accept the selected completion with Right.
        self.require(choice)
        self.type(suffix)
        self.pump(0.5)
        self.key("\r", 0.8)

    def save(self) -> None:
        from PIL import Image

        self.capture()
        self.durations[-1] += 2500
        # A shared palette prevents color flicker between frames.
        samples = Image.new("RGB", (192, 120 * len(self.frames)))
        for index, frame in enumerate(self.frames):
            samples.paste(frame.resize((192, 120), Image.Resampling.NEAREST), (0, index * 120))
        palette = samples.quantize(colors=128)
        frames = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in self.frames]
        frames[0].save(
            self.output, save_all=True, append_images=frames[1:],
            duration=self.durations, loop=0, optimize=True, disposal=1,
        )
        cast = self.output.with_suffix(".cast")
        with cast.open("w") as stream:
            stream.write(json.dumps({"version": 2, "width": COLUMNS, "height": ROWS}) + "\n")
            stream.write(json.dumps([0, "o", ">>>"]) + "\n")
            for event in self.events:
                stream.write(json.dumps(event) + "\n")
        print(f"Saved {self.output}: {sum(self.durations) / 1000:.1f}s, {len(frames)} frames", flush=True)
        self.frames.clear()
        self.durations.clear()

    def close(self) -> None:
        if self.child.isalive():
            self.child.send("\x04")
            try:
                self.child.expect_exact("__never_matches__", timeout=5)
            except Exception:
                pass
            self.child.close(force=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repl", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--port", type=int, default=4840)
    parser.add_argument("--output", type=Path, default=ROOT / "docs/assets/ptpython")
    parser.add_argument("--font", default="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf")
    args = parser.parse_args()
    if args.repl:
        repl()
        return

    args.output.mkdir(parents=True, exist_ok=True)
    server = Recording("01  Build a server with API completion", args.output / "server-completion.gif", args.font)
    client = None
    try:
        server.caption = "Create an OPC UA server in the Python REPL"
        server.pump(1)
        server.line("from o6 import Server")
        server.line(f"server = Server(port={args.port})")
        server.caption = "API completion: choose addObject with Tab"
        server.completion("plant = server.addO", "addObject", '("Plant", server.objects)')
        server.caption = "API completion: add a Temperature variable under Plant"
        server.completion("temperature = server.addV", "addVariable", '("Temperature", plant, 22.5)')
        server.caption = "Start the server; it stays running for the client demo"
        server.completion("server.sta", "start", "()")
        server.line(f'print("Listening on opc.tcp://localhost:{args.port}")', 1)
        server.require(f"Listening on opc.tcp://localhost:{args.port}")
        server.save()

        client = Recording("02  Discover live server nodes in the REPL", args.output / "repl-completion.gif", args.font)
        client.caption = "A separate Python process connects to the server from demo 01"
        client.pump(1)
        client.line("from o6 import Client")
        client.line(f'client = Client("opc.tcp://localhost:{args.port}")')
        client.line("client.connect()", 1)
        client.caption = "Live completion: the Objects folder exposes plant"
        client.type("client.objects.")
        client.pump(2)
        client.require("plant")
        client.type("pl")
        client.pump(1)
        client.key("\t", 0.4)
        client.key("\033[C", 0.2)
        client.require("client.objects.plant")
        client.caption = "Live completion: Plant exposes its temperature variable"
        client.type(".")
        client.pump(2)
        client.require("temperature")
        client.key("\t", 0.5)
        client.key("\033[C", 0.2)
        client.require("client.objects.plant.temperature")
        client.type("()")
        client.pump(0.5)
        client.key("\r", 1)
        client.require("22.5")
        client.caption = "Read, write, and read back the live OPC UA variable"
        client.line("client.objects.plant.temperature(25.0)", 0.8)
        client.line("client.objects.plant.temperature()", 1)
        client.require("25.0")
        client.save()
    finally:
        if client is not None:
            client.close()
        server.close()


if __name__ == "__main__":
    main()
