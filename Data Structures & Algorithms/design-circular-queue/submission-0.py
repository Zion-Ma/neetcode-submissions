class Node:
    def __init__(self, value: int = 0) -> None:
        self.value = value
        self.prev = None
        self.nxt = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.length = 0
        self.head, self.tail = Node(), Node()
        self.head.nxt, self.tail.prev = self.tail, self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = Node(value)
        prev = self.tail.prev
        prev.nxt = self.tail.prev = new_node
        new_node.prev, new_node.nxt = prev, self.tail
        self.length += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        target = self.head.nxt
        self.head.nxt = target.nxt
        target.nxt.prev = self.head
        del target
        self.length -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.nxt.value

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.prev.value

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()