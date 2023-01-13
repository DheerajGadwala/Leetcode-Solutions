class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        n = len(s)
        adj = [[] for i in range(n)]
        for i in range(n):
            if parent[i] != -1:
                adj[parent[i]].append(i)
        
        ans = 0
        
        def res(u = 0):
            nonlocal ans
            mx, mx2 = 0, 0
            for v in adj[u]:
                temp = res(v)
                if s[v] != s[u]:
                    if temp > mx:
                        mx2 = mx
                        mx = temp
                    elif temp > mx2:
                        mx2 = temp
            
            ans = max(ans, 1 + mx + mx2)
            return 1 + mx
        
        res()
        
        return ans
        