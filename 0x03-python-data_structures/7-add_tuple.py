#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    x = list(tuple_a)
    y = list(tuple_b)

    if len(x) < 1:
        x.append(0)
        x.append(0)
    if len(x) < 2:
        x.append(0)
    if len(y) < 1:
        y.append(0)
        y.append(0)
    if len(y) < 2:
        y.append(0)

    new_tuple = (x[0] + y[0], x[1] + y[1])

    return new_tuple
