class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def res(pos = 0, buy = True, k = k):
            if k == 0 or pos == n:
                return 0
            elif buy:
                return max(-prices[pos]+res(pos+1, False, k), res(pos+1, True, k))
            else:
                return max(prices[pos]+res(pos+1, True, k-1), res(pos+1, False, k))
        return res()
                