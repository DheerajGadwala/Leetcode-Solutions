# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preOrder: List[int], inOrder: List[int]) -> Optional[TreeNode]:
        
        def res(inorder = inOrder, preorder = preOrder):
            if len(inorder) == 0:
                return None
            else:
                n = preorder[0]
                lIn = []
                rIn = []
                for i in range(len(inorder)):
                    if inorder[i] == n:
                        lIn = inorder[:i]
                        rIn = inorder[i+1:]
                        break
                lInSet = set(lIn)
                rInSet = set(rIn)
                lPre = []
                rPre = []
                for i in range(1, len(preorder)):
                    if preorder[i] in lInSet:
                        lPre.append(preorder[i])
                    elif preorder[i] in rInSet:
                        rPre.append(preorder[i])
                t = TreeNode(n, res(lIn, lPre), res(rIn, rPre))
                return t

        return res()        