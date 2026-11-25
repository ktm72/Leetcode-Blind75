def countBits( n: int) -> list[int]:
    ans = [0] * (n + 1)  # ans[0] = 0 is the base case
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1) # repeating count + last bit
    return ans


# i	binary	bits
# 2	10	1
# 3	11	2
# 4	100	1
# 5	101	2
# 6	110	2
# 7	111	3

# Shifting right by one (i >> 1, same as i // 2) drops the last bit. 
# So i is just i >> 1 plus one extra bit at the end:

# 6 = 110 → 6 >> 1 = 3 = 11, last bit is 0 → bits[6] = bits[3] + 0
# 7 = 111 → 7 >> 1 = 3 = 11, last bit is 1 → bits[7] = bits[3] + 1


# def countBits(self, n: int) -> list[int]:
#     ans = [0] * (n + 1)              # ans[0] = 0 is the base case
#     for i in range(1, n + 1):        # start at 1, never 0
#         ans[i] = ans[i & (i - 1)] + 1
#     return ans