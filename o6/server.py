# Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner)

from typing import Union, Optional, Any, List, Callable, Tuple, TypeVar, Awaitable, cast
from types import TracebackType
from pathlib import Path
import asyncio
import builtins
import concurrent.futures
import inspect
import logging
import threading

import o6
import o6.namespaces
from . import _o6
from o6.nodeapi import (
    ServerBackend,
    Node,
    ObjectNode,
    VariableNode,
    MethodNode,
    ObjectTypeNode,
    VariableTypeNode,
    _str2attributeid,
)

if not hasattr(_o6, "Server"):
    raise ImportError(
        "Server support is not available. "
        "The o6 package was built without server support."
    )

from o6 import HasNodeId, NodeIdLike, LocalizedTextLike, MaybeAwaitable
from o6.utils import _infer_data_type, NS0_DT_INT32, NS0_DT_DOUBLE, _WorkerLoop
from o6.crypto import _load_cert_or_bytes, _load_cert_list

# --- Well-known NodeIds (namespace 0) ----------------------------------------

_ns0 = o6.ns.ns0
_rt = _ns0.reftypes.References
_HR = _rt.HierarchicalReferences
_AGG = _HR.HasChild.Aggregates

OBJECTS_FOLDER = _ns0.objects.Root.Objects()
TYPES_FOLDER = _ns0.objects.Root.Types()
VIEWS_FOLDER = _ns0.objects.Root.Views()
SERVER_NODE = _ns0.objects.Root.Objects.Server()

BASE_OBJECT_TYPE = _ns0.objtypes.BaseObjectType()
BASE_VARIABLE_TYPE = _ns0.vartypes.BaseVariableType()
BASE_DATA_VARIABLE_TYPE = _ns0.vartypes.BaseVariableType.BaseDataVariableType()

ORGANIZES = _HR.Organizes()
HAS_COMPONENT = _AGG.HasComponent()
HAS_PROPERTY = _AGG.HasProperty()
HAS_TYPE_DEFINITION = _rt.NonHierarchicalReferences.HasTypeDefinition()
HAS_SUBTYPE = _HR.HasChild.HasSubtype()

# =============================================================================
# Server – high-level OPC UA server
# =============================================================================


