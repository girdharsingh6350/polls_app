
test_str = "occurence"

dict = {}

for i in test_str:
	if i in dict:
		dict[i] += 1
	else:
		dict[i] = 1


print ("Count of all characters in occurence is :\n "
										+ str(dict))
