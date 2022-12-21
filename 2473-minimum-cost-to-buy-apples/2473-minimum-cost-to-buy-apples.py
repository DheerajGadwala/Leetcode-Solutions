class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        adj = {i:[] for i in range(n)}
        
        for u, v, w in roads:
            adj[u-1].append((v-1, w*(k+1)))
            adj[v-1].append((u-1, w*(k+1)))
        
        def dijkstra(src):
            q = [(appleCost[src], src)]
            cost = {src:0}
            ans = math.inf
            while len(q) != 0:
                c, u = heappop(q)
                ans = min(ans, c)
                for v, w in adj[u]:
                    if ((v in cost and cost[v] > cost[u] + w) or v not in cost) and cost[u] + w < c:
                        heappush(q, (cost[u] + w + appleCost[v], v))
                        cost[v] = cost[u] + w
            return ans
        
        return [dijkstra(i) for i in range(n)]