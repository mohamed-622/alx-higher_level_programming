#!/usr/bin/python3


def pow(a, b):
    # holds the result of the multiplication
    result = 1
    base = 1
    nb = 0
    # multiply a b times
    if b < 0:
        nb = b
        b = (-1) * b

    for i in range(b):
        result *= a
        base = result * result

    if nb < 0:
        result /= base
    return result
