class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        comb = []
        def backtrack(ind, total):
            if total > target or ind >= len(nums):
                return

            if total == target:
                res.append(comb.copy())
                return
            
            comb.append(nums[ind])
            backtrack(ind, total + nums[ind])
            comb.pop()
            backtrack(ind + 1, total)

        backtrack(0, 0)
        return res

        