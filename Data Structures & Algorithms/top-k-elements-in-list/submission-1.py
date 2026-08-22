from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = Counter(nums)
        
        heap = []
        for item, frequency in hm.items():
            heapq.heappush(heap, [-1 * frequency, item])

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])


        return res