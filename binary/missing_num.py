# sum of n mumbers = n(n+1) // 2
# def missingNumber( nums: list[int]) -> int:
#   n = len(nums)
#   return n * (n + 1) // 2 - sum(nums)


# XOR, a ^ a = 0 and a ^ 0 = a
def missingNumber( nums: list[int]) -> int:
    result = len(nums)
    for i, x in enumerate(nums):
        result ^= i ^ x
    return result