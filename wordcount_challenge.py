# Insight Data Engineering Fellows Program - Coding Challenge

# One of the first problems you'll encounter in data engineering is Word Count, which takes in 
# a text file or set of text files from a directory and outputs the number of occurrences for each word.  
# For example, Word Count on a file containing the following passage:


# So call a big meeting,
# Get everyone out out,
# Make every Who holler,
# Make every Who shout shout.

# would return:

# a		1
# big		1
# call		1
# every		2
# everyone	1
# get		1
# holler		1
# make	 	2
# meeting	        1
# out		2
# shout		2
# so		1
# who		2

# The first part of the coding challenge is to implement your own version of Word Count that counts all
# the words from the text files contained in a directory named wc_input and outputs the counts 
# (in alphabetical order) to a file named wc_result.txt,which is placed in a directory named wc_output.

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

				# word does not exist in the dictionary. starts with 1
				clean_word = ''.join(e for e in word if e.isalnum())
				
				if clean_word not in worddic:
					worddic[clean_word.lower().strip()] = 1
				# word does exist in the dictionary. +1
				else:
					worddic[clean_word.lower().strip()] += 1

for a,b in worddic.items():
	print a,b

with open('wc_output/wc_result.txt', 'w') as f:
	data = [worddic]
	json.dump(data, f)

# NLTK part

