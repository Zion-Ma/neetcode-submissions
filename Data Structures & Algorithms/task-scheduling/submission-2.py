class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        freq = [-val for val in count.values()]
        heapq.heapify(freq)
        time = 0
        while freq:
            cycle_size = n + 1
            task_count = 0
            updated = []
            while cycle_size > 0 and freq:
                f = heapq.heappop(freq)
                if f < -1:
                    updated.append(f + 1)
                cycle_size -= 1
                task_count += 1
            for f in updated:
                heapq.heappush(freq, f)
            time += task_count if not freq else n + 1
        return time