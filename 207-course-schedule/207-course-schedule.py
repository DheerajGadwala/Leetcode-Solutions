class Solution:
    def canFinish(self, n: int, prereqs: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(n)}
        for p in prereqs:
            adj[p[0]].append(p[1])
        
        completed = set()
        def dfs(u, visited):
            visited.add(u)
            ret = True
            for v in adj[u]:
                if v in visited and v not in completed:
                    return False
                elif v not in completed:
                    ret &= dfs(v, visited)
            completed.add(u)
            return ret
        
        ans = True
        for i in range(n):
            ans &= dfs(i, set())
        return ans