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

"""Receive certificate and trust-list updates from an external manager.

External GDS interoperability is unverified. Follow the setup instructions below.
"""


import argparse
import getpass
import hmac
import os
import time
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

import o6
from o6.ns import ns0





class ManagementAccessControl(o6.AccessControl):
    """Accept only the configured administrator on encrypted sessions."""

    def __init__(self, username: str, password: str) -> None:
        super().__init__(anonymous=False, username=True)
        if not username or not password:
            raise ValueError("Administrator username and password must be nonempty")
        self._username = username
        self._password = password.encode("utf-8")

    def activateSession(
        self,
        endpoint: ns0.datatypes.EndpointDescription,
        remoteCertificate: bytes,
        session: o6.Session,
        userIdentityToken: Any,
    ) -> o6.SessionActivation:
        if endpoint.securityMode != o6.SecurityMode.SIGN_AND_ENCRYPT:
            raise o6.StatusCodeError(o6.StatusCode.BAD_SECURITY_MODE_INSUFFICIENT)
        if (
            not isinstance(userIdentityToken, ns0.datatypes.UserNameIdentityToken)
            or userIdentityToken.userName != self._username
            or not hmac.compare_digest(userIdentityToken.password, self._password)
        ):
            raise o6.StatusCodeError(o6.StatusCode.BAD_USER_ACCESS_DENIED)
        return o6.SessionActivation(context=self._username, roles=(o6.roles.security_admin,))

    def _is_administrator(self, session: o6.Session) -> bool:
        return session.context == self._username and o6.roles.security_admin in session.roles

    # Custom Python hooks replace the SDK authorization callbacks.
    def allowBrowseNode(self, session: o6.Session, nodeId: o6.NodeId) -> bool:
        return self._is_administrator(session)

    def getUserExecutable(self, session: o6.Session, methodId: o6.NodeId) -> bool:
        return self._is_administrator(session)

    def getUserExecutableOnObject(
        self, session: o6.Session, methodId: o6.NodeId, objectId: o6.NodeId
    ) -> bool:
        return self._is_administrator(session)






def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--endpoint", required=True, help="opc.tcp://host:port to listen on")
    parser.add_argument("--store", required=True, type=Path, help="manually provisioned PKI root")
    parser.add_argument(
        "--certificate", required=True, type=Path, help="server certificate, DER/PEM"
    )
    parser.add_argument("--private-key", required=True, type=Path, help="matching key, DER/PEM")
    parser.add_argument("--application-uri", required=True, help="URI in the server certificate")
    parser.add_argument("--admin-user", required=True)
    args = parser.parse_args()
    endpoint = urlsplit(args.endpoint)
    try:
        port = endpoint.port
    except ValueError as error:
        parser.error(str(error))
    if (
        endpoint.scheme != "opc.tcp"
        or not endpoint.hostname
        or not port
        or endpoint.username is not None
        or endpoint.password is not None
        or endpoint.query
        or endpoint.fragment
        or endpoint.path not in ("", "/")
    ):
        parser.error("--endpoint must be opc.tcp://host:port (port 1–65535)")
    password = os.environ.get("O6_GDS_ADMIN_PASSWORD")
    if password is None:
        password = getpass.getpass("GDS administrator password: ")
    access_control = ManagementAccessControl(args.admin_user, password)
    certificate = args.certificate.read_bytes()
    private_key = args.private_key.read_bytes()


    server = o6.Server()
    server.config.setDefaultWithFilestore(certificate, private_key, str(args.store), port=port)
    # Filestore setup resets defaults, including identity and authentication.
    server.config.applicationUri = args.application_uri
    server.config.serverUrls = [args.endpoint]
    server.config.setAccessControl(access_control)
    server.enablePushManagement()

    with server:
        print(f"GDS receiver ready at {args.endpoint} (externally unverified)", flush=True)
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass




if __name__ == "__main__":
    main()