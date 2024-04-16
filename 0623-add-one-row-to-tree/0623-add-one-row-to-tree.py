class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int, side = 1) -> Optional[TreeNode]:
        if depth == 1:
            if side == 1:
                return TreeNode(val, root, None)
            else:
                return TreeNode(val, None, root)
        elif root is None:
            return None
        else:
            root.left = self.addOneRow(root.left, val, depth - 1, 1)
            root.right = self.addOneRow(root.right, val, depth - 1, 2)
            return root