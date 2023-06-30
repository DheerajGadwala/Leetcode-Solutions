class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        isValid = lambda x: x[0] > -1 and x[1] > -1 and x[0] < m and x[1] < n
        start = None
        keyCount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                elif grid[i][j] in 'abcdef':
                    keyCount += 1
        q = deque([])
        q.append((start, ''))
        visited = {(start, ''), }
        dist = {(start, ''):0}
        while len(q) != 0:
            u, keys = q.popleft()
            for d in directions:
                v = (u[0]+d[0], u[1]+d[1])
                x, y = v
                if isValid(v) and (grid[x][y] in '.@abcdef' or grid[x][y] in keys):
                    queue_key = None
                    if grid[x][y] in '.@' or grid[x][y] in keys:
                        queue_key = (v, keys)
                    elif grid[x][y].upper() in keys:
                        queue_key = (v, keys)
                    else:
                        new_keys = ''.join(sorted(keys + grid[x][y].upper()))
                        queue_key = (v, new_keys)
                    if queue_key not in visited:
                        q.append(queue_key)
                        visited.add(queue_key)
                        dist[queue_key] = dist[(u, keys)] + 1
                        if len(queue_key[1]) == keyCount:
                            return dist[queue_key]
        return -1
                    
        
        
        