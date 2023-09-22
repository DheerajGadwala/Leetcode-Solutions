class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        
        def res(i = 0, j = 0):
            if i == m:
                return True
            elif j == n:
                return False
            elif s[i] == t[j]:
                return res(i+1, j+1)
            else:
                return res(i, j+1)
        
        return res()