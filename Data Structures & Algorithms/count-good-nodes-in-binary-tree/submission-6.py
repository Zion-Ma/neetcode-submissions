# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(maxNode: int, curr: TreeNode) -> None:
            if curr is None:
                return
            if maxNode <= curr.val:
                self.count += 1
            dfs(max(maxNode, curr.val), curr.right)
            dfs(max(maxNode, curr.val), curr.left)
        dfs(float("-inf"), root)
        return self.count
