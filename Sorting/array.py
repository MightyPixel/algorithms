arrays = [
    [6, 2, 3, 1, 9, 0, 5],
    [1, 2, 3, 5, 4, 5, 6, 7, 8, 7, 8, 9, 10]
]

def insertion_sort(xs):
    """
    Stable
    Space O(1)
    Time O(n^2)
    Adaptive O(n) when nearly sorted
    """
    for i in range(len(xs)):
        for j in range(i, 0, -1):
            if xs[j] > xs[j - 1]:
                break

            xs[j], xs[j - 1] = xs[j - 1], xs[j]

    return xs

def selection_sort(xs):
    """
    Not stable
    Space O(1)
    Time O(n^2)
    Low number of swaps O(n)
    Not adaptive
    """
    n = len(xs)
    for i in range(n):
        k = i
        for j in range(i + 1, n):
            if xs[j] < xs[k]:
                k = j

        xs[i], xs[k] = xs[k], xs[i]

    return xs

def bubble_sort(xs):
    """
    Stable
    Space O(1)
    Time O(n^2)
    Adaptive O(n) when nearly sorted
    """
    n = len(xs)
    for i in range(n):
        ordered = True
        for j in range(n - 1, i, -1):
            if xs[j] < xs[j-1]:
                ordered = False
                xs[j-1], xs[j] = xs[j], xs[j-1]
        if ordered:
            break

    return xs

def merge_sort(xs):
    """
    Stable
    Space O(n)
    Time O(nlogn)
    Not adaptive
    Good for linked list
    """
    n = len(xs)

    if n <= 1:
        return xs

    mid = n//2
    left = merge_sort(xs[:mid])
    right = merge_sort(xs[mid:])

    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    result += left
    result += right

    return result


sorting_methods = [insertion_sort, selection_sort, bubble_sort, merge_sort]

for method in sorting_methods:
    for array in arrays:
        result = method(array[:])
        if result == sorted(array):
            print(method.__name__, 'Works')
        else:
            print(method.__name__, 'Does not work')

        print(array)
        print(result)
