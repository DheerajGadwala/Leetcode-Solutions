# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        
        def res(node):
            nonlocal count
            if node is None:
                return [0, 0]
            else:
                leftSum, leftCount = res(node.left)
                rightSum, rightCount = res(node.right)
                Sum = leftSum + rightSum + node.val
                Count = leftCount + rightCount + 1
                if Sum // Count == node.val:
                    count += 1
                return [Sum, Count]
        res(root)
        
        return count