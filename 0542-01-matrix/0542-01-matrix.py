class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    mat[i][j] = math.inf

        for i in range(n):
            for j in range(m):
                if mat[i][j] != 0:
                    if i > 0:
                        mat[i][j] = mat[i-1][j] + 1
                    if j > 0:
                        mat[i][j] = min(mat[i][j], mat[i][j-1] + 1)
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if mat[i][j] != 0:
                    if i + 1 < n:
                        mat[i][j] = min(mat[i][j], mat[i+1][j] + 1)
                    if j + 1 < m:
                        mat[i][j] = min(mat[i][j], mat[i][j+1] + 1)
        return mat
        