# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr and curr.next:
            curr = curr.next.next
            count += 2
        count += 1 if curr else 0
        oneBefore = count - n
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        for _ in range(oneBefore):
            curr = curr.next
        print(curr.val)
        temp = curr.next
        curr.next = curr.next.next if curr.next else None
        del temp
        return dummy.next