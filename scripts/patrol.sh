#!/usr/bin/env bash
# Send the robot through the waypoint route. Run in a second terminal after run_sim.sh.
# Add --loop to repeat the route until Ctrl+C.
set -eo pipefail

source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

ros2 run navturtle_bringup patrol "$@"
