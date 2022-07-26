class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        q = [(0, 0, k)]
        m = len(grid)
        n = len(grid[0])
        visited = {(0, 0, k):0}
        
        
        isValid = lambda u: u[0] > -1 and u[1] > -1 and u[0] < m and u[1] < n
        
        while len(q) != 0:
            x, y, t = q.pop(0)
            neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            if x == m - 1 and y == n - 1:
                return visited[(x, y, t)]
            for nei in neighbours:
                if isValid(nei):
                    a, b = nei
                    if grid[a][b] == 0 and (a, b, t) not in visited:
                        q.append((a, b, t))
                        visited[(a, b, t)] = visited[(x, y, t)] + 1
                    elif t > 0 and (a, b, t - 1) not in visited:
                        q.append((a, b, t - 1))
                        visited[(a, b, t - 1)] = visited[(x, y, t)] + 1
        
        return -1                