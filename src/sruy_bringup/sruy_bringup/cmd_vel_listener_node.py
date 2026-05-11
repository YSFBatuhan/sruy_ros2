#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class CmdVelListenerNode(Node):

    def __init__(self):
        super().__init__("cmd_vel_listener_node")

        self.subscription = self.create_subscription(
            Twist,
            "/cmd_vel",
            self.cmd_vel_callback,
            10
        )

        self.get_logger().info("Cmd Vel Listener Node Started")

    def cmd_vel_callback(self, msg):

        linear_speed = msg.linear.x
        angular_speed = msg.angular.z

        self.get_logger().info(
            f"Received cmd_vel -> linear.x: {linear_speed}, angular.z: {angular_speed}"
        )


def main(args=None):

    rclpy.init(args=args)

    node = CmdVelListenerNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
