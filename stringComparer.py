import sys
import time
from compareString import *

class StringComparer:

	def __init__(self, password):
		# create array of all possible legal characters found in a password
		self.characters = map(chr, xrange(33, 127))
		self.password = password
		self.avglen = 10

	# returns password length vulnerability
	def length_atk(self):
		time_list = {}

		# assumes average password length of up to 10 characters
		for i in xrange(self.avglen):
			string1 = 'x' * i
			time_list[i] = []

			# averages out of 1000 runs for accuracy
			for j in xrange(1000):
				start = time.time()
				compare(string1, string2)
				time_list[i].append(time.time() - start)
			time_list[i] = sum(time_list[i])/10.0

		# string length that took the longest time == correct length of password
		return max(time_list, key=time_list.get)

	def string_atk(self, length):

		#create array of to store all possible combination of passwords with each char
		possible = []
		for i in xrange(94):
			possible.append(characters[i]+'x'*8)

		# looping attack 20 times for accuracy


if __name__ == '__main__':
	string2 = 'password1'
	stringHack = StringComparer(string2)
	print stringHack.length_atk()




