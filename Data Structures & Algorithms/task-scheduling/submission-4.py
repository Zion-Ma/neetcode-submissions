class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        freq_heap = [-f for f in counter.values()]
        heapq.heapify(freq_heap)
        time = 0
        while freq_heap:
            cycle_size = n + 1
            task_done = 0
            remain = []
            while freq_heap and cycle_size > 0:
                curr_freq = heapq.heappop(freq_heap) + 1
                if curr_freq < 0:
                    remain.append(curr_freq)
                task_done += 1
                cycle_size -= 1
            for f in remain:
                heapq.heappush(freq_heap, f)
            time += task_done if not freq_heap else n + 1
        return time