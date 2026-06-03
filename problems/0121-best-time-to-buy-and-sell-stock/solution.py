class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = prices[0]
        for i in prices:
            if i < lowest:
                lowest = i
            profit = i - lowest
            max_profit = max(profit,max_profit) 
        return max_profit