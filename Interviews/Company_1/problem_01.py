import sys

def get_most_popular_destination(n):
    destinations = {}

    for i in range(n):
        destination = input()
        if destination in destinations:
            destinations[destination] += 1
        else:
            destinations[destination] = 1

    return max(destinations, key=destinations.get)

n = int(input())
print(get_most_popular_destination(n))
