class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        mod = 10**9+7
        m, n = len(pizza), len(pizza[0])
        grid = [[0] * (n+1) for i in range(m+1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, - 1, -1):
                grid[i][j] = 1 if pizza[i][j] == 'A' else 0
                grid[i][j] += grid[i+1][j] + grid[i][j+1] - grid[i+1][j+1]
        
        @cache
        def res(i = 0, j = 0, k = k):
            nonlocal mod
            if k == 1:
                return 1 if grid[i][j] > 0 else 0
            elif i == m or j == n:
                return 0
            else:
                ret = 0
                for l in range(i+1, m):
                    top = grid[i][j] - grid[l][j]
                    if top > 0:
                        ret += res(l, j, k - 1)
                        ret %= mod
                for l in range(j+1, n):
                    left = grid[i][j] - grid[i][l]
                    if left > 0:
                        ret += res(i, l, k - 1)
                        ret %= mod
                return ret
        
        return res()
                