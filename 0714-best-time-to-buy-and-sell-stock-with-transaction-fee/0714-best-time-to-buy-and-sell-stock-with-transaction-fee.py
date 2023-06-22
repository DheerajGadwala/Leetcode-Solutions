from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        @lru_cache
        def res(i = 0, holding = False):
            if i == n:
                return 0
            elif holding:
                return max(-fee + prices[i] + res(i + 1, False), res(i + 1, True))
            else:
                return max(res(i + 1, False), - prices[i] + res(i + 1, True))
        return res()