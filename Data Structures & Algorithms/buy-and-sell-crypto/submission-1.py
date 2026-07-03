class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # buy = prices[0]
        # maxProfit = 0
        # for sell in range(1, len(prices)):
        #     buy = min(buy, prices[sell])
        #     profit = prices[sell] - buy
        #     maxProfit = max(maxProfit, profit)

        # return maxProfit

        max_profit = 0
        buy = prices[0]

        for sell in prices:
            profit = sell - buy
            max_profit = max(max_profit, profit)
            buy = min(buy, sell)
        
        return max_profit