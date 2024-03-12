#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def joystick_publisher():
    rospy.init_node('joystick_node', anonymous=True)
    pub = rospy.Publisher(String, que_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        pass

if __name__ == '__main__':
    try:
        joystick_publisher()
    except rospy.ROSInterruptException:
        pass