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

"""Load the JSON5 configuration files into a server or client config."""

from __future__ import annotations

import datetime
import json
import logging
import os
from typing import Any

from . import _o6

_types = _o6.types

_logger = logging.getLogger("o6")


def _set_fields(fields: dict[str, Any]) -> dict[str, Any]:
    """Drop unset fields, so that they stay unset instead of becoming empty."""
    return {key: value for key, value in fields.items() if value not in (None, "", [], {})}


def _localized_text(text: Any) -> dict[str, Any]:
    return _set_fields({"locale": text.locale, "text": text.text})


_EPOCH_1601 = datetime.datetime(1601, 1, 1, tzinfo=datetime.timezone.utc)


def _date_time(value: Any) -> str:
    """Render an OPC UA DateTime as ISO 8601 with its full 100 ns resolution."""
    seconds, ticks = divmod(int(value), 10_000_000)
    moment = _EPOCH_1601 + datetime.timedelta(seconds=seconds)
    return moment.strftime("%Y-%m-%dT%H:%M:%S") + (f".{ticks:07d}" if ticks else "") + "Z"


def _build_info(info: Any) -> dict[str, Any]:
    """Render a BuildInfo with the field names of the file format."""
    return _set_fields(
        {
            "productUri": info.productUri,
            "manufacturerName": info.manufacturerName,
            "productName": info.productName,
            "softwareVersion": info.softwareVersion,
            "buildNumber": info.buildNumber,
            "buildDate": _date_time(info.buildDate) if info.buildDate is not None else None,
        }
    )


def _application_description(description: Any) -> dict[str, Any]:
    """Render a server ApplicationDescription with the field names of the file format."""
    return _set_fields(
        {
            "applicationUri": description.applicationUri,
            "productUri": description.productUri,
            "applicationName": _localized_text(description.applicationName),
            "applicationType": int(description.applicationType),
            "gatewayServerUri": description.gatewayServerUri,
            "discoveryProfileUri": description.discoveryProfileUri,
            "discoveryUrls": list(description.discoveryUrls or []),
        }
    )


def _client_description(description: Any) -> dict[str, Any]:
    """Render the fields of a client ApplicationDescription that the file format has.

    open62541 does not skip the value of an unknown nested field, which
    misreads the rest of the document, so only known fields may be sent.
    """
    return _set_fields(
        {
            "applicationUri": description.applicationUri,
            "productUri": description.productUri,
            "applicationName": _localized_text(description.applicationName),
        }
    )


def _server_defaults(config: Any) -> dict[str, Any]:
    return {
        "buildInfo": _build_info(config.buildInfo),
        "applicationDescription": _application_description(config.applicationDescription),
        "serverUrls": list(config.serverUrls),
        "copyMethodsOnInstances": config.copyMethodsOnInstances,
    }


def _client_defaults(config: Any) -> dict[str, Any]:
    defaults = {
        "applicationDescription": _client_description(config.applicationDescription),
        "maxAsyncServiceCalls": config.maxAsyncServiceCalls,
        "tcpReuseAddr": config.tcpReuseAddr,
    }
    if config.endpointUrl is not None:
        defaults["endpointUrl"] = config.endpointUrl
    return defaults


def _merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    """Merge objects key by key; any other value of `override` replaces `base`.

    A nested object of the file then keeps the o6 default of every field it
    leaves out.
    """
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = _merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def _pubsub_entitled() -> bool:
    try:
        _o6._require_pubsub()
    except PermissionError:
        return False
    return True


def _name_invalid_settings(config: Any, document: dict[str, Any], error: Exception) -> None:
    """Add a note for each top-level setting that fails to load on its own."""
    for key, value in document.items():
        try:
            config._loadJson(json.dumps({key: value}).encode(), dryRun=True)
        except _o6.StatusCodeError:
            error.add_note(f"Invalid setting {key!r}")


def load(config: Any, path: str | os.PathLike[str]) -> None:
    """Replace `config` with the settings of a JSON5 file and o6 defaults for the rest.

    Args:
        config: A `ServerConfig` or `ClientConfig`.
        path: The JSON5 file in the open62541 configuration format.
    """
    with open(path, "rb") as file:
        document = _types._parseJson5(file.read())
    options = {}
    if isinstance(config, _o6.ServerConfig):
        defaults = _server_defaults(config)
        # The file adds its security policies without endpoints
        options["addEndpoints"] = "securityPolicies" in document
        if document.get("pubsubEnabled") and not _pubsub_entitled():
            _logger.warning("pubsubEnabled ignored: the active Credential does not include PubSub")
    else:
        defaults = _client_defaults(config)
        if document.get("asyncServiceCallRule", 1) not in (0, 1):
            _logger.warning(
                "asyncServiceCallRule ignored: requests beyond maxAsyncServiceCalls are rejected"
            )
    try:
        config._loadJson(json.dumps(_merge(defaults, document)).encode(), **options)
    except _o6.StatusCodeError as error:
        _name_invalid_settings(config, document, error)
        raise
