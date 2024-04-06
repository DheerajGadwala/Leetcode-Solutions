class Solution:
    def maxBottlesDrunk(self, n: int, x: int) -> int:
        
        def res(n=n, x=x):
            if n < x:
                return n
            else:
                return x + res(n-x+1, x+1)
        
        return res()