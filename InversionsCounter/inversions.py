"""
The task is to compute the number of inversions in the file given,
where the i-th row of the file indicates the i-th entry of an array.
"""

inputFile = "IntegerArray.txt"

f = open(inputFile)
array = []
for number in f:
    array.append(int(number))


def merge(left, right):
    i = j = 0
    inversions = 0
    merged = []
    n = len(left) + len(right)
    while len(merged) < n:
        if i == len(left):
            merged += right[j:]
            break
        if j == len(right):
            merged += left[i:]
            break
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            inversions += len(left) - i
            merged.append(right[j])
            j += 1

    return merged, inversions


def countInversions(arr):
    if len(arr) == 1:
       return arr, 0
    left, left_inv = countInversions(arr[:len(arr)/2])
    right, right_inv = countInversions(arr[len(arr)/2:])
    merged, split_inv = merge(left, right)
    return merged, split_inv + left_inv + right_inv


print "The number of inversions is " + countInversions(array)[1]
