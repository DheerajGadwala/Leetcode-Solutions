class DisjointSet:
    def __init__(self):
        self.parent = dict()
    def makeSet(self, u):
        self.parent[u] = u
    def find(self, u):
        if u not in self.parent:
            self.parent[u] = u
            return u
        elif self.parent[u] == u:
            return u
        else:
            return self.find(self.parent[u])
    def union(self, u, v):
        uParent = self.find(u)
        vParent = self.find(v)
        if uParent != vParent:
            self.parent[vParent] = uParent
            return True
        else:
            return False
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        for i in grid:
            i.insert(0, '0')
            i.append('0')
        grid.insert(0, ['0']*len(grid[0]))
        grid.append(['0']*len(grid[0]))
        ds = DisjointSet()
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] == '1':
                    if grid[i-1][j] == '1' or grid[i][j-1] == '1':
                        if grid[i-1][j] == '1':
                            ds.union((i-1, j), (i, j))
                        if grid[i][j-1] == '1':
                            ds.union((i, j-1), (i, j))
                    else:
                        ds.makeSet((i, j))
        pSet = set()
        for i in ds.parent:
            pSet.add(ds.find(i))
        return len(pSet)
        
        
        