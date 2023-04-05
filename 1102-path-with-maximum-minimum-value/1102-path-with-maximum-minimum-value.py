class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = {(0, 0)}
        q = [(-grid[0][0], 0, 0)]
        while len(q) != 0:
            val, i, j = heappop(q)
            for nei in neighbours:
                u, v = i + nei[0], j + nei[1]
                if u > -1 and v > -1 and u < m and v < n:
                    nxt = -min(-val, grid[u][v])
                    if (u, v) not in visited:
                        heappush(q, (nxt, u, v))
                        visited.add((u, v))
                    if u == m - 1 and v == n - 1:
                        return -nxt
        
        