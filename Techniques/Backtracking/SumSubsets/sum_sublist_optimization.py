def substract_lists(xs, ys):
    # return xs difference ys
    result = []
    i = j = p = 0
    n = len(xs)
    m = len(ys)

    while i < n and j < m:
        x = xs[i]
        y = ys[j]

        if x == y:
            result += xs[p:i]
            i += 1
            j += 1

            p = i
        elif x < y:
            i += 1
        else:
            j += 1

    if i < len(xs):
        result += xs[i:]

    return result


def sumSubsets(xs, s):
    subsets = [[]]
    result = []

    while subsets:
        current = subsets.pop()
        current_sum = sum(current)

#        print(current, current_sum)

        if current_sum == s:
            sorted_current = sorted(current)
            if not sorted_current in result:
                result.append(sorted_current)
            continue

        # excluded_xs = substract_lists(xs, current)
        excluded_xs = xs[:]
        for x in current:
            excluded_xs.remove(x)

        for x in excluded_xs:
            if current_sum + x > s:
                break
            else:
                subsets.append(current + [x])

    return sorted(result)


# print(substract_lists([1, 2, 3, 4, 5], [2, 4]))

# print(sumSubsets([1, 2, 3, 4, 5], 5))
# import cProfile
# cProfile.run('sumSubsets([1, 1, 2, 4, 4, 4, 7, 9, 9, 13, 13, 13, 15, 15, 16, 16, 16, 19, 19, 20], 36)')
# print(sumSubsets([1, 1, 2, 4, 4, 4, 7, 9, 9, 13, 13, 13, 15, 15, 16, 16, 16, 19, 19, 20], 36))
print(sumSubsets([1, 1, 2, 2, 2, 5, 5, 6, 8, 8], 9))
