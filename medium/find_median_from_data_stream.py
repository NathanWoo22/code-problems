class MedianFinder:

    def __init__(self):
        self.lowerQueue = []
        self.upperQueue = []
        self.lowerCount = 0
        self.upperCount = 0
        self.totalCount = 0

    def addNum(self, num: int) -> None:
        if self.totalCount == 0:
            self.upperQueue.append(num)
            self.upperCount += 1
            self.totalCount += 1
            return
        self.totalCount += 1
        
        if self.lowerCount < self.upperCount: 
            heapq.heappush(self.upperQueue, num)
            heapq.heappush_max(self.lowerQueue, heapq.heappop(self.upperQueue))
            self.lowerCount += 1
            return
        
        heapq.heappush_max(self.lowerQueue, num) 
        heapq.heappush(self.upperQueue, heapq.heappop_max(self.lowerQueue))
        self.upperCount += 1

    def findMedian(self) -> float:
        if self.totalCount % 2 == 0: 
            return (self.upperQueue[0] + self.lowerQueue[0]) / 2
        return self.upperQueue[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
