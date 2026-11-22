def getSum(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    MAX = 0x7FFFFFFF

    while b != 0:
        carry = ((a & b) << 1) & MASK # AND = carry bits
        a = (a ^ b) & MASK # XOR = sum bits
        b = carry

    # If a is "negative" in 32-bit terms
    # convert back to Python's negative int
    return a if a <= MAX else ~(a ^ MASK)

print(getSum(0, 1))
print(getSum(4, 7))