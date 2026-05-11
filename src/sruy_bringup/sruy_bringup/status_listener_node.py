#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class StatusListenerNode(Node):

    def __init__(self):
        super().__init__("status_listener_node")

        self.subscription = self.create_subscription(
            String,
            "/robot_status",
            self.listener_callback,
            10
        )

        self.get_logger().info("Status Listener Node started.")

    def listener_callback(self, msg):
        self.get_logger().info(f"Received: {msg.data}")


def main(args=None):
    rclpy.init(args=args)

    node = StatusListenerNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
