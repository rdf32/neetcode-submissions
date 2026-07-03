class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pre = [0] * n
        pos = [0] * n
        
        pre[0] = nums[0]
        pos[n - 1] = nums[n - 1]

        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i]
        
        for i in range(n - 2, -1, -1):
            pos[i] = pos[i + 1] * nums[i]

        for i in range(n):
            if i == 0:
                res[i] = 1 * pos[i + 1]
            elif i == (n - 1):
                res[i] = pre[i - 1] * 1
            else:
                res[i] = pre[i - 1] * pos[i + 1]
        return res