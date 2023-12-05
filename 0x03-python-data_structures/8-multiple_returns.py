#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        tuple_m = (len(sentence), None)
    else:
        tuple_m = (len(sentence), sentence[0])
    return tuple_m
