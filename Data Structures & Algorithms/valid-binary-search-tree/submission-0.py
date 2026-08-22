# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(node, leftBound, rightBound):
            if not node:
                return True
            elif not (leftBound < node.val < rightBound):
                return False
            
            return check(node.left, leftBound, node.val) and check(node.right, node.val, rightBound)

        return check(root, float("-inf"), float("inf"))