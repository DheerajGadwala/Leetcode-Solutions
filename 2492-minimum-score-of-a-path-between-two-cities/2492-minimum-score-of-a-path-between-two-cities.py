class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = dict()
        for i in range(1, n + 1):
            adj[i] = dict()
        for u, v, d in roads:
            adj[u][v] = d
            adj[v][u] = d
        q = deque([1])
        minEdge = math.inf
        visited = {1, }
        while len(q) != 0:
            u = q.popleft()
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
                minEdge = min(minEdge, adj[u][v])
        return -1 if n not in visited else minEdge
        