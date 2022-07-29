class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        ans, ansr = 0, 0
        
        @cache
        def res(i, j):
            nonlocal m, n
            if i + 1 < m and j - 1 > -1 and j + 1 < n and grid[i][j] == 1:
                l = res(i+1, j-1)
                b = res(i+1, j)
                r = res(i+1, j+1)
                return 1 + min(l, b, r)
            else:
                return grid[i][j]
        
        @cache
        def resr(i, j):
            nonlocal m, n
            if i - 1 > -1 and j - 1 > -1 and j + 1 < n and grid[i][j] == 1:
                l = resr(i-1, j-1)
                b = resr(i-1, j)
                r = resr(i-1, j+1)
                return 1 + min(l, b, r)
            else:
                return grid[i][j]
            
        for i in range(m):
            for j in range(n):
                if res(i, j) != 0:
                    ans += res(i, j) - 1
                if resr(i, j) != 0:
                    ans += resr(i, j) - 1
        return ans