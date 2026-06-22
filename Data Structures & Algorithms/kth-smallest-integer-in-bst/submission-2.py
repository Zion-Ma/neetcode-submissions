# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 0
        self.traversed = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(root):
            if root is None:
                return
            inOrder(root.left)
            self.traversed += 1
            if self.traversed == k:
                self.ans = root.val
                return
            inOrder(root.right)
        inOrder(root) 
        return self.ans
            
                
        