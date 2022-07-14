# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preOrder: List[int], inOrder: List[int]) -> Optional[TreeNode]:
        if len(preOrder) == 1:
            return TreeNode(preOrder[0], None, None)
        elif len(preOrder) == 0:
            return None
        else:
            root = preOrder[0]
            node = TreeNode(root, None, None)
            inOrderLeft = []
            inOrderLeftSet = set()
            inOrderRight = []
            inOrderRightSet = set()
            preOrderLeft = []
            preOrderRight = []
            rightEnd = None
            flag = False
            for i in range(len(inOrder)):
                if inOrder[i] == root:
                    rightEnd = inOrder[i-1]
                    flag = True
                elif flag:
                    inOrderRight.append(inOrder[i])
                    inOrderRightSet.add(inOrder[i])
                else:
                    inOrderLeft.append(inOrder[i])
                    inOrderLeftSet.add(inOrder[i])
            for i in range(1, len(preOrder)):
                if preOrder[i] in inOrderLeftSet:
                    preOrderLeft.append(preOrder[i])
                else:
                    preOrderRight.append(preOrder[i])
            node.left  = self.buildTree(preOrderLeft, inOrderLeft)
            node.right = self.buildTree(preOrderRight, inOrderRight)
            return node
                    
        