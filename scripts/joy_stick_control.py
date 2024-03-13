#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from joystick_control.msg import Comamnd
import pygame


def joystick_publisher():
    rospy.init_node('joystick_node', anonymous=True)
    pub = rospy.Publisher('command', Position, que_size=10)
    rate = rospy.Rate(10)

    # Initialize pygame
    pygame.init()
    pygame.joystick.init()

    # Check for connected joysticks
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("No joystick detected.")
        quit()

    # Initialize the joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()


    while not rospy.is_shutdown():
        msg = Command()

        msg.axis1 = joystick.get_axis(1)
        msg.axis2 = joystick.get_axis(2)
        msg.axis3 = joystick.get_axis(3)
        msg.axis4 = joystick.get_axis(4)
        
        msg.b0 = joystick.get_button(0)
        msg.b1 = joystick.get_button(1)
        msg.b2 = joystick.get_button(2)
        msg.b3 = joystick.get_button(3)
        msg.b4 = joystick.get_button(4)
        msg.b5 = joystick.get_button(5)
        msg.b6 = joystick.get_button(6)
        msg.b7 = joystick.get_button(7)
        msg.b8 = joystick.get_button(8)
        msg.b9 = joystick.get_button(9)
        msg.b10 = joystick.get_button(10)
        msg.b11 = joystick.get_button(11)
        
        pub.publish()

        rate.sleep()

if __name__ == '__main__':
    try:
        joystick_publisher()
    except rospy.ROSInterruptException:
        pass