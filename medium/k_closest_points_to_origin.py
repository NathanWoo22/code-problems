class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        pq = []
        for point in points:
            dist = self.calcPoint(point)
            combo = (dist, point)
            heapq.heappush_max(pq, combo)
            if len(pq) > k:
                heapq.heappop_max(pq)
        
        return [x[1] for x in pq]

    def calcPoint(self, point):
        return math.sqrt(point[0]**2 + point[1]**2)
