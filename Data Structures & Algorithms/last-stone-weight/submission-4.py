import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            largest = -heapq.heappop(heap)
            secondLargest = -heapq.heappop(heap)
            if largest - secondLargest != 0:
                heapq.heappush(heap, -(largest - secondLargest))
        return -heap[0] if heap else 0 