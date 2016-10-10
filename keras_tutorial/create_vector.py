import os 
import glob 
import fileinput 
import numpy as np
import matplotlib.pyplot as plt

# After the Stanford CoreNLP toolkit has analysed the corpus, use this script
# to codify sentiments as integers [-2,2] for one line in a large text file
# that can be passed to a learning algorithm.

# Example of output vectors can be seen in ironic.txt and regular.txt

pathname1 = '/path_to_sentiment_analysed_files/Sentiment1/*.txt'
pathname2 = '/path_to_sentiment_analysed_files/Sentiment2/*.txt'

#Ironic Reviews

out1 = file('ironic.txt', 'a')

for fname in glob.glob(pathname1):
	cur_review = open(fname, 'r')
	sent_arr = np.array([])
	i = 1
	for line in cur_review:
		if i % 2 == 0:
			if line == '  Very negative\n':
				sent_arr = np.append([sent_arr], [-2])
			elif line == '  Negative\n':
				sent_arr = np.append([sent_arr], [-1])
			elif line == '  Neutral\n':
				sent_arr = np.append([sent_arr], [0])
			elif line == '  Positive\n':
				sent_arr = np.append([sent_arr], [1])
			elif line == '  Very positive\n':
				sent_arr = np.append([sent_arr], [2])
		i += 1
	#print(sent_arr)
	np.savetxt(out1, [sent_arr], fmt='%i', delimiter = ' ')

out1.close()

#Regular Reviews

out2 = file('regular.txt', 'a')

for fname in glob.glob(pathname2):
	cur_review = open(fname, 'r')
	sent_arr = np.array([])
	i = 1
	for line in cur_review:
		if i % 2 == 0:
			if line == '  Very negative\n':
				sent_arr = np.append([sent_arr], [-2])
			elif line == '  Negative\n':
				sent_arr = np.append([sent_arr], [-1])
			elif line == '  Neutral\n':
				sent_arr = np.append([sent_arr], [0])
			elif line == '  Positive\n':
				sent_arr = np.append([sent_arr], [1])
			elif line == '  Very positive\n':
				sent_arr = np.append([sent_arr], [2])
		i += 1
	#print(sent_arr)
	np.savetxt(out2, [sent_arr], fmt='%i', delimiter = ' ')

out2.close()
