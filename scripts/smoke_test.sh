#!/usr/bin/env bash
# Run the stock Nav2 TurtleBot3 demo with no custom code.
# Opens Gazebo (GUI), RViz, and the full Nav2 stack on the default turtlebot3_world map.
# If this works, the system is ready for our own bringup package.
set -eo pipefail

source "$(dirname "${BASH_SOURCE[0]}")/env.sh"

# Clean up any old Gazebo processes that block a new launch
pkill -x gzserver || true
pkill -x gzclient || true

ros2 launch nav2_bringup tb3_simulation_launch.py headless:=False
