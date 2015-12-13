def convert_roman_num_to_int(user_input): 
    total              = 0
    previous_value     = 0 #this is a intermediate variable, to help keep tabs on corner cases such as IX or CM
    rom_num_dictionary = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    
    for letter in user_input:
        if rom_num_dictionary[letter] > previous_value:
            total -= previous_value
        else:
            total += previous_value
        previous_value = rom_num_dictionary[letter]
    
    total += previous_value
    return total

try:
    roman_num = input("Please enter a Roman Numeral below MMMMCMXCIX: ")
    print (convert_roman_num_to_int(roman_num))
except KeyError:
    print("That is not a valid input!")   
    