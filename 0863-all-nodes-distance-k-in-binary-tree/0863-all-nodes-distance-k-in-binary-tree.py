# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = dict()
        visited = dict()
        ret = []
        def inOrder(node, par = None):
            nonlocal parent
            if node is not None:
                parent[node] = par
                visited[node.val] = False
                inOrder(node.left, node)
                inOrder(node.right, node)
        inOrder(root)
        visited[target.val] = True
        def search(node, dis = 0):
            nonlocal parent, visited, k, ret
            if dis == k:
                ret.append(node.val)
            neighbours = [node.left, node.right, parent[node]]
            for v in neighbours:
                if v is not None and not visited[v.val]:
                    visited[v.val] = True
                    search(v, dis + 1)
        search(target)
        return ret