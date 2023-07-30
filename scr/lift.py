#!/usr/bin/env python3

import rospy
from applications.srv import lift_command

def Up_Down(request):
    if (request.estimated_floor < 4) and (request.estimated_floor > 0):
        answer = "Lifted up".format(request.floor)
        return answer

def send_answer():
    rospy.init_node("server_node")
    rospy.Service("estimated_floor", lift_command, Up_Down)
    rospy.spin()

send_answer()

