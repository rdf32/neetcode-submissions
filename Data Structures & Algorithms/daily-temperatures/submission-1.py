class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res   = [0] * len(temperatures)
        stack = []
        for ind, temp in enumerate(temperatures):
            if stack:
                while stack and stack[-1][1] < temp:
                    prev_ind, prev_temp = stack.pop()
                    dist = ind - prev_ind
                    res[prev_ind] = dist
            stack.append((ind, temp))
        
        return res

        