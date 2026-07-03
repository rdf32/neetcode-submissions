class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def backtrack(ind):
            if ind >= len(nums):
                result.append(nums.copy())
            
            for j in range(ind, len(nums)):
                nums[ind], nums[j] = nums[j], nums[ind]
                backtrack(ind + 1)
                nums[ind], nums[j] = nums[j], nums[ind]

        backtrack(0)
        return result        