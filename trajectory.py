#!/usr/bin/env python

import rospy
from visualization_msgs.msg import  Marker
from geometry_msgs.msg import Point
import math

rospy.init_node('points_and_lines', anonymous=True)
marker_pub = rospy.Publisher("pl_publisher", Marker, queue_size=10)
rate = rospy.Rate(30)
points = Marker()
line_strip = Marker()

######### POINT LIST ######
points_list = [0.0, 0.0, 0.59, -6.2,0.59, -6.2, 4.18, -13.46, 4.18, -13.46, 11.63, -16.85, 11.63, -16.85, 15.5, -11.18, 15.5, -11.18, 18.08, -5.9, 18.08, -5.9, 28.62, -6.17, 28.62, -6.17, 29.13, 0.0, 29.13, 0.0, 25.04, 4.36, 25.04, 4.36, 19.51, 7.88, 19.51, 7.88, 12.19, 8.73]
# x1 = 0.59
# y1 = -6.20

# x1 = 4.18
# y1 = -13.46

# x1 = 11.63
# y1 = -16.85

# x1 = 15.5
# y1 = -11.18

# x1 = 18.08
# y1 = -5.9

# x1 = 28.62
# y1 = -6.17

# x1 = 29.16
# y1 = 0.0

# x1 = 25.04
# y1 = 4.36

points.header.frame_id = line_strip.header.frame_id = 'map'
points.header.stamp = line_strip.header.stamp = rospy.Time.now()
points.ns = line_strip.ns = "points_and_lines"
points.action = line_strip.action = Marker.ADD
points.pose.orientation.w = line_strip.pose.orientation.w = 1.0

points.id = 0
line_strip.id = 1

points.type = Marker.POINTS
line_strip.type = Marker.LINE_LIST

# POINTS: x and y for width and height
points.scale.x = 0.2
points.scale.y = 0.2

# LINE_LIST: only x for width
line_strip.scale.x = 0.1

# Points are green
points.color.g = 1.0
points.color.a = 1.0

# Linestrip is blue
line_strip.color.b = 1.0
line_strip.color.a = 1.0

while not rospy.is_shutdown():
    for i in xrange(0,len(points_list),2):
        p = Point()
        p.x = points_list[i]
        p.y = points_list[i+1]

        points.points.append(p)
        line_strip.points.append(p)
        


    
    #marker_pub.publish(points)
    marker_pub.publish(line_strip)
    rate.sleep()


    


