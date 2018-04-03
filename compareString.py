import time

def compare(string1, string2):
	if len(string2) != len(string1):
		
		return False
	for i in range(len(string2)):
		if string2[i] != string1[i]:
			return False
	return True


