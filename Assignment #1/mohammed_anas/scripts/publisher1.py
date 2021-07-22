#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher1():
	pub=rospy.Publisher('name_listener',String,queue_size=10)
	rospy.init_node('publisher1',anonymous=True)
	rospy.loginfo("Mohammed Anas")
	pub.publish("Mohammed Anas")

if __name__ =='__main__':
	try:
		publisher1()
	except:
		rospy.loginfo("error")
