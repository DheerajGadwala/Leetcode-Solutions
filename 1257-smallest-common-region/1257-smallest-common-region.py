class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        adj = dict()
        par = dict()
        for li in regions:
            adj[li[0]] = []
            if li[0] not in par:
                par[li[0]] = None
            for i in range(1, len(li)):
                adj[li[0]].append(li[i])
                par[li[i]] = li[0]
                if li[i] not in adj:
                    adj[li[i]] = []
        
        root = None
        for node in adj:
            if par[node] is None:
                root = node
                break
        
        depth = dict()
        def res(node = root, d = 0):
            depth[node] = d
            for nei in adj[node]:
                res(nei, d + 1)
        res()
        
        while region1 != region2:
            if depth[region1] > depth[region2]:
                region1 = par[region1]
            else:
                region2 = par[region2]
        return region1
        
        
            