# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = dict()
        
        def res(node = root, par = None):
            if node is not None:
                adj[node.val] = []
                if node.left is not None:
                    adj[node.val].append(node.left.val)
                    res(node.left, node)
                if node.right is not None:
                    adj[node.val].append(node.right.val)
                    res(node.right, node)
                if par is not None:
                    adj[node.val].append(par.val)
        
        res()
        
        q = [start]
        dist = {start : 0}
        ans = 0
        
        while len(q) != 0:
            u = q.pop(0)
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    ans = max(ans, dist[v])
                    q.append(v)
        return ans