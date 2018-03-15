# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(salad_places, pizza_places, cake_places):
    # sort places
    # for salad place
    # for pizza place
    # for cake place
    # make a journey
    # time O(n^3)

    salad_places.sort()
    pizza_places.sort()
    cake_places.sort()

    journey_count = 0

    for salad_place in salad_places:
        for pizza_place in pizza_places:
            if pizza_place <= salad_place:
                continue
            for cake_place in cake_places:
                if cake_place <= pizza_place:
                    continue

                if journey_count > 1000000000:
                    return -1

                journey_count += 1

    return journey_count



def solution2(A, B, C):
    salad_places = sorted(A)
    pizza_places = sorted(B)
    cake_places = sorted(C)

    journeys = []

    for salad_place in salad_places:
        for pizza_place in pizza_places:
            if pizza_place <= salad_place:
                continue
            for cake_place in cake_places:
                if cake_place <= pizza_place:
                    continue

                if len(journeys) > 1000000000:
                    return -1

                journeys.append([salad_place, pizza_place, cake_place])

    return len(journeys)

print(solution([29, 50], [61, 37], [37, 70]))
