def countBits( n: int) -> list[int]:
    ans = [0] * (n + 1)  # ans[0] = 0 is the base case
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1) # repeating count + last bit
    return ans