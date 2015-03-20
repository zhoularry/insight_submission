#2 median words in a line
	
# order the files in alphabetical order
# read in file line by line
# deliniate by 1 space and count how many words on in each line
# add that number of words in the dictionary to the dictionary.
# if the number of words in the line has been seen before, 
# #   then we add 1 to the key in the dictionary
# if the number of words in the line has not been seen before,
#   then we add that number as a key in the dictionary
# +1 to a counter that finds out how many lines have been read
# if the counter = even, then we go through the keys to whatever 
# key that gives us where n/2 falls
# if the counter = odd, then we go through to the n/2 where that falls
# and take the key of the dic --- make it a float 1.0
# move onto next line
# repeat
 
# if we can use a median() function, then 
# count the words in the line and dump that into an array.
# then just take the median() function of the array. spit that out before going onto the next line

import glob
import json
import pdb # debugger. remove

file_list = sorted(glob.glob('wc_input/*.txt'))
# pdb.set_trace()

# create a dictionary
line_count = {} 
# wordcount for the line
wordcount = 0

# read the file into the dictionary in alphabetic order
# puts everything into lowercase

for input_file in file_list:
	with open(input_file, 'r') as curfile:

		for word in curfile.read().split():
			wordcount += 1
				
				if clean_word not in line_count:
					line_count[clean_word.lower().strip()] = 1
				# word does exist in the dictionary. +1
				else:
					line_count[clean_word.lower().strip()] += 1

for a,b in line_count.items():
	print a,b

with open('wc_output/med_result.txt', 'w') as f:
	data = [line_count]
	json.dump(data, f)

