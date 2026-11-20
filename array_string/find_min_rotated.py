# find minimum in rotated sorted array
# [3,4,5,1,2] -> 1, rotated 3 times
# [4,5,6,7,0,1,2] -> 0, rotated 4 times
# [11,13,15,17] -> 11, not rotated

def findMin(nums: list[int]) -> int:
    return min(nums)

print(findMin([3,4,5,1,2]))
print(findMin([4,5,6,7,0,1,2]))
print(findMin([11,13,15,17]))