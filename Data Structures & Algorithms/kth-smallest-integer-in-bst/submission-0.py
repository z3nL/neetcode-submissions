# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.res = None
        self.k = k

        def uhh(node):
            if not node:
                return
            
            uhh(node.left)
            if self.k == 0:
                return

            self.res = node.val
            self.k -= 1

            if k > 0:
                uhh(node.right)

        uhh(root)
        
        return self.res