"""Start Gazebo Classic, TurtleBot3, Nav2, and RViz with one command.

Everything here is composed from upstream launch files:
  - gazebo_ros:        gzserver / gzclient
  - turtlebot3_gazebo: robot_state_publisher + robot spawn (reads TURTLEBOT3_MODEL)
  - nav2_bringup:      map server, AMCL, planner, controller, behaviors, BT navigator, RViz
Only the world, map, Nav2 params, and RViz config come from this package.
"""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    pkg_share = get_package_share_directory('navturtle_bringup')
    gazebo_ros_launch = os.path.join(get_package_share_directory('gazebo_ros'), 'launch')
    tb3_gazebo_launch = os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch')
    nav2_launch = os.path.join(get_package_share_directory('nav2_bringup'), 'launch')

    world = LaunchConfiguration('world')
    map_yaml = LaunchConfiguration('map')
    params_file = LaunchConfiguration('params_file')
    rviz_config = LaunchConfiguration('rviz_config')
    x_pose = LaunchConfiguration('x_pose')
    y_pose = LaunchConfiguration('y_pose')
    gui = LaunchConfiguration('gui')
    use_rviz = LaunchConfiguration('use_rviz')
    use_sim_time = 'true'

    declare_args = [
        DeclareLaunchArgument(
            'world', default_value=os.path.join(pkg_share, 'worlds', 'obstacles.world'),
            description='Gazebo world file'),
        DeclareLaunchArgument(
            'map', default_value=os.path.join(pkg_share, 'maps', 'turtlebot3_world.yaml'),
            description='Map yaml used by map_server and AMCL'),
        DeclareLaunchArgument(
            'params_file', default_value=os.path.join(pkg_share, 'config', 'nav2_params.yaml'),
            description='Nav2 parameters file'),
        DeclareLaunchArgument(
            'rviz_config', default_value=os.path.join(pkg_share, 'rviz', 'navturtle.rviz'),
            description='RViz config file'),
        # Must match amcl.initial_pose in nav2_params.yaml
        DeclareLaunchArgument('x_pose', default_value='-2.0', description='Spawn x [m]'),
        DeclareLaunchArgument('y_pose', default_value='-0.5', description='Spawn y [m]'),
        DeclareLaunchArgument('gui', default_value='true', description='Start the Gazebo GUI'),
        DeclareLaunchArgument('use_rviz', default_value='true', description='Start RViz'),
    ]

    gzserver = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(gazebo_ros_launch, 'gzserver.launch.py')),
        launch_arguments={'world': world}.items(),
    )

    gzclient = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(gazebo_ros_launch, 'gzclient.launch.py')),
        condition=IfCondition(gui),
    )

    robot_state_publisher = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(tb3_gazebo_launch, 'robot_state_publisher.launch.py')),
        launch_arguments={'use_sim_time': use_sim_time}.items(),
    )

    spawn_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(tb3_gazebo_launch, 'spawn_turtlebot3.launch.py')),
        launch_arguments={'x_pose': x_pose, 'y_pose': y_pose}.items(),
    )

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(nav2_launch, 'bringup_launch.py')),
        launch_arguments={
            'map': map_yaml,
            'params_file': params_file,
            'use_sim_time': use_sim_time,
            'autostart': 'true',
        }.items(),
    )

    rviz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(nav2_launch, 'rviz_launch.py')),
        launch_arguments={'rviz_config': rviz_config}.items(),
        condition=IfCondition(use_rviz),
    )

    return LaunchDescription(
        declare_args + [gzserver, gzclient, robot_state_publisher, spawn_robot, nav2, rviz]
    )
