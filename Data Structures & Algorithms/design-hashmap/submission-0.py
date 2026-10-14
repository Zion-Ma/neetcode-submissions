class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.nxt = None

class MyHashMap:

    def __init__(self):
        self.bucket_size = 10000
        self.bucket = [Node() for _ in range(self.bucket_size)]

    def put(self, key: int, value: int) -> None:
        index = key % self.bucket_size
        curr = self.bucket[index]
        while curr.nxt:
            if curr.nxt.key == key:
                curr.nxt.value = value
                return
            curr = curr.nxt
        curr.nxt = Node(key, value)

    def get(self, key: int) -> int:
        index = key % self.bucket_size
        curr = self.bucket[index]
        while curr.nxt:
            if curr.nxt.key == key:
                return curr.nxt.value
            curr = curr.nxt
        return -1

    def remove(self, key: int) -> None:
        index = key % self.bucket_size
        curr = self.bucket[index]
        while curr.nxt:
            if curr.nxt.key == key:
                temp = curr.nxt
                curr.nxt = curr.nxt.nxt
                del temp
                return
            curr = curr.nxt
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)