#!/bin/python3

import sys

def lonely_integer(a):
    """
    Using bit manipulation determine integer < 100 that is unique in array
    """
    index = 1 << 100
    for x in a:
        x_mask = 1 << x
        index ^= x_mask

    index ^= 1 << 100

    unpaired_number = 0
    while (index & 1) == 0:
        index = index >> 1;
        unpaired_number += 1

    return unpaired_number


# n = int(input().strip())
# a = [int(a_temp) for a_temp in input().strip().split(' ')]
# print(lonely_integer(a))

print(lonely_integer([0, 0, 1, 2, 2, 3, 1]))
