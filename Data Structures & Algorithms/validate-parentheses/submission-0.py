class Solution:
    def isValid(self, s: str) -> bool:

        closeToOpen = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []
        for c in s:
            if c in closeToOpen:
                if stack:
                    o = stack.pop()
                    if closeToOpen[c] == o:
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0
        