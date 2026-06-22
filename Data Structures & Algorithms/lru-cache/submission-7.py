class Node:
    def __init__(self, key: int = -1, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = defaultdict(Node)
        self.head = Node(key = -1)
        self.tail = Node(key = -2)
        self.head.nxt, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        target = self.cache[key]
        new_node = Node(key = key, val = target.val)
        self.remove(target)
        self.insert(new_node)
        self.cache[key] = new_node
        return new_node.val

    def put(self, key: int, value: int) -> None:
        new_node = Node(key = key, val = value)
        if key in self.cache.keys():
            self.remove(self.cache[key])
        self.insert(new_node)
        self.cache[key] = new_node
        if len(self.cache) > self.cap:
            lru = self.head.nxt
            self.head.nxt = lru.nxt
            self.remove(lru)
            del self.cache[lru.key]
    
    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.nxt
        node.prev.nxt, node.nxt.prev = nxt, prev
        del node
    
    def insert(self, node: Node) -> None:
        prev = self.tail.prev
        prev.nxt = self.tail.prev = node
        node.prev, node.nxt = prev, self.tail

        

