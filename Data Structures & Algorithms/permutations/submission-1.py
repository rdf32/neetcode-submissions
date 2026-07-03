class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        def perm(j):

            if j == len(nums):
                res.append(nums[:])
            
            for i in range(j, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                perm(j + 1)
                nums[i], nums[j] = nums[j], nums[i]
        
        perm(0)
        return res
        