def reverse_string(user_string):
    user_string = user_string.split()
    user_string.reverse()
    reversed_str = " ".join(user_string)
    print(reversed_str)

try:
    num_of_strings = int(input("Please enter how many strings you want to type: "))
    count          = 0
except ValueError:
    print("That is not a valid input!")
else:
    if num_of_strings <= 0:
        print("That is not a valid input!")
    else:
        for n in range(num_of_strings):
            count += 1
            actual_string = input(("Please enter your #%d string: ") % count)
            reverse_string(actual_string)