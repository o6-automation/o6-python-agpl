#!/usr/bin/env python3
# Copyright (c) 2026 o6 Automation GmbH
#
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

"""
Generate a self-signed OPC UA certificate and private key.

Usage:
    python examples/create_selfsigned_cert.py [options]

The certificate and key are written as DER files by default.
"""

import argparse
from pathlib import Path

from o6.crypto import create_self_signed_certificate


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="create_selfsigned_cert",
        description="Generate self-signed OPC UA certificates.",
    )
    parser.add_argument(
        "--app-uri",
        default="urn:open62541.server.application",
        help="Application URI (default: urn:open62541.server.application)",
    )
    parser.add_argument(
        "--common-name",
        default="Open62541Server@localhost",
        help="Common name for the certificate subject",
    )
    parser.add_argument(
        "--organization",
        default="o6",
        help="Organization name (default: o6)",
    )
    parser.add_argument(
        "--country",
        default="DE",
        help="Country code (default: DE)",
    )
    parser.add_argument(
        "--alt-name",
        action="append",
        default=[],
        help="Additional SAN entry (repeatable, e.g. DNS:myhost)",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=365,
        help="Certificate validity in days (default: 365)",
    )
    parser.add_argument(
        "--key-size",
        type=int,
        default=2048,
        choices=[2048, 4096],
        help="RSA key size in bits (default: 2048)",
    )
    parser.add_argument(
        "--fmt",
        default="DER",
        choices=["DER", "PEM"],
        help="Output format (default: DER)",
    )
    parser.add_argument(
        "--out-key",
        default="key.der",
        help="Output file for the private key (default: key.der)",
    )
    parser.add_argument(
        "--out-cert",
        default="cert.der",
        help="Output file for the certificate (default: cert.der)",
    )

    args = parser.parse_args(argv)

    key, cert = create_self_signed_certificate(
        app_uri=args.app_uri,
        common_name=args.common_name,
        organization=args.organization,
        country=args.country,
        alt_names=args.alt_name or None,
        expires_in_days=args.days,
        key_size=args.key_size,
        fmt=args.fmt,
    )

    Path(args.out_key).write_bytes(key)
    Path(args.out_cert).write_bytes(cert)

    print(f"Private key written to {args.out_key} ({len(key)} bytes)")
    print(f"Certificate written to {args.out_cert} ({len(cert)} bytes)")


if __name__ == "__main__":
    main()
