def is_solution(xs, s):
    return sum(xs) == s

def is_viable(xs, s):
    return sum(xs) <= s

def sumSubsets(xs, s):
    subsets = [xs]
    result = []

    while subsets:
        current = subsets.pop()
        current_sum = sum(current)

        if current_sum == s:
            sorted_current = sorted(current)
            if not sorted_current in result:
                result.append(sorted_current)
            continue

        for i, x in enumerate(current):
            if x > s:
                continue
            if x + current_sum >= s:
                subsets.append(current[:i] + current[i+1:])

    return sorted(result)


# print(sumSubsets([1, 2, 3, 4, 5], 5))
# print(sumSubsets([1, 1, 1, 1, 1, 1, 1, 1, 1], 9))

print(sumSubsets([1, 1, 2, 2, 2, 5, 5, 6, 8, 8], 9))

# import cProfile
# cProfile.run('sumSubsets([1, 1, 2, 4, 4, 4, 7, 9, 9, 13, 13, 13, 15, 15, 16, 16, 16, 19, 19, 20], 36)')

# print(sumSubsets([1, 1, 2, 4, 4, 4, 7, 9, 9, 13, 13, 13, 15, 15, 16, 16, 16, 19, 19, 20], 36))
