#!/usr/bin/env python

import rospy
from std_msgs.msg import String

global name,num,nameflag,numflag
name=None
num=None
nameflag=0
numflag=0

def callbackname(data):
	global name 
	name=data.data
	global nameflag
	nameflag=1


def callbacknum(data):
	global num
	num=data.data
	global numflag
	numflag=1
	

def listener():
	rospy.init_node('subscriber',anonymous=True)
	rospy.Subscriber('name_listener',String,callbackname)
	rospy.Subscriber('num_listener',String,callbacknum)
	rate=rospy.Rate(10)
	while not rospy.is_shutdown():
		if nameflag==1 and numflag==1:
			rospy.loginfo("If you want to contact %s, then call %s", name, num)
			break
		rate.sleep()
	rospy.spin()

if __name__ =='__main__':
		listener()

