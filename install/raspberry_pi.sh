#!/bin/bash
# Based on: 2019-06-20-raspbian-buster-full

#apt packages
sudo apt install python3-pip python3-h5py python3-scipy \
    libsdl1.2-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libportmidi-dev \
    libatlas-base-dev libjasper1 libilmbase-dev libopenexr-dev libgstreamer1.0-dev libswscale-dev \
    libavformat-dev libavcodec-dev libpng-dev libjpeg-dev libhdf5-dev gfortran 

#pip source
sudo su
mkdir ~/.pip/
cat > ~/.pip/pip.conf<<-EOF
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/
EOF
exit

#pip packages
sudo pip3 install pygame flask Pillow picamera tensorflow opencv grpcio
sudo python3 -c "from tensorflow.python.client import device_lib; print(device_lib.list_local_devices())"
