class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        isValid = lambda i, j: i > -1 and j > -1 and i < m and j < n
        mod = 10**9+7
        
        @cache
        def dfs(u):
            nonlocal ans
            ret = 1
            for d in dirs:
                v = (u[0] + d[0], u[1] + d[1])
                if isValid(v[0], v[1]) and grid[u[0]][u[1]] < grid[v[0]][v[1]]:
                    ret += dfs(v)
                    ret %= mod
            return ret
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += dfs((i, j))
                ans %= mod
        
        return ans