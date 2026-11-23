def hammingWeight(n: int) -> int:
    count = 0
    while n:
        count += n & 1   # is the lowest bit 1?
        n >>= 1          # drop it
    return count

print(hammingWeight(11))
print(hammingWeight(128))