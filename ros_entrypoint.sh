#!/bin/bash
set -e

# setup ros environment
source "/opt/ros/$ROS_DISTRO/setup.bash"
alias pycharm='/root/.local/share/umake/ide/pycharm/bin/pycharm.sh'
export PYTHONPATH=/usr/local/lib/python3.5/dist-packages/:/opt/ros/kinetic/lib/python2.7/dist-packages/
source /root/catkin_build_ws/install/setup.bash --extend
exec "$@"

