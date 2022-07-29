class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        @cache
        def countDown(i, j):
            nonlocal m, n
            if i + 1 < m and j - 1 > -1 and j + 1 < n and grid[i][j] == 1:
                left = countDown(i+1, j-1)
                bottom = countDown(i+1, j)
                right = countDown(i+1, j+1)
                return 1 + min(left, bottom, right)
            else:
                return grid[i][j]
        
        @cache
        def countUp(i, j):
            nonlocal m, n
            if i - 1 > -1 and j - 1 > -1 and j + 1 < n and grid[i][j] == 1:
                left = countUp(i-1, j-1)
                top = countUp(i-1, j)
                right = countUp(i-1, j+1)
                return 1 + min(left, top, right)
            else:
                return grid[i][j]
            
        ans = 0
            
        for i in range(m):
            for j in range(n):
                if countDown(i, j) != 0:
                    ans += countDown(i, j) - 1
                if countUp(i, j) != 0:
                    ans += countUp(i, j) - 1

        return ans