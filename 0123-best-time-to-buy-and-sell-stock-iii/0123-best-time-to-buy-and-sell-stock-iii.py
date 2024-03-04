class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0

        n = len(prices)
        left_max_profit = [0] * n
        right_max_profit = [0] * n

        # Calculate maximum profit from left to right
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left_max_profit[i] = max(left_max_profit[i - 1], prices[i] - min_price)

        # Calculate maximum profit from right to left
        max_price = prices[n - 1]
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            right_max_profit[i] = max(right_max_profit[i + 1], max_price - prices[i])

        # Find the maximum total profit by combining profits from both sides
        max_total_profit = 0
        for i in range(n):
            max_total_profit = max(max_total_profit, left_max_profit[i] + right_max_profit[i])

        return max_total_profit
        
        
      