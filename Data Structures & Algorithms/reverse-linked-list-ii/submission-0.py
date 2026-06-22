# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first_section = dummy
        for _ in range(left - 1):
            first_section = first_section.next
        groupHead = first_section.next
        prev, curr = None, groupHead
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        first_section.next.next = curr
        first_section.next = prev
        return dummy.next

        