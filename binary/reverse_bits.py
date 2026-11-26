def reverseBits( n: int) -> int:
    res = 0
    for i in range(32):
        bit = (n >> i)&1  # read the bit at position i
        if bit == 1 :
            res += (bit << (31-i)) # place it at position 31 - i
    return res

print(43261596)