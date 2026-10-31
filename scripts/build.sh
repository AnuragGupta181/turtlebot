#!/usr/bin/env bash
# Build the workspace from the repo root.
set -eo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."
source scripts/env.sh

colcon build --symlink-install
