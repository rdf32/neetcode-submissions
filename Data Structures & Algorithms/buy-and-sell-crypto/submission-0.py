class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        maxProfit = 0
        for sell in range(1, len(prices)):
            buy = min(buy, prices[sell])
            profit = prices[sell] - buy

            maxProfit = max(maxProfit, profit)

        return maxProfit
