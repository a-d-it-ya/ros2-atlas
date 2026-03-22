from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        
        Node(
            package='atlas_monitor',
            executable='system_monitor',
            name='system_monitor',
            parameters=[{
                'publish_rate': 1.0,
                'cpu_threshold': 80.0
            }]
        ),

        Node(
            package='atlas_monitor',
            executable='system_listener',
            name='system_listener',
        ),

        Node(
            package='atlas_monitor',
            executable='health_service',
            name='health_service',
        ),

        Node(
            package='atlas_monitor',
            executable='diagnostic_action',
            name='diagnostic_action',
        ),

    ])