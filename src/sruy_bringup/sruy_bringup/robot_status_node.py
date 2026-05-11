#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RobotStatusNode(Node):
    def __init__(self):
        super().__init__("robot_status_node")

        self.publisher_ = self.create_publisher(
            String,
            "/robot_status",
            10
        )

        self.timer_ = self.create_timer(1.0, self.publish_status)

        self.get_logger().info("Robot Status Node started.")

    def publish_status(self):
        msg = String()
        msg.data = "SRUY robot system is alive"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published: {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    node = RobotStatusNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
