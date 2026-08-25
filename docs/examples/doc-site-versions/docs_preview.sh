#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-serve}"
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/../../.." && pwd)"
SRC_CFG="$SCRIPT_DIR/zensical.preview.toml"
TMP_CFG="$REPO_ROOT/.zensical.preview.generated.toml"

# Render config from repo root so docs_dir defaults to "$REPO_ROOT/docs".
grep -v '^docs_dir\s*=' "$SRC_CFG" > "$TMP_CFG"

cleanup() {
  rm -f "$TMP_CFG"
}
trap cleanup EXIT

cd "$REPO_ROOT"

if [[ "$MODE" == "serve" ]]; then
  zensical serve -f "$TMP_CFG"
elif [[ "$MODE" == "build" ]]; then
  zensical build -f "$TMP_CFG" --clean
else
  echo "Usage: docs/examples/doc-site-versions/docs_preview.sh [serve|build]" >&2
  exit 1
fi
