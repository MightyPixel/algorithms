"""
The task is to compute the number of inversions in the file given,
where the i-th row of the file indicates the i-th entry of an array.
"""

import sys
sys.setrecursionlimit(1000000)

inputFile = "QuickSort.txt"

f = open(inputFile)
array = []
for number in f:
    array.append(int(number))


def choosePivotIndexStrategyOne(array):
    return 0


def choosePivotIndexStrategyTwo(array):
    return len(array) - 1


def partition(array, l, r):
    i = l + 1
    for j in range(l+1, len(array)):
        if array[j] < array[l]:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[l], array[i-1] = array[i-1], array[l]
    return i-1


counter = 0

def quickSort(array):
    global counter
    if len(array) <= 1:
        return array
    else:
#        print array
        #pivot = len(array) - 1#choosePivotIndexStrategyOne(array)
        critical_points = [array[0], array[-1], array[(len(array) - 1)/2]]
        critical_points.sort()
        pivot = array.index(critical_points[1])
#        print "pivot", array[pivot]
        array[pivot], array[0] = array[0], array[pivot]
        pivot = 0
#        print array
        pivot = partition(array, pivot, len(array))
#        print array

        counter += pivot - 1
        counter += len(array) - pivot
        left = quickSort(array[:pivot])
        #print "left", left
        right = quickSort(array[pivot+1:])
        #print "right", right
        return left + [array[pivot]] + right


print "Total comperations:", counter

"""
counter = 0

def partition(list, l, e, g):
    if list == []:
        return (l, e, g)
    else:
        @global counter
        head = list[0]
        if head < e[0]:
            counter +=
            return partition(list[1:], l + [head], e, g)
        elif head > e[0]:
            return partition(list[1:], l, e, g + [head])
        else:
            return partition(list[1:], l, e + [head], g)

"""
