class MedianFinder:

    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        if (
            self.maxHeap and self.minHeap and \
            -self.maxHeap[0] > self.minHeap[0]
        ):
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return float(-self.maxHeap[0])
        elif len(self.maxHeap) < len(self.minHeap):
            return float(self.minHeap[0])
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        
        