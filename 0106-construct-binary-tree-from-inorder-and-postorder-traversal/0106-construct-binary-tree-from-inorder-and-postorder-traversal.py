# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inOrder: List[int], postOrder: List[int]) -> Optional[TreeNode]:
        if len(inOrder) == 0:
            return None
        else:
            inOrderLeft = []
            inOrderRight = []
            inOrderLeftSet = set()
            inOrderRightSet = set()
            postOrderLeft = []
            postOrderRight = []
            flag = False
            for i in inOrder:
                if i == postOrder[-1]:
                    flag = True
                elif flag:
                    inOrderRight.append(i)
                    inOrderRightSet.add(i)
                else:
                    inOrderLeft.append(i)
                    inOrderLeftSet.add(i)
            for i in postOrder:
                if i in inOrderLeftSet:
                    postOrderLeft.append(i)
                elif i in inOrderRightSet:
                    postOrderRight.append(i)
            node = TreeNode(postOrder[-1], None, None)
            node.left = self.buildTree(inOrderLeft, postOrderLeft)
            node.right = self.buildTree(inOrderRight, postOrderRight)
            return node