import heapq

class MedianFinder:
    def __init__(self):
        # maxHeap for lower half (store negatives)
        self.maxHeap = []
        # minHeap for upper half
        self.minHeap = []
        self.count = 0

    def addNum(self, num: int) -> None:
        self.count += 1
        # Decide where to push
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        # Rebalance to maintain size invariant: len(maxHeap) >= len(minHeap),
        # and difference at most 1
        if len(self.maxHeap) > len(self.minHeap) + 1:
            # move one from maxHeap to minHeap
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        elif len(self.minHeap) > len(self.maxHeap):
            # move one from minHeap to maxHeap
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)

    def findMedian(self) -> float:
        if self.count % 2 == 1:
            # odd: maxHeap has the extra
            return float(-self.maxHeap[0])
        else:
            # even: average of tops
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
