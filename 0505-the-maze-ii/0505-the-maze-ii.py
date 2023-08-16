class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        adj = dict()
        m, n = len(maze), len(maze[0])
        
        for i in range(m):
            for j in range(n):
                if maze[i][j] == 1:
                    continue
                adj[(i, j)] = []
                k = 1
                while i + k < m and maze[i+k][j] == 0:
                    k += 1
                adj[(i, j)].append((i+k-1, j))
                k = 1
                while i - k > -1 and maze[i-k][j] == 0:
                    k += 1
                adj[(i, j)].append((i-k+1, j))
                k = 1
                while j + k < n and maze[i][j+k] == 0:
                    k += 1
                adj[(i, j)].append((i, j+k-1))
                k = 1
                while j - k > -1 and maze[i][j-k] == 0:
                    k += 1
                adj[(i, j)].append((i, j-k+1))
        
        for i in range(m):
            for j in range(n):
                maze[i][j] = math.inf
        
        q = [(0, start[0], start[1])]
        maze[start[0]][start[1]] = 0
        
        while len(q) != 0:
            d, i, j = heappop(q)
            if i == destination[0] and j == destination[1]:
                return d
            for u, v in adj[(i, j)]:
                if d + abs(j-v) + abs(i-u) < maze[u][v]:
                    maze[u][v] = d + abs(j-v) + abs(i-u)
                    heappush(q, (maze[u][v], u, v))
                
        return -1