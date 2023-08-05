class Solution:
    
    def generateTrees(self, n: int) -> int:
        self.mem = dict()
        return self.gt(1, n+1)
    
    def gt(self, f, t):
        if (f, t) in self.mem:
            return self.mem[(f, t)]
        elif f == t:
            return [None]
        else:
            cnt = 0
            ret = []
            for i in range(f, t):
                left = self.gt(f, i)
                right = self.gt(i + 1, t)
                for j in left:
                    for k in right:
                        ret.append(TreeNode(i, j, k))
            self.mem[(f, t)] = ret
            return ret