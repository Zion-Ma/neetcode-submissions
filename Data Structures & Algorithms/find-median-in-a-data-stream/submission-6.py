class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and num > -self.minHeap[0]:
            heapq.heappush(self.maxHeap, num)
        else:
            heapq.heappush(self.minHeap, -num)
        if len(self.maxHeap) > len(self.minHeap):
            maxTop = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -maxTop)
            return
        if len(self.minHeap) > len(self.maxHeap) + 1:
            minTop = -heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, minTop)
            return

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (-self.minHeap[0] + self.maxHeap[0]) / 2
        else:
            return float(-self.minHeap[0])
        
        