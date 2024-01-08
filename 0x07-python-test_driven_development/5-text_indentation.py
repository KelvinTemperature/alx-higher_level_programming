#!/usr/bin/python3
"""Module to handle print by special characters"""


def text_indentation(text):
    """
        Function to print text by indenting them 
        at special characters . ? :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sen = ""
    spch = ['.', '?', ':']
    i = 0

    while i < len(text):
        sen += text[i]
        if text[i] in spch:
            sen += '\n'
            i += 2
            continue
        i += 1

    print(sen, end='')
