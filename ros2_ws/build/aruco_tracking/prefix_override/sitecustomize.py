import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/saif/Desktop/ROARTASK/ros2_ws/install/aruco_tracking'
