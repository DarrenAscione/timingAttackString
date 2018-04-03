from hashlib import sha256

def constant_compare(string1, string2):

	# hashed to 64
	hashed1 = sha256(string1).hexdigest()
	hashed2 = sha256(string2).hexdigest()

	# forming byte array of hashed strings
	byteArray1 = [int(elem.encode("hex")) for elem in hashed1]
	byteArray2 = [int(elem.encode("hex")) for elem in hashed2]

	# XOR operator
	res = 0
	for i in xrange(len(byteArray1)):
		res = byteArray1[i] ^ byteArray2[i]

	return True if res == 0 else False

print constant_compare('aa', 'aa')


	
	

