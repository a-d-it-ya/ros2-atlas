# ROS2 Atlas — Learning ROS 2 from Scratch

A hands-on ROS 2 learning repository built from zero, covering all core concepts through a real implementation.

## What's Inside

### `atlas_monitor` — Core ROS 2 Package
A complete system monitoring and robot control package demonstrating every ROS 2 communication primitive.

| Node | What it does |
|---|---|
| `system_monitor` | Publishes CPU & RAM stats to `/atlas/cpu` and `/atlas/memory` at configurable rate |
| `system_listener` | Subscribes to system topics and alerts on high resource usage |
| `health_service` | On-demand health report via ROS 2 Service |
| `diagnostic_action` | Multi-step system diagnostic scan with live feedback via ROS 2 Action |
| `tf2_broadcaster` | Broadcasts sensor frame transform relative to robot base |

### `atlas_interfaces` — Custom Message Types
Custom action definition for the diagnostic scan system.

### `urdf/robot.urdf` — Atlas Bot
A two-wheeled differential drive robot built from scratch and simulated in Gazebo 11.

## Concepts Covered

- **Nodes** — single-responsibility processes
- **Topics** — continuous pub/sub data streams
- **Services** — request/response communication
- **Actions** — long-running tasks with feedback and cancel
- **Parameters** — runtime configurable node values
- **Launch Files** — single command full system startup
- **TF2** — coordinate frame transforms
- **URDF** — robot description and physical modeling
- **Gazebo** — physics simulation with differential drive control
- **RViz** — 3D robot visualization

## Quick Start
```bash
# Build
cd ~/ros2_ws
colcon build
source install/setup.bash

# Launch full system
ros2 launch atlas_monitor atlas.launch.py

# Launch robot in Gazebo
gazebo --verbose -s libgazebo_ros_factory.so
ros2 run gazebo_ros spawn_entity.py -file ~/ros2_ws/src/atlas_monitor/urdf/robot.urdf -entity atlas_bot -z 0.1

# Control the robot
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.5, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}"
```

## Stack
- ROS 2 Humble
- Gazebo Classic 11
- Python 3
- WSL2 Ubuntu 22.04