#!/usr/bin/python3
"""Module to find the peak of a list"""

def find_peak(list_of_integers):
    """Function to find the peak of list_of_integers"""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
