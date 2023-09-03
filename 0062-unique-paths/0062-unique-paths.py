class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def res(i = 0, j = 0):
            if i == m or j == n:
                return 0
            elif i == m - 1 and j == n - 1:
                return 1
            else:
                return res(i + 1, j) + res(i, j + 1)
        
        return res()