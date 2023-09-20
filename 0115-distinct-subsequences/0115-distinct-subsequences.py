class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        @cache
        def res(i=0, j=0):
            if j == n:
                return 1
            elif i == m:
                return 0
            elif s[i] == t[j]:
                return res(i+1, j+1) + res(i+1, j)
            else:
                return res(i+1, j)
        
        return res()