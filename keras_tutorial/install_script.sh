#!/bin/bash

sudo apt-get update

#Install all the python tools and fun other bits
sudo apt-get install python-numpy python-scipy python-dev python-pip python-nose g++ libopenblas-dev git libhdf5-serial-dev
#install the python package manager pip
sudo apt-get -y install python-pip
sudo pip install --upgrade pip

#Use pip to install theano and keras
sudo pip install pyyaml h5py
sudo pip install git+git://github.com/Theano/Theano.git
sudo pip install keras
