#!/usr/bin/python3
def best_score(a_dictionary):
    temp_list = []

    if a_dictionary == {} or a_dictionary is None:
        return None

    for k in a_dictionary:
        temp_list.append(a_dictionary[k])

    best_score = max(temp_list)

    for k, v in a_dictionary.items():
        if v == best_score:
            return k
