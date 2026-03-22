import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import psutil
import json

class SystemMonitorNode(Node):
    def __init__(self):
        super().__init__('system_monitor')

        # Declare parameters with default values
        self.declare_parameter('publish_rate', 1.0)
        self.declare_parameter('cpu_threshold', 80.0)

        # Read parameter values
        rate = self.get_parameter('publish_rate').value
        self.cpu_threshold = self.get_parameter('cpu_threshold').value

        self.cpu_pub = self.create_publisher(String, '/atlas/cpu', 10)
        self.mem_pub = self.create_publisher(String, '/atlas/memory', 10)

        self.timer = self.create_timer(rate, self.publish_stats)
        self.get_logger().info(f'Atlas System Monitor online. Rate: {rate}s | CPU threshold: {self.cpu_threshold}%')

    def publish_stats(self):
        # Re-read threshold in case it was changed at runtime
        self.cpu_threshold = self.get_parameter('cpu_threshold').value

        cpu = {
            'percent': psutil.cpu_percent(interval=None),
            'cores': psutil.cpu_count()
        }
        cpu_msg = String()
        cpu_msg.data = json.dumps(cpu)
        self.cpu_pub.publish(cpu_msg)

        mem = psutil.virtual_memory()
        memory = {
            'total_mb': round(mem.total / 1e6, 1),
            'used_mb': round(mem.used / 1e6, 1),
            'percent': mem.percent
        }
        mem_msg = String()
        mem_msg.data = json.dumps(memory)
        self.mem_pub.publish(mem_msg)

        # Alert if CPU crosses threshold
        if cpu['percent'] > self.cpu_threshold:
            self.get_logger().warn(f"HIGH CPU: {cpu['percent']}% > {self.cpu_threshold}%")
        else:
            self.get_logger().info(f"CPU: {cpu['percent']}% | RAM: {memory['percent']}%")

def main(args=None):
    rclpy.init(args=args)
    node = SystemMonitorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()