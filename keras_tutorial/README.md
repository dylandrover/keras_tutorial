## Install Keras

To install Keras first update your repos

~$ sudo apt-get update

Keras will need numerous extra libraries to run properly so run this line and obtain these packages

~$ sudo apt-get install python-numpy python-scipy python-dev python-pip python-nose g++ libopenblas-dev git libhdf5-serial-dev python-pip python-matplotlib python-sklearn

Installing Theano and Keras is easiest using the pip package manager. Update it first

~$ sudo pip install --upgrade pip

Use pip to install the following packages. NOTE: the newer version of theano is needed for "ReLu" to work properly

~$ sudo pip install pyyaml h5py
~$ sudo pip install git+git://github.com/Theano/Theano.git
~$ sudo pip install keras

## Install Stanford CoreNLP toolkit for sentiment analysis

http://stanfordnlp.github.io/CoreNLP/

http://nlp.stanford.edu/sentiment/code.html

## Amazon Sarcasm Corpus 

http://storm.cis.fordham.edu/~filatova/SarcasmCorpus.html

## Using the Scripts

To generate vectors to feed the learning algorithms ... 
