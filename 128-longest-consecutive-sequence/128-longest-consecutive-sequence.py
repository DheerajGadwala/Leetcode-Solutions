class DisjointSet:
    def __init__(self):
        self.parent = dict()
    def makeSet(self, u):
        self.parent[u] = u
    def find(self, u):
        if u not in self.parent:
            self.makeSet(u)
            return u
        elif u is not self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
            return self.parent[u]
        else:
            return u
    def union(self, u, v):
        up = self.find(u)
        vp = self.find(v)
        if up != vp:
            if up > vp:
                up, vp = vp, up
            self.parent[vp] = up
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ds = DisjointSet()
        for i in nums:
            ds.makeSet(i)
            if i+1 in ds.parent:
                ds.union(i, i+1)
            if i-1 in ds.parent:
                ds.union(i-1, i)
        for i in nums:
            ds.find(i)
        mx = 0
        ret = dict()
        for i in ds.parent:
            if ds.parent[i] in ret:
                ret[ds.parent[i]] += 1
            else:
                ret[ds.parent[i]] = 1
            mx = max(mx, ret[ds.parent[i]])
        return mx