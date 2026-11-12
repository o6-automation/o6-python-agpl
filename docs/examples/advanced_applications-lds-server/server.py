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

"""Run a Local Discovery Server, optionally announcing registrations through mDNS."""

import argparse
import time

import o6
from o6.discovery import MdnsConfig
from o6.ns.ns0.datatypes import ApplicationType
from o6.util import createSelfSignedCertificate

PORT = 4840


def main(mdns=False):
    key, certificate = createSelfSignedCertificate(appUri="urn:o6:lds")
    server = o6.Server(
        port=PORT,
        applicationUri="urn:o6:lds",
        certificate=certificate,
        privateKey=key,
        acceptAllCertificates=True,
    )
    server.config.applicationType = ApplicationType.DISCOVERY_SERVER
    if mdns:
        server.setMdns(MdnsConfig(announceRegisteredServers=True))

    with server:
        print(f"LDS ready at opc.tcp://localhost:{PORT}", flush=True)
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
    print("LDS stopped", flush=True)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mdns", action="store_true", help="announce registrations through mDNS")
    main(parser.parse_args().mdns)