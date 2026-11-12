# Tutorials

Each tutorial covers one task. All of them run against the same example server, so you can run the snippets as you read.

**Start here:** [Set the Stage](setup.md) gets the example server running. Save two files and run one command.

## Contents

| Topic | What it covers |
|---|---|
| [Set the Stage](setup.md) | One-time setup: save `server.py` and `sim.py` side by side, then run the example server. |
| [Client tutorials](client/index.md) | Connecting to an existing server: browsing, reading and writing, calling methods, subscriptions, security, information modelling, async. |
| [Server tutorials](server/index.md) | Building your own server: the same distillery, one concept at a time. |

## The example server

The example server is a small automated still driven by a background simulation. Wash goes in and is heated to a setpoint. Vapour turns into spirit in the condenser, the spent wash drains out, and the still returns to idle until the next batch.

It consists of two Python files that you save side by side: `server.py` for the OPC UA side and `sim.py`, which it imports. [Set the Stage](setup.md) contains both files, the address-space layout with every NodeId the tutorials use, and what to know before you start.

## Next steps

| Topic | What it covers |
|---|---|
| [Set the Stage](setup.md) | Get the example server running. |
| [Server tutorials](server/index.md) | Build the server the client tutorials talk to. Start with [Creating a server](server/100_create-server.md). |
| [Client tutorials](client/index.md) | If you already have a server, start with [Connect / disconnect](client/100_connect.md). |
