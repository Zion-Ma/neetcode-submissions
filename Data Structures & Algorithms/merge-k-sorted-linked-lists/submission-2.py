# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        pq = []
        idx = 0
        for lst in lists:
            heapq.heappush(pq, (lst.val, idx, lst))
            idx += 1
        while pq:
            val, i, node = heapq.heappop(pq)
            curr.next = node
            curr = curr.next
            if node.next:
                idx += 1
                heapq.heappush(pq, (node.next.val, idx, node.next))
        return dummy.next