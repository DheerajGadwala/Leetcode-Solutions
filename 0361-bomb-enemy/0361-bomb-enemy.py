class Solution(object):
    def maxKilledEnemies(self, grid):
        m, n = len(grid), len(grid[0])
        lr = [[0] * n for i in range(m)]
        for i in range(m):
            rs = 0
            for j in range(n):
                if grid[i][j] == "E":
                    rs += 1
                elif grid[i][j] == "W":
                    rs = 0
                lr[i][j] = rs
        rl = [[0] * n for i in range(m)]
        for i in range(m-1, -1, -1):
            rs = 0
            for j in range(n-1, -1, -1):
                if grid[i][j] == "E":
                    rs += 1
                elif grid[i][j] == "W":
                    rs = 0
                rl[i][j] = rs
        ud = [[0] * n for i in range(m)]
        for i in range(n):
            rs = 0
            for j in range(m):
                if grid[j][i] == "E":
                    rs += 1
                elif grid[j][i] == "W":
                    rs = 0
                ud[j][i] = rs
        du = [[0] * n for i in range(m)]
        for i in range(n-1, -1, -1):
            rs = 0
            for j in range(m-1, -1, -1):
                if grid[j][i] == "E":
                    rs += 1
                elif grid[j][i] == "W":
                    rs = 0
                du[j][i] = rs
        mx = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    mx = max(mx, lr[i][j] + rl[i][j] + ud[i][j] + du[i][j])
        
        return mx
        