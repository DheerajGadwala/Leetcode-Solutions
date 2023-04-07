class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(i, j):
            if grid[i][j] == 1:
                grid[i][j] = 0
                for r, c in dirs:
                    u, v = i + r, j + c
                    if u > -1 and v > -1 and u < m and v < n:
                        dfs(u, v)
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for i in range(n):
            dfs(0, i)
            dfs(m - 1, i)
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += grid[i][j]
        return ans
        