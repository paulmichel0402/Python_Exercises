def reverse(str):
	retStr = ""
	for char in str[::-1]:
		retStr += char
	return retStr

reverse("Test")

def is_palindrome(str):
	revStr = reverse(str)
	for index in range(len(str)):
		if str[index] != revStr[index]:
			return False
	return True

print is_palindrome("Panda")
print is_palindrome("amanaplanacanalpanama")
