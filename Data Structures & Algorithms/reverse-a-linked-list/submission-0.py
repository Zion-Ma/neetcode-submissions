# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        prev = None
        tail = None
        curr = head
        # the final node's next is not
        # when the current becomes None, that means we reach the end
        while curr != None:
            tail = prev
            prev = curr
            curr = curr.next
            prev.next = tail
        head = prev
        return prev
        