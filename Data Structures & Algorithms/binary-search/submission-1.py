class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = ((right - left) // 2) + left
            value = nums[mid]

            if value == target:
                return mid
            
            elif value < target:
                left = mid + 1
            
            else:
                right = mid - 1
        
        return -1
        

        