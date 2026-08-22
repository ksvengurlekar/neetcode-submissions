# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdiam = 0

        def maxHeight(node):
            nonlocal maxdiam
            if not node:
                return 0
            
            left = maxHeight(node.left)
            right = maxHeight(node.right)
            maxdiam = max(maxdiam, left+right)
            return 1 + max(left, right)
        
        maxHeight(root)
        return maxdiam