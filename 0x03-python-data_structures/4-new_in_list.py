#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_list = my_list.copy()
    if idx < 0:
        return cp_list
    if idx > len(cp_list) - 1:
        return cp_list
    else:
        cp_list[idx] = element
        return cp_list
