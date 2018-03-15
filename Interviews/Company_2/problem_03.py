
def solution(xs):
    unsorted_groups = []

    j = 0
    for i in range(len(xs) - 1):
        if xs[i] < xs[i+1]:
            unsorted_groups.append(xs[j:i+1])
            j = i + 1

    unsorted_groups.append(xs[j:])
    print(unsorted_groups)

    return len(unsorted_groups)

def get_unsorted_groups(xs):
    unsorted_groups = []

    j = 0
    for i in range(len(xs) - 1):
        if xs[i] < xs[i+1]:
            unsorted_groups.append(xs[j:i+1])
            j = i + 1

    unsorted_groups.append(xs[j:])

    return unsorted_groups

def get_group_min(groups):
    group_minimals = {}

    def find_group_min(i):
        if i in group_minimals:
            min_i_group = group_minimals[i]
        else:
            min_i_group = min(groups[i])
            group_minimals[i] = min_i_group

        return min_i_group

    return find_group_min



def solution(xs):
    unsorted_groups = get_unsorted_groups(xs)
    result = len(unsorted_groups)

    min_groups = {}

    get_min = get_group_min(unsorted_groups)

    for i, group in enumerate(unsorted_groups):
        min_i_group = get_min(i)

        for j in range(i - 1, -1, -1):
            min_j_group = get_min(j)

            if min_i_group < min_j_group:
                result -= 1

    return result




# print(solution([1, 5, 4, 9, 8, 7, 12, 13, 14]))
# print(solution([5, 4, 9, 8, 7, 12, 13, 14, 1]))
print(solution([4, 3, 2, 6, 1]))
# print(solution([4, 3, 2, 6, 1, 7, 8]))
