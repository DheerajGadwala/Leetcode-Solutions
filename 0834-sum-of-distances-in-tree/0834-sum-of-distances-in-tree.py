class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adj = {i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        
        mem = dict()
        def dfs(u = 0, visited = set()):
            visited.add(u)
            ret = 1
            cnt = 1
            for v in adj[u]:
                if v not in visited:
                    if (u, v) not in mem:
                        mem[(u, v)] = dfs(v, visited)
                    ret += mem[(u, v)][0]
                    cnt += mem[(u, v)][1]
            return (ret+cnt-1, cnt)
        
        ret = []
        for i in range(n):
            ret.append(dfs(i, set())[0] - n)

        return ret