class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        res = []
        stack = []

        def backtrack(nOpen, nClose):

            if nOpen == nClose == n:
                res.append("".join(stack))
                return
            
            if nOpen < n:
                stack.append("(")
                backtrack(nOpen + 1, nClose)
                stack.pop()
            
            if nClose < nOpen:
                stack.append(")")
                backtrack(nOpen, nClose + 1)
                stack.pop()
            
        backtrack(0, 0)
        return res