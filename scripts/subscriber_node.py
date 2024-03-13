#!/usr/bin/env

import rospy
from joystick_control.msg import Comamnd


def callbac(data):
    rospy.loginfo('RECEIVED DATA: a1: %f a2: %f' ,data.axis1, data.axis2)

def listener():
    rospy.init_node("Subscriber_Node", anonymous = True)
    rospy.Subscriber('command', Command, callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass