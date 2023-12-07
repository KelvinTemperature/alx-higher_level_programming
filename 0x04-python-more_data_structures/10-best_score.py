#!/usr/bin/python3
def best_score(a_dictionary):
    temp_dict = []
    i = 0
    if a_dictionary(sorted(a_dictionary)[i]) < a_dictionary(sorted(a_dictionary)[i + 1]):
        temp_dict[i] = a_dictionary(sorted(a_dictionary)[i])
