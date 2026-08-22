from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = deque()
        
        for c in s:
            if c in matches and stack and stack[-1] == matches[c]:
                stack.pop()
            elif c in matches:
                return False
            else:
                stack.append(c)
        
        return not stack


'''
    [(])
      ^

    i = 2
    [(
'''