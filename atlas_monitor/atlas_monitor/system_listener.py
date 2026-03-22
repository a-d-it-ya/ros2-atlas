import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class SystemListenerNode(Node):
    def __init__(self):
        super().__init__('system_listener')
        
        self.cpu_sub = self.create_subscription(
            String,
            '/atlas/cpu',
            self.cpu_callback,
            10
        )
        self.mem_sub = self.create_subscription(
            String,
            '/atlas/memory',
            self.mem_callback,
            10
        )
        self.get_logger().info('Atlas Listener online.')

    def cpu_callback(self, msg):
        data = json.loads(msg.data)
        if data['percent'] > 80.0:
            self.get_logger().warn(f"HIGH CPU: {data['percent']}%")
        else:
            self.get_logger().info(f"CPU OK: {data['percent']}%")

    def mem_callback(self, msg):
        data = json.loads(msg.data)
        if data['percent'] > 80.0:
            self.get_logger().warn(f"HIGH MEM: {data['percent']}%")
        else:
            self.get_logger().info(f"MEM OK: {data['percent']}%")

def main(args=None):
    rclpy.init(args=args)
    node = SystemListenerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()