class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        n = len(original)
        alph = 'abcdefghijklmnopqrstuvwxyz'
        adj = {j:{i:math.inf for i in alph} for j in alph}
        dist = {j:{i:math.inf for i in alph} for j in alph}
        for i in range(n):
            adj[original[i]][changed[i]] = min(adj[original[i]][changed[i]], cost[i])
        
        for i in alph:
            dist[i][i] = 0
            q = []
            heappush(q, (0, i))
            while len(q) != 0:
                d, u = heappop(q)
                for v in adj[u]:
                    if d + adj[u][v] < dist[i][v]:
                        dist[i][v] = d + adj[u][v]
                        heappush(q, (dist[i][v], v))
        
        m = len(source)
        ans = 0
        for i in range(m):
            ans += dist[source[i]][target[i]]
        
        return -1 if ans == math.inf else ans