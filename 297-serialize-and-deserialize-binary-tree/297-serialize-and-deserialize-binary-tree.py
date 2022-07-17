# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def assignIDs(node):
            nonlocal i, ids
            if node is not None:
                assignIDs(node.left)
                ids[node] = i
                i += 1
                assignIDs(node.right)
        
        def inOrder(node):
            if node is not None:
                return inOrder(node.left) + [node.val, ids[node]] + inOrder(node.right)
            else:
                return []

        def preOrder(node):
            if node is not None:
                return [node.val, ids[node]] + preOrder(node.left) + preOrder(node.right)
            else:
                return []
        
        i = 0
        ids = dict()
        assignIDs(root)
        
        inorder = inOrder(root)
        preorder = preOrder(root)
        return str(inorder)[1:-1] + "|" + str(preorder)[1:-1]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "|":
            return None
        inorder, preorder = data.split("|")
        inorder = inorder.split(", ")
        preorder = preorder.split(", ")
        inorder = [int(i) for i in inorder]
        preorder = [int(i) for i in preorder]
        val = dict()
        for i in range(0, len(inorder), 2):
            val[inorder[i+1]] = inorder[i]
        inorder = [inorder[i] for i in range(1, len(inorder), 2)]
        preorder = [preorder[i] for i in range(1, len(preorder), 2)]
        
        def res(inorder=inorder, preorder=preorder):
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
                for i in range(len(preorder)):
                    if preorder[i] in lInSet:
                        lPre.append(preorder[i])
                    elif preorder[i] in rInSet:
                        rPre.append(preorder[i])
                t = TreeNode(val[n], res(lIn, lPre), res(rIn, rPre))
                return t
        return res()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))