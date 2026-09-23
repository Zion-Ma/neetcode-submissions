class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycles = 0
        counter = Counter(tasks)
        freq = [-f for f in counter.values()]
        heapq.heapify(freq)
        while freq:
            task_count = 0
            remain = []
            while freq and task_count < n + 1:
                curr = -heapq.heappop(freq) - 1
                if curr > 0:
                    remain.append(-curr)
                task_count += 1
            for f in remain:
                heapq.heappush(freq, f)
            cycles += (n + 1) if freq else task_count
        return cycles
