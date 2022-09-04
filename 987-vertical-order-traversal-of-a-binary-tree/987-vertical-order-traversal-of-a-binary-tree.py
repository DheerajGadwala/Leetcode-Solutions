# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        ret = dict()
        mn = math.inf
        def res(node = root, ver = 0, hei = 0):
            nonlocal mn
            if node is not None:
                if ver in ret and hei in ret[ver]:
                    l = ret[ver][hei]
                    l.append(node.val)
                    i = len(l)-1
                    while i != 0 and l[i] < l[i-1]:
                        l[i], l[i-1] = l[i-1], l[i]
                        i -= 1
                elif ver in ret:
                    ret[ver][hei] = [node.val]
                else:
                    ret[ver] = {hei:[node.val]}
                    mn = min(ver, mn)
                res(node.left, ver-1, hei+1)
                res(node.right, ver+1, hei+1)
        res()
        fin = []
        keys = sorted(list(ret.keys()))
        for i in keys:
            l = []
            innerkeys = sorted(list(ret[i].keys()))
            for j in innerkeys:
                l += ret[i][j]
            fin.append(l)
        return fin
            
            
        