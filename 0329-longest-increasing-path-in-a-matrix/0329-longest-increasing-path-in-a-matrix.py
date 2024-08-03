class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        isValid = lambda x, y: x > -1 and y > -1 and x < m and y < n
        
        dist = dict()
        ans = 0
        for i in range(m):
            for j in range(n):
                
                if (i, j) in dist:
                    continue
                    
                dist[(i, j)] = 1
                
                q = [(matrix[i][j], i, j)]
                
                while len(q) != 0:
                    u = heappop(q)
                    p = [u[1], u[2]]
                    ans = max(ans, dist[(p[0], p[1])])
                    
                    for d in dirs:
                        x, y = p[0] + d[0], p[1] + d[1]
                        if isValid(x, y) and matrix[x][y] > matrix[p[0]][p[1]]:
                            if (x, y) not in dist:
                                dist[(x, y)] = 1 + dist[(p[0], p[1])]
                                heappush(q, (matrix[x][y], x, y))
                            elif dist[(x, y)] < 1 + dist[(p[0], p[1])]:
                                dist[(x, y)] = 1 + dist[(p[0], p[1])]
                                heappush(q, (matrix[x][y], x, y))
                
        return ans
                    
                    
                    
                    
                
                