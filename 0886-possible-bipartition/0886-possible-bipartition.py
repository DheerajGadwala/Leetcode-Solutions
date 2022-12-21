class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        group = dict()
        adj = {i+1:[] for i in range(n)}
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(u, g):
            group[u] = g
            for v in adj[u]:
                if v not in group:
                    dfs(v, not g)
                elif group[v] == g:
                    return False
            return True
                
        
        for i in range(1, n+1):
            if i not in group:
                if not dfs(i, True):
                    return False
        
        return True