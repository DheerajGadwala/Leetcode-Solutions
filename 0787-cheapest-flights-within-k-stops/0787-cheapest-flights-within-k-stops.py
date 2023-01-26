class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = [[] for i in range(n)]
        for u, v, p in flights:
            adj[u].append((v, p))
        
        q = [(0, src, k)]
        dist = {(src, k): 0}
        while len(q) != 0:
            c, u, d = heappop(q)
            if u == dst:
                return c
            if d >= 0:
                for v, p in adj[u]:
                    if (v, d - 1) not in dist:
                        heappush(q, (c + p, v, d - 1))
                        dist[(v, d - 1)] = c + p 
                    elif c + p < dist[(v, d - 1)]:
                        heappush(q, (c + p, v, d - 1))
                        dist[(v, d - 1)] = c + p
        return -1
                        