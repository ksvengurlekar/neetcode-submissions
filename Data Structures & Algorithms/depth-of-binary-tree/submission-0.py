# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        m = 1
        stack = [(root, 1)]
        while stack:
            curr, count = stack.pop()
            
            if curr.left:
                stack.append((curr.left, count+1))
            if curr.right:
                stack.append((curr.right, count+1))

            m = max(m, count)

        return m