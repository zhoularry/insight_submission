
###################
# PSEUDO CODE
#1 Word Count
# deliniate by 1 space and read into an array per line

# then for each array read into a dictionary
# if it doesnt exist, add to the dic and assign it to 1
# if it does exist, go to dic entry and +1

# sort the dictionary by word
# display dic along with counts

# write the sorted dic with all counts into the .txt final
###################

import csv
import glob
import json
import pdb # debugger. remove

# sorts the files in alpha order and takes the 1 at a time
file_list = sorted(glob.glob('wc_input/*.txt'))
# pdb.set_trace()

# create a dictionary
worddic = {} 

# read the current file into the dictionary
for input_file in file_list:
	with open(input_file, 'r') as curfile:

		# going line by line (read), word for word (split)
		for word in curfile.read().split():

				# remove the punctuation from the word
				clean_word = ''.join(e for e in word if e.isalnum())

				# word does not exist in the dictionary. start with 1
				# remove any spaces and makes all lowercase
				if clean_word not in worddic:
					worddic[clean_word.lower().strip()] = 1
				# if word does exist in the dictionary, +1
				else:
					worddic[clean_word.lower().strip()] += 1

# sort dictionary by key
s = sorted (worddic.keys())
	
# show sorted dic
for key in s:
 	print key, worddic[key]

# sort dictionary by key
# for key in sorted(worddic.iterkeys()):	
#  	print "%s: %s" % (key, worddic[key])

with open('wc_output/wc_result.txt', 'w') as f:

	for key in sorted(worddic.keys()):
	 	f.write(key + " " + str(worddic[key]) +'\n')

# NLTK part

