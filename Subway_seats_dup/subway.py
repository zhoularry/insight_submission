# Q1: There is a subway car with N adjacent seats in a row.
#  People walk into the subway and choose a random available 
#  seat (drawn uniformly). The only constraint on seat 
#  availability is that they do not like to sit next to one 
#  another so there is always (at least) one empty seat 
#  between any two individuals. This process continues until 
#  all available seats are taken. What is the mean and 
#  standard deviation of the fraction of occupied seats (when 
#  the process is complete) for different values of N? Give the answer with 10 digits of significance.
# N=25
# N=50000

import random 
import pandas as pd
import numpy as np

# PROCESS
# produce a car of size n
# initially all seats are 0
# user enters into the car and takes random seat, now switched to 2
# seats around said person become 1's  -  this is the 1 seat buffer (no one wants to sit next to each other)
# next person comes in and chooses only from the seat that are 0
# repeat until all seats are taken or are buffer

# how many seats are there in the subway car
n = 50
# used to get how many runs
x = 0

# declare the list called fill that will hold the ratios of the cars
fill = []

# increase/decrease this number to show how many runs you wnat to do
while x < 500:
	# initiate the array of the car of length n
	car = []
	# and empty seat array that gives us seats to choose from
	empty_seat = []

	# appends 0's into the car. 0's represent an empty seat
	for i in xrange(n):
		car.append(0)

	# looks for empty seats in the car that are marked by 0 and appends them the empy_seat array
	for position, seat in enumerate(car):
		if seat == 0:
			empty_seat.append(position)
	#counts the people on the train
	people = 0

	# while there are empty seats in the car, so as long as there a 0 in the car
	while len(empty_seat)>1:

		# finds a seat based on how long the empty_seat array is
		# index number
		seat_index = random.randrange(0,len(empty_seat)) 

		# find the value in the empty_seat array using the index seat_index
		seat_number = empty_seat[seat_index]
		# occupied seat is denoted as a 2
		car[seat_number] = 2
		# pop out the occupied seat in the empty_seat array
		empty_seat.pop(seat_index)

		# case if it's the first seat
		if seat_number == 0:
			car[seat_number + 1] = 1
			# pops the first number in the array since the taken seat, 0, was already
			empty_seat.pop(0)		

		# case if it's the last seat
		elif seat_number == n - 1:
			car[seat_number - 1] = 1
			empty_seat.pop(seat_index - 1)

		# case if chosen seat is neither end case
		else:

			# if the seat was already removed, skips
			if empty_seat[seat_index - 1] == seat_number - 1:
				empty_seat.pop(seat_index - 1)

				# all seats taken, skips
				if len(empty_seat)>0:

				# pop out the empty_seat 1 "ahead" of the taken seat
				# counter intuitive as the array is getting smaller so it's actually " - 1" instead of " + 1"
					if seat_number + 1 in empty_seat:
						empty_seat.pop(seat_index - 1)
			
			car[seat_number + 1] = 1
			car[seat_number - 1] = 1

		people += 1

	# this means there is 1 last seat in the car
	if 0 in car:
		people = people + 1

	# determines ratio of taken seats to total seats
	fill_ratio = people / float(n)

	# appends the fill_ratio to the list
	fill.append(fill_ratio)

	x += 1;

# display what the ratio is for every run through the program
print fill

# using numpy to find mean and standard deviation of the array
np_mean = np.mean(fill, axis=0)
np_std = np.std(fill, axis=0)

print "mean ratio of a filled car:", np_mean
print "standard deviation of ratio of a filled car: ", np_std