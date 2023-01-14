class DisjointSets:
    
    def __init__(self):
        self.parent = dict()
    
    def makeSet(self, u):
        self.parent[u] = u
    
    def find(self, u):
        if u not in self.parent:
            self.makeSet(u)
            return u
        elif self.parent[u] == u:
            return u
        else:
            self.parent[u] = self.find(self.parent[u])
            return self.parent[u]
    
    def union(self, u, v):
        if u not in self.parent:
            self.makeSet(u)
        if v not in self.parent:
            self.makeSet(v)
        up = self.find(u)
        vp = self.find(v)
        if up < vp:
            self.parent[vp] = up
        else:
            self.parent[up] = vp

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        ds = DisjointSets()
        n = len(s1)
        for i in range(n):
            ds.union(s1[i], s2[i])
        ret = [ds.find(i) for i in baseStr]
        return ''.join(ret)