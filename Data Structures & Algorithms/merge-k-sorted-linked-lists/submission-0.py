# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        dummy = ListNode()
        curr = dummy
        count = 0
        for l in lists:
            print(l.val)
            heapq.heappush(h, (l.val, count, l))
            count += 1
        while h:
            _, _, nxt = heapq.heappop(h)
            curr.next = nxt
            if nxt.next is not None:
                heapq.heappush(h, (nxt.next.val, count, nxt.next))
                count += 1
            curr = curr.next
        return dummy.next
            
        