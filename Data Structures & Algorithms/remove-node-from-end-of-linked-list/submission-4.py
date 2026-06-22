# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first, second = head, ListNode(0, head)
        target = second
        for _ in range(n):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next if second.next else None
        return target.next
        