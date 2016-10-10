import os 
import fileinput
import glob

command = 'java -cp "*" -mx5g edu.stanford.nlp.sentiment.SentimentPipeline -file '
pathname1 = '/point_towards_original_paragraphs/Ironic/*.txt'
pathname2 = '/point_towards_original_paragraphs/Regular/*.txt'

#os.system(command+filename+operation) 

#for every .txt file in your corpus take text b/w <REVIEW><\REVIEW> and analyse it. 

for fname in glob.glob(pathname1):
	temp = open('results/temp.txt', 'w+')
	cur_review = open(fname, 'r')
	for line in cur_review:
		if line == '<REVIEW>\n':
			for line in cur_review:
				if line != '</REVIEW>':
					temp.write(line)
	temp.close()
	os.system(command+'results/temp.txt'+' > results/'+os.path.basename(fname))
	os.remove('results/temp.txt')

for fname in glob.glob(pathname2):
	temp = open('results/temp.txt', 'w+')
	cur_review = open(fname, 'r')
	for line in cur_review:
		if line == '<REVIEW>\n':
			for line in cur_review:
				if line != '</REVIEW>':
					temp.write(line)
	temp.close()
	os.system(command+'results/temp.txt'+' > results/'+os.path.basename(fname))
	os.remove('results/temp.txt')