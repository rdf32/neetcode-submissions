class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = {
            "+",
            "-",
            "*",
            "/"
        }
        stack = []
        for char in tokens:
            if char in operators:
                if char == "+":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a + b)
                elif char == "-":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)
                elif char == "*":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a * b)
                else:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a / b))
            else:
                stack.append(int(char))
        
        return stack[-1]