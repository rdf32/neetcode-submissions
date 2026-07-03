class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        res = 1
        left, right = 1, max(piles)
        
        while left <= right:
            mid = left + (right - left) // 2

            time = 0
            for pile in piles:
                time += math.ceil(float(pile) / mid)
            
            if time <= h:
                res = mid
                right = mid - 1 ## want to find minimum value so move right side
            
            else:
                left = mid + 1
        
        return res
        