## Synopsis 

The purpose of this project was two-fold. One was that it serves as a quick and simple intro to Keras, the second was that it was a proof of concept for the idea that sarcasm or verbal irony (I'm aware there's a subtle difference between the two but let's move on...) can be detected by drastic or frequent changes in the sentiment between sentences within a paragraph. 

To test this, a corpus was found with sarcastic and regular reviews from amazon.com. Using the Stanford Sentiment Analysis Recursive Network (part of Stanford's CoreNLP toolkit, see below) each sentence was determined to be Very Negative, Negative, Neutral, Positive or Very Positive. From this, each paragraph's sentences were coded into a vector of numbers with Very Negative as -2, Negative as -1, Neutral as 0, Positive as +1 and Very Positive as +2. The final vector of integers between -2 and +2 would be considered one training example for a Keras neural network to learn from. For more information on Keras, please check out their site (https://keras.io/) or look at a tutorial I did some time ago (https://www.youtube.com/watch?v=Tp3SaRbql4k) 

## Install Keras

To install Keras first update your repos...

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

The vectors used to train the networks are based on sentiment analysis that was performed by the excellent Stanford Sentiment Analysis Recursive Network project (terminal commands and more info here: http://nlp.stanford.edu/sentiment/code.html). This project is part of the Stanford CoreNLP toolkit which can be downloaded from: http://stanfordnlp.github.io/CoreNLP/. Once these tools are installed, analysis on a desired corpus is possible. 

## Amazon Sarcasm Corpus 

The code here uses the corpus downloaded from the Sarcasm Corpus (http://storm.cis.fordham.edu/~filatova/SarcasmCorpus.html). In theory, the sentiment_analyzer.py and create_vector.py scripts can be altered and used on other corpuses, so long as the Stanford Sentiment Analyser is installed. 

## Using the Scripts

To generate vectors to feed the learning algorithms, first set up your respective corpus sections (NOTE: these scripts were written to run with the Sarcasm Corpus mentioned above, they won't work for another corpus without modification) Run sentiment_analyzer.py on your corpus first, it will insert the perceived sentiment of a sentence into a new line below the sentence. This is done for every sentence in a paragraph. To codify these inserted sentiments, run create_vectors.py to generate one large .file of vectors for the desired sentiments (set up to do ironic and regular reviews). In the final txt file, each line corresponds to one paragraph or review. An example of these files can be seen in the ironic.txt and regular.txt filed in this project. 

The keras based neural networks are configured to take in these text files and perform learning and prediction. 
