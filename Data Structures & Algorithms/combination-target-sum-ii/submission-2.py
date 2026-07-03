class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        subset = []
        candidates.sort()  ## whenever removing duplicates make sure to sort
        def backtrack(ind, total):
            if total == target:
                result.append(subset.copy())
                return
            
            elif total > target or ind >= len(candidates):
                return
            
            subset.append(candidates[ind])
            backtrack(ind + 1, total + candidates[ind])
            while ind + 1 < len(candidates) and candidates[ind] == candidates[ind + 1]:
                ind += 1
            subset.pop()
            backtrack(ind + 1, total)
        
        backtrack(0, 0)
        return result
        