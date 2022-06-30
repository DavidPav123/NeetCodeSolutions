class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_best = 0
        best_day = 0
        
        for nums in range(len(prices)):
            for sub_nums in range(len(prices)):
                if (prices[sub_nums] - prices[nums]) > current_best:
                    current_best = (prices[sub_nums] - prices[nums])
                    best_day = prices[sub_nums]

        return best_day