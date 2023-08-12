class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.mem = dict()
        self.obstacleGrid = obstacleGrid
        self.m = len(obstacleGrid)
        self.n = len(obstacleGrid[0])
        return self.findCount(0, 0)
    
    def findCount(self, x, y):
        if((x, y) in self.mem):
            return self.mem[(x, y)]
        elif(x>=self.n or y>=self.m or self.obstacleGrid[y][x]==1):
            self.mem[(x, y)] = 0
            return 0
        elif(x == self.n-1 and y == self.m-1):
            self.mem[(x, y)] = 1
            return 1
        else:
            self.mem[(x, y)] = self.findCount(x+1, y) + self.findCount(x, y+1)
            return self.mem[(x, y)]
            
        
        
        