
###################
# PSEUDO CODE
#1 Word Count
# deliniate by 1 space and read into an array per line

# then for each array read into a dictionary
# if it doesnt exist, add to the dic and assign it to 1
# if it does exist, go to dic entry and +1

# sort the dictionary by word
# display dic along with counts

import csv
import glob
import json
import pdb # debugger. remove

file_list = sorted(glob.glob('wc_input/*.txt'))
# pdb.set_trace()

	# file = open('wc_input/wc_input.txt', 'r')

# create a dictionary
worddic = {} 

# read the file into the dictionary
# puts everything into lowercase

for input_file in file_list:
	with open(input_file, 'r') as curfile:

		for word in curfile.read().split():

				# remove the punctuation
				clean_word = ''.join(e for e in word if e.isalnum())

				# word does not exist in the dictionary. starts with 1
				# remove any spaces and makes all lowercase
				if clean_word not in worddic:
					worddic[clean_word.lower().strip()] = 1
				# word does exist in the dictionary. +1
				else:
					worddic[clean_word.lower().strip()] += 1

sorteddic = {}

# sort dictionary by key
for key in sorted(worddic.iterkeys()):	
	print "%s: %s" % (key, worddic[key])

with open('wc_output/wc_result.txt', 'w') as f:
	data = [worddic]
	json.dump(data, f)

# NLTK part

