#!/usr/bin/env python3
from math import factorial as f
from math import ceil as ceil


def c(a, b):
    return f(a) / (f(b) * f(a - b))


# Global variables for faster computation
r = 6
n = 56
# Probability to get the Additional Number
P_ADD = f(n - r) / (1 * f(n - r - 1))
P_ALL = c(n, r)


def melate(k, additional=False):
    if k == r:
        result = 1/P_ALL
    else:
        result = (c(r, k) * c(n - r, r - k)) / P_ALL
    if additional:
        result = result * (1/P_ADD)

    return ceil(1 / result)


if __name__ == '__main__':
    print("Melate Probability")
    p = 1
    for i in range(6, 1, -1):
        if i == 6:
            print(str(p) + " Place | " + str(i) + " | 1:" + str(melate(i)))
            p += 1
        else:
            print(str(p) + " Place | " + str(i) + "+a | 1:" + str(melate(i, True)))
            p += 1
            print(str(p) + " Place | " + str(i) + " | 1:" + str(melate(i)))
            p += 1
