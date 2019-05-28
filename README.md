# MyFirstDocker
The docker includes
* Ubuntu 16.04
* ROS kinetic
* python 3.5.2 (In addition to python2 which comes with ROS)
* OpenCV 4.1
* All needed ROS-related configuration to run python3 with
	* rospy
	* rosbag
	* cv_bridge
* pycahrm community with virtual enviroment under `/root/PycharmProjects/dev`

## How to build
```
sudo apt-get install docker.io
git clone https://github.com/amiravni/MyFirstDocker.git
cd MyFirstDocker
chmod +x build_docker.sh
./build_docker.sh
```

## How to run and make the display working on the host machine (tested on ubuntu 18.04)
```
chmod +x run_docker.sh
./run_docker.sh
```
