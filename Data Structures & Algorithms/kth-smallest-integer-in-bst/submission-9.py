# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = 0
        self.traverse = 0
        def dfs(curr):
            if curr is None:
                return
            dfs(curr.left)
            self.traverse += 1
            if self.traverse == k:
                self.ans = curr.val
                return
            dfs(curr.right)
        dfs(root)
        return self.ans