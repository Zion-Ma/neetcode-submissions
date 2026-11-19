class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-num, char) for num, char in zip([a, b, c], "abc") if num != 0]
        heapq.heapify(heap)

        res = []
        prev = None
        while heap:
            left, char = heapq.heappop(heap)
            left += 1
            res.append(char)
            if left < 0:
                heapq.heappush(heap, (left, char))
            if prev:
                heapq.heappush(heap, prev)
                prev = None
            if heap and (len(res) > 1 and res[-2] == res[-1] == heap[0][1]):
                prev = heapq.heappop(heap)
            # print(heap, prev)
        return ''.join(res)