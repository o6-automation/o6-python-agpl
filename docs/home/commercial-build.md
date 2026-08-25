# Commercial build

This page applies to the commercial `o6` wheels distributed on PyPI. The AGPL
build does not use o6 Credentials or evaluation mode.

The commercial wheel contains the full Client and Server API. Without a valid
o6-issued Credential, importing `o6` starts a process-wide two-hour evaluation
period. When the period expires, the process terminates with a failure status.
On POSIX systems this is an immediate hard exit, so applications must not rely
on shutdown handlers running at evaluation expiry.

## Feature scope

The full compiled API remains importable so documentation, annotations, and
type discovery behave consistently. A valid Credential can separately enable
`client`, `server`, and `pubsub` operations:

| Feature | Effect when omitted |
| --- | --- |
| `client` | Constructing `o6.Client` raises `PermissionError`. |
| `server` | Constructing `o6.Server` raises `PermissionError`. |
| `pubsub` | `o6.pubsub` operations raise `PermissionError`; Server instances contain no PubSub manager, information-model methods, or PubSub transports. |

`pubsub` requires `server`, so a PubSub-enabled Credential contains both names.
An empty Feature Scope enables every compiled feature. Unknown, duplicate,
empty, or inconsistent scope entries make the Credential unusable and trigger
the documented evaluation fallback.

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

If the default file is absent, o6 enters evaluation mode and prints the normal
Trial Mode message without an additional missing-file warning. If
`O6PYTHON_LICENSE_FILE` names a missing file, or a Credential is unreadable,
malformed, incorrectly signed, not yet valid, or expired, o6 prints the specific
reason to standard error and falls back to evaluation mode. These warnings
remain visible when `O6PYTHON_SKIP_GREET` suppresses the startup banner and
routine valid-Credential information. The Trial Mode notice and expiry message
also always remain visible on standard error.
