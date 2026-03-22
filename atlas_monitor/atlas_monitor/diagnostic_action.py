import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from atlas_interfaces.action import DiagnosticScan
import psutil
import time

class DiagnosticActionNode(Node):
    def __init__(self):
        super().__init__('diagnostic_action')
        
        self._action_server = ActionServer(
            self,
            DiagnosticScan,
            '/atlas/diagnostic_scan',
            self.execute_callback
        )
        self.get_logger().info('Atlas Diagnostic Action Server ready.')

    def execute_callback(self, goal_handle):
        self.get_logger().info(f'Scan started for {goal_handle.request.duration_seconds} seconds...')
        
        feedback_msg = DiagnosticScan.Feedback()
        issues = []

        for step in range(1, goal_handle.request.duration_seconds + 1):
            # Check system at each step
            cpu = psutil.cpu_percent(interval=0.5)
            mem = psutil.virtual_memory().percent

            if cpu > 80.0:
                issues.append(f"Step {step}: HIGH CPU {cpu}%")
            if mem > 80.0:
                issues.append(f"Step {step}: HIGH MEM {mem}%")

            # Send feedback
            feedback_msg.current_step = step
            feedback_msg.status = f"Step {step}: CPU {cpu}% | RAM {mem}%"
            goal_handle.publish_feedback(feedback_msg)
            self.get_logger().info(feedback_msg.status)

            time.sleep(1.0)

        # Final result
        goal_handle.succeed()
        result = DiagnosticScan.Result()
        result.success = True
        result.final_report = (
            f"Scan complete. {len(issues)} issue(s) found. " +
            (", ".join(issues) if issues else "All systems nominal.")
        )
        self.get_logger().info(result.final_report)
        return result

def main(args=None):
    rclpy.init(args=args)
    node = DiagnosticActionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()