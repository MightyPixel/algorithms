
def get_sorted_groups(xs):
    sorted_groups = []

    j = 0
    for i in range(len(xs) - 1):
        if xs[i] > xs[i+1]:
            sorted_groups.append(xs[j:i+1])
            j = i + 1

    sorted_groups.append(xs[j:])

    return sorted_groups


def merge_sorted_groups(sorted_groups):
    sorted_result = []

    not_empty_groups = sorted_groups
    while not_empty_groups:
        first_elements = [g[0] for g in not_empty_groups]
        i, min_element = min(enumerate(first_elements), key=lambda e: e[1])
        sorted_result.append(min_element)

        not_empty_groups[i] = not_empty_groups[i][1:]
        not_empty_groups = [group for group in not_empty_groups if group]

    return sorted_result

def sort(xs):
    sorted_groups = get_sorted_groups(xs)

    return merge_sorted_groups(sorted_groups)



print(get_sorted_groups([1, 2, 6, 4, 5]))
print(merge_sorted_groups(get_sorted_groups([1, 2, 6, 4, 5])))

print(sort([1, 2, 6, 4, 5]))
print(sort([1, 2, 6, 4, 5, 3]))
print(sort([9, 2, 6, 4, 5, 3]))
print(sort([42]))
print(sort([9, 8, 7, 1, 2, 3]))
print(sort([9, 8, 7, 1, -2, 3]))

