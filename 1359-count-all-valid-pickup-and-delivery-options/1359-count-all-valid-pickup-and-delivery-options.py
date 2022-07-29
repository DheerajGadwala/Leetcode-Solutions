class Solution:
    def countOrders(self, n: int) -> int:
        
        MOD = 1000000007
        
        @cache
        def res(a = n, b = 0):
            if a == 0 and b == 0:
                return 1
            elif a > 0 and b > 0:
                return (a * res(a-1, b+1) + b * res(a, b-1)) % MOD
            elif a > 0:
                return (a * res(a-1, b+1)) % MOD
            else:
                return (b * res(a, b-1)) % MOD
        
        return res()