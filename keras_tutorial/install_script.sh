#!/bin/bash

sudo apt-get update

#Install all the python tools and fun other bits
sudo apt-get install python-numpy python-scipy python-dev python-pip python-nose g++ libopenblas-dev git libhdf5-serial-dev python-pip python-matplotlib python-sklearn

#Update pip
sudo pip install --upgrade pip

#Use pip to install theano, keras and other things I guess
sudo pip install pyyaml h5py
sudo pip install git+git://github.com/Theano/Theano.git
sudo pip install keras
