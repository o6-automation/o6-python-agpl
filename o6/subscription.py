# Copyright 2026 (c) o6 Automation GmbH
"""Client subscriptions and monitored items."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, Generator, TypeAlias
import copy
import inspect
import logging
from o6.ns import ns0
import weakref
import o6
from o6 import MaybeAwaitable, NodeIdLike
from o6.util import _index_range_to_string

if TYPE_CHECKING:
    from .client import Client
    from .server import Server


_logger = logging.getLogger(__name__)


class MonitoredItem:
    """One monitored item inside a [`Subscription`][o6.subscription.Subscription].

    Created by `Client.monitor(...)`, or by
    `Server.createDataChangeMonitoredItem(...)` and its event counterparts for a
    server-local item, rather than directly. An item is falsy once deleted, and
    every operation on a deleted item raises `RuntimeError`.

    Awaiting the item resolves it, which is what lets `await client.monitor(...)`
    return an item whose `id` the server has already assigned.

    See [Managing monitored items](../manual/client/subscriptions.md#managing-monitored-items).
    """

    DataChangeCallback: TypeAlias = Callable[[Any], None] | Callable[["MonitoredItem", Any], None]
    EventCallback: TypeAlias = Callable[[dict], None] | Callable[["MonitoredItem", dict], None]
    CreatedCallback: TypeAlias = Callable[
        ["MonitoredItem", ns0.datatypes.MonitoredItemCreateResult], None
    ]
    DeletedCallback: TypeAlias = Callable[["MonitoredItem", int, int], None]

    def __init__(
        self,
        subscription: Subscription | None = None,
        *,
        server: Server | None = None,
        monitoredItemId: int | None = None,
    ) -> None:
        """Create an item handle. Use `Client.monitor` or the server's
        `createDataChangeMonitoredItem` family instead.

        Args:
            subscription: The client subscription this item belongs to.
            server: The server that owns the item, for a server-side item.
            monitoredItemId: An existing server-assigned item id to wrap.
        """
        self._subscription_ref: weakref.ref[Subscription] | None = (
            weakref.ref(subscription) if subscription is not None else None
        )
        self._monitored_item_id: int | None = None
        self._pending_init: Any | None = None
        self._sampling_interval: float = 0.0
        self._queue_size: int = 0
        self._item_to_monitor = ns0.datatypes.ReadValueId()
        self._monitoring_params = ns0.datatypes.MonitoringParameters()
        self._monitoring_mode: ns0.datatypes.MonitoringMode = ns0.datatypes.MonitoringMode.REPORTING
        self._value_only: bool = True
        self._server_ref: weakref.ref[Server] | None = (
            weakref.ref(server) if server is not None else None
        )
        if monitoredItemId is not None:
            self._monitored_item_id = int(monitoredItemId)

    @classmethod
    def _from_server(cls, server: Server, monitored_item_id: int) -> MonitoredItem:
        return cls(None, server=server, monitoredItemId=int(monitored_item_id))

    @classmethod
    def _data_change(
        cls,
        subscription: Subscription,
        nodeid: NodeIdLike | ns0.datatypes.ReadValueId,
        callback: MonitoredItem.DataChangeCallback,
        attribute_id: o6.AttributeId = o6.AttributeId.VALUE,
        index_range: o6.IndexRange = "",
        data_encoding: Any = "",
        sampling_interval: float = 250.0,
        value_only: bool = True,
        on_created: MonitoredItem.CreatedCallback | None = None,
        on_deleted: MonitoredItem.DeletedCallback | None = None,
        *,
        filter: ns0.datatypes.DataChangeFilter | None = None,
        monitoring_mode: ns0.datatypes.MonitoringMode = ns0.datatypes.MonitoringMode.REPORTING,
        queue_size: int = 1,
        discard_oldest: bool = True,
    ) -> MonitoredItem:
        for _cb, _name in ((on_created, "on_created"), (on_deleted, "on_deleted")):
            if _cb is not None and not callable(_cb):
                raise TypeError(f"{_name} must be callable or None")
        item = cls(subscription)
        if isinstance(nodeid, ns0.datatypes.ReadValueId):
            item._item_to_monitor = copy.copy(nodeid)
        else:
            item._item_to_monitor.nodeId = o6.NodeId(nodeid)
            item._item_to_monitor.attributeId = attribute_id
            item._item_to_monitor.indexRange = _index_range_to_string(index_range) or ""
            item._item_to_monitor.dataEncoding = (
                o6.QualifiedName(data_encoding) if isinstance(data_encoding, str) else data_encoding
            )
        item._monitoring_params.samplingInterval = sampling_interval
        item._monitoring_params.queueSize = queue_size
        item._monitoring_params.discardOldest = discard_oldest
        if filter is not None:
            item._monitoring_params.filter = filter
        item._monitoring_mode = monitoring_mode
        item._value_only = value_only

        async def _create() -> None:
            assert subscription.id is not None  # subscription awaited before use
            create_request = ns0.datatypes.CreateMonitoredItemsRequest()
            create_request.subscriptionId = subscription.id
            create_request.timestampsToReturn = ns0.datatypes.TimestampsToReturn.BOTH

            monitored_item_request = ns0.datatypes.MonitoredItemCreateRequest()
            monitored_item_request.itemToMonitor = copy.copy(item._item_to_monitor)
            monitored_item_request.monitoringMode = monitoring_mode
            monitored_item_request.requestedParameters = copy.copy(item._monitoring_params)

            create_request.itemsToCreate = [monitored_item_request]

            # Count only *required* positional parameters (no default value).
            _sig = inspect.signature(callback)
            _POSITIONAL = (
                inspect.Parameter.POSITIONAL_OR_KEYWORD,
                inspect.Parameter.POSITIONAL_ONLY,
            )
            n_required = sum(
                1
                for p in _sig.parameters.values()
                if p.kind in _POSITIONAL and p.default is inspect.Parameter.empty
            )

            if n_required <= 1:
                if not item._value_only:

                    def wrapper(data_value):
                        callback(data_value)

                else:

                    def wrapper(data_value):
                        callback(data_value.value)

            else:
                if not item._value_only:

                    def wrapper(data_value):
                        callback(item, data_value)

                else:

                    def wrapper(data_value):
                        callback(item, data_value.value)

            client_logger = subscription._client._logger

            def c_created(response_obj):
                results = response_obj.results
                if not results:
                    return
                try:
                    on_created(item, results[0])  # type: ignore[misc]
                except Exception:
                    client_logger.exception("Error in MonitoredItem on_created callback")

            def c_deleted(sub_id, mon_id):
                try:
                    on_deleted(item, sub_id, mon_id)  # type: ignore[misc]
                except Exception:
                    client_logger.exception("Error in MonitoredItem on_deleted callback")

            response = await subscription._client._service_createMonitoredItems_datachange(
                create_request,
                wrapper,
                c_created if on_created is not None else None,
                c_deleted if on_deleted is not None else None,
            )
            response.responseHeader.serviceResult.check(message="Monitored item creation")

            if len(response.results) != 1:
                raise Exception("Wrong results returned from monitored item creation")

            result = response.results[0]
            result.statusCode.check(message="Monitored item result")
            item._monitored_item_id = result.monitoredItemId
            item._sampling_interval = result.revisedSamplingInterval
            item._queue_size = result.revisedQueueSize

        item._pending_init = subscription._client._maybe_async(_create())
        return item

    @classmethod
    def _event(
        cls,
        subscription: Subscription,
        nodeid: NodeIdLike,
        callback: MonitoredItem.EventCallback,
        on_created: MonitoredItem.CreatedCallback | None = None,
        on_deleted: MonitoredItem.DeletedCallback | None = None,
        *,
        filter: ns0.datatypes.EventFilter | str | None = None,
        monitoring_mode: ns0.datatypes.MonitoringMode = ns0.datatypes.MonitoringMode.REPORTING,
        queue_size: int = 100,
        discard_oldest: bool = True,
    ) -> MonitoredItem:
        for _cb, _name in ((on_created, "on_created"), (on_deleted, "on_deleted")):
            if _cb is not None and not callable(_cb):
                raise TypeError(f"{_name} must be callable or None")
        item = cls(subscription)
        item._item_to_monitor = ns0.datatypes.ReadValueId()
        item._item_to_monitor.nodeId = o6.NodeId(nodeid)
        item._item_to_monitor.attributeId = o6.AttributeId.EVENT_NOTIFIER

        async def _create() -> None:
            assert subscription.id is not None  # subscription awaited before use
            create_request = ns0.datatypes.CreateMonitoredItemsRequest()
            create_request.subscriptionId = subscription.id
            create_request.timestampsToReturn = ns0.datatypes.TimestampsToReturn.BOTH

            monitored_item_request = ns0.datatypes.MonitoredItemCreateRequest()
            monitored_item_request.itemToMonitor = copy.copy(item._item_to_monitor)
            monitored_item_request.monitoringMode = monitoring_mode

            monitoring_params = ns0.datatypes.MonitoringParameters()
            monitoring_params.clientHandle = 0  # Will be overwritten by server anyway
            monitoring_params.samplingInterval = 0.0
            monitoring_params.queueSize = queue_size
            monitoring_params.discardOldest = discard_oldest
            if isinstance(filter, str):
                ef = ns0.datatypes.EventFilter.parse(filter, logger=subscription._client._logger)
            elif filter is None:
                ef = ns0.datatypes.EventFilter.parse(
                    "SELECT /EventId, /EventType, /SourceName, /Time, /Message, /Severity"
                )
            else:
                ef = filter
            monitoring_params.filter = ef
            monitored_item_request.requestedParameters = monitoring_params

            create_request.itemsToCreate = [monitored_item_request]

            n_params = len(inspect.signature(callback).parameters)
            if n_params == 1:

                def wrapper(event_fields):
                    callback(event_fields)

            else:

                def wrapper(event_fields):
                    callback(item, event_fields)

            client_logger = subscription._client._logger

            def c_created(response_obj):
                results = response_obj.results
                if not results:
                    return
                try:
                    on_created(item, results[0])  # type: ignore[misc]
                except Exception:
                    client_logger.exception("Error in MonitoredItem on_created callback")

            def c_deleted(sub_id, mon_id):
                try:
                    on_deleted(item, sub_id, mon_id)  # type: ignore[misc]
                except Exception:
                    client_logger.exception("Error in MonitoredItem on_deleted callback")

            response = await subscription._client._service_createMonitoredItems_event(
                create_request,
                wrapper,
                c_created if on_created is not None else None,
                c_deleted if on_deleted is not None else None,
            )
            response.responseHeader.serviceResult.check(message="Event monitored item creation")

            if len(response.results) != 1:
                raise Exception("Wrong results returned from event monitored item creation")

            result = response.results[0]
            result.statusCode.check(message="Event monitored item result")
            item._monitored_item_id = result.monitoredItemId
            item._monitoring_params.samplingInterval = result.revisedSamplingInterval
            item._monitoring_params.queueSize = result.revisedQueueSize

        item._pending_init = subscription._client._maybe_async(_create())
        return item

    def __await__(self) -> Generator[Any, None, MonitoredItem]:
        """Wait for the server to create this item, then return it."""

        async def _init() -> MonitoredItem:
            if self._pending_init is not None:
                await self._pending_init
                self._pending_init = None
            return self

        return _init().__await__()

    def __bool__(self) -> bool:
        """False once the item has been deleted, or before it is created."""
        return self._monitored_item_id is not None

    def _check_valid(self, op: str) -> None:
        if not self:
            raise RuntimeError(
                f"Cannot call {op!r} on an uninitialized or already-deleted MonitoredItem"
            )

    def delete(self) -> MaybeAwaitable[None]:
        """Delete this monitored item on the server.

        Deleting an item that is already gone logs a warning instead of raising,
        so cleanup paths can run unconditionally.

        Raises:
            RuntimeError: The owning client or server has been garbage-collected.
            StatusCodeError: The DeleteMonitoredItems service call failed.
        """

        async def _delete() -> None:
            if self._server_ref is not None:
                server = self._server_ref()
                if server is None:
                    raise RuntimeError("Server has been garbage-collected")

                if self._monitored_item_id is None:
                    _logger.warning(
                        "MonitoredItem.delete() called on an uninitialized or already-deleted monitored item"
                    )
                    return

                monitored_item_id = self._monitored_item_id
                self._monitored_item_id = None
                result = server.deleteMonitoredItem(monitored_item_id)
                if inspect.isawaitable(result):
                    await result
                return

            if self._monitored_item_id is None:
                self._subscription._client._logger.warning(
                    "MonitoredItem.delete() called on an uninitialized or already-deleted monitored item"
                )
                return

            monitored_item_id = self._monitored_item_id
            self._monitored_item_id = None

            delete_request = ns0.datatypes.DeleteMonitoredItemsRequest()
            assert self._subscription.id is not None  # subscription must be valid
            delete_request.subscriptionId = self._subscription.id
            delete_request.monitoredItemIds = [monitored_item_id]

            response = await self._subscription._client._service_deleteMonitoredItems(
                delete_request
            )
            response.responseHeader.serviceResult.check(message="Monitored item deletion")

            if monitored_item_id in self._subscription._monitored_items:
                del self._subscription._monitored_items[monitored_item_id]

        if self._server_ref is not None:
            server = self._server_ref()
            if server is None:
                raise RuntimeError("Server has been garbage-collected")
            return server._maybe_async(_delete())
        return self._subscription._client._maybe_async(_delete())

    def modify(
        self,
        samplingInterval: float | None = None,
        queueSize: int | None = None,
        discardOldest: bool | None = None,
        filter: ns0.datatypes.DataChangeFilter | ns0.datatypes.EventFilter | str | None = None,
    ) -> MaybeAwaitable[None]:
        """Change this item's sampling parameters on the server.

        Omitted arguments keep their current value. The server may revise the
        sampling interval and queue size, and the revised values are stored back,
        so [`params`][o6.subscription.MonitoredItem.params] reports what was
        actually granted.

        Args:
            samplingInterval: Requested sampling interval in milliseconds.
            queueSize: Requested notification queue depth.
            discardOldest: Drop the oldest queued notification when the queue is
                full, rather than the newest.
            filter: A `DataChangeFilter` for a data-change item, an `EventFilter`
                for an event item, or a filter query string, which is only valid
                for event items.

        Raises:
            TypeError: The filter kind does not match the item kind, or a string
                filter was passed for a data-change item.
            RuntimeError: The item has been deleted.
            StatusCodeError: The ModifyMonitoredItems service call failed.
        """

        async def _modify() -> None:
            self._check_valid("modify")
            assert self._subscription.id is not None  # _check_valid ensures non-None
            assert self._monitored_item_id is not None  # _check_valid ensures non-None

            resolved_filter: ns0.datatypes.DataChangeFilter | ns0.datatypes.EventFilter | None
            if isinstance(filter, str):
                is_event = self._item_to_monitor.attributeId == o6.AttributeId.EVENT_NOTIFIER
                if not is_event:
                    raise TypeError(
                        "String filter queries are only supported for EventFilter "
                        "(event monitored items). Use DataChangeFilter() for data-change items."
                    )
                resolved_filter = ns0.datatypes.EventFilter.parse(
                    filter, logger=self._subscription._client._logger
                )
            else:
                resolved_filter = filter

            if resolved_filter is not None:
                is_event = self._item_to_monitor.attributeId == o6.AttributeId.EVENT_NOTIFIER
                if is_event and isinstance(resolved_filter, ns0.datatypes.DataChangeFilter):
                    raise TypeError(
                        "Cannot set a DataChangeFilter on an event MonitoredItem, use EventFilter instead"
                    )
                if not is_event and isinstance(resolved_filter, ns0.datatypes.EventFilter):
                    raise TypeError(
                        "Cannot set an EventFilter on a data-change MonitoredItem, use DataChangeFilter instead"
                    )

            modify_request = ns0.datatypes.ModifyMonitoredItemsRequest()
            modify_request.subscriptionId = self._subscription.id
            modify_request.timestampsToReturn = ns0.datatypes.TimestampsToReturn.BOTH

            item_modify = ns0.datatypes.MonitoredItemModifyRequest()
            item_modify.monitoredItemId = self._monitored_item_id

            params = copy.copy(self._monitoring_params)
            if samplingInterval is not None:
                params.samplingInterval = samplingInterval
            if queueSize is not None:
                params.queueSize = queueSize
            if discardOldest is not None:
                params.discardOldest = discardOldest
            if resolved_filter is not None:
                params.filter = resolved_filter

            item_modify.requestedParameters = params

            modify_request.itemsToModify = [item_modify]

            response = await self._subscription._client._service_modifyMonitoredItems(
                modify_request
            )
            response.responseHeader.serviceResult.check(message="Monitored item modification")

            result = response.results[0]
            result.statusCode.check(message="Monitored item modify result")
            self._monitoring_params.samplingInterval = result.revisedSamplingInterval
            self._monitoring_params.queueSize = result.revisedQueueSize

        return self._subscription._client._maybe_async(_modify())

    def setMonitoringMode(self, mode: ns0.datatypes.MonitoringMode) -> MaybeAwaitable[None]:
        """Set whether this item samples and reports.

        Args:
            mode: `DISABLED` stops sampling, `SAMPLING` samples without
                reporting, and `REPORTING` samples and reports.

        Raises:
            RuntimeError: The item has been deleted.
            StatusCodeError: The SetMonitoringMode service call failed.
        """

        async def _set_mode() -> None:
            self._check_valid("set_monitoring_mode")
            assert self._subscription.id is not None  # _check_valid ensures non-None
            assert self._monitored_item_id is not None  # _check_valid ensures non-None

            request = ns0.datatypes.SetMonitoringModeRequest()
            request.subscriptionId = self._subscription.id
            request.monitoringMode = mode
            request.monitoredItemIds = [self._monitored_item_id]

            response = await self._subscription._client._service_setMonitoringMode(request)
            response.responseHeader.serviceResult.check(message="Set monitoring mode")

            result = response.results[0]
            result.check(message="Set monitoring mode result")
            self._monitoring_mode = mode

        return self._subscription._client._maybe_async(_set_mode())

    def setTriggering(
        self,
        linksToAdd: list[MonitoredItem] | None = None,
        linksToRemove: list[MonitoredItem] | None = None,
    ) -> MaybeAwaitable[None]:
        """Link other items so they report whenever this item reports.

        A triggering link lets a rarely-changing item pull others along: the
        linked items report together with this one even while they are only
        `SAMPLING`.

        Args:
            linksToAdd: Items to start reporting alongside this one.
            linksToRemove: Items to unlink.

        Raises:
            RuntimeError: The item has been deleted.
            StatusCodeError: The SetTriggering service call failed, or the server
                rejected one of the links.
        """

        async def _set_triggering() -> None:
            self._check_valid("set_triggering")
            assert self._subscription.id is not None  # _check_valid ensures non-None
            assert self._monitored_item_id is not None  # _check_valid ensures non-None

            request = ns0.datatypes.SetTriggeringRequest()
            request.subscriptionId = self._subscription.id
            request.triggeringItemId = self._monitored_item_id
            if linksToAdd:
                request.linksToAdd = [item.id for item in linksToAdd]  # type: ignore[misc]
            if linksToRemove:
                request.linksToRemove = [item.id for item in linksToRemove]  # type: ignore[misc]

            response = await self._subscription._client._service_setTriggering(request)
            response.responseHeader.serviceResult.check(message="Set triggering")

            for i, result in enumerate(response.addResults):
                result.check(message=f"Set triggering add link [{i}]")
            for i, result in enumerate(response.removeResults):
                result.check(message=f"Set triggering remove link [{i}]")

        return self._subscription._client._maybe_async(_set_triggering())

    @property
    def _subscription(self) -> Subscription:
        if self._subscription_ref is None:
            raise RuntimeError("MonitoredItem is not bound to a client subscription")
        s = self._subscription_ref()
        if s is None:
            raise RuntimeError("Subscription has been garbage-collected")
        return s

    @property
    def client(self) -> Client:
        """The client that owns the subscription this item belongs to."""
        return self._subscription._client

    @property
    def subscription(self) -> Subscription:
        """The subscription this item belongs to."""
        return self._subscription

    @property
    def itemToMonitor(self) -> ns0.datatypes.ReadValueId:
        """What is being monitored: node, attribute, index range, and encoding.

        A copy, so the item's own state cannot be mutated behind the client's
        back.
        """
        # Return a copy so callers cannot mutate the item's internal state.
        return copy.copy(self._item_to_monitor)

    @property
    def params(self) -> ns0.datatypes.MonitoringParameters:
        """The sampling parameters in force, as revised by the server.

        A copy, so the item's own state cannot be mutated behind the client's
        back.
        """
        # Return a copy so callers cannot mutate the item's internal state.
        return copy.copy(self._monitoring_params)

    @property
    def mode(self) -> ns0.datatypes.MonitoringMode:
        """The current monitoring mode."""
        return self._monitoring_mode

    @property
    def id(self) -> int | None:
        """Server-assigned item id; `None` before creation and after deletion."""
        return self._monitored_item_id


class Subscription:
    """A client subscription that groups monitored items.

    Created by `Client.createSubscription(...)` rather than directly. A
    subscription owns its [`MonitoredItem`][o6.subscription.MonitoredItem] objects and their
    common publishing schedule, so items can be enabled, retimed, and removed
    together.

    Awaiting the subscription waits for the server to acknowledge creation, which
    is when its `id` becomes available. The subscription is falsy once deleted,
    and every operation on a deleted subscription raises `RuntimeError`.

    All configuration properties are read-only and report the values the server
    revised, not the values requested.

    See [Managing subscriptions explicitly](../manual/client/subscriptions.md#managing-subscriptions-explicitly).
    """

    def __init__(
        self,
        client: Client,
        publishingInterval: float,
        lifetimeCount: int,
        maxKeepaliveCount: int,
        maxNotificationsPerPublish: int = 10,
        publishingEnabled: bool = True,
        onCreated: (
            Callable[["Subscription", ns0.datatypes.CreateSubscriptionResponse], None] | None
        ) = None,
        onStatusChange: (
            Callable[["Subscription", ns0.datatypes.StatusChangeNotification], None] | None
        ) = None,
        onDeleted: Callable[["Subscription"], None] | None = None,
    ) -> None:
        """Request a new subscription from the server.

        Prefer `Client.createSubscription(...)`, which registers the result with
        the client. The CreateSubscription call is started here and completed when
        the subscription is awaited.

        Args:
            client: The client that will own the subscription.
            publishingInterval: Requested publishing interval in milliseconds.
            lifetimeCount: Publishing intervals the server keeps the subscription
                alive without a Publish request.
            maxKeepaliveCount: Publishing intervals without notifications after
                which the server sends a keepalive.
            maxNotificationsPerPublish: Cap on notifications per Publish
                response. `0` means unlimited.
            publishingEnabled: Whether the server starts out publishing.
            onCreated: Called when the server acknowledges creation, as
                `(subscription, response)`. The subscription's own `id` is
                assigned after this runs, so read `response.subscriptionId`.
            onStatusChange: Called with `(subscription, notification)` when the
                server publishes a StatusChangeNotification, for example on a
                keepalive timeout or a session transfer.
            onDeleted: Called with `(subscription,)` on explicit deletion and on
                session close.

        Raises:
            TypeError: A callback argument is not callable.
        """
        self._client_ref: weakref.ref[Client] = weakref.ref(client)
        self._subscription_id: int | None = None
        self._monitored_items: dict[int, MonitoredItem] = {}
        self._publishing_interval = publishingInterval
        self._lifetime_count = lifetimeCount
        self._max_keepalive_count = maxKeepaliveCount
        self._max_notifications_per_publish = maxNotificationsPerPublish
        self._publishing_enabled = publishingEnabled
        self._on_created = onCreated
        self._on_status_change = onStatusChange
        self._on_deleted = onDeleted

        for cb, name in (
            (onCreated, "onCreated"),
            (onStatusChange, "onStatusChange"),
            (onDeleted, "onDeleted"),
        ):
            if cb is not None and not callable(cb):
                raise TypeError(f"{name} must be callable or None")

        # Build C-level trampolines that inject `self` so user callbacks
        # receive (sub, ...) rather than (sub_id, ...).  None is passed
        # through verbatim so the C layer can take the zero-overhead path.
        c_created = None
        if onCreated is not None:

            def c_created(response: ns0.datatypes.CreateSubscriptionResponse) -> None:
                try:
                    onCreated(self, response)
                except Exception:
                    client._logger.exception("Subscription on_created callback raised")

        c_status_change = None
        if onStatusChange is not None:

            def c_status_change(
                sub_id: int, notification: ns0.datatypes.StatusChangeNotification
            ) -> None:
                try:
                    onStatusChange(self, notification)
                except Exception:
                    client._logger.exception("Subscription on_status_change callback raised")

        c_deleted = None
        if onDeleted is not None:

            def c_deleted(sub_id: int) -> None:
                try:
                    onDeleted(self)
                except Exception:
                    client._logger.exception("Subscription on_deleted callback raised")

        async def _create_subscription() -> None:
            create_request = ns0.datatypes.CreateSubscriptionRequest()
            create_request.requestedPublishingInterval = publishingInterval
            create_request.requestedLifetimeCount = lifetimeCount
            create_request.requestedMaxKeepAliveCount = maxKeepaliveCount
            create_request.maxNotificationsPerPublish = maxNotificationsPerPublish
            create_request.publishingEnabled = publishingEnabled
            create_request.priority = 0

            response = await client._service_createSubscription(
                create_request, c_created, c_status_change, c_deleted
            )
            response.responseHeader.serviceResult.check(message="Subscription creation")
            self._subscription_id = response.subscriptionId

        self._pending_init = client._maybe_async(_create_subscription())

    def __await__(self) -> Generator[Any, None, Subscription]:
        """Wait for the server to create this subscription, then return it."""

        async def _init() -> Subscription:
            if self._pending_init is not None:
                await self._pending_init
                self._pending_init = None
            return self

        return _init().__await__()

    def __bool__(self) -> bool:
        """False once the subscription has been deleted, or before creation."""
        return self._subscription_id is not None

    def _check_valid(self, op: str) -> None:
        if not self:
            raise RuntimeError(
                f"Cannot call {op!r} on an uninitialized or already-deleted Subscription"
            )

    def _monitor(
        self,
        nodeid: NodeIdLike | ns0.datatypes.ReadValueId,
        callback: MonitoredItem.DataChangeCallback | None = None,
        sampling_interval: float = 100.0,
        on_created: MonitoredItem.CreatedCallback | None = None,
        on_deleted: MonitoredItem.DeletedCallback | None = None,
        *,
        value_only: bool = True,
        filter: ns0.datatypes.DataChangeFilter | None = None,
        monitoring_mode: ns0.datatypes.MonitoringMode = ns0.datatypes.MonitoringMode.REPORTING,
        queue_size: int = 1,
        discard_oldest: bool = True,
    ) -> MaybeAwaitable[MonitoredItem]:

        def printout(mon: MonitoredItem, value) -> None:
            print(f"MonitoredItem {mon._monitored_item_id}: {value}")

        typed_callback: MonitoredItem.DataChangeCallback = printout
        if callback is not None:
            typed_callback = callback

        # if isinstance(nodeid, nodes.Node):
        #    nodeid = nodeid._nodeid

        async def _monitor_async() -> MonitoredItem:
            self._check_valid("monitor_data_change")
            monitored_item = await MonitoredItem._data_change(
                self,
                nodeid,
                typed_callback,
                sampling_interval=sampling_interval,
                value_only=value_only,
                on_created=on_created,
                on_deleted=on_deleted,
                filter=filter,
                monitoring_mode=monitoring_mode,
                queue_size=queue_size,
                discard_oldest=discard_oldest,
            )
            assert monitored_item.id is not None
            self._monitored_items[monitored_item.id] = monitored_item
            return monitored_item

        return self._client._maybe_async(_monitor_async())

    def _monitor_event(
        self,
        nodeid: NodeIdLike,
        callback: MonitoredItem.EventCallback,
        on_created: MonitoredItem.CreatedCallback | None = None,
        on_deleted: MonitoredItem.DeletedCallback | None = None,
        *,
        filter: ns0.datatypes.EventFilter | str | None = None,
        monitoring_mode: ns0.datatypes.MonitoringMode = ns0.datatypes.MonitoringMode.REPORTING,
        queue_size: int = 100,
        discard_oldest: bool = True,
    ) -> MaybeAwaitable[MonitoredItem]:

        async def _monitor_event_async() -> MonitoredItem:
            self._check_valid("monitor_event")
            monitored_item = await MonitoredItem._event(
                self,
                nodeid,
                callback,
                filter=filter,
                on_created=on_created,
                on_deleted=on_deleted,
                monitoring_mode=monitoring_mode,
                queue_size=queue_size,
                discard_oldest=discard_oldest,
            )
            assert monitored_item.id is not None
            self._monitored_items[monitored_item.id] = monitored_item
            return monitored_item

        return self._client._maybe_async(_monitor_event_async())

    def delete(self) -> MaybeAwaitable[None]:
        """Delete this subscription and every item in it.

        The monitored items are deleted first, then the subscription itself.
        Deleting a subscription that is already gone logs a warning instead of
        raising.

        Raises:
            RuntimeError: The owning client has been garbage-collected.
            StatusCodeError: The DeleteSubscriptions service call failed.
        """

        async def _delete() -> None:
            if self._subscription_id is None:
                self._client._logger.warning(
                    "Subscription.delete() called on an uninitialized or already-deleted subscription"
                )
                return

            subscription_id = self._subscription_id

            # Delete all monitored items first (before clearing _subscription_id,
            # because item.delete() reads self._subscription._subscription_id)
            for item in list(self._monitored_items.values()):
                await item.delete()  # type: ignore[misc]

            self._subscription_id = None

            # Delete subscription
            delete_request = ns0.datatypes.DeleteSubscriptionsRequest()
            delete_request.subscriptionIds = [subscription_id]

            response = await self._client._service_deleteSubscriptions(delete_request)
            response.responseHeader.serviceResult.check(message="Subscription deletion")

            if subscription_id in self._client._subscriptions:
                del self._client._subscriptions[subscription_id]

        return self._client._maybe_async(_delete())

    def modify(
        self,
        publishingInterval: float | None = None,
        lifetimeCount: int | None = None,
        maxKeepaliveCount: int | None = None,
        maxNotificationsPerPublish: int | None = None,
        publishingEnabled: bool | None = None,
    ) -> MaybeAwaitable[None]:
        """Change this subscription's publishing parameters on the server.

        Omitted arguments keep their current value. The server may revise the
        timing values, and the revised values are stored back, so reading the
        properties afterwards reports what was actually granted. Changing
        `publishingEnabled` needs a second service call, which is only sent when
        the value actually differs.

        Args:
            publishingInterval: Requested publishing interval in milliseconds.
            lifetimeCount: Publishing intervals the server keeps the subscription
                alive without a Publish request.
            maxKeepaliveCount: Publishing intervals without notifications after
                which the server sends a keepalive.
            maxNotificationsPerPublish: Cap on notifications per Publish
                response. `0` means unlimited.
            publishingEnabled: Whether the server sends notifications at all.

        Raises:
            RuntimeError: The subscription has been deleted.
            StatusCodeError: The ModifySubscription or SetPublishingMode service
                call failed.
        """

        async def _modify() -> None:
            self._check_valid("modify")
            assert self._subscription_id is not None  # _check_valid ensures non-None

            modify_request = ns0.datatypes.ModifySubscriptionRequest()
            modify_request.subscriptionId = self._subscription_id
            modify_request.requestedPublishingInterval = (
                publishingInterval if publishingInterval is not None else self._publishing_interval
            )
            modify_request.requestedLifetimeCount = (
                lifetimeCount if lifetimeCount is not None else self._lifetime_count
            )
            modify_request.requestedMaxKeepAliveCount = (
                maxKeepaliveCount if maxKeepaliveCount is not None else self._max_keepalive_count
            )
            modify_request.maxNotificationsPerPublish = (
                maxNotificationsPerPublish
                if maxNotificationsPerPublish is not None
                else self._max_notifications_per_publish
            )

            response = await self._client._service_modifySubscription(modify_request)
            response.responseHeader.serviceResult.check(message="Subscription modification")

            self._publishing_interval = response.revisedPublishingInterval
            self._lifetime_count = response.revisedLifetimeCount
            self._max_keepalive_count = response.revisedMaxKeepAliveCount

            # publishing_enabled requires a separate SetPublishingMode service call
            if publishingEnabled is not None and publishingEnabled != self._publishing_enabled:
                spm_request = ns0.datatypes.SetPublishingModeRequest()
                spm_request.publishingEnabled = publishingEnabled
                spm_request.subscriptionIds = [self._subscription_id]
                spm_response = await self._client._service_setPublishingMode(spm_request)
                spm_response.responseHeader.serviceResult.check(message="Set publishing mode")
                self._publishing_enabled = publishingEnabled

        return self._client._maybe_async(_modify())

    # Properties

    @property
    def _client(self) -> Client:
        c = self._client_ref()
        if c is None:
            raise RuntimeError("Client has been garbage-collected")
        return c

    @property
    def client(self) -> Client:
        """The client that owns this subscription."""
        return self._client

    @property
    def id(self) -> int | None:
        """Server-assigned subscription id; `None` before creation and after deletion."""
        return self._subscription_id

    @property
    def monitoredItems(self) -> dict[int, MonitoredItem]:
        """The items in this subscription, keyed by item id.

        A copy, so adding or removing entries does not affect the subscription.
        """
        return self._monitored_items.copy()

    @property
    def publishingInterval(self) -> float:
        """Publishing interval in milliseconds, as revised by the server."""
        return self._publishing_interval

    @property
    def lifetimeCount(self) -> int:
        """Lifetime count in publishing intervals, as revised by the server."""
        return self._lifetime_count

    @property
    def maxKeepaliveCount(self) -> int:
        """Keepalive count in publishing intervals, as revised by the server."""
        return self._max_keepalive_count

    @property
    def maxNotificationsPerPublish(self) -> int:
        """Cap on notifications per Publish response. `0` means unlimited."""
        return self._max_notifications_per_publish

    @property
    def enabled(self) -> bool:
        """Whether the server is currently publishing notifications."""
        return self._publishing_enabled


__all__ = ["MonitoredItem", "Subscription"]


def __dir__() -> list[str]:
    return sorted(__all__)
