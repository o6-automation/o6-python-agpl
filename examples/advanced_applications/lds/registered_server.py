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

"""Publish a value and register this application with the local LDS."""

import time

import o6
from o6.util import createSelfSignedCertificate

LDS_URL = "opc.tcp://localhost:4840"
PORT = 4841
APPLICATION_URI = "urn:o6:lds:application"
APPLICATION_NAME = "O6-LDS-Application"


# BEGIN MD
# ## Register an application
# Start the application before registering its discovery URL. Renew the
# registration every 30 seconds and unregister when Ctrl+C is pressed.
# The client certificate must carry the registered application URI.
# END MD
# BEGIN CODE
def main():
    url = f"opc.tcp://localhost:{PORT}"
    server = o6.Server(port=PORT, applicationUri=APPLICATION_URI)
    server.addVariable(
        "LdsDemoValue",
        server.objectsNode,
        "Hello from the registered LDS application",
        nodeId="ns=1;s=LdsDemoValue",
    )
    key, certificate = createSelfSignedCertificate(appUri=APPLICATION_URI)
    lds = o6.Client(
        LDS_URL,
        certificate=certificate,
        privateKey=key,
        applicationUri=APPLICATION_URI,
        acceptAllCertificates=True,
        securityMode=o6.SecurityMode.SIGN_AND_ENCRYPT,
        securityPolicy=o6.SecurityPolicy.BASIC256SHA256,
    )
    try:
        lds.connect(noSession=True)
        with server:
            print(f"Application ready at {url}", flush=True)
            try:
                while True:
                    lds.registerServer(
                        APPLICATION_URI,
                        [url],
                        serverName=APPLICATION_NAME,
                        mdnsServerName=APPLICATION_NAME,
                        serverCapabilities=["DA"],
                    )
                    print("Registration confirmed", flush=True)
                    time.sleep(30)
            except KeyboardInterrupt:
                pass
            finally:
                lds.unregisterServer(APPLICATION_URI, [url])
                print("Unregistration confirmed", flush=True)
        print("Application stopped", flush=True)
    finally:
        lds.disconnect()


# END CODE

if __name__ == "__main__":
    main()
