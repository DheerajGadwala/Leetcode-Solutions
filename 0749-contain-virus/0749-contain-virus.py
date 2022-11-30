class Solution:
    def containVirus(self, g: List[List[int]]) -> int:
        neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
        m, n = len(g), len(g[0])
        walls = set()
        ans = 0
        while True:
            mx = 0
            mx_coor = None
            visited = set()
            for i in range(m):
                for j in range(n):
                    next_inf = set()
                    if g[i][j] == 1 and (i, j) not in visited:
                        q = [(i, j)]
                        visited.add((i, j))
                        while len(q) != 0:
                            u = q.pop(0)
                            for nei in neighbours:
                                x, y = (u[0] + nei[0], u[1] + nei[1])
                                if x > -1 and y > -1 and x < m and y < n and (x, y) not in visited:
                                    if g[x][y] == 1:
                                        q.append((x, y))
                                        visited.add((x, y))
                                    elif g[x][y] == 0:
                                        next_inf.add((x, y))
                    if mx < len(next_inf):
                        mx = len(next_inf)
                        mx_coor = (i, j)
            if mx_coor == None:
                break
            q = [mx_coor]
            visited = {mx_coor, }
            while len(q) != 0:
                u = q.pop(0)
                g[u[0]][u[1]] = -1
                for nei in neighbours:
                    x, y = (u[0] + nei[0], u[1] + nei[1])
                    if x > -1 and y > -1 and x < m and y < n and (x, y) not in visited:
                        if g[x][y] == 1:
                            q.append((x, y))
                            visited.add((x, y))
                        else:
                            walls.add((u, (x, y)))
                            walls.add(((x, y), u))
            visited = set()
            for i in range(m):
                for j in range(n):
                    next_inf = set()
                    if g[i][j] == 1 and (i, j) not in visited:
                        q = [(i, j)]
                        visited.add((i, j))
                        while len(q) != 0:
                            u = q.pop(0)
                            for nei in neighbours:
                                x, y = (u[0] + nei[0], u[1] + nei[1])
                                if x > -1 and y > -1 and x < m and y < n and (x, y) not in visited:
                                    if g[x][y] == 1:
                                        q.append((x, y))
                                        visited.add((x, y))
                                    elif g[x][y] == 0:
                                        g[x][y] = 1
                                        visited.add((x, y))

        return len(walls) // 2
            
            
                        