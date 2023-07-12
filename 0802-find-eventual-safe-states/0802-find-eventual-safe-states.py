class Solution:
    def eventualSafeNodes(self, adj: List[List[int]]) -> List[int]:
        n = len(adj)
        safe = set()
        visited = set()
        grey = set()
        
        def dfs(u):
            visited.add(u)
            grey.add(u)
            ret = True
            for v in adj[u]:
                if v not in visited:
                    ret &= dfs(v)
                elif v in grey or v not in safe:
                    ret = False
            grey.remove(u)
            if ret:
                safe.add(u)
            return ret
        
        ans = []
        for i in range(n):
            if dfs(i):
                ans.append(i)
        return ans