def maxProduct( nums: list[int]) -> int:
    product = curr_max = curr_min = nums[0]
    # first value has taken already
    for num in nums[1:]:
        # think about positive product value
        candidates = (num, curr_max * num, curr_min * num)
        curr_max = max(candidates)
        curr_min = min(candidates)
        product = max(product, curr_max)
    return product

print(maxProduct([2,3,-2,4]))
print(maxProduct([-2,0,-1]))

# def maxProduct( nums: list[int]) -> int:
#     result = nums[0]
#     prefix = suffix = 1
#     n = len(nums)
#     for i in range(n):
#         # leave the segment if hits 0 from left side, start again from 1
#         prefix = (prefix or 1) * nums[i] 
#         suffix = (suffix or 1) * nums[n - 1 - i]
#         result = max(result, prefix, suffix)
#     return result