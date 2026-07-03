class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        stack  = []

        def backtrack(num_open, num_closed):
            if num_open == num_closed == n:
                result.append("".join(stack))
                return
            
            if num_open < n:
                stack.append("(")
                backtrack(num_open + 1, num_closed)
                stack.pop()
            
            if num_closed < num_open:
                stack.append(")")
                backtrack(num_open, num_closed + 1)
                stack.pop()
            
        backtrack(0, 0)
        return result
        