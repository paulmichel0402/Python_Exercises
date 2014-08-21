def is_member(lookFor, list):
	for elt in list:
		if elt == lookFor:
			return True
	return False
print is_member("dog", ["What", "to", "look", "for"])

def overlapping(listA,listB):
	for elt1 in listA:
		for elt2 in listB:
			if elt1 == elt2:
				return True
	return False
print overlapping([1,2,3,4], [4,5,6,7])
print overlapping(["What's", "up?"], ["Not", "much."])