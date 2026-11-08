from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
import xacro

gazebo_config_path = '/home/zae/ros2_ws/src/my_robot_bringup/config/gazebo_bridge.yaml'
xacro_file = '/home/zae/ros2_ws/src/test_robot_package/urdf/my_robot.urdf.xacro'
robot_description = xacro.process_file(xacro_file).toxml()

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{
                "robot_description": robot_description}]
        ),

         Node(

            package = "ros_gz_sim",
            executable= "create",
            arguments= ["-topic", "robot_description"]

        ),

 Node(

            package = "ros_gz_bridge",
            executable= "parameter_bridge",
            parameters=[{
                "config_file": gazebo_config_path}]


        ),

                Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui",
        ),

         
        Node(
            package="rviz2",
            executable="rviz2",
            output="screen"
        ),



        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(['/opt/ros/jazzy/share/ros_gz_sim/launch/gz_sim.launch.py']),
       launch_arguments={'gz_args': '/home/zae/Downloads/tugbot_depot/tugbot_depot.sdf -r'}.items()  )
 
    ])
