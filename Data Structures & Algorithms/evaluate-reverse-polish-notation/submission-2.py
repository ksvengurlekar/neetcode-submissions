class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = deque()
        for c in tokens:
            if c in operators:
                num1, num2 = stack.pop(), stack.pop()
                if c == '+':
                    result = num2 + num1
                elif c == '-':
                    result = num2 - num1
                elif c == '*':
                    result = num2 * num1
                else:
                    result = int(float(num2) / num1)

                stack.append(result)
            else:
                stack.append(int(c))

        return stack[0]