class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        charSet = set()

        for val in nums:
            if val in charSet:
                return True
            charSet.add(val)
        
        return False