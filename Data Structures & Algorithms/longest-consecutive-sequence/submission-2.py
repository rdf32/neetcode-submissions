class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        store = set(nums)
        
        max_len = 0
        for num in nums:
            length = 1
            while (num + length) in store:
                length += 1
            max_len = max(length, max_len)
        
        return max_len
        