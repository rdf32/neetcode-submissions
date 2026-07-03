class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        def backtrack(j):

            if j == len(nums):
                res.append(nums[:])
            
            for i in range(j, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(j + 1)
                nums[i], nums[j] = nums[j], nums[i]
        
        backtrack(0)
        return res
        