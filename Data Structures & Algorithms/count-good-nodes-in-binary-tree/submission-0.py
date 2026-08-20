# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def good(node, high):
            if not node:
                return
            
            if node.val >= high:
                self.res += 1
                high = node.val
        
            good(node.left, high)
            good(node.right, high)

        good(root, float('-inf'))
        return self.res