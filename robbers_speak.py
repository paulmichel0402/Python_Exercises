def translate(str):
	vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', " "]
	retStr = ""
	for char in str:
		if char in vowels:
			retStr = retStr + char
		else:
			retStr = retStr + char
			retStr = retStr + 'o'
			retStr = retStr + char
	return retStr

strIn = raw_input("Give me a string, I will translate it: ")
print translate(strIn)