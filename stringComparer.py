import sys
import time
from compareString import *


# returns password length vulnerability
def length_atk(string2):
	time_list = {}
	for i in xrange(10):
		string1 = 'x' * i
		time_list[i] = []
		# averages out of 1000 runs for accuracy
		for j in xrange(1000):
			start = time.time()
			compare(string1, string2)
			time_list[i].append(time.time() - start)
		time_list[i] = sum(time_list[i])/10.0
	return max(time_list, key=time_list.get)

def string_atk(length, string2):
	# create array of all possible legal characters found in a password
	characters = map(chr, xrange(33,127))

	#create array of to store all possible combination of passwords with each char
	possible = []
	for i in xrange(94):
		possible.append(characters[i]+'x'*8)

	# looping attack 20 times for accuracy


if __name__ == '__main__':
	string2 = 'password1'
	length =  length_atk(string2)
	string_atk(length, string2)
	


