class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in matrix:
            i.insert(0, math.inf)
            i.append(math.inf)
        for i in range(len(matrix)-2, -1, -1):
            for j in range(len(matrix[i])-2, 0, -1):
                matrix[i][j] += min(matrix[i+1][j-1:j+2])
        return min(matrix[0])