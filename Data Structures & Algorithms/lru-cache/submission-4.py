class Node:
    def __init__(self, key: int = 0, val: int = 0) -> None:
        self.key, self.val = key, val
        self.prv, self.nxt = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache: dict[int, Node] = dict()
        self.head, self.tail = Node(), Node()
        self.head.nxt, self.tail.prv = self.tail, self.head

    def remove(self, node: Node) -> None:
        prv, nxt = node.prv, node.nxt
        prv.nxt, nxt.prv = nxt, prv
        del node

    def insert(self, node: Node) -> None:
        prv, nxt = self.tail.prv, self.tail
        prv.nxt = nxt.prv = node
        node.prv, node.nxt = prv, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        new = Node(key, value)
        if key in self.cache:
            self.remove(self.cache[key])
        self.insert(new)
        self.cache[key] = new
        if len(self.cache) > self.cap:
            lru = self.head.nxt
            self.remove(lru)
            del self.cache[lru.key]
        
