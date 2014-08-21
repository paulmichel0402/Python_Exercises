def correct(strIn):
	retStr = ''
	ctr = 0
	for i in range(len(strIn)):
		i += ctr
		if strIn[i] == ' ':
			while strIn[i] == ' ':
				ctr += 1
			retStr += ' '
		elif (strIn[i] == '.' and strIn[i+1] != ' '):
			retStr += '. '
		else:
			retStr += strIn[i]
	return retStr
print correct('This   is  very funny  and    cool.Indeed!')