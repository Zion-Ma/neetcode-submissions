# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans: TreeNode = None
        self.traversed: int = 0
        def inorder(curr: TreeNode) -> None:
            if curr is None:
                return
            inorder(curr.left)
            self.traversed += 1
            if self.traversed == k:
                self.ans = curr
                return
            inorder(curr.right)
        inorder(root)
        return self.ans.val
        