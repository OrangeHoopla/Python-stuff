def find_anagrams(listq,word1):
	newlist = []
	for word in listq:
		count = 0
		for letter in word:
			
			if letter in word1:
				count += 1
		if count == len(word):
			newlist.append(word)


	return newlist
	

	
     
print find_anagrams(["spare", "hello", "pears", "world", "reaps"], "parse")