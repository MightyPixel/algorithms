def memoize(f):
    cache = {}

    def memoized_f(l):
        l = tuple(l)

        if l in cache:
            return cache[l]
        else:
            result = f(l)
            cache[l] = result

            return result

    return memoized_f


@memoize
def houseRobber(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)

    odd_houses = nums[0] + houseRobber(nums[2:])
    even_houses = houseRobber(nums[1:])

    return max(even_houses, odd_houses)


print(houseRobber([]))
print(houseRobber([1]))
print(houseRobber([1, 1, 1]))
print(houseRobber([2, 5, 1]))
print(houseRobber([4, 9, 7, 1]))
print(houseRobber([2, 7, 9, 3, 1]))
print(houseRobber([1, 3, 1, 3, 100]))
print(houseRobber([10, 100, 25, 250, 330]))


