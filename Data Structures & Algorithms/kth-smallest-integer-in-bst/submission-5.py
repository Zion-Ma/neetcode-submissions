# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traversed = 0
        self.ans = None
        def dfs(curr):
            if curr is None:
                return 
            dfs(curr.left)
            self.traversed += 1
            if self.traversed == k:
                self.ans = curr
                return
            dfs(curr.right)
        dfs(root)
        return self.ans.val
        