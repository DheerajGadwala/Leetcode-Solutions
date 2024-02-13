class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0 and i != 0 and j != 0:
                    mat[i][j] = min(mat[i-1][j], mat[i][j-1], mat[i-1][j-1]) + 1
                ans += mat[i][j]
        return ans