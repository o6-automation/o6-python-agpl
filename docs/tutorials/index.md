# Tutorials

The tutorials are task-by-task walkthroughs: each page introduces one concept at a time, against a single fixed example server, so you can follow along by running the snippets as you read.

**Start here:** [Set the Stage](setup.md) gets the example server running on your machine: save two files, run one command. Every tutorial talks to it, so it is worth the five minutes before anything else.

Beyond that, the tutorials are split by which side of the connection you are writing:

| Section | What it covers |
|---|---|
| [Set the Stage](setup.md) | One-time setup: save `server.py` and `sim.py` side by side, then run the example server. |
| [Client tutorials](client/index.md) | Connecting to an existing server: browsing, reading and writing, calling methods, subscriptions, security, information modelling, async. |
| [Server tutorials](server/index.md) | Building your own server. *Coming soon* — the [Server manual](../manual/server/index.md) covers this material today. |

## The example server

Every tutorial on this site talks to the same example server: a small **automated still** driven by a background simulation. Wash goes in, gets heated to a setpoint, vapour turns into spirit on the way through the condenser, the spent wash drains out, and the still goes back to idle to wait for the next batch.

It is two Python files you save side by side and run — `server.py` for the OPC UA side and the `sim.py` it imports. [Set the Stage](setup.md) has both, the address-space layout with every NodeId the tutorials use, and the handful of things worth knowing before you start poking at it.

## Where to go next

- [Set the Stage](setup.md) — get the example server running.
- [Client tutorials](client/index.md) — then start with [Connect / disconnect](client/100_connect.md).
- [Server tutorials](server/index.md) — coming soon.
