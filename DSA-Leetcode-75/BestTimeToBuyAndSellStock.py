# 121. Best Time to Buy and Sell Stock
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

def maxProfit(self, prices: list) -> int:
    left = 0
    right = 1
    max_profit = 0
    n = len(prices)
    while right < n:
        profit = prices[right] - prices[left]
        if profit < 0:
            left = right
        max_profit = max(max_profit, profit)
        right += 1
    return max_profit