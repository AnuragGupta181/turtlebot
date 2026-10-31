from glob import glob

from setuptools import setup

package_name = 'navturtle_bringup'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
        ('share/' + package_name + '/config', glob('config/*.yaml')),
        ('share/' + package_name + '/maps', glob('maps/*')),
        ('share/' + package_name + '/worlds', glob('worlds/*.world')),
        ('share/' + package_name + '/rviz', glob('rviz/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Anurag Gupta',
    maintainer_email='job4anurag11@gmail.com',
    description='TurtleBot3 autonomous navigation in Gazebo Classic with Nav2 (ROS 2 Humble).',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'patrol = navturtle_bringup.patrol:main',
        ],
    },
)
