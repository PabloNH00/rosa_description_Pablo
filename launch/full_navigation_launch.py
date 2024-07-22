# import os

# from launch import LaunchDescription
# from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
# from launch.conditions import LaunchConfigurationEquals, LaunchConfigurationNotEquals
# from launch.substitutions import LaunchConfiguration
# from launch_ros.actions import Node
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from ament_index_python.packages import get_package_share_directory


# def generate_launch_description():
#     slam_toolbox_launch_dir = os.path.join(
#         get_package_share_directory('slam_toolbox'), 'launch')
#     nav2_toolbox_launch_dir = os.path.join(
#         get_package_share_directory('nav2_bringup'), 'launch')

#     # Paths to slam_param_files
#     default_mapper_params = os.path.join(
#         './src/rosa_description_Pablo/config/mapper_params_online_async.yaml')
#     pre_mapped_params = os.path.join(
#         './src/rosa_description_Pablo/config/load_pre_mapped_params_online_async.yaml')
    
#     # Path to nav2 params_file    
#     nav2_params = os.path.join(
#         'src/rosa_description_Pablo/config/nav2_params.yaml')

#     # Paths to RViz configuration files
#     default_rviz_config = os.path.join(
#         get_package_share_directory('rosa_description'), 'rviz', 'slam_rviz_config.rviz')
#     pre_mapped_rviz_config = os.path.join(
#         get_package_share_directory('rosa_description'), 'rviz', 'nav2_rviz_config.rviz')

#     ld = LaunchDescription()

#     # Argument declaration
#     use_sim_time = LaunchConfiguration('use_sim_time', default='false')
#     use_pre_mapped = LaunchConfiguration('use_pre_mapped')

#     ld.add_action(DeclareLaunchArgument(
#             'use_sim_time',
#             default_value='false',
#             description='Use simulation (Gazebo) clock if true'))
    
#     ld.add_action(DeclareLaunchArgument(
#         'use_pre_mapped',
#         default_value='false',
#         description='Use pre-mapped parameters for navigation if true, else use SLAM parameters for mapping'
#     ))

#     # Default SLAM launcher for mapping
#     ld.add_action(IncludeLaunchDescription(
#         PythonLaunchDescriptionSource(
#             os.path.join(slam_toolbox_launch_dir, 'online_async_launch.py')
#         ),
#         condition=LaunchConfigurationNotEquals('use_pre_mapped', 'true'),
#         launch_arguments={
#             'use_sim_time': use_sim_time,
#             'slam_params_file': default_mapper_params
#         }.items(),
#     ))

#     # Premapped SLAM launcher for navigation
#     ld.add_action(IncludeLaunchDescription(
#         PythonLaunchDescriptionSource(
#             os.path.join(slam_toolbox_launch_dir, 'online_async_launch.py')
#         ),
#         condition=LaunchConfigurationEquals('use_pre_mapped', 'true'),
#         launch_arguments={
#             'use_sim_time': use_sim_time,
#             'slam_params_file': pre_mapped_params
#         }.items(),
#     ))

#     # Nav2 launcher only if use_pre_mapped == True
#     navigation_launch_node = IncludeLaunchDescription(
#         PythonLaunchDescriptionSource(
#             os.path.join(nav2_toolbox_launch_dir, 'navigation_launch.py')
#         ),
#         condition=LaunchConfigurationEquals('use_pre_mapped', 'true'),
#         launch_arguments={
#             'use_sim_time': use_sim_time,
#             'params_file': nav2_params
#         }.items()
#     )
#     ld.add_action(navigation_launch_node)

#         # Rviz2 config
#     ld.add_action(Node(
#         condition=LaunchConfigurationEquals('use_pre_mapped', 'true'),
#         package='rviz2',
#         executable='rviz2',
#         name='rviz2',
#         output='screen',
#         arguments=['-d', os.path.join(
#                 get_package_share_directory('rosa_description'), 'rviz', pre_mapped_rviz_config)]
#     ))
#         # Rviz2 config
#     ld.add_action(Node(
#         condition=LaunchConfigurationNotEquals('use_pre_mapped', 'true'),
#         package='rviz2',
#         executable='rviz2',
#         name='rviz2',
#         output='screen',
#         arguments=['-d', os.path.join(
#                 get_package_share_directory('rosa_description'), 'rviz', default_rviz_config)]
#     ))

#     return ld
