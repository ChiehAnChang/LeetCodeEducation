from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max      = 0    # best “sell” price seen so far (to our right)
        curr_max_profit = 0  # best profit seen so far
        i = len(prices) - 1

        while i >= 0:

            # “If we bought at price[i] and sold later at curr_max,
            #  how much would we make?”
            if curr_max - prices[i] > curr_max_profit:
                curr_max_profit = curr_max - prices[i]

            # “Is today’s price a better sell‐point than any we’ve seen?”
            if prices[i] > curr_max:
                curr_max = prices[i]

            i -= 1

        return curr_max_profit



