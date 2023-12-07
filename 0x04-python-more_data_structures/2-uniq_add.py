#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_set = 0
    for n in set(my_list):
        sum_set += n
    return sum_set
