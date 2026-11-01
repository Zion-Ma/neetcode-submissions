class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        freq = Counter(s)
        maxHeap = [(-f, ch) for ch, f in freq.items()]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            prev = None
            if ans and ans[-1] == maxHeap[0][1]:
                prev = heapq.heappop(maxHeap)
            curr_f, ch = heapq.heappop(maxHeap)
            curr_f += 1
            ans.append(ch)
            if curr_f < 0:
                heapq.heappush(maxHeap, (curr_f, ch))
            if prev:
                heapq.heappush(maxHeap, prev)
        if maxHeap:
            if -maxHeap[0][0] > 1:
                return ""
            ans.append(maxHeap[0][1])
        return "".join(ans)
