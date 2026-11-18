def productExceptSelf( nums: list[int]) -> list[int]:
    n = len(nums)
    left = [1] * n # [1,1,1,1]
    right = [1] * n # [1,1,1,1]
    
    # prefix product
    for i in range(1,n):
        # product of left numbers from i
        left[i] = left[i-1] * nums[i-1]
    
    # suffix product
    for i in range(n-2,-1,-1):
        # product of right numbers from i
        right[i] = right[i+1] * nums[i+1]

    return [left[i] * right[i] for i in range(n)]

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))