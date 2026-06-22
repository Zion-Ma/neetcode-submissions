# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        one = head
        two = head
        time = 0
        while two and two.next:
            time += 1
            one = one.next
            two = two.next.next
            if one == two:
                print(time)
                return True
        return False
