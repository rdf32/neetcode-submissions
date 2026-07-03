class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        buy = prices[0]
        for sell in prices:
            profit = sell - buy
            max_profit = max(max_profit, profit)
            buy = min(buy, sell)
        
        return max_profit