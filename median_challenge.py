#2 median words in a line
	
# order the files in alphabetical order and 
# add text files to the bottom of the ones prior to it

# read in file line by line
# deliniate by 1 space and count how many words on in it

# for loop through the 

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

with open('wc_output/med_result.txt', 'w') as f:
	data = [worddic]
	json.dump(data, f)

