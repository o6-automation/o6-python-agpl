# Copyright 2026 (c) o6 Automation GmbH
from __future__ import annotations

import asyncio
import threading
from typing import Any, Tuple

import o6


class _WorkerLoop:
    def __init__(self, loop: asyncio.AbstractEventLoop) -> None:
        self._loop = loop
        self._thread: threading.Thread | None = None

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        return self._loop

    @property
    def running(self) -> bool:
        return self._thread is not None and self._thread.is_alive()

    @property
    def on_loop_thread(self) -> bool:
        return self._thread is not None and threading.current_thread() is self._thread

    def start(self) -> None:
        if self.running:
            return
        loop = self._loop

        def worker() -> None:
            asyncio.set_event_loop(loop)
            loop.run_forever()

        self._thread = threading.Thread(target=worker, daemon=True)
        self._thread.start()

    def stop(self, close: bool = False, timeout: float = 2.0) -> None:
        thread = self._thread
        self._thread = None
        if thread is not None and thread.is_alive():
            try:
                self._loop.call_soon_threadsafe(self._loop.stop)
            except RuntimeError:
                pass
            if threading.current_thread() is not thread:
                thread.join(timeout=timeout)
        if close and not self._loop.is_closed():
            try:
                self._loop.close()
            except Exception:
                pass


# --- Data-type NodeIds from ns0 namespace hierarchy -------------------------

_ns0 = o6.ns.ns0
_dt = _ns0.datatypes.BaseDataType
_num = _dt.Number
_int = _num.Integer
_uint = _num.UInteger

NS0_DT_BOOLEAN = o6.NodeId(_dt.Boolean)
NS0_DT_SBYTE = o6.NodeId(_int.SByte)
NS0_DT_BYTE = o6.NodeId(_uint.Byte)
NS0_DT_INT16 = o6.NodeId(_int.Int16)
NS0_DT_UINT16 = o6.NodeId(_uint.UInt16)
NS0_DT_INT32 = o6.NodeId(_int.Int32)
NS0_DT_UINT32 = o6.NodeId(_uint.UInt32)
NS0_DT_INT64 = o6.NodeId(_int.Int64)
NS0_DT_UINT64 = o6.NodeId(_uint.UInt64)
NS0_DT_FLOAT = o6.NodeId(_num.Float)
NS0_DT_DOUBLE = o6.NodeId(_num.Double)
NS0_DT_STRING = o6.NodeId(_dt.String)
NS0_DT_BASE_DATA_TYPE = o6.NodeId(_dt)

# --- Python → OPC UA data-type mapping ---------------------------------------

_PYTHON_TYPE_MAP = {
    bool: (NS0_DT_BOOLEAN, -1),
    int: (NS0_DT_INT32, -1),
    float: (NS0_DT_DOUBLE, -1),
    str: (NS0_DT_STRING, -1),
}


def _infer_data_type(value: Any) -> Tuple[o6.NodeId, int]:
    if isinstance(value, bool):
        return _PYTHON_TYPE_MAP[bool]
    if isinstance(value, int):
        return _PYTHON_TYPE_MAP[int]
    if isinstance(value, float):
        return _PYTHON_TYPE_MAP[float]
    if isinstance(value, str):
        return _PYTHON_TYPE_MAP[str]
    if isinstance(value, list):
        if value:
            elem_dt, _ = _infer_data_type(value[0])
            return elem_dt, 1  # 1D array
        return NS0_DT_INT32, 1  # Fallback: Int32 array
    # Try numpy
    try:
        import numpy as np

        if isinstance(value, np.ndarray):
            dtype_map = {
                np.dtype("bool"): NS0_DT_BOOLEAN,
                np.dtype("int8"): NS0_DT_SBYTE,
                np.dtype("uint8"): NS0_DT_BYTE,
                np.dtype("int16"): NS0_DT_INT16,
                np.dtype("uint16"): NS0_DT_UINT16,
                np.dtype("int32"): NS0_DT_INT32,
                np.dtype("uint32"): NS0_DT_UINT32,
                np.dtype("int64"): NS0_DT_INT64,
                np.dtype("uint64"): NS0_DT_UINT64,
                np.dtype("float32"): NS0_DT_FLOAT,
                np.dtype("float64"): NS0_DT_DOUBLE,
            }
            dt = dtype_map.get(value.dtype, NS0_DT_INT32)
            return dt, len(value.shape)  # dimensionality
    except ImportError:
        pass
    # Fallback
    return NS0_DT_BASE_DATA_TYPE, -1
