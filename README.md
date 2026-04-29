# ROS 2 + Gazebo Robot Simulation

A 6-wheeled Mars rover simulation with IMU and camera sensors, built with ROS 2 Humble and Gazebo Ignition (Harmonic). Features ArUco marker detection for visual perception and localization.

## Features

- **6-Wheeled Mars Rover**: Differential drive with suspension arms, modular URDF/Xacro design
- **Sensors**: IMU (100 Hz) and RGB camera (640×480 @ 30 Hz) with realistic noise modeling
- **Custom World**: 4 ArUco marker poles (IDs 51-54) positioned in 6m × 6m square
- **Teleoperation**: Python GUI with sliders for manual control
- **ROS 2 Integration**: Complete topic bridging, TF tree management, and sensor data publishing

## Prerequisites

- Ubuntu 22.04 LTS
- ROS 2 Humble
- Gazebo Ignition (Sim 8.11.0+)
- Python 3.10+

## Quick Start

### 1. Verify Installation

```bash
cd ~/Desktop/ROARTASK
./verify_installation.sh
./verify_marker_world.sh
```

### 2. Build Workspace

```bash
cd ros2_ws
source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash
```

### 3. Launch Simulation

```bash
# Using alias (recommended)
rosgp

# Or full command
ros2 launch my_robot_gazebo spawn_robot.launch.py
```

### 4. Control Robot (Optional)

```bash
# Terminal 2: Launch teleop GUI
python3 robot_teleop_gui.py
```

### 5. View Camera Feed (Optional)

```bash
# Terminal 3: View camera
ros2 run rqt_image_view rqt_image_view
# Select topic: /camera/image_raw
```

## Available Aliases

Add to `~/.bashrc` for convenience:

```bash
alias rosb='cd ~/Desktop/ROARTASK/ros2_ws && source /opt/ros/humble/setup.bash && colcon build --symlink-install && source install/setup.bash'
alias rosd='cd ~/Desktop/ROARTASK/ros2_ws && source install/setup.bash && ros2 launch my_robot_description display.launch.py'
alias rosg='cd ~/Desktop/ROARTASK/ros2_ws && source install/setup.bash && ros2 launch my_robot_description gazebo.launch.py'
alias rosgp='cd ~/Desktop/ROARTASK/ros2_ws && source install/setup.bash && ros2 launch my_robot_gazebo spawn_robot.launch.py'
alias rosgu='cd ~/Desktop/ROARTASK/ros2_ws && source install/setup.bash && python3 robot_teleop_gui.py'
```

- `rosb` - Build workspace
- `rosd` - Launch RViz (visualization only)
- `rosg` - Launch Gazebo (empty world)
- `rosgp` - Launch Gazebo (marker world) ⭐ **Recommended**
- `rosgu` - Launch teleop GUI

## Project Structure

```
ROARTASK/
├── ros2_ws/
│   └── src/
│       ├── my_robot_description/    # Robot URDF/Xacro models
│       ├── my_robot_gazebo/         # Simulation worlds & models
│       │   ├── worlds/              # marker_world.world
│       │   ├── models/              # pole51-54 (local)
│       │   └── launch/              # spawn_robot.launch.py
│       ├── my_robot_perception/     # Perception integration
│       └── aruco_tracking/          # ArUco detection node
├── verify_installation.sh           # Environment check
├── verify_marker_world.sh           # Marker world check
├── CAMERA_TESTING_GUIDE.md          # Camera testing
├── MARKER_WORLD_GUIDE.md            # World creation guide
└── README.md                        # This file
```

## System Architecture

**Coordinate Frames:**
- `base_footprint` → `base_link` → `imu_link`, `camera_link`, 6 arms, 6 wheels

**Data Flow:**
```
Gazebo Sensors → ros_gz_bridge → ROS 2 Topics
  ├─ IMU      → /imu/data (100 Hz)
  ├─ Camera   → /camera/image_raw (30 Hz)
  │           → /camera/camera_info
  ├─ Odometry → /odom (50 Hz)
  └─ Control  ← /cmd_vel (teleop input)
```

## Common Commands

```bash
# Topics
ros2 topic list
ros2 topic hz /camera/image_raw
ros2 topic echo /imu/data

# TF Tree
ros2 run tf2_tools view_frames

# Nodes
ros2 node list
ros2 node info /robot_state_publisher

# Gazebo
gz topic -l
gz model -l
```

## Troubleshooting

### Robot Not Spawning
**Solution**: Wait 3 seconds for Gazebo to load (automatic delay in launch file)

### Camera Feed Not Showing
**Solution**: Check bridge is running:
```bash
ros2 node list | grep bridge
ros2 topic list | grep camera
```

### Teleop Not Working
**Solution**: Verify cmd_vel bridge:
```bash
ros2 topic info /cmd_vel
# Should show publishers and subscribers
```

### Markers Not Visible
**Solution**: Verify models are in workspace:
```bash
ls ros2_ws/src/my_robot_gazebo/models/
# Should show: pole51 pole52 pole53 pole54
```

## Documentation

- **[CAMERA_TESTING_GUIDE.md](CAMERA_TESTING_GUIDE.md)**: Camera sensor testing procedures
- **[MARKER_WORLD_GUIDE.md](MARKER_WORLD_GUIDE.md)**: Step-by-step world creation guide
- **[tasks.md](.kiro/specs/ros2-gazebo-robot-simulation/tasks.md)**: Implementation task list
- **[requirements.md](.kiro/specs/ros2-gazebo-robot-simulation/requirements.md)**: System requirements
- **[design.md](.kiro/specs/ros2-gazebo-robot-simulation/design.md)**: Architecture design

## Development Status

**Phase 4 Complete** - Environment and Perception

✅ Completed:
- Environment setup (ROS 2 Humble + Gazebo Sim 8.11.0)
- 6-wheeled Mars rover model with suspension
- IMU sensor integration with noise modeling
- Camera sensor integration (640×480 @ 30 Hz)
- Custom marker world with 4 ArUco poles
- Differential drive control system
- Teleoperation GUI
- ArUco marker detection integration
- Complete system visualization in RViz

## Resources

- [ROS 2 Humble Documentation](https://docs.ros.org/en/humble/)
- [Gazebo Ignition Documentation](https://gazebosim.org/docs)
- [ROS 2 + Gazebo Integration](https://github.com/gazebosim/ros_gz)

## License

Educational project for ASU ROAR'26 Solo Mission Part 2 assignment.

---

**Version**: 1.0.0 | **Last Updated**: April 29, 2026 | **Status**: All Tasks Complete
