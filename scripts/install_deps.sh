#!/usr/bin/env bash
# Install everything needed to run TurtleBot3 + Nav2 in Gazebo Classic on ROS 2 Humble.
#
# What it does:
#   1. Removes the legacy duplicate ROS apt source (ros2.list) if the official
#      ros2-apt-source package (ros2.sources) is already installed. Having both
#      breaks apt with a "Conflicting values set for option Signed-By" error.
#   2. Updates the apt index.
#   3. Installs Nav2, TurtleBot3, and Gazebo Classic ROS packages.
#
# Note: on Ubuntu 22.04, Gazebo Classic (gazebo11) conflicts with Gazebo Harmonic
# (gz-harmonic). apt will ask before removing Harmonic. Reinstall it later with:
#   sudo apt install gz-harmonic
set -euo pipefail

if [[ -f /etc/apt/sources.list.d/ros2.sources && -f /etc/apt/sources.list.d/ros2.list ]]; then
  echo "[install] Removing duplicate ROS source /etc/apt/sources.list.d/ros2.list (backup in /etc/apt/ros2.list.bak)"
  sudo mv /etc/apt/sources.list.d/ros2.list /etc/apt/ros2.list.bak
fi

echo "[install] Updating apt index"
sudo apt-get update

PACKAGES=(
  ros-humble-navigation2            # Nav2 stack: planner, controller, AMCL, costmaps
  ros-humble-nav2-bringup           # Nav2 launch files, params, maps, RViz config
  ros-humble-nav2-simple-commander  # Python API to send goals and waypoints
  ros-humble-turtlebot3             # TurtleBot3 description, bringup, navigation2 configs
  ros-humble-turtlebot3-simulations # TurtleBot3 Gazebo worlds and models
  ros-humble-gazebo-ros-pkgs        # Gazebo Classic 11 + ROS 2 integration
)

# apt does not auto-remove conflicting packages in a multi-package install, so remove
# gz-tools2 (Harmonic CLI, conflicts with gazebo11) explicitly. The trailing "-" means remove.
# This also removes the rest of gz-harmonic.
CONFLICTS=()
if dpkg -s gz-tools2 >/dev/null 2>&1; then
  CONFLICTS+=(gz-tools2-)
fi

echo "[install] Installing: ${PACKAGES[*]} ${CONFLICTS[*]}"
sudo apt-get install "${PACKAGES[@]}" "${CONFLICTS[@]}"

echo "[install] Done. Next: source scripts/env.sh && scripts/smoke_test.sh"
