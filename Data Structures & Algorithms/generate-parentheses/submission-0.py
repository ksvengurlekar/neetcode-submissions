from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = deque()
        result = []

        def backtrack(openparen, closedparen):
            if openparen == closedparen == n:
                result.append("".join(stack))
                return

            if openparen < n:
                stack.append("(")
                backtrack(openparen + 1, closedparen)
                stack.pop()
            if closedparen < openparen:
                stack.append(")")
                backtrack(openparen, closedparen + 1)
                stack.pop()

        backtrack(0, 0)
        return result