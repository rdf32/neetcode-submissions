class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result = []
        subset = []
        nums.sort()
        def backtrack(ind):
            if ind >= len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[ind])
            backtrack(ind + 1)
            while ind + 1 < len(nums) and nums[ind] == nums[ind + 1]:
                ind += 1
            subset.pop()
            backtrack(ind + 1)

        backtrack(0)
        return result        