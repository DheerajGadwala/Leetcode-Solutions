class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        adj = {i+1:[] for i in range(n)}
        for u, v in relations:
            adj[v].append(u)
        
        mem = dict()
        grey = set()
        
        def dfs(u):
            if u in mem:
                return mem[u]
            else:
                grey.add(u)
                ret = 1
                for v in adj[u]:
                    if v in grey:
                        return math.inf
                    else:
                        ret = max(ret, 1 + dfs(v))
                mem[u] = ret
                grey.remove(u)
                return ret
        
        ans = -math.inf
        for i in range(1, n+1):
            ans = max(ans, dfs(i))
        return -1 if ans == math.inf else ans