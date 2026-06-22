"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        records = dict()
        curr, target = head, Node(x = 0)
        dummy = target
        while curr:
            node = Node(curr.val)
            target.next = node
            records[curr] = target.next
            target = target.next
            curr = curr.next
        target = dummy.next
        while head:
            if head.random is not None:
                target.random = records[head.random]
            target = target.next
            head = head.next
        return dummy.next
        