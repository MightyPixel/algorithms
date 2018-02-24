
def memoize(f):
    cache = {}

    def memoized_f(n):
        if n in cache:
            return cache[n]
        else:
            result = f(n)
            cache[n] = result

            return result

    return memoized_f


@memoize
def climbingStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return climbingStairs(n - 1) + climbingStairs(n - 2)


def test(n, expected):
    print('#########')
    print(n)
    result = climbingStairs(n)
    print(result, '==', expected, result == expected)

test(4, 5)
test(5, 8)
test(23, 46368)
test(20, 10946)
test(17, 2584)
test(13, 377)
test(28, 514229)
test(38, 63245986)
