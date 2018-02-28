"""
The task is to compute the number of inversions in the file given,
where the i-th row of the file indicates the i-th entry of an array.
"""

#!/bin/python3

import sys


def merge(left, right):
    i = j = 0
    inversions = 0
    merged = []

    left_len = len(left)
    right_len = len(right)

    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            inversions += left_len - i
            merged.append(right[j])
            j += 1

    if i == left_len:
        merged += right[j:]
    if j == right_len:
        merged += left[i:]

    return merged, inversions


def countInversions(arr):
    if len(arr) == 1:
       return arr, 0

    mid = len(arr)//2

    left, left_inv = countInversions(arr[:mid])
    right, right_inv = countInversions(arr[mid:])
    merged, split_inv = merge(left, right)

    return merged, split_inv + left_inv + right_inv

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print(result[1])

