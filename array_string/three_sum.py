def threeSum(nums):
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n - 2):
        if nums[i] > 0:
            break
        # already used as the first element, 
        # so any triplet starting with it is a repeat.
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            # need a bigger number, move right
            if total < 0:
                left += 1
            # need a smaller number, move left
            elif total > 0:
                right -= 1
            # found a triplet
            else:
                # add to result
                res.append([nums[i], nums[left], nums[right]])
                # move left and right pointers
                left += 1
                right -= 1
                # exactly the value we used on left
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                # exactly the value we used on right
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return res

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,0,0,0]))
print(threeSum([-2,0,1,1,2]))
print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([-1,0,1,2,-1,-4]))


from collections import Counter

def threeSum( nums: list[int]) -> list[list[int]]:
    counts = Counter(nums)

    # distinct; duplicates in the input never cause repeat work.
    values = sorted(counts)
    res = []

    for i, a in enumerate(values):

        # a is the smallest of the three. If it's positive, all three
        # are positive and the sum can't be 0.
        if a > 0:
            break

        for j in range(i, len(values)):
            b = values[j]

            # The third value is forced by the sum: a + b + c = 0.
            c = -a - b

            # We need b <= c. As b grows, c shrinks, so once c < b
            # it stays that way for every later b. Stop this inner loop.
            if c < b:
                break

            # c isn't in the array at all.
            if c not in counts:
                continue

            # Count how many copies of each value this triplet uses.
            needed = Counter((a, b, c))

            # Valid only if the array has at least that many of each value.
            if all(counts[v] >= k for v, k in needed.items()):
                res.append([a, b, c])

    return res