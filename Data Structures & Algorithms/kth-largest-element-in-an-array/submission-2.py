class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sort = [-n for n in nums]
        # print(sort)
        heapq.heapify(sort)
        # print(sort)
        ans = -sort[0]
        while k > 0:
            ans = -heapq.heappop(sort)
            k -= 1
        return ans    