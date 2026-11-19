# Kadane's Algorithm
# At each position, face one decision:
# extend the previous subarray, or start fresh here?

def maxSubArray(nums):
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)   # extend or restart
        best = max(best, cur)   # track global max
    return best

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([5,4,-1,7,8]))