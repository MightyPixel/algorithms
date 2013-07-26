"""
The task is to compute the number of inversions in the file given,
where the i-th row of the file indicates the i-th entry of an array.
"""

counter = 0

# load example array conatining 10000 numbers
inputFile = "QuickSort.txt"
f = open(inputFile)
array = []
for number in f:
    array.append(int(number))


def partition(array, l, r):
    """
    swaps elements such that the [l] element is at it's final position
    once the partision is done partitioning
    """
    i = l + 1
    for j in range(l+1, len(array)):
        if array[j] < array[l]:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[l], array[i-1] = array[i-1], array[l]
    return i-1




def quickSort(array):
    """
    Main Quicksort function
    Uses global variable counter to count the comperations

    Complexity: nlogn

    Arguments: Array - array that will be sorted
    Result: Sorted Array
    """
    global counter
    if len(array) <= 1:
        return array
    else:
        # Find pivot
        critical_points = [array[0], array[-1], array[(len(array) - 1)/2]]
        critical_points.sort()
        pivot = array.index(critical_points[1])

        array[pivot], array[0] = array[0], array[pivot] # Swap pivot with the first element
        pivot = partition(array, 0, len(array))

        counter += pivot - 1
        counter += len(array) - pivot
        left = quickSort(array[:pivot])
        right = quickSort(array[pivot+1:])

        return left + [array[pivot]] + right
