#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist


def movement():
    rospy.init_node("go_straight")
    pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
    speed_message = Twist()
    speed_message.linear.x = 0.5
    distance = 1.5
    change_place = 0
    t0 = rospy.Time.now().to_sec()
    
    while (change_place < distance):
        pub.publish(speed_message)
        t1 = rospy.Time.now().to_sec()
        change_place = speed_message.linear.x * (t1 - t0)
        
    speed_message.linear.x = 0.0
    pub.publish(speed_message)   
movement()
