import rclpy
from rclpy.node import Node
# your new imports here
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped

class TF2BroadcasterNode(Node):
    def __init__(self):
        super().__init__('tf2_broadcaster')
        self.broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.broadcast_transform)  

    def broadcast_transform(self):
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'base_link'
        t.child_frame_id = 'sensor_link'
        t.transform.translation.x = 0.5 
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.2
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0
        self.broadcaster.sendTransform(t)
def main(args=None):
    rclpy.init(args=args)
    node = TF2BroadcasterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()