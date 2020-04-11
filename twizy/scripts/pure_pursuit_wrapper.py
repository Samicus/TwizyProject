#!/usr/bin/env python
from twizy.scripts.src import pure_pursuit
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from twizy.msg import car_control
from matplotlib import pyplot as plt
import numpy as np
import math

# Parameters
k = 0.1  # look forward gain
Lfc = 0.3  # [m] look-ahead distance
Kp = 2  # speed proportional gain
dt = 0.1  # [s] time tick
WB = 1.63  # [m] wheel base of vehicle


def shutdown_hook():
    print('Goal reached!')


def ros_plot(state, states, target_ind):
    plt.cla()
    pure_pursuit.plot_arrow(state.x, state.y, state.yaw)
    plt.plot(path.cx, path.cy, "-r", label="course")
    plt.plot(states.x, states.y, "-b", label="trajectory")
    plt.plot(path.cx[target_ind], path.cy[target_ind], "xg", label="target")
    plt.axis("equal")
    plt.grid(True)
    plt.title("Speed[km/h]:" + str(state.v * 3.6)[:4])
    plt.pause(0.001)


def GPS_callback(msg):
    if path.is_path_generated():
        GPS = msg.data

        target_speed = -2 / 3.6  # [m/s]
        time = 0.0

        # initial state
        state = pure_pursuit.State(GPS[0], GPS[1], GPS[2], v=0.0)  # yaw+3.14?
        lastIndex = len(path.cx) - 1
        target_ind, _ = path.search_target_index(state)

        states = pure_pursuit.States()
        states.append(time, state)

        while lastIndex > target_ind:

            # Calc control input
            ai = pure_pursuit.proportional_control(target_speed, state.v)
            di, target_ind = pure_pursuit.pure_pursuit_steer_control(
                state, path, target_ind)
            state.update_from_gps(GPS,ai)

            if di < -40:
                angle = -40
            elif di > 40:
                angle = 40
            else:
                angle = di
            msg_to_publish.angle = angle
            msg_to_publish.speed = state.v
            pub.publish(msg_to_publish)

            if lastIndex <= target_ind:
                ros_plot(state, states, target_ind)
                rospy.on_shutdown(shutdown_hook())


def path_callback(msg): # fix when mapping is done
    a = 0.8960  # msg.data[0]
    b = 0.6765  # msg.data[1]
    c = 0  # msg.data[2]
    path.path_generated = 1  # msg.data[3]
    if path.is_path_generated():
        path.set_path(a, b, c)


if __name__ == '__main__':

    rospy.init_node('pure_pursuit')
    pub = rospy.Publisher('controls', car_control, queue_size=5)
    msg_to_publish = car_control
    rate = rospy.Rate(1000)  # Adjust rate?

    path = pure_pursuit.TargetCourse()

    while not rospy.is_shutdown():
        rospy.Subscriber('GPS_pos', Float32MultiArray, GPS_callback)
        rospy.Subscriber('path_planner', Float32MultiArray, path_callback)
        rate.sleep()