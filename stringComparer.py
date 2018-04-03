import sys
import time
import random
from compareString import *

class StringComparer:

	def __init__(self, password, avglen=10):
		# create array of all possible legal characters found in a password
		# self.characters = map(chr, xrange(33, 127))
		# self.characters = map(chr, xrange(97, 123))
		self.characters = ['a','b']
		self.password = password
		self.avglen = avglen

	# returns password length vulnerability
	def length_atk(self):
		time_list = {}

		# loop through possible password length based on avglen
		for i in xrange(self.avglen):
			string1 = 'x' * i
			time_list[i] = []
			time_list[i] = self.time_loop(string1, 100)

		# string length that took the longest time == correct length of password
		return max(time_list, key=time_list.get)

	# runs compare string function vulnerable count no. of times
	def time_loop(self, string1, count):
		time_list = []
		# averages out of 100 runs for accuracy
		for i in xrange(count):
			start = time.time()
			try:
				compare(string1, self.password)
			except Exception as e:
				raise e
			finally:
				time_list.append((time.time() - start)*10**10)
		return sum(time_list)/count

	def string_atk(self, length):
		#create array of to store all possible combination of passwords with each char
		possible = ['x'*length for i in xrange(len(self.characters))]

		# looping attack 20 times for accuracy
		for i in xrange(len(possible[0])):
			time_list = {}
			possible = self.index_change(i, possible)
			print possible
			for j in xrange(len(possible)):
				time_list[possible[j]] = []
				time_list[possible[j]] = self.time_loop(possible[j], 10000)
			print str(i) + " Char Guess: " + max(time_list, key=time_list.get)
			possible =  [max(time_list, key=time_list.get) for ii in xrange(len(possible))]
		return max(time_list, key=time_list.get)

	def index_change(self, key, array):
		random.shuffle(self.characters)
		for i in xrange(len(array)):
			temp = list(array[i])
			temp[key] = self.characters[i]
			array[i] = "".join(temp)
		return array

if __name__ == '__main__':
	string2 = 'aaaaaabb'
	stringHack = StringComparer(string2)
	length = stringHack.length_atk()
	print length == len(string2)
	print "Length of password found: " + str(length) + '\n'

	answer = stringHack.string_atk(length)
	print answer == string2





