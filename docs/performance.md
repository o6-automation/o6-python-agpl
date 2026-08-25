# Performance

The end-to-end read benchmark compares native open62541 C, o6\\Python, and
asyncua 2.0.1 as OPC UA clients and servers. It measures seven pairings:

| Client / server | Purpose |
| --- | --- |
| C / C | Native baseline |
| o6 / C and C / o6 | Isolate the o6 client and server |
| asyncua / C and C / asyncua | Isolate the asyncua client and server |
| o6 / o6 and asyncua / asyncua | Complete Python applications on both sides |

Each client is a separate process. All configurations read the same 100
writable `Int32` variables using the same NodeId sequence and a common process
barrier. Node objects are resolved before timing. Each table entry is the
median aggregate throughput across five samples; every client performs 2,000
reads after 100 warm-up reads.

Async clients keep at most 32 application requests open independently. The
total limits are therefore 32, 96, and 320 requests for one, three, and ten
client processes.

## Results

These measurements were recorded on 4 August 2026. Larger rates are better.
`#None` and `#Basic256Sha256` are OPC UA SecurityPolicy URI suffixes. Secure
runs use `SignAndEncrypt`.

### `#None`: native and crossed implementations

| Mode | Clients | C / C | o6 / C | C / o6 | asyncua / C | C / asyncua |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Sync | 1 | 40.8k | 9.8k | 35.7k | 7.6k | 13.2k |
| Sync | 3 | 109.9k | 23.1k | 81.3k | 19.5k | 26.3k |
| Sync | 10 | 216.3k | 42.7k | 88.4k | 35.6k | 26.3k |
| Async, depth 32 | 1 | 76.5k | 47.2k | 125.1k | 27.1k | 28.5k |
| Async, depth 32 | 3 | 168.1k | 136.4k | 130.1k | 87.5k | 30.1k |
| Async, depth 32 | 10 | 376.4k | 255.5k | 139.4k | 188.3k | 30.5k |

### `#None`: Python on both sides

| Mode | Clients | o6 / o6 | asyncua / asyncua |
| --- | ---: | ---: | ---: |
| Sync | 1 | 9.2k | 4.9k |
| Sync | 3 | 21.0k | 13.2k |
| Sync | 10 | 38.7k | 23.2k |
| Async, depth 32 | 1 | 47.2k | 26.9k |
| Async, depth 32 | 3 | 140.8k | 34.0k |
| Async, depth 32 | 10 | 135.1k | 33.8k |

### `#Basic256Sha256`: native and crossed implementations

| Mode | Clients | C / C | o6 / C | C / o6 | asyncua / C | C / asyncua |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Sync | 1 | 38.8k | 9.1k | 26.9k | 6.5k | 10.5k |
| Sync | 3 | 91.1k | 21.7k | 63.7k | 16.7k | 18.6k |
| Sync | 10 | 153.4k | 39.9k | 67.0k | 29.8k | 18.7k |
| Async, depth 32 | 1 | 126.5k | 38.8k | 77.5k | 20.5k | 20.9k |
| Async, depth 32 | 3 | 159.8k | 119.8k | 86.8k | 65.2k | 21.6k |
| Async, depth 32 | 10 | 225.7k | 150.7k | 89.3k | 128.5k | 22.0k |

### `#Basic256Sha256`: Python on both sides

| Mode | Clients | o6 / o6 | asyncua / asyncua |
| --- | ---: | ---: | ---: |
| Sync | 1 | 8.1k | 4.2k |
| Sync | 3 | 19.3k | 11.3k |
| Sync | 10 | 36.5k | 17.0k |
| Async, depth 32 | 1 | 39.8k | 20.4k |
| Async, depth 32 | 3 | 98.0k | 23.4k |
| Async, depth 32 | 10 | 97.7k | 23.2k |

All rates are reads per second.

## What the crossed results show

- Against the same C server, the o6 client is faster than asyncua in every
  row. At ten async clients it reaches 255.5k versus 188.3k reads/s without
  security and 150.7k versus 128.5k with `Basic256Sha256`.
- The larger difference is on the server side. With ten async C clients, the
  o6 server sustains 139.4k unencrypted reads/s versus 30.5k for asyncua. The
  encrypted results are 89.3k and 22.0k respectively.
- With Python on both sides, o6/o6 reaches 140.8k reads/s with three async
  clients and 135.1k with ten; asyncua/asyncua levels off near 34k. Under
  encryption the corresponding ceilings are about 98k and 23k.
- Both Python servers reach their single-process ceiling early. Additional
  client processes increase synchronous throughput, but async throughput is
  already effectively saturated at three clients.

## Test system and interpretation

| Component | Configuration |
| --- | --- |
| Computer | MacBook Pro, model Mac17,9 |
| Processor | Apple M5 Pro, 18 cores (6 Super, 12 Performance) |
| Memory | 64 GB |
| Operating system | macOS 26.6, Darwin 25.6.0, arm64 |
| Python | CPython 3.14.6, standard GIL build |
| asyncua | 2.0.1 |
| Transport | OPC UA TCP over `127.0.0.1:4840` |

These are development measurements, not release claims. The C executables
are compiled from the plain-C sources included under
`examples/benchmarks/open62541`; they do not use the o6 C++ API. They were
built in Release mode, while the o6 extension used the repository's
current debug configuration (`-O0 -g` with a Debug open62541 build). This puts
the native portion of o6 at a disadvantage relative to a release wheel.

Certificate generation, endpoint discovery, connection setup, session setup,
NodeId resolution, and warm-up are outside the timed region. The asyncua sync
rows use its public synchronous wrapper; its async rows use the native asyncio
API. The secure benchmark uses short-lived self-signed RSA certificates.

## Reproducing the benchmark

Install asyncua into the benchmark environment:

```sh
python3 -m pip install asyncua==2.0.1
```

Build the open62541 C benchmark programs included in this repository. Their
C sources are under `examples/benchmarks/open62541`; the build uses the
vendored open62541 source directly and supports both security profiles:

```sh
cmake -S examples/benchmarks/open62541 -B examples/benchmarks/open62541/build \
  -DCMAKE_BUILD_TYPE=Release
cmake --build examples/benchmarks/open62541/build -j
```

Run the complete matrix:

```sh
python3 examples/benchmarks/run_end_to_end.py \
  --clients 1,3,10 \
  --max-outstanding 32
```

The default runs both security profiles, both request modes, and all seven
pairings. Each pairing is a `<client>:<server>` token where the implementation
is one of `open62541`, `o6-python`, or `asyncua`. Select one (or several) with
`--pair open62541:open62541`, `--pair o6-python:open62541`,
`--pair open62541:o6-python`, `--pair o6-python:o6-python`,
`--pair asyncua:open62541`, `--pair open62541:asyncua`, or
`--pair asyncua:asyncua`. Multiple pairs can be passed as a comma-separated
list. Use `--security` and `--mode` to reduce the matrix.
