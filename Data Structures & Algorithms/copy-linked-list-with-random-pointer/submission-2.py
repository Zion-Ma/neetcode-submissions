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
        records, copy = dict(), Node(x = 0)
        curr, curr_copy = head, copy
        while curr:
            curr_copy.next = Node(curr.val)
            records[curr] = curr_copy.next
            curr_copy = curr_copy.next
            curr = curr.next
        curr, curr_copy = head, copy.next
        while curr:
            if curr.random is not None:
                curr_copy.random = records[curr.random]
            curr_copy = curr_copy.next
            curr = curr.next
        return copy.next
