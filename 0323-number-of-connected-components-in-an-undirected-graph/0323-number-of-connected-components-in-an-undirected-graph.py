class Solution(object):
    def countComponents(self, n, edges):
        adj = {i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * n
        ans = 0
        
        def dfs(u):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    dfs(v)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                ans += 1
        
        return ans
        