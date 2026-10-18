class Node:
    def __init__(self, key: int = -1, value: int = -1) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.nxt = None
        self.freq = 0

class Bucket:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.count = 0
        self.head.nxt = self.tail
        self.tail.prev = self.head
    
    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.nxt
        prev.nxt = nxt
        nxt.prev = prev
        self.count -= 1

    def insert(self, node: Node) -> None:
        prev = self.tail.prev
        prev.nxt = node
        self.tail.prev = node
        node.prev = prev
        node.nxt = self.tail
        self.count += 1
    

class LFUCache:

    def __init__(self, capacity: int):
        self.records = dict()
        self.cap = capacity
        self.freq = dict()
        self.minFreq = 1

    def get(self, key: int) -> int:
        if key not in self.records:
            return -1
        node = self.records[key]
        self.freq[node.freq].remove(node)
        if self.freq[node.freq].count == 0:
            del self.freq[node.freq]
        node.freq += 1
        if node.freq not in self.freq:
            self.freq[node.freq] = Bucket()
        self.freq[node.freq].insert(node)
        if node.freq - 1 == self.minFreq and (node.freq - 1) not in self.freq:
            self.minFreq = node.freq
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.records:
            node = self.records[key]
            node.value = value
            self.freq[node.freq].remove(node)
            if self.freq[node.freq].count == 0:
                del self.freq[node.freq]
        else:
            if len(self.records) == self.cap:
                targetList = self.freq[self.minFreq]
                targetNode = targetList.head.nxt
                targetList.remove(targetNode)
                del self.records[targetNode.key]
                if targetList.count == 0:
                    del self.freq[self.minFreq]
            node = Node(key, value)
            self.records[key] = node
            self.minFreq = 1
        node.freq += 1  
        if node.freq not in self.freq:
            self.freq[node.freq] = Bucket()
        self.freq[node.freq].insert(node)
        if node.freq - 1 == self.minFreq and (node.freq - 1) not in self.freq:
            self.minFreq = node.freq
    




# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)