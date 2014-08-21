def pangram_check(strIn):
	letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	strLow = strIn.lower()
	for let in letters:
		if let not in strLow:
			return False
	return True

print pangram_check('The quick brown fox jumps over the lazy dog')
print pangram_check('This won\'t have all the letters')