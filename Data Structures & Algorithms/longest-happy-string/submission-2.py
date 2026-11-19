class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-num, char) for num, char in zip([a, b, c], "abc") if num != 0]
        heapq.heapify(heap)
        res = []
        while heap:
            left, char = heapq.heappop(heap)
            if len(res) > 1 and (res[-2] == res[-1] == char):
                if not heap:
                    break
                left2, char2 = heapq.heappop(heap)
                left2 += 1
                res.append(char2)
                if left2 < 0:
                    heapq.heappush(heap, (left2, char2))
                heapq.heappush(heap, (left, char))
            else:
                left += 1
                res.append(char)
                if left < 0:
                    heapq.heappush(heap, (left, char))
        return ''.join(res)
