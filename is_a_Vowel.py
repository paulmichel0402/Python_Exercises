def vowelCheck(char):
	vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
	if char in vowels:
		return True
	return False
charIn = raw_input("Give me a char, I'll check if it's a vowel: ")
print str(vowelCheck(charIn))