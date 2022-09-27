class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        if s % 4 != 0 or max(matchsticks) > s // 4:
            return False
        s //= 4
        n = len(matchsticks)
        allUsed = sum([2**i for i in range(n)])
        
        @cache
        def dp(mask = 0, side = s):
            if mask == allUsed:
                return side == 0
            elif side == 0:
                return dp(mask)
            elif side < 0:
                return False
            else:
                i = 1
                ret = False
                for j in range(n):
                    if (mask & i) == 0:
                        ret |= dp(mask|i, side-matchsticks[j])
                    i <<= 1
                return ret
        
        return dp()