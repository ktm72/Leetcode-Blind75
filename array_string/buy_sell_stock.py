def maxProfit( prices: list[int]) -> int:
    buy = prices[0] # buy at first day
    profit = 0
    for price in prices:
        if price < buy:
            buy = price
        profit = max(profit, price - buy)
    return profit

print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))