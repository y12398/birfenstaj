# birfenstaj
# Turtlebot3 Map and Navigation
We start the terminal. On the first screen, we start the gazebo by typing the command;
'roslaunch turtlebot3_gazebo turtlebot3_house.launch'
On the second screen, we run Rviz by entering the command;
'roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping'
On the third screen, we enter the command to move the robot in Rviz;
'rosrun turtlebot3_teleop turtlebot3_teleop_key to start the teleop'
We create a map in Rviz by visiting the whole House with w(forward),a(right),s(stop),d(left),x(back).
On the fourth screen we save the map we created by typing;
'rosrun map_server map_saver -f ~/tb3_house_map' 
Then we close the terminals and Gazebo and Rviz. 
Again, we start the gazebo environment by typing;
'turtlebot3_gazebo turtlebot3_house.launch'
Then we open the map we saved in Rviz by typing;
'roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/home/yeknur/tb3_house_map.yaml'
By synchronizing Turtlebot's position in the gazebo and Rviz, we can direct the robot to any part of the map by using the 2D nav goal bar.
