#!/usr/bin/env python
# This object stores functions that set different "move states" of the GEM vehicle

from geometry_msgs.msg import Twist


class GemControl:
    def __init__(self):  # Constructor
        return

    def flip(self):
        gem_twist_msg = Twist()
        gem_twist_msg.linear.x = 5
        gem_twist_msg.angular.z = 4
        return gem_twist_msg

    def fast(self):
        gem_twist_msg = Twist()
        gem_twist_msg.linear.x = 10
        gem_twist_msg.angular.z = 0
        return gem_twist_msg

    def left(self):
        gem_twist_msg = Twist()
        gem_twist_msg.linear.x = 2
        gem_twist_msg.angular.z = 0.1
        return gem_twist_msg

    def right(self):
        gem_twist_msg = Twist()
        gem_twist_msg.linear.x = 2
        gem_twist_msg.angular.z = -0.1
        return gem_twist_msg

    def stop(self):
        gem_twist_msg = Twist()
        gem_twist_msg.linear.x = 0
        gem_twist_msg.angular.z = 0
        return gem_twist_msg

    def forward(self):
        gem_twist_msg = Twist()
        gem_twist_msg.linear.x = 2
        gem_twist_msg.angular.z = 0.0
        return gem_twist_msg

    def reverse(self):
        gem_twist_msg = Twist()
        gem_twist_msg.linear.x = -2
        gem_twist_msg.angular.z = 0.0
        return gem_twist_msg




