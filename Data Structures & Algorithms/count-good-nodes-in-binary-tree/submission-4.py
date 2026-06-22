# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(curr, max_val) -> int:
            if curr is None:
                return 0
            res = 1 if curr.val >= max_val else 0
            max_val = max(max_val, curr.val)
            res += dfs(curr.left, max_val)
            res += dfs(curr.right, max_val)
            return res
        return dfs(root, -101)
                