class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        adj = [[] for i in range(n)]
        for i in range(n):
            if edges[i] != -1:
                adj[i].append(edges[i])

        def bfs(adj, src):
            dist = [math.inf] * len(adj)
            q = [src]
            dist[src] = 0
            while len(q) != 0:
                u = q.pop(0)
                for v in adj[u]:
                    if dist[v] == math.inf:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return dist
        
        dist1 = bfs(adj, node1)
        dist2 = bfs(adj, node2)
        mn = math.inf
        mnInd = -1
        for i in range(n):
            d = max(dist1[i], dist2[i])
            if d < mn:
                mn = d
                mnInd = i
        return mnInd
        
                    