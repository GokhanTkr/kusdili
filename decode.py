def decode(yazi):
	delete = []

	b = 0 # for loop element
	new_list =[]# empty string for rebuilding the word
	new_str = ""

	for i in range(len(yazi)): # for loop for detecting the kusdili rules

		if (yazi[i] == 'g'):# search for g letter

			if(yazi[i+1] in sesliharf):
				
				if(yazi[i-1] in sesliharf):

					delete.append(i-1)
					delete.append(i)
					# if the letters are vowels one before and one after from the letter g; store them in a list

	

	for a in range(len(yazi)): # loop for deleting sequence

		new_list.append(yazi[a])

	for b in range(len(delete)):
		new_list[delete[b]] = ""


	for c in range(len(new_list)):
		new_str = new_str + new_list[c]


	return new_str

###^^^^^^^^^^^^^^^^###

def bruteforce(yazi):
    pass
