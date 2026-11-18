# This works like counting multiple occurences of a number
# def containsDuplicate( nums: list[int]) -> bool:
#     map = {}
#     for num in nums:
#         if num in map:
#             return True
#         map[num]= 1
#     return False

def containsDuplicate( nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))