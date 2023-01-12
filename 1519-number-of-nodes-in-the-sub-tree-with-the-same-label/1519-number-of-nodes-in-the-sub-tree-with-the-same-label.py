class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0] * n
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * n
        alp = 'abcdefghijklmnopqrstuvwxyz'
        pos = {alp[i]:i for i in range(26)}
        labels = [pos[i] for i in labels]
        def res(node = 0):
            visited[node] = True
            ret = [0] * 26
            ret[labels[node]] += 1
            for v in adj[node]:
                if not visited[v]:
                    temp = res(v)
                    for i in range(26):
                        ret[i] += temp[i]
            ans[node] = ret[labels[node]]
            return ret
        res()
        return ans