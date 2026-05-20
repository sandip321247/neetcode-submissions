class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]
        for c in tokens:
            if c not in operations:
                stack.append(int(c))
            else:
                if c == "+":
                    stack.append(stack.pop() + stack.pop())
                elif c == "-":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                elif c == "*":
                    stack.append(stack.pop() * stack.pop())
                elif c == "/":
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(float(b) / a))
        return stack[0]