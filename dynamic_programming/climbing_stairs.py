def climbStairs( n: int) -> int:
    # looks like fibonacci problem
    memo = {}

    def f(k):
        if k <= 1:
            return 1
        if k in memo:
            return memo[k]
        memo[k] = f(k - 1) + f(k - 2)
        return memo[k]

    return f(n)