# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        
        stack = [root]
        while stack:
            curr = stack.pop()
            if p.val <= curr.val <= q.val:
                return curr

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        
        return root
        