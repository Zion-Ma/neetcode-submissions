class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        freq = [-cnt for cnt in counter.values()]
        heapq.heapify(freq)
        time = 0
        queue = deque() # (-count, time)
        while freq or queue:
            time += 1
            if not freq:
                time = queue[0][1]
            else:
                count = heapq.heappop(freq) + 1
                if count < 0:
                    queue.append((count, time + n))
            if queue and queue[0][1] == time:
                heapq.heappush(freq, queue.popleft()[0])
        return time
