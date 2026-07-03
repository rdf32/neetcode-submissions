class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)
        res = right
        while left <= right:

            mid = left + (right - left) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p) / mid)
            
            if total_time <= h:
                res = mid
                right = mid - 1

            else:
                left = mid + 1
        return res