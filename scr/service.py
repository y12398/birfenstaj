#!/usr/bin/env python3

import rospy
from apps.srv import lift_command


def request(x):
    rospy.wait_for_service("estimated_floor")
    try:
        service = rospy.ServiceProxy("estimated_floor", lift_command)
        answer = servis(x)
        return answer.deleted
        
    except rospy.ServiceException:
        print("error!")
    
goal = float(input("estimated floor: "))
t = request(goal)
print(t)
