class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        directions = [lambda x, y: (x-1, y), lambda x, y: (x+1, y), lambda x, y: (x, y-1), lambda x, y: (x, y+1)]
        isBorder = lambda x, y: x == 0 or x == len(maze) - 1 or y == 0 or y == len(maze[0]) - 1
        isNotBorder = lambda x, y: x > -1 and x < len(maze) and y > -1 and y < len(maze[0])
        
        q = [tuple(entrance)]
        visited = [[False for i in range(len(maze[j]))] for j in range(len(maze))]
        dist = [[math.inf for i in range(len(maze[j]))] for j in range(len(maze))]
        visited[entrance[0]][entrance[1]] = True
        dist[entrance[0]][entrance[1]] = 0
        
        while len(q) != 0:
            u = q.pop(0)
            if isBorder(u[0], u[1]) and u != tuple(entrance):
                return dist[u[0]][u[1]]
            for d in directions:
                v = d(u[0], u[1])
                if isNotBorder(v[0], v[1]) and maze[v[0]][v[1]] == '.' and not visited[v[0]][v[1]]:
                    q.append(v)
                    visited[v[0]][v[1]] = True
                    dist[v[0]][v[1]] = dist[u[0]][u[1]] + 1
        return -1
                    