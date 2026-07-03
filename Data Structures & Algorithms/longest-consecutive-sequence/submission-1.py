class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        store = {}
        for num in nums:
            store[num] = 1
        
        mlen = 0
        for num in nums:
            length = 1
            while (num + length) in store:
                length += 1
            mlen = max(length, mlen)
        
        return mlen