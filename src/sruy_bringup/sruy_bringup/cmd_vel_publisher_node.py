#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class CmdVelPublisherNode(Node):

    def __init__(self):
        super().__init__("cmd_vel_publisher_node")

        self.publisher_ = self.create_publisher(
            Twist,
            "/cmd_vel",
            10
        )

        self.timer_ = self.create_timer(
            1.0,
            self.publish_cmd_vel
        )

        self.get_logger().info("Cmd Vel Publisher Node Started")

    def publish_cmd_vel(self):

        msg = Twist()

        msg.linear.x = 0.5
        msg.angular.z = 0.3

        self.publisher_.publish(msg)

        self.get_logger().info(
            f"Publishing cmd_vel | linear.x={msg.linear.x}, angular.z={msg.angular.z}"
        )


def main(args=None):

    rclpy.init(args=args)

    node = CmdVelPublisherNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
