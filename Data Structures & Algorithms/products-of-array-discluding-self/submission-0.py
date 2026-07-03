class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pre = [0] * n
        pos = [0] * n


        pre[0] = pos[n - 1] = 1

        for i in range(1, n):
            pre[i] = nums[i - 1] * pre[i - 1]

        for i in range(n - 2, -1, -1):
            pos[i] = nums[i + 1] * pos[i + 1]
        
        for i in range(n):
            res[i] = pre[i] * pos[i]
        
        return res