class Solution:
    def search(self, nums: List[int], target: int) -> int:


        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        
        pivot = left
        
        right_search = self.binary_search(nums[:pivot], target)
        if right_search != -1:
            return right_search
        left_search = self.binary_search(nums[pivot:], target)
        if left_search != -1:
            return left_search + pivot
        return -1

    def binary_search(self, sub: List[int], target: int) -> int:
        left, right = 0, len(sub) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if sub[mid] == target:
                return mid
            elif sub[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
        