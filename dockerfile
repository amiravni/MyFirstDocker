### based on ubuntu 16.04 with ros kinetic
FROM ros:kinetic

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y software-properties-common

RUN add-apt-repository -y ppa:ubuntu-desktop/ubuntu-make
RUN apt-get update
RUN apt-get install -y openjdk-8-jre-headless
RUN apt-get install -y ubuntu-make
RUN apt-get install -y python3-pip \
gedit \
python3-tk \
python3-yaml \
python-catkin-tools \
python3-dev \
python3-numpy \
ros-kinetic-cv-bridge

RUN pip3 install --upgrade pip==9.0.3
RUN pip install opencv-python matplotlib rospkg catkin_pkg

## pycharm installation
RUN umake ide pycharm /root/.local/share/umake/ide/pycharm

## this part is for compiling cv_bridge for python3
WORKDIR /usr/lib/x86_64-linux-gnu/
RUN ln -s libboost_python-py35.so libboost_python3.so
RUN mkdir /root/catkin_build_ws
WORKDIR   /root/catkin_build_ws
RUN catkin config -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.5m -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.5m.so
RUN catkin config --install
RUN mkdir src
WORKDIR /root/catkin_build_ws/src
RUN git clone -b kinetic https://github.com/ros-perception/vision_opencv.git
WORKDIR /root/catkin_build_ws 
RUN /bin/bash -c "source /opt/ros/kinetic/setup.bash && catkin build cv_bridge"

## copying data to docker and add settings 
RUN mkdir /root/work/
RUN mkdir /root/work/shared/
RUN mkdir /root/PycharmProjects/
WORKDIR /root/
COPY root .
WORKDIR /
COPY ros_entrypoint.sh .
RUN chmod +x ros_entrypoint.sh
RUN echo "alias pycharm='/root/.local/share/umake/ide/pycharm/bin/pycharm.sh'" >> /root/.bashrc


