# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        def dfs(curr, max_val):
            if curr is None:
                return 
            if curr.val >= max_val:
                self.good += 1
                max_val = curr.val
            dfs(curr.left, max_val)
            dfs(curr.right, max_val)
        dfs(root, -101)
        return self.good
        