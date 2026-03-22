import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger
import psutil

class HealthServiceNode(Node):
    def __init__(self):
        super().__init__('health_service')
        
        # Create a service named /atlas/health
        self.srv = self.create_service(
            Trigger,            # service type
            '/atlas/health',    # service name
            self.health_callback  # function to run when called
        )
        self.get_logger().info('Atlas Health Service ready.')

    def health_callback(self, request, response):
        cpu = psutil.cpu_percent(interval=0.1)
        mem = psutil.virtual_memory().percent

        response.success = True
        response.message = f"CPU: {cpu}% | RAM: {mem}%"

        self.get_logger().info(f"Health check requested. {response.message}")
        return response

def main(args=None):
    rclpy.init(args=args)
    node = HealthServiceNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()