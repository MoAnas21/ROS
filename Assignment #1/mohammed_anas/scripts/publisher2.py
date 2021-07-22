#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher2():
	pub=rospy.Publisher('num_listener',String,queue_size=10)
	rospy.init_node('publisher2',anonymous=True)
	rospy.loginfo("9567833299")
	pub.publish("9567833299")

if __name__ =='__main__':
	try:
		publisher2()
	except:
		rospy.loginfo("error")
