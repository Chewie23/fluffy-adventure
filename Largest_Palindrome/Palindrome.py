"""
Problem: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palidrome(product):
    product_string = str(product)
    valid_palindrome = True
    
    for n in range(len(product_string)): #checks if palindrome! Now need to find biggest one!
        if product_string[n] != product_string[len(product_string) - 1 - n]:
            valid_palindrome = False
            
    return valid_palindrome

def find_largest_palindrome(bottom, top):
    for x in range(bottom, top):
        for y in range(bottom, top):
            product = x * y
            if is_palidrome(product):
                biggest = product
                factor_1 = x
                factor_2 = y
    print ("%d is the biggest palindrome. It is the product between %d and %d." % (biggest, factor_1, factor_2))
    
find_largest_palindrome(900, 1000)