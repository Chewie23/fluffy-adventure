from random import randrange
from heapq import nlargest

def organize_and_pull_K_biggest_num(num_of_elem, Kth):
    if Kth <= 0 or Kth > num_of_elem:
        print("That number is out of range!")
        exit(0)
    
    num_list = []
    for n in range(num_of_elem):
        num_list.append(randrange(-100, 100))
    print ("The unsorted list:", num_list)
    
    largest_K_num_list = nlargest(Kth, num_list) #"nlargest" makes a list of the top "K" largest numbers
    Kth_largest_num = largest_K_num_list[Kth - 1]
    print ("The #%d largest number in the list: %d" % (Kth, Kth_largest_num))

try:
    num_of_elem = int(input("Please enter how many numbers you want in the list: "))
    Kth         = int(input("Please enter a nonzero positive integer to determine 'Kth' biggest number: "))
except ValueError:
    print ("That is not a valid input!")
else:
    organize_and_pull_K_biggest_num(num_of_elem, Kth)