class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def ret(pos = 0, buy = True):
            if pos >= len(prices):
                return 0
            elif buy:
                return max(-prices[pos] + ret(pos+1, False), ret(pos+1, True))
            else:
                return max(prices[pos] + ret(pos+2, True), ret(pos+1, False))
        
        return ret()