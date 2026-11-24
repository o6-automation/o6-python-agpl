# Commercial build

This page applies to the commercial `o6` wheels on PyPI. The AGPL build does
not use o6 Credentials or Script Mode.

The commercial wheel contains the full Client and Server API. Without a valid
o6-issued Credential, it runs in ten-minute Script Mode, which permits commercial
use. Importing `o6` starts a process-wide timer. When the timer expires, the
process terminates with a failure status. On POSIX systems this is an immediate
hard exit, so don't rely on shutdown handlers running when Script Mode expires.
A valid Credential removes the limit.

## Feature scope

A valid Credential can enable `client`, `server` and `pubsub` operations
separately. The full compiled API stays importable either way, so
documentation, annotations and type discovery behave the same.

| Feature | Effect when omitted |
| --- | --- |
| `client` | Constructing `o6.Client` raises `PermissionError`. |
| `server` | Constructing `o6.Server` raises `PermissionError`. |
| `pubsub` | `o6.pubsub` operations raise `PermissionError`; Server instances contain no PubSub manager, information-model methods, or PubSub transports. |

`pubsub` requires `server`, so a PubSub-enabled Credential contains both names.
An empty feature scope enables every compiled feature. Unknown, duplicate,
empty or inconsistent scope entries make the Credential unusable, and o6 falls
back to Script Mode.

## Credential location

Set `O6PYTHON_LICENSE_FILE` to the Credential file's path:

```sh
export O6PYTHON_LICENSE_FILE=/path/to/o6python_license.json
python application.py
```

If `O6PYTHON_LICENSE_FILE` is unset, o6 checks only
`o6python_license.json` in the process's current working directory. It does not
search the user home directory, platform configuration directories, or the
installed package.

If the default file is absent, o6 enters Script Mode and prints only the normal
Script Mode message, with no missing-file warning.

If `O6PYTHON_LICENSE_FILE` names a missing file, or a Credential is unreadable,
malformed, incorrectly signed, not yet valid or expired, o6 prints the reason to
standard error and falls back to Script Mode.

`O6PYTHON_SKIP_GREET` suppresses the startup banner and routine
valid-Credential information. It does not suppress these warnings, the Script
Mode notice or the expiry message; they always appear on standard error.

## Check the active Credential

[`o6.license`](../api_reference/license.md) reports what o6 decided on import:
the edition, whether a Credential was accepted, its details and the enabled
features. Use it for deployment health checks and support diagnostics.

```python
import o6

info = o6.license
if info.licensed:
    print(f"{info.usageScope} for {info.holder}, valid to {info.validTo}")
elif info.rejectionReason:
    print("Credential rejected:", info.rejectionReason)
else:
    print("No Credential; Script Mode:", info.scriptMode)
```

[`LicenseInfo`](../api_reference/licenseinfo.md) describes each field.

The values never change after import. `o6.license` never contains the
Credential's signature or file contents. The AGPL build reports
`edition="agpl"`, `licensed=False`, `scriptMode=False` and every feature.
