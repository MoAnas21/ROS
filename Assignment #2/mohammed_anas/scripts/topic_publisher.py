#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

global scanF,scanM,scanL,tempscanF,tempscanL
scanF=None
scanM=None
scanL=None
tempscanF=None
tempscanL=None

def callback(scandata):
	global scanF,scanM,scanL
	scandata.range_max=5
	scandata.range_min=0
	scandata.time_increment=(1/10)/640
	scanF=scandata.ranges[0]
	scanM=scandata.ranges[319]
	scanL=scandata.ranges[639]

def publisher():
	rospy.init_node('moveturtlebot')
	pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=1)
	rate = rospy.Rate(10)
	move = Twist()
	global scanF,scanM,scanL,tempscanF,tempscanL


	while not rospy.is_shutdown():
		
		rospy.Subscriber('/scan',LaserScan,callback)

		if (scanM<1 or scanL<1) and scanL<tempscanL and scanL>=0:

			if scanL>1:
				move.linear.x=0.25
			else:
				move.linear.x=0
			move.angular.z=-2


		elif (scanM<1 or scanF<1) and scanF<tempscanF:
			
			if scanF>1:		
				move.linear.x=0.25
			else:
				move.linear.x=0
			move.angular.z=2

		else:
			move.linear.x=0.5
			move.angular.z=0


		tempscanL=scanL
		tempscanF=scanF
		pub.publish(move)
		rate.sleep()


if __name__=='__main__':
	publisher()
	
