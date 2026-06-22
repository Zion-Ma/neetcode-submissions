# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(curr: TreeNode, Max: float) -> None:
            if curr is None:
                return
            if curr.val >= Max:
                self.ans += 1
            next_Max = max(curr.val, Max)
            dfs(curr.left, next_Max)
            dfs(curr.right, next_Max)
        dfs(root, float("-inf"))
        return self.ans