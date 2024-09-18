class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        n = len(values)
        adj = dict()
        
        for i in range(n):
            u, v = equations[i]
            if u not in adj:
                adj[u] = dict()
            if v not in adj:
                adj[v] = dict()
            adj[u][v] = values[i]
            adj[v][u] = 1/values[i]
        
        ret = []
        
        for t in range(len(queries)):
            q = queries[t]
            if q[0] not in adj or q[1] not in adj:
                ret.append(-1)
                continue
            l = [(q[0], 1)]
            visited = set()
            while len(l) > 0:
                u, val = l.pop(0)
                if u == q[1]:
                    ret.append(val)
                    continue
                for v in adj[u]:
                    if v not in visited:
                        l.append((v, val*adj[u][v]))
                        visited.add(v)
            if len(ret) == t:
                ret.append(-1)
        
        return ret
                