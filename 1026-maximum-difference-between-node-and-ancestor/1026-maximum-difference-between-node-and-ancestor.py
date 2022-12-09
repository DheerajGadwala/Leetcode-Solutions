# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution(object):
    def maxAncestorDiff(self, root):
        self.mem = dict()
        self.minAndMax(root)
        mx = -math.inf
        for node in self.mem.keys():
            if mx < abs(node.val - self.mem[node][0]):
                mx = abs(node.val - self.mem[node][0])
            if mx < abs(node.val - self.mem[node][1]):
                mx = abs(node.val - self.mem[node][1])
        return mx
            
    def minAndMax(self, node):
        if node == None:
            return [math.inf, -math.inf]
        else:
            l = self.minAndMax(node.left)
            r = self.minAndMax(node.right)
            self.mem[node] = [min(l[0], r[0], node.val), max(l[1], r[1], node.val)]
            return self.mem[node]
        