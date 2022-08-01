class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.mem = dict()
        self.m = m
        self.n = n
        return self.countPaths(0,0)
    def countPaths(self, x, y):
        if((x, y) in self.mem):
            return self.mem[(x, y)]
        elif(x==self.n-1 and y==self.m-1):
            self.mem[(x, y)] = 1
            return self.mem[(x, y)]
        elif(x>=self.n or y>=self.m):
            self.mem[(x, y)] = 0
            return self.mem[(x, y)]
        else:
            self.mem[(x, y)] = self.countPaths(x+1, y) + self.countPaths(x, y+1)
            return self.mem[(x, y)]
        