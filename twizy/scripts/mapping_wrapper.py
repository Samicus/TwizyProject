#!/usr/bin/env python

import twizy.scripts.mapping
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Float64MultiArray


def __init__(self):
    self.GPS = None
    self.dist = None
    self.xs = []
    self.ys = []
    self.GPS_start = (0.0, 0.0, 0.0)

def callback_GPS(self, msg):
    # "Store" message received.
    self.GPS = msg.data
    # print(msg.data)

def callback_dist(self, msg):
    #"Store" the message received.
    dist = msg.data
    

def calculate(self):
    if self.dist is None:
        print('self.depth is None')
    if self.GPS is None:
        print('self.GPS is None')
    if self.dist is not None and self.GPS is not None:
        pass #TODO run code here?
    return None


# This is the method that decides if it should run on ROS
# message or the text-file
if __name__ == '__main__':
    rospy.init_node('pathplanner')
    pub = rospy.Publisher('aim_coords', String, queue_size=10)
    msg_to_publish = String()
    rate = rospy.Rate(1000)
    while not rospy.is_shutdown():
        rospy.Subscriber('dist_sensors', Float64MultiArray, callback_dist)
        rospy.Subscriber('GPS_pos', Float32MultiArray, callback_GPS)
        ret = pp.calculate()
        if not ret is None:
            # x,y = pp.calculate()
            msg_to_publish.data = str(ret)[1:len(str(ret)) - 1]
        else:
            msg_to_publish.data = 'stop'

        pub.publish(msg_to_publish)
        rate.sleep()
