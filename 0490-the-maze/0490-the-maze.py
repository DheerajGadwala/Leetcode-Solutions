class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
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
        
        q = deque([start])
        maze[start[0]][start[1]] = 1
        while len(q) != 0:
            i, j = q.popleft()
            if i == destination[0] and j == destination[1]:
                return True
            for u, v in adj[(i, j)]:
                if maze[u][v] == 0:
                    q.append((u, v))
                    maze[i][j] = 1
                
        return False