#!/usr/bin/env bash
# Rebuilds dist/study-mode.zip — the file you upload to Claude.ai (Settings → Capabilities → Skills).
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist
rm -f dist/study-mode.zip
(cd skills && zip -r -X ../dist/study-mode.zip study-mode)
echo "Built dist/study-mode.zip"
