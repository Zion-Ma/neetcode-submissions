class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        pq = []
        for i in range(len(nums)):
            heapq.heappush(pq, (-nums[i], i))
            if i < k - 1:
                continue
            else:
                while pq[0][1] < i - k + 1:
                    heapq.heappop(pq)
                ans.append(-pq[0][0])
        return ans