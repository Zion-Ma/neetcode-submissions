class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        freq = [-val for val in count.values()]
        heapq.heapify(freq)
        time = 0
        while freq:
            task_num = n + 1
            updated = []
            task_count = 0
            while task_num > 0 and freq:
                f = -heapq.heappop(freq)
                if f > 1:
                    updated.append(-(f - 1))
                task_num -= 1
                task_count += 1
            for f in updated:
                heapq.heappush(freq, f)
            time += task_count if not freq else n + 1
        return time
        