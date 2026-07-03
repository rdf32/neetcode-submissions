class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        values = {}
        for ind, num in enumerate(nums):
            remainder = target - num
            if remainder in values:
                return [values[remainder], ind]
            values[num] = ind

