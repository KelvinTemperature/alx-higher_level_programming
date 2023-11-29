#!/usr/bin/python3
def remove_char_at(str, n):
    ret_str = ""
    for i in range(len(str)):
        if i != n:
            ret_str = ret_str + str[i]
    return (ret_str)
