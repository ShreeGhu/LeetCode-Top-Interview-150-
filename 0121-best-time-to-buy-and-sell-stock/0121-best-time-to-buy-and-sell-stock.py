class Solution(object):
    def maxProfit(self, prices):
        
        left, right = 0, 1
        max_profit = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right +=1
        return max_profit
            
            
            
            
        """
        :type prices: List[int]
        :rtype: int
        """
        