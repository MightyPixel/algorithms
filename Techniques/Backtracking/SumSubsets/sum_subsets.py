def sum_subsets(xs, s):
    subsets = [[]]
    result = []

    while subsets:
        current = subsets.pop()
        current_sum = sum(current)

        if current_sum == s: # is solution
            sorted_current = sorted(current) # called rarely - [1, 4] and [4, 1] are the same
            if not sorted_current in result:
                result.append(sorted_current)
            continue

        excluded_xs = [x for x in xs if x not in current]

        # All decisions from current
        for x in excluded_xs:
            if x > s: # pruning
                break

            new_state = current + [x]

            if sum(new_state) <= s: # is viable
                subsets.append(new_state)

    return sorted(result)


print(sum_subsets([1, 2, 3, 4, 5], 5))

# Source https://people.sc.fsu.edu/~jburkardt/datasets/subset_sum/subset_sum.html
big_example = [518533,1037066,2074132,1648264,796528,1593056,686112,1372224,244448,488896,977792,1955584,1411168,322336,644672,1289344,78688,157376,314752,629504,1259008]
big_example_target = 2463098
print(sum_subsets(big_example, big_example_target))


