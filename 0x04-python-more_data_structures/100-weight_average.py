#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    weight = 0
    average = 0
    i = 0

    if len(my_list) == 0:
        return 0

    while i < len(my_list):
        total += (my_list[i][0] * my_list[i][1])
        weight += my_list[i][1]
        i += 1

    average = total / weight
    return average
