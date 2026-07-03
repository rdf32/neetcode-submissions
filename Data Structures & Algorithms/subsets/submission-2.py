class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        sub = []
        def dfs(index):
            if index >= len(nums):
                res.append(sub[:])
                return
            

            sub.append(nums[index])
            dfs(index + 1)
            sub.pop()
            dfs(index + 1)
        
        dfs(0)

        return res

        