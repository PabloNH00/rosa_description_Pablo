from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    slam_toolbox_launch_dir = os.path.join(
        get_package_share_directory('slam_toolbox'), 'launch')
    
    default_mapper_params = os.path.join(
        './src/rosa_description_Pablo/config/mapper_params_online_async.yaml')
    
    pre_mapped_params = os.path.join(
        './src/rosa_description_Pablo/config/load_pre_mapped_params_online_async.yaml')

    return LaunchDescription([
        # Argument declaration
        DeclareLaunchArgument(
            'use_pre_mapped',
            default_value='false',
            description='Use pre-mapped parameters if true, else use SLAM parameters for mapping'
        ),

        # default SLAM launcher for mapping
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(slam_toolbox_launch_dir, 'online_async_launch.py')
            ),
            condition=UnlessCondition(LaunchConfiguration('use_pre_mapped')),
            launch_arguments={
                'use_sim_time': 'true',
                'slam_params_file': default_mapper_params
            }.items(),
        ),

        # premapped SLAM launcher for navigation
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(slam_toolbox_launch_dir, 'online_async_launch.py')
            ),
            condition=IfCondition(LaunchConfiguration('use_pre_mapped')),
            launch_arguments={
                'use_sim_time': 'true',
                'slam_params_file': pre_mapped_params
            }.items(),
        ),

        # Rviz2 config
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(
                get_package_share_directory('rosa_description'), 'rviz', 'slam_rviz_config.rviz')]
        )
    ])
