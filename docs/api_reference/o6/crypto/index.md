# o6.crypto

Cryptographic utilities for OPC UA encryption.

Provides certificate generation, loading, and a CLI tool for creating
self-signed certificates suitable for OPC UA client/server communication.

Usage as module:
    from o6.crypto import create_self_signed_certificate, load_certificate

    key, cert = create_self_signed_certificate(
        app_uri="urn:my:app",
        common_name="MyApp@localhost",
    )

Usage as CLI:
    python -m o6.crypto --app-uri urn:my:app --common-name MyApp@localhost

::: o6.crypto
    options:
      show_root_heading: true
      show_source: false
      show_category_heading: true
      members_order: source
      inherited_members: true
      show_signature: true
      separate_signature: true