from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    slam_toolbox_launch_dir = os.path.join(
        get_package_share_directory('slam_toolbox'), 'launch')
    nav2_bringup_launch_dir = os.path.join(
        get_package_share_directory('nav2_bringup'), 'launch')

    pre_mapped_params = os.path.join(
        './src/rosa_description_Pablo/config/load_pre_mapped_params_online_async.yaml')  
    nav2_params = os.path.join(
        './src/rosa_description_Pablo/config/nav2_params.yaml')

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'
        ),

        # premapped SLAM launcher for navigation
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(slam_toolbox_launch_dir, 'online_async_launch.py')
            ),
            launch_arguments={
                'use_sim_time': use_sim_time,
                'slam_params_file': pre_mapped_params
            }.items(),
        ),

        # Nav2 launcher for navigation
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(nav2_bringup_launch_dir, 'navigation_launch.py')
            ),
            launch_arguments={
                'use_sim_time': use_sim_time,
                'params_file': nav2_params
            }.items(),
        ),

        # Rviz2 config
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(
                get_package_share_directory('rosa_description'), 'rviz', 'nav2_rviz_config.rviz')]
        )
    ])
