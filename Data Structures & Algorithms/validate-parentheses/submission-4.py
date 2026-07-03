class Solution:
    def isValid(self, s: str) -> bool:

        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "["            
        }
        
        stack = []
        for c in s:
            if c not in close_to_open:
                stack.append(c)
            else:
                if stack:
                    open_c = stack.pop()
                    if close_to_open[c] == open_c:
                        continue
                    else:
                        return False
                else:
                    return False
                    
        return len(stack) == 0