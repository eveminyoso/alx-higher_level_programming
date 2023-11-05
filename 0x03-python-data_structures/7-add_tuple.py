#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = (0,)
    j = (0, 0)

    if len(tuple_a) > 2:
        tuple_a = tuple_a[:2]
    if len(tuple_b) > 2:
        tuple_b = tuple_b[:2]
    tuple_a
    tuple_b
    if len(tuple_a) == 1:
        tuple_a = tuple_a + i
        t_a = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return t_a
    elif len(tuple_b) == 1:
        tuple_b = tuple_b + i
        t_a = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return t_a
    elif len(tuple_a) == 0:
        tuple_a = j
        t_a = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return t_a
    elif len(tuple_b) == 0:
        tuple_b = j
        t_a = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return t_a
    else:
        t_a = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return t_a
