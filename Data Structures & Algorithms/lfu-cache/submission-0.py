class Node:
    def __init__(self, key: int = -1, value: int = -1) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.nxt = None
        self.freq = 0

class LFUCache:

    def __init__(self, capacity: int):
        self.records = defaultdict(Node)
        self.cap = capacity
        self.freq = dict() # [head, tail, count]
        self.minFreq = 1

    def get(self, key: int) -> int:
        if key not in self.records:
            return -1
        node = self.records[key]
        self.remove(node)
        node.freq += 1
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.records:
            node = self.records[key]
            node.value = value
            self.remove(node)
        else:
            if self.cap > 0 and len(self.records) == self.cap:
                targetList = self.freq[self.minFreq]
                targetNode = targetList["head"].nxt
                self.remove(targetNode)
                del self.records[targetNode.key]
            node = Node(key, value)
            self.records[key] = node
            self.minFreq = 1
        node.freq += 1  
        self.insert(node)

    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.nxt
        prev.nxt = nxt
        nxt.prev = prev
        self.freq[node.freq]["count"] -= 1
        if self.freq[node.freq]["count"] == 0:
            del self.freq[node.freq]

    def insert(self, node: Node) -> None:
        if node.freq not in self.freq:
            self.createBucket(node.freq)
        tail = self.freq[node.freq]["tail"]
        prev = tail.prev
        prev.nxt = node
        tail.prev = node
        node.prev = prev
        node.nxt = tail
        self.freq[node.freq]["count"] += 1
        if node.freq - 1 == self.minFreq and (node.freq - 1) not in self.freq:
            self.minFreq = node.freq
    
    def createBucket(self, freq: int) -> None:
        self.freq[freq] = dict()
        head, tail, count = Node(), Node(), 0
        head.nxt, tail.prev = tail, head
        self.freq[freq]["head"] = head
        self.freq[freq]["tail"] = tail
        self.freq[freq]["count"] = count



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)