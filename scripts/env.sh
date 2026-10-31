# Source this file in every new terminal:  source scripts/env.sh
# It sets up ROS 2 Humble, the TurtleBot3 model, Gazebo Classic, and the local overlay.
# Other ROS workspaces already sourced in the shell (for example from ~/.bashrc) are
# dropped first, so only /opt/ros/humble and this repo are on the paths.

_repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Keep only path entries that do not belong to some other colcon workspace (*/install/*).
_keep_clean_paths() {
  local IFS=':' out=() entry
  for entry in $1; do
    [[ -z "${entry}" ]] && continue
    if [[ "${entry}" == */install/* && "${entry}" != "${_repo_root}/install/"* ]]; then
      continue
    fi
    out+=("${entry}")
  done
  (IFS=':'; echo "${out[*]}")
}

unset AMENT_PREFIX_PATH CMAKE_PREFIX_PATH COLCON_PREFIX_PATH ROS_PACKAGE_PATH
export PYTHONPATH="$(_keep_clean_paths "${PYTHONPATH:-}")"
export LD_LIBRARY_PATH="$(_keep_clean_paths "${LD_LIBRARY_PATH:-}")"
export PATH="$(_keep_clean_paths "${PATH}")"
unset -f _keep_clean_paths

source /opt/ros/humble/setup.bash

export TURTLEBOT3_MODEL=burger

# Gazebo Classic environment (model and resource paths)
if [[ -f /usr/share/gazebo/setup.sh ]]; then
  source /usr/share/gazebo/setup.sh
fi

# Local workspace overlay, if it has been built
if [[ -f "${_repo_root}/install/setup.bash" ]]; then
  source "${_repo_root}/install/setup.bash"
fi
unset _repo_root

echo "[env] ROS_DISTRO=${ROS_DISTRO} TURTLEBOT3_MODEL=${TURTLEBOT3_MODEL}"
