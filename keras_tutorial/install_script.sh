#!/bin/bash

sudo apt-get update

#Install all the python tools and fun other bits
sudo apt-get -y install libhdf5-8 libhdf5-dev libhdf5-cpp-8 python-h5py python2.7 python-numpy python-scipy python-dev g++ python-sklearn libblas3 libblas-common

#install the python package manager pip
sudo apt-get -y install python-pip
sudo pip install --upgrade pip

#Use pip to install theano and keras
sudo pip install pyyaml 
sudo pip install git+git://github.com/Theano/Theano.git
sudo pip install keras
