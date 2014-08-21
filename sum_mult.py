def sum(sumList):
	retSum = 0
	for elt in sumList:
		retSum += elt
	return retSum

def mult(multList):
	retProd = 1
	for elt in multList:
		retProd *= elt
	return retProd

numList = [0,2,3,-4]

print str(sum(numList)) + " " + str(mult(numList))