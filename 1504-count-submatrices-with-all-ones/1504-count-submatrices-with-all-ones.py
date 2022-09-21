class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat)+1, len(mat[0])
        mat.insert(0, [0]*n)
        for i in range(1, m):
            for j in range(n):
                mat[i][j] += mat[i-1][j]
        cnt = 0
        for i in range(m):
            for j in range(i+1, m):
                curr = 0
                for k in range(n):
                    ones = mat[j][k] - mat[i][k]
                    if ones == j - i:
                        curr += 1
                        cnt += curr
                    else:
                        curr = 0
        return cnt