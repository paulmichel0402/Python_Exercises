def max_in_list(intList):
	max = intList[0]
	for elt in intList:
		if elt > max:
			max = elt
	return max
print max_in_list([700,2,3,565,4289, -123])

def find_longest_word(wordsList):
	lengths = []
	for i in range(len(wordsList)):
		lengths.append(len(wordsList[i]))
	return max_in_list(lengths)

def filter_long_words(wordsList,n):
	words = []
	for word in wordsList:
		if len(word) > n:
			words.append(word)
	return words

print find_longest_word(["a", "man", "a", "plan", "a", "canal", "Panama", "Abracadabra"])
print filter_long_words(["a", "man", "a", "plan", "a", "canal", "Panama", "Abracadabra"],4)