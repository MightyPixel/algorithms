#!/bin/python3

import sys


def find_price(prices, price, other_then):
    l = 0
    r = len(prices)

    while l < r:
        mid = l + (r-l) // 2
        mid_price = prices[mid][1]

        if mid_price == price and prices[mid][0] != other_then:
            return prices[mid][0]
        if price < mid_price:
            r = mid
        else:
            l = mid+1

    return -1

def solve(arr, money):
    prices = sorted(enumerate(arr), key=lambda x: x[1])
    price_a = price_b = 0

    for i, price_a in prices:
        if price_a >= money:
            continue

        remaining_money = money - price_a

        price_b_index = find_price(prices, remaining_money, i)
        if price_b_index != -1:
            break

    a = i + 1
    b = price_b_index + 1

    if prices[i][1] >= prices[price_b_index][1]:
        return b, a
    else:
        return a, b

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = solve(arr, money)
        print(result[0], result[1], '')