class Server(_o6.Server):

    def __init__(
        self,
        port: int = 4840,
        logger: Optional[logging.Logger] = None,
        loop: Optional[asyncio.AbstractEventLoop] = None,
        *,
        certificate: Union[str, Path, bytes, None] = None,
        private_key: Union[str, Path, bytes, None] = None,
        trust_list: Optional[List[Union[str, Path, bytes]]] = None,
        issuer_list: Optional[List[Union[str, Path, bytes]]] = None,
        revocation_list: Optional[List[Union[str, Path, bytes]]] = None,
        secure_only: bool = False,
        accept_all_certificates: bool = False,
        application_uri: Optional[str] = None,
    ) -> None:
        if loop is not None:
            self._loop: asyncio.AbstractEventLoop = loop
            self._owns_loop = False
        else:
            try:
                self._loop = asyncio.get_running_loop()
                self._owns_loop = False
            except RuntimeError:
                self._loop = asyncio.new_event_loop()
                self._owns_loop = True

        if logger is None:
            logger = logging.getLogger(__name__)

        kwargs: dict = {"port": port, "loop": self._loop, "logger": logger}
        super().__init__(**kwargs)

        if application_uri is not None:
            self.config.application_uri = application_uri

        # Apply encryption if certificate and key are provided
        cert_bytes = _load_cert_or_bytes(certificate)
        key_bytes = _load_cert_or_bytes(private_key)
        if cert_bytes and key_bytes:
            tl = _load_cert_list(trust_list)
            il = _load_cert_list(issuer_list)
            rl = _load_cert_list(revocation_list)
            self.config.set_encryption(
                cert_bytes,
                key_bytes,
                port,
                tl,
                il,
                rl,
                secure_only,
            )

        if accept_all_certificates:
            self.config.set_accept_all_certificates()

        self._worker: _WorkerLoop | None = None
        self.ns = o6.namespaces.Namespaces(self)

    # -- Thread-safe dispatch ------------------------------------------------

    def _maybe_async_coro(self, coro) -> MaybeAwaitable:
        """Dispatch a coroutine with the same threading semantics as
        ``_on_event_loop``, but accepting a coroutine instead of a callable.

        - No running loop + loop not started: runs inline via
          ``loop.run_until_complete``.
        - No running loop + server started (worker thread owns the loop):
          posts the coroutine via ``call_soon_threadsafe`` and blocks on a
          ``concurrent.futures.Future``.
        - Caller is on a *different* event loop: schedules with
          ``run_coroutine_threadsafe`` and returns an awaitable so the
          caller's loop is not blocked.
        """
        try:
            caller_loop = asyncio.get_running_loop()
        except RuntimeError:
            caller_loop = None

        if caller_loop is None:
            if self._loop.is_running():
                # Worker thread owns the loop — post from outside and block.
                fut: concurrent.futures.Future = concurrent.futures.Future()

                async def _run():
                    try:
                        fut.set_result(await coro)
                    except Exception as exc:
                        fut.set_exception(exc)

                self._loop.call_soon_threadsafe(lambda: self._loop.create_task(_run()))
                return fut.result()
            else:
                return self._loop.run_until_complete(coro)

        # Caller is on a different loop — return an awaitable.
        cfut = asyncio.run_coroutine_threadsafe(coro, self._loop)
        return asyncio.wrap_future(cfut)

    T = TypeVar("T")

    def _maybe_async(self, aw: Awaitable[T]) -> MaybeAwaitable[T]:
        """Dispatch an awaitable to the server's loop and either block
        (sync caller) or return an awaitable (async caller).

        Differs from :meth:`Client._maybe_async` in handling the
        pre-start case: a Server may be configured (variables added,
        attributes written, etc.) *before* :meth:`start` is called,
        so the loop is not yet running.  In that case we fall back to
        ``loop.run_until_complete`` rather than blocking on
        ``run_coroutine_threadsafe`` (which would deadlock).
        """
        if self._worker is not None and not self._worker.running:
            if asyncio.iscoroutine(aw):
                aw.close()
            raise RuntimeError("Server event loop is not running")

        try:
            loop = asyncio.get_running_loop()
            if loop == self._loop:
                return aw  # type: ignore[return-value]
        except RuntimeError:
            loop = None

        async def _await(f):
            return await f

        # Sync caller, but our loop is not running yet (pre-start configuration
        # phase).  Drive the awaitable to completion inline.
        if loop is None and not self._loop.is_running():
            if asyncio.iscoroutine(aw) or inspect.iscoroutine(aw):
                return self._loop.run_until_complete(aw)
            return self._loop.run_until_complete(_await(aw))

        try:
            if asyncio.iscoroutine(aw) or inspect.iscoroutine(aw):
                fut = asyncio.run_coroutine_threadsafe(aw, self._loop)
            else:
                fut = asyncio.run_coroutine_threadsafe(_await(aw), self._loop)
        except RuntimeError:
            if asyncio.iscoroutine(aw):
                aw.close()
            raise RuntimeError("Server event loop is not running")

        if (
            loop is None
            or asyncio.current_task() is None
            or hasattr(builtins, "__IPYTHON__")
        ):
            # Sync caller: no running loop, or running on a foreign loop as a
            # scheduled callback (not inside an async task).  Block until done.
            return fut.result()
        else:
            # Async task on a foreign loop — return an awaitable the caller can
            # ``await`` on their own loop.
            return asyncio.wrap_future(fut)

    def _wrap_future(
        self,
        fut: concurrent.futures.Future,
        caller_loop: asyncio.AbstractEventLoop,
    ) -> asyncio.Future:
        afut = asyncio.wrap_future(fut)
        afut._concurrent_future = fut  # type: ignore[attr-defined]
        original_result = cast(Callable[[float | None], Any], afut.result)

        def result(timeout: float | None = None) -> Any:
            if not afut.done():
                return fut.result(timeout)
            return original_result(timeout)

        afut.result = result  # type: ignore[assignment]
        return afut

    def _on_event_loop(self, fn: Callable[[], Any]) -> Any:
        # No worker thread yet, or already on it — call directly
        if (
            self._worker is None
            or not self._worker.running
            or self._worker.on_loop_thread
        ):
            out = fn()
            # Synchronous async-server calls resolve their future inline.
            # Unwrap to keep the public API sync-friendly.
            if asyncio.isfuture(out) and out.done():
                return out.result()
            return out

        # Detect whether the caller is itself inside an event loop
        try:
            caller_loop = asyncio.get_running_loop()
        except RuntimeError:
            caller_loop = None

        # Schedule fn() on the worker loop and collect the result via a
        # thread-safe concurrent.futures.Future
        fut: concurrent.futures.Future = concurrent.futures.Future()

        def _call() -> None:
            try:
                out = fn()
                if asyncio.isfuture(out) or inspect.isawaitable(out):
                    task = asyncio.ensure_future(out, loop=self._loop)

                    def _complete(task: asyncio.Future) -> None:
                        try:
                            fut.set_result(task.result())
                        except BaseException as exc:
                            fut.set_exception(exc)

                    task.add_done_callback(_complete)
                else:
                    fut.set_result(out)
            except BaseException as exc:
                fut.set_exception(exc)

        try:
            self._loop.call_soon_threadsafe(_call)
        except RuntimeError as exc:
            fut.set_exception(exc)

        # Sync caller (no running loop) or same loop — block until done
        if (
            caller_loop is None
            or caller_loop is self._loop
            or asyncio.current_task() is None
        ):
            return fut.result()

        # Async task on a different running loop — return an awaitable.
        return self._wrap_future(fut, caller_loop)

    # -- Well-known nodes (convenience properties) ---------------------------

    @property
    def objects_node(self) -> o6.NodeId:
        return OBJECTS_FOLDER

    @property
    def types_node(self) -> o6.NodeId:
        return TYPES_FOLDER

    @property
    def server_node(self) -> o6.NodeId:
        return SERVER_NODE

    # -- Lifecycle -----------------------------------------------------------

    def start(self) -> None:
        if self.running:
            return

        if self._loop.is_running():
            # Async context: the loop is already running, startup directly.
            self.run_startup()
        else:
            # Sync fallback: start the event loop in a background thread
            # first, then call run_startup from the loop thread so that
            # create_server() tasks execute immediately.
            self._worker = _WorkerLoop(self._loop)
            self._worker.start()
            import concurrent.futures

            fut: concurrent.futures.Future = concurrent.futures.Future()

            def _do_startup():
                try:
                    self.run_startup()
                    fut.set_result(None)
                except Exception as e:
                    fut.set_exception(e)

            self._loop.call_soon_threadsafe(_do_startup)
            fut.result(timeout=5.0)

    def stop(self) -> None:
        if not self.running:
            return
        if self._worker is not None and self._worker.running:
            # Sync fallback: run_shutdown from the loop thread, then
            # keep the loop alive until the server reaches STOPPED so
            # that asyncio transport close events (connection_lost) and
            # subscription timers can complete the teardown.
            import concurrent.futures

            fut: concurrent.futures.Future = concurrent.futures.Future()

            async def _shutdown_and_drain():
                try:
                    self.run_shutdown()
                    # Give asyncio a few cycles so transport close events
                    # (connection_lost) and pending timer callbacks can fire
                    # before we tear down the event loop.
                    for i in range(10):  # up to ~0.5 s
                        if self._is_fully_stopped:
                            break
                        await asyncio.sleep(0.05)
                    # A couple of extra iterations so asyncio fully processes
                    # the pending transport.close() / server.close() calls
                    # that the C event source stop scheduled.  The selector
                    # may need more than one pass to unregister the listening
                    # socket, so a single sleep(0) is not always sufficient.
                    for _ in range(10):
                        await asyncio.sleep(0)
                    # Stop the C event loop while asyncio is still live so
                    # that listener/connection cleanup can safely use Python
                    # APIs.  Without this, pyServer_clear (tp_dealloc) would
                    # call el->stop during GC, where PyObject_CallMethod on
                    # transport.close() can segfault.
                    self._stop_event_loop()
                    fut.set_result(None)
                except Exception as e:
                    fut.set_exception(e)

            self._loop.call_soon_threadsafe(
                lambda: self._loop.create_task(_shutdown_and_drain())
            )
            fut.result(timeout=10.0)

            # Stop the worker thread but keep the asyncio loop alive so
            # subsequent sync configuration / calls can still drive it via
            # ``run_until_complete``.  The loop is closed in ``__del__``.
            self._worker.stop(close=False)
            self._worker = None
        else:
            self.run_shutdown()
            self._stop_event_loop()

    def __enter__(self) -> "Server":
        self.start()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.stop()

    async def __aenter__(self) -> "Server":
        self.start()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.stop()

    def __del__(self):
        try:
            if self.running:
                self.stop()
        except Exception:
            pass
        try:
            self._cleanup()
        except Exception:
            pass
        try:
            if self._owns_loop and not self._loop.is_closed():
                self._loop.close()
        except Exception:
            pass

    # -- Reverse connect ------------------------------------------------------

    def add_reverse_connect(
        self,
        url: str,
        callback: Callable[[int, int], None] | None = None,
    ) -> int:
        return self._on_event_loop(
            lambda: super(Server, self).add_reverse_connect(url, callback)
        )

    def remove_reverse_connect(self, handle: int) -> None:
        self._on_event_loop(lambda: super(Server, self).remove_reverse_connect(handle))

    # -- Add nodes (high-level) -----------------------------------------------

    def add_variable(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike,
        value: Any = None,
        *,
        nodeid: NodeIdLike | None = None,
        data_type: NodeIdLike | None = None,
        writable: bool = True,
        historizing: bool = False,
        ns: int = 1,
    ) -> VariableNode:
        parent_id = o6.NodeId(parent)
        requested_id = o6.NodeId(nodeid)

        # Infer data type
        if data_type is not None:
            dt_id = o6.NodeId(data_type)
            # Still derive value_rank from the value so arrays work correctly
            # when data_type is given explicitly.
            if value is not None:
                _, value_rank = _infer_data_type(value)
            else:
                value_rank = -1
        elif value is not None:
            dt_id, value_rank = _infer_data_type(value)
        else:
            dt_id = NS0_DT_INT32
            value_rank = -1

        # Build attributes
        attr = o6.VariableAttributes()
        attr.display_name = o6.LocalizedText(name)
        attr.data_type = dt_id
        attr.value_rank = value_rank
        if value_rank >= 1:
            # OPC UA spec requires array_dimensions to have exactly value_rank
            # elements. Use 0 for each dimension to mean "any length".
            attr.array_dimensions = [0] * value_rank

        access = 0
        if writable:
            access = 3  # Read | Write
        else:
            access = 1  # Read only
        if historizing:
            access |= 4 | 8  # HistoryRead | HistoryWrite
            attr.historizing = True
        attr.access_level = access
        attr.user_access_level = access

        if value is not None:
            # numpy arrays must not be embedded in VariableAttributes.value —
            # open62541 rejects array variants during add_variable_node type-check.
            # Scalars are safe to embed; arrays are written via write_value below.
            try:
                import numpy as _np

                _is_array = isinstance(value, _np.ndarray)
            except ImportError:
                _is_array = False
            if not _is_array:
                attr.value = o6.Double(value) if isinstance(value, float) else value

        browse_name = o6.QualifiedName(f"{ns}:{name}")
        type_def = BASE_DATA_VARIABLE_TYPE

        out_id = self._on_event_loop(
            lambda: self.add_variable_node(
                requested_id, parent_id, ORGANIZES, browse_name, type_def, attr
            )
        )

        # Write the value separately if provided – ensures variant wrapper is correct
        if value is not None:
            v = o6.Double(value) if isinstance(value, float) else value
            self._on_event_loop(lambda: super(Server, self).write_value(out_id, v))

        return VariableNode(ServerBackend(self), out_id, browse_name)

    def add_object(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike,
        *,
        nodeid: NodeIdLike | None = None,
        type_definition: NodeIdLike = BASE_OBJECT_TYPE,
        ns: int = 1,
    ) -> ObjectNode:
        parent_id = o6.NodeId(parent)
        requested_id = o6.NodeId(nodeid)
        type_def = o6.NodeId(type_definition)

        attr = o6.ObjectAttributes()
        attr.display_name = o6.LocalizedText(name)

        browse_name = o6.QualifiedName(f"{ns}:{name}")

        out_id = self._on_event_loop(
            lambda: self.add_object_node(
                requested_id, parent_id, ORGANIZES, browse_name, type_def, attr
            )
        )
        return ObjectNode(ServerBackend(self), out_id, browse_name)

    def add_object_type(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike = BASE_OBJECT_TYPE,
        *,
        nodeid: NodeIdLike | None = None,
        ns: int = 1,
    ) -> ObjectTypeNode:
        parent_id = o6.NodeId(parent)
        requested_id = o6.NodeId(nodeid)

        attr = o6.ObjectTypeAttributes()
        attr.display_name = o6.LocalizedText(name)

        browse_name = o6.QualifiedName(f"{ns}:{name}")

        out_id = self._on_event_loop(
            lambda: self.add_object_type_node(
                requested_id, parent_id, HAS_SUBTYPE, browse_name, attr
            )
        )
        return ObjectTypeNode(ServerBackend(self), out_id, browse_name)

    def add_variable_type(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike = BASE_VARIABLE_TYPE,
        *,
        data_type: NodeIdLike = NS0_DT_DOUBLE,
        value_rank: int = -1,
        nodeid: NodeIdLike | None = None,
        ns: int = 1,
    ) -> VariableTypeNode:
        parent_id = o6.NodeId(parent)
        requested_id = o6.NodeId(nodeid)
        dt_id = o6.NodeId(data_type)

        attr = o6.VariableTypeAttributes()
        attr.display_name = o6.LocalizedText(name)
        attr.data_type = dt_id
        attr.value_rank = value_rank

        browse_name = o6.QualifiedName(f"{ns}:{name}")

        out_id = self._on_event_loop(
            lambda: self.add_variable_type_node(
                requested_id, parent_id, HAS_SUBTYPE, browse_name, dt_id, attr
            )
        )
        return VariableTypeNode(ServerBackend(self), out_id, browse_name)

    def add_method(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike,
        callback: Callable,
        *,
        input_args: Optional[List[o6.Argument]] = None,
        output_args: Optional[List[o6.Argument]] = None,
        nodeid: o6.NodeId | None = None,
        ns: int = 1,
    ) -> MethodNode:
        parent_id = o6.NodeId(parent)
        requested_id = o6.NodeId(nodeid)

        attr = o6.MethodAttributes()
        attr.display_name = o6.LocalizedText(name)
        attr.executable = True
        attr.user_executable = True

        browse_name = o6.QualifiedName(f"{ns}:{name}")

        out_id = self._on_event_loop(
            lambda: self.add_method_node(
                requested_id,
                parent_id,
                HAS_COMPONENT,
                browse_name,
                attr,
                callback,
                input_args if input_args is not None else [],
                output_args if output_args is not None else [],
            )
        )
        node = MethodNode(ServerBackend(self), out_id, browse_name)
        node._default_object = parent_id
        return node

    # -- References / deletion ------------------------------------------------

    def add_reference(  # type: ignore[override]
        self,
        source: NodeIdLike,
        target: NodeIdLike,
        reference_type: NodeIdLike,
        *,
        forward: bool = True,
    ) -> None:
        src_id = o6.NodeId(source)
        tgt_id = o6.NodeId(target)
        ref_id = o6.NodeId(reference_type)
        self._on_event_loop(
            lambda: super(Server, self).add_reference(src_id, ref_id, tgt_id, forward)
        )

    def delete_node(  # type: ignore[override]
        self,
        nodeid: NodeIdLike,
        *,
        delete_references: bool = True,
    ) -> None:
        nid = o6.NodeId(nodeid)
        self._on_event_loop(
            lambda: super(Server, self).delete_node(nid, delete_references)
        )

    # -- Method call ----------------------------------------------------------

    def call(  # type: ignore[override]
        self,
        object_id: NodeIdLike,
        method_id: NodeIdLike,
        input_args: list[Any] = [],
    ) -> MaybeAwaitable[tuple]:
        obj_id = o6.NodeId(object_id)
        mth_id = o6.NodeId(method_id)
        args = list(input_args) if input_args else []

        async def _do() -> tuple:
            return await super(Server, self).call(obj_id, mth_id, args)

        return self._maybe_async(_do())

    # -- Read / write ---------------------------------------------------------

    def _sync_result(self, result: Any) -> Any:
        if asyncio.isfuture(result):
            if hasattr(result, "_concurrent_future"):
                return result._concurrent_future.result()  # type: ignore[attr-defined]
            return result.result()
        return result

    def read(
        self,
        target: NodeIdLike | list[NodeIdLike],
        attr: o6.AttributeId | str = o6.AttributeId.VALUE,
    ) -> MaybeAwaitable[Any]:
        if isinstance(attr, str):
            attr = _str2attributeid(attr)

        if isinstance(target, list):

            async def _do_list() -> list:
                results = []
                for item in target:
                    nid = o6.NodeId(item)
                    if attr == o6.AttributeId.VALUE:
                        results.append(await super(Server, self).read_value(nid))
                    else:
                        results.append(
                            await super(Server, self).read_attribute(nid, int(attr))
                        )
                return results

            return self._maybe_async(_do_list())

        nid = o6.NodeId(target)
        attr_id = int(attr)

        async def _do() -> Any:
            if attr == o6.AttributeId.VALUE:
                return await super(Server, self).read_value(nid)
            return await super(Server, self).read_attribute(nid, attr_id)

        return self._maybe_async(_do())

    def write(
        self,
        target: NodeIdLike | list[NodeIdLike],
        value: Any,
        attr: o6.AttributeId | str = o6.AttributeId.VALUE,
    ) -> MaybeAwaitable[None]:
        if isinstance(attr, str):
            attr = _str2attributeid(attr)

        if isinstance(target, list):

            async def _do_list() -> None:
                for item in target:
                    nid = o6.NodeId(item)
                    if isinstance(value, o6.DataValue):
                        await super(Server, self).write_data_value(nid, value)
                    elif attr == o6.AttributeId.VALUE:
                        v = o6.Double(value) if isinstance(value, float) else value
                        await super(Server, self).write_value(nid, v)
                    else:
                        await super(Server, self).write_attribute(nid, int(attr), value)

            return self._maybe_async(_do_list())

        nid = o6.NodeId(target)
        attr_id = int(attr)

        async def _do() -> None:
            if isinstance(value, o6.DataValue):
                await super(Server, self).write_data_value(nid, value)
                return
            if attr == o6.AttributeId.VALUE:
                v = o6.Double(value) if isinstance(value, float) else value
                await super(Server, self).write_value(nid, v)
                return
            await super(Server, self).write_attribute(nid, attr_id, value)

        return self._maybe_async(_do())

    def browse_node(  # type: ignore[override]
        self,
        nodeid: NodeIdLike,
        result_mask: int,
    ) -> list:
        nid = o6.NodeId(nodeid)
        return self._sync_result(
            self._on_event_loop(
                lambda: super(Server, self).browse_node(nid, result_mask)
            )
        )

    def translate_browse_paths(  # type: ignore[override]
        self,
        request: Any,
    ) -> Any:
        return self._sync_result(
            self._on_event_loop(
                lambda: super(Server, self).translate_browse_paths(request)
            )
        )

    def read_node_info(  # type: ignore[override]
        self,
        nodeid: NodeIdLike,
    ) -> tuple:
        nid = o6.NodeId(nodeid)
        return self._sync_result(
            self._on_event_loop(lambda: super(Server, self).read_node_info(nid))
        )

    def find_data_type(  # type: ignore[override]
        self,
        nodeid: NodeIdLike,
    ) -> Any:
        nid = o6.NodeId(nodeid)
        return self._sync_result(
            self._on_event_loop(lambda: super(Server, self).find_data_type(nid))
        )


# -- Helper: build Argument objects easily ------------------------------------


def make_argument(
    name: str,
    data_type: NodeIdLike,
    *,
    value_rank: int = -1,
    description: LocalizedTextLike = "",
) -> o6.Argument:
    arg = o6.Argument()
    arg.name = name
    arg.data_type = o6.NodeId(data_type)
    arg.value_rank = value_rank
    arg.description = o6.LocalizedText(description)
    return arg


__all__ = [
    "Server",
    "Node",
    "make_argument",
    "OBJECTS_FOLDER",
    "TYPES_FOLDER",
    "BASE_OBJECT_TYPE",
    "BASE_VARIABLE_TYPE",
    "BASE_DATA_VARIABLE_TYPE",
    "ORGANIZES",
    "HAS_COMPONENT",
    "HAS_PROPERTY",
    "HAS_TYPE_DEFINITION",
    "HAS_SUBTYPE",
]
