class Solution:
    def countGoodStrings(self, l: int, h: int, zero: int, one: int) -> int:
        
        MOD = 10**9+7
        
        @cache
        def res(le = 0):
            if le > h:
                return 0
            elif le < l:
                return (res(le+zero) + res(le+one)) % MOD
            else:
                return (1 + res(le+zero) + res(le+one)) % MOD
        
        return res()