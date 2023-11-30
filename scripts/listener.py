#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist, Vector3

class RobotController:
    def __init__(self):
        # Subscribe to the /robot1/cmd_vel topic to receive movement commands
        self.sub = rospy.Subscriber('gc_vel', Twist, self.cmd_vel_callback)
        # Also create a publisher for issuing movement commands
        self.pub = rospy.Publisher('gc_vel', Twist, queue_size=10)
        self.speed_x = 0.15
        self.has_moved = False  # Flag to check if the robot has already moved

    def cmd_vel_callback(self, msg):
        # Print received commands (or you can remove this if not needed)
        print('Received Motor Commands: {} Linear, {} Angular'.format(msg.linear.x, msg.angular.z))
        # Drive the robot forward based on the received message if it hasn't moved before
        if not self.has_moved:
            self.drive_forward(msg.linear.x)
            self.has_moved = True  # Set the flag to True after moving

    def drive_forward(self, speed_x):
        # Create a Twist message for forward movement
        twist = Twist()
        twist.linear = Vector3(speed_x, 0, 0)  # Set linear velocity (forward)
        twist.angular = Vector3(0, 0, 0)      # Set angular velocity to zero
        # Publish the forward movement command
        self.pub.publish(twist)
        print('Published Motor Commands: {} Linear, {} Angular'.format(speed_x, 0))

if __name__ == '__main__':
    rospy.init_node('gc_controller_node')
    controller = RobotController()
    # Keep the program alive
    rospy.spin()
