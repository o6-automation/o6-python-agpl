# o6-python2 Client Configuration Options

This document provides a comprehensive overview of all OPC UA client configuration options from the underlying open62541 library and their implementation status in o6-python2.

## Configuration Options

| Option | Type | Status | Comment |
|--------|------|--------|---------|
| `clientContext` | `void*` | ❌ | User-defined pointer attached to the client |
| `logging` | `UA_Logger*` | ❌ | Plugin for log output |
| `timeout` | `UA_UInt32` | ✅ | Response timeout in ms |
| `clientDescription` | `UA_ApplicationDescription` | ✅ | Client application metadata (as `applicationDescription`) |
| `endpointUrl` | `UA_String` | ✅ | Target OPC UA server endpoint URL |
| `userIdentityToken` | `UA_ExtensionObject` | ✅ | User authentication token |
| `securityMode` | `UA_MessageSecurityMode` | ✅ | Message security mode (0=None, 1=Sign, 2=SignAndEncrypt) |
| `securityPolicyUri` | `UA_String` | ✅ | Security policy URI |
| `noSession` | `UA_Boolean` | ✅ | Only open SecureChannel, no Session |
| `noReconnect` | `UA_Boolean` | ✅ | Don't reconnect SecureChannel when connection lost |
| `noNewSession` | `UA_Boolean` | ✅ | Don't create new Session when initial one is lost |
| `endpoint` | `UA_EndpointDescription` | ✅ | Target endpoint description |
| `userTokenPolicy` | `UA_UserTokenPolicy` | ✅ | User token policy for authentication |
| `applicationUri` | `UA_String` | ✅ | Application URI filter for FindServers/GetEndpoints |
| `tcpReuseAddr` | `UA_Boolean` | ✅ | Enable TCP socket address reuse |
| `customDataTypes` | `UA_DataTypeArray*` | ❌ | Custom data types for message decoding |
| `namespaces` | `UA_String*` | ❌ | Predefined namespace mappings |
| `namespacesSize` | `size_t` | ❌ | Size of namespaces array |
| `secureChannelLifeTime` | `UA_UInt32` | ❌ | SecureChannel lifetime in ms |
| `requestedSessionTimeout` | `UA_UInt32` | ❌ | Requested session timeout in ms |
| `localConnectionConfig` | `UA_ConnectionConfig` | ❌ | Local connection configuration |
| `connectivityCheckInterval` | `UA_UInt32` | ❌ | Connectivity check interval in ms |
| `eventLoop` | `UA_EventLoop*` | ❌ | EventLoop instance |
| `externalEventLoop` | `UA_Boolean` | ❌ | EventLoop is not deleted with config |
| `securityPoliciesSize` | `size_t` | ❌ | Number of available security policies |
| `securityPolicies` | `UA_SecurityPolicy*` | ❌ | Available security policies |
| `certificateVerification` | `UA_CertificateGroup` | ❌ | Certificate verification plugin |
| `maxTrustListSize` | `UA_UInt32` | ❌ | Maximum trust list size in bytes |
| `maxRejectedListSize` | `UA_UInt32` | ❌ | Maximum rejected list size |
| `authSecurityPoliciesSize` | `size_t` | ❌ | Number of auth security policies |
| `authSecurityPolicies` | `UA_SecurityPolicy*` | ❌ | Security policies for authentication |
| `authSecurityPolicyUri` | `UA_String` | ❌ | SecurityPolicyUri for authentication |
| `stateCallback` | `function pointer` | ❌ | Callback for client state changes |
| `inactivityCallback` | `function pointer` | ❌ | Callback for connectivity check failures |
| `outStandingPublishRequests` | `UA_UInt16` | ❌ | Number of queued PublishResponse in server |
| `subscriptionInactivityCallback` | `function pointer` | ❌ | Callback for subscription inactivity |
| `sessionName` | `UA_String` | ❌ | Name of the session |
| `sessionLocaleIds` | `UA_LocaleId*` | ❌ | Locale IDs for the session |
| `sessionLocaleIdsSize` | `size_t` | ❌ | Size of sessionLocaleIds array |
| `privateKeyPasswordCallback` | `function pointer` | ❌ | Callback for private key password |

## Status Legend

- ✅ **Implemented**: Fully supported with getter/setter functionality
- ❌ **Not Implemented**: Available in open62541 but not exposed in o6-python2
- ⏳ **Partial**: Limited or indirect support

## Access Pattern

Configuration options are accessed via `client._client.config`:

```python
import o6

client = o6.Client()
config = client._client.config

# Example: Set basic options
config.timeout = 30000
config.endpointUrl = "opc.tcp://localhost:4840"
config.securityMode = 2
```

## Implementation Summary

**Total Configuration Options**: 37  
**Implemented**: 13 (35%)  
**Not Implemented**: 24 (65%)

The implemented options cover the essential client configuration needs:
- Basic connection parameters (timeout, endpointUrl)
- Security configuration (securityMode, securityPolicyUri, userIdentityToken)
- Connection control (noSession, noReconnect, noNewSession, tcpReuseAddr)
- Application identification (applicationDescription, applicationUri)
- Endpoint and token policy configuration

Advanced features like custom data types, namespace mapping, callbacks, and certificate management are not currently exposed through the Python interface.
