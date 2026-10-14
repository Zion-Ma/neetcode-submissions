class ListNode:
    def __init__(self, key: int = 0):
        self.key = key
        self.nxt = None

class MyHashSet:

    def __init__(self):
        self.bucket = [ListNode() for _ in range(10 ** 4)]

    def add(self, key: int) -> None:
        index = key % (10 ** 4)
        curr = self.bucket[index]
        while curr.nxt:
            if curr.nxt.key == key:
                return
            curr = curr.nxt
        curr.nxt = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % (10 ** 4)
        curr = self.bucket[index]
        while curr.nxt:
            if curr.nxt.key == key:
                temp = curr.nxt
                curr.nxt = curr.nxt.nxt
                del temp
                return
            curr = curr.nxt

    def contains(self, key: int) -> bool:
        index = key % (10 ** 4)
        curr = self.bucket[index]
        while curr.nxt:
            if curr.nxt.key == key:
                return True
            curr = curr.nxt
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)