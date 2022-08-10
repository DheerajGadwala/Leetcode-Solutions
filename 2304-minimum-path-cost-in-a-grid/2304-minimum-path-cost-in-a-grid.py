class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        @cache
        def res(i, j):
            if i == m - 1:
                return grid[i][j]
            val = grid[i][j]
            ret = math.inf
            for k in range(n):
                ret = min(ret, moveCost[val][k] + res(i + 1, k))
            return ret + val
        
        return min([res(0, i) for i in range(n)])
                
                