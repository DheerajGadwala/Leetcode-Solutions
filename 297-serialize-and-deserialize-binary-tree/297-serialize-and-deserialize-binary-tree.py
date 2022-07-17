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
        ret = []
        def res(node = root):
            if node is None:
                ret.append("N")
            else:
                ret.append(str(node.val))
                res(node.left)
                res(node.right)
        
        res()
        return ','.join(ret)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        t = data.split(",")
        pos = 0
        def res():
            nonlocal pos
            if t[pos] == "N":
                pos+=1
                return None
            else:
                ret = TreeNode(int(t[pos]))
                pos+=1
                ret.left = res()
                ret.right = res()
                return ret
        return res()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))