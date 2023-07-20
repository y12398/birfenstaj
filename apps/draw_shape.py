#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
import random

def draw_shape(shape):
    rospy.init_node('turtle_shapes', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  

    vel_msg = Twist()

    

   
    if shape == 'square':
        for _ in range(4):
            rospy.sleep(0.5)
            vel_msg.linear.x = 3
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)
            rospy.sleep(1)

            vel_msg.linear.x = 0
            vel_msg.angular.z = 1.570796  
            velocity_publisher.publish(vel_msg)
            rospy.sleep(1)
    elif shape == 'circle':
        rospy.sleep(0.5)
        vel_msg.linear.x = 1
        vel_msg.angular.z = 0.523598  
        for _ in range(12):
            velocity_publisher.publish(vel_msg)
            rospy.sleep(1)

    elif shape == 'triangle':
        for _ in range(3):
            rospy.sleep(0.5)
            vel_msg.linear.x = 2
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)
            rospy.sleep(1)

            vel_msg.linear.x = 0
            vel_msg.angular.z = 2.094395   
            velocity_publisher.publish(vel_msg)
            rospy.sleep(1)
    
def change_background_color_client():


          rospy.wait_for_service('/clear')

          try: 

            rospy.set_param('/turtlesim/background_r', random.randint(0, 255))
            rospy.set_param('/turtlesim/background_g', random.randint(0, 255))
            rospy.set_param('/turtlesim/background_b', random.randint(0, 255))

            change_background_color = rospy.ServiceProxy('/clear', Empty)

            resp = change_background_color()

            return resp

          except rospy.ServiceException as e:   
           
           rospy.loginfo("error changing background color:", str(e))



if __name__ == '__main__':
    shape = input("type the shape (square/circle/triangle): ")
    draw_shape(shape)
    change_background_color_client()
