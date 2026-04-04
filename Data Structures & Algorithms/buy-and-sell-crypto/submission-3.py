class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we have to start somewhere
        min_val, diff, max_diff, min_i, max_i = 1000, -1, -1, -1, 1000
        # we will go through the list once
        for i, p in enumerate(prices):
            # hoping to find the minimum
            if p < min_val:
                min_val, min_i = p, i
            # calculating the diff since the last minimum
            if p > min_val and i > min_i:
                diff = p - min_val
            # storing the biggest difference (there could be intermediate minima!)
            if diff > max_diff:
                max_diff = diff
        # if we were unlucky
        if max_diff < 0:
            max_diff = 0

        return max_diff
            