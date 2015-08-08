#problem found here: https://projecteuler.net/problem=1
#Basically asks us to find the multiples of 3 and 5 in the range of 1-1000, and the sum


sum = 0 #this is here for the end result

for x in range(1, 1000):
	if x % 3 == 0 or x % 5 == 0: #don't forget to add the "==0" to the "x % 3 == 0"
	#if x % 3 or x % 5 == 0: is completely different statement. x % 3 doesn't equate to anything. Code will work, but not correctly!
		sum += x

print "The sume of all the multiples of 3 and 5 between 1-1000 is %r" % sum