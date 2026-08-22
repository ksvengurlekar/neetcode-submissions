import heapq 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            stone1, stone2 = -heapq.heappop(heap), -heapq.heappop(heap)
            newWeight = abs(stone1 - stone2)

            if newWeight > 0:
                heapq.heappush(heap, -newWeight)

        if not heap: return 0

        return -heap[0]