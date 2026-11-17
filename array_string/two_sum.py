def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [seen[diff], i]
        seen[val] = i
    return []

print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))