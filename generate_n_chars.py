def generate_n_chars(n,c):
	retStr = ''
	for i in range(n):
		retStr += c
	return retStr
print generate_n_chars(5, 'P')

def histogram(intList):
	for elt in intList:
		print generate_n_chars(elt, '*')
	return
histogram([10,4,7])