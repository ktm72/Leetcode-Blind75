def hammingWeight(n: int) -> int:
    count = 0
    while n:
        count += n & 1   # is the lowest bit 1?
        n >>= 1          # drop it
    return count

print(hammingWeight(11))
print(hammingWeight(128))


# Brian Kernighan's trick (the "aha" one)
# def hammingWeight(n: int) -> int:
#     count = 0
#     while n:
#         n &= n - 1 # n & (n - 1) clears the lowest set bit.
#         count += 1
#     return count