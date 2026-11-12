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

"""Python aliases for browsed names, matching the nodeset compiler's spelling rules.

Keep these pure helpers independent of the compiler package: `o6` must not import
`o6_nodeset_compiler`, which is a build-time tool. Each helper below is therefore a
verbatim copy of its counterpart in `o6_nodeset_compiler/_browse_names.py` and must
stay that way, so a generated package and a browsed node agree on how a BrowseName
is spelled. That module's `attribute_identifier` and `enum_member` are compiler-only
and are deliberately not copied: `o6.node` imports `browse_identifier` and nothing
else from here.
"""

import keyword
import re
import unicodedata

_LEADING_DIGIT_NAMES = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

_UNDERSCORE_RUN = re.compile(r"_+")


def _sanitize(name: str) -> str:
    """Normalize, then replace each run of characters Python rejects with one ``_``.

    NFKC comes first because Python applies it to every identifier in a source
    file. Without it the compiler emits one spelling and the class gets another:
    a decomposed ``Gro`` + ``U+0308`` reaches the module as ``Größe``, and
    ``getattr`` with the emitted text fails. Worse, two BrowseNames that differ
    only by normalization -- ``ﬁle`` and ``file`` -- are one name to Python, so a
    class body declaring both silently keeps the second and drops the first,
    while a textual collision check sees nothing wrong. Normalizing first also
    keeps what the folded character meant: ``A²`` becomes ``A2``, not ``A_``.

    The replacement test is ``str.isidentifier`` rather than the regex ``\\W``,
    because the two disagree: ``\\w`` admits anything ``str.isalnum`` accepts,
    which includes fractions an identifier may not contain.

    A run counts ``_`` itself as a separator, so ``Temperature_<No.>`` collapses
    to ``Temperature_No_`` rather than ``Temperature__No__``. A leading run is
    therefore always a single ``_``, which ``identifier`` then drops outright;
    only ``enum_member`` keeps one, and an enum's members are read off the
    generated class, never browsed.
    """
    name = unicodedata.normalize("NFKC", name)
    return _UNDERSCORE_RUN.sub("_", "".join(c if f"a{c}".isidentifier() else "_" for c in name))


def _spell_leading_digit(name: str) -> str:
    """Spell out a digit that opens a name, which no identifier may start with."""
    if name[:1] not in _LEADING_DIGIT_NAMES:
        return name
    word = _LEADING_DIGIT_NAMES[name[0]].capitalize()
    rest = name[1:]
    return word + (rest[:1].upper() + rest[1:] if rest else "")


def _underscore_identifier(name: str) -> str:
    value = _sanitize(name)
    if not value:
        value = "_"
    elif not value[:1].isidentifier():
        # A digit or a combining mark may continue an identifier but not open
        # one. ``_spell_leading_digit`` has a word for the ten ASCII digits; for
        # anything else ``_`` is the only spelling left, and a valid name beats a
        # public one.
        value = f"_{value}"
    if keyword.iskeyword(value):
        value += "_"
    return value


def identifier(name: str) -> str:
    """Return the class-level Python spelling of an OPC UA name.

    A leading digit is spelled out (``3DVector`` becomes ``ThreeDVector``), which
    matches both the OPC UA type dictionary and open62541's ``UA_ThreeDVector``.
    Prefixing ``_`` instead would hide the class from ``import *`` and make the
    backend treat the symbol as private, degrading cross-references to NodeId
    lookups. Digits elsewhere are retained.

    Leading punctuation is dropped rather than kept as that same private ``_``:
    a ``<Placeholder>`` is spelled ``Placeholder_``, marked by the ``_`` its
    closing bracket leaves behind, so it stays distinct from a plain
    ``Placeholder`` without going private. Dropping it first also lets the digit
    rule see ``<3DVector>``, which then agrees with bare ``3DVector``.
    """
    return _underscore_identifier(_spell_leading_digit(_sanitize(name).lstrip("_")))


def member_identifier(name: str) -> str:
    """Use type-name sanitization with a lowercase initial for public members.

    An ``<Identifier>`` placeholder is spelled ``identifier_`` for a member just
    as it is ``Identifier_`` for a type. Leaving the leading punctuation as a
    ``_`` would make the member private to ``o6.node.Node.__getattr__``, which
    rejects every ``_``-prefixed name so that the whole unprefixed namespace can
    belong to browsed children.
    """
    value = identifier(name)
    # Apply keyword escaping after member casing: None becomes none, not none_.
    if keyword.iskeyword(name):
        value = value[:-1]
    value = value[:1].lower() + value[1:]
    return value + "_" if keyword.iskeyword(value) else value


def browse_identifier(name: str, *, is_type: bool) -> str:
    """Return the attribute a browsed child answers to, type node or instance.

    The compiler spelling is already what Python's dot syntax reaches: ``_sanitize``
    normalizes it the way a source file is normalized and keeps only characters an
    identifier may contain, and no spelling opens with a digit. So this adds
    nothing to it, and that is the point -- it is the runtime's entry point and the
    seam that keeps the two in step. A browsed node carrying no declaration has
    only its BrowseName to go on and has to land on the attribute the generated
    declaration defines.
    """
    return identifier(name) if is_type else member_identifier(name)
