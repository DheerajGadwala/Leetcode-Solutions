class Solution:
    def canWin(self, currentState: str) -> bool:
        
        cs = 0
        i = 1
        for s in currentState:
            cs <<= 1
            if s == '+':
                cs |= 1
            i <<= 1
        
        @cache
        def res(state = cs):
            winnable = False
            n = 3
            while n <= state:
                if n & state == n:
                    winnable |= not res(state ^ n)
                n <<= 1
            return winnable
        
        return res()
            