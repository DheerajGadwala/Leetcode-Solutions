class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        @cache
        def res(i = 0, j = 0):
            if i == m and j == n:
                return 0
            elif i == m:
                return ord(s2[j]) + res(i, j+1)
            elif j == n:
                return ord(s1[i]) + res(i+1, j)
            elif s1[i] == s2[j]:
                return res(i+1, j+1)
            else:
                return min(ord(s1[i]) + res(i+1, j), ord(s2[j]) + res(i, j+1))
        return res()