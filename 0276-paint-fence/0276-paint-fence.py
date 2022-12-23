class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        @cache
        def res(pos = 1):
            if pos == n: 
                return k
            elif pos == n - 1: 
                return k * k
            else:
                return (k - 1) * res(pos + 1) + 1 * (k - 1) * res(pos + 2)
        
        return res()