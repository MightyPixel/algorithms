def climbingStaircase(n, k):
    stack = [[]]
    result = []

    while stack:
        current = stack.pop()

        climbed_steps = sum(current)
        if n == climbed_steps:
            result += [current]

        for i in range(k, 0, -1):
            if i + climbed_steps <= n:
                stack += [current + [i]]

    return result


def test(n, k):
    print('#########')
    print(n, k)
    print(climbingStaircase(n, k))

test(4, 2)
test(4, 1)
test(7, 3)
test(0, 0)
test(1, 1)
test(2, 2)
