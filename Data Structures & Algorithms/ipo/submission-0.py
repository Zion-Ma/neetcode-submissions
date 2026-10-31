class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minCap, maxProf = [(c, p) for c, p in zip(capital, profits)], []
        heapq.heapify(minCap)
        for _ in range(k):
            while minCap and minCap[0][0] <= w:
                c, p = heapq.heappop(minCap)
                heapq.heappush(maxProf, -p)
            if not maxProf:
                break
            w += -heapq.heappop(maxProf)
        return w





        
