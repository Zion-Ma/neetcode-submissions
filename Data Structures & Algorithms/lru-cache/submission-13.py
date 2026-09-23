class Node:
    def __init__(self, key: int = 0, value: int = 0) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.records = defaultdict(Node)
        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.nxt
        prev.nxt = nxt
        nxt.prev = prev
    
    def insert(self, node: Node) -> None:
        prev = self.tail.prev
        prev.nxt = node
        node.prev = prev
        node.nxt = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.records:
            return -1
        node = self.records.get(key)
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.records:
            node = self.records[key]
            node.value = value
            self.remove(node)
            self.insert(node)
            return
        node = Node(key, value)
        self.records[key] = node
        self.insert(node)
        if len(self.records) > self.cap:
            lru = self.head.nxt.key
            self.remove(self.records[lru])
            del self.records[lru]
        return
