# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = None
        self.traverse = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            self.traverse += 1
            if self.traverse == k:
                self.ans = root.val
                return
            inorder(root.right)
        inorder(root)
        return self.ans
        
