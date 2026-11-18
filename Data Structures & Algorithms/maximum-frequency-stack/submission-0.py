class FreqStack:

    def __init__(self):
        self.freq_heap = [] # max heap for frequency
        self.freq_num = defaultdict(set) # freq:{nums}
        self.num_freq = defaultdict(int) # num:freq
        self.stack = [] # [nums]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.cleanup(val, 1)

    def pop(self) -> int:
        buffer = []
        while len(self.freq_num[-self.freq_heap[0]]) == 0:
            heapq.heappop(self.freq_heap)
        while -self.num_freq[self.stack[-1]] != self.freq_heap[0]:
            buffer.append(self.stack.pop())
        curr = self.stack.pop()
        self.cleanup(curr, -1)
        while buffer:
            self.stack.append(buffer.pop())
        return curr

    def cleanup(self, val: int, change: int) -> None:
        if self.num_freq[val] > 0:
            self.freq_num[self.num_freq[val]].remove(val)
        self.num_freq[val] += change
        if self.num_freq[val] > 0 and len(self.freq_num[self.num_freq[val]]) == 0:
            heapq.heappush(self.freq_heap, -self.num_freq[val])
        self.freq_num[self.num_freq[val]].add(val)
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()