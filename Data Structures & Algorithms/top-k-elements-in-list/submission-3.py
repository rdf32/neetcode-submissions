class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        heap = []
        for num, count in counts.items():
            heapq.heappush(heap, (-count, num))

        res = []
        while k > 0:
            count, num = heapq.heappop(heap)
            res.append(num)
            k -= 1
            
        return res


        