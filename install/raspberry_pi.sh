#!/bin/bash
# Based on: 2019-04-08-raspbian-stretch-full

#apt source
sudo su
cp /etc/apt/sources.list /etc/apt/sources.list.bak
cat > /etc/apt/sources.list<<-EOF
deb http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ stretch main non-free contrib
deb-src http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ stretch main non-free contrib
EOF
apt update
exit

#apt packages
sudo apt install python3-pip python3-h5py python3-scipy\
    libsdl1.2-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libportmidi-dev \
    libatlas-base-dev libjasper1 libilmbase-dev libopenexr-dev libgstreamer1.0-dev libswscale-dev \
    libavformat-dev libavcodec-dev libpng-dev libjpeg-dev libqttest4-perl libhdf5-dev gfortran 

#pip source
sudo su
mkdir ~/.pip/
cat > ~/.pip/pip.conf<<-EOF
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/
EOF
exit

#pip packages
sudo pip3 install pygame futures==2.2 flask Pillow picamera

#tensorflow
wget https://github.com/lhelontra/tensorflow-on-arm/releases/download/v1.12.0/tensorflow-1.12.0-cp35-none-linux_armv7l.whl
sudo pip3 install tensorflow-1.12.0-cp35-none-linux_armv7l.whl
sudo python3 -c "from tensorflow.python.client import device_lib; print(device_lib.list_local_devices())"

#opencv
wget https://www.piwheels.hostedpi.com/simple/opencv-python/opencv_python-3.4.4.19-cp35-cp35m-linux_armv7l.whl
sudo pip3 install opencv_python-3.4.4.19-cp35-cp35m-linux_armv7l.whl