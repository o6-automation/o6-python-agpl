# o6 OPC UA MCP server

A [Model Context Protocol](https://modelcontextprotocol.io) server that exposes
the [`o6`](../o6) OPC UA client as MCP tools. Connect any MCP-aware host (Claude
Desktop, VS Code, agent frameworks, …) to a running OPC UA server through this
bridge.

## Install

```bash
pip install -r examples/mcp_server/requirements.txt
# the o6 module itself is already part of this workspace
```

## Tools

| Tool | Purpose |
|---|---|
| `connect`         | Open a session to an OPC UA endpoint (optional username/password) |
| `disconnect`      | Close the session |
| `status`          | Report channel/session connection state |
| `get_endpoints`   | List endpoints offered by a server (no session required) |
| `read`            | Read a node attribute (defaults to `VALUE`) |
| `write`           | Write a value to a node attribute |
| `browse`          | Browse references (defaults to Objects folder, FORWARD) |
| `browse_path`     | Resolve and read a value through a dotted path under Root |
| `call_method`     | Invoke an OPC UA method |
| `get_server_info` | Read common `ServerStatus` fields |

The MCP server keeps a single shared `o6.Client` and serializes operations
with an asyncio lock.

## Running standalone

```bash
# stdio (default) — for MCP hosts that spawn the server as a subprocess
python -m examples.mcp_server.server

# SSE transport (HTTP) — for hosts that connect to a running server
python -m examples.mcp_server.server --transport sse
```

### Claude Desktop / generic MCP host config


You drive it from VS Code Copilot Chat in agent mode, which speaks MCP natively. Here is the minimal setup:

1. Register the MCP server with VS Code

    Create `.vscode/mcp.json` in this workspace with the following content:

```json
{
  "mcpServers": {
    "o6-opcua": {
      "command": "/path/to/o6-python/.venv/bin/python",
      "args": ["-m", "examples.mcp_server.server"],
      "cwd": "/path/to/o6-python"
    }
  }
}
```

2. Use it in Copilot Chat
   - Open the Chat view (`Ctrl+Alt+I`).
   - Switch the chat mode dropdown from **Ask** to **Agent**.
   - Click the tools icon at the bottom of the chat input — you should see the `o6-opcua` server with its 10 tools (`connect`, `read`, `browse`, …). If it isn't running yet, click **Start**. Output goes to **Output → MCP: o6-opcua**.
     - Tipp: you can selectively enable or disable tools, i.e. disable call() or write() operations
   - Tick the tools you want the model to be allowed to call (or leave them all on).
   - Now just chat. Examples to try:
     - Connect to `opc.tcp://localhost:4840` and tell me what's under the Objects folder.
     - What is the current temperature and pressure on the OPC UA server?
     - Set the `SetPoint` to `75` and confirm the new value.
     - Read `Objects.Server.ServerStatus.CurrentTime` via `browse_path`.
     - Disconnect from the server.

#### Try it with the demo_server

Start the demo OPC UA server (in one terminal) and leave it running. 
```bash
python -m examples.mcp_server.demo_server
```
It exposes `Temperature`, `Pressure`, `SetPoint`, `IsRunning`, `MachineName` on `opc.tcp://localhost:4840`.

Chat with the Agent about the server on localhost port 4840, the model will call `connect`, `browse`, `read`, `write`, `browse_path`, etc. on its own and you'll see each tool call expand inline with its JSON response.

#### Useful commands in VS Code
- `MCP: List Servers` — see status, restart, view logs
- `MCP: Show Output` — stderr from the server (the o6 banner / log lines)
- Each tool call is shown inline in chat; click it to inspect arguments and result JSON.

#### Other clients (optional)
The same `command`/`args` work for any MCP host:

Claude Desktop — put the same block under `mcpServers` in `claude_desktop_config.json`.

MCP Inspector for a graphical playground without an LLM:
It opens a UI where you can fire tools manually and see the raw JSON.

#### Tips
- The MCP server keeps one persistent OPC UA session, so once the agent has called connect it can do many read/write/browse calls in a row without reconnecting.
- If something looks stuck, run MCP: List Servers → Restart — that respawns the subprocess and drops the cached client.
- If you start demo_server after the MCP server has already been told to connect, just ask the AI to disconnect then connect again.


## Demo

`examples/mcp_server/demo.py` is a self-contained end-to-end test:

1. starts a small OPC UA server (port 4840) in a background thread,
2. launches `examples.mcp_server.server` over stdio,
3. drives it through the official MCP client,
4. prints every tool response.

```bash
python -m examples.mcp_server.demo
```

You should see endpoints, server status, a browse listing, a read/write
round-trip on `ns=1;s=SetPoint`, and the current server time.

`examples/mcp_server/demo_server.py` exposes the same OPC UA server as a standalone
process, useful when driving the MCP server from an external host.
