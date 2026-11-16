ROS2 Jazzy Learning Sprint

This repository contains my first self-directed ROS2 project, built over a weekend to prepare for a Robotics Research Internship.

What it does
- Publisher (sensor_publisher): Simulates a sensor sending a reading every 0.5 seconds on the 'sensor_data' topic.
- Subscriber (anomaly_detector): Listens to 'sensor_data', applies a basic rule, and logs a warning if an anomaly is detected.

How to build and run
bash
cd ~/ros2_ws
colcon build --packages-select anamoly_pkg
source install/setup.bash

In terminal 1:
ros2 run anamoly_pkg publisher

In terminal 2:
ros2 run anamoly_pkg subscriber
