def solution(xs):
    n = len(xs) + 1

    positive_numbers = [0] * n

    for x in xs:
        if 0 < x <= n:
            positive_numbers[x - 1] += 1

    for i, count in enumerate(positive_numbers):
        if count == 0:
            return i + 1

    return 1



print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
