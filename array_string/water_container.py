def maxArea( height: list[int]) -> int:
    l, r = 0, len(height) - 1
    best = 0
    while l < r:
        l_height = height[l]
        r_height = height[r]
        # area = container * distance
        water =  min(l_height, r_height) * (r - l) 
        best = max(best, water)
        # move the short wall
        if l_height < r_height:
            l += 1
        else:
            r -= 1
    return best

print(maxArea([1,8,6,2,5,4,8,3,7]))