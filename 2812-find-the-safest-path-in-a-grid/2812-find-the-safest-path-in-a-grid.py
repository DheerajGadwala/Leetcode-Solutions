class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q=deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        isValid = lambda x, y: x > -1 and y > -1 and x < m and y < n
        
        while len(q) != 0:
            u = q.popleft()
            for d in dirs:
                v = [u[0] + d[0], u[1] + d[1]]
                x, y = v
                if isValid(x, y) and grid[x][y] == 0:
                    q.append(v)
                    grid[x][y] = grid[u[0]][u[1]] + 1
        
        q = [(-grid[0][0], 0, 0)]
        mx = {(0, 0): -grid[0][0]}
        while len(q) != 0:
            s, i, j = heappop(q)
            if i == m - 1 and j == n - 1:
                return -s-1
            for d in dirs:
                x, y = i + d[0], j + d[1]
                if isValid(x, y) and mx.get((x, y), 0) > max(-grid[x][y], s):
                    mx[(x, y)] = max(-grid[x][y], s)
                    heappush(q, (mx[(x, y)], x, y))
        
        return -1
        
                    
                    
        