# README #

ROSA robot repository for the ROS2 Simulation package 

### How to run the simulation ###
    colcon build --symlink-install
    source install/local_setup.bash
    ros2 launch rosa_description rosa_gazebo_launch.py

### How to run the SLAM ###
To install slam-toolbox

    sudo apt install ros-humble-slam-toolbox

To install nav2

    sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup
    sudo apt install ros-humble-turtlebot3*

After launch gazebo launch SLAM for map the world:

    ros2 launch rosa_description amcl_launch.py use_sim_time:=true slam:=True

It will run "bringup_launch.py" from nav2 stack and pass the parameter slam to launch "online_async_launch.py" from slam_toolbox, it will also execute a pre-configured rviz2 with all necessary components. This launcher set by default the use_sim_time argument as "false", it should be true for SLAM in gazebo. 


Start moving the robot publishing in /cmd_vel or using goal pose and save the map using the SLAM plug-in openned in rviz2 
* "save map" for .pgm and .yaml (necessary for navigation)
* "serialize map" for serialized version (.data and .posegraph)

Once you have your map files modify "nav2_params.yaml" and change "yaml_filename" param with your path to the map file

    map_server:
        ros__parameters:
            use_sim_time: True
            # Overridden in launch by the "map" launch configuration or provided default value.
            # To use in yaml, remove the default "map" value in the tb3_simulation_launch.py file & provide full path to map below.
            yaml_filename: "/home/pablonh-ubuntu/tfg_ROSA_ws/gaz_world"
    

For use your map for navigation run:

    ros2 launch rosa_description amcl_launch.py 

It will launch navigation with amcl. To start navigating set the initial pose in the openned rviz first.


* Repo owner or admin
* Other community or team contact
