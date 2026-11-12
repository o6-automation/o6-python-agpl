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

# BEGIN MD
# This example lets an external certificate manager update the server's application
# certificate and trust lists using standard OPC UA PushManagement methods.
# Configure certificate storage and administrator authentication, then start the
# receiver. See [GDS PushManagement](../manual/server/security.md#gds-pushmanagement)
# for supported operations and limitations.
#
# Interoperability with external Global Discovery Server (GDS) products is unverified.
#
# ## Prepare trust and protected storage
#
# Use Linux or Windows. Both filestore setup and receiver enablement raise a
# `NotImplementedError` on macOS or builds missing the respective feature.
# Install `o6` and supply a server certificate and matching private key
# (DER or PEM). The certificate's application URI and hostnames must match the
# configured application URI and endpoint. Keep the manager's private key on the
# manager; transfer only its public certificate or certificate authority (CA) chain.
#
# Before startup, create the [PKI filestore](../manual/server/security.md#pki-filestore-configuration)
# root and manually provision the manager's trust. Missing directories are created
# during setup. The layout is the same below `ApplCerts`
# (application SecureChannels) and `UserTokenCerts` (certificate user tokens):
#
# ```text
# pki/
#   ApplCerts/                 UserTokenCerts/ has the same subdirectories
#     trusted/certs/          trusted certificates
#     trusted/crl/            trusted certificate revocation lists
#     issuer/certs/           issuer certificates
#     issuer/crl/             issuer certificate revocation lists
#     own/certs/              saved application certificates
#     own/private/            saved keys
#     rejected/certs/         rejected public certificates, not automatically trusted
# ```
#
# For example, with an independently verified, self-signed manager certificate,
# on Linux, run from the directory containing the downloaded `server.py`:
#
# ```sh
# umask 077
# mkdir -p pki/ApplCerts/trusted/certs
# cp /secure/manager.der pki/ApplCerts/trusted/certs/manager.der
# python server.py --endpoint opc.tcp://localhost:4840 --store ./pki \
#   --certificate /secure/server.der --private-key /secure/server-key.der \
#   --application-uri urn:example:gds-server --admin-user certificate-manager
# ```
#
# Replace the paths, URI and hostname with your provisioned identity. On Windows,
# create the same directory tree and restrict its ACL to the service account and
# required administrators before using the equivalent command. On Linux, protect
# existing directories and files too: `umask` affects only newly created files.
# Private keys are not encrypted at rest by this example.
# Protect the bootstrap key and backup copies as well as `own/private`.
#
# The password is prompted without echo, or read from `O6_GDS_ADMIN_PASSWORD` for
# service configuration. There is no default administrator or password. Configure
# the manager to trust the server certificate/issuer chain independently, and to
# connect using `Basic256Sha256`, `SignAndEncrypt` and the configured username and
# password. Trust and user authentication are separate checks. Unknown applications
# are never enrolled automatically; anonymous users, other usernames and wrong
# passwords are rejected.
# END MD

# BEGIN CODE
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

# END CODE


# BEGIN MD
# ## Authenticate and authorize the administrator
#
# The authenticated username receives `o6.roles.security_admin`. The example's
# custom browse, method and method-on-object hooks require both that identity and
# role. It accepts only administrator sessions and grants that administrator method
# access across this dedicated server; it is not a multi-user application policy.
# Its `activateSession` callback requires `SignAndEncrypt`. The unencrypted
# discovery endpoint does not accept application sessions through this plugin.
# END MD


# BEGIN CODE
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


# END CODE


# BEGIN MD
# ## Read explicit configuration
#
# The command-line arguments select the endpoint, PKI root and startup identity.
# Read the administrator password from the environment or a hidden prompt, and
# load the selected certificate and key before configuring the server.
# END MD


def main() -> None:
    # BEGIN CODE
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
    # END CODE

    # BEGIN MD
    # ## Configure the filestore and enable the receiver
    #
    # Filestore setup resets defaults. Apply the identity, endpoint and access-control
    # plugin afterwards, then attach PushManagement before startup.
    # END MD

    # BEGIN CODE
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
    # END CODE


# BEGIN MD
# ## Manage the receiver
#
# 1. Browse `Server/ServerConfiguration` (`i=12637`) over the encrypted session.
#    Read `DefaultApplicationGroup/CertificateTypes` (`i=14161`) and select a
#    configured certificate type.
# 2. Call `CreateSigningRequest` with `RegeneratePrivateKey` set to `False` to
#    retain the key. Have your CA sign the DER PKCS #10 certificate signing request
#    (CSR), preserving the application URI, hostnames and required usages.
#    For key rotation, generate a replacement key and certificate externally.
#    See [certificate renewal](../manual/server/security.md#renewing-the-application-certificate)
#    for the limitations of server-generated keys.
# 3. Call `UpdateCertificate` with the signed leaf certificate and an empty key
#    to retain the current key, or supply the replacement key in `DER` or `PEM`
#    format. Verify that the certificate matches the intended key. Provision
#    issuer chains through TrustList management separately.
# 4. Check the Call service result and each method's status. When
#    `ApplyChangesRequired` is `True`, call `ApplyChanges` in the same session.
#    Configure the manager to trust the replacement certificate and its issuer
#    chain, then reconnect after the server closes affected channels.
#
# Manage application and user-token trust through
# [TrustList operations](../manual/server/security.md#updating-trust-lists).
# Keep the manager's certificate trusted so it can reconnect. This example uses
# password login; user-token trust lists apply to certificate login.
#
# Finish or discard transactions and close TrustList handles before stopping.
# See [stopping and restarting](../manual/server/security.md#stopping-and-restarting)
# for pending operations that can survive a restart.
#
# ## Restart with explicitly selected credentials
#
# Trust lists and certificate revocation lists reload from the PKI store.
# Select the startup certificate and key explicitly:
#
# 1. Find the installed replacement certificate in `ApplCerts/own/certs` and pass
#    its path as `--certificate`.
# 2. For retained-key renewal, keep the original `--private-key`. For an explicitly
#    supplied key, select its matching file in `ApplCerts/own/private` or the
#    securely held original. Saved keys use the certificate-derived basename and
#    a `.key` suffix.
# 3. Verify the certificate/key pair before stopping, then restart the script with
#    those paths. Old files can remain; using the bootstrap paths restores that
#    identity.
#
# Verify the live identity and saved pair even after a successful update result.
# Certificate updates can leave partial changes in memory and on disk. See
# [certificate renewal](../manual/server/security.md#renewing-the-application-certificate)
# for recovery and storage limitations.
# END MD


if __name__ == "__main__":
    main()
