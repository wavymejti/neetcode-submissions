import math, heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lenghts = [] 
        output = []
        for x,y in points:
            lenght = math.sqrt(x**2 + y**2)
            lenghts.append([lenght, x, y])
        heapq.heapify(lenghts)
        for _ in range(k):
            dist, x, y = heapq.heappop(lenghts)
            output.append([x,y])
        return output

