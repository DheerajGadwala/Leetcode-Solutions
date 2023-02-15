class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        path = []
        visited = dict()
        adj = dict()
        for u, v in tickets:
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append(v)
            if u + v not in visited:
                visited[u + v] = 0
            visited[u+v] += 1
        for u in adj:
            adj[u].sort()
        
        ans = None
        
        def res(u = "JFK"):
            nonlocal ans
            path.append(u)
            # print(path, visCount, len(tickets) + 1)
            if ans != None:
                return
            if len(path) == len(tickets) + 1:
                ans = path[:]
                return
            
            for v in adj[u]:
                if visited[u+v] > 0:
                    visited[u + v] -= 1
                    res(v)
                    visited[u + v] += 1
            
            path.pop()
        
        res()
        return ans