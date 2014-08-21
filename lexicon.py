def translate(strIn):
	dictionary = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year" : "ar"}

	wordsList = strIn.split()
	retStr = ""
	for word in wordsList:
		retStr = retStr + " " + dictionary[word]
	return retStr

print translate("merry christmas and happy new year")