# search in rotated sorted array
# In a rotated sorted array, one half is sorted and the other is not.
# Check which half is sorted and then check if the target is in that half.
# If not, check the other half.

def searchRotatedArray( nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1      # target is in the sorted left half
            else:
                l = mid + 1      # target must be in the right half
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1      # target is in the sorted right half
            else:
                r = mid - 1      # target must be in the left half

    return -1

print(searchRotatedArray([4,5,6,7,0,1,2], 0))
print(searchRotatedArray([4,5,6,7,0,1,2], 3))
print(searchRotatedArray([1], 0))