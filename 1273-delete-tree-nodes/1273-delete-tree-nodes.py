class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        adj = [[] for i in range(nodes)]
        for i in range(nodes):
            if parent[i] != -1:
                adj[parent[i]].append(i)
        
        exc = set()
        print(adj)
        def res(node = 0):
            val = value[node]
            for nei in adj[node]:
                val += res(nei)
            if val == 0:
                exc.add(node)
            return val
        res()
        
        def res2(node = 0):
            if node in exc:
                return 0
            else:
                ret = 1
                for nei in adj[node]:
                    ret += res2(nei)
                return ret
        
        return res2()
                