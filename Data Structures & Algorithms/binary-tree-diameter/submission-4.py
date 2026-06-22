# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiam = 0
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            right = dfs(node.right)
            left = dfs(node.left)
            self.maxDiam = max(self.maxDiam, left + right)
            return 1 + max(right, left)
        _ = dfs(root)
        return self.maxDiam