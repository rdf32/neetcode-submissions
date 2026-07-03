class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## trying to find minimum and we know it was sorted
        ## in ascending order at one point
        ## so we always move right pointer to the exact location
        ## of number a when we know its less than number b
        ## in other case we increment left + 1 because we need
        ## to keep moving left to the right to find the place
        ## where the sequence starts
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        
        return nums[left]
            