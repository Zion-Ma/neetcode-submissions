# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")
        def dfs(curr) -> int:
            if curr is None:
                return 0
            left = max(0, dfs(curr.left))
            right = max(0, dfs(curr.right))
            self.ans = max(self.ans, curr.val + left + right)
            return curr.val + max(left, right)
        val = dfs(root)
        return self.ans