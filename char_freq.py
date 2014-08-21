def char_freq(strIn):
	char_freqs = {}
	for char in strIn:
		if char_freqs.has_key(char):
			char_freqs[char] += 1
		else:
			char_freqs[char] = 1
	return char_freqs

print char_freq("abbabcbdbabdbdbabababcbcbab")

def cipher(strIn):
	key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

	retStr = ''
  	for char in strIn:
  		if key.has_key(char):
  			retStr += key[char]
		else:
			retStr += char
	return retStr
print cipher("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!")

