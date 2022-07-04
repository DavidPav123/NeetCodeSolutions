class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        pointer = 0
        for days in range(1, len(prices)):
            if prices[days] < prices[pointer]:
                pointer = days
            max_profit = max(max_profit, prices[days] - prices[pointer])
        return max_profit