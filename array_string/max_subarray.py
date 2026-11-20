# Kadane's Algorithm
# At each position, facing one decision:
# extend the previous subarray, or start fresh here?

def maxSubArray(nums):
    cur = best = nums[0]
    for num in nums[1:]:
        cur = max(num, cur + num)   # extend or restart
        best = max(best, cur)   # track global max
    return best


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([5,4,-1,7,8]))


# return the max subarray and the indices
def maxSubArrayWithIndices(nums):
    cur = best = nums[0]
    start = bs = be = 0
    for i in range(1, len(nums)):
        if nums[i] > cur + nums[i]:   # restart
            cur = nums[i]
            start = i
        else:
            cur += nums[i]
        if cur > best:
            best = cur
            bs, be = start, i
    return best, nums[bs:be+1]
    
print(maxSubArrayWithIndices([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArrayWithIndices([5,4,-1,7,8]))