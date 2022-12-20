class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        n = len(pid)
        adj = dict()
        root = None
        for i in range(n):
            p, pp = pid[i], ppid[i]
            if pp != 0 and pp not in adj:
                adj[pp] = []
            if p not in adj:
                adj[p] = []
            if pp == 0:
                root = p
            else:
                adj[pp].append(p)
        
        ret = []
        
        def res(node = root, parentKilled = False):
            flag = node == kill or parentKilled
            if flag:
                ret.append(node)
            for child in adj[node]:
                res(child, flag)
        res()
        return ret
            