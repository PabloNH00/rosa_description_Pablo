# README #

ROSA robot repository for the ROS2 Simulation package 

### How to run the simulation ###
    colcon build --symlink-install
    source install/local_setup.bash
    ros2 launch rosa_description rosa_gazebo_launch.py

### How to run the SLAM ###
To install slam-toolbox

    sudo apt install ros-humble-slam-toolbox

After launch gazebo:

    ros2 launch rosa_description slam_launch.py

It will run "online_async_launch.py" from slam_toolbox and execute a pre-configured rviz2 with all necessary components. This launcher set by default the use_sim_time param as "true", mandatory for SLAM in gazebo

Start moving the robot publishing in /cmd_vel and save the map using the SLAM plug-in openned in rviz2 
* "save map" for .pgm  and .yaml
* "serialize map" for serialized version (.data and .posegraph)


* Repo owner or admin
* Other community or team contact
