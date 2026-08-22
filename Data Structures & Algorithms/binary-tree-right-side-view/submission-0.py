# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        rights = []    
        q = deque([(root, 1)])

        while q:
            current, depth = q.popleft()
            
            if current.left:
                q.append((current.left, depth+1))
            if current.right:
                q.append((current.right, depth+1))

            if not q or depth < q[0][1]:
                rights.append(current.val)

        return rights