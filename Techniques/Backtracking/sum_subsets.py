def is_solution(xs, s):
    return sum(xs) == s

def is_viable(xs, s):
    return sum(xs) <= s

def sumSubsets(xs, s):
    subsets = [[]]
    result = []

    while subsets:
        current = subsets.pop()

        if sum(current) == s:
            sorted_current = sorted(current)
            if not sorted_current in result:
                result.append(sorted_current)
            continue

        excluded_xs = xs[:]
        for x in current:
            excluded_xs.remove(x)

        for x in excluded_xs:
            if x > s:
                break

            new_state = current + [x]

            if sum(new_state) <= s:
                subsets.append(new_state)

    return sorted(result)


print(sumSubsets([1, 2, 3, 4, 5], 5))
import cProfile
cProfile.run('sumSubsets([1, 1, 2, 4, 4, 4, 7, 9, 9, 13, 13, 13, 15, 15, 16, 16, 16, 19, 19, 20], 36)')

print(sumSubsets([1, 1, 2, 4, 4, 4, 7, 9, 9, 13, 13, 13, 15, 15, 16, 16, 16, 19, 19, 20], 36))
