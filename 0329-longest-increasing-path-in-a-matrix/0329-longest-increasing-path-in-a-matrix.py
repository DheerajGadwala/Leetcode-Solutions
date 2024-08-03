class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        isValid = lambda x, y: x > -1 and y > -1 and x < m and y < n
        
        visited = set()
        
        @cache
        def getMaxPath(curr, prev=None):
            
            visited.add(curr)
            i = curr // n
            j = curr % n
            
            ret = 0
            
            for nei in neighbours:
                
                to_i = i + nei[0]
                to_j = j + nei[1]
                
                to = to_i * n + to_j
                
                if to != prev and isValid(to_i, to_j) and to not in visited and matrix[to_i][to_j] > matrix[i][j]:
                    
                    ret = max(ret, 1 + getMaxPath(to, curr))
            
            visited.remove(curr)
            
            return ret
        
        ans = 1
        
        for i in range(m):
            for j in range(n):
                ans = max(ans, getMaxPath(i*n+j) + 1)
        
        return ans
                    
            
            
            
            
            