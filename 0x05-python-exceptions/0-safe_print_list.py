#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    j = 0
    while i < x:
        try:
            print(my_list[i], end='')
        except IndexError:
            break
        else:
            j += 1
        i += 1
    print()

    return j
