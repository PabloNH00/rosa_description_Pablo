# README #

ROSA robot repository for the ROS2 Simulation package 

### How to run the simulation ###
    colcon build --symlink-install
    source install/local_setup.bash
    ros2 launch rosa_description rosa_gazebo_launch.py

### How to run the SLAM ###
To install slam-toolbox

    sudo apt install ros-humble-slam-toolbox

After launch gazebo launch SLAM for map the world:

    ros2 launch rosa_description slam_launch.py use_pre_mapped:=false

It will run "online_async_launch.py" from slam_toolbox and execute a pre-configured rviz2 with all necessary components. This launcher set by default the use_sim_time argument as "true", mandatory for SLAM in gazebo. 
This launcher also use substitution with "use_pre_mapped" argument, set by default to false, to launch SLAM with different .yaml configuration.

Start moving the robot publishing in /cmd_vel and save the map using the SLAM plug-in openned in rviz2 
* "serialize map" for serialized version (.data and .posegraph)

Once you have your map files modify "load_pre_mapped_params_online_async.yaml" and change "map_file_name" param with your path to the serialized files WITHOUT THE EXTENSION

    # will use pose
    map_file_name: /home/user/ros_ws/world_serialized
    # map_start_pose: [0.0, 0.0, 0.0]
    

For use your map for navigation run:

    ros2 launch rosa_description slam_launch.py use_pre_mapped:=true


* Repo owner or admin
* Other community or team contact
