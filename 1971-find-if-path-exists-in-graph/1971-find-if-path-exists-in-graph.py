class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adj = [[] for _ in range(n)]
        for i in edges:
            adj[i[0]].append(i[1]) 
            adj[i[1]].append(i[0])
        visited = [False] * n
        q = [start]
        visited[start] = True
        while len(q) != 0:
            u = q.pop(0)
            for v in adj[u]:
                if not visited[v]:
                    q.append(v)
                    visited[v] = True
        return visited[end]
            