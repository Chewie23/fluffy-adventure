done = True

while done:
	x = raw_input("Please enter an awesome number that isn't 42: \n>") #remember that the raw_input's output is a string!
	if x != "42":
		print x
	if x == "42":
		print "You typed in 42!"
		done = False
		break