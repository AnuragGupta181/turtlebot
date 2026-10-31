#!/usr/bin/env bash
# Start Gazebo, TurtleBot3, Nav2, and RViz. Extra args are passed to the launch file,
# for example:  scripts/run_sim.sh gui:=false
set -eo pipefail

source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

# Clean up any old Gazebo processes that block a new launch
pkill -x gzserver || true
pkill -x gzclient || true

ros2 launch navturtle_bringup sim_nav.launch.py "$@"
