class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        l, h = 0, m - 1
        col = 0
        while l <= h:
            m = (l + h) // 2
            if matrix[m][0] <= target:
                col = m
                l = m + 1
            else:
                h = m - 1
        
        l, h = 0, n - 1
        while l <= h:
            m = (l + h) // 2
            if matrix[col][m] < target:
                l = m + 1
            elif matrix[col][m] == target:
                return True
            else:
                h = m - 1
        
        return False