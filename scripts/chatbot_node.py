#!/usr/bin/env python
# Homework 3 - "Smart Vehicle Club Chatbot"
# - Ben Grudzien

import rospy
from std_msgs.msg import String
from dialogflow_ros.msg import DialogflowResult
from dialogflow_ros.msg import DialogflowParameter
from dialogflow_ros.msg import DialogflowContext
from geometry_msgs.msg import Twist
from GemControl import *

pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
gem = GemControl()  # Instance of GemControl object
move_state = ""  # Initialize movement state of GEM


def move_gem(data):

    global move_state  # To allow access to state in "pub_gem_cmd"

    if data.intent == 'move_gem':  # If "Intent" true
        print data.parameters[0].value[0]  # First param because only 1 param

        if 'Forward' in data.parameters[0].value[0]:  # if "Entity" then set move_state
            move_state = 'Forward'
        elif 'Reverse' in data.parameters[0].value[0]:
            move_state = 'Reverse'
        elif 'Right' in data.parameters[0].value[0]:
            move_state = 'Right'
        elif 'Left' in data.parameters[0].value[0]:
            move_state = 'Left'
        elif 'Fast' in data.parameters[0].value[0]:
            move_state = 'Fast'
        elif 'stop' in data.parameters[0].value[0]:
            move_state = 'Stop'
        elif 'Flip' in data.parameters[0].value[0]:
            move_state = 'Flip'


def pub_gem_cmd(event):  # The point of this function is so Twist message is constantly published
    if move_state == 'Flip':
        pub.publish(gem.flip())
    elif move_state == 'Left':
        pub.publish(gem.left())
    elif move_state == 'Right':
        pub.publish(gem.right())
    elif move_state == 'Forward':
        pub.publish(gem.forward())
    elif move_state == 'Reverse':
        pub.publish(gem.reverse())
    elif move_state == 'Stop':
        pub.publish(gem.stop())
    elif move_state == 'Fast':
        pub.publish(gem.fast())


def listener():
    rospy.init_node("GemChatbot", anonymous=True)
    rospy.Subscriber('/dialogflow_client/results', DialogflowResult, move_gem)  # Subscribing to chatbot output
    rospy.Timer(rospy.Duration(0.1), pub_gem_cmd)  # Publish Twist every 0.1 second
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

