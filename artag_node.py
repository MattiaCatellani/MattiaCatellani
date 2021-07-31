#!/usr/bin/env python
import rospy
import ar_track_alvar
from ar_track_alvar_msgs.msg import AlvarMarker
from ar_track_alvar_msgs.msg import AlvarMarkers

def callback(data):
    print("LANDMARK IDENTIFIED!")
    for i in range(0,len(data.markers)):
        num = data.markers[i].id
        x = data.markers[i].pose.pose.position.x
        y = data.markers[i].pose.pose.position.y
        z = data.markers[i].pose.pose.position.z

        print("ID = %i" % num)
        print("x = %f" % x)
        print("y = %f" % y)
        print("z = %f" % z)




    # for i in range(0,len(tag_list)):
    #     x = tag_list.markers[i].pose.pose.position.x
    #     y = tag_list.markers[i].pose.pose.position.y
    #     z = tag_list.markers[i].pose.pose.position.z

    #     # print coords
    #     print("Coordinates:")
    #     print("x = ", x)
    #     print("y = ", y)
    #     print("z = ", z) 

    
def listener():

    rospy.init_node('artag_listener', anonymous=True)

    rospy.Subscriber("ar_pose_marker", AlvarMarkers, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()