def str_length(str):
	ctr = 0
	for elt in str:
		ctr += 1
	return ctr

strIn = raw_input("Give me a string, I'll give you the length: ")
print(str_length(strIn))
	