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

"""Discover the registered application through the LDS and read its value."""

import argparse

import o6

LDS_URL = "opc.tcp://localhost:4840"


def main(mdns=False):
    url = None
    lds = o6.Client(LDS_URL)
    try:
        lds.connect(noSession=True)
        if mdns:
            for record in lds.findServersOnNetwork(serverCapabilityFilter=["DA"]):
                print(
                    f"Network: {record.serverName} {record.discoveryUrl} {list(record.serverCapabilities)}"
                )
                if record.serverName == "O6-LDS-Application":
                    url = record.discoveryUrl
        else:
            for application in lds.findServers(LDS_URL):
                print(f"Registered: {application.applicationUri} {list(application.discoveryUrls)}")
                if application.applicationUri == "urn:o6:lds:application":
                    url = application.discoveryUrls[0]
    finally:
        lds.disconnect()

    if url is None:
        print("No application found.")
        return
    with o6.Client(url) as client:
        print(f"Read: {client.read('ns=1;s=LdsDemoValue')}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mdns", action="store_true", help="discover through FindServersOnNetwork")
    main(parser.parse_args().mdns)