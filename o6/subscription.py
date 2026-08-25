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
        async def _init() -> MonitoredItem:
            if self._pending_init is not None:
                await self._pending_init
                self._pending_init = None
            return self

        return _init().__await__()

    def __bool__(self) -> bool:
        return self._monitored_item_id is not None

    def _check_valid(self, op: str) -> None:
        if not self:
            raise RuntimeError(
                f"Cannot call {op!r} on an uninitialized or already-deleted MonitoredItem"
            )

    def delete(self) -> MaybeAwaitable[None]:

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
        return self._subscription._client

    @property
    def subscription(self) -> Subscription:
        return self._subscription

    @property
    def itemToMonitor(self) -> ns0.datatypes.ReadValueId:
        # Return a copy so callers cannot mutate the item's internal state.
        return copy.copy(self._item_to_monitor)

    @property
    def params(self) -> ns0.datatypes.MonitoringParameters:
        # Return a copy so callers cannot mutate the item's internal state.
        return copy.copy(self._monitoring_params)

    @property
    def mode(self) -> ns0.datatypes.MonitoringMode:
        return self._monitoring_mode

    @property
    def id(self) -> int | None:
        return self._monitored_item_id


class Subscription:
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
        async def _init() -> Subscription:
            if self._pending_init is not None:
                await self._pending_init
                self._pending_init = None
            return self

        return _init().__await__()

    def __bool__(self) -> bool:
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

    def delete(self) -> Any:

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
    ) -> Any:

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
        return self._client

    @property
    def id(self) -> int | None:
        return self._subscription_id

    @property
    def monitoredItems(self) -> dict[int, MonitoredItem]:
        return self._monitored_items.copy()

    @property
    def publishingInterval(self) -> float:
        return self._publishing_interval

    @property
    def lifetimeCount(self) -> int:
        return self._lifetime_count

    @property
    def maxKeepaliveCount(self) -> int:
        return self._max_keepalive_count

    @property
    def maxNotificationsPerPublish(self) -> int:
        return self._max_notifications_per_publish

    @property
    def enabled(self) -> bool:
        return self._publishing_enabled


__all__ = ["MonitoredItem", "Subscription"]


def __dir__() -> list[str]:
    return sorted(__all__)
