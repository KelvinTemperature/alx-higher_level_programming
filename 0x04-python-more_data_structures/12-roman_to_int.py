#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num_int = 0

    if not roman_string or roman_string is None:
        return 0

    if len(roman_string) == 0:
        return 0
    elif len(roman_string) == 1:
        return romans[roman_string]
    elif len(roman_string) > 1:
        if romans[roman_string[0]] > romans[roman_string[1]]:
            num_int = romans[roman_string[0]] + romans[roman_string[1]]
        else:
            num_int = romans[roman_string[1]] - romans[roman_string[0]]
        i = 2
        while i < len(roman_string):
            num_int += romans[roman_string[i]]
            i += 1
        return num_int
