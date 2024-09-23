# LAUNCH FOLDER

This folder contains all the ROS2 launchers created for ROSA robot. Most of them can be executed with differents arguments depending on the objective and they will launch processes on different ways to simulate on Gazebo or run the real robot. 

## rosa_gazebo_launch.py

Launches Gazebo program with the ROS2 parameter "use_sim_time" set to true. This launcher execute "spawn_entity.py", run the "robot_state_publisher" and load the URDF model from "/description/rosa".

Gazebo opens with preloaded URDF a world, which correspond to "/worlds/pal_office.world"

![rosa_gazebo_launch.py](images/rosa_gazebo_launch.png)

## rosa_urdf_launch.py

Load URDF model to work with ROS2 using real ROSA. Set "use_sim_time" param to false and run "robot_state_publisher" with "/description/rosa" xacro model.