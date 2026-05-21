# o6.server.Server

High-level OPC UA Server.

Parameters
----------
port : int, optional
    TCP port number (default 4840).
logger : logging.Logger, optional
    Custom logger object.
loop : asyncio.AbstractEventLoop, optional
    Event loop used for cooperative scheduling.
    When provided (or when a running loop is detected), the server
    avoids spawning a background thread and instead schedules
    non-blocking iterations on the loop.  If *None* and no running
    loop exists, a daemon thread is used as a fallback.
certificate : str, Path, or bytes, optional
    Server certificate (file path or raw bytes).
private_key : str, Path, or bytes, optional
    Server private key (file path or raw bytes).
trust_list : list, optional
    Trusted certificates for client verification.
issuer_list : list, optional
    Issuer certificates.
revocation_list : list, optional
    Certificate revocation lists.
secure_only : bool
    If True, reject unencrypted connections (default False).
accept_all_certificates : bool
    If True, trust all client certificates (default False).
application_uri : str, optional
    Override the default application URI.

Example
-------
>>> server = Server(port=4840)
>>> with server:
...     temp = server.add_variable("Temperature",
...                                server.objects_node, 22.5)
...     print(temp.value)
22.5

::: o6.server.Server
    options:
      show_root_heading: true
      show_source: false
      show_category_heading: true
      members_order: source
      inherited_members: true
      show_signature: true
      separate_signature: true