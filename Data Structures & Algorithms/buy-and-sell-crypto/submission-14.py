class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we have to start somewhere
        min_val, max_profit = float('inf'), 0
        # we will go through the list once
        for p in prices:
            # hoping to find the minimum
            if p < min_val:
                min_val = p
            # calculating the maximum profit
            elif p - min_val > max_profit:
                max_profit = p - min_val

        return max_profit
            