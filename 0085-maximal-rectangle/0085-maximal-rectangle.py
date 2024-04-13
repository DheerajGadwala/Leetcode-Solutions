class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] != 0 and j > 0:
                    matrix[i][j] += matrix[i][j-1]
        
        ans = 0
        for i in range(m):
            for k in range(n):
                l = matrix[i][k]
                for j in range(i, m):
                    l = min(l, matrix[j][k])
                    h = j - i + 1
                    ans = max(ans, l*h)
        
        return ans
        