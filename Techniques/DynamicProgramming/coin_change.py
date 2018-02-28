#!/bin/python3

import sys


def memoize(f):
    cache = {}

    def memoized_f(coins, n):
        index = tuple([n] + coins)
        if index in cache:
            return cache[index]
        else:
            result = f(coins, n)
            cache[index] = result

            return result

    return memoized_f


@memoize
def make_change(coins, n):
    if n <= 0 or not coins:
        return 0

    if coins[0] > n:
        return make_change(coins[1:], n)

    if coins[0] == n:
        return 1 + make_change(coins[1:], n)

    return make_change(coins, n - coins[0]) + make_change(coins[1:], n)


# n,m = input().strip().split(' ')
# n,m = [int(n),int(m)]
# coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
# print(make_change(sorted(coins), n))

print(make_change(sorted([1, 2, 3], reverse=True), 4))
print(make_change(sorted([1, 2, 3, 4], reverse=True), 4))
print(make_change(sorted([2, 5, 3, 6], reverse=True), 10))
