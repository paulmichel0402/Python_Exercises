def max(m,n):
	if m >= n:
		return m
	else:
		return n

firstNum = int(raw_input("Type the first number:"))
secondNum = int(raw_input("Type the second number:"))

print str(max(firstNum,secondNum))

def max_of_three(l,m,n):
	if (l >= m and l >= n):
		return l
	elif m >= l and m >= n:
		return m
	else:
		return n
firstNum = int(raw_input("Type the first number:"))
secondNum = int(raw_input("Type the second number:"))
thirdNum = int(raw_input("Type the third number:"))

print str(max(firstNum, secondNum, thirdNum))