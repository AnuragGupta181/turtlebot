"""Send the robot through a list of waypoints using the Nav2 Simple Commander API.

Run after sim_nav.launch.py is up:
    ros2 run navturtle_bringup patrol
    ros2 run navturtle_bringup patrol --loop      # repeat until Ctrl+C

Nav2 does all planning and obstacle avoidance. This node only sends goals one by one
and prints progress.
"""

import argparse
import math

import rclpy
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult

# Spawn pose (x [m], y [m], yaw [deg]) in the map frame.
START_POSE = (-2.0, -0.5, 0.0)

# (x [m], y [m], yaw [deg]) in the map frame. Picked from free space in
# maps/turtlebot3_world.pgm, with routes that pass the extra obstacles in obstacles.world.
WAYPOINTS = [
    (-1.2, 1.8, 0.0),     # north west
    (1.2, 1.8, -45.0),    # north east, passes obstacle_box_1
    (1.2, -1.8, 180.0),   # south east, passes obstacle_box_2
    (-1.2, -1.8, 135.0),  # south west, passes obstacle_cylinder_1
    (-2.0, -0.5, 0.0),    # back to start
]


def make_pose(navigator: BasicNavigator, x: float, y: float, yaw_deg: float) -> PoseStamped:
    yaw = math.radians(yaw_deg)
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = navigator.get_clock().now().to_msg()
    pose.pose.position.x = x
    pose.pose.position.y = y
    pose.pose.orientation.z = math.sin(yaw / 2.0)
    pose.pose.orientation.w = math.cos(yaw / 2.0)
    return pose


def run_once(navigator: BasicNavigator) -> bool:
    """Visit every waypoint in order. Returns False if a goal fails."""
    for index, (x, y, yaw) in enumerate(WAYPOINTS, start=1):
        navigator.info(f'Goal {index}/{len(WAYPOINTS)}: x={x:.2f} y={y:.2f} yaw={yaw:.0f}')
        navigator.goToPose(make_pose(navigator, x, y, yaw))

        tick = 0
        while not navigator.isTaskComplete():
            tick += 1
            feedback = navigator.getFeedback()
            if feedback and tick % 20 == 0:
                navigator.info(f'  distance remaining: {feedback.distance_remaining:.2f} m')

        result = navigator.getResult()
        if result == TaskResult.SUCCEEDED:
            navigator.info(f'Goal {index} reached')
        else:
            navigator.error(f'Goal {index} finished with result: {result}')
            return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description='Patrol TurtleBot3 through fixed waypoints.')
    parser.add_argument('--loop', action='store_true', help='repeat the route until Ctrl+C')
    args, ros_args = parser.parse_known_args()

    rclpy.init(args=ros_args)
    navigator = BasicNavigator()

    # waitUntilNav2Active() publishes navigator.initial_pose before it checks /amcl_pose.
    # Its default is (0, 0), which would break localization, so set the real spawn pose
    # first. It matches amcl.initial_pose in nav2_params.yaml and x_pose/y_pose in the launch.
    navigator.setInitialPose(make_pose(navigator, *START_POSE))
    navigator.waitUntilNav2Active()

    try:
        while True:
            ok = run_once(navigator)
            if not args.loop or not ok:
                break
    except KeyboardInterrupt:
        navigator.cancelTask()
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
