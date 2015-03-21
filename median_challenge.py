#2 median words in a line

########## PSEUDO

# order the files in alphabetical order
# read in file line by line, count how many words on in each line
# add that number of words in the dictionary to the dictionary.
# if the number of words in the line has been seen before, 
#    then we add 1 to the key in the dictionary
# if the number of words in the line has not been seen before,
#    then we add that number as a key in the dictionary
# +1 to a line counter
# if the counter = even, 
#	  then get middle avg between middle 2 keys
# if the counter = odd, 
#    then find middle x
# and take the key of the dic --- make it a float 1.0
# move onto next line
# repeat
 
# if we can use a median() function, then 
# count the words in the line and dump that into an array.
# then just take the median() function of the array. spit that out before going onto the next line

import glob
import json

file_list = sorted(glob.glob('wc_input/*.txt'))


line_count = {} # dictionary of words in lines
counter = 0.0 # line counter
wordcount = 0.0 # words in a line
strike = 0.0 # when to jump out of the dic to get the key 
median_words = 0.0 # the median of the running today

# read the file into the dictionary in alphabetic order
# puts everything into lowercase
for input_file in file_list:
	with open(input_file, 'r') as curfile:

		# wordcount for the line needs to refresh every time a new line hits
		for line in curfile:

			# counts words in a line		
			wordcount = len(line.split())
			# counts the lines read
			counter += 1
			strike = 0

			if wordcount not in line_count:
				line_count[wordcount] = 1
			# word does exist in the dictionary. +1
			else:
				line_count[wordcount] += 1

			#corner case of only 1 key
			if len(line_count) == 1:
				for key, value in line_count.items():
					print float(key)
			
			# all other cases
			else:

				# even -- take the sum(middle 2 keys) divide by 2
				if counter % 2 ==0:
					while True:
						# sums up the key's definition and sums to strike
						for a,b in line_count.items():
							
							# add to the running total for the strike to jump out
							strike += b

							# now we have the middle left key in a 
							if strike > float(counter)/2:
								strike = 0
								while True:
									for c,d in line_count.items():
										strike += d
										if strike >= float(counter)/2:
											break
									break
								# get out completely
								break	
						median_words = (float(a)+c)/2
						print median_words
						break	

				# odd -- take the middle key
				elif counter % 2 == 1:
					while True:
						# sums up the key's definition and sums to strike
						for a,b in line_count.items():
							
							# add to the running total for the strike to jump out
							strike += b 
							if strike > counter/2:
								break
						median_words = float(a)
						print median_words
						break	

with open('wc_output/med_result.txt', 'w') as f:
	data = [line_count]
	json.dump(data, f)

