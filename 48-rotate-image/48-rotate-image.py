class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        l = n - 1
        for i in range(n):
            k = n - 1
            for j in range(n):
                if i == k and j == l:
                    break
                matrix[i][j], matrix[k][l] = matrix[k][l], matrix[i][j]
                k-= 1
            l -= 1
        k = n-1
        for i in range(n):
            if i >= k:
                break
            for j in range(n):
                matrix[i][j], matrix[k][j] = matrix[k][j], matrix[i][j]
            k-= 1