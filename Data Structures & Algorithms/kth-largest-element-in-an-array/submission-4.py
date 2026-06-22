class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_heap = [-n for n in nums]
        heapq.heapify(nums_heap)
        while k > 1:
            heapq.heappop(nums_heap)
            k -= 1
        return -nums_heap[0]