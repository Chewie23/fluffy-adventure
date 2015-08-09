#!/usr/bin/env python
#Problem can be found here: https://projecteuler.net/problem=2
"""Verbatim: Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
#setting up the list to contain the even Fibonacci numbers
even = []
even_sum = 0

def fib(num): #function to get Fibonacci Sequence
    x = 0
    fib_list = [1, 2]
    for item in range (1, num):
        x = fib_list[item] + fib_list[item-1]
        fib_list.append(x)
    return fib_list
    

for i in fib(100): #finds Fibonacci Sequence's even numbers < 4 million
    if i % 2 == 0: #finds the even numbers
        even_sum += i
    if i > 4000000: #This is here to break out of the loop when the number is greater than 4 million
        break

print "The sum of all even Fibonacci numbers under 4 million is: %r" % even_sum


#Output for above: [2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578]
#4613732
