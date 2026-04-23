# AUTO-GENERATED — DO NOT EDIT
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

import importlib
import logging
from concurrent.futures import ThreadPoolExecutor
from typing import Optional, Tuple

from .namespace import Namespace as _Namespace
from .namespaces import Namespaces

_logger = logging.getLogger(__name__)

ns = Namespaces()

# dependency-ordered by update_ns.py
_NODESETS_LIST: list[str] = [
    "ns0",
    "di",
    "ia",
    "machinery",
    "amb",
    "lads",
    "machine_vision",
    "robotics",
    "pumps",
    "pack_ml",
    "weihenstephan",
    "commercial_kitchen",
    "cranes_hoists",
    "pnem",
    "powerlink",
    "profinet",
    "sercos",
    "io_link",
    "adi",
    "fdi",
    "mdis",
    "auto_id",
    "cas",
    "dexpi",
    "ecm",
    "rsl",
    "gpos",
    "iredes",
    "isa95",
    "mt_connect",
    "gds",
    "onboarding",
    "open_scs",
    "safety",
    "scales",
    "scheduler",
    "wot",
    "aml",
    "bacnet",
    "csp_plus",
    "i4aas",
]


def _parse_one(
    short_name: str,
) -> Tuple[Optional[_Namespace], str, Optional[str]]:
    try:
        _mod = importlib.import_module(f"o6._nodesets.{short_name}")
        return ns._parse_nodeset_prebuilt(_mod), short_name, None
    except Exception as _e:
        return None, short_name, str(_e)


with ThreadPoolExecutor() as _pool:
    _parsed_results: list[Tuple[Optional[_Namespace], str, Optional[str]]] = list(
        _pool.map(_parse_one, _NODESETS_LIST)
    )

# Append in dependency order (sequential — _build_types needs prior types linked)
for _desc, _short_name, _parse_error in _parsed_results:
    if _parse_error is not None or _desc is None:
        _logger.warning("Could not load nodeset %r: %s", _short_name, _parse_error)
        continue
    try:
        ns.append(_desc, short_name=_short_name)
    except Exception as _e:
        _logger.warning("Could not load nodeset %r: %s", _short_name, _e)
