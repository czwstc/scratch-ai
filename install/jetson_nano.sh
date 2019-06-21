#!/bin/bash
# Based on: jetson-nano-sd-r32.1.1-2019-05-31

#apt source
sudo su
cp /etc/apt/sources.list /etc/apt/sources.list.bak
cat > /etc/apt/sources.list<<-EOF
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic main restricted universe multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic-updates main restricted universe multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic-backports main restricted universe multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/ bionic-security main restricted universe multiverse
EOF
apt update
exit

#apt packages
sudo apt-get install python3-pip python3-setuptools python3-dev python3-opencv \
    libhdf5-serial-dev hdf5-tools \
    libsdl1.2-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libfreetype6-dev libportmidi-dev \
    libatlas-base-dev libilmbase-dev libopenexr-dev libgstreamer1.0-dev libswscale-dev \
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
sudo pip3 install pygame futures==2.2 flask Pillow keras==2.0.9 numpy==1.16.4

#tensorflow
wget https://developer.download.nvidia.com/compute/redist/jp/v42/tensorflow-gpu/tensorflow_gpu-1.13.1+nv19.3-cp36-cp36m-linux_aarch64.whl
sudo pip3 install tensorflow_gpu-1.13.1+nv19.3-cp36-cp36m-linux_aarch64.whl
sudo python3 -c "from tensorflow.python.client import device_lib; print(device_lib.list_local_devices())"