def max_in_list(listNum):
	def get_max(x,y):
		if x > y: 
			return x
		else: 
			return y
	return reduce(get_max, listNum)
print max_in_list([1,2,4,545,342,353])
