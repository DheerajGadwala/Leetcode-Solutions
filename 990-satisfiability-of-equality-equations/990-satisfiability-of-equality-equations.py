class DisjointSet:
    def __init__(self):
        self.parent = dict()
    def makeSet(self, u):
        self.parent[u] = u
    def find(self, u):
        if u not in self.parent:
            self.parent[u] = u
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
            self.parent[vp] = up

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dse = DisjointSet()
        neq = []
        for e in equations:
            a = e[0]
            b = e[-1]
            op = e[1:3]
            if a == b and op == "!=":
                return False
            elif op == "==":
                dse.union(a, b)
            else:
                neq.append([a, b])
        for i in dse.parent:
            dse.find(i)
        for i in neq:
            if i[0] in dse.parent and i[1] in dse.parent and dse.parent[i[0]] == dse.parent[i[1]]:
                return False
        return True
        
            