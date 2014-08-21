def palindrome_checker(strIn):
	letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	revStr = reverse(strIn).lower()
	strLow = strIn.lower()
	for i in range(len(revStr)):
		while revStr[i] not in letters:
			i += 1
		for j in range(len(strLow)):
			while strLow[j] not in letters:
				j += 1
			if strLow[j] != revStr[i]:
				return False
			else:
				i += 1 
				j += 1
				break
			break
	return True


def reverse(str):
	retStr = ""
	for char in str[::-1]:
		retStr += char
	return retStr
print palindrome_checker('lion oil')	